# One working tree, two version control systems, and why we stopped, sgit.ai case study

> How this site was developed for 76 releases in a single folder that was both an sgit vault and a git repository (the .gitignore boundary, why the encrypted ref always looked dirty to git (fresh AES-GCM IVs), the ordering rule) and why the vault mirror was retired and purged: no reader, no published read key, 91% of the repository, and seven releases shipped without it before anyone noticed.

*Source: <https://sgit.ai/case-studies/one-tree-two-remotes.html> · site v0.6.7 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Case studies](index.md) / One tree, two remotes

# One working tree, two version control systems, and why we stopped

For seventy-six releases this site was developed in a single folder that was simultaneously an sgit vault and a git repository, and every release pushed both. On 19 September 2026 the vault mirror was removed from the repository and purged from its history. This page keeps the workflow as it ran, the boundary that made it safe, and the ordering rule that kept the mirror true, and then records, with the numbers, why a pattern that was correct stopped being worth carrying.

**Status: retired at v0.2.84.** The site now ships over git alone. The [git-and-vaults](../docs/vault/git-and-vaults.md) pattern this page demonstrated is still right for the cases described there; what changed is that this site stopped being one of them. The reasons are in [the last section](#stopped).

## What we ran

The folder that held this site had two version control directories side by side:

```
sgit-ai-website/
├── .git/          → github.com/SGit-AI/SGit-AI__Website  (public mirror + Pages deploy)
├── .sg_vault/     → an SG/Send vault                     (encrypted history + live vault)
└── index.html, why/, case-studies/, admin/ …         ← the same files, once
```

They were not two copies kept in agreement. They were two version control systems pointed at **one directory**: `git status` and `sgit status` described the same bytes. There was no synchronisation step because there was nothing to synchronise; a release was simply two pushes of the same tree:

```
$ sgit commit -m "site v0.2.1: …" && sgit push   # encrypted history → SG/Send
$ git add -A && git commit && git push            # public mirror → GitHub → Pages
```

Each remote did a different job. The git push was what deployed, a GitHub Action publishes the tree to GitHub Pages. The sgit push was meant to be what other agents read: the plan was that Claude Code sessions building the site would clone and pull the vault, and that the encrypted store committed to git would double as a full off-site mirror of it.

## The boundary that made it safe

The entire pattern rested on one file: `.gitignore`. Everything encrypted **was** committed to git, ciphertext objects under `.sg_vault/bare/`, all under opaque ids. What was excluded was exactly the plaintext tier:

```
.sg_vault/local/     # vault key, access token, private PEM — plaintext, never committed
.sg_vault/work/      # scratch state
*.pem
```

That was the whole rule, and it is worth stating as a condition rather than a pattern: committing ciphertext alongside plaintext is right *for a public site*, where the working tree is meant to be published anyway. For a confidential vault the same layout is a leak-audit boundary, one bad `.gitignore` edit away from publishing the plaintext tree. The [git repos inside vaults](../docs/vault/git-and-vaults.md) page covers which side of that line a given project is on.

Because the boundary was one file, it got a machine check, not a convention. The build's validator read the vault passphrase from the gitignored `local/` tier at runtime and scanned every tracked file for it, so a key that reached the tree failed the build by construction. That check exists because of [the day it actually happened](exposed-vault-key.md): an agent hardcoded this site's passphrase into a tracked file, it survived three public commits, and the vault had to be rekeyed. **The tripwire outlived the mirror.** It now reads the write keys of published demo vaults from a gitignored `admin/local/demo-keys/` folder and scans for those instead; the mechanism is unchanged, only the folder moved.

## The one ordering rule: sgit first, then git

Almost everything in the shared store is content-addressed, an object's name is the hash of its ciphertext, so it never changes under its id and the two systems can never disagree about it. Exactly one file is mutable: the vault's HEAD pointer, the **ref**. Every real `sgit push` rewrites it, and that made the order of the two pushes matter:

```
✓ sgit commit && sgit push     # 1st — writes the new ref
✓ git add -A && git commit && git push   # 2nd — captures that exact ref
```

Done in this order, the git mirror always carried the ref the push had just written, and a clean `git status` was the normal end state of every release. Reverse the order and the failure was quiet: the mirror carried the *previous* ref, in sync by bytes, one commit behind in meaning.

One property worth keeping from this: **the ref's bytes carry no information about staleness.** AES-GCM encrypts with a fresh random IV on every write, so a rewritten ref never byte-matches its previous encryption even when it decrypts to the same commit id. "Dirty" did not mean stale, and byte-equality would not have meant current, the only real answers were decrypting the ref or asking `sgit status`. This is also why `.gitattributes` marked the store `binary -diff -merge`: a textual diff of ciphertext is noise, and a git merge of two encrypted refs would produce garbage that decrypts to nothing.

## The release script, then and now

Two pushes with no enforcement is an invitation to forget one, so the release was one script, [`admin/build/release.sh`](../admin/index.md), and it was strict: build, validate, sgit push and verify in sync, git push and verify HEAD equals origin, then poll the live site until it served the new version. The same script ships the site today with the sgit step removed. It still refuses to push until the validator, including the key-leak tripwire, has passed, and it still refuses to call a release done until `https://sgit.ai/` is serving the version it just pushed.

## Why we stopped

Nothing about the pattern broke. What happened is that its costs stayed and its benefits never arrived, and a container recycle made that impossible to ignore.

- **The mirror had no reader.** The design assumed other sessions would `sgit clone` the site vault. In practice every session that built the site cloned it from GitHub, because that is where the deploy runs from and where the history is legible. Not one release was ever produced from a vault clone.
- **The vault had no published read key.** Every other vault on this site is openable by anyone; the site's own vault was the one nobody could open. A zero-knowledge mirror of public content that nobody can read is storage, not publication.
- **It went dead quietly, and the site did not notice.** The container holding the write key was recycled after **v0.2.76**. Because `.sg_vault/local/` is gitignored by design, no clone could push the vault again. Releases **v0.2.77 through v0.2.83**, seven of them, went out over git alone, and the live site was correct throughout. The mirror had been carrying nothing the deploy depended on.
- **It was 91% of the repository.** The encrypted store was **258 MB in 15,933 files** against **24 MB of site content in about 750 files**. Every clone paid for it; every `git add -A` walked it.
- **Two published pages had become false.** This one said "every release pushes both"; the site's `llms.txt` said the site "is itself served from an encrypted vault". Both statements were true when written and had stopped being true, which is a worse state for a case study than either honest answer.

So on 19 September 2026 the store was removed from the tree, the history was rewritten with `git filter-repo` to drop it from every commit, and the branch was force-pushed. The mechanics, and why the purged files were still downloadable from GitHub afterwards, are drawn out in [a page of their own](purging-history.md). The purge is safe for the same reason the mirror was safe: everything removed was ciphertext under a key that was never in the repository. What is gone from GitHub is a copy of the vault's encrypted history; the vault itself, on the SG/Send server, is untouched and still holds it.

## The numbers

| What | Count |
|---|---|
| Releases shipped with both pushes | 76 (through v0.2.76) |
| Releases shipped over git alone while the mirror was unreachable | 7 (v0.2.77 – v0.2.83) |
| Encrypted objects removed from git | 15,933 files, 258 MB |
| Site content that remained | ~750 files, 24 MB |
| Times the mirror was cloned to produce a release | 0 |
| Plaintext ever in the purged history | none, the local/ tier was gitignored from the first commit |

## What we would do differently

- **Give the mirror a reader before giving it a remote.** If nobody clones the vault, do not build a release process around pushing it. The [board vault](../demos/vaults/board/index.md) is the pattern working: it is pulled by the release, rendered into a page, and updated by anyone holding its key, it earns its place because something reads it.
- **A public site's vault should have a public read key, or not exist.** The site publishes read keys for thirty vaults. Withholding its own was an inconsistency, not a precaution.
- **Measure the mirror against the content.** Ninety-one per cent of a repository is a number that should have been on this page from the start.

## Related

- [Git repos inside vaults](../docs/vault/git-and-vaults.md), the general pattern, and the confidential-vault caution, both still current
- [The day we leaked our own vault key](exposed-vault-key.md), why the tripwire exists, and why it stayed after the mirror went
- [The board as a vault](../demos/vaults/board/index.md), the vault this site still pulls at every release
- [Admin & engineering](../admin/index.md), the release process as it is now

[← Case studies](index.md)[Git repos inside vaults →](../docs/vault/git-and-vaults.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/case-studies/one-tree-two-remotes.html)*
