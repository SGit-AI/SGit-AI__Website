# Working documents with clients — sgit use cases

> Engagement vaults for legal, M&A, audit and assessment work: versioned working notes, review as branches, and read-only handover with a published read key.

*Source: <https://sgit.ai/use-cases/professional-services.html> · site v0.2.40 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Use cases](index.md) / Professional services

# Working documents with clients

Legal, M&A, audit, security assessment. The material that most needs versions and review is the material that least belongs readable on a third party's disk.

## The problem

A engagement produces two bodies of text: the deliverable, and everything behind it — working notes, drafts, the evidence, the arguments that did not survive. Both need history: who changed what, when, and what the previous version said. Both need more than one person in them.

The usual tools split badly. A shared drive gives you collaboration and no history worth the name. A private repo gives you history and hands the whole engagement to a host. Email attachments give you neither and produce six versions named `final_v3_JS_edits`.

And then the engagement ends, and you need to hand the client something they can keep and verify — without giving them an account on your systems, and without them needing your tooling to read it later.

## What sgit does about it

The working set is a vault: full history, branches, diffs, three-way merge, all client-side. The store holds ciphertext under opaque ids, so "where is this hosted" and "who can read this" stop being the same question — including for the host's staff, a subpoena served on the host, or a breach of it.

For handover, a **read key** is derived one way: it decrypts and cannot be turned into write access. You can give a client read access to a specific vault without giving them anything else, and without the host mediating it.

## The recipe

**One vault per engagement.** Keep the boundary at the vault, not at a folder — it is the unit of access.

```
$ sgit create acme-acquisition
  Vault key: <passphrase>:<vault-id>   ← password manager, now. There is no reset.
$ mkdir deliverable working evidence && sgit commit -m "structure" && sgit push
```

**Review as branches**, so the draft in flight is never the draft on the record:

```
$ sgit branch new draft-2 && sgit push
$ sgit history diff --commit <prev>      # exactly what changed since the last version
$ sgit resolve --show                     # when two reviewers touch the same file
```

**Hand over read-only** at the end, or throughout:

```
$ sgit dev derive-keys '<vault-key>'    # the read key, derived one way
# the client, with nothing but that key:
$ sgit clone --read-key <read-key> <vault-id> engagement
# …and a write attempt is refused, which they can verify themselves
```

**Archive on close.** The archive is self-contained ciphertext — keep it wherever your retention policy says, including somewhere you don't trust:

```
$ sgit vault backup --include-key       # store the key separately from the archive
```

## Evidence status

PATTERN — not yet evidenced publicly

The mechanics above are all shipped commands and are exercised daily; what we do **not** have is a published professional-services deployment we can point you at. Treat this page as a design that fits the constraints, not as a case study.

Two things to weigh before you use it on a real engagement: sgit is in [beta](../docs/limitations.md), and there is no key recovery — if your firm's key management is not already real, this trade-off will find you. If you do run this pattern, we would like to write it up: [say so in the open](https://github.com/SGit-AI/SGit-AI__CLI/issues).

## Brief for an agent

Paste this into an agent that has the [sgit skill](../skills/index.md) installed, or point it at the markdown directly.

```
# everything on this site is readable as markdown — no HTML parsing needed
$ curl -s https://sgit.ai/use-cases/professional-services.md
$ curl -s https://sgit.ai/llms.txt          # the index of everything
```

> Read https://sgit.ai/use-cases/professional-services.md and https://sgit.ai/docs/agents.md. Then set up an engagement vault for this project: create the vault, structure the folders as described, commit and push, and report the vault key back to me once — I will store it. Do not write the key to any file in the repository.

That last sentence matters. We have a [write-up of the day we got it wrong](../case-studies/exposed-vault-key.md).

## Related

- [When NOT to use sgit](../docs/limitations.md) — read this before committing a client engagement to it
- [SG/Vault](../vault/index.md) — the browser app, so a client can read without installing anything
- [Security model](../security/index.md) — precisely what the server can and cannot see

[← AI agents](ai-agents.md)[Security teams →](security-teams.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/use-cases/professional-services.html)*
