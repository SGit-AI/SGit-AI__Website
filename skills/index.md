# Skills for AI agents — sgit

> Packaged, versioned instructions that make any AI agent an effective sgit and vault user: operate the CLI, build vault apps, author vault content.

*Source: <https://sgit.ai/skills/index.html> · site v0.2.8 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

# Skills — sgit for AI agents

A skill is a packaged set of instructions an AI agent loads to do a job well: the commands that matter, the patterns that work, the traps already hit and documented so the agent doesn't hit them again. sgit treats agents as first-class users, so its skills are first-class artifacts — versioned, verified against specific releases, and shipped right here in this vault.

## The three skills

## Operate

[use sgit and vaultsThe CLI end to end — and the cross-session pattern: clone/pull at session start, commit + push at session end, so state survives the context window. Includes the multi-agent branch-per-agent workflow.](use_sgit-and-vaults__SKILL.md)

## Build

[create vault appsThe vault-app playbook: the authoring contract, what the host gives you for free, proven layout patterns, the validation gate, and a nine-row table of failure modes with fixes — all bug-fixed against real vault behaviour.](create-vault-apps__SKILL.md)

## Author

[create vault contentStructured content without code: the full _page.json schema (embedded — no repo clone needed) and vault markdown authoring, with checklists and copy-paste templates.](create-vault-content__SKILL.md)

## Installing a skill

For Claude Code and compatible agents: drop the skill file into your skills directory (e.g. `~/.claude/skills/<name>/SKILL.md`) or paste it into the session as context. The skill's own description tells the agent when to trigger it. A minimal bootstrap for a fresh session is one line:

```
$ pip install sgit-ai && sgit clone <vault-key> workspace
# then read skills/ inside any vault that ships them — like this one
```

The skills above are the canonical current versions, verified against sgit-ai v0.14.x and the current app-shell. They carry their own honesty markers — including which CLI commands are disabled right now and which platform features are trial-only — so an agent reading them gets ground truth, not marketing.

**Also for agents:** this site ships an [llms.txt](../llms.txt) at the vault root — the standard machine-readable index. Inside the vault it is encrypted like everything else (agents holding the key read it via `sgit cat llms.txt`); on a static deployment it becomes a plain public llms.txt. Same file, two trust contexts.

[← Working with AI agents](../docs/agents.md)[The SG/Vault platform →](../vault/index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/skills/index.html)*
