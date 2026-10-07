#!/usr/bin/env python3
"""send_to_registry: hand SG/Send vault keys to the DC Vault Registry without displaying them.

The instructions are https://sgit.ai/docs/send-a-vault-key.html. Needs only `pip install cryptography`:
no sgit, no account, no access token. The registry's public key is in this file and its fingerprint
is checked before anything is sealed.

    python3 send_to_registry.py --vault-id <inbox vault id> --file handover.json
    (the append token is read from REGISTRY_APPEND_TOKEN, or prompted for; never pass it on the
     command line, where it lands in your shell history)

You were given two values privately: the inbox vault id and an append token. Together they are a
write credential, so keep them out of anything you publish. The token is write-only: it cannot
list, read or delete anything, not even what you just wrote.

handover.json is a vault-key-handover/v1 payload. Delete it the moment this script reports success:
it is the only place the keys exist in the clear on your side.
"""
import argparse, base64, getpass, hashlib, json, os, re, sys, urllib.error, urllib.request

try:
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import padding
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
except ImportError:
    sys.exit('this needs the cryptography package: pip install cryptography')

ENDPOINT = 'https://dev.send.sgraph.ai'
REGISTRY_FINGERPRINT = 'sha256:20b7bb9dbac7df90'
REGISTRY_PUBLIC_KEY = '''-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAt2j3zEqSeQnXjJWIhcyk
OslbIjYqvIKRy1seGB2J9QR6o/xaDI6nY7ZtDBOya/nEobSQmjP+qoeTDjfK3jRa
oNIG90qMsFuk+9MotSCfnU7USeJBtKWUoL9IT9xXwFsHRKym5VhPxPDP3ptsNbYZ
ngab1eOQcKzyC8LRGPamJrz4LeuLv9nbEBP6Njt4c3WF8xap3DidW2W2pzhpUl/i
zSOiANqOxlbgIEOWzt2l3G+HDkjwYrWd2Tw2bLPymhvoFfeyvi0zIX1i9LgwxZo2
r1qcJ6ZsiuoCRq9vF2pv7TRY3zJn0UTtMDiOOktvyjNNhdY7Ezh8WPzZRI26gJ8Y
l1zVevkKghJC2SUynJYle4mVuVaglXK61i/wJ0HV0qj4uG5/vvZ3PBCZPkTvb6t0
nL8lBHETyG2VUsIzH0akFrHsJBKGaMN8KnbF33GRFC1aHA9nbAM/UamSyfArOxxs
8USYkSGWSnBQyRigS6OFQ9STAdLtzACEarMK1k4tyKWped/XoSAbZxDfLZCrfoMS
bLeUkaquaNT5oq9+mGx4bXlE7AV3c29cqICsAxeSidewmbSYwXwHAhow0AVKG5QS
vbJhaDZkYW8fEJBVmTeYIdPxSAk9C/+kwFgmaeJMfop6RJWPJhoLhxhlgfNLcTUr
4i9ETwJnopdaZaWRZErzNBsCAwEAAQ==
-----END PUBLIC KEY-----
'''
KEY_SHAPE = re.compile(r'^(sgit_private_vault_)?[A-Za-z0-9]{8,64}:[a-z0-9]{8}$')


def registry_key():
    """The pinned public key, refused if it does not hash to the pinned fingerprint."""
    try:
        pub = serialization.load_pem_public_key(REGISTRY_PUBLIC_KEY.encode())
        der = pub.public_bytes(serialization.Encoding.DER, serialization.PublicFormat.SubjectPublicKeyInfo)
        fp = 'sha256:' + hashlib.sha256(der).hexdigest()[:16]
    except ValueError:
        fp = 'an unreadable key'
    if fp != REGISTRY_FINGERPRINT:
        sys.exit(f'the registry key in this file hashes to {fp}, not {REGISTRY_FINGERPRINT}: do not send; '
                 'download the script again from https://sgit.ai/assets/send_to_registry.py')
    return pub


def seal(pub, plaintext):
    """sgit's hybrid envelope, v2: AES-256-GCM under an RSA-OAEP-SHA256 wrapped key. Returns the .enc text."""
    aes_key, iv = os.urandom(32), os.urandom(12)
    ct = AESGCM(aes_key).encrypt(iv, plaintext.encode(), None)
    wrapped = pub.encrypt(aes_key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                algorithm=hashes.SHA256(), label=None))
    env = dict(v=2, w=base64.b64encode(wrapped).decode(), i=base64.b64encode(iv).decode(),
               c=base64.b64encode(ct).decode())
    return base64.b64encode(json.dumps(env).encode()).decode()


def main():
    p = argparse.ArgumentParser(description='Hand vault keys to the DC Vault Registry.')
    p.add_argument('--vault-id', required=True, help='the inbox vault id you were given')
    p.add_argument('--file', required=True, help='your vault-key-handover/v1 JSON')
    a = p.parse_args()
    if not re.fullmatch(r'[a-z0-9]{8}', a.vault_id):
        sys.exit('the inbox vault id is eight lower-case letters and digits; check what you were given')
    token = os.environ.get('REGISTRY_APPEND_TOKEN') or getpass.getpass('append token: ')
    if not re.fullmatch(r'[0-9a-f]{16,128}', token.strip()):
        sys.exit('the append token is hex; check what you were given')

    body = json.load(open(a.file))
    if body.get('schema') != 'vault-key-handover/v1':
        sys.exit('the payload needs "schema": "vault-key-handover/v1"')
    if not body.get('handover_id'):
        sys.exit('the payload needs a unique "handover_id" (a repeat is dropped as a replay)')
    items = body.get('vaults') if 'vaults' in body else [body]
    for n, it in enumerate(items):                         # say which entry is wrong, never what the key is
        if not KEY_SHAPE.fullmatch((it.get('vault_key') or '').strip()):
            sys.exit(f'vaults[{n}].vault_key is not a vault key (expected sgit_private_vault_<passphrase>:<vault id>)')

    payload = base64.b64encode(seal(registry_key(), json.dumps(body)).encode()).decode()   # lane payload = b64(.enc text)
    req = urllib.request.Request(f'{ENDPOINT}/api/vault/append/write/{a.vault_id}', method='POST',
                                 data=json.dumps({'append_token': token.strip(), 'payload': payload}).encode(),
                                 headers={'Content-Type': 'application/json'})
    ids = [it['vault_key'].strip().rsplit(':', 1)[1] for it in items]
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            print(f'HTTP {r.status} {r.read().decode()[:40]}  vault ids: {", ".join(ids) or "(none)"}')
    except urllib.error.HTTPError as e:
        why = {404: 'the token is unknown, revoked or rotated, or the vault id is wrong (the two look the same by design): '
                    'check the id, then stop and ask for a current token and id',
               400: 'the request was malformed (a token that is not hex, or a missing field)',
               413: 'the payload is over 5 MB; send fewer keys per handover',
               507: 'the lane is full (1000 pending files); tell the registry owner'}.get(e.code, 'stop and report this code')
        sys.exit(f'HTTP {e.code}: {why}. Nothing else to try.')
    except urllib.error.URLError as e:
        sys.exit(f'could not reach {ENDPOINT}: {e.reason}. Report it and stop.')
    print('Now delete your handover file.')


if __name__ == '__main__':
    main()
