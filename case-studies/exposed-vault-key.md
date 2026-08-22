# The day we leaked our own vault key — sgit.ai case study

> The runbook for a leaked vault key — rotate, verify, re-point — plus a worked case study of the time it happened to this website.

*Source: <https://sgit.ai/case-studies/exposed-vault-key.html> · site v0.2.41 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Docs](../docs/index.md) / Project

# If a vault key is exposed

A vault key is a **bearer credential**: whoever holds it can read and write the vault, from anywhere, with no account and no reset. There is no revocation list to add it to. So an exposed key has exactly one remedy — **rotate it**, which means taking the old vault off the server and re-encrypting the content under a new key.

**Act first, investigate second.** Rotation takes minutes and costs you a commit history. Working out exactly who saw what takes hours. Do them in that order.

## The runbook

1. **Confirm you hold a complete local clone.** The rotation re-encrypts from your working copy — if your only full copy is on the server, clone it before you delete anything. `sgit status` should be clean, and `sgit vault backup` is cheap insurance.
2. **Delete the vault from the server:** `sgit vault delete-on-remote --token <token>`. This is the step that actually revokes the old key. Rekeying *without* it leaves the old vault — and the old key's access to it — alive on the server.
3. **Rotate:** `sgit vault rekey`. It wipes the local encrypted store, mints a new key and vault ID, and re-encrypts every file. It asks twice for confirmation; the second question ("have you saved your current vault key") is worth taking seriously.
4. **Save the new key** — password manager, before you do anything else. It cannot be recovered.
5. **Publish:** `sgit push`. The vault is now live under the new key with a fresh ID.
6. **Verify the old key is dead** (see below). Do not skip this: "I rotated" and "the old key no longer works" are different claims.
7. **Re-point every consumer** — other machines, agents, CI secrets, share links, bookmarks into the web client. The old vault ID appears in URLs, so anything referencing it needs updating.
8. **Then** investigate: where did the key appear, for how long, and who could have fetched it.

## Verifying the old key is dead

Four independent checks — each should fail or 404:

```
# 1. the obvious one
$ sgit clone <old-vault-key> /tmp/check     # must fail: no branch index found

# 2-4. raw HTTP against the old vault id — derive the ids, then GET/PUT them
#   - the old ref file id            → expect 404
#   - a known old object id          → expect 404
#   - a PUT with the old write key   → expect rejection
```

A successful clone or a 200 on any of those means the rotation did not take — most often because `delete-on-remote` was skipped.

## What rotation costs

- **Vault history resets to a single commit.** Rekey re-encrypts your current files, not the object graph. (A history-preserving rotation is [proposed to the CLI team](../briefs/index.md).) If the vault is [mirrored to git](../vault/git-and-vaults.md), the content history survives there — which is one of the better arguments for running the two side by side.
- **Every object ID changes.** IDs are content hashes *of the ciphertext*, so identical plaintext under a new key produces an entirely new store — zero overlap with the old one. In a git mirror that lands as one large commit swapping the whole encrypted tree.
- **The vault ID changes**, so every URL and stored reference to it breaks.

## The limit worth understanding: mirrors

**A rotation protects the server. It cannot un-publish a mirror.** Encrypted objects already pushed to a git remote stay in that history and remain decryptable by the old key. If the old key was *also* committed there, anyone who clones the repository can still read the old content, forever, regardless of what you rotate.

- **Public content** (a website, published docs): a non-issue — the plaintext was public anyway. Rotate and move on.
- **Private content:** the rotation is only half the job. The mirror's history must be scrubbed too (rewrite or delete the repository), and until it is, treat the old content as exposed.

## Case study: this website, 11 August 2026

This page exists because it happened here, to the vault that serves this site.

**What went wrong.** The site's build has a validator that blocks secrets and stale terms from being published. To catch the vault passphrase specifically, an agent (me) added a rule matching that exact passphrase — and wrote the literal secret into `admin/build/validate.js`, a *tracked* file. The guard against leaking became the leak. Combined with the vault ID (public by design), the full write-capable key sat in three commits of a public repository.

**How it was caught.** Not by tooling — by a question. The vault owner asked "you haven't leaked that key, right?", which triggered the audit documented on the [git page](../vault/git-and-vaults.md): grep the working tree and every commit for the passphrase, for private-key headers, and for readable content in the encrypted store. The first two checks passed. The history grep found it.

**The response,** inside the hour: `delete-on-remote` (336 files removed from the server) → `rekey` (39 files re-encrypted under a new key and ID) → `push`. Then the four verification checks, all confirming the old key was dead: clone failed, old ref 404, old object 404, write with the old write key rejected.

**The aftermath, measured.** 336 old objects out, 90 new in, **zero overlap** — no object ID survived, because the addressing hashes ciphertext. Plaintext was byte-identical across the rotation (verified by hashing files before and after). Vault history went from 14 commits to one; the git mirror kept all 14.

**What changed structurally.** The tripwire now reads the passphrase from the gitignored `.sg_vault/local/` tier at runtime and scans for it, instead of carrying it — so the secret can no longer live in a tracked file, and the check still works. It was tested by planting the new key in a draft page: the build failed, as it should.

**The transferable lessons.** (1) Never write a secret into a file that ships — derive it at runtime from the ignored tier. (2) A leak audit is worth running before your first publish *and* after anything touches your build config. (3) Grep the full history, not just the working tree; `git grep <secret> $(git rev-list --all)` is the check that found this. (4) Rotate before you investigate. (5) Write the incident down — this page is more useful than a quiet fix.

[← When NOT to use sgit](../docs/limitations.md)[The security model →](../security/index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/case-studies/exposed-vault-key.html)*
