# Article Views, five readers of one article, sgit.ai

> Five articles read again after they were written by five agents with roles: a Librarian's catalogue of every item with its sentence, a Cartographer's ontology at three altitudes and nine maps, a Historian's arc, an Explainer's two minutes and a Storyteller's decks. Published with its read key.

*Source: <https://sgit.ai/demos/vaults/article-views/index.html> · site v0.7.36 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../index.md) / Article Views

# Article Views: five readers of one article, run on five articles

The articles on this site are written once, as prose with their evidence attached. This vault is a simulation of what happens when five agents with defined roles read each one again afterwards: a Librarian that catalogues every fact, claim, number, question and source with the sentence it came from; a Cartographer and Ontologist that turns the catalogues into concepts and verbs at three altitudes and draws the maps; a Historian that says what the article added and where it sits; an Explainer that says it in two minutes; and a Storyteller that tells it as a deck. It was run on the five articles about agent behaviour policies published between 7 and 10 October 2026, and published with the article [One article, five readers](../../../articles/one-article-five-readers.md).

Five articles, five readers each, one app.

**Open it yourself. The key is the whole credential.**
 Read key: `sgit_public_read_19230bd5438497c7f73760c6eab2e5b57ab465834ccfaba585bf21cacafea68d:chtgtd9e`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_public_read_19230bd5438497c7f73760c6eab2e5b57ab465834ccfaba585bf21cacafea68d%3Achtgtd9e) · From the CLI: `sgit clone sgit_public_read_19230bd5438497c7f73760c6eab2e5b57ab465834ccfaba585bf21cacafea68d:chtgtd9e`
Published deliberately under the `sgit_public_read_` prefix, and **derived** one-way from a vault key kept in the gitignored tier and never published. Classified with `check_credential.py` before it touched this page, cloned back with the published key alone and compared with the source file by file, and checked with an all-zeros read key as the negative control. Created, pushed and audited with sgit-ai 0.20.0.

## See it live, here

The vault opens as an app: the five views of each article (two minutes, the arc, the deck, the map, the ontology, the catalogue), the arc across all five, which article carries which idea, all nine maps, and the five role files. You can also [**open it in the official UI**](https://dev.vault.sgraph.ai/#sgit_public_read_19230bd5438497c7f73760c6eab2e5b57ab465834ccfaba585bf21cacafea68d%3Achtgtd9e).

## The one idea

Keep writing the article first, because writing is how the argument is found, and extract everything else from it afterwards. Two readers build the platform: every item in the article anchored to its sentence, and every concept connected at the altitude of the article, the topic and the site. Three readers write for a person from that platform: short, and never adding a claim the article does not make.

## What is in it

librarian

### 662 items, every one anchored to its sentence

Five Librarians ran in parallel, one per article. Each item has a kind (fact, data point, claim, evidence, hypothesis, question, definition, method, decision, limitation, example, source, artefact, name), a one-line statement, its section, its index terms and its anchor, the exact sentence it came from. A script checked all 662 anchors against the articles. Cataloguing that closely also produced 32 flags for the authors: totals that do not add up, lists shorter than their count, claims the text does not support.

Search, filter by kind, and every item points home.

cartographer

### Three altitudes, one grammar, nine maps

13 classes and 24 verbs at the site altitude, each verb with its inverse; 45 concepts and 78 edges for the topic, every edge citing the catalogue items it rests on; and each article's own concepts mapped up as same-as, narrower-than or instance-of. Ideas named differently across articles are merged (expectation and hope; second reader and maker-checker) and the merges are explained. A feedback file sends the Librarian 13 merges, 8 splits and 6 changes of kind: the round trip.

Each map states the question it answers.

topic

### Which article carries which idea

Every topic concept against the five articles, amber where it first appears. Seventeen concepts run through three or more articles. New concepts per article fall 17, 11, 5, 11, 1: the newest article introduced one and reused 25.

The spine of the topic, and what each article brought.

historian

### What each article added, and the arc

For each article, under 400 words: what it introduced, the nugget quoted exactly, what it reused, what it changed, what it left open, and its contribution. Then the five as one story: the pattern none of them names, the tensions between them, and a lineage table that reaches back into earlier articles on the site.

"The rule moves out of the agent, and every article stops one barrier short."

explainer

### Two minutes, no jargon

For a smart reader who has never configured an agent: the point, one example from the article, why it matters, one thing to remember, and up to four words defined in a line each. Under 250 words, every number from the article.

The view that opens first.

storyteller

### Nine slides per article, and a PDF

Each deck is data: one idea per slide in one of nine layouts, a headline of at most nine words. A renderer draws them at 1080 by 1350, the shape of a LinkedIn document post, refuses to clip a slide with too many words, and writes a PDF. Every slide also carries a prompt for an image model, not yet run.

Swipe sideways; click to enlarge.

ontology

### What an article brought, concept by concept

For each article: the concepts it introduced to the topic, the ones it reused and where each was first seen, and its own concepts with the topic concept each maps to.

One new concept, 25 reused.

## How it is built

The five articles and their graphs are in `sources/` exactly as they were read. Each reader's role is a file in `roles/` with its mission, its failure sentence, what it must never do, its output format and its starting prompt; each agent was given one role file and its inputs. `tools/check.py` runs before every commit: every anchor verbatim, every cited item and concept exists, every verb is declared, word limits, quotes on slides verbatim, no em-dash and none of the site's retired words. `tools/render_maps.mjs` renders the Mermaid maps offline; `tools/render_deck.mjs` draws the decks; `tools/build_app.py` gathers everything into `app/data.json` and inlines it into the app, so the page also works opened on its own.

## The audit, honestly

**What was scanned.** Every file before the first commit for credential shapes (vault keys, every `sgit_` credential prefix, private-key headers, the SG/Send access token), and again after cloning with the published read key alone. The clone matched the source, file by file.

**What was found.** Nothing. The negative control, an all-zeros read key against the same vault id, returned nothing.

**What it does not claim.** The views were produced by agents and checked by script where a script can check them; a summary that is subtly unfair to its article passes every check, so each was read before publication. The Librarian checks each article against itself, not against the world. "New" concepts are new to these five articles, not to the site. The Cartographer's feedback to the Librarian is written and not yet applied. The 32 flags are open: the articles have not been corrected in this release.

**Write-key status:** escrowed, in the gitignored credential tier, before this page was written.

## Derived facts

From `admin/build/catalogue_derive.py chtgtd9e <read key hex>`, read-only, no token, no clone.

- **Files:** 143 · **plaintext size:** 9608 KB
- **Commits:** 2 · **last updated:** 2026-10-10 · **HEAD:** `obj-cas-imm-e72e985c5b14`
- **Top level:** `README.md`, `app.json`, `app/`, `cartographer/`, `explainer/`, `historian/`, `index.html`, `librarian/`, `roles/`, `sources/`, `storyteller/`, `tools/`
- **File types:** .webp ×54, .md ×26, .json ×26, .mmd ×9, .png ×9, .svg ×9, .pdf ×5, .py ×2, .mjs ×2, .html ×1
- **Vault app:** yes, entry `index.html` · **browser-renderable:** yes

## Notes

**Where this came from.** A voice memo by Dinis Cruz asking for multiple views of the same article; the roles of the [SG/Send agent team](https://github.com/the-cyber-boardroom/SGraph-AI__App__Send/tree/HEAD/team/roles); the argument in [Liquid content needs water](../../../articles/liquid-content-needs-water.md); and the method in [Fractal Semantic Graphs](../../../articles/introducing-fractal-semantic-graphs.md). The five articles read: [The behaviour policy is the business logic](../../../articles/the-behaviour-policy-is-the-business-logic.md), [Every mistake added a rule](../../../articles/every-mistake-added-a-rule.md), [Hope or enforcement](../../../articles/hope-or-enforcement.md), [A second reader the agent cannot skip](../../../articles/a-second-reader-the-agent-cannot-skip.md) and [Re-anchoring](../../../articles/re-anchoring-agent-behaviour-policies.md).

**Who wrote this.** [agent@riskmandate.ai](mailto:agent@riskmandate.ai) (Claude Opus 5.5, `claude-opus-5-5`), in the sgit.ai site session, with Claude agents for each reader. AI-generated text, disclosed as Article 50 of the EU AI Act asks; the person with editorial responsibility is Dinis Cruz.

[← All published vaults](../index.md)


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/article-views/index.html)*
