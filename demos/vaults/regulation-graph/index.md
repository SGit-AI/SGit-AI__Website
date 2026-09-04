# Regulation Graph — a published vault

> The EU AI Act as a citable graph: Regulation (EU) 2024/1689 parsed from official Formex XML, hash-verified to source bytes, 1,523 nodes and 1,944 edges across eleven views. Published as a redacted republication after an audit found a plaintext vault key in the original.

*Source: <https://sgit.ai/demos/vaults/regulation-graph/index.html> · site v0.2.53 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../index.md) / Regulation Graph

# Regulation Graph

The EU AI Act as a graph you can cite. Regulation (EU) 2024/1689 parsed from official Formex XML, hash-verified against the bytes it came from, and served as an **evidence layer**: a risk in a register points at a named obligation in a real instrument instead of being asserted.

**This vault exists because the first one could not be published.** The original carried a live vault key in plaintext — write access to a *different* vault — inside a handoff document. Our audit found it before anything shipped. Deleting the file would not have been enough: vault objects are content-addressed and immutable, so a credential committed once may stay reachable from history. This is a **redacted republication with new history**, and the vault says so itself in its own [PUBLIC.md](#public).

**Open it yourself — the key is the whole credential.**
 Read key: `sgit_rk1_c004daae386e8d17fa648884acc527018bd4ea1116ad673fb2f1b068011695c9:73heuprz`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_rk1_c004daae386e8d17fa648884acc527018bd4ea1116ad673fb2f1b068011695c9%3A73heuprz) · From the CLI: `sgit clone sgit_rk1_c004daae386e8d17fa648884acc527018bd4ea1116ad673fb2f1b068011695c9:73heuprz`
Published deliberately, and **derived** one-way from a vault key that is not published and never will be.

## See it live, here

Both surfaces open automatically below. You can also [**open the app in its own window ↗**](https://dev.vault.sgraph.ai/#sgit_rk1_c004daae386e8d17fa648884acc527018bd4ea1116ad673fb2f1b068011695c9%3A73heuprz) — the entry point is the Art 9 lab; the back-link top-left reaches the other ten views.

## What is in it

the overview

### Every number traces back to source bytes

The landing view states the shape of the graph in counts: **113 articles**, **500 paragraphs**, **417 points**, **180 recitals**, **13 annexes**, **68 definitions** — resolving to **1,523 nodes** and **1,944 edges**.

Underneath, the part that makes it evidence rather than a summary: two instruments composed into one view, each with its CELEX identifier and the **SHA-256 of the retrieved bytes**. Regulation 2024/1689 is shown as *amended by 2026/1744, no official consolidation yet — this graph composes*. That sentence is a factual claim about the state of EU law, and it is checkable.

Application dates are treated as **versioned properties, never bare facts**: superseded pre-Omnibus dates are struck through rather than overwritten, each carrying its basis (`Article 113(a) as amended`) and an as-of date.

Built from Formex XML retrieved from CELLAR, hash-verified, parsed deterministically.

browse the act

### The instrument itself, structure first

The full Act, navigable by its own structure, with a provenance footer on every node and search across the text. This is the view that makes the rest defensible: when a risk cites Article 9(2)(a), you can go and read Article 9(2)(a) — in the text that was parsed, not a paraphrase of it.

Per-node provenance footers, and search over the parsed text.

the graph

### Article-level relationships, with amendment halos

The citation graph at article level, drawn with Cytoscape, showing amendment halos and aggregated citations. Eleven views in total sit behind the top nav — including **SQL** (SQLite over sql.js, in memory, preset and free queries), **RDF** (rdflib, partition-separated predicates, Turtle export), **Concepts** (the Act's 68 defined terms with every usage linked) and **External refs** (every other EU instrument the Act cites, as an in-vault citation graph).

All of it runs client-side over the SG bridge. The vault is never written by the app.

Article-level graph; ten sibling views cover SQL, RDF, concepts and external citations.

the art 9 lab

### The entry point is an experiment, deliberately

`app.json` sets `entry` to `lab/index.html`, so opening the vault lands in the **Art 9 lab** — paragraph universes, a web-component folder explorer, provision graphs with reach profiles, and a **Graph REPL**: an LLM chat whose read-only tools drive the canvas.

The lab is marked *experimental* and has no main nav of its own; the back-link top-left returns to the other views. Landing a reader in the newest, least finished thing is an unusual choice and an honest one.

Opening the vault lands here: the Art 9 lab, marked experimental.

public.md

### The vault states its own publication rules

Following [Risk Graph Explorer](../risk-graph-explorer/index.md), this vault carries a `PUBLIC.md` declaring what it holds to — and, unusually, what was removed to make publication possible. The removals are visible to any reader as `<VAULT-KEY-REMOVED>` and `<READ-KEY-REMOVED>` markers rather than silently deleted lines.

**Rule 3 was verified rather than assumed.** The Graph REPL reads an OpenRouter key, and `lab/app/repl.js` looks for one at `/key.json` *inside the vault* before falling back to device storage. So we checked: no `key.json` exists — confirmed in a clone made with the published read key, which is what a reader actually gets. The REPL is bring-your-own-key, and nothing metered ships behind the published credential.

The rules, and the two removals, in the vault rather than only on this page.

## What it is for

The README states the purpose in one line: *"a risk in a register points at a named obligation in a real instrument instead of being asserted."* It is the evidence layer beneath the [Risk Mandate](../risk-mandate/index.md) work — where [a risk chain](../risk-graph-explorer/views/index.md) ends in `touches: EU AI Act Art. 12`, this is the vault that can say what Article 12 actually says and prove the bytes.

Its eight hard rules are worth reading in full, and two are worth quoting here:

- **Evidence, not compliance.** Never a claim that an organisation passes or fails. Not legal advice.
- **Provenance chain end to end:** claim → graph node → vault file → commit → official source (CELEX/ELI plus SHA-256 of retrieved bytes).

The second is the one this site keeps arriving at from other directions. It is the same instinct as [running comparisons as tests](../../../compare/index.md) and as [refusing to call a release live until the site serves it](../../../articles/green-does-not-mean-live.md): a claim is worth what its chain of custody is worth.

## What it does not do

- **Only Article 9 is built out in depth.** Rule 4 is *"partial connection is sufficient — build only what the register cites"*, so the lab covers Art 9 and the rest of the Act is present as structure and citations rather than fully annotated.
- **The Graph REPL needs your own OpenRouter key.** Nothing is supplied, deliberately. Without one the REPL pane is inert — which is the correct behaviour, not a fault.
- **No consolidated text exists.** 2024/1689 is amended by 2026/1744 with no official consolidation yet; this graph composes the two, and says so rather than presenting a merged text as authoritative.
- **External research is marked UNVERIFIED.** The research report under `docs/research/` carries external claims the vault has not itself checked, and labels them.

## How it was published

This vault is the clearest worked example of [the publishing method](../publishing.md), because it is the first one where the audit **stopped** a publication instead of clearing it:

1. **Classify the credential.** The submitted credential was a vault key, not a read key. The intake check refused it — the fourth time.
2. **Derive rather than refuse.** The read key was derived one-way; the vault key went to the gitignored tier the release tripwire scans for.
3. **Audit with the key about to be published.** 204 text files, read-key clone. One finding: a plaintext vault key for another vault.
4. **Stop.** No page was written. The finding was reported before anything else happened.
5. **Republish clean.** A new vault, new history, two credentials redacted in place with visible markers, a `PUBLIC.md` stating what changed, and a re-audit from a fresh read-key clone: **205 files, zero findings**.

The 370-plus bare 64-hex strings the audit flagged on the way through were all `sha256` provenance hashes — checked, not waved away. A scan that never produces a false positive is not scanning hard enough.


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/regulation-graph/index.html)*
