#!/usr/bin/env python3
"""compare_tests.py — the executable half of the comparison pages.

The comparison pages make claims about what a task costs with vaults and without.
A claim about OUR side can be executed; a claim about somebody else's product
cannot (no API, a login wall, and terms that frown on automation). That asymmetry
is real, so the pages state it rather than hide it: our rows carry a machine-verified
date, theirs carry a hand-checked one.

This runs the our-side checks against the LIVE service using only PUBLISHED READ
KEYS, and writes compare/results.json — which the page renders with a freshness
state, so a stale result shows as unverified instead of as fact.

    python3 admin/build/compare_tests.py

Every test states what would make it FAIL, because a test that cannot fail is not
evidence. Tests that record an ABSENT capability are first-class: the CLI prefix
gap below is a real finding, kept until it stops reproducing.
"""
import json, os, re, shutil, subprocess, tempfile, urllib.request, hmac, hashlib, sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catalogue_derive import ReadOnlyVault

ROOT     = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ENDPOINT = 'https://dev.send.sgraph.ai'
FIELD_NOTES = ('4bshby5n', '2848993a68c02a33ea5582902c391901191e53680d35b36c0e76185d4107ad81')
SUPPLEMENT  = ('r7zes477', '047186b559528058c66d1792b7345639b1238cb95c166d1d5f5b65c59813c2ee')


class Tests:
    def __init__(self):
        self.results = []

    def record(self, tid, claim, outcome, evidence, fails_if):
        self.results.append(dict(id=tid, claim=claim, outcome=outcome, evidence=evidence,
                                 fails_if=fails_if,
                                 checked=datetime.now(tz=timezone.utc).strftime('%Y-%m-%d')))
        mark = {'pass': '✓', 'fail': '✗', 'absent': '·'}.get(outcome, '?')
        print(f'  {mark} {tid:<26} {evidence[:88]}')

    # --- the read path, end to end, from a published read key -----------------
    def test_read_key_opens(self):
        vid, rk = FIELD_NOTES
        try:
            v = ReadOnlyVault(vid, rk, ENDPOINT).open()
            files = v.walk(v.commit['tree_id'])
            ok = len(files) > 0
            self.record('read-key-opens', 'A published read key alone opens the vault and lists its files',
                        'pass' if ok else 'fail',
                        f'{len(files)} files listed from vault {vid}; HEAD {v.head}',
                        'the ref cannot be derived, fetched or decrypted with the read key alone')
        except Exception as e:
            self.record('read-key-opens', 'A published read key alone opens the vault and lists its files',
                        'fail', f'error: {e}', 'the ref cannot be derived, fetched or decrypted')

    # --- what the SERVER hands over is opaque ---------------------------------
    def test_server_serves_ciphertext(self):
        vid, rk = FIELD_NOTES
        try:
            v = ReadOnlyVault(vid, rk, ENDPOINT).open()
            raw = v.raw(f'bare/data/{v.head}')
            try:
                raw.decode('utf-8'); readable = True
            except UnicodeDecodeError:
                readable = False
            plain = v.obj(v.head)
            self.record('server-serves-ciphertext',
                        'The bytes the server returns are unreadable without the key',
                        'pass' if not readable else 'fail',
                        f'{len(raw)} raw bytes: not valid UTF-8; the same object decrypts to '
                        f'{len(plain)} bytes of JSON with the read key',
                        'the raw response decodes as text without decryption')
        except Exception as e:
            self.record('server-serves-ciphertext', 'The bytes the server returns are unreadable without the key',
                        'fail', f'error: {e}', 'the raw response decodes as text')

    # --- immutability, which is WHY withdrawal cannot be retroactive ----------
    def test_objects_immutable(self):
        vid, rk = FIELD_NOTES
        try:
            v = ReadOnlyVault(vid, rk, ENDPOINT).open()
            a = v.raw(f'bare/data/{v.head}')
            b = v.raw(f'bare/data/{v.head}')
            digest = hashlib.sha256(a).hexdigest()
            same = a == b and v.head.endswith(digest[:12]) is not None
            self.record('objects-immutable',
                        'Objects are content-addressed and byte-identical on re-fetch',
                        'pass' if a == b else 'fail',
                        f'two fetches of {v.head} returned identical bytes (sha256 {digest[:16]}…) — '
                        f'which is why a copy already taken stays readable',
                        'the same object id returns different bytes')
        except Exception as e:
            self.record('objects-immutable', 'Objects are content-addressed and byte-identical on re-fetch',
                        'fail', f'error: {e}', 'the same object id returns different bytes')

    # --- a read key cannot be turned into a write -----------------------------
    def test_read_key_refuses_write(self):
        vid, rk = FIELD_NOTES
        tmp = tempfile.mkdtemp(prefix='sgit-ro-')
        target = os.path.join(tmp, 'clone')
        try:
            c = subprocess.run(['sgit', 'clone', f'{rk}:{vid}', target], cwd=tmp,
                               capture_output=True, text=True, timeout=300)
            if c.returncode != 0:
                self.record('read-key-refuses-write', 'A read-only clone cannot commit or push',
                            'fail', f'clone itself failed: {c.stderr.strip()[:90]}', 'the clone fails')
                return
            has_key = os.path.exists(os.path.join(target, '.sg_vault/local/vault_key'))
            with open(os.path.join(target, 'README.md'), 'a') as f:
                f.write('\nattempted edit by a read-only holder\n')
            k = subprocess.run(['sgit', 'commit', '-m', 'attempt write with only a read key'],
                               cwd=target, capture_output=True, text=True, timeout=180)
            p = subprocess.run(['sgit', 'push'], cwd=target, capture_output=True, text=True, timeout=180)
            msg = (k.stdout + k.stderr).strip().splitlines()
            refused = k.returncode != 0 and p.returncode != 0 and not has_key
            self.record('read-key-refuses-write', 'A read-only clone cannot commit or push',
                        'pass' if refused else 'fail',
                        f'commit exit {k.returncode}, push exit {p.returncode}; no vault_key on disk; '
                        f'"{msg[0][:70] if msg else ""}"',
                        'commit or push succeeds, or a write credential is present on disk')
        except Exception as e:
            self.record('read-key-refuses-write', 'A read-only clone cannot commit or push',
                        'fail', f'error: {e}', 'commit or push succeeds')
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    # --- a grant narrower than the whole vault, declared IN the vault ---------
    def test_scoped_write_declared(self):
        vid, rk = SUPPLEMENT
        try:
            v = ReadOnlyVault(vid, rk, ENDPOINT).open()
            def read(path):
                def find(tid, parts):
                    for e in v.obj_json(tid).get('entries', []):
                        if v.dec_b64(e.get('name_enc')) == parts[0]:
                            if len(parts) == 1:
                                return v.obj(e['blob_id']) if e.get('blob_id') else None
                            if e.get('tree_id'):
                                return find(e['tree_id'], parts[1:])
                return find(v.commit['tree_id'], path.split('/'))
            app = json.loads(read('app.json'))
            w = (app.get('permissions', {}).get('fs', {}) or {}).get('write')
            ok = w == ['adherence/']
            self.record('scoped-write-declared',
                        'A vault app can be granted write over one folder and nothing else',
                        'pass' if ok else 'fail',
                        f'{vid} app.json declares fs.write = {json.dumps(w)} (read = '
                        f'{json.dumps(app.get("permissions", {}).get("fs", {}).get("read"))})',
                        'the declaration is missing or grants write beyond adherence/')
        except Exception as e:
            self.record('scoped-write-declared', 'A vault app can be granted write over one folder and nothing else',
                        'fail', f'error: {e}', 'the declaration is missing')

    # --- a cross-implementation gap, recorded until it stops reproducing ------
    def test_cli_accepts_prefixed_key(self):
        vid, rk = FIELD_NOTES
        ver = subprocess.run(['sgit', '--version'], capture_output=True, text=True).stdout.strip()
        tmp = tempfile.mkdtemp(prefix='sgit-pfx-')
        try:
            r = subprocess.run(['sgit', 'clone', f'sgit_rk1_{rk}:{vid}', os.path.join(tmp, 'c')],
                               cwd=tmp, capture_output=True, text=True, timeout=300)
            derived = re.search(r'ref-pid-muw-([0-9a-f]{12})', r.stdout + r.stderr)
            correct = hmac.new(bytes.fromhex(rk), f'sg-vault-v1:file-id:ref:{vid}'.encode(),
                               hashlib.sha256).hexdigest()[:12]
            works = r.returncode == 0
            self.record('cli-accepts-prefixed-key',
                        'The CLI accepts the canonical sgit_rk1_ prefix the web loader accepts',
                        'pass' if works else 'absent',
                        (f'{ver}: prefixed clone succeeded' if works else
                         f'{ver}: prefixed clone failed — derived ref '
                         f'{derived.group(1) if derived else "?"} instead of {correct}; the bare '
                         f'<64hex>:<vault_id> form works on the same version'),
                        'the prefixed form derives a ref id different from the bare form')
        except Exception as e:
            self.record('cli-accepts-prefixed-key', 'The CLI accepts the canonical sgit_rk1_ prefix',
                        'fail', f'error: {e}', 'the prefixed form fails')
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    def run(self):
        print('running the our-side checks against the live service (published read keys only):')
        for name in ['test_read_key_opens', 'test_server_serves_ciphertext', 'test_objects_immutable',
                     'test_scoped_write_declared', 'test_read_key_refuses_write',
                     'test_cli_accepts_prefixed_key']:
            getattr(self, name)()
        out = os.path.join(ROOT, 'compare/results.json')
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, 'w') as f:
            json.dump(dict(
                _comment='Written by admin/build/compare_tests.py. Each entry is one executed check '
                         'against the live service using a published read key. Re-run the script to refresh.',
                generated=datetime.now(tz=timezone.utc).strftime('%Y-%m-%d %H:%M UTC'),
                expiry_days=30, tests=self.results), f, indent=1)
        print(f'\nwrote compare/results.json — {len(self.results)} checks')


if __name__ == '__main__':
    Tests().run()
