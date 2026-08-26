# SG/Vault & the vault platform — sgit.ai

> The official working documentation for the SGraph vault platform: the SG/Vault browser app, the SG/Send zero-knowledge API, and vault apps.

*Source: <https://sgit.ai/vault/index.html> · site v0.2.45 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / SG/Vault

# SG/Vault & the vault platform

This section is — for now — the official documentation for the SGraph vault platform: the **SG/Vault** browser app, the **SG/Send** zero-knowledge API, and **vault apps** — websites and applications that live *inside* encrypted vaults. Product background lives at [sgraph.ai](https://sgraph.ai); the working documentation lives here.

## What SG/Vault is

SG/Vault is the browser client for the same vaults sgit manages from the terminal. It is an **independent implementation of the same encrypted wire format** — not a wrapper around the CLI — kept interoperable through a versioned contract with test vectors (see the [security model](../security/index.md#interop)).

You open a vault by its key, carried in the URL *fragment* (the part after `#`):

```
https://vault.sgraph.ai/en-gb/#<vault-key>
# the fragment never leaves the browser — it is not sent in the HTTP request,
# so the server serves the app without ever seeing the key
```

From there you get a file browser over the decrypted vault — history, branches, editing — and, if the vault contains an app, **App Mode**: the vault boots straight into its own user interface.

## The three pieces

| Piece | What it is | Where it runs |
|---|---|---|
| **sgit** | The CLI — git workflows over encrypted vaults | Your terminal, your agents' sessions |
| **SG/Vault** | The browser client — browse, edit, review, App Mode | Any browser; all crypto via Web Crypto, client-side |
| **SG/Send** | The transfer API — stores ciphertext under opaque IDs | The server; the only piece that never sees plaintext |

## Vault apps: the app *is* the vault

A vault can contain an `index.html` plus an `app.json`. When the vault opens, the app launches — full-screen, talking to the vault through a runtime bridge, with the encrypted blob serving as both the storage and the distribution mechanism. Sharing the vault link *is* deploying the app.

**You are looking at one.** This entire website is a vault app: generated pages, shared assets loaded through the bridge, deployed by `sgit push`. The [admin section](../admin/index.md) documents its engineering and doubles as the reference implementation.

## Three on-ramps

| You want to… | Use | Code needed |
|---|---|---|
| Publish documents, galleries, hub pages | [Markdown + `_page.json`](content-authoring.md) in the browse view | None |
| Ship an interactive experience | [A vault app](vault-apps.md) on the [`window.sg` bridge](sg-bridge.md) | HTML/JS |
| Automate, script, collaborate, back up | The [sgit CLI](../docs/index.md), plus [git side-by-side](git-and-vaults.md) and [static hosting](static-hosting.md) | A terminal |

[Sub-vaults](sub-vaults.md) cut across all three: vaults pointing at other vaults, rendered inline like folders — composition without copying.

## In this section

## Publish

[Content without codeMarkdown + _page.json layouts, themes, print](content-authoring.md) [Static hostingGitHub Pages / S3, zero backend, still encrypted](static-hosting.md)

## Build

[Building vault appsThe project shape, app.json, and the authoring contract](vault-apps.md) [The window.sg bridgeThe runtime API, permissions, and the sovereignty rail](sg-bridge.md)

## Compose & integrate

[Sub-vaultsVaults inside vaults — links, embeds, extract & seed](sub-vaults.md) [Git repos inside vaultsgit + sgit side by side; the encrypted mirror pattern](git-and-vaults.md)

[Building vault apps →](vault-apps.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/vault/index.html)*
