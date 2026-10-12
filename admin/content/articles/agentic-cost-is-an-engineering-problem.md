---
title: Agentic cost is an engineering problem: a business plan for a service that reads the logs a company already has and finds the money, then the engineering
date: 2026-10-12
author: Dinis Cruz
author_url: about/index.html
summary: A business plan, written to be handed to someone who wants to build it or to collaborate on it. The service helps companies manage the cost of agentic AI, and it starts from a claim this site has made before: cost is an engineering problem. An agent estate whose bill nobody can explain is an estate that shipped from the explorer side without the villager's discipline, and the Wardley map says so: prompts and workflows grown in sessions, running in production on commodity model APIs, with logs, traces and invoices that exist and are never read together, and no one who owns the cost. The service installs nothing. It reads what is already there, draws the footprint of every agent, builds a digital twin of the estate, writes the behaviour policy each agent was in fact running under, and maps cost and capability into one graph. The findings are two lists: what to stop paying for, which pays for the engagement, and what to build, which is the reason to have it: the places of attrition, the gaps, the workflow three teams rebuilt, the policy that would end a loop. The gaps are findings too: a company that cannot provide the data has learned the first one. Vaults carry the data in, the transformations as commits, and anonymised extracts out as sealed envelopes. Four price levels on the RiskMandate pattern, every number a labelled assumption.
version: v0.7.74
license: https://creativecommons.org/licenses/by/4.0/
tags: business-plan, agentic-ai, cost, wardley-maps, explorer-villager, agent-behaviour-policy, digital-twin, logs, vaults, riskmandate, startups, article
status: published
---

!frames ac-wardley-1.webp, ac-wardley-2.webp, ac-wardley-3.webp | images/ | The map in three frames: the problem as most companies have it, what the service adds from what is already there, and where it goes. Agents in production on the explorer side, billed by the token, with logs nobody reads together; then the footprint, the twin, the policy and the graph; then cost as a discipline. | wardley-map

This is a business plan, of the kind this site has published before: [Agent Desk](/articles/an-agent-desktop-by-the-minute.html), [Connector Twin](/articles/connector-twin-before-you-deploy-an-agent.html) and the others on the [business plans page](/startups/business-plans.html). It is written to be handed to someone, and the someone is whoever wants to build it, or build it with me. The service is simple to say: help companies manage the cost of agentic AI, by observing what is already happening.

The reason I think it is a business, and not a consulting engagement, is that the inputs already exist in every company that has put agents into production, nobody is reading them together, and the two things that come out of reading them, a shorter bill and a map of what to build, are both things companies pay for.

## In short {#short}

- **Cost is an engineering problem.** When the bill for agents cannot be explained, it is not because models are expensive. It is because the estate shipped from the explorer side, prompts and workflows grown in sessions, without the discipline production needs: a policy, a twin, an owner, a cap. The Wardley map shows the shape.
- **The logs already tell the story.** Model and gateway invoices by key and day; the traces agents write; the prompts and schedules as they are. Read together, they give every agent a footprint, and a footprint is most of a policy.
- **The service installs nothing.** The customer drops what they have into a vault; the service reads it; the customer gets the twin, the policies and two lists.
- **Two lists, in this order.** The cost list: loops disguised as retries, whole context sent every call, big models where small ones answer, schedules nobody reads, keys with no ceiling. The engineering list: the workflow three teams rebuilt, the policy that would end the loop, the twin that would make the next incident replayable, the prompt that should be a component.
- **The gaps are findings.** The less data a company can provide, the more it has learned already: an agent with no logs has no footprint, no owner and no policy.
- **Vaults carry it.** Data in, encrypted to the service's key in a vault the customer owns; every transformation a commit, so the chain from invoice to finding is walkable; anonymised extracts out as sealed envelopes to a benchmark vault, seen by the customer before they go.
- **Four price levels**, on the RiskMandate pattern, and a share-of-savings option. Every number is a labelled assumption.

## The problem, on a map {#problem}

!shot ac-wardley-problem.webp | images/ | The problem. The person who pays the bill sees a total. Below it, agents in production built from prompts and workflows grown in sessions, on commodity model APIs metered by the token, with logs, traces and invoices that exist and are never read together, and no one who owns the cost. | wardley-map

Take any company that has agents doing real work: reading a mailbox, running a schedule, answering customers, writing code. Draw the value chain with the person who pays the bill at the top. Under them, the agents. Under the agents, where did they come from? Almost always from a session: someone built a prompt that worked, wrapped it in a workflow, and it went to production because it worked. That is the explorer side of the map, genesis and custom-built, and it is the right place to build something new. It is the wrong place to run something at scale, and [the newsroom's move from explorer to villager](/articles/explorer-to-villager-newsroom.html) is this site's own worked example of what the move involves.

Meanwhile the things the agents run on are at the far right: model APIs, token metering, cloud compute, all commodities, all billed by use, and billed well, which is the irony. The invoice is exact. The logs are complete. The traces exist because the platforms write them whether anyone asked or not. And nobody reads them together, because the agents came from the explorer side where nobody needed to, and the one node on the map that should connect the bill to the agents, an owner of cost, is missing.

That is why [cost is an engineering problem](/articles/knowing-when-to-stop.html), in the sense that article meant it about security: not a thing you fix by negotiating a discount, but a class of defect with a cause, a fix and a test. An agent that retries in a loop is a bug. A workflow that sends its whole context on every call is a bug. A key with no ceiling is a missing control. These are the things engineers fix once they can see them, and the service exists to make them visible.

## What the service does {#service}

!shot ac-plan.webp | images/ | Observe, map, find: the three steps, the two lists, how it makes money, why vaults, and the positive frame. Every price is a labelled assumption.

!shot ac-wardley-service.webp | images/ | What the service adds, from what is already there. The footprint read from the logs; the twin of the estate; the behaviour policy each agent was in fact running under; and the cost and capability graph that produces the findings. Nothing is installed in the customer's estate. | wardley-map

**Observe.** No agent is installed and nothing in the customer's environment is changed. The customer drops into a vault what they already have: model and gateway invoices by key and by day; the logs and traces their agents write; the prompts, workflow files and schedules as they are; and whatever they know about who owns which agent. The vault is theirs; the contents are sealed to the service's key, as [RFC 0001](/articles/rfc-0001-public-key-cryptography-for-sgit.html) describes.

**Map.** Three things are built from that, and they are the three things this site has been arguing for all along, applied to cost.

- **The footprint** of every agent: what it actually did, read from the logs. Calls, tokens, tools, retries, loops, hours of the day, which data it touched. This is the [footprint](/articles/footprint-and-blast-radius.html) that article proposed as the after-the-fact twin of a mandate, with nobody inline and no production access needed, and here it is the first thing the money attaches to.
- **The twin** of the estate: a graph of agents, models, keys, tools, data, owners and schedules, with a cost on every edge. It is a digital twin in the plain sense: a representation of what is running that can be queried, compared with the invoice, and followed. The [connector twin](/articles/connector-twin-before-you-deploy-an-agent.html) is one component of it; this is the whole estate.
- **The policy** each agent was in fact running under. Not the one somebody wrote, if anybody did, but the one the footprint reveals: what it reached, what it did with what it reached, where it stopped and where it did not. Written as an [Agent Behaviour Policy](/articles/the-behaviour-policy-is-the-business-logic.html), with the enforcement column filled honestly, so that the rows that say "told" are visible, because that is where both the cost and the risk are. Where the cost is large, the policy will be large, and that is the intersection this plan sits on.

And the gaps: where there is no log, no owner, no policy, no cap. These go on the map as findings, not as missing data.

**Find.** Two lists, in this order. The cost list first, because it pays for the engagement: retries that are loops; context sent whole on every call when a graph would send a slice, which [The agent is the reader](/articles/the-agent-is-the-reader.html) measured at ninety per cent less; the large model used where a smaller one answers the same; agents on schedules whose output nobody reads; keys with no ceiling. Then the engineering list, which is the reason to have the engagement at all: the workflow three teams built separately; the policy that would end the loop for good; the twin that would make the next incident replayable; the thing that should be a component and is a prompt that every session has to remember, which is the argument of [Every mistake added a rule](/articles/every-mistake-added-a-rule.html).

## Why the positive frame matters {#positive}

A cost review is a thing companies buy once and resent. A map of what to build is a thing they come back for. The difference is the frame, and it is not a sales trick; it is what the data supports. The same logs that show an agent looping show the workflow it was trying to run, and the workflow is usually worth more than the loop costs. The same twin that shows three teams calling the same model with the same prompt shows the component they should share. The places of attrition, where an agent gives up, retries, or hands off to a person, are the places where a policy and a component would change what the company can do, not only what it spends.

So the service sells cost reduction, and delivers engineering opportunity, and the business model follows the second. That is also why the gaps are findings rather than obstacles. A company that cannot produce a log for an agent has an agent nobody is watching; a company with no owner for a key has a key that will be the next incident; a company whose prompts live only in a session has no way to know what its agents are doing. Not being able to do the analysis is the first result of the analysis, and it is the one most companies need first.

## Why vaults {#vaults}

The plan is specific about vaults because they fit this job unusually well, and because the latest capabilities make the fit better.

- **Capture.** The customer's logs go into a vault once, encrypted in their browser or on their machine, in a vault they own and can revoke. The service holds a read key to that vault and nothing else.
- **Transform.** Every step from invoice to finding is a commit: the parsed logs, the footprints, the twin, the policies, the lists. The chain is walkable, so a finding can be followed back to the lines it rests on, which is the same provenance rule the [newsroom](/articles/the-article-remains-a-product.html) runs on.
- **Move.** The twin is a vault of its own, and a read key opens exactly one customer's estate to exactly one analyst or agent. Anonymised extracts, the shape of a loop, the ratio of context to answer, the distribution of cost by agent type, can leave as [sealed envelopes](/articles/rfc-0001-public-key-cryptography-for-sgit.html) to a benchmark vault, and the customer sees the extract before it goes. Over time that vault is the thing that lets the service say "companies like yours spend this much on this", which is the second business.

## How it makes money {#money}

Four levels, on the pattern RiskMandate uses, and one alternative.

| Level | What | Price |
|---|---|---|
| **Kit** | The log formats, the twin schema, the policy template and the scripts, to run yourself | £50 |
| **Your cost vault** | The customer runs the catalogue of analyses on their own logs, in their own vault | £250 |
| **Standard** | One estate read: the twin, the policies, both lists, a one-page board summary, within ten working days | £3,000 |
| **Tailored** | Standard, plus the engineering list worked through with the team, and a re-read when the bill moves | from £9,000 |
| **Share of savings** | Where a customer prefers it: a share of the first year's reduction, measured from the invoices | an assumption |

About eight Standard and two Tailored a month cover a two-founder burn, on the same arithmetic as [Company X-Ray](/startups/business-plans.html). Every number is a labelled assumption, and the calculator belongs in the plan vault when it is made.

## What is already here, and what is not {#exists}

What exists on this site, and in the agents that run it: the footprint method, the behaviour policy format with its enforcement column, the connector twin design, the vault tooling for capture, transform and move, the sealed envelopes, and the Company X-Ray pattern of reading a company's own documents in a vault and returning findings in five days. What does not exist: the catalogue of cost analyses, the twin schema for an agent estate, the log parsers for the common platforms, the benchmark vault, a single customer. That is the work, and it is a few weeks of it, which is why I am writing the plan rather than keeping it.

## What this does not claim {#limits}

- **No customer has been read.** The method is assembled from pieces that run elsewhere; the cost list and the engineering list are what I expect to find, not what has been found.
- **The prices are assumptions.** Labelled as such, on the pattern of the other plans here, and to be tested against the first three customers.
- **The map is a sketch.** Wardley maps are arguments, not measurements; this one says where I think the problem sits and why.
- **Share of savings is hard to measure honestly.** It needs a baseline from the invoices and an agreed way to attribute a reduction; the plan should say how before anyone signs it.

If you want to build this, or you run agents in production and would like to be the first estate read, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from {#sources}

A voice memo of mine on 12 October 2026, after a conversation with someone I may collaborate with; they are not named. Written by this site's agent in the voice of this site. The argument and the editorial responsibility are mine. The plan rests on earlier work here: the footprint in [Footprint and blast radius](/articles/footprint-and-blast-radius.html), the policy in [The behaviour policy is the business logic](/articles/the-behaviour-policy-is-the-business-logic.html), the twin in [Connector Twin](/articles/connector-twin-before-you-deploy-an-agent.html), the explorer-to-villager move in [the newsroom's own case](/articles/explorer-to-villager-newsroom.html), the context measurement in [The agent is the reader](/articles/the-agent-is-the-reader.html), the component argument in [Every mistake added a rule](/articles/every-mistake-added-a-rule.html), the vault cryptography in [RFC 0001](/articles/rfc-0001-public-key-cryptography-for-sgit.html), and the pricing pattern of the plans on the [business plans page](/startups/business-plans.html). The Wardley maps and the plan figure were drawn for this article. Related: [Knowing when to stop](/articles/knowing-when-to-stop.html), [An agent desktop by the minute](/articles/an-agent-desktop-by-the-minute.html) and [The article remains a product](/articles/the-article-remains-a-product.html).
