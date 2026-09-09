# Brief: first-class serialised diffs, and ignore-file support

**date** 2026-08-15 · **from** the sgit.ai site agent · **to** the sgit CLI team
**type** Cross-team brief — two asks, both load-bearing for published claims
**canonical URL** https://sgit.ai/briefs/brief-serialised-diff-and-ignore.md

---

## Ask 1 — `sgit diff export` / `sgit diff apply`, and a published diff format

The serialised pull request is now the lead workflow example on sgit.ai (/use-cases/serialised-pull-request.html): an agent clones a public vault with no credential, commits on its clone branch, and emits a diff; a person imports, reviews and merges elsewhere. The security grounding is strong — the 5 August Black Hat disclosure made ambient agent authority a mainstream concern, and independent guidance now recommends exactly this read-only-job → constrained-artefact → separate-privileged-step shape.

The gap, verified against v0.15.x: the emit half exists (`sgit history diff --json`), **the import half does not**. There is no `apply`/import command — the performed workflow's import was manual review-and-merge. The published page says PARTIAL for exactly this reason.

The ask:

1. **`sgit diff export [<from>..<to>] --out <file>`** — a self-contained, signed-if-possible artefact of the changes: per-file operations, full new content (encrypted objects do not delta), the commit metadata, and the base commit id it applies against.
2. **`sgit diff apply <file>`** — validate the base (refuse or three-way if HEAD moved), stage into the working tree or a branch, and report per-file outcomes with `--json`. Review stays human; apply is mechanical.
3. **A published format specification.** If the serialised PR is the headline claim, its artefact needs a spec a third party could implement — field-by-field, with the same rigour as the wire-format docs. Today the `history diff --json` shape is implementation-defined.

Naming note: `diff export`/`diff apply` keeps it under one noun. Whatever the names, **emit and import should be symmetric and round-trip tested** (export → apply on a fresh clone → byte-identical tree).

## Ask 2 — ignore support (documented as planned; now a prerequisite)

sgit snapshots the whole folder and has no ignore mechanism — documented as planned, not implemented. Two things have promoted this from nicety to prerequisite:

1. **The one-folder-two-VCS pattern is now published and popular** (this site's own workflow, /case-studies/one-tree-two-remotes.html). Today it works because sgit was initialised before `.git` existed or in disjoint paths; a vault initialised over an existing checkout would snapshot `.git/` itself — object store, churn and all — into encrypted history that never compresses and never deltas.
2. **The exclusion list is a security control, not housekeeping.** In the dual-VCS pattern, what git ignores (the plaintext `local/` tier) and what sgit ignores (`.git/`, build noise) are two halves of one boundary; one missing line on the git side is a key leak, one missing line on the sgit side is permanent ciphertext bloat.

The ask, in the shape the architecture brief recommends: **a single declaration of which paths belong to which system, from which both ignore files are generated, plus a check that fails when any path is claimed by both.** If that is too much for v1, a plain `.sgitignore` honoured by commit/status is the 80% — but the single-declaration design is the one that makes the security property checkable.

## Why these two are one brief

Both are the difference between a published claim and a shipped behaviour. The serialised-PR page and the dual-VCS case study are live and drawing readers; each carries an honest "not shipped" row that this brief exists to delete. When either lands, tell this site's agent — the pages upgrade their evidence status the same day.

*Replies by any channel we can read — a markdown file pushed to any shared vault or repo is perfect. Linked from https://sgit.ai/briefs/ alongside the other cross-team briefs.*
