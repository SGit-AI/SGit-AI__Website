# graphs.sgit.ai — A node is just a node — meaning lives in the edges — sgit.ai

> A grammar for semantic graphs, argued in increasing depth from five rules you can apply tomorrow to a full positioning against schemas and vector search. It opens by insisting it is not a graph database pitch, and it publishes the four situations in which its own argument is the wrong one.

*Source: <https://sgit.ai/network/graphs.html> · site v0.2.52 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Network](index.md) / graphs.sgit.ai

# graphs.sgit.ai

A node is just a node — meaning lives in the edges

Screenshots captured 2026-08-21 · `v0.1.0` when captured · [SGit-AI__Website__Graphs ↗](https://github.com/SGit-AI/SGit-AI__Website__Graphs)

[Open graphs.sgit.ai ↗](https://graphs.sgit.ai)

## The claim is about edges, not storage

The hero states the whole thesis in two sentences and then proves it with the smallest possible example. Two nodes both hold the value `8080`. One is connected to a type, which is connected to a library, which is connected to a version; the other is connected to nothing.

**The difference is not in the value. The difference is in the connectivity.**

The source formulation is dated and attributed, as everything on that site is:

*"in our graph we do not use properties, because properties do not have meaning, they are just words; we capture meaning through connectivity."* — Dinis Cruz, 26 June 2026, in an architecture brief about digital twins

The home page: the thesis, the sourced quote, and the disclaimer immediately under it.

**And then, before anything else, a disclaimer** — which is the reason this entry leads with it rather than with the grammar:

**Read this before you read anything else: this is not a graph database pitch.** The claim is that one grammar is the interface at every boundary — *not* that we store things in a graph. There is no graph database anywhere in the work behind this site, and we say so on its own page.

A site about graphs whose first move is to disown the product category a reader expects to be sold is doing the same thing [sg-sentinel.sgit.ai](../network/sg-sentinel.md) does with its `NOT BUILT` banner. The house rule holds: publish the work, then say precisely what it is worth.

## The story that needs no background

The best argument on the site needs no security or graph knowledge at all.

Everyone knows expertise takes **10,000 hours**. The number comes from a 1993 study of violinists, where it was an *average* — not a threshold — and half the top group had not reached it. The original author spent much of his career correcting the popularisation.

**None of the corrections ever attached to the claim.** By then it had been carried through a citation graph of 242 papers and 200,000+ citation paths, every one of them leading back to a reading the source never supported. A document cannot fix that: the correction is a new document, and nothing connects it to the thousands that already rest on the error.

A graph can. Mark the claim superseded, and every path that rested on it becomes a query — *what did we build on this?* — rather than an archaeology project. That is the concrete thing a graph does that a document cannot, and it is why the depth pages insist on **supersede, never delete**.

## Five rules, and one banned edge

`/grammar/` is the page to keep open while drawing a graph — and, explicitly, *"the page an agent should be given before it starts emitting one."* Every edge is a verb, stated in both directions, and both directions get a name worth saying out loud:

| Edge | Its inverse | Reads as |
|---|---|---|
| `owned_by` | `owns` | this system is owned by this team · this team owns this system |
| `gives_rise_to` | `arises_from` | this vulnerability gives rise to this risk · this risk arises from this vulnerability |
| `backed_by` | `evidences` | this fact is backed by this evidence · this evidence evidences this fact |
| `grants` | `granted_by` | this role grants this permission · this permission is granted by this role |

The test for an edge is not "is this technically the reverse?" but **"would a person in this business say this sentence?"**

And `relates-to` is banned outright:

*"You can never have relates-to, because relates-to is meaningless, two things always relate to each other. The more granular the edge, the better the query you can write."*

The reason given is mechanical rather than aesthetic: an edge with no verb carries no constraint, so it cannot narrow a traversal — it costs fan-out and buys nothing. **The granularity of the verb is the precision of the query.** The remaining rules: rich nodes are good (solve the picture at query time, never by removing relationships), and never render the whole graph — render the result of a query.

The grammar page: the one-screen version, the verb/inverse table, and the ban on `relates-to`.

`/grammar/edge-set.html` carries the working set — 15 established edges, proposed inverses labelled as proposed, and a numbered gap (`G5`) where a glossary the corpus cites does not actually exist in the repository. The site also records that **the project breaks its own rule** in its own shipped configuration, and names where.

## What ships, what is argued

`/shipped/index.html` is the page to read first if you are deciding whether to trust the rest, and it says so. Its opening concession is the sharp one: *"this site's subject matter is almost entirely design."*

What is running, and checkable by opening the repository:

| What | The detail that makes it checkable |
|---|---|
| The vault commit DAG | Content-addressed objects — the identifier is a SHA-256 of the **ciphertext** — with multi-parent commits, a tree per directory, HMAC-derived deterministic refs, wave-BFS merge-base over all parents, and three-way merge |
| A graph of graphs | Typed `*.link.json` edges between vaults, optionally pinned to a commit in the target's history — a cross-graph edge that cannot silently follow a moving target |
| A read-only query API over the DAG | `sg.history.log / list / read / readText / readBlob`, exposed to *untrusted sandboxed apps* |
| A live typed property graph | The issue tracker's own data: 12 node types, 10 verb/inverse edge types with domain and range constraints, **71 nodes and 141 edges across 107 issue files** |
| Three published vaults | The regulation graph, the Risk Graph Explorer, agentic browser isolation |

Every number on the site is labelled live or parsed-from-a-design-document, and the two are never mixed. The line that ties it back to us is the project's own description of the shipped layer: *"what we've built is not fundamentally an encryption system. It is a content-addressed, portable, storage-agnostic version control protocol."* A commit DAG is a graph — and it is the one graph on that site that has been running for months.

The reality page: the ships-versus-argued table, with the absence of a graph database stated at the top.

## Where it says it loses

`/about/participant.html` is the most unusual page, and worth the click. It opens by applying the site's own thesis to itself — *"provenance should be traversable and the interested party should be a visible node; that applies to us"* — states the conflict plainly (*"if the argument on this site is right, the products we build are more valuable"*), and then lists **four situations where this approach is the wrong one**:

1. **Everyone already agrees, and always will.** One team, one codebase, one jurisdiction, stable vocabulary, no external party — a schema is simpler and faster. *"No boundary, no benefit."*
2. **You need the answer enforced, not computed.** "This field must never be null" is a validator's job. Some systems need a gate, and a gate is a schema.
3. **The graph would be empty.** Edges are work somebody has to do; where nobody has done it, similarity search wins outright.
4. **You want to buy it rather than build it.** The semantic layer is designed, not shipped.

## Why it is relevant here

Three connections, and the third is the one to watch.

**The commit DAG is already a graph.** The one indisputably shipped item on that site is sgit's own object model — content-addressed over ciphertext, multi-parent, with a real merge-base. The grammar argument and the vault are not neighbours by theme; they share a data structure.

**The query API is the vault's read model.** `sg.history.log/list/read` handed to untrusted sandboxed code is exactly the surface the [vault demos](../demos/index.md) run on. A graph query interface that an app you do not trust may call is a zero-knowledge story as much as a graph one.

**It is the first sibling that links back.** Its nav carries an `↗ part of sgit.ai` chip, and its footer links to this network page directly. Until now the network was a one-way index; this is the first entry that closes the loop.

**One correction to pass upstream.** The graphs site's footer links to `sentinel.sgit.ai`, which does not resolve. The site is at [`sg-sentinel.sgit.ai`](../network/sg-sentinel.md) — the `sg-` prefix is load-bearing. Checked 2026-08-21.

## Sections

- **Start here** — the five-minute version, why graphs at all, glossary
- **The grammar** — the five rules, and the working edge set with its numbered gaps
- **Depth** — the full argument, and a graph at every boundary
- **Examples** — browser isolation, the 2FA graph, Article 26(5) end to end, Wardley maps as graphs
- **Reality** — what ships and what is argued
- **Site** — the source documents in full, release history, and the participant disclosure

[← All network sites](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/network/graphs.html)*
