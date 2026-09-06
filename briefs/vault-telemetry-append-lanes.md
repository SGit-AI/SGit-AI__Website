# Telemetry from a published vault — a build brief

> How one vault sends messages to another, and how a vault whose read key is public reports anonymous usage back to its author. The append-lane mechanism, why a write-only token is the one credential that survives being published inside a public vault, the three things to verify before building, and the prompt to hand the builder agent.

*Source: <https://sgit.ai/briefs/vault-telemetry-append-lanes.html> · site v0.2.55 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Briefs](index.md) / Telemetry from a published vault

# Telemetry from a published vault

A build brief, written to be handed to the agent that will build the thing. The problem: a vault is about to be published with a **read key**, so every visitor can read every file in it — and it still needs to report anonymous usage back to its author. The answer is an **append lane**, and it works for one reason that is worth understanding before you write any code.

**What a build brief is, and how it differs from the asks below it.** The [cross-team briefs](index.md) are requests addressed to another team, with a status, that close when answered. This is the other kind: a durable reference an agent executes. It carries the mechanism, the traps, the things to verify first, and — at the bottom — [the prompt to hand the builder](#prompt), written to be pasted rather than paraphrased.

## What to read first

| Page | What it gives you |
|---|---|
| [Vault messaging](../docs/vault-messaging.md) | The worked example: two vaults exchanging encrypted messages, end to end, with curl |
| [API — append lanes](../api/append-lanes.md) | The six endpoints, the gates, the limits and the status codes |
| [`sg.append`](../vault/sg-bridge.md) | The same transport from inside a vault app, plus the `sg.on` event push |
| [PKI](../docs/pki.md) | Keypair lifecycle — `sgit pki keygen / export / encrypt / decrypt` |
| [Sub-vaults](../vault/sub-vaults.md) | The *other* cross-vault mechanism — `*.link.json`, for reading across rather than writing |

**One signpost, so you do not go looking.** The [Private Health Score vault](../demos/vaults/health-score/index.md) looks like the two-party case study and is not one: it is a single vault with three audiences — `patient/`, `doctor/` and `shared/` — split by *who is reading* rather than by copying, where sharing with the clinician means handing over a derived read key. There is no second vault and no message passing in it.

## The mechanism: four capabilities, deliberately split

| Capability | Holder | Can | Cannot |
|---|---|---|---|
| `append_token` | the sender | **write** | list, fetch, read anything |
| `enum_key` | the vault owner | list, fetch, mark-processed | write, purge |
| `write_key` | the vault owner | configure, purge | — |
| private key | the vault owner | **decrypt** | *never sent to the server* |

The server stores `SHA-256` of the first three and compares hashes. It never holds a raw capability key and never holds a private key at all. Two consequences decide the whole design:

- **The write response is blind** — exactly `{"ok": true}`. No file ID, no count, no metadata. A sender cannot learn what else is in the lane, or whether theirs was the first write.
- **No account is needed to send.** `POST /api/vault/append/write/{vault_id}` requires no access token; the `append_token` in the body is the entire gate.

## The shape of it

```
   PUBLISHED VAULT (read key public)          TELEMETRY VAULT (private, yours)
   ───────────────────────────────           ──────────────────────────────────
   holds: append_token                       holds: enum_key, write_key,
          + telemetry vault_id                      private key
          + your PUBLIC key

   a reader reaches step 4
        │  encrypt(event, your_public_key)
        │  POST /api/vault/append/write/{telemetry_vault_id}
        ├────────────────────────────────▶  gate: H(append_token) ∈ append_anchors?
        ◀────────────────────────────────   {"ok": true}   ← blind
                                                  │
                                            you: list (free) → fetch → decrypt locally
```

## Why publishing the token is acceptable — and where it stops being

Every visitor holds the published vault's read key, so **every visitor can read the `append_token` out of it.** That is not avoidable, and it is not the mistake it looks like: an append token grants *write only*. A visitor who extracts it cannot list the lane, cannot fetch anything, cannot read another reader's events — and because the write response is blind, cannot even tell whether the lane holds anything at all.

This is the one credential shape that survives being published inside a public vault. A vault key would not. A read key to a private vault would not: a read key decrypts **everything**, which is exactly the finding that has held two vaults back from publication here.

**What you do not get is authenticity.** Anything the browser holds, the visitor holds.

**Events can be forged.** Treat every row as an untrusted claim about what happened, never as fact. Encrypting to your public key gives you confidentiality, not proof of origin — the public key ships in the published vault, so anyone can produce a well-formed payload.

**The lane can be flooded.** The cap is **1000 pending files per token → 507**, at which point your real telemetry stops arriving. *This* is the failure mode to design against, not the confidentiality one.

Mitigations, in the order they matter: register **several `append_anchors`** so one flooded lane does not bury the others and revoking a sender is removing one anchor; drain aggressively (`list` → `fetch` → `mark-processed`, then `purge` with `folder:"processed"`); rotate the token by re-`configure`-ing and shipping a new vault release; and rate-limit client-side so honest readers never approach the cap.

## Three things to verify before building

Do not assume any of them. In order of how badly they break the design:

1. **Does `sg.append.write` work from a read-only session?** Your entire audience opens the vault with a *read* key. The authoring guide says read-only sessions fail closed, and the static-hosting notes list `sg.append.*` as rejected with `EREADONLY` in read-only contexts. If that holds in the hosted viewer, **the bridge path is unavailable to your readers**.
**The fallback is better anyway:** a direct `fetch()` POST to `/api/vault/append/write/{vault_id}`. That endpoint is account-less by design — no bridge, no permission grant, no writable session. The authoring guide is explicit that `fetch()` may be used for absolute `https://` URLs; those leave the vault and behave like any web request.
2. **Does the vault frame's CSP allow `connect-src` to the API host?** If the sandbox blocks the origin, neither path works and the answer is a host change, not an app change.
3. **Token format.** `^[0-9a-f]{16,128}$` — **hex only**. A prefixed token returns **400**, not 403, because it fails input validation before reaching any gate. Do not paste a `sha256:` CLI fingerprint in as a token; that is the most likely way to hit it.

**And one gap to design around.** The intended model is `append_token = H(recipient public key)`, so a sender could compute the lane address from a public bundle with no coordination. No shipped command emits the token — that derivation is **PROPOSED**, not shipped. Until it lands, treat the token as an opaque 64-hex secret you generate and register yourself.

Checked against the shipped CLI while writing this: `sgit pki` ships `keygen`, `export`, `encrypt`, `decrypt`, `sign` and `verify`. There is **no append-lane command in the CLI at all**, so the transport is HTTP or the browser bridge — nothing else.

## Setting it up

```
# once, on the telemetry vault
$ sgit pki keygen --label "Telemetry"
$ sgit pki export sha256:FINGERPRINT > telemetry-identity.json

$ curl -X POST https://send.sgraph.ai/api/vault/append/configure/$TELEMETRY_VAULT_ID \
    -H "x-sgraph-vault-write-key: $WRITE_KEY" -H "Content-Type: application/json" \
    -d '{"append_anchors":["<sha256 of the append_token>"],
         "enum_key_hash":"<sha256 of your enum_key>"}'

# reading — metadata-only listing reads ZERO payloads, so poll with this
$ curl -X POST https://send.sgraph.ai/api/vault/append/list/$TELEMETRY_VAULT_ID \
    -H "x-sgraph-vault-enum-key: $ENUM_KEY" -d '{"include_content": false}'
```

Filenames are server-assigned as `{epoch_ms}_{24-hex}.enc`, so they sort chronologically — which is what makes cursor pagination stable. Page with `after_file_id`. `mark-processed` is idempotent: an already-moved file comes back in `missing` rather than as an error, so a retried batch is safe.

## “Real time”, precisely

On the receiving side the kernel pushes `sg.on('append.new-messages', …)` on **tab focus and app open** — a dashboard app does not poll, it declares `"host_events": ["append.new-messages", "append.error"]` in `app.json` and reacts.

That means real time *while you are looking at it*, not a live stream. For anything closer, poll `list` with `include_content: false`; it is free.

## What you can and cannot learn

**Can:** that the vault was opened, which screens were reached, how far a reader got, event ordering and timing, and a session journey via a random per-session id the app mints in memory.

**Cannot: who.** There is no identity in this system and no login. Every reader is anonymous by construction — which is usually the point, but it does mean *“who opened the vault”* is not an answerable question. Only *how many*.

Two disclosure points, and neither should be skipped:

- **The platform's own default is that opening a vault never phones home.** External embeds are [click-to-load](../vault/sub-vaults.md) precisely so that it does not. A telemetry beacon breaks that expectation, so the vault should say so **visibly, in the vault** — not in a footnote. That is the same house rule every published vault page here follows: publish the work, then say exactly what it is and what it costs.
- **The server sees lane activity, size and timing** regardless of encryption, and it sees the requesting IP. *“The server cannot read the content”* is true. *“The traffic is invisible”* is not.

## The prompt to hand the builder agent

Written to be pasted as-is. Substitute the vault ids.

>

Build a vault app for *THE THING*. It will be published with a **read key**, so assume every visitor can read every file in it, including any credential it carries.

Emit anonymous usage events to a separate telemetry vault over an **append lane**. Read `https://sgit.ai/docs/vault-messaging.html` and `https://sgit.ai/api/append-lanes.html` first.

Constraints:

- Events go to `POST /api/vault/append/write/{TELEMETRY_VAULT_ID}` with the `append_token` in the body. **Verify first** whether `sg.append.write` is available in a read-only session; if it returns `EREADONLY`, use a direct `fetch()` to the account-less endpoint instead.
- Encrypt each payload to the telemetry vault's public key before sending. The public key ships in the published vault; that is fine, public keys are publishable.
- Never put a vault key, a read key to any other vault, or any other credential in this vault. The append token is the only credential that may appear, and only because it is write-only.
- Mint a random per-session id in memory. No names, no emails, no fingerprinting, nothing that identifies a person. Anonymous is the design, not a setting.
- Rate-limit client-side. The lane caps at 1000 pending files per token and returns 507 after that.
- Fail silently and never block on telemetry — if the POST fails, the reader must not notice.
- Put a visible, plain-English notice in the vault saying that anonymous usage events are sent and what they contain. Opening a vault does not normally phone home; this one does, so say so.
- Treat every received event as an untrusted claim. Anyone holding the read key can forge or flood the lane; the data is directional, not evidential.

Deliverables: the app, the event schema, the telemetry vault's `configure` call, and a dashboard app in the telemetry vault that subscribes to `sg.on('append.new-messages')` and renders the funnel.

The canonical markdown copy lives in the [SGit-AI__CLI](https://github.com/SGit-AI/SGit-AI__CLI) repo under `team/humans/dinis_cruz/claude-code-web/`, which is where every brief on this page is filed.

[← Briefs](index.md)[Publishing a vault →](../demos/vaults/publishing.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/briefs/vault-telemetry-append-lanes.html)*
