# A proposed partnership between sgit.ai and OpenAI

> We would like vaults to be where ChatGPT and Codex put work that has to be handed over. OpenAI's agents already produce reports, code and analyses that someone else has to receive, check and keep. A vault carries that result, its history and its app as one read key. OpenAI's platform now reaches remote MCP servers from the Responses API and lists MCP-based plugins in a directory shared by ChatGPT and Codex, which is exactly where a vault connector would live.

*Source: <https://sgit.ai/partnerships/openai.html> · site v0.6.8 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Partnerships](index.md) / [AI providers](ai-providers.md) / OpenAI

A proposed partnership · sgit.ai with OpenAI · public material only · 24 September 2026

# A proposed partnership between sgit.ai and OpenAI

**We would like vaults to be where ChatGPT and Codex put work that has to be handed over.** OpenAI's agents already produce reports, code and analyses that someone else has to receive, check and keep. A vault carries that result, its history and its app as one read key. OpenAI's platform now reaches remote MCP servers from the Responses API and lists MCP-based plugins in a directory shared by ChatGPT and Codex, which is exactly where a vault connector would live.

**Nothing on this page is confidential, and there has been no conversation yet.** Every statement about OpenAI comes from its own public pages, linked. Every statement about sgit points at the [deployment documentation](../deploy/index.md), a published vault or a page on this site. sgit is Apache-2.0, so OpenAI does not need our permission to run it or to build on it. A partnership is about doing that well and together. The general argument is on [the AI providers page](ai-providers.md).

## In short

- **A vault connector fits OpenAI's rules.** The [Responses API's MCP tool](https://developers.openai.com/api/docs/guides/tools-connectors-mcp) calls remote MCP servers and asks for approval before sharing data by default.
- **The directory is the channel.** OpenAI's [Plugins directory](https://developers.openai.com/plugins/deploy/submission), shared by ChatGPT and Codex, takes submissions with domain verification and tool annotations such as `readOnlyHint` and `destructiveHint`.
- **Vault tools map cleanly onto those annotations.** Reading a vault with a read key is read-only. Appending to a lane writes but cannot overwrite or delete. Nothing in a vault connector needs to be destructive.
- **What we would like:** a review of the connector before submission, API credits to test it, and a shared example of agent work delivered as a vault.

## Where vaults fit OpenAI's platform

| Meeting point | On OpenAI's platform | Status |
|---|---|---|
| **Agents read and write vaults** | Remote MCP servers in the Responses API, and plugins in ChatGPT and Codex | Connector not built yet. |
| **Vault apps call models** | OpenAI models, reached through the host bridge | Works today through OpenRouter, with the key held by the host. |
| **Vaults carry the work** | Codex and ChatGPT agent output | Pattern published here; no OpenAI integration. |
| **Data controls** | [API data not used for training unless opted in; data residency in Europe and elsewhere](https://developers.openai.com/api/docs/guides/your-data) | Complementary: what is in the vault stays encrypted either way. |

## Where we are with OpenAI today

We use OpenAI models through OpenRouter, from vault apps, with the key held by the host rather than the page. We have no direct relationship with OpenAI and no connector in its directory. The risk side, how an agent's behaviour policy differs between ChatGPT on the web and the API, is published separately: RiskMandate.ai already has [a behaviour policy for ChatGPT on the web](https://riskmandate.ai/agent-behaviour-policy.html).

## What a partnership could be

| Shape | What it would be | On their side |
|---|---|---|
| **1 · A vault connector** | A remote MCP server with read-only vault tools and one append tool, annotated to the directory's rules, submitted to the Plugins directory. | Directory review. |
| **2 · Deliver as a vault** | A Codex or ChatGPT agent task that ends with its output committed to a vault and a read key returned to the user. | A shared example, published on both sides. |
| **3 · Startup support** | API credits to test the connector and the bridge properly. | [OpenAI for Startups](https://openai.com/startups/). |

## What we are asking OpenAI for

1. A review of the vault connector against the Plugins directory rules before we submit it.
2. API credits through [OpenAI for Startups](https://openai.com/startups/).
3. A technical contact on the Apps SDK and MCP side.
4. One shared example: Codex work delivered as a vault.

## What this page does not claim

- **No endorsement.** OpenAI has not endorsed sgit, and we have not spoken to anyone there about this. Product and programme descriptions quote OpenAI's own pages and documentation as of 24 September 2026.
- **The vault connector does not exist yet.** This page describes what it would be and which rules it would have to meet.

## If you work at OpenAI

This page is written to be forwarded as it is, and everything on it can be checked by the person who receives it. [Who is asking, and how to reach them →](../about/index.md)

[← AI providers](ai-providers.md)[Anthropic →](anthropic.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/partnerships/openai.html)*
