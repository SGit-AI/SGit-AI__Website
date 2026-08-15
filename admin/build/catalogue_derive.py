#!/usr/bin/env python3
"""Derive a catalogue entry from a read key.

The catalogue's design constraint (see the 14 Aug catalogue brief) is that a human
supplies only what a human knows — purpose, shape, evidence status, copy-or-reference,
write-key status — and EVERYTHING else is derived by opening the vault with the read
key it was submitted with. This is the deriver: read-only, no token, no clone.

    python3 catalogue_derive.py <vault_id> <read_key_hex> [endpoint]

Prints a markdown DERIVED block ready to paste into a catalogue entry.
"""
import sys, json, base64, urllib.request, hmac, hashlib
from datetime import datetime, timezone

from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def http_get(url):
    with urllib.request.urlopen(url) as r:
        return r.read()


class ReadOnlyVault:
    def __init__(self, vault_id, read_key_hex, endpoint):
        self.vault_id = vault_id
        self.key = bytes.fromhex(read_key_hex)
        self.endpoint = endpoint.rstrip('/')
        self.aes = AESGCM(self.key)

    def file_id(self, domain):
        return hmac.new(self.key, domain.encode(), hashlib.sha256).hexdigest()[:12]

    def raw(self, path):
        return http_get(f'{self.endpoint}/api/vault/read/{self.vault_id}/{path}')

    def decrypt(self, blob):
        return self.aes.decrypt(blob[:12], blob[12:], None)

    def obj(self, obj_id):
        return self.decrypt(self.raw(f'bare/data/{obj_id}'))

    def obj_json(self, obj_id):
        return json.loads(self.obj(obj_id))

    def dec_b64(self, b64):
        return self.decrypt(base64.b64decode(b64)).decode() if b64 else ''

    def open(self):
        ref_id = 'ref-pid-muw-' + self.file_id(f'sg-vault-v1:file-id:ref:{self.vault_id}')
        ref = json.loads(self.decrypt(self.raw(f'bare/refs/{ref_id}')))
        self.head = ref['commit_id']
        self.commit = self.obj_json(self.head)
        return self

    def walk(self, tree_id, prefix=''):
        out = {}
        tree = self.obj_json(tree_id)
        for e in tree.get('entries', []):
            name = self.dec_b64(e.get('name_enc'))
            full = f'{prefix}/{name}' if prefix else name
            if e.get('tree_id'):
                out.update(self.walk(e['tree_id'], full))
            else:
                size = self.dec_b64(e.get('size_enc')) or '0'
                out[full] = int(size) if size.isdigit() else 0
        return out

    def history_depth(self, limit=200):
        n, seen, frontier = 0, set(), [self.head]
        while frontier and n < limit:
            cid = frontier.pop()
            if cid in seen:
                continue
            seen.add(cid)
            n += 1
            try:
                frontier.extend(self.obj_json(cid).get('parents') or [])
            except Exception:
                break
        return n, (n >= limit)


def derive(vault_id, read_key, endpoint='https://dev.send.sgraph.ai'):
    v = ReadOnlyVault(vault_id, read_key, endpoint).open()
    files = v.walk(v.commit['tree_id'])
    commits, truncated = v.history_depth()
    total = sum(files.values())
    tops = sorted({p.split('/')[0] + ('/' if '/' in p else '') for p in files})
    exts = {}
    for p in files:
        ext = ('.' + p.rsplit('.', 1)[1].lower()) if '.' in p.split('/')[-1] else '(none)'
        exts[ext] = exts.get(ext, 0) + 1
    entries = []
    if 'app.json' in files:
        entries = [p for p in files if p.endswith('.html') and '/' not in p]
    updated = datetime.fromtimestamp(v.commit['timestamp_ms'] / 1000, tz=timezone.utc)

    lines = [
        '<!-- DERIVED by admin/build/catalogue_derive.py — do not hand-edit; re-run instead -->',
        '## Derived (from the read key alone)',
        '',
        f'- **Files:** {len(files)} · **plaintext size:** {total/1024:.0f} KB',
        f'- **Commits:** {commits}{"+" if truncated else ""} · **last updated:** {updated:%Y-%m-%d %H:%M} UTC',
        f'- **HEAD:** `{v.head}`',
        f'- **Top level:** {", ".join("`" + t + "`" for t in tops)}',
        f'- **File types:** ' + ', '.join(f'{k} ×{n}' for k, n in sorted(exts.items(), key=lambda x: -x[1])),
        f'- **Vault app:** {"yes — entries: " + ", ".join("`" + e + "`" for e in sorted(entries)) if entries else "no `app.json`"}',
        f'- **Browser-renderable:** {"yes (app present)" if entries else ("markdown only" if any(p.endswith(".md") for p in files) else "raw files")}',
        f'- **Derived:** {datetime.now(tz=timezone.utc):%Y-%m-%d} · endpoint `{endpoint.replace("https://", "")}` · read-only, no token',
    ]
    return '\n'.join(lines)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    print(derive(sys.argv[1], sys.argv[2], *(sys.argv[3:4] or ['https://dev.send.sgraph.ai'])))
