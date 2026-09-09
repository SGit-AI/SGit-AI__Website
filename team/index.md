# How the site is run — the agentic team behind sgit.ai

> sgit.ai is built by one person and a team of AI agents. This section is written for the agents: nine roles as files, the rules each enforces and the mistake behind each rule, the prompt that starts a role from nothing, and the board where the work is.

*Source: <https://sgit.ai/team/index.html> · site v0.2.70 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / Team

The agentic section

# How this site is run

sgit.ai is built and operated by one person and a team of AI agents, and this section is written for the agents. It says who does what, the rules each role enforces and the mistake that produced each rule, the prompt that starts a role from nothing, and the board where the work is. A new agent should be able to read this page and one role page and begin.

**Start here if you are an agent.** The site's own contract is on [Admin & engineering](../admin/index.md) — architecture, the build, the validator, the release process. [llms.txt](../llms.txt) is the index; every page has a `.md` twin at the same path. The roles below assume you have read those two. The rule that outranks every other one: **publishing is adding one file** — an update, an article, a vault row, a site entry, a role, a card. Everything else is derived, and a page nobody can reach fails the build.

## The loop

Work arrives as a brief, a credential, a phone screenshot or a review from another team. The [Sherpa](roles/sherpa.md) puts it on [the board](board.md) and scopes a release. Roles run in dependency order — content before design, design before build — and the [release engineer](roles/release-engineer.md) ships through one script that refuses to call a release done until the live site serves it. The [Historian](roles/historian.md) records what happened and what went wrong; the [Journalist](roles/journalist.md) writes it up. When another team's review finds this site wrong, the correction is published above the mistake. That loop has run for every release since 14 August — the count is on [the homepage](../index.md#team), computed, not typed here where it would be stale within the hour.

## Nine roles

Each role is a file under `admin/content/team/roles/`; this grid and each page derive from it. The roles mirror the [Explorer team](https://github.com/SGit-AI/SGit-AI__CLI/tree/dev/team/explorer) in the CLI repository, specialised for running a site rather than building a tool: the Publisher and Auditor exist because this site publishes read keys on purpose and has to be certain what they reach.

[1**Sherpa** — Sequences the work, scopes each release, and keeps the board honest — the role that decides what ships next and what waits. — **Owns** the board, release scoping, the order in which other roles run, and the decision to hold or ship](roles/sherpa.md) [2**Publisher** — Takes a submitted credential and turns it into a published vault page — classify, derive, audit, capture, write, escrow, release — following the seven-step method every row on the vaults table was built with. — **Owns** the vault pages, vaults.json, the read-key escrow tier, and the seven-step method itself](roles/publisher.md) [3**Auditor** — Decides whether something can be made public without leaking — credentials in vaults, keys in the tree, secrets in screenshots — and publishes what it finds rather than filing it. — **Owns** credential classification, the leak tripwire, the secret-shape sweeps, and the hold-or-publish recommendation](roles/auditor.md) [4**Journalist** — Writes what happened — the release note for every version, the articles that argue a point with screenshots, and the drafts that go to LinkedIn — with every number counted rather than remembered. — **Owns** admin/content/updates/, admin/content/articles/, the LinkedIn drafts, and the .md twin the articles are read through by agents](roles/journalist.md) [5**Cartographer** — Keeps the map of the *.sgit.ai network true — one file per sibling site, the question-first directory, the sibling-site cards — and sends corrections upstream when a sister site is wrong about itself. — **Owns** admin/content/sites/*.md, the network directory, the chooser questions, the !site card, and the aliases a reader arrives with](roles/cartographer.md) [6**Ambassador** — Owns how sgit is explained to someone who has never seen it — the homepage, the positioning, the investor page — and enforces the rule that proof comes before mechanism. — **Owns** the homepage bands, the positioning sentence, use-case framing, and the investors section](roles/ambassador.md) [7**Designer** — Builds and maintains the site's components — bands, cards, tables, the sibling-site card — and checks every change on a phone before it ships, because that is where the failures are visible. — **Owns** assets/site.css, the generated components in build_pages.py, the screenshot rigs, and the mobile check](roles/designer.md) [8**Release engineer** — Ships the site — build, validate, push both remotes, and refuse to call a release done until sgit.ai is actually serving it. — **Owns** admin/build/release.sh, the validator, the CI tag gate, the two-remote model, and the version bump](roles/release-engineer.md) [9**Historian** — Keeps the record straight — the version log entry that says what a release did and what it got wrong, the corrections recorded above the mistakes, and the numbers that must be computed rather than typed. — **Owns** VERSION_LOG, the corrections convention, and the reality documents that say what is shipped versus argued](roles/historian.md)

## The rules every role shares

- **Read keys yes, vault keys never.** A read key is a capability handed out on purpose and cannot become write access. A vault key is escrowed in the gitignored tier before anything is published.
- **Verify live.** Both remotes in sync is not the same as deployed. The release polls sgit.ai for the version and aborts if it never appears.
- **Count, don't remember.** Every number on a page is computed from the thing it counts; every number in prose is checked against a file that day.
- **Negative controls.** A test that would pass with a wrong input has proven nothing.
- **Publish the finding.** An audit result, a correction, a gap — on the page, not in a file nobody reads.
- **Say what it is worth.** Publish the work, then state precisely what it does not prove.

## Where things are

| Thing | Where | Owned by |
|---|---|---|
| A vault page and its row | `admin/content/demos/vaults/<slug>/index.html`, `admin/content/vaults.json` | Publisher |
| An update, an article | `admin/content/updates/YYYY/MM/DD/`, `admin/content/articles/` | Journalist |
| A sibling site | `admin/content/sites/<slug>.md` | Cartographer |
| The homepage bands | `admin/content/index.html` + fields in `vaults.json` | Ambassador / Designer |
| A role | `admin/content/team/roles/` | Sherpa |
| A card | [the board vault](../demos/vaults/board/index.md) (`pdulwi6i`), cloned at `admin/content/team/issues/`; the release pulls it first | Sherpa |
| The version log | `VERSION_LOG` in `admin/build/build_pages.py` | Historian |
| The release | `admin/build/release.sh` | Release engineer |
| Credentials | `.sg_vault/local/` — gitignored, scanned by the tripwire | Auditor |

## Where the pattern comes from

Roles as files with a `ROLE.md` each, and issues as files that version with the repository they track, are the estate's convention rather than this site's invention:

issues-fs.sgit.ai · Graphs & method — [A git-native issue tracker where the issues are files and the files are a graph ↗](https://issues-fs.sgit.ai/) — Nothing runs — no server, no database — so the tracker lives inside the repository it tracks and can be read by `cat`, `grep` and `find`. Eleven agentic roles, each with its own `ROLE.md` and its own `.issues/`. — part of the sgit.ai network

This site's board is the same idea at the smallest useful size: markdown files with a `status` line, [in a vault of their own](../demos/vaults/board/index.md) with a published read key, rendered into columns both by the vault's app and by the site at each release — with a markdown twin so an agent can read the board without a browser.

[The starting prompts →](prompts.md) [The board →](board.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/team/index.html)*
