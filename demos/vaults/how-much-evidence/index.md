# The evidence behind one article, published as a vault, sgit.ai

> Every number in the article How much of this did I write? as a file in a vault: the session's messages, releases and days; per-article ledgers with the turns behind each; the corrections and their latency; the article dependency map three levels deep; the article's own fractal from strategy to data; the record the memos stood on; seventy-five article versions with a diff between any two; and a screenshot and hash of each cited source. With the app that reads them.

*Source: <https://sgit.ai/demos/vaults/how-much-evidence/index.html> · site v0.7.35 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../index.md) / How Much Evidence

# The evidence behind one article, published as a vault

Every number in [How much of this did I write?](../../../articles/how-much-of-this-did-i-write.md) comes from a file in this vault: the session's messages, releases and days as rows; the per-article ledgers with the turns behind each; the catalogue of corrections and how long each waited; the map of how the articles cite each other, with every article's own graph; the article's own fractal from strategy to data; the record the memos stood on; seventy-five saved versions of twenty-two articles with a diff between any two; and a screenshot and hash of each cited source as it stood on 5 October 2026. The app that reads them is in the vault too.

**The argument is in the article.** This vault is the worked example for [**How much of this did I write?**](../../../articles/how-much-of-this-did-i-write.md), which measures the session that wrote the last twenty-two articles on this site and asks what the input actually was. The article's first version was built from an earlier cut of the same data; where the vault's numbers differ, the article says so and the vault's `hand_check.json` shows both.

The nine views of the vault app. Every screenshot on this page is a picture of the real vault, and clicking one opens the article it belongs to.

**Open it yourself. The key is the whole credential.**
 Read key: `sgit_public_read_02e541ca5f9aec53b4f7242ce1c9c801e10749cd48907457aa8d6023c211d6f9:kd0xhy6z`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_public_read_02e541ca5f9aec53b4f7242ce1c9c801e10749cd48907457aa8d6023c211d6f9%3Akd0xhy6z)
 From the CLI: `sgit clone sgit_public_read_02e541ca5f9aec53b4f7242ce1c9c801e10749cd48907457aa8d6023c211d6f9:kd0xhy6z`
This key is published on purpose, under the `sgit_public_read_` prefix. It is **derived** one way from a vault key that is kept in the gitignored tier and never published. `check_credential.py` classifies it as read-only and safe to publish. A clone with it can read every file and change none; the write key stays with the author.

## See it live, here

The vault opens as an app. Pick a view on the left: the overview, the timeline, the ledger, the corrections, the dependencies, the evidence fractal, the record, the files and versions. You can also [open it in the official UI](https://dev.vault.sgraph.ai/#sgit_public_read_02e541ca5f9aec53b4f7242ce1c9c801e10749cd48907457aa8d6023c211d6f9%3Akd0xhy6z).

## What was derived, and from what

The source is the Claude Code session that has run this site since 11 August 2026, read from 9 September to 18:50 on 5 October: 19,899 events, parsed for the author's messages, the agent's prose and tool calls, the research agents it launched and the times its context was compacted. The transcript itself is private and is not in the vault; the derived rows are, and the two scripts that derived them are in `tools/`. The second source is the site's git history, read for every commit in the window and every version of every article. The third is the articles themselves and the graph file beside each. Nothing was typed in by hand except the catalogue of corrections, which is marked as such, and the fractal of the article's own argument.

Attribution of a message to an article is exact for the nine articles checked by hand, with the message ids listed, and a stated heuristic for the rest. A hundred and four of the 266 rows feed vaults, pages and the site rather than any article, and are left unattributed rather than forced. Two numbers in the article's first version were corrected by this data: the session's context was compacted eleven times, not twenty-two, and the message count had included rows the client injects when the agent reads a screenshot. The vault keeps both counts.

## What is in it

timeline

### Twenty-seven days, as words and releases

Per day: what the author sent, with the long memos in dark teal, and what the agent wrote back in blue, with amber ticks for the 123 releases labelled by version, red diamonds for the eleven compactions and black dots for the days an article went out. Twenty releases on 21 September, nineteen on 2 October, five silent days, and a 143-hour gap in the second week.

The timeline view.

ledger

### One row per article, with the messages behind it

Words in against words out, turns, memos, rounds and figures for every article in the window, with a badge saying whether the input was attributed by hand or by the heuristic. Open a row and the messages themselves are listed with their kind and first line, beside the releases that touched the article, and a note where the article's published ledger and the vault's count differ.

The ledger, opened on one article.

corrections

### Twenty-eight corrections, and how long each waited

The catalogue from the article, one card each, grouped by kind, with the fifteen that became rules marked. Beside it, the latency: a median of thirty-eight minutes from a release to the author's next correction of the same article, and of five minutes from the correction to the release that carried it, with the twenty attributed correction turns as dots on a log scale.

The corrections view.

dependencies

### Who references this, three levels deep

The twenty-nine articles in date order round a ring, sized by how many cite them, teal edges back in time and amber edges forward. Click one and the panel shows what it builds on and what continued it, one, two or three hops out, with mention counts, and under that the article's own semantic graph nodes grouped by kind. The fractal semantic graphs article has ten articles standing on it and stands on none.

The dependencies view, focused on the most-cited article.

evidence

### The article as a fractal: strategy to data

Five columns: the three things the article argues for, the six concepts its sections develop, the thirteen claims in its summary list, the twenty-eight pieces of evidence those claims rest on, and the fourteen data files the evidence is derived from. Click any node and its paths light up and down, and a trace panel lists the chain from a claim to the file and field that measures it.

The evidence view, with one claim traced to its data.

files and versions

### Every file, every version, and the diff between any two

A viewer for the data files as tables and collapsible JSON, the seventy-five saved versions of twenty-two articles as markdown, and a diff between any two versions of an article, paragraph by paragraph, the same algorithm as the site's diff pages. The provenance captures sit beside them: each cited source as fetched on 5 October, with its HTTP status, byte length, SHA-256 and a screenshot of its first screen.

The files view, comparing two versions of the article.

**Fixed the same evening.** The first push of this vault routed its views on the browser's hash, which inside the vault host does nothing, so every view link was dead there; a parallel session found it, the rule is now in [the vault-app guidance](../../../docs/vault/vault-apps.md), and the app was re-pushed with the route held in a variable and the host's minimal chrome. A fresh read-only clone carries the fix; the version in the vault's own file viewer is the first one.

## What to connect next

The messages are attributed to articles; they are not yet attributed to the vaults, pages and business plans the other hundred and four fed, which is the next ledger. The corrections are a hand-written catalogue; the next pass has a model propose them from the turns and a person confirm each. The evidence fractal is one article's; the same five columns could be built for every article from its graph file. And the brief for the due diligence article arrived as an uploaded transcript rather than a typed message, which the parser cannot see, so that article shows no input; the next version of the parser reads uploads.

## Read the article

[**How much of this did I write? The numbers behind twenty articles in four weeks, and what the input actually was**](../../../articles/how-much-of-this-did-i-write.md). The argument, the figures and the corrections, with the vault as its evidence.


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/how-much-evidence/index.html)*
