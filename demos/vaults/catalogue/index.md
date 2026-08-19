# The Vault Catalogue — a published vault

> The index of published vaults, itself a vault, listed in itself — a submission queue where an entry costs a read key and one line, with published to-do lists and first-class write-key status.

*Source: <https://sgit.ai/demos/vaults/catalogue/index.html> · site v0.2.35 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../../../index.md) / The Vault Catalogue

# The Vault Catalogue

The index of published vaults — itself a vault, published with a read key, and listed in itself.

**Open it yourself — the key is the whole credential.**
 Read key: `sgit_rk1_fd71e4bde7232498e43a5da869b1501260d9d403031b20af87b5bc801bdf6280:kc67yhgw`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_rk1_fd71e4bde7232498e43a5da869b1501260d9d403031b20af87b5bc801bdf6280%3Akc67yhgw) · From the CLI: `sgit clone sgit_rk1_fd71e4bde7232498e43a5da869b1501260d9d403031b20af87b5bc801bdf6280:kc67yhgw`
Published deliberately. It grants read, and only read — a write attempt is refused by the server’s write gate (the **R1 W0** badge you will see in the chrome).

## See it live, here

## What this vault demonstrates

| Feature | How this vault uses it |
|---|---|
| Recursion, usefully | an index of published vaults that is itself a published vault, listed in itself — [rendered live at /catalogue/](../../../catalogue/index.md) |
| Submission queue | an entry costs a read key and one line; everything else is derived by an agent opening the vault |
| Published to-do lists | `todo/awaiting-read-key.md` and `todo/awaiting-processing.md` are public, because a named gap gets filled |
| First-class write-key status | every entry records whether the write key is escrowed or lost, because a frozen vault can never be corrected |

## What this shape is for

Machine-and-human-readable registries that update by pushing to a vault rather than deploying a site. The schema here is deliberately the first instance of what a vault hub would need.

## Derived facts

9 files · 11 KB · 2 commits · markdown, no app · derived from the read key alone by `admin/build/catalogue_derive.py` — the same derivation that populates [the catalogue](../../../catalogue/index.md), where this vault also has an entry.


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/catalogue/index.html)*
