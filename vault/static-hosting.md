# Static hosting on GitHub Pages — SG/Vault

> Serve an encrypted vault and its app from GitHub Pages or S3 with zero backend: deterministic GET paths, client-side decryption, clean read-only degradation.

*Source: <https://sgit.ai/vault/static-hosting.html> · site v0.2.23 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [SG/Vault](index.md) / Static hosting

# Static hosting — GitHub Pages / S3

The same vault-app HTML runs against the live API **or** a 100% static file host, transparently. The app only talks to `window.sg`; static vs live is a property of the transport, not the app. Shipped, opt-in, default-off.

## Why it works

Everything needed to open and browse a vault is a plain GET to a deterministic path: file IDs (commits, trees, refs, indexes) are content hashes or HMACs of the key, computed client-side — **no discovery or listing call exists**. So a static host that serves those exact paths just works: the browser GETs ciphertext from GitHub Pages or S3 and decrypts locally. No backend, no server, still zero-knowledge — the bytes on the CDN are ciphertext.

```
<!-- on the hosting page, before the host boots -->
<script>
  window.SG_STATIC   = true;                    // batch reads → GETs; writes → EREADONLY
  window.SG_ENDPOINT = 'https://my-org.github.io/my-vault';
</script>
```

## What works statically — and what doesn't

| Call | Static? |
|---|---|
| Open, browse, read files, history — `sg.vfs.read/readText/list` | ✅ plain GETs |
| Large reads | ✅ falls back from presigned to direct GET |
| Batch reads | ✅ fan out to parallel GETs, identical result shape |
| Writes, deletes, `sg.append.*`, vault creation | ❌ rejected cleanly with `EREADONLY` |

A static vault is a **read-only snapshot** — ideal for published docs, reports, dashboards and view-only shares. The app detects it via `sg.app.writable === false` and hides its editing UI; the same HTML runs writable against the live endpoint. *Same app, two backends.*

## The layout — path mirroring is the one hard requirement

The live API serves `GET /api/vault/read/<vaultId>/<filePath>`; the static host must serve the vault's encrypted `bare/` tree at exactly that path under your base:

```
<repo root>/                    → https://my-org.github.io/my-vault/
└── api/vault/read/<vaultId>/
    └── bare/
        ├── data/      obj-cas-imm-*    # immutable — cache forever
        ├── refs/      ref-pid-muw-*    # mutable head — no-store
        ├── indexes/   idx-pid-muw-*
        └── keys/      key-rnd-imm-*
```

If the repo is your vault's own git remote (working tree + `bare/` committed per the [side-by-side pattern](git-and-vaults.md)), the encrypted tree is already in the repo — publishing is just placing it under the right path prefix. Visitors open `https://…/my-vault/#<key>`: the key travels in the URL fragment (never sent to the host), the transport GETs ciphertext, the browser decrypts and renders.

## Honest caveats

- **Read-only and frozen.** The static tree is a snapshot at export time; new live commits appear only when you re-export.
- **Paths must match exactly**, or reads 404. (A configurable read-path template is a proposed follow-on, not shipped.)
- **Cross-origin setups need CORS** on the static host for GETs; same-origin needs nothing.
- **The key is the read capability.** Anyone with the full URL can read the snapshot — that is the point of publishing one — but the host itself only ever holds ciphertext.

[← Git repos inside vaults](git-and-vaults.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/vault/static-hosting.html)*
