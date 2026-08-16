# The vault catalogue — sgit.ai

> An index of published vaults rendered live from a vault that indexes vaults, including itself. Each entry: a deliberately published read key, shape, evidence status, copy-or-reference semantics, and write-key status (known-and-escrowed or lost — a frozen vault can never be corrected). Submitting a vault costs a read key and one line; the rest is derived.

*Source: <https://sgit.ai/catalogue/index.html> · site v0.2.17 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / Catalogue

# The vault catalogue

An index of published vaults, rendered live from a vault that indexes vaults — including itself. Every entry carries a deliberately published read key, an honest evidence status, and its write-key status, because a vault whose write key is lost can never be corrected and a reader deserves to know.

**The design constraint, stated openly:** the bottleneck is one person with a backlog of vaults, so an entry costs **a read key and one line** — everything else (listing, sizes, commit count, whether an app is present) is derived by an agent opening the vault with the key it was just given. The two to-do queues are published in the catalogue itself: a named gap gets filled, an unnamed one does not. This page renders vault `kc67yhgw` directly — a push to it updates this page with no site deploy.

opening the catalogue…

Fetching the encrypted index…

### Vault debug [how this works →](../case-studies/live-vault-docs.md)

not open yet

what you are looking at

 Every row above is an encrypted object pulled from the SG/Send API and decrypted locally — click one to see what it actually contains. Objects whose id contains **-imm-** are content-addressed and therefore immutable, so they are cached permanently; the mutable **ref** is the one mutable object, so it is checked at most once per freshness window (120s) rather than once per page — inside the window, reading the docs makes no requests at all, and **check for new commit** forces one whenever you want it.

The **tree** objects are the reason a first visit reads more than one file: filenames are encrypted inside them, so building the navigation means reading every directory. That index is a pure function of the commit id, so it is memoised — after the first visit, an unchanged commit reads no tree objects at all. Nothing here is stored on sgit.ai.

[How this page works →](../case-studies/live-vault-docs.md) Architecture diagrams, the object model, the cache tiers, and how a page like this one reads a vault it holds only the read key to.


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/catalogue/index.html)*
