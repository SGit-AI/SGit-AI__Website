# Local evidence log, live local stories kept as evidence, sgit.ai

> A vault for the moments when a local public service is running badly and nothing a local person could check says so: evidence by level, fourteen claims and what would resolve them, twenty six sources and how each was reached, the leads that do not fit, sixteen places a local could look, the enquiry to the trust, and scheduled re-checks. First incident: reported IT disruption at two London hospitals on 8 October 2026. Published with its read key.

*Source: <https://sgit.ai/demos/vaults/local-evidence-log/index.html> · site v0.7.24 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../index.md) / Local evidence log

# Local evidence log: live local stories, kept as evidence

A vault for the moments when a local public service is running badly, the people affected find out on the spot, and nothing they could have checked beforehand says so. It keeps the evidence by level, from heard second-hand to independently corroborated; the claims and what would resolve each; every source and how it was accessed; the leads that do not fit, with their real dates; the enquiries, sent or not; and regular re-checks of the public sources. Its first incident is reported IT disruption at two London hospitals on the afternoon of 8 October 2026. It was published with the article [The waiting room knew first](../../../articles/the-waiting-room-knew-first.md).

The overview, as the app opens.

**Open it yourself. The key is the whole credential.**
 Read key: `sgit_public_read_4900050df2cd015ca92b35898b328c4ebd35818d4dc3170e6bc2f1a72bdbadd4:92yb24y9`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_public_read_4900050df2cd015ca92b35898b328c4ebd35818d4dc3170e6bc2f1a72bdbadd4%3A92yb24y9) · From the CLI: `sgit clone sgit_public_read_4900050df2cd015ca92b35898b328c4ebd35818d4dc3170e6bc2f1a72bdbadd4:92yb24y9`
Published deliberately under the `sgit_public_read_` prefix, and **derived** one-way from a vault key kept in the gitignored tier and never published. Classified with `check_credential.py` before it touched this page, read back with the published key alone by `catalogue_derive.py`, and verified with an all-zeros read key as the negative control.

## See it live, here

The vault opens as an app: the incident, the timeline, the claims, the sources, the leads that do not fit, where a local could look, the enquiries, the re-checks, the method, and every file with a download button. You can also [**open it in the official UI**](https://dev.vault.sgraph.ai/#sgit_public_read_4900050df2cd015ca92b35898b328c4ebd35818d4dc3170e6bc2f1a72bdbadd4%3A92yb24y9).

## The one idea

When a local service is running badly, the people inside know first, and the people about to set off cannot find out. This log does not try to name and shame anyone. It asks one question, for any hospital, council or operator: where is the source of information for a local person? It answers with evidence, separated by what it can establish, and keeps asking: the sources are re-checked, the enquiry is logged when it is sent and when it is answered, and the status changes only when the evidence does.

## What is in it

claims

### Fourteen claims, by what the evidence supports

One verified: both hospitals are run by Imperial College Healthcare NHS Trust. Two supported first-hand: staff at both sites said the IT systems were down, and a wait of about five hours was announced. The rest are plausible, unresolved, unknown, or not established, among them a national outage, a named failed system, a cyber attack and a recovery. Each claim carries its evidence and what would resolve it.

A status says what the evidence supports, not whether a claim is true.

sources

### Every source, and how it was reached

Twenty six sources from the research, each marked fetched, indexed only, blocked, behind a login, or attempted. The regulator's records, the trust's own announcement of shared IT across four north-west London trusts, the NHS service desk portals that need a login, and the neighbouring trusts' homepages. Blocked is a limit of our access, never evidence about the hospital.

The register, filterable by access outcome.

where could a local look?

### Sixteen places, and whether any is live

Northern Ireland publishes live median waits for every emergency department; Wales has a live service; one English trust's own page is shown as an example; England nationally publishes monthly. The trust's own website, its social account, community groups, outage trackers that track websites rather than wards, comparisons from Alberta, New South Wales and Queensland, and the legal duty to warn and inform, with its limits.

None of the sixteen was found to carry anything about this incident.

enquiries

### The question to the trust, drafted, not yet sent

A short request to the trust's press office: which service failed, the incident reference, start time and recovery, which sites, what "national" meant, whether the redirection was related, and where a patient could have found a notice. The author's agent will send it; the date sent, and the answer, will be logged here. A second entry records the plan to ask clinicians the author knows, who are not named.

Status: drafted, not sent.

checks and method

### Re-checked on a schedule, by a written method

`tools/check_sources.py` fetches each public source anonymously and records the status, a hash of the page and keyword counts; the first run, at 22:37 BST, is in the vault, and later runs will show what changed. The method defines six evidence levels and the logging rules: write down the time, who said it and in what words; separate the observation from the explanation; never log patient details; date-check every lead; and treat "not found" as a result.

The evidence levels and the logging rules.

## How it is built

The records are hand-written JSON, one folder per incident, against shared lists of levels, statuses and access outcomes in `records/method.json`. `tools/build.py` validates every record, every reference, and the privacy and wording rules, and writes the index the app reads; `tools/bundle.py` packs the app into one `index.html`; `tools/gate.py` runs sixteen checks, including that the index and the bundle rebuild byte for byte, that no file holds a family word, an age, a condition, a credential or an em-dash, and that every view renders at desktop and phone widths with no errors and no network requests. The app uses the design system of the [agency scale](../agency-scale/index.md) and [hope or enforcement](../hope-or-enforcement/index.md) vaults. A new incident is a new folder, from the template in the method.

## The audit, honestly

**What was scanned.** Every file before the first commit, and every file again after cloning with the published read key alone: vault-key shapes, every `sgit_` credential prefix, private-key headers, cloud key shapes, the SG/Send access token and the vault's own key. The clone matched the source, file by file.

**What was found.** Nothing. The negative control, an all-zeros read key against the same vault id, returned nothing.

**Privacy.** The patient, their relationship to anyone and their condition are not in the vault, and a gate check refuses the words that would describe them. The observer is "the companion". Staff and the doctor are not named or described. The press office address in the enquiry is the trust's published contact.

**What it does not claim.** It does not claim a national outage, a cause, a cyber attack, or a recovery. It does not claim that the trust hid anything; no evidence of that was found. A fetch result is a fact about what our client could retrieve, not about the hospital's systems.

**Write-key status:** escrowed, in the gitignored credential tier, before this page was written.

## Derived facts

From `admin/build/catalogue_derive.py 92yb24y9 <read key hex>`, read-only, no token, no clone.

- **Files:** 54 · **plaintext size:** 927 KB
- **Commits:** 3 · **last updated:** 2026-10-08 · **HEAD:** `obj-cas-imm-5edc53908c0f`
- **Top level:** `PUBLIC.md`, `README.md`, `REALITY.md`, `app.json`, `app/`, `checks/`, `data/`, `index.html`, `records/`, `tools/`, `versions/`
- **File types:** .json ×17, .js ×14, .css ×13, .md ×4, .py ×4, .html ×2
- **Vault app:** yes, entry `index.html` · **browser-renderable:** yes

## Notes

**Where this came from.** An afternoon at two London hospitals, a research report written that evening, a voice memo by Dinis Cruz, and the site's fictional [Mill Street Bridge](../bridge-simulation/index.md), of which this is the live counterpart.

**Who wrote this.** [agent@riskmandate.ai](mailto:agent@riskmandate.ai) (Claude Opus 5.5, `claude-opus-5-5`), in the sgit.ai site session, for RiskMandate.ai and sgit.ai. AI-generated text, disclosed as Article 50 of the EU AI Act asks; the person with editorial responsibility is Dinis Cruz. Replies to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

[← All published vaults](../index.md)


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/local-evidence-log/index.html)*
