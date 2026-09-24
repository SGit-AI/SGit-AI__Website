# A proposed partnership between sgit.ai and Google Gemini

> The quickest listing on this page is one we can do ourselves. Gemini CLI supports MCP servers, and Gemini CLI extensions are listed automatically when a public repository carries the right topic and manifest. For the enterprise side, partner agents listed on Google Cloud Marketplace appear in the Gemini Enterprise Agent Gallery. We would like to do both properly, with Google, so that agent work done with Gemini can land in a vault.

*Source: <https://sgit.ai/partnerships/google-gemini.html> · site v0.6.5 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Partnerships](index.md) / [AI providers](ai-providers.md) / Google Gemini

A proposed partnership · sgit.ai with Google Gemini · public material only · 24 September 2026

# A proposed partnership between sgit.ai and Google Gemini

**The quickest listing on this page is one we can do ourselves.** Gemini CLI supports MCP servers, and Gemini CLI extensions are listed automatically when a public repository carries the right topic and manifest. For the enterprise side, partner agents listed on Google Cloud Marketplace appear in the Gemini Enterprise Agent Gallery. We would like to do both properly, with Google, so that agent work done with Gemini can land in a vault.

**Nothing on this page is confidential, and there has been no conversation yet.** Every statement about Google Gemini comes from its own public pages, linked. Every statement about sgit points at the [deployment documentation](../deploy/index.md), a published vault or a page on this site. sgit is Apache-2.0, so Google Gemini does not need our permission to run it or to build on it. A partnership is about doing that well and together. The general argument is on [the AI providers page](ai-providers.md).

## In short

- **A self-service first step.** [Gemini CLI extensions](https://geminicli.com/docs/extensions/releasing/) are listed from a public GitHub repository with the `gemini-cli-extension` topic and a manifest, and can bundle an MCP server.
- **An enterprise route.** [Partner agents on Google Cloud Marketplace](https://docs.cloud.google.com/gemini/enterprise/docs/agent-gallery) appear in the Gemini Enterprise Agent Gallery.
- **Google already runs MCP servers.** Google [offers managed remote MCP servers](https://cloud.google.com/blog/products/ai-machine-learning/announcing-official-mcp-support-for-google-services) for its own services.
- **What we would like:** a review of the extension, and a route to the Agent Gallery through [the Google Cloud partnership](google-cloud.md).

## Where vaults fit Gemini

| Meeting point | On Google Gemini's platform | Status |
|---|---|---|
| **Agents read and write vaults** | Gemini CLI MCP servers and extensions; the Agent Gallery for enterprise agents | Neither built yet. The extension is the first step and needs no permission. |
| **Vault apps call models** | Gemini models, reached through the host bridge | Works today through OpenRouter. |
| **Vaults carry the work** | Gemini CLI and Gemini Enterprise agent output | Pattern published here; no Google integration. |
| **Data controls** | [Paid Gemini API use is not used to improve products](https://ai.google.dev/gemini-api/terms_preview) | Complementary. |

## Where we are with Google Gemini today

We reach Gemini models through OpenRouter and have no relationship with Google on the model side. The infrastructure side is on [the Google Cloud page](google-cloud.md).

## What a partnership could be

| Shape | What it would be | On their side |
|---|---|---|
| **1 · A Gemini CLI extension** | A public extension bundling a vault MCP server and context on how to commit and hand over work as a vault. | Self-service listing; a review would help. |
| **2 · An agent in the Agent Gallery** | A vault agent listed on Google Cloud Marketplace and shown in the Gemini Enterprise Agent Gallery. | Partner Advantage and Marketplace. |
| **3 · Startup support** | Credits for testing on Gemini and Google Cloud together. | [Google for Startups Cloud Program](https://cloud.google.com/startup). |

## What we are asking Google Gemini for

1. A review of the Gemini CLI extension once it is published.
2. An introduction to the Gemini Enterprise Agent Gallery team.
3. Support through the [Google for Startups Cloud Program](https://cloud.google.com/startup).

## What this page does not claim

- **No endorsement.** Google Gemini has not endorsed sgit, and we have not spoken to anyone there about this. Product and programme descriptions quote Google Gemini's own pages and documentation as of 24 September 2026.
- **The vault connector does not exist yet.** This page describes what it would be and which rules it would have to meet.

## If you work at Google Gemini

This page is written to be forwarded as it is, and everything on it can be checked by the person who receives it. [Who is asking, and how to reach them →](../about/index.md)

[← Mistral AI](mistral.md)[OpenRouter →](openrouter.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/partnerships/google-gemini.html)*
