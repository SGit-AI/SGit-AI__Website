# Updates — sgit.ai

> What changed on sgit and on this site, as it happens — one entry per story rather than per release, each linked to the release that carries it. RSS and JSON feeds included.

*Source: <https://sgit.ai/updates/index.html> · site v0.2.35 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

# Updates

What changed on sgit and on this site, as it happens — one entry per story rather than per release. The [version log](../admin/versions.md) is the complete technical record; this is the readable one.

Follow along: [RSS](feed.xml) · [JSON](updates.json). Every entry links to the release that carries it.

## 2026-08-18

### [Verify the fix pack, not just the bug](#verify-the-fix-pack-not-just-the-bug) [v0.2.34](../admin/versions.md)

processpkiaccuracy

The documentation gap above arrived as a well-built fix pack from the SG/API team: a gap analysis, code-verified source material, and a draft of the missing page. The most valuable line in it was its own instruction to check the claims before publishing. **Three did not survive.**

- **"The security page actively denies PKI."** It did not. A sweep for *symmetric*, *asymmetric*, *public key*, *PKI* and *keypair* returned zero occurrences. The page was silent, not wrong — and publishing a correction for a claim we never made would have put a false statement in our own changelog.
- **"Search the site for stale `inbox` naming."** There is none. Two hits, both ordinary English; no `/api/vault/inbox/*` path anywhere.
- **"Seal to the recipient's X25519 key."** Not what ships. Running `sgit pki keygen` prints **RSA-OAEP 4096-bit** and **ECDSA P-256**. Publishing the draft as written would have told integrators to build against the wrong primitive.

Two more corrections came from running the CLI rather than reading about it: `sgit pki export` emits a **JSON bundle** of two PEM blocks, not the `.pem` file the draft redirected into — so the draft's `sha256sum public-key.pem` derivation of a lane address is not well defined — and `keygen` requires a passphrase, which no draft step mentioned.

The whole exchange, including what we got wrong, is on [the briefs page](../briefs/index.md).

### [The API reference we did not have](#the-api-reference-we-did-not-have) [v0.2.34](../admin/versions.md)

apimessagingdocs

An agent was asked how to send an encrypted message between two vaults. It read this site and could not find out. The capability had shipped months earlier.

The diagnosis was uncomfortable and simple: **we documented both halves and never wrote the sentence that joins them.** The transport was on one page as `sg.append`, the crypto on another as `sgit pki`, and neither referenced the other. There was also no HTTP API reference anywhere — awkward for a project whose whole argument is that the API *is* the surface.

- **[Sending messages between vaults](../docs/vault-messaging.md)** is the page that was missing: append lanes composed with keypairs, worked end to end in CLI, curl and `sg.append`.
- **[An /api/ section](../api/index.md)** now exists — [authentication](../api/authentication.md), [vault objects](../api/vault-objects.md), [append lanes](../api/append-lanes.md) and [errors](../api/errors.md).
- **[The PKI page](../docs/pki.md)** documents the keypair lifecycle, run against the shipped CLI rather than recalled.
- **[The security page](../security/index.md#pki)** gained the asymmetric layer it never mentioned. It never claimed sgit had no public-key layer — it simply said nothing, and on a page like that one, silence reads as denial.

The one step that is not wired end to end is labelled **PROPOSED** with an interim recipe, rather than quietly documented as working.

## 2026-08-17

### [Three walkthroughs, read back as documents](#three-walkthroughs-read-back-as-documents) [v0.2.32](../admin/versions.md)

vaultsvideorisk-graph-explorer

A video is invisible to a search engine, to `llms-full.txt`, and to any agent reading this site as documentation. It is also full of *"this guy here"* and *"look at this"* — pointing that a transcript cannot resolve.

So [the Risk Graph Explorer walkthroughs](../demos/vaults/risk-graph-explorer/videos/index.md) now carry the player at the top and **the same session read back underneath**: fifteen moments, each a timestamp that deep-links into the video, the frame the screen was showing then, and what is actually happening in it.

- Nine frames come from a narrated-review export; the other six were captured from the **live vault** with its published read key, driven to the exact state being described.
- What the frames turned up is most of the value, because none of it is audible: negative answers draw **named edges** (`never-exercised-on`, `absent-for`) rather than silence; "no egress" draws a single assurance-coloured edge in a field of amber; and every risk ships with a **"ceases when any of these hold"** list — its own falsification condition, cited to facts.

The [seven views page](../demos/vaults/risk-graph-explorer/views/index.md) covers the same vault view by view.

### [Printing stopped costing every reader](#printing-stopped-costing-every-reader) [v0.2.31](../admin/versions.md)

printperformance

Save a walkthrough page as a PDF and it used to come out wrong in two ways: the site navigation painted **across the middle of page 2**, translucent, with the prose showing through it — and any screenshot you had not scrolled past exported as a blank gap.

The first was a sticky header: Chrome paints a sticky box once, wherever it happens to fall in the paginated flow. The second was subtler. Screenshots load lazily, and `loading="lazy"` defers the **decode**, not just the download — so an image far below the viewport sat there fetched, at zero width, and printed as nothing.

- The first fix made every reader pay: it pre-loaded all the images so printing would work. That was the wrong trade and it was rejected.
- **The bypass now fires only on print** — on `beforeprint`, and on the Cmd/Ctrl-P keystroke, which lands a few hundred milliseconds earlier and buys the images a head start.
- Measured on a page nobody scrolled: **1 image loaded while reading, 9 of 9 in the PDF.**

Also in this release: `@page` margins, colour preservation so the amber/green distinction survives, `break-inside` rules so a caption is never stranded on the page after its picture, and per-release cache-busting on assets — because for ten minutes after every release, returning readers were running new HTML against old CSS.

### [Green does not mean live](#green-does-not-mean-live) [v0.2.33](../admin/versions.md)

cideployprocess

Two consecutive releases pushed cleanly, reported success, and **never reached the site.** A human noticed on a phone, forty minutes later, because the version badge still showed the old number.

The release script verified that both remotes were in sync — and they were. The failure was in a job neither remote knows about: GitHub Pages could not download `actions/configure-pages`, got a **429 Too Many Requests**, and the deploy died in "Set up job" before running a single step. Validation passed. Tagging passed. The site served a two-release-old page.

- **A release now ends by asking the live site what version it is serving**, polling with a cache-buster until the badge matches — and **aborting loudly** if it never does.
- The cost is up to eight minutes per release. The alternative, demonstrated twice in one afternoon, is telling somebody a fix is live when it is not.
- Same principle as the rules already in the build: a page nothing links to, a page the index omits, and a page the deploy never published are all equally unpublished.

There is a longer account of this one in [Green does not mean live](../articles/green-does-not-mean-live.md).


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/updates/index.html)*
