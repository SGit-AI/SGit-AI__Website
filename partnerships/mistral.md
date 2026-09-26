# A proposed partnership between sgit.ai and Mistral AI

> A European model, a European cloud, and vaults: a fully European AI stack in which no key leaves the customer. Mistral hosts data in the EU by default, supports MCP connectors in its Agents API and in Vibe (formerly Le Chat), and runs a partner programme with an integration tier. sgit provides the encrypted data layer, open source and runnable on any European cloud. Together they make a sovereignty story that holds at every layer.

*Source: <https://sgit.ai/partnerships/mistral.html> · site v0.6.10 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Partnerships](index.md) / [AI providers](ai-providers.md) / Mistral AI

A proposed partnership · sgit.ai with Mistral AI · public material only · 24 September 2026

# A proposed partnership between sgit.ai and Mistral AI

**A European model, a European cloud, and vaults: a fully European AI stack in which no key leaves the customer.** Mistral hosts data in the EU by default, supports MCP connectors in its Agents API and in Vibe (formerly Le Chat), and runs a partner programme with an integration tier. sgit provides the encrypted data layer, open source and runnable on any European cloud. Together they make a sovereignty story that holds at every layer.

**Nothing on this page is confidential, and there has been no conversation yet.** Every statement about Mistral AI comes from its own public pages, linked. Every statement about sgit points at the [deployment documentation](../deploy/index.md), a published vault or a page on this site. sgit is Apache-2.0, so Mistral AI does not need our permission to run it or to build on it. A partnership is about doing that well and together. The general argument is on [the AI providers page](ai-providers.md).

## In short

- **European by default.** Mistral [hosts data in the EU by default](https://help.mistral.ai/en/articles/347629-where-do-you-store-my-data-or-my-organization-s-data), with regional endpoints generally available since August 2026.
- **MCP in two places.** [Studio connectors are registered MCP servers](https://docs.mistral.ai/studio/connectors), and [Vibe supports custom MCP connectors](https://docs.mistral.ai/le-chat/knowledge-integrations/connectors/mcp-connectors) added by admins.
- **An integration tier.** The [Mistral partner programme](https://mistral.ai/partners/) has Strategic, Ecosystem and Integration partners.
- **What we would like:** an integration partnership, a vault connector for Vibe, and a joint European reference with one of [the European clouds](european-clouds.md).

## Where vaults fit Mistral's platform

| Meeting point | On Mistral AI's platform | Status |
|---|---|---|
| **Agents read and write vaults** | Agents API connectors (MCP), and custom MCP connectors in Vibe | Connector not built yet. |
| **Vault apps call models** | Mistral models, reached through the host bridge | Works today through OpenRouter. |
| **Vaults carry the work** | Agent output from the Agents API or Vibe | Pattern published here; no Mistral integration. |
| **Sovereign stack** | EU hosting by default, regional endpoints | Complementary: the data in the vault is encrypted on the device. |

## Where we are with Mistral AI today

We reach Mistral's models through OpenRouter and have no direct relationship. Mistral is on this list because it completes the argument made on [the UK Sovereign AI page](sovereign-ai.md) and [the European clouds page](european-clouds.md): sovereignty is only as strong as the layer that is not sovereign, and a European model with European, client-side-encrypted data leaves no such layer.

## What a partnership could be

| Shape | What it would be | On their side |
|---|---|---|
| **1 · A vault connector for Vibe** | A remote MCP server with read-only vault tools and one append tool, usable as a custom connector in Vibe and in the Agents API. | An integration partnership. |
| **2 · A European reference** | A published reference stack: Mistral models, a European cloud, and vaults, with every key held by the customer. | Joint publication. |
| **3 · Open models next to vaults** | Mistral's open-weight models running beside a vault server on a European cloud, for customers who want neither data nor prompts to leave. | Technical guidance. |

## What we are asking Mistral AI for

1. An integration partnership through the [Mistral partner programme](https://mistral.ai/partners/).
2. A technical contact for the connector and the reference stack.
3. A joint European reference, published on both sides.

## What this page does not claim

- **No endorsement.** Mistral AI has not endorsed sgit, and we have not spoken to anyone there about this. Product and programme descriptions quote Mistral AI's own pages and documentation as of 24 September 2026.
- **The vault connector does not exist yet.** This page describes what it would be and which rules it would have to meet.

## If you work at Mistral AI

This page is written to be forwarded as it is, and everything on it can be checked by the person who receives it. [Who is asking, and how to reach them →](../about/index.md)

[← Anthropic](anthropic.md)[Google Gemini →](google-gemini.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/partnerships/mistral.html)*
