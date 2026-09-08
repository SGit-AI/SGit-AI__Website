---
title: The chat pane inside a vault: route through sg.llm instead of a pasted key
id: T11
kind: task
status: backlog
role: designer
priority: medium
opened: 2026-09-07
---
The pane (`assets/site-chat.js`) has three tiers and the third is not wired: when a page renders inside a vault, `sg.llm.chat` would let the host hold the key below the permission floor. Blocked on one fact — whether the bridge's chat contract accepts OpenAI-style `tools` and returns `tool_calls`. Ask llms.sgit.ai's owners; until then the pane falls back to the key-in-page tier with the warning it already carries.
