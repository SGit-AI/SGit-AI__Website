# Use cases — sgit

> Who has the problem sgit solves, with a working recipe and an honest evidence status for each: AI agents, professional services, security teams, health and regulated data — plus the underlying workflows.

*Source: <https://sgit.ai/use-cases/index.html> · site v0.2.5 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / Use cases

# Use cases

Two kinds of page here. **Workflows** are the mechanics — what sgit does, on shipped commands. **Situations** are who has the problem, each with a working recipe, an honest evidence status, and a brief you can hand to an agent.

**Reading this as an agent?** Every page on this site has a `.md` twin at the same path — this one is [use-cases/index.md](index.md). Internal links inside the markdown point at markdown, so you can traverse the whole site without parsing HTML. The machine index is [llms.txt](../llms.txt).

## Situations

Each of these is a place where the sentence "this needs version control, and the store must not be able to read it" is literally true. The pages are written to be usable: the setup, the commands, what is proven versus what is a pattern, and an agent brief.

[AI agents### Agent state that isn't the vendor's to readDurable memory across sessions and machines, and shared memory between agents, with the store unable to read either. **Evidence: this website.**](ai-agents.md)

[Professional services### Working documents with clientsLegal, M&A, audit, assessment: the deliverable and the working notes, versioned, in a store that cannot read them — and read access you can hand out without an account.](professional-services.md)

[Security teams### Findings about your own weaknessesPentest output and vulnerability data need history, diffs and multi-person workflow — and are the last thing to put in a SaaS you don't control.](security-teams.md)

[Health & regulated### Data that changes what is permissibleWhen the host provably cannot read the content, the conversation stops being about the provider's access controls. Read the caveats on that page before quoting it.](health-regulated.md)

## Workflows

The mechanics underneath those situations. Every one runs on shipped commands — nothing aspirational.

## Private memory for AI agents

An agent's context window ends; its work shouldn't. A vault is just a folder — the agent clones it, reads and writes files normally, commits, and pushes. The next session pulls and continues where the last one stopped. Everything is encrypted before it leaves the agent's machine, so the shared state can hold things you would never put in a third-party database: client documents, security findings, personal data.

```
# session 1
$ sgit clone <vault-key> workspace
$ sgit commit -m "session 1: research notes" && sgit push
# session 2, days later, different machine
$ sgit pull   # continue exactly where session 1 stopped
```

[Full agent guide →](../docs/agents.md)

## Multi-agent collaboration

Give each agent its own named branch. Every clone also gets a private clone branch whose key never leaves that agent's session, so agents cannot trample each other's work-in-progress. Work meets on named branches, and a human reviews the merge. Agents can inspect each other's commits read-only with `sgit history show` and `sgit history diff` — without pulling, so looking never means merging.

```
# agent A  $ sgit branch new feature-analysis … sgit push
# agent B  $ sgit branch new feature-report   … sgit push
# human    $ sgit pull → review → merge, with sgit resolve --show on conflicts
```

## Human ↔ agent workspaces

The same vault has two doors: you in the SG/Vault web app, the agent in the CLI. The browser client is an independent implementation of the same wire format — you browse, edit and review in a UI while the agent works the same files from the terminal. Both sides see each other's commits; neither side's plaintext ever touches the server. (How the browser side works: [sgraph.ai](https://sgraph.ai).)

```
$ sgit vault info
  Web URL: https://vault.sgraph.ai/en-gb/#<your-vault-key>
```

## Encrypted folders with history

A shared folder where the hosting provider cannot read the contents — with commits, diffs, and rollback. Work offline, commit locally, push when ready; restore any prior version with `sgit history revert`. Vault-level `backup` and `restore` produce portable archives, and `sgit vault move` rotates keys if a key is ever exposed.

```
$ sgit init --existing        # vault-ify a folder you already have
$ sgit commit -m "baseline" && sgit push
$ sgit history revert --commit obj-cas-imm-b2d70f   # roll back
```

## Signed & encrypted file exchange

Alongside vault sync, sgit ships a PKI toolset: generate keypairs, exchange public keys as contact bundles, then sign, verify, encrypt and decrypt individual files for named recipients — useful when a file has to travel outside a vault but still needs integrity and confidentiality.

```
$ sgit pki keygen --label "release keys"
$ sgit pki sign report.pdf --fingerprint <fp>
$ sgit pki encrypt report.pdf --recipient <fp>
```

[← Why this exists](../why/index.md)[Documentation →](../docs/index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/use-cases/index.html)*
