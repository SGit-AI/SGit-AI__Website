# Building vault apps — SG/Vault

> How to build apps that live inside encrypted vaults: the project shape, app.json, the authoring contract, and shipping with sgit push.

*Source: <https://sgit.ai/vault/vault-apps.html> · site v0.2.53 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [SG/Vault](index.md) / Vault apps

# Building vault apps

A vault app is a single `index.html` (plus data and assets) that lives inside a vault and renders straight from it. The experience and the security are the same artifact: the app ships encrypted, the link-holder holds the key, and the server never sees the page you're reading.

## The project shape

```
my-vault/
├── index.html          # the app — self-contained entry point
├── app.json            # auto-launch config (below)
├── content.json        # editable content, separate from the app
├── assets/             # css / js, loaded through the bridge
└── <your data>         # the files the app presents
```

Keep content in data files, not in HTML — so you (or an agent) can edit captions, prose, and structure without touching the app. Then the manifest (preferred location `.vault/app.json`; a legacy root `app.json` is still read):

```
{
  "entry":       "index.html",
  "present":     true,        # boot into App Mode instead of the file browser
  "title":       "My app",
  "permissions": { "fs": { "read": true } },
  "hud":         { "mode": "full" }
}
```

One rule with teeth: **an app cannot write its own manifest** — `.vault/**` and the legacy root `app.json` are a protected floor (`EPROTECTED`). The manifest *is* the grant; letting an app edit it would defeat the model. Edit it via the vault browser or sgit.

## The authoring contract

Vault pages render inside a sandboxed frame, and the browser fetches declarative resources *before* the vault bridge can install. Anything declarative pointing at a vault path will fail. The contract:

- **No** `<link rel="stylesheet" href="…">`, `<script src="…">`, or `<img src="…">` against vault files — inline it, or load it from JS through the bridge (`sg.loadCss` / `sg.loadJs`, or read + inject via `sg.vfs.readText`; set `img.src` from JS).
- **No external resources at all** — no CDNs, fonts, or analytics. A vault app is self-contained by construction; inline SVG is the graphics format.
- **`fetch()` of vault paths does not work** — use `sg.vfs.readText(path)` / `sg.vfs.read(path)`. Plain `fetch` is only useful as a fallback for static hosting.
- **Plain `<a href>` links between vault pages work** — the host intercepts clicks and routes them, so multi-page sites navigate normally (this site is the proof). Hash anchors work too; **query strings don't** (`page.html?x=1` lands on the broken-link overlay), and never assign `location.hash` from JS — the sandboxed frame re-navigates.
- **Signal readiness** — post `{type:'sg-app-ready'}` to the parent when your page has rendered (in the error path too), or users stare at the host's loading overlay. The host also watches for blank apps: ~2.5 s after load with nothing painted, it tells the user so — if you legitimately render late, paint a spinner first.
- **Provide fallbacks** — embed critical styles inline and degrade gracefully, so the page stays readable if the bridge is slow or absent.

## Ship it with sgit

```
$ sgit clone <vault-key> my-app     # or sgit create my-app
# … build index.html, app.json, assets …
$ sgit commit -m "app v1"
$ sgit push                          # deployment == pushing the vault
```

There is no separate hosting step, no build server, no CDN configuration. The vault is the deployment target, the version history, and the rollback mechanism (`sgit history revert`) in one.

## The reference implementation

This website follows every rule on this page and carries its own build system in-vault: a page generator, a validation suite (contract scan, link check, JS parse check), and a versioned release process. Start at [admin & engineering](../admin/index.md) and read `admin/build/` — cloning this vault gives you a complete working example.

[← SG/Vault & the platform](index.md)[The window.sg bridge →](sg-bridge.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/vault/vault-apps.html)*
