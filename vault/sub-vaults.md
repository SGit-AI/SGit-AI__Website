# Sub-vaults — SG/Vault

> Vaults inside vaults: link files, owner records, read-only team access, click-to-load external embeds, and the extract-and-embed workflow.

*Source: <https://sgit.ai/vault/sub-vaults.html> · site v0.2.21 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [SG/Vault](index.md) / Sub-vaults

# Sub-vaults: vaults inside vaults

A vault can point at other vaults. A pointed-to vault shows up inline in the file tree, exactly like a folder — expand it and browse. A clinic's parent vault can hold many per-patient vaults; a demos vault can gather live project vaults — **without copying their contents**.

## The mechanism is a convention — like git submodules

Nothing is baked into the vault format. A sub-vault is a small pointer file plus UI behaviour: any file named `*.link.json` is treated as a link, and renders as an expandable folder at its own path. It really is "just create some files" — write the pointer, `sgit commit`, `sgit push`.

```
# demos/acme.link.json → renders as folder demos/acme
{ "vault_id": "75f1c88be33d", "ref_id": "lk-37939d3b9b1a", "label": "ACME PoC" }
```

Two levels of setup:

- **Link file only** — the sub-vault appears; each device enters the child's key once.
- **Link file + owner record** — a `.vault/owner/ro-links.json` entry stores the child's **read key only, never its write key**; the child then opens silently, read-only, on any device that has the parent. This is what makes it usable for a team.

The same pointer convention covers **external resources** (a YouTube video, an image, a page) — with a privacy default worth advertising: external embeds are **click-to-load**, showing a placeholder until the user acts, so opening a vault never phones home on its own; and external frames get no bridge and a visible "cannot read this vault" banner.

## Apps read across the boundary

To an app, an inner-vault file is just another path: `sg.vfs.readText('patients/alice/score.json')` auto-opens the child read-only with the stored key — no prompt fires during a read, and if no key is available the read simply fails: the zero-knowledge boundary holds. This is the workflow that lets one dashboard read across many per-user vaults without anyone seeing raw vault UI.

## Extract & embed — one primitive, three techniques

The reverse direction: pull a folder out into its own vault (separate lifecycle, separate sharing, separate history) and bring it back into the parent's app. Extraction is one call from inside a vault app:

```
await sg.vault.create({
  label: 'Q3 Report', seedFrom: 'self:reports/q3',
  returnKey: true, custody: true, link: { path: 'sub/q3-report' }
})
```

The new vault gets a strong random passphrase; the seed copy **structurally cannot carry `.vault/**`** — so a child can never inherit the parent's owner secrets or tokens. Then choose how to surface it: a **read-only sub-vault link** (the default, and the recommended one today), a **live embedded app** via `sg.vault.embed` (host-managed key handshake — the key never touches the URL or storage; the frame is sandboxed to scripts only, and the host refuses escape-hatch sandbox tokens even if asked), or a **cross-vault mount** where the child performs operations under its own grants — your app never gains cross-vault write authority itself.

**Honesty notes:** the mount technique's credential resolution is explicitly a trial-only stub in current code — prefer the link or embed forms for real users today. And treat an extract-and-link split as an *organisational* boundary (lifecycle, sharing, history), not a confidentiality boundary from the parent's own readers. Sub-vault access from the sgit CLI is proposed, not shipped — today sub-vaults are a browser-side capability.

[← Content authoring](content-authoring.md)[Git repos inside vaults →](git-and-vaults.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/vault/sub-vaults.html)*
