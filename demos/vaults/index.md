# Published vaults — sgit.ai

> Every vault whose read key sgit.ai has deliberately published: what each does, the features it uses, and the vault running live in the page. A read key is the complete credential — no account, no write capability.

*Source: <https://sgit.ai/demos/vaults/index.html> · site v0.2.26 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../index.md) / Vaults

# Published vaults

Every vault whose read key this site has deliberately published — with, for each one, a page describing what it does, the features it uses, what the shape is good for, and the vault itself running live inside the page. The keys below are the complete credential: no account, no token, and no write capability anywhere in them.

**Intake, since it nearly went wrong.** A credential submitted for publication here was once a **vault key** described as a read key — a legacy `passphrase:vault_id` form with no prefix to give it away. It was caught, only the derived read key was published, and nothing leaked; but the catch depended on somebody looking. Every submission now runs through `admin/build/check_credential.py` first, which refuses a write credential by **prefix** (`sgit_vk1_`, which new vaults emit) or, for anything older, by **shape** — a read key is 64 hex characters, and anything else before the colon is a passphrase. Prefixes are the better answer; the shape check covers the years of keys created before them.

**The two rules, applied to every row.** Read keys yes, vault keys never — a read key is a capability we hand out on purpose, and it cannot become write access. And every vault is audited before its key appears here, because content travels with the key forever; findings are published on the vault’s page, not filed away.

| Vault | Id | Shape | Contents | Published read key |  |
|---|---|---|---|---|---|
| [Field Notes](field-notes/index.md) | `4bshby5n` | application (vault app) | 4 files · 11 KB · 2 commits · app entry `index.html` | `sgit_rk1_2848993a68c02a33ea5582902c391901191e53680d35b36c0e76185d4107ad81:4bshby5n` | [open live ↗](https://dev.vault.sgraph.ai/#sgit_rk1_2848993a68c02a33ea5582902c391901191e53680d35b36c0e76185d4107ad81%3A4bshby5n) |
| [Strategy Maps](strategy-maps/index.md) | `ookq4mn4` | structured analysis (two apps, one vault) | 33 files · 830 KB · 3 commits · app entries `index.html` and `sgit-maps.html` | `sgit_rk1_451c4c1e28fbb24a7f350bb3f107b2c103d69ed363167029ef9c9000ff76c07b:ookq4mn4` | [open live ↗](https://dev.vault.sgraph.ai/#sgit_rk1_451c4c1e28fbb24a7f350bb3f107b2c103d69ed363167029ef9c9000ff76c07b%3Aookq4mn4) |
| [Deploy Docs](deploy-docs/index.md) | `fyofmkvr` | record-keeping (live markdown) | 17 files · 25 KB · 2 commits · markdown, no app | `sgit_rk1_8d01421290efc3fa03205eced0534335a06ae209d627555b3dde136b878e3de1:fyofmkvr` | [open live ↗](https://dev.vault.sgraph.ai/#sgit_rk1_8d01421290efc3fa03205eced0534335a06ae209d627555b3dde136b878e3de1%3Afyofmkvr) |
| [The Vault Catalogue](catalogue/index.md) | `kc67yhgw` | record-keeping (an index of vaults) | 9 files · 11 KB · 2 commits · markdown, no app | `sgit_rk1_fd71e4bde7232498e43a5da869b1501260d9d403031b20af87b5bc801bdf6280:kc67yhgw` | [open live ↗](https://dev.vault.sgraph.ai/#sgit_rk1_fd71e4bde7232498e43a5da869b1501260d9d403031b20af87b5bc801bdf6280%3Akc67yhgw) |
| [Algarve · May 2026](algarve-may-2026/index.md) | `3d04e6b9ca98` | gallery (photo story) | 71 files · 29 MB · 36 commits · app entry `index.html` | `sgit_rk1_0a0f34839d737eef0f8f66e5236990b1f397af064763e3f71dca2717015f9d15:3d04e6b9ca98` | [open live ↗](https://dev.vault.sgraph.ai/#sgit_rk1_0a0f34839d737eef0f8f66e5236990b1f397af064763e3f71dca2717015f9d15%3A3d04e6b9ca98) |
| [Supplement Stack](supplement-stack/index.md) | `r7zes477` | record-keeping (patient-held health record) | 23 files · 2.3 MB · 5 commits · app entry `index.html` | `sgit_rk1_047186b559528058c66d1792b7345639b1238cb95c166d1d5f5b65c59813c2ee:r7zes477` | [open live ↗](https://dev.vault.sgraph.ai/#sgit_rk1_047186b559528058c66d1792b7345639b1238cb95c166d1d5f5b65c59813c2ee%3Ar7zes477) |
| [Risk Mandate](risk-mandate/index.md) | `4zf6pf2z` | application (a software project in a vault) | 124 files · 1.9 MB · 98 commits · 8 app entries | `sgit_rk1_a702fba803faac4369eb5d5a320b4dfa017af62bd2425fb298aac4b99e95c0ae:4zf6pf2z` | [open live ↗](https://dev.vault.sgraph.ai/#sgit_rk1_a702fba803faac4369eb5d5a320b4dfa017af62bd2425fb298aac4b99e95c0ae%3A4zf6pf2z) |

The machine-first version of this list is [the catalogue](../../catalogue/index.md) — an index of vaults that is itself a vault, updated by an sgit push with no site deploy. New entries start there: a read key and one line, the rest derived. The walkthrough of how a vault gets published at all — creation, audit, deliberate key publication, embed — is on [the embed demo page](../vault-app-embed.md).


---

*[Site index for agents](../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/index.html)*
