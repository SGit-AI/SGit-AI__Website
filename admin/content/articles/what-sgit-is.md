---
title: Git for things you cannot put on GitHub
date: 2026-08-25
summary: An introduction to sgit and sgit.ai — what an encrypted vault is, why version control had to be rebuilt to get one, and what nineteen published vaults look like when the server storing them cannot read a byte.
version: v0.2.42
tags: intro, zero-knowledge, vaults, agents
status: published
---

There is a category of file that has nowhere good to live.

A risk register with real system names in it. A regulatory analysis you are still arguing about internally. The working memory of an AI agent that has been reading your codebase for a month. Client material under NDA. Anything a lawyer would want to see before it went near a third party.

All of it wants exactly what git gives you — history, branches, diffs, the ability to hand somebody a link and know what they will see. And all of it is the reason people say *"we can't put that in GitHub."* So it ends up in a shared drive, an email thread, or a Notion page nobody can diff, and the version history that mattered is gone.

**sgit is git for those files.** Encrypted before they leave your machine, versioned exactly like git, stored on a server that cannot read a single byte.

!shot site-home.webp | images/ | sgit.ai — `pip install sgit-ai`. Pure Python, two runtime dependencies, Apache-2.0.

## The part that is easy to say and hard to build

Zero knowledge is a claim people make loosely, so here is the precise version: **the server holds ciphertext and nothing else.** Not your filenames, not your directory structure, not your commit messages. Encryption and decryption happen on your machine. There is no key escrow, no admin override, no support engineer who can recover it for you — and that last part is a feature with a real cost, which is worth being honest about up front.

What makes it work is a single string:

```
<24-char passphrase>:<vault-id>
```

That is the **vault key**, and it is three things at once — the address of the vault, the authorisation to write to it, and the key that decrypts it. Lose it and the data is gone. Leak it and someone can rewrite your history.

From it you can derive, one way, a **read key**: same vault, read-only, safe to publish. That asymmetry is the whole sharing model. Every vault linked from sgit.ai is published as a read key, and no vault key has ever been published — a rule enforced by a tripwire in the release pipeline that scans every file before either remote is touched.

## Ten seconds of proof

The read key is the entire credential. No account, no login, no access request:

!shot cli-clone.webp | images/ | A real clone of the published EU AI Act vault. 273 objects, 207 files.

Now the same vault, as the machine storing it sees it:

!shot cli-ciphertext.webp | images/ | 786 bytes of AES-256-GCM ciphertext. The object's name is a SHA-256 of the encrypted bytes.

That second screenshot is the argument. The object is **content-addressed over its ciphertext**, which means the host can deduplicate it, cache it for a year, and serve it from a CDN — while remaining unable to tell you what it is. You get the operational benefits of a normal object store without granting it the usual price of admission.

Underneath, it is a real version control system rather than a sync folder: multi-parent commits, a tree per directory, deterministic refs derived by HMAC, a genuine merge-base computation across all parents, and three-way merge. Branches, diffs and history all work, on content the server cannot interpret.

## Nineteen vaults you can open right now

The best way to understand a vault is to open one. **Every vault on sgit.ai is live** — the screenshots are of real vaults, opened with the read keys published beside them.

!shot site-vaults.webp | images/ | The published vaults. Each one carries its read key on the page.

They range from a photo library to Regulation (EU) 2024/1689 parsed from official Formex XML into 1,523 nodes and 1,944 edges. Before writing this I cloned all nineteen from their published keys: **1,389 files, no failures.**

## The part that surprises people

A vault can contain an *application*, not just documents — and that application runs against the vault without ever being handed a credential.

!shot permissions.webp | ../demos/vaults/risk-graph-explorer/images/ | `"permissions": {}` — the app requests nothing, and is granted nothing.

Look at `"permissions": {}` in that file. The app asks for no filesystem access at all. It still renders the whole risk graph, because the host reads the vault and passes results in. The app never sees a key. **Capability without credential** — and it means you can run code you did not write against data you care about, with the blast radius set by a config file you can read in one screen.

## Why there is a network of sites

sgit.ai is one of **nineteen** sites on `*.sgit.ai`, each taking one question further than a section could. Most of the thinking behind sgit now lives out there rather than here.

!shot site-network.webp | images/ | The network directory: start from the question you arrived with.

A few of them, to give the range:

- [**graphs.sgit.ai**](/network/graphs.html) — *"A node is just a node. Meaning lives in the edges."*
- [**risks.sgit.ai**](/network/index.html#risk-governance) — *"You cannot deny a risk. You can only say how long you accept it."*
- [**llms.sgit.ai**](/network/index.html#agents-ai) — your app calls a language model without ever holding an API key.
- [**issues-fs.sgit.ai**](/network/index.html#graphs-method) — the issues are files, and the files are a graph.
- [**open-source.sgit.ai**](/network/index.html#business-publishing) — *"Open source is a strategy. It is not a charity."*
- [**sg-sentinel.sgit.ai**](/network/sg-sentinel.html) — an edge guard design that says `NOT BUILT` at the top of every page.

The [network directory](/network/index.html) starts from the question you arrived with rather than the list of domains.

That last one is the house style in miniature. Each site publishes its argument **before** the thing exists, and states plainly what has shipped and what has not. graphs.sgit.ai devotes a page to [where its own approach loses](https://graphs.sgit.ai/about/participant.html). We would rather be checkable than impressive.

## Try it

```
pip install sgit-ai
sgit clone sgit_rk1_c004daae386e8d17fa648884acc527018bd4ea1116ad673fb2f1b068011695c9:73heuprz
```

That is the EU AI Act vault — 207 files on your disk in under a minute, from a key printed on a public web page, with no account anywhere.

If you would rather not install anything, [every vault opens in the browser](/demos/vaults/index.html) from the same key.

> **Status, plainly.** sgit is beta and says so on every page. The CLI is `pip install sgit-ai`, Apache-2.0, pure Python. The site you are reading is itself served from a vault, released 59 times, and each release is [logged in full](/admin/versions.html) — including the ones that broke something.

This article is also published as a [LinkedIn newsletter post](https://www.linkedin.com/pulse/git-things-you-cannot-put-github-dinis-cruz-qwrte/) — same argument, same screenshots, for readers who live there.

*Written by Dinis Cruz and the agentic team working with him. Licensed CC BY 4.0 — reuse it, quote it, argue with it.*
