# Seven shorts on the licence to operate — the author's walkthroughs

> Seven vertical videos walking through the Licence to Operate vault, collected in the order they are meant to be watched: the mechanism (grant against mandate, blocking, who accepts which risk), how to find and open the vault, and the insurance model behind it — each with what it covers and which part of the vault it demonstrates.

*Source: <https://sgit.ai/demos/vaults/licence-to-operate/videos/index.html> · site v0.2.66 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../../index.md) / [Vaults](../../index.md) / [Licence to Operate](../index.md) / The seven shorts

# Seven shorts on the licence to operate

The author recorded seven vertical videos walking through [the Licence to Operate vault](../index.md) — the mechanism first, then how to open it yourself, then the model behind it. They are collected here in order, with what each one covers and which part of the vault it is demonstrating, so the series is readable as one argument rather than seven unconnected clips in a feed.

## Four words, and the gap between two of them

If you arrived here from a feed with no context, this is the entire model in four terms. Every one of the seven videos is about one of them, or about what happens when one of them is wrong. The numbers in the last column are the ones in the demo you can open below.

|  | What it means | In the vault |
|---|---|---|
| **Grant** | Everything the agent *can* do — the union of every tool, key and permission it actually holds | **12 capabilities** |
| **Mandate** | What it *may* do — the specific job you asked for, and the only thing the policy insures | **4** — `crm:read`, `kb:search`, `llm:generate`, `mail:draft` |
| **The delta** | The gap between them: inside the agent's reach, outside its authority. **Nothing covers these** | **8** — including `crm:export`, `mail:send`, `shell:exec` |
| **Licence to operate** | A policy over the mandate, with a normal band, an overflow pool and named people accepting each risk in advance. Exceed it and the licence is withdrawn | Priced per turn in a live simulation |

The claim the series makes is that the delta is where agent risk actually lives — not in the model, not in the prompt, but in the distance between the capability you handed over and the job you asked for. Nobody asked for `shell:exec`; nothing insures it; the agent can still reach it. Write the two sets down side by side and the risk stops being a discussion and becomes a number.

**Open the thing the videos are showing.** It runs in a browser, read-only, with no account and nothing to install — the read key below is the whole credential.
 Read key: `d990a52efb9af32c8463e2962f3ca5ccf92b3b6e8ea788e55009073c29b4da29:posrhzp3`
[**The Licence to Operate vault on this site →**](../index.md) · [open it directly in the vault UI ↗](https://dev.vault.sgraph.ai/#d990a52efb9af32c8463e2962f3ca5ccf92b3b6e8ea788e55009073c29b4da29%3Aposrhzp3)

**Where this goes commercially: [RiskMandate.ai ↗](https://riskmandate.ai/)** — the business risk layer for autonomous systems: every autonomous system mapped to its blast radius, given a business owner, and driven to a time-bound decision — **accept, fund, or fix**. What you are about to watch is that model made concrete for a single agent. The vault is the demonstration; RiskMandate is the product it is a demonstration *of*, and [the Risk Graph Explorer](../../risk-graph-explorer/index.md) is the same engine already published as a vault.

## The order they are meant to be watched in

The series has three movements, and they are not in the order a viewer arriving from a feed would guess:

|  | Videos | What they establish |
|---|---|---|
| **The mechanism** | 1 · 2 · 3 | Grant against mandate, what a block looks like when an agent exceeds its mandate, and who in the organisation accepts which risk |
| **The artefact** | 4 | How to find and open the vault on this site — the shortest one, and the one to send someone who wants to poke at it themselves |
| **The model** | 5 · 6 · 7 | Why the grant/mandate gap is where risk lives, the insurance framing that governs it, and the policy, claim and premium mechanics underneath |

Short 1 · the mechanism

### Grants, mandates & token policies in AI agent workflows

A walkthrough of the MVP, demonstrating how agents are governed through a clear separation of what an agent *can* do (the grant) versus what it *should* do (the mandate).

- **Grant against mandate** — permitted actions versus expected behaviour
- **Token-based policy enforcement**, with normal-use thresholds and overflow pools
- A live demo of normal insurance and CRM flows **staying within policy**
- What happens when token budgets are exhausted — **automatic escalation**
- Blocking behaviour when an agent attempts an action **outside its allowed scope**

**In the vault:** the grant of 12 capabilities and the mandate of 4, and the simulated conversation where every reply carries its cost against a live policy.

Short 2 · the mechanism

### Blocking AI agents that exceed their mandate

What happens when an agent attempts an action that is **technically within its system privileges but outside its defined mandate**.

- An agent blocked when it tries to send a password reset email **without being mandated to**
- The difference between what an agent *can* do (grant, privileges) and what it *should* do (mandate)
- How an agent **loses its licence to operate** when it steps outside its approved scope
- A second example: a CRM data export it has access to but is not authorised to perform
- **Pre-action checks (ideal) versus post-action detection (problematic)**

**The distinction that carries the series:** a privilege the agent holds is not a permission to use it. That last bullet — catching it before rather than after — returns in short 6 as the sharpest version of the argument.

Short 3 · the mechanism

### Risk acceptance flow — who accepts what, and why

The risk-acceptance side of the framework: how risks cascade upward through an organisation, from the support team to the C-suite.

- Risks linked upward through the layers — **support team → SRE → platform owner → CTO → CPO → CFO**
- What each stakeholder actually accepts: token and rate limits, mandate overruns, database change risk, cost and premium exposure
- Why the **platform owner** must accept that an agent can act outside its mandate, because of capabilities like a mail client, a shell and export tools
- A **withdrawn licence**, simulated out of band, automatically enforcing policy and restricting the agent
- Pre-defining the rules of the game, so agents operate **only when a valid policy exists**

**In the estate:** this is [risks.sgit.ai](../../../../network/index.md#risk-governance)'s acceptance model applied to an agent — a risk cannot be denied, only accepted by a named person for a stated interval. The same model the [Risk Graph Explorer](../../risk-graph-explorer/index.md) vault publishes.

Short 4 · the artefact — start here if you want to poke at it

### How to find and open the vault on sgit.ai

Exactly where the vault is on this site, and how to open it in your browser. No account, nothing to install.

- Navigating to [Published Vaults](../../index.md) on sgit.ai
- Locating **vault #23** — the Licence to Operate vault
- Exploring the contents: decks, docs, grants, mandates, policies, risks and more
- Opening the vault in a new window to interact with it
- The vault structure — `app.json` as the entry point, and `index.html`

**The shortest route:** the vault's read key is on [its page](../index.md), and it is the whole credential — the same string the video walks you to.

Short 5 · the model

### The grant against mandate gap — where risk lives

When you deploy an agent you typically give it far more capability than it needs. **The gap between the two is where risk lives.** An agent might have full access to your email account while your mandate only requires it to write drafts, never to send. Making that gap explicit is the first step to controlling it.

- The **grant**: the union of all actions an agent is authorised to perform
- The **mandate**: the specific tasks you actually expect it to do
- Why the gap is a security and governance concern rather than an accounting detail
- How capabilities **expand over time** — new tools, environment changes, prompt updates
- How visualising the gap helps you monitor, contain and manage agents

**In the vault:** the **delta** — the 8 capabilities in the grant that no policy covers. The vault page calls this the idea worth stealing, and this is the video that explains why.

Short 6 · the model

### An insurance model for governing AI agents

What if every agent had to **prove it has a licence to operate** — as licensed professionals do in regulated industries? An insurance-based operating model that governs agents through defined mandates, scoped policies and risk underwriting.

- **Licence to operate** — why every agent needs a mandate, not just a badge
- **Grant, mandate, delta** — mapping what an agent can do against what it should
- **The normal band of operation** — token and record thresholds that limit exposure at scale
- **Claims, must-ask and refused tiers** — controlling thousands of agents with a tiered policy
- **Three ways to lose your licence** — overuse, out-of-scope action, or pool lapse
- **Pre-check versus post-check**, and why post-check is far riskier

**Why this is the one to watch if you watch one:** it is the whole framework in a single pass, and it is the video that connects the vault to [the AIUC-1 conformance layer](../../aiuc-1-conformance/index.md), which computes insurability as a query into a `policy/v1` object.

Short 7 · the model

### Policies, claims and risk acceptance

A deep dive into the insurance model powering the MVP: how policies (licences) are sold to agent owners, how claims are triggered when token thresholds are exceeded, and how a credit balance tracks the flow between premiums and claims.

- Selling policies to business owners as **a cost model for running agents**
- Token-based claim triggers, and the **balance and credit pool** mechanism
- Mapping **facts → risks → roles → the corporate risk register**
- Why risks **cannot be denied** — only accepted in advance
- How pre-accepted risks streamline the human in the loop, and enable scale

**The line that ties the series to the rest of the estate:** *risks cannot be denied, only accepted in advance.* That is the position [risks.sgit.ai](../../../../network/index.md#risk-governance) argues from first principles, and the reason there is no deny button anywhere in this model.

## Where to go next

- **Open the thing itself.** [The Licence to Operate vault](../index.md) — the read key is on the page, and the vault runs live inside it.
- **The insurance model, computed.** [The AIUC-1 conformance layer](../../aiuc-1-conformance/index.md) turns this framing into a query: conformance states become conditions and exclusions on a policy, and moving the date forward turns conditions into exclusions with nobody editing anything.
- **The acceptance model it inherits.** [The Risk Graph Explorer](../../risk-graph-explorer/index.md), and [its three walkthroughs](../../risk-graph-explorer/videos/index.md) — which are transcribed, and are the standard this page is not yet meeting.

All seven videos are on [the author's channel ↗](https://www.youtube.com/@diniscruz-ai). Embedded through `youtube-nocookie.com`, and lazily — opening this page sets no YouTube cookie until you press play on one. The text under each video is the author's own description, not a transcript: these seven carry no caption track, so the spoken words are not on this site yet and [transcribing them is on the board](../../../../team/board.md). [← The vault](../index.md) · [All published vaults](../../index.md)


---

*[Site index for agents](../../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/licence-to-operate/videos/index.html)*
