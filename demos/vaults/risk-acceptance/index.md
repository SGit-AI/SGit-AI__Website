# Risk Acceptance Office, a business plan with one risk replayed, published as a vault

> A business plan for a company that runs the risk acceptance loop in the gaps of an organisation's GRC platform: every material risk established on facts, held by a named person, accepted for a stated interval, and at expiry accepted again, escalated, funded or fixed. Opens on ten principles and a six-week replay of one invented risk with a hash-chained decision record verified in the browser, then the operating model, services priced per material risk, a calculator, go-to-market, the risks and the open questions.

*Source: <https://sgit.ai/demos/vaults/risk-acceptance/index.html> · site v0.6.5 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../index.md) / Risk Acceptance Office

# Risk Acceptance Office, a business plan with one risk replayed

A business plan for a company that runs the risk acceptance loop for organisations: every material risk established on facts, held by a named person, accepted for a stated interval, and at the end of that interval accepted again, escalated, funded or fixed. It works in the gaps of the client's existing GRC platform, and keeps each material risk's evidence and decisions in a vault of its own. The vault opens on the principles, then replays one invented risk over six weeks, then sets out the business. The foundation is argued in [Every risk is already accepted](../../../articles/every-risk-is-already-accepted.md).

**Open it yourself. The key is the whole credential.**
 Read key: `sgit_public_read_3e6f04360f083cff58daa851a63d6d0fcc7f6eadb5bdca7c57acef6ef15bc93e:odn10gfp`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_public_read_3e6f04360f083cff58daa851a63d6d0fcc7f6eadb5bdca7c57acef6ef15bc93e%3Aodn10gfp) · From the CLI: `sgit clone sgit_public_read_3e6f04360f083cff58daa851a63d6d0fcc7f6eadb5bdca7c57acef6ef15bc93e:odn10gfp`
Published deliberately under the `sgit_public_read_` prefix, and **derived** one-way from a vault key kept in the gitignored tier and never published. Classified with `check_credential.py` before it touched this page, and verified with an all-zeros negative control: the real key cloned 32 files, identical to the source folder, and the control cloned nothing.

## See it live, here

The replay opens as an app. Drag the slider and follow the risk from the facts that establish it to the facts that end it. You can also [**open it in its own window ↗**](https://dev.vault.sgraph.ai/#sgit_public_read_3e6f04360f083cff58daa851a63d6d0fcc7f6eadb5bdca7c57acef6ef15bc93e%3Aodn10gfp).

## What is in it

the principles

### Every risk is already accepted

The app opens on ten principles, drawn from the method published on risks.sgit.ai, RiskMandate.ai and graphs.sgit.ai: no deny button; accept, fund or fix; the interval is the decision; a named person and no delegation; unaccepted is critical; every path ends at the board; accepted is not acceptable; established by facts and ended by facts; and GRC validates while the business accepts.

The method in ten principles.

escalation

### An acceptance that expires, and the risk that moves up

An invented payments company lets a deployment agent change its production ledger. The SRE lead accepts the risk for two weeks, with an action. The action is not done, the acceptance expires, nobody renews it, and on day 15 the risk rolls up to the platform owner, who must accept, fund or fix.

Day 15: escalated to the platform owner.

the interval is the decision

### A funded month, then a four-hour incident

The platform owner funds a four-week project and accepts for a month, the default rung. On day 24 the risk materialises: an irreversible migration stalls settlement. A four-hour acceptance follows, which is an incident response by definition, and the incident's timeline becomes a fact in the risk's own record.

Day 24: the incident, as a four-hour acceptance.

ended on facts

### The risk ceases when the fact that ends it holds

On day 41 the approval step is merged. One of the facts the risk named as ending it now holds, with its source, and on day 42 it ceases. Underneath, the same moment in a typical register row: "Open until the committee on 12 December", no evidence attached. That difference is the air gap.

Day 42: ceased, on evidence.

the business

### A service, priced per material risk

A free one-hour acceptance audit, a foundation engagement at £18,000 for one business unit, the Acceptance Office at £2,500 a month plus £60 per material risk, incident support by the day, and a partner licence for consultancies. A calculator lets every input move. Every price is marked as a hypothesis.

What you sell.

## What this vault demonstrates

| Feature | The mechanism, not the marketing |
|---|---|
| **A risk as its own record** | The risk's facts, controls, holders and decisions live in `risk/`, and the decision record is fourteen hash-chained entries in `risk/record.jsonl`. It is the shape of a vault per material risk, which the plan proposes for every material risk a client carries. |
| **A record verified in your browser** | The app recomputes the chain with the browser's own crypto and prints the head. `tools/verify-record.py` does the same offline. It passed inside the vault host's sandbox. |
| **The air gap, shown side by side** | At every step the app shows what a typical register row says next to what the risk's record holds. The row never learns that the risk was accepted twice, expired, escalated, funded, materialised and ended. |
| **An app with nothing requested** | `app.json` declares `"permissions": {}`. No LLM, no writes, no network. |
| **A plan written for another operator** | Eleven plan documents, the acceptance record and risk vault specifications, and three prototypes: the acceptance audit, the acceptance meeting, and a GRC integration outline. |

## The audit, honestly

**What was scanned.** Every one of the 32 files, from a clone made with the published read key alone, compared byte for byte with the source folder. Patterns: vault-key shapes, every `sgit_` credential prefix, API-key shapes, private-key blocks, bearer tokens, and any email address not on the reserved `.example` domain.

**What was found.** Nothing. The company, people and risk are invented. The negative control, an all-zeros read key against the same vault id, produced an empty directory.

**What the research found, and the plan says.** The published method disagrees with itself in four places: two different interval ladders, whether an unaccepted risk rolls up automatically or waits, what happens at expiry, and a present-tense description of a product queue that the method's own inventory says is not built. The plan picks one position on each, says which, and lists the rest as open questions.

**Write-key status:** escrowed, in the gitignored credential tier, before this page was written.

## Derived facts

From `admin/build/catalogue_derive.py odn10gfp <read key hex>`, read-only, no token, no clone.

- **Files:** 32 · **plaintext size:** 673 KB
- **Commits:** 3 · **last updated:** 2026-09-24 · **HEAD:** `obj-cas-imm-b89dfa86528d`
- **Top level:** `PUBLIC.md`, `README.md`, `app.json`, `content.json`, `diagrams/`, `index.html`, `plan/`, `prototypes/`, `risk/`, `spec/`, `tools/`
- **Vault app:** yes, entry `index.html` · **browser-renderable:** yes

## Notes

**Where this came from.** A voice memo by the founder on 24 September 2026: risk acceptance deserves a company of its own, separate from RiskMandate.ai's focus on the insurability of agents, delivered as a governance service that works in the gaps of existing GRC platforms, with a vault per material risk as its evidence pack. **Where it sits.** With the other [business plans published for founders](../../../startups/business-plans.md).

[← All published vaults](../index.md)


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/risk-acceptance/index.html)*
