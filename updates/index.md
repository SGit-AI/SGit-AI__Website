# Updates — sgit.ai

> What changed on sgit and on this site, as it happens — one entry per story rather than per release, each linked to the release that carries it. RSS and JSON feeds included.

*Source: <https://sgit.ai/updates/index.html> · site v0.2.54 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

# Updates

What changed on sgit and on this site, as it happens — one entry per story rather than per release. The [version log](../admin/versions.md) is the complete technical record; this is the readable one.

Follow along: [RSS](feed.xml) · [JSON](updates.json). Every entry links to the release that carries it.

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
