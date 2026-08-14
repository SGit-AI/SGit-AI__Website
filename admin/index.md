# Admin & engineering — sgit.ai

> How the sgit.ai site is built: a vault app with generated pages, bridge-loaded assets, a validation suite, and sgit itself as the deployment pipeline.

*Source: <https://sgit.ai/admin/index.html> · site v0.1.26 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / Admin

# Admin & engineering

How this site is built, shipped, and versioned. sgit.ai is not hosted on a web server — it is a **vault app**: a set of HTML pages living inside an encrypted SG/Send vault, decrypted and rendered in your browser. The site about sgit is delivered by sgit.

## Architecture

```
vault root
├── index.html · security.html · why.html      # root pages
├── docs/*.html                                      # 8 documentation pages
├── vault/*.html                                     # 4 SG/Vault platform pages
├── admin/                                           # this section
│   ├── index.html · versions.html
│   ├── brief-design-improvements.md                 # brief for Claude Code
│   └── build/                                       # the build system itself
│       ├── build_pages.py                           # generates every page
│       └── validate.js                              # pre-push checks
├── assets/site.css · assets/site.js                 # shared, loaded at runtime
└── app.json                                         # auto-launch config
```

- **The authoring contract.** Vault pages render inside a sandboxed frame, so declarative references to vault files (`<link>`, `<script src>`, `<img src>`) would 404 before the vault bridge installs. Every page therefore carries only a tiny critical-style block plus a ~20-line bootstrap.
- **Shared assets over the bridge.** The bootstrap waits for the `window.sg` bridge and loads `assets/site.css` / `assets/site.js` through it — trying `sg.loadCss`/`sg.loadJs` first, then `sg.vfs.readText` + inject, then plain `fetch` as a static-hosting fallback. Worst case, pages degrade to readable unstyled HTML.
- **Multi-page navigation.** Plain relative `<a href>` links between pages — the vault host intercepts clicks and routes them, giving normal browser-style navigation (back/forward/history come from the host chrome).
- **Read-only by design.** The app requests no write permissions in `app.json`; reads need no grant. Nothing on this site can modify the vault.

## Build system

Every page is generated from a single Python script holding one shared template (nav, footer, bootstrap, version stamp) plus per-page content. Nothing is hand-edited twice: change the template once, regenerate, and every page updates consistently — including the version badge you can see in the nav.

## Validation before every push

- Every inline script and `site.js` is parse-checked with Node.
- A contract scan proves no `<link href>`, `<script src>`, or `<img src>` references a vault path.
- Every internal link is resolved against the real file tree — broken links fail the build.
- A banned-words scan keeps retired concepts and legacy naming out of the content.

## Release process

```
# 1. bump SITE_VERSION (v0.1.n — n increases on every push) + add a versions row
# 2. regenerate + validate
$ python3 admin/build/build_pages.py && node admin/build/validate.js
# 3. ship to the vault — the encrypted deployment
$ sgit commit -m "site vX.Y.Z: …" && sgit push
# 4. ship to git — same folder, second remote; GitHub Pages deploys from it
$ git add -A && git commit -m "site vX.Y.Z" && git push origin dev
```

One folder, one source of truth, two remotes: the same working tree is an sgit vault *and* a git repository (`SGit-AI/SGit-AI__Website`). Every release pushes both — sgit carries the encrypted history; git carries the public mirror and triggers the GitHub Pages deployment. A release isn't done until both remotes report in sync. See [release history](versions.md).

## Design & contributions

A standing brief for Claude Code sessions proposing design improvements lives at [admin/brief-design-improvements.md](brief-design-improvements.md) — it carries the constraints (authoring contract, self-contained assets, validation suite, version bump) that any change must respect.

[← Home](../index.md)[Release history →](versions.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/admin/index.html)*
