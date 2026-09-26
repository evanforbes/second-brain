---
title: UA Weekly Review Routine
type: doc
status: living
created: 2026-09-26
updated: 2026-09-26
owners: [evan]
tags: []
last_verified: 2026-09-26
verified_by: evan
related: ["[[ua-daily-report]]", "[[decision-log]]"]
references: []
---

## What it does

- Rolls up the week's `daily/`, `tests/`, `meetings/`, and [[decision-log]] into one channel-level review for the COO.
- Writes `weekly/YYYY-MM-DD-channel-review.md`.
- Offers new [[learnings]] lines for concluded tests, then commits locally. Never pushes.
- Works from vault notes alone; uses connectors when they are available.

## How to run it

Paste into a fresh Claude session:

```
Working directory: /Users/evanforbes/Documents/GitHub/second-brain
Run the ua-weekly-review skill for the week ending today.
```

For a mid-week COO update: "Draft my COO update since the last review."

## How to disable it

Stop pasting the prompt. Nothing runs in the background.

## Troubleshooting

(Fill in the first time it misbehaves.)
