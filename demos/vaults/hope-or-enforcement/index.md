# Hope or enforcement, the Agent Behaviour Policy at work on a customer service agent, sgit.ai

> One customer service mandate for a fictional shop, built three ways: one model with connectors, a harness of business tools, and a team of narrow agents behind a deterministic gateway. Sixty-two emails through each, every policy rule marked by what enforces it, the share that is hope, the analyst's report after the run, the client's promises and a recomputable year. Published with its read key.

*Source: <https://sgit.ai/demos/vaults/hope-or-enforcement/index.html> · site v0.7.24 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../index.md) / Hope or enforcement

# Hope or enforcement: one customer service agent, three designs, and who keeps each promise

A simulation of the Agent Behaviour Policy at work. One mandate for a customer service agent at a fictional UK homeware shop; three designs of the agent: one model with two connectors, the same model behind a harness of business tools, and a team of narrow agents behind a deterministic identity gateway; sixty-two fictional emails, sixteen of them hostile, run through all three. Every rule in every policy is marked by what enforces it, so the share that is hope, a rule only the model keeps, can be counted. It was published with the article [Hope or enforcement](../../../articles/hope-or-enforcement.md).

The overview, as the app opens.

**Open it yourself. The key is the whole credential.**
 Read key: `sgit_public_read_21c37a5a4b730d351a5de1d8c3fc9dfc59de8b14e7328f1b0ef64a9a81ad49fe:wz9dw0m5`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_public_read_21c37a5a4b730d351a5de1d8c3fc9dfc59de8b14e7328f1b0ef64a9a81ad49fe%3Awz9dw0m5) · From the CLI: `sgit clone sgit_public_read_21c37a5a4b730d351a5de1d8c3fc9dfc59de8b14e7328f1b0ef64a9a81ad49fe:wz9dw0m5`
Published deliberately under the `sgit_public_read_` prefix, and **derived** one-way from a vault key kept in the gitignored tier and never published. Classified with `check_credential.py` before it touched this page, read back with the published key alone by `catalogue_derive.py`, and verified with an all-zeros read key as the negative control.

## See it live, here

The vault opens as an app: the mandate, each design with its flow, tools and policy, a comparison, the mailbox with every email through every design, the analyst's report after the run, the tokens, the client's promises, and a year you can recompute with your own assumptions. You can also [**open it in the official UI**](https://dev.vault.sgraph.ai/#sgit_public_read_21c37a5a4b730d351a5de1d8c3fc9dfc59de8b14e7328f1b0ef64a9a81ad49fe%3Awz9dw0m5).

## The one idea

In principle every design has a rule for every behaviour. The difference is who enforces each rule, and how much the agent can reach. The [Agent Behaviour Policy](https://abp.sgit.ai/) records, for every capability, what stands in the way: nothing; an expectation, a rule in prose enforced by nobody; a setting the agent's own account could flip; or a boundary enforced above the grant, out of the agent's reach. Its test: "A control bounds a grant only if it is enforced by something the grant does not include." Refactor the agent so that its reach shrinks, and the policy shrinks with it, because it no longer has to forbid what the agent cannot do.

## What is in it

three designs

### The same mandate, built three ways

**Design 1** connects one model to the whole mailbox, with Google's broadest mail scope, and to a read-write database role, with a careful 38-rule policy: 37 of the rules are expectations. **Design 2** puts the model behind fourteen business tools with some limits in code: six rules become boundaries, sixteen stay expectations. **Design 3** is a code gateway that binds each run to one verified customer, then nine narrow agents with tools that take no customer argument: 27 of 35 rules are boundaries, and the largest single policy is 70 words.

Design 3: the grant equals the mandate, and nothing outside it is in reach.

compare

### Twenty-five actions, three grants

Every action in the ABP's verb.object.reach shape, with its undo class, and for each design whether it is granted and what stands in the way. The excess falls from twelve actions to seven to none; the mandated limits that rest on hope stay at six in the first two designs and fall to none in the third.

Side by side, action by action.

the mailbox

### Sixty-two emails through every design

Forty-six ordinary emails across thirteen query types and sixteen hostile ones: injected instructions, impersonation, a request for another customer's address, a phishing link, a fake supplier changing bank details, a compromised customer mailbox and voucher farming. For each email and design: what handles it, the tokens it costs, and for the hostile ones what could happen if the model were fooled, and what held.

A compromised mailbox: the one kind of attack that works inside the mandate.

what is left

### The policy finds what the refactor missed

Two hostile emails still get somewhere in Design 3, because they use the mandate itself. The policy is the map of what still rests on hope, and for each line the boundary to build next: confirm a new address by email, cap automatic refunds and vouchers per customer, require an image for a damage claim, and keep tone and accuracy as an expectation, sampled by a person.

What the policy still says, and the boundary to build next.

after the run

### How did the policy survive?

The analyst's report: for each rule, how often ordinary mail exercised it, how often hostile mail tested it, and whether a boundary held or the result rested on the model, plus the rules nothing used. In Design 1, all 138 tests rest on the model. In Design 3, 52 of 85 are held by a boundary. Tokens are reported against the 8,000 budget: about 35,000 per email in Design 1, 7,500 in Design 2 and 4,400 in Design 3.

Design 1 after the run: every test rested on the model.

the client

### The promises, and who keeps them

Eight promises a vendor would make to the shop, and for each design the barrier behind each, in plain words. A promise is as strong as the weakest thing it rests on. Design 1 keeps none by a boundary, Design 2 one, Design 3 six. The year view recomputes the business case live as you change how often a rule in prose fails, how much mail is hostile, and what an exposed record costs.

No score: the record of who keeps each promise.

## How it is built

`tools/simulate.py` writes every data file from the tables in it: the company, the assumptions, the mandate, the designs, the mailbox, the runs, the report and the year. It is deterministic; no model is called, and the assumptions that are not facts are labelled illustrative. The app uses the same design system as the [threat-sized security](../threat-sized-security/index.md) and [bridge simulation](../bridge-simulation/index.md) vaults: four themes, a template that escapes by default, one folder per view, one bundled `index.html`. `tools/gate.py` runs twenty checks, including that the simulation reproduces the data byte for byte, that the browser's port of the year matches the Python one, and that every view renders at desktop and phone widths with no errors and no network requests.

## The audit, honestly

**What was scanned.** Every file before the first commit, and every file again after cloning with the published read key alone: vault-key shapes, every `sgit_` credential prefix, private-key headers, cloud key shapes, the SG/Send access token and the vault's own key. The clone was compared with the source, file by file, and matched.

**What was found.** Nothing. The negative control, an all-zeros read key against the same vault id, returned nothing.

**What it does not claim.** The simulation does not measure any model. Whether a hostile email gets past a rule in prose is an assumption, set by default to one in fifty and adjustable. The designs are illustrations of a pattern, not a product; the shop and its mail are invented. The ABP itself publishes the record and never a verdict, and so does this vault.

**Write-key status:** escrowed, in the gitignored credential tier, before this page was written.

## Derived facts

From `admin/build/catalogue_derive.py wz9dw0m5 <read key hex>`, read-only, no token, no clone.

- **Files:** 67 · **plaintext size:** 1,068 KB
- **Commits:** 2 · **last updated:** 2026-10-08 · **HEAD:** `obj-cas-imm-1fe1419ea9bb`
- **Top level:** `BRIEF-CORRECTIONS.md`, `PUBLIC.md`, `README.md`, `REALITY.md`, `app.json`, `app/`, `data/`, `index.html`, `tests/`, `tools/`, `versions/`
- **File types:** .js ×19, .css ×18, .json ×16, .py ×8, .md ×4, .html ×2
- **Vault app:** yes, entry `index.html` · **browser-renderable:** yes

## Notes

**Where this came from.** A voice memo by Dinis Cruz describing the three designs, and the related vault [Licence to Operate](../licence-to-operate/index.md), where an insurer prices an agent's mandate.

**Who wrote this.** [agent@riskmandate.ai](mailto:agent@riskmandate.ai) (Claude Opus 5.5, `claude-opus-5-5`), in the sgit.ai site session, for RiskMandate.ai and sgit.ai. AI-generated text, disclosed as Article 50 of the EU AI Act asks; the person with editorial responsibility is Dinis Cruz. Replies to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

[← All published vaults](../index.md)


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/hope-or-enforcement/index.html)*
