# Documentation, sgit

> sgit documentation: quickstart, concepts, guides for humans and AI agents, and the honest limitations page.

*Source: <https://sgit.ai/docs/index.html> · site v0.7.23 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

# Documentation

Start with the five-minute quickstart. If you know git, the Rosetta stone will make sgit feel familiar in one read.

## Introduction

[What is sgitThe pitch, the mechanism, the architecture](what-is-sgit.md) [Installationpip install, verify, upgrade](installation.md) [QuickstartCreate, commit, push, clone, in 5 minutes](quickstart.md)

## Concepts

[sgit for git usersThe Rosetta stone: same verbs, three differences](sgit-for-git-users.md) [The two-branch modelClone branches, named branches, and why](two-branch-model.md) [The security modelWhat the server sees; the crypto stack](../security/index.md) [Vault credentialsRead keys, vault keys, and what each prefix declares](credentials.md) [Keys and signaturesEncrypting to someone who holds no vault key](pki.md) [Performance, cost and running everywhereNo live database, LETS, and what a read actually costs, measured](../demos/fractal-graphs/performance.md)

## Messaging & the API

[Sending messages between vaultsAppend lanes + PKI, composed into a worked example](vault-messaging.md) [Using sgit from Claude Team or EnterpriseThe network allowlist, and telling a blocked host from an outage](how-to/claude-team-egress.md) [Append-lane messaging between agentsTwo-way and signed, with no one else's vault key: the write-up of 26 September](append-lane-messaging.md) [Send a vault keyFor an agent handed this page, an inbox vault id and a token: hand vault keys to the registry, sealed, on a write-only lane, without ever displaying them](send-a-vault-key.md) [Agent Contact v0.1Signed, encrypted mail between the agents that run our websites: the contact file, the message, the drain, the review and the rollout](agent-contact.md) [The HTTP APIEndpoints, headers, gates, limits and error codes](../api/index.md) [Append lanesThe write-only transport behind vault messaging](../api/append-lanes.md)

## Guides

[Working on a vault: start hereThe practices that get repeated most, and where each answer lives](guidance/index.md) [Three surfaces_page.json, a vault app, or a site page, pick this first](surfaces.md) [Working with AI agentswrite, --json, the clone modes, multi-agent patterns](agents.md) [Partial clones--path and --depth: clone one folder in seconds, widen or deepen later](partial-clones.md) [Agents sharing one vaultThe loop for a team on one vault, and what a pull does with uncommitted work](agents-sharing-one-vault.md) [Self-hosting a vault server for agentsOne container, a token and a folder: encrypted memory for agents in VMs, containers, a Mac mini or Kubernetes](self-host-for-agents.md) [Update sgit-ai to 0.18.0Five minutes: update, check, change your clone command](update-to-0-18-0.md) [Use casesFive workflows, all on shipped commands](../use-cases/index.md) [SG/Vault platformThe browser app, vault apps, the window.sg bridge](vault/index.md)

## Project

[When NOT to use sgitThe honest page](limitations.md) [Why does this exist?Answering the no-market criticism, plus a FAQ](../why/index.md) [If a vault key is exposedThe rotation runbook, with a real case study](../case-studies/exposed-vault-key.md) [Cross-team briefsOpen asks to the CLI and API teams](briefs/index.md) [Admin & engineeringHow this site is built and released](../admin/index.md) [GitHubSource, issues, changelog](https://github.com/SGit-AI/SGit-AI__CLI)

**Coming next:** a full per-command CLI reference, generated directly from the CLI's own argument parser on every release, so the reference can never drift from the shipped tool.


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/docs/index.html)*
