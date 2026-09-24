# Connector Twin, a business plan with a working replay, published as a vault

> A business plan for a service that journals every request and response an AI agent makes through Gmail, Calendar or any connector, and replays it into the views the agent saw, with before and after and a revert plan for every change. Opens on a working replay of an invented seventeen-call session with a hash chain verified in the browser. Facts sourced from Google's documentation, the journal specification, revert rules, prototypes, packages priced per agent and a calculator.

*Source: <https://sgit.ai/demos/vaults/connector-twin/index.html> · site v0.6.3 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../index.md) / Connector Twin

# Connector Twin, a business plan with a working replay

A business plan for a service that gives every AI agent deployment a twin of its connectors: a journal of every request and response the agent makes to Gmail, Google Calendar or any other connected system, replayed into the views the agent saw, with a before and after for every change and a revert plan for each one. The vault opens on a working replay of an invented agent session, rebuilt from seventeen hash-chained journal entries, and then sets out the business. **The sales question:** do you know what your agents did? The case is argued in [Before you give an agent a connector, give the connector a twin](../../../articles/connector-twin-before-you-deploy-an-agent.md).

**Open it yourself. The key is the whole credential.**
 Read key: `sgit_public_read_4fb639e76d976d691c7655060e74f6d7fe13a7b96ea77d9230446977e5cdf860:7tkvspwp`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_public_read_4fb639e76d976d691c7655060e74f6d7fe13a7b96ea77d9230446977e5cdf860%3A7tkvspwp) · From the CLI: `sgit clone sgit_public_read_4fb639e76d976d691c7655060e74f6d7fe13a7b96ea77d9230446977e5cdf860:7tkvspwp`
Published deliberately under the `sgit_public_read_` prefix, and **derived** one-way from a vault key that is kept in the gitignored tier and never published. Classified with `check_credential.py` before it touched this page, and verified with an all-zeros negative control: the real key cloned 31 files, identical to the source folder, and the control cloned nothing.

## See it live, here

The replay opens as an app. Drag the slider and the inbox and calendar rebuild step by step. You can also [**open it in its own window ↗**](https://dev.vault.sgraph.ai/#sgit_public_read_4fb639e76d976d691c7655060e74f6d7fe13a7b96ea77d9230446977e5cdf860%3A7tkvspwp), where the replay has more room.

## What is in it

the question

### What an organisation can answer, with a twin and without

The app opens on the sales question and a six-row table: what can the agent do, what did it do, what did it see, why, can you undo it, and can you show someone else. Without a twin, most answers are the agent's own summary. With one, every answer is a record.

Every claim about what Gmail and Calendar keep comes from Google's own documentation, and the plan's facts document links each one.

Do you know what your agents did? The table, without a twin and with one.

the replay

### The inbox and the calendar, as the agent saw them

An invented scheduling assistant is given a Gmail and a Calendar connector and one instruction. Its seventeen calls are the journal. The app folds them in order into the inbox and the calendar at any step, marking what the agent archived, trashed, permanently deleted, sent, moved, declined, deleted and created, with a ghost where a moved event used to be.

The twin is not a copy of the mailbox. One message the agent listed and never opened appears as an id and nothing more, because that is all the agent saw.

The calendar as the agent left it, rebuilt from the journal alone.

before and after

### Every change, with what the twin can put back

Pick a write and the app shows the state before and after, and a grade: exact, partial, content only, or none. Step 15 is the one that matters: a payment reminder deleted with the Gmail API's permanent delete, which Google documents as "cannot be undone". The twin still holds the full message, because the agent read it before deleting it, so its content can be put back as a new message.

Step 15: permanently deleted in Gmail, still held in the twin.

said versus did

### The agent's summary, against the journal

The agent's summary is true in every sentence. The journal shows that "removed the supplier call" was a delete with notifications on, so the supplier received a cancellation, and that "deleted an old reminder" was the unpaid invoice's reminder, removed permanently. That gap is what a twin exists to close.

What the agent said, what the journal shows, and what can be put back.

the revert plan

### Newest first, side effects named

For every write up to the current step, the inverse call, newest first, with its grade and the side effect it cannot avoid: a second round of notifications, a new message id, a cancellation already sent. Executing the plan is a separate step that a person approves and that is journalled like everything else.

The revert plan, newest first, each step graded.

the business

### Priced per agent, with a calculator

A connector review once (£750, £2,500 or £6,000 by size), then per agent per month: Journal £15, Twin £40, Assured £90, and incident replays on demand. Three capture modes, broker, gateway and agent-reported, which change the evidence grade rather than the price.

The calculator moves customers, agents per customer, tier, set-up and burn. At the Twin price, about 380 agents cover a two-founder burn of £14,000 a month. Every number is marked as a hypothesis.

What you sell: set-up once, per agent monthly, and on demand.

## What this vault demonstrates

| Feature | The mechanism, not the marketing |
|---|---|
| **A replay built from a journal, not a copy** | The app holds seventeen entries, each a tool call, an upstream request and a response, and folds them into state. Nothing else is shipped: no snapshot of the inbox, no snapshot of the calendar. What you see at step nine is what the agent had seen by step nine. |
| **A hash chain verified in your browser** | Each entry carries the SHA-256 of the one before. The app recomputes the chain with the browser's own crypto and prints the head; `tools/verify-journal.py` does the same offline. It ran and passed inside the vault host's sandbox. |
| **An app with nothing requested** | `app.json` declares `"permissions": {}`, and the vault host shows it as read-only with no read or write grants. No LLM, no writes, no network. |
| **A specification to build against** | `spec/journal-entry.md` is the contract between capture and replay, including what is never captured. `spec/revert-rules.md` lists every Gmail and Calendar action in scope, what the platform keeps, the inverse, and the side effects. |
| **Facts with sources** | `plan/02-the-facts.md` links every claim about Gmail, Calendar and Google Vault to Google's documentation, and marks the one thing the plan has not tested: whether an event deleted through the API appears in Calendar's trash. |
| **Written for another operator** | Eleven plan documents with a reading order, three prototypes (the agent-reported capture instruction, the broker, and the processor schedule), and the tools to regenerate the journal and rebuild the app. |

## The audit, honestly

**What was scanned.** Every one of the 31 files, from a clone made with the published read key and nothing else, and compared byte for byte with the source folder. Patterns: vault-key shapes, every `sgit_` credential prefix, API-key shapes, private-key blocks, bearer tokens, and any email address not on the reserved `.example` domain.

**What was found.** Nothing. The journal is invented: its people, companies and addresses are fictional, every address uses `.example`, and the Authorization header is recorded only as `[never captured]`. The negative control, an all-zeros read key against the same vault id, produced an empty directory.

**What the research corrected.** The plan first assumed Google Vault did not cover Calendar; it has since November 2023, keeping the last revision of each day, and the facts now say so. It also first said Calendar keeps no record of edits; administrators have an audit log that records some earlier values, and the facts now say that too, with the distinction that a log is a record, not a restore.

**Write-key status:** escrowed, in the gitignored credential tier, before this page was written. The vault is correctable.

## Derived facts

From `admin/build/catalogue_derive.py 7tkvspwp <read key hex>`, read-only, no token, no clone.

- **Files:** 31 · **plaintext size:** 515 KB
- **Commits:** 2 · **last updated:** 2026-09-24 · **HEAD:** `obj-cas-imm-3ad848e2891f`
- **Top level:** `PUBLIC.md`, `README.md`, `app.json`, `content.json`, `diagrams/`, `index.html`, `journal/`, `plan/`, `prototypes/`, `spec/`, `tools/`
- **File types:** .md ×18, .json ×4, .py ×3, .svg ×2, .webp ×2, .html ×1, .jsonl ×1
- **Vault app:** yes, entry `index.html` · **browser-renderable:** yes

## Notes

**Where this came from.** A voice memo by the founder on 24 September 2026: a twin of what an agent can do and has done is close to a minimum requirement for deploying one, with Gmail and Calendar as the worked example, and the idea split in two, an article for the need and a business plan for the service. **Where it sits.** With the other [business plans published for founders](../../../startups/business-plans.md), each a vault, each written for somebody else to run.

[← All published vaults](../index.md)


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/connector-twin/index.html)*
