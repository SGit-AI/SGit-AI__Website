#!/usr/bin/env python3
"""check_credential.py — classify a submitted credential BEFORE it touches anything.

Run this the moment a key arrives, before it is pasted into a page, a catalogue
entry, a capture script or a commit:

    python3 admin/build/check_credential.py '<credential>'
    echo $?     # 0 = safe to publish · 1 = WRITE credential, never publish

Why this exists, honestly: on 17 August a vault key was submitted for publication
described as a read key. It was caught by shape — 24 lowercase alphanumerics before
the colon, not 64 hex — and only the derived read key was published. That catch
depended on someone looking. This makes it a check.

Two mechanisms, and they cover different eras:

  * PREFIX     new vaults emit sgit_vk1_ (write) and sgit_rk1_ (read). Unambiguous,
               and the reason the prefixes exist.
  * SHAPE      legacy credentials carry no prefix and will circulate for years. A
               read key is 64 hex characters; anything else before the colon is a
               passphrase, which means a WRITE credential.

The release tripwire in validate.js is the backstop — it fails the build if a
key-shaped string reaches a tracked file. This is the front stop: it refuses the
credential before any of that can happen.

This script never prints the credential it was given.
"""
import re, sys

RE_READ_KEY_BARE = re.compile(r'^[a-f0-9]{64}:[a-z0-9]{4,24}$')
RE_READ_KEY_ONLY = re.compile(r'^[a-f0-9]{64}$')
RE_VAULT_ID      = re.compile(r'^[a-z0-9]{4,24}$')
RE_SIMPLE_TOKEN  = re.compile(r'^[a-z]+-[a-z]+-\d{4}$')
RE_LEGACY_RO     = re.compile(r'^([a-z0-9]{4,24})\s+([a-f0-9]{64})$')   # "<vault_id> <64hex>"


class Credential_Check:

    def classify(self, raw):
        """Return (kind, publishable, note). Never echoes the credential."""
        s = (raw or '').strip()
        if not s:
            return 'empty', False, 'nothing supplied'

        if s.startswith('sgit_vk1_'):
            return ('vault key (prefixed)', False,
                    'the sgit_vk1_ prefix marks a WRITE credential. Derive the read key and '
                    'publish only that; keep this one in the gitignored local tier')
        if s.startswith('sgit_rk1_'):
            body = s[len('sgit_rk1_'):]
            if RE_READ_KEY_BARE.match(body) or RE_READ_KEY_ONLY.match(body):
                return 'read key (prefixed)', True, 'read-only by construction — safe to publish'
            return ('prefixed but malformed', False,
                    'carries the read prefix but does not match <64-hex>[:<vault_id>] — do not '
                    'publish until it is explained')

        if RE_READ_KEY_BARE.match(s) or RE_READ_KEY_ONLY.match(s):
            return 'read key (bare)', True, 'read-only by construction — safe to publish'
        if RE_LEGACY_RO.match(s):
            return 'read key (legacy space-separated)', True, 'read-only — safe to publish'

        if RE_SIMPLE_TOKEN.match(s):
            return ('vault key (legacy token)', False,
                    'a retired low-entropy credential form, and a WRITE credential — never publish')

        if ':' in s:
            head, _, tail = s.rpartition(':')
            if RE_VAULT_ID.match(tail) and head and not re.fullmatch(r'[a-f0-9]{64}', head):
                return ('vault key (legacy passphrase:vault_id)', False,
                        f'{len(head)} characters before the colon and not 64 hex, so it is a '
                        'passphrase — a WRITE credential. This is the form that has no prefix to '
                        'give it away; derive the read key and publish only that')

        return ('unrecognised', False,
                'does not match any known credential form — do not publish until identified')

    def report(self, raw):
        kind, publishable, note = self.classify(raw)
        print(f'  form      : {kind}')
        print(f'  publish?  : {"YES — read-only" if publishable else "NO"}')
        print(f'  why       : {note}')
        if not publishable and 'vault key' in kind:
            print()
            print('  next step : store it in .sg_vault/local/demo-keys/<name>-vault-key (gitignored,')
            print('              and the release tripwire then scans every tracked file for it), then:')
            print('                from sgit_ai.crypto.Vault__Crypto import Vault__Crypto')
            print('                c = Vault__Crypto(); pw, vid = c.parse_vault_key(vault_key)')
            print('                read_key = c.derive_keys(pw, vid)["read_key"]')
            print('              Publish the derived read key. It is one-way: it cannot be turned back.')
        return 0 if publishable else 1


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('usage: check_credential.py <credential>   (0 = safe to publish, 1 = do not)')
    sys.exit(Credential_Check().report(sys.argv[1]))
