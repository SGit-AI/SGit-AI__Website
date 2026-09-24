# Company X-Ray, a business plan with one company X-rayed, published as a vault

> A business plan for a service that reads a company's own documents together: the customer drops them into an encrypted vault, agents run a catalogue of twelve analyses, a person reviews, and the customer gets back their questions answered, a board pack, findings tied to the file and row they rest on, and a Claude setup to keep asking. No connectors or integrations. One invented company X-rayed end to end with fourteen findings and a script that re-runs every figure, four levels from £50 to £1,500 on the RiskMandate pattern, a calculator, the prompts and the plan.

*Source: <https://sgit.ai/demos/vaults/company-xray/index.html> · site v0.6.8 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../index.md) / Company X-Ray

# Company X-Ray, a business plan with one company X-rayed

A business plan for a service that reads a company's own documents together. The customer drops them into an encrypted vault: management accounts, customer and supplier lists, board minutes, the plan, a complaints log. Agents run a catalogue of analyses across them and a person reviews the result. Within five working days the customer gets back their own questions answered, a one-page board pack, findings that each name the file and row they rest on, and a Claude setup so the team can keep asking questions of the same documents. There are no connectors, no integrations and no access to the customer's systems. It sells in four levels, from £50 to £1,500, on the pattern RiskMandate.ai already uses.

The whole service: an agent platform, a vault, and the customer's own documents. Nothing else.

**Open it yourself. The key is the whole credential.**
 Read key: `sgit_public_read_6da900d8edd0abd580452a85f6bbe588474cecf21e5f7cbbbbad57d1bf228454:ukpqjkly`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_public_read_6da900d8edd0abd580452a85f6bbe588474cecf21e5f7cbbbbad57d1bf228454%3Aukpqjkly) · From the CLI: `sgit clone sgit_public_read_6da900d8edd0abd580452a85f6bbe588474cecf21e5f7cbbbbad57d1bf228454:ukpqjkly`
This key is published on purpose, under the `sgit_public_read_` prefix. It is **derived** one way from a vault key that is kept in the gitignored tier and never published. `check_credential.py` classified it before it was put on this page. It was then tested with an all-zeros key as a control: the real key cloned 60 files, identical to the source folder, and the all-zeros key cloned nothing.

## See it live, here

The plan opens as an app. Pick any finding, then open any line of its evidence to see it highlighted in the document it came from. You can also [**open it in its own window ↗**](https://dev.vault.sgraph.ai/#sgit_public_read_6da900d8edd0abd580452a85f6bbe588474cecf21e5f7cbbbbad57d1bf228454%3Aukpqjkly).

## What is in it

the customer's questions

### Answered first, in plain words

An invented cleaning and maintenance company, Northgate Facilities, sent twelve documents and three questions. Why is profit down when revenue is up? How exposed are we to our largest customer? What should the board be looking at that it is not? The X-ray answers those three first, and each answer points to the findings behind it.

The three questions, and the findings each answer rests on.

evidence

### Every finding names the file and the row

There are fourteen findings. Each carries one of three labels. *Read* means it is stated in a document the customer sent. *Computed* means it is arithmetic on their data, and `tools/recompute.py` re-runs all 46 figures from the documents and checks them. *Inferred* means it is a reading of several documents together, and should be checked before anyone acts on it. In this finding, £1.5m of contracts reach their notice date two weeks before the next board meeting.

A finding, with its evidence opened in the customer's own file.

documents read together

### What nobody set side by side

The most useful findings come from reading one document against another. The minutes describe the largest customer as "strong", while the complaints log shows that customer's complaints nearly tripled. The price list is older than two wage rises. The same half-hour action was carried forward at three board meetings in a row.

One action, carried forward three times, highlighted in the minutes.

keep asking

### A Claude setup, so the conversation continues

A report gets read once, but a setup keeps being used. The delivery includes project instructions, a list of the files to upload and twelve questions to start with. The team can keep asking questions of the same documents under the same rules about evidence. Claude Projects are available on every plan, including free accounts, and the same files work in a ChatGPT Project.

The project instructions the customer pastes into Claude.

the numbers

### A couple of hours with each customer

A Standard X-ray takes about three and a half hours of a person's time, with thirty minutes of it spent with the customer. A Tailored one takes about nine, including two hours with the customer. That works out at £135 to £165 an hour for the reviewer. Two founders break even at around eleven Standard and three Tailored X-rays a month. The calculator lets every input move, and every number is marked as a hypothesis.

A month, with every input on a slider.

## Four levels, the RiskMandate way

Each level is the level below it plus exactly one thing, as on RiskMandate.ai's pricing page.

| Level | Price | What it is | Done when |
|---|---|---|---|
| **The sample** | Free | This vault: an invented company X-rayed end to end, plus the catalogue and the prompts. | You have read it. |
| **The kit** | £50 | The catalogue, the self-run prompt, the intake checklist and the Claude setup, as files. You run it. | The download's hash matches the published hash. |
| **Your X-ray vault** | £150 | The kit as a vault set up for your company, versioned and shareable read-only. You run it. | You have opened it with your key. |
| **Standard X-ray** | £500 | We run the catalogue on your documents, a person reviews every finding, and a thirty-minute call hands it over. Five working days. | The X-ray and the review note are committed to your vault. |
| **Tailored X-ray** | £1,500 | Two one-hour sessions, up to three analyses written for your questions, and a sign-off with a reviewer's name and the date. | Both sessions are held and the sign-off is committed. |

Next to these sit the **Re-X-ray**, at £350 or £900, for when the next quarter's numbers are in. It lands in the same vault, so the difference between the two X-rays is a diff. There is also a **partner licence** at £250 a month plus £100 per X-ray, for accountants and fractional finance directors who already hold their clients' documents. The first two levels are the vault without customisation, and the last two are the vault with it.

## What is reused, and what exists today

| Piece | Where it comes from |
|---|---|
| **The four levels, "done is a commit", free examples first, the prompt free on purpose, reviewer sign-off** | [RiskMandate.ai's pricing](https://riskmandate.ai/pricing.html) and its [reviewed level](https://riskmandate.ai/abp-reviewed.html), reused as they stand. Read, computed and inferred stand in for RiskMandate's measured, documented and derived. |
| **A vault per customer** | An sgit vault, encrypted on the device, versioned, with read-only keys for sharing. The host holds ciphertext only. |
| **The agents** | Claude Code, or any agent that can run `sgit` and Python, using the run prompt in `prototypes/run-the-xray.md`. |
| **The handover** | Claude Projects, or ChatGPT Projects. Sharing a Claude project with colleagues needs a Team or Enterprise plan. |
| **Business terms for the model** | By default, Anthropic does not use inputs or outputs from its commercial products, such as Claude for Work and the API, to train models. The plan says to check the terms before the first customer and to state them on the intake page. |

## Who adds what

The customer adds most of the value: the documents, the context and the questions. The model makes the price possible, because it reads everything and does the arithmetic at speed, and it is available to everybody. The operator adds four things. First, the catalogue: which questions to ask of which documents. Second, the discipline of evidence and labels. Third, the review. Fourth, the packaging, meaning the vault, the board pack and the Claude setup. That is why the price is modest and the method is given away. The review, and the catalogue getting better with every customer, are what a competitor cannot copy in a week.

## The audit, honestly

**What was scanned.** All 60 files, taken from a clone made with the published read key alone and compared byte for byte with the source folder. The scan looked for vault-key shapes, every `sgit_` credential prefix, API-key shapes, private-key blocks, bearer tokens and email addresses.

**What was found.** Nothing. The company, its people, customers, suppliers and numbers are invented, and the vault contains no email addresses at all. The only public facts are the National Living Wage rates, cited to gov.uk. The negative control, an all-zeros read key against the same vault id, produced an empty directory. `tools/recompute.py` was re-run inside the clone, and all 46 figures matched.

**What the plan says about its own risks.** An inferred finding can be wrong, so every one is labelled and a person reads it against its evidence. The documents will contain some personal data even after the intake checklist, so the operator is a processor and needs an agreement and a deletion record. An X-ray describes documents and is not accounting, legal or financial advice, and the plan says so to every customer.

**Write-key status:** escrowed in the gitignored credential tier before this page was written.

## Derived facts

From `admin/build/catalogue_derive.py ukpqjkly <read key hex>`, read-only, no token, no clone.

- **Files:** 60 · **plaintext size:** 710 KB
- **Commits:** 3 · **last updated:** 2026-09-24 · **HEAD:** `obj-cas-imm-ef1f1e4d99b7`
- **Top level:** `PUBLIC.md`, `README.md`, `app.json`, `content.json`, `diagrams/`, `index.html`, `plan/`, `prototypes/`, `sample/`, `spec/`, `tools/`
- **Vault app:** yes, entry `index.html` · **browser-renderable:** yes

## Notes

**Where this came from.** A voice memo by the founder on 24 September 2026. It was written for another entrepreneur who wants to build and run this service, and it is published for anyone else who does. **Where it sits.** Alongside the other [business plans published for founders](../../../startups/business-plans.md). An X-ray often writes down a risk for the first time. The next steps for acting on those risks are published beside it: [RiskMandate.ai](https://riskmandate.ai/) for the AI tools a company runs, and the [Risk Acceptance Office](../risk-acceptance/index.md) for holding each material risk with a named owner.

[← All published vaults](../index.md)


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/company-xray/index.html)*
