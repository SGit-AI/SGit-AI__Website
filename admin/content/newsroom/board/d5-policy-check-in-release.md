---
title: Run the policy check inside release.sh when a role is named
id: D5
status: backlog
role: developer
opened: 2026-10-07
---
`admin/build/policy_check.py --role <role>` exists and is run by hand. A `ROLE=` environment variable read by `release.sh` would make it a gate rather than a habit.
