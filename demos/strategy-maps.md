# The Strategy in Seven Maps — a real document republished from a vault — sgit.ai demos

> The actual SG/Send strategy (eight Wardley Maps, published on LinkedIn in May 2026) served live from an encrypted vault with a published read key — plus the audit that found the original vault could NOT publish its key (its own write credential was inside its content) and the republish pattern that fixed it.

*Source: <https://sgit.ai/demos/strategy-maps.html> · site v0.2.50 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Demos](index.md) / The Strategy in Seven Maps

# A real strategy document, republished from a vault

This is not demo content. It is the actual SG/Send strategy — eight Wardley Maps with commentary, written by the founder, [published on LinkedIn](https://www.linkedin.com/feed/update/urn:li:ugcPost:7464691060775120896/) in May 2026 — served live below from an encrypted vault with a published read-only key. And the process of publishing it is itself a security lesson, so that is on this page too.

## The live embed

The vault's own app — the scrollable strategy essay with the eight maps, click-to-zoom included. Every byte, including the PNG maps, is fetched as ciphertext and decrypted here.

~30 encrypted objects (~900 KB, mostly the map PNGs) from `dev.send.sgraph.ai`, decrypted in your browser.

## Why this vault could not simply publish its read key

The original lives in a vault created in May 2026, before today's key practices. Asked "is it OK to share its read key?", we audited it — and the answer was **no**, for reasons worth publishing because they generalise:

| Finding | Why it blocks publishing the read key |
|---|---|
| **The vault's own write credential was inside its content.** A production briefing in the vault documented the clone command — including the vault's read-write token, verbatim. | Publishing the read key would hand every reader the *write* key. This is the general trap: a read key exposes everything ever committed, including documentation that casually quotes credentials. |
| **Server-side bookkeeping with live tokens.**`.vault/owner/public-previews/` held records containing `delete_auth` tokens — capabilities to delete the published previews. | A read key decrypts the whole tree, dot-folders included. Operational bookkeeping and publishable content were in the same trust boundary. |
| **Legacy low-entropy credential.** The vault's keys derive from a legacy dictionary-words-plus-digits token — a small keyspace by construction. | Even with the content clean, "public read, protected write" is only as strong as the write credential. This class of token is being retired for exactly this reason. |

**The fix is the pattern to copy:** republish, don't retrofit. The content was copied out, the credential quotes redacted (with a visible publication note in the affected file), the operational bookkeeping and test debris dropped, and the result committed to a *new* vault (`ookq4mn4`) with a full-entropy key that has never appeared anywhere. Only then was the read key derived and published:

```
# the audit, in one honest line: grep before you publish
$ grep -rniE "token|secret|key|delete_auth" . --include="*.md" --include="*.json"
# the republish
$ sgit init --existing .   # fresh vault, full-entropy key — saved to a password manager
$ sgit commit -m "republished, credentials redacted" && sgit push
$ sgit dev derive-keys '<vault-key>'
  read_key: 451c4c1e28fbb24a…   ← published below, in full, on purpose
```

```
vault id : ookq4mn4
endpoint : https://dev.send.sgraph.ai
read key : 451c4c1e28fbb24a7f350bb3f107b2c103d69ed363167029ef9c9000ff76c07b
```

The original vault is untouched and stays private. Its history — which contains the credential-bearing briefing — is not carried over: a republish is also how you shed a history you cannot publish.

## What this demo adds to the embed host

The [first demo](vault-app-embed.md) was built without image files. This app loads eight PNG maps by setting `img.src` to vault paths — which, inside a sandboxed frame, resolve against an opaque origin and fail. The embed host now does what the real SG/Vault host does: a `MutationObserver` intercepts vault-path images, reads the bytes over the bridge, and swaps in `blob:` URLs. The maps you see above each travelled as ciphertext.

| Shape | Evidence status | Copy or reference |
|---|---|---|
| Report / strategy microsite | **REAL** — a production artefact, published externally in May 2026; not authored for this demo | **Reference** — the embed reads vault `ookq4mn4` live; a push updates this page with no rebuild |

## Related

- [The first demo](vault-app-embed.md) — the walkthrough of the embed mechanism itself
- [The day we leaked our own vault key](../case-studies/exposed-vault-key.md) — the incident behind the audit habits used here
- [Briefing to the SG/Vault UI team](../briefs/briefing-sgvault-ui-embed.md) — the path to embedding the official UI instead of our minimal host

[← First demo](vault-app-embed.md)[All demos →](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/demos/strategy-maps.html)*
