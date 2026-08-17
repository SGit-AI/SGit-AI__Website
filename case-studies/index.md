# Case studies — sgit.ai

> Worked accounts of things that actually happened, including the ones that went wrong: a leaked vault key and its rekey, and the architecture of a live site whose host cannot read it.

*Source: <https://sgit.ai/case-studies/index.html> · site v0.2.27 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / Case studies

# Case studies

Things that actually happened, written up while the details were still checkable — including the ones that went wrong. Each is a worked account with the mechanism, the numbers, and what changed as a result.

**What counts as a case study here:** a specific event or system, with evidence a reader can verify — commands they can run, numbers we measured, or a live page they can open. Not a pattern, not a design we like the look of. Patterns live in [use cases](../use-cases/index.md), which label their evidence honestly; if a use case ever earns a real deployment, its write-up lands here and the two link to each other.

## Published

[Incident### The day we leaked our own vault keyAn agent hardcoded this site's vault passphrase into a tracked file as part of an anti-leak check. It reached three public commits and was caught only because someone asked. The runbook, the rekey, the measured blast radius — 336 objects out, 90 in, zero overlap — and the structural fix.Read the incident →](exposed-vault-key.md)

[Workflow### One working tree, two version control systemsThis site's own development model: one folder that is both an sgit vault and a git repository, two pushes per release, the one-file boundary that makes it safe, and the ordering rule that keeps the git mirror true to the vault.Read the workflow →](one-tree-two-remotes.md)

[Architecture### A live site whose host cannot read itTwo Claude Code sessions, two encrypted vaults, one page: how the Deploy section is fetched as ciphertext from an SG/Send server and decrypted in your browser, with the object model, the cache tiers and the request timeline drawn out.Read the architecture →](live-vault-docs.md)

## How these are written

Same shape every time, so they stay comparable and so an agent can parse them:

- **What happened** — the sequence, in order, with timestamps or commit ids where they exist.
- **The mechanism** — why it happened, at the level of the object model or the code, not at the level of "human error".
- **The numbers** — measured, not estimated, and stated even when they are unflattering.
- **What changed** — the structural fix, and the check that stops it recurring. A write-up with no change attached is a story, not a case study.
- **What we still do not know** — stated rather than smoothed over.

The incident write-up is the template for the uncomfortable kind. It names the agent that made the mistake, the detection gap that let it survive three commits, and the cost of the fix — because a project that hides that class of mistake is the one to worry about.

## Related

- [Use cases](../use-cases/index.md) — the patterns, each with an explicit evidence status
- [Cross-team briefs](../briefs/index.md) — what this site's agent hands to other teams, and what they hand back
- [Release history](../admin/versions.md) — every change to this site, with the vault commit that carried it

[← Home](../index.md)[Use cases →](../use-cases/index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/case-studies/index.html)*
