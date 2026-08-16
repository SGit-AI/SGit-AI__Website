#!/usr/bin/env python3
"""Generate every page of the sgit.ai vault site from a shared template.

Release process (see admin/index.html):
  1. bump SITE_VERSION below (v0.1.n — n increases on every push)
  2. add a row to VERSION_LOG
  3. run this script, run the validation suite, sgit commit + push
"""
import os
import re
import json
from html.parser import HTMLParser

SITE_VERSION = 'v0.2.21'
BUILD_DATE   = '2026-08-15'

def find_vault_root():
    d = os.path.dirname(os.path.abspath(__file__))
    while not os.path.exists(os.path.join(d, 'app.json')):
        parent = os.path.dirname(d)
        if parent == d:
            raise SystemExit('vault root not found (no app.json above this script)')
        d = parent
    return d

VERSION_LOG = [
    ('v0.2.21', '2026-08-16', 'this release',
     "Two reader reports from an iPhone, both fixed with the cause named. (1) The vault pages now open both surfaces ON LOAD — the reader lands on the vault, not on a row of buttons. The opens are sequential by design: the browser surface starts once App Mode reports vault-ready (grace-capped), so its objects come out of the client's encrypted-object cache and the second open mostly decrypts rather than fetches — the caching architecture demonstrating itself on every page view. Buttons are gone; each frame carries a label and its own status line, and a failed handshake leaves a retry control instead of a dead page. (2) The landscape-iPhone report — site and iframe not using the full width after a pinch-zoom — was hunted down empirically rather than guessed at: one unbreakable 702px token (the sgit clone command with its 90-character credential) on a 393px viewport made the page 743px wide, which drops Safari's fit-to-width scale below 1; pinch out and the entire site sits narrow with a white gutter. Fixed with overflow-wrap:anywhere on inline code (breaks only when a token would overflow) plus the html canvas painted the site colour so any zoomed-out or overscrolled area reads as the site rather than as white margin. Verified at iPhone viewports: every checked page now measures exactly the viewport width, and the auto-open completes with zero clicks."),
    ('v0.2.20', '2026-08-16', 'obj-cas-imm-23e6ea08a77d',
     "Both surfaces at once, reader-requested: on the vault pages, App Mode and the vault browser now each open in their OWN frame, stacked — the app first, the FILES/SGIT/SETTINGS browser under it — instead of one frame the buttons fought over. The second open is fast by design and the component says so: the encrypted objects are already in the client's cache from the first surface, so the second mostly decrypts rather than fetches — the caching story demonstrating itself. Each frame carries its own status line from its own handshake (one listener, replies routed by which frame sent them). The Full screen button is gone from these pages — with each surface getting a full-width, viewport-height frame of its own, it earned nothing. Verified headless: both surfaces open (5.0s through the slow test mirror, faster live), app above browser, two independent vault-ready events."),
    ('v0.2.19', '2026-08-16', 'obj-cas-imm-2773e0dfba35',
     "The site starts doing the thing it was building toward: publishing vaults. New /vaults/ section — an index of every read key this site has deliberately published, and one page per vault (five at launch: Field Notes, Strategy Maps, Deploy Docs, the Catalogue itself, and — new — Algarve · May 2026) with a real description, the features that vault exercises, what the shape is good for, the derived facts, the key as a copyable sgit_rk1_ credential with a CLI command and an open-in-the-official-UI link, and the vault RUNNING LIVE in the page via the reusable embed component (assets/vault-ui-embed.js — the two-surface embed-protocol host from the demo page, now attribute-driven; App Mode hidden for vaults without an app). Pages load the component contract-compliantly (fetch+eval, no script src — every page must survive being served from inside a vault). The Algarve vault is the first entry processed through the catalogue's submission queue as designed: read key supplied in chat, everything else derived — 71 files, 29 MB (60 WebP photos in originals/web/thumbs), 36 commits, auto-opening gallery app with a chaptered narrative. Its pre-publication audit is published on the page per the rules: one finding (a live delete_auth token in public-preview bookkeeping — narrow scope, the owner advised to rotate) and one counterpoint worth showcasing (the same vault's readonly-tokens bookkeeping decrypts to further ciphertext: owner secrets double-encrypted, the pattern that fixes the finding class). Catalogue vault updated in the same breath — new entry, trip-gallery-1 ticked off the awaiting list (7 remain) — and /catalogue/ picked it up with no site deploy, which is that design working."),
    ('v0.2.18', '2026-08-16', 'obj-cas-imm-68578f7b1bf4',
     "The tag pipeline's first contact with a real GitHub rule, fixed within the hour. v0.2.17's run DID tag itself — the first CI-authored tag — but the historical backfill push was rejected wholesale: a workflow's GITHUB_TOKEN cannot push any ref pointing at a commit whose tree carries a different version of a workflow file, and the `workflows` permission that would allow it is not grantable to that token. Every pre-v0.2.17 release predates the current deploy-pages.yml, so all 33 backfill tags bounced — and because the tag job failed, the deploy was skipped and v0.2.17 never reached the live site (this release carries its changes out). The fix splits the pushes by what they are: THIS release's tag at HEAD is load-bearing and fails the job if rejected (it never should be — HEAD's workflow blob matches the branch, which is why v0.2.17's own tag went through); the historical backfill is best-effort per tag, warns per rejection, and emits one notice with the single human command that completes the set — `git push origin --tags` from any workflows-scoped credential. Once a human has done that once, the backfill loop becomes a chain of no-ops. Lesson recorded for the case-studies pile: the same both-remotes discipline that made CI verify-and-tag instead of commit-and-tag also meant the failure cost nothing but a skipped deploy — no bump commit was stranded on one side of the two-VCS split."),
    ('v0.2.17', '2026-08-16', 'obj-cas-imm-24876be44e37',
     "Two reader-driven fixes and the release pipeline grows tags. (1) Layout: the embed buttons and their status line sit back in the text column where they belong — only the vault surface itself breaks out wide, since it is the thing with the big UX. (2) CI tagging, ported from the VoiceDebrief website pipeline (validate → tag → publish, every push to dev a minor release tagged v{release}.{major}.{minor}) with one deliberate adaptation: the upstream OSBot action has CI commit a version-file bump, but this repo is simultaneously an sgit vault, and a CI-authored commit would exist only on the git side — breaking the both-remotes-in-sync invariant release.sh enforces. Here CI verifies-and-tags instead of owning: SITE_VERSION (bumped once per release by release.sh) must match the release commit's subject and be the next minor after the latest tag, then the commit is tagged. No CI commits, no drift, same discipline — and a forgotten bump now fails the pipeline loudly instead of shipping quietly. The first run backfills tags for every historical release by parsing the commit subjects, so the whole v0.1.9→now history becomes navigable by tag. Also: validate.js now runs in CI as the gate before tagging and publishing, which puts the key-leak tripwire on the deployment path as well as the release path. (Tags could not be pushed from the authoring session — the session's git proxy authorizes branch pushes only, which settled the design question of who owns tags: CI does.)"),
    ('v0.2.16', '2026-08-16', 'obj-cas-imm-34ed83dd03e6',
     "The embed grows up: both official surfaces, one click each, over the UI's new embed protocol. Reading the deployed bundle found what the addendum's Phase 3 had shipped — embed-protocol.js and a shared embed-receiver on BOTH shells: the host page loads ?embed=1&parent=<origin>, the frame proves itself with vault-embed-ready, and only then is the key sent by postMessage with the targetOrigin pinned. Strictly better than the URL-fragment flow shipped yesterday: the key never appears in any URL, is never written to the frame's storage (verified — sessionStorage and localStorage empty after open, memory-only as the protocol promises), and the host gets structured vault-ready/vault-error events instead of guessing from load timings. The demo page now has two buttons: App Mode, and — new — the vault browser with the FILES/SGIT/SETTINGS rail, which previously needed a two-step trick because /en-gb/vault deliberately strips URL hashes and root is the only inbox. Headless-verified both: App Mode ready in 2.7s, browser in 9.7s, rail present, R1 W0 badge, no horizontal scroll. The embed area breaks out of the text column (94vw up to 1680px, height tracking the viewport) because the vault browser is a full working surface, plus a full-screen button — both asked for by a reader with big-UX vaults. What is still not possible is stated precisely on the page: vault-open carries {key, mode, deepLink} where deepLink is a file path, so a host can select a SURFACE but not a VIEW — SGIT and SETTINGS remain in-page events. The briefing gains an addendum thanking the UI team, recording the verification, and sharpening the last ask to one optional field: view:'files'|'sgit'|'settings' on vault-open, applied after mount. Also fixes a stale paragraph v0.2.15 left behind (a silent curly-quote replace failure) — the page no longer promises a swap that already happened."),
    ('v0.2.15', '2026-08-15', 'obj-cas-imm-576ba8a1a09f',
     "The gap closed: the official SG/Vault interface now opens from a published read key, and this site embeds it. Our v0.2.7 experiment had isolated the blocker to exactly one thing — the loader documented a read-only credential but rejected it, and the CLI shorthand was parsed as a passphrase and PBKDF2'd into the wrong ref id. The UI team shipped the fix: a read-key credential is now its own format (<64-hex>:<vault_id>, the shape sgit clone already accepted) and is tested BEFORE the passphrase formats, which was the precise ordering bug; canonical CLI key prefixes are stripped first. Re-running the same experiment against the deployed build, read key only, no vault key anywhere: all three credential forms parse; App Mode boots the Field Notes demo under full chrome with its six studies rendered and the bridge live; the vault browser opens with the FILES/SGIT/SETTINGS rail over the real decrypted tree; and the SGit view lists both commits with real object ids — all inside a cross-origin iframe, with an explicit R1 W0 / Read-only badge. So /demos/vault-app-embed.html now carries TWO hosts and keeps both on purpose: the ~170-line minimal host that shows the protocol with nothing hidden, and the official UI opened with the same published key. One ask stays open and is stated as such — no URL selects a view, so the SGit inspector cannot yet be framed in isolation. Also: the release tripwire learned the CLI's canonical WRITE-key prefix (its read-only sibling is deliberately exempt — we publish one), proven by making it fail before trusting it; it promptly caught this very release note's first draft, which had spelled the banned prefix out while explaining it. The hub capability audit is updated with verified evidence — row 1, the entry point for everything, flips from partial to present, which settles the spec's assembly-not-construction question for the forge's read-only tier."),
    ('v0.2.14', '2026-08-15', 'obj-cas-imm-2f3c360b2de1',
     "Ask B of the 14 Aug pack begins: the hub.sgit.ai briefing-pack plan lands in admin/plans/, and — per the spec's central instruction — the capability audit comes before any architecture. The audit table is already 13 rows deep, seeded entirely from evidence this project has produced: verified present (open-from-read-key in our readers, single-object decrypt, the app runtime under a sandboxed iframe, sparse per-object fetch, cross-session caching with the 120s ref window, frameability), verified partial with the exact gap named (the official UI parses but rejects its own documented read-only credential format), and honestly unknown (client-side merge, the in-UI diff and history views — enumerated in the bundle, never driven). The partial rows are flagged as the dangerous ones, because a partial capability gets assumed complete. The plan also fixes the pack's shape: six parts in order, the four absences stated up front, surfacing/adding/absent applied per feature (blame is adding, not surfacing), permissions as worked key topologies, and the private-vault key-handling flow named as the one needing a considered position. The crawler question is closed as answered: full text in the served HTML, noscript reveal since v0.1.26, and Google indexing confirmed."),
    ('v0.2.13', '2026-08-15', 'obj-cas-imm-35d4e3e3a906',
     "Fix: the catalogue page shipped without the vault debug panel markup that the shared reader wires unconditionally, so the reader threw on two missing elements and the first document never rendered (navigation and clicked entries worked; the initial body stalled at the fetching message). The panel is now on the page — which it should have been anyway, since watching the ciphertext arrive is half the point — and the headless check confirms the README renders on load with zero page errors."),
    ('v0.2.12', '2026-08-15', 'obj-cas-imm-15dbcf053020',
     "The catalogue: a vault indexing vaults, including itself. The 14 Aug briefing pack's Ask A lands as designed — a submission queue whose per-entry cost is a read key and one line, with everything else derived by opening the vault. The deriver (admin/build/catalogue_derive.py, ~120 lines, read-only, no token) turns a read key into file count, plaintext size, commit depth, HEAD, top-level layout, file types, app entries and browser-renderability; proven on all three published-key vaults (Field Notes 4bshby5n, the strategy/maps vault ookq4mn4 — both app entry points detected — and the deploy-docs vault fyofmkvr, markdown-only). The catalogue itself lives in a new vault (kc67yhgw) published with its own read key and listed in itself: README (how to submit), SCHEMA (supplied-vs-derived, and the two rules — read keys yes, vault keys never; escrow the write key BEFORE publishing, because a frozen vault can never be corrected), three processed entries, and the two public to-do lists the brief asked for — awaiting-a-read-key (seeded with eight vaults named in the memos, each carrying the pre-publish audit instruction the strategy-maps case taught) and awaiting-processing (the agent's queue, currently empty). /catalogue/ renders it live via the same reader as the deploy docs — updated by pushing to the vault, no site deploy. Write-key status is a first-class field: 'known and escrowed' or 'lost', stated publicly per entry."),
    ('v0.2.11', '2026-08-15', 'obj-cas-imm-1f8635c410ef',
     "sgit gets its own Wardley map analysis — six maps starting with git at full strength, because a map that flatters its author is not a map: version control today (git's moat is the platform layer, resting on readable storage), the files that cannot follow (a hole in the map where their foundation should be), sgit's move (no new verbs, invert the bottom layer), the boundary on one map (two chains from one team, split by 'may the store read this?'), agents as the new user (the serialised diff versus ambient authority), and the strategy (commoditise private version control). The maps are drawn as inline SVG by a ~90-line renderer — no images, no dependencies — and the analysis ships as a SECOND app inside the same vault as the SG/Send strategy essay (ookq4mn4): one encrypted store, two entry points, one published read key; the embed opens it by passing entry to the same host. The embed shim gained link handling — in-page anchors scroll manually (assigning location.hash re-navigates a srcdoc frame) and relative .html links remount the frame on the new entry, so the two apps cross-link inside the embed; verified headless: 6 maps, 42 nodes, 12 evolve arrows, and clicking the companion link lands on the strategy essay. Linked from the Why page's boundary section. Also: Google has confirmed indexing sgit.ai, which unblocks the component registry when its turn comes."),
    ('v0.2.10', '2026-08-15', 'obj-cas-imm-cedfb3d06f6a',
     "Plan bookkeeping: the why-expansion plan's status table now reflects reality — Why reframe done, serialised PR done with its CLI brief, two of three demo vaults live, embed at the minimal-host stage pending the UI team's credential fix."),
    ('v0.2.9', '2026-08-15', 'obj-cas-imm-2ce42cfd214e',
     "The two remaining pieces of the briefing-pack plan land. (1) The Why page is reframed from rebuttal to boundary map: it now opens with where git wins, then draws the boundary precisely — the operations are not the gap (commit through merge all exist; proposing reviewable changes without write access is present, as a serialised diff, and is a differentiator); what is absent is the hosted review interface and the ecosystem above the protocol; and git is also client-side, so the real difference is that the objects are encrypted there, with the losses stated as a given-up/in-exchange-for table. New protocol section: the six-step read path verbatim, the two keys named explicitly, the three modes (Local/API/Web), and the two-implementations proof point. The LinkedIn comment and the market answer move below the boundary, kept whole. (2) New lead use case: the serialised pull request — no credential issued at all, grounded in the 5 Aug Black Hat disclosure, with an honest shipped-vs-pattern table (emit exists as history diff --json; import is not first-class) and evidence status PARTIAL. The matching brief to the CLI team asks for sgit diff export/apply, a published diff format, and ignore-file support — the latter now a prerequisite for the one-folder-two-VCS pattern the site publishes."),
    ('v0.2.8', '2026-08-15', 'obj-cas-imm-4060eca3121d',
     "Second demo, and the first with real content: The Strategy in Seven Maps — the actual SG/Send strategy, published on LinkedIn in May 2026 — served live from a vault with a published read key. The page also publishes the audit that made this interesting: the original vault could NOT publish its read key, because its own read-write credential was written inside its content (a production briefing quoted the clone command verbatim), server-side bookkeeping under .vault/owner/ carried live delete_auth tokens, and the vault's keys derive from a legacy low-entropy token. The fix is the pattern the page teaches: republish, don't retrofit — sanitised copy, credentials redacted with a visible note, fresh full-entropy vault (ookq4mn4), and only then a published read key; a republish also sheds the history you cannot publish. The embed host gained vault-path image support (a MutationObserver swaps img.src vault paths for blob: URLs read over the bridge, the same job the real host's interceptor does) — verified: all eight Wardley Map PNGs travelled as ciphertext and rendered."),
    ('v0.2.7', '2026-08-15', 'obj-cas-imm-1b9cd77fb6d7',
     "The full-UI embed experiment, run and published. Driving the real SG/Vault interface framed inside a page: the UI is frameable (no X-Frame-Options, no frame-ancestors), and App Mode works completely inside a cross-origin iframe — with a valid credential the official app-shell booted the Field Notes demo under the full HUD chrome. The one gap is the credential: the loader documents a read-only format (vault_id + 64-hex read key) but the client rejects it, and the CLI's 64hex:vault_id shorthand gets PBKDF2'd as a passphrase and derives the wrong file ids. No URL selects the SGit view, either. Both are now precise, evidence-backed asks in the UI-team briefing — honour the documented format (which alone makes the official UI embeddable with only the published read key) and add a |view:sgit deep-link. The demo page carries the findings table."),
    ('v0.2.6', '2026-08-15', 'obj-cas-imm-966aed3bd862',
     "The first demo ships: a vault app running live inside a sgit.ai page from a published read-only key. A new vault (Field Notes, 4bshby5n) was created from scratch for it — a self-contained app following the authoring contract, generative SVG art, content in content.json read over the bridge — and /demos/vault-app-embed.html is the complete walkthrough: init, commit, push, derive the read key, publish it deliberately, embed. The embed host is assets/vault-embed.js (~170 lines): HMAC-derived ids, ciphertext over CORS, Web Crypto decryption, the app booted in a sandbox=allow-scripts iframe with an opaque origin, and its sg.vfs/loadCss/loadJs calls answered over postMessage — the same shape as SG/Vault's vault-in-vault, minimal by design until the UI team answers the reuse briefing. Also rewrites the one-tree-two-remotes ordering section as a clean rule (the discovery narrative is gone), adds the Demos nav section, and extends the key-leak tripwire to scan for every demo vault's passphrase, not only the site's own. Verified end to end in headless Chromium: bridge live (the app's status line reads content via sg.vfs.readText from the vault), six tiles rendered, frame origin opaque, mutations impossible by construction."),
    ('v0.2.5', '2026-08-14', 'obj-cas-imm-fedcfbd348c0',
     "Corrects the one-tree-two-remotes case study, prompted by a reader question: if sgit pushes first and git commits after, don't the files match? They do — tested rather than argued. With that ordering git captures the freshly written ref every time and a clean tree is the normal end state of a release; reads (ls, history, status, vault info), no-op commits and pushes, pull and fetch were all tried and none rewrites the ref. The section is now a rule about ordering rather than a claim of permanent drift, keeping the part that is true and useful: when the ref IS dirty, the bytes tell you nothing, because a rewritten ref never byte-matches even when it decrypts to the same commit."),
    ('v0.2.4', '2026-08-14', 'obj-cas-imm-854db222f8cb',
     "Wider layout across the site. The reading column was a classic 720px prose measure, which squeezed the content into the middle of a modern display and made every page longer than it needed to be. The measure is now 960px and the wide container 1360px, with the body type up a step (.93rem to .98rem) so the longer line keeps a comfortable character count; the home-page sections (hero, terminal, feature grid, cards) scaled in proportion, and the deploy-section nav column widened with them. Verified at 1600px (no overflow, content fills the frame) and at 390px (no horizontal scroll)."),
    ('v0.2.3', '2026-08-14', 'obj-cas-imm-6deb6376d9bd',
     "Plans and briefs from the 14 Aug briefing pack. Publishes the implementation plan for the Why reframe (boundary map), the serialised-pull-request lead example (with one honesty gap found while planning: the diff emit exists as history diff --json, but the CLI has no apply/import command, so the page will ship as PARTIAL and a brief goes to the CLI team asking for sgit diff export/apply plus a published diff format), three end-to-end demo vaults with deliberately published read keys, the embed-reuse work, and the component registry (components, never plugins — plugin stays reserved for capability grants; registry gated on indexing being observed). Files a briefing to the SG/Vault UI team with six concrete questions about reusing their app-iframe host code inside sgit.ai pages, linked from the briefs page."),
    ('v0.2.2', '2026-08-14', 'obj-cas-imm-29aa935bd44a',
     "New case study: one working tree, two version control systems — the workflow this site is actually developed with. One folder is both an sgit vault and a git repository; a release is two pushes of the same tree. The page covers what each remote carries, the one-file .gitignore boundary that makes it safe (everything encrypted is committed; only the plaintext local/ tier is excluded), and the finding that surprised us: the encrypted ref always looks modified to git because AES-GCM uses a fresh IV per write, so for that one file git status cannot detect staleness — proved by decrypting both sides to the same commit id. Ships admin/build/release.sh, which makes the discipline mechanical: build, validate (the key-leak tripwire gates BOTH pushes, not just the deployed one), push sgit, push git, and refuse to finish unless both remotes report in sync. The script deliberately never invokes commands that echo the vault key."),
    ('v0.2.1', '2026-08-14', 'obj-cas-imm-49cf3a524b0c',
     "Fixes a gap the v0.2.0 restructure opened: llms.txt is generated by walking a list of known sections, and the new case-studies section was not in it, so all three of those pages were silently absent from the machine index — present on the site, invisible to any agent reading llms.txt. The section is added, and the generator now refuses to build if any page would be omitted, which is the same guard as the orphan-page rule and for the same reason: a page nothing links to and a page the index does not list are both unpublished."),
    ('v0.2.0', '2026-08-14', 'obj-cas-imm-d8f580db4d0f',
     "Structural release — the middle digit moves, as the numbering note below promised it would. Two changes. (1) The root held 19 files and every page body was inlined in a 2,709-line generator; bodies now live one-per-file in admin/content/ with a pages.json manifest, and the generator is a 648-line engine that does not grow as the site does. Adding a page is a content file plus a manifest row; the build then produces the HTML, the markdown twin, the llms.txt row, the llms-full.txt section, the sitemap entry and the canonical/OG/JSON-LD tags. The refactor was verified output-preserving before any page moved: all 31 pages byte-identical. (2) Sections became folders — why/, try/, security/, skills/, briefs/ — leaving 9 files in the root, all of them ones that must be there. New case-studies/ section, which is where the leaked-key incident and the live-vault architecture now live; they were filed under docs/ and deploy/ where nobody looking for a case study would find them. Links were rewritten mechanically by resolving each href against the old path and re-expressing it from the new one, then verified by crawling every internal URL from the homepage: 29 URLs, zero broken."),
    ('v0.1.27', '2026-08-14', 'obj-cas-imm-87daa0751f0d',
     "Entity disambiguation, after checking what search actually returns. Google's AI Overview for the bare query already knows this project — and sources it from PyPI, because the PyPI page never linked here and this site was not in the index. \"sgit\" is also an Android Git client, an Indian engineering college and a class of shell shortcut, so the job is not only being indexed but being resolved to the right thing. Every page now carries JSON-LD: a SoftwareApplication node with sameAs pointing at the PyPI and GitHub identifiers that already rank, an explicit disambiguatingDescription naming the collisions, and a per-page TechArticle node. Google's own 2026 guidance says structured data is not required for generative-AI features — this is here for entity resolution, not ranking. The validator now fails the build if a page has no structured data or if any JSON-LD block does not parse."),
    ('v0.1.26', '2026-08-14', 'obj-cas-imm-5da2eb791bb2',
     "Acts on an inbound brief from an agent that tried to use this site as documentation and could not. It reported that the site did not rank for its own positioning language and guessed the pages might be client-side rendered. They are not — the full text is in the served HTML — but the fade-in that hides the unstyled flash left body{opacity:0} until a JavaScript bootstrap ran, so any client applying our CSS without running that bootstrap rendered a complete but entirely invisible page (measured: 15,733 characters at opacity 0), which is also a hidden-text signal to an indexer. Fixed with a noscript override and a CSS-only reveal failsafe, both now enforced by the validator. Adds the crawler surface that never existed: robots.txt, a generated sitemap.xml covering every page, and canonical plus Open Graph tags. Adds llms-full.txt — every page in one document — for the very common agent harness that will not follow a link out of a fetched file, and makes llms.txt self-sufficient: inline answers to the common questions (including exactly which git operations exist and which do not) and per-page key facts, on the brief's observation that for such an agent the descriptions are the only content it will ever see. The brief and what changed are published on the briefs page."),
    ('v0.1.25', '2026-08-14', 'obj-cas-imm-1861dd16dd11',
     "Three changes that go together. (1) Every page now has a .md twin at the same path, generated from the same content so the two cannot drift, with internal links rewritten to point at markdown — an agent can traverse the whole site without parsing HTML, and llms.txt is now generated from the page registry rather than hand-maintained. (2) A git-and-sgit comparison on the Why page that says plainly where git is better — performance at scale, ecosystem, bisect/blame/rebase, partial commits — and how the two run side by side, as they do on this site. (3) Use cases moved to /use-cases/ with a page per situation: the problem, a working recipe on shipped commands, an honest evidence status (proven / partial / pattern), and a brief you can hand to an agent. Validator gained three rules: every page has a markdown twin, markdown links resolve, and no raw HTML leaks into the markdown."),
    ('v0.1.24', '2026-08-14', 'obj-cas-imm-3c426ddbe9e9',
     "Why page rewritten around the right question. The first version answered \"is there a market\" with verticals and a comparison table; the sharper answer is what sgit makes possible that was not possible before, so that is now the headline: six capabilities running on this site — a live site its host cannot read, read access as a publishable capability, two agents sharing a workspace neither host can read, private data with CDN economics, storage as untrusted commodity, and transit security that does not rest on the CA system (including where that goes next: the read key never leaving the client, or PKI with a client-only private key). The page now assumes the reader knows git and only covers the delta. Also corrects the business-model answer: the client being open source IS the distribution strategy, with services built on top — not \"no revenue attached\"."),
    ('v0.1.23', '2026-08-14', 'obj-cas-imm-89a142ee3598',
     "A freshness window on the mutable HEAD pointer. The ref was the last per-page-view network request left; it is now checked at most once every ref_ttl_s seconds (120 by default, configurable in deploy/vault.json), so reading inside the window costs zero requests and server load scales with readers rather than page views. The cost is a bounded propagation delay — a new commit appears within the window at worst — and \"check for new commit\" forces a fetch that ignores it. The vault panel logs the reused ref as TTL and counts down live to the next check."),
    ('v0.1.22', '2026-08-14', 'obj-cas-imm-d9ac70d78c31',
     "Kills the load-time flicker of the vault panel. The panel's remembered width and open state were restored by the reader script, which loads asynchronously — so the panel painted at its CSS default width, then jumped and slid open a beat later. Restoration now happens synchronously, before the first paint, and the slide transition is suppressed until state has settled. Opening and closing the panel by hand still animates; restoring it never does."),
    ('v0.1.21', '2026-08-14', 'obj-cas-imm-5a60bc3bf25b',
     "Object bodies in the vault panel are now syntax-coloured like an editor — keys, strings, numbers, literals and punctuation each get their own colour — and word wrapping is off, so structure survives and long values (base64 ciphertext, object ids) scroll horizontally instead of folding into a wall of text. Highlighting is applied only when the decrypted object actually parses as JSON, so markdown blobs stay plain."),
    ('v0.1.20', '2026-08-14', 'obj-cas-imm-78146d2f4f86',
     "The vault panel now links to the page that explains it. There is a compact “how this works” link in the panel header (always visible) and a fuller card at the foot of the panel pointing at deploy/how-this-works.html — the panel is where you are when the question occurs to you, so it is where the answer should be offered."),
    ('v0.1.19', '2026-08-14', 'obj-cas-imm-fe67d9589a2e',
     "Fixes the resize grip, which shipped in v0.1.18 but was unusable: it was absolutely positioned inside the panel\'s scrolling area, so it scrolled out of reach as soon as you moved down the object list, and at 6px fully transparent it was invisible anyway. The panel is now a flex shell — a fixed 12px drag rail with a visible handle, plus a separately scrolling body — and dragging uses pointer events with capture (mouse, pen and touch). Double-click the rail to reset the width."),
    ('v0.1.18', '2026-08-14', 'obj-cas-imm-6eded1c95732',
     'Vault panel becomes an object inspector: every row now shows what the object IS (ref/commit/tree/blob), WHY it was read, and — on click — its decrypted contents, pretty-printed for JSON. The panel is width-resizable (dragged from its left edge, remembered). Plus a real optimisation the panel made obvious: the path→blob index is a pure function of the commit id, so it is now memoised in localStorage — a first visit walks every tree to learn the encrypted filenames, but subsequent visits to an unchanged commit read zero tree objects.'),
    ('v0.1.17', '2026-08-14', 'obj-cas-imm-9d5b50f68679',
     'Vault panel: a "clear list" button that resets the request log and counters without touching the caches (so you can see exactly which objects one page needs); the panel\'s open/closed state now persists across navigation and reloads; cached objects record when they were stored and the panel shows their age. Navigation now scrolls to the top of the content rather than the top of the document. New page: deploy/how-this-works.html — the full architecture with hand-drawn SVG diagrams of the two-session publishing pipeline and the client-side read path.'),
    ('v0.1.16', '2026-08-12', 'obj-cas-imm-34684a789fe6',
     'New /why page answering the sharpest public criticism of the project ("I see no market or value whatsoever") directly and without marketing: who actually has the problem, why git-crypt/Dropbox/S3+KMS do not cover it, the market question answered plainly (the CLI has no revenue attached; hosting is the commercial layer; no TAM claims), where the criticism is right, and a twelve-question FAQ pre-answering the promised follow-ups.'),
    ('v0.1.15', '2026-08-12', 'obj-cas-imm-0959988dd4fe',
     'New Deploy section: self-hosting guidance rendered LIVE in the browser from an encrypted SG/Send vault, using a published read-only key — ciphertext over CORS, AES-256-GCM decryption via Web Crypto, no copy stored on this site and no rebuild when the SG/Send team pushes. Includes a three-tier cache (session memory, permanent Cache API for immutable objects, always-fresh ref) and a vault debug panel showing the HEAD commit, per-object request log, and cache hit/miss stats.'),
    ('v0.1.14', '2026-08-12', 'obj-cas-imm-3b54c02dbb96',
     'Two new pages, both linked this time: docs/exposed-vault-key.html (the rotation runbook plus the case study of this site\'s own key leak) and briefs.html (cross-team briefs — which v0.1.13 built but never registered, so nothing linked to it). New validator rule: every generated page must be reachable from another page, or the build fails. Added a fourth CLI-team ask: history-preserving rekey.'),
    ('v0.1.13', '2026-08-12', 'obj-cas-imm-5168ef3fe1a7',
     'SECURITY: the vault passphrase had been written into admin/build/validate.js as an anti-leak tripwire regex — which put the literal secret into a tracked, public file (present in 3 commits). Removed; the tripwire now reads the secret from the gitignored local/ tier and scans for it, so it can never be hardcoded again. The key must be treated as compromised and rotated. Also: a /briefs page collecting the cross-team briefs (multi-agent collaboration log), and a "contacting the server" notice before network commands in the browser terminal.'),
    ('v0.1.12', '2026-08-11', 'obj-cas-imm-e8ceb3fc2239',
     'In-browser clone completes: serial-executor shim for Pyodide (WebAssembly cannot spawn threads, so all parallel blob transfers run sequentially in the browser) — validated natively against the live server with thread creation disabled: full 225-blob clone of this site vault. A serial/auto-detect mode is proposed upstream to the sgit CLI.'),
    ('v0.1.11', '2026-08-11', 'obj-cas-imm-c9afa76a79cb',
     'Browser-transport fix for in-browser clone: drop the redundant X-API-Key header (the servers CORS-allow x-sgraph-access-token but not x-api-key, and one disallowed header fails the whole preflight — diagnosed live from the first user clone attempt); CORS/network failures now surface as readable HTTP 599 errors instead of a Pyodide SystemError.'),
    ('v0.1.10', '2026-08-11', 'obj-cas-imm-deac6363bff9',
     'In-browser terminal on /try: the real sgit CLI in-process (init, commit, status, history — and network commands via a browser XHR transport: clone/push/pull straight to the SG/Send servers), plus a busybox of file commands over the in-memory filesystem. Key hygiene: every example key on the site is now an obviously-invalid placeholder (format-valid example keys are squattable namespaces), enforced by a new validator rule.'),
    ('v0.1.9', '2026-08-11', 'obj-cas-imm-83b8c23a1baa',
     '"Try sgit in your browser" page: the real sgit-ai wheel running client-side under Pyodide (verified in headless Chromium first) — key derivation, encrypt/decrypt, an in-memory vault round trip, and a Python REPL. Plus: bootstrap fast-path for static hosting (no 2.5s bridge wait on GitHub Pages), CNAME for sgit.ai, and GitHub Pages deployment via Actions in the SGit-AI__Website repo.'),
    ('v0.1.8', '2026-08-11', 'obj-cas-imm-775783f31110',
     'Skills promoted to a top-level nav item with a new /skills page and the three agent skills shipped in the vault (latest versions, verbatim); llms.txt added at the vault root — encrypted for key-holders today, a standard public llms.txt when the site deploys to GitHub Pages; Home nav link retired (the brand mark covers it).'),
    ('v0.1.7', '2026-08-11', 'obj-cas-imm-c226a3aff160',
     'SG/Vault section rebuilt from the official docs bundle: corrected security-page structure-key claim to current reality, git page aligned with the publishing guide (three-rule boundary, leak audit, GitHub round trip, restore drill), new pages for static hosting on GitHub Pages, sub-vaults, and no-code content authoring; .gitignore extended with work/ and *.pem rules.'),
    ('v0.1.6', '2026-08-11', 'obj-cas-imm-f62d9bd2d0d4',
     'Corrected git integration to the side-by-side design: git now tracks the encrypted .sg_vault store (only the plaintext local/ folder is excluded), so a git remote doubles as a zero-knowledge mirror of the vault. Pattern documented on the git-and-vaults page.'),
    ('v0.1.5', '2026-08-11', 'obj-cas-imm-353038cc3e56',
     'Git integration: .gitignore (keeps .sg_vault/ — above all local/ keys and token — plus git metadata and build noise out of git and out of vault snapshots) and .gitattributes (raw sgit store files marked binary/-diff/-merge; generated *.html marked linguist-generated).'),
    ('v0.1.4', '2026-08-11', 'obj-cas-imm-90254d9591ff',
     'New SG/Vault section — for now the official sgraph platform documentation: SG/Vault & the platform, building vault apps, the window.sg bridge & host capabilities, and "git repos inside vaults" (engineering preview of the pure-Python git reader, verified against a real 906-commit repo).'),
    ('v0.1.3', '2026-08-11', 'obj-cas-imm-46a8b14d4fca',
     'Beta status (in production use), light theme, admin & engineering section, per-push version badge on every page, SG/Vault & SG/Send now link to sgraph.ai, design-improvements brief for Claude Code.'),
    ('v0.1.2', '2026-08-11', 'obj-cas-imm-c3084abbba8c',
     'Replaced the proposal app with the sgit.ai MVP site: 12 individually-navigable pages, shared CSS/JS loaded through the SG bridge, full-strength keys in all examples.'),
    ('v0.1.1', '2026-08-11', 'obj-cas-imm-7f1fbacf0485',
     'Initial vault app: the positioning & messaging proposal microsite with an embedded landing-page prototype.'),
]

ROOT  = find_vault_root()
ADMIN = os.path.join(ROOT, 'admin')

BOOT = """<script>
(function(){var R=document.documentElement.getAttribute('data-root')||'';var C=[R,'','../','/'].filter(function(v,i,a){return a.indexOf(v)===i});
function wait(ms){return new Promise(function(res){var t=Date.now();(function p(){if(window.sg)return res(window.sg);if(Date.now()-t>ms)return res(null);setTimeout(p,60)})()})}
function grab(sg,p){return new Promise(function(res){(async function(){if(sg&&sg.vfs&&sg.vfs.readText){try{var t=await sg.vfs.readText(p);if(t)return res(t)}catch(e){}}try{var r=await fetch(p);if(r.ok)return res(await r.text())}catch(e){}res(null)})()})}
async function css(sg){for(var i=0;i<C.length;i++){var p=C[i]+'assets/site.css';if(sg&&sg.loadCss){try{await sg.loadCss(p);return}catch(e){}}var t=await grab(sg,p);if(t){var s=document.createElement('style');s.textContent=t;document.head.appendChild(s);return}}}
async function js(sg){for(var i=0;i<C.length;i++){var p=C[i]+'assets/site.js';if(sg&&sg.loadJs){try{await sg.loadJs(p);return}catch(e){}}var t=await grab(sg,p);if(t){try{(0,eval)(t)}catch(e){console.error('[site] js failed',e)}return}}}
async function boot(){var inVault=false;try{inVault=(window!==window.parent)||location.protocol==='blob:'}catch(e){inVault=true}
var sg=inVault?await wait(2500):null;await css(sg);await js(sg);document.documentElement.classList.add('ready');try{window.parent&&window.parent.postMessage({type:'sg-app-ready'},'*')}catch(e){}}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',boot);else boot();})();
</script>"""

# The fade-in hides the unstyled flash while site.css is bridge-loaded. It must never be able
# to leave the page invisible: a crawler that applies CSS but does not run our bootstrap would
# otherwise see a fully hidden body — invisible to a reader and a hidden-text signal to an
# indexer. Two failsafes: <noscript> reveals immediately, and a CSS-only animation reveals at
# 1.6s regardless of why the bootstrap never arrived.
CRITICAL = ("<style>html{background:#faf9f5}body{margin:0;background:#faf9f5;color:#1c1d21;"
            "font-family:ui-sans-serif,system-ui,sans-serif;opacity:0;transition:opacity .25s;"
            "animation:sg-reveal 0s linear 1.6s forwards}"
            "html.ready body{opacity:1;animation:none}"
            "@keyframes sg-reveal{to{opacity:1}}</style>"
            "<noscript><style>body{opacity:1;animation:none}</style></noscript>")

def nav(p, here):
    def cls(k):
        return 'nl here' if k == here else 'nl'
    return f"""<nav class="site"><div class="row">
  <a class="brand" href="{p}index.html">sgit<span>.ai</span></a>
  <span class="stage-pill">beta</span>
  <a class="ver" href="{p}admin/versions.html" title="Site release history">{SITE_VERSION}</a>
  <a class="{cls('why')}" href="{p}why/index.html">Why</a>
  <a class="{cls('try')}" href="{p}try/index.html">Try</a>
  <a class="{cls('demos')}" href="{p}demos/index.html">Demos</a>
  <a class="{cls('catalogue')}" href="{p}catalogue/index.html">Catalogue</a>
  <a class="{cls('vaults')}" href="{p}vaults/index.html">Vaults</a>
  <a class="{cls('use-cases')}" href="{p}use-cases/index.html">Use Cases</a>
  <a class="{cls('case-studies')}" href="{p}case-studies/index.html">Case Studies</a>
  <a class="{cls('docs')}" href="{p}docs/index.html">Docs</a>
  <a class="{cls('vault')}" href="{p}vault/index.html">SG/Vault</a>
  <a class="{cls('deploy')}" href="{p}deploy/index.html">Deploy</a>
  <a class="{cls('skills')}" href="{p}skills/index.html">Skills</a>
  <a class="{cls('security')}" href="{p}security/index.html">Security</a>
  <a class="gh" href="https://github.com/SGit-AI/SGit-AI__CLI">★ GitHub</a>
</div></nav>"""

def footer(p, md=''):
    return f"""<footer class="site"><div class="cols">
  <div>
    <div class="brandline">sgit<span>.ai</span></div>
    <p>sgit is git for encrypted vaults — clone, commit, branch and merge files that are encrypted with AES-256-GCM before they leave your machine. Open source, Apache-2.0, in beta and powering production workflows.</p>
    <p class="vaultnote">🔒 This site is itself served from an encrypted SG/Send vault — the page you are reading was decrypted in your browser. The medium is the message.</p>
    <p class="verline">site <a href="{p}admin/versions.html">{SITE_VERSION}</a> · <a href="{p}admin/index.html">engineering</a> · <a href="{md}" title="The same page as plain markdown — for agents, and for reading without the styling">this page as markdown</a></p>
  </div>
  <div>
    <h4>Docs</h4>
    <a href="{p}docs/what-is-sgit.html">What is sgit</a>
    <a href="{p}docs/installation.html">Installation</a>
    <a href="{p}docs/quickstart.html">Quickstart</a>
    <a href="{p}docs/sgit-for-git-users.html">sgit for git users</a>
    <a href="{p}docs/agents.html">Working with AI agents</a>
    <a href="{p}docs/limitations.html">When NOT to use sgit</a>
  </div>
  <div>
    <h4>SG/Vault platform</h4>
    <a href="{p}vault/index.html">SG/Vault &amp; the platform</a>
    <a href="{p}vault/vault-apps.html">Building vault apps</a>
    <a href="{p}vault/sg-bridge.html">The window.sg bridge</a>
    <a href="{p}vault/content-authoring.html">Content authoring</a>
    <a href="{p}vault/sub-vaults.html">Sub-vaults</a>
    <a href="{p}vault/git-and-vaults.html">Git repos inside vaults</a>
    <a href="{p}vault/static-hosting.html">Static hosting</a>
    <a href="https://sgraph.ai">More at sgraph.ai</a>
  </div>
  <div>
    <h4>Project</h4>
    <a href="https://github.com/SGit-AI/SGit-AI__CLI">GitHub</a>
    <a href="{p}security/index.html">Security</a>
    <a href="{p}why/index.html">Why does this exist?</a>
    <a href="{p}use-cases/index.html">Use cases</a>
    <a href="{p}case-studies/index.html">Case studies</a>
    <a href="{p}skills/index.html">Skills for AI agents</a>
    <a href="{p}briefs/index.html">Cross-team briefs</a>
    <a href="{p}llms.txt">llms.txt</a>
    <a href="{p}llms-full.txt">llms-full.txt</a>
    <a href="{p}admin/index.html">Admin &amp; engineering</a>
    <a href="{p}admin/versions.html">Release history</a>
  </div>
</div></footer>"""

# ---------------------------------------------------------------- structured data
# Google's 2026 AI-optimisation guidance is explicit that structured data is not required
# to appear in generative-AI features — "it is still SEO". It is included here for a
# different and specific reason: "sgit" is an ambiguous string. It also names an Android
# Git client, an Indian engineering college, and a class of shell shortcut, and Google's
# AI Overview for the bare query currently disambiguates between them while sourcing this
# project from PyPI. sameAs links the site to the identifiers that already rank, which is
# how an entity gets resolved to the right thing rather than to the most popular thing.

def json_ld(path, title, desc):
    site = {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": "sgit",
        "alternateName": ["sgit-ai", "sgit CLI"],
        "applicationCategory": "DeveloperApplication",
        "applicationSubCategory": "Version control",
        "operatingSystem": "macOS, Linux, Windows",
        "url": "https://sgit.ai",
        "downloadUrl": "https://pypi.org/project/sgit-ai/",
        "installUrl": "https://pypi.org/project/sgit-ai/",
        "softwareHelp": "https://sgit.ai/docs/",
        "license": "https://www.apache.org/licenses/LICENSE-2.0",
        "programmingLanguage": "Python",
        "softwareRequirements": "Python >= 3.11",
        "description": ("git for encrypted vaults: clone, commit, branch and merge files that are "
                        "encrypted client-side with AES-256-GCM before they leave your machine. The "
                        "server stores ciphertext under opaque ids and never sees filenames, contents "
                        "or commit messages."),
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "sameAs": ["https://pypi.org/project/sgit-ai/",
                   "https://github.com/SGit-AI/SGit-AI__CLI",
                   "https://github.com/SGit-AI/SGit-AI__Website"],
        "disambiguatingDescription": ("Distinct from SGit, the Android Git client, and from SGIT, "
                                      "the Dr. Samuel George Institute of Engineering and Technology. "
                                      "This is the encrypted-vault CLI published to PyPI as sgit-ai."),
    }
    page_node = {"@context": "https://schema.org",
                 "@type": "TechArticle" if path != 'index.html' else "WebSite",
                 "name": title, "headline": title, "description": desc,
                 "url": f"https://sgit.ai/{path}",
                 "inLanguage": "en",
                 "isPartOf": {"@type": "WebSite", "name": "sgit.ai", "url": "https://sgit.ai"},
                 "about": {"@type": "SoftwareApplication", "name": "sgit",
                           "sameAs": "https://pypi.org/project/sgit-ai/"}}
    blocks = [site, page_node] if path == 'index.html' else [page_node]
    return '\n'.join('<script type="application/ld+json">' + json.dumps(b, ensure_ascii=False)
                      + '</script>' for b in blocks)


def page(path, title, desc, here, body):
    p = '../' if '/' in path else ''
    md_name = os.path.basename(path)[:-5] + '.md'
    html = f"""<!doctype html>
<html lang="en" data-root="{p}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://sgit.ai/{path}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="sgit.ai">
<meta property="og:url" content="https://sgit.ai/{path}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta name="twitter:card" content="summary">
<link rel="alternate" type="text/markdown" href="{md_name}" title="This page as markdown">
{json_ld(path, title, desc)}
{CRITICAL}
</head>
<body>

{nav(p, here)}

{body}

{footer(p, os.path.basename(path)[:-5] + '.md')}

{BOOT}
</body>
</html>
"""
    out = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w') as f:
        f.write(html)
    print('wrote', path, f'({len(html)} bytes)')


def versions_body():
    rows = '\n'.join(
        f'    <tr><td class="vnum">{v}</td><td>{d}</td><td class="vid">{c}</td><td>{note}</td></tr>'
        for v, d, c, note in VERSION_LOG)
    return f"""<main class="doc">
  <p class="crumb"><a href="../index.html">Home</a> / <a href="index.html">Admin</a> / Versions</p>
  <h1>Release history</h1>
  <p class="lead">This site ships by pushing its vault, and the site version — <b>{SITE_VERSION}</b>, shown in the nav of every page — increments on every push. Each release is also an sgit commit, so the vault's own <code>sgit history log</code> is the authoritative audit trail; this page is the human-readable index of it.</p>
  <div class="tablewrap"><table class="vers">
    <tr><th>Version</th><th>Date</th><th>Vault commit</th><th>Changes</th></tr>
{rows}
  </table></div>
  <p class="small dim">Numbering: v0.1.n while the site is in its first structure; the middle digit will bump on structural redesigns. The "vault commit" of the newest row reads "this release" because the commit ID only exists once the release is committed — it is recorded here retroactively by the next release.</p>
  <div class="pagenav"><a href="index.html">← Admin &amp; engineering</a><span></span></div>
</main>"""

# ============================================================ markdown mirror
# Every page is also written as .md next to its .html. This is not a nicety: agents
# are a first-class audience for this site, and asking them to parse styled HTML to
# reach guidance is a tax with no upside. The markdown is generated from the same
# body the HTML is built from, so the two can never drift.
#
# Internal .html links are rewritten to .md so an agent can traverse the whole site
# without ever touching HTML. Anything visual (SVG diagrams, terminal chrome) is
# reduced to its caption or its plain text — the words survive, the styling does not.

class Markdown_Writer(HTMLParser):
    SKIP       = {'script', 'style', 'svg', 'button', 'nav', 'footer'}
    SKIP_CLASS = {'capnum'}          # decoration whose text says nothing in prose
    VOID       = {'br', 'img', 'hr', 'input', 'meta', 'link', 'source'}
    BLOCK  = {'p', 'div', 'section', 'article', 'main', 'header', 'ul', 'ol', 'table', 'tr', 'blockquote', 'details'}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out       = []          # emitted chunks
        self.skipst    = []          # tag stack while inside a skipped element
        self.pre       = 0           # depth inside <pre>
        self.list      = []          # stack of ('ul'|'ol', counter)
        self.row       = None        # cells of the table row being built
        self.thead     = False
        self.cols      = 0
        self.href      = None
        self.link_text = None
        self.figcap    = False

    # ---- helpers
    def emit(self, s):
        if self.skipst: return
        if self.link_text is not None: self.link_text.append(s)
        elif self.row is not None:     self.row[-1] += s
        else:                          self.out.append(s)

    def block(self):
        if self.out and not self.out[-1].endswith('\n\n'):
            self.out.append('\n\n' if self.out[-1].strip() else '\n')

    # ---- tags
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if self.skipst:                                  # already inside a skipped subtree
            if tag not in self.VOID: self.skipst.append(tag)
            return
        if tag in self.SKIP or a.get('class') in self.SKIP_CLASS:
            self.skipst = [tag]
            return

        if   tag == 'pre':  self.pre += 1; self.block(); self.emit('```\n')
        elif tag == 'code' and not self.pre: self.emit('`')
        elif tag in ('b', 'strong'): self.emit('**')
        elif tag in ('em', 'i'):     self.emit('*')
        elif tag == 'br':            self.emit('  \n' if not self.pre else '\n')
        elif tag == 'a':
            self.href = a.get('href'); self.link_text = []
        elif tag in ('h1', 'h2', 'h3', 'h4'):
            self.block(); self.emit('#' * int(tag[1]) + ' ')
        elif tag in ('ul', 'ol'):
            self.block(); self.list.append([tag, 0])
        elif tag == 'li':
            if not self.list: self.list.append(['ul', 0])
            self.list[-1][1] += 1
            kind, n = self.list[-1]
            indent = '  ' * (len(self.list) - 1)
            self.out.append('\n' + indent + (f'{n}. ' if kind == 'ol' else '- '))
        elif tag == 'table':
            self.block(); self.thead = True; self.cols = 0
        elif tag == 'tr':
            self.row = []
        elif tag in ('td', 'th'):
            if self.row is not None: self.row.append('')
        elif tag == 'blockquote':
            self.block(); self.emit('> ')
        elif tag == 'summary':
            self.block(); self.emit('**')
        elif tag in self.BLOCK:
            self.block()
        if a.get('class') == 'figcap': self.figcap = True

    def handle_endtag(self, tag):
        if self.skipst:
            if tag in self.skipst:
                while self.skipst and self.skipst.pop() != tag:
                    pass
            if not self.skipst and tag == 'svg':
                self.out.append('\n\n*[diagram]*')
            return

        if   tag == 'pre': self.pre = max(0, self.pre - 1); self.emit('\n```\n\n')
        elif tag == 'code' and not self.pre: self.emit('`')
        elif tag in ('b', 'strong'): self.emit('**')
        elif tag in ('em', 'i'):     self.emit('*')
        elif tag == 'a':
            text = ''.join(self.link_text or []).strip()
            href, self.link_text, self.href = self.href, None, None
            if not text: return
            if href and not href.startswith(('http', 'mailto:', '#')):
                href = re.sub(r'\.html(#|$)', r'.md\1', href)
            self.emit(f'[{text}]({href})' if href else text)
        elif tag in ('h1', 'h2', 'h3', 'h4'): self.out.append('\n\n')
        elif tag in ('ul', 'ol'):
            if self.list: self.list.pop()
            self.out.append('\n')
        elif tag == 'tr':
            cells = [' '.join(c.split()) for c in (self.row or [])]
            self.row = None
            if not cells: return
            self.out.append('\n| ' + ' | '.join(cells) + ' |')
            if self.thead:
                self.out.append('\n|' + '---|' * len(cells))
                self.thead = False
        elif tag == 'table':  self.out.append('\n\n')
        elif tag == 'summary': self.emit('**\n')
        elif tag in self.BLOCK: self.block()
        self.figcap = False

    def handle_data(self, data):
        if self.skipst: return
        if self.pre:
            self.emit(data)
        else:
            text = re.sub(r'\s+', ' ', data)
            if text.strip() or (self.out and self.out[-1].endswith((')', '`', '*'))):
                self.emit(text)

    def markdown(self):
        md = ''.join(self.out)
        md = md.replace('\u00a0', ' ')
        md = re.sub(r'[ \t]+\n', '\n', md)
        md = re.sub(r'\n{3,}', '\n\n', md)
        md = re.sub(r'\n +([-*] |\d+\. )', r'\n\1', md)      # un-indent top-level bullets
        return md.strip() + '\n'


def to_markdown(body):
    w = Markdown_Writer()
    w.feed(body)
    return w.markdown()


def write_md(path, title, desc, body):
    depth = path.count('/')
    root  = '../' * depth
    md    = (f'# {title}\n\n> {desc}\n\n'
             f'*Source: <https://sgit.ai/{path}> · site {SITE_VERSION} · '
             f'this file is generated from the same content as the page, so the two cannot drift. '
             f'Every page on this site has a `.md` twin; internal links below point at them.*\n\n---\n\n'
             + to_markdown(body)
             + f'\n\n---\n\n*[Site index for agents]({root}llms.txt) · '
               f'[HTML version](https://sgit.ai/{path})*\n')
    out = os.path.join(ROOT, path[:-5] + '.md')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w') as f:
        f.write(md)
    return len(md)



# ============================================================ llms.txt
# Generated from PAGES, so it cannot go stale — the same reason the orphan and
# link checks exist. Every entry points at the .md twin: an agent following this
# index never has to parse HTML.

LLMS_PREAMBLE = """# sgit.ai

> sgit is git for encrypted vaults: clone, commit, branch and merge files that are
> encrypted client-side (AES-256-GCM) before they leave your machine. The server stores
> ciphertext under opaque IDs — it never sees filenames, contents, or commit messages.
> This site is the official documentation for sgit and the SGraph vault platform
> (SG/Vault, SG/Send) — and is itself served from an encrypted vault.

Every page below is markdown, generated from the same source as the HTML page at the
same path (swap `.md` for `.html`). Links inside the markdown point at markdown, so you
can traverse the entire site without parsing HTML.

Notes for agents:
- sgit is in beta and powers production workflows. Honest edges: /docs/limitations.md
- Install: pip install sgit-ai (Python >= 3.11; entry points `sgit` and `sgit-ai`)
- Vault keys are full-strength generated keys (`passphrase:vault_id`). No password reset exists.
- Never write a vault key into a tracked file. See /docs/exposed-vault-key.md for what that costs.
- The agent-facing command is `sgit write <path> --file <f> --message <m> --push --json`;
  every read path has a --json flag.
- Cross-session state pattern: clone/pull at session start, commit + push at session end.
- Task-shaped guidance with recipes and agent briefs lives under /use-cases/.

If your tooling cannot follow links out of this file, fetch /llms-full.txt — every page of
this site concatenated into one document (~155 KB). One request gets the complete set.

Quick answers (so you do not need a second request for the common questions):
- Does sgit do the git operations you know? Yes for: init, create, clone, status, commit,
  push, pull, fetch, branch (new/list/switch/checkout), merge with conflict resolution,
  history log/diff/show/revert/reset, stash. No for: pull requests (a hosting-platform
  construct layered on merge, not a git primitive), a staging area or partial commits
  (a commit snapshots the whole folder), bisect, blame, rebase, cherry-pick, hooks,
  submodules and tags. Full mapping: /docs/sgit-for-git-users.md
- The three deliberate differences from git: no staging area; every clone gets its own
  private branch and publishing to a shared branch is explicit; the vault key is address,
  credential and encryption key in one string.
- What the server can see: the vault ID, the size of each encrypted object, and request
  timing. Never filenames, contents, or commit messages. /security.md
- Read access is a separate, one-way-derived key: publishable, cannot be turned into write
  access, works against any server holding the ciphertext. This site publishes one.
- Crypto: AES-256-GCM, PBKDF2-HMAC-SHA256 at 600k iterations, HKDF-SHA256. No custom
  primitives; output matches the browser Web Crypto API byte for byte.
- sgit is beta; it has no compliance certification of any kind.
"""

LLMS_SECTIONS = [
    ('why',       'Why this exists'),
    ('demos',     'Demos (live end-to-end examples with published read keys)'),
    ('catalogue', 'Catalogue (the index of published vaults — read keys, shapes, evidence and write-key status)'),
    ('vaults', 'Published vaults (one page per vault: description, features, live embed, and the read key that opens it)'),
    ('use-cases', 'Use cases (task-shaped guidance: recipe, evidence status, agent brief)'),
    ('case-studies', 'Case studies (worked accounts of what actually happened, with numbers)'),
    ('docs',      'Docs'),
    ('vault',     'SG/Vault platform'),
    ('deploy',    'Deploy (rendered live from an encrypted vault)'),
    ('try',       'Try it'),
    ('skills',    'Skills (packaged instructions for AI agents)'),
    ('briefs',    'Cross-team briefs'),
    ('home',      'Optional'),
    ('security',  'Optional'),
    ('admin',     'Optional'),
]

LLMS_FACTS = {
    'docs/sgit-for-git-users.html': 'The three differences: no staging area; private clone branch per machine or agent with explicit publishing; the vault key is address + credential + encryption key in one string.',
    'docs/limitations.html':        'Not a secrets manager; no partial commits; no key recovery; the server cannot index or search; beta.',
    'docs/two-branch-model.html':   'Every clone commits to its own private branch; pushing to a shared named branch is a separate, explicit act.',
    'security.html':                'The server sees the vault ID, object sizes and request timing — nothing else. Sizes and timing are an acknowledged side channel.',
    'docs/agents.html':             'sgit write <path> --file <f> --message <m> --push --json is the one-shot agent command; every read path takes --json.',
    'docs/quickstart.html':         'sgit create <name> then commit/push; the vault key is printed once and there is no reset.',
    'docs/installation.html':       'pip install sgit-ai — Python >= 3.11, two runtime dependencies, entry points sgit and sgit-ai.',
    'use-cases/health-regulated.html': 'No HIPAA, ISO 27001, SOC 2 or GDPR finding exists; client-side encryption does not by itself make processing lawful.',
    'deploy/how-this-works.html':   'The ref is checked at most once per 120s freshness window; every other object is content-addressed and cached forever.',
}

LLMS_EXTRA = {
    'skills': ['- [use sgit and vaults](/skills/use_sgit-and-vaults__SKILL.md): the CLI + cross-session persistent state',
               '- [create vault apps](/skills/create-vault-apps__SKILL.md): build an app that lives inside a vault',
               '- [create vault content](/skills/create-vault-content__SKILL.md): author _page.json layouts and vault markdown'],
}


def write_llms(pages):
    out, seen, optional = [LLMS_PREAMBLE], set(), []
    for key, heading in LLMS_SECTIONS:
        rows = []
        for path, title, desc, here, _ in pages:
            if here != key or path in seen:
                continue
            seen.add(path)
            name = title.split(' — ')[0].split(' | ')[0]
            fact = LLMS_FACTS.get(path)
            rows.append(f'- [{name}](/{path[:-5]}.md): {desc}'
                        + (f' **Key fact:** {fact}' if fact else ''))
        rows += LLMS_EXTRA.get(key, [])
        if not rows:
            continue
        if heading == 'Optional':
            optional += rows
        else:
            out.append(f'## {heading}\n' + '\n'.join(rows) + '\n')
    missing = [p for p, *_ in pages if p not in seen]
    if missing:
        raise SystemExit('llms.txt would omit these pages (add their section to LLMS_SECTIONS): '
                         + ', '.join(missing))
    if optional:
        out.append('## Optional\n' + '\n'.join(optional) + '\n')
    text = '\n'.join(out)
    with open(os.path.join(ROOT, 'llms.txt'), 'w') as f:
        f.write(text)
    return text




# ============================================================ crawl + agent surface
# An agent reported that it could fetch llms.txt but could not follow a link out of it —
# its harness only allows URLs a search has already returned, and the site did not rank for
# its own positioning language. Two consequences, both handled here: the site has to be
# crawlable (robots + sitemap, and a page that is not invisible without JS — see CRITICAL),
# and the index has to be useful to an agent that will never follow a link, which means
# self-sufficient answers in llms.txt and a single-fetch concatenation in llms-full.txt.

def write_robots():
    text = f"""# sgit.ai — everything here is public and intended to be indexed.
User-agent: *
Allow: /

Sitemap: https://sgit.ai/sitemap.xml

# For agents and LLMs:
#   https://sgit.ai/llms.txt       annotated map of the site, one line per page
#   https://sgit.ai/llms-full.txt  every page concatenated — one fetch gets everything
# Every page is also available as markdown at the same path with .html swapped for .md.
"""
    with open(os.path.join(ROOT, 'robots.txt'), 'w') as f:
        f.write(text)
    return text


def write_sitemap(pages, today):
    urls = []
    for path, *_ in pages:
        pri = '1.0' if path == 'index.html' else ('0.8' if '/' not in path else '0.6')
        urls.append(f'  <url>\n    <loc>https://sgit.ai/{path}</loc>\n'
                    f'    <lastmod>{today}</lastmod>\n    <priority>{pri}</priority>\n  </url>')
    for extra in ('llms.txt', 'llms-full.txt'):
        urls.append(f'  <url>\n    <loc>https://sgit.ai/{extra}</loc>\n'
                    f'    <lastmod>{today}</lastmod>\n    <priority>0.5</priority>\n  </url>')
    text = ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + '\n'.join(urls) + '\n</urlset>\n')
    with open(os.path.join(ROOT, 'sitemap.xml'), 'w') as f:
        f.write(text)
    return text


def write_llms_full(pages):
    """Every page in one document. For agents whose harness will not follow a link out of a
    fetched file — a common restriction — this is the difference between the documentation
    being reachable and being unreachable."""
    parts = [f"""# sgit.ai — complete documentation, single file

> Every page of https://sgit.ai concatenated into one document, generated at build time
> ({SITE_VERSION}). Nothing here needs a second request. Individual pages live at the paths
> shown below, as markdown (`.md`) and as HTML (`.html`); the annotated map is /llms.txt.
>
> sgit is git for encrypted vaults: clone, commit, branch and merge files that are encrypted
> client-side (AES-256-GCM) before they leave your machine. The server stores ciphertext under
> opaque IDs — it never sees filenames, contents, or commit messages.
"""]
    for path, title, desc, here, body in pages:
        parts.append(f'\n\n{"=" * 78}\n# {title}\n\n> {desc}\n>\n> Page: https://sgit.ai/{path}\n\n'
                     + to_markdown(body))
    text = '\n'.join(parts).rstrip() + '\n'
    with open(os.path.join(ROOT, 'llms-full.txt'), 'w') as f:
        f.write(text)
    return text




# ============================================================ page registry
# Content lives in admin/content/<path>.html — one file per page, holding only the <main>
# body. This file is the engine: template, markdown mirror, llms/robots/sitemap, and the
# registry below. Adding a page is a new content file plus one row here; nothing in this
# file grows with the site.

MANIFEST = os.path.join(ADMIN, 'content', 'pages.json')


def load_pages():
    with open(MANIFEST) as f:
        rows = json.load(f)
    pages = []
    for r in rows:
        if r.get('dynamic') == 'versions':
            body = versions_body()
        else:
            with open(os.path.join(ADMIN, 'content', r['path'])) as f:
                body = f.read().rstrip('\n')
        pages.append((r['path'], r['title'], r['desc'], r['section'], body))
    return pages


PAGES = load_pages()

md_total = 0
for path, title, desc, here, body in PAGES:
    page(path, title, desc, here, body)
    md_total += write_md(path, title, desc, body)
print(f'wrote {len(PAGES)} markdown mirrors ({md_total} bytes)')
print('wrote llms.txt (%d bytes)' % len(write_llms(PAGES)))
print('wrote llms-full.txt (%d bytes)' % len(write_llms_full(PAGES)))
print('wrote robots.txt (%d bytes)' % len(write_robots()))
print('wrote sitemap.xml (%d bytes)' % len(write_sitemap(PAGES, BUILD_DATE)))
print('done:', len(PAGES), 'pages —', SITE_VERSION)
