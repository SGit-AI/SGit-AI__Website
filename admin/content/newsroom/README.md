# The SGit Newsroom

The editorial layer over the articles. Rendered publicly at https://sgit.ai/newsroom/.

**Publishing is still adding one file.** An article at `admin/content/articles/<slug>.md` is live,
in Latest, in the archive, in `articles/feed.xml` and in `newsroom/wire.json` as soon as the build
runs. Nobody approves it.

**Placement has one owner.** `front.json` (the lead, the highlights, the homepage band, the
featured collections) is written by the Editor only. Anyone else asks with a pitch.

| Path | What | Who writes it |
|---|---|---|
| `front.json` | the front: lead, highlights, homepage, featured collections, editor's note | Editor |
| `roles/<slug>.md` | one desk role per file; its `writes`/`edits` lists ARE the behaviour policy | Editor (with the human) |
| `collections/<id>.md` | a curated set of articles with an introduction | Historian |
| `notes/YYYY/MM/DD/<slug>.md` | nugget, thread, weekly, brief, correction | Historian, Journalist, Editor |
| `pitches/YYYY-MM-DD__<slug>.md` | a request for placement | anyone; the Editor edits `status` only |
| `board/<id>-<slug>.md` | the desk's kanban: backlog, doing, review, done | Editor |
| `log/YYYY/MM/DD/HHMM__<role>__<slug>.md` | one record per desk run, append-only | each role, its own |
| `newsletter/NNN-YYYY-MM-DD.md` | a newsletter issue, published at `articles/newsletter/YYYY/MM/DD/NNN-<slug>.html`: `title`, `date`, `slug`, `summary`, `dek` (banner line), `ideas` (`|`-separated, banner), `cites`, `linkedin` (URL once posted) | Journalist |

Directives available in notes and collections, on top of the article markdown:

    !quote <article-slug> | <exact text>     a quote, checked verbatim against the article at build time
    !quote <article-slug> #<n>               the n-th quote in the article's graph
    !article <article-slug>                  the article's card
    !articles YYYY-MM-DD..YYYY-MM-DD         every article in the range, with its teaser, and the count
    !list <slug>, <slug>, ...                  a hand-grouped list: title and teaser, no dates
    !figure <repo path> | caption            one image from an article or a vault, e.g. articles/images/x.webp
    !collage <name> | img :: label, ... | caption   two to six images as one 1920x1080 picture
                                             (rendered by make_banners.mjs; listed in the LinkedIn box)
    !covers YYYY-MM-DD..YYYY-MM-DD           a promise: every article in the range appears in some !list
                                             in this file, or the build fails and names what is missing

Tools:

    python3 admin/build/desk.py                       the desk report: what the Editor should do next
    python3 admin/build/policy_check.py --role <r>    did this branch write only what role <r> may?
    node admin/build/make_banners.mjs                 1920x1080 LinkedIn covers for articles and issues
                                                      (run after the build; release.sh does both)

Readers subscribe to the newsletter, not to articles. An issue is due a week after the last or once
five articles have been published since it; desk.py says when. Each issue is cross-posted as a
LinkedIn article in Deterministic GenAI: upload its cover from articles/banners/, paste the title,
select and copy the issue's body from its page (in an issue a quote has no source line; the paragraph before it must link the article it quotes, and the build checks that), then set `linkedin:` in the issue file. End the LinkedIn article with the subscribe paragraph and, optionally, articles/banners/subscribe.jpg; both point at https://sgit.ai/subscribe/, the one page with the form.

A placement naming an article that does not exist is skipped and reported, never a build failure:
a contributor's rename must not be blocked by a file only the Editor may edit.
