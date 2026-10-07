---
title: Point the subscriber agents at the wire
id: D3
status: doing
role: developer
opened: 2026-10-07
---
`newsroom/wire.json` carries every article with its placement, teaser, topics and graph link, every desk note and every collection. The agents that write to subscribers should read it rather than scrape pages. Next: a per-topic slice, and a `since` cursor so an agent asks only for what is new.
