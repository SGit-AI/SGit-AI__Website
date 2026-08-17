# The serialised pull request — sgit use cases

> An agent contributes to a shared vault holding no credential at all: clone with a public read key, commit on a private branch, emit a diff; a person imports, reviews and merges. The ambient-authority problem it removes, the 5 Aug 2026 Black Hat grounding, and the honest shipped-vs-pattern table.

*Source: <https://sgit.ai/use-cases/serialised-pull-request.html> · site v0.2.33 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Use cases](index.md) / The serialised pull request

# The serialised pull request

An agent clones a public vault needing no credential at all, makes changes, commits, and emits a diff. A person imports that diff on another machine, reviews it, and merges. No token was issued, so no token could be stolen, scoped too widely, or left unrevoked.

## The problem: ambient authority

The standard way to let an agent contribute to a repository is to give it a credential — and the credential is nearly always bigger than the task. One widely used coding agent held a token scoped to *every repository its developer had authorised*. The platform capability that would fix this — a user-minted, short-lived, single-repository token — has been an open feature request since June 2026, which is the polite way of saying it does not exist.

The consequences stopped being theoretical this month. Research disclosed at Black Hat on **5 August 2026** showed that a GitHub issue opened by an account with *no repository privileges* was enough to reach CI secrets in the vendors' own repositories — for three leading agents, under each vendor's default, unmodified workflow configuration. The attacker did not break anything; they asked a confused deputy to use authority it already held. That is what ambient authority means, and every write-scoped agent token is a standing instance of it.

## The workflow

In the project lead's own words, from the session where it happened:

> "I got Claude to clone a vault, a public repo, and I didn't need any permissions. Then Claude made a bunch of changes, then I got Claude to create commits and give me a diff. On another machine I cloned that vault, imported the diff, saw the changes, and then I merged them. Fundamentally, it's like a serialised pull request."

```
# the agent's side — no credential at any point
$ sgit clone --read-key <published-read-key> <vault-id> work
# … changes, commits on the private clone branch …
$ sgit history diff --json > proposed-changes.json   # the serialised artefact

# the human's side, on another machine
$ sgit clone '<vault-key>' review
# import the diff, review it, merge, push — see "honest mechanics" below
```

Four properties, and each is the strong form of something a platform PR only approximates:

- **No credential is issued at all.** Stronger than a short-lived scoped token: there is nothing to steal, nothing to expire, nothing to revoke, and nothing for an injected instruction to spend.
- **The artefact is inspectable before it takes effect.** A diff is reviewed; a write is discovered. The privileged action happens on the reviewer's machine, after human eyes.
- **Provenance survives per commit**, not per session — the history records what was proposed, not just what was merged.
- **It is capability-shaped, not trust-shaped.** It assumes no shared platform accounts and no fork write access, and the artefact moves by any channel — a vault, an email, a queue.

Published security guidance now independently recommends exactly this shape: run analysis in a read-only job holding no publishing credentials, and pass a constrained, reviewed artefact into a separate privileged step — never one job that both consumes untrusted input and can publish. Having built the recommended control *before* the recommendation is a stronger claim than any feature comparison, so we make it plainly.

## The honest mechanics

What is shipped versus what is pattern, checked against the CLI rather than asserted:

| Step | Status today |
|---|---|
| Credential-free clone of a public vault (read key only) | **Shipped** — `sgit clone --read-key`; this site publishes working read keys on its [demo pages](../demos/index.md) |
| Private-branch commits that cannot touch the shared branch | **Shipped** — the [two-branch model](../docs/two-branch-model.md) |
| Emit the diff as a machine-readable artefact | **Shipped** — `sgit history diff --json` |
| First-class import: `sgit diff apply` | **Not shipped.** The workflow was performed, but the import half was review-and-merge by hand. A [brief to the CLI team](../briefs/brief-serialised-diff-and-ignore.md) asks for `sgit diff export` / `sgit diff apply` as first-class commands |
| A published specification of the diff format | **Not published.** If this is the headline workflow, its artefact needs a spec a third party can implement — same brief |

## Evidence status

PARTIAL — performed once, import not yet first-class

The workflow ran end to end exactly as quoted, and every step on the agent's side is a shipped command exercised daily. What keeps this from PROVEN is the import: until `sgit diff apply` exists, the human side leans on manual review-and-merge, and a workflow with a manual middle is a pattern, not a product. The brief is filed; this page upgrades itself when the commands land.

## Brief for an agent

```
$ curl -s https://sgit.ai/use-cases/serialised-pull-request.md
```

> Read https://sgit.ai/use-cases/serialised-pull-request.md. Clone the vault I name using only its read key, make the changes I describe on your clone branch, commit with clear messages, then emit `sgit history diff --json` and give me the output as a file. Do not ask for, hold, or use any write credential at any point.

## Related

- [The two-branch model](../docs/two-branch-model.md) — why the agent's commits cannot reach the shared branch
- [Agent state that isn't the vendor's to read](ai-agents.md) — the memory half of the agent story
- [The boundary map](../why/index.md) — where this sits: proposing changes without write access is present; the hosted review interface is not

[← Use cases](index.md)[AI agents →](ai-agents.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/use-cases/serialised-pull-request.html)*
