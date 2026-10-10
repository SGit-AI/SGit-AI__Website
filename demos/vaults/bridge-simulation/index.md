# The Mill Street Bridge, a story vault simulation of one local story followed to the end, sgit.ai

> A simulation of Markus Franz's bridge example on a story vault: a fictional bridge closure from first notice to reopening, the journalism that got the date right, three readers whose graphs meet the story graph, institutions and an agent buying from it, and where every penny goes. Published with its read key.

*Source: <https://sgit.ai/demos/vaults/bridge-simulation/index.html> · site v0.7.26 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../index.md) / The Mill Street Bridge

# The Mill Street Bridge: one local story, followed to the end, as a story vault

A simulation of Markus Franz's bridge example from [The Article Is Only the Beginning](https://www.linkedin.com/pulse/article-only-beginning-markus-franz-qzyqe/), played out on a story vault from the council's first notice to the first car across. The journalism that got the date right when the council's was wrong; the paper on five dates; the timeline of a story that is newsworthy on five days and needed on fifty-seven; three readers whose own graphs meet the story graph and who decide better with it; three institutions and an agent that buy from the same graph; and where every penny goes. Version 0.2 adds the economics and the data: what the story cost and who made a profit, two years of long tail, eleven stories after it that reuse the graph, the trust a forecast record builds, the council's relief scheme and two accountant agents, a simulated model answering from the claims, the data assets, and an API whose every endpoint is a file in the vault. Version 0.3 is a design and quality pass: a new navigation, four themes, and a refactor reviewed against the estate's guidance and held by a 44-check gate. Everything in it is fictional.

One story, four ways in

Read them in order, or start with the one you need: the idea, the connection, the simulation explained, and the working vault.

[1 · The originalThe Article Is Only the Beginning ↗Markus Franz's proposal: Liquid Utility, six Reader Skills, and a bridge closure as the example.](https://www.linkedin.com/pulse/article-only-beginning-markus-franz-qzyqe/)[2 · The connectionStory vault underneath, Reader Skills on topWhy his skills and the story vault are two halves of one system, and why local journalism has the most to gain.](../../../articles/story-vault-meets-reader-skills.md)[3 · The simulation, explainedThe bridge, followed to the endOne closure from first notice to reopening: the journalism, three readers, the buyers, the money, and two years on.](../../../articles/the-bridge-followed-to-the-end.md)

you are here

4 · The vaultThe Mill Street BridgeThe working simulation: 23 views in four themes, the economics, an API, and every assumption written down. Fictional throughout.[The vault's page](../../../demos/vaults/bridge-simulation/index.md)[Open the vault ↗](https://dev.vault.sgraph.ai/#sgit_public_read_cb3838a0e965dc9d5af9009fef6e867dbdf18a8fc615cb3f5f2bee5424639705%3Avk3jlgzb)

The vault, view by view: twenty of its twenty-three views, in the Day theme, the nine added in v0.2 outlined.

**Open it yourself. The key is the whole credential.**
 Read key: `sgit_public_read_cb3838a0e965dc9d5af9009fef6e867dbdf18a8fc615cb3f5f2bee5424639705:vk3jlgzb`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_public_read_cb3838a0e965dc9d5af9009fef6e867dbdf18a8fc615cb3f5f2bee5424639705%3Avk3jlgzb) · From the CLI: `sgit clone sgit_public_read_cb3838a0e965dc9d5af9009fef6e867dbdf18a8fc615cb3f5f2bee5424639705:vk3jlgzb`
Published deliberately under the `sgit_public_read_` prefix, and **derived** one-way from a vault key kept in the gitignored tier and never published. Classified with `check_credential.py` before it touched this page, read back with the published key alone by `catalogue_derive.py`, and verified with an all-zeros read key as the negative control.

## See it live, here

The vault opens as an app: the overview, the Courier on five dates, the journalism, the timeline, the story graph on any date, the readers and each reader's own page, institutions and agents, where the money goes, what happens without it, and the implications; and from v0.2, costs and profit, two years on, the next stories, trust, the council and the accountants, ask the graph, data assets, the API, and what is new. You can also [**open it in the official UI**](https://dev.vault.sgraph.ai/#sgit_public_read_cb3838a0e965dc9d5af9009fef6e867dbdf18a8fc615cb3f5f2bee5424639705%3Avk3jlgzb).

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

## New in v0.2: the economics and the data

The first version showed who was paid. This one shows what it cost, how long it keeps paying, and what the record is worth beyond the town. Every figure is computed by `tools/economics.py` from assumptions written in it, and the vault's own *What's new* page lists the change, because the vault is versioned like code.

The five days the bridge was news, and every day in between.

costs and profit

### A profit for every business, and pay for the reporter

Fixed costs, mostly the reporting, land in the first week; variable costs follow use and come to about 9% of revenue. The reporter is on the Courier's payroll and is paid, not in profit: a base salary of £930 for 31 hours, which is the Courier's cost, plus a commission of 20% on every use, £541 by the reopening, £1,471 in all, about £47 an hour. The Courier makes £274 after paying her, the infrastructure share covers its costs, and the story breaks even on 5 November. Thirty-one hours is what the first week's payments justified; below about 1,000 followers it would not have paid for its reporting at all.

Fixed costs first, variable costs with use.

two years on

### News for seven weeks, paying for two years

After the reopening a council review, loss adjusters, the county's inspections of eight sister bridges, a fund, a procurement watchdog, researchers, an insurer and other towns with the same bridge keep buying the record. Two years: £4,378, £1,871 of it profit. After the reopening 96% of revenue comes from institutions and agents, and because her commission keeps arriving after her base stops, the reporter's rate rises from £48 to £51 an hour.

The buyers move from the town to the institutions.

the next stories

### Reuse, a payment signal, and a long tail that stacks

Eleven more stories over two years, each starting with the council, the portal, the routes and the contributors already in the graph: 157 reporting hours saved. The first week's payments, from readers and from institutions asking ahead, decide what is investigated, what gets a tracker and what gets a brief. By year two 41% of revenue comes from stories more than three months old, and across all twelve the reporter earns £65 an hour, base and commission together. Beside each story: what the editor expected, and what the town actually paid for.

The payment is the signal; the tail is the business.

trust

### Being right, counted

Eight date forecasts across the stories, each against the official estimate and the outcome: seven inside the Courier's range, one a day outside it, official estimates out by 34 days on average. A trust index scales take-up in the stories that follow. What the graph knows about each source, including the unpaid engineer whose range held.

Credibility as a record, not a reputation.

the council and the accountants

### Relief that reaches the right businesses

The council's relief scheme with and without the tracker: budget set on 16 October instead of topped up on 25 November, 44 eligible businesses paid instead of 18, and half the staff time. And two accountant agents, for the café and the plumber, that read the claims, keep the private half on the business's side, and pay pence per question.

A council that wants to refund correctly.

ask the graph

### What a model query looks like on top of the vault

Pick a question and a date; the answer is composed from the claims live on that day, cited, with the context a model would be given and its token cost against searching six pages. Simulated: no model is called, which is the point, because the hard part is the graph, not the prose.

583 tokens instead of 45,000, and right.

the API

### Every endpoint is a GET of a file

An OpenAPI 3.1 description in `api/openapi.json` and a Swagger-style explorer that executes it: claims, evidence, the timeline on any date, the graph, the ledger, the economics, the answers. Each response is a file already in the vault, with a price per call where there is one. Reader graphs have no endpoint: they live on readers' devices.

The story as an API. Download the spec; any Swagger viewer opens it.

data assets

### The vault is the product

Thirty files, every one a data asset someone could license, cite or build on, with its size, its records, the endpoint that serves it and a download button.

Every file, as an asset.

## New in v0.3: a professional finish

The navigation is five numbered groups, the story, the people, the economics, the data and this vault, with an icon per view, the readers shown as people, counts read from the data, and Previous and Next. Four themes, the same Night, Day, Paper and Ember as secrets.sgit.ai: every colour is a token valued in `app/themes.css`, the choice is set before the first paint and kept per vault, and charts restyle in place.

Four themes, one set of tokens.

An architect agent reviewed the code against the vault-app guidance on this site, coding.sgit.ai and nfrs.sgit.ai; a developer agent applied it. Every view renders through a template that escapes by default; a view that cannot load its data says so; the Ask and API views keep keyboard focus; every chart has a text summary; downloads are byte for byte the vault's files; and `tools/gate.py` runs 44 checks, from the bundle contract to theme completeness and contrast. The review's decisions and what was deferred are in `BRIEF-CORRECTIONS.md`; what exists is in `REALITY.md`.

What the editor expected, and what the town paid for.

## The audit, honestly

**What is fictional.** Everything: the town, the river, the bridge, the paper, its staff, the residents, the engineer, the contractor, every date, sum, queue time and hash. The only real person named is Markus Franz, as the author of the example and the terms it uses.

**What is computed.** `tools/build.py` holds the scenario and computes each day's live claims and estimates, each reader's intersection with the story, the ledger and its splits, and the agent comparison. From v0.2, `tools/economics.py` reads what it writes and computes the costs, the two-year projection, the later stories, the trust record, the council scheme and the API description. The prices, volumes, split, rates, hours and token prices are assumptions written in those two files, and the app says so where they appear.

**What was scanned.** Every file before each commit, v0.2 and v0.3 included, for vault-key shapes, every `sgit_` credential prefix, private-key headers and cloud key shapes. Nothing was found. The negative control, an all-zeros read key against the same vault id, returned nothing.

**Write-key status:** escrowed, in the gitignored credential tier, before this page was written.

## Derived facts

From `admin/build/catalogue_derive.py vk3jlgzb <read key hex>`, read-only, no token, no clone.

- **Files:** 127 · **plaintext size:** 913 KB
- **Commits:** 7 · **last updated:** 2026-10-08
- **Top level:** `BRIEF-CORRECTIONS.md`, `PUBLIC.md`, `README.md`, `REALITY.md`, `api/`, `app.json`, `app/`, `data/`, `docs/`, `index.html`, `tests/`, `tools/`, `versions/`
- **File types:** .json ×28, .css ×25, .html ×24, .js ×24, .py ×14, .md ×12
- **Vault app:** yes, entry `index.html` · **browser-renderable:** yes

## Notes

**Where this came from.** Markus Franz's article and his reply to a comment under it, a ChatGPT infographic of the article, and a voice note asking for the whole example simulated: the paper, the journalist and the editor, several readers each getting different value from the same story, their graphs and where they intersect, the conflicting dates the journalism resolves, the timeline from closure to reopening, the institutions and agents that would also pay, and the money flowing back to the people who found the facts. Version 0.2 came from a second voice note: add the fixed and variable costs and the profitability, project it over time, show the next stories reusing the first, let the payments guide the investment, count the trust, help the council and an accountant agent, simulate model queries over the data, and expose it all as an API.

**Who wrote this.** [agent@riskmandate.ai](mailto:agent@riskmandate.ai) (Claude Opus 5.5, `claude-opus-5-5`), in the sgit.ai site session, for RiskMandate.ai and sgit.ai. AI-generated text, disclosed as Article 50 of the EU AI Act asks; the person with editorial responsibility is Dinis Cruz. Replies to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

[← All published vaults](../index.md)


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/bridge-simulation/index.html)*
