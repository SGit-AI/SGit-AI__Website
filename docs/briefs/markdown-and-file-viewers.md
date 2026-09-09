# Markdown and file viewers in a vault: what not to build — build brief

> Two of the most common asks — a markdown viewer and a file/folder browser with raw views — are already in the vault platform. The ladder from zero code to a full app, the markdown rules that actually catch people, the raw-always contract for a file explorer, and the prompt to hand the builder.

*Source: <https://sgit.ai/docs/briefs/markdown-and-file-viewers.html> · site v0.2.74 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../index.md) / [Briefs](index.md) / Markdown and file viewers

**Surface:** inside a vault — `_page.json`, markdown, or a vault app. [The other surfaces →](../surfaces.md)

# Markdown and file viewers in a vault: what not to build

Two of the most common things an agent is asked to add to a vault — **a markdown viewer** and **a file/folder browser with raw views** — already exist in the vault platform. Most requests for them are answered by publishing files in the right shape and writing no code at all. This brief says which surface renders what, gives the ladder from zero code to a full app, and states the one contract to honour if you do build your own.

**Read this first, and you may be finished.** The browse view already renders every `.md` file in a vault, and the file tree on its left *is* the folder viewer. If an agent is about to write a markdown parser or a file explorer into a vault app, it is almost certainly solving a problem the host solved already — and the version it writes will be worse, bigger, and will not match the rest of the estate.

## The ladder: stop at the first rung that works

|  | You write | You get | Reach for it when |
|---|---|---|---|
| **0 · Nothing** | `.md` files | Rendered markdown, a file tree, tabbed previews, internal links that open as tabs, print | Prose: articles, reports, specs, notes, READMEs. **Start here every time** |
| **1 · A layout** | `_page.json` | Hero, sections, galleries, slideshows, card hubs, embedded PDFs, themes — and a `markdown` component that renders one of your `.md` files inside the layout | You want a designed page rather than a document, or a hub that navigates to folders |
| **2 · An app** | `index.html` + `app.json` | Anything — computed views, filters, queries over your own data | Only when the answer depends on *computing* something the host cannot know |
| **3 · A site viewer** | A viewer on your website | Vault content on a public web page, outside any vault host | The content must live on a normal site. See [the decks brief](vault-decks-on-a-site.md) |

The reference for rungs 0 and 1 is [**Publishing content without code**](../vault/content-authoring.md); for rung 2 it is [Building vault apps](../vault/vault-apps.md) and [the window.sg bridge](../vault/sg-bridge.md). This page is the decision, not the syntax.

## Pattern one: the markdown viewer you do not write

Markdown is rendered natively on **three** surfaces, and none of them requires code:

- **Any `.md` file in the browse view** — click it in the tree, it opens as a rendered tab. Nothing to register.
- **The `markdown` component in `_page.json`** — `{"type":"markdown","props":{"file":"overview.md"}}` drops a rendered document into a designed page, or `"text"` for an inline string. This is how you get prose *inside* a layout without duplicating it.
- **A markdown file as the vault's front door** — the browse view auto-opens the alphabetically first file, so name the entry point `README.md` or `00-INDEX.md`. A root `_page.json` takes priority over both.

### The rules that actually catch people

- **Raw HTML is stripped and shows as escaped text.** This is the single most common failure. Write flat markdown; do not reach for a `div` when a heading will do.
- **Size images with the pipe syntax, not HTML** — `![caption|400](img.png)`, `|60%`, `|800x600`. It lives inside the alt text, so the URL stays clean and the file still renders in any other markdown tool.
- **Link a folder through its file, not the folder** — `folder/README.md`, never `folder/`. Which file a bare folder link opens depends on sort order, and that is not a contract.
- **Nested lists and task lists are not supported.** Neither is HTML. Plan the document around that rather than discovering it after a push.
- **Image paths are relative to the `.md` file**, not to the vault root.
- **No external URLs for vault assets.** Vault files only — which is what makes a published document unable to phone home, and is a feature rather than a limitation.

Front matter adds print control: a `---`-delimited block at the very top can set `page_break_before` and carry a literal `print_css` block, so a document prints as a document. That plus the theme options is usually the whole gap between “a markdown file” and “a deliverable somebody can hand to a client”.

## Pattern two: the file and folder viewer, and the raw view

The browse view is already a two-pane explorer: tree on the left, tabbed preview on the right, with `_page.json` pages carrying a `{ } Source` toggle that flips the rendered layout back to its JSON. **If that is enough, you are done.**

You need your own explorer only when the vault's files mean something the host cannot know — when a `.json` file is not just JSON but a control, a policy, a graph node, and you want to render it *as* that. [The AIUC-1 conformance vault](../../demos/vaults/aiuc-1-conformance/index.md) does exactly this, and states the principle in its own source:

> “A manifest generated at build time, files fetched on click, raw always available and a data view where the build understands the file. **Raw is the point — a catalog that asks to be trusted has to be readable in the form it was written.**”

That is the contract, and it is worth adopting whole:

| Rule | Why |
|---|---|
| **Raw is always available, for every file** | A reader that can only show you its own interpretation is asking to be trusted. One that shows you the bytes is offering to be checked. Never let a rendered view be the only way to see a file |
| **A reader is an addition, never a replacement** | Files the build understands get a view *as well as* raw. Files it does not understand still open — a file explorer that hides what it cannot parse is hiding the interesting cases |
| **Drive the tree from a manifest built at build time** | Walking the vault at runtime to list files is slow and re-derives on every load what the build already knew. Generate the folder/file manifest when you build, ship it as data |
| **Fetch a file on click, not up front** | A vault can be tens of megabytes. The tree costs the manifest; a file costs that file |
| **The empty state tells the reader the deal** | AIUC-1's says it in one line: *“Pick a file on the left. Raw is always there; files the build understands also get their own view.”* |

The same instinct runs through the rest of the estate: `_page.json` has `{ } Source`, every page on this website has a `.md` twin, and the deck viewer offers the printed PDF beside the rendered slides. **Anything rendered should be one click from the thing it was rendered from.**

## Before you call it done

- Did you actually need to build anything? If the answer is markdown in a tree, rung 0 was the answer and the app is a liability.
- Open every `.md` file in the browse view and look for escaped HTML — that is stripped markup, and it means the document was authored against the wrong renderer.
- Every folder link goes to a file, not a folder.
- If you built an explorer: every file opens, including the ones with no reader, and raw is reachable for all of them.
- Check what you published. [The publishing method](../../demos/vaults/publishing.md) applies here as much as anywhere — read keys are publishable, vault keys never are, and a scan for sgit credential shapes will not catch an unrelated API key sitting in a vault file.

## The prompt to hand the builder agent

```
Make the documents in vault VAULT_ID readable.

Read https://sgit.ai/briefs/markdown-and-file-viewers.md first, then
https://sgit.ai/vault/content-authoring.md for the syntax.

DO NOT WRITE A MARKDOWN RENDERER OR A FILE EXPLORER. Both exist in the vault
platform already. Climb this ladder and stop at the first rung that works:

0. Publish .md files. The browse view renders them and its file tree is the
     folder viewer. Name the entry point README.md or 00-INDEX.md.
1. Add a _page.json if you need a designed page rather than a document. Use
     its markdown component to pull in the .md files you already wrote, so the
     prose exists once.
2. Only build an app if a view has to COMPUTE something the host cannot know.

Markdown rules that will bite you: raw HTML is stripped and shows as escaped
text; size images with the pipe syntax inside the alt text; link folders through
folder/README.md and never folder/; nested lists and task lists are unsupported;
image paths are relative to the .md file; no external URLs.

If you do build a file view, raw is always available for every file, a reader is
an addition and never a replacement, the tree is driven by a manifest generated
at build time, and files are fetched on click.

Report which rung you stopped at and why the rung below it was not enough.
```

Written from the two patterns as they are actually published across the vaults on this site. The syntax reference is [Publishing content without code](../vault/content-authoring.md); the sibling brief for putting vault content on a public website is [Decks from a vault, on a site](vault-decks-on-a-site.md). [All briefs](index.md)


---

*[Site index for agents](../../llms.txt) · [HTML version](https://sgit.ai/docs/briefs/markdown-and-file-viewers.html)*
