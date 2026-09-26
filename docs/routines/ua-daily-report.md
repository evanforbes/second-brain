---
title: UA Daily Report Routine
type: doc
status: living
created: 2026-09-26
updated: 2026-09-26
owners: [evan]
tags: []
last_verified: 2026-09-26
verified_by: evan
related: ["[[ua-weekly-review]]"]
references: []
---

## What it does

- Pulls today from Slack, Gmail, Google Calendar, and (for live tests) AppsFlyer and Hex.
- Writes or improves one note: `daily/YYYY-MM-DD-ua-daily.md`.
- Extracts action items, asks from leadership and the team, decisions, test status changes, and contradictions with the vault.
- Offers memory promotions and decision-log entries, then commits locally. Never pushes.

## How to run it

Not active until connectors are set up on the work machine. Then paste this into a fresh Claude session:

```
Working directory: <absolute path to this vault on the work machine>
Run the ua-daily-report skill for today.
```

## How to disable it

Stop pasting the prompt. Nothing runs in the background.

## Scheduling later

Once it runs cleanly for a week or two, it can move onto a schedule so it runs while the machine is awake. Describe the task, have Claude write the prompt, and paste that into the scheduler.

## Troubleshooting

(Fill in the first time it misbehaves.)
