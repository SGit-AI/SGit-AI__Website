# The sgit.ai board — a vault

The open work on [sgit.ai](https://sgit.ai/), as files. This vault is the **source of truth** for
the board at https://sgit.ai/team/board.html: the site clones it and renders a snapshot at each
release; the vault itself is updated by `sgit push` with no site release at all.

Everything here is public by design — tasks, bugs, features, and the things only the author can
answer. The read key is published on the site. There is no private tier in this vault, so there
is nothing a read key could leak.

## Layout

```
issues/<id>-<slug>.md     one card per file — frontmatter + a body that says what it unblocks
issues/index.json         derived from the files by tools/reindex.py; the board app reads it
                          when it is served outside a vault host
index.html + app.json     the board, as a vault app: five columns, no permissions requested
tools/reindex.py          regenerate issues/index.json after adding or moving a card
```

## A card

```
---
title: The ask: round size, instrument, and what it buys
id: N1
kind: need          # need = only the author can supply it · task = an agent can pick it up
status: needs       # needs | backlog | doing | review | done
role: ambassador    # which sgit.ai team role owns it — see https://sgit.ai/team/
priority: high      # high | medium | low
opened: 2026-09-07
---
What it is, and what it unblocks. Links are root-relative to sgit.ai.
```

Ids are `N<n>` for needs and `T<n>` for tasks, numbered in order of creation and never reused.
**Moving a card is editing its `status` line.** A card that names a need is closed only by the
author's answer. Corrections to published claims are not cards — they are version-log entries on
the site, so the record of a mistake is never tidied away.

## Working on it

```bash
sgit clone <vault key>              # write access — the site's release engineer holds it
# or, read-only, with the published key:
sgit clone f41d03b0de550479b3c4359709130386df48f34b2cd75e5ed83de28e9776b479:pdulwi6i

# add or move a card, then:
python3 tools/reindex.py
sgit commit -m "board: T12 opened — …"
sgit push
```

The site picks the change up at its next release (`admin/build/release.sh` pulls this vault
before it builds). Opening the vault in SG/Vault shows the board live, from the files, without
waiting for that.

## Provenance

Created 7 September 2026 from the cards that lived in the site repository under
`admin/content/team/issues/` (site v0.2.62–v0.2.63). The pattern — issues as files that version
with the thing they track — is issues-fs.sgit.ai's; this is the smallest useful size of it.
CC BY 4.0.
