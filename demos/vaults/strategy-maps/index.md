# Strategy Maps — a published vault

> The SG/Send strategy in seven Wardley maps plus the sgit positioning analysis — two app entry points in one encrypted vault, published after the audit that made a republish necessary.

*Source: <https://sgit.ai/demos/vaults/strategy-maps/index.html> · site v0.2.29 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../../../index.md) / Strategy Maps

# Strategy Maps

The SG/Send strategy in seven Wardley maps, plus the sgit positioning analysis as a second app in the same encrypted store.

**Open it yourself — the key is the whole credential.**
 Read key: `sgit_rk1_451c4c1e28fbb24a7f350bb3f107b2c103d69ed363167029ef9c9000ff76c07b:ookq4mn4`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_rk1_451c4c1e28fbb24a7f350bb3f107b2c103d69ed363167029ef9c9000ff76c07b%3Aookq4mn4) · From the CLI: `sgit clone sgit_rk1_451c4c1e28fbb24a7f350bb3f107b2c103d69ed363167029ef9c9000ff76c07b:ookq4mn4`
Published deliberately. It grants read, and only read — a write attempt is refused by the server’s write gate (the **R1 W0** badge you will see in the chrome).

## See it live, here

## What this vault demonstrates

| Feature | How this vault uses it |
|---|---|
| Two app entry points | `index.html` (the strategy essay, eight Wardley map PNGs) and `sgit-maps.html` (six inline-SVG maps) — one encrypted store, two front doors |
| Vault-path images | the essay’s PNGs travel as ciphertext and are swapped in as `blob:` URLs after decryption |
| Republish pattern | this vault is a sanitised republish: the original could not publish its key because a write credential was inside its content — [the audit is public](../../strategy-maps.md) |
| Cross-app links | the two apps link to each other and the links survive embedding |

## What this shape is for

Published analysis with real assets: strategy documents, briefs, decks. The two-entry-point trick means one vault can carry a family of related documents that share content, history and a single published key.

## Derived facts

33 files · 830 KB · 3 commits · app entries `index.html` and `sgit-maps.html` · derived from the read key alone by `admin/build/catalogue_derive.py` — the same derivation that populates [the catalogue](../../../catalogue/index.md), where this vault also has an entry.


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/strategy-maps/index.html)*
