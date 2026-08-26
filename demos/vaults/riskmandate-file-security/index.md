# RiskMandate: File security — a published vault

> A risk-acceptance walk in eleven steps over one evolving register, where the browser becomes the database: versioned JSON in the vault is the source of truth, queried live through SQLite compiled to WebAssembly.

*Source: <https://sgit.ai/demos/vaults/riskmandate-file-security/index.html> · site v0.2.44 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../index.md) / RiskMandate — File security

# RiskMandate — File security

A worked risk decision, structured as an **eleven-step walk** over one shared, evolving register. Its argument is a process one: risk acceptance belongs at the **centre** of the flow, not rubber-stamped at the end — and when the facts change, the risks and their owners change with them.

**Open it yourself — the key is the whole credential.**
 Read key: `sgit_rk1_e8a1e664b9f984b0d8df442f463231077d455d7cbaa3e336610b14f9a1e1dc77:wu365g94`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_rk1_e8a1e664b9f984b0d8df442f463231077d455d7cbaa3e336610b14f9a1e1dc77%3Awu365g94) · From the CLI: `sgit clone sgit_rk1_e8a1e664b9f984b0d8df442f463231077d455d7cbaa3e336610b14f9a1e1dc77:wu365g94`
Published deliberately, and **derived** one-way from a vault key that is not published and never will be.

## See it live, here

Both surfaces open automatically below. You can also [**open the app in its own window ↗**](https://dev.vault.sgraph.ai/#sgit_rk1_e8a1e664b9f984b0d8df442f463231077d455d7cbaa3e336610b14f9a1e1dc77%3Awu365g94).

## What is in it

the inversion

### Risk acceptance, moved to the centre

The comparison is made on the page itself. Traditional: `Build → Ship → Run →` then a Sign-off — described as *"a rubber-stamp after the fact — blind spots, low accountability, and stale by the time it's signed."*

RiskMandate: `Facts → Risks → Accept & own → Propagate ↻ recalibrate`. The dashboard tracks two competing costs at once — **detect-only residual** against **control cost & friction** — so choosing a control is visibly a trade, not a free win. There is no *deny* fork: each risk is accepted, mitigated, or awaiting data, and someone owns the choice.

The discipline it sets itself is *"Grounded, not FUD — facts first."* Each fact walks to its evidence and its source before any decision is offered.

Step 1 of the walk: the counters, the two competing costs, and risk acceptance moved to the centre.

the pattern

### The browser is the database

The vault holds the issues as **versioned JSON files** — that is the source of truth. On load the app copies those nodes and edges into a real database running in the browser, and every read the UI performs is a query against it.

The vault's own note puts it plainly: this is the ordinary shape of a database system — a durable store plus a working engine — *except the durable store is a zero-knowledge, git-versioned file tree*. Steps 7 through 11 expose the layers directly: Data, Database, Graph DB, Graph viz, Explorer.

The vault browser: issues as versioned JSON, and the grant behind the walk.

## Notes

**On the permission line.** `app.json` requests `fs.read` and an explicitly empty `fs.write: []` — the write array is present and empty rather than absent, which states the intent instead of leaving it to be inferred.

[← All published vaults](../index.md)


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/riskmandate-file-security/index.html)*
