# Start with an AI decision, then trace it back to the guidance: the DSIT AI Risk Toolkit vault

> An independent, experimental journey through the UK DSIT AI Risk Management Toolkit, published as a vault: describe a use case, review the risk prompts that apply, record evidence and owners, propose controls and reassessment, and follow each step back to its source. An eight-slide walkthrough plays on the page from the encrypted vault, with the PDF as a download. Underneath: separate worlds with named bridges, every edge labelled curated or lexical, hashed source snapshots, 13 passing checks and 6 published gaps. Not an official DSIT service or certification.

*Source: <https://sgit.ai/demos/vaults/dsit-ai-risk-toolkit/index.html> · site v0.6.6 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../index.md) / DSIT AI Risk Toolkit

An independent, experimental journey through the UK DSIT AI Risk Management Toolkit

# Start with an AI decision, then trace it back to the guidance

Describe a use case, review the risk prompts that apply to it, record evidence and owners, propose controls and a reassessment trigger, and follow each step back to its source in the official guidance. The vault below is a working prototype of that journey. An eight-slide walkthrough shows it with a fictional example.

[Try the live vault ↗](https://dev.vault.sgraph.ai/#sgit_public_read_cdc00d2baaf75361d86ae1b7a40169bd98d71aaae1bd581e181a0f0ba0e0e6bb%3A0q4sfr57) [View the eight-slide walkthrough ↓](#walkthrough) [Download the PDF deck](#walkthrough)

The walkthrough uses fictional data. This is an independent experiment with public UK government guidance, not an official DSIT service, assessment or certification. Nothing you enter leaves your browser tab until you export it.

## See the journey in eight slides

The deck is read live out of the vault as you click: the slide source runs in a sandboxed frame with no origin and no network, each slide renders in a second frame with scripting switched off, and the five screenshots are decrypted in your browser. Use **notes** for the speaker notes, **focus** to hide the slide list, the arrow keys to move, and **PDF** to download the printed deck.

**The eight slides, in one line each**

1. **A decision before a risk list.** The vault opens on a use case and a governance decision, not a checklist.
2. **The journey.** Use case, relevant risks, evidence and owner, control and reassessment, original source.
3. **Start with the use case.** Title, decision, scope and decision owner. Three synthetic examples, or your own.
4. **Context changes the questions.** Ten context facts prioritise 153 top-level prompts; unknown answers stay open.
5. **One risk, a working record.** Pick a source question, record evidence, owners, a control and a review trigger.
6. **The graph stays underneath.** The research graph of 941 nodes and 4,735 edges connects question, topic and source.
7. **Take the work with you.** A JSON export of your answers and the derived session graph; import recomputes conclusions.
8. **Try a decision in the vault.** Bring one use case and one decision, and say where the journey is confusing.

## What you can try in the vault

Five steps, in the order the journey asks them. Each one is a screen in the live vault; the graph does the tracing underneath, and you do not need to learn it first.

| Step | What you do | What to notice |
|---|---|---|
| **1 · Use case** | Write the decision you need to make: a title, the governance decision, the scope, the decision owner. Or pick one of three clearly labelled synthetic examples. | The journey starts from a decision, not from a list of risks. |
| **2 · Risk prompts** | Answer ten context facts. The 153 top-level prompts from the official guidance are prioritised for your case; unknown answers stay open. | The prompts keep the source wording. Six conservative rules propose scope changes for human review; none removes a question silently. |
| **3 · Evidence and owner** | For a risk that applies, record an evidence reference and the people responsible. | A recorded reference is a user assertion. It is not independently verified by anything in the vault. |
| **4 · Control and reassessment** | Propose a control and the trigger that would make you look at the risk again. | These are proposals, kept apart from the source text, and labelled as such. |
| **5 · Source** | Follow any prompt back to the retained guidance snapshot and the GOV.UK page it came from. | Every prompt walks back to hashed source bytes. That is the graph, doing its job without being asked. |

**Where your answers go.** Nowhere, until you say so. Draft answers live in the browser tab; **export the JSON before closing it**. The export holds your entries and a derived session graph, not copies of the source corpus, and importing it recomputes the scope conclusions. This is a prototype built to be tested with the people it is for, and the most useful thing to send back is where it confused you. [Open the journey ↗](https://dev.vault.sgraph.ai/#sgit_public_read_cdc00d2baaf75361d86ae1b7a40169bd98d71aaae1bd581e181a0f0ba0e0e6bb%3A0q4sfr57)

## The vault, embedded

The journey opens as the vault's home page. The earlier source-backed reference edition is one click away inside it, at `reference.html`. It has more room [in its own tab ↗](https://dev.vault.sgraph.ai/#sgit_public_read_cdc00d2baaf75361d86ae1b7a40169bd98d71aaae1bd581e181a0f0ba0e0e6bb%3A0q4sfr57).

## How it works underneath

The journey sits on the reference edition this vault started as, and the reference edition is the reason the source trace works. Its structure has not changed; it has moved below the decision.

### Separate worlds, and the bridges are the point

The guidance, the official spreadsheet, the risk method it describes, the 160 risk-question bullets and the frameworks it cites are not the same kind of thing, and modelling them in one vocabulary would force most of them to pretend to be another. The vault declares separate worlds and lets each keep its own shape, with named bridges between them. Its ontology states the limit plainly: *"containment alone is not fractality. Cross-world edges make the semantic transitions inspectable."* That is the same distinction [Fractal Semantic Graphs](../../fractal-graphs/index.md) arrives at from the other direction.

| World | What lives in it |
|---|---|
| `source` | The publication as retrieved: 30 guidance sections, 67 blocks, and the bytes they came from |
| `risk_method` | The method the guidance describes: risk categories, treatments and appetite |
| `risk_question` | The 160 risk-question bullets, in nine category shards, with 274 punctuation units for stable traversal and no semantic claim |
| `workbook` | The official spreadsheet as data: 4 sheets, 490 cells, 208 of them formulas |
| `frameworks` | The external standards the text cites, referenced and never reproduced |

The semantic explorer at the four-world edition of 20 September 2026. Each connection states its verb and how it was obtained: `is_derived_from · curated` is an authored claim, `is_mentioned_by · lexical` is a string match, and the vault never lets you mistake one for the other.

### Curated against lexical

Every assertion is labelled with which it is: an edge somebody decided, or an edge a search found. A reader who disagrees with a `curated` edge is disagreeing with a person. A `lexical` edge claims only that a word appeared, and the vault's own limits say *"lexical mentions are not validated meaning."* It also refuses the inference everyone wants to make from a compliance artefact: *"no compliance inference or organisation attestation is made."*

The risk-method world, from identification to treatment. Nine categories, each an edge away from the guidance that defines it and the workbook cells that score it.

### Every claim carries the bytes it came from

Five source snapshots are retained inside the vault, each with its URL, its retrieval date and the SHA-256 of the bytes: the guidance body, two content-API responses, and the official workbook in both XLSX and ODS. The workbook is read rather than rewritten: cached values are not recalculated, dates stay as Excel serials, styling is not reproduced, and the vault says so. Two of its checks exist purely to prove the originals were not touched.

*"A claim is only as useful as its trace."* The checks, all passing, and the known gaps published beside them.

### The six gaps it publishes about itself

- **It corrects its own earlier number.** *"Direct OOXML recount finds 208 formula cells, correcting 227 in the retained earlier briefing."* The earlier briefing stays in the vault, uncorrected, with the correction recorded beside it.
- **It preserves a contradiction in the source.** The official file is named v1.1 and its own Welcome sheet says v1.0. Both labels are kept.
- **It refuses to repair the source.** Two defined names in the official workbook are broken. They are reported broken. *"No source repairs were made."*
- **It declines the flattering reading.** *"Starter rows are not evidence of adoption"*, and no independent implementation, compliance assessment or adoption metric is asserted.
- **It dates itself.** The retained research briefing is a snapshot as of 20 September 2026; external sources may change.
- **It names what it did not build.** Formula dependency expansion and shared-formula expansion are not implemented.
*"Inspect. Download. Query."* The official files remain unchanged, and SQLite compiled to WebAssembly runs the queries in your tab.

### What it demonstrates about vaults

| Feature | How this vault uses it |
|---|---|
| **Read and download, no write** | `fs.read` is true and `write` and `delete` are both empty arrays, with downloads and external links declared. The journey's drafts stay in the tab and are never written back |
| **Queries with no backend** | sql.js, which is SQLite compiled to WebAssembly, is bundled so the query view works offline. The copies were taken from the published [Regulation Graph vault](../regulation-graph/index.md) and the provenance of that decision is recorded in `NOTICE.md` |
| **Two things versioned in the open** | The reference edition and the journey carry separate version records, each with its own release page, and the version badge in the app links to the release it is showing |
| **A licence that survives the copy** | Source text under OGL v3.0, application code with no additional licence assigned by the release, bundled sql.js under MIT with SQLite in the public domain, marked under MIT. Each is stated rather than blended |
| **Machine-readable on the way out** | `downloads/graph.jsonld` keeps every assertion's provenance and partition, and the journey's JSON export carries the derived session graph, so both leave the vault without losing what made them checkable |
| **A deck, on the site, from the vault** | The walkthrough above follows the [decks/v2 contract](../../../docs/briefs/vault-decks-on-a-site.md): manifest, slide source, styling, screenshots and PDF read from the vault; controls, routing and download owned by this page |

## Status, versions and limits

| What | As published, 23 September 2026 |
|---|---|
| **Main journey** | v0.2.0, dated 23 September 2026, an independent experiment. Its record describes itself as *"experimental, unverified user assertions; no official DSIT endorsement or compliance assessment"*. Its ontology and question shards remain the v0.1.0 research snapshot |
| **Reference edition** | v0.2.3, dated 23 September 2026: the journey promoted to the vault home, the former reference home kept at `reference.html`, every source-backed page retained |
| **Research graph** | 941 nodes and 4,735 edges, as stated in the deck's own notes and counted from the vault's edge shards. A separate graph from the reference edition's, and the counts are not merged |
| **Reference graph** | 1,051 nodes and 1,289 edges in `data/graph.json`, measured from a read-key clone on 23 September 2026. The four-world edition of 20 September was 617 nodes and 694 edges; that figure is kept below as the dated snapshot it was |
| **Checks** | 13 of 13 passing in `data/validation.json`, with 6 known gaps published beside them |
| **Licences** | DSIT source text: Open Government Licence v3.0, attributed, with no departmental logos or crests. Application and graph code: created for this edition, with no additional licence assigned by the release; the owner may choose one separately. Bundled sql.js and marked: MIT. SQLite: public domain |
| **What this is not** | Not an official DSIT service, standard, certification or conformance assessment. No validated risk scoping, no claim of organisational adoption, no user-tested effectiveness. A prototype for testing with intended users |

****Provenance and the credential****

**The key is the whole credential.**
 Read key: `sgit_public_read_cdc00d2baaf75361d86ae1b7a40169bd98d71aaae1bd581e181a0f0ba0e0e6bb:0q4sfr57`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_public_read_cdc00d2baaf75361d86ae1b7a40169bd98d71aaae1bd581e181a0f0ba0e0e6bb%3A0q4sfr57) · From the CLI: `sgit clone sgit_public_read_cdc00d2baaf75361d86ae1b7a40169bd98d71aaae1bd581e181a0f0ba0e0e6bb:0q4sfr57`
Published under the `sgit_public_read_` prefix, which is the form for a key published on purpose. It grants read and only read; the owner credential is kept outside the vault, as its README says. Classified before it touched anything, and verified with an all-zeros negative control at first publication: the real key produced 42 files, the control an empty directory. [What the prefixes declare →](../../../docs/credentials.md)

### Derived facts, 23 September 2026

From `admin/build/catalogue_derive.py 0q4sfr57 <read key hex>` and a read-key clone, no token: **155 files** · 12.1 MB plaintext · 14 commits · HEAD `obj-cas-imm-16ef099d1561` · app entry `index.html` declared in `.vault/app.json` with `fs.read`, empty `write` and `delete`, downloads and external links · one deck in `decks/decks.json` (type `decks/v2`), 8 slides, 5 screenshots, PDF `deck/DSIT_AI_Risk_Use_Case_Journey.pdf` with SHA-256 `36f9e16c295824c09e4acffa0c0370f4a66c0fd01c58068f733857c8de4e1cf6` · 6 version records, current 0.2.3 · 5 hashed source snapshots retrieved 20 September 2026.

### The pre-publication audit

| Checked | Result |
|---|---|
| Credentials and secrets | **None.** No vault key, no credential under any `sgit_private_` prefix, no API keys, tokens, `delete_auth` or `append_token` values, no private-key blocks. The public read key appears in the deck's last slide and in the PDF's link annotation, on purpose |
| Personal data | **None.** Two email addresses appear, `alt.formats@dsit.gov.uk` and `psai-tech@dsit.gov.uk`, both published institutional contacts carried over from the official publication. The deck's second slide paraphrases a public LinkedIn comment and says it did not verify the post or claim endorsement |
| Its own checks | Re-read from `data/validation.json`: 13 of 13 passing, 6 known gaps published |
| Attribution | OGL v3.0 acknowledged, no crests or logos used, external standards referenced and not reproduced, official status disclaimed on the front page, in `NOTICE.md` and on every slide's footer |

### The historical snapshot, 20 September 2026

First published as row #31 with 42 files, 3.2 MB, 617 nodes and 694 edges across 3 partitions and 4 worlds, 8 predicates all with declared inverses, 8 of 8 checks passing, and 2 released versions with 0.1.1 current. Those numbers described that edition and are kept here with their date. The four screenshots in the section above were taken from it.

The usual rule applies to this key as to every other one here: **revocation is not retroactive**. Anyone who fetches these objects keeps them.

A rung on [Fractal Semantic Graphs](../../fractal-graphs/index.md), beside the [Regulation Graph](../regulation-graph/index.md) whose sql.js copies it reuses. [← All published vaults](../index.md) · [The publishing method](../publishing.md) · [Decks from a vault, on a site](../../../docs/briefs/vault-decks-on-a-site.md)


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/dsit-ai-risk-toolkit/index.html)*
