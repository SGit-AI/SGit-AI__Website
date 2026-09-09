# The sgit.ai board — a published vault

> The site's own task board, moved into a vault: every card a markdown file, a five-column board app that requests no permissions, and a published read key — because every task, bug and need on it is public. The site renders a snapshot at each release; the vault is the truth between them.

*Source: <https://sgit.ai/demos/vaults/board/index.html> · site v0.2.69 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../index.md) / The sgit.ai board

# The site's own board, as a vault

Two days after [the board](../../../team/board.md) appeared as files in the site repository, it moved out into a vault of its own. Every card is a markdown file; a five-column board app renders them and asks the host for nothing; and the read key is published, because every task, bug and need on it is public. The vault is the source of truth — **moving a card is `sgit push`, with no site release** — and the site renders a snapshot from a clone each time it ships.

**Open it yourself — the key is the whole credential.**
 Read key: `f41d03b0de550479b3c4359709130386df48f34b2cd75e5ed83de28e9776b479:pdulwi6i`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#f41d03b0de550479b3c4359709130386df48f34b2cd75e5ed83de28e9776b479%3Apdulwi6i) · From the CLI: `sgit clone f41d03b0de550479b3c4359709130386df48f34b2cd75e5ed83de28e9776b479:pdulwi6i`
Published as a read key, derived from the vault key at creation. The vault key is held by the site's release engineer and is not published.

## See it live, here

[Open the board in a new tab ↗](https://dev.vault.sgraph.ai/#f41d03b0de550479b3c4359709130386df48f34b2cd75e5ed83de28e9776b479%3Apdulwi6i)Five columns wide — it has more room in its own tab than in the frame below.

## Why a vault, and not the repository

The cards started as files in the site repository, which was already the right shape — issues-fs.sgit.ai's argument that a tracker should be files that version with the thing they track. But it tied every board change to a site release: to move a card from *review* to *done*, an agent had to build, validate, push two remotes and wait for the deploy to verify. A board should be cheaper to update than the thing it tracks.

So the files moved into a vault. Now the site is a **reader** of the board rather than its home: the release script pulls the vault before it builds, and the columns on [the board page](../../../team/board.md) are a snapshot as of that release, labelled as such. Between releases, the vault is ahead of the site, and opening it shows the truth.

## What is in it

the app

### Five columns, from the files, asking for nothing

`index.html` lists `issues/` through `sg.vfs`, parses each card's frontmatter, and draws the columns. `app.json` declares `"permissions": {}` — the app reads the vault it is in and touches nothing else. Served outside a vault host, it falls back to `issues/index.json`, which `tools/reindex.py` regenerates from the same files.

Needs — the things only the author can supply — keep their own column and their own colour, so they are never discovered late.

The app, rendered from the files. Moving a card is editing one line and pushing.

## The card format

```
---
title: The ask: round size, instrument, and what it buys
id: N1
kind: need          # need = only the author can supply it · task = an agent can pick it up
status: needs       # needs | backlog | doing | review | done
role: ambassador    # the sgit.ai team role that owns it
priority: high
opened: 2026-09-07
---
What it is, and what it unblocks.
```

Ids are `N<n>` for needs and `T<n>` for tasks, never reused. A card that names a need is closed only by the author's answer. Corrections to published claims are not cards: they are version-log entries on the site, so the record of a mistake is never tidied away.

## Notes

**Audited before publishing**, briefly, because there is nothing to find: the vault holds card text, a README, one app and one tool. No credentials of any kind, no personal data. Every link in a card is root-relative to sgit.ai and resolves.

**The write key is escrowed** in the site's gitignored credential tier, the same place every other published vault's write key lives, so the board can be corrected by the release engineer and by nobody who holds only the read key.

**The site's clone is a mirror, not a fork.** `admin/content/team/issues/` in the site repository is this vault's working tree; its encrypted store is gitignored, its card files are tracked as the build's input. If the two ever disagree, the vault is right.

[← The board, as the site renders it](../../../team/board.md) · [All published vaults](../index.md)


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/board/index.html)*
