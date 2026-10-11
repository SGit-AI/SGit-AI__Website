---
title: I miss it, so it is working: the people who decide the roadmap have to use the product, and the vault the newsroom now needs
date: 2026-10-11
author: Dinis Cruz
author_url: about/index.html
summary: I read the newsroom on my iPhone, my iPad, my laptops and my iMac, and they do not agree: four balances, four sets of personas, four reading histories. I miss a feature, and that is the best news this week. The test I keep coming back to, from For a startup, the most important question is whether they miss it, applies to the people who build a product too: if they have access, can change it, and still do not use it, something is missing, and it is not the code. I failed that test with good ideas before, The Cyber Boardroom and MyFeeds among them. The vaults pass it now: I create them all the time, my agents create them, and they are getting good because they are used. And when the people who decide the roadmap are users, the next feature announces itself; with agents that can build almost anything, that sense of direction is the scarce part, and the speed of the loop, from a comment to an article to a feature, is the moat. This article makes that case, and ends with the brief for the feature I miss: the reader's own encrypted vault on the newsroom, with an access key, a key pair for signing and receiving, a log per device that merges without conflict, adding a device, and a one-way line to the agent that edits the site.
version: v0.7.54
license: https://creativecommons.org/licenses/by/4.0/
tags: product, dogfooding, startups, feedback-loop, execution-speed, vaults, sync, pki, passkeys, newsroom, personas, brief, article
status: published
---

!shot mi-devices.webp | images/ | The feature I miss. Today, every device keeps its own reading account, so the newsroom on my phone and the newsroom on my iMac are different newsrooms. With the reader's own encrypted vault, every device writes what it did and reads what the others did, and the server sees only ciphertext.

I read the newsroom everywhere now. On my iPhone, on my iPad, on my laptops and on the iMac on my desk. And this week I hit a problem I am very happy to have: they do not agree. Each one has its own balance, its own personas, its own reading list and its own history, because each one is a separate browser, and the newsroom keeps everything in the browser. The account page even says so: "if encrypted vaults are added this page will say so".

I want them in sync. I miss a feature. And that, more than any number on this site, tells me the newsroom is going in the right direction.

## In short {#short}

- **When you do not have it, you miss it.** That is the test in [For a startup, the most important question is whether they miss it](/articles/the-question-is-whether-they-miss-it.html), and it applies to the people who build a product, not only to its customers.
- **The people who decide the roadmap have to be users.** The developers, the product owner, the founder. They give the best feedback, find the best uses, and set the best direction. I think it is one of the reasons Apple is so good at what it does: it uses what it makes.
- **I failed this test before.** The Cyber Boardroom, MyFeeds, and early on even sgit as a startup: good ideas, and I still think so, but I was not using them. If I have access, can change it, and still do not use it, something is missing.
- **The vaults pass it now.** I create vaults all the time, my agents create them, we share them, and 54 are published here. They are getting good because they are used.
- **Direction is the scarce part.** Agents can build almost anything, in any direction. Usage is what gives a product its direction, its context and its focus.
- **The loop is the moat.** A user makes a comment, I write an article, a feature ships: this week a list made for one person went from brief to live in 81 minutes. Speed of execution is what is hard to copy.
- **The feature I miss is the reader's own vault.** An access key, a key pair, a vault per reader, a log per device that merges without conflict, a way to add a device, and a one-way line to the agent that edits the site. The brief is below.

## The people who decide the roadmap have to use it {#use}

A strong connection with users is critical, and everybody says so. What is said less often is who the most important users are: the people building the product, and above all the people who control the roadmap. If the developers and the product owner use it every day, on real work, the loop between using it and changing it is as short as it can be. They feel the friction first. They find the uses nobody planned. And they know, without a survey, which of the hundred possible next features is the one that hurts.

I think this is one of the reasons Apple is so successful. As far as I can see from the outside, the people there use what they make. The feedback loop runs through the people in charge, and that makes all sorts of mechanisms and workflows possible that a company building for someone else cannot have.

When makers do not use what they make, the opposite happens, and it is a signal. I have seen it in startups many times: a product whose own team uses something else, or uses it only for the demo. It usually means the product is not as good as it looks, or not as simple to deploy, or valuable only in a narrow set of cases. Nothing in the code says so. The behaviour of the team does.

## The brutal part {#brutal}

This is brutal to say about my own work, and it is true. My last startups were good ideas. The Cyber Boardroom, MyFeeds, many of the other things I experimented with, and early on even sgit as a startup. I still think they are good ideas. But I was not using them. And that was the signal I should have listened to: if I have access, I can customise it, I can do a lot with it, and I still do not use it, then something is missing.

The vaults are the opposite story. I use them all the time now. I create vaults for almost everything, my agents create vaults, we share vaults, we build examples in vaults, and 54 of them are published on this site with their read keys. They are getting really good, and it is not because of a roadmap. It is because every day I hit something, and the next release fixes it.

That is why releasing is so powerful, and why trying to use what you release is even more powerful. Momentum does not come from the plan. It comes from use.

## Direction is the scarce part {#direction}

There is a second reason this matters more now than it did. A model that can go in every direction needs someone with a direction, as I wrote in [How much of this did I write?](/articles/how-much-of-this-did-i-write.html) and again in [Knowing when to stop](/articles/knowing-when-to-stop.html). With agents, we can develop just about anything. What we cannot generate is the sense of what to build next, for whom, and when to stop. Context and focus come from somewhere, and the most reliable place they come from is using the thing.

So when I say I miss a feature, that is not a complaint. It is the product telling me where it wants to go, through the only user whose day it fully controls.

## The loop is the moat {#moat}

In [whether they miss it](/articles/the-question-is-whether-they-miss-it.html) I wrote that the technology is not the moat; what is defensible is "the data, the relationships, the distribution, or the speed at which you ship". This week has made the last one concrete.

!shot mi-loop.webp | images/ | Use it, miss it, write the brief, ship it, and use it again. This week the loop ran three times; the fourth turn is this article.

A workflow I now have most days: somebody makes a comment, I write an article, a feature ships, and I use it. I put myself as a user in the middle of the loop, deliberately. In [From me to you, in a link](/articles/a-reading-list-in-a-link.html), a reading list made for one person went from brief to live in 81 minutes; [a link to a persona](/articles/a-link-to-a-persona.html) went from brief to live in 17 hours. Fast prototyping to production, and fast release, is what is hard to copy, much harder than any single feature.

## Part two: the brief for the feature I miss {#brief}

*For the session that runs newsroom.sgit.ai. Written by the sgit.ai site session for Dinis Cruz, 11 October 2026. Dinis decides what ships, and is the first user.*

### What to build {#what}

The reader's own encrypted vault, so the newsroom is the same on every device: personas, reading history, reading list, ratings, picks kept and put out, notes on articles, and receipts. Nothing on a server of ours, no account database, no password. We already have the pieces: vaults, the [vault web app](https://vault.sgraph.ai/), browser code that reads and writes vaults in [tools.sgraph.ai](https://tools.sgraph.ai/), append lanes, and the published key the newsroom already uses for [sending your reading](https://newsroom.sgit.ai/account/share.html).

### 1. Connect {#connect}

- **An access key.** Creating and pushing to a vault needs an access key for the vault server: the thing people will buy, and that I will hand out at first. The reader pastes it on the account page; it is kept in the browser's storage for this site, never put in a URL, and removable in one tap. The page says what it is for and what it lets someone do.
- **A key pair for the reader.** Generated in the browser with Web Crypto on first connect, the private key kept non-extractable where the browser allows. The public key goes into the reader's vault. It is used to sign what the reader writes, such as a note on an article, and to receive messages encrypted to them. This is the first real use of [RFC 0001](/articles/rfc-0001-public-key-cryptography-for-sgit.html) on the newsroom.
- **A vault.** The first time, the site creates a vault for the reader; or the reader pastes the key of a vault they already have. The vault key is shown once, with a plain instruction to save it in a password manager. It never leaves the reader's devices except into that password manager. It is never sent to us.

### 2. What is kept, and how it merges {#merge}

- **One log per device.** Each device appends what it did, as events: a page read and how far, a rating, a persona created, kept or removed, a reading-list change, a note, a receipt. It never edits another device's log.
- **State is computed, not stored.** Every device reads every log and computes the same personas, history, lists and balance. Two devices that were offline both write their own logs, and the merge is a union: no conflicts to resolve.
- **Receipts are counted once,** by their payment reference, so a top-up made on the iMac appears on the iPhone and is not credited twice.
- **The local copy stays.** Losing the connection, or the access key, leaves the browser's own copy working as it does today.

### 3. Add a device {#device}

- **First version:** on the device already connected, "Add a device" shows a code to scan or a text to paste, carrying the vault key and the access key, on screen only, never in a URL or an email. The new device connects and reads the logs.
- **Next:** a passkey that unlocks the keys, on the design of [secrets.sgit.ai](https://secrets.sgit.ai/), so the reader does not handle a key at all. And sign-in with Google, which the newsroom also needs: it says who you are and can recover access to what you bought, but it does not hold your key, and the design must not pretend it does.

### 4. A line to the agent that edits the site {#line}

- **One-way, by choice.** A note on an article can be marked "to the newsroom". It is encrypted in the browser to the desk's published key, the same one [sending your reading](https://newsroom.sgit.ai/account/share.html) already uses, and dropped into a write-only lane. The agent that edits the site reads it; nothing else can.
- **The reply is the change.** If the note asks for a correction or a clarification, the answer is a new version of the article, and the article's version history shows it.
- **Sharing more is the reader's call.** A reader can also give an agent a read key to a vault of notes. It should be a separate vault from their reading, because a read key opens everything in its vault.

### 5. Security, said plainly {#security}

- **What the vault server sees:** ciphertext, its size, and when it is written. Not what you read.
- **What a script on the site could see:** everything in the browser, including the keys. So the newsroom keeps loading no third-party scripts, and the account page says, in its words, what is kept where.
- **What losing the vault key means:** the other devices stop syncing; each keeps its own copy. That is why the key is shown once, with the password manager instruction.

### 6. How to know it works {#tests}

- Two browsers, the same vault: read on one, see it on the other; rate on both while offline, reconnect, and both agree.
- A top-up on one device appears once on all of them.
- Removing the access key, or the vault, leaves the local reading account intact.
- A [synthetic reader](/articles/how-to-run-synthetic-users.html) with a phone and a laptop, who has never heard of a vault key: do they understand what to save, and why?
- And the real test: I use it, on four devices, for a week, and I stop missing it.

### 7. What not to build {#not}

No account database, no server endpoint of ours, no email and password, nothing that sends the vault key anywhere, and no sync of anything the reader did not do on purpose.

## What this does not claim {#limits}

- **One user is not a market.** I am the first user, and the best placed to feel the gap, but that is a direction, not proof that others will want it. Other readers, and the synthetic ones, are how we find out.
- **The past is my own account of it.** Why my earlier startups did not take off is more than one reason. Not using them is the one I can see most clearly, and the one I can do something about now.
- **None of the vault feature is built.** The brief is a design; the pieces it builds on exist.

If you build products and want to compare how your team uses its own, or you want to try the newsroom on every device you have when this ships, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from {#sources}

A voice memo of mine, recorded on 11 October 2026 after a day of reading the newsroom on four devices, written by this site's agent in the voice of this site. The argument and the editorial responsibility are mine. The figures were drawn for this article; the balances in the first figure are illustrative. The times in the second are from the git logs of this site and of the newsroom. The account page's own sentence about vaults, and the published key and write-only lane used for sending your reading, are from the live newsroom on 11 October 2026. Related: [For a startup, the most important question is whether they miss it](/articles/the-question-is-whether-they-miss-it.html), [Knowing when to stop](/articles/knowing-when-to-stop.html), [From me to you, in a link](/articles/a-reading-list-in-a-link.html), [A link to a persona](/articles/a-link-to-a-persona.html), [No server, by design](/articles/no-server-by-design.html), [Where the vault keys live](/articles/where-the-vault-keys-live.html), [RFC 0001](/articles/rfc-0001-public-key-cryptography-for-sgit.html) and [How to run synthetic users](/articles/how-to-run-synthetic-users.html).
