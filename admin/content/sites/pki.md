---
title: pki.sgit.ai
domain: pki.sgit.ai
tagline: A key registry for agents, designed from a documented failure
summary: Good public key repositories existed and were destroyed. This site is the 2019 keyserver catastrophe, the four registry rules it produces, and the build order — all published before the registry exists, so the commitments are checkable against whatever eventually ships.
category: Security & infrastructure
thesis: Good public key repositories existed, and were destroyed
observed: 2026-08-19
seen_version: v0.1.2
repo: SGit-AI__Website__PKI
hero: pki-home.webp
tags: pki, registry, history
---

## Publishing the design before the implementation

The premise is unusual and worth stating plainly: **this site describes a registry that does not exist.** That is deliberate. Publishing the rules now is cheap; claiming them afterwards is impossible. If something ships that breaks one of them, the site is the evidence.

!shot pki-home.webp | images/ | The home page. The claim is historical before it is technical.

## The failure it is designed from

In 2019 the global keyserver network was flooded with garbage signatures until importing a poisoned certificate would break your installation. Its own maintainer called it **unsalvageable**. The cause was not a bug — it was a design goal stated at the outset.

That design goal was **append-only**. And append-only is a pattern this project relies on in five places, which is exactly why a shrug would not do. The site's resolution is a precise one, and it is the most useful idea on the page:

- **Append-only, owner-writes** — only the record's owner may write to it. Every entry is attributable because the owner signed it; a record grows slowly, in one hand; something can be withdrawn by a signed append that supersedes it.
- **Append-only, anyone-writes** — anybody may grow anybody's record, without limit, and garbage is indistinguishable from signal. Nothing can ever be withdrawn, by design. This destroyed the network.

The rule to carry forward is **not** "append-only". It is *the writer owns what it writes*.

## The four rules

Each one turns around a specific property the 2019 attack abused:

!shot pki-rules.webp | images/ | Each rule states the property it turns around, so it can be checked rather than trusted.

1. **Only the owner writes to their own record** — turns around *anyone may append to anybody's certificate*.
2. **Revocation is a signed append, not a deletion** — signed by the key being revoked, so it is self-authenticating, the record stays append-only, and what a key said before revocation stays checkable.
3. **Records are size-bounded** — one poisoned key reached about 150,000 signatures because certificates had no limit. The bound is a stated parameter, with the honest cost that it will one day reject a legitimate record.
4. **Every entry is signed** — so nothing anonymous can accumulate.

Rule 2 is the one to notice. Deletion and append-only are usually treated as incompatible; making revocation a *signed statement appended by the revoked key itself* resolves the contradiction without weakening either property.

!shot pki-failure.webp | images/ | The history, in five minutes — sourced rather than summarised from memory.

## Why it is relevant here

sgit's own [PKI](/docs/pki.html) ships keypairs today — RSA-OAEP 4096 for encryption, ECDSA P-256 for signing — and has **no revocation, no directory and no web of trust**, which [the limitations page](/docs/limitations.html) says plainly. This site is the design work for what a directory would have to be before it could responsibly exist.

The connection to [append lanes](/api/append-lanes.html) is direct: a lane is append-only and *owner-configured* — a sender writes only to a lane the owner registered for them. That is rule 1, already shipped, in a different corner of the system.

## Sections

- **The failure** — 2019, with sources
- **The rules** — four commitments, each tied to the property it turns around
- **Mandate** — what a registry would be for
- **Build order** — private before public, and why
