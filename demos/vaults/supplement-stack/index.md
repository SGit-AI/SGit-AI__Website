# Supplement Stack — a published vault

> A patient-held health record as a vault: a real supplement regimen, label photographs every extracted value is traceable to, deterministic totals against UK RNIs and EFSA upper limits, and an adherence log the app may write to and nothing else. Shared with a professional by handing over a read key.

*Source: <https://sgit.ai/demos/vaults/supplement-stack/index.html> · site v0.2.43 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../index.md) / Supplement Stack

# Supplement Stack

A patient-held health record as a vault: a real supplement regimen, a photograph of every label the numbers were read from, deterministic totals against UK reference values — and an app permitted to write to exactly one folder and nothing else.

**The idea it is built on, in one line.** Every label describes one product; **nothing describes the sum**. The missing artefact is the total per nutrient across everything a person is taking — so the model extracts (fuzzy, and traceable to a label photo), the code adds up (deterministic, and reproducible), and the output is a briefing for somebody qualified. **Never a verdict.** This is a record-keeping tool, not medical advice, and no compliance finding of any kind exists for this pattern.

**Open it yourself — the key is the whole credential.**
 Read key: `sgit_rk1_047186b559528058c66d1792b7345639b1238cb95c166d1d5f5b65c59813c2ee:r7zes477`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_rk1_047186b559528058c66d1792b7345639b1238cb95c166d1d5f5b65c59813c2ee%3Ar7zes477) · From the CLI: `sgit clone sgit_rk1_047186b559528058c66d1792b7345639b1238cb95c166d1d5f5b65c59813c2ee:r7zes477`
Published deliberately. It grants read, and only read — a write attempt is refused by the server's write gate.

## See it live, here

Both surfaces open automatically below. You can also [**open the app in its own window ↗**](https://dev.vault.sgraph.ai/#sgit_rk1_047186b559528058c66d1792b7345639b1238cb95c166d1d5f5b65c59813c2ee%3Ar7zes477).

## What this vault demonstrates

| Feature | How this vault uses it |
|---|---|
| **Scoped write permission** | `app.json` grants the app `read` over everything but `write` and `mkdir` over `adherence/`*only*. The app that records what you took each day cannot touch the regimen, the label photographs or the references — least authority, declared in the vault and enforced by the host |
| Source-mapped extraction | every amount in `regimen.json` carries a `label_image` pointing at the photograph it was read from, so a misread is *visible* rather than propagated — the same discipline a diff gives code |
| Deterministic analysis | `scripts/totals.py` sums per nutrient with its rules stated in the open: topicals contribute nothing, as-needed items sit outside daily totals, and a null amount is **flagged, never guessed**. The in-app JavaScript does the same arithmetic, so two implementations can be checked against each other |
| Named, dated reference data | UK RNIs and EFSA upper limits, with sources and a transcription note — explicitly *not* US Daily Values, because comparing a UK intake to US references without saying so would be a quiet error |
| Honest incompleteness | one product's 27-nutrient panel is not yet captured, so the app labels the totals **INCOMPLETE** rather than showing a confident wrong number |
| The brief ships with the vault | `briefs/` carries the architecture brief the whole thing was built from — the reasoning travels with the artefact |

## What is going on here, step by step

The embeds above are the real vault, which makes it easy to scroll past the parts that matter. Each row points at one of them. Every screenshot is of this vault, driven by a script holding nothing but the published read key.

the daily record

### What was actually taken, not what was intended

The **Today** tab is a checklist of the day's regimen, grouped by timing. Ticking an item and pressing **Save today** writes one small JSON file — `adherence/2026-08-16.json` — into the vault.

That distinction is the point: a regimen file says what you *mean* to take; the adherence log says what you *did*. When the conversation with a professional finally happens, the second is the honest input.

The Today tab: per-item, per-timing, with a Save that writes into the vault.

traceable extraction

### Every number points back at the photograph it came from

The **Stack** tab lists each product with its dose, timing, route — and the label photograph the amounts were read from. A model did that reading, which is a fuzzy step, so each value carries a `label_image` back to its source.

This is the source-map discipline applied to health data: a misreading stays *visible* and checkable against the picture, instead of quietly becoming a number in a total.

The Stack: products, doses and the label photograph behind each set of numbers.

the missing artefact

### The sum nobody else computes

This is the tab the whole vault exists for. Every label describes one product; **nothing describes the sum**. Here it is: total per nutrient per day, each against the UK RNI and the EFSA upper limit, with the contributing products named.

Two details matter more than the numbers. The reference set is *named and dated* (UK RNI + EFSA UL — deliberately not US Daily Values, for a regimen bought in the UK). And the amber banner says the totals are **incomplete**, listing exactly which amounts have not been captured: *"Nothing is guessed: a value that is not on a captured label is flagged, never estimated."*

Totals per nutrient with ×RNI and ×UL ratios — and an honest incompleteness banner.

never a verdict

### The output is a briefing, not a diagnosis

The **Briefing** tab assembles everything into something to hand to a pharmacist or GP: the stack, the totals, the overlaps, the open questions — *"Three products target the knee — is that a sensible combination or redundant?"*, *"Do any of these interact with my other medication?"*

The tool deliberately stops there. It does the arithmetic nobody had done and hands the result to somebody qualified. It never answers the questions itself, and the vault says so on its own About tab.

The Briefing: what to take to a professional, including the questions to ask.

least authority

### The app may write to one folder — and nothing else

Here is the vault's own `app.json`, read straight out of the store. The permission block grants `read` broadly but `write` and `mkdir` over `adherence/` *only*.

So the app that ticks off today's doses cannot alter the regimen, the label photographs, or the reference values — not by policy, but because the capability was never granted. This is what permissions look like when they are a property of the vault rather than a setting on a server, and it is the healthcare-shaped version of the whole argument.

app.json: read broadly, write only adherence/ — least authority, declared in the vault.

## Why this shape matters beyond supplements

This is the clearest **patient-held record** on the site. The data lives in a vault the person controls; sharing it with a professional is handing over a read key, not granting an account on someone's platform, and not emailing a PDF that is copied forever the moment it arrives. The write key never leaves the owner, so a reader can read *everything* and change *nothing*.

The division of labour is the transferable part: **a model does the fuzzy work** (reading amounts off a photograph), **code does the exact work** (adding them up), and every fuzzy step is traceable to its source so a human can check it. Any domain where an LLM reads documents and arithmetic must be right — expenses, lab results, invoices, dosing — can borrow that shape. See the [healthcare use case](../../../use-cases/health-regulated.md) for where this fits.

## The audit, honestly

Every vault is audited before its read key appears here. This one is **clean on credentials**: no tokens, no keys, no `.vault/` operational bookkeeping — and the scan for personal identifiers found none either (no name, address, contact details, date of birth or health-service number; the record describes its owner only as "UK-based adult male").

What it *does* publish is a real person's actual supplement regimen, and the health context that can be inferred from it — a knee, sport, sleep. That is the owner's own data, published on purpose, and it is worth stating the rule that goes with it: **revocation is not retroactive**. Anybody who fetches these objects keeps them. Rotating the key protects future commits and returns nothing already read. The regimen is published because a real record demonstrates the pattern in a way a fabricated one cannot — and because the alternative, a sanitised sample, is exactly the thing this vault argues against.

## Derived facts

23 files · 2.3 MB · 5 commits · app entry `index.html` · twelve label photographs — derived from the read key alone by `admin/build/catalogue_derive.py`, the same derivation that populates [the catalogue](../../../catalogue/index.md).


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/supplement-stack/index.html)*
