# Agentic Browser Isolation — a published vault

> A living risk graph for whether an AI agent browses with your logged-in sessions or an isolated identity: seventeen entry points, a page per stakeholder altitude, acceptance-gated escalation, cited evidence, and an app that requests no write capability at all.

*Source: <https://sgit.ai/demos/vaults/agentic-browser-isolation/index.html> · site v0.2.30 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../index.md) / Agentic Browser Isolation

# Agentic Browser Isolation

A living risk graph for one narrow, consequential question: when an AI agent browses and acts on the web, does it run **inside your browser with your logged-in sessions**, or inside an isolated browser with a scoped identity of its own?

**Why this one is here.** It is the site's own argument, made by somebody else and in far more detail: this is the ambient-authority problem the [serialised change proposal](../../../use-cases/serialised-pull-request.md) and the [agent use case](../../../use-cases/ai-agents.md) circle around — an agent borrowing a human's whole session because that is the only credential on offer. Here it is a register with owners, evidence and an escalation mechanism, and it is vendor-neutral: any isolation product is an *instance of* the control, and its own self-created risks go on the register like everything else.

**Open it yourself — the key is the whole credential.**
 Read key: `sgit_rk1_92cad4cea8f58c55f59b686c71c935225a1ba7c41ecb6922a8aa570467604f6e:0610gsp9`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_rk1_92cad4cea8f58c55f59b686c71c935225a1ba7c41ecb6922a8aa570467604f6e%3A0610gsp9) · From the CLI: `sgit clone sgit_rk1_92cad4cea8f58c55f59b686c71c935225a1ba7c41ecb6922a8aa570467604f6e:0610gsp9`
Published deliberately, and **derived**: the owner supplied a vault key, our intake check refused it for publication, and only this one-way derivation appears here.

## See it live, here

Both surfaces open automatically below. You can also [**open the app in its own window ↗**](https://dev.vault.sgraph.ai/#sgit_rk1_92cad4cea8f58c55f59b686c71c935225a1ba7c41ecb6922a8aa570467604f6e%3A0610gsp9) — with ten pages to walk, it is worth the room.

## What is going on here, step by step

Four things worth stopping on. Every screenshot is of this vault, driven by a script holding nothing but the published read key.

ten front doors

### One vault, seventeen entry points

The app opens on **Facts** and carries a numbered spine across the top: your reality, the two designs, the chain, how it unfolds, stakeholders, an explorer, two graph views and the raw data. Seventeen HTML entry points in one vault, each a real page.

The evidence is cited outward, too — the facts link to Brave's prompt-injection write-up, an arXiv paper on credential exposure, independent testing. A risk register that names its sources is one you can argue with.

The app on open: a ten-step spine, and the decision stated at the top.

the mechanism

### The same exposure, in seven languages

This is the idea worth stealing. Every altitude has **one named owner** — L1 IT, L2 CISO, L3 DPO/CFO/COO, L4 CEO, L5 Board — and each owns the risk *in their own language*.

A risk is never assigned automatically. It sits **pending** until that owner accepts it personally, and *only an accepted risk escalates to the altitude above*. Look at the counts in the picture: IT has 5 risks pending; everyone above is `waiting`, with nothing yet arrived — because nothing has been passed up. There is **no deny button**: accept, mitigate, or ask for more data.

Seven stakeholder altitudes, each with its own pending/accepted counts.

a graph, not a document

### The register is data, and you can see it as one

Seventy JSON files hold the register — risks, controls, evidence, owners, acceptances — and the app offers them as an explorer, a rendered graph, and a queryable graph database, with RDF tooling vendored into the vault so none of it needs the network.

That is the shape argument for vaults holding structured analysis rather than prose: the same encrypted objects serve a narrative page, a stakeholder view and a graph query, because the underlying thing is data.

The graph view, rendered in the browser from the vault\u2019s own JSON.

read-only by declaration

### An app that asks for nothing

Its `app.json` declares `fs.read: true` and `fs.write: []` — an **empty** write list. Compare the [Supplement Stack](../supplement-stack/index.md), which writes to one folder, and [Risk Mandate](../risk-mandate/index.md), which uses an LLM without holding its key.

Three vaults, three points on the same scale, each declared in the vault rather than configured on a server. The footer states the consequence plainly: *your changes are device-local; the vault baseline is never modified*.

app.json: read true, write [] — the app requests no write capability at all.

## What this vault demonstrates

| Feature | How this vault uses it |
|---|---|
| **Seventeen entry points** | The most in the catalogue: a narrative spine, a page per stakeholder altitude, an explorer, two graph views and the raw data — one encrypted store, many front doors |
| **Zero write capability** | `fs.write: []`. The app reads and renders; edits stay device-local and the vault baseline is untouched |
| Structured analysis, not prose | ~70 JSON files hold risks, controls, evidence and acceptances; the pages are views over that data |
| Graph tooling inside the vault | RDF libraries vendored in, so the explorer and graph database work with no network and no CDN — the authoring contract making offline the default |
| Cited evidence | Facts link out to primary sources; the register can be checked rather than believed |
| A mechanism, not a spreadsheet | Acceptance-gated escalation with named owners and no deny button — the part most worth copying |

## The audit, honestly

Audited across all 104 files before the key was published. **Clean:** no credentials, no personal data, no operational bookkeeping, and the vault's own key does not appear in its content.

The scan produced six hits and all six were false positives — digit runs like `0123456789` inside a minified RDF library, matching a phone-number pattern. Worth recording because it is what a real audit looks like: the interesting output of a secret scanner is usually the part you have to rule out by reading it.

As always: revocation is not retroactive. Anyone who fetches these objects keeps them.

## Derived facts

104 files · 2.4 MB · 4 commits · seventeen app entries · last updated 2026-07-18 — derived from the read key alone by `admin/build/catalogue_derive.py`, the same derivation that populates [the catalogue](../../../catalogue/index.md).


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/agentic-browser-isolation/index.html)*
