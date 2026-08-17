# Risk Mandate — a published vault

> A working application built and delivered as a vault: 124 files, 98 commits, eight entry points, pinned releases, offline capable — and it calls an LLM without ever holding the API key, which is sealed under the vault key.

*Source: <https://sgit.ai/demos/vaults/risk-mandate/index.html> · site v0.2.27 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../index.md) / Risk Mandate

# Risk Mandate

A field demo built to be handed to a stranger on an iPad — and, underneath it, the most complete software project published here: 124 files, 98 commits, eight entry points, a test suite, build tooling and pinned releases, all inside one encrypted vault.

**Why this one matters.** It answers the question the other demos leave open: *can you actually build something real in a vault?* This is a working application with a release history, developed in the vault, delivered by the vault, and running offline once cached. It also does the thing that is hardest to do safely — **it uses an LLM without ever holding the API key**.

**Open it yourself — the key is the whole credential.**
 Read key: `sgit_rk1_a702fba803faac4369eb5d5a320b4dfa017af62bd2425fb298aac4b99e95c0ae:4zf6pf2z`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_rk1_a702fba803faac4369eb5d5a320b4dfa017af62bd2425fb298aac4b99e95c0ae%3A4zf6pf2z) · From the CLI: `sgit clone sgit_rk1_a702fba803faac4369eb5d5a320b4dfa017af62bd2425fb298aac4b99e95c0ae:4zf6pf2z`
Published deliberately, and **derived** — this read key is a one-way derivation of the vault key, which stays with its owner. It grants read, and only read.

## See it live, here

Both surfaces open automatically below. You can also [**open the app in its own window ↗**](https://dev.vault.sgraph.ai/#sgit_rk1_a702fba803faac4369eb5d5a320b4dfa017af62bd2425fb298aac4b99e95c0ae%3A4zf6pf2z) — it is more fun full size.

## What is going on here, step by step

Three things this vault does that the others do not. Every screenshot is of this vault, driven by a script holding nothing but the published read key.

the app

### A real application, delivered as a vault

This is **Risk Mandate**, a field demo built to be handed to someone on an iPad: pick a scenario, answer eight questions, and a risk register assembles beside you — readable as an operator, a CISO or a board.

It is one `index.html` with everything inlined, and it opens straight from the vault. Note the chrome: a **release selector** ("Live (latest)"), a sealed-secret badge, and **Read-only** — you are looking at a published build, not a preview.

The line under the button is the part worth reading twice: *"Nothing leaves this device."* On the stand it runs with the network off — one cached load, then flight mode all day.

The app as it opens from the published read key: scenarios, presets, and a version chip.

the privilege claim

### It uses an LLM. It never holds the API key.

The whole argument of this vault is in its `app.json`. It grants the app `llm: chat, models, usage, listen` — and `fs.write` over `field/workspace/` and nothing else.

What is *not* granted is the credential. `.vault/llm/config.json` carries `keySealed: {iv, ct}` — the OpenRouter key encrypted under the vault key. The host decrypts it and makes the outbound call; the frame is handed a result, never a secret. Opening this vault with the published read key, that field is ciphertext we cannot decrypt — which is the point, and we checked.

In the [privilege vocabulary](../../../compare/index.md): the app gets `ops:llm-chat` without ever getting `bearer` of the key. That distinction is usually impossible to express, let alone enforce.

app.json: LLM use granted, the key withheld, and write scoped to one folder.

version control, seriously

### Ninety-eight commits, and releases pinned to them

This is not a document that happens to live in a vault — it is a software project developed in one. **98 commits**, a test suite, build tooling, and `.vault/releases.json` pinning named releases (`v0.15.5`, `v0.10.3`, `v0.7.7`…) to specific commit ids, which is what the release selector in the app chrome is reading.

Its build script is the detail we enjoyed most: `tools/build.mjs` fails the build on any declarative external reference *and* on any credential-shaped string. They arrived at the same tripwire this site runs on its own releases, independently, for the same reason.

The SGit view: 98 commits of a real project, read with a published read key.

## What this vault demonstrates

| Feature | How this vault uses it |
|---|---|
| **AI without the credential** | Sealed OpenRouter key in `.vault/llm/config.json`; the host decrypts and calls, the app frame receives results only. Read-key holders — including us — see ciphertext in that field |
| **Scoped permissions, two kinds** | `llm` capabilities enumerated (chat, models, usage, listen) and `fs.write` limited to `field/workspace/` |
| Eight entry points | `index.html`, plus a board, a takeaway page, talking points, a build-history page and three proofs-of-concept — one vault, many front doors |
| Pinned releases | `.vault/releases.json` maps names to commit ids; the app chrome offers them as a live selector |
| Offline by design | One cached load, then it runs with the network off — the demo survives conference wifi |
| A build that enforces the contract | `tools/build.mjs` exits non-zero on declarative external references *and* on credential-shaped strings — their own version of this site's release tripwire |
| Shareable results without a server | `takeaway.html` rebuilds a saved register from the link alone |

## The audit, honestly

Audited independently before this key was published, across all 124 files. **Clean:** no credentials, no personal data, and the vault's own key does not appear in its content — the failure that forced a republish in [an earlier case](../strategy-maps/index.md).

Two findings worth publishing because they are the *good* kind. The OpenRouter credential is present but **sealed**: encrypted under the vault key, so a read-key holder gets ciphertext. And the one match our secret scanner produced was `sk-test-abcdefghijklmnop` in `tests/suites/40-llm.mjs` — a deliberately fake key in a test that asserts a reachable API key *is caught*. A scanner hit that turns out to be a security test is a good sign about a codebase.

As always: revocation is not retroactive. Anyone who fetches these objects keeps them.

## Derived facts

124 files · 1.9 MB · 98 commits · eight app entries · last updated 2026-08-06 — derived from the read key alone by `admin/build/catalogue_derive.py`, the same derivation that populates [the catalogue](../../../catalogue/index.md).


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/risk-mandate/index.html)*
