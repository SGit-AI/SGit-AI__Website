# The RiskMandate sandbox: three twins, one policy, a real model, and the question of whose key

> A project brief for a place where an Agent Behaviour Policy is tested rather than read. A real model runs against a simulated inbox, through a simulated OAuth connector and a simulated MCP connector, with and without a policy, and the two footprints sit side by side. What already exists in the __Send project and on this site, the four ways a model gets called from a browser with no server, what the providers' terms say about selling keys, a map of who can cap spending, and the build plan.

*Source: <https://sgit.ai/docs/briefs/riskmandate-sandbox-twins-and-tokens.html> · site v0.7.22 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../index.md) / [Briefs](index.md) / The RiskMandate sandbox

# The RiskMandate sandbox: three twins, one policy, a real model, and the question of whose key

**A project brief from the sgit.ai site team, for the RiskMandate.ai team and the SG/Send teams.** Status: draft for the founders to review. Written 2 October 2026 from a voice memo. Nothing in it has been built as a whole; most of its parts have, and the brief says which.

The sandbox in one picture. An agent, a real model, calls a simulated MCP connector, which calls a simulated OAuth connector, which reads and writes a simulated inbox held as files in a vault. The policy sits across the top and can be switched off, so the same scenario runs both ways. On the right, the four ways a model can be reached, all from the browser. Illustrative.

## What this is, in one paragraph

A place where an Agent Behaviour Policy can be tested rather than read. You pick a scenario, say an inbox agent asked to clear a backlog, and the sandbox runs a real model against a simulated inbox, through a simulated connector, under a simulated permission prompt. Nothing is live: no account, no Gmail, no OAuth grant. The run produces a footprint, every tool call with its result. Then you run it again with a policy in place, and the two footprints sit side by side. The difference is what the policy bought, and the [gap rows the agent reached, shaded by blast radius](../../articles/footprint-and-blast-radius.md), are what it did not. The sandbox is also where a policy gets written, because the fastest way to write one is to watch the agent without it first.

## Why write it here first

Because the parts are here. The vault LLM bridge, the connector twin, the chat panel with tools, the one-prompt workflow, the vault-app proofs of concept, the synthetic users run, the provider reports, and now footprint and blast radius: every one of them is a published page or a published vault on this site or a sibling, with a read key and an audit. The RiskMandate team has the policy and the sixteen published examples. A brief written from here can point at a running thing for almost every box in the picture and say what is missing, which is the assembly. Written from the RiskMandate side it would have to describe the vault machinery second-hand. So: the brief here, the product there, and the sandbox vault itself published on both.

## Three names, and which to use

- **Sandbox** for the place. It says safe to break, which is the point. "Playground" is what the model vendors call a prompt box, and "eval" is a measurement, not a room.
- **Evals** for the scenarios. Each one is a seeded inbox, a task, an optional policy, and a model, and it produces a footprint that can be scored. The word is already what the industry uses for exactly this, and it says the result is a number, not a feeling.
- **Twins** for the simulated systems, as in the [connector twin](../../articles/connector-twin-before-you-deploy-an-agent.md). A twin behaves like the real thing at the boundary and records everything that crosses it.

## The three twins, and why three

The memo's instinct that an inbox needs three twins, not one, is the architectural centre of this. Each layer adds a different kind of constraint, and a policy has to be tested against all of them.

| Twin | What it simulates | What it adds that the layer below does not | Starts from |
|---|---|---|---|
| **1 · The inbox store** | The data: messages, threads, labels, drafts, trash. Files in a vault, seeded per scenario, append-only so every change is kept. | Nothing yet; it is the ground truth. Its history is the footprint recorder for the whole stack. | The Vault Chat app's in-memory file system, which already exists with tests; the Email-FS message shape this site's agents already use. |
| **2 · The OAuth connector** | Gmail as its API exposes it, with the scopes enforced. `gmail.modify` can read, send, label and move to trash but cannot permanently delete; only `https://mail.google.com/` can. Errors come back shaped like the real ones. | The platform's barriers. These are the only true boundaries in the stack, and the twin has to get them right or the policy is tested against a fiction. | The [Connector Twin vault](../../demos/vaults/connector-twin/index.md), which already records and replays inbox and calendar calls with side effects named. |
| **3 · The MCP connector** | What the chat product puts on top: which tools are exposed, the allow-once and always-allow prompts, and the approval card that asks you to approve a label without telling you which message or which label. | The human-in-the-loop as it actually is: a prompt with too little context, a button that removes future prompts, and settings that do not always persist. This is where "the user approved it" gets its real meaning. | The [agent permission games](../../demos/vaults/agent-permission-games/index.md) vault and the [six agents](../../articles/six-agents-one-inbox.md) article. Anthropic's public issue trackers document the always-allow behaviour across plans and surfaces in detail. |

The agent sits on top with a real model, chosen per run. Its calls go down through the three twins and the results and errors come back up. The policy, when on, is in the agent's context and, where the harness supports it, enforced at twin 3. When off, the agent has the reach and nothing else.

## What a run shows

1. **The footprint.** Every tool call, its arguments, its result or error, and the twin that answered it. Written to the sandbox vault, so it is signed, versioned and readable with a read key.
2. **With and without.** The same seed, the same task, the same model, policy on and policy off, side by side. The gap rows the agent reached without the policy, and whether it still reached them with it.
3. **Blast radius per row.** Each row the agent touched, shaded by what it would have cost against the seeded inbox at that moment: a draft is nothing, a send as the owner is the business, a permanent delete is hatched because there is no way back.
4. **Per model.** The same eval across models, because a policy that one model honours and another ignores is a finding about the model as much as the policy.
5. **Per harness.** The same eval through the products that say they log, control and enforce agent behaviour. If a harness enforces at twin 3, the footprint shows rows blocked that the bare run reached. If it only logs, the footprints match and the claim is measured.

## What already exists

The list below is what the brief could verify from the published record. The Librarian's pass through the __Send project is in the next section.

| Piece | State | Where |
|---|---|---|
| Vault LLM bridge: a vault app calls a model and never holds the key | **Shipped.** Key in `.vault/llm/config.json`, below the permission floor; `sg.llm.available / chat / cancel / models / usage`; grants default to deny; three chat surfaces, two of them with no app code | [llms.sgit.ai](https://llms.sgit.ai/) |
| The bridge's own limit, in its own words | "The bridge protects your key; it is not yet a boundary that prevents all egress." | [llms.sgit.ai/security](https://llms.sgit.ai/security/) |
| Bring-your-own-key chat on a static page, with a fallback that needs no key | **Shipped.** Three tiers: local matcher, OpenRouter key in the browser, the bridge | [Chat on a static site](../../articles/chat-on-a-static-site.md) |
| A site-wide chat pane whose model calls tools over the site's index | **Shipped**, v0.2.63 | Every page here |
| Connector twin: record and replay what an agent saw and did at a connector | **Shipped** as a business plan vault with a working replay demo | [Connector Twin](../../demos/vaults/connector-twin/index.md) |
| Vault apps that write real files into a vault from a form, and test the platform rather than trust it | **Shipped** (POC-08, POC-09) | [Vault app proofs of concept](../../demos/vaults/vault-app-pocs/index.md) |
| Synthetic users walking a site and writing up what they found | **Shipped**, two runs | [Synthetic users, RiskMandate](../../demos/vaults/synthetic-users-riskmandate/index.md) |
| Bounded provider credentials: a key with a spend limit and a reset, proven to stop at the limit | **Shipped** for ElevenLabs; OpenRouter specified, not built | [providers.sgit.ai](https://providers.sgit.ai/) |
| Agent Behaviour Policy: reach, mandate, gap, barriers; sixteen published examples | **Shipped** | [riskmandate.ai](https://riskmandate.ai/abp.html) |
| Footprint and blast radius: the vocabulary the sandbox reports in | **Proposed**, 2 October | [The article](../../articles/footprint-and-blast-radius.md) and [the brief](riskmandate-footprint-and-blast-radius.md) |
| The three twins as one stack, the eval format, the with-and-without view, the harness comparison | **Not built.** This is the sandbox. |  |

## What the __Send project already holds

The Librarian of the SG/Send project was asked six questions against the repository at v0.33.69. Paths are inside that repository; nothing was changed. The short version is that the chat, the file system, the bridge and the commercial model are further along than the memo remembered, and the twins are entirely on paper.

| Asked about | Found | Where |
|---|---|---|
| **The one-prompt workflow** | Exists under the name **one-shot**. A March article draft, never published: "When I send a one-shot request via API, I control the model's entire universe. Everything the model doesn't need? Simply absent." A March architecture brief: "curate reality, send it all at once, get the answer, then use the answer to improve the reality for the next prompt." A June brief records it "now starting to work in practice." The onboarding variants, one prompt pasted into Lovable or into Claude, are the same idea applied to agents. The memo's instinct to bring it back is right; the article is sitting in `team/humans/dinis_cruz/briefs/03/09/`. | `briefs/03/09/article__one-shot-llm-controlling-reality.md`; `briefs/03/30/v0.19.7__arch-brief__oneshot-feedback-loops.md`; `briefs/06/16/tools-and-memory/` |
| **A chat with tools and a file system in a vault** | **Shipped**, twice. The **Vault Chat** app (phases 1 to 4, June 2026) has an in-memory file system, tools for list, read, stat, exists, write, create folder, rename and delete, a consolidate-memory tool, and three flush modes to the vault: ephemeral, snapshot and synced. Every turn is written to `/chat/history/`; `/.vault/**` is unreachable from the tools, and a run-code tool "cannot be enabled by any UI or injection because it isn't in the registry." The **native AI chat panel** (August) sits on every vault and app: "the default is no tools at all," with opt-in groups for session costs and read-only file access, grants committed to `/.vault/llm/tools.json`, and tool results fenced as untrusted data. | `en-gb/vault/chat/`; `_common/js/lib/vault-chat/`; `_common/js/components/vault-llm-chat/`; dev pack `v0.27.80__vault-chat` |
| **The bridge** | **Shipped**, OpenRouter only in phase one, with Ollama in the older workspace UI. Ten verbs, four grants, nine error codes, one of them `EBUDGET`. Bring-your-own-key: the vault admin pastes an OpenRouter key in settings. Two tiers: an **owner** tier sealed with a key derived from the vault's write key, so "an RO session cannot derive this key and cannot open owner secrets," and a **shared** tier where the key is in the file in clear, encrypted only at rest. The brief that shipped it says the limit plainly: "Sharing the vault key shares the ability to spend it. Short-lived minted credentials are planned." The architect's as-built review: egress lockdown did not ship, "a malicious app could still call an LLM provider itself with its own key," and the network grant is "a dead grant." | `AUTHORING.md` lines 1065 to 1295; `sg-llm-config.js`; `sg-vault-owner-secrets.js`; architect review `08/13 v0.33.47` |
| **Spending control in the bridge** | Default limits of one dollar and two hundred calls per session, eight thousand tokens per call, two concurrent, overridable per app, with a five-hundred-entry cost ledger that separates billed from estimated and exports CSV. The code comment is the sentence this brief needs: "NOT security: the enforceable cap is the upstream key's own credit limit." Which is why the bounded key is the barrier and the bridge's limits are settings. | `sg-llm-config.js``DEFAULT_LIMITS`; `vault-llm-log.js` |
| **A virtual file system twin** | **Shipped** as `MemoryVfs`, "the LLM's working set: an in-context, commit-free file system," with pull-through from the vault on a miss, reserved paths, a mock `window.sg` for tests, and unit tests. This is twin 1's foundation, ready. An S3-compatible vault twin for boto3 is proposed, not built. | `_common/js/lib/vault-chat/memory-vfs.js`; dev pack doc `05__vfs-persistence-memory.md` |
| **Twins of Gmail, OAuth or MCP** | **Not found as code.** Four June briefs on digital twins and world models: "we can make a digital twin out of anything, an organisation, an element, a mail system, an inbox, a person," and "an agent is a twin with permissions, capabilities, track record, and credibility as properties." An August brief for a **service twin**, a broker that "performs only the permitted operation using credentials held inside its own boundary, and returns a signed receipt," with a note that "twin already means something specific" and a rename to execution broker still open. Its market research covers MCP Guard, Arcade and Composio, which hold the connector credential for the agent. Nothing specific to a Gmail or OAuth twin. | `briefs/06/26/digital-twins-and-world-models/`; `briefs/08/19/briefs/v0.33.60__arch-brief__service-twin-...`; reality index `proposed/risk-mandate.md` P-415 to P-422 |
| **Selling credits** | Thought through more than once. June: "we are basically selling OpenRouter keys, we do a little markup on it, and all of this is client-side," with a read-only vault carrying a budgeted rotating key. June again: central key management issuing per-child credits to child vaults. July: "a key can be issued per user with a spend cap and OpenRouter meters and deducts against it," with three modes, routed, restricted-provider and browser-local model. And the sentence that explains why none of it shipped: "the missing piece is identical in every case: the purchase of the tokens, the page to sell from, and the users." No provider map exists anywhere in the project. | `briefs/06/13/.../v0.33.26__dev-brief__sg-send-selling-llm-usage-openrouter-keys-via-vaults...`; `briefs/06/07/v0.32.7__dev-brief__...central-key-management...`; `briefs/07/27/first-product-to-market/` |

Three consequences for the plan. Twin 1 is the memory file system with an inbox shape on it, so it is days, not a week. The service-twin brief and this brief want the same word for different things; this brief uses **twin** for a simulation and leaves **broker** for the thing that holds a credential and executes on the agent's behalf, which is the rename the August brief already proposed. And the credits question was never a technical one: the mechanism, a bounded key sealed in a vault, has been specified three times. What stopped it is the page to sell from and the legal position, which is exactly what the two sections below are about.

## Whose key: the four ways a model gets called

The sandbox is useless without a real model, and the site has no server, so every call is made from the browser. That leaves four ways to reach a model, and they are not alternatives: a shipped sandbox should support all four and say plainly what each one costs and who holds what.

| Mode | Who holds the key | What it costs the user | State |
|---|---|---|---|
| **Bring your own key** | The user, sealed in the vault's LLM config under a key derived from the vault's write key. A read-only session cannot open it; whoever holds the write key can. The shipping brief says so: "Sharing the vault key shares the ability to spend it." | Their own provider bill. A bounded key, with a spend limit, is the right thing to paste. | Works today through the bridge. |
| **Credits sold with the vault** | Us, or whoever we buy the credits from. A vault shipped with 5, 10 or 50 credits carries a provisioned key with that limit. The key is the credit. | The price of the vault. | Mechanically simple. Legally the open question, below. |
| **A gateway that holds the key** | The gateway. Cloudflare's AI Gateway stores provider keys and sells unified-billing credits at a five per cent fee; Vercel's AI Gateway sells credits at list price and takes stored keys on its paid tier; OpenRouter is itself a gateway with prepaid credits and per-key limits. | The gateway's fee, if any, on top of list price. | Integration work. May be the legal route for selling credits, because the gateway, not us, is the one reselling. |
| **A local model** | Nobody. Ollama, LM Studio, or a model running in the browser. | Hardware and patience. | Documented on llms.sgit.ai for Ollama; the in-browser case is untested. |

## Can we sell keys? What the terms actually say

This is a question for a lawyer, and the brief does not answer it. What it can do is put the clauses on the table so the lawyer's question is precise.

**OpenRouter.** Its [Terms of Service](https://openrouter.ai/terms) prohibit using the service "for purposes of reselling API access to Models or otherwise developing a competing service" (section 7, item 4) and prohibit any attempt to "sell or otherwise transfer the access granted under these Terms" (section 7, item 14). The same terms, in section 5, contemplate "your customers (to the extent you incorporate the Service into your own products and services)" and require that those customers use the models only within the agreement and the model terms. So the line OpenRouter draws is between *reselling access*, which is forbidden, and *a product that uses the service*, which is expected. That distinction is the whole question for us.

**Where the sandbox sits on that line.** A sandbox eval is a product: our prompts, our tools, our twins, a defined task, a scored result. A vault shipped with credits whose chat panel will send any prompt the user types to any model looks much more like access. The design choice that keeps the sandbox on the product side is to spend sold credits only inside the sandbox's own workflows, and to make the open chat panel bring-your-own-key only. That is a product decision with a legal consequence, and it should be made deliberately.

**The precedents.** Vercel sells AI Gateway credits and Cloudflare sells unified-billing credits, each with the provider's key held by them and never shown to the user. Both are, in plain terms, reselling model access, under whatever agreements they hold with the providers. Buying credits from a gateway that is permitted to resell, and spending them inside a product, is the cleanest version of the model the memo describes. It also moves the key out of the vault entirely, which answers the "whoever holds the vault key can read it" problem.

**The ask to each provider.** Not "may we resell your keys", which has a known answer, but: "we ship an encrypted vault that runs a defined evaluation workflow against a model; the vault carries a bounded credential with a small spend limit that we paid for; the user cannot extract the credential without the vault key and cannot use it outside the workflow; is that a product under your terms, or is it resale?" Ask it of OpenRouter, Anthropic, OpenAI, Google, Mistral, AWS, Azure, Cloudflare and Vercel, publish each answer as it arrives, and keep the page honest about who has not replied. That page is also, as the memo notes, the first time most of them will have seen a behaviour policy.

## The provider map: who can cap spending, and how hard the cap is

An agent needs cost control the way it needs every other barrier: enforced above its own reach. The map below is what the vendors' own pages say as of 2 October 2026. It belongs in the sandbox as a live table, because it is one of the things the sandbox tests.

| Provider | Hard spend cap? | How | Source |
|---|---|---|---|
| **OpenAI API** | **Yes** | Monthly spend limit at organisation or project level with "Enforce a hard limit"; requests return 429 after it. OpenAI says enforcement is not instantaneous and a small amount can leak past. | [Spend limits](https://developers.openai.com/api/docs/guides/spend-limits) |
| **Anthropic (Claude API)** | **Yes** | Organisation spend limits, and a monthly spend limit per workspace, set lower than the organisation's. API keys can be scoped to a workspace. Setting limits through the API is early access. | [Workspaces](https://platform.claude.com/docs/en/manage-claude/workspaces) |
| **OpenRouter** | **Yes, per key** | Prepaid credits, plus a credit limit and a daily, weekly or monthly reset on each API key. providers.sgit.ai has watched a $5 key stop at $4.79 with a 402. | [Limits](https://openrouter.ai/docs/api_reference/limits), [providers.sgit.ai](https://providers.sgit.ai/) |
| **Mistral** | **Yes** | Monthly spending limit at organisation and workspace level; access suspended until the next month or the limit is raised. No cap by default. | [Usage limits](https://docs.mistral.ai/admin/workspaces/usage-limits) |
| **Amazon Bedrock** | **No, not natively** | AWS Budgets alerts; it does not stop spending. A hard stop needs a Lambda that revokes inference access when the budget is exhausted, or an application gateway in front. | [AWS re:Post](https://repost.aws/articles/AR5rBgrAyQStqFOiBYu88PDg/governing-amazon-bedrock-costs-team-and-user-level-tracking-budgets-and-hard-spend-controls-for-claude-code) |
| **Azure OpenAI / Foundry** | **No** | Budgets and cost alerts only; Microsoft's own answer is that no direct spending limit exists independent of the subscription. | [Microsoft Q&A](https://learn.microsoft.com/en-us/answers/questions/5725505/can-azure-openai-enforce-a-hard-spending-limit-or) |
| **Google Cloud / Vertex AI** | **No, with a workaround** | Budgets do not cap usage. Spend caps exist for selected services and are not instantaneous. The documented hard stop is a Cloud Function that disables billing on the project. | [Disable billing with notifications](https://docs.cloud.google.com/billing/docs/how-to/disable-billing-with-notifications) |
| **Cloudflare AI Gateway** | **Prepaid** | Unified-billing credits, five per cent fee on purchase; stored provider keys; a setting to require provider credentials so the gateway never falls back to its own. | [Docs](https://developers.cloudflare.com/ai-gateway/) |
| **Vercel AI Gateway** | **Prepaid** | Credits at list price with no markup; bring-your-own-key on the paid tier. | [Pricing](https://vercel.com/docs/ai-gateway/pricing) |

The pattern is plain. The model vendors and the gateways cap; the clouds alert. An agent on Bedrock, Azure or Vertex with no gateway in front has no spend barrier above its reach, only an expectation. That is a row in the policy, and the sandbox should show it as one.

## The deployment model

The thing being sold is a vault. Three variants, in the order they should ship:

1. **The public sandbox**, a read-only vault with every eval, every twin and every published footprint, bring-your-own-key for anyone who wants to run it live. Free, and the demo.
2. **A sandbox with credits**, the same vault with a bounded credential sealed inside it, sold at a small fixed price, credits spent only inside the evals. Whether the credential is ours or a gateway's depends on the answers above.
3. **A customer's own sandbox**, seeded with their twins and their policies, run in their vault, with their key or their gateway. This is the RiskMandate product, and it is where the policy's licence to operate gets its evidence.

Two honest notes travel with all three. The key sealed in a vault is protected from the app and from a read-only session, not from a holder of the write key, and there is no arrangement of files that changes that; the only thing that does is a credential that is bounded, so that what the holder can spend is the credit and nothing more. And the bridge protects the key; it is not yet a boundary that stops an app calling a provider with a credential of its own. Both are stated in the __Send project's own documents and should be stated wherever the sandbox is sold.

## Build plan

1. **Twin 1, the inbox store**, as the Vault Chat memory file system with an inbox shape on it, a seed generator and the Email-FS message shape. Days.
2. **Twin 2, the OAuth connector**, as a tool set over twin 1 with the Gmail scopes enforced and the real error shapes. Start from the Connector Twin's replay code. A week.
3. **One eval, both ways.** The clear-the-backlog task, one model, the bridge, policy off then on, footprints side by side in the vault. This is the first thing to show anyone. Two weeks including the UX.
4. **Twin 3, the MCP connector**, with the prompts and the always-allow behaviour, and the harness comparison on top of it.
5. **The provider map as a live page**, the legality tracker, and the agent-written letters to each provider, sent from the comms vault and logged on the page.
6. **Credits**, once the legal answer is in: bounded keys sealed in sold vaults, or a gateway account behind them.

## Questions for the founders

1. **Sandbox, evals, twins?** The brief uses those three words. Say now if RiskMandate wants others, because they will be in every file name.
2. **Sold credits inside the evals only, or in the open chat too?** The first keeps the sandbox a product under the terms as read; the second is the better demo and the harder legal position.
3. **Which gateway to approach first** about carrying the credits, if any: Cloudflare, Vercel, OpenRouter, or one of the companies already spoken to.
4. **Who signs the letters to the providers.** The memo wants the agent to write them. The agent can, from the comms vault, under the byline the site already uses; the founder decides whether a person co-signs.

**House rules.** Every claim about a provider on this page links to the provider's own page and carries the date it was read. Terms change; the table says when it was last checked. Nothing here says the sandbox exists; it says which of its parts do.


---

*[Site index for agents](../../llms.txt) · [HTML version](https://sgit.ai/docs/briefs/riskmandate-sandbox-twins-and-tokens.html)*
