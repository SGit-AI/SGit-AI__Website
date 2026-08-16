# One working tree, two version control systems — sgit.ai case study

> How this site is developed in a single folder that is both an sgit vault and a git repository: what each remote carries, the .gitignore boundary that makes it safe, why the encrypted ref always looks dirty to git (fresh AES-GCM IVs), and the release script that refuses to finish until both remotes are in sync.

*Source: <https://sgit.ai/case-studies/one-tree-two-remotes.html> · site v0.2.18 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Case studies](index.md) / One tree, two remotes

# One working tree, two version control systems

This site is developed in a single folder that is simultaneously an sgit vault and a git repository. Every release pushes both. This page is the workflow, the boundary that makes it safe, the one ordering rule that keeps the mirror true, and the script that enforces it.

## What happened

The folder that holds this site has two version control directories side by side:

```
sgit-ai-website/
├── .git/          → github.com/SGit-AI/SGit-AI__Website  (public mirror + Pages deploy)
├── .sg_vault/     → an SG/Send vault                     (encrypted history + live vault)
└── index.html, why/, case-studies/, admin/ …         ← the same files, once
```

They are not two copies kept in agreement. They are two version control systems pointed at **one directory** — `git status` and `sgit status` describe the same bytes. There is no synchronisation step because there is nothing to synchronise; a release is simply two pushes of the same tree:

```
$ sgit commit -m "site v0.2.1: …" && sgit push   # encrypted history → SG/Send
$ git add -A && git commit && git push            # public mirror → GitHub → Pages
```

Each remote does a different job. The git push is what deploys — a GitHub Action publishes the tree to GitHub Pages (excluding `.sg_vault/`, which the public site does not need). The sgit push is what other agents read — this site's vault is cloned and pulled by the Claude Code sessions that build it, and the encrypted store in the git repo doubles as a full off-site mirror of the vault.

## The boundary that makes it safe

The entire pattern rests on one file: `.gitignore`. Everything encrypted **is** committed to git — 900+ objects under `.sg_vault/bare/`, all ciphertext under opaque ids. What is excluded is exactly the plaintext tier:

```
.sg_vault/local/     # vault key, access token, private PEM — plaintext, never committed
.sg_vault/work/      # scratch state
*.pem
```

That is the whole rule, and it is worth stating as a condition rather than a pattern: committing ciphertext alongside plaintext is right *for a public site like this one*, where the working tree is meant to be published anyway. For a confidential vault the same layout is a leak-audit boundary — one bad `.gitignore` edit away from publishing the plaintext tree. The [git repos inside vaults](../vault/git-and-vaults.md) page covers which side of that line a given project is on.

Because the boundary is one file, it gets a machine check, not a convention. The build's validator reads the vault passphrase from the gitignored `local/` tier at runtime and scans every tracked file for it — so a key that reaches the tree fails the build by construction. That check exists because of [the day it actually happened](exposed-vault-key.md): an agent hardcoded this site's passphrase into a tracked file, it survived three public commits, and the vault had to be rekeyed. The tripwire is the structural fix, and the release script below refuses to push unless it has run.

## The one ordering rule: sgit first, then git

Almost everything in the shared store is content-addressed — an object's name is the hash of its ciphertext, so it never changes under its id and the two systems can never disagree about it. Exactly one file is mutable: the vault's HEAD pointer, the **ref**. Every real `sgit push` rewrites it, and that makes the order of the two pushes matter:

```
✓ sgit commit && sgit push     # 1st — writes the new ref
✓ git add -A && git commit && git push   # 2nd — captures that exact ref
```

Done in this order, the git mirror always carries the ref the push just wrote, and a clean `git status` is the normal end state of every release — reads and no-op operations (`ls`, `history`, `status`, `pull`, `fetch`) do not rewrite the ref, so nothing drifts between releases. We verified both claims by testing them.

Reverse the order and the failure is quiet: commit git first and the mirror carries the *previous* ref — in sync by bytes, one commit behind in meaning. Push sgit without a following git commit and the ref shows as modified in `git status`.

One property to know when reading that modified flag: **the ref's bytes carry no information about staleness.** AES-GCM encrypts with a fresh random IV on every write, so a rewritten ref never byte-matches its previous encryption even when it decrypts to the same commit id. "Dirty" therefore does not mean the mirror is stale, and byte-equality would not mean it is current — the only real answers are decrypting the ref or asking `sgit status`. This is also why `.gitattributes` marks the store `binary -diff -merge`: a textual diff of ciphertext is noise, and a git merge of two encrypted refs would produce garbage that decrypts to nothing.

## What changed: the release script

Two pushes with no enforcement is an invitation to forget one — push only sgit and the site never deploys; push only git and the live vault (the one other sessions clone) falls behind. So the release is now one script, [`admin/build/release.sh`](../admin/index.md), and it is deliberately strict:

```
$ ./admin/build/release.sh "site v0.2.2: describe the release"
1. build     — regenerate every page, markdown twin, llms*.txt, sitemap
2. validate  — 90+ file checks, including the key-leak tripwire; any failure aborts
3. sgit      — commit + push the vault, verify "in sync with remote"
4. git       — commit + push, verify local HEAD == origin
5. confirm   — both remotes reported in sync, or exit 1 loudly
```

The ordering inside the script is the rule above, made unforgettable: sgit pushes before git commits, and the expected end state of every release is a clean tree. Two further design points. The script never prints the vault key — it deliberately avoids the commands that would (some sgit inspection commands echo it), because a release log is exactly the kind of artefact that ends up pasted somewhere public. And it will not push *either* remote until the validator has passed, so the key-leak scan and the structural checks gate both histories, not just the deployed one.

## The numbers

| What | Count |
|---|---|
| Files in the shared working tree | ~120 |
| Encrypted objects committed to git under `.sg_vault/bare/` | 933 |
| Plaintext files excluded from git (the `local/` tier) | 5 — key, token, PEM, config, base_url |
| Mutable files in the store (the false-drift class) | 1 — the ref |
| Releases shipped through this workflow so far | every version on the [release history](../admin/versions.md) |

## What we still do not know

- **History depth differs and we accept it.** The vault was rekeyed after the key leak, which reset its history; git kept the full history across the rekey. The two histories agree from that point forward but are not equal before it. For this site that is fine; for an audit-grade deployment you would want the equivalence stated precisely.
- **The IV churn is cosmetic but not free.** Every release commits a re-encrypted ref to git — a 69-byte file that changes on every push forever. Harmless at this scale; a vault with many mutable refs would want them out of git or normalised.

## Related

- [Git repos inside vaults](../vault/git-and-vaults.md) — the general pattern, including the confidential-vault caution
- [The day we leaked our own vault key](exposed-vault-key.md) — why the tripwire exists
- [A live site whose host cannot read it](live-vault-docs.md) — what the sgit push feeds
- [Admin & engineering](../admin/index.md) — the build system this script belongs to

[← Case studies](index.md)[Git repos inside vaults →](../vault/git-and-vaults.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/case-studies/one-tree-two-remotes.html)*
