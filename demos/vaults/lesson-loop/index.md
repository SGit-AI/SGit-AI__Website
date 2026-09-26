# Lesson Loop, a business plan for coaches with one player's record, published as a vault

> A workflow and a business for padel coaches and any teacher with students: the coach records a voice memo at the end of the lesson, an agent turns it into a lesson note in the player's own vault, the player adds match notes, and the next coach starts from a two-minute briefing. One invented player's record across four lessons with three coaches, the themes each saw, phases, the two-vault architecture with write-only lanes for coaches, pay-on-demand credits, new coach income, a calculator, and the prompts for phase one.

*Source: <https://sgit.ai/demos/vaults/lesson-loop/index.html> · site v0.6.10 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../index.md) / Lesson Loop

# Lesson Loop, a business plan for coaches with one player's record

A workflow and a business for padel coaches, and for any teacher with students. At the end of every lesson the coach has the best picture of the player they will ever have, and today it is gone by the next lesson. Lesson Loop captures it at that moment: the coach records a two-minute voice memo, an agent turns it into a lesson note in the player's own vault, the player adds what happens in their games, and the next lesson, with the same coach or a different one in another city, starts from a two-minute briefing instead of from memory. Paid on demand, with new income for coaches beyond the hour on court.

The lesson loop. Phase one is only the top row: a voice memo, an agent and a vault.

**Open it yourself. The key is the whole credential.**
 Read key: `sgit_public_read_2d397a3a06c235452300c55375ebe8e470ba70a1a5263dc72679f8a78c42dfc1:3s9q7zl7`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_public_read_2d397a3a06c235452300c55375ebe8e470ba70a1a5263dc72679f8a78c42dfc1%3A3s9q7zl7) · From the CLI: `sgit clone sgit_public_read_2d397a3a06c235452300c55375ebe8e470ba70a1a5263dc72679f8a78c42dfc1:3s9q7zl7`
Published deliberately under the `sgit_public_read_` prefix, and **derived** one-way from a vault key kept in the gitignored tier and never published. Classified with `check_credential.py` before it touched this page, and verified with an all-zeros negative control: the real key cloned 27 files, identical to the source folder, and the control cloned nothing.

## See it live, here

The plan opens as an app. Pick any entry in the player's record. You can also [**open it in its own window ↗**](https://dev.vault.sgraph.ai/#sgit_public_read_2d397a3a06c235452300c55375ebe8e470ba70a1a5263dc72679f8a78c42dfc1%3A3s9q7zl7).

## What is in it

the moment

### The coach's memo, as spoken

An invented player, Alex, takes four lessons with three coaches in two cities over three weeks, and plays in between. For each lesson you can read the coach's end-of-lesson voice memo exactly as spoken: two or three minutes of what they saw, what they worked on and what comes next. This is the knowledge that exists for five minutes and is normally lost.

The first lesson's memo, as recorded.

the player's view

### Three things for the next games

The agent turns the memo into a lesson note and a player view: no more than three points to take into the next game, written to the player, and the drills to practise. Instead of an hour of instructions to remember, the player has three sentences on their phone.

What the player sees after lesson one.

the briefing

### Two minutes before the next lesson

Before each lesson the coach reads a briefing that folds together every coach's notes and every match since they last saw the player. In the demo, the coach in Lisbon says it saved the first fifteen minutes, and a new coach in London starts her first lesson already knowing what three coaches saw.

The briefing for the player's regular coach.

three coaches

### Every coach sees something different, and none of it is lost

The agent tracks themes across the record. The London coach fixed the bandeja; the Lisbon coach saw that the lob came from the arm and that the player stayed back after a good lob; the second London coach confirmed both. Amber is where something was first seen or is still a problem, green is where it holds.

Themes across three coaches, two matches and a clip.

the business

### Paid on demand, and new income for coaches

No subscription. Players buy credits and spend them on processing: about 20p for a lesson note, about £1 for a short clip. Coaches price their own remote reviews, drill plans, follow-ups and content, and the operator takes a share. Clubs can include notes in the lesson price. The calculator shows it is a small business at 200 coaches and a real one at a few thousand, and every number is a hypothesis.

What is sold, and who sets the price.

## How it is built

Two vaults: one app for everybody, one record per player. The record belongs to the player, so it travels.

| Piece | What exists today |
|---|---|
| **Voice capture** | Claude and ChatGPT apps take voice input, and transcription apps such as Otter record and transcribe. Phase one needs nothing else on the coach's side. |
| **An agent to process it** | The same assistant, with the prompt in the vault's `prototypes/coach-memo-prompt.md`, ready to paste. |
| **A record the player holds** | An sgit vault per player, encrypted on the device and versioned. [Supplement Stack](../supplement-stack/index.md) and [Health Score](../health-score/index.md) are published examples of records a person holds, with a professional's view. |
| **Write-only lanes for coaches** | [Append lanes](../../../api/append-lanes.md): a coach can add a memo, and cannot read the other lanes or change anything. |
| **Apps that call a model without a key** | The `sg.llm` bridge, documented on [llms.sgit.ai](https://llms.sgit.ai/). |
| **Easy key handling** | Open. It is the subject of [the call for collaboration on vault key management](../../../partnerships/vault-key-management.md). |

## Beyond padel

The loop fits wherever one person teaches another in sessions and knows most about the student at the end of each one: tennis, squash and pickleball, golf, music lessons, language tutoring, personal training and physiotherapy, driving instruction, climbing and swimming. The pieces do not change; each domain needs its own note template and its own themes.

## The audit, honestly

**What was scanned.** Every one of the 27 files, from a clone made with the published read key alone, compared byte for byte with the source folder. Patterns: vault-key shapes, every `sgit_` credential prefix, API-key shapes, private-key blocks, bearer tokens, and email addresses.

**What was found.** Nothing. The player, coaches and clubs are invented, and the vault contains no email addresses at all. The negative control, an all-zeros read key against the same vault id, produced an empty directory.

**What the plan says about its own risks.** Many students are children, so the plan keeps to adults until consent and a guardian's key are designed. Match clips show other players, so clips stay with the coach. Coaches' kit recommendations must declare any commercial interest, and the demo shows one that does.

**Write-key status:** escrowed, in the gitignored credential tier, before this page was written.

## Derived facts

From `admin/build/catalogue_derive.py 3s9q7zl7 <read key hex>`, read-only, no token, no clone.

- **Files:** 27 · **plaintext size:** 407 KB
- **Commits:** 2 · **last updated:** 2026-09-24 · **HEAD:** `obj-cas-imm-3e90049fe51f`
- **Top level:** `PUBLIC.md`, `README.md`, `app.json`, `content.json`, `diagrams/`, `index.html`, `plan/`, `player/`, `prototypes/`, `spec/`, `tools/`
- **Vault app:** yes, entry `index.html` · **browser-renderable:** yes

## Notes

**Where this came from.** A voice memo by the founder on 24 September 2026, after several padel lessons in a few days with different coaches, each seeing something different. The founder already has a padel vault of their own, not yet published, where phase one will be tried first. **Where it sits.** With the other [business plans published for founders](../../../startups/business-plans.md).

[← All published vaults](../index.md)


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/lesson-loop/index.html)*
