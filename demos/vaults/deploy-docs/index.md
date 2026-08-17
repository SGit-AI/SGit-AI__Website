# Deploy Docs — a published vault

> The living deployment documentation for sgit.ai: markdown written by two Claude Code sessions, rendered live in the visitor’s browser, updated by an sgit push with no site deploy.

*Source: <https://sgit.ai/demos/vaults/deploy-docs/index.html> · site v0.2.26 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../../../index.md) / Deploy Docs

# Deploy Docs

The living deployment documentation for sgit.ai itself — written by two Claude Code sessions, rendered live on the /deploy page.

**Open it yourself — the key is the whole credential.**
 Read key: `sgit_rk1_8d01421290efc3fa03205eced0534335a06ae209d627555b3dde136b878e3de1:fyofmkvr`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_rk1_8d01421290efc3fa03205eced0534335a06ae209d627555b3dde136b878e3de1%3Afyofmkvr) · From the CLI: `sgit clone sgit_rk1_8d01421290efc3fa03205eced0534335a06ae209d627555b3dde136b878e3de1:fyofmkvr`
Published deliberately. It grants read, and only read — a write attempt is refused by the server’s write gate (the **R1 W0** badge you will see in the chrome).

## See it live, here

## What this vault demonstrates

| Feature | How this vault uses it |
|---|---|
| Live markdown rendering | [the /deploy page](../../../deploy/index.md) decrypts and renders this vault in the visitor’s browser — a push here updates that page with no site deploy |
| Freshness window | the mutable HEAD pointer is checked at most once per 120 s; everything else is content-addressed and cached forever |
| Two writers | written by two Claude Code sessions collaborating through the vault — the commit history shows the handoffs |
| Debug panel | the page’s vault panel shows every encrypted object arriving and what it decrypts to |

## What this shape is for

Documentation that updates without a deploy pipeline, from any writer who holds the vault key, to any reader who holds the read key. The natural shape for runbooks, guides and anything agents co-author.

## Derived facts

17 files · 25 KB · 2 commits · markdown, no app · derived from the read key alone by `admin/build/catalogue_derive.py` — the same derivation that populates [the catalogue](../../../catalogue/index.md), where this vault also has an entry.


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/deploy-docs/index.html)*
