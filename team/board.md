# The board — open work on sgit.ai, as a kanban of files

> Every card is a markdown file with a status line; the columns are those lines rendered. Needs are items only the author can supply; tasks are work an agent can pick up from its starting prompt. Nothing runs; the board versions with the site.

*Source: <https://sgit.ai/team/board.html> · site v0.2.62 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Team](index.md) / The board

# The board

The open work on this site, as a kanban. Each card is a markdown file under `admin/content/team/issues/` with a `status` line; the columns are those lines, rendered. **Needs** are items only the author can supply and are kept visible rather than discovered late; everything else is work an agent can pick up from its [starting prompt](prompts.md). Nothing runs — the board versions with the site, and its `.md` twin is the same board without a browser.

**16 items** — 13 open, 6 of them waiting on the author. Each card is a file under `admin/content/team/issues/`; moving a card is editing its `status` line.

### Needs — only the author can supply 6

N1 — **The ask: round size, instrument, and what it buys** — [Ambassador](roles/ambassador.md) · high · 2026-09-07

The [investors page](../investors/index.md) has the architecture, the traction and the business model, and a dashed box where the ask goes. Round size, instrument and the use-of-funds split are the author's to state; nothing is invented in the meantime. Unblocks: a page that can be handed to an angel without a caveat.

N2 — **The deck, or permission to build one from the page** — [Ambassador](roles/ambassador.md) · high · 2026-09-07

Your other companies publish the pitch in the open (investor.myfeeds.ai). Either the sgit deck exists and should be linked, or the investors page is the source and a deck can be built from it — a vault with a presenter app, like the [VoiceDebrief pitch](../demos/vaults/voicedebrief-pitch/index.md). Unblocks: something to show in the room next week.

N3 — **A vault where two agents and a human merge are visible in the history** — [Publisher](roles/publisher.md) · high · 2026-09-07

The homepage's strongest multi-agent claim — a branch per agent, a human reviews the merge — has no published vault behind it. If one exists, its read key is enough; if not, the next multi-agent build should be run so its history shows it. Unblocks: closing the gap the [after article](../articles/proof-moved-up.md) names; it goes in the hero.

N4 — **The games vault: one manifest line so the telemetry actually sends** — [Publisher](roles/publisher.md) · medium · 2026-09-07

The other agent's fix is `{"permissions": {"append": {"write": true}}}` and a switch to `sg.append.write` — not `network: true`. When it lands, the page's status note comes off and the two 'nothing sent' footers should be gone. Unblocks: the [games vault page](../demos/vaults/agent-permission-games/index.md) describing behaviour the vault performs.

N5 — **Answers to the seven append-lane questions** — [Cartographer](roles/cartographer.md) · medium · 2026-09-07

Sent to the SG/API team on 7 September (in the CLI repo under `team/humans/dinis_cruz/claude-code-web/09/07/`). The two that matter most: which hosts serve `/api/vault/append/*`, and whether the enum-key derivation is stable enough to publish as a spec. Unblocks: the API page stating facts where it currently says unresolved.

N6 — **Republish the two held vaults clean, or retire them** — [Auditor](roles/auditor.md) · low · 2026-09-07

`bite-coil` (a live provider key in `key.json`, since rotated) and `6kdhnpfx` are held on audit findings. Both are republishable via a fresh vault with the offending file removed. A decision either way closes them. Unblocks: the vaults count telling the whole story.

### Backlog 5

T1 — **An About page about sgit, linking to the fuller record** — [Ambassador](roles/ambassador.md) · high · 2026-09-07

Agreed direction: who builds it (one human and the roles on this page), why, the commercial line (sgraph.ai sells the hosted service; the code stays Apache-2.0), and two sections borrowed from open-source.sgit.ai/about — *Interests declared* and *Reach me, or correct me* — with a `!site` card out to the fuller record rather than a copy of it.

T2 — **Re-verify the 21 published read keys with the marker that actually discriminates** — [Auditor](roles/auditor.md) · high · 2026-09-07

The earlier 24-key sweep used the presence of `.sg_vault/` as success, which an all-zeros key also produces. Three vaults were verified properly by decrypting content; the other 21 were not. Re-run with `clone_mode.json` as the marker and a negative control.

T3 — **Investors page: print stylesheet and a one-page PDF export** — [Designer](roles/designer.md) · medium · 2026-09-07

The page should print to one or two clean pages for the event. The site already has `@media print` rules; extend them for the investor bands and check the output.

T6 — **Flip skills.sgit.ai from not-published to live when Pages serves it** — [Cartographer](roles/cartographer.md) · low · 2026-09-07

DNS and a repository exist; the site 404s from GitHub Pages. Listed in the network directory as *not published yet* rather than omitted. Re-check weekly.

T7 — **Upstream: graphs.sgit.ai footer links to sentinel.sgit.ai, which does not resolve** — [Cartographer](roles/cartographer.md) · low · 2026-09-07

The site is at `sg-sentinel.sgit.ai`; the `sg-` prefix is load-bearing. Noted on our graphs page since 21 August; the brief to their team is the remaining step.

### Doing 0

empty

### Review 2

T4 — **The agentic section: roles, starting prompts, the board** — [Sherpa](roles/sherpa.md) · high · 2026-09-07

Nine roles as files under `admin/content/team/roles/`, a page each; the starting prompts for the regular tasks; this board, as files under `admin/content/team/issues/`. In review: does each prompt start a fresh agent correctly with nothing but the page?

T5 — **The investors section, on the open-investor-materials model** — [Ambassador](roles/ambassador.md) · high · 2026-09-07

Same structure as investor.myfeeds.ai — hook, how it works, architecture, market, traction, business model, the ask, use of funds — with the traction numbers computed from the site and the ask left visibly open (N1). In review: nothing on it may be a number the author has not supplied.

### Done 3

T8 — **Rebuild the homepage: proof before mechanism** — [Ambassador](roles/ambassador.md) · high · 2026-09-07

Shipped as v0.2.60, with the diagnosis in v0.2.59 and two corrections in v0.2.61. [Before](../articles/proof-behind-the-claim.md) and [after](../articles/proof-moved-up.md).

T9 — **The vaults table: sortable, categorised, no keys, newest first** — [Designer](roles/designer.md) · medium · 2026-09-06

Shipped as v0.2.57 and v0.2.58: generated from `vaults.json`, `#` as a permanent publication ordinal, published dates from git.

T10 — **A card for pointing at the sibling sites (!site)** — [Cartographer](roles/cartographer.md) · medium · 2026-09-07

Shipped in v0.2.59. One line in markdown; the card pulls the target site's own category and thesis from `sites/*.md`.

**Moving a card** is editing one line. **Adding one** is adding one file with `id`, `title`, `kind` (need | task), `status`, `role`, `priority`, `opened` and a body that says what it unblocks. A card that names a Need is closed only by the author's answer. Corrections to published claims are not cards; they are [version-log entries](../admin/versions.md), so the record of the mistake is never tidied away.

[← How the site is run](index.md) · [Starting prompts](prompts.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/team/board.html)*
