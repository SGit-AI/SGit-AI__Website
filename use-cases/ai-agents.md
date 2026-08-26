# Agent state that isn't the vendor's to read — sgit use cases

> Durable and shared memory for AI agents in a store that cannot read it: the session protocol, multi-agent branches, sparse clones, and the evidence (this website).

*Source: <https://sgit.ai/use-cases/ai-agents.html> · site v0.2.44 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Use cases](index.md) / AI agents

# Agent state that isn't the vendor's to read

An agent's context window ends; its work shouldn't. Where that work goes is a storage decision that quietly becomes a disclosure decision.

**A worked example, opened with a read key.** The question this page circles — an agent acting with a human's ambient authority because that is the only credential on offer — has a published vault devoted to it: [Agentic Browser Isolation](../demos/vaults/agentic-browser-isolation/index.md), a living risk graph asking whether an agent browses inside *your* browser with *your* logged-in sessions, or an isolated one with a scoped identity. It is vendor-neutral, it cites its evidence outward, and its mechanism is worth borrowing: every altitude has one named owner, a risk stays pending until that owner accepts it personally, and only an accepted risk escalates.

## The problem

Every durable-agent design needs somewhere to put state between sessions: notes, intermediate findings, drafts, the record of what was already tried. In practice that is a database, a repo, or a vendor's memory feature — all of which the provider can read.

That is fine while the state is "which step am I on". It stops being fine the moment the state contains the client's documents, the security findings, the unreleased code, the personal data. At that point the question is no longer about engineering: it is whether you are permitted to put that material there at all, and the answer often arrives from someone who does not care how good the access controls are.

The second half of the problem is coordination. One agent needs durable memory; several agents need *shared* memory with isolation, a review step, and a way to look at each other's work without merging it. That is version control — and version control's usual answer is a host that reads everything.

## What sgit does about it

A vault is a folder. The agent clones it, reads and writes files normally, commits, and pushes; the next session pulls and continues. Encryption happens before anything leaves the machine, so the shared state can hold what a third-party database cannot. Each clone also gets a [private branch](../docs/two-branch-model.md) whose key never leaves that session, so agents can work concurrently without trampling each other, and meet on a shared named branch.

## The recipe

**One agent, many sessions.** The whole pattern is two commands at the session boundaries:

```
# session start — always, before anything else
$ sgit clone <vault-key> workspace   # or: sgit pull
# … the agent works normally: read, write, edit files …
# session end — always, before the context runs out
$ sgit commit -m "session 4: drafted the migration plan" && sgit push
```

**Write a single file without a working copy** — the agent-shaped command, with machine-readable output:

```
$ sgit write notes/findings.md --file ./findings.md \
      --message "add findings" --push --json
```

**Several agents, one vault.** Give each a named branch; let a human own the merge:

```
# agent A  $ sgit branch new research  … sgit push
# agent B  $ sgit branch new drafting  … sgit push
# either agent, read-only — looking is not merging
$ sgit history show <commit>
$ sgit history diff --remote
```

**Big vault, small task.** A sparse clone keeps the agent's working set — and its token budget — proportionate to the job:

```
$ sgit clone <vault-key> workspace --sparse notes/ drafts/
```

## Evidence status

PROVEN

**This website is the evidence.** It is built and published by Claude Code sessions that share state through a vault; the site you are reading was deployed by pushing that vault. Two independent details are worth more than the claim:

- The [Deploy section](../deploy/index.md) is maintained by a *different* team's agent, in a different vault, and rendered here by decrypting it in your browser. Neither agent has access to the other's repository.
- The [cross-team briefs](../briefs/index.md) and the [key-leak incident](../case-studies/exposed-vault-key.md) were written by one agent for another team to act on — including the incident where this agent leaked a key into a public commit, which is the sort of thing a marketing page omits.

Honest limit: n is small, and the agents are supervised by the people who wrote the tool.

## Brief for an agent

Paste this into an agent that has the [sgit skill](../skills/index.md) installed, or point it at the markdown directly.

```
# everything on this site is readable as markdown — no HTML parsing needed
$ curl -s https://sgit.ai/use-cases/ai-agents.md
$ curl -s https://sgit.ai/llms.txt          # the index of everything
```

> Read https://sgit.ai/use-cases/ai-agents.md and https://sgit.ai/docs/agents.md. Then set up agent state in a vault for this project: create the vault, structure the folders as described, commit and push, and report the vault key back to me once — I will store it. Do not write the key to any file in the repository. Then write a short SESSION.md describing the clone/pull-at-start and commit/push-at-end protocol so future sessions follow it.

That last sentence matters. We have a [write-up of the day we got it wrong](../case-studies/exposed-vault-key.md).

## Related

- [Working with AI agents](../docs/agents.md) — the full agent-facing surface: `--json` everywhere, the session pattern, multi-agent collaboration
- [The two-branch model](../docs/two-branch-model.md) — why every clone gets a private branch
- [Skills](../skills/index.md) — packaged instructions that make an agent competent at this without you explaining it

[← Use cases](index.md)[Professional services →](professional-services.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/use-cases/ai-agents.html)*
