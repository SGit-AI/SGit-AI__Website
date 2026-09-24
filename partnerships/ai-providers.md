# Models do the work, vaults hold it: proposed partnerships with the AI providers, sgit.ai

> Three places where a model provider meets a vault (agents read and write vaults through a connector, vault apps call models without holding a key, vaults carry the agent's work to a person), what we already do with these providers, what we ask of each, and one page per provider: OpenAI, Anthropic, Mistral AI, Google Gemini, OpenRouter and ElevenLabs.

*Source: <https://sgit.ai/partnerships/ai-providers.html> · site v0.6.6 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Partnerships](index.md) / AI providers

Proposed partnerships · sgit.ai with the model and voice providers · public material only · 24 September 2026

# Models do the work. Vaults hold it. We would like to work with the people who make the models.

**An invitation from our side, published in the open.** Almost everything on this site was made with AI: the site itself, the thirty-five published vaults, the diagrams, the narration. The models came from the providers on this page, mostly reached through OpenRouter. What we have built in return is a place for that work to live: encrypted, versioned, openable in a browser with a key, and callable by a model without anyone leaking an API key. We use these providers every day and have no relationship with any of them. This page, and the page for each provider linked from it, sets out where vaults and models meet and what a partnership could be.

**Nothing on these pages is confidential, and there has been no conversation yet.** Every statement about a provider comes from its own public pages or documentation, linked. Every statement about sgit points at a published vault or a page on this site. sgit is Apache-2.0, so any provider can build on it without asking. A partnership is about building the connection properly, and being listed where the provider's users look for it.

## In short

- **Agents need somewhere to put their work.** An agent that writes a report, a site, a test or a plan produces something a person has to receive, check and keep. A vault carries the result, its history and its app as one read key.
- **Documents need to call models without leaking keys.** A vault app can call a language model through the host, holding no key of its own. [llms.sgit.ai](https://llms.sgit.ai/) documents how, including the traps.
- **Agents need to read and write encrypted data safely.** Read with a read key, and write only through a write-only [append lane](../api/append-lanes.md). That is the shape of a connector that can be switched on without handing an agent the keys to everything.
- **Every provider now has a directory.** OpenAI's Plugins directory, Anthropic's Connectors Directory, Mistral's connectors in Vibe, Gemini CLI extensions, OpenRouter's app listings, the ElevenLabs Voice Library. A vault connector belongs in the ones that fit.
- **We have already done independent work on some of them.** [providers.sgit.ai](https://providers.sgit.ai/) reports what a provider cost on a named workload, what broke, and where the key has to live. The ElevenLabs report is published, and the OpenRouter report is next.

## Where a provider meets a vault

Three places where a model provider and a vault meet. The provider holds the model; the customer holds the keys to the data.

| Meeting point | What exists today | What a partnership would add |
|---|---|---|
| **1 · Agents read and write vaults** | The vault API, read keys, and write-only append lanes, all documented. Agents already work in vaults through the CLI. | A vault connector, as a remote MCP server, built to each directory's rules and listed there. It does not exist yet, and it is the first piece of work. |
| **2 · Vault apps call models** | The `sg.llm` bridge: the host makes the call on the app's behalf, so no key sits in the page. [Risk Mandate](../demos/vaults/risk-mandate/index.md) calls an LLM this way. | Credentials made for this pattern, such as keys with a spend limit and an expiry, and first-class support in each provider's documentation. |
| **3 · Vaults carry the agent's work** | This site, most of its vaults, and the [penetration test delivered as a vault](../demos/vaults/pentest-report/index.md) are agent work handed over this way. | A "deliver as a vault" option inside the provider's own agent products. |

## What we already do with these providers

- **This site is built and published by Claude Code sessions** that share state through a vault. So are the deployment docs, the briefs and most of the vaults.
- **Vault apps reach models through OpenRouter.** The key is held by the host, sealed under the vault key, and never reaches the page.
- **Narration is rendered with ElevenLabs**, and [the independent report](https://elevenlabs.providers.sgit.ai/) records what it cost, what broke and which credential patterns the product supports.
- **Agent behaviour policies for several of these products are already published** at [RiskMandate.ai](https://riskmandate.ai/agent-behaviour-policy.html): what an agent can reach in Claude Code, ChatGPT on the web, Claude with Gmail, and more. The risk side of these partnerships will be written there.

## The pages, one per provider

| Provider | Why them | The page |
|---|---|---|
| **OpenAI** | ChatGPT and Codex list MCP-based plugins in a shared directory, and the Responses API can call a remote MCP server directly. | [**The OpenAI page →**](openai.md) |
| **Anthropic** | This site is built by Claude Code sessions sharing state through a vault. Claude reaches remote MCP servers and lists them in the Connectors Directory. | [**The Anthropic page →**](anthropic.md) |
| **Mistral AI** | A European model provider with EU hosting by default and MCP connectors in Vibe and the Agents API. With a European cloud and vaults, a fully European stack. | [**The Mistral AI page →**](mistral.md) |
| **Google Gemini** | Gemini CLI lists extensions automatically from public repositories, and partner agents on Cloud Marketplace reach the Gemini Enterprise Agent Gallery. | [**The Google Gemini page →**](google-gemini.md) |
| **OpenRouter** | The provider we use most. Its keys can carry a spend limit and a reset, the one credential pattern vault apps most need. | [**The OpenRouter page →**](openrouter.md) |
| **ElevenLabs** | We render narration with ElevenLabs and have published an independent report on it. One missing credential feature would make it safe inside vault apps. | [**The ElevenLabs page →**](elevenlabs.md) |

## What we ask of every provider

1. **A review of the vault connector** against your directory's rules, before we submit it.
2. **A credential that fits a vault app**: a key with a spend limit, an expiry, or both, or a short-lived token the host can mint.
3. **Credits or access** through your startup programme, so the integrations are tested rather than described.
4. **A technical contact** for the questions documentation does not answer.
5. **A shared example**: one piece of agent work in your product, delivered as a vault, published on both sides.

## What these pages do not claim

- **No provider has endorsed sgit**, and we have not spoken to any of them about this.
- **The vault connector does not exist yet.** The pages describe what it would be and which directory rules it would meet.
- **Product names change quickly.** Le Chat became Vibe on 12 August 2026, and OpenAI's app directory is now its Plugins directory. The pages use the names on the providers' own pages as of 24 September 2026.
- **Risk is out of scope here.** How the choice between providers, or between an API and a consumer chat product, changes an agent's behaviour policy belongs to RiskMandate.ai, and a brief for that work is published in [the briefs](../docs/briefs/index.md).

## If you work at one of these providers

These pages are written to be forwarded as they are. [Who is asking, and how to reach them →](../about/index.md) The same argument, from the infrastructure side, is on [the cloud platforms page](cloud-platforms.md).

[← Cloud platforms](cloud-platforms.md)[Partnerships →](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/partnerships/ai-providers.html)*
