# PCI DSS v4.0.1 as a semantic graph, first pass, published as a vault

> The Payment Card Industry Data Security Standard v4.0.1 as a typed graph: six goals, twelve requirements, 63 sections, 85 individual requirement identifiers, nine appendices, 21 terms, eight roles, assessment artefacts, merchant levels and the four dates, joined by 367 edges that each read in both directions. The standard's licensed text is deliberately not in it; identifiers, quoted titles and marked paraphrases are, every node with provenance and every source hashed, plus a tool for licence holders to add the text locally. Built to be connected to the other graphs on this site.

*Source: <https://sgit.ai/demos/vaults/pci-dss-graph/index.html> · site v0.6.89 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../index.md) / PCI DSS Graph

# PCI DSS v4.0.1 as a semantic graph, first pass

The Payment Card Industry Data Security Standard, version 4.0.1, as a typed graph you can click through: six goals, twelve principal requirements, 63 sections, 85 individual requirement identifiers, nine appendices, 21 defined terms, eight roles, the assessment artefacts, the merchant levels and the four dates that matter, joined by 367 edges, every one a verb with a named inverse. It exists so that the standard can be **connected**: a risk that cites a section, an evidence file that satisfies a control, a regulation that overlaps with a requirement. The text of the standard is not in it, on purpose, and the page says why.

The graph as it opens. Counts, the tree by goal, and the standard node with the rules of the graph. Rendered from the read-key clone, served locally.

**Open it yourself. The key is the whole credential.**
 Read key: `sgit_public_read_0de0b2f3a337f0a495df2dad8243d2cd2f7dbba3de57921b75e08b7fbe11dcc9:7xyzg5zs`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_public_read_0de0b2f3a337f0a495df2dad8243d2cd2f7dbba3de57921b75e08b7fbe11dcc9%3A7xyzg5zs) · From the CLI: `sgit clone sgit_public_read_0de0b2f3a337f0a495df2dad8243d2cd2f7dbba3de57921b75e08b7fbe11dcc9:7xyzg5zs`
This key is published on purpose, under the `sgit_public_read_` prefix. It is **derived** one way from a vault key that is kept in the gitignored tier and never published. `check_credential.py` classified it before it was put on this page. A read-only clone with it produced twelve files identical to the source folder; an all-zeros key as a control failed while downloading the vault index.

## See it live, here

The vault opens as an app. Click any node in the tree; the card shows what it is, where it comes from, and its edges in both directions. You can also [**open it in its own window ↗**](https://dev.vault.sgraph.ai/#sgit_public_read_0de0b2f3a337f0a495df2dad8243d2cd2f7dbba3de57921b75e08b7fbe11dcc9%3A7xyzg5zs).

## Why the text is not in it

PCI DSS is copyright PCI Security Standards Council, LLC, and is distributed from its Document Library under a licence that does not allow reproduction or derivative works. Every other reference graph on this site is built from a source that can be copied and hashed: the EU AI Act from its official Formex XML, a government toolkit from its published pages. That is not available here, so the rules of this vault are different and are stated in the graph itself. Identifiers are facts about the document and are in. The short official titles of the twelve requirements are quoted from a public secondary source, hashed in the vault. The 63 section subjects, the defined terms, the roles and the appendices are **our own one-line paraphrases**, each marked `provenance: paraphrase`. And each individual requirement is an identifier and nothing else.

For the people who need the text, which is everyone who actually has to comply, the vault ships `tools/import_official.py`. A licence holder runs it against the PDF they downloaded, it extracts the numbered requirements into a local file, and the app shows the text beside every identifier. That file stays on their machine or a private branch. The published graph carries the structure; the licence holder's copy carries the standard.

## What is in it

a section

### Every node is a card with edges in both directions

Section 3.3 is the one everybody in payments knows: sensitive authentication data is not stored after authorization. Its card shows our paraphrase, its provenance, the edge `turns_on` to the term it depends on, the edge `part_of` back to Requirement 3, and its individual requirement identifiers below it. Read from the term's side, the same edge is `bears_on`. Nothing on the card is asserted without saying where it came from.

Section 3.3, with its edges out and its edges in.

the terms

### The vocabulary is a graph too

Account data is cardholder data plus sensitive authentication data; the PAN is a kind of cardholder data; full track data, the card verification code and the PIN are kinds of SAD. Those `is_a` edges are what let a question like "which sections bear on anything derived from the PAN" be a query rather than a reading. Twenty-one terms, each with a one-line paraphrase and the appendix that is the authority for it.

Sensitive authentication data: what it is a kind of, what its kinds are, and which sections turn on it.

roles and assessment

### Who assesses whom, with what

The Council qualifies QSAs, ISAs and ASVs. A QSA or an ISA produces the Report on Compliance. An ASV performs the quarterly external scan. Payment brands set the merchant levels, and each level validates with a ROC or a self-assessment questionnaire, of which there are nine types by payment channel. Merchants rely on service providers and acquirers. It is the part of the standard that is usually a diagram in a slide deck, here as edges that can be walked from either end.

A QSA: qualified by the Council, produces the ROC, assesses the standard.

an identifier

### The individual requirements, and where their identifiers come from

Microsoft publishes, under the MIT licence, the Azure Policy initiative it maps to PCI DSS v4.0.1, and its policy groups are named by requirement identifier. That file is in the vault with its hash, and the 85 identifiers it names are the individual requirement nodes here, each with a `mapped_by` edge to the initiative. It is a citable list, not a complete one. The card for an identifier says so, and says what a licence holder can do about it.

An individual requirement: the identifier, the notice, and the mapping it was cited from.

## The rules of the graph, and the sources

- Every node carries `provenance`: a source node whose file and SHA-256 are in the same graph, or the word `paraphrase`.
- Every edge is a verb with a named inverse. Seventeen verb pairs, listed in the graph and in the README.
- Five sources, fetched on 29 September 2026 and hashed: the PCI SSC announcement of v4.0.1 (11 June 2024, "no additional or deleted requirements"), the v4.x resource hub, the Document Library page, the Wikipedia article for the twelve requirement titles, and the Azure Policy file for the identifiers.
- Four dates as milestone nodes: v4.0 published 31 March 2022; v4.0.1 published 11 June 2024; v4.0 retired 31 December 2024; the future-dated requirements mandatory from 31 March 2025.
- Built by `tools/build_graph.py` from tables in that file, with no model in the line. A wrong paraphrase is a one-line fix and a commit.

## What to connect next

This is a first pass, made in an afternoon so that there is something to connect to. The obvious edges, in the order they are worth adding: a risk register whose risks `cite` a section here, which the [Risk Graph Explorer](../risk-graph-explorer/index.md) already has the shape for; an evidence vault whose artefacts `satisfy` a control, with hashes, the way [The Evidence Dispatch](../evidence-dispatch/index.md) ties claims to bytes; the [Regulation Graph](../regulation-graph/index.md), where the EU AI Act's obligations overlap with Requirements 6, 10 and 12; SAQ eligibility, once cited from the SAQ documents; and the list of which controls became mandatory on 31 March 2025. Every one of those is an edge between two vaults, which is what [a fractal graph](../../fractal-graphs/index.md) is for.

## Files

| Path | What |
|---|---|
| `index.html`, `app.json` | The app, opened when the vault opens; requests no permissions, calls no model, writes nothing |
| `graph/pci-dss-v4.0.1.graph.json` | The graph: schema `sgit-graph/v1`, 232 nodes, 367 edges, the verb table and the counts |
| `sources/` | The five public pages the graph rests on, with their hashes in the graph |
| `tools/build_graph.py` | The tables and the generator |
| `tools/import_official.py` | For licence holders: fill the identifiers with the standard's text, locally |
| `README.md`, `PUBLIC.md` | What it is, what it deliberately is not, and what anyone may do with it |


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/pci-dss-graph/index.html)*
