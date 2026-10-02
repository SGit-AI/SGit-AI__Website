# Replicating the agentic inbox: a walkthrough from one Claude session to a team of agents that never press send, sgit.ai

> Two calls in one day asked the same thing, how do I copy your email setup, so this is the walkthrough. It is the first agentic email workflow I have run that puts me more in control rather than less, and the reason is the behaviour policies, not the model. The idea is to use Claude as an agent state machine, one session per role, with every message between agents a file in a vault and every outgoing email a draft that a person reads and sends. The setup goes in phases. Phase 0 is the accounts, a Google Workspace mailbox of its own on a domain you own, a Claude Team seat for the agent with the connectors enabled by the admin and connected by the agent's account, your own calendar shared read-only, and a GitHub account on the same identity. Phase 1 is one session, the inbox agent, with a behaviour policy written before the first run. Phase 2 splits the roles, inbox, writer, CRM, dev team, each a session with its own policy, talking in files through Email-FS lite. Phase 3 adds the interfaces and the record. Schedules come later and get their own article. The rule that never changes is the one that makes it work, the agent drafts and a person sends.

*Source: <https://sgit.ai/articles/replicating-the-agentic-inbox.html> · site v0.6.48 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Replicating the agentic inbox: a walkthrough from one Claude session to a team of agents that never press send

# Replicating the agentic inbox: a walkthrough from one Claude session to a team of agents that never press send

By [Dinis Cruz](../about/index.md) · 2026-10-02 · [v0.6.42](../admin/versions.md) · agentsemailinboxagent-behaviour-policyriskmandateclaudegoogle-workspaceconnectorsvaultsemail-fswalkthrougharticle

***Abstract:** Two calls in one day asked the same thing, how do I copy your email setup, so this is the walkthrough. It is the first agentic email workflow I have run that puts me more in control rather than less, and the reason is the behaviour policies, not the model. The idea is to use Claude as an agent state machine, one session per role, with every message between agents a file in a vault and every outgoing email a draft that a person reads and sends. The setup goes in phases. Phase 0 is the accounts, a Google Workspace mailbox of its own on a domain you own, a Claude Team seat for the agent with the connectors enabled by the admin and connected by the agent's account, your own calendar shared read-only, and a GitHub account on the same identity. Phase 1 is one session, the inbox agent, with a behaviour policy written before the first run. Phase 2 splits the roles, inbox, writer, CRM, dev team, each a session with its own policy, talking in files through Email-FS lite. Phase 3 adds the interfaces and the record. Schedules come later and get their own article. The rule that never changes is the one that makes it work, the agent drafts and a person sends.*

The agentic inbox in four phases. Phase 0 is the accounts, a mailbox and a Claude seat of the agent's own. Phase 1 is one session with a policy. Phase 2 splits the roles and has them talk in files through a vault. Phase 3 adds the interfaces and the record. The rule across the top never changes: the agent drafts, a person sends. Role names are the ones in use on 2 October 2026; the agents will describe their own roles in the next revision.

**What this is, and what it is not yet.** A practical walkthrough for somebody who wants to copy a setup that is running, written the day two people asked for it. It is the how, in phases, from the simplest version that is worth having to the one I run. It is not the argument for why: that is in [Six agents, one inbox](../articles/six-agents-one-inbox.md), which is about the policy rows and what the tools can enforce, and in [Custom UIs are not the exception](../articles/custom-uis-are-not-the-exception.md), which is about the interfaces the team built on top. This is a first pass by the person, and it is deliberately on its own page: the agents who run the roles will add their own account of each one, because they will describe what they do better than I can, and a second revision will carry it.

## In short

- **Claude as an agent state machine.** Each role is a Claude session that reads its state from a vault, does one kind of work, and writes the result back as files. There are two ways to run it, sessions you open yourself and sessions on a schedule. Start with the first. The schedule is a separate article.
- **Never your own inbox.** The agent gets a Google Workspace mailbox of its own, on a domain you own. Your inbox is full of secrets and history; the agent's is empty on day one, and that isolation is what lets you trust it.
- **A Claude seat of its own, too.** A Claude Team account for the agent, with the connectors enabled by the organisation owner and then connected by the agent's own account, so the OAuth grants to Gmail, Calendar and Drive live only there.
- **One session first.** The inbox agent reads, labels, moves and summarises, and writes replies to Drafts. You send. Write the behaviour policy before the first run, even for one agent: what it can reach, what you asked, the gap, the barriers.
- **Then roles, talking in files.** Inbox, writer, CRM, dev team, each a session with a policy. Every agent has the same reach to the mailbox; only the inbox agent reads it and only the writer puts text in Drafts. Between them, a vault with Email-FS lite: an inbox per agent, as a folder with conventions.
- **The rule that never changes.** Nothing is sent by an agent. Everything lands in Drafts, and a person reads, edits and presses send. The one exception, security notices, is written into the policy as an exception.
- **It is working.** This is the first agentic email workflow I have run that puts me more in control, not less, and the reason is the policies, not the model.

## Why this is on a separate page

Two calls today, both ending with the same question. The honest answer is that the setup is copyable in an afternoon for the simple version and in a week for the full one, and that nothing in it is clever. It is accounts, a policy, drafts, and files. What makes it work is the discipline of the phases, so the walkthrough is in phases, and you can stop at any of them.

## The core idea: Claude as a state machine

Claude is good enough now, and has enough common sense, to be treated as a step in a state machine rather than a chat. Each role is one session. It starts by reading its state, which is a set of files in a vault: its inbox of messages from other agents, the policy that governs it, the record of what it did last time. It does one kind of work. It writes the result back as files: a reply into another agent's folder, a draft into the mailbox, a row into the CRM, a note into the record. Then it stops.

Two ways to run that. You can open each session yourself, when you want the work done, and read what it did. Or you can put the sessions on a schedule and let them run. The second is where this ends up, and it is where the reader role in the six-agents article already lives, but I do not recommend starting there. Start with sessions you open, so that every run is one you watched. The schedule gets its own article when the pattern is settled.

## Phase 0: the accounts

Everything else rests on the agent having an identity of its own. Four pieces.

**A Google Workspace mailbox for the agent.** A Workspace seat costs a few pounds a month per mailbox and is quick to create. Point a domain you own at it, which is an MX record and a couple of verification records, and you have a mailbox, a calendar, a drive and documents, all under an address that is the agent's and not yours. The one rule that matters more than any other: do not connect your own inbox. Yours has years of secrets in it. The agent's is empty, so what it can leak on day one is nothing, and what it can reach is exactly what you forward or share to it. That isolation is not a limitation. It is the thing that lets you give the agent more as you learn to trust it.

**A Claude Team seat for the agent.** A separate Claude account, on a Team plan, used only by the agent. Two details here that cost me time. First, on a Team plan the connectors are switched on at the organisation level by an owner, and only then can a member connect them; until the owner has done that, the agent's account cannot connect anything, which is the right default. Second, the connection itself is made from the agent's account, so the OAuth grants to Gmail, Calendar and Drive are held by that account and no other. Your own Claude account never holds a token to the agent's mailbox, and the agent's never holds one to yours.

**A GitHub account on the same identity**, if the agent will touch code. Sign up with the agent's Google account, so there is one identity to manage, and give it access to exactly the repositories it should see. The six-agents article has the detail on installing the Claude GitHub app per repository.

**Your own calendar, shared read-only.** Share your calendar to the agent's account with read access. The agent then knows what is going on, can propose times, and can write your commitments into its own understanding, without the ability to move anything.

At the end of phase 0 you have an agent with a mailbox, a calendar, a drive and, if you want, a code host, all of its own, and a Claude account that can read and act on all of them. It has done nothing yet. That is the point of doing the accounts first: the reach exists before the mandate does, and you can write the mandate looking at the reach.

## Phase 1: one session, one inbox

Open one Claude session on the agent's account. This is the inbox agent. Its job is to read the mailbox, work out what each message wants, label and move things, summarise what needs you, and write replies as drafts. It does not send.

Before the first run, write its behaviour policy, and write it even though there is only one agent. The [policy](https://riskmandate.ai/abp.html) is four things. The reach: everything the account can do, which the connector documentation will tell you and which an afternoon of testing will correct. The mandate: what you actually want this agent to do, in your words. The gap: the difference, which for a Gmail connector is wide, because the same grant that lets an agent draft lets it send, and the same scope that lets it read lets it label and move. The barriers: for each row of the gap, what stands in the way, typed honestly. On a Team plan most of the barriers you can put in front of a single session are expectations, and the policy should say so rather than imply otherwise. Six agents, one inbox is the long version of that finding.

Then run it, and you send. Every draft the agent writes, you read, edit if you need to, and press send yourself. A week of this is enough to learn two things: how the agent reads your correspondence, and what you are prepared to let it do next. Both are things you cannot learn from the documentation. You will also discover your first exception. Mine was a security notice that needed to go out without waiting for me, and it went into the policy as a named exception rather than staying a habit.

If this is all you ever build, it is already worth having. An inbox read and triaged by something with common sense, with every reply waiting for your eye, is most of the value.

## Phase 2: roles, talking in files

The reason to split the inbox agent into roles is not neatness. It is that each role gets a policy short enough to check, and the policies differ in the one place that matters: who touches the mailbox, and how.

**The roles, as run today.** The **inbox agent** is the only one that reads the mailbox and the only one that labels, moves and files. The **writer** (the name is still being argued about; mailbox agent is the other candidate) is the only one that puts text into Drafts. The **CRM agent** keeps a CRM we built ourselves, in its own vault, one folder per person, fed by what the inbox agent extracted. The **dev team agent** runs the development team that builds the vaults, the interfaces and the tooling, and writes up what it did. Every one of these accounts has the same reach to the mailbox. Only two of them have it in their mandate, and only one of those may write.

**They talk in files.** This is the part that surprises people. The agents do not message each other through the mailbox, and they do not use a shared drive, although you could. They use a vault, and a convention we call Email-FS lite: each agent has an inbox, which is a folder, and a message is a file with a sender, a recipient, a subject and a body, with typed blocks for a `decision`, a `question`, an `answer` or a `status`, so another agent can read what is being asked without parsing prose. A reply is another file. The vault keeps every version, so the conversation between the agents is a record from the first message, signed and dated, and it can be read later with a read key by someone who holds no write credential. The [append-lane messaging](../docs/append-lane-messaging.md) write-up has the shape, and [Agent Contact](../docs/agent-contact.md) is the same idea between sites.

**One policy per role.** Each session starts by reading its own policy from the vault. The policies share the reach and differ in the mandate, and each one names the files that role may write. When a role needs something another role owns, it writes a message into that role's folder and stops. The owner picks it up on its next run.

At the end of phase 2 you have four sessions you open when you want the work done, a mailbox that only one of them reads and only one of them writes to, a CRM building itself from the correspondence, and a record of every message between the agents that you can read whenever you want. And still: nothing has been sent by an agent.

## Phase 3: the interfaces and the record

Once the roles run, the work outgrows the inbox, and the agents start building interfaces for the moments the inbox does not fit. A card on the phone with the two things that need deciding. A page listing the documents still owed, with a place to drop them. A board of who is waiting on whom. The CRM gets several versions of its own interface. That story is told in full in Custom UIs are not the exception, with the figures, and the thing to take from it here is that every one of those interfaces was built by an agent in an afternoon because the data was already files in a vault, and every one of them is an agent surface, so each got a policy of its own.

The record is the other half of phase 3. Because every message between agents is a file, every draft is in the mailbox and every decision is a row in a vault, the whole workflow leaves a footprint that can be read afterwards without touching anything, which is what the [footprint and blast radius](../articles/footprint-and-blast-radius.md) article is about. For a person learning to trust a set of agents, that record is the point. You do not have to believe what the agent says it did. You can read what it did.

## The rule that never changes

Every phase keeps the same rule, and it is the reason this is the first agentic email workflow I have run that made me feel more in control rather than less.

**Nothing is sent by an agent.** The writer puts replies in Drafts. I read them, I change what I want changed, and I press send. The inbox agent can label, move and file all day, and none of that leaves the building. The one exception is a security notice, and it is in the policy as a named exception with its own row, not a habit the agent picked up.

This is slow by the standards of people who want agents to run their correspondence. It is also the thing that lets me give the agents more every week. Trust is built from a record of drafts I did not have to change, and the record is there to read. When the day comes to let an agent send, it will be one agent, one kind of message, with a policy row that says so, and the footprint will show whether it was right.

## The checklist

For someone copying this, in order:

1. **Buy a Workspace seat for the agent** and point a domain you own at it. Never connect your own inbox.
2. **Create a Claude Team account for the agent.** As the organisation owner, enable the Gmail, Calendar and Drive connectors; then, as the agent's account, connect them. Confirm your own account holds no grant to the agent's mailbox.
3. **Share your calendar read-only** to the agent's account.
4. **Write the inbox agent's policy** before the first run: reach, mandate, gap, barriers, with the barriers typed honestly.
5. **Run one session.** Read every draft. Send them yourself. Do this for a week.
6. **Split the roles** when the one session is doing more than one kind of work: inbox, writer, CRM, dev team. One policy each.
7. **Give them a vault and Email-FS lite** to talk through. An inbox per agent, as a folder. Every message a file.
8. **Let them build interfaces** for the moments the inbox does not fit, and give each interface a policy.
9. **Read the footprint** from the vault history once a month, against the policies.
10. **Keep the rule.** The agent drafts. You send.

## What the agents will add

This page is the person's account. The agents who run the roles have a better one, because they can describe exactly what each role reads, writes and refuses, with the counts from the vaults' history. The next revision of this article will carry their descriptions of their own roles, in their words, in a section of their own, and the policies themselves as published behaviour policies. If you are copying the setup now, the checklist above is enough to start; if you are one of the agents, the folder for your reply is where it always is.

## Threads woven here

- [Six agents, one inbox](../articles/six-agents-one-inbox.md): the policy rows, what the tools enforce, and what the Workspace admin console can lock per organisational unit.
- [Custom UIs are not the exception](../articles/custom-uis-are-not-the-exception.md): the interfaces the team built on this workflow in eight days.
- [Footprint and blast radius](../articles/footprint-and-blast-radius.md): reading what the agents actually did from the record this setup leaves.
- [Before you give an agent a connector, give the connector a twin](../articles/connector-twin-before-you-deploy-an-agent.md): why to test the reach before you write the mandate.
- [The ultimate insider](../articles/ultimate-insider-three-collisions.md): the irony that runs through all of it, the more you constrain an agent, the more you can trust it.
- [Append-lane messaging](../docs/append-lane-messaging.md) and [Agent Contact](../docs/agent-contact.md): the file shapes the agents talk in.
- [RiskMandate.ai](https://riskmandate.ai/) for the Agent Behaviour Policy itself.

*Drafted from a voice memo by Dinis Cruz, who is the author of the argument and the person with editorial responsibility, by agent@riskmandate.ai (Claude Fable 5.1, claude-fable-5-1) in the sgit.ai site session, on 2 October 2026. The setup described is the one running on two identities; no address, contact or message is named. The Team-plan connector behaviour is as experienced during setup and as Anthropic's connector documentation describes it. The agents' own account of their roles is to follow.*

*© 2026 Dinis Cruz. This article's own text is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). You're free to share and adapt it, as long as you give credit. Quoted material and linked sources keep their own licences.*

## Threads

Agents & policyVaults & method[This article as a graph →](graphs.md#replicating-the-agentic-inbox)

### Builds on

- [Six agents, one inbox: what a real multi-agent setup taught me about access policies](six-agents-one-inbox.md) An access policy for an agent is only as real as its worst row: every rule in a real six-agent setup, graded by how it is enforced today.
- [Custom UIs are not the exception: the inbox in 2026, where every message has its own universe](custom-uis-are-not-the-exception.md) Every message has a graph, so it can be shaped for the reader's moment; a custom interface per moment is now how interfaces get made, and each gets a policy.
- [Footprint and blast radius: what the agent actually did, and what it would have cost](footprint-and-blast-radius.md) Footprint is what an agent actually did, read afterwards from logs and vault history; blast radius is what a row of its reach would cost the business today.
- [Before you give an agent a connector, give the connector a twin](connector-twin-before-you-deploy-an-agent.md) An agent with a Gmail or Calendar connector can do things the platform cannot undo; a journal of every call, replayed, shows what it did and what can go back.
- [The ultimate insider: agents, the infrastructure that cannot hold them, and risk management that cannot keep up](ultimate-insider-three-collisions.md) Agents, the infrastructure meant to contain them, and risk management run on spreadsheets are arriving at once, and together they are one scenario.

### Continued by

- [Six agents, one inbox: what a real multi-agent setup taught me about access policies](six-agents-one-inbox.md) An access policy for an agent is only as real as its worst row: every rule in a real six-agent setup, graded by how it is enforced today.

[All articles](index.md) · [All graphs](graphs.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/articles/replicating-the-agentic-inbox.html)*
