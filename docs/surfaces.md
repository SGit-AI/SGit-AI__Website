# Three surfaces: which one are you building for? — sgit.ai

> _page.json inside a vault, an HTML vault app, or a page on a *.sgit.ai site: what each can do, which credential each uses, and the trust direction that inverts between them — plus the same job done on all three, and where each surface’s guidance lives.

*Source: <https://sgit.ai/docs/surfaces.html> · site v0.2.73 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Docs](index.md) / Three surfaces

# Three surfaces: which one are you building for?

Almost every question about “how do I show this” has three different right answers, because there are three places code runs in this estate — **`_page.json`** inside a vault, an **HTML vault app** inside a vault, and a page on a **`*.sgit.ai` site** outside every vault. They have different capabilities, different credentials and, most importantly, **opposite trust directions**. Pick the surface first; the rest of the guidance follows from it.

**The short version.** Publishing a document? `_page.json` or plain markdown, and write no code. Need to *compute* something over the vault's own data, for someone who already has the vault open? A vault app. Need it on the public web, indexed, linkable, with no key-holding required of the reader? A `*.sgit.ai` site page — and there **you** become the one who has to distrust the vault.

## The three, side by side

|  | `_page.json` | HTML vault app | `*.sgit.ai` site page |
|---|---|---|---|
| **Where it runs** | The vault browse view | A sandboxed frame inside the vault host | A normal public web page, any origin |
| **Who reads the vault** | The host | The host, answering `window.sg` calls | **You do** — a CORS `GET` plus Web Crypto |
| **The credential** | The reader already opened the vault | Same — the app never holds a key | A published **read key, printed in your page** |
| **What the reader needs** | The vault link or key | The vault link or key | **Nothing.** It is a URL |
| **Search engines and agents** | Invisible | Invisible | **Indexed**, linkable, quotable |
| **You write** | JSON | HTML, CSS, JS + `app.json` | Whatever your site is built from |
| **Trust direction** | Host renders your content | Host distrusts *your app* and sandboxes it | **You distrust the vault** and sandbox *it* |
| **Ships when** | `sgit push` | `sgit push` | Your site's release |

The last two rows are the ones people get wrong. Inside a vault host, **the host is the one doing the protecting** — it sandboxes the app, gates permissions and keeps the sovereignty rail. On your own site there is no host: **you** are the host, and vault bytes are untrusted input arriving in your origin.

## The same job, on each surface

| You want to… | `_page.json` | Vault app | Site page |
|---|---|---|---|
| **Show a markdown document** | Native — the `markdown` component, or just publish the `.md` | `sg.vfs.readText`, then render | Fetch, decrypt, render — or write the prose as a page and keep a `.md` twin |
| **Browse files and folders** | Native — the host's tree is the browser | Build one from a build-time manifest; raw always available | Same, with the manifest read out of the vault |
| **Show a deck** | `slides` or `gallery` components | Your own viewer, or the vault's `decks/v2` shell | [The deck-viewer pattern](briefs/vault-decks-on-a-site.md) — parse frame plus render frame |
| **Show a PDF** | The `pdf` component | `sg.ui.preview` | **Download only.** A sandboxed frame cannot render one |
| **Compute over the data** | Not possible — it is a layout format | Yes, this is the reason apps exist | Yes, in your own code |
| **Be found by someone who has never heard of you** | No | No | **Yes** — the only surface that does this |

## Where the guidance lives

| Surface | Read |
|---|---|
| **`_page.json` and markdown** | [Publishing content without code](vault/content-authoring.md) — the syntax. [Markdown and file viewers: what not to build](briefs/markdown-and-file-viewers.md) — the decision |
| **HTML vault apps** | [Building vault apps](vault/vault-apps.md) — the project shape and `app.json`. [The window.sg bridge](vault/sg-bridge.md) — the runtime and its permission model |
| **`*.sgit.ai` site pages** | [Reading a vault from a site page](briefs/sgit-ai-site-pages.md) — the brief. [Reading one file out of a vault](vault/reading-a-vault-file.md) — the primitive. [Decks from a vault, on a site](briefs/vault-decks-on-a-site.md) — a worked example |
| **All three** | [Publishing a vault: the method](../demos/vaults/publishing.md) — read keys are publishable, vault keys never are, whichever surface you are on |

## They combine, and the combination is usually right

These are not alternatives to choose between once. The vaults on this site do all three at the same time, and that is the intended shape:

- **The vault holds the content** — markdown, data, images, decks — authored once.
- **A vault app computes over it** for anyone who opens the vault directly, with the full file tree beside it.
- **A site page publishes a view of it** for everyone else: indexed, linkable, and readable without a key or an account.

[The AIUC-1 conformance vault](../demos/vaults/aiuc-1-conformance/index.md) is the clearest example — a fourteen-tab app inside the vault, and [deck pages on this site](../demos/vaults/aiuc-1-conformance/decks/index.md) reading the same files. One set of content; three ways in. **What must never be duplicated is the content itself**: if a paragraph exists in the vault and again in a site page, they will disagree, and the vault is the one that is right.

Every guidance page in this estate is labelled with the surface it applies to. If a page is not labelled, it applies to all three. [All briefs](briefs/index.md) · [Docs](index.md) · [SG/Vault](vault/index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/docs/surfaces.html)*
