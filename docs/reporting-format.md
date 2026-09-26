---
title: Reporting Format
type: doc
status: living
created: 2026-09-26
updated: 2026-09-26
owners: [evan]
tags: []
last_verified: 2026-09-26
verified_by: evan
related: ["[[decision-log]]", "[[ua-weekly-review]]", "[[ua-daily-report]]", "[[measurement-principles]]"]
references: []
---

## Summary

How performance data is presented, whether answering Evan's questions, drafting COO or leadership updates, or writing the weekly review. **Every lever is reported as a closed loop: Saw → Did → Expected → Happened → Call.** No block without a call.

## The lever block

```
Saw: [the signal that triggered the move, with the number]
Did: [the change, sized: e.g. moved $X from A to B]
Expected: [what we said would happen, with a number and a date]
Happened: [yes / no / partial, with the actual number]
Call: [MAINTAIN / CHANGE] - [what we do next week]
```

- **Saw:** a specific signal with a number, never "performance softened."
- **Did:** always sized: amount, channels, window.
- **Expected:** a number *and* a date. This is what makes Happened checkable. If no expectation was set, say "no expectation set" and set one now.
- **Happened:** starts with **yes / no / partial**, then the actual number. If it's too early to tell, write "pending: check [date]."
- **Call:** exactly **MAINTAIN** or **CHANGE**, then the next action.

## The five levers, and how often each is reported

| # | Lever | Cadence | Saw is typically… | Did is typically… |
|---|---|---|---|---|
| 1 | **Mix, channels** | Daily | Channel CPFTD or volume signal | Budget shift between channels, sized |
| 2 | **Creative (live and in test)** | 1–2× a week | A winner, a fatigue signal, or a test result | Scaled, killed, or launched |
| 3 | **Day parting** (island games) | As needed | Hour or day-of-week efficiency gap | Schedule change, by channel |
| 4 | **Pulse** (incremental spend pushes) | Event-driven | An event, slate, or moment driving demand | Pulse size, channels, window |
| 5 | **State levers** | 2× a week | State-level performance, supply, or regulatory change | Geo weighting, on/off, reallocation by state |

For a **Pulse**, Happened must also cover **any post-pulse hangover.**

## Watch list

Every report ends with a watch list. Each item has **an owner (by role) and a decision date.**

```
WATCH LIST
- [thing, owner, decision date]
```

## Rules for answering questions

1. **Lead with the call.** If Evan asks "how's Snap doing?", answer with the relevant lever block(s), not a narrative. Include only the levers that moved; skip empty ones.
2. **Every number carries its layer and its window:** platform, AppsFlyer, warehouse (Hex), or incremental, plus the date range. For example: "CPFTD (Hex, Sep 15–21)." Platform-reported numbers are labeled as such (see [[measurement-principles]]).
3. **Say when data is provisional.** The last 3 days of SSOT, SKAN windows, and cost restatements (see [[appsflyer-discrepancies]]).
4. **Tie it to the evidence.** When a Call relies on an experiment or a case study, link it: [[decision-log]], [[measurement-case-studies]], or a `tests/` note.
5. **Non-performance questions** (how a platform works, policy, setup) get a direct answer with source links, not lever blocks.

## Numbers in chat vs. in files

The format calls for real numbers, and **in chat it uses them**, pulled live from Hex, AppsFlyer, or the MCP connector. **Files in this vault use relative figures** (for example, "CPFTD ~12% better vs. prior week") until CLAUDE.md 7a is lifted on the work machine. At that point, files switch to real numbers too.

## Where the format is used

- **Chat answers** to performance questions.
- [[decision-log]] entries: one lever block per budget move.
- The `weekly/` channel review, via [[ua-weekly-review]], and the daily Mix block, via [[ua-daily-report]].
- COO and leadership update drafts.
