# Updates — sgit.ai

> What changed on sgit and on this site, as it happens — one entry per story rather than per release, each linked to the release that carries it. RSS and JSON feeds included.

*Source: <https://sgit.ai/updates/index.html> · site v0.2.65 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

# Updates

What changed on sgit and on this site, as it happens — one entry per story rather than per release. The [version log](../admin/versions.md) is the complete technical record; this is the readable one.

Follow along: [RSS](feed.xml) · [JSON](updates.json). Every entry links to the release that carries it.

## 2026-09-09

### [Seven shorts on the Licence to Operate vault — indexed, and put in the right order](#seven-shorts-on-the-licence-to-operate) [v0.2.65](../admin/versions.md)

vaultsvideoagentsrisk

The author recorded seven vertical videos walking through [the Licence to Operate vault](../demos/vaults/licence-to-operate/index.md). None of them was on the site. [They now have a page](../demos/vaults/licence-to-operate/videos/index.md), collected in the order they are meant to be watched rather than the order a feed shows them:

- **The mechanism** (1–3) — grant against mandate, what a block looks like when an agent exceeds its mandate, and how risk cascades from the support team to the CFO.
- **The artefact** (4) — how to find and open the vault. The shortest one, and the one to send someone who wants to poke at it themselves.
- **The model** (5–7) — why the grant/mandate gap is where risk lives, the insurance framing that governs it, and the policy, claim and premium mechanics underneath.

Each carries the author's own description plus a line mapping it to what it demonstrates: the **delta** for 5, [the AIUC-1 conformance layer's](../demos/vaults/aiuc-1-conformance/index.md) insurability query for 6, and risks.sgit.ai's *there is no deny button* for 7.

**What the page refuses to pretend.** These are descriptions, **not transcripts**. All four of YouTube's `timedtext` endpoints return empty for every one of the seven, so there is no caption track to pull — and the words actually spoken are absent from this site, from `llms-full.txt`, and from the chat pane's `read_page` tool. That is precisely the failure [the Risk Graph Explorer walkthroughs](../demos/vaults/risk-graph-explorer/videos/index.md) page was built to avoid, so the gap is stated in a box at the top, measured rather than guessed, and opened as board card T12.

**A number that cannot rot, demonstrated by accident.** Video 4 tells the viewer to look for *"Vault #23"*. Checked against the table: Licence to Operate is still #23, and always will be — v0.2.58 made that column a permanent publication ordinal rather than a row position. A recorded video naming a row number would have been wrong within a day. Naming an identity is safe, and this is the first time that decision has paid for itself.

Embeds go through `youtube-nocookie.com` with `loading="lazy"`, so opening the page sets no YouTube cookie until somebody presses play. The players needed new 9:16 CSS — the existing embed box is 16:9, and a Short in it is two black pillars.

## 2026-09-07

### [Two new sections — the team, written for the agents; and investors, in the open](#the-team-for-the-agents-and-investors-in-the-open) [v0.2.62](../admin/versions.md)

teamagentsinvestorsboardmethod

**[The team](../team/index.md)** is the agentic section: how this site is run by one person and a team of AI agents, written for the agents. A new agent should be able to read that page and one role page and begin.

- **Nine roles, each a file.** Sherpa, Publisher, Auditor, Journalist, Cartographer, Ambassador, Designer, Release engineer, Historian — mirroring the Explorer team in the CLI repository, specialised for running a site rather than building a tool. Each page carries the role's mission, what it owns and must not touch, the files it works in, the checks it runs, **the rules it enforces with the mistake that produced each one**, and the prompt that starts it from nothing. The Publisher and Auditor exist because this site publishes read keys on purpose and has to be certain what they reach.
- **[Twelve starting prompts](../team/prompts.md)** for the work that recurs — publish a vault, audit it, write the update, write an article, add a sibling site, handle an inbound brief, cut a release, fix a phone bug, turn markup into data, correct a claim, update the board, re-verify the read keys. Each is written to be pasted into a fresh agent, and each ends before the release step on purpose: the release engineer's prompt is the one that ships, and the Sherpa decides when it runs.
- **[The board](../team/board.md)** is a kanban of files. Each card is a markdown file with a `status` line; the five columns are those lines rendered. **Needs** — items only the author can supply — are kept apart from tasks and never discovered late. This follows issues-fs.sgit.ai's *issues are files* and the open comms board on open-source.sgit.ai. It is seeded with the real open work, including six things only the author can answer.

**[Investors](../investors/index.md)** follows the founder's practice of publishing investor material in the open, and the structure of the pitch his other companies publish: the problem, what it is, the open-source zero-knowledge architecture, traction, business model, the beachhead market, what could go wrong, and the materials. Two rules hold it honest:

- **Traction is computed from the site**, with the same generator the homepage team band uses. If a number is wrong, the site is wrong somewhere else too.
- **The ask is left visibly open.** Round size, instrument and use of funds are the founder's to state; the page has a dashed box saying so and tracks it as board item N1 — rather than a number nobody supplied.

The business-model section does not restate the founder's position on open source; it points at it through the new sibling-site card, so the argument is read in its own words.

**Nav:** *Try* folds into Docs; *Why* becomes a group with Investors; *Team* is new. Eight top-level items, as before.

One build lesson, recorded because it bit twice: angle-bracket placeholders inside code spans broke the markdown twin while being regex-wrapped. The whole team section now uses `UPPERCASE` placeholders with no angle brackets — one convention that survives every renderer this site has.

### [The proof moved up — the homepage, rebuilt to show vaults before it explains them](#the-proof-moved-up) [v0.2.60](../admin/versions.md)

homepagepositioningvaultsagents

The homepage is rebuilt, following [the diagnosis published this morning](../articles/proof-behind-the-claim.md) rather than a fresh opinion — and [the "after" article](../articles/proof-moved-up.md) puts each new band beside a screenshot of what it replaced, so the comparison is honest rather than flattering.

**The first screen now shows vaults.** The headline changed from *"the encrypted git for humans and AI agents"* to *"a vault is a unit of work: data, app, history and sources, shipped as one string."* Encryption did not leave — it became the subordinate clause, which is where a property nobody can look at belongs. Under it: **four real published vaults**, a screenshot each, one click from open. Which four is a field in the vault data, so changing the front door is a data edit.

**The use cases became things.** A new band, *what people actually ship*, replaces five category cards with six vaults chosen by the job they do — hand over a report, publish a standard as data, give a talk, pitch an investor, ship a game that reports back, give an agent a workspace — each with one line on why it is hard any other way. None of those lines is about encryption.

**The collaboration story got a front door.** *One human, a team of agents*: four numbers computed at build time — releases, vaults, sibling sites, cross-team briefs — and the loop told in three beats with the artefacts linked. The numbers are not typed here or on the page, and this sentence deliberately does not repeat them: the first draft did, and was off by one within the hour because a release had happened. The tile cannot drift; prose can.

**Cut:** the abstract use-case band (the pages remain, in the nav) and the *three doors* band (now one pill in the trust strip). **Moved down:** the terminal walkthrough, under *Under the hood, it is git*, because for a visitor who has just opened a real vault, *how* is now the question. The band count is unchanged — nine before, nine after; three cut, three added — so what changed is the order and the first screen. The page got longer in bytes, because ten screenshots replaced paragraphs, and shorter in words.

**One thing the computed number caught.** The network heading had been retyped as "Twenty sites" while the tile beside it said 19. The tile was right — nineteen siblings, twenty with this one — and it is the tile that cannot drift.

**The gap stands.** No published vault yet shows two agents on one vault with a human merging their branches. The band tells the story of agents building *for* each other, which is evidenced, and is written so as not to pretend it shows more.

### [The diagnosis before the rebuild — and a card for pointing at the sibling sites](#the-diagnosis-before-the-rebuild) [v0.2.59](../admin/versions.md)

homepagearticlesnetworkmethod

Asked to step back and say how this site should present its twenty-five published vaults, the answer was a diagnosis rather than a redesign — and it is published first, as [an article with screenshots of the current site](../articles/proof-behind-the-claim.md), so the rebuild that follows can be compared against it honestly.

The short version: **the proof is two clicks behind the claim.**

- The homepage leads with encryption, which cannot be looked at, and a terminal walkthrough of `create`, `commit`, `history` and `clone` — commands every git user has watched a thousand times. The word *vault* appears three times in the hero and the visitor is never shown one.
- The twenty-five artefacts a stranger can open in one click, with no account, sit under a dropdown as a table. A good table now — but a table is the right shape for *finding* a vault and the wrong shape for being *convinced* by one.
- The use-case cards are categories. Concrete examples of every one of them exist one level down.
- The strongest story — agents building for agents; a brief published here turned into a vault the same day, then reviewed by the team that owns the API — is filed under Docs, as a log.

One gap named plainly: the homepage's strongest multi-agent claim, *a branch per agent and a human reviews the merge*, has **no published vault behind it**. Every vault here was built by one agent, or by one agent on another's finished work.

The fix is set out in order — proof before mechanism; reorder and cut rather than add — and is the next release.

**Also new: a card for pointing at the sibling sites.** The `*.sgit.ai` sites exist so each topic gets the depth a section here could not give it, which only pays off if this site points at them constantly — and a bare link does not say *this continues elsewhere, on purpose*. A one-line `!site` directive now renders a card that pulls the target site's own category and thesis from the network directory, so it describes that site the way the site describes itself. It debuts in the article pointing at [open-source.sgit.ai/about](https://open-source.sgit.ai/about/index.html), which is also a decision recorded there: this site will get an About page about **sgit**, and link to the fuller record rather than duplicate it.

### [The board moves into a vault of its own — and its read key is published](#the-board-moves-into-a-vault) [v0.2.64](../admin/versions.md)

boardvaultsteammethod

Two releases after [the board](../team/board.md) appeared as files in the site repository, the shape was right and the home was wrong: moving a card from *review* to *done* cost a full site release — build, validate, two pushes, and a wait for the deploy to verify. A board should be cheaper to update than the thing it tracks.

So the cards moved into [a vault of their own](../demos/vaults/board/index.md), `pdulwi6i`, and its read key is published — because every task, bug and need on it is public, and a read key is the complete credential for reading them.

- **The vault is the truth; the site is a reader.** The release script pulls the vault before it builds, and the columns on the board page are labelled as a snapshot at the site version. Between releases the vault is ahead, and opening it shows the live board.
- **Moving a card is `sgit push`.** Edit one `status` line, regenerate the index, commit, push. No site release.
- **A board app that asks for nothing.** `index.html` lists `issues/` through `sg.vfs` and draws five columns; `app.json` declares `permissions: {}`. Served outside a vault host it falls back to `issues/index.json`, so it can be screenshotted, tested and read from a script — a board that only renders inside one host is a board nobody can check.
- **Cloned in place.** The site's `admin/content/team/issues/` *is* the vault's working tree: its encrypted store is gitignored, its card files are tracked as the build's input. If the two ever disagree, the vault is right.

Published as row #26 on the [vaults table](../demos/vaults/index.md), following the method: write key escrowed, audit run (nothing secret-shaped beyond the read key in its own README), the app screenshotted by driving it, permissions stated. The Sherpa's [board prompt](../team/prompts.md#board) now ends with a push rather than a build.

### [Our build brief was wrong, and the team that owns the code said so precisely](#our-brief-was-wrong-and-the-team-that-owns-the-code-said-so) [v0.2.58](../admin/versions.md)

briefsapicorrectionagents

Two days ago v0.2.55 published a [build brief](../briefs/vault-telemetry-append-lanes.md) on getting telemetry out of a vault whose read key is public. An agent [built a vault from it](../demos/vaults/agent-permission-games/index.md) and could not get events out. The SG/API team read the append-lane code against our page and returned a line-referenced review.

**Both of the things the brief told a builder to *verify*, it had already answered wrongly.**

- We said `sg.append.write` fails closed in a read-only session. **It does not.** There is no read-only gate on append anywhere; `permissions.append.write: true` is the entire requirement, and `sg.app.writable` is irrelevant to it. The `EREADONLY` we cited belongs to `sg.vfs.write` — a different code path that happens to deny with the same string, which is exactly how the misdiagnosis propagated.
- We steered readers to a direct `fetch` instead. That path is **blocked by default**: the frame ships `connect-src blob: data:`. The escape hatch is `permissions.network: true`, which the reviewer notes appears *"zero times"* in the authoring guide and zero times on our page — *"discoverable only by reading `app-permissions.js`."* It is also the wrong fix, since it reopens every egress from a frame holding decrypted vault content.

The brief now recommends the bridge, and the correction sits in a box **above** the section it corrects rather than being edited in quietly. The prompt at the bottom — the part written to be pasted to a builder — is reversed.

**It also resolved an open finding.** When the games vault was published we could not confirm the write endpoint and said so rather than guessing. The answer is that its telemetry is *built and never sent*: the vault declares no permissions at all, so the CSP blocks its sender. That matches the author's report that nothing arrived, and [its page](../demos/vaults/agent-permission-games/index.md) now leads with that status instead of claiming it phones home.

**Three facts that existed nowhere public** are now on [the API reference](../api/append-lanes.md): only `write` takes a `vault_id` while the other five verbs bind to the currently open vault, so listing a remote lane is impossible by design; `fetch` maps to `append.read`, not `append.fetch`; and the `inbox` field in a listing is the lane folder, which today is the **raw append token** while config stores only its hash.

Seven questions went back, including the two we most want to publish: whether the enum-key derivation is stable enough to document as a spec, and whether any non-destructive way exists to tell an append token from a read key — they are the same 64-hex shape, and confusing them would be a serious leak.

Also in this release: the `#` column on [the vaults table](../demos/vaults/index.md) was renumbering 1–25 on every sort, which said nothing. It is now a permanent publication ordinal — `#1` is the first vault ever published here — so it never changes, and sorting by it is by construction the same order as sorting by date.

### [Ask this site — a pane on every page whose model calls tools over the site's own content](#ask-this-site) [v0.2.63](../admin/versions.md)

chatllmtoolsbyokagents

Every page now carries a pane, bottom right: **Ask this site**. It follows the three tiers the [network chooser](../articles/chat-on-a-static-site.md) set out, with one difference that matters — the model does not read a catalogue pasted into its prompt. It is given **seven tools** and calls them.

| Tool | What it does |
|---|---|
| `search_site` | keyword search over pages, vaults, sibling sites, release notes, articles, roles and board cards |
| `read_page` | the markdown twin of any page, up to 6,000 characters — so the model quotes rather than paraphrases |
| `list_vaults` · `list_sites` | the vaults table and the network directory, filterable by category |
| `latest_updates` · `get_board` | the feed and the kanban |
| `current_page` | what the reader is looking at, for "this page" questions |

- **No key:** the tools run directly. Type words to search everything, or `/vaults`, `/sites`, `/updates`, `/board`, `/read PATH`, `/here`. Instant, private, no network once the index has loaded.
- **Your own OpenRouter key:** the model gets the seven tools as function definitions, calls them, and **every call is shown** as a trace line above the answer. Each call executes in the page over a build-emitted index and the `.md` twins, so the model can only say what a tool returned. It ends with the paths it used, as links.
- **Inside a vault:** the host could hold the key below the permission floor through `sg.llm`. Not wired yet — blocked on whether the bridge's chat contract carries tool calls — and on [the board as T11](../team/board.md#T11).

The index the tools read, `assets/site-index.json`, is written beside `llms.txt` from the same data as the vaults table, the directory, the feed and the board. One derived file: an answer given in the pane is an answer the site already gives somewhere.

The key goes to openrouter.ai and nowhere else — sgit.ai has no server to send it to — and the pane says so in the same words the chooser uses. Model output is escaped, and links are allowed only to `http(s)` or to paths on this site.

The [chat article](../articles/chat-on-a-static-site.md) gains an addendum, and its *shared component: not started* row becomes *partly*: this is one site's copy, not yet the versioned module the other eighteen could load.

## 2026-09-06

### [The vaults table stops being a key dump — sortable, categorised, newest first](#the-vaults-table-you-can-sort) [v0.2.57](../admin/versions.md)

vaultsuxmobile

Reported from an iPad, where the failure was obvious in a way it never is on a desktop. The read key is a 64-hex string; giving it room squeezed the vault id down to **one character per line** — `ookq4mn4` rendered as a vertical stack.

The fix was not narrower columns. It was noticing that the two widest columns were the two nobody needs on an index: the read key and the *open live* link are both already on each vault's own page, one click away. So [the index](../demos/vaults/index.md) now answers *which of these do I want*, and the vault's page answers *how do I open it*.

**Gone:** the read key, the open-live link, and the dense contents blob. **New:** a `#` column, a one-line **what it is**, a **category** pill, files and size as separate numeric columns, and a **published** date. **Click any heading to sort** — default newest first, because the recent ones tend to be the interesting ones. The count line carries the total and the breakdown: 25 vaults across 8 categories.

**Generated, not hand-written.** Twenty-five hand-written table rows could not be sorted, counted, or kept consistent, so the table now comes from `admin/content/vaults.json` through a `VAULTS` comment marker — the same mechanism the homepage articles band uses.

**The published date is not a date anybody typed.** It is the commit on which each vault's page first appeared in git, recovered with `git log --diff-filter=A`. Two weaker sources were tried and rejected first: update posts missed ten vaults and false-matched `health-score` against a later release that merely mentioned it in passing, and the version log had no line for two of them at all.

**Sorting is progressive enhancement.** The rows ship newest-first in the HTML, so with JavaScript off the table is still correct and still in the most useful order; the headings are keyboard-operable. On a narrow viewport the *what it is* column drops out rather than wrapping to nothing, since that sentence is on the vault's page anyway.

Verified at 1280 and 390 wide: 25 rows, **zero** 64-hex strings on the page, zero open-live links, no horizontal overflow — and the sorting checked by asserting the order actually flips rather than by looking at it.

### [The brief came back as a vault — and it is the first one here that phones home](#the-brief-came-back-as-a-vault) [v0.2.56](../admin/versions.md)

vaultstelemetryagentsauditbriefs

v0.2.55 published a [build brief](../briefs/vault-telemetry-append-lanes.md) on getting telemetry out of a vault whose read key is public. Another agent read it and shipped the thing, so [two games about agent permissions](../demos/vaults/agent-permission-games/index.md) now joins the published vaults — two deterministic games about grants, permissions and mandates, sending anonymous usage events over an append lane to a separate private vault.

It is the first vault published here that **sends anything anywhere**, and the first end-to-end test of whether a brief written for an agent produces what it describes.

- **It took the fallback path**, which is the part the brief was least sure about. Not `sg.append` through the bridge — a direct `fetch` to the account-less write endpoint, `credentials: 'omit'`, `keepalive` on the final flush, payload in the `sgit pki` v2 envelope. `app.json` declares no `permissions` key at all, which is consistent: it does not need the host for this.
- **Exactly one 64-hex string exists in the whole vault** — the append token, in five places. No private keys, no enum/write/vault/read key fields, no third-party secrets, no personal data. One credential, and it is the write-only one.
- **The disclosure page is the model.** `telemetry.html` opens by naming the default it breaks — *"Opening a vault does not normally send anything anywhere. This one does"* — publishes the event schema, and then writes the sentence most analytics pages never do: *"What it proves. Nothing about anyone. Anyone holding this vault's read key holds that token and could forge or flood the lane."*

**A method correction that cost nothing only because the control was run.** The first version of the token test called a leak on the strength of `sgit clone` creating a directory. Then an all-zeros key produced the identical result — the directory is created regardless, and the test discriminated nothing. The marker that actually works is `.sg_vault/local/clone_mode.json`. A credential test with no negative control is not a test, and that now belongs in [the publishing method](../demos/vaults/publishing.md).

**Two findings, published rather than filed.** Two of the four pages still tell the player *"nothing sent"* — `what-can-it-do` was corrected to *"nothing stored"*, the home page and `which-agent-is-it` were missed, and the latter contradicts itself on a single screen. Nothing leaks; but the subject of this vault is informed consent, which raises the stakes on leftover copy. And the write endpoint could not be confirmed from this container — 404 on both hosts under both names — so that is recorded as unresolved rather than dressed up as a conclusion.

### [Briefs gets a second kind — references written to be executed, not asks waiting on a reply](#briefs-gets-a-second-kind) [v0.2.55](../admin/versions.md)

briefsagentsdocsmulti-agent

[Briefs](../briefs/index.md) has been a single scroll of cross-team asks since v0.1.13 — each addressed to another team, each carrying a status, each closing when it is answered. A brief arrived this week that is a different species, so the page now says so and separates them.

- **Build briefs** — a durable reference an agent executes: the mechanism, the traps, what to verify first, and the prompt to paste. It never closes.
- **Cross-team asks** — the seven that were already there, untouched, addressed to the sgit CLI, SG/Send API and SG/Vault UI teams.

The first build brief is [**telemetry from a published vault**](../briefs/vault-telemetry-append-lanes.md): how one vault sends messages to another, and how a vault whose read key is public reports anonymous usage back to its author. The mechanism is an **append lane**, and it works for one reason worth stating plainly — the sender's `append_token` grants **write only**. A visitor who extracts it from the published vault (and they can, because a read key decrypts everything) cannot list the lane, cannot fetch anything, and cannot read another reader's events. The write response is blind by design: exactly `{"ok": true}`.

It is the only credential shape that survives being published inside a public vault. What it does not buy is authenticity: events can be forged, and the real failure mode is **1000 pending files per token → 507**, not a confidentiality breach.

The new group starts with two entries rather than one, because [publishing a vault](../demos/vaults/publishing.md) was already a build brief — *"written to be followed by another site's agent"* — filed in the vaults section where nobody looking for a method would find it. That is the same misfiling that created `case-studies/` in v0.1.14.

**Briefs also moves in the nav**, out of Evidence and into Docs beside Skills. The section's centre of gravity is now agent-facing documentation rather than a record of conversations, and Docs is where an agent looks. Evidence keeps comparisons, case studies and use cases.

One editorial call, recorded because it went the other way from the obvious. The source brief opened by answering *"is there a doctor/patient case study for this?"* — there is not; the [health-score vault](../demos/vaults/health-score/index.md) is one vault with three audiences, not two vaults exchanging messages. In the repo copy that section earned its place because the question was asked. On a published page nobody asked it, and listing that vault among the pages to read implies it is a source for cross-vault messaging. So it is cut from the reading list and kept as a single line of signposting — because that vault is exactly where the next reader will go looking, and a named absence beats a hidden one.

## 2026-09-05

### [Provenance is not conformance — the AIUC-1 vault, forked and layered](#provenance-is-not-conformance) [v0.2.54](../admin/versions.md)

vaultsstandardsconformancegraphspermissions

[Provenance is not conformance](../demos/vaults/aiuc-1-conformance/index.md) joins the published vaults. It is a **fork** of the [AIUC-1 catalogue vault](../demos/vaults/aiuc-1-graph/index.md) that keeps every byte of it and adds one directory above it — 649 files against the catalogue's 135. Both vaults stay published, and the catalogue page now says what it is and links to the fork.

The distinction the whole thing rests on is two edges that are never allowed to touch:

| edge | answers | absent means |
|---|---|---|
| `evidenced_by` | does the standard say this? | a build defect |
| `attested_by` | does **this subject** do this? | the control is unevidenced — **which is the finding** |

- **Unevidenced is a state, and it is the default.** Every control in scope gets a row whether or not anybody has looked at it, so an absent row is never read as compliance. The first build across all 53 controls comes out 2 evidenced, 48 unevidenced, 3 contradicted — the designed answer, not an unfinished one.
- **Insurability is computed, not asserted.** Conformance states become conditions and exclusions on a `policy/v1`: 1 condition met, 52 exclusions, 0 of 5 consequences covered. Move the `as_of` date to 2027-01-15 with nothing edited by anybody and the condition has expired, leaving 53 exclusions.
- **A crosswalk becomes a join between two vaults.** 62 of AIUC-1's 1,126 crosswalks resolve into article nodes in the published [regulation graph](../demos/vaults/regulation-graph/index.md), with CELEX and a hash on each edge; the other 1,064 are reported unresolved rather than forced. The join then finds something neither vault knew alone: **8 of the 27 target articles are amended by Regulation (EU) 2026/1744**, so the crosswalk was published against the text before amendment.
- **The first vault here to ask for a write grant** — `fs.write` scoped to `["chat/"]` and nothing else, plus `sg.llm.*`. The chat is stored in the vault; the authored terms the query depends on cannot be written by the app at all.

The claim that makes a fork readable is that it did not edit what it copied, and that claim is checkable rather than decorative. Run from the clone before publishing: the catalogue's own tests report **21/21 passed**, including the one that rebuilds every source document to the word, and the added layer's report **19 tests, 0 failed**.

It remains unofficial and derivative — not approved, certified, endorsed or reviewed by AIUC, and not a substitute for the standard. The subjects it measures are invented for the demonstration. The catalogue's open question about reuse rights applies here too, doubled, and is stated on the page rather than tidied away.

## 2026-08-27

### [The directory answers questions now — and the default tier needs no key](#the-directory-answers-questions-now) [v0.2.47](../admin/versions.md)

chatllmnetworkvaults

Two things: [the network directory](../network/index.md) grew a chat box, and a second conference vault went up.

**Ask it which of the nineteen sites is yours.** Type *"I have to sign off a risk"* and it points at risks.sgit.ai — and shows you the words it matched on. It runs in your browser against the catalogue generated from the same files the cards and the table come from, so it cannot drift from the directory underneath it.

- **No key, no account, no network call** in the default tier. A reader should not have to hold a credential to use an index.
- **It tells you why it chose.** A hit in a site's thesis or domain outweighs one in its summary, and the answer names the matched terms. An LLM answer does not give you that for free.
- **Bring your own key if you want prose.** Opt-in, OpenRouter, streaming — reusing the pattern already proven in the workbench vault. The cost is stated on the panel rather than buried: with no host there is no permission floor, so the key lives in the page's origin. If the call fails it falls back to the local matcher and says so.
- **[The plan](../articles/chat-on-a-static-site.md)** covers the third tier — serving the directory as a vault app, where `sg.llm.chat` keeps the key below the permission floor and the app never sees it. Not built; scoped honestly, including the parts that are not started.

One fix worth recording. The matcher first sent *"I need to cite a regulation precisely"* to **wardley-maps**, because it only knew each site's own vocabulary — standards.sgit.ai says *provision*, and the reader typed *regulation*. Site entries now carry an `aliases` field holding the words readers actually arrive with. Five real questions, five correct first hits; nonsense still returns nothing rather than a confident wrong answer.

Also live: **[Scaling Threat Modeling with Semantic Knowledge Graphs](../demos/vaults/threatmodcon-2025/index.md)** — ThreatModCon 2025, Barcelona. Eleven linked threat models from customer to compute instance, so a vulnerability in a line of code traces up to the revenue it risks. 51 nodes, 179 threats, five interactive views and five Wardley walkthroughs, all running offline in the vault. Two of its data files are **invalid JSON upstream** and are repaired here, with the repair proved rather than asserted: the only differences are four stray brackets removed and one `],` added, and the multiset of content lines is unchanged.

### [An insurance policy for an agent — and the delta is the risk](#the-delta-is-the-risk) [v0.2.52](../admin/versions.md)

vaultsagentspermissionsrisk

[Licence to Operate](../demos/vaults/licence-to-operate/index.md) joins the published vaults — one agent, its policy, and a simulated conversation where every reply carries its price.

**The idea worth stealing is the delta.** Three sets:

- **CAN DO** — the grant. 12 capabilities.
- **MAY DO** — the mandate. 4, and the only thing the policy insures: `crm:read`, `kb:search`, `llm:generate`, `mail:draft`.
- **THE DELTA** — 8 capabilities inside the agent's reach and outside its authority, including `crm:write`, `crm:export`, `mail:send` and `shell:exec`. **No policy covers these.**

The mandate is *"answer a customer's question from their own record and the help centre, and draft — never send — a reply."* The grant includes `shell:exec`. Nobody asked for it, nothing insures it, and the agent can reach it. That is [nhi.sgit.ai](../network/nhi.md)'s blast-radius argument made countable, and here the gap is priced rather than described.

The simulation makes you spend it: a customer cannot log in, and each of three replies shows its cost before you commit — 1,400 tokens in band, 4,800 tokens and three records which *claims*, or a password reset that is `mail:send` and outside the mandate entirely. Underneath is a live rate table with a normal band, an ask-above threshold, a pool with an untouchable reserve, and customer records marked *uninsurable above 20*.

**The permission grant proves the architecture rather than asserting it.** The vault holds the terms; your browser holds the run. And `app.json` requests `fs.read` and `downloads` — **read, no write, at any path**. An app that simulates spending against a policy is structurally incapable of editing the policy it spends against; not because it behaves, but because it never asked for the grant that would let it.

One process note. The agent that built this vault supplied its own audit of all 16 commits, and it was accurate — but it was checked rather than accepted. Re-verified against a fresh read-key clone: no credentials anywhere, the `/home/claude/` build paths baked into the PDF are gone (zero occurrences), and the one full-length credential in the vault is the vault's **own** read key — confirmed by deriving it independently and matching byte for byte, rather than by trusting the label on it.

### [A standard as a graph, and the one line that makes it trustworthy](#a-standard-as-a-graph-and-the-line-that-makes-it-trustworthy) [v0.2.49](../admin/versions.md)

vaultsgraphsprovenancestandards

[AIUC-1, as a graph you can cite](../demos/vaults/aiuc-1-graph/index.md) joins the published vaults — an **unofficial, derivative** machine-readable catalog of the public AIUC-1 agent standard. It is not approved, certified or endorsed by AIUC, and the page carries that in a box above everything else rather than in a footnote.

- **53 controls, 144 requirements, 1,126 crosswalks** to 13 external frameworks, resolving to 1,238 nodes and 3,526 edges across five releases.
- **Every field names its source.** Each control carries the official page it was read from; each of the 82 captured pages carries its HTTP status, retrieval timestamp, the **SHA-256 of the bytes**, and the retained gzipped snapshot inside the vault.
- **A control is drawn as its edges** — `has_requirement`, `maps_to`, `evidenced_by`, `applies_to_capability` — which is [graphs.sgit.ai](../network/graphs.md)'s argument applied to a compliance standard.
- **A release that could not be built is recorded as unbuilt.** AIUC names a 2025-07-22 release that carries no commit, so the catalog says so rather than dropping it.

The best thing in it is a refusal. It publishes the five places where the official website and the official changelog repository disagree, classifies each as presentation rather than meaning, and then declines to pick:

**"None of these is resolved here. Resolving one means choosing a source, and that is not this build's to choose."**

A derived artefact that silently picks a winner when its sources conflict has stopped being derived and become an opinion — and the reader cannot tell which. This one preserves both readings and stops a release being marked `validated` if a difference changes meaning.

Its collection policy is worth copying too: an identifying user agent, one request per second, no authentication, no slug guessing, every page reached from a page already fetched — and `robots.txt` fetched first, returning 404 at capture time, **with the manifest recording that observation verbatim rather than the conclusion alone**.

One thing stated plainly rather than buried: the vault's own `NOTICE.md` records that **reuse rights for the full AIUC-1 control text have not been confirmed with AIUC**, and that anyone republishing publicly should confirm first. Publishing this read key is that kind of republication, and it is here at the author's decision with the vault's disclaimers reproduced rather than summarised. The vault's undertaking — *"If you are AIUC and want something here changed or removed… removal will be honoured"* — is repeated on the page and applies to it too.

### [A three-minute pitch, delivered from a vault — and the first grant that is not empty](#a-pitch-delivered-from-a-vault) [v0.2.51](../admin/versions.md)

vaultspermissionspresentation

[The VoiceDebrief pitch to Founder Institute](../demos/vaults/voicedebrief-pitch/index.md) joins the published vaults — the 23rd, and not a deck *about* a vault but a deck **presented from** one.

- **A presenter, not a PDF.** Twelve slides with per-slide target timings, a live 3:00 countdown, speaker notes, Focus and Fullscreen — plus five backup slides for Q&A, one of them titled *"WhatsApp / ChatGPT already does this"*, which is the obvious objection answered rather than avoided.
- **The working ships with the conclusion.** The approved outline and its claims-to-keep-exact list, the spoken script per slide, the fifteen-part pitch pack, the research notes, the screenshots, and the PDF and PPTX exports — all in the same object as the slides. The deck is generated from a template by a script inside the vault, so the slides are built, not hand-maintained.

**It is also the first vault here that asks for anything.** Every other one declares `"permissions": {}`. This one declares:

```

"permissions": { "downloads": true, "externalLinks": true }

```

It offers PDF and PPTX buttons, so it asks for downloads. It links to the live product, so it asks for external links. That is the whole request — **no filesystem access at all**, not read, not write, at any path. The grant is one line, it maps onto two things you can point at in the interface, and nothing outside it is reachable however the app is written. Set beside the [Risk Graph Explorer](../demos/vaults/risk-graph-explorer/index.md)'s empty grant, the difference is legible without reading any code.

Audited clean on credentials. Three things become public with it, all apparently by design and all named on the page rather than left to be discovered: the unit economics and commercial terms, the author's contact address on the closing slide, and the three named judges of the session with their affiliations — names and roles only, with no tactical notes about them anywhere in the vault.

## 2026-08-26

### [Nineteen sibling sites, and a way to find the one that is yours](#nineteen-sites-and-a-way-to-find-yours) [v0.2.44](../admin/versions.md)

networknavigationrefactor

[The network](../network/index.md) was four sites. It is **nineteen** — seventeen live, two with the repository and subdomain in place but nothing published yet. That is no longer a footnote on this site; it is where most of the writing now lives.

- **The page now starts with a question, not a list.** Seventeen lines, each one something somebody actually arrives with — *"I need to give an AI agent an identity"*, *"I have to sign off a risk and I do not want to rubber-stamp it"*, *"my app has to call an LLM and I do not want it holding an API key"* — and the site that takes it seriously. At four siblings a list was fine. At nineteen, a list is a directory you have to read before it helps you.
- **Grouped by area** — Agents &amp; AI, Risk &amp; governance, Graphs &amp; method, Security &amp; infrastructure, Business &amp; publishing — with a full scannable table underneath for anyone who would rather see all nineteen at once.
- **Every thesis is the site's own words**, quoted from its H1 or lede rather than summarised here, so an entry cannot drift into describing a site that no longer says that.
- **Network moved to the top-level navigation.** It had been the third child of Updates, which was a reasonable filing decision at four entries and a bad one at nineteen.
- **And the homepage says it out loud**, with five doors in by area — because a reader who does not yet know these sites cannot pick one from a list of domains.

Two sites appear with no screenshot and no link to a live page: `skills.sgit.ai` and `influences.sgit.ai` have DNS and a repository but GitHub Pages has not published them. They are listed as *not published yet*, pointing at their repositories, rather than quietly left out — the same reason a missing tag is preferable to a missing page.

This is the refactor it looks like from the outside. Material that would have made this site sprawl has a better home; this page is the index back into it. Adding the twentieth site is writing one markdown file.

### [Articles get a place on the homepage, and a band gets its width back](#articles-get-a-home-and-a-band-gets-its-width-back) [v0.2.45](../admin/versions.md)

articleshomepagelayout

Three changes, one of them a bug I shipped yesterday.

- **The network band ran the full viewport width.** The homepage bands each carry their own measure — `.eco` has `max-width:1100px` on the component itself, not on a wrapper — and the band added in v0.2.44 simply had none, so it stretched edge to edge on a wide screen while everything above it stayed in the column. Measured after the fix: `.eco`, `.netpick` and the new `.artcards` all report exactly **1100px**, with no horizontal overflow. The five area cards also now lay out 3+2 rather than 4+1, which stops the last card sitting alone.
- **[A new article](../articles/nineteen-sites.md)** on what the split actually was: twenty repositories in fifteen days, fifteen of them in the last five, and what that did to the writing — what forced it, what it cost (discovery got worse before it got better), and why the directory now opens with a question rather than an inventory.
- **Articles now have a place on the homepage.** They turned out to be the readable surface over all of this — a reader who will not work through a docs tree will read one argued page. The band is **derived from the articles list**, so a new article appears there by being written. No list to maintain, same rule as everywhere else here.

Also: [influences.sgit.ai](../network/index.md#business-publishing) went live and is now a full entry with its screenshot — *"where the thinking came from"*, an influence map in three tiers with a changelog recording when a source moves between them. That leaves **eighteen of nineteen live**; `skills.sgit.ai` still has DNS and a repository and nothing published, and is still listed as such rather than hidden.

### [A conference keynote as a vault — the deck, its exports, and the research it came from](#a-conference-keynote-as-a-vault) [v0.2.46](../admin/versions.md)

vaultspresentationprovenance

[AI vs. AI — Black Hat Europe 2025](../demos/vaults/blackhat-eu-2025/index.md) joins the published vaults. It is the twentieth, and the first that is a **talk** rather than a document set or an app.

- **The whole chain, one credential.** The deck as presented (26 slides), six PDF exports from v0.1.1 to v0.2.0, the eight research papers it was built from, and the slide system's own source at ten versions — all in one vault, opened with one read key.
- **The slide content is data, not markup.** `deck/blackhat-eu-2025.json` is read through the vault bridge at load time, so changing a slide is a commit rather than a rebuild. That separation is why the vault can carry ten versions of the renderer beside one deck without either owning the other.
- **It asks for nothing.** `"permissions": {}` with `present: true` — the deck opens full-screen and never touches the filesystem.

The argument is worth the click on its own. It opens by conceding the ground — *security's four pillars, all broken* — then lands on four publicly documented outages that were **not** attacks: a timing bug that wiped a global database, a config inconsistency that detonated worldwide, a routine change that halted traffic, and a faulty update that bricked 8.5 million machines. The turn is one line: *"These weren't sophisticated attacks — they were minor glitches that cascaded. Now imagine if they were deliberate."*

Several of its later slides describe things this site now demonstrates rather than proposes — *assume compromise, contain blast radius*, *version control everything*, *identity graphs for least privilege*. Those threads have their own homes in [the network](../network/index.md) now.

Audited clean before publishing: no sgit credentials, no third-party API keys, no private keys, no emails, no client named. The organisations that appear — AWS, Azure, Cloudflare, CrowdStrike — are cited for public incidents, which is what the slide is about. The deck uses Black Hat Europe's official speaker template because it is a talk that was given there; the page says plainly that it is published as the speaker's own material, not as anything endorsed by or affiliated with the conference.

## 2026-08-25

### [Six vaults published, three held back — and the check that nearly missed one](#six-vaults-published-three-held-back) [v0.2.43](../admin/versions.md)

vaultsauditsecurity

Nine vaults were submitted for publication. **Six are now live**, [in the gallery](../demos/vaults/index.md). Three were held, and the third one is the reason this post exists.

- **[Penetration Test Report](../demos/vaults/pentest-report/index.md)** — a pentest delivered as a vault instead of a PDF. Eight audience-specific views over one engagement, and every finding ships a retest script that exits `0` if it is fixed and `1` if it is not. Entirely fictional, with a `SIMULATED DEMO` badge on its own front page.
- **[Standards Atlas — GDPR](../demos/vaults/standards-atlas-gdpr/index.md)** — *"the standard is the graph."* Rulings, regulator guidance and per-country variation as first-class nodes over the articles they bend, with corrections written back into `feedback/` and nowhere else.
- **[RiskMandate · File security](../demos/vaults/riskmandate-file-security/index.md)** — risk acceptance moved from a rubber stamp at the end to the centre of the flow, over versioned JSON queried live by SQLite in the browser.
- **[Content-Transformation Proxy](../demos/vaults/content-transformation-proxy/index.md)**, **[SG Commercialisation](../demos/vaults/commercialisation/index.md)** and the **[SG/Payments Brief Pack](../demos/vaults/payments-brief-pack/index.md)** complete the six.

**Two were held for carrying credentials.** One contained two live vault keys in plaintext — including **its own write key**, which would have turned a published read key into full write access. The other is a private working log that was never meant to be public.

**The third is the one worth recording.** A vault whose app reads an LLM key from a file scored *clean* on the first credential pass — and then a screenshot of it showed a chip reading `key: vault key.json`. The file held a live OpenRouter API key. The scan had looked for vault-key shapes, `sgit_` prefixes, private-key blocks and the string `api_key`; the field was named `openrouter_key`, so nothing matched.

That is a real gap, not a near miss reframed as a win. The credential tooling here was built to protect *sgit* credentials and does that well; it had no opinion about third-party API keys, which are just as costly to leak and far more common. A broader sweep — OpenAI, Anthropic, GitHub, AWS, Google, Slack and JWT shapes, with placeholders filtered out — now runs over every candidate, and it found exactly one other hit: a forged `alg:none` token in the pentest vault, which *is* the finding it documents.

The lesson is the cheap one to state and the easy one to skip: **a scan that has never surprised you is not evidence that you are clean.** It was a screenshot, not the scanner, that caught this.

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
