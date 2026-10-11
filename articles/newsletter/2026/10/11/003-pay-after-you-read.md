# Issue 3: Pay after you read, no server by design, and authority that sits outside the model, SGit Newsroom

> Three days and twenty-four articles. The reading meter went from an experiment to a working model: you pay for the share of a page you read, you say how useful it was and that sets the price, your balance can go below zero without a word of nagging, and your reading builds personas that are yours. Underneath it, the whole newsroom now runs in the reader's browser, with a language model arriving in the tab as the last piece. And from the other side of the network, an answer to Satya Nadella on models as insider risks, and Microsoft's new agent containers mapped to the behaviour policies they make enforceable.

*Source: <https://sgit.ai/articles/newsletter/2026/10/11/003-pay-after-you-read.html> · site v0.7.47 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../../../index.md) / [SGit Newsroom](../../../../../articles/index.md) / [Newsletter](../../../../../articles/newsletter/index.md) / Issue 3

SGit Newsroom · Issue 3 · 2026-10-11

# Pay after you read, no server by design, and authority that sits outside the model

By [Dinis Cruz](../../../../../about/index.md), written with the [Journalist](../../../../../newsroom/roles/journalist.md)

***Abstract:** Three days and twenty-four articles. The reading meter went from an experiment to a working model: you pay for the share of a page you read, you say how useful it was and that sets the price, your balance can go below zero without a word of nagging, and your reading builds personas that are yours. Underneath it, the whole newsroom now runs in the reader's browser, with a language model arriving in the tab as the last piece. And from the other side of the network, an answer to Satya Nadella on models as insider risks, and Microsoft's new agent containers mapped to the behaviour policies they make enforceable.*

What would you pay for an article, if you only paid after you had read it, and only as much as it was worth to you? Most of what was published between 9 and 11 October is the answer to that question, built and tested one release at a time, and the infrastructure that let it be built in an afternoon. The rest is the same idea from the agents' side: a limit is only a limit if the thing it limits cannot change it.

Three days in six pictures, one from each of the lead articles

## Pay after you read

The reading meter started on 10 October as a demonstration, a few pence a page from five pounds of credit kept in the browser. By the end of the afternoon it was something else. [Pay after you read](https://sgit.ai/articles/pay-after-you-read.html) tells how, in seven releases in under four hours, each one coming from using the one before:

>

You pay after you see the value.

You pay for the share of a page you scroll through, not for opening it. At the foot of each article you say how useful it was, and that sets the price, from free to double. Your balance can go below zero and stay there; nothing is blocked and nothing nags. [Going live with the reading meter](https://sgit.ai/articles/going-live-with-the-reading-meter.html) wrote down the business case, the numbers we expect and the ones that would prove us wrong, before the first payment:

>

And going below zero is not a failure state.

Six changes, and five hypotheses written down before the first payment, each with what we expect and what would prove us wrong.

The payment link is now live on newsroom.sgit.ai, so the eight weeks have started, and the hypotheses will be reviewed on 6 December. [Who will game the reading meter](https://sgit.ai/articles/who-will-game-the-reading-meter.html) is the security side: eight kinds of reader, none of them attackers, nine ways to cheat a meter kept in the browser, and why every one of them is allowed. Its sharpest line is about agents, which move between kinds of reader in a single request:

>

An agent is not a step; it is a lift.

## Your reading, kept by you

The meter keeps a history because a ledger has to, and that history builds a persona: a name, a front page of its own, and a graph you can watch grow. [Pay to keep your persona](https://sgit.ai/articles/pay-to-keep-your-persona.html) argues that this, not guilt, is what a reader would pay for: time, context, focus, and a persona that follows you between devices.

>

The reader should pay because paying helps them.

A newsroom of your own: picks for each persona, the graph of what you read, and the card where you rate what you read

[A link to a persona](https://sgit.ai/articles/a-link-to-a-persona.html) is the next step, written as a brief: personas kept in a vault by the newsroom's own agents, so that a link can open the newsroom as a CISO, a data protection officer or one particular person, and the reader can follow the persona or make it their own.

>

The better move is for the person who sends the link to choose it

## No server, by design

None of that runs on a server. [No server, by design](https://sgit.ai/articles/no-server-by-design.html) explains the choice: first the database was retired, the file system took its place, and now the back end is retired too. What is left on the server side is commodity, static hosting and a vault server that stores ciphertext it cannot read:

>

It is no servers of mine with logic in them.

The SGit Newsroom's architecture: every piece of application logic runs in the reader's browser.

[A model in the tab](https://sgit.ai/articles/a-model-in-the-tab.html) is about the hardest remaining piece. Chrome now ships a language model that any page can prompt, offline, on capable desktops. It is real and it has rough edges, and the objections to it are serious; the way through is to keep the meaning where it belongs:

>

The way to build on it without being captured by it is to keep the meaning in the data, not in the prompt.

Two pieces underneath it all were also written up: [where the vault keys live](https://sgit.ai/articles/where-the-vault-keys-live.html), on how a key travels sealed to a registry instead of through a chat, and [RFC 0001](https://sgit.ai/articles/rfc-0001-public-key-cryptography-for-sgit.html), a request for comments on two key pairs so that a reader cannot write.

## The agent is the reader

The newsroom's articles are long, so [one article, five readers](https://sgit.ai/articles/one-article-five-readers.html) sends five agents through each one after it is written: a librarian, a cartographer, a historian, an explainer and a storyteller. [The agent is the reader](https://sgit.ai/articles/the-agent-is-the-reader.html) does the arithmetic on what that produces. A curated graph answers a question about a concept in a median of 2,579 tokens, against 25,698 to read the five articles:

>

If a publisher saves an agent more tokens than it charges, paying is rational.

What five articles became, in tokens: the catalogue is large, and what an agent loads from it is small.

Two more pieces on making things with agents: [how to run synthetic users](https://sgit.ai/articles/how-to-run-synthetic-users.html), five invented readers driving a real browser, which found bugs every test had passed over; and [the infographic bake-off](https://sgit.ai/articles/the-infographic-bake-off.html), every image model on OpenRouter given eleven briefs, 101 images judged blind, for $10.44.

## Authority outside the model

Satya Nadella published seven principles for treating models as insider risks. [Authority outside the model](https://sgit.ai/articles/authority-outside-the-model.html) answers them one by one, with what we run, what is only designed and what is argued, and names five things the list leaves out. Its core is the test this network has used for a while:

>

a control bounds a grant only if it is enforced by something the grant does not include.

[The same argument, in our words](https://sgit.ai/articles/the-same-argument-in-our-words.html) translates his post idea by idea into the vocabulary of behaviour policies, and finds the same ending read from the other side:

>

the more you can constrain an agent, the more you can trust it, and the more autonomy you can afford to give it.

[Where the platform draws the line](https://sgit.ai/articles/where-the-platform-draws-the-line.html) reads Microsoft's new execution containers and agent control specification field by field. The platform bounds what it can see, files, addresses and processes, and the business logic is above that line. That is the shared responsibility model again, and rows of a behaviour policy that were hope can now become boundaries:

>

an agent must not be the one that decides its own limits.

The shared responsibility model, drawn for agents: each layer can only name what it can see.

Closer to home, [a second reader the agent cannot skip](https://sgit.ai/articles/a-second-reader-the-agent-cannot-skip.html) is a hook that makes a second model approve every email draft, failing closed, after two went out in my voice despite a written rule; [re-anchoring](https://sgit.ai/articles/re-anchoring-agent-behaviour-policies.html) prints an agent's rules back after each summary of a long session; and [how I work with Claude](https://sgit.ai/articles/how-i-work-with-claude.html) is the practical guide behind all of it.

## Everything published from 9 to 11 October

Twenty-four articles were published from 2026-10-09 to 2026-10-11, grouped below by what they are about.

### Paying for reading

The reading meter, from the first version to a working model, and who could game it.

- [**Pay after you read: how a reading meter became a working business model in one afternoon, one release at a time**](../../../../../articles/pay-after-you-read.md). Seven releases in one afternoon turned the reading meter into a working model: pay after you read, and the rating sets the price.
- [**Going live with the reading meter: pay for what you read, go below zero if you like, and the numbers we will check in eight weeks**](../../../../../articles/going-live-with-the-reading-meter.md). Pay for the share of a page you read, go below zero with no nagging, top up £5 on Stripe: the plan, and the numbers we check in eight weeks.
- [**A meter in the browser: a penny a page, a history you keep, and a site that picks for you**](../../../../../articles/a-meter-in-the-browser.md). Every page now costs a few pence from £5 of credit kept in your browser, and the reading history it keeps is what personalises the site.
- [**Who will game the reading meter? Eight kinds of reader, nine ways to cheat, and the risks that will actually happen**](../../../../../articles/who-will-game-the-reading-meter.md). Eight kinds of reader, none of them attackers, nine ways to cheat a browser meter, and the quieter risks that will actually happen.
- [**Pay to keep your persona: readers should pay because it helps them, not because they feel they should**](../../../../../articles/pay-to-keep-your-persona.md). Readers should pay because it helps them: a persona with a name and a graph, several for focus, and one that follows you between devices.
- [**A link to a persona: send people to the newsroom as someone, not as nobody**](../../../../../articles/a-link-to-a-persona.md). Send a CISO to the newsroom as a CISO: personas kept in a vault by the newsroom's agents, opened from a link, followed or forked.

### No server, by design

The newsroom in the browser, a model in the tab, and the keys and cryptography underneath.

- [**No server, by design: first I retired the database, now I am retiring the back end**](../../../../../articles/no-server-by-design.md). First the database went, now the back end: the SGit Newsroom runs all its logic in the browser, on commodity servers that cannot read your data.
- [**A model in the tab: Chrome now ships an LLM to capable desktops, and it is the hardest piece of the client-side puzzle**](../../../../../articles/a-model-in-the-tab.md). Chrome now ships a language model any page can prompt, offline, on capable desktops. The last piece of the client-side puzzle, with rough edges.
- [**Where the vault keys live: key management at sgit-ai v0.20.0, and what comes next**](../../../../../articles/where-the-vault-keys-live.md). Vault key management at sgit-ai v0.20.0: the one secret, where keys are kept, how they travel sealed on append lanes, and what comes next.
- [**RFC 0001: two ways to add public-key cryptography to sgit, and the questions we want you to answer**](../../../../../articles/rfc-0001-public-key-cryptography-for-sgit.md). A Request for Comments: two key pairs so a reader cannot write, sealed files only named people can open, and fourteen questions for reviewers.

### Reading and making with agents

Five agent readers, what their graphs save, synthetic users, image models judged blind, and a governance stack as a graph.

- [**One article, five readers: a librarian, a cartographer, a historian, an explainer and a storyteller read the same piece**](../../../../../articles/one-article-five-readers.md). Write the article first, then send five agent readers through it: a catalogue, an ontology and maps, the arc, two minutes, and a deck.
- [**The agent is the reader: why agents will pay for graphs, personas and signed claims, because it is cheaper than not paying**](../../../../../articles/the-agent-is-the-reader.md). Agents pay to read the raw web and guess its meaning. A curated graph answers for 90% fewer tokens, so paying the publisher is cheaper than not paying.
- [**How to run synthetic users on your own site: five people who do not exist, a browser, and an afternoon**](../../../../../articles/how-to-run-synthetic-users.md). Five invented users, a model reading screenshots, and a real browser: how to run synthetic users, from three studies.
- [**The infographic bake-off: which image model for which job, judged blind on 10 October 2026**](../../../../../articles/the-infographic-bake-off.md). Every image model on OpenRouter, eleven briefs, 101 images judged blind, $10.44: which model for which infographic, and what it costs.
- [**The AI governance stack, as a graph: an answer to Hari Kota, built**](../../../../../articles/the-ai-governance-stack-as-a-graph.md). Hari Kota's ten-layer AI governance stack, kept as posted and turned into a fractal semantic graph: the gaps become missing edges, and queries.

### Authority outside the model

Models as insider risks, the platforms that now enforce some of the limits, and the controls we run on our own agents.

- [**Authority outside the model: an answer to Satya Nadella on models as insider risks, principle by principle, with what we run, what we ship and what we plan**](../../../../../articles/authority-outside-the-model.md). Satya Nadella's seven principles for models as insider risks, answered one by one: what we run, what is design, and the five things the list leaves out.
- [**The same argument, in our words: Satya Nadella on models as insider risks, translated into the language of RiskMandate**](../../../../../articles/the-same-argument-in-our-words.md). Satya Nadella's case for treating models as insider risks, translated idea by idea into our vocabulary: reach, mandate, gap, barriers and accepted risk.
- [**Where the platform draws the line: Microsoft Execution Containers, the shared responsibility model for agents, and the business logic above it**](../../../../../articles/where-the-platform-draws-the-line.md). Microsoft's MXC and ACS, briefed field by field and mapped to Agent Behaviour Policies: the platform bounds what it can see; the business logic is above.
- [**Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not**](../../../../../articles/riskmandate-ten-questions.md). Ten hard questions from a conference, answered in a two-hour interview: what RiskMandate does, what it deliberately is not, and how mature each part is.
- [**A second reader the agent cannot skip: how two wrong emails became a gate on every draft**](../../../../../articles/a-second-reader-the-agent-cannot-skip.md). Two emails went out in my voice despite a written rule. The fix: a hook that makes a second model approve every draft, failing closed.
- [**Re-anchoring: keeping an agent's rules alive through every summary, and a canary that shows when they are not**](../../../../../articles/re-anchoring-agent-behaviour-policies.md). Summaries keep under 2% of a long session. Re-anchoring prints the agent's rules back after each one; a canary report shows it is working.
- [**How I work with Claude: one session per topic, agents with names, and memory you curate**](../../../../../articles/how-i-work-with-claude.md). A practical guide from a year of daily use: one Claude session per topic, named agents with a role.md, curated memory, vaults, and policy before connectors.

### Business plans and economics

A desktop for an agent, and who pays for the long tail of open source.

- [**A Mac of the agent's own: a business plan for agent desktops, what Apple's licence allows, and three behaviour policies**](../../../../../articles/a-mac-of-the-agents-own.md). A business plan for a Mac of the agent's own: what Apple's licence allows, a desktop built from vaults per run, and three behaviour policies for one agent.
- [**Open source is not free: who pays to keep the long tail working?**](../../../../../articles/open-source-is-not-free.md). An old iMac, the long tail of old versions that projects are not paid to support, measured from public data, and five ways to pay for it, simulated.

*This is issue 3 of the SGit Newsroom newsletter, also published on LinkedIn in [Deterministic GenAI](https://www.linkedin.com/newsletters/deterministic-genai-7174563523795005440/). Every article it links to is on [sgit.ai](https://sgit.ai/articles/index.html), with its sources and its data. To get the next issue by email, [subscribe at sgit.ai/subscribe](https://sgit.ai/subscribe/).*

**Posting this issue on LinkedIn?** The cover is [003-pay-after-you-read.jpg](../../../../../articles/banners/003-pay-after-you-read.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page. LinkedIn drops images from a paste, so add these where they appear, in this order, with the caption under each:

1. [003-2026-10-11-week.jpg](../../../../../articles/banners/collages/003-2026-10-11-week.jpg) Three days in six pictures, one from each of the lead articles
2. [gl-anchors.webp](../../../../../articles/images/gl-anchors.webp) Six changes, and five hypotheses written down before the first payment, each with what we expect and what would prove us wrong.
3. [003-2026-10-11-personas.jpg](../../../../../articles/banners/collages/003-2026-10-11-personas.jpg) A newsroom of your own: picks for each persona, the graph of what you read, and the card where you rate what you read
4. [ns-architecture.webp](../../../../../articles/images/ns-architecture.webp) The SGit Newsroom's architecture: every piece of application logic runs in the reader's browser.
5. [ar-layers.webp](../../../../../articles/images/ar-layers.webp) What five articles became, in tokens: the catalogue is large, and what an agent loads from it is small.
6. [pl-stack.webp](../../../../../articles/images/pl-stack.webp) The shared responsibility model, drawn for agents: each layer can only name what it can see.

[← All issues](../../../../../articles/newsletter/index.md)


---

*[Site index for agents](../../../../../llms.txt) · [HTML version](https://sgit.ai/articles/newsletter/2026/10/11/003-pay-after-you-read.html)*
