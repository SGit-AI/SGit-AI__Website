# Article graphs

One JSON file per article, `<slug>.json`, beside this file. The build reads them to
produce the article cards (teaser, topics, image), the per-article "threads" block,
the graphs page, and the newsroom view. They are the semantic graph of each article:
its core ideas, the concepts it rests on, and how it connects to the rest of the site.

The file is written by the agent that wrote or revised the article and is reviewed
by a person. It must not restate facts the article does not contain. Every `links`
entry must be a link that actually appears in the article's markdown.

## Schema

```json
{
  "slug": "footprint-and-blast-radius",
  "teaser": "One sentence, at most 160 characters, plain, no claims of firsts or of what nobody has done.",
  "topics": ["agents-and-policy"],
  "core_idea": "One sentence stating the article's central idea in the article's own terms.",
  "nodes": [
    {"id": "footprint", "label": "Footprint", "kind": "concept",
     "summary": "What the agent actually did, read afterwards from logs."}
  ],
  "edges": [
    {"from": "footprint", "to": "mandate", "rel": "compared-with"}
  ],
  "links": {
    "articles": ["ultimate-insider-three-collisions"],
    "pages": ["/demos/vaults/kit-bag/index.html"],
    "sites": ["https://riskmandate.ai/abp.html"]
  },
  "quotes": [
    {"text": "A sentence quoted verbatim from the article.", "why": "Why this line carries the argument."}
  ]
}
```

### Topics (fixed list; one or two per article)

| id | means |
|---|---|
| `agents-and-policy` | agents, behaviour policies, permissions, insider risk, RiskMandate |
| `vaults-and-method` | sgit, vaults, the publishing method, proofs and audits, the site's own practice |
| `news-and-evidence` | newsrooms, evidence, claims, story vaults, the token bill |
| `startups-and-strategy` | business models, pricing, open source, investors, early access |
| `graphs-and-knowledge` | fractal semantic graphs, altitudes, memory, interfaces built from graphs |
| `site-and-engineering` | how this site and its network are built, performance, deploy |

### Node kinds

`concept` (a named idea), `claim` (something the article asserts), `method` (a way of
doing something), `artefact` (a vault, page, tool or document the article points at),
`example` (a worked case or incident), `question` (left open by the article).

### Edge relations

`extends`, `depends-on`, `compared-with`, `contrasts`, `produces`, `example-of`,
`answers`, `leads-to`. Edges run between node ids in the same file. Cross-article
relations go in `links.articles`, not in `edges`.

### Size

Eight to sixteen nodes. Ten to twenty-four edges. One or two quotes. The graph is a
map of the argument, not an index of every noun.
