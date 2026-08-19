# Sending messages between vaults — sgit.ai

> How two vaults exchange encrypted messages without sharing a vault key and without the sender holding an account: append lanes addressed by a token, composed with PKI. Worked example in CLI, curl and sg.append, with the one step that is not yet wired marked PROPOSED.

*Source: <https://sgit.ai/docs/vault-messaging.html> · site v0.2.34 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Docs](index.md) / Vault messaging

# Sending messages between vaults

Two vaults can exchange encrypted messages without sharing a vault key, without the sender having an account, and without the server ever being able to read anything. The mechanism is an **append lane**: a write-only channel attached to a vault, addressed by the hash of a public key.

**Why this page exists.** Both halves of this capability were already documented — the transport as [`sg.append`](../vault/sg-bridge.md), the crypto as [`sgit pki`](pki.md) — on pages that never referenced each other. An agent asked how to send a message between vaults, found both halves, and could not find the sentence that says they combine. This is that sentence, written out.

## The shape of it

```
   SENDER                        SERVER                      RECIPIENT
   ──────                        ──────                      ─────────
   has: your public key          stores: ciphertext          has: private key
                                         + hashes of keys          + enum_key

   encrypt(msg, your_pubkey)
   append_token = H(pubkey)
        │
        │  POST /api/vault/append/write/{vault_id}
        │  { append_token, payload }
        ├────────────────────────▶  gate: H(append_token) ∈ append_anchors?
        ◀────────────────────────  { "ok": true }   ← blind: no id, no count
                                          │
                                          │   POST /append/list      (enum_key)
                                          ◀──────────────────────────┤
                                          │   POST /append/fetch     │
                                          ├─────────────────────────▶│ decrypt locally
                                          │   POST /append/mark-processed
                                          ◀──────────────────────────┤
```

**What the server can see:** that a lane received something, how big it was, and when. **What it cannot see:** the content, or the recipient’s private key, which never leaves their machine.

## Four capabilities, deliberately separated

This is the part worth understanding, because it is why a sender cannot read the lane they write to:

| Capability | Who holds it | Can | Cannot |
|---|---|---|---|
| `append_token` | the sender | write | list, fetch, read anything |
| `enum_key` | the vault owner | list, fetch, mark-processed | write, purge |
| `write_key` | the vault owner | configure, purge | — |
| private key | the vault owner | **decrypt** | *never sent to the server* |

The server stores `SHA-256` hashes of the first three and checks `H(presented) == stored`. It never holds a raw capability key, and never holds a private key at all. Compromising the server yields hashes and ciphertext.

Read in the [privilege vocabulary](../compare/index.md) the comparison pages use: the sender’s capability is **scoped** to one operation on one lane, **bearer**-held, and **observable** to the owner but not to the sender. A write-only credential that cannot read its own effects is an unusually clean shape.

## Setting up a lane — recipient, one-time

Have a keypair and publish the public half ([full lifecycle here](pki.md)):

```
$ sgit pki keygen --label "My Vault Identity"
$ sgit pki export sha256:a4615402a0bc23ac > my-identity.json
```

Then register, against your vault, the hash of the sender’s lane address and the hash of your enumeration key:

```
$ curl -X POST https://send.sgraph.ai/api/vault/append/configure/$VAULT_ID \
    -H "x-sgraph-vault-write-key: $WRITE_KEY" \
    -H "Content-Type: application/json" \
    -d '{"append_anchors":["<sha256 of the append_token>"],
         "enum_key_hash":"<sha256 of your enum_key>"}'
```

`configure` patches an existing vault manifest — it does not create a vault. A 403 means the vault ID or the write key is wrong.

## Deriving the lane address — read this before writing code

**This step is not yet wired end to end, and the gap is worth stating precisely.**
 The design is `append_token = H(recipient public key)`, so a sender can compute your lane address from the public bundle you gave them, with no extra coordination. That is an elegant property and it is the intended model.

 What ships today on **sgit v0.15.0**: `sgit pki export` emits a **JSON bundle** containing two PEM blocks, a label and two fingerprints — *not* a bare public key. No shipped command emits the append token, and hashing the bundle file is not a defined derivation (field order and whitespace would change the answer). The **server** side of append lanes is code-verified and shipped; the **client** derivation that turns a public key into a lane address is **PROPOSED**.

**What to do meanwhile:** treat `append_token` as an opaque 64-hex secret you agree out of band — generate one, hand it to your sender, register its SHA-256 as an `append_anchor`. Everything else on this page works today. When the derivation lands, the token stops needing to be exchanged; nothing else changes.

Two format rules that cause avoidable failures:

- The token pattern is `^[0-9a-f]{16,128}$` — **hex only**. A prefixed token like `tok_abc…` returns **400**, not 403, because it fails input validation before it reaches any gate.
- CLI fingerprints are printed as `sha256:a4615402a0bc23ac`. That `sha256:` prefix is part of the CLI identifier and is **not** part of a token. Pasting a fingerprint straight in is the most likely way to hit that 400.

## Sending

```
# 1. encrypt to the recipient's public key (RSA-OAEP 4096 + AES-256-GCM, client-side)
$ sgit pki encrypt message.txt --recipient sha256:a4615402a0bc23ac
Encrypted to message.txt.enc

# 2. append it to their lane
$ curl -X POST https://send.sgraph.ai/api/vault/append/write/$THEIR_VAULT_ID \
    -H "Content-Type: application/json" \
    -d '{"append_token":"'$APPEND_TOKEN'","payload":"'$(base64 -w0 message.txt.enc)'"}'
{"ok": true}
```

**No account is needed to send.** The write endpoint requires no access token — the `append_token` is the whole gate. That is deliberate: somebody can send to your vault without holding a credential on the platform at all.

The response is **blind by design**: exactly `{"ok": true}`, with no file ID, no count and no metadata. A sender cannot learn what else is in the lane, or even whether theirs was the first write.

## Receiving

Poll cheaply first — a metadata-only listing reads **zero** payloads:

```
$ curl -X POST https://send.sgraph.ai/api/vault/append/list/$VAULT_ID \
    -H "x-sgraph-vault-enum-key: $ENUM_KEY" \
    -H "Content-Type: application/json" \
    -d '{"include_content": false}'
```

Filenames are server-assigned as `{epoch_ms}_{24-hex}.enc`, so they sort chronologically — which is what makes cursor pagination stable. Page with `after_file_id` set to the last ID you saw.

```
$ curl -X POST .../append/fetch/$VAULT_ID -H "x-sgraph-vault-enum-key: $ENUM_KEY" \
    -d '{"file_ids":["1755302400000_a3f8….enc"]}'

$ sgit pki decrypt message.txt.enc --fingerprint sha256:a4615402a0bc23ac

$ curl -X POST .../append/mark-processed/$VAULT_ID -H "x-sgraph-vault-enum-key: $ENUM_KEY" \
    -d '{"file_ids":["1755302400000_a3f8….enc"]}'
```

`mark-processed` is idempotent — a file already moved comes back in `missing` rather than as an error, so a retried batch is safe.

## From inside a vault app

The same transport through the browser bridge, with no HTTP of your own (see [`sg.append`](../vault/sg-bridge.md)):

```
await sg.append.configure({ appendAnchors: [anchorHash], enumKeyHash });
await sg.append.write({ appendToken, payload });            // blind
const { entries } = await sg.append.list({ includeContent: false });
const { files }   = await sg.append.fetch({ fileIds });
await sg.append.markProcessed({ fileIds });
await sg.append.purge({ folder: 'processed' });
```

## Practical notes

- **Limits.** 5 MB per message (**413**) · 1000 pending files per token (**507**) · 100 file IDs per batch (**400**) · 3 MB inline-content ceiling when listing with content (**413**) · list page size 50 by default, 200 max, clamped silently.
- **Several senders.** Register several `append_anchors`. Each sender writes to their own lane, so a listing can be scoped to one of them.
- **Housekeeping.** `purge` with `folder:"processed"` and no file IDs clears a whole lane’s processed set in one call. It takes `"pending"` or `"processed"` — the older `"inbox"` value now returns 400.
- **The API was renamed.** `inbox` became `append` in v0.32.7; any `/api/vault/inbox/*` URL is gone.

## What this is not

Not a chat protocol, not a queue with delivery guarantees, and not anonymous — the server sees lane activity and timing even though it cannot read content. It is a **generic append-only transport**: the same primitive carries logs, signals, control messages and state flows between agents. The client decides what the bytes mean.

## See also

- [API — append lanes](../api/append-lanes.md): the six endpoints, gates, limits and status codes
- [PKI](pki.md): keypair lifecycle, verified against the shipped CLI
- [`sg.append`](../vault/sg-bridge.md): the same transport from a vault app
- [Security model](../security/index.md#pki): where the keypair sits relative to the symmetric vault key


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/docs/vault-messaging.html)*
