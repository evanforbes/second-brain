---
title: Measurement Principles
type: doc
status: living
created: 2026-09-26
updated: 2026-09-26
owners: [evan]
tags: []
last_verified: 2026-09-26
verified_by: evan
related: ["[[user-value-architecture]]", "[[attribution-paths]]", "[[incrementality-and-mmm]]", "[[measurement-case-studies]]", "[[appsflyer-discrepancies]]"]
references: []
---

## Summary

The operating philosophy behind every UA measurement call at Underdog. When a platform number, a model, and an experiment disagree, these principles decide. Source: Evan's measurement document (Sep 2026).

## Principles

1. **Instrument → learn → automate → scale, in that order.** Running it backwards means spending month six untangling month one.
2. **Optimize to the customer, not the install.** Platforms buy whatever you call a conversion. Define the deep value event (a funded, active account, meaning the FTD), and send it clean, server-side, with real values.
3. **Attribution = who gets credit. Events = what happened. Warehouse and P&L = what it was worth.** Three separate layers, never collapsed into one.
4. **Platform ROAS and reported CPA are not incremental CAC.** Never scale on platform ROAS.
5. **One canonical event per funnel stage.** Never sum SDK, S2S, and Hightouch equivalents. Legacy variants are for QA only.
6. **Triangulate:**
   - MMP attribution, to operate campaigns
   - incrementality and holdouts, to answer "did spend cause growth?"
   - MMM, for allocation at scale

   **When layers conflict, the experiment wins,** and the conflict tells you where to test next.
7. **"Dashboards operate campaigns; experiments move money."**
8. **Signal integrity is the through-line:** clean value events, independent causal reads, agentic operating leverage, and budget decisions that survive an audit.
9. **Brand and search-brand get the most scrutiny, not the least.** They harvest demand other media created.
10. **Own the objective function.** A black box that decides budget is a liability if you can't debug it.
11. **Do it by hand until you understand it cold, then automate it.** Never the reverse.
12. **The first read is not the truth.** Early-window metrics (D2/D7) can reverse as cohorts mature. See [[measurement-case-studies]].
13. **A fast wrong number is more dangerous than a slow right one.** Protect the integrity layer (anomaly detection, a single source of truth for reporting) before optimization tooling.

## Three conversion numbers people conflate

| Number | What it is | Use |
|---|---|---|
| Platform-attributed | Credit the platform claims | In-channel operation only |
| Directly observed (promo codes, self-reported attribution) | Real but incomplete | A floor and a sanity check |
| Incremental (from a valid holdout) | What the spend caused | **The only one that answers a budget question** |

A flat CPA can hide falling deposit size or worse retention. Flat CPA with declining value is a worse business wearing the same number.

## What this means day to day

- Label every number with its layer when reporting: platform, AppsFlyer, warehouse, or incremental.
- A cheap channel is a hypothesis until a holdout confirms it. Log the decision in [[decision-log]].
- See [[appsflyer-discrepancies]] for why the layers differ.
