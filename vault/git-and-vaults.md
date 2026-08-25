# Git repos inside vaults — SG/Vault

> Run git and sgit side by side: the encrypted store in a git remote, the leak-audit boundary, the GitHub round trip — plus a pure-Python git reader preview.

*Source: <https://sgit.ai/vault/git-and-vaults.html> · site v0.2.42 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [SG/Vault](index.md) / Git repos inside vaults

# Git repos inside vaults

Engineering preview. A git repository is, in the end, just files — which means a vault can hold a complete repo, `.git` folder included, giving you an end-to-end-encrypted remote for your full history. The missing piece is *legibility*: making that history readable wherever the vault lands, without assuming a git binary. That piece now exists.

**Live example:** this website is built exactly this way — one folder, both systems, two pushes per release. The worked case study, including the surprise (the encrypted ref always looks modified to git, because AES-GCM re-encrypts with a fresh IV on every write) and the release script that keeps both remotes honest, is at [one working tree, two remotes](../case-studies/one-tree-two-remotes.md).

## A pure-Python git reader

The sgit project has a working git reader — ~600 lines of implementation in the same Type_Safe style as sgit itself — that reads the `.git` object store directly: loose objects, packfiles (index v2, including large offsets), delta reconstruction (both OFS and REF deltas), symbolic refs and `packed-refs`. No `git` binary, no gitpython, no dulwich — its only dependency is the same type-safety framework sgit already uses.

Verified against sgit's own development repository (900+ commits) during review:

```
>>> svc = Git_Repo__Reader__Service(repo_path='…/SGit-AI__CLI')
>>> [b.name for b in svc.branches()]
['dev', 'claude/sgit-positioning-proposal…']
>>> svc.head_commit()
HEAD 2e2dd4c · 1 file changed · author + message parsed
>>> len(svc.object_parser.flatten_tree(head.tree_sha))
1161   # every file in HEAD, resolved through packfiles and deltas
```

## Why this matters for vaults

- **Legible encrypted code archives.** Clone a vault containing a repo, and an agent — or a vault app — can render its history, branches, and per-commit file changes anywhere Python runs: sandboxes, Lambdas, CI containers, none of which need git installed.
- **A repo view for SG/Vault.** The same parsing logic, ported to the browser client, would let SG/Vault show commit history for repos stored in vaults — GitHub-style legibility over content the server cannot read.
- **Agent code-analysis on a time budget.** Combine a [sparse clone](../docs/agents.md) with the reader: fetch only `.git`, walk the history, fetch working-tree files on demand.
- **One mental model, twice.** git's object graph (commits → trees → blobs, refs on top) is exactly the model sgit rebuilt over an encrypted content-addressed store. The reader proves the model small enough to reimplement legibly in ~600 typed lines — which is the same bet sgit made, in the other direction.

## Run git and sgit side by side

The integration runs the other way too: the same folder can be a git repository *and* an sgit vault at once — git's ecosystem (remotes, pull requests, CI, GitHub Pages) over the working files, sgit's zero-knowledge sync over the same content, and a git remote that doubles as an **encrypted mirror of the vault itself**.

Why this is safe by construction: the `bare/` store is byte-parity with what the sync server holds, and the server is untrusted *by design* — everything in `bare/` is protected by the vault key, not by where it sits. Git exposure of `bare/` is therefore equivalent to server exposure, which the zero-knowledge model already accepts. A git remote is just a second untrusted server — one that also gives you distribution, replication and history for free.

The boundary reduces to three rules:

```
# .gitignore — the whole of it
.sg_vault/local/   # plaintext tier: vault key, push token, unwrapped private keys
.sg_vault/work/    # scratch area — may hold plaintext transiently
*.pem              # defence in depth: no unwrapped key material anywhere, ever
```

Pair it with a `.gitattributes` that marks `.sg_vault/**` as `binary -diff -merge`: ciphertext has no meaningful line diff, and a textual merge would corrupt it. Everything else is committed — including the **plaintext working tree, which is the point**: the vault's contents readable, searchable and reviewable on GitHub, with blame, PRs and CI on top. That makes repo visibility a *content* decision, not a crypto one: `bare/` is safe either way; your documents are what you are choosing to expose.

### The round trip: edit on GitHub, pull back into the vault

Because the working tree is real files, the flow runs both ways. Edit a file in the GitHub web editor, merge a colleague's pull request, let a CI job rewrite a document — then `git pull` into the local clone, and **sgit sees exactly what changed**, the same way it sees your own edits: `sgit status` reports them, `sgit commit` records them in the vault's history, `sgit push` seals them to the server. Two provenance trails, both kept: git records who proposed and reviewed a change; sgit records it landing in the encrypted vault.

### Before first publication: audit, then keep the discipline

- **Run the leak audit from the vault root** before the first `git add`: the vault-key secret must not appear in the working tree, no `BEGIN PRIVATE KEY` outside `local/`, and `bare/` must contain no greppable filenames or content. (The vault serving this site passed all checks before its dotfiles shipped.)
- **Write the protection files before the first `git add -A`** — once `local/` is in a commit it is in history, and removing it later means a history rewrite plus key rotation.
- **For CI**, the vault key goes in GitHub Actions Secrets (and a password manager) — never in files, commit messages, issues or workflow YAML.
- **Disaster recovery comes free:** a git clone of the repo plus the key reconstitutes everything — content, sgit history, all branches — even if the sync server is gone. Do one restore drill before you need it in anger.

The vault serving this site ships the full `.gitignore` / `.gitattributes` pair — clone it for a working example. And once the vault is on GitHub, the same repo can serve the app itself: see [static hosting on GitHub Pages](static-hosting.md).

### What a key rotation does to the mirror

Rotating a vault key (`delete-on-remote` → `rekey` → `push`) re-encrypts every object under a new key, so every content-addressed ID changes and the entire store is replaced. In the git mirror that lands as one large commit — for this site, 336 objects deleted and a fresh set added. Nothing breaks (the `.gitattributes` binary rule means no diff churn), but two consequences are worth knowing before you rotate:

- **Git becomes the history.** A rekey resets the vault's own commit history to a single commit. The git mirror still holds every previous version — which is the side-by-side pattern earning its keep: each remote covers the other's gap.
- **A rekey protects the server, not the mirror.** Old ciphertext already pushed to git stays in git history, and remains decryptable by the old key. If that key was ever exposed *and* the repo is public, rotating does not un-publish the old content — for public content (like this site) that is a non-issue, but for a private vault, treat a rotation as incomplete until the mirror's history is scrubbed too. Rotate first, then decide about history.

This section exists because it happened here: the passphrase for this site's own vault was written into a tracked build file (an anti-leak regex that became the leak), reached three public commits, and was caught by the audit above. The key was rotated the same hour and the old vault deleted from the server; the exposed content was this public website. Recorded rather than quietly fixed — see the [release history](../admin/versions.md).

## Status — honestly

- The reader is **in review, not shipped**. It is read-only, follows first parents (no merge traversal), and skips submodules and shallow clones by design.
- Review has already produced fixes: two schemas needed the project's own default-value convention applied, and the string-sanitization rules need loosening so file paths and commit messages round-trip byte-faithfully before this ships.
- When it lands, it lands the way everything here does: typed, tested against real repositories, and documented on this page.

[← Sub-vaults](sub-vaults.md)[Static hosting →](static-hosting.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/vault/git-and-vaults.html)*
