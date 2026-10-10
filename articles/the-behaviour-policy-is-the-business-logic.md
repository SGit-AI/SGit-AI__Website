# Zoom into an agent's behaviour policy and you find the business logic, sgit.ai

> The first rules anybody writes for an agent are mechanical. Do not send, only draft. Do not delete. Use your own account. Vendors are good at those, and should be. Zoom in on any real agent's behaviour policy, though, and within a few layers you are writing how this company does email, which steps an invoice goes through, who a client is to it this week, and what the company is for. That is business logic, and many organisations have never written it down, because their software was the law. This article walks one fictional firm's email agent through six layers, from the platform to the board, records what stands in the way of each rule, counts how much of the policy is backed by a control, how much by an accepted risk and how much by hope, and shows where a vendor's existing control plugs in. The argument is that a behaviour policy built in layers, each refining the one below and each with its own owner, is the only way to describe agent behaviour at the granularity a business actually runs at, that vendors cannot and should not try to model it for each customer, and that writing it down is what lets the business scale.

*Source: <https://sgit.ai/articles/the-behaviour-policy-is-the-business-logic.html> · site v0.7.23 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Zoom into an agent's behaviour policy and you find the business logic

# Zoom into an agent's behaviour policy and you find the business logic

By [Dinis Cruz](../about/index.md) · 2026-10-07 · [v0.6.91](../admin/versions.md) · agentsagent-behaviour-policybusiness-logicfractal-semantic-graphscontrolsrisk-acceptancerbacskillsintegrationsarticle

***Abstract:** The first rules anybody writes for an agent are mechanical. Do not send, only draft. Do not delete. Use your own account. Vendors are good at those, and should be. Zoom in on any real agent's behaviour policy, though, and within a few layers you are writing how this company does email, which steps an invoice goes through, who a client is to it this week, and what the company is for. That is business logic, and many organisations have never written it down, because their software was the law. This article walks one fictional firm's email agent through six layers, from the platform to the board, records what stands in the way of each rule, counts how much of the policy is backed by a control, how much by an accepted risk and how much by hope, and shows where a vendor's existing control plugs in. The argument is that a behaviour policy built in layers, each refining the one below and each with its own owner, is the only way to describe agent behaviour at the granularity a business actually runs at, that vendors cannot and should not try to model it for each customer, and that writing it down is what lets the business scale.*

One fictional firm's email agent, layer by layer, with the barrier that stands in the way of each rule. The bottom two layers are mechanics; the four above them are the firm's business.

The first rules anybody writes for an agent are easy. Do not send email, only draft it. Do not delete anything. Use your own account, not mine. They are short, they are the same in every company, and they are the rules I wrote first when I set up [six agents on one inbox](../articles/six-agents-one-inbox.md).

Then you keep going, and something changes. Which drafts may it send once a person has looked? Replies only, or new conversations too? To clients, or to anybody? Can it mention a price? Can it chase an invoice that finance has not approved? Can it write to a client who is in a dispute with us? Can it write to a candidate about the outcome of an interview? A few questions in, you are no longer describing an agent. You are describing the business.

That is the point of this article. Zoom into an [Agent Behaviour Policy](https://riskmandate.ai/abp.html) and, below the first layer or two, what you are capturing is business logic: how this company works, function by function and process by process, up to what it is for. Much of it has never been written down. The tools that sell agent controls mostly stop before it. And it is the part that decides whether an agent can be trusted with real work.

## The bottom is mechanics, and vendors do it well

The lowest layers of the example in the figure above are mechanical. The agent signs in as its own account. It never holds the mailbox password; the platform holds the token. Deleting mail is switched off by an administrator. Forwarding to outside domains is blocked. Sending needs a person.

These are the controls platforms are good at, and they matter more than they look. The difference between an administrator and an ordinary user is one of the oldest controls in computing, and it is still the one that decides most of what an agent can reach. Secrets held by the platform rather than the agent, tools switched off rather than discouraged, an identity per agent rather than a shared login: each of these is a **boundary** in the behaviour policy's terms, enforced by something the agent's own grant does not include, and so a real control.

They are also less obvious than they sound. When the agent operating a Google Workspace mailbox [measured its own connector](https://abp.sgit.ai/gmail/measured/index.html), on 19 September, it found thirty tools; on that account `send_message` ran with no prompt while trashing a message stopped for an approval. The mechanics are where a policy starts, and getting them right takes measurement, not reading the documentation.

## Above the mechanics is the business

Go one layer up and the rules stop being the same in every company.

**The function.** How this firm does email. Reply inside existing threads; a new recipient needs a person. Never quote a price or a discount; pricing goes to sales. Every sent mail is copied to a log the agent cannot edit.

**The process.** The steps a piece of work goes through. An invoice goes out only after finance has approved it in the ledger. No email tells a candidate the outcome of a hiring decision. A complaint reaches a named person within one working hour.

**The relationship.** Who this customer is to us, right now. During an open dispute, nothing goes to that client except through legal. Key accounts get a reviewed draft rather than a sent mail.

**The organisation.** What the company is for. Treat customers fairly: no pressure, no hidden terms. Or, in another company, win back every customer who cancels.

None of these is exotic. Each is a sentence a manager would say out loud. Together they are the firm's business logic as it applies to one agent doing one job, and each layer has a different owner: IT and security, the head of operations, finance and HR and legal, the account managers, the board.

## Why the vendors stop at the mechanics

A platform that sells agent controls is in a catch. It has to add value to every customer, and it has to scale, so it builds what is the same for everybody: roles, switches, secret stores, tool permissions, approval prompts. Those are worth having. But the layers above are different in every company, they change every week, and in many companies they are not written anywhere a product could read them. A vendor that tries to model each customer's business becomes a consultancy; one that does not is left selling the bottom of the stack.

That is not a criticism of the vendors. It is the shape of the problem. The mechanical layer is a product. The business layers are the customer's, and the customer has to write them.

## Software was the law

Why have so many companies never written this down? Because they did not need to. Their software was the law.

For decades the rules of engagement lived in the systems people used. A clerk could not send an unapproved invoice because the finance system had no button for it until the approval was recorded. A support agent could not see a customer's payment details because their role did not include the screen. Approval chains, role-based access control, field-level permissions, workflow engines: these are business logic, encoded in software, and often far more complex than anybody would choose to write in prose. They are also important. They are where privacy decisions live, who can see what, who can do what, and much of what governance means in practice.

An agent breaks that arrangement. It works through APIs, not screens. It can call the endpoint the button would have called, without the screen that hid the button. The rule that the user interface enforced by omission is no longer enforced, unless somebody writes it down and something enforces it. The behaviour policy is where it gets written down.

## Policies inside policies

The structure I have found that can hold this is a fractal one: behaviour policies inside behaviour policies, each layer refining the one below, inside the room the one below allows.

At the bottom are the foundational controls: identity, secrets, what the platform switches on and off, a few levels of privilege from administrator upwards. Above them, the soft controls that the agent enforces on itself, or that another agent checks. Above those, the function, the process, the relationship. And at the top, whatever the company says it is for. That top layer is the company's to define. It might be to treat customers fairly. It might be to maximise revenue from every account. A behaviour policy describes; [it does not judge](https://riskmandate.ai/abp.html). But a policy that is written down can be read, and a company whose top layer says it treats customers fairly, with the layers beneath to show it, has something to show that a company without one does not.

This is the same grammar as the rest of the site's [fractal semantic graphs](../articles/introducing-fractal-semantic-graphs.md): the same small set of rules at every level, so one reader and one set of tools work from the board's principle down to a single tool permission. It is also how the behaviour policy itself is already built. The ABP's vocabulary is [three layers](https://abp.sgit.ai/model/graph/layers/index.html): shared facts owned by nobody, each party's own formulas over those facts, and declared bridges between vocabularies. A customer extends it by adding nodes in its own vault, never by asking for a change in ours.

## How much of it is hope?

The worked example, counted. Each rule is backed by a control, governed by an accepted risk with an owner and an expiry, or resting on hope. The proportions are illustrative; the shape is the point.

Once the rules are written in layers, a question becomes answerable that is usually only felt: how much of this agent's behaviour is actually enforced?

The behaviour policy already records, for every rule, which of four things stands in the way: nothing, an **expectation** (a rule in prose, enforced by nobody), a **setting** the agent's own account can flip, or a **boundary** enforced above it. Only the last is a control. Add one more fact, whether a named person has accepted the risk of the rule not being enforced, with an expiry, and every rule lands in one of three states: backed by a control, governed by an accepted risk, or resting on hope.

In the example, five of the seventeen rules are backed by a control, six are governed by an accepted risk, and six are hope. The shape is the finding. The platform layer is all control. The organisation layer is all hope. In between, the more specific a rule is to this firm, the more it rests on the agent behaving and on somebody having [accepted that it might not](../articles/every-risk-is-already-accepted.md). That is not a failure; most of a business has always run on people behaving as asked. But it is worth knowing which is which, and with an agent it can be counted.

## Where the vendors plug in

Five rules from the example, and the control that would move each one. Every control is a kind of product that already exists; what is new is that it enforces a rule the customer wrote.

This is also where the catch for vendors comes undone. A vendor does not have to model the customer's business. It has to enforce the parts of the customer's written policy that its product can reach.

A send gateway that holds mail to an address the thread has not seen moves "a new recipient needs a person" from an accepted risk to a control. An outbound content check moves "never quote a price" from hope to a control. A finance system that answers "is this invoice approved?" to a gateway the agent cannot reach moves the invoice rule. A blocked-recipients list that legal maintains moves the dispute rule. The principle at the top has no single control, but sampling sent mail against it, with a named reviewer, turns hope into an accepted risk.

Each of these is a product somebody already sells. What changes is that it now enforces a rule at the layer the customer wrote it, and the policy can count the move. A control attached to a written rule is worth more than one switched on in general, because the customer can see what it bought. That is why I think the behaviour policy is a good place for vendors to integrate rather than a threat to them: it gives their controls a rule to enforce and a number to move, and it lets several vendors each own a different row without any of them having to own the whole business.

It is also why the frameworks are starting to ask for this. The [AI Baseline Control Framework](../articles/ai-baseline-control-framework.md) asks, in RG.2, that for every AI system acting autonomously "what it does is described", and, in AC.3, that each one has a named owner. The description RG.2 asks for is the layers above the mechanics. The owner AC.3 asks for is the person whose name goes on each layer.

## It looks a lot like a skill

Read the upper layers of the example again and they look less like access control and more like a skill: the instructions that tell an agent how a function is done here. How we answer clients. How an invoice goes out. What we never say about price. A skill file and a behaviour policy layer are written by the same people, about the same work, for the same agent.

The difference is what each one carries. A skill says how. A policy layer says what is allowed, who owns the rule, and what stands in the way of breaking it. Written together, they are the business codified for an agent: the functions, the processes, the relationships and the principles, with the controls and the acceptances attached. That is what lets the business hand real work to agents and still know what it handed over. It is also what lets it scale: the knowledge that lived in a few people's heads, and in software nobody could read, becomes something an agent can follow, a person can review and a control can enforce.

## What comes next

The example here is fictional on purpose, so the shape is clear. The next step is a real one: take the [measured Gmail deployment](https://abp.sgit.ai/gmail/measured/index.html) as the bottom two layers, write the function, process and relationship layers above it for one real inbox, count the three states, and publish it as a vault with its read key. Then do it again with a vendor's control in the path, and publish the count before and after.

*Drafted from a voice note by Dinis Cruz, who is the author of the argument and the person with editorial responsibility, by agent@riskmandate.ai (Claude Opus 5.5, claude-opus-5-5) in the sgit.ai site session, on 7 October 2026. The firm, its rules and its counts are illustrative. The measured Gmail figures and the ABP's barrier kinds and layers are from abp.sgit.ai and riskmandate.ai as published that day. The kinds of product named in the third figure are categories, not recommendations, and no vendor was contacted.*

## Threads

Agents & policy[This article as a graph →](graphs.md#the-behaviour-policy-is-the-business-logic)

### Builds on

- [Six agents, one inbox: what a real multi-agent setup taught me about access policies](six-agents-one-inbox.md) An access policy for an agent is only as real as its worst row: every rule in a real six-agent setup, graded by how it is enforced today.
- [Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](introducing-fractal-semantic-graphs.md) A fractal semantic graph has no privileged level and no single schema: each world keeps its own vocabulary and connects to others through named edges.
- [Every risk is already accepted. The only question is by whom, and for how long.](every-risk-is-already-accepted.md) A risk exists the moment the exposure does, so somebody is already carrying it; the only questions worth asking are who has accepted it and until when.
- [An open AI governance framework, and what its licence let us build](ai-baseline-control-framework.md) Twenty open AI governance controls under CC BY-SA, why the licence matters, and the same day's conversion into a graph, a database and a walk down to EU law.

### Continued by

- [Ten hard questions for RiskMandate, answered: the mandate, the reach, the gap, and what we are deliberately not](riskmandate-ten-questions.md) Ten hard questions from a conference, answered in a two-hour interview: what RiskMandate does, what it deliberately is not, and how mature each part is.
- [Hope or enforcement: one customer service agent, three designs, and who keeps each promise](hope-or-enforcement.md) One customer service agent built three ways, each with an Agent Behaviour Policy: how much of each policy is hope, and what one run can reach.

[All articles](index.md) · [All graphs](graphs.md)

## From the desk

- [Behaviour policy in practice](collections/behaviour-policy-in-practice.md) collection, 11 articles

**Posting this article on LinkedIn?** The cover is [the-behaviour-policy-is-the-business-logic.jpg](../articles/banners/the-behaviour-policy-is-the-business-logic.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/articles/the-behaviour-policy-is-the-business-logic.html)*
