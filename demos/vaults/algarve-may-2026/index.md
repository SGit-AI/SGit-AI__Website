# Algarve · May 2026 — a published vault

> A travel diary as a vault: twenty photographs in three sizes, an eight-chapter narrative and an auto-opening gallery app — 29 MB of ciphertext opened by one published read key, with its pre-publication audit finding stated on the page.

*Source: <https://sgit.ai/demos/vaults/algarve-may-2026/index.html> · site v0.2.54 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../../../index.md) / Algarve · May 2026

# Algarve · May 2026

A travel diary as a vault: twenty photographs in three sizes, an eight-chapter narrative, and a gallery app that opens automatically.

**Open it yourself — the key is the whole credential.**
 Read key: `sgit_rk1_0a0f34839d737eef0f8f66e5236990b1f397af064763e3f71dca2717015f9d15:3d04e6b9ca98`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_rk1_0a0f34839d737eef0f8f66e5236990b1f397af064763e3f71dca2717015f9d15%3A3d04e6b9ca98) · From the CLI: `sgit clone sgit_rk1_0a0f34839d737eef0f8f66e5236990b1f397af064763e3f71dca2717015f9d15:3d04e6b9ca98`
Published deliberately. It grants read, and only read — a write attempt is refused by the server’s write gate (the **R1 W0** badge you will see in the chrome).

## See it live, here

Both surfaces open automatically below. You can also [**open the gallery app in its own window ↗**](https://dev.vault.sgraph.ai/#sgit_rk1_0a0f34839d737eef0f8f66e5236990b1f397af064763e3f71dca2717015f9d15%3A3d04e6b9ca98) — the read key travels in the URL fragment, which the vault UI accepts directly.

## What this vault demonstrates

| Feature | How this vault uses it |
|---|---|
| Real binary payload | 60 WebP photographs in three sizes (originals ≈29 MB total, web ≈1600px, thumbnails) — every byte stored and served as ciphertext |
| Auto-opening gallery app | `app.json` sets `auto_open` with a minimal HUD; the app is an editorial photo story with chapters and a lightbox, driven by `gallery.json` |
| Content + narrative | `NARRATIVE.md` carries the written week; `gallery.json` carries per-photo titles, captions, chapters — edit the JSON, push, and the gallery updates |
| Deep history | 36 commits of organising, captioning and re-cutting — open the SGIT view above and read the story of the story |
| Owner secrets done right | `.vault/owner/readonly-tokens.json` decrypts to *further ciphertext* — owner bookkeeping is double-encrypted under a key the read key cannot reach |

## What is going on here, step by step

The two embeds above are the real product, which makes them easy to scroll past without noticing what is unusual. Each row below points at one thing and says why it matters. Every screenshot is of this vault, driven by a script that opens it with the **published read key** and nothing else — the same credential printed at the top of this page.

the app itself

### The app is real HTML, not a viewer

The gallery is the vault's own `index.html` — an editorial layout with chapters, pull quotes and photo rows, written as ordinary HTML and CSS. Nothing renders it into a fixed "photo album" template: whatever the author wrote is what runs.

Each photograph here arrived as ciphertext, was decrypted in the browser, and was handed to the page as a `blob:` URL. The server never saw a picture — it served opaque bytes and has no idea this is a gallery.

A chapter row: two decrypted photographs, laid out by the vault’s own CSS.

interaction

### Click a photo and the app takes over

Because the app is real HTML, it can behave like any web app. Clicking a photograph opens the gallery's own lightbox: a larger image, the caption and chapter from `gallery.json`, and arrows to move through all twenty.

This is the part that surprises people most — an encrypted store is usually a download-and-open experience. Here the interaction is authored *inside* the vault and the reader never leaves the page.

The lightbox: caption, chapter, position (1 / 20), and prev/next arrows.

watch it decrypt

### A pane that shows the decryption happening

The app frame ships with a debug pane, and its **Vault** tab is the timeline of the open: the vault unlocked, the file tree loaded, `app.json` found, the app iframe ready — each with the milliseconds it took.

Read the key line: the vault opens from a key that is shown truncated, and the file tree — *seventy files* — is built in the browser from encrypted directory objects. Filenames are encrypted too, so even the folder structure is something the client reconstructs rather than something the server reports.

The Vault tab: each step of the open, with timings.

the sg bridge

### And a console you can type into

The **REPL** tab is a small console over the `sg.*` bridge — the same API the app itself uses. `vfs.list` walks the decrypted tree, `vfs.read` prints a text file.

Note what the help text says about writing: `vfs.write` and `vfs.delete` are marked *writable vaults only*. This page's key is read-only, so those commands are refused — not hidden by the interface, but impossible, because no write capability exists anywhere in the chain.

vfs.list at the vault root, then inside /photos — typed live, answered from decrypted objects.

transparency

### The whole vault is browsable — including its source

The second surface on this page is the vault browser. It shows the real tree: `photos/originals/` with its twenty WebP files, the thumbnails and web-sized copies beside them, and the app's own files.

Open `index.html` and press **Source** and you are reading the gallery's code — the same 29.9 KB the app boots from. A published vault is transparent in a way a hosted gallery rarely is: the reader can inspect exactly what is running.

photos/originals expanded, with index.html open in source view.

version control

### And it is version control, not just storage

The **SGIT** tab is why this is sgit rather than a folder in the cloud. Every commit that built this gallery is here — thirty-six of them — with real object ids, dates and branch labels, and `tree` and `diff` links per commit.

This is the vault's history, read from the same encrypted objects, with the same read key. Nothing was re-uploaded to make it browsable: the history *is* the storage.

The SGit view: the commit history of the gallery, read-only.

**How these pictures were made.** They are not mock-ups and they are not hand-cropped. `admin/build/capture_shots.mjs` opens this vault in a real browser with the published read key, performs the navigation each row describes — scroll to a chapter, click a photograph, open the debug pane, switch to the REPL and type `vfs.list`, expand `photos/originals`, switch to the SGit view — and crops the result. Re-running it after the vault changes regenerates every image. The tool takes a read key, so it can document any published vault the same way.

## The audit, honestly

Every vault gets an audit before its read key is published here, and this one has a finding worth stating plainly: the server-side bookkeeping file for a public preview (`.vault/owner/public-previews/…`) carries a live `delete_auth` token, readable by anyone holding this read key. Its scope is narrow — it permits deleting or replacing that one *public preview*, not writing to the vault, whose write gate remains closed — and the owner has been advised to rotate it. It stays on this page because the finding class is the lesson: bookkeeping written into vault content travels with the read key forever. The newer pattern — owner secrets double-encrypted, as the row above shows this same vault doing for its read-only tokens — is the fix.

## What this shape is for

Photo albums, trip diaries, family archives, portfolio galleries — anything where the pictures should not sit plaintext on someone else’s server, but a single shareable key should open the whole experience, chapters and captions included. This is the first of several galleries in [the catalogue’s](../../../catalogue/index.md) awaiting list.

## Derived facts

71 files · 29 MB · 36 commits · app entry `index.html` · derived from the read key alone by `admin/build/catalogue_derive.py` — the same derivation that populates [the catalogue](../../../catalogue/index.md), where this vault also has an entry.


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/algarve-may-2026/index.html)*
