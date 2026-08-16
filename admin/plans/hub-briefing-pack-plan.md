# Plan: the hub.sgit.ai briefing pack

**Source:** 14 Aug briefing pack, Part B (`02-hub-briefing-pack-spec`). Ask A (the catalogue) shipped in v0.2.12–13.
**Status:** capability audit STARTED — 16 rows below, seeded from evidence this project has produced. **Updated 15 Aug against the deployed read-key build: row 1, the entry point for everything, has flipped from partial to present.** Rows still marked `?` go into the next UI-team briefing.
**Deliverable:** a six-part pack published on the site in the cross-team brief form, BEFORE the hub is built.

## The model (settled — restate, do not relitigate)

A forge whose application layer runs in the browser. The client holds the vault key or read key; the server is object storage plus the existing interface and reads nothing. Reference class: the self-hostable forges, not the largest code host. Features follow the key — only discovery across vaults you hold **no** key to needs a reading index.

## 1. The capability audit (first deliverable — facts, not design)

Legend: **✓ verified** = demonstrated by this project with a written check; **UI ✓** = observed in the official SG/Vault UI; **?** = needs the UI team; status is present / partial / absent.

| # | Capability | Status | Where it lives | Evidence |
|---|---|---|---|---|
| 1 | Open a vault in the browser from a read key | **present** | **Gap closed 15 Aug.** The official UI's `vault-loader-format.js` now detects **format 6** (`<64-hex>:<vault_id>`, CLI-clone parity) *before* the passphrase formats — the exact ordering that previously PBKDF2'd the read key into the wrong ref id — and strips the CLI's canonical key prefixes first. Our own readers already did it: `assets/vault-docs.js`, `assets/vault-embed.js`, `admin/build/catalogue_derive.py` | ✓ verified against the deployed build: all three credential forms parse; App Mode boots the demo vault from the published read key alone in a cross-origin iframe |
| 2 | Open from a full vault key | **present** | Official UI `/#token` flow; App Mode booted with a valid credential — including inside a cross-origin iframe | ✓ verified (v0.2.7) |
| 3 | List a tree, navigate directories | **present** | Our readers walk trees with encrypted names (`name_enc`); the official `/en-gb/vault` browser now verified too — `vault-shell` with the FILES / SGIT / SETTINGS rail and the real decrypted tree, opened read-only | ✓ verified both (the earlier "Initialising…" stall was harness timing, not the UI) |
| 4 | Fetch and decrypt a single object by path | **present** | derive → fetch → decrypt, the six-step read path; all three of our readers | ✓ verified |
| 5 | Render markdown, highlight code | **partial** | Markdown: `vault-docs.js` renders the deploy docs and catalogue live. Code highlighting inside a vault viewer: unknown | md ✓ verified; highlight ? |
| 6 | Walk commit history | **present** | Our deriver walks `parents` to depth 200; CLI `sgit history log`. The official SGit view is now driven and verified: HISTORY / REFS / TREE / BRANCHES / STATUS / REPAIR, both commits listed with real object ids, dates and branch labels — **from the read key alone** | ✓ verified both |
| 7 | Fetch two versions and compare | **partial** | CLI: `sgit history diff --json` exists (basis of the serialised-PR page). Browser: each history row renders `tree` and `diff` affordances in the read-only SGit view — present in the UI, but we have **not** driven them, so rendering quality is unmeasured | CLI ✓; UI present-but-unexercised |
| 8 | Sparse / partial fetch | **present** | Inherent to the object model: our readers fetch per-object on demand — a page visit reads only the ref, the trees, and that page's blob. CLI documents sparse clones | ✓ verified (4-file page load demo) |
| 9 | Local caching between sessions | **present** (ours) | `vault-docs.js`: immutable objects in the Cache API, memoised tree index, ref checked once per 120 s window — a warm reload makes **zero** requests. Official UI behaviour unknown | ✓ verified headless; UI ? |
| 10 | Sub-vault traversal and link files | **partial** | Vault-in-vault embedding exists both sides: UI's `sg-embed-frame`, our embed host. Link-file traversal untested | embed ✓; links ? |
| 11 | App runtime and its permission model | **present** | `app.json` entry points, sandboxed iframe with opaque origin, `sg.*` bridge over postMessage; verified in our host AND official App Mode in an iframe | ✓ verified (v0.2.6–7, v0.2.11) |
| 12 | Write and push from the browser | **present** (UI) | `vault-browse-edit` components; R1 W0 badge implies write path. Not driven by us; our readers are read-only by design | UI ✓ observed; ? to confirm |
| 13 | Merge and conflict handling client-side | **unknown** | No component found for it in the enumeration | ? — likely the genuinely new build |
| — | Frameable at all | **present** | No `X-Frame-Options`, no `frame-ancestors` on the official UI | ✓ verified (v0.2.7, re-verified 15 Aug) |
| — | Read-only posture visible to the reader | **present** | The chrome carries an explicit `R1 W0` and `Read-only` badge when opened with a read key — the write gate reporting it has none. Useful for the pack's "see that you cannot write" screen | ✓ verified |
| — | Deep-link to a specific view (e.g. SGit) | **absent** | View switching remains an in-page event; no URL selects a view, so a host page cannot frame the SGit view *in isolation*. The one UI ask still open | ✓ verified absent |

**The partial rows are the dangerous ones** (the spec's own warning): 5, 7, 10 and 12 will each be assumed complete by anyone writing architecture without this table. Row 7 is the sharpest example — the diff affordances are visibly *there*, which is exactly how a partial gets recorded as done.

**What changed on 15 Aug, and why it matters to the pack:** row 1 was the single gap blocking the forge's entry point, and it closed. The consequence is larger than one row — it means the hub's read-only tier can be **assembled from the existing UI rather than built**, opened by a published read key, which is the assembly-not-construction claim the spec asks the audit to settle. The remaining new build is concentrated in rows 12–13 and the deep-link absence.

## 2–6. The pack's remaining parts (order matters)

2. **Architecture** — one diagram: browser-with-key / ciphertext boundary / object store + existing interface. Include the single-file data path (derive, fetch, decrypt, render) — we already publish exactly this on the deploy case study, so this is largely assembly of existing material.
3. **User flows** — five: arrive-public (key in link), open-private (**the hard one: pasting a vault key into a web page is the obvious wrong answer — reach a considered position**, candidates: fragment-only keys that never leave the browser, WebAuthn-wrapped local key storage, read-key-by-default with write elevation), browse+diff, propose-change (the serialised diff — already a use-case page), review+merge.
4. **Mock-ups** — forge conventions, minimal difference. The one screen that matters: the reader watching the server return only ciphertext — our vault debug panel is the working prototype of exactly that screen and should be presented as such.
5. **Development guidance** — read-only over one vault first, then the same view over a private vault. Reused-vs-new comes straight from the audit table: rows 1–11 are assembly, 12 is confirm-and-surface, 13 is new.
6. **Hosting** — objects on the existing interface; the self-hosting claim (server = storage, no database).

## Four absences, stated plainly

Search across vaults you hold no key to (needs a reading index; published-key vaults only — the catalogue is that index's first instance) · continuous integration (a builder must read to build; the interesting answer: a build-scoped sub-vault key — least authority applied to CI) · server-enforced granular permissions (possession of a key IS access) · content-triggered notifications (the server cannot see what changed).

## Per-feature classification (carried into every list in the pack)

**Surfacing** what sgit does (diff, history, branch, merge) · **adding** something computed client-side (blame — the correction: quick answers list blame among operations sgit does NOT have — and within-vault search) · **absent** with a reason (the four above).

## Permissions = topology (worked examples to write)

Two or three worked shapes, e.g. docs-vault (published read key) + working-vault (team holds vault key) + secrets sub-vault (separate key, two holders); who holds what, what each can therefore do. Plus the two hard limits: revocation is not retroactive; granularity costs structure (five levels = five vaults, decided in advance). Write-key status is part of this discussion — the catalogue already records `escrowed | lost` per entry and the strategy-maps republish is the lived example.

## The crawler question — CLOSED

Checked and fixed in earlier releases, and now confirmed externally: every page's full text is in the served HTML (the vault-rendered pages are the exception and say so), the noscript/CSS reveal has been in since v0.1.26, `robots.txt` + `sitemap.xml` + `llms.txt` + `llms-full.txt` are generated with a section guard, and **Google has indexed sgit.ai** (confirmed by the project lead, Search Console connected). The pack reports this as answered, not pending.

## Next actions

1. Confirm-or-deny pass on the `?` rows with the UI team (extends the existing embed briefing — now rows 5, 7, 9, 10, 12, 13, plus the view deep-link, which is the only original ask still open).
2. Draft the pack as `briefs/hub-briefing-pack.html` (+ .md twin) in the cross-team brief form; audit table first, absences up front.
3. Publish before building — the method demonstrated at its largest scale so far.

Later, per the pack: one topic section (healthcare) assembled from catalogue entries; the component registry (unblocked now indexing is confirmed); the third demo vault (two-agent inbox).
