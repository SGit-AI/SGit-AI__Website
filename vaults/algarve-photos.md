# Algarve · May 2026 — a published vault

> A travel diary as a vault: twenty photographs in three sizes, an eight-chapter narrative and an auto-opening gallery app — 29 MB of ciphertext opened by one published read key, with its pre-publication audit finding stated on the page.

*Source: <https://sgit.ai/vaults/algarve-photos.html> · site v0.2.21 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Vaults](index.md) / Algarve · May 2026

# Algarve · May 2026

A travel diary as a vault: twenty photographs in three sizes, an eight-chapter narrative, and a gallery app that opens automatically.

**Open it yourself — the key is the whole credential.**
 Read key: `sgit_rk1_0a0f34839d737eef0f8f66e5236990b1f397af064763e3f71dca2717015f9d15:3d04e6b9ca98`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_rk1_0a0f34839d737eef0f8f66e5236990b1f397af064763e3f71dca2717015f9d15%3A3d04e6b9ca98) · From the CLI: `sgit clone sgit_rk1_0a0f34839d737eef0f8f66e5236990b1f397af064763e3f71dca2717015f9d15:3d04e6b9ca98`
Published deliberately. It grants read, and only read — a write attempt is refused by the server’s write gate (the **R1 W0** badge you will see in the chrome).

## See it live, here

## What this vault demonstrates

| Feature | How this vault uses it |
|---|---|
| Real binary payload | 60 WebP photographs in three sizes (originals ≈29 MB total, web ≈1600px, thumbnails) — every byte stored and served as ciphertext |
| Auto-opening gallery app | `app.json` sets `auto_open` with a minimal HUD; the app is an editorial photo story with chapters and a lightbox, driven by `gallery.json` |
| Content + narrative | `NARRATIVE.md` carries the written week; `gallery.json` carries per-photo titles, captions, chapters — edit the JSON, push, and the gallery updates |
| Deep history | 36 commits of organising, captioning and re-cutting — open the SGIT view above and read the story of the story |
| Owner secrets done right | `.vault/owner/readonly-tokens.json` decrypts to *further ciphertext* — owner bookkeeping is double-encrypted under a key the read key cannot reach |

## The audit, honestly

Every vault gets an audit before its read key is published here, and this one has a finding worth stating plainly: the server-side bookkeeping file for a public preview (`.vault/owner/public-previews/…`) carries a live `delete_auth` token, readable by anyone holding this read key. Its scope is narrow — it permits deleting or replacing that one *public preview*, not writing to the vault, whose write gate remains closed — and the owner has been advised to rotate it. It stays on this page because the finding class is the lesson: bookkeeping written into vault content travels with the read key forever. The newer pattern — owner secrets double-encrypted, as the row above shows this same vault doing for its read-only tokens — is the fix.

## What this shape is for

Photo albums, trip diaries, family archives, portfolio galleries — anything where the pictures should not sit plaintext on someone else’s server, but a single shareable key should open the whole experience, chapters and captions included. This is the first of several galleries in [the catalogue’s](../catalogue/index.md) awaiting list.

## Derived facts

71 files · 29 MB · 36 commits · app entry `index.html` · derived from the read key alone by `admin/build/catalogue_derive.py` — the same derivation that populates [the catalogue](../catalogue/index.md), where this vault also has an entry.


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/vaults/algarve-photos.html)*
