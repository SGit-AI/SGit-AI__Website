# A vault app, live inside this page — sgit.ai demos

> The complete walkthrough: create a vault app, push it, derive and publish the read key, and open the app live inside a sgit.ai page in a sandboxed iframe with a postMessage window.sg bridge.

*Source: <https://sgit.ai/demos/vault-app-embed.html> · site v0.2.12 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Demos](index.md) / Vault app embed

# A vault app, live inside this page

Below is an application running out of an encrypted vault, embedded in this page with nothing but a **published read-only key**. This walkthrough is the complete process that produced it — every command, the key that is deliberately public, and the one that never will be.

**The one-sentence mechanism:** the vault's ciphertext is fetched from the SG/Send server over CORS, decrypted in your browser with the read key printed on this page, and the vault's `index.html` is booted inside a sandboxed iframe with a `window.sg` bridge — the same shape SG/Vault's own vault-in-vault embedding uses. No copy of the app or its content exists on sgit.ai.

## The live embed

Click to open it. The status line inside the app will read `content: sg.vfs.readText("content.json") — live from the vault`, which is the bridge proving itself: the app asked the embed host for a vault file and got it.

Loads ~10 encrypted objects from `dev.send.sgraph.ai` and decrypts them here. Nothing you do in it can write — the page only holds a read key.

## How this vault was made, end to end

**1 — Write the app.** A vault app is one self-contained `index.html` — CSS and JS inlined, content in `content.json`, generative SVG instead of image files — plus an `app.json` that auto-launches it. It follows the [authoring contract](../vault/vault-apps.md): no `<link href>`, `<script src>` or `<img src>` against vault paths, content read via `sg.vfs.readText` with an inlined fallback, and `sg-app-ready` posted when rendered.

```
demo-vault-gallery/
├── index.html      # the app — one file, contract-compliant
├── content.json    # the editable content the app reads over the bridge
├── app.json        # { "entry": "index.html", "present": true, "auto_open": true }
└── README.md
```

**2 — Make the folder a vault and push it.**

```
$ sgit init --existing .
  Vault key: <passphrase>:4bshby5n   ← saved to a password manager. Not printed here, not ever.
$ sgit commit -m "Field Notes v1: app, content, README" && sgit push
  Push complete. Pushed 1 commit(s), 4 object(s) uploaded.
```

**3 — Derive the read key.** It is computed one-way from the vault key: it can decrypt everything in the vault and can never be turned back into write access.

```
$ sgit dev derive-keys '<vault-key>'
  read_key: 2848993a68c02a33…   ← this one is safe to publish. See below.
```

**4 — Publish the read key.** Deliberately, in full, in this page's source:

```
vault id : 4bshby5n
endpoint : https://dev.send.sgraph.ai
read key : 2848993a68c02a33ea5582902c391901191e53680d35b36c0e76185d4107ad81
```

Anyone can take those three lines and read this vault — from the CLI (`sgit clone --read-key 2848993a68c0… 4bshby5n`), from their own page, from a script. That is the point: **read access is a capability you can hand out**, without an account, without the host mediating it, and without it ever becoming write access. A write attempt with this key is refused by construction — try it.

**5 — Embed it.** The host on this page is [`assets/vault-embed.js`](../admin/index.md), ~170 lines: derive the ref id with HMAC-SHA256, fetch ciphertext over CORS, decrypt with Web Crypto, boot the app in an iframe with `sandbox="allow-scripts"` (opaque origin — the app gets no cookies, no storage, no reach into this page), and answer its `sg.vfs` calls over postMessage.

## What the app can and cannot do in here

| Capability | In this embed | Why |
|---|---|---|
| `sg.vfs.readText` / `sg.vfs.read` | works | served by the host from decrypted vault objects |
| `sg.loadCss` / `sg.loadJs` | works | same read path, injected into the frame |
| any mutation (`sg.fs.*`, `sg.vault.*`, …) | impossible | the page holds only a read key — there is no write capability to misuse, not even by a bug in the host |
| reach this page, cookies, storage, top navigation | blocked | `sandbox="allow-scripts"` and an opaque origin; the only channel is postMessage |

## Embedding the full SG/Vault UI — what we found

The embed above is our minimal host. The obvious next step is embedding the *real* SG/Vault interface — the App-Mode chrome, or the vault browser with its FILES / SGIT / SETTINGS rail — so we ran the experiment against the live UI, framed inside a page like this one. Results, honestly:

| Question | Answer | Evidence |
|---|---|---|
| Can the vault UI be iframed at all? | **Yes** | no `X-Frame-Options`, no `frame-ancestors` |
| Does App Mode work inside a cross-origin iframe? | **Yes — fully** | with a valid credential, `app-shell` booted this same Field Notes app under the complete HUD: toolbar, URL bar, read/write badges |
| Can it open with *only the read key*? | **Not yet** | the loader's format catalogue documents a read-only credential (`<vault_id> <64-hex read_key>`), but the client rejects it — and the CLI's `64hex:vault_id` shorthand gets treated as a passphrase and derives the wrong file ids |
| Can the SGit view be embedded in isolation? | **No URL for it** | view switching is an in-page event; there is no deep-link that selects a view |

So the one thing between this page and embedding the official UI is the credential format — everything downstream of it already works. Both gaps are now precise asks in [the briefing to the SG/Vault UI team](../briefs/briefing-sgvault-ui-embed.md): honour the documented read-only format end to end, and add a `|view:sgit` deep-link so the commit/ref/tree inspector — the best possible "look inside the encrypted store" demo — can be a page of its own. The moment the first ask lands, this page gains a second embed: the real UI, opened with the same published read key you see above.

## Honest scope

This is our **minimal** host — enough bridge for read-only apps, which is exactly what a published read key permits. The canonical app-iframe host (full `window.sg`, permissions, HUD chrome) is the SG/Vault UI's code, and [a briefing asking to reuse it](../briefs/briefing-sgvault-ui-embed.md) is with that team; when it lands, this page swaps hosts and the walkthrough gains the full-fidelity embed. Until then: what you see above is real, live, and reproducible from the commands on this page.

| Shape | Evidence status | Copy or reference |
|---|---|---|
| Gallery (app + content) | **LIVE** — the embed above reads the real vault on every load | **Reference** — a push to the vault changes this page's embed with no rebuild |

## Related

- [Building vault apps](../vault/vault-apps.md) — the authoring contract this app follows
- [A live site whose host cannot read it](../case-studies/live-vault-docs.md) — the same read path rendering markdown docs
- [Sub-vaults](../vault/sub-vaults.md) — vault-in-vault, the pattern this embed mirrors
- [The plan](../admin/plans/why-expansion-plan.md) — two more demo vaults (a report, a two-agent inbox) follow this template

[← Demos](index.md)[Building vault apps →](../vault/vault-apps.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/demos/vault-app-embed.html)*
