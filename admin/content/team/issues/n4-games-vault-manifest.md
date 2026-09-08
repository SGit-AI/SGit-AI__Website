---
id: N4
title: The games vault: one manifest line so the telemetry actually sends
kind: need
status: needs
role: publisher
priority: medium
opened: 2026-09-07
---
The other agent's fix is `{"permissions": {"append": {"write": true}}}` and a switch to `sg.append.write` — not `network: true`. When it lands, the page's status note comes off and the two 'nothing sent' footers should be gone. Unblocks: the [games vault page](/demos/vaults/agent-permission-games/index.html) describing behaviour the vault performs.
