# Demos, sgit.ai

> Live end-to-end demonstrations: vaults actually created, pushed, and embedded in the pages that document them, each with a deliberately published read-only key.

*Source: <https://sgit.ai/demos/index.html> · site v0.6.2 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / Demos

# Demos

Live, end-to-end demonstrations, each one a vault that was actually created, pushed, and embedded in the page that documents it. The walkthroughs are complete: every command, the keys that are deliberately public, and the ones that never will be.

**The rule every demo follows:** the vault's *read key* is published on purpose. It is derived one-way and cannot write, so publishing it is what makes the demo openable by anyone. The vault's *write key* appears nowhere: not in these pages, not in the repos, and the build refuses to push if one ever reaches a tracked file.

## Thirty vaults, one page each

The demos outgrew this page. Every vault whose read key this site publishes now has its own page under [**Published vaults**](vaults/index.md), what it does, which features it uses, the audit that ran before the key was published, and the vault itself running live in the page. Thirty at the last count, from a regulation parsed into a graph to a job application delivered as a vault, and the table there is generated from the same file as [the machine-readable list](vaults/llms.txt), so the two cannot drift.

[Gallery · 30 vaults### Published vaultsEvery vault with a deliberately published read key, one page per vault, the vault running live in it. Graphs, presentations, briefing packs, records, applications.Open the gallery →](vaults/index.md)

[Method### How a vault gets published hereThe seven steps behind every row: classify the credential, derive rather than refuse, audit with the read key, screenshot the real app, write the page, publish the key, verify with a negative control.Read the method →](vaults/publishing.md)

[Concept · 8 vaults### Fractal Semantic GraphsEvery node opens into a graph with its own ontology, down to the word; only the grammar is shared. What that means, why it is worth connecting everything with everything, and then how far down it goes: the law, the standard, the evidence, the risk, the owner, the policy, and a threat in one line of code, each a live graph in a published vault, with the pictures and the counts.Walk the ladder →](fractal-graphs/index.md)

[Index · live from a vault### The catalogueAn index of vaults that is itself a vault, rendered live on this site with a published read key. The machine-first companion to the gallery.Open the catalogue →](../catalogue/index.md)

## The three walkthroughs

These were the first demos, and they are still the pages to read if you want to see *how* a vault ends up inside a page, the sandboxed iframe, the postMessage bridge, the republish pattern when an original vault cannot publish its key, and two apps served from one store.

[Walkthrough · live### A vault app, live inside this pageField Notes: a self-contained vault app created from scratch, pushed, and opened inside sgit.ai with a published read key, sandboxed iframe, postMessage bridge, every byte decrypted in your browser.Open the walkthrough →](vault-app-embed.md)

[Report · real### The Strategy in Seven MapsNot demo content: the actual SG/Send strategy, published on LinkedIn in May 2026, served live from a vault with a published read key, plus the audit that shows why the original vault could not publish its key, and the republish pattern that fixed it.Open the walkthrough →](strategy-maps.md)

[Analysis · live### sgit, on a Wardley MapSix maps of sgit's own positioning (where git wins, where the boundary falls, the agent as the new user) drawn as inline SVG and served as a **second app from the same vault** as the strategy essay: one store, two entry points, one read key.Open the analysis →](sgit-maps.md)

## Reading a vault from a site, without the vault supplying the viewer

The newer pattern, used by the deck and document pages under the gallery, is the reverse of the embed: the site owns the viewer, the vault supplies only data, and the two meet in an iframe with no origin. It is written up for other sites' agents in [the deck brief](../docs/briefs/vault-decks-on-a-site.md), [the markdown and file-viewer brief](../docs/briefs/markdown-and-file-viewers.md), and [reading a single file out of a vault](../docs/vault/reading-a-vault-file.md).

[← Home](../index.md)[Published vaults →](vaults/index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/demos/index.html)*
