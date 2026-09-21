# Build your startup on sgit vaults, sgit.ai

> For founders: a vault removes the four costs that usually stand between you and a first user (a database to run, hosting for your reader, an account, an install), so you can ship something usable, give it away briefly, take it away, and find out whether they missed it. What you get on day one, the ladder from first vault to first customer, what you still have to bring (billing, identity, server-side query), and the measured cost base.

*Source: <https://sgit.ai/startups/index.html> · site v0.4.2 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / Startups

For founders building on vaults

# Build your startup on sgit vaults

A large part of why sgit exists is to make it cheap enough to ship something a stranger can actually use, repeatedly, and to take it away again when you need to find out whether they missed it. That loop is hard mostly because the infrastructure under it is expensive: a database to run, hosting to pay for, an account for every reader, an install before anybody sees anything. **A vault removes all four.** This section is for founders who want to build on that, and it will grow as more of them do.

**The operating model comes first, because the technology is the easy part.** [**The most important question is whether they miss it →**](../articles/the-question-is-whether-they-miss-it.md) is the model this is all built to serve: ship something somebody can use, give it away briefly, take it away, and find out whether anybody noticed. Be profitable before you raise, so the investors are calling you. Open source everything, because the technology is not the moat. Read that first, then come back for the substrate.

## What you get on day one

Not a platform to sign up for. A format, a CLI and a credential, all open source, that between them remove the four things that usually stand between you and a first user.

| The usual cost | On a vault |
|---|---|
| **A database to run** | None. The store is encrypted files in cloud storage, read directly. Nothing runs between requests, so nothing is billed between requests |
| **Hosting for your reader** | None. A vault carries its own app, and it opens in the browser with no server of yours in the path. It also runs from a plain static host or a bucket, so your deployment is a copy |
| **An account, and an install** | Neither. [A read key](../docs/credentials.md) is the whole credential: the address, the capability and the decryption key in one string. You send it. They open it. There is nothing to sign up for and nothing to download |
| **Versioning you bolt on later** | Already there. Every change is a commit, every version is retained, and a reader can see the history, which means you can take something away and put it back without losing what was there |
| **An audit story for the first serious customer** | The server storing it cannot read it. That is the default, not a tier, and [the security model](../security/index.md) states exactly what the server does see |

The numbers behind that are measured rather than claimed. [Performance, cost, and running everywhere](../demos/fractal-graphs/performance.md) has the full set, and the shape of the bill is the part founders care about: **storage and egress only, no instance hours, and query compute paid by the reader's own device**. The entire published estate on this site is 2,662 files and 295 MB of object storage.

## First vault to first customer

The point of the model is a short loop. Here is what it actually looks like on this stack, with the page that owns each step.

| **1 · Put the thing in a vault** | `pip install sgit-ai`, create, commit, push. [Five minutes](../docs/quickstart.md), and it is the same verbs as git |
|---|---|
| **2 · Make it usable, not demoable** | Publish content with no code at all, or ship an app inside the vault. [Pick the surface first](../docs/surfaces.md): that choice decides more than anything after it |
| **3 · Give a read key to five people** | No onboarding to build, no invites, no seats. If the content is meant to be open, use the prefix that says so |
| **4 · Take it away** | Rotate the key and the trial is over. Nothing else about the product changes, which is the point: you are testing whether they miss it, not whether they liked the email |
| **5 · Charge, if they came back** | The stack does not do billing, and you should not want it to. What it gives you is a cost base low enough that a small price can be a profitable one |

**One honest caveat on step 4.** [Revocation is not retroactive.](../docs/credentials.md#read) Anybody who cloned while they had the key keeps what they cloned. For a trial that is usually fine, and it is better to know it now than to design as though a key could be recalled.

## What you still have to bring

This section would not be worth reading if it only listed what is free. A vault is a storage, distribution and versioning layer. It is not a product, and it is deliberately not several things.

- **Billing and payments.** Not here, not planned. Use whatever charges cards.
- **Identity and per-user accounts.** A read key is a capability, not a login. If you need to know *who* opened something rather than *that* it was opened, that is yours to build.
- **Server-side search and query.** The server cannot read the content, so it cannot index it. Whatever the client needs, the client downloads, which is fine at a megabyte and a design problem at a gigabyte.
- **The judgement about what to ship.** Obviously. But it is worth saying, because the cheapest part of this is now the part everybody used to spend their seed round on.

[When NOT to use sgit](../docs/limitations.md) is the longer version of this list, and it is kept honest on purpose.

## The arguments this rests on, and where they live

The market you are building into is described in [**What SaaS refused to build is exactly what the agents need**](../articles/what-saas-refused-to-build.md): most users were never happy, most features were never used, most licences sit idle, and the portability and APIs the incumbents starved to protect their moats are what an agent now needs. The opportunity it points at is the one this section is for: be the company that takes the brief and keeps it running.

Two of the three pillars have a whole site to themselves, because they outgrew a section here. They are worth reading before you commit to a commercial shape.

open-source.sgit.ai · Business & publishing · [Open source is a strategy ↗](https://open-source.sgit.ai/) · Why giving away the technology is the commercial choice rather than the charitable one, what it does to your architecture, and why it is the better exit for a founder who wants to leave with their tools. · “Open source is a strategy. It is not a charity.” · part of the sgit.ai network

subscriptions.sgit.ai · Business & publishing · [A subscription is not rent ↗](https://subscriptions.sgit.ai/) · The pricing trap most founders walk into by default. Charging rent for something nobody is using is a worse business than being paid when you deliver, and pay on demand is usually the healthier shape for both sides. · “A subscription is a discount for regular use, not rent on something you ignore.” · part of the sgit.ai network

## Evidence, rather than a pitch

Everything above is how this site itself is built, which is the only reason to believe any of it.

- **Thirty one vaults published with their read keys**, each with a page describing what it does and the vault running live inside it. [Open any of them](../demos/vaults/index.md) with no account and nothing installed.
- **The method is written down**, including the mistakes that produced each rule. [The publishing method](../demos/vaults/publishing.md) is written to be followed by somebody else's agent.
- **The measurements are repeatable**, with the commands printed. [Performance and cost](../demos/fractal-graphs/performance.md).
- **One person, working with agents.** The whole estate is built this way, which is the actual claim about how small a team this needs.

## Where to start

| **Read the model** | [The most important question is whether they miss it](../articles/the-question-is-whether-they-miss-it.md) |
|---|---|
| **Ship something today** | [Quickstart](../docs/quickstart.md), then [pick your surface](../docs/surfaces.md) |
| **Build with agents** | [The agent guide](../docs/agents.md) and [the skills](../skills/index.md), since this is how the work actually gets done here |
| **See what exists already** | [What exists, and what is still a design](../summit/startups.md), the sheet that says which is which |
| **Raising, eventually** | [sgit.ai for investors](../investors/index.md), published in the open, which is the same rule this section follows |

**This section is new, and deliberately small.** It will grow with the founders who use it, and when it outgrows a page it will become its own site, the way nineteen others already have. If you are building on vaults, the most useful thing you can send is what broke.

[← The operating model](../articles/the-question-is-whether-they-miss-it.md)[Open a real vault →](../demos/vaults/index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/startups/index.html)*
