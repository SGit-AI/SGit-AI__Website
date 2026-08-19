# Publishing updates and articles

*The authoring contract for `admin/content/updates/` and `admin/content/articles/`.
Adopted from the [VoiceDebrief](https://voicedebrief.ai) journalist pipeline, whose
central rule is the one worth copying verbatim.*

## The one rule

> **Publishing is adding one file. Nothing else.**

No index to update, no HTML to splice, no manifest to hand-edit, no decision about where
a post goes. Ordering, permalinks, markup, `updates.json` and `feed.xml` are all derived
at build time by `admin/build/content.py`.

That is not tidiness. It is the property that makes an **unattended agent** safe to run:
two agents publishing on the same day touch two different files and cannot conflict, and
neither can corrupt a shared index by half-writing it.

## Layout

```
admin/content/updates/YYYY/MM/DD/<version>__update__<slug>.md    a post
admin/content/articles/<slug>.md                                 an article
```

The `<slug>` in an update filename becomes its permalink (`/updates/#the-slug`), so it
must be unique across all posts. The build fails if it is not.

## Frontmatter

Flat `key: value` lines between `---` fences. Lists are comma-separated. No nesting, no
YAML parser, nothing to get subtly wrong — and a malformed line names itself in the error.

### An update

```markdown
---
title: The API reference we did not have
date: 2026-08-18                 # required, YYYY-MM-DD, MUST match the folder path
version: v0.2.34                 # optional — renders the release chip
tags: api, messaging, docs       # optional — rendered as chips
status: published                # or: draft (written, held back from the build)
---

Short opening paragraph — what the reader can now do, or what went wrong.

- **A bold lead-in**, then the detail.
- One bullet per point. Keep it scannable.
```

### An article

```markdown
---
title: Green does not mean live
date: 2026-08-17
summary: One or two sentences. Required — it is the card text and the meta description.
version: v0.2.33                 # optional
tags: ci, deploy                 # optional
status: published
---
```

Articles get their own page at `/articles/<slug>.html`, generated without a `pages.json`
row — because an article must be publishable by adding one file too.

## Rules the build enforces

1. **The folder is the date.** `updates/2026/08/18/…` must carry `date: 2026-08-18`. A
   mismatch means one of them is a typo, and sorting a feed by a date the path disagrees
   with is how a post silently lands in the wrong place.
2. **Internal links are root-relative** — `/docs/pki.html`, never `../docs/pki.html`. The
   build rewrites each to a depth-relative path for the page it lands on. This matters
   more here than on an ordinary site: these pages also render **inside a vault**, mounted
   at an arbitrary path, where a leading slash escapes the app entirely.
3. **Slugs are unique.** A duplicate breaks a permalink somebody may already have shared.
4. **Run the build before committing.** `python3 admin/build/build_pages.py` then
   `node admin/build/validate.js` — the same checks the release runs. A bad file fails
   the build rather than shipping a broken page.

## Markdown you can use

Paragraphs, `- ` bullets, `1. ` numbers, `## `–`#### ` headings, `**bold**`, `*italic*`,
`` `code` ``, `> ` callouts (rendered as the site's note box), ``` fences, `---` rules,
and `[links](/root/relative.html)`.

One site-specific block, for screenshots captured by `admin/build/capture_shots.mjs`:

```
!shot view-estate.webp | ../demos/vaults/risk-graph-explorer/images/ | The estate view.
```

`filename | directory | caption`. It emits the same lazy figure the walkthrough pages
use, so an article gets the screenshot pipeline — including the print behaviour — free.

## What belongs where

| | |
|---|---|
| **Update** | One user-visible change worth telling somebody about. A release with three stories in it gets three posts — that is the point, and it is why this is not the version log with a nicer stylesheet. |
| **Article** | An argument that crosses pages: what a thing means, why it is shaped that way, what it cost to find out. |
| **Version log** (`VERSION_LOG` in `build_pages.py`) | The complete technical record, one entry per release. Still the source of truth; updates are the readable surface over it. |

## Grounding — the rule that matters most

Every claim comes from the repository: `git log`, the tags, `VERSION_LOG`, the validator
output, a command you actually ran. **If something is only proposed, say PROPOSED or leave
it out.** Never describe behaviour you have not seen evidence of.

An article that makes a testable claim should link to the test — the same discipline
`/compare/` already uses, where results carry an expiry and render as UNVERIFIED once
stale. An article that only restates a fact another page owns should link to that page
instead, so when the fact changes the article does not start lying.

---
Licensed CC BY 4.0.
