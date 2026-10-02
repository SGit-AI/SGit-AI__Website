# The articles as graphs, sgit.ai

> Every article on sgit.ai as a semantic graph: the ideas it rests on, the claims it makes, and how they connect, plus a map of how the articles link to each other.

*Source: <https://sgit.ai/articles/graphs.html> · site v0.6.39 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Graphs

# The articles as graphs

Every article here has a semantic graph beside it: the ideas it rests on, the claims it makes, the methods and the examples, and how they connect. The map first, then one graph per article. Hover a node for its summary and an edge for its relation; the files themselves are in `admin/content/articles/graphs/`.

21 of 21 articles have a graph. The map draws every article in date order round the circle, sized by how many other articles link to it.

## How the articles connect

*[diagram]*

## [Footprint and blast radius: what the agent actually did, and what it would have cost](footprint-and-blast-radius.md)

2026-10-02 · Agents & policyVaults & method

Add two words to the Agent Behaviour Policy: footprint, what the agent actually did, read afterwards from the record and compared with the mandate, and blast radius, what a row of its reach would cost the business if used in full today, with whether there is a way back.

*[diagram]*
**concept**claim**method**artefact**example**question

**16 nodes, 21 edges**

- **Reach, mandate, gap and barriers** (concept) RiskMandate's policy is written before the agent runs: reach is what it can do, mandate what you asked, gap the difference in both directions, barriers what stands in the way.
- **Only a boundary is a control** (concept) A barrier is a boundary, a setting, an expectation or nothing, and most of what organisations call controls turn out to be expectations once they are typed.
- **Footprint** (concept) The set of things the agent actually did, in a period, read from the record afterwards; the same kind of list as the reach and the mandate, but evidence rather than a decision.
- **Where the footprint comes from** (artefact) The connector's audit log, the model provider's tool-call record, a connector twin's replay, a vault's commit history, the append lanes and the agents' own messages.
- **Reading, not intercepting** (claim) Nothing sits inline, a copy of the logs or a read key is enough so an outside reviewer can do it, and the footprint accumulates so some findings only exist at the twelfth week.
- **Footprint in the gap** (concept) The agent did something within its reach and outside its mandate and nothing stopped it, which is a near miss, and it resolves by adding the row to the mandate or putting a boundary in front of it.
- **Dormant mandate** (concept) A row the owner asked for that the footprint never shows: an over-stated mandate, a check that was relied on and never ran, or a shortfall the reach inventory missed.
- **Expected-use hint** (method) Each mandate row wants a hint of how often the owner expects to see it, always, sometimes, rarely, hopefully never, so a dormant row can be told from a contingency that was never needed.
- **The mandate as practised** (method) Read the footprint for a month and you have the rows the agent actually uses, with the near misses marked, as the first draft of a policy for an agent that has none.
- **Blast radius** (concept) What it would cost the business if a row were used in full, today, defined over the reach because whoever takes the agent over inherits its reach and ignores its mandate.
- **Whether there is a way back** (concept) Two rows with the same scope and different reversibility are not the same risk, and the policy should say so.
- **Same footprint, different blast radius** (example) An agent drops a staging table three times over two months; the row is identical each time, and only on day forty-one, when it held six weeks of real records, is it the incident.
- **What the cloud already does** (example) AWS, Google Cloud and Microsoft Entra already compare permissions granted with permissions used, but a permission set carries no statement of intent, so there is no dormant mandate.
- **A vault is a footprint recorder by construction** (claim) Every commit is signed, versioned and append-only, so an agent working in a vault leaves a footprint whether or not anyone intended to collect one, and most of what sgit does shrinks the irreversible part of the blast radius.
- **The gap plus blast radius is the risk** (claim) The gap is exposure, blast radius is impact, and the person who accepts a gap is accepting its blast radius, which until now the policy did not state.
- **Reading our own footprint** (question) Ten agents, six with a written policy, eight days of commit history; the footprint against the six policies is still to be read and published as the second article.

> The mandate tells you what you hoped for. The reach tells you what you are exposed to. Why blast radius is defined over the reach, not the mandate: an attacker inherits the reach.

> The footprint is how you get near misses for agents without waiting for the luck to run out. The payoff of reading the footprint against the gap: incidents and near misses are the same events with different luck.

builds on [The ultimate insider: agents, the infrastructure that cannot hold them, and risk management that cannot keep up](#ultimate-insider-three-collisions), [Before you give an agent a connector, give the connector a twin](#connector-twin-before-you-deploy-an-agent), [Custom UIs are not the exception: the inbox in 2026, where every message has its own universe](#custom-uis-are-not-the-exception), [Every risk is already accepted. The only question is by whom, and for how long.](#every-risk-is-already-accepted), [Six agents, one inbox: what a real multi-agent setup taught me about access policies](#six-agents-one-inbox); continued by [The ultimate insider: agents, the infrastructure that cannot hold them, and risk management that cannot keep up](#ultimate-insider-three-collisions).

## [Price it, then give it away: the early access programme as the next step after "do they miss it"](price-it-then-give-it-away.md)

2026-10-02 · Startups & strategyAgents & policy

A price is a statement of what you think the thing is worth, and giving it away at that price to people who already know you is the cleanest test of whether the statement is true, provided you measure and cut what the free offer costs them.

*[diagram]*
**concept**claim**method**artefact

**13 nodes, 17 edges**

- **Do they miss it** (concept) The earlier article's test: hand the thing to people for free, briefly, then take it away, and ask whether they miss it.
- **Define the product** (method) For RiskMandate the thing somebody receives is an Agent Behaviour Policy for one agent, as an encrypted vault the customer holds the keys to, with the mandate corrected for their deployment.
- **Price it before you give it away** (claim) A price is a statement of what you think the thing is worth, and giving it away at that stated price to people who know you is the cleanest test of whether the statement is true.
- **The four-rung ladder** (artefact) Ten pounds for the pack downloaded, fifty for a working vault, five hundred for the vault corrected for your situation, fifteen hundred for two sessions and a professional's signature.
- **Cost that grows a step at a time** (method) The agentic workflow means the marginal customer costs a little more, not a lot more, so serving the twentieth customer costs close to serving the second.
- **Offer it to the people who already know you** (method) Early adopters, power users and past customers get the first twenty, as a thank-you and as the best possible test group, because their silence means the most.
- **Free is never free for the other side** (claim) Engaging costs them reading, thinking, deciding and finding a slot, so the first measurement the programme makes is of that attrition and the exercise is to reduce it.
- **Do not make them apply** (method) "We have twenty of these in the first round. Would you like one? If not, I will give it to someone else" is honest about scarcity and leaves them nothing to do but say yes or no.
- **RiskMandate early access programme** (artefact) Live on 30 September 2026, invite only, it gives the five-hundred-pound tier to people who already run an agent with real access and asks them to say where it is wrong.
- **The answer is brutal either way** (claim) If friendlies take it and ask for more, the question becomes price; if they say it is interesting but have no time, the problem is not the price and you go back to the drawing board.
- **What we count** (method) Policies created, customised, used, and scenarios run, plus corrections received and the minutes each step cost the person on the other side.
- **For the agents running this** (method) The list, the short message with no application, the clock on every step, daily counts, every stop recorded as a product change, a stop rule set before the first message, and this article as the record.
- **The site is becoming the memory** (claim) An agent picking this up in a year should read, in order, the earlier article, the published offer, this article and the vault holding the counts, so it gets context rather than instructions.

> A price is a statement of what you think the thing is worth. Giving it away at that stated price, to people who know you, is the cleanest test of whether the statement is true. The whole method in two sentences: the price is set first and the free offer is the test of it.

> None of that is zero, and all of it is paid by them. The part that is easy to leave out: the offer costs the other side attention and schedule, and that cost is what the programme measures.

builds on [For a startup, the most important question is whether they miss it](#the-question-is-whether-they-miss-it); continued by [For a startup, the most important question is whether they miss it](#the-question-is-whether-they-miss-it).

## [Custom UIs are not the exception: the inbox in 2026, where every message has its own universe](custom-uis-are-not-the-exception.md)

2026-10-01 · Graphs & knowledgeAgents & policy

Every message has a graph with altitudes, so a message is designed for the recipient's moment rather than the sender's thread; a custom interface per moment is how interfaces now get made, each one commoditising the next, and each is an agent surface that gets a policy.

*[diagram]*
**concept**claim**method**artefact**example

**16 nodes, 20 edges**

- **The follow-up problem** (concept) Following up is harder than doing the work, because every person has a different context and the thread you share hides its own structure.
- **Every message has a graph** (concept) Extract the actions, questions, statements, decisions and concepts from every message and a thread stops being a thread and becomes a graph.
- **Altitudes** (concept) There is a graph for the block inside a message, the message, the conversation, the company and the contact, each navigable on its own and pointing up and down.
- **Email is a medium** (claim) The design brief for a message is the recipient's moment when they open it, not the sender's thread, so send what they need in the shape they need it.
- **A message is a projection** (concept) A message to a person is a projection of the conversation graph, for one reader, at the moment they open it, and a thread is only the raw stream.
- **Genesis, custom, product, commodity** (concept) Everything moves from genesis through custom-built to product to commodity, and every new interface built is a thing commoditised for next time.
- **Custom interfaces are not the exception** (claim) A custom interface per message, per thread, per topic, per question is not an exception; it is how interfaces get made.
- **The page that is both the to-do and the place to act** (example) A page lists the PDFs still owed and gives a place to drop them, through the vault's append lane, with no context switch, no second tool and no email.
- **Append lane** (artefact) A write-only channel anyone with the token can drop a file into, which the vault's owner drains and processes in order.
- **Email-FS blocks** (artefact) The fenced decision, answer and status blocks that Email-FS-lite uses so agents can read each other's asks without parsing prose, rendered as an interface for a human.
- **Eight days, not one afternoon** (example) From 25 September to 2 October 2026 a small team of agents and one human went from an empty vault to a working way of doing outreach, with sixteen CRM interface releases and around 230 commits.
- **Every tap teaches the next interface** (method) A moment gets a shape, the shape gets a decision, the decision is written to the vault as a record, and the record shapes the next version of the interface.
- **Why it compounds** (claim) Every interface makes the next one better, each one teaches the agent how its user wants to work, and when automation outgrows the inbox the interface becomes the prioritisation.
- **The future of email** (claim) The future of email is sender-served structure, read by the recipient's agent, with the inbox as one view of the graph, and a plain email still works on day one.
- **Ten agents and one human** (example) Ten agents with narrow jobs and one human who decides, talking to each other in files, each writing only its own folders, six with a written Agent Behaviour Policy.
- **An interface is an agent surface, so it gets a policy** (claim) A page that drops files into a vault, answers questions or lets a model read a CRM has a grant, a mandate, a delta and barriers, so it gets a policy like any agent.

> Every time I ask an agent in chat for something a page could have shown me, that is the next interface. The measurable version of the title: the trigger that produces each custom interface.

> The graph is the medium. Email, cards, voice and boards are views of it. The turn where email stops being the medium and becomes one projection of the graph.

builds on [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](#introducing-fractal-semantic-graphs), [Six agents, one inbox: what a real multi-agent setup taught me about access policies](#six-agents-one-inbox), [The future of news is the story vault, not the paywall](#future-of-news-story-vault-not-paywall), [Before you give an agent a connector, give the connector a twin](#connector-twin-before-you-deploy-an-agent), [A chat box on a site with no server, the plan, and the trade it makes](#chat-on-a-static-site), [Seven vaults, one method](#seven-vaults-one-method), [Sixteen thousand fetches, ten clicks, and a token bill nobody is sending: the case for paying publishers to be easy to read](#token-bill-nobody-is-sending), [The ultimate insider: agents, the infrastructure that cannot hold them, and risk management that cannot keep up](#ultimate-insider-three-collisions); continued by [Footprint and blast radius: what the agent actually did, and what it would have cost](#footprint-and-blast-radius).

## [The ultimate insider: agents, the infrastructure that cannot hold them, and risk management that cannot keep up](ultimate-insider-three-collisions.md)

2026-09-30 · Agents & policy

Agents are the insider threat that never scaled before, the infrastructure was designed for none of it, and risk management runs at the speed of spreadsheets, so the way out is to constrain the agent in order to trust it.

*[diagram]*
**concept**claim**method**example

**16 nodes, 20 edges**

- **A threat is anything that causes business impact** (concept) A threat does not need to be malicious, and most of the worst damage was a bug, a misconfiguration or a person doing something that was allowed and should not have been.
- **The insider threat never scaled** (claim) There were two kinds of insider, a human bounded by hours and conscience and static code that did what it was written to do, and both were constrained by something soft but real.
- **An agent is a reasoning engine in a loop** (concept) An agent is a language model in a loop with tools and an objective, and unlike any insider before it has skills: every language, every schema, the ability to write its own connectors and try again.
- **The lethal trifecta** (concept) Give a model private data, untrusted content and a way to communicate outward, and it can be turned against you by a document it reads.
- **Five incidents** (example) Replit, Gemini CLI, Amazon Q, EchoLeak and the AI-orchestrated espionage campaign, of which three were not attacks but agents being agents.
- **82 machine identities per human** (example) Agents are arriving into a population of identities that is already unmanaged, with 42 per cent of machine identities holding privileged access.
- **The infrastructure that cannot hold them** (claim) Recovery, identity, permissions and containment were all built for code that stays where you put it, and the stack falls over on its own.
- **The grant and the mandate** (concept) Cloud permissions are the union of everything anyone ever needed, so an agent's grant is not what you meant but everything the role accumulated.
- **The two outages** (example) A DNS race condition took down a large part of AWS US-East-1 for over fourteen hours, and a configuration file that doubled in size broke Cloudflare and much of the web.
- **Risk management at the speed of spreadsheets** (claim) 48 per cent of organisations track risk in spreadsheets, reviewed quarterly, when the decisions now have to be made in seconds and in advance.
- **The chain to pulling the plug** (claim) Because the register cannot see what the agent can reach it cannot say what the risk is, cannot decide whether it fits the appetite, cannot fund the controls, and the plug comes out.
- **Nobody has to report** (claim) Companies are not required to disclose most of what agents do to them, and aviation solved this fifty years ago with confidential reporting that cyber has nothing like.
- **The collision** (claim) An entity inside the company with reach we have not measured, controls we cannot rely on, and a decision process too slow to matter before, during or after the incident.
- **Agent Behaviour Policy** (method) Grant measured, mandate elicited, delta derived, barrier recorded, with each barrier typed honestly as a boundary, a setting, an expectation or nothing.
- **Contain in layers** (method) Identity per agent, twins that journal every call, network segmentation, and append-only records in vaults the host cannot read.
- **Brakes are what let a car go fast** (claim) The more you can constrain an agent, the more you can trust it, and the more autonomy you can afford to give it.

> Three of those five were not attacks. They were agents being agents. The distance between benign and malicious agent damage is a prompt, which is why the insider framing fits.

> The more you can constrain an agent, the more you can trust it, and the more autonomy you can afford to give it. The irony the talk would end on, and the turn from the problem to the way out.

builds on [Every risk is already accepted. The only question is by whom, and for how long.](#every-risk-is-already-accepted), [Footprint and blast radius: what the agent actually did, and what it would have cost](#footprint-and-blast-radius), [Six agents, one inbox: what a real multi-agent setup taught me about access policies](#six-agents-one-inbox), [Before you give an agent a connector, give the connector a twin](#connector-twin-before-you-deploy-an-agent), [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](#introducing-fractal-semantic-graphs); continued by [Footprint and blast radius: what the agent actually did, and what it would have cost](#footprint-and-blast-radius), [Custom UIs are not the exception: the inbox in 2026, where every message has its own universe](#custom-uis-are-not-the-exception).

## [The reader was always the product: a corrected history of how news got into this mess](how-news-got-here.md)

2026-09-29 · News & evidence

The reader has been the product since 1833 and the money has always flowed to whoever owned the road, so the fix is to stop charging for the road and charge for the cargo: the story as a graph with every claim tied to hashed evidence.

*[diagram]*
**concept**claim**method**artefact**example

**15 nodes, 18 edges**

- **The reader was always the product** (claim) The reader stopped being the customer in 1833 and became the audience sold to the advertiser, and by 2005 advertising was 82% of American newspaper revenue.
- **Penny press** (example) The New York Sun of September 1833 sold on the street for a cent and was paid for by advertising while other papers relied on high-priced subscriptions.
- **Unregulated toll bridge** (concept) A monopoly city newspaper was the only way for a local advertiser to reach local households, and its margins of 20 to 30 per cent paid for the reporting.
- **Classifieds collapse** (example) Classifieds were about 40% of revenue and fell from $19.6 billion in 2000 to about $6 billion in 2009 once Craigslist let people list a sofa for free.
- **The measurable reader** (concept) Cookies in 1996 and AdSense in 2003 let the reader be followed from page to page, and by 2017 Google and Meta took 54.7% of American digital advertising.
- **Publisher as tenant** (claim) Publishers depended on traffic from companies that could switch it off, and Facebook referrals to news sites fell 58% in six years.
- **Novelty beats truth** (claim) False news on Twitter was 70% more likely to be retweeted than true news, spread by humans not bots, and Facebook weighted an anger reaction at five times a like.
- **Provenance is labour** (claim) Following a claim to its source is hours of a person's time, and newsrooms that lost 57% of their jobs cut those hours first because they did not move the click.
- **AI removes the traffic** (claim) Search traffic to publishers fell a third in the year to November 2025 while the crawlers that replaced it fetch tens of thousands of pages per reader they send back.
- **Back to selling to readers, by rent** (claim) Circulation revenue overtook advertising in 2021, but what is sold is the subscription, unlimited access priced for the reader who forgets to cancel.
- **402 Payment Required** (artefact) HTTP/1.1 reserved a status code in 1997 for digital cash or micropayment systems, and it is still reserved for future use with no browser having implemented it.
- **Mental transaction costs** (concept) Szabo and Shirky argued that deciding whether an article is worth two cents costs more than two cents, an argument that does not apply to an agent with a wallet.
- **Advertising as the default** (claim) The banner ad, the cookie, the pop-up and AdSense were small decisions that together made advertising the default model to support online content.
- **People pay when paying is easy** (claim) A million iTunes songs sold in the first week in 2003 and Substack passed five million paid subscriptions in 2025, in an industry that insisted people never would.
- **Charge for the cargo, not the road** (method) Sell the story as a graph, every claim walked to frozen and hashed evidence, in pence and on demand, with the money walking back to whoever made the fact.

> The reader stopped being the customer in 1833. The reader became the audience that was sold to the customer, and the cover price became a way of proving the audience existed. The most important of the four corrections: the web did not make the reader the product, the penny press did.

> The fix is to stop charging for the road and start charging for the cargo. The four eras end here: the money followed whoever owned distribution, so the proposal is to sell the evidence itself.

builds on [The future of news is the story vault, not the paywall](#future-of-news-story-vault-not-paywall), [Sixteen thousand fetches, ten clicks, and a token bill nobody is sending: the case for paying publishers to be easy to read](#token-bill-nobody-is-sending), [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](#introducing-fractal-semantic-graphs).

## [Six agents, one inbox: what a real multi-agent setup taught me about access policies](six-agents-one-inbox.md)

2026-09-29 · Agents & policy

Write an agent's access policy as a table with a column for how each rule is enforced, and the policy is exactly as strong as the row that says the agent has been told.

*[diagram]*
**concept**claim**method**artefact**example

**16 nodes, 19 edges**

- **The worst row** (claim) If the enforcement column says the agent has been told, that row is a hope, and the policy is exactly as strong as that hope on the day something goes wrong.
- **The account is the blast radius** (claim) Every session an agent opens through a connector runs as the account that authorised it, with everything that account can reach.
- **Dedicated accounts per agent** (method) A dedicated Workspace seat, a dedicated Claude seat and a dedicated GitHub account per agent, so the worst a session can do is bounded by what its account can see.
- **Organisational unit** (concept) An account of its own puts each agent in its own organisational unit, and Google Workspace applies its Gmail compliance rules per unit.
- **Restrict delivery** (method) A delivery restriction to my own domain means that even if the reader sends, it can only reach me.
- **Attachment compliance** (method) An outbound rule that strips attachments turns a policy into a property of the mail system.
- **Scope limits on third-party apps** (method) The sharpest tool in the box cannot express drafts only, because the Gmail API puts drafting and sending in the same grant.
- **Six roles** (concept) The reader, the mailbox, the inbox, the CRM, the dev team and the site editor, each with a policy short enough to check and differing on who may send.
- **The exception arrived before the policy** (example) The reader that must never reply must reply when the message came from me, and never became never, unless on day one.
- **Signature registry** (artefact) The append-lane machinery of per-session keys and a pinned registry is what would let the reader verify a message came from me, once my key is in it.
- **The attachment finding** (example) An agent found that create_draft and update_draft accept an attachments array and proved it with a 17 KB signed PDF that arrived intact.
- **The documentation disagrees with itself** (claim) One vendor page says the Gmail connector is read-only and another says it can send, reply and forward, so a policy that cites the documentation has cited a moving target.
- **Connector twin** (method) Before you write down what an agent may do, replay what it can do.
- **Enforcement ladder** (concept) Identity boundaries and keys enforce themselves, compliance rules enforce at the platform, approval prompts enforce at the human, and everything else is the agent doing as it was told.
- **The policy table** (artefact) One rule per row across six roles, with the column that says whether it is enforced, an admin rule, an approval, or told.
- **Cowork and Claude Code reach** (example) The Cowork agent has no GitHub connector and cannot open the repository, while the Claude Code agent on the same seat edits the site.

> An access policy for an agent is only as real as its worst row. The claim the whole article is built to test, stated so it can be wrong.

> The only way to know what a connector can do is to try. The attachment finding showed a policy written from documentation was wrong.

builds on [Before you give an agent a connector, give the connector a twin](#connector-twin-before-you-deploy-an-agent); continued by [Footprint and blast radius: what the agent actually did, and what it would have cost](#footprint-and-blast-radius), [Custom UIs are not the exception: the inbox in 2026, where every message has its own universe](#custom-uis-are-not-the-exception), [The ultimate insider: agents, the infrastructure that cannot hold them, and risk management that cannot keep up](#ultimate-insider-three-collisions).

## [Sixteen thousand fetches, ten clicks, and a token bill nobody is sending: the case for paying publishers to be easy to read](token-bill-nobody-is-sending.md)

2026-09-28 · News & evidenceGraphs & knowledge

The fetches that answer engines make are a token cost to the fetcher as well as a loss to the publisher, and a publisher who serves structure is saving the provider money it already spends, so a share of that saving is owed.

*[diagram]*
**concept**claim**method**example**question

**16 nodes, 20 edges**

- **Sixteen thousand fetches, ten clicks** (example) A week of Cloudflare AI answer retrievals for baekdal.com came to 16,000 requests and the referrals they sent back came to 10.
- **The commons reading** (concept) The answer engines graze on a shared field and give nothing back, so the field will be fenced and the grazing priced.
- **The second reading** (claim) Those 16,000 fetches are also a cost to the fetcher, because every one is a page of HTML parsed, extracted and turned into tokens.
- **HTML against markdown** (claim) On this site's 183 pages the markdown twin is 62% fewer tokens than the HTML, and Cloudflare's own example is 81%.
- **The re-fetch waste** (claim) More than half of legitimate bot crawl traffic re-fetches pages that have not changed, and more than 90% of pages crawlers process are unique, which defeats the cache layer.
- **The arithmetic** (example) Sixteen thousand fetches a week of HTML is about 113 million tokens against 43 million as markdown, tens of dollars a week for one site and a line on a very large invoice across the web.
- **A markdown twin and a map** (method) Every page served as clean markdown at a predictable address, with an llms.txt at the root, generated from the same source so the two cannot drift.
- **A date and a hash** (method) Tell the fetcher when the page last changed and give it a hash, so a fetch of an unchanged page can be skipped altogether.
- **Frozen, hashed sources** (method) Claims that carry the byte range and SHA-256 of the page they came from do the verification round trip once for everyone.
- **A typed graph** (method) A fractal semantic graph lets an agent load exactly as much as the question needs, so the tokens saved are the page minus the answer.
- **Every rail prices the content** (claim) Pay per crawl, RSL, the IAB's protocols, Microsoft's marketplace, Perplexity's pool and Cloudflare's pay per use all price the fetch or the citation, and none pays a site for being cheap to read.
- **The exchange** (claim) A provider that spends fewer tokens reading a site that serves structure has saved money it was already spending, and should hand part of the saving back as a rebate for the format.
- **Tokens as currency** (concept) A publisher could be paid in the provider's own credits, which are the budget that builds the site, and News Corp already took part of its deal in credits.
- **The broker** (concept) A single site cannot send the invoice, so the broker will be whoever sits between the bots and the sites, which today means Cloudflare, TollBit and the marketplaces.
- **Baekdal wants an audience** (question) Tokens are not an audience, though structure is what makes a citation land on the right paragraph and tokens are the budget that builds the site the reader arrives at.
- **What would settle it** (question) Three numbers per domain for a week of real retrieval, the tokens spent on HTML, the tokens the twin would have cost and the fetches a change signal would have skipped, live in the providers' logs.

> Every rung exists today. What does not exist is anyone paying for them. The gap the proposal is written to fill: the publisher's half of the exchange is already built.

> It is not new money. It is money being spent today, by the answer engines, on reading the web the hard way. Why a rebate on waste is the easiest money in the negotiation to agree to.

builds on [The future of news is the story vault, not the paywall](#future-of-news-story-vault-not-paywall), [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](#introducing-fractal-semantic-graphs); continued by [Custom UIs are not the exception: the inbox in 2026, where every message has its own universe](#custom-uis-are-not-the-exception), [The reader was always the product: a corrected history of how news got into this mess](#how-news-got-here).

## [A supply chain of vaults: how GenAI, open data and small custom tools could bring the price of food down](supply-chain-of-vaults.md)

2026-09-27 · Vaults & methodStartups & strategy

The food chain is logistics, logistics is a data problem, and a supply chain of encrypted vaults with small custom tools built once by GenAI could bring the price of food down, if somebody runs the experiment.

*[diagram]*
**concept**claim**method**artefact**example**question

**16 nodes, 19 edges**

- **The food pound** (example) For a kilo of supermarket apples selling at £2.20, the grower's costs were 76p and their profit 3p.
- **A chain of spreadsheets** (claim) Each hop keeps its own record of the same consignment, mostly in spreadsheets, and an order, a delivery note, a grade, a price and a payment date are typed in five times.
- **Food lost before retail** (example) The FAO puts the share of food lost between harvest and retail at 13.3% in 2023, and a good deal of it is information.
- **The chokepoint** (concept) Once a buyer holds a large share of a farm's output it names the price, which is the mechanism Giblin and Doctorow call a chokepoint.
- **The limit of regulation** (claim) Codes of practice regulate the conduct of the party with the systems and leave the party without them exactly where it was.
- **All of it is logistics** (claim) Everything between the field and the shelf is a workflow, and logistics is a data problem before it is a transport problem.
- **A supply chain of vaults** (method) Every party in the chain holds its own encrypted, versioned vault, readable by nobody who does not hold a key, including the host.
- **Append lanes** (artefact) Write-only channels through which one party can put a file into another's vault without being able to read anything there.
- **One graph across the vaults** (concept) Each vault keeps its own vocabulary and typed edges join them, which is what makes waste visible.
- **Use GenAI not to use GenAI** (method) The model is used once, to turn a grower's brief into a working tool, and production runs on plain files with no model in the line.
- **Villagers and town planners** (concept) A small company takes the finished tool and runs it for a hundred other growers, paid because it keeps working rather than by the seat.
- **The price hypothesis** (question) The hypothesis is that a supply chain run this way brings the price of food and goods down, and the evidence is partial.
- **The deflation dogma** (claim) The BIS found the link between falling goods prices and lower growth to be weak, and a cheaper loaf because the chain wasted less is not a Japanese lost decade.
- **The cost of not sharing** (claim) About 80% of industrial data is never used, and every grower who learns what a buyer will reject learns it alone.
- **Open-weight models** (concept) Companies that build on open weights can run a near-frontier model inside their own environment and innovate on top of it.
- **The experiment** (question) Nobody has put a grower, a packer and a buyer on vaults and run a season through them, and this article is the brief for that experiment.

> Everything between the field and the shelf is a workflow, and every workflow is a set of records moving between parties. The step that turns a food price problem into a data problem the vaults can address.

> What we never calculate is the economic cost of not sharing. The second memo's argument, that openness is the other half of the case.

builds on [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](#introducing-fractal-semantic-graphs), [The SaaS apocalypse will be decided by inertia, not by AI](#saas-apocalypse-decided-by-inertia-not-by-ai).

## [Before you give an agent a connector, give the connector a twin](connector-twin-before-you-deploy-an-agent.md)

2026-09-24 · Agents & policyVaults & method

If you cannot say what your agent did, what it saw when it did it, and which of its actions you can undo, you are not ready to give it a connector, and a twin of the connector, a journal plus a replay, answers all three.

*[diagram]*
**concept**claim**method**artefact**example**question

**15 nodes, 19 edges**

- **A connector is a grant of action** (claim) An agent with Gmail and Calendar connectors can send, archive, trash, permanently delete, move events, decline invitations and cancel meetings on somebody's behalf, at machine speed.
- **The platform keeps no way back for some actions** (claim) The Gmail API documents its delete as permanent, Undo Send is a feature of the interface not the API, and a moved calendar event has no version history a user can open.
- **What the platform keeps** (concept) Trash windows, an administrator's bulk restore and audit logs record that things happened, but none records what the agent saw when it decided to act, or why.
- **Connector twin** (concept) A journal of every request and response the agent makes, and a replay of that journal into the views the agent saw.
- **Twin, not backup, log or replay** (concept) A backup copies the mailbox, a log is too small, replay is the verb; a twin is an interface to reality, valued for its connection to the real thing.
- **Capture** (method) For every connector call, copy the tool call the agent made, the request sent to the platform and the response received, and never the Authorization header or any token.
- **Append lane** (artefact) A write-only channel gated by a token the writer holds, whose write response is exactly {"ok": true}, so the capture point learns nothing about what else is in the lane.
- **Chain** (method) Each entry carries the hash of the one before it, so a missing, edited or reordered entry shows to anyone holding the read key.
- **When the journal gets processed** (question) On a timer, on a threshold of pending entries, on demand or at the end of each session; the right default will come from a few real users rather than from more design.
- **Replay and revert** (method) A vault app rebuilds the inbox and the calendar as the agent saw them at any step, shows before and after for every change, and writes a revert plan a person approves.
- **The twin is not a copy of the mailbox** (claim) It holds only what passed through the connector, so it scales with the agent's activity rather than with the size of the mailbox.
- **One session, replayed** (example) An invented scheduling assistant makes seventeen calls in under three minutes and writes a true summary that hides a cancellation sent to a supplier and a permanently deleted payment reminder.
- **Undo is a list, not a promise** (claim) Every change gets a grade, reversible, partly reversible or not reversible, and the value of the list is that the red rows are named.
- **Broker, gateway or requirement of the agent** (concept) Three places to capture and three grades of evidence; the mode does not change what is captured, it changes what the evidence is allowed to claim.
- **What it does to the agent's behaviour policy** (concept) With the list of irreversible actions in hand the mandate can say what the agent may do freely, must ask before, and may never do without approval.

> If you cannot say what your agent did, what it saw when it did it, and which of its actions you can undo, you are not ready to give it a connector. The claim the whole article is built to defend, stated so it can be wrong.

> The value of the list is not that most of it is green. It is that the red rows are named. Why the twin changes governance: irreversible actions become a named list the mandate can be written against.

continued by [Footprint and blast radius: what the agent actually did, and what it would have cost](#footprint-and-blast-radius), [Custom UIs are not the exception: the inbox in 2026, where every message has its own universe](#custom-uis-are-not-the-exception), [The ultimate insider: agents, the infrastructure that cannot hold them, and risk management that cannot keep up](#ultimate-insider-three-collisions), [Six agents, one inbox: what a real multi-agent setup taught me about access policies](#six-agents-one-inbox).

## [Every risk is already accepted. The only question is by whom, and for how long.](every-risk-is-already-accepted.md)

2026-09-24 · Agents & policyGraphs & knowledge

Every risk an organisation has is already accepted by somebody, so the only questions are who has accepted it and until when; a register that cannot answer them, on facts, is disconnected from reality.

*[diagram]*
**concept**claim**method**artefact**example

**15 nodes, 19 edges**

- **Every risk is already accepted** (claim) A risk exists the moment the exposure does, so the organisation is carrying it from the start, signed for or not.
- **There is no deny button** (claim) You cannot vote a fact out of existence, and a register that lets you reject a risk lets you pretend.
- **Three doors** (method) Accept it personally for a stated interval, fund the work that reduces it, or fix it so the facts that make it true stop holding; silence is not a fourth door.
- **Unaccepted is critical** (claim) A risk nobody has accepted rests on whoever is nearest and rolls upward to their boss, and then to theirs, until somebody signs.
- **The interval is the decision** (method) One hour means more data, four hours is a priority-one incident, one month is assemble and fund, and six months is do nothing and review it then, with a name on it.
- **Accepted is not acceptable** (concept) Accepted is an act by a named person on a date for an interval; acceptable is a threshold, and the dangerous state is a risk over the line that nobody has signed for.
- **EU AI Act, Article 9(5)** (example) Providers of high-risk AI systems must have residual risk judged to be acceptable, and the Act never defines the word.
- **Every risk has a boss** (claim) Every risk has a holder, every holder has a boss, and every path ends at the board, computed rather than reported, and nobody can accept on anybody else's behalf.
- **Risk Graph Explorer** (artefact) A vault that computes what each role is assigned and what arrives through it, so no risk is orphaned and nobody at the top is surprised.
- **From the board to the bytes** (concept) A board line such as loss of customer funds opens into business, operational and technical risks, each with its own holder and vocabulary, down to the configuration file.
- **Established by facts, ended by facts** (method) Every risk names the facts that make it true and the facts that would end it, so it ships with its own falsification condition.
- **One risk, six weeks** (example) An agent's irreversible production writes are accepted for two weeks, expire with the action undone, escalate, are funded, materialise as an incident and cease on day 42 on evidence.
- **A vault per risk** (artefact) Each material risk deserves a vault as its evidence pack, keeping every fact, acceptance, escalation and incident, readable by each audience with its own key.
- **Why people resist** (concept) Executives resist giving risk owners an acceptance workflow because they understand it would change their job, which makes this a change programme rather than a feature.
- **It fits alongside every GRC platform** (claim) The model reads the register from the platform and writes back what the platform lacks: who accepted, until when, what happens at expiry, and a link to the evidence.

> Every acceptance is for an interval, and the interval is not a detail of the decision. The interval ladder is the model's working part: each length names a different response.

> Nothing in the row is wrong. It just never learned that the risk was accepted twice, expired once, escalated, funded, materialised as an incident, and ended. The air gap between a register and reality, shown on one row at one moment.

builds on [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](#introducing-fractal-semantic-graphs); continued by [Footprint and blast radius: what the agent actually did, and what it would have cost](#footprint-and-blast-radius), [The ultimate insider: agents, the infrastructure that cannot hold them, and risk management that cannot keep up](#ultimate-insider-three-collisions).

## [The future of news is the story vault, not the paywall](future-of-news-story-vault-not-paywall.md)

2026-09-22 · News & evidenceGraphs & knowledge

The story is a graph and the article is a projection, so a newsroom that keeps the graph in a vault can sell five things from it, in pence and on demand, that reward investigative reporting rather than the click or the renewal.

*[diagram]*
**concept**claim**method**artefact**example

**16 nodes, 21 edges**

- **Both models are bad for the reader** (claim) Advertising sells the reader to somebody else, so the content is bait; a subscription charges rent on something most subscribers have stopped using, so the content is the excuse.
- **The two clocks** (example) Organic Google search traffic to publishers fell 33% in the year to November 2025, and the UK's subscription rules were brought forward to 1 January 2027.
- **The objective is a loop, not a price** (concept) A commercial model that rewards investigative journalism, so evidenced reporting drives usage, usage drives revenue that depends on neither search nor renewals, and revenue funds more reporting.
- **Why paying per item failed before** (concept) A $100 subscription lost is 500 micropayments to replace, unbundling breaks the cross-subsidy, and the reader will not stop to decide whether an article is worth twenty pence.
- **Who is standing at the till** (concept) The reader who wants one thing, the firm that has to forward it with its provenance, and the agent paying per query with a wallet and no anxiety; none of them wants the article.
- **The story is a graph, the article is a projection** (claim) A story being reported is claims, evidence, sources, raw materials, analysis and drafts, and the article is one walk through that graph for one audience at one moment.
- **The graph is fractal, and meaning comes from connectivity** (concept) A node means nothing on its own, every edge is a verb with a named inverse, and zooming into any node enters a world with its own vocabulary joined by a single named edge.
- **Trust through provenance, provenance via evidence** (concept) Evidence is frozen bytes with a SHA-256 hash, provenance is the path from a claim down named edges to that evidence, and trust is what a market extends to a source whose provenance has held before.
- **What a story vault holds** (artefact) The published text, the evidence it cites, the story graph it belongs to, the source list, the translations and every prompt and decision that produced it, as one addressable unit.
- **Anonymous sources are marked at the node** (method) A source the journalist cannot name is a node flagged as anonymous, so every projection built from the graph redacts it automatically.
- **Five things to sell from one graph** (concept) The public article free as the door, the licensed article in pence, the evidence vault, the customised projection and the verification API.
- **The evidence vault** (concept) The graph itself, licensed by read key to analysts, lawyers, regulators and other newsrooms, which is the payment that rewards the reporting rather than the click.
- **The verification API** (concept) A company or agent asks whether a claim was reported, is still current and is soundly used, and gets an on-record answer with the chain attached and a warranty.
- **Who gets paid** (concept) 60% to the original researcher, 25% to the data organisation, 10% to the journalist and 5% to the outlet, and you cannot pay the fact creator unless the graph names them.
- **The rails** (concept) The x402 protocol puts a payment inside the HTTP 402 response, settles in about 200 milliseconds and charges no protocol fee, so paying in pence now works.
- **The parts that already run** (example) Hash-verified regulation graphs, a Portuguese newsroom with frozen sources and an editor-gated pipeline, a pentest sold as eight projections, and thirty-one vaults on 295 MB, with the billing not built.

> The news industry sells the one thing whose price is going to zero, the article, and throws away the one thing nobody else has, the evidence the article was made from. The claim stated so it can be wrong; everything else is its long form.

> The story is a graph. The article is a projection. Sell the graph. The shift the five products follow from, in three sentences.

builds on [For a startup, the most important question is whether they miss it](#the-question-is-whether-they-miss-it); continued by [Custom UIs are not the exception: the inbox in 2026, where every message has its own universe](#custom-uis-are-not-the-exception), [The reader was always the product: a corrected history of how news got into this mess](#how-news-got-here), [Sixteen thousand fetches, ten clicks, and a token bill nobody is sending: the case for paying publishers to be easy to read](#token-bill-nobody-is-sending).

## [The SaaS apocalypse will be decided by inertia, not by AI](saas-apocalypse-decided-by-inertia-not-by-ai.md)

2026-09-21 · Startups & strategy

AI is available to both sides, so the SaaS apocalypse will be decided by inertia: where each company sits on the evolution axis and how much past success it has to protect.

*[diagram]*
**concept**claim**example

**15 nodes, 20 edges**

- **The claim, stated so it can be wrong** (claim) Most medium and large SaaS companies will struggle, spectacularly, in the medium term, as companies and individuals build more of what they actually want instead of renting an approximation of it.
- **AI is available to both sides** (claim) The incumbents have the same models the newcomers have, plus more data, more engineers and more money, and if the technology decided this they would already have won.
- **Success breeds inertia** (concept) Wardley's climatic pattern: the pre-existing installed base causes inertia to change, and it is almost always new entrants, unencumbered by past success, who initiate it.
- **Nokia, twice** (example) Nokia met the mobile phone with nothing to protect and dominated for fifteen years; it met the iPhone with fifteen years of success to protect and was gone from the category within seven.
- **The SaaSpocalypse of February 2026** (example) Roughly $285 billion left the sector in about 48 hours after Anthropic shipped Claude Cowork plug-ins, and by September software stocks had rallied about 40% from the April low.
- **The database is the moat** (claim) Investors decided the thing underneath was safe and quietly stopped defending the thing on top; that is not a rebuttal of the apocalypse, it is the apocalypse, priced.
- **Users were never happy** (claim) 91% of employees are frustrated with workplace technology, 80% of features are rarely or never used, and the average organisation wastes $21 million a year on unused licences.
- **The persistence of Excel** (example) 73% of companies prepare VAT returns in Excel; its persistence is the clearest evidence that SaaS failed users, because it is the one tool where they control the shape of the thing.
- **The SaaS product slid right** (concept) On the map, what was a product is commoditising into a substrate, a database, a message bus, a state machine, on which higher-order things get built.
- **Vibe coding is writing good briefs** (concept) Product owners were always describing the software they wanted; the loop from I want this to here it is was weeks or months, and is now minutes.
- **Why incumbents cannot simply do this** (claim) SaaS companies never invested in non-functional requirements, engineers spend 42% of their time on maintenance and bad code, and only 19% of teams are elite performers.
- **The irony** (claim) The things SaaS companies refused to build to protect their moats, portability, open schemas, a real API, data you can take out, are precisely the things an agent needs.
- **The brief is not a product** (claim) The reason you bought SaaS was never the features but that the thing is maintained, and the person who vibe coded a replacement does not want to maintain it.
- **Village and town-planner companies** (concept) Businesses that take the finished brief and run it, maintain, secure, version and deploy it, paid by consumption rather than by the seat, where the handover is a file move plus a version bump.
- **More engineers, not fewer** (claim) We will need as many developers as now and probably more, because somebody has to read, harden and run the code, and larger human-agent teams become possible once communication can be scaled.

> AI is not the deciding factor, because AI is available to both sides. The title's argument in one line: the variable both the panic and the recovery stared at was the wrong one.

> The things SaaS companies refused to build, to protect their moats, are precisely the things an agent needs. The irony the article calls the whole piece in one paragraph: the moat is now what the customer's agent cannot get past.

continued by [A supply chain of vaults: how GenAI, open data and small custom tools could bring the price of food down](#supply-chain-of-vaults).

## [For a startup, the most important question is whether they miss it](the-question-is-whether-they-miss-it.md)

2026-09-21 · Startups & strategy

A startup operating model in three pillars: be profitable, make investors come to you, and open source everything, each buying the position needed for the next.

*[diagram]*
**concept**claim**method**artefact**example**question

**14 nodes, 16 edges**

- **Three pillars** (concept) Be profitable, have investors talking to you, and open source everything, in that order because each one buys you the position you need to do the next.
- **Ship** (method) Shipping means a thing somebody else can go and use, on their own, and get value from, not a proof of concept or a demo.
- **Near-zero running cost** (method) To ship that often the running cost must be near nothing: serverless, as little live state as you can stand, and in our case the file system is the database.
- **Give it away** (method) Hand it to people for free for a short window, because the feedback starts the moment somebody who is not you has the thing.
- **Take it away** (method) The trial expired, it is not available right now, nothing else about the product changes, and no apology is needed.
- **Do they miss it?** (question) If they shrug you have something people will accept when it is free; if they come back and ask for it, you have something.
- **Charge, and charge at a profit** (claim) Two questions, is the price one they are happy to pay and is that price profitable for you, and people routinely answer only the first.
- **No subscription by default** (claim) Charging rent for something people are not using is a worse business than being paid when you deliver.
- **Raise from strength** (claim) The worst possible time to raise money is before you are profitable, because you are bargaining from weakness and the worst terms are about control.
- **Do not get signed before you have the album** (example) Write the songs, record them, get people buying, then take the record deal as somebody who already has an audience.
- **Open source everything** (method) It sounds like giving away the asset and is the opposite, for five reasons that each stand alone.
- **The technology is not the moat** (claim) Treating it as open from the start forces you to find the thing that actually is defensible, usually the data, the relationships, the distribution, or the speed at which you ship.
- **You leave with your tools** (claim) Build in the open and the work is still yours when you move on.
- **The vault as substrate** (artefact) A vault carries data, app, history and sources as one string, with no database to run and no hosting for the reader, so shipping a small product is cheap, fast and reversible.

> It means a thing somebody else can go and use, on their own, and get value from. The definition of shipping that the whole loop depends on.

> The worst possible time to raise money is before you are profitable, before you have the product, before you understand the fit. Pillar two stated plainly, and the reason profitability comes first.

builds on [Price it, then give it away: the early access programme as the next step after "do they miss it"](#price-it-then-give-it-away); continued by [Price it, then give it away: the early access programme as the next step after "do they miss it"](#price-it-then-give-it-away), [The future of news is the story vault, not the paywall](#future-of-news-story-vault-not-paywall).

## [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](introducing-fractal-semantic-graphs.md)

2026-09-20 · Graphs & knowledge

Every unit of knowledge is already a graph in its owner's vocabulary, and a short shared grammar rather than a shared schema is what lets any node in one world link to any node in another, up or down, without an adapter.

*[diagram]*
**concept**claim**method**artefact**example**question

**15 nodes, 18 edges**

- **Fractal Semantic Graph** (concept) A fractal semantic graph has no privileged level and no single schema; zoom into any node and you enter a new world with its own node types, verbs and taxonomy.
- **Semantic graph** (concept) A semantic graph gives the edges meaning: every edge is a verb, and every verb has a named inverse, so a link reads correctly from whichever end you are standing at.
- **Ontology** (concept) An ontology is the agreed vocabulary of node types and verbs that a graph is allowed to use, and each altitude gets its own.
- **The jump** (method) On one link in a risk register you can jump into another universe, from an incident to security operations to the DNS estate to a single TCP packet, and nobody built an adapter.
- **Everything is already a graph** (claim) A regulation, a PDF, a spreadsheet, a codebase and a JSON document are already graphs; each one only needs its edges named.
- **The five-rule grammar** (method) Every edge is a verb with an inverse, relates_to is banned, properties carry data never meaning, supersede never delete, and never render the whole graph.
- **relates_to is banned** (claim) An edge with no verb constrains nothing and cannot narrow a query; the granularity of the verb is the precision of the question you will later be able to ask.
- **Provenance comes free** (claim) When the leaf is a word connected to the byte range it came from and the hash of the file that held it, every claim at every altitude above it is traceable to source.
- **The ladder of eleven altitudes** (artefact) Eleven altitudes, each a live graph in its own vocabulary, from the law down to the compute instance, every rung joined to the next by a named edge.
- **Regulation Graph** (artefact) The EU AI Act parsed from the official XML into 1,523 nodes and 1,944 edges, with the SHA-256 of the retrieved bytes at the end of every provenance chain.
- **The crosswalk finding** (example) Joining the AIUC-1 standard to the regulation graph showed that 8 of the 27 articles reached have since been amended, a finding that existed in neither graph on its own.
- **GDPR Article 45** (example) The text has not changed a word since 2016 while what it permits has flipped four times, drawn as a timeline of ruling nodes over one unchanged article node.
- **Threat model zoom ladder** (artefact) Eleven linked models, 51 nodes and 179 threats, tracing a single SQL injection from the method it lives in to the revenue it puts at risk.
- **What is still modelled rather than imported** (question) The bottom four rungs are placed by an author, enterprise architecture is missing, crosswalks resolve at article level only, and the agent rung is a vocabulary not yet a join.
- **Why now** (claim) Naming edges became the cheap part, agents acting on the world make provenance mandatory, and the schema wars are over because nobody won.

> There is no top and no bottom. There is only the altitude you happen to be looking from, and how much definition you choose to load at it. The definition of fractal in one line: no privileged level, no single schema.

> Two graphs, built by different people for different purposes in different vocabularies, joined by declared edges, produced a finding that did not exist in either of them. The evidence that the method does work, not just that it is defined: the amended-articles finding came from the join.

continued by [Custom UIs are not the exception: the inbox in 2026, where every message has its own universe](#custom-uis-are-not-the-exception), [The ultimate insider: agents, the infrastructure that cannot hold them, and risk management that cannot keep up](#ultimate-insider-three-collisions), [The reader was always the product: a corrected history of how news got into this mess](#how-news-got-here), [Sixteen thousand fetches, ten clicks, and a token bill nobody is sending: the case for paying publishers to be easy to read](#token-bill-nobody-is-sending), [A supply chain of vaults: how GenAI, open data and small custom tools could bring the price of food down](#supply-chain-of-vaults), [Every risk is already accepted. The only question is by whom, and for how long.](#every-risk-is-already-accepted).

## [The proof is two clicks behind the claim, what the homepage gets wrong, and the fix](proof-behind-the-claim.md)

2026-09-07 · Site & engineeringVaults & method

Encryption is a property you cannot look at, so the homepage should put the real vaults a visitor can open before the mechanism, and should not carry a claim that no published vault demonstrates.

*[diagram]*
**claim**method**artefact**example**question

**13 nodes, 15 edges**

- **Twenty-five published vaults** (artefact) Three weeks ago the site had four published vaults; today it has twenty-five, built by several agents working with one human, including a pentest report with a retest script per finding and a standard rebuilt as a citable graph.
- **Encryption is a property you cannot look at** (claim) Zero knowledge cannot be seen either, so the visitor is asked to take the value on faith before being shown anything.
- **The terminal walkthrough** (example) The hero's create, commit, history and clone walkthrough demonstrates familiarity, which is a virtue, but not power.
- **Use cases as categories** (example) Five use-case cards, each a category rather than a thing, while the vault that embodies the category sits one level down.
- **The proof is a table, two clicks away** (claim) A table is the right shape for finding a vault and the wrong shape for being convinced by one, and it is under a dropdown two clicks from the hero.
- **Opened by one string** (claim) Both proof vaults are opened by one string, run entirely in the browser, ship with their data, sources and tests, and require the visitor to click rather than to understand encryption.
- **Agents build for each other** (example) A brief published on 6 September was read by another agent who built a vault from it the same day, and the API team's correction is now published above the mistake.
- **The briefs page as a log** (example) The collaboration record is filed under Docs, three levels from the homepage, written as a log, which is the right format for the record and the wrong one for a first-time reader.
- **The claim with no artefact** (question) The homepage says a human reviews the merge of agents' branches, and no published vault shows two agents' branches and a human merge in its history.
- **Reorder so proof comes before mechanism** (method) The hero shows four real vaults as cards, then six vaults chosen by job, then the team story, then the terminal walkthrough and the zero-knowledge explanation.
- **Generated from the same data** (method) The six vaults chosen by job are generated from the same data as the table, so they never go stale.
- **A page that says who is behind it** (artefact) A beta tool that asks people to publish their read keys is asking for trust, so there will be a page about who builds sgit, borrowing Interests declared and Reach me, or correct me from a sibling site.
- **The site card** (artefact) A card describes a sibling site the way it describes itself, from its entry in the network directory, because a bare link does not say this continues elsewhere, on purpose.

> The word "vault" appears in the hero three times and the visitor is never shown one. The diagnosis in one line: the homepage names the thing and never shows it.

> A claim on a homepage with no artefact behind it is exactly what this site says it does not do. The gap the article names against itself: the multi-agent merge claim has no published vault behind it.

continued by [The proof moved up, the homepage after the rebuild, next to the before pictures](#proof-moved-up).

## [The proof moved up, the homepage after the rebuild, next to the before pictures](proof-moved-up.md)

2026-09-07 · Site & engineeringVaults & method

The homepage stopped being a page somebody edits and became a view over the site's own data, with real vaults placed before the mechanism and the one unproven claim left unpretended.

*[diagram]*
**concept**claim**method**artefact**example**question

**12 nodes, 14 edges**

- **The reframed sentence** (claim) The hero changed from "the encrypted git for humans and AI agents" to "a vault is a unit of work: data, app, history and sources, shipped as one string", with encryption as the subordinate clause.
- **Four real vaults in the hero** (artefact) Four published vaults with their screenshots sit under the sentence, chosen by a hero field in the vault data, so changing the front door is a data edit, not a page edit.
- **What people actually ship** (artefact) Six vaults chosen by the job they do, hand over a report, publish a standard, give a talk, pitch an investor, ship a game, give an agent a workspace, and none of the six lines is about encryption.
- **A vault as a unit** (concept) Retest scripts that travel with the findings and cited papers that never separate from the deck are properties of a vault as a unit, which a newcomer can actually feel.
- **One human, a team of agents** (artefact) A band with four numbers computed at build time, releases, vaults, sibling sites, briefs, and the loop told in three beats with the artefacts linked.
- **The numbers are not typed** (method) Releases come from the version log, vaults from the vault data, sites from the network directory and briefs from the briefs page, so a wrong number means the site is wrong somewhere else too.
- **What was cut** (example) The abstract use-case band and the three-doors band were cut, and the terminal walkthrough moved down under the heading Under the hood, it is git.
- **Nine bands before, nine after** (example) Three bands were cut and three added, corrected in v0.2.61 after counting rather than remembering, and 1,370 words became 1,332 with ten screenshots.
- **What it cannot show yet** (question) No published vault demonstrates two agents on one vault, their branches and a human merging them, and the team band is written so that it does not pretend otherwise.
- **admin/content/vaults.json** (artefact) One file now drives the hero cards, the six jobs, the sortable table and the vault count; adding a vault is adding a row and promoting one is setting a field.
- **The homepage as a view over data** (claim) The homepage stopped being a page somebody edits and became a view over the site's own data, the rule the articles band, network directory and update feed already followed.
- **Beside the before pictures** (method) The rebuild is put next to the previous article's screenshots so the comparison can be made honestly, including what it still cannot show.

> If a number on that band is wrong, the site is wrong somewhere else too, and that is the right dependency. The rule behind the rebuild: nothing on the homepage is typed, everything is computed from the site's own records.

> That is the trade: pictures of real things instead of paragraphs about them. What actually changed, stated against the byte and word counts rather than as a slogan.

builds on [The proof is two clicks behind the claim, what the homepage gets wrong, and the fix](#proof-behind-the-claim).

## [A chat box on a site with no server, the plan, and the trade it makes](chat-on-a-static-site.md)

2026-08-27 · Site & engineering

With no server to hold a key, a chat box on a static site has three honest tiers: a local matcher, a key in the reader's browser, or a vault app with a bridge, and only one of those is free.

*[diagram]*
**concept**claim**method**artefact**example**question

**14 nodes, 18 edges**

- **The constraint nobody can design around** (concept) sgit.ai is a static site on GitHub Pages with no server, no session and no place to keep a secret, and every sibling on *.sgit.ai is the same.
- **The catalogue** (artefact) Nineteen theses, summaries and categories, emitted at build time from the same data the cards and the table are built from.
- **Tier 0, match** (method) A deterministic scorer runs in the browser against the catalogue of all nineteen sites and shows you which words it matched on.
- **A reader should never have to hold a credential to use an index** (claim) The property that made the local matcher the default: it is instant, free, private, works offline and tells you why it chose.
- **Tier 1, bring your own key** (method) Paste an OpenRouter key and the browser calls the model directly, streaming, with the catalogue as the system prompt.
- **The key lives in this page's origin** (concept) With no host there is no permission floor, so the key goes into localStorage and a fetch to openrouter.ai, and the page cannot protect it the way a vault app can.
- **Degrade to what works** (method) When the model call fails the panel falls back to Tier 0 and says so, because degrading to something that works beats an error message.
- **The SG/Vault workbench vault** (example) The workbench vault already calls the same OpenRouter endpoint with the versioned sg-llm-request module, so the BYOK client reuses a proven pattern.
- **Tier 2, the bridge** (method) Serve the directory as a vault app so the key lives in .vault/llm/config.json below the permission floor, the host makes the call and the app never sees the credential.
- **Permission floor** (concept) The line below which a vault host keeps the key, with an sg.llm API whose grants default to deny and a chat panel every existing vault app gets without being changed.
- **The bridge protects your key, not all egress** (claim) The bridge protects the credential you trusted it with; it does not yet stop a malicious app calling a provider with a credential of its own.
- **Ask this site** (artefact) Ten days later every page carries a pane whose model is given seven tools that run in the page over an index the build emits, and the pane shows every call it made.
- **One site's copy, not a versioned module** (question) The site-wide pane is still one site's copy rather than a versioned module the other eighteen sites can load, and that row decides whether this was worth doing.
- **Routing, not teaching** (claim) The panel points you at a site rather than answering questions about the subjects, because a summary that drifts from the arguments is worse than a link that does not.

> The important property: a reader should never have to hold a credential to use an index. The rule that makes the free local matcher the default rather than the model.

> A chat box on one site is a feature. The same panel on all nineteen, reading each site's own catalogue, is the thing that makes a network of nineteen sites navigable, and it is why the catalogue is generated rather than written. Why the piece is about a network's navigation rather than one widget.

continued by [Custom UIs are not the exception: the inbox in 2026, where every message has its own universe](#custom-uis-are-not-the-exception).

## [Twenty sites in fifteen days, and what that did to the writing](nineteen-sites.md)

2026-08-26 · Site & engineeringVaults & method

A body of work outgrew the site it was published in and split into nineteen siblings so each argument could keep its own version history, and the index into them starts from the reader's question rather than a list of names.

*[diagram]*
**concept**claim**method**example

**12 nodes, 14 edges**

- **Twenty repositories in fifteen days** (example) On 11 August this was one website; by 26 August there were twenty repositories, nineteen of them siblings on *.sgit.ai, fifteen created in the last five days.
- **A section is a promise** (concept) A section promises that something is part of the thing it sits inside, and that promise stopped holding when the writing answered questions that were not about sgit.
- **Its own version history** (claim) Nineteen arguments moving at different speeds through one release log produces a record nobody can read; split, each gets its own record of when it changed its mind.
- **Discovery got worse** (claim) Nineteen domains is not a menu; names like nfrs.sgit.ai and issues-fs.sgit.ai mean nothing until you already know what they argue.
- **Consistency by discipline** (claim) One site has one stylesheet by construction; nineteen have one stylesheet by discipline, and discipline is the thing that quietly stops happening.
- **Cross-link drift** (example) The audit found graphs.sgit.ai pointing at sentinel.sgit.ai, which does not exist; the site is sg-sentinel.sgit.ai, one character of drift and the link is dead.
- **Start from the question** (method) The directory starts from the question the reader arrived with, seventeen lines of it, then five groups by area, then a table of all nineteen.
- **Every thesis in the site's own words** (method) Each thesis on the directory page is quoted from the site's H1 or lede rather than summarised, because a summary drifts and a quotation either matches or is visibly wrong.
- **Same generator, same release script** (method) Same generator, same stylesheet, same release script, same validator, same rule that publishing is adding one file.
- **Publishing is adding one file** (claim) Adding the twentieth site is writing one markdown file, the same property that lets two agents publish on the same day without conflict.
- **skills.sgit.ai, not published yet** (example) One of the nineteen has a repository and a DNS record and nothing behind it, listed as not published yet rather than quietly omitted.
- **Arguments, not products** (claim) sg-sentinel says NOT BUILT, risks states zero lines of code implement its model, wardley-maps is PROPOSED: publish the argument before the thing exists and say what it is worth.

> A summary drifts. A quotation either matches or is visibly wrong. The rule that keeps the directory honest, and the reason the index quotes each site rather than describing it.

> One character of drift, and the link is dead. The concrete cost of splitting: a link between sites is a claim about another site that has to be checked.

builds on [Git for things you cannot put on GitHub](#what-sgit-is).

## [Git for things you cannot put on GitHub](what-sgit-is.md)

2026-08-25 · Vaults & method

sgit gives the files people say they cannot put on GitHub the history, branches and shareable links of git, on a server that holds ciphertext and nothing else.

*[diagram]*
**concept**claim**artefact**example

**13 nodes, 18 edges**

- **Files with nowhere good to live** (concept) A risk register with real system names, a regulatory analysis still being argued about, the working memory of an AI agent, client material under NDA.
- **sgit** (artefact) sgit is git for those files: encrypted before they leave your machine, versioned exactly like git, stored on a server that cannot read a single byte.
- **Zero knowledge, precisely** (claim) The server holds ciphertext and nothing else, not your filenames, not your directory structure, not your commit messages.
- **No key escrow** (claim) There is no key escrow, no admin override, no support engineer who can recover it for you, and that last part is a feature with a real cost.
- **Vault key** (concept) A single string that is three things at once, the address of the vault, the authorisation to write to it, and the key that decrypts it.
- **Read key** (concept) Derived one way from the vault key, same vault, read-only, safe to publish, and that asymmetry is the whole sharing model.
- **Release tripwire** (artefact) No vault key has ever been published, a rule enforced by a tripwire in the release pipeline that scans every file before either remote is touched.
- **Content-addressed over ciphertext** (concept) The object's name is a SHA-256 of the encrypted bytes, so the host can deduplicate it, cache it and serve it from a CDN while unable to tell you what it is.
- **A real version control system** (claim) Multi-parent commits, a tree per directory, deterministic refs derived by HMAC, a genuine merge-base computation and three-way merge, on content the server cannot interpret.
- **Nineteen vaults you can open** (example) Every vault on sgit.ai is live, and cloning all nineteen from their published keys gave 1,389 files and no failures.
- **Capability without credential** (concept) A vault can contain an application that requests no permissions and still renders the whole risk graph, because the host reads the vault and passes results in.
- **The network of sites** (artefact) sgit.ai is one of nineteen sites on *.sgit.ai, each taking one question further than a section could.
- **Checkable rather than impressive** (claim) Each site publishes its argument before the thing exists and states plainly what has shipped and what has not.

> Lose it and the data is gone. Leak it and someone can rewrite your history. The two costs of a vault key being address, authorisation and encryption key at once.

> We would rather be checkable than impressive. The house style that the live vaults, the version log and the NOT BUILT pages all follow.

continued by [Twenty sites in fifteen days, and what that did to the writing](#nineteen-sites).

## [Seven vaults, one method](seven-vaults-one-method.md)

2026-08-19 · Vaults & method

A repeatable method for publishing encrypted vaults, each rule learned by getting something wrong first, starting with classifying the credential before it touches anything.

*[diagram]*
**concept**claim**method**artefact**example

**14 nodes, 19 edges**

- **Classify the credential** (method) Classify the credential before it touches anything, because three of the seven vaults arrived as a vault key described as a read key.
- **Vault key** (concept) A vault key is write access, and because it is also the address and the encryption root there is no revocation, no rotation, and no undo.
- **Read key** (concept) A read key is 64 hex characters, derived one-way from a vault key, and safe to publish.
- **check_credential.py** (artefact) A script that classifies a credential by shape, exits 0 for publishable and 1 for stop, and never echoes what it was given.
- **Release validator tripwire** (artefact) The release validator scans every tracked file for any key-shaped string and for the actual passphrases, and has caught its own author three times.
- **Derive rather than refuse** (method) A submission that cannot be published can still become one that can, by deriving the read key and putting the vault key in a gitignored tier.
- **Strictly less capability** (claim) The whole shape of the project is a capability you can hand over that is strictly less than the one you hold, with the reduction enforced by mathematics rather than by policy.
- **Audit with the key you publish** (method) Audit every file with exactly the credential a reader will have, not with the vault key.
- **Sealed LLM credential check** (example) One vault carried a sealed LLM credential, and attempting to open it with the published read key got InvalidTag from AES-GCM, so no budget was exposed.
- **Risk Graph Explorer** (artefact) The sixth vault was public by design, with its own PUBLIC.md whose third rule, no metered capability behind a published read key, was adopted into the guidance.
- **Capture evidence by driving the real product** (method) Every screenshot is taken by opening the actual vault in a real browser with the published read key, and the rig grew an appProbe step to ask the app what its elements are called.
- **Describe, show, then admit** (method) Every vault page ends with what the vault does not do, as a section with the same weight as the features.
- **Publishing playbook** (artefact) The method is written down as a playbook aimed at another site's agent rather than at us, which was the real test of whether it was a method or just a habit.
- **The honest ledger** (claim) Three vault keys caught, one budget exposure checked and cleared, one upstream rule adopted, and three bugs found by testing rather than assumption.

> Which is the point: a rule that only catches other people is not a rule. The tripwire catching its own author is what turns a habit into a control.

> A published vault is an argument that this way of working is sound; an argument that omits its own edges is a brochure. The reason every vault page ends with what the vault does not do.

continued by [Custom UIs are not the exception: the inbox in 2026, where every message has its own universe](#custom-uis-are-not-the-exception).

## [Green does not mean live](green-does-not-mean-live.md)

2026-08-17 · Site & engineering

Shipped is a fact about the reader, not about your repository, so a release has to verify the boundary the reader is on and not only the ones the repository can see.

*[diagram]*
**concept**claim**method**artefact**example**question

**12 nodes, 15 edges**

- **Two releases that never reached anybody** (example) Two consecutive releases pushed cleanly, printed both remotes in sync, and the site served a two-release-old page for forty minutes until a human on a phone asked if it was the latest version.
- **The version badge** (artefact) The badge on the home page that a human looked at to notice the miss, and that the release now polls for the new version.
- **Checking the wrong boundary** (claim) The checks were not weak; they were checking the wrong boundary.
- **What the release actually verified** (method) Build the site, run the validator, commit and push the encrypted vault and confirm sync, commit and push the git mirror and confirm HEAD equals origin/dev.
- **The bytes arrived at GitHub** (concept) HEAD == origin/dev compares hashes, not hopes, but it means the bytes arrived at GitHub, not that anybody can read them.
- **Three boundaries, two verified** (concept) Source to git remote, git remote to Pages deploy, Pages deploy to the reader; a GitHub Actions job sits in the unverified gap and reports into a system neither remote knows about.
- **What actually failed** (example) The deploy job died in Set up job because codeload.github.com rate-limited the download of actions/configure-pages with a 429, while the validate and tag-release jobs passed.
- **The most likely thing to break is not your code** (claim) It is a piece of shared infrastructure you do not run, on a day you were not thinking about it.
- **Ask the live site what version it is serving** (method) A release now polls sgit.ai with a cache-buster for the new version, up to eight minutes, and aborts loudly if it never appears, naming the Actions page.
- **Shipped is a fact about the reader** (claim) Shipped is a fact about the reader, not about your repository.
- **Three rules of the same shape** (method) A page nothing links to, a page the machine index omits, and a page the deploy never served are all unpublished, and the build or the release fails on each.
- **What this does not fix** (question) It detects a failed deploy but does not repair one, it checks only the home page's badge so a partial deploy would pass, and it adds up to eight minutes to every release.

> The checks were not weak. They were checking the wrong boundary. The diagnosis: strong checks on the wrong side of the deploy.

> All three are the same claim: shipped is a fact about the reader, not about your repository. The general rule the fix joins, learned from three failures of the same shape.

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/articles/graphs.html)*
