# The author’s walkthroughs — Risk Graph Explorer

> Three recorded walkthroughs of the risk graph explorer with full transcripts: the graph browser, risk chains, and the role risk map — the designer explaining why the tool is shaped as it is.

*Source: <https://sgit.ai/demos/vaults/risk-graph-explorer/videos/index.html> · site v0.2.29 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../../index.md) / [Vaults](../../index.md) / [Risk Graph Explorer](../index.md) / Walkthroughs

# The author’s walkthroughs

Three recorded walkthroughs of this vault, with full transcripts. They are the best explanation of *why* the tool is shaped as it is — the reasoning behind a view is rarely visible in a picture of it, and these are the designer thinking aloud while using it.

**Why the transcripts are here in full.** A video is invisible to a search engine, to [llms-full.txt](../../../../llms-full.txt), and to any agent reading this site as documentation. The transcript is the content; the video is one rendering of it. Lightly cleaned for filler words, otherwise unedited — including the moment the author disagrees with his own tool, which is the most useful passage in all three.

## Graph Browser · 4:21 · 5 Aug 2026

How answering the questions builds the fact graph — and why a "no" is still information.

**Watch:** [youtu.be/PP6zsrC0KEg ↗](https://youtu.be/PP6zsrC0KEg) · **Shows:** [The estate](../views/index.md)

**What it establishes**

- A vault with no agent still produces a fact; absence is recorded, not skipped.
- The question path walks reach → capability → change → stop → authority → blast radius → egress → reversibility → procedure → reconstruction → account ownership.
- Different edge types are drawn for different relationships, so the graph is evidence rather than decoration.
- "This is a great way to almost in one day capture all the data."

### Transcript

Okay, so I want to just talk about this graph explorer that we pushed as an MVP, which is I think ridiculously powerful as a way to present. So what we have here now is how the questions we originally talked about in the demo. But it's in a weird way, we start with the first question, right? Do you have an agent and where does it run? Because if you don't have an agent, then we only have one piece of information here, which is — and but this is a fact, right? So this here captures the facts and information. So you could see that you have both the operation state or the test environment. And it's interesting because the risk will be very similar.

The only question is whether it's live, so in a way that there's a risk level that is probably going to be there, right? So let's say you have one, right? And now you can see what kind of data is enriched. Let's say I got personal data. And what's cool about this is you can see that what's happening is this graph is now going to be populated with the data that we collected. So you can think of this graph as the evidence piece, right? So look, there's the output of facts and decision. Okay, it informs decisions.

So you can see that what's cool about it is that we actually have different, in a way, almost different edges depending of what it is. And then, what can do with the data, right? It cannot see it, or reads it, or reads and changes. So this is a typical example of you have a production system, right, that touches personal data, accounts, contact details, it informs the decision, you know, of the there, and it reads and changes. So it's a typical agent, right? And now you got it. So now you talk about the information of this.

You know, can the agent change things, right? Can you read and report? Can changes? Can change on its own? So you start to map, you know, for example, how it's done, right? With a person approval or change. So that so this is where you take that to the next level. So it changes on its own, right? So how do you stop it? Let's say you have an action to stop, or eventually can stop, or we don't know how to stop it. And how long should we stop it? Is it minutes? An hour? Don't know. So you start to see again, you know, the stop control now we map stop in many actions, never, time for, an hour, minutes, right? And then, have you actually stopped it? Yes, we have, only in test, never, right? Do you know the effects of stopping it? Have we mapped it? Is it partially? Etc.

So this is an interesting one because this is connected to the stop control. So you can actually see that this is here depends on that one. So it's in a way now a next line up, like down, sorry, of the flow. Is there a named person? Do you have a named person or not? So this is the stop authority, right? The team, you know, if it really is, you know, misbehavior for full speed, could, you know, what could you reach, right? Internal only, customer facing? Don't know. So this would be customer only.

So you could now start to see again, you know, what's the damage, that it can acts, you know, can you reach anything outside the network? This means that does it have internet access or not. So again, you can see here, outbound access, right? For example, no egress. Could, you know, could you undo the damage, right? So let's say you have fully reversible versus not, or some change are forever, which is important, right? Is there a written procedure for how you pull the plug? You tested it, you've written, you don't have it. Could you reconstruct what you did, for example, every day, right? Or, you know, do you have, you know, fully or partially or not, right? Cuz sometimes you have backups, but they do not allow you to restore specific things, and whose account it is, right? A service account, a named person, a team, right? So, you know, what is actually the, for example, the flow that happens. And then this is great, like because you can look at it.

This is — I love this, right, because it's a great way to almost in one day capture all the data. Just for reference, we then capture the context. We have now these really cool road map with all the risks that flow forward. We also have these risk chains, which I go in more detail in others, but that means that every risk that is then connected connects to the top level, right? And then we even have a risk register, right? And for every risk that you have here, you can see who's assigned, who causes it, and who leads to, and how does it connect, right? So it's pretty cool.

## Risk Chains · 4:18 · 5 Aug 2026

Risks that cause risks — and why being able to disagree with the register is the feature.

**Watch:** [youtu.be/kWip3QnuN1I ↗](https://youtu.be/kWip3QnuN1I) · **Shows:** [Risk chains](../views/index.md)

**What it establishes**

- Every risk should arrive at the corporate register at the top; the chain is how it gets there.
- "Leads to" navigates upward, "led by" walks back down to the answers that caused it.
- The author disagrees with his own tool on camera — and resolves it by pointing at facts.
- "When you go and push your risk to be approved, the stakeholder is going to challenge you really hard. The cool thing is that we start to have the evidence to show exactly why we are saying this."

### Transcript

...to go through this UI which I think is starting to really show the idea of connecting the risks upstream. So what you have here to show you, this is part of the UI that we have that you know, you can basically see the multiple workflows that we have from a typical, non-exposed, one that's actually quite governed. What I really like is this, let's look at the exposed first, this sort of chain, and let's consolidate this here. So the idea here is that the risks connect from one element to the other. So if you look at this guy here, for example, you have risk 6.

"The production can be changed by an agent." This is now connected to that risk. "Organization acts to the system that acts for a person", who then creates this risk, right? "Organization asks to, Tech to be changed." And then hits the top two risk register. So the logic here, this is the corporate risk register, so you can see that that particular risk will arrive there, and when I click here, I can also see the reverse. So I can see, if we say we have a risk of this, why is it? It's because we have that one, and we have that one, and we have this one, and that one. And I could also see it here, what actually happens.

You can see, for example, this particular risk, corporate 2, who is assigned to, and then to the CEO, to what, you know, is reduced by this particular choices, touches GDPR, and then leads to this. So, so actually, so this is a good example, so you can see that this guy here, this risk leads to these two, and is led by that and that. So you can see that, you know, and again I can click on it and see the risk, right? So, so if you, if you go to "led by" at the bottom, you arrive at the bottom of the, the risk. If you go "leads to", you're basically navigating upwards the risk through. And the idea is that every risk should arrive at the corporate, at the top, right? So, so this now becomes a very powerful way to start to understand connections, and then we map the risks to the correct one, and I'll do a separate one to show how again, we connect all these risks to the particular CEO, CFO, you know, stakeholder, right? Now, the cool thing about this is you could see that the risks that you have go from zero, we don't have anything, to yes, you have an agent, bang, you got some risk.

So as we start to add basically these answers, you see that we basically start to populate and start to add the risks and they start to interconnect, which is really cool, right? So, the idea is that the changes here impact the risks that exist and how the risk register almost looks like and the evidence that we have, right? So, and what's interesting about this, is if you look for example at "governed", actually this is there because of, I was actually, when I was explaining Claude about how to do this, I was saying just the fact they have an agent, you're going to have risks, but I actually don't agree with these risks because, see even that loss of control, I would argue that's not the risk that I have by having an agent, right? So the logic here is like if I have an agent in production and I have a lot of these values which are pretty good, I don't buy that at the moment I have this, right? Because we said in this one that we already have some of these. So, I think this is a good example of why when you go and push your risk to be approved, the stakeholder is going to challenge you really hard. The cool thing is that we start to have the evidence to show exactly why we are saying this. So, I think that in this particular case, it has more to do with the fact that the agent touches EU act, so suddenly we are in compliance with the EU AI act, or we might be compliant with it, and we now have an agent in the mix, and then the organization, and we have, and even though here we say we can stop within a minute, right? There is still some disruption to production, right? Which is interesting, right? So we should capture that operation, right? Because the system, like that one's a good one, you know, stopping the agent might have an interruption. So, again, we need to capture these nuances.

The cool thing is this is all now fact-driven, which is super powerful.

## Role risk map (the risk org chart) · 3:15 · 5 Aug 2026

The org chart with risks flowing up it — and the two ways a risk arrives at a person.

**Watch:** [youtu.be/yqQgff4RWuE ↗](https://youtu.be/yqQgff4RWuE) · **Shows:** [Role risk map](../views/index.md)

**What it establishes**

- Two modes: risks assigned directly to a role, and risks that arrive through the chain.
- A role inherits everything held below it and adds its own — the CTO carries the SRE’s set plus its own.
- Presets change the shape: nothing, typical, exposed, governed.
- "No risk then becomes orphaned, because every risk will flow upwards, and that’s super important."

### Transcript

Okay, so this next video shows another super powerful capability that we had here to our risk graph explorer, which is the org chart, and how we have, in this case, the board, we have the CEO, we have three direct reports, and we have then the kind of the team, where the platform owner, to the CTO, to the CEO, to the board, and you can actually see, you know, it's quite nice, the chain, right, the chief product officer, you know, has a customer service owner who connects to the board, who responds to the CEO and the board, right? And we can kind of see the sequence of events, right? So, what we're going to see here is how as we add risks to the organization, right? You start to have risks that are flowing to here, right? Which is pretty cool, so you could see that as we add, basically, and we provide answers, you basically start to see the, fundamentally, the risks changing. And what's cool about it is you could see how they arrive, and one of the things that's quite interesting is that we have two modes already, because you could see that the CEO, in this case, or the board, right, receive all these risks, so the CEO, in this case, is assigned his three corporate risk registers directly to him, but you also have these risks that arrive from the risk chain, and that's very important. Right? So you basically could see that because somebody, you know, a senior, holds, he arrives because of the risk graph says so, right? So that means that these particular risks that exist there, which for example, come from here, so you could see that this risk here, so let's say, the SRE is holding risk 2, risk 6, risk 9, risk 21, and risk 31, and that risk is also now going to exist — same risks are going to be connected to the platform owner, who now has a couple more risks of itself, and now the CTO has a couple risks of itself but also inherits all the risks that we mentioned below all the way up. So it's pretty cool, right? Because again, same thing, right? So the DPO is assigned a couple of risks, and then, you know, that he has, right? And then, you know, it also arrives from the risk chain, and then you got the CFO, the same thing, right? And then the CEO, you know, connects the dots. So this is a really powerful capability because it's how you connect all the dots, right? So if you look at the different scenarios, if you have no agent, you have nothing, if you have a typical kind of agent deployment, you have this kind of shape, if you have a lot of exposure, you get a much bigger set of responsibilities, and you have the govern, we can see it's a much cleaner sort of flow of events.

And now we can start to challenge, you know, is those risks in the right place because everybody that is going to accept it is going to push back. But this is crazy powerful because now we start to see the relationships, and we see that no risk then becomes orphaned, because every risk will flow upwards, and that's super important.

## Where the ideas landed

Each walkthrough is matched to a screenshot of the live vault, with the mechanism explained, on [**the seven views page**](../views/index.md). The vault itself, with its read key and both live surfaces, is on [the vault page](../index.md).


---

*[Site index for agents](../../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/risk-graph-explorer/videos/index.html)*
