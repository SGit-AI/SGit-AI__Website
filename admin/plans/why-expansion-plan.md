# Plan: the Why reframe, three end-to-end demo vaults, and the component registry

**date** 2026-08-14 · **owner** the sgit.ai site agent · **source** the 14 Aug briefing pack (leading brief + 9 supporting docs)
**canonical URL** https://sgit.ai/admin/plans/why-expansion-plan.md

Decisions taken up front, per the project lead: reusable interface pieces are **components**, never plugins (plugin stays reserved for capability grants); the three demo vaults are **actually created**, each as a full end-to-end walkthrough; demo vault **read keys are published on purpose**, vault keys never; the embed mechanism **reuses the SG/Vault UI code** (briefing filed: /briefs/briefing-sgvault-ui-embed.md).

## Status against the leading brief

| Brief item | Status |
|---|---|
| Discoverability (crawlability, sitemap, llms-full.txt, self-sufficient llms.txt) | **Done** (v0.1.26–27) — remaining: watch Search Console after the v0.2.0 URL moves |
| Naming decision (component vs plugin) | **Decided** — enforce from the first component page |
| Why reframe to boundary map | **Done** (v0.2.9) — boundary first, protocol section, rebuttal moved below |
| Serialised PR as the lead example | **Done** (v0.2.9) — /use-cases/serialised-pull-request.html, PARTIAL status; CLI brief filed |
| Three sample vaults | 2 of 3 done — gallery (v0.2.6) and the real strategy report (v0.2.8); the two-agent inbox remains |
| Embed reuse from the SG/Vault UI | Minimal host shipped (v0.2.6–8, images included); official-UI embed blocked on the read-only credential format — findings in the briefing (v0.2.7) |
| Component registry | Phase 5 — gated on indexing being observed, per the brief |

## Phase 1 — Reframe /why/ from rebuttal to boundary map

Rewrite of the existing page, not new work. The git-vs-sgit table (already on the page) moves to the top and becomes the frame; the rebuttal to the LinkedIn comment moves underneath it. Corrections the pack is right about and the page currently gets subtly wrong:

- **The boundary is not the operations.** commit/push/pull/clone/branch/diff/merge all exist. What is absent is the *hosted review interface* and the ecosystem above the protocol (CI, issues, server-side search, delta compression). A pull request is a platform construct layered on merge.
- **Git is also client-side.** The difference is not that work moved to the client — a git client already holds the object model. The difference is the objects are *encrypted* there. Losses are what a readable server could have added; "the server can do nothing" overstates it and costs trust.
- **Name the two keys and the three modes** (Local / API / Web), and publish the six-step read path verbatim — it fits on a page and is the protocol argument.
- **Scenario template** for every situation added later: THE SITUATION / WHAT YOU TRIED / WHAT CHANGED / HOW → link. The second field is the one that makes it believable.
- One canonical location per fact: the Why links to the Rosetta page, limitations, security — never restates them.

## Phase 2 — The serialised pull request, honestly stated

The lead example: an agent clones a public vault **with no credential at all**, changes, commits, emits a diff; a person imports, reviews, merges elsewhere. Grounding to cite: the 5 Aug 2026 Black Hat disclosure (an issue from a no-privilege account reached CI secrets in three vendors' default configurations); no-credential is stronger than short-lived-scoped (which remains an open platform feature request); published security guidance independently recommends read-only-job → constrained artefact → separate privileged step.

**Honesty gap found while planning:** `sgit history diff --json` (emit) is shipped; **there is no `apply`/import command in the current CLI** (v0.15.x). The workflow was performed, but its import half is not a first-class command. Therefore:

1. The page ships with evidence status **PARTIAL** and shows the real mechanics (emit via `history diff --json`; import via review-and-merge).
2. A brief goes to the CLI team: `sgit diff export` / `sgit diff apply` as first-class commands, plus a **published diff format specification** — the pack itself flags that the headline claim needs one.

## Phase 3 — Three demo vaults, built end-to-end in public

Three shapes, chosen for maximum difference, each **created from scratch** so the walkthrough is complete and reproducible — not imported from existing vaults (those can follow as catalogue entries once the mechanism is proven):

| # | Shape | Demo | Content |
|---|---|---|---|
| 1 | Gallery | a small image/notes gallery vault | generated demo content |
| 2 | Report | a fictional security-assessment report with re-test history | authored for the demo, clearly fictional |
| 3 | Multi-agent collaboration | an inbox/folder vault two agents write to on separate branches | produced by actually running two sessions |

Each demo page (under `/demos/`) is the full transcript: `sgit create` → structure → commit → push → derive the read key → **publish the read key in the page, with the sentence explaining why that is safe and deliberate** → the live embed (Phase 4) → a downloadable archive. Per-sample metadata, stated on every page: **shape · evidence status · copy-or-reference semantics** (archive = copy that diverges; embed = reference that stays live). Archives go in **GitHub release assets, never the repo tree** (3,000-entries-per-directory recommendation; ciphertext neither compresses nor deltas, so the archive is ~vault-sized and every tree copy is paid for by every clone forever).

**Key hygiene, mechanical:** each demo vault's key lives in the gitignored `.sg_vault/local/demo-keys/` tier; the validator's tripwire extends to scan every tracked file for **all** passphrases found there, not only the site vault's; `release.sh` already refuses to push until that passes. Read keys (64-hex) are exempt by design.

## Phase 4 — The embed: reuse the SG/Vault UI host code

Goal: open the vault app iframe (opaque origin, `window.sg` bridge, deny-by-default permissions) inside a sgit.ai page from **read key + vault id alone**, using the same code dev.vault.sgraph.ai runs — one codebase, and the embed itself demonstrates the capability. Briefing with six concrete questions filed to the UI agent: **/briefs/briefing-sgvault-ui-embed.md** (modules, embeddable entry point, read-key-only behaviour, sandbox recipe, version pinning, `_page.json` renderer).

Fallback so Phase 3 never blocks: `<iframe>` straight to `dev.vault.sgraph.ai/en-gb/#<read-key>:<vault-id>` — whole-app embed, works today. Ship demos on the fallback if the reuse answer takes time; swap the inner-host embed in when it lands and write the integration up as a case study.

## Phase 5 — Component registry (gated)

Only after search indexing of the site is *observed*, per the brief: a registry an agent cannot fetch does not remove the agent tax. When unblocked: **vault-in-vault first** (small, everything depends on it); chat is two-or-three components, not one; each component gets a single canonical URL whose artefact is self-sufficient, an evidence status, and the one-line agent reference as the most prominent thing on the page. Component fetching and capability granting never share a command.

## Also queued from the pack

- **Case study: the site's own multi-vault build** — the inbox-coordinated multi-agent, multi-vault architecture behind this site, written up properly.
- **Ignore-file gap brief to the CLI team:** sgit has no ignore support (documented as planned); the single-declaration two-ignore-files-generated pattern in the pack is the right ask, plus the build check that fails when a path is claimed by both systems.
- **Per-path index** (`sg-vault-v1:file-id:path-index:{vault_id}:{path}`) — briefed, not built; our reader adopts it for single-request page loads when it ships.

## Order and dependencies

1 (Why rewrite) → 2 (serialised PR page + CLI brief) → 3+4 together (demos on the fallback embed; upgrade embed when the UI agent answers) → registry last, behind indexing. The naming decision applies from the first word written.
