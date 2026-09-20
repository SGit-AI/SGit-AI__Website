# Deleting files from git history, and why they are still on GitHub afterwards — sgit.ai case study

> How this repository dropped 15,933 files from every one of its 112 commits: the setup with two branches drawn out, why git rm is not deletion, what git filter-repo does to every commit id, why the push had to be forced and how the lease made it safe, why a forgotten merged branch kept the purged objects reachable and downloadable, what happens when it is deleted, and the order to do it in when the file is a secret.

*Source: <https://sgit.ai/case-studies/purging-history.html> · site v0.2.99 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Case studies](index.md) / Deleting files from git history

# Deleting files from a repository's history, and why they are still on GitHub afterwards

On 19 September 2026 this site's repository dropped 15,933 files it no longer wanted — not just from the current tree, but from every one of the 112 commits that had ever carried them — and force-pushed the result. This page is the exact scenario, drawn out: what the setup was, which branches were in play, what was deleted, why a plain `git rm` would not have done it, why the push had to be forced, and why the deleted files were **still downloadable from GitHub** after the force push landed, until one more branch was removed.

**Read this before copying it.** Everything purged here was ciphertext under a key that was never in the repository, so the purge was housekeeping, not remediation. If the thing you want out of history is a *secret*, history rewriting is the second step and never the first: **rotate the secret, then rewrite**. A rewrite shrinks the window; it does not close it, for the reasons in [the section on why the files are still there](#still-there). The account of that situation is [the day we leaked our own vault key](exposed-vault-key.md).

## The setup

One working folder, two version control systems, one remote with two branches. The folder was both an sgit vault and a git repository ([the pattern and why it was retired](one-tree-two-remotes.md)), and git tracked the vault's encrypted store as a mirror.

```
LOCAL WORKING TREE                              GITHUB · SGit-AI/SGit-AI__Website
sgit-ai-website/                                 ┌──────────────────────────────────────┐
├── .git/            ← git metadata              │ refs/heads/dev            e70d582d  │ ── deploys ──▶ GitHub Pages
├── .sg_vault/                                   │   112 commits, v0.1.0 … v0.2.83     │                sgit.ai
│   ├── bare/        ← 15,933 encrypted files    │                                      │
│   │   ├── data/       (258 MB)   TRACKED       │ refs/heads/claude/site-access-…      │
│   │   ├── indexes/               TRACKED       │   9f9f7772 · 23 Aug · merged in dev  │
│   │   ├── keys/                  TRACKED       └──────────────────────────────────────┘
│   │   └── refs/                  TRACKED
│   ├── local/       ← vault key, token   GITIGNORED (never committed)
│   └── work/        ← scratch           GITIGNORED
├── admin/, docs/, demos/ …   ← the site: ~750 files, 24 MB
└── index.html
```

Two things to notice before anything is deleted. The plaintext credential tier under `.sg_vault/local/` was excluded from git from the very first commit, which is the single fact that made the rest of this page routine. And the remote had *two* branches: `dev`, which GitHub Pages deploys, and a working branch from August that had been fully merged into `dev` and then left behind. That second branch is the reason for the last two sections.

## What we wanted gone

Everything under `.sg_vault/`. It was 91% of the repository by size, had had no reader since it was created, and had been dead — unreachable for a push — since v0.2.76. The numbers:

| What | Before | After |
|---|---|---|
| Tracked files | 16,679 | 746 |
| Of which under `.sg_vault/` | 15,933 | 0 |
| Size of `.sg_vault/` in the working tree | 258 MB | — (folder removed) |
| Git pack (the whole history) | 276 MB | 21 MB |
| Commits | 112 | 112 — same commits, every one rewritten |
| Commits whose id survived unchanged | 0 |

## Why `git rm` is not deletion

Git does not store diffs. Every commit points at a complete snapshot — a tree of trees ending in blobs — and a blob stays in the repository for as long as *any* commit anywhere points at it. Removing a folder in a new commit produces a new snapshot without it. Every previous snapshot is untouched.

```
"git rm -r .sg_vault  →  git commit"  — the folder leaves the tip and nothing else:

  v0.1.5 ──▶ v0.1.6 ──▶ … ──▶ v0.2.83 ──▶ v0.2.84 (new)
    │          │                 │            │
    ▼          ▼                 ▼            ▼
  tree       tree              tree         tree
  ├ site     ├ site            ├ site       ├ site        ← only this one lacks it
  └ .sg_vault└ .sg_vault       └ .sg_vault

  git clone  →  fetches ALL of these  →  258 MB arrives anyway.
  git checkout v0.2.83  →  the folder is back, byte for byte.
```

So the tip would have been clean and the clone would have been the same size. For the mirror that was merely wasteful. For a leaked secret it is the failure mode that catches people every year: the file is gone from the branch, and `git log --all -- path/to/secret` still finds it in thirty seconds.

## What a history rewrite does

`git filter-repo` walks every commit, rebuilds its tree without the excluded paths, and writes a *new* commit. A commit's id is a hash of its content, including its tree and its parent's id, so removing a path from the first commit that carried it changes that commit's id, which changes its child's id, and so on to the tip. The old objects are left unreferenced and swept away by the repack that follows.

```
BEFORE  (the history GitHub had)
  4c1d11d4 v0.2.76 ──▶ bb248b12 v0.2.77 ──▶ … ──▶ e70d582d v0.2.83
  tree: site + .sg_vault   tree: site + .sg_vault         tree: site + .sg_vault

        git filter-repo --path .sg_vault --invert-paths --force
        (1.5 s to rewrite 112 commits; then a repack drops the orphaned blobs)

AFTER   (a different history: same authors, dates, messages, site files; new ids)
  005361e8 v0.2.76 ──▶ 44323549 v0.2.77 ──▶ … ──▶ 45b99758 v0.2.83 ──▶ b5ae665d v0.2.84
  tree: site only          tree: site only                tree: site only    tree: site only

  Not one id is shared between the two rows. They are two unrelated chains
  that happen to contain the same site files at each step.
```

Three practical consequences. Every commit id anyone had written down — in the release history, in an issue, in a URL — now names a commit that exists only in the old chain. Any clone made before the rewrite is on the old chain and cannot fast-forward onto the new one; it has to be re-cloned or hard-reset. And the tool refuses to run on anything but a fresh clone unless told `--force`, and removes the `origin` remote when it finishes, precisely so that nobody pushes the rewrite by reflex.

## Why the push had to be forced

A normal push is a fast-forward: the remote accepts a new tip only if the tip it currently holds is an ancestor of it. After a rewrite that is never true.

```
remote refs/heads/dev  =  e70d582d   (old chain)
local  refs/heads/dev  =  b5ae665d   (new chain)

  is e70d582d an ancestor of b5ae665d?   NO — they share no commit at all
  →  ordinary push is refused: "non-fast-forward"

  git push --force-with-lease=dev:e70d582d origin dev
                        └────────┬────────┘
    "replace dev, but ONLY if it still points at e70d582d" — if anyone had
    pushed to dev in the meantime, this fails instead of overwriting their work.

  +  e70d582d...b5ae665d  dev -> dev  (forced update)
```

The lease is the important half. A bare `--force` overwrites whatever is there; `--force-with-lease` pinned to the id we started from turns the push into a compare-and-swap. On a branch with more than one contributor it is the difference between a rewrite and an accident.

GitHub Pages then rebuilt from the new `dev` exactly as it does for any push. The deployed site never carried the mirror, so nothing visible changed — v0.2.84 appeared within ninety seconds.

## Why the deleted files were still on GitHub, and downloadable

This is the part that surprises people, and it comes back to the second branch in the first diagram.

```
GITHUB, one minute after the forced push

  refs/heads/dev ──────────▶ b5ae665d ──▶ 45b99758 ──▶ … ──▶ 005361e8 ──▶ …   (NEW chain, no .sg_vault)

  refs/heads/claude/site-access-branch-commit-6h2bix
                 └─────────▶ 9f9f7772 ──▶ 82d5d1e3 ──▶ … ──▶ (68 commits)     (OLD chain)
                              tree: site + .sg_vault  — 6,191 encrypted files at that point

  Git keeps every object reachable from ANY ref. The old branch is a ref.
  Everything it can reach — including every .sg_vault blob in those 68 commits —
  is therefore still a live, first-class object in the repository on GitHub.
```

Reachability is the whole rule. Deleting a branch's content from *one* chain does nothing to objects that another ref can still walk to. The stale branch had been merged into `dev` in August and forgotten; it never had a reason to exist after that, but it kept the old chain alive.

Concretely, while that branch exists:

- **`git clone` brings the old objects down.** A clone fetches every branch by default. Anyone cloning after the force push gets the small new `dev` *and* the old branch with its 6,191 encrypted files — the clone is smaller than before, but the purge is not visible from the outside.
- **Old commit URLs keep working.** `github.com/…/commit/9f9f7772` renders, its tree is browsable, and any file in it can be viewed or downloaded raw.
- **`git fetch origin claude/site-access-…` re-imports the whole thing** into a clean clone in one command. We know, because verifying this page did exactly that.

There are two further places the old objects can live that no branch deletion reaches, and both are worth knowing even though neither applied here. **Forks** share GitHub's object storage with the parent and keep their own refs, so a fork made before the rewrite holds the old chain regardless of what the parent does. And **pull request refs** (`refs/pull/N/head`) are kept by GitHub for closed and merged PRs; they are not listed as branches and cannot be deleted by the repository owner, but they pin the commits they point at. This repository had no forks and no pull requests carrying the mirror.

## What happens when the branch is deleted

```
  git push origin --delete claude/site-access-branch-commit-6h2bix

  refs/heads/dev ──▶ b5ae665d ──▶ … (new chain)             ← still reachable

  (no ref) ·········▶ 9f9f7772 ──▶ … ──▶ .sg_vault blobs    ← UNREACHABLE
                                                             nothing points here any more
```

Three things follow, on three timescales.

1. **Immediately:** a fresh clone no longer receives the old chain. Clone size drops to the 21 MB pack. From the outside the purge is now complete.
2. **Soon, but not instantly:** the old commit URLs stop rendering and raw-file downloads by old id stop working. Unreachable objects sit on GitHub's storage until its garbage collection runs, which is on its own schedule and not the owner's; anyone who already knows a full 40-character id can still address those objects until then. For a real secret exposure, GitHub Support will run that collection and purge cached views on request — the request is the step that turns "eventually" into "today".
3. **Never, on its own:** every clone made *before* the deletion still holds the old objects, and nothing anyone does on GitHub changes that. This is why a purge is not a remediation for a secret, and why the case study on the leak rotated the key before it did anything else.

Status as this page is written: the deletion was attempted three times from the session that did the rewrite and was refused by the session's git proxy, which permits pushes but not ref deletion. The branch is to be removed from the GitHub UI, and until it is, everything in the previous section holds. The paragraph will be updated when it has been.

## The order we did it in

Written as a recipe, because the order matters more than any single command.

1. **Know what the deletion is for.** Housekeeping (this case) or secret exposure? If the latter, rotate first and treat the rest of this list as a size reduction, not as containment.
2. **Get the whole history locally.** A shallow clone cannot be rewritten meaningfully; ours had to be unshallowed to all 112 commits first.
3. **List every ref on the remote** with `git ls-remote --heads origin`, and for each branch you did not know about, find out whether it is merged and whether it carries the paths. The stale branch here was fully merged and did carry them.
4. **Park uncommitted work.** The rewrite ends with a hard reset. We saved the pending edits as a patch, reset the tree, and re-applied afterwards.
5. **Rewrite:** `git filter-repo --path .sg_vault --invert-paths --force`. Check the result before going further: file count, pack size, `git ls-files` for the path returning nothing.
6. **Re-add the remote** the tool removed, and re-apply the parked edits.
7. **Make the tree consistent** in the same release: `.gitignore` now excludes the path outright, every page that described the old state is rewritten, tooling that read from the path is re-pointed. Build and validate.
8. **Force-push with a lease** pinned to the id the remote held when you started.
9. **Delete every other ref that reaches the old chain** — branches you own, tags, and ask GitHub Support about anything you cannot delete yourself.
10. **Tell every other clone.** Anyone with a checkout is now on a dead chain and must re-clone or hard-reset; a `git pull` will produce a confused merge of two unrelated histories.
11. **Verify from the outside:** a fresh clone, its size, and that the paths appear in no ref.

## What made this safe here

Every object removed was ciphertext under a key that never entered the repository — the `local/` tier was gitignored from the first commit and the tripwire that scans for the passphrase has run on every release since [the one time it got in](exposed-vault-key.md). So the old chain surviving on a forgotten branch for a few hours is a storage anomaly, not an exposure. The same procedure applied to a repository where the plaintext tier *had* been committed would be the right mechanics in the wrong order: the rewrite would go through, the stale branch would keep the plaintext downloadable, existing clones would keep it forever, and the only thing that would actually have protected anyone is the rotation that should have come first.

## Related

- [One working tree, two version control systems — and why we stopped](one-tree-two-remotes.md) — why the mirror existed and why it was retired
- [The day we leaked our own vault key](exposed-vault-key.md) — the same tools, in the order that matters when a secret is involved
- [Git repos inside vaults](../docs/vault/git-and-vaults.md) — the pattern this repository used, still right when something reads the mirror
- [Release history](../admin/versions.md) — where the commit column switches from the old chain's ids to the new one's

[← One tree, two remotes](one-tree-two-remotes.md)[The exposed vault key →](exposed-vault-key.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/case-studies/purging-history.html)*
