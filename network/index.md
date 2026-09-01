# The sgit.ai network — sibling sites

> Focused sites on *.sgit.ai subdomains, each pursuing one question further than a section here could: non-human identity for rented agents, and a key registry designed from the 2019 keyserver failure. Screenshots of each, with what it argues and why it is relevant.

*Source: <https://sgit.ai/network/index.html> · site v0.2.50 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

# The sgit.ai network

Nineteen focused sites on `*.sgit.ai`, each taking one question further than a section here could. They share this site's design and its discipline — sourced claims, a stated status, honest edges — and they publish their arguments **before** the things they describe exist, so the commitments stay checkable afterwards.

18 live, 1 with the repository and subdomain in place but nothing published yet. Screenshots are of the real sites, captured on the date each entry gives.

**Which of these is mine?**instant match · no key, no network

Describe what you are trying to do and I will point at the site that takes it seriously. This runs in your browser against the catalogue on this page — no key needed, nothing sent anywhere.

Optional. Answers get more conversational; the matching does not get more correct.

**Bring your own key (OpenRouter).** It is stored in this browser only and sent only to `openrouter.ai` — never to sgit.ai, which is a static site with no server to send it to. **This page cannot protect it the way a vault app can**: with no host there is no permission floor, so the key lives in this page's origin. [llms.sgit.ai ↗](https://llms.sgit.ai) explains the difference, and [the plan](../articles/chat-on-a-static-site.md) explains how we intend to remove the trade-off.

## Start from what you need

Each line is a question somebody actually arrives with, and the site that takes it seriously.

[I need to give an AI agent an identity**nhi.sgit.ai** · agents you run vs agents you rent, and why only one is answered](nhi.md) [My app has to call an LLM and I do not want it holding an API key**llms.sgit.ai** ↗ · the bridge that lets it call one without a credential](https://llms.sgit.ai) [I have to sign off a risk and I do not want to rubber-stamp it**risks.sgit.ai** ↗ · there is no deny button — only how long you accept it](https://risks.sgit.ai) [I need to cite a regulation precisely, not paraphrase it**standards.sgit.ai** ↗ · point at the provision, or you are asserting](https://standards.sgit.ai) [I want to distribute public keys without a central authority**pki.sgit.ai** · a key registry for agents, designed from a directory that was destroyed](pki.md) [I am drawing a graph and want to get the edges right**graphs.sgit.ai** · five rules, and why relates-to is banned](graphs.md) [I want an issue tracker with no database**issues-fs.sgit.ai** ↗ · the issues are files and the files are a graph](https://issues-fs.sgit.ai) [I need somewhere disposable to run an agent**sg-compute.sgit.ai** ↗ · ephemeral AWS environments, one command away](https://sg-compute.sgit.ai) [I am deciding how to license and sustain an open-source project**open-source.sgit.ai** ↗ · open source is a strategy, not a charity](https://open-source.sgit.ai) [I keep being asked what a digital twin actually is**twins.sgit.ai** ↗ · an interface to reality, not a simulation of it](https://twins.sgit.ai) [I want to protect an app at the edge without renting a WAF**sg-sentinel.sgit.ai** · an app-coupled edge guard — published as a design, not built](sg-sentinel.md) [I want to map a strategy without drawing a pretty picture**wardley-maps.sgit.ai** ↗ · maps are claims, not pictures](https://wardley-maps.sgit.ai) [I need the requirements nobody writes down until they break**nfrs.sgit.ai** ↗ · resilience, budgets and backups, from the inside](https://nfrs.sgit.ai) [I want to know how this code is actually written**coding.sgit.ai** ↗ · the style guide that measured itself](https://coding.sgit.ai) [I am pricing something and rent feels wrong**subscriptions.sgit.ai** ↗ · a subscription is a discount for regular use, not rent](https://subscriptions.sgit.ai) [I care where a published fact came from**newsroom.sgit.ai** ↗ · the story is a graph; the article is a projection](https://newsroom.sgit.ai) [I just want the picture**infographics.sgit.ai** ↗ · every rendered brief in one catalogue](https://infographics.sgit.ai)

## Agents & AI

[**coding.sgit.ai**The style guide that measured itself.How software actually gets written across this family: the rules, the compliance measurement against them, which rules are machine-enforced and which are explicitly not, and the open tensions. Includes a section on writing code for agents to read.](https://coding.sgit.ai)
v0.2.0[Open coding.sgit.ai ↗](https://coding.sgit.ai)

[**llms.sgit.ai**Your app calls a language model without ever holding an API key.The sg.llm.* bridge: how an app running inside a vault reaches a model with no credential of its own. The reference, the traps, a four-layer security ladder, the attached-file question, and a pre-ship checklist.](https://llms.sgit.ai)
reference draftv0.2.0[Open llms.sgit.ai ↗](https://llms.sgit.ai)

[**nhi.sgit.ai**The question splits into two populations, and the industry only answers oneThe question of how to give an AI agent an identity splits into two populations, and every product on the market answers only the first. For the agents you actually name — the ones running in Claude, Codex or behind an API — the honest current answer is to hand over a broad credential and hope.](nhi.md)
v0.1.14[What it argues →](nhi.md) · [Open nhi.sgit.ai ↗](https://nhi.sgit.ai)

[**skills.sgit.ai**published soonThe skills site. The repository and subdomain exist; GitHub Pages has not published yet, so there is nothing to read at the address.](https://github.com/SGit-AI/SGit-AI__Website__Skills)
not published yet · [repo ↗](https://github.com/SGit-AI/SGit-AI__Website__Skills)

## Risk & governance

[**nfrs.sgit.ai**The non-functional requirements, from the inside.The requirements nobody writes down until they are violated — resilience, budgets, project management, backups — treated as a reality system rather than a checklist. Includes an honest column: a scorecard, and a page naming backups as a gap.](https://nfrs.sgit.ai)
v0.1.2[Open nfrs.sgit.ai ↗](https://nfrs.sgit.ai)

[**risks.sgit.ai**You cannot deny a risk. You can only say how long you accept it.Risk management inverted: a named human underwrites an exposure that already exists, insurance-style, with personal liability attached. There is no deny button — the only choice is how long, and the interval is the decision. 42 concepts, a six-rung interval ladder, and a stated zero lines of code implementing any of it.](https://risks.sgit.ai)
research sitev0.1.0[Open risks.sgit.ai ↗](https://risks.sgit.ai)

[**standards.sgit.ai**Point at the provision, or you are asserting.Laws, standards and frameworks as addressable graphs rather than PDFs to paraphrase. A citation scheme, a grounding ladder, and worked instruments — the EU AI Act, GDPR, ISO/IEC 27001, ISO 31000 — with a subset method for handing an agent only the part that applies.](https://standards.sgit.ai)
v0.1.4[Open standards.sgit.ai ↗](https://standards.sgit.ai)

## Graphs & method

[**graphs.sgit.ai**A node is just a node. Meaning lives in the edges.A grammar for semantic graphs, argued in increasing depth from five rules you can apply tomorrow to a full positioning against schemas and vector search. It opens by insisting it is not a graph database pitch, and it publishes the four situations in which its own argument is the wrong one.](graphs.md)
v0.1.0[What it argues →](graphs.md) · [Open graphs.sgit.ai ↗](https://graphs.sgit.ai)

[**infographics.sgit.ai**The brief is the argument. The infographic is one picture of it.A catalogue, not a generator: every rendered brief across the sgit.ai family in one place, each picture kept next to the argument it came from rather than circulating on its own.](https://infographics.sgit.ai)
v0.1.0[Open infographics.sgit.ai ↗](https://infographics.sgit.ai)

[**issues-fs.sgit.ai**The issues are files. The files are a graph.An issue tracker with no database: nodes, edges and labels on disk, a small DSL, and a live graph derived from the repository itself. Ships a five-minutes-no-install lite mode for agents alongside the full model.](https://issues-fs.sgit.ai)
reference draftv0.1.2[Open issues-fs.sgit.ai ↗](https://issues-fs.sgit.ai)

[**twins.sgit.ai**A digital twin is an interface to reality, not a simulation of it.Twins as actors rather than models: what a working twin actually is, what was built versus designed, the simulation layer, and an execution broker. Carries its own gaps-and-open-questions page and a where-we-lose section.](https://twins.sgit.ai)
v0.1.0[Open twins.sgit.ai ↗](https://twins.sgit.ai)

[**wardley-maps.sgit.ai**Maps are claims, not pictures.Wardley mapping treated as graphs with position, so a map becomes something you can disagree with precisely. A 40-record doctrine assessment, the custom-axis verdict, the broken middle, and all 34 resources verified with dead links marked.](https://wardley-maps.sgit.ai)
PROPOSEDv0.1.2[Open wardley-maps.sgit.ai ↗](https://wardley-maps.sgit.ai)

## Security & infrastructure

[**pki.sgit.ai**Good public key repositories existed, and were destroyedGood public key repositories existed and were destroyed. This site is the 2019 keyserver catastrophe, the four registry rules it produces, and the build order — all published before the registry exists, so the commitments are checkable against whatever eventually ships.](pki.md)
v0.1.2[What it argues →](pki.md) · [Open pki.sgit.ai ↗](https://pki.sgit.ai)

[**sg-compute.sgit.ai**Ephemeral environments in AWS, one command away.A serverless environment for agents: the machine surface, isolation and the one trade-off it makes, measured numbers rather than claims, and a clear what-ships-today line against the roadmap.](https://sg-compute.sgit.ai)
v0.2.0[Open sg-compute.sgit.ai ↗](https://sg-compute.sgit.ai)

[**sg-sentinel.sgit.ai**Layer 1 decides and signals. Layer 2 acts and writes.A design for an edge security and logging layer you own rather than rent, built on the observation that your own app already knows what a valid request looks like — so the edge can allowlist rather than denylist. Published as a complete design that has deliberately not been built.](sg-sentinel.md)
v0.1.1[What it argues →](sg-sentinel.md) · [Open sg-sentinel.sgit.ai ↗](https://sg-sentinel.sgit.ai)

## Business & publishing

[**influences.sgit.ai**Where the thinking came from.The sources behind this body of work, registered rather than gestured at — an influence map in three tiers, a register format, a changelog recording when a source moves between tiers, and a distinction between what was designed and what was discovered then confirmed.](https://influences.sgit.ai)
v0.2.0[Open influences.sgit.ai ↗](https://influences.sgit.ai)

[**newsroom.sgit.ai**The story is a graph. The article is a projection.Provenance as the product: a worked story costed at £8.40, payment rails to the fact creator, micro and nano payments, CC-Signed content rights, and the roles an operating newsroom would need. A published design, not a running newsroom.](https://newsroom.sgit.ai)
not builtv0.2.5[Open newsroom.sgit.ai ↗](https://newsroom.sgit.ai)

[**open-source.sgit.ai**Open source is a strategy. It is not a charity.Survivability as the test rather than licence purity: a stress test, a self-audit, six recorded corrections, six success stories with numbers, three licences compared, and why Apache-2.0 rather than MIT here.](https://open-source.sgit.ai)
draftv0.1.1[Open open-source.sgit.ai ↗](https://open-source.sgit.ai)

[**subscriptions.sgit.ai**A subscription is a discount for regular use, not rent on something you ignore.The commercial model stated as a position: a register of what you actually hold, governance and schema, an exit-path method, and the law behind it — with the service itself marked as later, not now.](https://subscriptions.sgit.ai)
draftv0.1.0[Open subscriptions.sgit.ai ↗](https://subscriptions.sgit.ai)

## Every site, at a glance

| Site | What it argues | Area | Status |  |
|---|---|---|---|---|
| **coding.sgit.ai** | The style guide that measured itself. | Agents & AI | live · `v0.2.0` | [open ↗](https://coding.sgit.ai) |
| [graphs.sgit.ai](graphs.md) | A node is just a node. Meaning lives in the edges. | Graphs & method | live · `v0.1.0` | [open ↗](https://graphs.sgit.ai) |
| **influences.sgit.ai** | Where the thinking came from. | Business & publishing | live · `v0.2.0` | [open ↗](https://influences.sgit.ai) |
| **infographics.sgit.ai** | The brief is the argument. The infographic is one picture of it. | Graphs & method | live · `v0.1.0` | [open ↗](https://infographics.sgit.ai) |
| **issues-fs.sgit.ai** | The issues are files. The files are a graph. | Graphs & method | reference draft · `v0.1.2` | [open ↗](https://issues-fs.sgit.ai) |
| **llms.sgit.ai** | Your app calls a language model without ever holding an API key. | Agents & AI | reference draft · `v0.2.0` | [open ↗](https://llms.sgit.ai) |
| **newsroom.sgit.ai** | The story is a graph. The article is a projection. | Business & publishing | not built · `v0.2.5` | [open ↗](https://newsroom.sgit.ai) |
| **nfrs.sgit.ai** | The non-functional requirements, from the inside. | Risk & governance | live · `v0.1.2` | [open ↗](https://nfrs.sgit.ai) |
| [nhi.sgit.ai](nhi.md) | The question splits into two populations, and the industry only answers one | Agents & AI | live · `v0.1.14` | [open ↗](https://nhi.sgit.ai) |
| **open-source.sgit.ai** | Open source is a strategy. It is not a charity. | Business & publishing | draft · `v0.1.1` | [open ↗](https://open-source.sgit.ai) |
| [pki.sgit.ai](pki.md) | Good public key repositories existed, and were destroyed | Security & infrastructure | live · `v0.1.2` | [open ↗](https://pki.sgit.ai) |
| **risks.sgit.ai** | You cannot deny a risk. You can only say how long you accept it. | Risk & governance | research site · `v0.1.0` | [open ↗](https://risks.sgit.ai) |
| **sg-compute.sgit.ai** | Ephemeral environments in AWS, one command away. | Security & infrastructure | live · `v0.2.0` | [open ↗](https://sg-compute.sgit.ai) |
| [sg-sentinel.sgit.ai](sg-sentinel.md) | Layer 1 decides and signals. Layer 2 acts and writes. | Security & infrastructure | live · `v0.1.1` | [open ↗](https://sg-sentinel.sgit.ai) |
| **standards.sgit.ai** | Point at the provision, or you are asserting. | Risk & governance | live · `v0.1.4` | [open ↗](https://standards.sgit.ai) |
| **subscriptions.sgit.ai** | A subscription is a discount for regular use, not rent on something you ignore. | Business & publishing | draft · `v0.1.0` | [open ↗](https://subscriptions.sgit.ai) |
| **twins.sgit.ai** | A digital twin is an interface to reality, not a simulation of it. | Graphs & method | live · `v0.1.0` | [open ↗](https://twins.sgit.ai) |
| **wardley-maps.sgit.ai** | Maps are claims, not pictures. | Graphs & method | PROPOSED · `v0.1.2` | [open ↗](https://wardley-maps.sgit.ai) |
| **skills.sgit.ai** | published soon | Agents & AI | not published yet | [repo ↗](https://github.com/SGit-AI/SGit-AI__Website__Skills) |

## Read one in full

Four have a full write-up here — what the site argues, where it is honest about its limits, and why it is relevant to sgit:

- [**graphs.sgit.ai**](graphs.md) — A node is just a node — meaning lives in the edges
- [**nhi.sgit.ai**](nhi.md) — Agents you run, agents you rent, and the identity gap
- [**pki.sgit.ai**](pki.md) — A key registry for agents, designed from a documented failure
- [**sg-sentinel.sgit.ai**](sg-sentinel.md) — An app-coupled edge guard — Layer 1 decides, Layer 2 acts

## Why they are separate sites

Each one is an argument that needs room and a reader who arrived for it. Splitting them out keeps this site about sgit while letting each question be pursued properly — and gives each its own version history, release cadence and repository. They are built from the same generator and hold to the same rules, so a reader moving between them is not changing register.

This is also the refactor it looks like: material that would have made sgit.ai sprawl now has a better home, and this page is the index back into it. Adding the twentieth site is writing one markdown file.


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/network/index.html)*
