# A proposed partnership between sgit.ai, RiskMandate.ai and UK Sovereign AI

> A proposal from our side, published in the open. UK Sovereign AI names trust, safety and assurance as one of five frontiers and the safe adoption of AI agents as a procurement challenge area. This page states their mission in their own words, maps each priority to vaults published here that can be opened now (Licence to Operate, Risk Mandate, AIUC-1 conformance, the DSIT AI Risk Toolkit, Regulation Graph), states the UK anchoring in the founder's own words (thirty years in the UK, a UK exit, The Cyber Boardroom Limited as the trading company), argues that sovereignty without open source is one acquisition deep, proposes three concrete partnership shapes sized to their instruments, and lists what the page cannot tell them.

*Source: <https://sgit.ai/partnerships/sovereign-ai.html> · site v0.6.0 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Partnerships](index.md) / UK Sovereign AI

A proposed partnership · sgit.ai and RiskMandate.ai with UK Sovereign AI · public material only · 23 September 2026

# A proposed partnership between sgit.ai, RiskMandate.ai and UK Sovereign AI

**This is a proposal from our side, published in the open.** [sgit.ai](../index.md) (git for encrypted vaults) and [RiskMandate.ai](https://riskmandate.ai/) (the business risk layer for AI agents) are two UK-built products from the same founder and the same UK company. UK Sovereign AI is Britain's sovereign venture fund for AI companies: *"backing Britain's AI founders to start here, scale here, and win everywhere."* One of its five frontiers is trust, safety and assurance, and one of the four challenge areas in its R&D procurement scheme is the safe adoption of AI agents by cybersecurity professionals. This page argues that the work published on this site and at RiskMandate.ai is a direct, already-built answer to both, that it is built by a founder who has been in the UK for thirty years through a UK-registered company, and that the open-source approach behind it is what makes sovereignty durable rather than one acquisition deep. It makes the argument from public material and the founder's own stated record, so it can be forwarded to anyone.

**Nothing on this page is confidential.** Every statement about UK Sovereign AI is taken from [sovereignai.gov.uk](https://www.sovereignai.gov.uk/) or from public reporting, and is linked. Every statement about us points at a published vault, a printed measurement or a page on this site, except [the anchoring section](#anchoring), which is the founder's own account and says so. There has been no conversation with the fund; this is the case we would make if there were one. Where it says what a partnership *could* be, that is our proposal, not their position.

## What UK Sovereign AI is trying to do

It is worth stating their mission as well as we can, because the fit only makes sense once it is clear.

The fund was established in April 2026 with [£500 million of government capital](https://en.wikipedia.org/wiki/Sovereign_AI_Fund), alongside a £282 million Strategic Assets Grants Programme, to act as a venture investor inside the state: early-stage equity of £1 million to £10 million at market terms and speed, invested alongside other investors and without bespoke conditions, because, in [their own words](https://www.sovereignai.gov.uk/faqs), conditions *"would risk making a company less competitive."* It is chaired by James Wise, with Suzanne Ashman as Managing Partner and Joséphine Kant as Investment Partner, and it is funded by the UK Government through the Department for Science, Innovation and Technology.

The idea underneath it is sharper than "a national fund". Their September 2026 post [From investment to sovereignty](https://www.sovereignai.gov.uk/post/from-investment-to-sovereignty) puts it this way: *"Rather than build a sovereign wall across the entire AI value chain, which could see us miss out on the best breakthroughs from across the world, we will build a sovereign edge."* Sovereignty, on this reading, is not self-sufficiency in everything. It is concentrating on the layers where the UK can win, and making sure the companies that win there are anchored here: *"Not by outspending larger economies, but by concentrating resources where the UK has the potential to win."*

They name five frontiers where they think that is possible:

| Frontier | What it covers, as we read it |
|---|---|
| **Compute and infrastructure** | The layer everything else runs on, with an emphasis on efficiency: doing more with less compute, and doing it here. |
| **Foundation models** | Next-generation models built from the UK. |
| **AI in health and life sciences** | Drug discovery and clinical applications, where the UK research base is a real advantage. |
| **Scientific discovery** | AI as an instrument of science, including materials and autonomous labs. |
| **Trust, safety and assurance** | The layer that lets the other four be adopted: knowing what a system can do, whether it did what it was allowed to, and being able to show that to a regulator, an insurer or a board. |

And they back founders with more than capital. [The offer beyond investment](https://www.sovereignai.gov.uk/offer-beyond-investment) is four things: up to a million GPU hours on the national AI Research Resource (Isambard and DAWN) for substantive UK R&D; an R&D procurement scheme with *"up to £100 million available over the lifetime of the scheme for UK-registered startups and SMEs"*, in which government acts as an early customer, contracts run to £5 million over 12 to 24 months, and *"suppliers retain ownership of their intellectual property"*; a Strategic Assets Programme funding pre-competitive datasets and lab infrastructure; and visa cost reimbursement for international R&D hires. The procurement scheme's four initial challenge areas are AI for NHS productivity, defence mission environment integration, compute efficiency for public infrastructure, and **safe AI agent adoption for cybersecurity professionals**.

The test they apply is anchoring. A company must *"have, or commit to building, a significant and enduring UK presence"*, and success is measured by *"both commercial performance and UK anchoring."* The portfolio so far runs from Callosum in AI infrastructure to Isomorphic Labs in drug discovery and Cusp AI in materials, with a second tier of compute recipients, and the unit has said it is in conversation with around thirty more.

Put simply: **they want British companies building the layers that matter, anchored here, and they are willing to be the first customer as well as an investor.** That is a good thing to want, and the rest of this page is about one of those layers.

## What we have built, in public

Two companies, one substrate, and a published body of evidence that can be opened by anyone with the read key printed on each page.

**[sgit.ai](../index.md)** is git for encrypted vaults. A vault is a folder versioned like a git repository, encrypted on the client before anything leaves the machine, openable by anyone holding a read key with no account and nothing installed, and able to carry its own application with the permissions it asks for declared in a file. The server that stores it cannot read it; [the security model](../security/index.md) states exactly what it does see. The code is Apache-2.0 and [deploys to Docker, AWS, GCP or a plain static host](../deploy/index.md), including, as this site demonstrates, to a bucket behind a CDN with no server of ours in the path. [Thirty-two vaults are published with their read keys](../demos/vaults/index.md), and [the method for publishing them safely is written down](../demos/vaults/publishing.md) with the mistakes that produced each rule.

**[RiskMandate.ai](https://riskmandate.ai/)** is the business risk layer for autonomous systems. Its tagline is *"know what your agents can do"*, and its central object is the Agent Behaviour Policy: a documented record of what an agent can reach, what it was authorised to do, the gap between the two, and which controls constrain it, written so that a CEO, a CTO, a CISO and an insurer can all sign the same document. From that comes the *licence to operate*: the business as the authority, the behaviour policy as the evidence, the agent operating under stated terms for a stated interval, with residual risk accepted by a named owner. *"Not what they did. What they can."*

Underneath both is the graph work described at [Fractal Semantic Graphs](../demos/fractal-graphs/index.md) and [graphs.sgit.ai](https://graphs.sgit.ai/): regulation, guidance, standards and risk registers modelled as semantic graphs where every edge is a verb and every claim walks back to hashed source bytes, so that trust comes through provenance and provenance comes via evidence.

## Where the two meet

Their fifth frontier and their fourth challenge area are the two places we already work, and the evidence for that is not a deck. It is vaults that are open right now.

| What they have said they want | What is already published, and can be opened |
|---|---|
| **Safe AI agent adoption for cybersecurity professionals** procurement challenge area | [Licence to Operate](../demos/vaults/licence-to-operate/index.md): one agent, its grant, its mandate, and the policy insuring that mandate, as a simulation where every turn shows whether the reply is inside the band, draws on the pool, or is outside cover. [Agentic Browser Isolation](../demos/vaults/agentic-browser-isolation/index.md): a living risk graph for whether an agent acts inside your logged-in browser or an isolated one with a scoped identity. [Two games about what an agent can do](../demos/vaults/agent-permission-games/index.md), built by another agent from a brief on this site. And [Risk Mandate](../demos/vaults/risk-mandate/index.md) itself, a working application with 98 commits inside one encrypted vault that uses an LLM without ever holding the API key, and runs on an iPad with the network off. |
| **Trust, safety and assurance** the fifth frontier | [Provenance is not conformance](../demos/vaults/aiuc-1-conformance/index.md): a standard tells you what good looks like and cannot tell you whether you do it, so the vault keeps two edges apart, *evidenced_by* (does the standard say this?) and *attested_by* (does this subject do this?), and asks what would be insurable on this date given what is actually evidenced. [A penetration test delivered as a vault](../demos/vaults/pentest-report/index.md): eight audience-specific views of one engagement, evidence attached to each finding, and a runnable retest per finding that exits 0 if fixed and 1 if not. |
| **Regulation and guidance that can be cited, not asserted** the substrate of assurance | [The DSIT AI Risk Management Toolkit as four connected worlds](../demos/vaults/dsit-ai-risk-toolkit/index.md): the department's own guidance, its spreadsheet, the risk method it describes and the frameworks it cites, modelled as separate worlds with named bridges, every claim carrying the bytes it came from and declaring whether a person curated it or a lexical match found it, published under the Open Government Licence and clearly marked as independent and derived. [Regulation Graph](../demos/vaults/regulation-graph/index.md): the EU AI Act as amended, parsed from official Formex XML and hash-verified, 1,523 nodes and 1,944 edges, so a risk in a register points at a named obligation in a real instrument. [Standards Atlas, GDPR](../demos/vaults/standards-atlas-gdpr/index.md): rulings and regulators' guidance as first-class nodes over the articles they bend. |
| **High-quality datasets as strategic assets** Strategic Assets Programme | Every graph above is a dataset with its provenance attached, distributed as an encrypted, versioned vault that opens with a read key. The shape generalises: a national dataset published this way is hash-verified against its source, versioned so every release is retained, portable across any cloud or a UK-hosted bucket, and readable by nobody without the key, including whoever hosts it. [The catalogue](../catalogue/index.md) is the index of such datasets, itself a vault, listed in itself. |
| **Compute efficiency for public infrastructure** procurement challenge area | Not our frontier, but a measured property of the substrate. [Performance, cost, and running everywhere](../demos/fractal-graphs/performance.md): no database, no instance hours, storage and egress only, query compute paid by the reader's device, a 2,660-fold semantic compression ladder from raw source to ontology with nothing discarded, and the whole estate at 2,662 files and 295 MB of object storage as measured on 21 September 2026. The commands are printed so the numbers can be re-run. |
| **Sovereignty as an edge, not a wall** their thesis | An open-source, client-side-encrypted substrate is what a sovereign edge looks like at the data layer. The code runs anywhere and belongs to nobody; the keys stay with the owner; the host, whichever country it is in, cannot read the content; and moving a vault between providers is a copy. A closed champion is one acquisition away from losing its sovereignty; an open substrate cannot be bought out from under the country that runs on it ([the argument, below](#anchoring)). [open-source.sgit.ai](https://open-source.sgit.ai/) makes the strategic argument for why the code being open is the commercial choice rather than the charitable one. |

## The UK anchoring, stated by the founder

The fund's central test is a significant and enduring UK presence, so this is stated plainly and in the first person, because it is the one part of the case that only the founder can supply.

| **Thirty years in the UK** | I have been based in the UK for thirty years. I live here and I have worked here throughout: as a security practitioner, as a CISO for UK companies, and as a founder. |
|---|---|
| **One UK exit already** | I have taken one UK company through to an exit. This is not a first attempt at building a British company that lasts. |
| **The commercial vehicle is a UK company** | The commercial venture behind sgit.ai and RiskMandate.ai today is [The Cyber Boardroom Limited](https://thecyberboardroom.com), a UK-registered company that has been trading for almost two years. |
| **The intent is more UK companies** | The plan is to grow UK-based companies on this technology, in the open, the way [the operating model](../articles/the-question-is-whether-they-miss-it.md) describes: profitable products, investors who come to you, and the code open so that the companies are portable and the founder leaves with the tools. |

**And one argument about sovereignty itself.** I do not think a country can have sovereign AI without open source, and I would make that case to the fund directly. A closed sovereign champion is one acquisition away from not being sovereign at all: the day it is bought, the code, the roadmap and the keys go with it, and the CMA and NSI Act reviews the fund's FAQ points to are a brake on that, not a guarantee against it. An open-source substrate cannot be acquired out from under the country that depends on it. The code stays available, the vaults stay openable by whoever holds the keys, and any UK company, including a new one, can pick the work up and continue it. That is why everything here is Apache-2.0, why the investor materials are public, and why [open-source.sgit.ai](https://open-source.sgit.ai/) argues that open source is the strategy rather than the charity. Read against *"a sovereign edge, not a sovereign wall"*, it is the same idea from the other side: the edge is only durable if it cannot be bought.

## What a partnership could be

Three concrete shapes, in the order we would propose them, each sized to what the fund already offers.

| Shape | What it would be | Which of their instruments |
|---|---|---|
| **1 · A procurement prototype for the safe adoption of agents** | Take the licence-to-operate model, the Agent Behaviour Policy, and the grant-against-mandate delta, and run them against real agents in a government cybersecurity setting: what each agent can reach, what it is authorised to do, the gap, the controls, and the named owner of the residual risk, as a versioned record a CISO and an insurer can both sign. The public simulation exists; the prototype is the same model on real deployments, with the evidence held in vaults the department controls and we cannot read. | The R&D procurement scheme, challenge area four. Contracts to £5 million over 12 to 24 months; IP stays with the supplier, which we would publish anyway. |
| **2 · Guidance and regulation as citable graphs** | Do for the department's own instruments what the DSIT toolkit and Regulation Graph vaults already do unofficially: publish the official guidance, its cited frameworks and the relevant regulation as hash-verified semantic graphs with an official status, so that every AI risk register in the portfolio, and in government, can point at a named obligation rather than assert one. The independent editions exist and state their own limits; an official edition would remove the disclaimer. | The Strategic Assets Programme's dataset strand, or a small procurement lot. Pre-competitive by construction: everyone in the portfolio benefits. |
| **3 · A substrate for the portfolio** | Every portfolio company will need to hand a working thing to a government user, a regulator or a customer without hosting it for them, without an account, and without the data leaving the owner's control. That is what a vault is for: the app, the data, the history and the read key travel as one string, and it runs offline once cached. Risk Mandate is the worked example, built to be handed to a stranger on an iPad. | The portfolio, as a shared capability rather than a per-company procurement. The measured cost base is on the performance page. |

We would start with the first, because it is the one where a public simulation already exists and the gap to a real prototype is smallest, and because the challenge area is written in almost exactly the words RiskMandate.ai uses.

## What this page cannot tell them, and what it does not claim

- **Anchoring is stated, not yet documented here.** The section above is the founder's own account: thirty years in the UK, a UK exit, a UK-registered trading company behind the work. It is first-hand rather than drawn from a public record on this site, and the corporate detail the fund would want, filings, cap table, team, is a conversation. The fund's own [contact form](https://www.sovereignai.gov.uk/about) or [the author's](../about/index.md) are the routes to it.
- **Certification.** sgit holds no compliance certification of any kind, and [the page that says so](../use-cases/health-regulated.md) says it first. The AIUC-1 and DSIT vaults are independent and derived, and each one states that on its own front page. Nothing here is a conformance claim.
- **Stage.** The fund invests in companies, typically alongside other investors. [sgit.ai for investors](../investors/index.md) is published in the open and leaves the ask visibly empty until the founder states it. This page is about partnership shapes that exist independently of an investment.
- **The fit is partial, on purpose.** Of five frontiers we serve one directly and touch one other. Of four procurement challenge areas we answer one. We would rather be precisely useful in the assurance layer than vaguely relevant to all five.
- **What is still a design.** The performance page notes what it did not measure, the newsroom design says which of its economics run nowhere, and [the sheet of what exists against what is still a design](../summit/startups.md) is kept honest for exactly this kind of reader.

## If you know somebody there

This page is written to be forwarded as it is. It explains what UK Sovereign AI is trying to do, in their words; what has been built, with the read keys to open it; where the two meet, and where they do not; and three concrete shapes a first piece of work could take. Everything on it can be checked by the person who receives it, which is the point. [Who is asking, and how to reach them →](../about/index.md)

[← Partnerships](index.md)[Open Licence to Operate →](../demos/vaults/licence-to-operate/index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/partnerships/sovereign-ai.html)*
