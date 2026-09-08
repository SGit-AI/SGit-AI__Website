---
id: T2
title: Re-verify the 21 published read keys with the marker that actually discriminates
kind: task
status: backlog
role: auditor
priority: high
opened: 2026-09-07
---
The earlier 24-key sweep used the presence of `.sg_vault/` as success, which an all-zeros key also produces. Three vaults were verified properly by decrypting content; the other 21 were not. Re-run with `clone_mode.json` as the marker and a negative control.
