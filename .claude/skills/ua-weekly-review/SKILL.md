---
name: ua-weekly-review
description: Use when Evan needs the weekly channel-level performance review or a COO update. Trigger phrasings include "weekly channel review", "draft my COO update", "what happened last week", "condense last week", "weekly review", "how did UA do this week", "what's working and what's not". Rolls up the week's daily notes, tests, meetings, and decision log into one note in weekly/.
---

# UA Weekly Review

Writes `weekly/YYYY-MM-DD-channel-review.md` (week-ending date) from `templates/weekly.md`. Default window: the last 7 days. If Evan asks for a mid-week COO update, use the days since the last review and say which window was used.

## Sources

1. `daily/` notes in the window. These are the primary input.
2. `tests/` notes whose `updated` falls in the window: verdicts reached, tests launched.
3. `meetings/` notes in the window, especially the COO 1:1 and creative sync.
4. [[decision-log]] entries in the window.
5. If connectors are available: Slack and Gmail for anything the dailies missed, and AppsFlyer / Hex for the current channel-level trend. Skip any connector that is missing and say so.

## Structure

- **Headline:** two or three sentences the COO can read alone.
- **By channel**, in priority order (TikTok, Meta, Snapchat, Google, Reddit, Apple Search Ads, Liftoff, Moloco, RZR), for each channel with activity: what is working, what is not, what we are doing about it. Judge on CPFTD first. Skip channels with nothing to report rather than padding.
- **Tests:** verdicts this week (link each), launches next week.
- **Budget moves:** link decision-log entries.
- **Risks and asks.**

## Rules

- Direction and relative change only in the file; no real spend or CPFTD figures (CLAUDE.md 7a). If Evan wants numbers for the actual send, pull them live and show them in chat.
- Platform-reported results are labeled as such; do not present them as incremental.
- Roles only, never names.

## Close-out

Offer to add new lines to [[learnings]] for tests concluded this week. Commit quietly. Never push.
