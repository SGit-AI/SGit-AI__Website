# Who holds the keys? A call for collaboration on vault key management, sgit.ai

> An open call to password managers, identity providers and platform credential managers. sgit vaults are encrypted on the client and opened in a browser with one key, and keys now multiply faster than people can manage them by hand. We would rather use a key manager than build one. The page explains sgit for someone new to it, states what we are looking for (something that exists, a joint pilot, or an open specification), the requirements (browser first, key kinds kept apart, release only on approval, end-to-end sharing, names in plain words that are addresses and never keys, revocation, keys for agents), a sketch of the share flow, why the old word-based token was removed, and what we would bring.

*Source: <https://sgit.ai/partnerships/vault-key-management.html> · site v0.6.4 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Partnerships](index.md) / Vault key management

A call for collaboration · public material only · 24 September 2026

# Who holds the keys? A call for collaboration on vault key management

**We are looking for a key manager, not building one.** [sgit.ai](../index.md) makes encrypted vaults: folders whose contents are locked on the owner's device before they are stored anywhere, and which open in a browser for anyone holding the right key. That works. What does not scale is the key itself. Every vault has one, people now hold dozens, AI agents are starting to create them by the hundred, and today those keys travel by copy and paste. Storing, indexing, sharing and taking back secrets is what password managers and identity providers already do well. This page asks whether one of you already has a way for us to use that, in the browser, and if not, whether you would like to build it with us in the open.

**If this is the first time you have heard of sgit**, that is expected, and the page is written for you. It starts with the short version, then what we are asking for and the requirements, then [what sgit is in two minutes](#sgit), then diagrams of how it could work, and only then the detail and the evidence. Nothing here is confidential and there has been no conversation with any organisation named on it. It can be forwarded as it is.

## In short

- **The product.** sgit is git for encrypted vaults: a versioned folder, encrypted on the client, stored on any host that cannot read it, and opened in a browser with one string, the key. It is open source under Apache-2.0.
- **The problem.** The key is the whole access control. There is no account, no reset and no revocation list. Lose it and the vault is gone; leak it and the only remedy is to re-encrypt under a new one. That is a key management problem, and it grows with every vault.
- **Why not solve it ourselves.** We could keep keys inside another vault, and we have designs for that, but the first key still has to live somewhere. Key management is a discipline of its own, with recovery, device sync, sharing, audit and enterprise policy, and it is already done well by people who do nothing else.
- **What we are asking for.** A way, in the browser, for a person to keep their vault keys in the password manager or identity system they already use, to open a vault with a passkey or a biometric prompt, and to share a vault with someone else by sending a short name in plain words rather than the key.
- **The one hard rule.** The words must be an address, never the key. sgit once shipped a word-based token that *was* the key, and [removed it](#history) when a review showed it could be guessed in a fraction of a second. The name has to resolve only inside the recipient's own key manager.
- **Who we would like to hear from.** Password managers, enterprise identity providers, the credential managers built into operating systems and browsers, and hardware key makers. The best outcome is that you already have this and tell us.
- **What we bring.** An open reference integration, published crypto test vectors, a key format designed for secret scanners, thirty-three published vaults to test against, and a willingness to write the specification in public so it is not tied to either of us.

## The opportunity

Password managers solved one problem so well that people stopped noticing it: the long random string that has to be stored somewhere safe, typed nowhere, shared carefully and taken back when someone leaves. Passkeys moved the same machinery from logging in to proving who you are. Client-side encryption brings a third kind of secret into daily use, the key that opens a piece of data rather than an account, and at the moment nothing in the browser treats it as a first-class item.

Today, vault keys travel by hand. The gap at the bottom is the thing this page is asking for.

Three things make this worth doing now rather than later.

| **The number of keys is growing fast** | One person running a few projects now holds a vault per project, per client and per shared folder, and a separate read key for each person they share with, so access can be told apart. [Thirty-three vaults are published on this site alone](../demos/vaults/index.md), each with its own key. |
|---|---|
| **Agents are starting to make vaults** | An AI agent that builds a website for a customer, writes up a penetration test or keeps a board pack can hand the result over as a vault. [Agent as Webmaster](../demos/vaults/agent-webmaster/index.md) is a business plan built on exactly that. Every one of those hand-overs is a key that has to go to a person, safely, and every agent doing the work needs a key it should not be able to paste anywhere. |
| **The pattern is not specific to sgit** | Any end-to-end encrypted document, folder or dataset opened in a browser has the same need: a key for the data, held by the user, released to a page only when they agree. Whoever makes that easy for sgit makes it easy for the category. |

## What we are looking for

In order of preference.

| What | What it would look like |
|---|---|
| **1 · Something that already exists** | An item type, an extension API, a browser capability or an SDK in your product that lets a web page ask for a stored secret by name, with the user's approval, without the page ever seeing the rest of the store. If you have this, we would like to integrate with it and write up how, publicly, as the worked example. |
| **2 · A pilot built together** | If the pieces exist but not the whole, a small joint pilot: your manager stores sgit keys as their own item type, shares them between your users the way it already shares passwords, and releases them to an sgit page on approval. We would do the sgit side, you would do yours, and both would be open to inspect. |
| **3 · A specification written in public** | If this is better solved as a standard than as a product feature, a short open specification for storing, naming and releasing data keys in the browser, with sgit as the first implementation and a reference test suite, so that any key manager can support any client-side encrypted app. |

We are not asking for an investment, an exclusive arrangement or anyone's customer data. We are asking for the conversation, and for the answer to the question *"is there something I can use?"*

## The requirements

Written in plain terms first. [The technical detail is further down.](#detail)

| Requirement | Why it matters |
|---|---|
| **Must · Works in the browser** | sgit vaults open in a browser tab with nothing installed. The key manager should meet that: a browser extension is fine as a first step, a capability built into the browser or the operating system is the goal. |
| **Must · Knows what kind of key it holds** | An sgit key declares itself: a vault key reads and writes, a read key only reads, and a public read key is published on purpose. The manager should keep them apart, and must never hand a read-and-write key to a page that only asked to read. |
| **Must · Releases a key only when the user agrees** | With a passkey, biometric or device prompt; only to the site that asked; only into that page's memory; and never to the storage host, which in sgit's design never sees a key at all. |
| **Must · Shares end to end** | Sharing a vault with someone means your manager passing the key to theirs, encrypted so that nobody in between, including the manager's own servers, can read it. Most password managers already share passwords this way. |
| **Must · Names are addresses, not keys** | The recipient gets a short name in plain words, easy to read out or paste, that their own manager resolves to the key it was given. Guessing or overhearing the name must give nothing, because the name is not derived from the key and the key is not derived from the name. |
| **Must · Access can be taken back** | Stopping a share, or letting it expire, is the manager's job. Making the old key useless for good is sgit's job, by rotating it. The two should be designed to work together. |
| **Should · An index of what I hold** | The list of vaults a person can open, with a name, whether they can read or write, who shared it and when. Today nobody has this list, including us. |
| **Should · Keys for agents, scoped and time-limited** | An AI agent should get a read key for one vault for one task, approved by a person, recorded, and expiring on its own. [RiskMandate.ai](https://riskmandate.ai/) is built around exactly this question: what an agent can reach against what it was authorised to do. |
| **Should · Recovery** | sgit has no recovery by design. A key manager with account recovery gives the owner one, without giving sgit or the host a way in. |
| **Should · No lock-in** | Keys should move between managers in an open format, and any key manager should be able to support any client-side encrypted app, not only ours. |
| **Nice · A record of use** | When a key was released, to which page, on which device. It is the audit trail that client-side encryption otherwise cannot give an organisation. |

## sgit in two minutes

You do not need to know git or cryptography for the rest of this page, only four ideas.

What a vault is, and where the key sits. The three kinds of key at the bottom are what a key manager would hold.

| **A vault is a folder with history** | Files, every earlier version of them, branches and merges, the way a developer's git repository works, and it can carry its own small application so it opens as a page rather than a file list. |
|---|---|
| **It is locked before it leaves your device** | Every file, name and commit message is encrypted on your machine or in your browser. What gets stored is ciphertext under meaningless identifiers. [The security model](../security/index.md) states exactly what the host can and cannot see. |
| **Any host will do** | Our server, your own, a cloud bucket or a plain static site behind a CDN. [It deploys to Docker, AWS, GCP or a static host](../deploy/index.md), and moving a vault between them is a copy, because none of them can read it. |
| **One string opens it** | The key. Whoever holds it can open the vault in a browser with no account and nothing installed. That is what makes vaults easy to hand over, and it is exactly why the key needs looking after. |

The fastest way to understand it is to open one. [The DSIT AI Risk Toolkit vault](../demos/vaults/dsit-ai-risk-toolkit/index.md) opens in the browser from its page, with its public read key printed underneath, and so does every vault in [the list](../demos/vaults/index.md).

## How it could work

A sketch, not a design. We would expect a key manager's team to improve every step of it.

Sharing a vault by name. The key moves only between the two key managers; the words move by any channel at all.

| Workflow | What the person does | What happens underneath |
|---|---|---|
| **Open a vault I hold** | Clicks a vault in their key manager, or opens a vault page and approves a prompt. | The page asks the browser for the key for this vault; the manager checks the site and the key kind, asks the person, and releases the key into the page's memory. The page fetches ciphertext and decrypts it locally. |
| **Share with a person** | Chooses "share, read only" and the recipient, then sends them the three-word name however they like. | The manager derives or selects a read key, never the vault key, and passes it to the recipient's manager end to end. The name is a random label attached to that shared item, meaningful only inside the recipient's store. |
| **Take it back** | Stops the share, or lets it expire. | The manager removes the item from the recipient's store. For a clean break, the owner rotates the vault in sgit, and the manager updates the remaining holders with the new key. |
| **Give an agent access** | Approves a request from an agent to read one vault for one task. | A read key scoped to that vault, released for a stated time, with the release recorded. The agent never sees the vault key and cannot pass on what it was not given. |
| **Create a new vault** | Creates it in sgit, from the command line or the browser. | The new vault key goes straight into the manager, before anything is published. Our own [publishing method](../demos/vaults/publishing.md) records for every published vault whether its write key is escrowed or lost, because a vault whose write key is lost is frozen: it can never be corrected. |

### Building blocks that may already be there

We are not experts in your stack, and we would like to be told what we have missed. These are the public pieces that look relevant from where we stand.

- **The WebAuthn PRF extension.** Part of the WebAuthn specification, it lets a passkey produce a secret that a web page can turn into an encryption key, after a user-verification prompt. Some password managers already use it to unlock their own encrypted stores. It could wrap vault keys so they are only usable after a passkey prompt.
- **The Credential Management API.** The browser's existing way for a page to ask for a stored credential. A new credential type for data keys, or an extension of an existing one, is the shape a built-in answer might take.
- **Password manager sharing.** The end-to-end sharing most managers already have for passwords and notes, between people and within an organisation, is the channel for step two in the diagram above.
- **The FIDO Alliance credential exchange work.** Specifications for moving credentials between managers securely, which is the no-lock-in requirement from the other side.

## Who we would like to hear from

Organisations are named below only as examples of the kind of team we mean. There has been no conversation with any of them, and nothing here is a claim about what their products do or do not support.

| Kind of organisation | For example | What they would bring |
|---|---|---|
| **Password managers** | 1Password, Bitwarden, Proton Pass, Dashlane, Keeper, KeePassXC | The store, the sharing, the browser extension and the people who already trust them with their secrets. |
| **Enterprise identity providers** | Okta, Microsoft Entra ID, Ping Identity | Policy: who in an organisation may hold which vault key, joiners and leavers, and the audit trail a regulated business needs. |
| **Platform credential managers** | The password and passkey managers built into Apple, Google and Microsoft platforms and browsers | The native answer: a capability every web page can use, with no extension to install. |
| **Hardware key makers** | Yubico and other FIDO authenticator makers | Keys that never leave a device, for the vault keys that matter most. |

## What is in it for a partner

- **A new kind of item.** Data keys, alongside passwords and passkeys, for any client-side encrypted app, with sgit as the first one and the published vaults as the test bed.
- **The agent era, on your platform.** Scoped, expiring, approved keys for AI agents are a problem every organisation is about to have, and a key manager is the natural place to answer it.
- **Work done in the open.** Everything on our side is Apache-2.0 and public, so the integration can be inspected, copied and cited, and nobody is locked in, including you.
- **A partner that stays out of your lane.** We make the vaults. We have no plans to build a key manager, and this page exists precisely so that we do not have to.

## What we bring

| **An open reference integration** | The sgit side of the pilot, in the Apache-2.0 client and the browser viewer, written so another key manager could plug into the same interface. |
|---|---|
| **Crypto that is specified and tested** | AES-256-GCM, HKDF-SHA256 and PBKDF2, with test vectors that the command-line client and the browser must match byte for byte. Keys are derived locally; the host never holds one. |
| **Keys that say what they are** | Every sgit key carries a prefix naming its kind: `sgit_private_vault_`, `sgit_private_read_` or `sgit_public_read_`. One secret-scanner rule, `sgit_private_`, catches every private key type, and a published read key cannot be mistaken for a leak. |
| **Real vaults to test against** | [Thirty-three published vaults](../demos/vaults/index.md) across security, regulation, business plans and applications, each with a public read key, plus [the catalogue](../demos/vaults/catalogue/index.md), a vault that lists vaults, which is the closest thing today to the index a key manager would keep. |
| **The failures, written down** | [What to do if a vault key is exposed](../case-studies/exposed-vault-key.md), [the publishing method](../demos/vaults/publishing.md) with the mistake behind each rule, and [when not to use sgit](../docs/limitations.md). A key manager partner should know the edges before the first call. |

## The detail

### The keys, exactly

A vault key is a passphrase and a vault identifier joined by a colon, and displayed with its prefix: `sgit_private_vault_<passphrase>:<vault id>`. From it, the client derives a read key and a write key locally, using PBKDF2 with 600,000 iterations and a per-vault salt. The read key alone can open and verify the vault but not change it, and it is what gets shared. A read key that is deliberately published carries `sgit_public_read_` instead of `sgit_private_read_`: the same bytes, a different declaration, so a scanner alert on `sgit_private_` stays meaningful. The vault identifier is a short opaque string by design, because a human-readable identifier would leak meaning into server and CDN logs, which is one more reason the friendly name has to live in the key manager and not in the vault.

### Why the words cannot be the key

sgit used to have exactly the friendly name this page asks for. An earlier share token was two words and four digits, and the vault's encryption keys were derived from it directly. It was easy to read out and easy to type. A security review on 6 August 2026 found that it carried about thirty bits of entropy and could be recovered from public data in around a tenth of a second on a GPU, and the feature was removed from the client entirely on 12 August 2026 rather than patched. The lesson is the requirement: **a name people can say out loud cannot also be the secret**. It can only be a pointer to one, resolved by something that already holds the secret and already knows who is asking. That is a key manager.

### Why a vault of keys is not enough

We can, and will, keep keys inside vaults: a vault that holds the read keys for a set of other vaults is a natural index, and [the catalogue](../demos/vaults/catalogue/index.md) is a public version of it. But the key to that vault still has to be kept somewhere, and so on down. At the bottom of every chain there is one secret that a person has to hold, recover, and use on a new device, and that is the problem password managers and identity providers were built for.

### What exists today, and what does not

| Exists and runs | Does not exist yet |
|---|---|
| Vault keys, read keys and public read keys with self-declaring prefixes. Local derivation. Browser opening from a read key with nothing installed. Thirty-three published vaults. Guidance to keep the vault key in a password manager, which is what this page wants to make first-class. | Any integration with any key manager. Revocation, expiry or a rotation workflow in the product: rotation is a manual re-encryption today, as [the limitations page](../docs/limitations.md) says. The word-name scheme. Agent-scoped keys. All of these are what a collaboration would build. |

## What this page does not claim

- **We have not spoken to anyone named here.** The examples are categories made concrete, and the page makes no statement about any product's features or roadmap.
- **Your product may already do this.** If so, that is the best outcome, and we would like to be told and to write it up as the worked example.
- **The flow is a sketch.** It shows the shape of the requirement, not a protocol. The step where a name is resolved, in particular, is where a key manager's team would know far more than we do.
- **sgit holds no certification.** It is open-source software with a stated security model and stated limits, not an audited product, and [the page for regulated sectors](../use-cases/health-regulated.md) says so first.

## If you work on this, or know someone who does

This page is written to be forwarded as it is. It explains what sgit is for someone who has never heard of it, what we are asking for, the requirements, how it could work, and what we would bring, and every claim on it links to something that can be opened. It is published by the founder of sgit.ai and [RiskMandate.ai](https://riskmandate.ai/), through [The Cyber Boardroom Limited](https://thecyberboardroom.com) in the UK. [Who is asking, and how to reach them →](../about/index.md)

[← UK Sovereign AI](sovereign-ai.md)[All partnerships →](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/partnerships/vault-key-management.html)*
