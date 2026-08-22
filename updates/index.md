# Updates — sgit.ai

> What changed on sgit and on this site, as it happens — one entry per story rather than per release, each linked to the release that carries it. RSS and JSON feeds included.

*Source: <https://sgit.ai/updates/index.html> · site v0.2.40 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

# Updates

What changed on sgit and on this site, as it happens — one entry per story rather than per release. The [version log](../admin/versions.md) is the complete technical record; this is the readable one.

Follow along: [RSS](feed.xml) · [JSON](updates.json). Every entry links to the release that carries it.

## 2026-08-22

### [The ninth published vault — four apps in one tree, and a reader that asked for nothing it did not need](#the-ninth-vault-four-apps-in-one-tree) [v0.2.40](../admin/versions.md)

vaultsgraphspermissions

[VoiceDebrief](../demos/vaults/voice-debrief/index.md) joins [the published vaults](../demos/vaults/index.md). Four apps in one encrypted vault, lifting meaning out of text — from fictional voice notes to Article 9(2) of the EU AI Act — into typed semantic graphs.

*Written up from the vault and the release that published it; the page itself is the primary record.*

- **The claim in one line.** A paragraph is not a string, it is a **graph** — and so is the paragraph next to it. Lift both into typed nodes and the two join *node-to-node* through an intermediate layer, never paragraph-to-paragraph. Part 4 works that end to end against one real legal provision. Parts 1–3 run on a **fictional** corpus, and the vault says so in its own README.
- **Read over one folder, write over nothing.** `app.json` declares `fs.read` on `part-4/` and nothing else — no write, no mkdir, at any path. The host's own chrome renders the result as `R3 W0`. A capability never requested cannot be misused.
- **Lineage kept rather than overwritten.** `part-2/` and `part-3/` hold frozen app snapshots at the state they shipped in, with a shared nav linking all three — so the earlier thinking stays openable instead of surviving only as a commit message.
- **A nested entry point**, `part-4/index.html`, which is what lets one vault hold four apps without one of them having to own the root.
- **The credential is derived.** It arrived as a vault key, was classified as a write credential before it touched anything, and only the one-way read key is published.

Ten screenshots, captured by driving the live vault from that published read key — no mock-ups.

It was written and pushed a day before it appeared here: [the tag gate](../updates/#an-ordinary-commit-should-not-be-able-to-take-the-site-down) had the deploy blocked.

### [An ordinary commit should not be able to take the site down](#an-ordinary-commit-should-not-be-able-to-take-the-site-down) [v0.2.40](../admin/versions.md)

cideployrelease

Two good commits landed on `dev` after v0.2.39 and sgit.ai served neither for a day. Nothing was wrong with either of them. The CI tag gate failed, and the deploy is gated on the tag gate.

- **What the error said, and what was actually true.** The job read `SITE_VERSION`, found `v0.2.39` already tagged on the *earlier* commit, and failed with *"SITE_VERSION was not bumped for this release."* But this was not a release — it was an ordinary commit on top of one. The message described a discipline failure where the real event was a category mistake in the check.
- **Why it became an outage rather than a warning.** The deploy job runs when `tag-release` is `success` **or** `skipped`. A *failure* is neither. So a missing tag — bookkeeping — silently became an unpublished site. Re-running could not help: the check is deterministic, and it failed identically on the second attempt.
- **The fix is to ask the right question.** What makes a push a release is now its **commit subject**, which is where `release.sh` already writes the version. No `site vR.M.N:` subject means an ordinary push: tagged nothing, published anyway.
- **And a commit that does claim a version is held to more than before.** The subject and `SITE_VERSION` must agree — previously that was only ever inferred, from whether the backfill loop had happened to produce the tag. The version must not already have shipped, and it must still be the next minor.

The asymmetry is the point, and it is written into the workflow so the next person changing it knows why: **a missing tag is a bookkeeping gap, a blocked deploy is an outage.**

Checked before shipping rather than after, by extracting the job's own script and running it over five cases in a throwaway clone: the exact commit that failed today now exits 0, a proper release tags, and subject/`SITE_VERSION` disagreement, a reused version and a skipped minor all still fail — each with a message that names what is actually wrong.

There was a quieter second consequence, and it is the one worth remembering. Those commits went to git only, so the vault remote never received them: `sgit status` showed all fifteen new files as uncommitted. Both stores are meant to move together, which is exactly [why CI does not author commits itself](../case-studies/one-tree-two-remotes.md) — a CI-written commit would exist on the git side alone. This release carries them across.

## 2026-08-21

### [A fourth sibling site — and the first one that links back](#the-first-sibling-that-links-back) [v0.2.39](../admin/versions.md)

networkgraphsmethod

[graphs.sgit.ai](../network/graphs.md) joins [the network](../network/index.md). It argues for a grammar of semantic graphs, from five rules you can apply tomorrow up to a full positioning against schemas and vector search — and it opens by disowning the product category a reader arrives expecting: *"this is not a graph database pitch… there is no graph database anywhere in the work behind this site."*

- **The thesis fits in two sentences.** Two nodes both hold `8080`. One is connected to a type, to a library, to a version; the other to nothing. *"The difference is not in the value. The difference is in the connectivity."*
- **The best argument needs no background.** 10,000 hours came from a 1993 violinist study where it was an *average*, not a threshold — and half the top group had not reached it. The corrections never attached: by then the claim had been carried through 242 papers and 200,000+ citation paths. A document cannot fix that. A graph can mark a claim superseded and make *"what did we build on this?"* a query.
- **`relates-to` is banned**, for a mechanical reason rather than a stylistic one: an edge with no verb carries no constraint, so it cannot narrow a traversal. It costs fan-out and buys nothing.
- **It separates ships from argues, and concedes the harder half** — *"this site's subject matter is almost entirely design"* — then lists what is running: the vault commit DAG, `*.link.json` cross-vault edges, the read-only query API handed to untrusted sandboxed apps, and a live typed property graph of 71 nodes and 141 edges across 107 issue files.

**It is the first sibling with a reciprocal link.** Its nav carries an `↗ part of sgit.ai` chip and its footer points back at this network page. Until now `/network/` was a one-way index.

Two build changes came with it. A site entry can now carry a `url:` that differs from its `domain:` — `graphs.sgit.ai` does not resolve yet, and an entry should link to the address that works rather than wait for the CNAME, so the page says which one it is instead of shipping a dead link. And the audit that comes with every network entry found one: the graphs site links to `sentinel.sgit.ai`, which does not exist. The site is `sg-sentinel.sgit.ai`; the `sg-` prefix is load-bearing.

## 2026-08-20

### [The audit that stopped a publication — and the vault we built instead](#the-audit-that-stopped-a-publication) [v0.2.37](../admin/versions.md)

vaultssecuritypublishing

A vault arrived for publication: the **EU AI Act as a citable graph** — 113 articles, 1,523 nodes, 1,944 edges, every node traced to hash-verified source bytes. Good demo, obvious yes.

It did not ship. The audit step — *open every file with the exact credential you are about to publish* — found a **live vault key in plaintext**, inside a handoff document, granting write access to a **different** vault. Publishing the read key would have handed that away to anyone who read the page.

- **Deleting the file would not have been enough.** Vault objects are content-addressed and immutable, so a credential committed once may stay reachable from history. The only clean remedy is history that never contained it.
- **So there is a new vault.** Same 206 files, two credentials redacted in place with visible `<VAULT-KEY-REMOVED>` markers rather than silent deletions, plus a `PUBLIC.md` stating what changed and why.
- **Re-audited from a fresh read-key clone**: 205 text files, zero findings. That is [Regulation Graph](../demos/vaults/regulation-graph/index.md), and it is live.

One rule got verified rather than assumed. The vault's Graph REPL is an LLM chat, and its code looks for an OpenRouter key at `/key.json` *inside the vault* before falling back to device storage — so a shipped key would be an open tab on somebody else's budget. There is no `key.json`, confirmed in the read-key clone. Bring your own key; nothing metered ships.

The rule that caught all of this came from the [Risk Graph Explorer](../demos/vaults/risk-graph-explorer/index.md) vault's own `PUBLIC.md`, not from us. It has now paid for itself.

### [A third sibling site — one that says, at the top of every page, that it does not exist](#a-third-sibling-site-that-says-it-does-not-exist) [v0.2.38](../admin/versions.md)

networkedgesecurity

[sg-sentinel.sgit.ai](../network/sg-sentinel.md) joins [the network](../network/index.md). It is a design for an app-coupled edge guard that replaces rented AWS WAF plus CloudWatch and Firehose with a layer you own — and its status pill reads `NOT BUILT` where its siblings read `MVP DRAFT`.

- **The inversion is the idea.** A generic WAF is blind to the app it protects, so it denylists known-bad and passes the rest. If you control both client and server, the edge knows the valid request space — so it can **allowlist**, and no invalid request reaches the origin.
- **One correction reshaped the design**, and it is stated as a governing constraint: *"Layer 1 never acts and never writes — it only decides and signals. Layer 2 is the sole actor and the sole I/O owner."* The reason is physical: a CloudFront Function has no network and no filesystem. The site names the earlier version — where L1 blocked inline — as a category error of its own making.
- **Rules are the engine, not configuration on it.** Six deterministic rules, each a pure function, each mapped to an ATT&CK technique, run in order with first-block-wins. The prototype ran the same engine across three targets with a parity matrix asserting identical decisions.
- **And it bounds its own evidence.** The prototype's testing manual reports 149 passing tests; the site immediately says *"not deployed anywhere, not in production use, not maintained, and not packaged for you to install."*

It is the third site here to publish a design **before** the thing exists — after [pki.sgit.ai](../network/pki.md)'s four registry rules. Same wager: publishing the design now is cheap, claiming it afterwards is impossible.

Adding it took one markdown file and three screenshots. The renderer gained pipe-table support on the way, since the six-rule core wanted a table and got a paragraph of vertical bars instead.

## 2026-08-19

### [The first two sibling sites, with screenshots](#the-first-two-sibling-sites) [v0.2.36](../admin/versions.md)

networkidentitypki

Two focused sites now run on `*.sgit.ai` subdomains, and [a network section](../network/index.md) covers both — what each argues, why it is relevant here, and screenshots of the real pages.

- **[nhi.sgit.ai](../network/nhi.md)** splits "how do I give my agents an identity?" into **agents you run** and **agents you rent**, and shows that everything on the market answers only the first. For rented agents — the ones in Claude, Codex, behind an API — the honest current answer is to hand over a broad credential and hope. Its sharpest idea is that **the real authorization is the closure**: inbox access is every account resettable by email.
- **[pki.sgit.ai](../network/pki.md)** designs a key registry from the 2019 keyserver catastrophe, publishing four rules **before the registry exists** so they stay checkable. The resolution it reaches is worth borrowing: append-only is safe when a writer appends only to objects it *owns*, and fatal when anyone may append to somebody else's. The rule to carry forward is not "append-only" — it is *the writer owns what it writes*.

Both connect directly to work here. Read keys and [append lanes](../api/append-lanes.md) are credentials with a provably bounded closure, which is the nhi problem stated as a mechanism; and an append lane is owner-configured, which is pki's rule 1 already shipped in another corner of the system.

More subdomains are coming. Adding one to this site is now writing a single markdown file and capturing its screenshots — the index, the cards and the page are all derived.

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
