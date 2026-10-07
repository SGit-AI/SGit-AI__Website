# AI BCF as a graph, the AI Baseline Control Framework converted into a semantic graph, sgit.ai

> Jan van Dijke's AI Baseline Control Framework v1.0, twenty AI governance controls published under CC BY-SA 4.0, converted from its CSV export into a semantic graph with an ontology, a SKOS taxonomy, JSON-LD and Turtle, eighty hyperlinked documents, a SQLite database that runs in the browser, and a join to the EU AI Act's own text in the Regulation Graph vault. A fractal graph view, a crosswalk, SQL and triple-pattern consoles. Published as a vault with its read key, under the same licence.

*Source: <https://sgit.ai/demos/vaults/aibcf-graph/index.html> · site v0.6.101 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../index.md) / AI BCF as a graph

# AI BCF as a graph: an open AI governance framework, converted into a semantic graph

The [AI Baseline Control Framework](https://aibcf.org/) v1.0, published by Jan van Dijke on 2 October 2026 under CC BY-SA 4.0, is twenty controls for organisations that deploy AI, mapped to the NIST AI RMF, ISO/IEC 42001 and the EU AI Act. Five days later its CSV export became this vault: a graph of 127 nodes and 239 edges, an ontology, a SKOS taxonomy, JSON-LD and Turtle, eighty hyperlinked documents, a SQLite database that also runs in the browser, and a join from every AI Act citation to the law's own text in the [Regulation Graph](../regulation-graph/index.md) vault. It is an adaptation, licensed the same way, and not an official AI BCF product.

The overview, as the app opens: the attribution first, then the framework's shape and what the conversion found.

**Open it yourself. The key is the whole credential.**
 Read key: `sgit_public_read_1ecf3a157b4be75b3623348a076ce0130ff6e4bd186fd5706af63bca999c0163:lop5iqzw`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_public_read_1ecf3a157b4be75b3623348a076ce0130ff6e4bd186fd5706af63bca999c0163%3Alop5iqzw) · From the CLI: `sgit clone sgit_public_read_1ecf3a157b4be75b3623348a076ce0130ff6e4bd186fd5706af63bca999c0163:lop5iqzw`
Published deliberately under the `sgit_public_read_` prefix, and **derived** one-way from a vault key kept in the gitignored tier and never published. Classified with `check_credential.py` before it touched this page, read back with the published key alone by `catalogue_derive.py`, and verified with an all-zeros read key as the negative control.

## See it live, here

The vault opens as an app: the overview, the twenty controls with filters, one page per control, the fractal graph view with three guided journeys, the crosswalk, a SQL console, a triple-pattern console, every file with a download button, and the licence. You can also [**open it in the official UI**](https://dev.vault.sgraph.ai/#sgit_public_read_1ecf3a157b4be75b3623348a076ce0130ff6e4bd186fd5706af63bca999c0163%3Alop5iqzw).

## The one idea

A control framework is a graph that has been written down as a list. Each control belongs to a category, has a type, applies under a condition, cites clauses of other frameworks, and refers to other controls in its prose. Put those relationships into edges, each a verb with its inverse, and questions that a list answers by reading become questions a graph answers by walking: which controls have no equivalent in the frameworks they map to, which clauses are cited by more than one control, which controls the law itself connects. The licence is what made the conversion possible on the day it was wanted. The argument, and what the conversion found, are in the article, [An open AI governance framework, and what its licence let us build](../../../articles/ai-baseline-control-framework.md).

## What is in it

the graph view

### One grammar, five altitudes, a question at each

The graph view puts one node at the centre and draws its neighbours grouped by verb, with in-edges read through their inverse. Click a neighbour and the view zooms one level: from the framework to a category, a control, a cited clause, and the paragraph of EU law that clause resolves to. Each altitude has its own question, shown above the drawing, and the view draws the answer rather than the whole graph. Edge styles show where each edge came from: the framework, parsed from its text, joined to the law, or the sgit.ai overlay. Three journeys walk the paths the article describes.

CM.3 at the centre: what it cites, when it applies, and the three controls the law links it to.

the law, joined

### From a citation to the paragraph it names

Eleven AI Act citations in the framework resolve to ten article and paragraph nodes in the Regulation Graph vault, joined by id. The node carries the paragraph's text and the amendments that vault records, so the view can say which controls cite an article that Regulation (EU) 2026/1744 changed: four of the eight cited articles. Two citations name a subparagraph the Regulation Graph does not model, and resolve one level up, to the paragraph; the join says so rather than pretending.

Article 50(1), as the Regulation Graph holds it, reached from CM.2.

the crosswalk

### Twenty rows against three frameworks, and four empty rows

One column per NIST AI RMF function, ISO/IEC 42001 Annex A group and AI Act article; each cell counts the clauses a control cites there. The empty rows are the Access controls, AC.1 to AC.4, which the framework itself marks as having no equivalent in the three. They are what an identity and access management practice adds to AI governance, and the reason the framework is worth reading next to the three.

The crosswalk. The four empty rows are the finding.

a browser database

### SQLite in the page, and the same tables as a file

sql.js, SQLite compiled to WebAssembly and carried inside the app, builds three tables from the graph JSON: controls, nodes and edges. Six saved queries answer the article's questions, and the box takes any SQL. Nothing leaves the browser. The same tables ship as `db/aibcf.sqlite` for any desktop tool.

Which controls cite an article the 2026 amendment changed: seven rows.

triples

### The same graph as statements, asked in either direction

Every edge is stored twice, once with its verb and once with its inverse, and indexed by subject, verb and object. A query is one or more patterns, `subject verb object`, with `?names` for what you want found; patterns join on shared names. Asking what the Access category *groups* works because `is_grouped_in` declared its inverse.

Three patterns, joined on shared names: control, clause, law, amendment.

a control, as a document

### The framework's own words, with the edges around them

Each control page shows the statement, trigger, why and how verbatim, then what it cites with each clause's heading resolved, the controls its prose refers to, the controls the law links it to, and, set apart and labelled as not part of AI BCF, the sgit.ai reading: which words of the Agent Behaviour Policy the control addresses and which articles here discuss the same ground. The same content is in `docs/controls/` as Markdown.

AC.3: a named owner for each autonomous AI system, and no equivalent in the three.

files

### Eleven files, five shapes, one build

The original CSV with its SHA-256; nodes and edges; the ontology; the SKOS taxonomy; JSON-LD; Turtle; the findings; the join; the SQLite file and its schema. Each has a download button, so the app is also the way to take the data elsewhere. `tools/build.py` regenerates all of it from the CSV, and the same inputs give the same bytes.

Every format, downloadable from inside the vault.

## The licence, and what it asks

AI BCF is licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). That allows anyone to share and adapt it for any purpose, on three conditions, and this vault meets each one where a reader will see it. **Attribution:** the framework, its author, version and licence are named on the overview, on every control, at the foot of every document and in `LICENSE.md`. **Changes indicated:** `LICENSE.md` lists them; no control text was altered; the overlay is labelled on every edge. **ShareAlike:** this adaptation is CC BY-SA 4.0 too. sql.js, bundled for the browser database, is MIT licensed. Nothing here implies endorsement by the framework's author.

## How the app is built

Web components in the shape [coding.sgit.ai](https://coding.sgit.ai/javascript/index.html) documents: one directory per component with a `.js`, an `.html` and a `.css` of the same basename, a base component that loads them and calls `onReady()`, a tokens file, events namespaced and dispatched through `document`. `tools/bundle.py` inlines the templates, the graph files, sql.js and the scripts into one `index.html`, as the vault-app contract asks; the source stays split under `app/` so it can be reviewed as code. The route is held in a variable so the app works inside the vault host.

## The audit, honestly

**What was scanned.** Every file in the vault folder before the first commit, for vault-key shapes, every `sgit_` credential prefix, private-key headers, cloud key shapes, the SG/Send access token and the names of real people who are not credited by the framework. The one 64-character hex string in the data is the CSV's SHA-256.

**What was found.** Nothing. The vault holds the framework's public text, identifiers of NIST and ISO clauses without their text, and paragraphs of EU law from the Regulation Graph vault, itself built from EUR-Lex. The negative control, an all-zeros read key against the same vault id, returned nothing.

**What the conversion does not claim.** The citations are the framework's; this vault did not check that each cited clause says what the control needs. The links through the law come from the AI Act's own cross-references and show that two controls touch the same provisions, not that one depends on the other. The overlay is a reading, not a mapping.

**Write-key status:** escrowed, in the gitignored credential tier, before this page was written.

## Derived facts

From `admin/build/catalogue_derive.py lop5iqzw <read key hex>`, read-only, no token, no clone.

- **Files:** 143 · **plaintext size:** 3,116 KB
- **Commits:** 2 · **last updated:** 2026-10-07 · **HEAD:** `obj-cas-imm-3ae105da1f75`
- **Top level:** `LICENSE.md`, `PUBLIC.md`, `README.md`, `app.json`, `app/`, `data/`, `db/`, `docs/`, `graph/`, `index.html`, `source/`, `tools/`, `versions/`
- **File types:** .md ×83, .json ×16, .html ×12, .css ×12, .js ×12, .jsonld ×2, .py ×2, .sqlite ×1, .sql ×1, .ttl ×1, .csv ×1
- **Vault app:** yes, entry `index.html` · **browser-renderable:** yes

## Notes

**Where this came from.** Jan van Dijke's post introducing the framework on LinkedIn, and a reply to the question of whether it was published as a semantic graph, through an API, or in other formats: "for now there is only Export as CSV on https://aibcf.org/controls/ on the top right. Good suggestions!" This vault is one answer to that question, built from the export, and offered back.

**Who wrote this.** [agent@riskmandate.ai](mailto:agent@riskmandate.ai) (Claude Opus 5.5, `claude-opus-5-5`), in the sgit.ai site session, for RiskMandate.ai and sgit.ai. AI-generated text, disclosed as Article 50 of the EU AI Act asks; the person with editorial responsibility is Dinis Cruz. Replies to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

[← All published vaults](../index.md)


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/aibcf-graph/index.html)*
