# For agent@riskmandate.ai: draining the subscribe lane, brief

> How the subscribe form on the articles pages works and how the agent that manages the list reads it: a public vault id, lane token and key, the one secret (the vault key), the message format, a tested drain script, four things that cost time, what to do with an address, and the prompt to paste.

*Source: <https://sgit.ai/docs/briefs/subscribe-lane-agent-brief.html> · site v0.6.78 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../index.md) / [Briefs](index.md) / Draining the subscribe lane

**Surface:** a page on a `*.sgit.ai` site writing into a vault's append lane. [The other surfaces →](../surfaces.md)

# For agent@riskmandate.ai: draining the subscribe lane

The “subscribe” form on the [articles page](../../articles/index.md#subscribe) and at the foot of every article does not send a form to a server and does not use a mailing-list service. It encrypts the reader's address in their browser to **your** public key and drops it into a write-only lane on a vault. This page is everything you need to read that lane and manage the list. Everything on it is public. The one thing that is not on it is the vault key.

**Why this is public.** A lane's append token can only write: it cannot list, fetch or read anything, and the server answers a write with `{"ok": true}` and nothing else. The message is encrypted to a key only you hold. So the vault id, the endpoint, the lane token and the public key can all sit on a public page, the same reasoning as [telemetry from a published vault](vault-telemetry-append-lanes.md) and the [agent contact file](../agent-contact.md). The only secret is the **vault key**, from which both the write key and the enum key are derived. It is handed to you privately, never committed here.

## The public facts

| What | Value |
|---|---|
| Contact file (the form reads this) | [`/.well-known/sgit-subscribe.json`](../../.well-known/sgit-subscribe.json) |
| Vault id | `y9j3nc60` |
| Endpoint | `https://dev.send.sgraph.ai`, the only host with the append routes |
| Lane | `subscribe`, append token `0158853058a43736c30f54d48d10f54bfe45330eae30817c79fdb3d67123bb75` (public on purpose) |
| Encrypted to | your published key, `sha256:9314437063df3bb6` (RSA-OAEP 4096), the one in [riskmandate.ai's contact file](https://riskmandate.ai/.well-known/sgit-agents.json). The form recomputes the fingerprint from the PEM before it encrypts |
| Signed? | No. A person filling in a form holds no key. Treat every message as untrusted input from the open internet |
| The secret | The subscribe vault's key. Not here, not in the repository, not in any log |

## What arrives

One single-part `.eml` per request, UTF-8, encrypted with sgit's hybrid envelope (the output of `sgit pki encrypt`).

```
From: web form <site@sgit.ai>
To: agent <agent@riskmandate.ai>
Subject: Subscribe: sgit.ai articles
Date: Sun, 04 Oct 2026 14:51:37 GMT
Message-ID: <sgit-subscribe-1791125498...-4b1c9e07@sgit.ai>
X-EmailFS-Kind: notification
X-SGit-Form: subscribe
X-SGit-Reply-To: reader@example.com
X-SGit-Page: /articles/index.html
Content-Type: text/plain; charset=utf-8

Subscribe to new sgit.ai articles
Email: reader@example.com
Name: (optional)

Consent: yes, keep this address in the subscribe vault and send new articles by email
Sent from: https://sgit.ai/articles/index.html
```

**The address to reply to is `X-SGit-Reply-To`, not `From`.** The consent line is only present because the form refuses to send without the box ticked. A honeypot field filled in by a bot is dropped in the browser and never reaches the lane.

## Draining it

With the vault key and your key's passphrase in the environment, the script below lists the lane, fetches the pending files, keeps each ciphertext before it does anything else, decrypts with `sgit pki decrypt`, writes the `.eml` and a line in `log.jsonl`, and only then marks the files processed. A file that will not decrypt goes to `quarantine/` and is never retried silently. It was run end to end on 4 October 2026 against this lane, from a real browser submission, and a second run found nothing to do.

```
pip install sgit-ai
export SUBSCRIBE_VAULT_KEY=<the vault key>     # the one secret
export SG_SEND_PASSPHRASE=<your pki key's passphrase>
python3 drain_subscribe.py sha256:9314437063df3bb6 ./subscribe-inbox
```

**`drain_subscribe.py`**

```
#!/usr/bin/env python3
"""Drain the sgit.ai subscribe lane. Needs: pip install sgit-ai; the subscribe vault key in
SUBSCRIBE_VAULT_KEY; the passphrase of the recipient's pki key in SG_SEND_PASSPHRASE.
Usage: drain_subscribe.py <encryption-key-fingerprint> <out-dir>
Writes <out-dir>/accepted/<id>.eml (+ .enc, kept for re-verification) and appends one line per
file to <out-dir>/log.jsonl; marks files processed only after they are safely written."""
import base64, email, hashlib, hmac, json, os, subprocess, sys, urllib.request, urllib.error
from email import policy
from sgit_ai.crypto.Vault__Crypto import Vault__Crypto

EP, VAULT = 'https://dev.send.sgraph.ai', 'y9j3nc60'
fingerprint, out = sys.argv[1], sys.argv[2]
keys = Vault__Crypto().derive_keys_from_vault_key(os.environ['SUBSCRIBE_VAULT_KEY'])   # strips the sgit_private_vault_ prefix
enum_key = hmac.new(bytes.fromhex(keys['write_key']), b'agent-contact/enum-key/v1', hashlib.sha256).hexdigest()

def post(route, body):
    req = urllib.request.Request(f'{EP}/api/vault/append/{route}/{VAULT}', data=json.dumps(body).encode(), method='POST',
                                 headers={'Content-Type': 'application/json', 'x-sgraph-vault-enum-key': enum_key})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)

for d in ('accepted', 'quarantine'): os.makedirs(f'{out}/{d}', exist_ok=True)
listing = post('list', {'include_content': False})
by_lane = {}
for e in listing['entries']: by_lane.setdefault(e['inbox'], []).append(e['file_id'])
for lane, ids in by_lane.items():
    for i in range(0, len(ids), 100):                                   # 100 file ids per batch
        batch = ids[i:i+100]
        files = post('fetch', {'inbox': lane, 'file_ids': batch})['files']
        done = []
        for f in files:
            fid = f['file_id']                                           # server ids look like 0000000000000_<24hex>.enc
            base = fid[:-4] if fid.endswith('.enc') else fid
            enc_path, eml_path = f'{out}/accepted/{base}.enc', f'{out}/accepted/{base}.eml'
            raw = base64.b64decode(f['content'])                         # payload was base64 of the .enc text
            open(enc_path, 'wb').write(raw)                              # keep the ciphertext before anything else
            try:
                r = subprocess.run(['sgit', 'pki', 'decrypt', enc_path, '--fingerprint', fingerprint],
                                   capture_output=True, text=True, check=True)
                plain = enc_path[:-4]                                    # sgit writes the plaintext beside the .enc, minus the suffix
                if not os.path.exists(plain): raise RuntimeError('decrypt wrote no file: ' + r.stdout[-200:])
                os.replace(plain, eml_path)
                m = email.message_from_bytes(open(eml_path, 'rb').read(), policy=policy.default)
                rec = {'file_id': fid, 'result': 'ok', 'form': m['X-SGit-Form'], 'reply_to': m['X-SGit-Reply-To'],
                       'subject': m['Subject'], 'page': m['X-SGit-Page'], 'date': m['Date']}
            except Exception as ex:
                os.replace(enc_path, f'{out}/quarantine/{base}.enc')
                rec = {'file_id': fid, 'result': 'quarantined', 'error': str(ex)[:200]}
            open(f'{out}/log.jsonl', 'a').write(json.dumps(rec) + '\n')
            done.append(fid)
        if done: post('mark-processed', {'inbox': lane, 'file_ids': done})
print('drained', sum(len(v) for v in by_lane.values()), 'file(s)')

```

**The derivation, so you can use your own tooling.** Strip the `sgit_private_vault_` prefix and derive the keys with sgit's `Vault__Crypto().derive_keys_from_vault_key(vault_key)`. The **write key** comes out of that. The **enum key** is `hex(HMAC-SHA256(bytes.fromhex(write_key), b"agent-contact/enum-key/v1"))`, the convention in [the contact-file spec](../agent-contact.md), never stored. The lane registered `sha256(append token)` as its anchor and `sha256(enum key)` as `enum_key_hash`.

## Four things that cost time

- **The payload is encoded twice.** The lane stores the bytes of the `.enc` file, which is itself base64 text of a JSON envelope. `fetch` returns base64 of those bytes: decode once to get the `.enc` file, which is what `sgit pki decrypt` wants.
- **Server file ids already end in `.enc`** (`{epoch_ms}_{24hex}.enc`), and `sgit pki decrypt x.enc` writes the plaintext to `x`, with no suffix. The script renames it to `.eml`.
- **Marking a file processed is final.** A processed file can no longer be fetched, so keep the ciphertext first, as the script does.
- **`configure` returns 404 until the vault has been pushed once.** The vault was created with `sgit init`, given a README and pushed, and only then configured. The documented 404 (wrong key or wrong vault) looks identical, so check the vault exists on the server before you suspect the key.

## What to do with a message

1. **Validate** `X-SGit-Reply-To` as a single plausible address. Header injection through a form field is the obvious attack on a list, so refuse any value with a newline or a second address. (The page strips newlines before it builds the headers. Do not rely on that, the lane is open to anyone with the token.)
2. **Confirm before the first send.** The lane is unauthenticated, so anyone can type someone else's address. We recommend a one-line confirmation email from `agent@riskmandate.ai` that the person has to answer before they are added. That is a decision for you and the owner, not something the page enforces.
3. **De-duplicate** on the lower-cased address, and record the consent line, the date and the page it came from.
4. **Unsubscribe** is a reply to any message that says so. The form's wording promises exactly that, so the list must honour it.
5. **Never** put the addresses on a public page, in a commit, or in a message to anyone outside the list's operators. Personal data belongs in the private vault, not here.

## Knowing what is new

The site publishes its articles as data: [`/updates/updates.json`](../../updates/updates.json) carries an `articles` array (slug, title, date, version, tags, summary), and [`/articles/graphs.json`](../../articles/graphs.json) carries each article's teaser, topics and links. Compare against the last slug you sent. The page for an article is `https://sgit.ai/articles/<slug>.html` and its markdown twin is the same path ending `.md`.

## Abuse, and how to take it down

- **Junk in the lane.** Anyone can write, at most 5 MB each and 1,000 pending per token. Drain on a schedule and drop what does not decrypt or parse. If it fills, **rotate**: a new token, `configure` with the new anchor, a one-line change to the contact file. Old writes then 404.
- **Take-down.** Set `inbox.status` to `"closed"` in the contact file and the form stops sending and offers the plain email instead, or rotate the token.
- **What the vault host sees:** a lane, a size and a time. Not the address, not the text.
- **No receipt.** The lane answers only `ok`. A reader who gets no confirmation can email you, and the form says so.

## The prompt to paste

```
You are agent@riskmandate.ai and you manage the subscribe list for new sgit.ai articles.
Read https://sgit.ai/docs/briefs/subscribe-lane-agent-brief.html. The vault key is in
SUBSCRIBE_VAULT_KEY and your key passphrase in SG_SEND_PASSPHRASE; never print either.
1. Drain the subscribe lane with drain_subscribe.py, ciphertext kept, quarantine on failure.
2. For each new address: validate it, send the confirmation email, add it only when confirmed.
3. For each article in https://sgit.ai/updates/updates.json newer than the last one sent,
   email the confirmed list a short note with the title, the summary and the link.
4. Honour any unsubscribe reply on the same day.
5. Report counts only (drained, quarantined, added, removed, sent). Never list addresses.
```

Written 4 October 2026 with the form, the contact file and the lane, tested together. The reader-facing side is `assets/subscribe.js`, about 120 lines you can read in a sitting. [← All briefs](index.md)


---

*[Site index for agents](../../llms.txt) · [HTML version](https://sgit.ai/docs/briefs/subscribe-lane-agent-brief.html)*
