# sgit.ai v2: transition plan, mapping and brief

**From:** the sgit.ai site agent (a Claude Code session), for Dinis Cruz
**Date:** 2026-10-11 · site v0.7.51 · sgit-ai 0.21.0 on PyPI
**Status:** PROPOSED. Nothing in this document has shipped. It is written into `admin/plans/` under the standing rule in `admin/brief-design-improvements.md`: structural changes are proposed here first and stop for human review.
**Companion:** `admin/plans/site-v2-page-map.md` holds the page-by-page, article-by-article and vault-by-vault mapping this brief summarises.

---

## 0. The ask, in one paragraph

The newsroom is moving to newsroom.sgit.ai. That is the trigger, not the task. The task is that sgit.ai was written for a product that no longer exists: most pages were built between 11 August and 20 September against sgit-ai 0.14 to 0.18, and the product in production today is 0.21.0, with scoped clones (`--path`), signed commits and tags, keyless mirrors, static publishing with an API spec, append lanes composed with PKI, and a key-management story that the articles of 8 to 10 October describe at a level the docs and homepage never reached. At the same time the newsroom grew to 74 articles and took the first slot in the nav and the second band on the homepage, so a developer arriving today meets an argument about journalism before they meet `pip install sgit-ai`. This brief proposes how to (1) unlink the newsroom without breaking a link, (2) re-state what sgit is from the shipped 0.21 surface, (3) rebuild the homepage, nav and docs for a developer who wants to point an agent at it, (4) reorganise 54 vaults by what they are examples of, (5) keep an sgit-specific journal on this site while the commentary lives on newsroom.sgit.ai, and (6) do it with visuals that are worth the money.

---

## 1. Historian: how the site got here, and what it recorded

The release log (`admin/versions.md`, generated from `VERSION_LOG`) records **313 releases in 61 days**, v0.1.1 on 11 August to v0.7.51 on 11 October. Read as eras, the site had four:

| Era | Releases | What the site was for |
|---|---|---|
| **v0.1.x** (11 to 14 Aug) | 27 | A vault app that was itself the website. 12 pages, the SG bridge, the in-browser terminal, the first `llms.txt`. The key leak on day two (v0.1.13) and the rules that came from it. |
| **v0.2.x** (14 Aug to 20 Sep) | 100 | Proof. Vault demos (v0.2.6), published vaults (v0.2.19), compare-as-tests (v0.2.24), the API section (v0.2.34), updates and articles (v0.2.35), the network of sibling sites (v0.2.36, 19 sites by v0.2.44), the homepage rebuilt "proof before mechanism" (v0.2.60), team and investors (v0.2.62), the vault mirror retired (v0.2.84), Fractal Semantic Graphs (v0.2.85 on). |
| **v0.3 to v0.5** (20 to 23 Sep) | 30 | House style and commerce. Em dashes banned (v0.3.0), startups (v0.4.0), OG images, bylines, about, partnerships (v0.5.7). |
| **v0.6.x and v0.7.x** (23 Sep to 11 Oct) | 156 | The newsroom. Business-plan vaults, the site's own agent and the Agent Contact protocol (v0.6.21), then from v0.6.85 the Newsroom: editor, front page, newsletter, subscribe, reading meter, personas, five readers, Stripe payments on newsroom.sgit.ai, and the brief to move it all (v0.7.37). 56 of the 74 articles were published in October. |

Two numbers explain the drift. First, **the product moved faster than the pages**: sgit-ai went from 0.14.27 (what the skills are verified against) through 0.15 (PKI), 0.16 (credential prefixes), 0.18 (scoped clones, 7 Oct), 0.20 (key management) to 0.21.0, while `docs/installation` still says "the current release is 0.18.0" and the homepage still says "sparse clones for fast cold starts". Second, **the newsroom grew faster than sgit's own story**: of 74 articles only 10 are about sgit itself, and no collection groups them.

What the site did right, and must keep: every page has a `.md` twin; every claim is checkable (the live vault behind it, the read key on the page, the release that shipped it); corrections sit above the mistakes they correct; publishing is adding one file; the validator refuses a vault key, an em dash and an unsourced absolute. The v2 site is a re-statement, not a rewrite. The method stays.

The record also contains the critique this brief repeats. `proof-behind-the-claim` (7 Sep) said the proof was two clicks behind the claim; `proof-moved-up` fixed it. One month on, the proof is still there but it is about the wrong product: the hero's "shipped as one string" is a statement about August's read-key handover, not October's scoped, signed, mirrored, lane-connected vault.

---

## 2. Architect: what sgit is, read from the 0.21.0 CLI

Installed from PyPI in this session (`sgit-ai v0.21.0`, 36 top-level commands, `sgit help all`). This is the capability map the site should be organised around. Items marked ✦ are **not on the site at all today**; items marked ◐ are documented but absent from the homepage, `/why` and `/compare`.

### 2.1 The layers

1. **The vault and its keys.** One string is the address, the write authorisation and the key. A read key is derived one way (`vault derive-keys`). Five credential prefixes. Keys live in a local store (`vault add/list/show`), can be rotated (`vault rekey`), moved with the vault (`vault move`), backed up (`vault backup`), and bound to a bare checkout that arrived by git (`vault attach` ✦).
2. **Version control like git.** No staging area; commit snapshots the folder. `history log/diff/show/revert/reset`, plus `reflog` and `undo` ✦. `branch new/switch/merge/checkout`, `vault stash`, `commit --amend` ✦, `push --force-with-lease` ✦ with `pull --accept-rewind` ✦. The two-branch model (a private clone branch per machine or agent, shared named branches) and a real three-way merge with `resolve --show`.
3. **Clone exactly what you need.** `clone --path FOLDER` (repeatable): "other folders are carried by id and never downloaded; commits and pulls touch only the held folders"; widen with `fetch <folder>`. `clone --depth N` with `fetch --unshallow`. `--sparse` structure-only clones with content on demand. `clone-branch`, `clone-headless`, `clone-range`. Measured on 0.18: 80 s / 173 MB for the whole vault, 14 s / 3.2 MB for one folder. ◐ This is the feature Dinis names as the one that makes the cost of a vault grow with what you need rather than with what exists, and it is the headline of the latest release. The homepage does not mention it.
4. **Agent plumbing.** `sgit write <path> --file --message --push --json --also` (one call: encrypt, commit, push, machine-readable result). `cat`, `ls --json`, `history --json`, `doctor --json`. `cache add/rm/status/repair` ✦ ("declare cached paths, fast single-request reads"). Agents sharing one vault: pull keeps uncommitted edits, `push --branch-only` for WIP, `check upload-objects` for recovery. 16 parallel connections and 429 retry.
5. **Messaging without accounts.** Append lanes (HTTP `append/write|list|fetch|mark-processed|purge`): a write-only address that anyone can post to blind, that the vault owner drains. Composed with `sgit pki` (RSA-OAEP 4096 encrypt, ECDSA P-256 sign) it is signed, encrypted vault-to-vault mail, and the Agent Contact v0.1 protocol at `/.well-known/sgit-agents.json` is built on it. ◐ On the homepage only as one vault card.
6. **Publishing without a server.** `publish --visibility bare|named|public --bundles --api-spec --api-docs` ✦ generates a plaintext surface for static hosting, with an OpenAPI description of the folder; `vault serve` ✦ serves it locally; `clone --transport static` ✦ clones from any plain GET host (GitHub Pages, S3) and `--transport local` from a folder; `vault mirror` ✦ copies a published vault you cannot read, "custody without access, keyless, verifiable". The site itself is the proof: it is served from GitHub Pages and reads vaults with CORS GETs and Web Crypto in the tab.
7. **Integrity you can check.** `check verify` ✦ verifies the ECDSA signature on every commit reachable from HEAD. `vault tag create/show` ✦ are named, signed release pointers. `vault format --set 2 --min-client --feature signatures-required` ✦ is a format gate per vault. `check fsck` verifies and repairs. `inspect vault/tree/object/stats/ignored/diff-state` ✦ is a read-only toolkit.
8. **Run it where you like.** `--base-url --token` against your own SG/Send server (Docker `sg-send-vault`, Compose, Kubernetes, with NetworkPolicy); named remotes with `push --remote backup`; two servers, one vault; restore by push. ◐
9. **Apps and pages inside the vault.** A vault can carry its own sandboxed app (`.vault/app.json` with declared permissions) and `_page.json` content; the `window.sg` bridge; sub-vaults as link files (browser only today).
10. **One tree, two version-control systems.** A git repo and an sgit vault in the same folder (`.gitignore`/`.gitattributes` pattern), which `vault attach` now completes: clone the git repo, attach the key, and the vault is live. ◐

### 2.2 What git does not have (the honest list)

The site must keep conceding where git wins (scale, ecosystem, CI, bisect/blame/rebase, partial commits, revocation, key recovery; `/why` and `/compare` already do). But the list on the other side has grown since `/why` was written, and the new entries are the ones a developer running agents cares about:

| sgit has it | git / GitHub |
|---|---|
| A host that cannot read filenames, structure, commit messages or branch names | git-crypt, SOPS, age leave all four readable |
| A clone whose cost is the size of the folder you asked for, where commits and pulls touch only that folder, so two agents in two folders never conflict | sparse checkout still fetches the objects; shallow still fetches every file at HEAD |
| A read capability that is one string, works against any server, needs no account, and can be printed on a web page | deploy keys are per host and per account |
| A write-only address (append lane) that anyone can post to and only the key holder can read | nothing; you need an account and a PR, or a webhook with a server behind it |
| A published surface that any GET host can serve and any client can clone, mirror and verify without the key | GitHub Pages serves plaintext; a mirror needs read access |
| Signed commits verified by one command across the whole history, and a per-vault gate that refuses unsigned ones | commit signing exists; "verify all history" and a per-repo gate do not come built in |
| Custody of a vault you cannot read (`vault mirror`), verifiable | no equivalent |
| Private data with public-CDN economics: content-addressed ciphertext cached forever by caches that cannot read it | private repos are not cacheable by third parties |
| Vault apps: the viewer travels with the data, with declared permissions | no equivalent |

This table is the spine of the new `/why` and the new `/compare` entries. Every row needs the command and, where one exists, the vault that proves it.

### 2.3 What the architect could not verify from here

- There are **no release notes for 0.19, 0.20 or 0.21** anywhere in the repo. The site's newest release page is `docs/update-to-0-18-0`. I have the 0.21 `--help` text but not the changelog. **Ask:** a pointer to the CLI repo's release notes, or a pasted changelog, so the "update to 0.21" page and the new feature pages are grounded in what changed rather than in what `--help` says exists.
- `clone --bare` says "full implementation in B09; currently stubs". `vault mirror`, `vault tag`, `check verify`, `vault format`, `cache` and `--transport static` are shipped in the CLI; whether each is production-tested I cannot tell. Every new page should say which release it was verified on, as the key-management page does.
- Every vault link on the site points at `dev.vault.sgraph.ai` / `dev.send.sgraph.ai`. That is a dependency on a dev host for a production site and the brief does not change it, but it should be a conscious decision.

---

## 3. Ambassador: positioning for v2

### 3.1 Who the homepage is for

One reader: **a developer who runs agents and wants to know in ninety seconds whether to point them at sgit.** Not a journalist, not an investor, not a CISO (they each keep a door, below the fold or one click away). The test for every homepage band: does it move that developer closer to `pip install sgit-ai` and a first `sgit create`, or to handing the skill to their agent?

### 3.2 The claim

Working title, two candidates, for Dinis to pick or redirect:

- **A.** "Encrypted memory for agents, versioned like git." Sub: "A vault is a folder your agents clone, commit and push, scoped to the part they need, on a server that cannot read it. One string to hand over. No account for the reader."
- **B.** "Git for what you cannot put on GitHub, built for agents." Sub: "Scoped clones, signed history, write-only lanes and apps that ship inside the data. The server stores ciphertext and nothing else."

A is the recommendation. It names the job (memory for agents), the mechanism (git), the new differentiator (scoped) and the old one (cannot read it) in two sentences, and "A vault is a folder" is already the site's best line (`docs/agents`). B reads better as the `/why` title.

### 3.3 The homepage in order (proposed)

| # | Band | Content | Why it is here |
|---|---|---|---|
| 1 | **Hero** | Claim A. CTAs: `pip install sgit-ai` (copy), "Point your agent at it" (skills), "Open a real vault". Eyebrow keeps "Pure Python · two runtime dependencies · Apache-2.0 · 0.21.0". | The claim, the install, the proof, in one screen. |
| 2 | **Ninety seconds** | A three-step strip with real output: `sgit create` → hand the skill to an agent → `sgit clone --path notes/` on the other side. Then `sgit write ... --json`. | The developer's path, before any argument. |
| 3 | **Clone what you need** | The `--path` story with the measured numbers (80 s / 173 MB vs 14 s / 3.2 MB), one diagram (section 7, V1). "Other folders are carried by id and never downloaded." | The feature that changes the cost model; new to the site. |
| 4 | **What people ship** | The existing jobs band, re-picked so each of the eight categories in section 5 has one vault. | Proof, already working. |
| 5 | **Built for agents** | Rewritten: memory that survives the context window; a branch per agent; agents sharing one vault safely (pull keeps edits); write-only lanes to talk to each other; the Agent Contact file. One diagram (V2). | The audience's own case. |
| 6 | **Under the hood it is git** | The terminal tabs, kept, re-recorded on 0.21: add a "Scoped" tab and a "Verify" tab (`check verify`, `vault tag`). | Muscle memory. |
| 7 | **What the server sees** | Kept as is; it is the signature visual. Redraw as one inline SVG per the standing design brief. | Zero knowledge, unchanged. |
| 8 | **Publish without a server** | New: `publish`, static transport, mirror, this very site. One diagram (V3). | The second new differentiator. |
| 9 | **In production, honest** | Kept: tests, mutation testing, limitations, security model. Add "verified on 0.21.0, 11 Oct". | Trust. |
| 10 | **Read more** | Three cards: the sgit journal on this site (section 6), the newsroom at newsroom.sgit.ai, the network. | Where the arguments went. |
| 11 | **Closer** | Install, quickstart, GitHub. | |

Removed from the homepage: the full newsroom band (replaced by one card in band 10), the "nineteen sites" band (moves to `/network`, which is one card in band 10), the Fractal Semantic Graphs band (it is one of the eight vault categories in band 4 and keeps its own section).

Fixed on the homepage in the same release, because they are wrong today: "Twenty-five real vaults" in the description (54), "Nineteen sites" (27), "sparse clones" (scoped clones), 0.18 examples.

---

## 4. Cartographer: the new site map

### 4.1 Nav (proposed)

Today: Newsroom · Why · Docs · Vaults · Agents · Evidence · Team · Network · Security. Proposed, nine groups kept to nine so nothing wraps on a laptop:

1. **Start** → `/docs/quickstart`. Children: Install · Quickstart · For git users · Point an agent at it (skills) · Try in the browser · Update to 0.21.
2. **Docs** → `/docs/`. Children: Documentation · CLI reference (new, generated) · Agents · Scoped clones · Messaging and lanes · Keys and credentials · Publishing and static hosting · Integrity (signing, tags, verify) · Self-host · HTTP API · SG/Vault and vault apps · Briefs.
3. **Vaults** → `/demos/vaults/`, reorganised by category (section 5). Children: By what they show · All 54, sortable · Fractal graphs · Catalogue · Performance and cost · Publishing method.
4. **Why** → `/why/`. Children: Why sgit exists · sgit vs git · Comparisons as tests · Case studies · Lessons · Use cases.
5. **Journal** → `/articles/` (sgit-specific, section 6). Children: Latest · Release notes · Architecture · RFCs · Subscribe.
6. **Agents** → `/agents/` (the contact directory; unchanged).
7. **Network** → `/network/`.
8. **Team** → `/team/` (roles, board, versions).
9. **Security** → `/security/`.

**Newsroom** leaves the nav. It stays reachable from: the footer ("The SGit Newsroom, now at newsroom.sgit.ai"), band 10 on the homepage, `/articles/` (a banner, see section 6), `/publishers/`, and every moved article page (a notice at the top). Nothing 404s.

### 4.2 Sections that change, in one line each

Full table in the page map. Headlines: `/docs/` is re-cut around the ten layers in section 2.1 with eight new pages and six refreshed; `/demos/vaults/` gains a categorised landing page above the sortable table; `/why` and `/compare` gain the sgit-vs-git rows; `/use-cases/` is folded into `/why` and the vault categories (its `--sparse` example is wrong on 0.18+); `/skills/` is rebuilt from 0.21; `/account/`, `/subscribe/`, `/meter/`, `/newsroom/` and the newsroom children of `/articles/` are frozen (no new content, a notice on each) until cutover under the existing move brief; `/publishers/` stays as the door to newsroom.sgit.ai; `/startups/`, `/investors/`, `/partnerships/`, `/summit/` stay as they are, reachable from `/why` and the footer.

---

## 5. Publisher: the vaults, organised by what they are examples of

The 54 published vaults (plus `aiuc-1-graph`, which has a page but no row in `vaults.json`) are today sorted by shape (Reference 20, Briefing 13, Analysis 10 ...). Shape is how a librarian files them; a developer asks "show me one for X". Proposed: add `use_case` (one of the eight below) and `shows` (the sgit features demonstrated) to `vaults.json`, as `docs/briefs/vault-map-infographic` already proposed, and build a landing page with eight cards, each "If you want to see a vault for X, open this one", with the rest listed under it.

| Category | The one to open first | Why | Also |
|---|---|---|---|
| **Agent memory and agent teams** | `deploy-docs` (two Claude sessions writing one vault, rendered live on `/deploy`) | the simplest proof that state survives the session | `risk-mandate` (an agent's workspace, 98 commits), `board`, `agent-desk`, `article-views` |
| **Messaging and lanes** | `lesson-loop` (write-only lanes per coach into a record the player holds) | the clearest working lane | `agent-permission-games` (append-lane telemetry, honest that it is not yet succeeding), `connector-twin` |
| **Publishing and newsrooms** | `evidence-dispatch` | a whole newsroom with an evidence graph | `bridge-simulation`, `local-evidence-log`, `how-much-evidence`, `infographic-bakeoff`, `catalogue` |
| **Policies, standards and governance** | `aiuc-1-conformance` (hero #1 today) | `evidenced_by` vs `attested_by` is the idea | `regulation-graph`, `standards-atlas-gdpr`, `pci-dss-graph`, `aibcf-graph`, `ai-governance-graph`, `dsit-ai-risk-toolkit`, `licence-to-operate`, `hope-or-enforcement`, `agency-scale`, `aiuc-1-graph` |
| **Security and pentest** | `pentest-report` (8 audience views, a retest script per finding) | hero #4 today, the handover case | `agentic-browser-isolation`, `content-transformation-proxy`, `threat-sized-security`, `threatmodcon-2025` |
| **Health and personal records** | `health-score` (one vault, three audiences, rules as versioned data) | a full clinical workflow | `supplement-stack`, `kit-bag` |
| **Documents, decks and handover** | `payments-brief-pack` ("the vault as the unit of handover") | one credential moves the whole pack | `interim-ciso-pack`, `fractional-ciso-pack`, `commercialisation`, `blackhat-eu-2025`, `voicedebrief-pitch`, `deck-vault`, `algarve-may-2026` |
| **Developer tooling and graphs** | `vault-app-pocs` ("read first if you are going to build one") | the guide for app builders | `code-review-graphs`, `field-notes`, `strategy-maps`, `voice-debrief`, the nine fractal-graph vaults, `synthetic-users` ×3, `risk-graph-explorer`, business plans (`agent-webmaster`, `risk-acceptance`, `company-xray`) |

**Gaps the vaults do not cover, which the v2 homepage will claim.** There is no published vault that demonstrates: a scoped clone (`--path`) side by side with a full one; signed commits and a signed tag (`check verify`, `vault tag`); a keyless mirror; `publish --api-spec` served from GitHub Pages and cloned with `--transport static`; an inbox / email-fs vault (the articles describe it, no vault shows it); a sub-vault. Each is one small vault and one page, and each closes a "show me" the new homepage opens. Proposed as five new vaults (section 9, phase 3).

**Housekeeping in the same phase:** add `aiuc-1-graph` to `vaults.json`; replace every hard-coded count ("Thirty at the last count", "8 vaults", "nine entries") with a derived number; decide what to do with the catalogue vault (9 of 54 entries, only the key holder can update it): refresh it or retire the page to a redirect to the gallery.

---

## 6. Journalist and Historian: the articles

### 6.1 The split

74 articles. By the inventory in the page map: **10 are about sgit itself**, **13 are sgit case studies that double as commentary**, **51 are commentary** (agent behaviour policy, RiskMandate, news, the meter, personas).

The existing move brief (`docs/briefs/newsroom-move-to-newsroom-sgit-ai`, decided 10 October) says *everything* under `/articles/` moves, "articles about sgit itself (for example what sgit is) move with the rest, and sgit.ai links to them". This brief proposes the opposite for the 10, and asks for the decision to be revisited:

- **S (10): stay canonical on sgit.ai, under `/articles/`, re-framed as the sgit journal.** `what-sgit-is`, `encrypted-memory-for-isolated-agents`, `where-the-vault-keys-live`, `rfc-0001-public-key-cryptography-for-sgit`, `seven-vaults-one-method`, `green-does-not-mean-live`, `nineteen-sites`, `chat-on-a-static-site`, `proof-behind-the-claim`, `proof-moved-up`, plus the 0.18 update page already under `/updates/`. A reader of sgit.ai who wants the architecture should not be sent to a newsroom to read it.
- **B (13): canonical on newsroom.sgit.ai, cross-linked from the sgit.ai page they prove.** `no-server-by-design` from the publishing docs; `the-identity-we-wanted-to-give-the-agents` and `a-mac-of-the-agents-own` from key management; `the-agent-team-as-it-runs`, `the-mandate-stack`, `why-my-agents-do-not-run-on-my-laptop`, `memory-is-not-a-spectator-sport`, `how-i-work-with-claude` from the agents docs; `custom-uis-are-not-the-exception`, `replicating-the-agentic-inbox` from messaging; `a-personal-agent-that-keeps-your-secrets`, `the-deck-i-could-not-download`, `supply-chain-of-vaults` from the vault categories.
- **N (51): move, per the existing brief.** Stub with canonical and forward at cutover.

Mechanically this needs one new front-matter key, `home: sgit | newsroom | both` (today `content.py` has no such field and `build_pages.py` hard-codes `canonical` to sgit.ai for every page), and the build uses it to set the canonical, the notice banner and which index the article appears in.

### 6.2 The sgit journal

What `/articles/` on sgit.ai becomes: **sgit-specific news and guidance only**, in four lanes, each a tag the build understands:

1. **Release notes.** One per CLI release, from 0.18 forward, back-filled for 0.19, 0.20 and 0.21 as soon as the changelog is available. The `/updates/` section already has the shape (`v0.6.83__update__sgit-ai-0-18-0.md`); the journal gives it a front page.
2. **Architecture.** The flow articles: how a scoped clone works, how a lane is drained, what a signed tag proves, what the server sees under `publish`. Each with one diagram and one vault.
3. **RFCs.** RFC 0001 and whatever follows, with the "nothing is built" status line kept honest.
4. **Field notes.** What running sgit in production taught (the lessons page has the first ten).

Pace: not the newsroom's. One good piece per release or per feature, not eight a day.

### 6.3 Transition without breaking a link

Three steps, each a release, each reversible:

1. **Unlink (phase 1).** Newsroom leaves the nav and the homepage band. A one-line banner on `/articles/`, `/newsroom/`, `/account/`, `/subscribe/`, the newsletter and every N or B article: "This article is part of the SGit Newsroom, which now lives at newsroom.sgit.ai. This copy stays for links." Footer gets the newsroom link. Nothing moves, nothing 404s, the feeds keep working.
2. **Canonical switch (the existing brief's phase 4).** Once newsroom.sgit.ai serves the same paths (its synthetic-user run on 10 Oct found 51 of 527 figures missing, so it is close but not there), set `home:` per article and let the build point canonicals at newsroom.sgit.ai for N and B. The `/articles/` index on sgit.ai shows S only, with a card for the rest.
3. **Cutover (phase 5 of the existing brief).** Stub plus meta-refresh for N; B keeps a stub too; S stays. `/account`, `/subscribe`, `/meter` follow the existing brief's decisions (storage key, Stripe redirect, meter docs).

---

## 7. Designer: visuals and infographics

The standing design brief (11 August) is still open on every point: no wordmark, a text-only hero, the server-sees diagram as two lists, no 360 px pass on record. v2 is the moment to close it, within the same constraints (inline SVG only, system fonts, no external resources, no emoji).

### 7.1 Diagrams that must be exact (inline SVG, drawn by hand, no generation)

These carry claims, so they are built as accessible SVG with real text, one source file each under `admin/build/diagrams/`, inlined by the build:

- **V1 Scoped clone.** Left: the vault tree with five folders, sizes. Right: a `--path notes/` clone holding one folder and four ids. Arrow labelled "14 s · 3.2 MB" against "80 s · 173 MB". Homepage band 3, `docs/partial-clones`.
- **V2 Agents sharing one vault.** Three agents, three clone branches, one named branch, a human at the merge; a dotted lane from agent C into the vault's append lane. Homepage band 5, `docs/agents`.
- **V3 Publish without a server.** `sgit publish` → a folder of ciphertext plus `api/openapi.json` → GitHub Pages / S3 → a browser decrypting in the tab, a `--transport static` clone, and a `vault mirror` that never gets the key. Homepage band 8, the publishing doc.
- **V4 What the server sees.** The existing two lists redrawn as one SVG (padlock, arrow, ciphertext ids), per the standing brief.
- **V5 The key family.** Vault key → read key (one way) → write key, append token, enum key; what each can do; which prefix each carries. Key-management doc, credentials doc.
- **V6 A lane, end to end.** Sender's `pki encrypt` + `sign` → `append/write` with the public token → the owner drains, verifies, marks processed, purges. Messaging doc, `/agents`.

### 7.2 Images worth generating (infographic-gen, ~$0.07 each)

For article covers, OG cards and the journal, where a picture sets a tone rather than carries a figure. The bake-off vault (10 Oct) already picked the models per job; the brief does not re-run it.

| # | Image | Where | Prompt sketch (dark navy, teal accent, no text in the image) |
|---|---|---|---|
| I1 | The vault as a folder an agent carries | hero background, faint | a single folder outlined in light, inside it smaller folders, one lit, the rest as hashes |
| I2 | Scoped clone | journal cover for the `--path` article | a large tree, one branch fetched in colour, the rest as faint ids |
| I3 | A server holding ciphertext | security, OG for `/security` | a rack of boxes with only hashes printed on them, one key held outside the frame |
| I4 | A lane | OG for `/agents` | a letterbox slot in a wall, sealed envelopes going in, one reader behind |
| I5 | Signed history | OG for the integrity page | a chain of commits each with a wax seal; one tag flag |
| I6 | Mirror without a key | OG for the publishing page | two identical shapes, one solid, one glass, no key between them |
| I7 | Eight categories | the vaults landing page header | eight small tiles: a report, a graph, a deck, a record, a folder, a game, a letter, a map |
| I8 to I11 | Journal lane covers (release notes, architecture, RFCs, field notes) | the journal index | one motif each |

Eleven images, about $0.80. Plus two decks if wanted (6 to 9 slides each, about $0.56 per deck): "What sgit is, in nine slides" for the journal and LinkedIn, and "Scoped clones" for the release-notes post. Total under $2.50. The generation needs an OpenRouter key, which this session does not hold; the prompts above are ready to run in a session that has it.

### 7.3 Design pass checklist (from the standing brief, unchanged)

Wordmark and mark · hero visual that does not push the terminal below the fold · typography rhythm · the V4 redraw · 360 px pass with screenshots in the release · contrast on `--dim` and the terminal caption · focus states · optional dark mode in the token layer. Each is a release; screenshots via sg-playwright go into the debrief.

---

## 8. Developer and release engineer: what changes in the build

- `admin/content/vaults.json`: add `use_case` and `shows`; `_vaults()` renders the categorised landing; the jobs band picks one per category.
- `admin/build/content.py`: allow `home:` on articles; `build_pages.py` uses it for canonical, banner and index membership; `LIST_KEYS` gains `shows` if vaults move to front-matter later.
- `NAV` in `build_pages.py`: the nine groups in section 4.1. `footer()`: the newsroom link, the journal link.
- Derived numbers everywhere a count is typed today (vaults, sites, articles, releases, tests). The validator gets a check for a bare number next to "vaults" or "sites" in page source.
- A **CLI reference generator**: `sgit help all` plus `sgit <cmd> --help` for every command, rendered to `docs/cli/<command>.html` with `.md` twins, run at release time against the pinned sgit-ai version, with the version printed on every page. This closes the "coming next: a full per-command CLI reference" promise on `docs/index` and keeps the docs from drifting again.
- `release.sh`: record the sgit-ai version the release was verified on (`sgit version`) in `VERSION_LOG`, next to the git ref.
- `skills/`: regenerate the three skill files from 0.21 (the installed skill and the repo skill both predate `--path`, `write`, lanes and `history`; the installed one says object ids are SHA-256 of plaintext, which the site contradicts). Mark the share-token commands as retired or document them: the 0.14.27 skill says `share send/publish` are disabled and the site has no page either way.
- Diagrams: `admin/build/diagrams/*.svg` inlined by a `<!--SVG:name-->` marker, validated for real text.

---

## 9. The plan, as releases

Each phase is one or more site releases in the existing convention (`site vX.Y.Z: ...`, build, validate, push to `dev`, verify live). The minor bumps to **v0.8.0** at phase 1 to mark the structural change, as v0.2.0 and v0.7.0 did. Every phase stops for Dinis's review before the next starts; phases 2 to 6 can run in parallel sessions once phase 1 has landed, because they touch different files.

| Phase | Releases | What ships | Depends on |
|---|---|---|---|
| **0. Decide** | 0 | This brief, the page map, the decisions in section 10. | Dinis |
| **1. Unlink and tell the truth** (v0.8.0) | 2 to 3 | Newsroom out of the nav and the homepage band, banners on, footer link in. Counts derived. Homepage, installation and update pages say 0.21.0; `--sparse` in use-cases becomes `--path`; "sparse clones" becomes "scoped clones". `aiuc-1-graph` in `vaults.json`. | nothing |
| **2. Re-state** | 3 to 4 | New hero and homepage order (section 3.3), new `NAV`, `/why` rewritten around section 2.2 with the compare rows, V1 to V4 drawn. | 1 |
| **3. Vaults by example** | 3 to 5 | `use_case`/`shows` fields, the categorised landing, the five gap vaults (scoped clone, signed tag, mirror, static publish, inbox) published by the seven-step method, catalogue decision. | 1 |
| **4. Docs for 0.21** | 4 to 6 | CLI reference generator and pages; new pages for scoped clones (refresh), integrity, publishing and static hosting, cache, `vault attach` and one-tree-two-systems; refreshed installation, agents, agents-sharing, key management, messaging; `update-to-0-21`; skills regenerated; V5 and V6. | changelog for 0.19 to 0.21 |
| **5. The journal** | 2 to 3 | `home:` key, the S/B/N split applied, the journal index with four lanes, release notes back-filled, canonical switch for N and B when newsroom.sgit.ai is ready. | 1, Dinis on 6.1, newsroom.sgit.ai |
| **6. Visuals** | 2 to 3 | I1 to I11 generated and placed, the design-pass checklist, screenshots at 360 px in the debrief. | an OpenRouter key; 2 |
| **7. Cutover** | 1 to 2 | Stubs and forwards per the existing move brief; `/account/move.html`; nav, feeds and sitemap final. | 5, newsroom.sgit.ai phases 3 and 4 |

Roughly 17 to 26 releases. At the site's recorded pace (313 in 61 days) that is days, not weeks; the gating item is the human review between phases and the two external inputs (the CLI changelog, the OpenRouter key).

---

## 10. Decisions needed from Dinis

1. **The claim.** A or B in section 3.2, or a redirect.
2. **The 10 sgit articles.** Stay canonical here (this brief) or move with the rest (the 10 October brief). The two cannot both be true.
3. **The nav.** Nine groups as in 4.1; in particular, "Journal" as the name for sgit-specific articles, and "Start" as the first group.
4. **The five gap vaults.** Build them (phase 3) or claim only what existing vaults show.
5. **The catalogue vault.** Refresh (needs its write key in a session) or retire the page.
6. **Dev hosts.** Keep `dev.vault.sgraph.ai` / `dev.send.sgraph.ai` on every vault link, or move to production hosts as part of phase 3.
7. **Share tokens.** Document `share`/`publish`/`export` as they stand on 0.21 or state that the share-token path is retired; the site is silent today and the old skill says disabled.
8. **Money.** Approve about $2.50 of image generation (section 7.2) and provide the OpenRouter key to the session that runs phase 6.
9. **Inputs.** A pointer to the 0.19 to 0.21 changelog (or the CLI repo) for phase 4.

---

## 11. What this brief did not do

It did not edit a page, bump the version or touch `vaults.json`. It installed sgit-ai 0.21.0 from PyPI in the session container to read the command surface; nothing was cloned and no key was used. It did not fetch newsroom.sgit.ai, so the statement that the newsroom side is "close" rests on the 10 October synthetic-user run recorded on this site. It did not re-run the infographic bake-off. It did not talk to the SG/Send team agents; the "Architect" voice in section 2 is this session reading `--help`, and should be checked by whoever owns the CLI.
