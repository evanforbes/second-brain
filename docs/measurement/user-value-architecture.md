---
title: User Value Architecture
type: doc
status: living
created: 2026-09-26
updated: 2026-09-26
owners: [evan]
tags: []
last_verified: 2026-09-26
verified_by: evan
related: ["[[measurement-principles]]", "[[appsflyer-events-and-s2s]]", "[[appsflyer-reporting-and-data]]"]
references: []
---

## Summary

How a CAC decision is actually produced. **A CAC decision is the output of several separate systems reconciled at cohort grain.** There is no single "install → deposit → CAC target" event. The warehouse (BigQuery) stitches independent evidence streams into a governed reporting model, which Hex reads. Internal table names are deliberately left out (CLAUDE.md 7a).

## The evidence streams

| Stream | Answers |
|---|---|
| AppsFlyer | Who drove the install |
| Internal FTD model | A valid first deposit |
| Spend | What acquisition cost |
| User economics (settled NGR) | What the user generated |
| D365 forecast | Eventual value |
| CAC target | Allowable cost |

## Layers

Raw sources (app databases, AppsFlyer, ad spend, payments, entries, Amplitude) → staging (rename, cast, parse, normalize timestamps, keep source grain) → intermediate (business logic, dedupe, identity resolution, grain control) → gold marts (users, first-time deposits, marketing spend, entries) → reporting (daily performance, then weekly KPIs) → Hex.

**Golden rule: aggregate facts before joining to users.**

## Identity: an AppsFlyer install is not an Underdog user

- A bridge table maps AppsFlyer ID and install to an Underdog user ID.
- It's **incomplete by design:** ATT opt-outs, multi-device use, and reinstalls. **Ambiguous mappings are nulled, never guessed.** SSOT and SKAN help aggregate reporting, not user-level truth.
- **Use the user ID for value. Use AppsFlyer for acquisition evidence.**

## How a deposit becomes an FTD

Deposit request (KYC, eligibility, processor checks) → approved transaction → **canonical FTD = the first valid approved deposit per user** → attribution waterfall (**partner/RAF → AppsFlyer paid → organic fallback**) → one FTD row per user.

- The deposit *amount* doesn't set CAC. It marks entry into the customer cohort.
- **Actual CAC = acquisition spend ÷ attributed FTDs.**
- AppsFlyer deposit events are marketing signals. The internal model is the financial truth.

## Spend is its own stream

Spend comes from each platform, the DSPs, affiliates, and RAF cost, at date × channel × campaign × state grain. **Never infer spend from deposits, installs, or event values.** Spend and FTDs are joined only at the agreed cohort grain.

## Value from settled economics

- NGR is calculated in the warehouse from transactions (entries, settlement, payouts, promo recognition), **not imported as AppsFlyer revenue.**
- **Daily user NGR = settled business revenue − recognized promo costs + expirations/clawbacks.**
- **Cohort windows:** D7, D28, D90, D365, D720 from the FTD date.
- **The core user-value table** holds FTD cohort identity (user, FTD date, source, campaign, state), observed value by window, and decision outputs (projected D365, actual CAC, projected ROAS, target CAC).

## From value to CAC

- **Projected ROAS** = projected NGR per FTD ÷ CAC.
- **Target CAC** = projected D365 NGR per FTD ÷ required ROAS. Forecast value first, then apply the return hurdle.
- **Current projection method:** prior-year matured D365 NGR per FTD × (1 + a recent D28 quality adjustment, with recency weights over recent weeks).
  - It's a planning estimate, not realized revenue.
  - **Watch-out:** D28 theo includes Pick'em and prediction markets, so periods spanning the prediction-markets launch aren't apples to apples.
- **The payback target is hard-coded upstream**, not inferred from ROAS.
- **Preferred rebuild:** observed D28 actual plus a forecast for D29–D365. Train on mature cohorts, use rolling time-based backtests, and use base and downside ranges for CAC decisions.

## Why numbers change after the fact

AppsFlyer and SKAN lateness, deposit approval vs. creation timing, settlement and payout timing, promo recognition and expirations, attribution restatements, and refunds. **Recent days are provisional.**

## Status

About 90% specified. Still open: exact source schemas, a finance-approved NGR definition, promo and RAF recognition rules, a channel-level spend source of truth, IAM/PII mapping, and scheduler details.
