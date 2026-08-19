# API: append lanes — sgit.ai

> The six append endpoints — the write-only vault-to-vault message transport. Four separated capabilities, the blind write response, server-assigned sortable filenames, idempotent mark-processed, and the limits.

*Source: <https://sgit.ai/api/append-lanes.html> · site v0.2.36 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [API](index.md) / Append lanes

# Append lanes

A write-only channel attached to a vault, gated by a token the writer holds and nothing else. This is the transport behind [vault-to-vault messaging](../docs/vault-messaging.md) and behind [`sg.append`](../vault/sg-bridge.md) in the browser bridge — and it is deliberately generic: the same primitive carries messages, logs, signals, control messages and state flows.

**Naming.** This API was called **inbox** before v0.32.7. Every `/api/vault/inbox/*` URL is gone, and `purge` takes `folder:"pending"` or `"processed"` — the old `"inbox"` value returns **400**. If you are reading older material, translate.

## The six endpoints

All **POST**, all under `/api/vault/append/`.

| Path | Gate | Does |
|---|---|---|
| `configure/{vault_id}` | `x-sgraph-vault-write-key` | Registers `append_anchors` — hashes of accepted senders — and `enum_key_hash` |
| `write/{vault_id}` | `append_token`**in the body** | Appends a payload. **Account-less**: no access token required |
| `list/{vault_id}` | `x-sgraph-vault-enum-key` | Paginated listing, optionally with inline content |
| `fetch/{vault_id}` | enum key | Fetch specific file IDs, batched |
| `mark-processed/{vault_id}` | enum key | Moves pending → processed. Idempotent |
| `purge/{vault_id}` | write key | Deletes. `folder: "pending" | "processed"` |

## Why the gates are split this way

Four capabilities, and the split is the whole design:

| Capability | Holder | Can | Cannot |
|---|---|---|---|
| `append_token` | the sender | write | list, fetch, read anything |
| `enum_key` | the vault owner | list, fetch, mark-processed | write, purge |
| `write_key` | the vault owner | configure, purge | — |
| private key | the vault owner | **decrypt** | *never sent to the server* |

A sender can put something into your vault and learn nothing at all — not the contents, not the volume, not whether anyone else writes there. The server stores `SHA-256` of the first three capabilities and compares hashes; the fourth it never sees.

## Four contracts worth relying on

- **The write response is blind.** `/write` returns exactly `{"ok": true}` — no file ID, no count, no metadata. This is a security property, not an oversight: a returned ID would leak lane state to a party who is only allowed to write.
- **Filenames are server-assigned** as `{epoch_ms:013d}_{24-hex}.enc`. Being chronologically sortable is what makes cursor pagination stable — pass the last file ID you saw as `after_file_id`.
- **Metadata-only listing is free.** `include_content: false` reads **zero** payloads. Poll with it, then fetch on demand; polling with content is the common way to hit the 3 MB ceiling for no reason.
- **mark-processed is idempotent.** An already-moved file comes back in `missing` rather than as an error, so retrying a batch after a timeout is safe.

## Several senders on one vault

Register several `append_anchors` and each sender writes into their own lane, distinguished by their token. A listing can be scoped to one lane, so one correspondent flooding you does not bury another — and revoking one sender is removing one anchor, with no effect on the rest.

## Limits and codes

| Limit | Value | On breach |
|---|---|---|
| Payload per write | 5 MB | 413 |
| Pending files per token | 1000 | 507 |
| File IDs per batch | 100 | 400 |
| Inline content when listing | 3 MB cumulative | 413 |
| Page size | 50 default, 200 max | clamped silently |

The `append_token` pattern is `^[0-9a-f]{16,128}$` — hex only. A prefixed token returns **400**, not 403; see [errors](errors.md) for why that distinction saves time.

## See also

- [Vault messaging](../docs/vault-messaging.md) — this API composed with PKI into a worked example
- [`sg.append`](../vault/sg-bridge.md) — the same six operations from a vault app
- [Errors and limits](errors.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/api/append-lanes.html)*
