# Field Notes — a published vault

> The minimum viable published vault: six studies with generative SVG art as a self-contained vault app, read over the sg.vfs bridge, opened by a single published read key.

*Source: <https://sgit.ai/demos/vaults/field-notes/index.html> · site v0.2.47 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../../../index.md) / Field Notes

# Field Notes

Six small studies — a note and a generative SVG drawing each — served as a self-contained vault app.

**Open it yourself — the key is the whole credential.**
 Read key: `sgit_rk1_2848993a68c02a33ea5582902c391901191e53680d35b36c0e76185d4107ad81:4bshby5n`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_rk1_2848993a68c02a33ea5582902c391901191e53680d35b36c0e76185d4107ad81%3A4bshby5n) · From the CLI: `sgit clone sgit_rk1_2848993a68c02a33ea5582902c391901191e53680d35b36c0e76185d4107ad81:4bshby5n`
Published deliberately. It grants read, and only read — a write attempt is refused by the server’s write gate (the **R1 W0** badge you will see in the chrome).

## See it live, here

## What this vault demonstrates

| Feature | How this vault uses it |
|---|---|
| Vault app (`app.json`) | one self-contained `index.html`, auto-opened; CSS and JS inlined per the authoring contract |
| `sg.vfs` bridge | the app reads `content.json` over the bridge at runtime — the status line in the app proves it |
| Generative SVG | the six drawings are code, not images — no binary assets to fetch |
| Published read key | the first vault created specifically to be published; the complete walkthrough is on [the embed demo page](../../vault-app-embed.md) |

## What this shape is for

The minimum viable published vault: content plus a small app, one key, no server that can read any of it. Use this shape for anything you would put on a small static site — except the host serves only ciphertext, and unpublishing is deleting one credential from a page rather than tearing down a site.

## Derived facts

4 files · 11 KB · 2 commits · app entry `index.html` · derived from the read key alone by `admin/build/catalogue_derive.py` — the same derivation that populates [the catalogue](../../../catalogue/index.md), where this vault also has an entry.


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/field-notes/index.html)*
