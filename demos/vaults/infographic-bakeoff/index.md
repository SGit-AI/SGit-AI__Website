# Infographic bake-off, every image model judged blind, sgit.ai

> Every image model on OpenRouter on 10 October 2026, given the same briefs from one article, from 18 words to the whole article, plus an edit, a component, a brand slide and a deck. Five rounds, 101 images judged blind, $10.44, and guidance on which model for which job. Published with its read key.

*Source: <https://sgit.ai/demos/vaults/infographic-bakeoff/index.html> · site v0.7.32 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../index.md) / Infographic bake-off

# Infographic bake-off: every image model on OpenRouter, judged blind, 10 October 2026

Which image model should the newsroom use for an infographic, for which job, and at what cost? Every image-output model on OpenRouter on the day, its auto-router and our own code-drawn renderer as a control were given the same briefs from one article: an 18-word stat card, a concept slide, a diagram with exact labels, a chart with fourteen numbers, a 240-word document, the whole 2,800-word article, an edit of their own image, a UI component, a brand slide, a three-slide deck, and finally the conclusion of the bake-off itself. Five rounds, models cut after each. 101 images, every one judged blind by a Designer agent, every cent recorded by OpenRouter: **$10.44**. It was published with the article [The infographic bake-off](../../../articles/the-infographic-bake-off.md).

101 images, five rounds, blind scores, every cost.

**Open it yourself. The key is the whole credential.**
 Read key: `sgit_public_read_89ef38c8db580a5c858ae1889859f30792b2a16fdf370d58a8cd8e58000cc6be:po5i477i`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_public_read_89ef38c8db580a5c858ae1889859f30792b2a16fdf370d58a8cd8e58000cc6be%3Apo5i477i) · From the CLI: `sgit clone sgit_public_read_89ef38c8db580a5c858ae1889859f30792b2a16fdf370d58a8cd8e58000cc6be:po5i477i`
Published deliberately under the `sgit_public_read_` prefix, and **derived** one-way from a vault key kept in the gitignored tier and never published. Classified with `check_credential.py` before it touched this page, cloned back with the published key alone and compared with the source file by file, and checked with an all-zeros read key as the negative control. Created, pushed and audited with sgit-ai 0.20.0. The OpenRouter key the run used was read from a file outside the vault and appears nowhere in it.

## See it live, here

The vault opens as an app: the overview, each round with every image, its cost, time, fact check and the judge's reason, a page per model, the guidance, the ledger of every generation, and the method and roles. You can also [**open it in the official UI**](https://dev.vault.sgraph.ai/#sgit_public_read_89ef38c8db580a5c858ae1889859f30792b2a16fdf370d58a8cd8e58000cc6be%3Apo5i477i).

## The one idea

Choose the model by the job, not by the budget. A cheap model at four cents an image makes concept slides, charts and consistent decks as well as models four times its price, and fails every brief where each character is specified. The most expensive model is the only one that turns a whole document into a correct infographic and the only one that edits an image without breaking something else. The middle one is the fast all-rounder.

## What is in it

rounds

### Every image, side by side, with its cost and the judge's reason

For each brief, every model's image with its recorded cost, seconds and size; the Designer's fact check of the required text, OCR recall as an independent check, anything invented; the overall score; and one line on why. Click any image for full size.

Fourteen exact numbers: five of six models got all of them.

directing it

### Edits, components and brand rules

Round 3 asked each model to change three things in its own diagram and nothing else, to draw a UI component with seven exact rows, and to follow house brand rules. Only GPT-5.4 Image 2 made the edit without breaking anything; the cheap model had no usable image in the round.

An edit is a redraw for most models.

guidance

### Which model for which job, and how to write the brief

For ten kinds of job: the model to use, the fallback, what to avoid, the cost and time, and the evidence. Twelve prompt rules learned from the faults (never name the platform, say "No other text", forbid invented numbers, attach slide 1 to every later slide of a deck), and how to call the models through OpenRouter.

The deliverable, for any agent that makes infographics.

ledger

### Every generation, every cent

One row per image: round, brief, model, OpenRouter's recorded cost, seconds, size, fact check, OCR recall, overall and usable scores. The Accountant's notes add cost per usable image, what drives cost, the cost of an edit and monthly projections.

$10.44, of which half paid for images nobody would use.

## How it is built

The briefs are in `scenarios.json`, built from the Re-anchoring article and its Five readers views (`source/`). `tools/run.py` calls OpenRouter's chat completions with image output, in parallel, and records each generation's cost, tokens, seconds, size and id; `tools/ocr_score.py` reads every image with tesseract in four segmentation modes and checks the required strings; Designer agents judged copies with random ids, never seeing the model; `tools/ledger.py` unblinds and totals; the Accountant and the Data Scientist, each an agent with a role file in `roles/`, wrote `analysis/`. The images are kept as full-size WebP in `img/`; the original PNGs are not in the vault.

## The audit, honestly

**What was scanned.** Every file before the first commit, for credential shapes (vault keys, every `sgit_` credential prefix, private-key headers, the SG/Send access token) and for the OpenRouter key and its prefix; and again after cloning with the published read key alone. The clone matched the source, file by file.

**What was found.** Nothing. The negative control, an all-zeros read key against the same vault id, returned nothing.

**What it does not claim.** Most cells hold one or two images, and repeats of one brief moved scores by up to two points, so a one-point difference between two models is noise; the tiers are not. The judge is one kind of agent with one rubric. Prices and models are OpenRouter's on 10 October 2026 and will change. Nothing here is a statement about any vendor beyond what these images show.

**Write-key status:** escrowed, in the gitignored credential tier, before this page was written.

## Derived facts

From `admin/build/catalogue_derive.py po5i477i <read key hex>`, read-only, no token, no clone.

- **Files:** 378 · **plaintext size:** 8818 KB
- **Commits:** 3 · **last updated:** 2026-10-10 · **HEAD:** `obj-cas-imm-953d35c76215`
- **Top level:** `README.md`, `analysis/`, `app.json`, `app/`, `img/`, `index.html`, `models.json`, `roles/`, `runs/`, `scenarios.json`, `scores/`, `source/`, `tools/`
- **Vault app:** yes, entry `index.html` · **browser-renderable:** yes

## Notes

**Where this came from.** A voice memo by Dinis Cruz asking for a bake-off of image models, from cheap to expensive, with the cost, the time and the ability to follow the brief recorded, ending in three models and guidance; the source article [Re-anchoring](../../../articles/re-anchoring-agent-behaviour-policies.md) and its [Five readers views](../article-views/index.md); the Designer role of the [SG/Send agent team](https://github.com/the-cyber-boardroom/SGraph-AI__App__Send/tree/HEAD/team/roles), and an Accountant and a Data Scientist written for this run.

**Who wrote this.** [agent@riskmandate.ai](mailto:agent@riskmandate.ai) (Claude Opus 5.5, `claude-opus-5-5`), in the sgit.ai site session, with Claude agents for the judges and the analysts. AI-generated text, disclosed as Article 50 of the EU AI Act asks; the person with editorial responsibility is Dinis Cruz.

[← All published vaults](../index.md)


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/infographic-bakeoff/index.html)*
