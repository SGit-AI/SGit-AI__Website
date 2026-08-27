# The author’s walkthroughs — Risk Graph Explorer

> Three recorded walkthroughs of the risk graph explorer with full transcripts: the graph browser, risk chains, and the role risk map — the designer explaining why the tool is shaped as it is.

*Source: <https://sgit.ai/demos/vaults/risk-graph-explorer/videos/index.html> · site v0.2.48 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../../index.md) / [Vaults](../../index.md) / [Risk Graph Explorer](../index.md) / Walkthroughs

# The author’s walkthroughs

Three recorded walkthroughs of this vault — each one played, then read. Under every video is the same session as a document: the moments that matter, the frame the screen was showing at that moment, and what is actually happening in it. The full transcript is at the foot of each.

**Why a video is not enough on its own.** A recording is invisible to a search engine, to [llms-full.txt](../../../../llms-full.txt), and to any agent reading this site as documentation. It is also full of *“this guy here”* and *“look at this”* — pointing that a transcript cannot resolve. So each moment below pairs the words with the picture they were pointing at, which is the only form in which the argument survives being read rather than watched.

Timestamps link into the video at that point. The **Graph Browser** moments are frames of the recording itself; the **Risk Chains** and **Role risk map** moments are captured from the live vault with the published read key, driven to the state being described.

## 1 · Graph Browser · 4:21 · 5 Aug 2026

How answering the questions builds the fact graph — and why a “no” is still information.

**Note on what you are looking at.** This walkthrough was recorded inside [Risk Mandate](../../risk-mandate/index.md), the field demo the explorer was later extracted from — so the chrome says *Risk Mandate — field demo* and the tab strip is shorter than today’s. The mechanism is the same one running in [this vault](../index.md).

[00:00](https://youtu.be/PP6zsrC0KEg?t=0)
### Five ready-made estates, before a single question

The video opens on the field demo’s front door — **“Eight questions about the agents you run”** — and the row of prepared examples underneath it: *a typical estate*, *a rough day*, *a well-run estate*, *a coding agent in CI*, *a support agent on accounts*. One tap loads a populated register.

That row is a design position, not a convenience. A tool that only shows you your own answers cannot show you what a different answer would have produced — and the argument here is entirely about difference.

“I want to just talk about this graph explorer that we pushed as an MVP, which is, I think, ridiculously powerful as a way to present.”

00:00 — the entry point, with five prepared estates to open instead of answering.

[00:31](https://youtu.be/PP6zsrC0KEg?t=31)
### One answer, one edge — and the counters start moving

The first question is answered: *“Yes, in production”*, which lands as `F-1`. Watch the header. It reads **1 fact · 4 risks · 5 provisions**, *where it runs: in production* — and **at stake: —**, because nothing has yet been said about data.

In the graph, exactly one edge is drawn: `runs-in`, from **The agent** to **The production estate**. Every other twin is ghosted and carries its own tally — `0/3 said`, `0/2 said` — which is the tool stating, per node, how much of what it wants to know it does not have.

00:31 — 1 fact, one edge, and “at stake” still empty.

[00:59](https://youtu.be/PP6zsrC0KEg?t=59)
### Edges are named, and the names carry the meaning

Personal data is selected (`F-36`) and the header flips: **personal data at stake**. **The data in its reach** lights amber with *Personal data* written beneath it, and **Decisions its output…** gains the note *Its output informs a person w…*.

This is the moment the deixis in the transcript resolves. He says the edges differ — and they do, by *name*: `runs-in`, `can-read`, `can-change`, `informed-by`. Not a generic line with a thickness, a labelled relation. That is what makes the picture evidence rather than decoration.

“We actually have different, in a way, almost, different edges depending of what it is. And then, what it can do with the data, right? It cannot see it, or reads it, or reads and changes it.”

00:59 — the data node lights, and the edges arrive with names on them.

[01:30](https://youtu.be/PP6zsrC0KEg?t=90)
### One answer can be two facts

*“Reads and changes it”* is selected — and its chip reads `F-33 F-34`. Two fact identifiers for one click, because the answer asserts two separable things, and each has to be independently citable later when a risk points back at what produced it.

The graph gains `can-read` and `can-modify` as distinct edges. Below, the questions have moved on to whether it can change production, whether it can be stopped, and how long stopping would take — the path from *capability* to *control*.

01:30 — one selection, two facts, two edges.

[02:01](https://youtu.be/PP6zsrC0KEg?t=121)
### “This is here, depends on that one” — the sentence a transcript cannot carry

Here is the clearest case for reading the video rather than only listening to it. He says two risks are connected and points; the words alone name neither end.

The frame answers it. *“Yes, eventually”* is selected under **q3 — if you had to stop it right now, could you?** (`F-12`), and an edge labelled `stops-in-many-actions` runs from the agent down to **The stop control**, which now shows `4/12 said`. The dependency he is pointing at is a named edge with a counted endpoint.

“This is an interesting one because this is connected to the stop control. So, you can actually see that this is here, depends on that one.”

02:01 — the referent of “this depends on that one”, named.

[02:30](https://youtu.be/PP6zsrC0KEg?t=150)
### Saying “never” draws an edge too

Two negative answers land: *never* actually stopped it (`F-19`), and *no*, the side effects of stopping are not known (`F-22`). A checklist would score these as gaps and move on.

Instead the graph grows `never-exercised-on`, `never-timed-for` and `absent-for` — negative relations, drawn and labelled exactly like the positive ones. This is the mechanism behind the claim that a “no” is information: the answer produces a fact with a name, so a risk downstream can cite it. **11 facts · 20 risks**, and the shape is filling in.

02:30 — “never” and “no” arrive as named edges, not as silence.

[03:00](https://youtu.be/PP6zsrC0KEg?t=180)
### The one green edge

Reach is answered *customer-facing* (`F-24`) and egress *no egress* (`F-47`) — and `cannot-reach`, running from the agent to **Outbound network access**, is drawn in the assurance colour rather than the exposure colour. In a field of amber it is the single teal line.

That is the whole two-colour scheme doing its job in one frame: amber is something true that costs you, teal is something true that helps you, and both are the same kind of object — a stated fact with an edge. A good answer is not the absence of a finding; it is a finding.

03:00 — “no egress” draws an edge too, in the other colour.

[03:30](https://youtu.be/PP6zsrC0KEg?t=210)
### Seventeen facts, and the question of whose account it acts under

By now the graph is dense with named relations — `cannot-reconstruct`, `held-by-a-group-for`, `irreversible-by`, `never-timed-for`, `absent-for` — and the header reads **17 facts · 30 risks · 11 provisions**. The agent node shows `15/43 said`: fifteen of the forty-three things the model would like to know have been said.

The last question is the sharpest, and it is deliberately last: **whose account does it act under** — *a named person’s · a team’s · a service account nobody owns*. Everything before it describes what the agent can do. This one asks who will be standing there when it does it.

“It’s a great way to almost in one day capture all the data.”

03:30 — 17 facts in, and the account question still to answer.

[04:01](https://youtu.be/PP6zsrC0KEg?t=241)
### The other views, in one sweep — and a risk with an owner

He closes by touring what the same answers become elsewhere, landing on **Risk chains** with **RISK-22** selected: *“Some changes the agent makes cannot be reversed by the operator”*, marked **OPERATIONAL · HOLDS NOW**, assigned to *SRE / platform on-call* and *Platform owner*, with a **blast radius** drawn from its own facts.

That panel is the payoff of everything above it. The risk was not typed by anybody. It exists because certain answers were given, it is owned because the org chart says who holds that class of thing, and it can be argued with by going back to the facts underneath — which is what the next walkthrough is about.

04:01 — a generated risk, with an owner and a blast radius.

**Full transcript — Graph Browser**

Okay, so I want to just talk about this graph explorer that we pushed as an MVP, which is I think ridiculously powerful as a way to present. So what we have here now is how the questions we originally talked about in the demo. But it's in a weird way, we start with the first question, right? Do you have an agent and where does it run? Because if you don't have an agent, then we only have one piece of information here, which is — and but this is a fact, right? So this here captures the facts and information. So you could see that you have both the operation state or the test environment. And it's interesting because the risk will be very similar.

The only question is whether it's live, so in a way that there's a risk level that is probably going to be there, right? So let's say you have one, right? And now you can see what kind of data is enriched. Let's say I got personal data. And what's cool about this is you can see that what's happening is this graph is now going to be populated with the data that we collected. So you can think of this graph as the evidence piece, right? So look, there's the output of facts and decision. Okay, it informs decisions.

So you can see that what's cool about it is that we actually have different, in a way, almost different edges depending of what it is. And then, what can do with the data, right? It cannot see it, or reads it, or reads and changes. So this is a typical example of you have a production system, right, that touches personal data, accounts, contact details, it informs the decision, you know, of the there, and it reads and changes. So it's a typical agent, right? And now you got it. So now you talk about the information of this.

You know, can the agent change things, right? Can you read and report? Can changes? Can change on its own? So you start to map, you know, for example, how it's done, right? With a person approval or change. So that so this is where you take that to the next level. So it changes on its own, right? So how do you stop it? Let's say you have an action to stop, or eventually can stop, or we don't know how to stop it. And how long should we stop it? Is it minutes? An hour? Don't know. So you start to see again, you know, the stop control now we map stop in many actions, never, time for, an hour, minutes, right? And then, have you actually stopped it? Yes, we have, only in test, never, right? Do you know the effects of stopping it? Have we mapped it? Is it partially? Etc.

So this is an interesting one because this is connected to the stop control. So you can actually see that this is here depends on that one. So it's in a way now a next line up, like down, sorry, of the flow. Is there a named person? Do you have a named person or not? So this is the stop authority, right? The team, you know, if it really is, you know, misbehavior for full speed, could, you know, what could you reach, right? Internal only, customer facing? Don't know. So this would be customer only.

So you could now start to see again, you know, what's the damage, that it can acts, you know, can you reach anything outside the network? This means that does it have internet access or not. So again, you can see here, outbound access, right? For example, no egress. Could, you know, could you undo the damage, right? So let's say you have fully reversible versus not, or some change are forever, which is important, right? Is there a written procedure for how you pull the plug? You tested it, you've written, you don't have it. Could you reconstruct what you did, for example, every day, right? Or, you know, do you have, you know, fully or partially or not, right? Cuz sometimes you have backups, but they do not allow you to restore specific things, and whose account it is, right? A service account, a named person, a team, right? So, you know, what is actually the, for example, the flow that happens. And then this is great, like because you can look at it.

This is — I love this, right, because it's a great way to almost in one day capture all the data. Just for reference, we then capture the context. We have now these really cool road map with all the risks that flow forward. We also have these risk chains, which I go in more detail in others, but that means that every risk that is then connected connects to the top level, right? And then we even have a risk register, right? And for every risk that you have here, you can see who's assigned, who causes it, and who leads to, and how does it connect, right? So it's pretty cool.

## 2 · Risk Chains · 4:18 · 5 Aug 2026

Risks that cause risks — and why being able to disagree with the register is the feature.

[“risk 6”](https://youtu.be/kWip3QnuN1I?t=45)
### Every risk carries the condition under which it would stop being true

He names one entry — *“if you look at this guy here, for example, you have risk 6”* — so this is that entry, selected in the live vault. **RISK-6 — the production estate can be changed by an agent**, with the app’s own one-line gloss: *“They hold the estate. A change they did not make can still be one they must live with.”*

The dashboard is where the design shows. **Established by**: `F-5`, the agent `can-change` the production estate — one fact, cited. **Ceases when any of these hold**: `F-4` reads-only-from, or `F-3` absent-from. That second list is unusual and worth stopping on: **the risk ships with its own falsification condition**. It is not a judgement to be argued down, it is a claim with stated exit criteria.

Then **reduced by — but not retired**: *narrowing what it may change*, *staging changes behind a gate*. Mitigation is recorded as reduction, never as removal. And **touches**: EU AI Act Art. 12, Art. 26.

The entry he names, opened: one fact establishes it, two would end it.

[“corporate 2”](https://youtu.be/kWip3QnuN1I?t=110)
### Walking it backwards: “why is it? Because we have that one, and that one”

The same view from the other end. **CORP-2 — customer harm**, assigned to the Chief Product Officer and the CEO, and the panel answers his question literally. **Established by**: *“Nothing directly. It holds because the entries below it do.”* **Leads to**: *“Nothing recorded”* — this is the top, which is where the question stops.

Underneath, **led by** enumerates the causes, and each carries a reason in the tool’s own words: RISK-5 *“← a person on the other end is what customer harm means”*; RISK-26 *“← the record is somebody’s”*; RISK-27 *“← this is what customer harm looks like in practice”*.

Note the colour: tracing upstream lights the path in the assurance tone rather than the exposure tone, so *what caused this* and *what this causes* are visually distinct operations on the same graph. And the corporate entry **touches no twin directly** — it is entirely a consequence, which is exactly why it cannot be edited into existence.

The top of a chain, interrogated backwards — with a reason attached to each cause.

[governed](https://youtu.be/kWip3QnuN1I?t=200)
### The same organisation with controls in place

Switching the preset to **Governed** re-derives every chain from a different set of answers: approvals in the path, a tested stop, a named authority, bounded reach. Fewer entries, shorter routes to the register — *“a much cleaner sort of flow of events.”*

The comparison is the argument. Nothing about the organisation changed between this frame and the last; only what is true about the agent did. A register that produced the same output either way would be measuring the questionnaire, not the estate.

Governed: same organisation, same graph, fewer and shorter chains.

**The most useful thirty seconds in all three videos** is the author disagreeing with his own tool. *“I actually don’t agree with these risks… I don’t buy that at the moment.”* He then works out what he does think is true — that the exposure is really about the agent touching EU AI Act obligations, and that stopping it would itself disrupt production — and says *“so we should capture that.”* The disagreement does not resolve into whose judgement wins. It resolves into **which fact is wrong or missing**, and then the register re-derives. That is the difference between a document you argue about and a model you correct. *“When you go and push your risk to be approved, the stakeholder is going to challenge you really hard. The cool thing is that we start to have the evidence to show exactly why we are saying this.”*

**Full transcript — Risk Chains**

...to go through this UI which I think is starting to really show the idea of connecting the risks upstream. So what you have here to show you, this is part of the UI that we have that you know, you can basically see the multiple workflows that we have from a typical, non-exposed, one that's actually quite governed. What I really like is this, let's look at the exposed first, this sort of chain, and let's consolidate this here. So the idea here is that the risks connect from one element to the other. So if you look at this guy here, for example, you have risk 6.

"The production can be changed by an agent." This is now connected to that risk. "Organization acts to the system that acts for a person", who then creates this risk, right? "Organization asks to, Tech to be changed." And then hits the top two risk register. So the logic here, this is the corporate risk register, so you can see that that particular risk will arrive there, and when I click here, I can also see the reverse. So I can see, if we say we have a risk of this, why is it? It's because we have that one, and we have that one, and we have this one, and that one. And I could also see it here, what actually happens.

You can see, for example, this particular risk, corporate 2, who is assigned to, and then to the CEO, to what, you know, is reduced by this particular choices, touches GDPR, and then leads to this. So, so actually, so this is a good example, so you can see that this guy here, this risk leads to these two, and is led by that and that. So you can see that, you know, and again I can click on it and see the risk, right? So, so if you, if you go to "led by" at the bottom, you arrive at the bottom of the, the risk. If you go "leads to", you're basically navigating upwards the risk through. And the idea is that every risk should arrive at the corporate, at the top, right? So, so this now becomes a very powerful way to start to understand connections, and then we map the risks to the correct one, and I'll do a separate one to show how again, we connect all these risks to the particular CEO, CFO, you know, stakeholder, right? Now, the cool thing about this is you could see that the risks that you have go from zero, we don't have anything, to yes, you have an agent, bang, you got some risk.

So as we start to add basically these answers, you see that we basically start to populate and start to add the risks and they start to interconnect, which is really cool, right? So, the idea is that the changes here impact the risks that exist and how the risk register almost looks like and the evidence that we have, right? So, and what's interesting about this, is if you look for example at "governed", actually this is there because of, I was actually, when I was explaining Claude about how to do this, I was saying just the fact they have an agent, you're going to have risks, but I actually don't agree with these risks because, see even that loss of control, I would argue that's not the risk that I have by having an agent, right? So the logic here is like if I have an agent in production and I have a lot of these values which are pretty good, I don't buy that at the moment I have this, right? Because we said in this one that we already have some of these. So, I think this is a good example of why when you go and push your risk to be approved, the stakeholder is going to challenge you really hard. The cool thing is that we start to have the evidence to show exactly why we are saying this. So, I think that in this particular case, it has more to do with the fact that the agent touches EU act, so suddenly we are in compliance with the EU AI act, or we might be compliant with it, and we now have an agent in the mix, and then the organization, and we have, and even though here we say we can stop within a minute, right? There is still some disruption to production, right? Which is interesting, right? So we should capture that operation, right? Because the system, like that one's a good one, you know, stopping the agent might have an interruption. So, again, we need to capture these nuances.

The cool thing is this is all now fact-driven, which is super powerful.

## 3 · Role risk map · 3:15 · 5 Aug 2026

The org chart with risks flowing up it — and the ways a risk arrives at a person.

[“no agent”](https://youtu.be/yqQgff4RWuE?t=160)
### The org chart exists before any risk does

Under the **New** preset the structure is already there — board, CEO, CTO, CISO, CFO, DPO, chief product officer, platform owner, customer-facing service owner, SRE — and nothing is flowing through it.

That ordering matters. The organisation is not derived from the risks; the risks are routed onto an organisation that was described first. Which is why the same estate can be re-answered all day and the chart underneath never moves.

“If you have no agent, you have nothing.”

Nothing answered: the structure, carrying nothing.

[the CTO](https://youtu.be/yqQgff4RWuE?t=95)
### Held, versus arrived — and the tool separates them explicitly

Selecting the CTO lights the path *Board → CEO → CTO → Platform owner / CISO* and splits what the role carries into named sections. **Holds — 4**: *“Assigned to this role. Its own to deal with.”* **Arrives by the risk chain — 16**, with the tool’s own explanation of why that category exists:

“It arrives because the **risk graph** says so, not because anybody reports here — which is how a board entry ends up with an unexercised runbook underneath it.”

That sentence is the whole feature. An owner is not surprised at the top by something nobody carried up, because arrival is computed rather than reported. On the chart itself each role is labelled in the same two terms — the CTO reads `4 assigned · 25 through`, and the board simply `37 arrive here`.

The CTO: four of its own, sixteen that arrive because the graph says they must.

[the SRE](https://youtu.be/yqQgff4RWuE?t=130)
### At the bottom, a third category — and it is empty

The SRE / platform on-call is the leaf, *reports to Platform owner → CTO → CEO → Board*, and it **holds 9** — RISK-2, 6, 10, 11, 12, 13, 19, 22, 35 — the operational set the walkthrough describes as travelling upward from here.

The panel here reveals something the video only implies: there are **three** ways a risk reaches a role, not two. **Arrives by the risk chain — 2**, and **arrives by the org chart — 0**, glossed *“Held by somebody who reports here”*, answered *“Nothing below.”* Inheritance through the reporting line and causation through the risk graph are counted separately, which is what lets you ask a manager *why* they hold something and get a structural answer rather than a list.

“No risk then becomes orphaned, because every risk will flow upwards, and that’s super important.”

The leaf of the chart: nine held, two caused, nothing inherited — because there is nothing below it.

**Full transcript — Role risk map**

Okay, so this next video shows another super powerful capability that we had here to our risk graph explorer, which is the org chart, and how we have, in this case, the board, we have the CEO, we have three direct reports, and we have then the kind of the team, where the platform owner, to the CTO, to the CEO, to the board, and you can actually see, you know, it's quite nice, the chain, right, the chief product officer, you know, has a customer service owner who connects to the board, who responds to the CEO and the board, right? And we can kind of see the sequence of events, right? So, what we're going to see here is how as we add risks to the organization, right? You start to have risks that are flowing to here, right? Which is pretty cool, so you could see that as we add, basically, and we provide answers, you basically start to see the, fundamentally, the risks changing. And what's cool about it is you could see how they arrive, and one of the things that's quite interesting is that we have two modes already, because you could see that the CEO, in this case, or the board, right, receive all these risks, so the CEO, in this case, is assigned his three corporate risk registers directly to him, but you also have these risks that arrive from the risk chain, and that's very important. Right? So you basically could see that because somebody, you know, a senior, holds, he arrives because of the risk graph says so, right? So that means that these particular risks that exist there, which for example, come from here, so you could see that this risk here, so let's say, the SRE is holding risk 2, risk 6, risk 9, risk 21, and risk 31, and that risk is also now going to exist — same risks are going to be connected to the platform owner, who now has a couple more risks of itself, and now the CTO has a couple risks of itself but also inherits all the risks that we mentioned below all the way up. So it's pretty cool, right? Because again, same thing, right? So the DPO is assigned a couple of risks, and then, you know, that he has, right? And then, you know, it also arrives from the risk chain, and then you got the CFO, the same thing, right? And then the CEO, you know, connects the dots. So this is a really powerful capability because it's how you connect all the dots, right? So if you look at the different scenarios, if you have no agent, you have nothing, if you have a typical kind of agent deployment, you have this kind of shape, if you have a lot of exposure, you get a much bigger set of responsibilities, and you have the govern, we can see it's a much cleaner sort of flow of events.

And now we can start to challenge, you know, is those risks in the right place because everybody that is going to accept it is going to push back. But this is crazy powerful because now we start to see the relationships, and we see that no risk then becomes orphaned, because every risk will flow upwards, and that's super important.

## Where to go next

Each view gets a systematic treatment, screenshot by screenshot, on [**the seven views page**](../views/index.md). The vault itself — its read key, both live surfaces, and the publication rules it enforces on its own build — is on [the vault page](../index.md).


---

*[Site index for agents](../../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/risk-graph-explorer/videos/index.html)*
