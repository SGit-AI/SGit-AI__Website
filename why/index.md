# Why does this exist? — sgit.ai

> A direct answer to the sharpest criticism we received: no market, no value. The use cases, why existing tools do not cover them, where the criticism is right, and a FAQ of the follow-up questions.

*Source: <https://sgit.ai/why/index.html> · site v0.2.7 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

# Why does this exist?

Someone left this under the announcement post. It is the most useful comment we received, so it gets its own page.

> "I appreciate the work and effort in this but i see no market or value what so ever (especially market). My first question if was being sold this would be why but then don't try and answer cause i would return with so many follow up questions to anything you would say."

Fair question — and the "don't bother answering" is fair too, because most answers to it *are* marketing. So: no pitch, no adjectives, and the follow-up questions answered in advance rather than deflected. Where the criticism lands, we say so.

There is also nothing being sold. sgit is Apache-2.0 and installable with `pip install sgit-ai`. So "why would I buy this" has no answer, because there is no purchase. The question worth answering is **why would anyone use it**.

**The whole thesis in one sentence:** you have files that need version control and collaboration, and the place they are stored must not be able to read them.
Everything below is a consequence of that sentence. If it doesn't describe a problem you have, use git and a private repo — we say so on [the page about when not to use this](../docs/limitations.md).

## What this makes possible that wasn't

This page assumes you know git. So rather than re-explain version control, here is only the delta: things you cannot do with git and a host, or cannot do without that host reading everything. Each one is running on this website right now — the links go to the thing itself, not to a description of it.

### A live website whose host cannot read it

The [Deploy section](../deploy/index.md) of this site is not part of this site. Its pages live in an encrypted vault maintained by a different team; your browser fetches the ciphertext straight from an SG/Send server over CORS and decrypts it in the tab. There is no build step, no CI job, no copy of that content on sgit.ai. When that team runs `sgit push`, the next page load has it.

**Without sgit:** you can serve a static site from a host, or you can keep the content private, but not both. GitHub Pages serves what GitHub can read. A private bucket plus a decrypting front end is buildable — content addressing, cache tiers, key derivation, an update path — and that is roughly the thing being described here. There is no documented, off-the-shelf way to do it with git and a git host.

See it working: [how this page works](../case-studies/live-vault-docs.md), with the object model and the request timeline.

### Read access as a thing you can publish

A vault has a **read key** that is derived one way, so it decrypts content and cannot be turned back into write access. That makes it safe to put in a file the whole internet can fetch — which is exactly what `deploy/vault.json` on this site does. Anyone can take it and run `sgit clone --read-key <key> fyofmkvr` to get the same documents on their own machine, and watch a write attempt get refused.

**Without sgit:** git access is repository-shaped and host-mediated. A deploy key that can read gives its holder everything in plaintext, and revoking it is an operation on the host's access-control list. Here, the capability *is* the key: it travels with the reader, it works against any server holding the ciphertext, and the host is not asked to enforce anything.

### Two agents collaborating in a workspace neither host can read

This site is built and published by Claude Code sessions that share state through a vault. Each session clones into its own private branch, commits there, and pushes to the shared named branch — the [two-branch model](../docs/two-branch-model.md), which is git's isolate-then-merge shape applied to encrypted objects. The pages in the Deploy section come from a *second* team's vault, maintained by an agent that has never had access to this repository or this site.

**Without sgit:** agent-to-agent shared memory means a database or a repo that the provider reads. That is fine until the state includes client documents, security findings, or unreleased work — at which point the question stops being technical.

The architecture, drawn: [two sessions, one vault, one live site](../case-studies/live-vault-docs.md).

### Private data with public-CDN economics

Object ids are SHA-256 hashes *of the ciphertext*, so an object can never change under its id. That makes every object permanently cacheable by infrastructure that cannot read it — a browser's Cache API, a proxy, a CDN edge. On this site that is not theory: after the first visit, a page load fetches **one 69-byte object** (the mutable HEAD pointer) and serves everything else from cache — and inside the [freshness window](../case-studies/live-vault-docs.md) it fetches nothing at all. Open the vault panel on any Deploy page and watch the counters.

**Without sgit:** caching private content at the edge is precisely what you are told not to do, because the cache would hold readable data. Content-addressed ciphertext removes the conflict — the cache holds bytes it cannot interpret, keyed by a hash it cannot invert.

### Storage becomes a commodity you don't have to trust

The server is a key-value store for opaque ids. It never receives a key, never sees a filename, and cannot tell a legal draft from a photo. That means the backing store is interchangeable — a managed SG/Send server, one you [run yourself](../deploy/index.md), an S3 bucket, a disk — and choosing it stops being a trust decision. A subpoena, a breach, or a curious administrator on that host yields ciphertext.

**Without sgit:** "who hosts this?" and "who can read this?" are the same question. Every migration is a re-negotiation of that trust; here it is a copy operation.

### Transit security that doesn't rest on the CA system

The content is already encrypted before it leaves the client, so TLS is transport hygiene rather than the security boundary. A mis-issued certificate, a coerced or compromised CA out of the ~150 your browser trusts by default, or a TLS-terminating middlebox in a corporate network sees the same thing the server sees: ciphertext addressed by opaque ids.

**The advanced version** — and where this is heading: the read key stays on the client and never appears in a published file, or the scheme moves to PKI with the private key existing only on the client. Then the confidentiality of the data in transit depends on one key you hold, not on the whole certificate-authority arrangement being sound end to end. Today's published-read-key form on this site is the deliberately simple case: the content *is* meant to be public, so the only job is proving the host never had it in the clear.

## Who has that problem

Not a market-size claim — just the situations where the sentence at the top is literally true today. These matter, but they are the ordinary reasons; the section above is the interesting one.

[AI agents### Agent state that isn't the vendor's to readAn agent's work has to survive its context window, so it goes somewhere — and that somewhere increasingly holds client documents, security findings, unreleased code.Recipe, evidence and an agent brief →](../use-cases/ai-agents.md)

[Professional services### Working documents with clientsLegal, M&A, audit, security assessment: the deliverable and the working notes are exactly the material that must not sit readable on a third party's disk.Recipe, evidence and an agent brief →](../use-cases/professional-services.md)

[Health & regulated### Data that changes what is permissibleWhen the host provably cannot read the content, you are no longer arguing about the provider's access controls, because there is nothing to control access to.Recipe, evidence and an agent brief →](../use-cases/health-regulated.md)

[Security teams### Findings about your own weaknessesPentest results are the last thing you want in a SaaS you don't control, and the first thing that needs history, diffs and multi-person workflow.Recipe, evidence and an agent brief →](../use-cases/security-teams.md)

## git and sgit, side by side

The honest framing is not "sgit instead of git". It is two tools with different jobs, and the interesting question is which one owns which files. **This site runs both at once** — one working tree, two remotes: the encrypted vault is pushed with `sgit push`, and the same directory is pushed to GitHub with `git push`, which is what builds and deploys it. Neither is a fallback for the other.

|  | git | sgit |
|---|---|---|
| **The host can read your content** | Yes — that is what makes everything else work | No. It stores ciphertext under opaque ids and never receives a key |
| **Performance at scale** | **Far better.** Twenty years of optimisation: packfiles, deltas, a mature index, repos with millions of files | Built for working sets of documents and code-sized files. Every object is encrypted and content-addressed individually; large binaries chunk-upload past ~4 MB but this is not a video archive |
| **Ecosystem** | **Everything.** CI, code review, IDEs, hosting, decades of tooling and answers | A CLI, a browser client, and an agent skill. Deliberately small, and young |
| **Archaeology** | **Better.**`bisect`, `blame`, `rebase`, `cherry-pick`, hooks, submodules | `history log / diff / show / revert / reset`. No bisect, no blame, no rebase — the server cannot help, so anything not implemented client-side does not exist |
| **Partial commits** | Staging area, index, `add -p` | None. A commit snapshots the whole folder |
| **Branching and merge** | The reference implementation of the idea | The same shape, applied to encrypted objects: a private branch per clone, shared named branches, whole-file three-way merge |
| **Read-only access for someone else** | An account on the host, or a deploy key that reads plaintext | A read key — derived one way, publishable, works against any server holding the ciphertext, no account and no host involvement |
| **Reading it from a browser** | Via the host's UI or API, in plaintext | Directly: fetch the ciphertext and decrypt in the tab with Web Crypto. This page's [Deploy section](../deploy/index.md) is that |
| **If the host is breached** | Your content is in the breach | Opaque ids, ciphertext, object sizes and timing |
| **Recovery when you lose the credential** | Reset your password; the repo is unaffected | Nothing. No reset, no recovery — the direct cost of the row above |

**So the split, concretely:** source code, issues, CI config and anything you would be happy to open-source belong in git — it is better at them and always will be. The material where "who can read the store" is the binding constraint belongs in a vault. Plenty of projects have both, and there is no reason to choose: the two live in one directory, ignore each other, and are pushed separately. The [side-by-side setup](../vault/git-and-vaults.md) — what to commit, what to keep out of git, and the `.gitattributes` that stops git trying to diff ciphertext — is documented, because it is how this site is developed.

## Why the existing answers don't cover it

This is the strongest form of the objection: every one of these exists and is more mature. Each solves part of it.

| What you'd reach for | What it gives you | What's missing |
|---|---|---|
| git + a private repo | Everything about workflow, perfected | The host reads all of it. Fine for code; not for client data — and none of the six capabilities above. |
| git-crypt / SOPS / age | Encrypted file *contents* inside git | Filenames, directory structure, commit messages and history shape stay readable to the host; no browser access; key distribution is manual. |
| Dropbox / Drive / SharePoint | Sync, sharing, a UI everyone knows | The provider can read it, and there are no branches, no merges, no commit history you can reason about. |
| S3 + KMS, or a database with encryption at rest | Encryption the auditors recognise | Whoever holds the key can decrypt — and that's the provider, or anyone with the right IAM role. No git-shaped workflow, no offline. |
| Build it yourself | Exactly what you want | Roughly what this project is: four thousand tests, a wire format two independent clients agree on, and a year of edge cases. It's free — you may as well take it. |

The gap they share is the same one: **you can have the workflow, or you can have the privacy, but not both in the same tool.** If you think that gap doesn't matter, we disagree about something factual — a much better disagreement to have than one about adjectives.

## The market question, answered directly

- **The client is open source, and that is the distribution strategy, not a substitute for one.** Apache-2.0, no licence tiers, no open-core feature gating in the CLI. It spreads by being free and useful, and the services are built on top of it — the ordinary way open source scales into a business.
- **The commercial layer is the hosted service** (SG/Send) and what gets built around it. You can also [self-host](../deploy/index.md) — that guidance is published, live, in a vault — so the lock-in argument doesn't hold: if the commercial layer becomes unpalatable, you run your own server and your data and workflow are unaffected.
- **We are not going to quote a market size.** We don't have credible numbers, and a TAM slide is exactly the marketing this page is avoiding. What we can say honestly: the amount of machine-generated state that someone else should not be able to read went from approximately zero to very large in about two years, and it has to live somewhere.
- **It might still be a small market.** That's a legitimate outcome. The tool would still be worth having for the people in it, and it costs them nothing.

## Where the criticism is right

- **The category is unproven.** "Git for encrypted vaults" is not a shelf anyone shops from yet. We might be early, wrong, or both.
- **Most people don't need it.** If your files aren't sensitive, this is strictly more complexity than a private repo.
- **Zero-knowledge has real costs** — no server-side search, no password recovery, and key management becomes your problem. Permanent trade-offs, not bugs to be fixed later.
- **It's beta.** In production use daily, but young.

## The follow-up questions

You said you'd have many. Here are the ones we'd expect, answered without hedging. If yours isn't here, [ask it in public](https://github.com/SGit-AI/SGit-AI__CLI/issues) and we'll add it.

**Give me one thing I cannot do with git and GitHub today.**

Publish a site whose content the host has never seen in the clear, updated by a push, readable by anyone you hand a read key to, and cached at the edge by infrastructure that cannot decrypt it. The [Deploy section](../deploy/index.md) is that, live. You can assemble something similar yourself out of a bucket, a decryption front end and a cache policy — and what you would have assembled is this.

**Isn't publishing a key on a website obviously a mistake?**

Publishing a *write* key would be — we have an [incident write-up](../case-studies/exposed-vault-key.md) about doing exactly that by accident. The read key is a different object: derived one way, it decrypts and cannot be inverted into write access. Publishing it is how a reader gets the content without the site ever being trusted with the ability to change it. That's a checkable property, not a policy: take the key, clone with it, and watch the write get refused.

**Doesn't TLS already solve the confidentiality problem?**

TLS protects the hop, not the destination. It ends at the server, which then holds your plaintext — and it rests on a certificate-authority system where any of roughly 150 default-trusted roots can vouch for any name, and where corporate middleboxes terminate it on purpose. Encrypting before the bytes leave means a mis-issued certificate or a terminating proxy sees ciphertext. The direction of travel is stronger still: the read key never leaving the client, or PKI where the private key exists only there.

**Isn't this just git with encryption bolted on?**

No — and the difference is why the existing tools don't cover the case. Encrypting files inside git still leaves the host holding your filenames, directory structure, commit messages and the shape of your history. sgit encrypts all of that: the server sees opaque identifiers and ciphertext, and never receives a key. A different storage model that keeps git's verbs.

**Why not git-crypt or SOPS? They're mature and I already know them.**

Use them if they fit — they're good tools designed for a different job: keeping a handful of secrets inside an otherwise-public repo. They don't hide structure, don't work in a browser, and key distribution across a team is manual. sgit targets the case where the *whole workspace* is the sensitive thing.

**If it's free, what's the business model — and what happens when you need to make money?**

The hosted service, and what gets built on it. The client stays Apache-2.0 and self-hosting is documented, which is the protection that matters: the escape hatch is a checkable property of the format, not a promise about future behaviour.

**What if you disappear?**

You keep a full local copy — every clone contains the complete encrypted store. The format is documented, the client is open source, and two independent implementations already read it. If the project stopped tomorrow, your data stays readable with code you already have.

**"Zero-knowledge" is a marketing term. What does the server actually see?**

The vault ID, the size of each encrypted object, and when requests happen. That's the list, and it's on [the security page](../security/index.md) including the uncomfortable parts: object sizes and timing are a real, if narrow, side channel. Anyone who tells you their zero-knowledge system leaks nothing at all is not being careful with words.

**How do I know the cryptography is right?**

You don't have to take our word for it, which is the point. It's standard and boring — AES-256-GCM, PBKDF2-SHA256 at 600k iterations, HKDF — with no custom primitives. The code is open, and the outputs must match the browser's Web Crypto API byte-for-byte, enforced with test vectors. Two independent implementations reading the same format is a stronger check than any single audit.

**What happens when I lose the key? Be honest.**

The data is gone. No reset, no recovery, no support ticket that helps. That's the direct consequence of the server not being able to read your content, and if your organisation can't manage keys reliably, this trade-off will hurt you and you should not use it.

**Why would an AI agent need this specifically?**

Because agent state is now sensitive and shared. An agent that stops and resumes needs durable memory; several agents working together need shared memory with isolation and a review step; and the contents are increasingly things a client or regulator cares about. Version control solves the coordination half. Client-side encryption solves the half that determines whether you're allowed to do it at all.

**Isn't this over-engineered for what it does?**

Judge it by the surface: two runtime dependencies, a pure-Python client, one file format. The complexity that exists — the two-branch model, content addressing, three-way merge — is what makes concurrent editing safe without the server being able to help, because the server can't read anything. Remove the encryption and yes, it's over-engineered; you'd just use git.

**Is anyone actually using it, or is this a demo?**

This website is served from a vault it manages, deployed by pushing that vault. The [deployment docs](../deploy/index.md) are decrypted in your browser, live, from a different vault maintained by another team. The [Try page](../try/index.md) runs the real client in your browser. It's in daily production use by its authors — a small n, honestly stated, and more than a demo.

**Why should I trust a beta?**

For anything critical, don't yet — and keep backups regardless. What we offer instead of a trust-me is evidence: ~4,000 tests, mutation testing, integration tests against a real server, a published threat model, and an [incident write-up](../case-studies/exposed-vault-key.md) of the day we leaked our own key, including what it cost to fix. A project that hides that class of mistake is the one to worry about.

**Fine — but I still think there's no market.**

You may be right. It costs nothing to be wrong about this in our direction: the code is free, the format is open, and if the category never materialises, the people who did need it still got a working tool. The failure mode we'd actually regret is the opposite one — building it after everyone had already put their machines' private state somewhere readable.

## An invitation, meant literally

You said you'd come back with many follow-up questions. Please do — [in the open, on the issue tracker](https://github.com/SGit-AI/SGit-AI__CLI/issues). Sharp questions from someone who doesn't buy the premise are worth more than agreement, and if any of them don't have a good answer, that's a finding: it goes on this page, or it changes the roadmap. That's the same way the [key-leak incident](../case-studies/exposed-vault-key.md) and the [open briefs](../briefs/index.md) got written.

[← Home](../index.md)[When NOT to use sgit →](../docs/limitations.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/why/index.html)*
