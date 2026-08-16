# Working with AI agents — sgit Docs

> The agent-facing surface: sgit write, --json everywhere, sparse clones, the session pattern, and multi-agent collaboration.

*Source: <https://sgit.ai/docs/agents.html> · site v0.2.20 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Docs](index.md) / Guides

# Working with AI agents

sgit is designed to be driven by AI agents as well as humans. A vault is just a folder — the agent reads and writes files normally; sgit handles versioning, encryption, and sync. This page covers the agent-facing surface.

## The session pattern

```
# start of session: get the workspace
$ sgit clone <vault-key> workspace   # or: sgit pull, if already cloned
# … agent works on files normally …
# end of session: persist the state
$ sgit commit -m "session: findings and next steps"
$ sgit push
```

The next session — hours or weeks later, on any machine — runs `sgit pull` and continues. State survives the context window, encrypted end to end.

## `sgit write` — the surgical commit

When an agent needs to record one result, cloning a whole vault is waste. `write` commits a file directly to the vault HEAD in a single call: no working-directory scan, no full clone needed.

```
$ sgit write notes/finding.md --file result.md \
    --message "agent A: analysis" --push --json
{ "status": "pushed", "path": "notes/finding.md",
  "blob_id": "obj-cas-imm-9c2e41ab77d0" }
```

- `--also vault-path:local-file` (repeatable) makes a multi-file write **atomic** — one commit, all or nothing.
- Content-hash dedup: writing identical content returns `unchanged` and creates no commit.
- `--json` gives a machine-readable result for the calling pipeline.

## Machine-readable everything

| Need | Command |
|---|---|
| Read one file, structured | `sgit cat <path> --json` · `sgit cat --id <blob-id>` (zero network calls) |
| List files with fetch state | `sgit ls --json` / `--ids` |
| History for pipelines | `sgit history log --json` · `history diff --json` |
| Health checks | `sgit doctor --json` |

## Fast cold starts

Agents run on time budgets. Three clone modes keep startup cheap:

- `sgit clone --sparse` — structure now, file content on demand via `sgit fetch <path>`.
- `sgit clone-branch` — full history, but only HEAD's content.
- `sgit clone-headless` — credentials only: derive keys and write config, fetch nothing.

## Multi-agent collaboration

Give each agent a named branch; the [two-branch model](two-branch-model.md) guarantees isolation of work-in-progress. Two commands make peer review safe:

- `sgit history show <commit>` and `sgit history diff` are **read-only** — they fetch missing objects on demand without merging, so an agent can inspect a peer's commit without touching its own working copy.
- `sgit resolve --show` renders base/ours/theirs with a per-file verdict, so genuine conflicts are distinguishable from noise — by a human or by an agent.

```
# agent A  $ sgit branch new feature-analysis … commit … push
# agent B  $ sgit history show obj-cas-imm-c4e81a   # look, don't merge
# human    $ sgit pull → review in SG/Vault → merge
```

**For Claude users:** a packaged sgit Skill teaches a Claude session this entire workflow — install, clone, work, commit, push — so cross-session persistent state works out of the box.

[← The two-branch model](two-branch-model.md)[When NOT to use sgit →](limitations.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/docs/agents.html)*
