# Lessons learned, the rules and the incidents behind them, sgit.ai

> Every rule this site enforces, with the event that produced it: classify a credential before it touches anything (a vault key once arrived labelled as a read key), read keys yes and vault keys never (we leaked our own), audit every vault before its key is published (three vaults shipped as republications), and write the method down rather than the outcome.

*Source: <https://sgit.ai/lessons/index.html> · site v0.4.9 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / Lessons learned

# Lessons learned

Every rule this site enforces started as something that went wrong, or very nearly did. This page is the index of those rules with the incident behind each one attached, because a rule with no origin is only a preference, and the first person who finds it inconvenient will drop it.

**How to read an entry.** **The rule** is the thing to copy, stated so it can be checked; **where it came from** is the event that produced it, kept because the event is what makes the rule survive contact with a deadline. The longer accounts live in [case studies](../case-studies/index.md), which are linked rather than repeated here.

## Classify a credential before it touches anything

**The rule.** Every credential submitted for publication is classified first, by a program, before it is used to clone, audit or render anything. `admin/build/check_credential.py` refuses a write credential by **prefix** (`sgit_vk1_`, which new vaults emit) or, for anything older, by **shape**: a read key is 64 hex characters, and anything else before the colon is a passphrase. Where a write credential arrives, the derived read key is published and the write credential is not; refusing outright just sends the sender back to try again with less care.

**Where it came from.** A credential submitted for publication here was once a **vault key** described as a read key: a legacy `passphrase:vault_id` form with no prefix to give it away. It was caught, only the derived read key was published, and nothing leaked. But the catch depended on somebody looking at it, which is not a control. Prefixes are the better answer because they let a key arrive self-labelled, and a prefix also declares *intent*: `sgit_public_read_` is a read key meant to be published, which is what every row in the vaults table carries or is being moved to. The shape check covers the years of keys created before prefixes existed. [**What each credential can do, and what its prefix declares →**](../docs/credentials.md)

## Read keys yes, vault keys never

**The rule.** A read key is a capability this site hands out on purpose, and it cannot become write access: it is derived from the vault key one way, and there is no path back. A vault key is never published, never pasted into a page, never committed. The validator enforces it rather than trusting anyone to remember: it fails the build on the write-credential prefixes and on the bare `passphrase:vault_id` shape, and it scans every tracked file for the real passphrases held in the gitignored tier.

**Where it came from.** An agent hardcoded this site's own vault passphrase into a tracked file, as part of an anti-leak check. It reached three public commits and was caught only because somebody asked a question about it. The rekey, the measured blast radius and the structural fix are written up in full. [**The day we leaked our own vault key →**](../case-studies/exposed-vault-key.md)

The sequel is worth reading beside it: removing a secret from git history does not remove it from GitHub, because a forgotten merged branch keeps the purged objects reachable and downloadable. [**Deleting files from git history →**](../case-studies/purging-history.md)

## Audit every vault before its key appears anywhere

**The rule.** A vault is audited before its read key is published, and the finding is published on the vault's own page rather than filed away. The reason is that a read key is permanent: content travels with the key forever, so anything in the vault at the moment of publication is public from then on, including the history. Several vaults on this site are *republications*, a clean vault created from audited content, precisely because the original could not be corrected after the fact.

**Where it came from.** Three separate audits found a plaintext write credential inside vault content that was about to be published: the strategy maps vault, the health score vault and the regulation graph vault each shipped as a sanitised republication instead. Each of those pages states its own finding. The audit step exists because in all three cases the vault looked finished and the finding was in a file nobody had opened for weeks.

## Write the method down, not just the outcome

**The rule.** Anything done more than twice is written as a method another agent can follow from nothing: the steps in order, the tool that does each one, and the mistake that produced each rule in it. Publishing a vault has seven such steps, from classifying the credential to recording what outlives the release.

**Where it came from.** The same publication mistakes kept arriving from different directions, because the knowledge lived in whoever had done it last. A method that names the mistake beside the step is the only version that survives being handed over. [**Publishing a vault: the method →**](../demos/vaults/publishing.md)

## Worked accounts

Where a lesson has a full write-up with numbers, it is a case study rather than an entry here, and this page links to it rather than retelling it.

[Incident### The day we leaked our own vault keyThree public commits, the rekey runbook, the measured blast radius (336 objects out, 90 in, zero overlap) and the structural fix that now fails the build.Read the incident →](../case-studies/exposed-vault-key.md)

[Runbook### Deleting files from git history15,933 files across 112 commits, why `git rm` is not deletion, why the push had to be forced, and the forgotten branch that kept the purged objects downloadable.Read the runbook →](../case-studies/purging-history.md)

[Workflow### One working tree, two version control systems76 releases in a folder that was both a vault and a git repository, the ordering rule that made it safe, and the numbers behind retiring it.Read the retrospective →](../case-studies/one-tree-two-remotes.md)

## Where the rest of the rules live

- [How the site is run](../team/index.md): nine agentic roles, each stating the rules it enforces and the mistake behind each rule. This page is the cross-role version of the same idea.
- [Vault credentials](../docs/credentials.md): the two capabilities, the five prefixes, and why a mislabelled read key is a real problem even when the bytes are identical.
- [When NOT to use sgit](../docs/limitations.md): the edges, stated plainly, so a reader finds them here rather than the hard way.
- [Published vaults](../demos/vaults/index.md): the vaults these rules were learned on, every read key published on purpose.

[← Case studies](../case-studies/index.md)[Published vaults →](../demos/vaults/index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/lessons/index.html)*
