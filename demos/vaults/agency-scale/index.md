# The agency scale, seven levels of agency for anyone asked to decide, a person or an agent, sgit.ai

> Seven observable dimensions, options, context, depth, time, incentives, escalation and authority, turned into seven levels from rubber stamp to delegator, where the weakest dimension caps the decision; fourteen cases scored by the same rule, an assessment you can run on your own decision points, the review as a QA loop, and the EU AI Act's oversight requirements mapped to it. Published with its read key.

*Source: <https://sgit.ai/demos/vaults/agency-scale/index.html> · site v0.7.25 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../index.md) / The agency scale

# The agency scale: seven levels of agency for anyone asked to decide, a person or an agent

A maturity model you can run. Seven dimensions that can be observed at any decision point: options, context, depth, time, incentives, escalation and authority. A rule that turns the answers into a level from 0, the rubber stamp, to 6, the delegator, where the weakest dimension caps the decision. Fourteen cases scored by the same rule, from a prompt that asks to add label 756-459-3214 to the one email an agent of ours is allowed to send. An assessment for your own decision points, the review as a QA loop, and the law that already asks for most of it. It was published with the article [Agency is not a yes](../../../articles/agency-is-not-a-yes.md).

The overview, as the app opens.

**Open it yourself. The key is the whole credential.**
 Read key: `sgit_public_read_ed44ea7c407ba44d6b65253035e1ecb2f69f916b64c579a7feba04c7e8c49375:ddfw24hx`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_public_read_ed44ea7c407ba44d6b65253035e1ecb2f69f916b64c579a7feba04c7e8c49375%3Addfw24hx) · From the CLI: `sgit clone sgit_public_read_ed44ea7c407ba44d6b65253035e1ecb2f69f916b64c579a7feba04c7e8c49375:ddfw24hx`
Published deliberately under the `sgit_public_read_` prefix, and **derived** one-way from a vault key kept in the gitignored tier and never published. Classified with `check_credential.py` before it touched this page, read back with the published key alone by `catalogue_derive.py`, and verified with an all-zeros read key as the negative control.

## See it live, here

The vault opens as an app: the scale, the dimensions, an assessment, the cases, who carries the accountability, the law, the review loop, and every file with a download button. You can also [**open it in the official UI**](https://dev.vault.sgraph.ai/#sgit_public_read_ed44ea7c407ba44d6b65253035e1ecb2f69f916b64c579a7feba04c7e8c49375%3Addfw24hx).

## The one idea

A yes or no is not agency. A decider, human or agent, has agency when they have options beyond yes, context in their own terms, the ability to look behind what they are shown, time or tokens, incentives that treat a wrong yes and a wrong no alike, somewhere to escalate, and authority over the system that produced the request. One missing dimension caps the decision. Below level 3, what the decider carries is liability, and accountability belongs to whoever designed the decision point and up their chain. Above it, the review becomes a QA step that fixes the source, and at the top, proven cases become rules that run as code.

## What is in it

the scale

### Seven levels, and who is accountable at each

Rubber stamp, informed yes or no, can look behind it, resourced, editor, owner of the source, delegator. For each: what the decider can do, what agency it gives, what it looks like, and who carries the accountability.

From rubber stamp to delegator.

assess

### Seven questions, one level, and what would have to change

Answer seven questions about a decision point and see its level, the cap each dimension sets, the weakest one, who is accountable at that level, and exactly which answers would have to change to reach the next. The answers live in the address, so an assessment can be shared as a link, and nothing is stored or sent.

The draft review, assessed: level 5, capped by options.

cases

### Fourteen decision points on one scale

Eight sit at level 0: a label prompt, a repository prompt, approval fatigue, a sign-in push, a driver asked to take over, a sign-off that cannot change anything, a shortfall that cannot be disputed, and an agent asked "is this OK?". The fixed sign-in push reaches level 1; a defensive reviewer, level 2; a controller agent with checks and a budget, level 3; a senior clinician, level 4; a draft that is really a QA step, level 5; the one email an agent may send, level 6.

Circles are people, squares are agents.

the review loop

### A draft is a QA step, not a sign-off

Eight steps: read it as the person who will sign it, question each statement, trace where it came from, classify the gap, fix the source rather than the output, think better, record the outcome, and promote what is proven into a rule. And a table of where each kind of gap gets fixed: the brief, the record, the graph, the tool, or the objectives.

Each pass validates everything upstream.

the law

### The floor is level 3

EU AI Act Article 14(4)(a) to (e) and Article 26(2), and the guidance that oversight must be "meaningful, rather than just a token gesture", each quoted and mapped to the dimensions it touches and the level it needs. Read together, they put the floor for overseeing a high-risk system at level 3. Not legal advice.

What the law asks for, dimension by dimension.

## How it is built

`tools/model.py` writes every data file, and scores every case with the same `assess()` rule, so a case's level is computed, never typed. The app uses the design system of the [hope or enforcement](../hope-or-enforcement/index.md) and [threat-sized security](../threat-sized-security/index.md) vaults: four themes, a template that escapes by default, one folder per view, one bundled `index.html`. `tools/gate.py` runs seventeen checks, including that the model reproduces the data byte for byte, that the browser's port of the rule agrees with the Python one on every case and on all 720 combinations of answers, and that every view renders at desktop and phone widths with no errors and no network requests.

## The audit, honestly

**What was scanned.** Every file before the first commit, and every file again after cloning with the published read key alone: vault-key shapes, every `sgit_` credential prefix, private-key headers, cloud key shapes, the SG/Send access token and the vault's own key. The clone matched the source, file by file.

**What was found.** Nothing. The negative control, an all-zeros read key against the same vault id, returned nothing.

**What it does not claim.** The scale is a model for thinking and comparing, not a standard or a certification. The cases from the public record are summarised from the sources linked in the vault and in [Where is the why?](../../../articles/where-is-the-why.md); the answers given for them are this vault's reading. Two cases come from the author's own agent team.

**Write-key status:** escrowed, in the gitignored credential tier, before this page was written.

## Derived facts

From `admin/build/catalogue_derive.py ddfw24hx <read key hex>`, read-only, no token, no clone.

- **Files:** 61 · **plaintext size:** 448 KB
- **Commits:** 2 · **last updated:** 2026-10-08 · **HEAD:** `obj-cas-imm-b0fed90c672f`
- **Top level:** `BRIEF-CORRECTIONS.md`, `PUBLIC.md`, `README.md`, `REALITY.md`, `app.json`, `app/`, `data/`, `index.html`, `tests/`, `tools/`, `versions/`
- **File types:** .js ×18, .css ×16, .json ×13, .py ×8, .md ×4, .html ×2
- **Vault app:** yes, entry `index.html` · **browser-renderable:** yes

## Notes

**Where this came from.** Two voice memos by Dinis Cruz on human and agent agency, and the cases this site has already written up.

**Who wrote this.** [agent@riskmandate.ai](mailto:agent@riskmandate.ai) (Claude Opus 5.5, `claude-opus-5-5`), in the sgit.ai site session, for RiskMandate.ai and sgit.ai. AI-generated text, disclosed as Article 50 of the EU AI Act asks; the person with editorial responsibility is Dinis Cruz. Replies to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

[← All published vaults](../index.md)


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/agency-scale/index.html)*
