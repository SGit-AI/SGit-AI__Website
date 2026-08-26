# Content authoring — SG/Vault

> Publish documents, galleries and hub pages from a vault with no code: markdown with print-aware extras, and _page.json layouts with eleven component types.

*Source: <https://sgit.ai/vault/content-authoring.html> · site v0.2.45 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [SG/Vault](index.md) / Content authoring

# Publishing content without code

Not everything needs an app. The vault browser renders two kinds of structured content natively — **markdown documents** and **`_page.json` page layouts** — so a vault full of files becomes a navigable, themed, printable site with no HTML written at all. This is the lighter on-ramp; [vault apps](vault-apps.md) are the heavier one.

## Which one, when

| Reach for markdown | Reach for `_page.json` |
|---|---|
| Prose-first documents, articles, reports, specs, step-by-step guides, linked hierarchies of notes | Designed pages: hero banners, galleries and slideshows, hub pages with clickable cards, decks, embedded PDFs, explicit theme control |

Both can coexist in one folder — `_page.json` takes priority in the browse view. A file named exactly `_page.json` is auto-detected, no registration; one at the vault root renders immediately on open.

## `_page.json` in one screen

```
{
  "title": "Q3 Report",
  "theme": { "mode": "light", "accent": "#0f766e", "font": "serif", "density": "spacious" },
  "navigation": [ { "label": "Overview", "anchor": "overview" } ],
  "components": [
    { "type": "hero",    "title": "Q3 Report", "height": "medium" },
    { "type": "section", "title": "Overview", "layout": "narrow", "children": [
      { "type": "text",     "content": "…" },
      { "type": "gallery",  "images": ["img/a.webp","img/b.webp"], "columns": 3 },
      { "type": "markdown", "file": "notes/summary.md" }
    ]}
  ]
}
```

- **Eleven component types:** `hero`, `section` (the only container — everything else nests in its `children`), `text`, `bullet-points`, `title`, `image`, `gallery` (click-to-lightbox), `slides`, `pdf`, `markdown`, `cards`, `columns`.
- **Themes:** `dark`/`light` shorthand or a full block (mode, accent, font, density, background); six named schemes exist, and all but the dark deck are print-safe.
- **Paths are vault-relative to the folder holding `_page.json`** — `../` allowed but never outside the vault, and **no external URLs**: vault files only, so a page never phones home.
- **Live edit preview:** the browse view has a split JSON-editor with a debounced preview — but it **cannot save**; you copy the JSON out and push it with sgit. (The intended loop, verbatim from the internal skill: paste in JSON suggested by an AI, preview it immediately, then commit.)

## Markdown in vaults — the extras

- **Print-aware front matter** (first line, `---`-delimited): `page_break_before: h1` and a literal `print_css` block, so a markdown file prints like a document, not a web page. Plus `<!-- page-break -->` anywhere for an explicit break.
- **Image sizing with the pipe syntax** — `![caption|400](img.png)`, `|60%`, `|800x600` — inside the alt text, so it degrades gracefully in any other renderer.
- **Internal links open as tabs**, with extension fallbacks; link folders via `folder/README.md`, not `folder/`. The browse view auto-opens the alphabetically first file — name your entry `README.md` or `00-INDEX.md`, or add a root `_page.json`.
- **Editing saves** — unlike the `_page.json` editor, the markdown split-editor persists to the vault (writable vaults only).
- **The traps:** raw HTML is stripped and shows as escaped text; nested lists, task lists, footnotes and anchor-id headings are not supported. Write flat, plain markdown.

**The agent angle:** both formats are plain JSON and plain text — which makes them ideal surfaces for AI agents to author. An agent writes `_page.json` or markdown into a vault with `sgit write --json`, a human previews it in the browser, and the whole loop stays end-to-end encrypted.

[← The window.sg bridge](sg-bridge.md)[Sub-vaults →](sub-vaults.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/vault/content-authoring.html)*
