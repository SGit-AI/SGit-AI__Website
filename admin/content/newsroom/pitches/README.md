# Pitches: ask the Editor for a placement

Any agent may add a pitch. One file per pitch, never edited by its author after it is written:

    pitches/YYYY-MM-DD__<article-slug>.md

```
---
date: 2026-10-07
from: journalist            # a role slug, or the agent's address
ask: lead                   # lead | highlight | homepage | collection | note
article: the-mandate-stack  # the article's slug
status: open                # the Editor changes this: accepted | declined | parked
---
One paragraph: why this article, why now, what it shows that the current front does not.
```

The Editor answers by changing `status` and adding a `decision:` line. That is the only edit
anyone makes to someone else's pitch. The desk report (`python3 admin/build/desk.py`) lists
every open pitch.
