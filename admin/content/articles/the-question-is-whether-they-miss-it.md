---
title: For a startup, the most important question is whether they miss it
date: 2026-09-21
author: Dinis Cruz
author_url: https://www.linkedin.com/in/diniscruz
summary: A startup operating and investing model in three pillars. Ship something somebody can actually use, give it away briefly, then take it away and find out whether anybody notices. Be profitable before you raise, so the investors are calling you rather than the other way round. And open source everything, because the technology was never the moat.
version: v0.3.9
tags: startups, strategy, open-source, investing, article
status: published
---

!shot startup-test-hero.webp | images/ | The startup test. Ship it, let them try it, take it away, and see whether anybody asks for it back.

Most advice about starting a company is about raising money. This is not that. It is the operating model I actually use, and it rests on three pillars that are easier to state than to do.

1. **Be profitable.** Ship a product that sells, at a price that works for you.
2. **Investors should be talking to you**, not the other way round.
3. **Open source everything**, because the technology is not the moat and you do not want to be locked into it.

They are in that order for a reason. Each one buys you the position you need to do the next.

!shot startup-model.webp | images/ | The loop. Ship something usable, give it away briefly, take it away, and find out whether anybody misses it. A no sends you back to the start with better information. A yes is the only thing that earns the right to charge, and charging at a profit is the only thing that earns the right to choose your investors.

## Pillar one: ship something somebody can use

Strip away the mythology and a startup is simple. **You make a thing somebody wants to buy, at a price that is profitable to you.** That is it. Whether the *company* makes a profit in a given year is a separate question with its own answer, but if the *product* is not profitable, it does not scale, and no amount of growth will fix that.

Which means the single most important skill is the ability to **ship**. Not to plan, not to pitch, not to architect. Ship. And ship every day, because shipping is how you find out what is true.

Be careful with the word, though, because it has been worn smooth. Shipping does not mean a proof of concept. It does not mean a demo, or a video of a demo, or a prototype you walk somebody through on a call. **It means a thing somebody else can go and use, on their own, and get value from.** It can be held together with tape. It can be vibe coded. Nobody using it cares how it was built, and neither should you, yet.

To ship that often you need the running cost to be near nothing, so build accordingly. Serverless. As few databases and as little live state as you can stand. In our case the file system *is* the database, which sounds like a compromise until you measure it: [what that actually costs, with the numbers](/demos/fractal-graphs/performance.html) is a whole page of its own, and the summary is that with nothing running between requests the standing bill for an estate of thirty one published graphs is a third of a gigabyte of object storage.

And do not underestimate the infrastructure. Getting a working thing into a stranger's hands is still, in 2026, genuinely hard, and a surprising amount of the toolchain is not designed to help you do it. **Solving that is not overhead, it is the first real product you build.** Everything after it gets cheaper.

## Then give it away, and then take it away

Now hand it to people for free. Not forever: a short window, whatever unit makes sense, but short. You want the feedback loop tight, and you want the cost of generosity to stay inside what you can absorb.

Just doing this solves dozens of problems you did not know you had. How do people get access. What breaks when somebody unfamiliar touches it. What they try first. What they never find. **The feedback starts the moment somebody who is not you has the thing.**

Then comes the part almost nobody does deliberately. **Take it away.** The trial expired. It is not available right now. Nothing else about the product changes, and no apology is needed.

And now ask the only question that matters:

> **Do they miss it?**

If they shrug and go back to their day, you do not have a product yet. You have something people will accept when it is free, which is a much weaker signal than it feels like from the inside. No sense of loss means no *why now*, and without a why now there is nothing to sell.

If they come back and ask for it, you have something. That is the moment the whole model turns on, and it is worth engineering your trial specifically so that this moment arrives early and unambiguously.

## Can you charge, and can you charge at a profit?

Two questions, and people routinely answer only the first.

**Is the price one they are happy to pay?** It has to sit inside the zone where they feel they are getting more than they are giving up. If you have to argue somebody into the value, the answer is no.

**And is that price profitable for you?** With one honest caveat: it might not be profitable today and still be the right price, if the economics clearly improve with scale. But keep it close enough that you can self fund the gap, because a gap you cannot cover yourself is how you end up back at pillar two on somebody else's terms.

Revenue comes first. **If you cannot get revenue at all, that is the problem to solve, and it is not a marketing problem.** Profitability is the milestone after it, and it is the one that changes your life, for reasons that are entirely about the next pillar.

A related trap, which has its own site because it deserves one: **do not reach for a subscription by default.** Charging rent for something people are not using is a worse business than being paid when you deliver. [subscriptions.sgit.ai](https://subscriptions.sgit.ai/) makes the full argument: a subscription is a discount for regular use, not rent on something somebody ignores. Pay on demand is usually the healthier shape, for both sides.

## Pillar two: the investors should be calling you

Here is the claim, stated plainly. **The worst possible time to raise money is before you are profitable**, before you have the product, before you understand the fit. Which is, of course, exactly when most companies raise.

Everything follows from the negotiating position.

**You are bargaining from weakness, and both sides know it.** You have no product and you have a clock. Profitability does not just mean money, it means *time*: when you are not bleeding, you can wait, and being able to wait is most of what a good negotiating position is.

**So the terms are bad, and the worst of them are not about money.** They are about control. You hand over a say in the business to people who, in most cases, do not understand the business. They do not understand the technical properties, they have not lived the vision, and that is not a character flaw: their job is to make money. But their focus is now structurally misaligned with yours, and their opinion has been given weight. **I think that is one of the most common ways companies fail**, and it is entirely self-inflicted at the moment of signing.

The analogy I keep coming back to is music. **Do not get signed before you have the album.** Write the songs. Record them, in a bedroom studio if that is what you have. Play locally. Get people listening, get people buying. *Then* take the record deal, and take it as somebody who already has an audience and does not strictly need one.

That is the whole of pillar two. Not "never raise". **Raise from strength, on terms you set, from people who came to you because the thing already works.**

## Pillar three: open source everything

This one surprises people, because it sounds like giving away the asset. It is the opposite, and there are five reasons, each of which stands alone.

**The technology is not the moat.** Believing it is will shape every decision you make badly. Treating it as open from the start forces you to find the thing that actually is defensible, which is usually the data, the relationships, the distribution, or the speed at which you ship.

**You get a better architecture.** Code written to be read by strangers has cleaner boundaries. Not because you are more virtuous in public, but because anything embarrassing has to be fixed rather than hidden.

**You stay comfortable throwing things away.** A team that has never deleted a component is a team that will defend one long after it should have gone. Open source normalises disposal.

**It is better for the customer**, obviously, and they can tell. Nobody has to trust a promise about what happens if you disappear, because they can read the thing.

**And it is a much better exit for you, the founder.** This is the one people miss. Build proprietary and you will accumulate a pile of technology, much of it not even specific to the startup, that you cannot take with you. Build in the open and the work is still yours when you move on. **You leave with your tools.**

[open-source.sgit.ai](https://open-source.sgit.ai/) carries the longer version of this argument, and its thesis is the sentence to remember: open source is a strategy, not a charity.

## Why this is on a site about encrypted vaults

Because the model has a substrate, and we have spent a year building it.

Every pillar above asks for the same thing: **shipping a usable product should be cheap, fast, and reversible.** That is not a slogan, it is an infrastructure requirement, and it is most of the reason this model is hard to follow. A vault is our answer to it. Data, app, history and sources travel as one string. There is no database to run, no hosting for the reader, no account, no install. The whole [published estate](/demos/vaults/index.html) is 2,662 files and 295 MB of object storage, with nothing running between questions, and a reader opens any of it with a single read key.

Which makes the cost of shipping a small product to a few real users low enough that you can do it repeatedly, be wrong in public, take it away, and find out whether anybody missed it. **That loop is the product I most want other people to have**, and it is why the whole stack is open source, down to the [measurements](/demos/fractal-graphs/performance.html) and the mistakes.

If you are building something on this, I would like to hear about it.
