# Risk Graph Explorer — a published vault

> A fact-to-risk graph explorer extracted into its own vault and designed to be public: its PUBLIC.md states three rules its build enforces, including no metered capability behind a published read key, and its app.json requests no permissions at all.

*Source: <https://sgit.ai/demos/vaults/risk-graph-explorer/index.html> · site v0.2.48 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../index.md) / Risk Graph Explorer

# Risk Graph Explorer

The graph explorer from [the risk-mandate work](../agentic-browser-isolation/index.md), refactored out into a vault of its own — and the first vault published here that was **designed to be public from the start**, with its own publication rules enforced by its own build.

**Answer the questions; the register assembles.** Seven views recompute as you go, including acceptance (who holds what) and what happens next (how decisions become incidents and projects). Nothing you answer leaves the page: no network call, no storage, no account. It is destined for riskmandate.ai, and the vault is how it will be served.

**Open it yourself — the key is the whole credential.**
 Read key: `sgit_rk1_1c1b95f5903e35850a9bc0541ffa09c6b5d4017cbf18817d2ad6f894127e5638:3simlnqe`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_rk1_1c1b95f5903e35850a9bc0541ffa09c6b5d4017cbf18817d2ad6f894127e5638%3A3simlnqe) · From the CLI: `sgit clone sgit_rk1_1c1b95f5903e35850a9bc0541ffa09c6b5d4017cbf18817d2ad6f894127e5638:3simlnqe`
Published deliberately, and **derived**: the owner supplied a vault key, our intake check refused it for publication, and only this one-way derivation appears here.

## See it live, here

Both surfaces open automatically below. You can also [**open the app in its own window ↗**](https://dev.vault.sgraph.ai/#sgit_rk1_1c1b95f5903e35850a9bc0541ffa09c6b5d4017cbf18817d2ad6f894127e5638%3A3simlnqe) — try the presets, then change one answer and watch the register move.

**Going deeper.** This vault has more in it than one page holds. [**The seven views, explained**](views/index.md) walks each view with a screenshot of the live vault and the mechanism behind it. [**The author’s walkthroughs**](videos/index.md) carries three recorded demos with full transcripts — the reasoning that the screenshots cannot show.

## What is going on here, step by step

the argument

### An empty register is a correct answer

It opens at zero: **0 facts, 0 risks, 0 provisions**, and a prompt to answer the first question. Nothing is assumed about your estate until you say something about it.

That is the claim the whole app is built to make, and its README states it plainly: *"the technical answers can be as bad as you like — if nothing is at stake behind them, the register is short, and that is the correct answer."* A tool that produces the same output for a scratch service and a payments platform is a checklist, not a risk register.

The explorer at zero: no answers, so no register.

context decides

### Answer differently and the graph changes shape

Load the **Exposed** preset and the same questions produce 18 facts, 37 risks and 14 provisions, with a header that reads *decides about a person · in production · at stake*. Seven views recompute together: the estate graph, context, a role risk map, risk chains, the register, acceptance, and what happens next.

Look at the graph itself — amber edges are exposure facts, green are assurance, and **ghosted means nobody has said either way**. Recording that absence as information, rather than as an implicit pass, is the detail that makes this a graph rather than a form.

The Exposed preset: 18 facts, 37 risks, and unanswered relationships drawn as ghosts.

published on purpose

### A vault that carries its own publication rules

Most vaults here were audited by us before their key went out. This one arrived with the audit already written into it: `PUBLIC.md` states that **every byte committed is already public**, and its build refuses if any of three rules is broken — nothing private committed (the gate scans *every file*, not just the built artefact), no write token, and **no metered capability**.

That third rule is the one worth borrowing, and we had not written it down: *"a published read key in front of an LLM config is an open tab on somebody else's budget, and a spend cap is a rate limiter on the fun, not a control."* It sent us back to re-check a vault we had already published — see the note below.

PUBLIC.md: three rules, enforced by the vault’s own build.

the floor

### permissions: {}

An empty permissions object. Not a scoped write, not a withheld credential — **nothing requested at all**. The app answers questions in the page: no network call, no storage, no account, as its README says.

The catalogue now spans the full range, each declared in the vault rather than configured on a server: [Risk Mandate](../risk-mandate/index.md) uses an LLM without holding its key, [Supplement Stack](../supplement-stack/index.md) writes to one folder, [Agentic Browser Isolation](../agentic-browser-isolation/index.md) declares `write: []`, and this one asks for nothing.

app.json with an empty permissions object — the floor of the scale.

## Extraction as a pattern

This vault began as a section of a larger one. Pulling it out gave it a smaller audience surface, a shorter history, its own release cadence and — decisively — **its own permission posture**: the parent could plausibly want a model; this one may never have one, and says so.

That is worth naming as a technique. Vault boundaries are permission boundaries, so the question *"should this be its own vault?"* is usually the question *"should this have a different key, a different audience, or a different set of capabilities?"* Here the answer was all three, and the split made the public version safe to publish in a way the parent could not have been.

## The audit, honestly

Clean: **zero** hits across every text file — no credentials, no personal data, no operational bookkeeping, and the vault's own key absent from its content. The tidiest audit of any vault published here, which is what you would expect of one built to be public.

**It also caused us to re-audit ourselves.** Its third rule — no metered capability behind a published read key — applies to [Risk Mandate](../risk-mandate/index.md), which does carry an LLM config. So we checked rather than assumed: taking the sealed credential from that vault and attempting to open it with the read key we published, AES-GCM refuses (`InvalidTag`). The seal is under a key a read-key holder does not hold, so publishing that read key did not expose anybody's budget. Rule satisfied there by sealing; satisfied here, more conservatively, by absence.

As always: revocation is not retroactive. Anyone who fetches these objects keeps them.

## Derived facts

33 files · 428 KB · 7 commits · one app entry · last updated 2026-08-10 — derived from the read key alone by `admin/build/catalogue_derive.py`, the same derivation that populates [the catalogue](../../../catalogue/index.md).


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/risk-graph-explorer/index.html)*
