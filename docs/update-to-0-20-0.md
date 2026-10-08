# Update sgit-ai to 0.20.0, sgit Docs

> For an agent told to update: sgit update, sgit version shows v0.20.0 (which includes 0.19.0). Nothing changes until the vault owner raises the vault. The three messages you might see, what each means, and what not to do: never vault move or fsck --repair when an old client blames the data.

*Source: <https://sgit.ai/docs/update-to-0-20-0.html> · site v0.6.104 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Docs](index.md) / Guides

# Update sgit-ai to 0.20.0

A short page for an agent, or a person running agents, that has been told "read this, update to the latest version". Two minutes. sgit-ai 0.20.0 was published to PyPI on 8 October 2026 and includes everything in 0.19.0 (7 October); there is no reason to stop at 0.19.0.

## 1. Update and check

```
$ sgit update          # wraps: pip install --upgrade sgit-ai
$ sgit version
sgit-ai v0.20.0
```

If `sgit version` still shows an older version, you have more than one Python environment; run `python -m pip install --upgrade sgit-ai` in the one your harness uses, then check again. [Installation](installation.md) has the rest.

## 2. What changes for you: nothing, until the vault owner raises the vault

Every command works as in 0.18.0. Three things are new:

| New | What it means for you |
|---|---|
| `sgit check verify` | how many commits in the vault have a verifiable signature. Read-only; works on a partial clone |
| `sgit vault format` | shows the vault's format and minimum client. Only the vault owner changes it |
| `sgit check fsck` | now takes seconds, not minutes, and prints a signature summary |

## 3. Three messages you might see

**Message 1**, on `status` or `pull`: `the named branch was REWOUND or rewritten on the server`. Someone force-pushed, or the server served an old pointer. Nothing was changed on your side. Do not accept it on your own; tell the vault owner. If the owner says it was deliberate: `sgit pull --accept-rewind`.

**Message 2**, on any command, once the owner has raised the vault's minimum client: `error: this vault needs sgit-ai >= X.Y.Z and this is …: run `sgit update`, then try again`. Do exactly that.

**Message 3**, only if you are still on 0.18.x or older and the owner has raised the vault: a fresh clone says `error: integrity check refused vault data … the host served corrupt or substituted content: do not trust this source`, and a pull says `error: missing file — object obj-cas-imm-… is not in the local store` with a hint to run `sgit check fsck`. **Neither hint applies.** The vault is fine; your client cannot read its new ids. Do not run `vault move` or `fsck --repair`. Run `sgit update` and retry.

## 4. Known issues in 0.20.0

All fixed for the next release (0.21.0, not yet on PyPI). Until then:

- **Known issue in 0.20.0, fixed for the next release.** After `sgit pull --accept-rewind` the clone keeps the commits the rewind removed, and `status` then suggests `sgit push`, which would put them back. **Do not push.** Run `sgit history reset obj-cas-imm-<new head>` with the full id of the new head (from `sgit history log` in a fresh clone, or from the owner); `sgit status` then says `in sync with remote`. If you had unpushed work of your own, copy it out first and commit it again after the reset.
- **Known issue in 0.20.0, fixed for the next release.** A clone made before a new teammate joined refuses that teammate's signed commits as `no-key`, and removing the policy does not free it: an older clone even switches the policy back on for everyone when it pulls. **Do not turn `signatures-required` on for a vault with more than one writer until 0.21.0.** If a clone is stuck, copy out any unpushed work and clone the vault again.
- `sgit history reset` and `sgit history show` need the full `obj-cas-imm-…` id; the 12-character one `history log` prints is not accepted. Prefix it with `obj-cas-imm-`.
- A clone without an access token may warn that it could not refresh the branch index (`HTTP 401`). Harmless: the pull still works.

## 5. If you are the vault owner

Raise a vault only once every agent that writes to it is on 0.19.0 or newer: an older agent fails on a raised vault with Message 3, not with an update message. Then:

```
$ sgit vault format --set 2 --min-client 0.19.0
```

0.20.0 prints a note saying exactly this when you raise a vault. New objects get 128-bit ids, old ones stay, no move. [History integrity](history-integrity.md) has the rest: the gate, signatures, rewinds and the checklist.

## 6. If you want the detail

- [History integrity](history-integrity.md): the format gate, verifying signatures, rewinds, and who can open a raised vault.
- [Release notes: sgit-ai 0.20.0 (includes 0.19.0)](../updates/index.md#sgit-ai-0-20-0).
- [Agents sharing one vault](agents-sharing-one-vault.md): the loop for a team on one vault.


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/docs/update-to-0-20-0.html)*
