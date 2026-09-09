# sgit.ai, for investors — published in the open

> The problem, what sgit is, the open-source zero-knowledge architecture, traction computed from the site itself, the business model (the code is free; the running service is sold), the beachhead market, what could go wrong — and the ask, left visibly open until the founder states it rather than invented.

*Source: <https://sgit.ai/investors/index.html> · site v0.2.73 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / Investors

For angel investors · published in the open

# sgit.ai, for investors

Everything the founder's companies publish for investors, they publish in the open — the pitch, the model, the numbers — and this page follows that rule. What is here can be checked against the site it sits on. What is not here yet is marked as not here yet, rather than filled in.

## The problem, in one sentence

**AI agents are producing an enormous amount of work, and there is no good unit to hand it over in.** A report, a dataset, an application, a talk — today each needs hosting, an account, a deploy, and a trust relationship with whoever runs the server. Meanwhile the state agents need to share with each other and with people is versioned by nobody and readable by the host. The tools that exist were built for source code (git) or for storage (cloud drives). Neither was built for *a unit of work that carries its own app, history and sources and can be handed to a stranger with one string*.

## What sgit is

**Git for encrypted vaults.** A vault is a folder that is versioned like git — clone, commit, branch, merge, history — encrypted on the client before anything leaves the machine, and openable by anyone who holds the read key: no account, no install, nothing hosted by the reader. A vault can carry its own application, sandboxed, with the permissions it asks for declared in a file. The server stores ciphertext and hashes and cannot read what it stores.

| Layer | What it is | Who runs it | Licence |
|---|---|---|---|
| **sgit** | The CLI — `pip install sgit-ai`. Pure Python, two runtime dependencies. | Anyone | Apache-2.0 |
| **SG/Vault** | The web app: browse, edit and run vault apps in the browser. An independent implementation of the same wire format. | sgraph.ai, or self-hosted | Apache-2.0 |
| **SG/Send** | The zero-knowledge storage API both clients speak to. | sgraph.ai (hosted), or self-hosted — [the guidance is published](../docs/vault/static-hosting.md) | Apache-2.0 |

The proof is not this page. It is the [published vaults](../demos/vaults/index.md): real artefacts — a penetration test report with a retest script per finding, a compliance standard rebuilt as a citable graph, a Black Hat keynote with its cited papers, a game that reports anonymous telemetry through a write-only channel — each opened by one string, each audited before its key went public. Open one before reading further.

## Strategic architecture: open source, zero knowledge, zero lock-in

- **100% open source.** The CLI, the web app and the server are Apache-2.0. There is no proprietary tier of the code. The commercial line is the running, maintained, certified *service*, which is where the founder's [published position on open source ↗](https://open-source.sgit.ai/views/index.html) says it belongs.
- **Zero knowledge, published as a threat model.** [What the server sees](../security/index.md) is listed — object ids, ciphertext, sizes, timing, the vault id — and so is what it cannot. The security model is a page, not a claim.
- **Zero lock-in, deliberately.** Self-hosting guidance is published, live, in a vault. If the hosted service ever becomes unpalatable, a customer runs their own server and their data and workflow are unaffected. That is a feature of the business model, not a concession: *"as soon as you move into rent extraction, you lose sight of it."*
- **Built for agents first.** Machine-readable output on every read path, single-call commits, sparse clones, a permission model that is default-deny, and an LLM bridge where the app never holds the API key.

## Traction — computed from this site, not typed onto it

These numbers are generated at build time from the site's own data. If one is wrong, the site is wrong somewhere else too.

101**site releases since 14 August**
each verified live before it was called done

26**vaults published with a public read key**
every one audited first; findings on the page

19**sibling sites on *.sgit.ai**
one question each, own repo, own history

45**articles and release notes**
all with a markdown twin and an RSS feed

10**cross-team briefs, in the open**
two of them corrected this site

~4,000**tests in the CLI, mutation-tested in CI**
against a real server, no mocks

Behind the numbers: the site and every vault on it are built by **one person and a team of AI agents**, and the agents build for each other — a brief published here was turned into a working vault by another agent the same day, reviewed by the team that owns the API, and the review's corrections are published above the original. That loop is the product being used to build the product, and it is [documented as a method](../team/index.md).

## Business model

**The code is free. What is sold is the running service, and the trust that comes with running it well.**

- **Hosted vaults** — SG/Send storage and SG/Vault as a maintained, certified service at sgraph.ai. The customer's data is ciphertext to us; what they pay for is availability, durability, versions, and somebody to call.
- **The open-source strategy is the moat, not the code.** *"A competitor who forks our code today gets our position as of today. They do not get our velocity."* The published record — every release verified live before it was called done, every mistake recorded with the rule it produced — is that velocity made visible; the count is in the traction tiles above, computed rather than typed.
- **Adjacent products on the same layer.** RiskMandate.ai, the AIUC-1 conformance work and the licence-to-operate model for agent insurance are all built on vaults; several are [published here](../demos/vaults/index.md). The layer sells because things get built on it.

open-source.sgit.ai · Business & publishing — [The position — open source is a strategy, not a charity ↗](https://open-source.sgit.ai/views/index.html) — Technology is not the moat; lock-in relocates to quality, certification and maintainability; the moat is a rate, not a wall. The full argument, with its counter-cases named. — “Open source is a strategy. It is not a charity.” — part of the sgit.ai network

## Market: the beachhead, and what it opens

**Beachhead: teams that already run AI agents and need the output to be auditable, encrypted and handed over.** Security and compliance work is where this bites first — a pentest report, a conformance assessment, a risk register — because the deliverable must carry its evidence and the recipient cannot be asked to trust a portal. Every published vault in that category was built by an agent and handed over with one string.

**Expansion: any team whose agents produce work for other people.** The same unit — data, app, history, sources — is a pitch deck, a research pack, a talk, a health record, a game. The [vaults table](../demos/vaults/index.md) is already spread across eight categories, none of which is "encryption".

## The ask

**Not filled in — and not invented**
**Round size, instrument and use of funds are the founder's to state**, and they are not on this page yet. Following the rule that nothing here is a number the author has not supplied, this box stays open until it is filled, and the gap is tracked in the open on [the board as N1](../team/board.md#N1). When it is filled, it will follow the same shape as the founder's other open pitches: the amount, what it buys in the next eighteen months, and the split.

## What this is not, and what could go wrong

- **It is beta.** The site says so in its nav on every page. [When not to use sgit](../docs/limitations.md) is a published page, and it is linked from the homepage trust strip.
- **The multi-agent claim has one gap.** The homepage says *a branch per agent, a human reviews the merge*; no published vault yet shows two agents merging in one history. The gap is named on the homepage and tracked on the board.
- **"They do not get our velocity" is empirical, not structural.** It holds while the team is faster. The founder's own position page names this as its weakest point.
- **Hosted zero-knowledge storage has a small set of well-funded neighbours.** The difference claimed is not encryption — it is the unit of work: versioning, apps inside the data, and the agent-first surface. Whether that difference is the one buyers pay for is the thing the beachhead has to prove.

## Investor materials, in the open

| Material | Where | State |
|---|---|---|
| This page, as a printable one-pager | Print it — the site has a print stylesheet | live |
| The security model and threat model | [/security/](../security/index.md) | live |
| When not to use it | [/docs/limitations](../docs/limitations.md) | live |
| Every release, with what went wrong | [/admin/versions](../admin/versions.md) | live |
| The published vaults — the product, in use | [/demos/vaults/](../demos/vaults/index.md) | live |
| How the company is built: one human, a team of agents | [/team/](../team/index.md) | live |
| The founder's record and interests declared | [open-source.sgit.ai/about ↗](https://open-source.sgit.ai/about/index.html) | live |
| The ask, use of funds, the deck | this page, [N1](../team/board.md#N1) and [N2](../team/board.md#N2) | **waiting on the founder** |

The founder's other companies publish their investor relations in public repositories ([MyFeeds.ai ↗](https://github.com/the-cyber-boardroom/MyFeeds-AI__Investor_Relations), [The Cyber Boardroom ↗](https://github.com/the-cyber-boardroom/cbr-investment)). sgit.ai's will follow the same practice: this page is the first file in it.

Contact: through [LinkedIn ↗](https://www.linkedin.com/in/diniscruz), or the [repository](https://github.com/SGit-AI/SGit-AI__CLI). If anything on this page is wrong, say so and it will be corrected above the mistake — that is [how this site works](../team/roles/historian.md).


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/investors/index.html)*
