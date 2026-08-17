# Publishing a vault: the method — sgit.ai

> The seven steps behind every vault published here, written for another agent to follow: classify the credential before it touches anything, derive rather than refuse, audit with the read key, derive the facts, capture evidence by driving the real product, write the page, and record what outlives it — plus the mistakes that produced each rule.

*Source: <https://sgit.ai/demos/vaults/publishing.html> · site v0.2.28 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../index.md) / [Vaults](index.md) / Publishing a vault

# Publishing a vault: the method

Every vault in this section went through the same seven steps. This page is that method written down so another site — or another agent — can follow it. It is deliberately specific: the commands are real, the tools are in this repo, and the rules are the ones learned by nearly getting them wrong.

**Who this is for.** An agent maintaining a site that publishes vaults. Read the [markdown twin](publishing.md) if you are one. The tooling referenced lives in `admin/build/` of the sgit.ai repository and is small enough to copy rather than depend on.

## The two rules everything else serves

| Rule | Why it is absolute |
|---|---|
| **Read keys yes, vault keys never** | A read key is a capability handed out on purpose and cannot become write access. A vault key is read *and* write; publishing one hands the vault to anybody |
| **Audit before the key, not after** | Revocation is not retroactive. Anyone who fetches the objects keeps them, so an audit that happens after publication has not happened |

## 1 · Classify the credential before it touches anything

Do this first, before the credential is pasted into a page, a script or a commit. Credentials arrive mislabelled — it has happened three times here, each time a vault key described as a read key.

```
python3 admin/build/check_credential.py '<credential>'
# exit 0 → read-only, safe to publish
# exit 1 → write credential (or unrecognised) — stop
```

It classifies two ways, because the problem has two eras: by **prefix** for vaults new enough to emit one, and by **shape** for everything older — a read key is 64 hex characters, and anything else before the colon is a passphrase, which means write.

## 2 · If it is a vault key, derive rather than refuse

A vault key does not block publication; it changes what you publish. Store it where the repository cannot commit it, then derive:

```
# the gitignored tier — the release tripwire then scans every tracked file for it
printf '%s' "$VAULT_KEY" > .sg_vault/local/demo-keys/<name>-vault-key

python3 - <<'PY'
from sgit_ai.crypto.Vault__Crypto import Vault__Crypto
c = Vault__Crypto()
pw, vault_id = c.parse_vault_key(open('.sg_vault/local/demo-keys/<name>-vault-key').read().strip())
print(c.derive_keys(pw, vault_id)['read_key'])     # publish only this
PY
```

The derivation is one-way: a published read key cannot be turned back into the vault key. Never print the write key; never let the vault key reach a tracked file.

## 3 · Audit with the read key, across every file

Open the vault with the *read* key — the credential your readers will have — and scan every text file. Look for: the vault's own key (this has really happened, and forced a republish), API keys, tokens and `delete_auth` values, private-key blocks, personal data, and operational bookkeeping under `.vault/`.

**Ruling hits out is the work.** Scanners produce false positives and that is normal: a phone-number pattern matching `0123456789` inside a minified library; an `sk-test-…` string that turns out to be a fixture in a test asserting a leaked key *is* caught. Read every hit. Publish the interesting ones — a finding explained is worth more than a clean sheet asserted.

## 4 · Derive the facts rather than describing them

```
python3 admin/build/catalogue_derive.py <vault_id> <read_key>
```

File count, size, commit depth, HEAD, top-level layout, file types, app entry points and browser-renderability — all from the read key, no token and no clone. A human supplies only what a human knows: what it is for, and whether it is production or a sketch.

## 5 · Capture evidence by driving the real product

Screenshots should be of the actual vault, produced by a script that opens it with the published read key and performs the navigation being described. Mock-ups age into lies; a capture script re-runs.

```
node admin/build/capture_shots.mjs --vault <slug>
```

Each shot declares a surface (the app, or the vault browser), the steps, and the crop. Steps can click in the app frame, drive shadow-DOM controls, type into the debug REPL, expand folders or switch views. Store the images beside the page — `demos/vaults/<slug>/images/` — so a vault's folder is self-contained.

## 6 · Write the page: describe, then show, then admit

| Section | What goes in it |
|---|---|
| Lead + why this one | What the vault is, and the one thing it demonstrates that others do not |
| The credential, in the open | The read key, a CLI command, and a link that opens it in the official UI. Say plainly that it grants read and only read |
| Live embed | Both surfaces, opened over the embed protocol so the key never enters a URL or the frame's storage |
| Walkthrough rows | Alternating prose and screenshot, one row per non-obvious thing. This is where a reader learns what a live embed cannot tell them |
| What it demonstrates | A feature table naming the mechanism, not the marketing |
| **The audit, honestly** | What was scanned, what was found, and what it means. Findings included |
| Derived facts | Step 4's output, with the tool named so it can be re-run |

## 7 · Record the things that outlive the page

Per entry: the **shape** (the workflow it resembles, not its domain), the **evidence status** (production, demonstration, or sketch), whether it is a copy or a live reference, and the **write-key status** — escrowed or lost. A vault whose write key is lost is frozen: readable forever, never correctable. Say so where a reader will see it.

## What we got wrong, so you do not have to

| Mistake | The rule that came out of it |
|---|---|
| A vault published its own write credential inside its content | **Republish, don't retrofit.** A sanitised copy into a fresh vault also sheds the history you cannot publish |
| A vault key submitted as a read key, three times | Classification is a check, not a habit — step 1 |
| A test reported a refusal that was really a truncated clone | Re-run before recording. A result you cannot reproduce is not evidence |
| Our own tripwire banned the string we needed in order to teach people to recognise it | Make the rule *precise*, not stricter: fire on the prefix plus a credential character, so documentation can name it |
| A read key was published in front of a vault carrying an LLM config | Check, do not assume: we attempted to unseal it with the published read key, and AES-GCM refused. State the result either way |

The best statement of the vault-side rules is not ours: the [Risk Graph Explorer](risk-graph-explorer/index.md) carries a `PUBLIC.md` whose three build-enforced rules — nothing private committed, no write token, **no metered capability** — are the version to copy if you are building a vault intended for publication.

## The tools, in one list

| Tool | Does |
|---|---|
| `admin/build/check_credential.py` | Classifies a credential; exit code says publish or stop |
| `admin/build/catalogue_derive.py` | Read key → the facts, read-only and no token |
| `admin/build/capture_shots.mjs` | Drives the live vault and crops evidence screenshots |
| `admin/build/validate.js` | The release gate, including the key-leak tripwire |
| `admin/build/compare_tests.py` | Executes the claims that can be executed, with dates |


---

*[Site index for agents](../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/publishing.html)*
