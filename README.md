# sgit.ai — the website, served from a vault

This vault contains the sgit.ai website, delivered as a vault app. sgit is in beta
and powers production workflows; this site says so honestly on every relevant page.

## Structure

- `index.html` — landing page (light theme)
- `use-cases.html` · `security.html` — root pages
- `docs/` — 8 documentation pages (hub, what-is-sgit, installation, quickstart,
  sgit-for-git-users, two-branch-model, agents, limitations)
- `vault/` — the SG/Vault platform section (for now, the official sgraph
  working documentation): platform overview, building vault apps, the
  window.sg bridge, and the git-repos-inside-vaults engineering preview
- `admin/` — engineering section:
  - `index.html` — how the site is built and released
  - `versions.html` — release history (site version bumps on every push)
  - `brief-design-improvements.md` — standing brief for Claude Code sessions
  - `build/build_pages.py` — generates every page from one shared template
  - `build/validate.js` — pre-push checks (JS parse, authoring contract,
    internal links, banned words)
- `assets/site.css` + `assets/site.js` — shared, loaded at runtime through the
  SG bridge (`sg.loadCss`/`sg.loadJs` → `sg.vfs.readText` → `fetch` fallbacks)

## Release process

1. Bump `SITE_VERSION` (v0.1.n) in `admin/build/build_pages.py` and add a
   `VERSION_LOG` row — the version badge appears in the nav of every page.
2. `python3 admin/build/build_pages.py && node admin/build/validate.js`
3. `sgit commit -m "site v0.1.n: ..." && sgit push`
4. `git add -A && git commit -m "site v0.1.n" && git push origin dev`

One folder, two remotes: this working tree is an sgit vault AND the git repo
`SGit-AI/SGit-AI__Website` (which deploys to https://sgit.ai via GitHub Pages
on every push to `dev`). A release is done when BOTH remotes are in sync.
