# sgit.ai v2: page map

Companion to `admin/plans/site-v2-transition-brief.md`. Same date (2026-10-11, site v0.7.51), same status (PROPOSED). Three maps: sections and pages, articles, vaults. Actions: **keep** (no change beyond derived numbers), **refresh** (same page, rewritten for 0.21 and the new positioning), **new**, **fold** (content moves into another page, old path stubs to it), **freeze** (no new content; a notice; cutover per the newsroom move brief), **retire** (stub and forward).

---

## A. Sections and pages

### Root and chrome

| Path | Today | Action | Notes |
|---|---|---|---|
| `/index.html` | hero "A vault is a unit of work", 11 bands, newsroom band second | **refresh** | section 3.3 of the brief; counts derived; 0.21 examples |
| nav (`NAV` in `build_pages.py`) | Newsroom · Why · Docs · Vaults · Agents · Evidence · Team · Network · Security | **refresh** | Start · Docs · Vaults · Why · Journal · Agents · Network · Team · Security |
| footer | Docs · SG/Vault platform · Project | **refresh** | add "SGit Newsroom, now at newsroom.sgit.ai" and "Journal"; drop "Thirty vaults" literal |
| `llms.txt`, `llms-full.txt`, `sitemap.xml`, `feed.xml` | derived | **keep** | will follow the `home:` key for article canonicals |
| `/.well-known/*` | agent contact, subscribe | **keep** | |

### Start (new group, existing pages)

| Path | Today | Action | Notes |
|---|---|---|---|
| `docs/installation` | "current release is 0.18.0, 7 Oct" | **refresh** | 0.21.0; `sgit doctor`, `sgit update`; pipx |
| `docs/quickstart` | create/commit/push/clone/pull | **refresh** | add `clone --path` and `sgit write --json` as steps 6 and 7 |
| `docs/sgit-for-git-users` | command table | **refresh** | add `reflog`, `undo`, `--amend`, `--force-with-lease`, `vault tag`, `check verify`, `branch merge` |
| `skills/` + 3 skill files | "verified against v0.14.27"; share send/publish disabled | **refresh** | regenerate from 0.21; decision 7 on share tokens |
| `try/` | Pyodide, latest wheel | **keep** | add `clone --path` to the demo script if the wheel supports it |
| `docs/update-to-0-18-0` | upgrade guide | **keep** | add `docs/update-to-0-21-0` (**new**) once the changelog is in hand |

### Docs

| Path | Today | Action | Notes |
|---|---|---|---|
| `docs/index` | hub; "coming next: CLI reference" | **refresh** | re-cut around the ten layers; link the generated CLI reference |
| `docs/cli/<command>` | none | **new** (generated) | from `sgit help all` and `--help`, version-stamped |
| `docs/what-is-sgit` | the three doors | **refresh** | fold in the "what git does not have" table; keep "beta" if still true on 0.21 |
| `docs/agents` | session pattern, five clone modes | **refresh** | lead with `--path`; `cache add`; agents sharing one vault summary; V2 |
| `docs/partial-clones` | 0.18 page | **refresh** | rename "Scoped clones"; keep the path; `--allow-deletions`; known gaps re-checked on 0.21; V1 |
| `docs/agents-sharing-one-vault` | 0.18 loop | **refresh** | `--force-with-lease`, `--accept-rewind`; verified on 0.21 |
| `docs/integrity` | none | **new** | `check verify`, `vault tag`, `vault format --feature signatures-required`, `check fsck`, `inspect`; I5 |
| `docs/publishing` | `docs/vault/static-hosting` says "proposed" | **new** (fold static-hosting into it) | `publish --visibility/--bundles/--api-spec/--api-docs`, `vault serve`, `--transport static|local`, `vault mirror`; this site as the proof; V3, I6 |
| `docs/key-management` | v0.20.0, 10 Oct | **refresh** | add `vault attach`, `vault show-key` warnings; V5 |
| `docs/credentials` | prefixes; "most pages still carry sgit_rk1_" | **refresh** | check whether that sentence is still true; derive it |
| `docs/pki` | v0.15.0 | **refresh** | re-verify on 0.21; `pki delete` |
| `docs/vault-messaging` | lanes + PKI; "H(pubkey) proposed" | **refresh** | V6; state what is wired on 0.21 and on send.sgraph.ai |
| `docs/append-lane-messaging` | 45 KB dated write-up | **keep** | link from vault-messaging as the history |
| `docs/agent-contact` | v0.1 spec | **keep** | |
| `docs/send-a-vault-key` | runbook | **keep** | |
| `docs/self-host-for-agents` | 0.20.0 | **refresh** | fix `--endpoint` in the embedded deploy docs; `--transport`; verified on 0.21 |
| `docs/two-branch-model` | | **keep** | add `branch merge` |
| `docs/limitations` | roadmap gaps from 0.15 | **refresh** | every gap re-checked on 0.21 (commit author, whole-file merges, `--bare` "stubs", PKI revoke/directory) |
| `docs/surfaces`, `docs/guidance/*`, `docs/how-to/claude-team-egress` | | **keep** | egress: re-check the `doctor` false negative |
| `docs/vault/index`, `vault-apps`, `sg-bridge`, `content-authoring`, `reading-a-vault-file` | | **keep** | sg-bridge: "verified against app-shell v0.2.x, 2026-08" needs a re-check |
| `docs/vault/sub-vaults` | "CLI access proposed, not shipped" | **refresh** | re-check on 0.21; if still browser-only, say so in the first line |
| `docs/vault/git-and-vaults` | engineering preview | **refresh** | `vault attach` is the missing piece; promote to "one tree, two systems" |
| `docs/briefs/*` | 16 briefs, cross-team asks | **keep** | add this brief to the index as PROPOSED; mark CLI asks that 0.21 closed (`--path`, `sgit_rk1_` prefix) |
| `api/*` (6) | server v0.33.54 audit | **refresh** lightly | resolve the append-routes contradiction between `api/append-lanes` and `docs/vault-messaging`; immutable cache header re-measured |
| `deploy/` | live-decrypted deploy docs | **keep** | the `--endpoint` note stays until the source vault is fixed |

### Vaults

| Path | Today | Action | Notes |
|---|---|---|---|
| `demos/vaults/index` | one sortable table by shape | **refresh** | categorised landing above the table (brief section 5); counts derived |
| `demos/vaults/<slug>` (54) | one page each | **keep** | add `use_case` and `shows` rows to each "What this vault demonstrates" table from `vaults.json` |
| `demos/vaults/aiuc-1-graph` | orphan | **keep** + add to `vaults.json` | |
| `demos/vaults/publishing` | seven-step method | **keep** | |
| `demos/index` | "Thirty at the last count" | **refresh** | derived count; link the categories |
| `demos/fractal-graphs/*` | | **keep** | one of the eight categories |
| `demos/vault-app-embed`, `strategy-maps`, `sgit-maps` | walkthroughs | **keep** | |
| `catalogue/` | 9 of 54 entries, dated 19 Sep | **decision 5** | refresh the vault or retire to the gallery |
| five new vaults | none | **new** | scoped-clone, signed-tag, keyless-mirror, static-publish, inbox |

### Why and evidence

| Path | Today | Action | Notes |
|---|---|---|---|
| `why/` | boundary map, git vs sgit, competitor table, FAQ | **refresh** | brief 2.2 table with commands and vaults; title candidate B |
| `compare/` | 3 entries, hand-checked 16 Aug | **refresh** | add entries: scoped clone vs sparse checkout (measured), write-only lane vs webhook, static mirror vs read access, verify-all-history |
| `case-studies/*` (4) | | **keep** | add one for the newsroom move when it completes |
| `lessons/` | | **keep** | source for the journal's field-notes lane |
| `use-cases/` + 5 subpages | `--sparse notes/ drafts/`; "report the vault key back to me" | **fold** into `why/` and the vault categories | the two sentences above are wrong on 0.18+ and conflict with key-management; fix in phase 1 before the fold |
| `startups/`, `investors/`, `partnerships/*` (20), `summit/`, `about/` | | **keep** | reachable from `why/` and the footer |
| `security/` | PKI read on v0.15.0; review series "being prepared" | **refresh** | re-verify; V4; link integrity page |
| `network/*`, `agents/`, `team/*`, `admin/*` | | **keep** | "Nineteen sites" heading derived |

### Newsroom (freeze, then cutover under the 10 Oct brief)

| Path | Today | Action | Notes |
|---|---|---|---|
| `articles/index` | the front page | **refresh** | becomes the journal index (S lanes) plus one card to newsroom.sgit.ai; banner |
| `articles/<slug>` ×74 | | per map B | `home:` key; banner on N and B |
| `articles/collections/*`, `desk/*`, `newsletter/*`, `graphs`, `versions/*`, `views/*` | | **freeze** | banner; move with the newsroom |
| `newsroom/*` (11) | backstage | **freeze** | banner: "the desk now runs at newsroom.sgit.ai" |
| `account/*` (6), `subscribe/`, `meter/*` | reader account, SG Meter | **freeze** | decisions in the move brief (storage key, Stripe redirect, meter docs) |
| `publishers/` | the door to newsroom.sgit.ai | **keep** | link from footer |
| `updates/*` (75) | | **keep** | CLI release entries also surface in the journal's release-notes lane |

---

## B. Articles (74)

`home:` value proposed per article. **S** = stays canonical on sgit.ai (the journal). **B** = canonical on newsroom.sgit.ai, cross-linked from the sgit.ai page named. **N** = moves. Decision 2 in the brief governs the S rows.

### S: the sgit journal (10 articles, plus the 0.18 update page)

| Slug | Date | Journal lane | Linked from |
|---|---|---|---|
| `what-sgit-is` | 08-25 | architecture | `docs/what-is-sgit`, hero |
| `encrypted-memory-for-isolated-agents` | 10-08 | architecture | `docs/agents`, `docs/partial-clones`, `docs/self-host-for-agents` |
| `where-the-vault-keys-live` | 10-10 | architecture | `docs/key-management` |
| `rfc-0001-public-key-cryptography-for-sgit` | 10-09 | RFCs | `docs/pki`, `docs/integrity` |
| `seven-vaults-one-method` | 08-19 | field notes | `demos/vaults/publishing` |
| `green-does-not-mean-live` | 08-17 | field notes | `admin/index`, `lessons` |
| `nineteen-sites` | 08-26 | field notes | `network/` |
| `chat-on-a-static-site` | 08-27 | architecture | `docs/publishing` |
| `proof-behind-the-claim` | 09-07 | field notes | `admin/index` |
| `proof-moved-up` | 09-07 | field notes | `admin/index` |
| `updates/.../sgit-ai-0-18-0` | 10-07 | release notes | `docs/update-to-0-18-0` |

Back-fill for the release-notes lane: 0.19.0, 0.20.0, 0.21.0 (needs the changelog).

### B: canonical on newsroom.sgit.ai, cross-linked here (13)

| Slug | Date | Cross-link from |
|---|---|---|
| `no-server-by-design` | 10-11 | `docs/publishing`, `why/` |
| `the-identity-we-wanted-to-give-the-agents` | 10-05 | `docs/key-management` |
| `a-mac-of-the-agents-own` | 10-09 | `docs/key-management`, vault `agent-desk` |
| `the-agent-team-as-it-runs` | 10-06 | `docs/agents`, `docs/agents-sharing-one-vault` |
| `the-mandate-stack` | 10-06 | `docs/agents`, vault `risk-mandate` |
| `why-my-agents-do-not-run-on-my-laptop` | 10-06 | `docs/self-host-for-agents` |
| `memory-is-not-a-spectator-sport` | 10-03 | `docs/agents` |
| `how-i-work-with-claude` | 10-09 | `docs/agents`, `skills/` |
| `custom-uis-are-not-the-exception` | 10-01 | `docs/vault-messaging`, `docs/vault/vault-apps` |
| `replicating-the-agentic-inbox` | 10-02 | `docs/vault-messaging`, the inbox vault (new) |
| `a-personal-agent-that-keeps-your-secrets` | 10-06 | vault category "Health and personal records" |
| `the-deck-i-could-not-download` | 10-06 | vault `deck-vault` |
| `supply-chain-of-vaults` | 09-27 | vault category "Documents, decks and handover" |

### N: move with the newsroom (51)

Agents and policy (16): `agency-is-not-a-yes`, `every-mistake-added-a-rule`, `hope-or-enforcement`, `knowing-when-to-stop`, `who-are-you-protecting-against`, `where-is-the-why`, `footprint-and-blast-radius`, `the-behaviour-policy-is-the-business-logic`, `six-agents-one-inbox`, `connector-twin-before-you-deploy-an-agent`, `a-second-reader-the-agent-cannot-skip`, `re-anchoring-agent-behaviour-policies`, `an-agent-desktop-by-the-minute`, `the-wall-under-the-reply`, `authority-outside-the-model`, `the-same-argument-in-our-words`.

RiskMandate and governance (8): `every-risk-is-already-accepted`, `ultimate-insider-three-collisions`, `riskmandate-ten-questions`, `where-the-platform-draws-the-line`, `ai-baseline-control-framework`, `the-ai-governance-stack-as-a-graph`, `code-review-as-a-fractal-semantic-graph`, `introducing-fractal-semantic-graphs`.

News, publishing and the meter (17): `future-of-news-story-vault-not-paywall`, `token-bill-nobody-is-sending`, `how-news-got-here`, `liquid-content-needs-water`, `story-vault-meets-reader-skills`, `the-bridge-followed-to-the-end`, `the-waiting-room-knew-first`, `a-link-to-a-persona`, `a-meter-in-the-browser`, `going-live-with-the-reading-meter`, `pay-after-you-read`, `pay-to-keep-your-persona`, `who-will-game-the-reading-meter`, `a-model-in-the-tab`, `a-reading-list-in-a-link`, `the-agent-is-the-reader`, `one-article-five-readers`.

Strategy, startups and method (10): `saas-apocalypse-decided-by-inertia-not-by-ai`, `the-question-is-whether-they-miss-it`, `price-it-then-give-it-away`, `if-somebody-built-a-company-on-code-review`, `send-an-agent-not-a-spreadsheet`, `the-investigation-github-owes-its-customers`, `how-much-of-this-did-i-write`, `how-to-run-synthetic-users`, `open-source-is-not-free`, `the-infographic-bake-off`.

(`introducing-fractal-semantic-graphs` could be argued into B because the nine graph vaults live here. Left as N to match the collections, which are all newsroom.)

---

## C. Vaults (54 + 1) by `use_case`

| use_case | first | the rest |
|---|---|---|
| `agent-memory` | `deploy-docs` | `risk-mandate`, `board`, `agent-desk`, `article-views`, and the new scoped-clone vault |
| `messaging` | `lesson-loop` | `agent-permission-games`, `connector-twin`, and the new inbox vault |
| `publishing` | `evidence-dispatch` | `bridge-simulation`, `local-evidence-log`, `how-much-evidence`, `infographic-bakeoff`, `catalogue`, and the new static-publish vault |
| `governance` | `aiuc-1-conformance` | `aiuc-1-graph`, `regulation-graph`, `standards-atlas-gdpr`, `pci-dss-graph`, `aibcf-graph`, `ai-governance-graph`, `dsit-ai-risk-toolkit`, `licence-to-operate`, `hope-or-enforcement`, `agency-scale` |
| `security` | `pentest-report` | `agentic-browser-isolation`, `content-transformation-proxy`, `threat-sized-security`, `threatmodcon-2025`, and the new signed-tag and keyless-mirror vaults |
| `health` | `health-score` | `supplement-stack`, `kit-bag` |
| `handover` | `payments-brief-pack` | `interim-ciso-pack`, `fractional-ciso-pack`, `commercialisation`, `blackhat-eu-2025`, `voicedebrief-pitch`, `deck-vault`, `algarve-may-2026` |
| `developer` | `vault-app-pocs` | `code-review-graphs`, `field-notes`, `strategy-maps`, `voice-debrief`, `risk-graph-explorer`, `riskmandate-file-security`, `risk-acceptance`, `agent-webmaster`, `company-xray`, `synthetic-users`, `synthetic-users-riskmandate`, `newsroom-synthetic-users`, `long-tail-ledger` |

`shows` values (one or more per vault, for the features filter): `vault-app`, `read-key`, `graph`, `deck`, `append-lane`, `scoped-write`, `pinned-release`, `two-writers`, `large-binary`, `deep-history`, `synthetic-users`, `hash-provenance`, `fork`, `scoped-clone`, `signed-tag`, `mirror`, `static-publish`, `inbox`.

Known partials to keep honest on their pages: `agent-permission-games` (telemetry "not yet succeeding"), `commercialisation` (templates are placeholders), `payments-brief-pack` (PROPOSED), `catalogue` (9 of 54).
