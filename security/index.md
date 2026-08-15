# Security model — sgit

> sgit's zero-knowledge security model, precisely stated: the crypto stack, what the server can and cannot see, key strength, and the open security process.

*Source: <https://sgit.ai/security/index.html> · site v0.2.1 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

# Security model

Zero knowledge, precisely stated: every file is encrypted on your machine before upload, keys are derived locally from your vault key, and the server stores ciphertext under opaque identifiers. This page tells you exactly what that means — including what the server *can* see.

## What the server sees — and never sees

| The server never sees | The server does see |
|---|---|
| File contents (encrypted client-side, AES-256-GCM) | The vault ID (an opaque random identifier) |
| Filenames and folder structure | Encrypted object sizes |
| Commit messages and branch names | Timing of reads and writes |
| Your vault key or any derived key | Approximate activity volume (object counts) |

We state the right-hand column deliberately. Traffic analysis of sizes and timing is a real (if narrow) channel, and pretending otherwise would be marketing, not security.

## The crypto stack

| Layer | Construction |
|---|---|
| Content encryption | AES-256-GCM, 12-byte IV, 16-byte tag — byte-compatible with the browser's Web Crypto API |
| Key derivation from the vault key | PBKDF2-HMAC-SHA256, 600,000 iterations, distinct per-vault salts for read and write keys |
| Purpose-specific keys | HKDF-SHA256 — per-file keys and a structure key, one-way derived from the read key |
| Server-side identifiers | HMAC-SHA256-derived opaque IDs — the server addresses files it cannot name |
| Object identity | Content-addressed: `obj-cas-imm-<sha256-prefix>` over ciphertext, enabling dedup without plaintext knowledge |

One precision note, because precision beats marketing: the key hierarchy derives a *structure key* (one-way from the read key) designed to separate access to vault metadata from access to file contents. Today, vault objects are encrypted under the read key — activating the structure-key split across structural objects is an in-progress, reviewed design change, and this page will say so when it lands, not before.

## Key strength

Vault keys are generated, not chosen. A generated passphrase is 24 characters over a 36-symbol alphabet — about **124 bits of entropy** (3624 ≈ 2124), far beyond brute-force reach — before key derivation adds 600,000 rounds of PBKDF2-SHA256 on top. The key never travels to the server: it is the address, the credential, and the root of the encryption hierarchy in one string, and it stays on your machines.

**Consequence you should want:** there is no password reset. If you lose the vault key, nobody — including us — can recover the contents. Keep it in a password manager, and use `sgit vault backup` for belt-and-braces.

## Two implementations, one wire format

The sgit CLI and the SG/Vault browser client are independent implementations of the same encrypted wire format, kept interoperable through a versioned contract with test vectors. Every crypto operation must produce byte-for-byte identical output to the Web Crypto API given the same inputs — that requirement is enforced with mandatory test vectors, and it means a second, independent codebase continuously exercises the same format. (More on the browser side at [sgraph.ai](https://sgraph.ai).)

## Secrets safety by default

sgit is not a secrets manager, and it actively refuses to become an accidental one: files like `.env*`, `.netrc`, `.pgpass`, `.git-credentials` and private key files (`id_rsa`, …) are *always* excluded from commits, so a stray credential can't get swept into a vault snapshot.

## Open security process

- Open source under Apache-2.0, with a deliberately tiny dependency surface: two runtime dependencies.
- ~4,000 tests including mutation testing in CI and integration tests against a real server — no mocks.
- An internal security review series (twelve findings, each individually worked through and debriefed — covering key residency, IV determinism trade-offs, logging hygiene, and more) is being prepared for publication on this page.
- Found something? Report it via [GitHub](https://github.com/SGit-AI/SGit-AI__CLI/issues) — security reports get priority.
- **Key exposed?** [The rotation runbook](../case-studies/exposed-vault-key.md) — including a worked case study of the day this site's own vault key leaked, and what it cost to fix.

**Honesty note:** sgit is in beta — it powers production workflows daily, and the cryptography is conservative and standard (AES-GCM, PBKDF2, HKDF — nothing exotic). Still: read [when NOT to use sgit](../docs/limitations.md) before trusting it with anything critical.


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/security/index.html)*
