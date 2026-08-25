# Private Health Score — a published vault

> A complete clinical workflow as a vault: adaptive questionnaire, a versioned scoring framework loaded at runtime, explainability tracing every recommendation to an answer, and a clinician review — published as a sanitised republication after an audit found the original vault carried its own write credential.

*Source: <https://sgit.ai/demos/vaults/health-score/index.html> · site v0.2.41 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../index.md) / Private Health Score

# Private Health Score

A complete clinical workflow in one vault — adaptive questionnaire, a versioned scoring framework, an explainability layer that traces every recommendation back to an answer, and a clinician review screen — running entirely client-side. It is published here as a **sanitised republication**, because the vault it was built from carried its own write credential in its home page and could never have had its key published.

**The idea it is built on, in one line.** The framework, not the model, produces the recommendations. A versioned JSON standard — five dimensions, five bands, eight scoring rules — is loaded from the vault at runtime and does the scoring deterministically; the LLM writes the narrative on top and is labelled as such, with its model and cost on the page. **Never a diagnosis.** This is a proof of concept on synthetic profiles, and no compliance finding of any kind exists for it.

**Open it yourself — the key is the whole credential.**
 Read key: `sgit_rk1_a76f327fb602f1619a67a15a0b756d69e82a1f7fa48438d4b6ecbebae2dc3d40:zc6abngv`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_rk1_a76f327fb602f1619a67a15a0b756d69e82a1f7fa48438d4b6ecbebae2dc3d40%3Azc6abngv) · From the CLI: `sgit clone sgit_rk1_a76f327fb602f1619a67a15a0b756d69e82a1f7fa48438d4b6ecbebae2dc3d40:zc6abngv`
This key opens vault `zc6abngv`, the sanitised republication — **not** the vault this content was authored in, whose key was never published and never will be. See the audit below.

## See it live, here

Both surfaces open automatically below. You can also [**open the app in its own window ↗**](https://dev.vault.sgraph.ai/#sgit_rk1_a76f327fb602f1619a67a15a0b756d69e82a1f7fa48438d4b6ecbebae2dc3d40%3Azc6abngv).

## What this vault demonstrates

| Feature | How this vault uses it |
|---|---|
| **One vault, three audiences** | `patient/`, `doctor/` and `shared/` split the same record by *who is reading it*, not by copying it. The patient fills in the questionnaire, the clinician opens a review of the same answers, and the framework and analysis both sides rely on sit in `shared/`. One credential, one copy, three views |
| The rules are data, and versioned | `shared/health-score-standard.json` is the scoring framework as a file — 5 dimensions with explicit weights (cardiovascular 25%, metabolic 20%, lifestyle 20%, wellbeing 20%, preventive care 15%), 5 bands and 8 rules, stamped `v1.0`. The viewer labels it *"loaded from vault at runtime"*, and a **Reveal JSON** button shows the source behind the rendering |
| Deterministic score, generated prose | the number comes from the framework; the LLM writes the narrative around it. The clinician screen states the provenance in the open — *AI-generated · estimated cost $0.024 · claude-sonnet-4* — and `llm-analysis.json` carries `status: pending_clinician_review`. The model's output is a draft for a human, and the file says so |
| Every recommendation traced to an answer | the explainability layer lists what helped and what hurt with the rule that decided it: *"Last Blood Test: over 2 years — scored 50/100, affects your Preventive Care score."* Its own note draws the line: *"The framework — not the AI — produced these. The AI analysis adds nuance; these are the foundations"* |
| Severity-ranked clinical actions | the review screen sorts suggested actions **URGENT → HIGH → MEDIUM → LOW** rather than presenting a flat list, and pairs them with the dimension scores that triggered them — plus an *adaptive risk gates* section showing which branches the questionnaire opened because of earlier answers |
| No account anywhere in the flow | sharing the record with a clinician is handing over a derived read key. There is no clinician login, no tenant, and no server-side copy — the vault's own architecture section states the three-credential model, and the read key you are holding is the proof |
| Permissions left undeclared | honest gap rather than a feature: `app.json` declares `entry`, `auto_open`, `present` and a HUD block, and **no permission block at all** — compare [VoiceDebrief](../voice-debrief/index.md), which scopes `fs.read` to one folder. An app that never states what it needs cannot demonstrate least authority, and will need a grant declared when the platform's deny-by-default lands |

## What is going on here, step by step

The embeds above are the real vault, which makes it easy to scroll past the parts that matter. Each row points at one of them. Every screenshot is of this vault, driven by a script holding nothing but the published read key.

what opens

### Two demo profiles, chosen to disagree

The vault opens on a hub built around two synthetic profiles that are deliberately not alike: **Alex, 34** — BMI 25.9, good lifestyle, scoring **74 · Good** — and **Sam, 47** — BMI 33.8, multiple risk factors, scoring **38 · Needs Attention**.

One profile would demonstrate the rendering. Two that land in different bands demonstrate the *framework*, because every screen after this one can be read twice and compared.

Two profiles, two bands — so every later screen can be read twice.

the patient side

### A ten-step questionnaire that branches on what you answer

The patient app is a ten-section flow — welcome, about you, lifestyle, health, history, concerns, score, AI analysis, vault save, complete — with a demo bar across the top that can drive each step or run the whole thing.

The two steps worth noticing are the last two. **Vault save** is where the record is encrypted and written, and **complete** is the final record — the flow ends by producing an artefact the person keeps, not a result page that disappears.

Ten sections, adaptive, ending in a saved encrypted record.

the rules, as a file

### The framework is versioned, readable and separate from the code

This is the part that makes the rest auditable. The scoring standard is a JSON file in the vault, rendered here as a document: five bands from **At Risk (0–29)** to **Excellent (85–100)**, and five weighted dimensions shown as a radar with the weights stated numerically beside it.

Because it is data rather than logic buried in a function, it can be versioned (`v1.0`), diffed between commits, and disagreed with. **Reveal JSON** shows the source that produced the page you are reading — the rendering and the rules are the same object.

The scoring framework as a versioned document, not as code.

explainability

### Each number carries the answer that produced it

Alex's 74 breaks into heart health 78, lifestyle 76, wellbeing 72 — and then into the individual answers behind them. *"Smoking: never — scored 100/100 in the framework."* *"Alcohol: light — 90/100."* Against him: *"Last blood test: over 2 years — 50/100, affects your Preventive Care score. Framework flag: book routine blood panel."*

Three tabs sit above it — **Your Health Story**, **Score Breakdown**, **Evidence Map** — the same result at three depths. The layer's own caveat is the important sentence: the recommendations come from the framework, and the model only adds nuance on top.

Score → dimension → the specific answer and its framework rule.

the clinician side

### The same record, arranged for someone qualified to act on it

Sam's review puts the record on the left — dimension scores with the reasoning under each, then the full profile — and the AI analysis on the right, as suggested actions ranked by urgency: two **URGENT** (a GP appointment for cardiac symptoms, and a specific blood panel), three **HIGH**, then medium and low.

Two things make this more than a dashboard. The analysis is labelled *AI-generated* with its model and cost, so a clinician knows what they are reading. And beneath it is a **clinical notes** block for the reviewer's own observations — the tool expects to be corrected, and keeps the correction next to what it corrected.

Ranked actions, provenance stated, and room for the clinician to disagree.

the fix, visible

### The card that used to hold a live write key

The vault explains its own credential model in three cards: the vault key (full read/write, kept private), the derived read-only share token for the clinician, and the data location (client device only). The model is right, and it is the argument the whole demo makes.

In the original vault, the first card contained an **actual working vault key** — the real credential for the vault you were reading it in. Here it shows the *shape*, `⟨passphrase⟩:⟨vault-id⟩`, with the reason attached: a write credential is never written into the vault's own content. The teaching value survives; the credential does not.

The same three-credential explanation, with the live key removed.

a fresh vault, not a rewrite

### Two commits, both from the day it was republished

The SGit view is the evidence for the claim in the audit below. This vault's history begins on **22 August 2026** with `init`, followed by the sanitising commit. The original's 61 commits are not here, and neither is anything they contained.

That is deliberate and it is the whole point of republishing rather than patching. A read key hands over *every* commit, so deleting a credential from the current files would have left it sitting in history, reachable by anyone holding the key that was supposed to be safe to publish.

A history that starts at the republication, because the old one could not be published.

what it asks for

### A manifest that declares no permissions at all

145 bytes: an entry point, `auto_open`, `present`, and a HUD configuration that hides the vault name. There is no permission block.

Included because it is the honest weak point of an otherwise careful vault. Silence is not least authority — it is an absence of a statement, and it reads as one next to [VoiceDebrief](../voice-debrief/index.md)'s scoped `fs.read` or [Risk Graph Explorer](../risk-graph-explorer/index.md)'s deliberate empty grant. When deny-by-default lands, an app that never said what it needs is the one that stops working.

`app.json`: an entry point, a HUD, and nothing said about permissions.

## Why this shape matters beyond health

The transferable pattern is **the rules as a versioned file, the model on top, and the trace between them**. Anywhere a decision has to be explainable — lending, eligibility, triage, grading — the same split applies: put the criteria in a document that can be versioned and argued with, compute deterministically against it, let the model write the part humans read, and label which is which. The failure mode this avoids is the one where nobody can say afterwards whether the number came from a rule or from a sentence a model produced.

The vault-shaped part is that sharing with a professional is **handing over a derived read key**, not creating them an account. The nearest thing on this site is [Supplement Stack](../supplement-stack/index.md), which does the same for a patient-held supplement record with real data; this one covers the fuller workflow, on synthetic profiles, and adds the clinician's side.

## The audit, honestly

This is the vault whose audit stopped a publication, so the finding comes first.

**The original vault published its own write credential.** `home/index.html` rendered a card labelled *"Patient vault key (write access) — full read/write, patient keeps this private"*, and the value in it was the **real, working vault key for that vault**. Anyone given the read key — the credential this page exists to hand out — could have read that card and gained write access to everything in it. The read key was therefore never publishable, and was never published.

**Why a fresh vault and not a fix.** Removing the card from the current files would not have been enough: a read key grants every commit, and the credential would have remained readable in the history. So the working tree was copied, sanitised, and committed into a *new* vault (`zc6abngv`) with a new key. The original's 61 commits were left behind. This is the site's own rule — [republish, don't retrofit](../publishing.md) — applied to the case that produced it.

**What was verified, and how.** After publishing, all 35 files were fetched back *using only the read key above* — the exact credential a reader holds — and scanned. No occurrence of the original passphrase, the new passphrase, the old vault id, or any `sgit_vk1_` / `sgit_private_vault_` / `delete_auth` string. The broad secret scan across API-key, bearer-token and private-key patterns is clean too.

**On the data.** Both profiles are synthetic and say so in their own files: `profile_id: demo-alex`, `vault_commit: "simulated"`, first names only, and a postcode *area* (SW1, M1) rather than a postcode. The test-lab submissions are labelled *Test Patient (lab)*, age 99. No real person's health data is published here — which is the difference between this vault and Supplement Stack, and worth stating rather than leaving to be assumed.

**One defect found, and it is not ours.** The patient app throws `Uncaught ReferenceError: loadStandard is not defined` on load: `patient/app/data.js` calls it at line 116, while `patient/app/app.js` defines it at line 9 — a load-order race. It is pre-existing, not introduced by the sanitising: `patient/index.html` is byte-identical between the original clone and this republication. The app still renders and runs, and the error is left as found rather than quietly patched, because this page publishes someone else's vault and the fix is theirs to make.

The rule that goes with any published key applies here too: **revocation is not retroactive.** Anybody who fetches these objects keeps them, and rotating the key protects future commits only.

## Derived facts

35 files · 1,224 KB · 3 commits · HEAD `obj-cas-imm-4c5c2c178517` · app entry `home/index.html` · 12 JSON, 9 HTML, 9 JS, 3 markdown, 2 CSS — derived from the read key alone by `admin/build/catalogue_derive.py`, the same derivation that populates [the catalogue](../../../catalogue/index.md), with no token and no clone.


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/health-score/index.html)*
