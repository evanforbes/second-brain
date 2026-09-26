---
title: Incrementality, MMM, and the Measurement Hierarchy
type: doc
status: living
created: 2026-09-26
updated: 2026-09-26
owners: [evan]
tags: [experiment]
last_verified: 2026-09-26
verified_by: evan
related: ["[[measurement-principles]]", "[[measurement-case-studies]]", "[[appsflyer-incrementality]]", "[[decision-log]]"]
references: []
---

## Summary

**Attribution assigns credit; incrementality estimates causality.** Budget decisions are anchored to experiments. Attribution is used only to operate campaigns.

## The four-layer hierarchy

| Layer | Tool at Underdog | Job |
|---|---|---|
| 1. Causal validation | Geo holdouts and lift tests (including Measured) | The truth anchors |
| 2. Response curves | Experiment-calibrated, in-house Bayesian MMM (built with DS) | Allocation, saturation, marginal return |
| 3. Always-on monitoring | INCRMNTAL | Hypotheses and trend alerts |
| 4. In-channel operations | AppsFlyer and platform attribution | Running campaigns day to day |

**When layers conflict, the experiment wins,** and the conflict says where to test next. Also see AppsFlyer's own geo-experiment product: [[appsflyer-incrementality]].

## MMM

- It breaks outcomes down into baseline, channel contribution, seasonality, promos, and external factors, with marginal response curves.
- **It's for strategic allocation, not daily optimization.**
- **Underdog's model:** daily FTDs broken into baseline, channel effects, and external factors, for contribution and cost-per-FTD by channel. **It's being migrated from optimizing FTD counts to longer-horizon revenue quality** (a D30 fees view).
- **Build for MMM-readiness:** consistent taxonomy, weekly spend and outcome history, geo and channel tags, cohort value events, promo flags, clean exclusions.
- **Danger: fake precision.** "Directional, not causal yet" beats a beautiful model the data can't support.

## Running holdouts

- **Geo design:** dark markets against matched controls, actual vs. predicted FTDs, over a powered multi-week window. Pre-register the hypothesis and the decision threshold.
- **Holdouts cost volume.** Run them when the decision is big enough. The end state is periodic experiments calibrating an always-on layer, not permanent holdouts.
- **Partner-level reads.** Aggregate affiliate or partner CAC is meaningless. Measure each partner with its own holdout cells.
- **Contamination** (Black Friday, a tentpole event, a promo) invalidates a read. Document it and rerun rather than forcing a conclusion.

## Low-volume methods

For new channels, small states, or new products:

- Deterministic instrumentation first (server-side events, one source of truth).
- **Self-reported attribution** at onboarding.
- **Switchback and time-based on/off tests** instead of geo splits.
- Fewer, larger geo units, with the minimum detectable effect widened honestly.
- **Bayesian priors** from experience across accounts, updated as thin data arrives.
- Be willing to say "we can't separate this from noise yet — here's what we're steering on until we can."

## Platform lift studies

- **Useful as hypothesis generators, never as the basis for allocation.** The platform grades its own homework.
- Take the betas and the access from reps, **not the measurement verdict.** Their study generates the hypothesis; an independent experiment moves the money.

## Governance

- **Every model output is a hypothesis. Moving budget requires an experiment behind it.**
- Put the rule in the process, not in a person, so it survives busy weeks and convincing dashboards.
- Log every budget move and its evidence in [[decision-log]].
