# AI Governance Graph, Hari Kota's stack as a fractal semantic graph, sgit.ai

> Hari Kota's ten-layer AI governance stack, kept exactly as posted, turned into a fractal semantic graph: the edges the table already contains, sourced edges between the layers, each example zoomed into the instrument and provisions it names, and the three gaps and the do-this-today test run as queries on a fictional shop. Published with its read key.

*Source: <https://sgit.ai/demos/vaults/ai-governance-graph/index.html> · site v0.7.37 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../index.md) / AI Governance Graph

# AI Governance Graph: Hari Kota's ten-layer stack as a fractal semantic graph

Hari Kota posted [The Full AI Governance Stack](https://lnkd.in/p/erGx6fqM) on LinkedIn: ten layers, what each does, and forty-six global examples. Under it, Dinis Cruz asked whether the layers had been mapped as a fractal semantic graph, and Hari asked back: "How would you structure the graph across the layers?" This vault is the answer, built. Hari's table is kept exactly as posted, every cell a node; the edges the table already contains are drawn first; then each example opens into the instrument it names, its provisions, and the people, controls, tests and records they require. Hari's three gaps and the "do this today" test run as queries on a fictional shop. It was published with the article [The AI governance stack, as a graph](../../../articles/the-ai-governance-stack-as-a-graph.md).

Hari's table, word for word, every cell a node.

**Open it yourself. The key is the whole credential.**
 Read key: `sgit_public_read_0a899b9e46ba92b1c2625ef911cbff307814fd3e1abf8a5fa1cf8a31045a01b9:1wp3xpf4`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_public_read_0a899b9e46ba92b1c2625ef911cbff307814fd3e1abf8a5fa1cf8a31045a01b9%3A1wp3xpf4) · From the CLI: `sgit clone sgit_public_read_0a899b9e46ba92b1c2625ef911cbff307814fd3e1abf8a5fa1cf8a31045a01b9:1wp3xpf4`
Published deliberately under the `sgit_public_read_` prefix, and **derived** one-way from a vault key kept in the gitignored tier and never published. Classified with `check_credential.py` before it touched this page, read back with the published key alone by `catalogue_derive.py`, and verified with an all-zeros read key as the negative control. Created, pushed and audited with sgit-ai 0.20.0.

## See it live, here

The vault opens as an app: the question, Hari's stack as posted, the same table as a graph, the edges between the layers, the zoom, do this today, the gaps as queries, one instrument across many layers, each layer's world, bring your own, and every source and file. You can also [**open it in the official UI**](https://dev.vault.sgraph.ai/#sgit_public_read_0a899b9e46ba92b1c2625ef911cbff307814fd3e1abf8a5fa1cf8a31045a01b9%3A1wp3xpf4).

## The one idea

Keep the stack as the view and make the graph the model. The ten layers are a great way to read governance, but an obligation does not live in one layer: Article 26(2) of the EU AI Act is binding law that names a person, for a system in the inventory, whose tier comes from a classification, and the evidence that it happened is a record for the board. The value is in the edges between the layers, so a gap is a missing edge, and a missing edge is a query anyone can run.

## What is in it

already a graph

### Hari's table contains ten edges before we add any

Where two rows name the same instrument, role or jurisdiction, the table itself makes an edge across layers. The EU AI Act is in rows 2, 6 and 10 and cites the DPIA of row 6; ISO/IEC 42001 is in rows 4 and 10; the NIST AI RMF in rows 4 and 6; Singapore in rows 3 and 8; the owner of row 5 is the RACI of row 9 and the training of row 10.

The ten curves were in the table all along.

between the layers

### A 10 x 10 matrix of edges, each resting on a provision

329 edges in the knowledge graph, 140 of them between layers: 10 from Hari's table, 11 from what its labels name, and 119 of ours, each citing the fact it rests on and marked as an addition. The busiest cells run from binding law to risk classification (12), from standards to risk classification (10), and from binding law to standards (9).

Click a cell for its edges, provisions and quotes.

zoom

### From one cell of the table down

An example opens into the instrument it names, the instrument into its provisions and dated values, a provision into what it requires, and that into the people, controls, tests and records of the worked example. The breadcrumb always leads back to the cell of Hari's table you started from.

Every deeper node keeps its way home.

do this today

### Hari's test, as a traversal

Pick one of Hollow Oak Home's eight AI systems (a fictional shop) and the app walks it across all ten layers, one row each, with the edge that answers it or a missing edge. Five of eight name an owner and a tier with its basis. The CV screening assistant passes Hari's test and still shows three missing edges: its owner has no literacy or training record, and its bias test result reaches nobody.

A test that passes, and what it does not see.

the gaps, as queries

### Layers 3, 5 and 10, run as queries

Soft law nobody tracks: Singapore, where two systems are used. No live inventory: a meeting transcription tool found in the expenses. Owners nobody trained: the HR Lead, owner and overseer of a high-risk system. Each query shows its plain question, its traversal step by step and its result, and four more follow: obligations without a control, guardrails without a test, results nobody reads, and one instrument across many layers.

A gap is a missing edge.

bring your own

### Your systems, the same queries, in your browser

Paste or load two small CSV files, systems and people, and the do-this-today test and Hari's three gap queries run locally. Nothing is sent anywhere. The templates hold Hollow Oak Home's data as the example.

Local only; the vault is never written.

## How it is built

Hari's table, the post and the comment thread are transcribed verbatim into `input/hari-stack.json`, the single source for the 85 nodes in Hari's words; the gate checks every one byte for byte. Facts about real instruments come from a research pack dated 9 October 2026 (`research/facts.md` and `facts.json`, 114 entries, each with its verified flag); nodes it could not verify carry an unverified badge. `tools/model.py` writes everything in `data/`: 335 nodes, 702 edges, one ontology per layer and 91 verbs, each with its inverse; exports as CSV, JSON-LD and Turtle. The app is on the design system of the [agency scale](../agency-scale/index.md) and [Agent Desk](../agent-desk/index.md) vaults. `tools/gate.py` runs 22 checks, among them: the data reproduces byte for byte; no edge uses `relates_to` or another verb without meaning; every edge cites a source; the matrix equals the count of edges; every query recomputes, in Python and in the browser; no credential shape, em-dash or unsupported absolute appears outside Hari's quoted words; and every view renders at desktop and phone widths with no errors and no network requests.

## The audit, honestly

**What was scanned.** Every file before the first commit, and every file again after cloning with the published read key alone: vault-key shapes, every `sgit_` credential prefix, private-key headers, cloud key shapes, the SG/Send access token, the vault's own key and its write key. The clone matched the source, file by file.

**What was found.** Nothing. The negative control, an all-zeros read key against the same vault id, returned nothing.

**What it does not claim.** It is a method and a worked example. Hollow Oak Home is fictional. Nothing in it says any real organisation complies or does not, and it is not legal advice. Several of Hari's examples moved in 2026 (the EU AI Act was amended by Regulation (EU) 2026/1744, Colorado SB 26-189 repealed and re-enacted SB24-205, Japan passed an AI Promotion Act); the labels stay as posted and the changes sit underneath as dated edges, the older values struck through.

**Write-key status:** escrowed, in the gitignored credential tier, before this page was written.

## Derived facts

From `admin/build/catalogue_derive.py 1wp3xpf4 <read key hex>`, read-only, no token, no clone.

- **Files:** 79 · **plaintext size:** 3006 KB
- **Commits:** 3 · **last updated:** 2026-10-09 · **HEAD:** `obj-cas-imm-cd3c326330e0`
- **Top level:** `PUBLIC.md`, `README.md`, `REALITY.md`, `app.json`, `app/`, `data/`, `docs/`, `index.html`, `input/`, `research/`, `templates/`, `tests/`, `tools/`, `versions/`
- **File types:** .json ×25, .js ×15, .css ×14, .py ×9, .md ×8, .csv ×4, .html ×2, .jsonld ×1, .ttl ×1
- **Vault app:** yes, entry `index.html` · **browser-renderable:** yes

## Notes

**Where this came from.** Hari Kota's LinkedIn post [The Full AI Governance Stack](https://lnkd.in/p/erGx6fqM), and the comment thread under it, October 2026; the method in [Fractal Semantic Graphs](../../../articles/introducing-fractal-semantic-graphs.md); the worked organisation from [Hope or enforcement](../hope-or-enforcement/index.md). The EU AI Act itself is parsed from official XML in the [Regulation Graph](../regulation-graph/index.md) vault, and an open AI control framework is a graph in [AI BCF as a graph](../aibcf-graph/index.md).

**Who wrote this.** [agent@riskmandate.ai](mailto:agent@riskmandate.ai) (Claude Opus 5.5, `claude-opus-5-5`), in the sgit.ai site session, for RiskMandate.ai and sgit.ai. AI-generated text, disclosed as Article 50 of the EU AI Act asks; the person with editorial responsibility is Dinis Cruz. Replies to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

[← All published vaults](../index.md)


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/ai-governance-graph/index.html)*
