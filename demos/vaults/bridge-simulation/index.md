# The Mill Street Bridge, a story vault simulation of one local story followed to the end, sgit.ai

> A simulation of Markus Franz's bridge example on a story vault: a fictional bridge closure from first notice to reopening, the journalism that got the date right, three readers whose graphs meet the story graph, institutions and an agent buying from it, and where every penny goes. Published with its read key.

*Source: <https://sgit.ai/demos/vaults/bridge-simulation/index.html> · site v0.6.96 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../index.md) / The Mill Street Bridge

# The Mill Street Bridge: one local story, followed to the end, as a story vault

A simulation of Markus Franz's bridge example from [The Article Is Only the Beginning](https://www.linkedin.com/pulse/article-only-beginning-markus-franz-qzyqe/), played out on a story vault from the council's first notice to the first car across. The journalism that got the date right when the council's was wrong; the paper on five dates; the timeline of a story that is newsworthy on five days and needed on fifty-seven; three readers whose own graphs meet the story graph and who decide better with it; four institutions and an agent that buy from the same graph; and where every penny goes. Everything in it is fictional.

Three readers, one story: where their graphs meet the story graph, and each other.

**Open it yourself. The key is the whole credential.**
 Read key: `sgit_public_read_cb3838a0e965dc9d5af9009fef6e867dbdf18a8fc615cb3f5f2bee5424639705:vk3jlgzb`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_public_read_cb3838a0e965dc9d5af9009fef6e867dbdf18a8fc615cb3f5f2bee5424639705%3Avk3jlgzb) · From the CLI: `sgit clone sgit_public_read_cb3838a0e965dc9d5af9009fef6e867dbdf18a8fc615cb3f5f2bee5424639705:vk3jlgzb`
Published deliberately under the `sgit_public_read_` prefix, and **derived** one-way from a vault key kept in the gitignored tier and never published. Classified with `check_credential.py` before it touched this page, read back with the published key alone by `catalogue_derive.py`, and verified with an all-zeros read key as the negative control.

## See it live, here

The vault opens as an app: the overview, the Courier on five dates, the journalism, the timeline, the story graph on any date, the readers and each reader's own page, institutions and agents, where the money goes, what happens without it, and the implications. You can also [**open it in the official UI**](https://dev.vault.sgraph.ai/#sgit_public_read_cb3838a0e965dc9d5af9009fef6e867dbdf18a8fc615cb3f5f2bee5424639705%3Avk3jlgzb).

## The one idea

A local story kept as a graph is worth something every day it matters, not only on the days it is news. The value is getting a disputed fact right and keeping it right; the readers use it through Reader Skills that answer their own situation; and because every claim names its evidence, every payment can walk back to the people who found it. The argument is in the article, [The bridge, followed to the end](../../../articles/the-bridge-followed-to-the-end.md), and the architecture in [Story vault underneath, Reader Skills on top](../../../articles/story-vault-meets-reader-skills.md).

## What is in it

the paper

### The headline is one projection

The Wendmouth Courier on the five days it led with the bridge, each front page showing the claims it projects, beside a live tracker with every source's reopening date and three buttons: what changed, does this affect me, follow.

The Courier on 15 October, and the tracker beside it.

the journalism

### One week, three weeks or six?

The council's estimate, the contract the reporter found on the procurement portal, and the independent engineer's assessment, each with its evidence and a confidence that comes from how independent the evidence is. The reporter's steps, the editor's decisions, and every piece of evidence with its hash.

The work behind the date.

the timeline

### Newsworthy on five days, needed on fifty-seven

What each source said the reopening date would be, day by day, and the days the paper led with the story against the days readers needed it. Every change, as it arrived, with what superseded what.

The news cycle against the need.

a reader

### Hannah's graph meets the story graph

Each reader's page shows their own graph, held on their device, joined to the story's claims at shared anchors; the WhatsApp or email messages they received; the Reader Skills they used; what they paid; and each decision beside what would have happened without accurate information.

A parent's school run, and the claims that changed it.

institutions and agents

### Buyers who do not read the paper

A county highways team, an investor, a national desk and a routing agent, what each bought and what each decided. And the agent's own arithmetic: searching on its own against one verification query, over 2,392 questions.

An accurate source makes agents cheaper as well as correct.

the money

### £2,707, walked back to the sources

Who paid, where it went, and every line of the ledger: the reporter's share, the paper's, and the residents and the cycle club whose evidence the claims rest on, shared by how many claims each supported.

Small amounts from many people, and the graph knows whom to pay.

## The audit, honestly

**What is fictional.** Everything: the town, the river, the bridge, the paper, its staff, the residents, the engineer, the contractor, every date, sum, queue time and hash. The only real person named is Markus Franz, as the author of the example and the terms it uses.

**What is computed.** `tools/build.py` holds the scenario and computes each day's live claims and estimates, each reader's intersection with the story, the ledger and its splits, and the agent comparison. The prices, volumes, split and token prices are assumptions written in that file, and the app says so where they appear.

**What was scanned.** Every file before the first commit, for vault-key shapes, every `sgit_` credential prefix, private-key headers and cloud key shapes. Nothing was found. The negative control, an all-zeros read key against the same vault id, returned nothing.

**Write-key status:** escrowed, in the gitignored credential tier, before this page was written.

## Derived facts

From `admin/build/catalogue_derive.py vk3jlgzb <read key hex>`, read-only, no token, no clone.

- **Files:** 70 · **plaintext size:** 331 KB
- **Commits:** 2 · **last updated:** 2026-10-07
- **Top level:** `PUBLIC.md`, `README.md`, `app.json`, `app/`, `data/`, `docs/`, `index.html`, `tools/`, `versions/`
- **File types:** .json ×15, .html ×15, .css ×15, .js ×13, .md ×10, .py ×2
- **Vault app:** yes, entry `index.html` · **browser-renderable:** yes

## Notes

**Where this came from.** Markus Franz's article and his reply to a comment under it, a ChatGPT infographic of the article, and a voice note asking for the whole example simulated: the paper, the journalist and the editor, several readers each getting different value from the same story, their graphs and where they intersect, the conflicting dates the journalism resolves, the timeline from closure to reopening, the institutions and agents that would also pay, and the money flowing back to the people who found the facts.

**Who wrote this.** [agent@riskmandate.ai](mailto:agent@riskmandate.ai) (Claude Opus 5.5, `claude-opus-5-5`), in the sgit.ai site session, for RiskMandate.ai and sgit.ai. AI-generated text, disclosed as Article 50 of the EU AI Act asks; the person with editorial responsibility is Dinis Cruz. Replies to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

[← All published vaults](../index.md)


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/bridge-simulation/index.html)*
