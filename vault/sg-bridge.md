# The window.sg bridge — SG/Vault

> The vault app runtime: sg.* namespaces, the deny-by-default permission model, and the capabilities the host chrome provides for free.

*Source: <https://sgit.ai/vault/sg-bridge.html> · site v0.2.14 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [SG/Vault](index.md) / The bridge

# The `window.sg` bridge

Inside App Mode, the host injects a bridge object — `window.sg` — that gives your page mediated access to the vault and to host capabilities. It installs synchronously while `<head>` parses, so any inline script can use it. The app frame never holds the vault key: every operation goes through the host, which owns the crypto and the consent UI.

## Namespaces at a glance

| Namespace | What it does | Grant |
|---|---|---|
| `sg.vfs` | `read` / `readText` / `list` / `write` / host-fulfilled `download`. Writes cap at ~3 MB (`EFBIG`); reads have no cap | `fs.read` / `fs.write` |
| `sg.loadCss` / `sg.loadJs` | Top-level functions (not under `vfs`) — the sanctioned way to load vault CSS/JS; injects into `<head>` | rides `fs.read` — no separate verb |
| `sg.fs` | `move` (grant needed on both paths) / `delete` / `mkdir` | `fs.*` + first-use consent |
| `sg.vault` | Cross-vault lifecycle: `create(opts)` (options object — `label`, `seedFrom`, `returnKey`, `custody`, `link`), `getKey`, `openApp`, `list`, `unlink`, `mount`, `embed` | `vault.*`; `embed` needs none — the key is the capability |
| `sg.history` | Read-only commit history: `log`, `list`, `read`/`readText` at a commit — works on read-only opens | no |
| `sg.sync` | `status` / `push` / `pull` / `refresh` against the named branch (`sg.git.*` survives as a deprecated alias) | writable vault |
| `sg.auth` | The write gate — the server access token, separate from the encryption key: `hasKey`, `setKey`, `check`, `clear` | no |
| `sg.ui` | Host toasts (`message`), quick-look `preview` (incl. PDFs — in-frame PDF rendering is sandbox-blocked), `requestPermission` | no |
| `sg.state` | Device-local prefs (64 KiB/key, kernel localStorage, survives reload, not a vault write — "a theme toggle shouldn't create a commit") | no |
| `sg.llm` | `available` / `models` / `chat` (streaming, cancel, image parts) / `usage` / voice `listen` — the vault's LLM key stays in the host; your frame never sees it | `llm.chat` / `llm.listen` / … |
| `sg.append` | Append-only transport (write verb is `write`): `configure`, `write`, `list`, `fetch`, `markProcessed`, `purge`. Lives outside the commit tree | `append.*` |
| `sg.on` / `sg.off` | Host events pushed to the app (e.g. `append.new-messages` on tab focus — the kernel checks; your app does not poll) | `host_events` allowlist (top-level key) |
| `sg.app` | Read-only context: `writable`, `selfPath`, `vaultName`, `vaultId`, `context` | no |

## The permission model

Grants live in `app.json` (preferred location: `.vault/app.json`; a legacy root `app.json` is still read). Each permission is `true | false | string[]`, and path lists are **prefix-based, not glob**: a trailing `/` means "this folder and everything under it"; no slash means an exact file. `"data/**"` is not valid — use `"data/"`.

```
{
  "entry": "index.html",
  "permissions": {
    "fs":    { "read": true, "write": ["data/"], "delete": ["data/"] },
    "vault": { "create": ["runs/"] },
    "llm":   { "chat": true },
    "externalLinks": true,
    "downloads": true
  },
  "host_events": ["append.new-messages"]
}
```

- **Mutations are deny-by-default.** Writes, deletes, vault lifecycle, append and llm all throw `EPERM` without a grant. **Reads are default-allow today** — and are planned to flip to deny-by-default, so declare `fs.read` anyway.
- **Two independent gates on every mutation:** the server access token (is the vault writable at all?) *and* the `app.json` grant. The manifest is a hard ceiling — an app can only ever do what it declares.
- **The floor is never grantable:** `.vault/**` is invisible and untouchable (`EPROTECTED`) — which is also why an app cannot edit its own manifest: the manifest *is* the grant.
- **Consent is host chrome.** Grant-gated verbs raise the host's own confirmation, cached per (vault, app, verb); `permissions.consent` can tune (never widen) the prompting. Apps can't fake or suppress it.
- **LLM calls are budgeted:** the host clamps `maxTokens`, filters models, enforces spend caps (`EBUDGET`) — call `sg.llm.available()` before rendering any AI UI, and render costs as estimates (`~`), never as a bill. Deliberate design: there is no tool-calling loop — *the LLM never gets ambient authority over the vault*; your app decides what to do with a reply, under its own grants.

## Error codes worth branching on

| Code | Meaning |
|---|---|
| `EPERM` | verb not granted in `app.json` |
| `EPROTECTED` | the floor — `.vault/**` or the manifest itself |
| `ECONSENT` | user declined the consent prompt |
| `ENOENT` | no such file — the usual cause when `loadCss`/`loadJs` "doesn't work" (typo, or written locally but never pushed) |
| `EFBIG` | single write over ~3 MB |
| `EREADONLY` | static host or read-only session |
| `EBUDGET` · `ENOKEY` · `EMODEL` · `EABORT` | llm namespace: spend cap, no key configured, model not allowed, cancelled |

## Host chrome vs API — two different things

**Chrome you configure but never call** (via `app.json`'s `hud` block — `mode: full | minimal | hidden | none` plus per-button `show.*` flags): the nav row, Print, the ✨ AI chat panel (text and voice, entirely at the host origin — your frame never sees the conversation, the key, or the microphone), the file-activity meter, friendly 404 overlays, and the external-link confirm. **API you call, with grants:** `sg.ui.preview`, `sg.vfs.download`, `sg.llm.*`.

And the **sovereignty rail** — three things an app can never suppress, whatever its `hud` config: consent prompts always render; `mode:"hidden"` keeps a corner exit pill; and the user can force the full HUD back on from their side, at a level app code cannot reach. The HUD config is for app *preferences*, not app *authority*.

**Versioning note:** this page is an orientation map, verified against the app-shell bridge (v0.2.x, 2026-08). The authoritative, always-current API reference ships with the app-shell source; where they disagree, the source-side reference wins.

[← Building vault apps](vault-apps.md)[Content authoring →](content-authoring.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/vault/sg-bridge.html)*
