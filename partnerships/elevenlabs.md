# A proposed partnership between sgit.ai and ElevenLabs

> We already publish an independent report on ElevenLabs, and it ends with one clear ask. The narration on this site is rendered with ElevenLabs, and elevenlabs.providers.sgit.ai records what it cost on a named workload, what broke, and which credential patterns the product supports. What would let a vault app use ElevenLabs safely, with no key in the page, is a key with a spend limit, or a short-lived token for text to speech.

*Source: <https://sgit.ai/partnerships/elevenlabs.html> · site v0.6.10 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Partnerships](index.md) / [AI providers](ai-providers.md) / ElevenLabs

A proposed partnership · sgit.ai with ElevenLabs · public material only · 24 September 2026

# A proposed partnership between sgit.ai and ElevenLabs

**We already publish an independent report on ElevenLabs, and it ends with one clear ask.** The narration on this site is rendered with ElevenLabs, and [elevenlabs.providers.sgit.ai](https://elevenlabs.providers.sgit.ai/) records what it cost on a named workload, what broke, and which credential patterns the product supports. What would let a vault app use ElevenLabs safely, with no key in the page, is a key with a spend limit, or a short-lived token for text to speech.

**Nothing on this page is confidential, and there has been no conversation yet.** Every statement about ElevenLabs comes from its own public pages, linked. Every statement about sgit points at the [deployment documentation](../deploy/index.md), a published vault or a page on this site. sgit is Apache-2.0, so ElevenLabs does not need our permission to run it or to build on it. A partnership is about doing that well and together. The general argument is on [the AI providers page](ai-providers.md).

## In short

- **We use it and measured it.** The first production video cost $0.18 at list price for 1,821 characters across nine scenes, recorded on 8 September 2026.
- **Four things broke on the first run, and we wrote them down.** PCM output is gated to the Pro tier, stitching is not supported on v3, a scoped key lacked one permission, and one problem was ours: an encoder that added fourteen seconds of silence.
- **One credential feature is missing.** Keys are scoped but carry no per-key spend limit, and text to speech has no vendor-issued short-lived token, so a vault app cannot yet hold an ElevenLabs credential safely.
- **What we would like:** per-key spend limits or short-lived TTS tokens, and a conversation about vault agents that speak.

## Where vaults fit ElevenLabs

| Meeting point | On ElevenLabs's platform | Status |
|---|---|---|
| **Narrated vault content** | Text to speech with character-level timestamps | Works today from a render script. Not yet from inside a vault app, for the reason in the next row. |
| **Voice agents over vaults** | [ElevenAgents connected to external MCP servers](https://elevenlabs.io/docs/eleven-agents/customization/tools/mcp) | Connector not built yet. |
| **A safe credential in a vault app** | A per-key spend limit, or a short-lived token for TTS | Missing. The report's main finding. |
| **Voices** | [The Voice Library](https://elevenlabs.io/docs/eleven-creative/voices/voice-library) | Not used by us. |

## Where we are with ElevenLabs today

ElevenLabs is part of how this site makes its explainers, and it is the first provider to get a full independent report here. The report makes no demands. It records what happened and names which of four credential patterns the product can support, and the gap it finds is specific enough to be a feature request.

## What a partnership could be

| Shape | What it would be | On their side |
|---|---|---|
| **1 · A bounded credential** | A per-key spend limit, or a short-lived token for text to speech, so a vault app can narrate without a long-lived key anywhere near the page. | A product conversation. |
| **2 · Vault agents that speak** | An ElevenAgents agent reading a vault through a connector: a briefing, a board pack or a report, read aloud to the person it was handed to. | A technical contact. |
| **3 · Startup support** | Characters to render the rest of the site's explainers. | [ElevenLabs Startup Grants](https://elevenlabs.io/startup-grants). |

## What we are asking ElevenLabs for

1. Per-key spend limits, or short-lived tokens for text to speech.
2. A fact-check of the independent report.
3. A conversation about [ElevenLabs Startup Grants](https://elevenlabs.io/startup-grants) and about vault agents that speak.

## What this page does not claim

- **No endorsement.** ElevenLabs has not endorsed sgit, and we have not spoken to anyone there about this. Product and programme descriptions quote ElevenLabs's own pages and documentation as of 24 September 2026.
- **The report is independent.** ElevenLabs did not commission or review it.

## If you work at ElevenLabs

This page is written to be forwarded as it is, and everything on it can be checked by the person who receives it. [Who is asking, and how to reach them →](../about/index.md)

[← OpenRouter](openrouter.md)[AI providers →](ai-providers.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/partnerships/elevenlabs.html)*
