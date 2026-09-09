# Working on a vault: start here — guidance

> The first page to read before building, publishing or changing a vault. The practices that get repeated most — pick the surface, do not rebuild what the platform has, publish read keys never vault keys, version everything and show the version — plus routes to the brief that answers each question, and out to coding.sgit.ai, nfrs.sgit.ai and graphs.sgit.ai.

*Source: <https://sgit.ai/docs/guidance/index.html> · site v0.2.73 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../index.md) / Guidance

# Working on a vault: start here

The first page to read before building, publishing or changing a vault — human or agent. It is deliberately short and made almost entirely of edges: the practices that get repeated most, and a route to the page that actually answers each question. If you are an agent and you fetch one thing, fetch [`/docs/guidance/llms.txt`](llms.txt), which is this page in the form you prefer.

**The one-minute version.** Pick your [surface](../surfaces.md) first — it changes every other answer. **Do not build what the platform already has**: markdown, file trees and page layouts are free. **Publish a read key, never a vault key.** **Version everything and show the version**, linked to what changed. **Anything rendered stays one click from the bytes it was rendered from.**

## Read in this order

|  | Read | Because |
|---|---|---|
| **1** | [Three surfaces](../surfaces.md) | Every “how do I show this” question has three different right answers. Picking the surface first collapses most of them |
| **2** | [What not to build](../briefs/markdown-and-file-viewers.md) | The two most common asks — a markdown viewer, a file browser — are already in the platform. Most tasks end here |
| **3** | [Content authoring](../vault/content-authoring.md) | The syntax for `_page.json` and vault markdown, once you know you need it |
| **4** | [Vault apps](../vault/vault-apps.md) and [the window.sg bridge](../vault/sg-bridge.md) | Only when a view has to *compute* something the host cannot know |
| **5** | [Publishing: the method](../../demos/vaults/publishing.md) | Before anything becomes public. Classify the credential before it touches anything |

## Version everything, show the version, link what changed

This is the single most repeated piece of guidance, so it goes first among the practices. A vault is a versioned thing; an app that does not say which version it is leaves the reader unable to tell what they are looking at, and leaves a screenshot or a recording undateable.

- **Show the version in the app's chrome** — small, in the top bar, always visible. Not in a footer, not in an About box.
- **Make it a link**, and make the link go to that version's own details — not to a generic changelog. A reader who clicks `v0.1.7` wants to know what *v0.1.7* was.
- **Give versions a home in the vault**: `versions/index.json` plus one file per version. It is data, so an app can render it, a script can check it, and an agent can read it without running anything.
- **Record the commit.** A version that does not name the vault commit it was built from cannot be verified later.
- **Say when a version is reconstructed** rather than recorded — a history assembled after the fact is still useful, but only if it is labelled.

[The AIUC-1 conformance vault](../../demos/vaults/aiuc-1-conformance/index.md) is the reference implementation: a `Versions` tab, the number in the top bar, and one JSON file per version carrying exactly this shape.

```
versions/index.json      { "current": "v0.18.0", "versions": [ … newest first … ] }
versions/v0.15.1.json    { "version", "date", "commit", "vault",
                           "reconstructed", "title", "summary",
                           "changes": [ … ], "basis": [ … ] }
```

`title` is a sentence, not a label — *“the settings move into the right-hand column, which folds and resizes”* tells a reader more than *“UI improvements”* ever will. `changes` names files. `basis` is for a reconstructed entry: the files that make that stage a distinct thing.

## The rest of the practices, in one place

| Practice | Why it exists |
|---|---|
| **Read keys are publishable. Vault keys never are** | A read key is derived one-way and cannot become write access. A vault key *is* write access, and there is no partly-public version of it. Escrow the write key **before** publishing, not after |
| **Scan for other people's secrets too** | A scan built for sgit credential shapes will not catch an API key sitting in a vault file. We nearly published a live OpenRouter key in a field called `openrouter_key` that matched no sgit pattern |
| **Every credential test needs a negative control** | `sgit clone` creates a directory whether or not the key is valid. The marker that discriminates is `.sg_vault/local/clone_mode.json`. We called a leak once on a directory that an all-zeros key produced identically |
| **Anything rendered stays one click from its bytes** | A reader that only shows its own interpretation asks to be trusted; one that also shows the source offers to be checked. `_page.json` has `{ } Source`; this site gives every page a `.md` twin |
| **Deny by default in `app.json`** | Declare the narrowest permission that works, and write down why each grant exists. `"permissions": {}` is a real answer and often the right one |
| **Manifests at build time, files on click** | A vault can be tens of megabytes. Do not re-derive at runtime what the build already knew, and do not fetch what nobody opened |
| **Content exists once** | If a paragraph is in the vault and again in a page about the vault, they will disagree, and the vault is the one that is right |
| **State the gap rather than papering over it** | A page that names what it is missing is more useful than one that quietly omits it. Measured, not guessed |

## Build briefs — written to be executed

| Brief | For |
|---|---|
| [Markdown and file viewers: what not to build](../briefs/markdown-and-file-viewers.md) | Documents and file browsing in a vault |
| [Decks from a vault, on a site](../briefs/vault-decks-on-a-site.md) | Presentations published on a web page |
| [Reading a vault from a site page](../briefs/sgit-ai-site-pages.md) | Devs coding the `*.sgit.ai` sites |
| [Telemetry from a published vault](../briefs/vault-telemetry-append-lanes.md) | A public vault reporting usage back to its author |
| [Publishing a vault: the method](../../demos/vaults/publishing.md) | Anything about to become public |

The mechanism underneath the last three is [reading one file out of a vault](../vault/reading-a-vault-file.md). The catalogue of what has already been built this way is [the published vaults](../../demos/vaults/index.md) — and [`/demos/vaults/llms.txt`](../../demos/vaults/llms.txt) is that catalogue with every read key, for an agent that wants to go and look rather than take our word for it.

## Where the rest of the answer lives

This site covers vaults and sgit. It deliberately does not cover how code should be written, what a system owes its users when nobody is watching, or how to model meaning — because each of those has a site of its own, with the room to do it properly. **An agent that stops at this domain will get a worse answer than one that follows the edge.**

coding.sgit.ai · Agents & AI — [How software actually gets written here ↗](https://coding.sgit.ai/) — The rules, the compliance measurement against them, which are machine-enforced and which are explicitly not, the open tensions — and a section on writing code for agents to read. Read this before writing a vault app, not after. — “The style guide that measured itself.” — part of the sgit.ai network

nfrs.sgit.ai · Risk & governance — [The requirements nobody writes down until they are violated ↗](https://nfrs.sgit.ai/) — Resilience, budgets, project management, backups — as a reality system rather than a checklist, with a scorecard and a page naming backups as a gap. The questions a vault has to answer once somebody depends on it. — “The non-functional requirements, from the inside.” — part of the sgit.ai network

graphs.sgit.ai · Graphs & method — [A grammar for semantic graphs ↗](https://graphs.sgit.ai/) — From five rules you can apply tomorrow to a full positioning against schemas and vector search — including the four situations in which its own argument is the wrong one. The page to read before modelling anything as data. — “A node is just a node. Meaning lives in the edges.” — part of the sgit.ai network

[The full network](../../network/index.md) lists every site with what it covers and the words it answers to.

## Why this page is mostly links

The estate is one semantic graph that happens to be served from many domains. A vault is a node; so is a site, a page, a version, a published read key. What makes any of them useful is not the node — it is what it is connected to. That is graphs.sgit.ai's own argument, applied to the thing you are reading:

> “A node is just a node. **Meaning lives in the edges.**”

So this page does not restate the guidance that lives elsewhere, and it should not grow into a manual. Its job is to be the node an agent can always find, with enough edges to reach the right answer in one hop. Three properties keep that working, and they are worth preserving in anything built here:

- **Every page is reachable and machine-readable.** Each has a `.md` twin and appears in `llms.txt`; the build fails on an orphan. A page nothing links to is a page nothing can find, which is the same as unpublished.
- **Indexes are generated from the data they index.** [The vault catalogue](../../demos/vaults/llms.txt) comes from the same file the human-readable table does, so the two cannot disagree. An index maintained by hand becomes a lie on a schedule.
- **Scope by domain, link across.** Each site says one thing properly and points at the others rather than summarising them badly. The edge is the answer; the summary would be a worse copy.

If something here is wrong, that is worth telling us — the last brief on this site was corrected by the team that read it, and [the correction sits above the mistake](../briefs/vault-telemetry-append-lanes.md). [/docs/guidance/llms.txt](llms.txt) · [All briefs](../briefs/index.md) · [The network](../../network/index.md)


---

*[Site index for agents](../../llms.txt) · [HTML version](https://sgit.ai/docs/guidance/index.html)*
