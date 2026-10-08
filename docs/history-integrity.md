# History integrity: the format gate, verifying signatures, and rewinds, sgit Docs

> Requires sgit-ai 0.19.0 or newer. sgit vault format raises a vault to 128-bit object ids and a minimum client; sgit check verify reports commit signatures; a rewound branch is refused unless accepted; the branch index is repaired after web pushes. Who can open a raised vault, the two misleading messages an older client shows and why sgit update is the only fix, and a checklist for raising a vault.

*Source: <https://sgit.ai/docs/history-integrity.html> · site v0.6.104 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Docs](index.md) / Guides

# History integrity: the format gate, verifying signatures, and rewinds

Requires sgit-ai 0.19.0 or newer: `sgit version` to check, `sgit update` to upgrade. **Nothing changes for an existing vault until its owner raises it** with `sgit vault format`; until then every client, old or new, behaves as it did in 0.18.0.

A vault is a Merkle tree of encrypted objects: every file, folder and commit is stored under the hash of its ciphertext, every commit names its parents and its root folder by those hashes, and every object and ref is AES-256-GCM encrypted under a key the server never holds. So the server cannot alter a byte of history without it failing to decrypt, and `sgit check fsck` finds anything missing or corrupt. 0.19.0 adds what that model did not give you: who may open a vault, 128-bit addresses, a branch pointer that only moves forward, and signatures you can check. All of it is per vault and off by default.

## The format gate: `sgit vault format`

Every vault has a gate in its branch index. A vault that has never been touched by this command reads as format 1 with no minimum client, which is exactly the 0.18.0 behaviour.

```
$ sgit vault format
  Format:      1  (new objects get 12-hex ids)
  Min client:  none   (this client: v0.20.0)
  Features:    none

Raise it with: sgit vault format --set 2 --min-client <X.Y.Z> [--feature signatures-required]
  Clients older than --min-client refuse the vault by name (sgit update); existing objects are untouched.
```

The owner raises it, from any clone with the vault key:

```
$ sgit vault format --set 2 --min-client 0.19.0
Vault format updated and written to the server.

  Note: once a new object is written here, sgit-ai older than 0.19.0 cannot read this vault.
        Those clients do not know this gate exists, so they will NOT say "update": a fresh clone
        reports "integrity check refused vault data" and a pull reports "missing file … run
        sgit check fsck". The fix for them is `sgit update`, never `vault move` or `fsck --repair`.
        Raise a vault only once every agent that writes to it is on 0.19.0 or newer.
  Format:      2  (new objects get 32-hex ids)
  Min client:  0.19.0   (this client: v0.20.0)
  Features:    ids-128
```

- **`--set 2`**: from now on, every new object this vault stores gets a 128-bit content address (`obj-cas-imm-` plus 32 hex characters) instead of 48 bits. Existing objects keep their ids and still verify; a clone holds both. Nothing is re-encrypted and no `vault move` is needed. A format cannot go back down: `error: … format cannot go down (vault is at 2); objects already written at the wider id would be unreadable`.
- **`--min-client X.Y.Z`**: a client from 0.19.0 on that is older than this refuses the vault by name: `error: this vault needs sgit-ai >= 0.20.0 and this is 0.19.0: run `sgit update`, then try again`. You cannot set a minimum you do not meet yourself (`… you would lock yourself out`). Compared on the three numbers; a dev build is never refused.
- **`--feature NAME` / `--remove-feature NAME`**: policies. `signatures-required` is the one that exists today, [below](#signatures).

**Why 128 bits.** A 48-bit address is plenty against the server, which cannot produce decryptable bytes at all. It is not plenty against someone who holds the vault key and wants to swap an object for another with the same address: that is 248 hashes, hours on a GPU. On a raised vault it is 2128. Cost on the shared CRM vault used as the example in these pages (674 commits, 19,780 objects): 1.5 % more bytes, no visible change in time.

## Who can open a raised vault

| Client | Un-raised vault (format 1) | Raised vault (format 2) |
|---|---|---|
| sgit-ai 0.20.0, 0.19.0 | works, unchanged | works; refuses by name if below the vault's `--min-client` |
| sgit-ai 0.18.x and older | works, unchanged | **fails, and blames the data.** A fresh clone says `integrity check refused vault data`; a pull says `missing file … sgit check fsck`. The fix is `sgit update` |
| The web UI | works | reads it; its pushes still write 48-bit ids and drop the index gate until its update ships, and the next CLI pull repairs the index |

**The one thing to plan.** A client older than 0.19.0 does not know the gate exists, so it cannot tell you to update. Raising the vault does nothing to it by itself; the first object written at a 32-hex id after the raise is what stops it, and it stops with one of these, both of which read like damage:

```
error: integrity check refused vault data — clone needs object obj-cas-imm-…, which was
refused by the content-address check … the host served corrupt or substituted content:
do not trust this source.

error: missing file — object obj-cas-imm-… is not in the local store
  hint: try "sgit check fsck ." to check and repair
```

**Neither hint applies.** Nothing is corrupt and nothing was lost: an old client cannot parse a 32-hex id. Do not run `sgit vault move` or `fsck --repair`. Run `sgit update` and retry. Checked on this site on 8 October 2026 with real 0.17.0 and 0.18.0 installs against a throwaway vault on the live dev API: those are the messages, word for word.

**The rule for vault owners:** raise a vault only once every agent that writes to it is on 0.19.0 or newer, and pass `--min-client 0.19.0` so that clients from 0.19.0 on refuse by name rather than by symptom.

## The branch index is shared, and now repaired

The branch index lists every clone branch, maps each to its signing key, and carries the gate. The web UI currently overwrites it with a single entry on every push, which used to lose the other entries for good. From 0.19.0 the CLI treats the index as a shared document: `pull` reads the remote copy, merges it with the local one (every branch, the stronger gate) and writes the merge back with compare-and-swap; `push` registers a clone branch the same way.

```
$ sgit pull
  ▸ Branch index: restored 2 entr(y/ies) the remote copy had lost
```

You do not have to do anything; it is the reason a raised gate survives a web push.

## Rewinds: the named branch only moves forward

The named branch is a pointer. The server, or anyone with the key running `sgit push --force`, can point it at an older or unrelated commit. Each clone now remembers the last remote head it accepted, and a new head that does not descend from it is a **rewind**.

```
$ sgit status
  Remote: the named branch was REWOUND or rewritten on the server (it no longer descends from obj-cas-imm-…)
          if that was a deliberate `sgit push --force`, run: sgit pull --accept-rewind
          otherwise treat it as tampering and check with the vault owner

$ sgit pull
error: the remote named branch was rewound or rewritten: it pointed at obj-cas-imm-… the last
time this clone saw it and now points at obj-cas-imm-…, which does not descend from it. If this
was a deliberate `sgit push --force`, run `sgit pull --accept-rewind`; otherwise treat it as
tampering and check with the vault owner. Nothing was changed.
```

- **You, or a teammate, force-pushed on purpose** (after `sgit history reset`, say): every other clone runs `sgit pull --accept-rewind` once. The clone that pushed needs nothing.
- **Nobody did**: do not accept it. Your clone still holds the newer history; `sgit push` would put it back. Tell the vault owner.
- **The web UI pushed**: today the web UI's push does not compare before writing, so two people saving at the same moment can drop one person's commits. The CLI reports that as a rewind, and it is right to. The web UI team is moving to compare-and-swap.

Normal forward moves, a clone's first pull, and a fresh `sgit init` over an existing vault id are never rewinds.

## Signatures: `sgit check verify`

Every CLI commit is signed with the clone branch's ECDSA P-256 key. 0.19.0 is the first release that checks them.

```
$ sgit check verify
Checked 674 commit(s): 247 verified, 0 bad, 112 unsigned, 315 without a known key, 0 missing
```

| Status | Meaning |
|---|---|
| verified | the signature checks under the key the commit names, or the key the branch index maps its branch to |
| bad | the signature does not check: the commit was altered after signing. `fsck` fails on this |
| unsigned | written without a key: the web UI, or a clone with no local signing key |
| without a known key | signed, but neither the commit nor the index says by which key: commits from before 0.19.0 whose branch has left the index |

New commits carry their key id and sign canonical bytes (RFC 8785 over the stored commit JSON, minus the signature), so from 0.19.0 on "without a known key" stops growing; older signatures still verify. `sgit check fsck` prints the same summary, and on the example vault now takes 12 s instead of 270 s. `check verify` works on a [partial clone](partial-clones.md) too: a scoped clone checks the commits it holds, a shallow one stops at its boundary.

**Requiring signatures.** `sgit vault format --feature signatures-required` makes every `pull` refuse the first incoming commit that is not *verified*, by name, before merging:

```
error: this vault requires signed commits and incoming commit obj-cas-imm-… is unsigned; the
pull was refused before anything was merged. Ask the vault owner, or relax the policy with
`sgit vault format --remove-feature signatures-required`.
```

Turn it on only for vaults written by 0.19.0+ CLIs with their keys: today's web UI does not sign, and history from before 0.19.0 is not retroactively verifiable. `sgit migrate apply` refuses on a vault with signed commits (a migration rewrites history) unless `--force`.

## A checklist for raising a vault

1. Every agent that writes to it is on 0.19.0 or newer (`sgit version`). Point them at [Update sgit-ai to 0.20.0](update-to-0-20-0.md).
2. `sgit check fsck` is clean and `sgit check verify` shows no *bad* commits.
3. `sgit vault format --set 2 --min-client 0.19.0`.
4. Each agent's next `sgit pull` picks the gate up; nothing else to do.
5. `signatures-required` only once no web-UI writes are expected on the vault.

From the sgit-ai team's 0.19.0 and 0.20.0 notes. The old-client messages were found by this site's own check of the 0.19.0 draft, which had said "a validation error"; the CLI team confirmed them and added the warning that 0.20.0 prints when a vault is raised. Release notes: [sgit-ai 0.20.0 (includes 0.19.0)](../updates/index.md#sgit-ai-0-20-0).


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/docs/history-integrity.html)*
