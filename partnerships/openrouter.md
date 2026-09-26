# A proposed partnership between sgit.ai and OpenRouter

> OpenRouter is how the vault apps on this site reach models, and it has the credential the pattern needs. A vault app calls a model through the host, and the key never reaches the page. The safest credential for that is one that is bounded: a spend limit and a reset. The independent provider report on this site records OpenRouter as "the one provider in this family that can do pattern one". We would like to make that a documented, supported pattern together.

*Source: <https://sgit.ai/partnerships/openrouter.html> · site v0.6.10 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Partnerships](index.md) / [AI providers](ai-providers.md) / OpenRouter

A proposed partnership · sgit.ai with OpenRouter · public material only · 24 September 2026

# A proposed partnership between sgit.ai and OpenRouter

**OpenRouter is how the vault apps on this site reach models, and it has the credential the pattern needs.** A vault app calls a model through the host, and the key never reaches the page. The safest credential for that is one that is bounded: a spend limit and a reset. The independent provider report on this site records OpenRouter as "the one provider in this family that can do pattern one". We would like to make that a documented, supported pattern together.

**Nothing on this page is confidential, and there has been no conversation yet.** Every statement about OpenRouter comes from its own public pages, linked. Every statement about sgit points at the [deployment documentation](../deploy/index.md), a published vault or a page on this site. sgit is Apache-2.0, so OpenRouter does not need our permission to run it or to build on it. A partnership is about doing that well and together. The general argument is on [the AI providers page](ai-providers.md).

## In short

- **We already use it.** Vault apps here reach models through OpenRouter, with the key held by the host and sealed under the vault key.
- **It has the right credential.** [providers.sgit.ai](https://providers.sgit.ai/) names OpenRouter's provisioned keys, with a spend limit and a reset, as the credential pattern vault apps need.
- **It has the right data controls.** [Provider routing](https://openrouter.ai/docs/guides/routing/provider-selection) can require `zdr: true` or `data_collection: "deny"` per request, which a vault app handling sensitive content should set.
- **What we would like:** a review of the bounded-key pattern, a listing among the apps that work with OpenRouter, and help with the independent OpenRouter report.

## Where vaults fit OpenRouter

| Meeting point | On OpenRouter's platform | Status |
|---|---|---|
| **Vault apps call models** | One API across providers, with the key held by the host | Works today. |
| **Bounded credentials** | Provisioned keys with a spend limit and a reset | The pattern the report recommends; the OpenRouter report itself is not built yet. |
| **Data controls per call** | Routing flags for zero data retention and no data collection | To adopt in the bridge. |
| **Attribution** | [App attribution through request headers](https://openrouter.ai/docs/app-attribution) | To adopt, so vault apps appear in OpenRouter's app listings. |

## Where we are with OpenRouter today

OpenRouter is the model provider this site depends on most. It is also the one the independent report family singles out, because its keys can be bounded. The report on OpenRouter is marked "not built yet" on providers.sgit.ai, and writing it is the natural first piece of shared work.

## What a partnership could be

| Shape | What it would be | On their side |
|---|---|---|
| **1 · The bounded-key pattern** | A documented pattern for vault apps: a provisioned key per vault or per app, with a spend limit and a reset, held by the host. | A technical review. |
| **2 · Listed as working with OpenRouter** | sgit's bridge listed through [Works with OpenRouter](https://openrouter.ai/works-with-openrouter), which takes a pull request to its list. | Self-service, with a review. |
| **3 · The independent report** | openrouter.providers.sgit.ai: what it cost on a named workload, what broke, which credential patterns it supports. | Fact-checking of the draft. |

## What we are asking OpenRouter for

1. A review of the bounded-key pattern for vault apps.
2. A fact-check of the OpenRouter report before it is published.
3. A conversation about featured partnerships.

## What this page does not claim

- **No endorsement.** OpenRouter has not endorsed sgit, and we have not spoken to anyone there about this. Product and programme descriptions quote OpenRouter's own pages and documentation as of 24 September 2026.
- **Heavy use is not a relationship.** We are a paying user, not a partner.

## If you work at OpenRouter

This page is written to be forwarded as it is, and everything on it can be checked by the person who receives it. [Who is asking, and how to reach them →](../about/index.md)

[← Google Gemini](google-gemini.md)[ElevenLabs →](elevenlabs.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/partnerships/openrouter.html)*
