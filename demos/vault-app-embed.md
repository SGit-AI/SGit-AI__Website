# A vault app, live inside this page — sgit.ai demos

> The complete walkthrough: create a vault app, push it, derive and publish the read key, and open the app live inside a sgit.ai page in a sandboxed iframe with a postMessage window.sg bridge.

*Source: <https://sgit.ai/demos/vault-app-embed.html> · site v0.2.47 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

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

## Embedding the full SG/Vault UI — the gap closed

The embed above is our minimal host: ~170 lines, enough bridge for a read-only app. The obvious next step was embedding the *real* SG/Vault interface — App-Mode chrome, or the vault browser with its FILES / SGIT / SETTINGS rail. When we first ran that experiment it worked in every respect but one: the credential. The loader documented a read-only format but the client rejected it, and the CLI's `64hex:vault_id` shorthand was parsed as a passphrase, PBKDF2'd, and derived the wrong file ids (we measured `abfd8ea0f1a2` where the vault's real ref id is `11ea50e81f4d` — hence "Vault not found"). We filed both as asks.

**They landed.** The deployed loader now detects a read-key credential as **format 6** — `<64-hex read_key>:<vault_id>`, matching what `sgit clone` already accepted — and, critically, *checks it before the passphrase formats*, which is exactly the ordering bug we hit. It also strips the sgit CLI's canonical key prefixes before detection, so a key pasted straight from new CLI output is understood — including `sgit_rk1_`, the read-only one, which is the form we publish. (Its write-credential sibling is the prefix our own build refuses to let onto this site at all: the release validator treats that string as a leak and fails the build, which is why you will not find it written out here.) Re-running the same experiment against the live build:

| Question | Answer | Evidence |
|---|---|---|
| Can the vault UI be iframed at all? | **Yes** | no `X-Frame-Options`, no `frame-ancestors` |
| Does App Mode work inside a cross-origin iframe? | **Yes — fully** | the complete HUD: toolbar, URL bar, read/write badges |
| Can it open with *only the read key*? | **Yes — now** | all three forms parse in the deployed loader (`hex:id`, `sgit_rk1_hex:id`, and the legacy `id hex`); App Mode booted this Field Notes app from the published read key alone, six SVG studies rendered, the app's own status line reading `content.json` over the bridge |
| Does the vault browser open read-only? | **Yes** | `vault-shell` with the FILES / SGIT / SETTINGS rail, the real decrypted tree (4 files, 10.6 KB), and an explicit `R1 W0` + **Read-only** badge in the chrome |
| Is the SGit view reachable? | **Yes — but still no deep-link** | driving the nav reaches HISTORY / REFS / TREE / BRANCHES / STATUS / REPAIR with both real commits listed; no URL selects a view, so a host page cannot frame the SGit view *in isolation*. The one ask still open. |

So the credential gap is closed, and the consequence is the point of this whole page: **a published read key is now enough to embed the official interface** — no account, no token, no write capability anywhere in the chain. And the mechanism got better than the one we first tested: the UI now ships an **embed protocol**, so the host page hands the key over a validated `postMessage` handshake instead of a URL fragment. The key never appears in any URL, is never written to the frame's storage (it lives in the frame's memory for the session), the frame proves it is the right recipient before the key is sent, and the host gets structured `vault-ready` / `vault-error` events back instead of guessing from load timings.

Below is exactly that — both surfaces, opened with the same published key printed further up this page, loading on click because they pull the full UI from another origin. The area is deliberately wider than this text column, because the vault browser is a full working surface, and there is a full-screen button for vaults with a big UX.

Loads `dev.vault.sgraph.ai` in an iframe and completes the embed handshake. Nothing on sgit.ai ever sees more than the published read key it already prints.

**What is still not possible — precisely.** The two buttons above select a *surface* (App Mode or the vault browser). They cannot select a *view* inside the browser: the SGIT inspector and SETTINGS panels are one click away on the left rail, but the embed message carries only `{key, mode, deepLink}` where `deepLink` is a file path — there is no field that names a view, and view switching stays an in-page event. So "open straight onto the commit history" is still one small protocol field away, and [the briefing](../briefs/briefing-sgvault-ui-embed.md) now states exactly that ask: an optional `view` field on `vault-open`, applied after mount. Everything else on this page works today.

## Honest scope

Two hosts now run on this page, and keeping both is deliberate. The **minimal** host is ~170 lines and shows the protocol with nothing hidden: derive, fetch, decrypt, answer `sg.vfs` over postMessage. The **official** host is the real product — full `window.sg` surface, permissions, HUD chrome, and now an embed handshake that keeps the key out of URLs and storage. Read the small one to understand the mechanism; use the big one to see what a product built on it feels like. Everything above is live and reproducible from the commands on this page.

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
