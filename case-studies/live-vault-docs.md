# A live site whose host cannot read it — sgit.ai case study

> A case study in the mechanism: two Claude Code sessions, two encrypted vaults, one page — with architecture diagrams of the publishing pipeline and the in-browser read path.

*Source: <https://sgit.ai/case-studies/live-vault-docs.html> · site v0.2.24 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Deploy](../deploy/index.md) / How this works

# How this page works

The [deployment guidance](../deploy/index.md) next door is not stored on this website. It is written by a different team, in a different Claude Code session, into a different encrypted vault — and your browser assembles it from ciphertext at the moment you ask for it. This page explains the whole mechanism, because it is a compact demonstration of what sgit is actually for.

## Two sessions, two vaults, one page

Nothing here is a pipeline anyone had to build. Both sides just use sgit, and the shared vault format does the integration:

*[diagram]*
Neither team's session knows about the other's. The only shared thing is a vault format and a published read key.

Concretely, when the SG/Send team improves a deployment guide, the sequence is: edit markdown → `sgit commit` → `sgit push`. That is the entire publish step. There is no build to trigger on our side, no webhook, no content sync, and no copy of their text in our repository. The next visitor to the Deploy page gets the new version because the browser reads their vault's current commit.

## What happens when you open the page

Everything below runs client-side, in about 300 lines of JavaScript using the browser's built-in Web Crypto API:

*[diagram]*
The server answers ordinary GETs for opaque file ids. It never sees a key, a filename, or a byte of plaintext.

## Why the caching is safe — and why it's this shape

The cache policy is not a tuning choice; it falls out of the data model. Object ids are content hashes *of the ciphertext*, so an object can never change under its id — which makes it permanently cacheable. The ref is the one mutable pointer, so it is the only thing that has to be refetched at all:

| Tier | What it holds | Lifetime | Why |
|---|---|---|---|
| memory | decrypted objects | this page session | avoids decrypting the same tree twice while you click around |
| Cache API | ciphertext of `obj-cas-imm-*` | until you clear it | content-addressed ⇒ immutable ⇒ can never be stale |
| localStorage | the file index (path → blob) | keyed by commit id | a pure function of the commit, so an unchanged HEAD reads no tree objects |
| freshness window | the ref (`ref-pid-muw-*`) | **120 s** (`ref_ttl_s`) | it is the mutable HEAD; checking it once per window instead of once per page view is what takes steady-state reading to zero requests |

### The freshness window

The ref has to be refetched sometimes — that is how a new commit is noticed. It does not have to be refetched on *every page view*. So the answer is kept for `ref_ttl_s` seconds (120 by default, set in `deploy/vault.json`), and inside that window the reader reuses it.

Three things follow, and they are the whole trade:

- **Reading the docs costs nothing.** Click through ten pages inside the window and the network stays silent — every object is content-addressed and already cached, and the one mutable object is inside its window. The panel logs the ref as `TTL` with a live countdown to the next check.
- **Server load stops scaling with page views.** It scales with *readers per window* instead: one 69-byte request per reader per two minutes, however much they read.
- **Propagation is delayed, and bounded.** A new commit is picked up within 120 seconds at worst, and immediately if you press **check for new commit** — which forces a fetch and ignores the window. That button is not a debug affordance; it is the escape hatch that makes the window safe to have.

Measured on this site: a cold load fetches 18 objects (~14 KB); the next load fetches **one 69-byte object** — the ref — and serves the rest from cache; a load inside the freshness window fetches **nothing at all**. Open the vault panel and press **clear list**, then click around, to watch it happen.

## Who can see what

### SG/Send server

- opaque object ids
- ciphertext blobs
- sizes and timing
- the vault id

### GitHub Pages

- the page shell
- the public read key
- no vault content at all

### Your browser

- the read key
- decrypted filenames
- decrypted content
- the commit history

Two hosts, neither of which can read the documents. The decryption exists in exactly one place: the tab in front of you.

The read key is deliberately public — it is *read-only by construction*, derived one-way so it cannot be turned back into write access. Publishing it is what lets the site show the content without the site ever being trusted with the ability to change it. Anyone can verify that: take the key out of `deploy/vault.json`, run `sgit clone --read-key <key> fyofmkvr`, and watch a write attempt get refused.

## Why this is the interesting demo

- **Two teams integrated without integrating.** No API contract was designed, no sync job written, no permissions negotiated. One side pushes to a vault; the other side holds a read key. That is the whole interface.
- **Publishing is a git operation.** The SG/Send team's release process is `sgit push` — and their content appears on a website they do not control and cannot deploy to.
- **Least privilege that is structural, not procedural.** This site *cannot* alter their documentation, however compromised it might be, because the key it holds does not carry that power.
- **The same property scales down to one agent.** Give an agent a read key and it can read a knowledge base without any ability to corrupt it; give it the full key and it can contribute. That is the same mechanism this page uses, applied to agent workflows.

## The honest trade-offs

- **Search engines and agents see an empty shell.** Content that only exists after decryption is invisible to anything that does not run JavaScript. sgraph.ai solves this by decrypting at the CDN edge and serving `.md` alongside each page; this site is static, so it does not. That is a real cost of the approach as built here.
- **It needs a secure context.** Web Crypto is unavailable over plain HTTP, so this only works on HTTPS (or localhost).
- **The server can't help.** No server-side search, no previews, no summaries — everything is opaque to it. That is the point, and it is also a limitation.
- **Diagrams are hand-drawn SVG, not a diagramming library.** This site is also served *from inside a vault*, where external resources are blocked by the app authoring contract — so importing a renderer from a CDN would break the very demonstration this page describes. The constraint chose the implementation.

[← The deployment docs](../deploy/index.md)[Git and vaults →](../vault/git-and-vaults.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/case-studies/live-vault-docs.html)*
