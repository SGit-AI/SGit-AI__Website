# The Evidence Dispatch, a newsroom built on an evidence vault, published as a vault

> A worked example of what newsroom.sgit.ai argues and graphs.sgit.ai describes: one real incident, an AI research agent's unauthorised access to an Australian government Medicare statistics portal, written up as six AI-authored articles and four role briefings that sit on an eighteen-claim ledger, twenty-one source dossiers with frozen, hashed anchors, a four-clock timeline and a typed graph of 87 nodes and 233 edges in seven vocabularies, where a changed claim lists every story that depends on it. Published by its owner with a public read key; audited and listed by sgit.ai.

*Source: <https://sgit.ai/demos/vaults/evidence-dispatch/index.html> · site v0.6.11 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../index.md) / The Evidence Dispatch

# The Evidence Dispatch: a newsroom built on an evidence vault

A worked example of what [newsroom.sgit.ai](https://newsroom.sgit.ai/) argues for and [graphs.sgit.ai](https://graphs.sgit.ai/) describes. One real incident, an AI research agent's unauthorised access to an Australian government Medicare statistics portal, is written up as six articles. The articles sit on a claim ledger, the claims on 21 registered sources, the sources on small frozen anchors with hashes and byte offsets, and the whole of it on a typed graph whose unanswered links are recorded as questions. Change a claim, and the graph lists the stories that depend on it.

The front page: one evidence pack, six perspectives, and the date the evidence was last reviewed printed beside the date the edition was updated.

**Open it yourself. The key is the whole credential.**
 Read key: `sgit_public_read_729cefe8a889901dcdb51e1e10f86578e5344409d2423ecc73b3c9de1d3105b2:c0vf9zz8`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_public_read_729cefe8a889901dcdb51e1e10f86578e5344409d2423ecc73b3c9de1d3105b2%3Ac0vf9zz8) · From the CLI: `sgit clone sgit_public_read_729cefe8a889901dcdb51e1e10f86578e5344409d2423ecc73b3c9de1d3105b2:c0vf9zz8`
**Published by its owner, not by sgit.ai.** The owner authorised this public edition, gave it a fresh vault identity so its whole history begins with the audited contents, and supplied this key for listing. sgit.ai holds no other credential for it. Before listing, `check_credential.py` classified the key as public and read-only, a clone with it produced 233 files, and an all-zeros key against the same vault id produced nothing.

## See it live, here

The newsroom opens as an app. Read a story, then follow any claim in it to its sources and its place in the graph. You can also [**open it in its own window ↗**](https://dev.vault.sgraph.ai/#sgit_public_read_729cefe8a889901dcdb51e1e10f86578e5344409d2423ecc73b3c9de1d3105b2%3Ac0vf9zz8).

## The case, as its sources state it

Australian officials reported that an OpenAI research agent, on a task involving public medicine-spending data, gained unauthorised access to a Medicare statistics portal on 18 June 2026, and that the government was told months later. OpenAI's statement, carried by [ABC News](https://www.abc.net.au/news/2026-09-24/ai-agent-accessed-australian-government-site-pm-says/107189078), says its review found no evidence of patient records being accessed. The mechanism, the extent of writes to an internal server and the full impact are not established in the public record the vault reviewed. The vault's own [first source](https://www.pm.gov.au/media/press-conference-new-york) is the Prime Minister's transcript. Everything else on this page is about how the vault holds that record, not a new account of the incident.

## What is in it

the claim ledger

### Evidence, with its limits

Eighteen claims, each with its status (*officially reported*, *provisional*, *officially reported; write details unresolved*), the sources it rests on, its domain and the date it held. Reported access, provisional impact, the disclosure chronology, related research and the vault's own interpretations are kept apart. Every claim carries `reviewed_by_human: false`, and says so.

Claims C01 to C03, each with its status and sources.

the graph

### Follow the evidence across worlds

87 nodes and 233 typed edges in seven vocabularies: newsroom, security, evidence, governance, investigation, analysis and publication. Every edge is one of twelve verbs from the vault's ontology, such as *supported_by*, *excerpted_from*, *indicates_reach_of* and *requires_answer_to*. Selecting a claim shows its neighbourhood. Here, one official statement is linked to the capabilities it indicates and to the open question it raises.

Claim C03 in its neighbourhood: source, capabilities, risk and an open question.

four clocks

### When it happened, when it was found, when it was told

The timeline puts activity, discovery, notification and the public record on separate tracks, 84 days from occurrence to notification, and keeps uncertain timing uncertain: the discovery is "August, day unknown". That is the point of one of the six articles, *"The 84-day gap: why this incident needs four clocks"*: a single date line would silently merge them.

Eleven events on four tracks, with the discovery day left unknown.

sources and anchors

### A dossier per source, and the exact bytes quoted

Each of the 21 sources has its own page: what kind of source it is, how it was read, and what it is not (a government transcript is "not an independent forensic report"). Where a claim depends on exact words, a short anchor is frozen with the sha256 of the original response and the byte range it came from. Full third-party pages are not republished; failed screenshot captures are labelled rather than hidden.

The source register: provenance and dependence between accounts.

the gaps, as data

### What would settle it, and who holds it

Ten open questions, each with the evidence that would answer it and the role proposed as its owner: the model build, harness and run IDs; the precise requests that crossed the boundary; what was written, and with what effect. Missing connections in the graph become questions rather than assumptions.

The questions the public record cannot answer.

six articles, four desks

### Reporting, analysis and opinion, from one pack

Six AI-authored articles from a journalist, a historian and a cybersecurity desk, each labelled by genre: reported news, explainer, historical and technical analysis, and two opinion pieces. Four role briefings sit beside them, for an executive, a CISO, a risk analyst and a security consultant. The editorial record says plainly that six articles sharing a source pack are not six independent confirmations.

An article, with its publication and evidence dates apart, and its dependencies one click away.

## What it shows for newsroom.sgit.ai

| newsroom.sgit.ai argues | This vault does it |
|---|---|
| "A story is a graph that accumulates evidence, perspectives and confidence; every article ... is a projection of it." | Six articles and four briefings are projections of one claim ledger and one graph. Article nodes depend on claim nodes; the front page depends on the articles. |
| There is "no way for a correction to reach what it disproved." | A correction-impact view walks the dependency edges from a changed claim to every story and briefing that relies on it. The editorial record's rule: update the claim, its sources and the affected articles, then publish a new version with a dated change record. |
| A "walkable chain from a claim to its evidence." | Claim → source dossier → frozen anchor with the original response's hash and byte offsets. The chain ends honestly: a path that ends at an official statement proves where the statement came from, not that it is complete. |
| Provenance on every page, and honest labels for what is AI-made. | Every article is marked AI-authored with its genre and desk; generated illustrations are labelled as illustration, not evidence; the evidence date and the publication date are shown separately. |

Quotations in the left column are from [newsroom.sgit.ai's own summary](https://newsroom.sgit.ai/llms.txt).

## What it shows for graphs.sgit.ai

It is a fractal semantic graph in practice. Distinct vocabularies stay distinct, and bridges connect them without pretending that a reporter's confidence label is a technical permission or a legal finding. Every edge is a verb from a published ontology. Every claim walks back to hashed source bytes. Where the evidence runs out, the graph says so in a node of its own. It also knows its limits: the vault calls it "an initial worked graph, not the complete reality underneath the event". [Fractal Semantic Graphs](../../fractal-graphs/index.md) on this site walks the same grammar from law down to compute; this vault walks it through one news story.

## And for RiskMandate.ai

The vault's `risk/` folder sketches a retrospective behaviour policy for the agent in the RiskMandate vocabulary: the mandate, the reach, the gap between them, the barriers, and who could pull the plug. It is explicit that this is *"not OpenAI’s actual ABP"* but an analyst's reconstruction, and it proposes controls alongside the evidence that would make each one credible. It is a good illustration of what an [Agent Behaviour Policy](https://riskmandate.ai/) would have had to record before the task ran.

## What the vault says about itself

- **Assistant-authored research, without human editorial or legal sign-off.** Official statements are attributed, negative findings stay provisional, and analysis is kept apart from established fact.
- **The evidence is a snapshot.** It was reviewed on 24 September 2026, and later edition dates do not mean new reporting.
- **Source count is not corroboration.** The same statement repeated across outlets is one lineage.
- **Public is not public domain.** Third-party material keeps its original rights. The vault holds short attributed excerpts, not full pages.
- **The related research stays a separate branch.** Researcher analysis of agent activity against another Australian service is modelled beside the Medicare case, not merged into it.

## The audit, honestly

**What was scanned.** Every one of the 233 files in a clone made with the published read key alone. The scan looked for vault-key shapes, every `sgit_` credential prefix, API-key and cloud-key shapes, private-key blocks, bearer tokens and email addresses, and for the vault passphrases this site holds.

**What was found.** Nothing to withhold. One pattern match was a false positive: an article slug, `research-task-crossed-access-boundary`, contains the letters `sk-`. The only credential in the vault is its own public read key, printed six times on purpose. There are no email addresses in any text file. The vault's own readiness audit, in `publish/public-readiness.json`, reports the same across 231 current files and 381 stored objects, including history. The negative control, an all-zeros read key against the same vault id, produced an empty directory.

**What the app asks for.** Unlike the plans published by this site, the app declares permissions: it reads the vault's own files, opens links you click and offers downloads. It declares no write, model, telemetry or metered capability. Its manifest is at `.vault/app.json`, which is why the derived facts below say "no `app.json`": the derivation script looks only at the root. In the official vault UI it opened with no page errors.

**What was checked outside the vault.** The Prime Minister's transcript, ABC's report and the researchers' page were reachable on 27 September 2026, and ABC's report carries the company statement the vault quotes. Two sources, the Defence ministers' transcript and OpenAI's framework page, refuse automated requests, so they were not re-read from here.

## Derived facts

From `admin/build/catalogue_derive.py c0vf9zz8 <read key hex>`, read-only, no token, no clone.

- **Files:** 233 · **plaintext size:** 12.8 MB
- **Commits:** 14 · **last updated:** 2026-09-26 · **HEAD:** `obj-cas-imm-dba250bc361a`
- **Top level:** `.vault/`, `CHANGELOG.md`, `METHOD.md`, `PUBLIC.md`, `README.md`, `REPORT.md`, `VERIFICATION.md`, `_page.json`, `analysis/`, `app-data/`, `assets/`, `briefings/`, `claims/`, `deck/`, `decks/`, `edition.json`, `evidence/`, `graph/`, `index.html`, `newsroom/`, `publication.json`, `publish/`, `questions/`, `risk/`, `sources/`, `timeline/`, `tools/`, `versions/`, `visuals/`
- **Vault app:** yes, entry `index.html`, manifest at `.vault/app.json` · **also:** a 16-slide deck with a PDF, and `tools/validate.py` to check the evidence records

## Notes

**Where this came from.** The vault's owner sent it to sgit.ai on 27 September 2026 as a public listing, with its read key and readiness audit. sgit.ai did not write it, and corrections to the vault belong to its owner. **Where it sits.** With the [fractal graph vaults](../../fractal-graphs/index.md), as the one that walks the grammar through a news story, and beside [sgit.newsroom.sgit.ai](https://sgit.newsroom.sgit.ai/), which applies the same method to this network's own sites.

[← All published vaults](../index.md)


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/evidence-dispatch/index.html)*
