---
title: nhi.sgit.ai
domain: nhi.sgit.ai
tagline: Agents you run, agents you rent, and the identity gap
summary: The question of how to give an AI agent an identity splits into two populations, and every product on the market answers only the first. For the agents you actually name — the ones running in Claude, Codex or behind an API — the honest current answer is to hand over a broad credential and hope.
category: Agents & AI
thesis: The question splits into two populations, and the industry only answers one
aliases: agent agents identity credential machine workload service account nonhuman non-human authentication authorisation
observed: 2026-08-19
seen_version: v0.1.14
repo: SGit-AI__Website__NHI
hero: nhi-home.webp
tags: identity, agents, security
---

## The distinction the whole site turns on

**Agents you run** execute on your infrastructure. You can attest the workload, install an identity agent, and control everything. An open standard — SPIFFE — issues short-lived cryptographic identities on exactly that basis.

**Agents you rent** execute on somebody else's. You cannot attest the workload, cannot install anything, and the only thing you control is the credential you hand over.

The site puts the two side by side and lets the table make the argument:

!shot nhi-home.webp | images/ | The home page, with the two-population comparison directly under the thesis.

The last row is the one that lands: for agents you run, the industry answer is *"mature — and expensive"*. For agents you rent, it is *"none"*. SPIFFE is described by practitioners as a multi-year engineering project needing a dedicated team; for rented agents, the equivalent capability is an open feature request.

## "Hope is not a control"

The site names the current practice rather than describing it politely. When you hand an agent a broad credential you are making **two hopes** — that it will not misuse what it holds, and that it will not discover the rest of what that credential actually reaches. Neither hope changes your accountability, which runs to the board.

The second hope is the one most people have not costed. The site's framing is that **the real authorization is the closure**: inbox access is every account resettable by email; desktop access is every stored credential. The grant is not the words in it — it is everything reachable from them.

!shot nhi-thesis.webp | images/ | The thesis page: the argument with citations, rather than assertion.

## Why it is relevant here

This is the problem sgit's [read keys](/demos/vaults/index.html) and [append lanes](/api/append-lanes.html) are shaped against. A published read key is a credential whose closure is *provably* bounded — it opens one vault, cannot write, and cannot be turned back into write access. An append token can write to one lane and cannot read it.

The [comparison pages](/compare/index.html) use a privilege vocabulary — scope, operations, bearer, mediation, duration, withdrawal, observability — that is the same question asked in a different register.

## Sections

- **Thesis** — the two populations, with citations
- **Hope** — why the current workflow is hope-driven, and what the two hopes cost
- **Method** — from hope to controls: enumerate, bound, observe, contain, account
- **Options, Industry, Collection** — what exists, what it costs, and the open questions
