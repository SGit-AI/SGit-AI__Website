# Moving the SGit Newsroom to newsroom.sgit.ai, migration brief

> For the agent working on newsroom.sgit.ai: what moves from sgit.ai (65 articles and their graphs, the desk, the newsletter, the reader account and SG Meter), where each piece is in the source, the URL plan, five phases with acceptance checks, moving reader data between origins, what not to break, and the decisions that are Dinis Cruz's.

*Source: <https://sgit.ai/docs/briefs/newsroom-move-to-newsroom-sgit-ai.html> · site v0.7.43 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../index.md) / [Docs](../index.md) / [Briefs](index.md) / Moving the newsroom

Brief · for the newsroom.sgit.ai session · 10 October 2026

# Moving the SGit Newsroom from sgit.ai to newsroom.sgit.ai (migration brief)

The SGit Newsroom grew up inside sgit.ai: 65 articles since 17 August, 47 of them in the first ten days of October, plus the desk that places them, a newsletter, and a reader account with a meter, personas and a way to send us one's reading. It has outgrown a product site. It moves to newsroom.sgit.ai, which until now has argued for exactly this kind of newsroom without running one. This brief is for the agent working in the newsroom.sgit.ai repository: what exists, where every piece of it is, what to build on your side, the order to do it in, and what not to break.

**Decided by Dinis Cruz, 10 October 2026.** The newsroom moves to newsroom.sgit.ai. The site there today becomes the reference for the design it argued. sgit.ai keeps its copies for links and reference for a while, drops them from its top navigation, and decommissions them later. Everything stays client side: no server, no database, reader data only in the reader's browser.

## Start here

1. **Download the bundle:** [newsroom-move-bundle.zip](files/newsroom-move-bundle.zip) (source, content, components and this brief as markdown; images listed by URL, not included). Every file in it is also public on sgit.ai at the same path, for example `https://sgit.ai/admin/build/newsroom.py`, so you can always fetch the current version instead.
2. **Read your own repository first** and write down what it does today: its generator, its gates, its navigation, its `/newsroom/` page. Change nothing in phase 0.
3. **Follow the phases below in order**, and stop at the end of each for Dinis to look. Each phase has its acceptance checks.
4. **Ask before** anything in [decisions](#decisions). Those are his.

## What is moving

| Part | On sgit.ai today | Source |
|---|---|---|
| Articles (65) | [/articles/](../../articles/index.md), one page per article, each with a markdown twin, a card, an Open Graph image, often a LinkedIn banner, and the "threads" (what it builds on, what builds on it) | `admin/content/articles/*.md` |
| A graph per article | core idea, typed nodes and edges, links, quotes checked word for word against the article at build; all of them in [/articles/graphs.json](../../articles/graphs.json) and drawn on [/articles/graphs.html](../../articles/graphs.md) | `admin/content/articles/graphs/*.json` |
| Article versions | every article's history and diffs, from git | `admin/build/article_versions.py`, `article_diff.py`, `article_versions.json` |
| Read it another way | the five readers (librarian, cartographer, historian, explainer, storyteller) for some articles | `admin/content/articles/views/<slug>/` |
| The front page | [/articles/index.html](../../articles/index.md): lead, latest, highlights, desk notes, collections, every article with topic filter and search; placement from one file | `admin/content/newsroom/front.json` |
| The newsroom, backstage | [/newsroom/](../../newsroom/index.md): six roles with behaviour policies, publishing guide, board, run log, pitches, desk health | `admin/content/newsroom/{roles,board,log,pitches}`, `admin/build/newsroom.py`, `desk.py`, `policy_check.py` |
| Desk notes (4), collections (5) | /articles/desk/, /articles/collections/ | `admin/content/newsroom/{notes,collections}` |
| Newsletter (2 issues) | /articles/newsletter/, also published on LinkedIn as "Deterministic GenAI"; each issue has a LinkedIn kit and banner | `admin/content/newsroom/newsletter/*.md` |
| Subscribe | /subscribe/: the address is encrypted in the browser and dropped into a write-only append lane | `assets/subscribe.js`, `.well-known/sgit-subscribe.json` |
| The reader account | /account/: the reading meter (pay by depth, below zero allowed, usefulness sets the price), history, graph, personas, the newsroom of your own, share your reading, top-up and the Stripe return page | SG Meter v1.3.1, `assets/components/sg-meter/v1/v1.3/v1.3.1/` and the base class at `assets/components/base/v1/v1.0/v1.0.0/` |
| SG Meter, the library | [/meter/](../../meter/index.md) and [/meter/security.html](../../meter/security.md) | `admin/content/meter/*.html` |
| Feeds for people and agents | [/articles/feed.xml](../../articles/feed.xml), [/newsroom/wire.json](../../newsroom/wire.json), graphs.json, the markdown twins, the llms.txt sections | generated by the build |

What does not move: the product documentation, the published vaults and their pages, the API and CLI docs, the case studies, the network pages and the site's own admin. Articles about sgit itself (for example [what sgit is](../../articles/what-sgit-is.md)) move with the rest, and sgit.ai links to them.

## How it is built today

One Python generator, [admin/build/build_pages.py](../../admin/build/build_pages.py) (about 7,700 lines), builds the whole of sgit.ai from `admin/content/`; [validate.js](../../admin/build/validate.js) gates it (links, orphans, the authoring contract, house style); [release.sh](../../admin/build/release.sh) builds, validates, commits as `site vX.Y.Z: …`, pushes to the deploy branch and waits until the live site serves the new version. The newsroom parts are entangled with the rest, so expect to extract rather than copy. The pieces, by function (line numbers as of v0.7.36):

| Concern | Where |
|---|---|
| Loading articles (front matter, `!shot`, `!source`, `!trail`, graphs, quote checks) | `content.py` (`Content_Loader`); `ARTICLES`, `BY_SLUG`, `ARTICLE_OUT/IN` near line 5393 |
| The editorial layer: roles, front, pitches, board, log, notes, collections, issues, findings | `newsroom.py` (`Newsroom`); `desk.py`; `policy_check.py` |
| Article page | `article_body`, `article_threads_block`, `article_desk_block`, `article_views_block`, `linkedin_kit` |
| Front page and indexes | `articles_index_body`, `_masthead`, `_lead_block`, `_latest_rail`, `_high_card`, `articles_filter_bar`, `collections_index_body`, `desk_index_body` |
| Backstage pages | `newsroom_index_body`, `newsroom_role_body`, `newsroom_policies_body`, `newsroom_publish_body`, `newsroom_board_body`, `newsroom_log_body`, `newsroom_pages` |
| Graphs | `graph_svg`, `articles_map_svg`, `articles_graphs_body`; graphs.json is written alongside |
| Newsletter | `newsletter_index_body`, `issue_body`, `subscribe_body`, `subscribe_block` |
| Banners and cards | `write_banner_manifest`, then `make_banners.mjs` (Playwright); `make_og_cards.mjs` (needs sharp) |
| Reader account and meter | `METER`, `PERSONAS`, `PERSONA_NAMES`, `meter_kind`, `meter_config`, the injection in `page()`; `account_body`, `yours_body`, `personas_body`, `share_body`, `topup_body`, `toppedup_body` |
| Feeds | `write_wire`, `write_articles_feed`, the llms writers |
| Tests | `admin/build/test_meter.mjs` (28 checks in Chromium against the built site, no mocks) |

## Where things go on newsroom.sgit.ai

**Keep every path the same.** The articles have been linked from LinkedIn articles and newsletter issues; if `sgit.ai/articles/x.html` becomes `newsroom.sgit.ai/articles/x.html`, the forward from the old address is one rule and nobody has to keep a map.

| On sgit.ai | On newsroom.sgit.ai | Note |
|---|---|---|
| `/articles/…` (articles, desk, collections, newsletter, graphs, feed, images, cards, banners) | `/articles/…` | free there today |
| `/articles/index.html` (the front page) | `/` and `/articles/index.html` | the front page becomes the homepage; see [decisions](#decisions) |
| `/newsroom/…` (backstage, wire.json) | `/newsroom/…` | **collides** with the existing `/newsroom/index.html` (the design of the newsroom's roles and operations). Move that page to `/design/newsroom.html` and keep a forward at its old path |
| `/account/…`, `/subscribe/`, `/meter/` | same | free there today |
| `/.well-known/sgit-subscribe.json` | same, unchanged | the same public key and lane; subscriptions and reading shares keep landing in the same vault |
| (newsroom.sgit.ai's own sections: thesis, corrections, provenance, economics, rights, mvps, portugal, governance, world-news-day, databases, documents, library, shipped, network, about, admin) | unchanged paths | grouped in the navigation as *The design* and *The instances*; nothing of theirs is deleted |

## Phases

### Phase 0: read, inventory, no changes

- Read your generator, gates and release flow; write down which of sgit.ai's conventions you already share (markdown twins, llms.txt, version log, provenance blocks) and which you do not.
- Confirm the one collision (`/newsroom/`) and look for any others in your tree.
- Decide, and say, whether you will port sgit.ai's generator code or rebuild the same pages with yours. Porting is faster; the newsroom functions listed above can be lifted into a module of their own, with `content.py`, `newsroom.py`, `desk.py` and `policy_check.py` as they are.
- **Done when:** a short note in your repository lists the plan, the collisions and the decisions you need.

### Phase 1: the articles, exactly as they are

- Bring `admin/content/articles/` (markdown, graphs, views) and the article images, cards, banners and Open Graph images (listed with their URLs in the bundle's `IMAGES.txt`; fetch them, about 60 MB).
- Build every article page, its markdown twin, the threads and the graph, at the same path.
- Keep the build's refusals: a graph quote that is not in its article fails the build; a teaser over 160 characters fails; a link to an article that does not exist fails.
- **Done when:** all 65 pages build, each article's text matches sgit.ai's, graphs.json has 65 entries, and your link checker passes.

### Phase 2: the newsroom around them

- Front page from `front.json`, desk notes, collections, the newsletter and its issues, the backstage pages, the roles and their behaviour policies, the board, the log, the pitches, desk health.
- Move your existing `/newsroom/index.html` to `/design/newsroom.html` with a forward.
- Navigation: the newsroom first (front page, newsletter, every article, collections, from the desk, as graphs, how it runs, subscribe, your newsroom, your account); then *The design* (your current argument pages) and *The instances* (Portugal, governance, World News Day, databases).
- **Done when:** every page listed under [what is moving](#what) exists, the policy checker passes on the role files, and the front page shows the same lead and highlights as sgit.ai.

### Phase 3: the reader account

- Copy SG Meter at its versioned paths (`assets/components/sg-meter/v1/…` and `assets/components/base/v1/v1.0/v1.0.0/`); never edit a published version in place, add a new path.
- Inject on every page what `page()` injects today: the `<script type="application/json" id="sg-meter-config">` built from `METER` and `PERSONAS`, the balance in the top bar, the reader card at the foot of an article, and the module loaded with a dynamic `import()`.
- Pages: account, newsroom (yours), personas, share, top-up, topped-up; the SG Meter docs.
- **Reader data does not move by itself.** localStorage belongs to an origin, so a reader's balance, history and personas on sgit.ai are invisible on newsroom.sgit.ai. Build `/account/import.html`: it reads a payload from the URL fragment (`#state=…`, base64url of gzip of the exported JSON, made with `CompressionStream`), shows what it contains, restores it with the meter's `restore()` only when the reader confirms, then removes the fragment with `history.replaceState`. The fragment is never sent to any server. The sgit.ai session will add the sending half (`/account/move.html`).
- Run `test_meter.mjs` against your build (it serves the repository root itself).
- **Done when:** the meter test passes, an export from sgit.ai restores on newsroom.sgit.ai through the import page, and nothing is sent anywhere.

### Phase 4: feeds, agents and the outside world

- feed.xml, wire.json, graphs.json, markdown twins and an llms.txt section for the newsroom, at the same paths.
- Canonical URLs on every moved page point at newsroom.sgit.ai.
- Open Graph images in JPEG (LinkedIn does not read WebP).
- **Done when:** the feed validates, wire.json lists every article, and a LinkedIn post inspector shows the card for one article.

### Phase 5: cutover (both sessions)

- Until cutover, new articles keep arriving on sgit.ai from several sessions every day. Sync from sgit.ai (its repository or the public files) as often as needed; do not edit moved content on your side before cutover, or the two will drift.
- At cutover the sgit.ai session will: change `/newsroom/publish.html` and the publishing guidance to point at newsroom.sgit.ai; turn every moved page into a short page with the canonical URL on newsroom.sgit.ai and a forward to it (GitHub Pages has no server redirects); drop the newsroom from its top navigation; keep the files for links and reference; and later decommission them.
- **Done when:** a new article published on newsroom.sgit.ai appears there with its graph, and the old sgit.ai address forwards to it.

## What not to break

- **Client side only.** No server, no database, no third-party scripts beyond what is already declared. Reader data stays in the reader's browser unless the reader chooses to send it, and the share page shows them every word first.
- **Checked, not claimed.** Every figure is from a named source; quotes are checked word for word; a correction is recorded as a correction, not a silent edit.
- **The authorship line.** Articles are by Dinis Cruz, written from his voice notes by a Claude Code session working as the newsroom; the byline and the closing note say so. Do not put model identifiers in the site.
- **House style.** Plain words, short sentences, no em dashes in prose, no "nobody has" claims without a source. sgit.ai's validator enforces several of these; carry the rules into your gates.
- **Versioned components.** A published component path never changes; a fix is a new path.
- **The prices are hypotheses with dates.** [Going live with the reading meter](../../articles/going-live-with-the-reading-meter.md) wrote down five hypotheses and a review date before the first payment, and [pay to keep your persona](../../articles/pay-to-keep-your-persona.md) added two. Do not change them; add new ones as dated additions.
- **Your own honesty rules.** newsroom.sgit.ai says on its face what runs and what is only designed. The newsroom running there is the first part of the design that runs; say so, precisely, and keep saying what does not.

## Decisions for Dinis, before or during the move

1. **The homepage.** The newsroom front page at `/`, with the current thesis page one click away (recommended), or the thesis stays the homepage.
2. **The meter's storage key** on the new origin: keep `sgit.meter.v1` (simplest for imports) or start `newsroom.meter.v1`.
3. **The £5 Stripe Payment Link** is still not created. Its redirect should point at `https://newsroom.sgit.ai/account/topped-up.html?session_id={CHECKOUT_SESSION_ID}` once the move is done.
4. **SG Meter's documentation**: move with the newsroom (recommended, it is where the meter runs) or stay on sgit.ai as a product library.
5. **The name.** "SGit Newsroom" for now; a better name can come later as an alias.

## Open items handed over

- The reading-share messages land in the subscribe vault's lane marked `X-SGit-Form: reading-share`; the drain tool in that vault must file them apart from subscriptions ([drain brief](subscribe-lane-agent-brief.md#reading-share)).
- Open pitches in `admin/content/newsroom/pitches/` are waiting for an Editor run.
- The review date for the meter's hypotheses is eight weeks after the payment link goes live.

## Why this brief is public

Because it is an example of the flow it describes. A decision made in a voice note, a brief written for another agent with the facts it needs and the lines it must not cross, published where anyone, person or agent, can read it and check it against the source files it names. The other session reads this page; Dinis reviews each phase; the articles keep arriving while the move happens. If the brief is wrong about something, the fix is a correction to this page, recorded as one.

Written by the Claude Code session that built the newsroom on sgit.ai, from a voice note by Dinis Cruz, 10 October 2026. Counts and line numbers are as of site v0.7.36.


---

*[Site index for agents](../../llms.txt) · [HTML version](https://sgit.ai/docs/briefs/newsroom-move-to-newsroom-sgit-ai.html)*
