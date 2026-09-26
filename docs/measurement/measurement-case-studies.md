---
title: Measurement Case Studies
type: doc
status: living
created: 2026-09-26
updated: 2026-09-26
owners: [evan]
tags: [experiment]
last_verified: 2026-09-26
verified_by: evan
related: ["[[measurement-principles]]", "[[incrementality-and-mmm]]", "[[tiktok]]", "[[snapchat]]", "[[apple-search-ads]]", "[[meta]]"]
references: []
---

## Summary

Lessons Underdog has already paid for, told as patterns. Relative results only; exact figures stay out of the vault for now (CLAUDE.md 7a). Cite these when a similar situation comes up.

## The model said cut; the experiment said scale (TikTok)

- **Situation:** the model flagged [[tiktok]] as much more expensive than average, a "cut it" signal.
- **Test:** a five-week geo holdout. TikTok went dark in markets covering most of its spend, against matched controls, comparing actual with predicted FTDs.
- **Result:** TikTok drove a meaningful share of total FTDs incrementally, with high confidence, at an incremental CAC well below blended.
- **Lesson:** the experiment overruled the model, and budget scaled. A Meta holdout on the same framework also showed confident lift (see [[meta]]).

## The first read was wrong (Snapchat)

1. **Act one:** an early holdout showed no significant lift, and D2/D7 looked weak. By the playbook, that means cut.
2. **Act two:** diagnosis. The account was heavy on Story Ads, an impression-led path. Moving to native Snap Ads multiplied CTR and click-to-install.
3. **Act three:** an independent retest came back well above program-average FTD efficiency. During a relaunch, Snap delivered a large share of FTDs on a small share of spend.

**Mechanism:** D14–D60 cohort maturation flipped the read. A slightly pricier, younger user was the cheapest customer on lifetime value. **Lesson: diagnose before you cut, and don't judge on early windows.** See [[snapchat]].

## Brand drift (Apple Search Ads)

- A measured [[apple-search-ads]] cell in a set of smaller states drifted brand-heavy, harvesting demand that other media created.
- It was paused, and Apple's view-through proposal was rejected as over-crediting.
- **Lesson:** brand and search-brand get the most scrutiny.

## Partner-level truth (affiliates)

- The first affiliate incrementality test was invalidated when Black Friday contaminated the baseline. It was documented, not forced, and rerun later as a four-cell, partner-level test.
- **Result:** two partners showed lift at very different true costs per caused FTD (one about 4× the other, despite similar headline CACs). Two showed no detectable effect.
- **Action:** scale one, renegotiate one, pause and retest two.
- **Lesson:** aggregate affiliate CAC is meaningless. Negotiate holdout rights and unique promo codes before signing, and treat a refusal to be measured as a signal.

## Too good to be true (CTV partner)

- A CTV partner reported CPI and CPA far better than target, and the room wanted to scale.
- It was held for independent validation (DS plus Measured) on the three ways CTV numbers inflate: **view-through inflation, audience overlap, attribution leakage.**
- **Lesson:** any number big enough to move budget has to survive validation, whether that vindicates it or kills it.

## Timing is not credit (INCRMNTAL audit)

- The always-on model was audited against the experiment-calibrated MMM (same ledger, taxonomy, and window).
- They agreed closely on *when* outcomes moved but disagreed sharply on *who* got credit. The model pushed organic baseline demand into always-on, high-impression channels.
- **Lesson:** timing correlation isn't credit validity. Model output is a hypothesis; budget moves need an experiment.

## Agents need priors (anomaly detection)

- The reporting and anomaly agent over-flagged predictable seasonality (Super Bowl pacing) as emergencies.
- It was fixed with priors for "normal" by event, daypart, and season.
- **Lesson:** agents need a human-set baseline, or they cry wolf and the team stops listening.
