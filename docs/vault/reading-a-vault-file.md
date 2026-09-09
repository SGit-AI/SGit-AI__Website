# Reading one file out of a vault — SG/Vault

> The primitive under every live embed on this site: derive the address from a published read key, fetch ciphertext over CORS, decrypt in the browser — and the sandbox rules for rendering what comes back, including why a PDF is a download and not an embed.

*Source: <https://sgit.ai/docs/vault/reading-a-vault-file.html> · site v0.2.75 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../index.md) / [Docs](../index.md) / Reading one file out of a vault

**Surface:** a page on a `*.sgit.ai` site, outside every vault host. [The other surfaces →](../surfaces.md)

# Reading one file out of a vault, from any web page

A published read key plus four browser APIs is enough to pull a single named file — a JSON manifest, a slide source, a screenshot, a PDF — out of an encrypted vault and use it on a page that has no backend, no build step and no copy of the file. This is the primitive underneath [the app embed](../../demos/vault-app-embed.md), [the live docs reader](../../case-studies/live-vault-docs.md) and [the deck viewer](../../demos/vaults/aiuc-1-conformance/index.md#decks), written down on its own because all three are built on it.

**The one-sentence version.** The vault's HTTP API serves ciphertext at a URL you can *compute* from the read key, so a page fetches bytes the server cannot read and decrypts them itself — which means **publishing a file to a web page is the same act as pushing it to the vault**, with nothing in between.

## The four steps

Everything below runs in the browser. The read key is a 64-character hex string and a vault id, and it is the whole credential — there is no account, no token and no session.

|  | What happens | Which API |
|---|---|---|
| **1 · Import the key** | The same 32 bytes are imported twice: once as an AES-GCM key for decryption, once as an HMAC-SHA256 key for deriving ids | `crypto.subtle.importKey` |
| **2 · Derive the address** | HEAD lives at `ref-pid-muw-` plus the first 12 hex characters of `HMAC(key, "sg-vault-v1:file-id:ref:" + vault_id)`. The server never told you this — you computed it | `crypto.subtle.sign` |
| **3 · Fetch the ciphertext** | `GET /api/vault/read/<vault_id>/bare/refs/<id>`, then `bare/data/<object id>`. Plain CORS GETs, no auth header: the bytes are useless without the key | `fetch` |
| **4 · Decrypt and walk** | First 12 bytes are the IV, the rest is the AES-GCM body. Ref → commit → tree → blob; filenames are encrypted inside the trees, so the path index is itself something you decrypt | `crypto.subtle.decrypt` |

The reader that does this is about 90 lines and is on this site twice, deliberately in the open: [`assets/vault-embed.js`](../../admin/index.md) exports it, and `assets/vault-docs.js` is the instrumented version that shows its own cache accounting.

## What may be cached, and the one thing that may not

The object model decides this, not a policy. An id containing `-imm-` is content-addressed and therefore immutable, so it can be cached forever. The ref is the single mutable pointer, and caching it is the one mistake that fails silently — a stale ref renders an *older commit from perfectly valid ciphertext*, so nothing errors and the page is simply wrong. The readers here keep a short freshness window on the ref instead, which is also the worst case delay before a new push is noticed. [The caching contract is part of the API reference.](../../api/vault-objects.md)

## Vault content is not your page's content

A read key lets anyone read the vault, so the interesting question is the other direction: **the vault's bytes arriving in your page are untrusted input**, authored by whoever holds the write key. Rendering them into your own document hands a vault author your origin — your cookies, your storage, your DOM. The rule this site follows is that **the viewer comes from the site and only the data comes from the vault**, and that the data is rendered inside an opaque origin.

| Vault content | Where it is allowed to run | Why |
|---|---|---|
| Static markup — a slide, a document | `<iframe sandbox>` with **no**`allow-scripts`, CSP `default-src 'none'; img-src data:` | It never needed scripting, so scripting is switched off rather than contained. Nothing in it can make a request |
| Executable — an app, a deck that builds its slides in JavaScript | `<iframe sandbox="allow-scripts">`, reads served over `postMessage` | Opaque origin: no cookies, no storage, no reach into the host page. It asks the host for bytes and gets only bytes |
| Images | Decrypted by the host, handed in as `data:` URIs, or blob URLs minted *inside* the frame | A vault path in a `src` resolves against an opaque origin and 404s, so the bytes have to be carried in |
| PDFs | Downloaded, not embedded | Measured, not assumed — see below |

## Why a PDF is a download and not an embed

The obvious move is to decrypt the PDF, wrap it in a blob and point a sandboxed iframe at it. **Chrome refuses.** Tested across every sandbox combination, the console says the same thing each time:

> `Failed to load 'blob:…' as a plugin, because the frame into which the plugin is loading is sandboxed.`

The browser's PDF viewer is a plugin, and plugins do not run in sandboxed frames. That leaves two honest options and one dishonest one. Dropping the sandbox works — and gives vault bytes your origin, which is the thing this whole page is about not doing. Shipping a JavaScript PDF renderer works and costs a megabyte of vendored dependency. **Handing the bytes to the browser's own download works, costs nothing, and is what this site does**: the file is decrypted in the page, wrapped in a blob, and offered through a normal download — while the slides, which are the thing anyone actually wants to read on a web page, are rendered live and are searchable, linkable and legible to an agent in a way a PDF never is.

A download is triggered from the page rather than from inside a frame for the same reason: a sandbox without `allow-downloads` blocks it, and adding that permission to untrusted content would be the wrong way round.

## The worked example: decks

[Four decks on the AIUC-1 page](../../demos/vaults/aiuc-1-conformance/index.md#decks) and [five on the Licence to Operate page](../../demos/vaults/licence-to-operate/index.md#decks) are read this way. The split, concretely:

- **From the vault:** the manifest, each deck's slide source, the speaker notes, the screenshots and the printed PDF.
- **From the site:** the deck tabs, the slide list, prev and next, the notes toggle, the PDF button, the deep links, and the sandbox policy the whole thing runs under.

A deck builds its slides by *running* — it is JavaScript that calls `S.push({t, notes, html})` — so it has to execute somewhere. It executes in a scripted, opaque-origin frame with `default-src 'none'`, which posts back a plain array; the site never evaluates it. Each slide's markup then goes into a second frame with scripting off. The stage is 1600×900 because that is the size the deck's own CSS was written against, and the *element* is scaled rather than the document, so a slide looks the same at any column width with no reflow.

Two published shapes are handled, because vaults differ in what they chose to publish: one ships its deck sources (small, screenshots fetched only when a slide uses one), the other ships only the built decks (large, screenshots already inline). The reader prefers the source and falls back to the built file, truncated at the point where the vault's own viewer starts.

**Doing this yourself?** This page explains the mechanism. [**The build brief**](../briefs/vault-decks-on-a-site.md) is the instructions — the contract a vault must publish, the checks that mean it is done, and a prompt to hand the agent who will build it.

## What this costs a reader

Nothing is installed and nothing is signed into. The first slide of a deck costs the ref, the commit, the trees, the manifest and one slide source; every later slide in that deck is already decrypted; a screenshot is fetched once and reused. The server sees requests for opaque ids and returns ciphertext, which is the entire point: **it is serving a presentation it cannot read.**

The credential on those pages is a read key, derived one-way from a vault key that is not published. Read keys can be handed out; vault keys never are. [The publishing method](../../demos/vaults/publishing.md) · [API: vault objects](../../api/vault-objects.md) · [Static hosting](static-hosting.md)


---

*[Site index for agents](../../llms.txt) · [HTML version](https://sgit.ai/docs/vault/reading-a-vault-file.html)*
