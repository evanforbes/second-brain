---
name: ua-daily-report
description: Use when Evan asks for a rollup of his day. Trigger phrasings include "EOD report", "what did I do today", "daily report", "run my daily", "wrap up today", "what happened today", "condense today". Pulls the day from Slack, Gmail, Google Calendar, Hex, and AppsFlyer and writes one dated note to daily/. Its main job is keeping Claude's context current for tomorrow and for the weekly channel review.
---

# UA Daily Report

Writes `daily/YYYY-MM-DD-ua-daily.md` from `templates/daily.md`. Window: today, midnight to now, local time.

## Before starting

Check which connectors are actually available in this session. **Skip any that are missing, say so in one line, and list only the ones used in `sources`.** Never fill a section from memory or guesswork. This skill was written on the personal machine before any connector existed; it activates on the work machine.

## Sources

- **Google Calendar:** today's meetings. Note which recurring meetings happened (COO 1:1, creative sync, team standup, channel rep calls) and link any `meetings/` note for them.
- **Slack:** messages Evan sent or was mentioned in, plus the UA and creative channels. Extract decisions, asks of Evan, test launches and verdicts, and budget changes.
- **Gmail:** today's threads with channel reps, partners, and leadership. Commitments made and received, beta or policy news from platforms.
- **AppsFlyer and Hex:** only for tests with `status: live` or `read-out` in `tests/`. Note which moved. Record direction relative to incumbent, not absolute figures.

## What to extract

- Action items assigned to Evan, with due dates.
- Asks from the COO, CEO, leadership, the creative team, and Evan's managers and associate. Roles only, never names.
- Decisions made, especially budget moves. Offer a [[decision-log]] entry for each.
- Test status changes. Offer to update the matching `tests/` note.
- Anything that contradicts what the vault already believes, with a link to the note it contradicts.

## Output rules

- One file per day. **A same-day re-run merges into and improves that file; never create a second one.** This is the only permitted edit to an existing daily note. Once the day is over, it is append-only.
- Obey `CLAUDE.md` section 7a: no names, no real spend or CPFTD figures, no player-level data, nothing about the external job search.
- Keep it scannable. Bullets, not prose.

## Close-out

1. Offer `MEMORY.md` promotions for open threads and facts.
2. Commit quietly: `git add daily/ && git commit -m "daily: YYYY-MM-DD"`. **Never push.**
