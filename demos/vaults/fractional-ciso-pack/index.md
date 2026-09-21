# The same pack, written for an archetype instead of a company, fractional CISO pack

> Sibling of vault #29 from the same generator: a fractional CISO pack that solves the publication problem by describing a type of company rather than withholding a real one. Five documents in four formats, a one-page infographic, an engagement document with a twelve-month map and a section on what two days a month is not, and the audit stated in full.

*Source: <https://sgit.ai/demos/vaults/fractional-ciso-pack/index.html> · site v0.3.4 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../index.md) / Fractional CISO application pack

# The same pack, written for an archetype instead of a company

A sibling of [vault #29](../interim-ciso-pack/index.md) from the same generator, one day later, and the interesting difference is how it solves the privacy problem. That pack described a real role and *withheld* the company. This one describes **a type of company**, derived from public sources, so there is nothing to withhold. Same three routes, same thirteen recommendations, a different argument: two days a month, on a retainer, for a business that is already certified.

**Open it yourself. The key is the whole credential.**
 Read key: `sgit_public_read_7c84275ebcbbf312dbbec4713a00c83fb0dd8520b6a52b082d7ff81e3523c40e:eaba68j5`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_public_read_7c84275ebcbbf312dbbec4713a00c83fb0dd8520b6a52b082d7ff81e3523c40e%3Aeaba68j5) · From the CLI: `sgit clone sgit_public_read_7c84275ebcbbf312dbbec4713a00c83fb0dd8520b6a52b082d7ff81e3523c40e:eaba68j5`
Submitted as a read key and published unchanged. No company is named anywhere in the vault, and none is implied, see the audit below.

The pack's own one-pager. Everything on it is also in the vault as data. The infographic is a rendering of `content.json`, not a separate document.

## See it live, here

[Open the vault in a new tab ↗](https://dev.vault.sgraph.ai/#sgit_public_read_7c84275ebcbbf312dbbec4713a00c83fb0dd8520b6a52b082d7ff81e3523c40e%3Aeaba68j5)The document viewer wants the room.

## The idea worth stealing: describe the category, not the company

Vault #29 had to be audited for whether an unnamed FTSE 250 client could be inferred from what was said about it. This pack removes the question. Its company route opens with the sentence *“this pack is written for a type of company rather than a named one”*, and then describes the type in six rows, what it does, who buys it, where the risk sits, what it already has, what it usually lacks, who governs it:

> “A venture-backed UK software company, post-Series A, somewhere between 40 and 100 people, whose product processes other people's most sensitive personal data.”

Everything after that *follows from the archetype*: third-party and sub-processor risk as the highest-value work, assurance as a revenue lever, data minimisation as a decision rather than a project. The pack says so itself: *“if the company you have in mind is different in any of these respects, the engagement below changes shape, and that conversation is a better first meeting than a pitch.”*

That is a better answer to the publication problem than redaction, and it generalises: **a document written for a class can be published; a document written for an instance has to be scrubbed.**

The company route leads with the archetype. Fourteen sections follow it, including *What it is not*, *Conflict* and *Tensions*.

## What changed from #29, precisely

|  | [#29, Interim](../interim-ciso-pack/index.md) | #30, Fractional |
|---|---|---|
| **The role** | Six months, near full-time, a dated regulatory deliverable | Two days a month, ongoing, a board advisory retainer |
| **The reader** | A specific FTSE 250 company, withheld | **An archetype**, described in six rows from public sources |
| **The company folder** | A strategy brief with a disclosed redaction | `company-archetype.md`, nothing to redact |
| **Documents** | Four, in four formats | **Five** in four formats, plus an infographic as PNG and PDF, plus the three 2019 decks rendered in the viewer |
| **New document** | none | *The engagement*: the monthly rhythm, a twelve-month map, and a section headed *What two days a month is not* |
| **Shared** | The generator, the CV facts, the thirteen recommendations, the three routes, the agentic team, and the deliberate absence of any rate or tax status |

The README states the relationship in one paragraph and ends it with the line that matters for both: *“Rates and tax status are deliberately absent from both.”*

## The section to read first is the one that says no

The engagement document's strongest passage is a list of what two days a month *is not*. Not cover, *“if something goes wrong at three in the morning, a fractional advisor is not the incident manager.”* Not a Data Protection Officer. Not delivery. Not an audit. And not a substitute for a full-time CISO once the company needs one, *“part of the job is saying when that point arrives.”*

The *Honest tensions* section goes further and names the economic one: a fractional CISO is cheaper than a permanent one, *“and that same economy can be used to defer a hire the company genuinely needs. Naming the trigger early is the only honest defence.”* A sales document that identifies how it could be misused against the buyer is rare enough to be worth pointing at.

Five documents, each as PDF, Word, Markdown and JSON; the infographic as PNG and PDF; and the 2019 decks now rendered in the viewer rather than only archived.

## The pre-publication audit

Run against a full clone with the published read key. The pack's own claim, *“no company is named anywhere in this pack … nothing here depends on inside knowledge, which is why it can be published”*: checked rather than accepted:

| Checked | Result |
|---|---|
| Company identification | **None, and none implied.** The reader is an archetype in six rows. The only company names in the vault are the candidate's past employers, from a public CV |
| Rates, fees, tax status | **Absent.***Retainer* appears as a word with no figure attached; the only monetary values are statutory penalty amounts |
| Contact details | One email address, the candidate's long-public OWASP one; the infographic adds public LinkedIn and GitHub handles. No phone, no address |
| Credentials and secrets | **None** |
| Named third parties | The same thirteen recommendations as #29, from the candidate's own 2019 CC BY-SA deck, labelled with their 2019 titles. Not reproduced on this page |
| Read key | Verified with an all-zeros negative control against the same vault id: real key 72 files, control an empty directory |

## Shape

| **Vault** | `eaba68j5` · 72 files · 19 MB |
|---|---|
| **App** | `index.html` with CSS, JS and a fallback copy of `content.json` inlined; PDF.js loaded through `sg.loadJs` inside a host, page images as the fallback |
| **Permissions** | `downloads: true`, and nothing else. No writes. The HUD hides the vault name and shows the app title |
| **Documents** | Six distinct: two CVs, the case, the recommendations, *the engagement*, and the infographic, 21 recruiter files across the formats, 18 pre-rendered page images |
| **Licence** | Content CC BY 4.0; the 2019 decks and recommendation slides CC BY-SA as originally published; PDF.js Apache-2.0 |

Published as row #30. Its sibling is [#29](../interim-ciso-pack/index.md); the two are worth reading as a pair, because they are the same machinery giving two different answers to *how do you publish a document about a job*. [← All published vaults](../index.md) · [The publishing method](../publishing.md)


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/fractional-ciso-pack/index.html)*
