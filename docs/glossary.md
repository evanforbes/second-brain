---
title: Glossary
type: doc
status: living
created: 2026-09-26
updated: 2026-09-26
owners: [evan]
tags: []
last_verified: 2026-09-26
verified_by: evan
related: []
references: []
---

## Summary

Every acronym, internal tool name, and piece of shorthand used in this vault, plus the allowed tags. New terms and tags get added here in the same change that introduces them.

## Metrics

| Term | Meaning |
|---|---|
| UA | User acquisition: paid media that brings in new users |
| FTD | First-time deposit: the first valid, approved deposit per user, from the internal model (the financial source of truth) |
| CPFTD | Cost per first-time deposit: spend divided by attributed FTDs. The primary metric |
| CAC | Customer acquisition cost |
| iCAC | Incremental CAC, measured by a holdout or lift test rather than attribution |
| CPI | Cost per install |
| IPM | Installs per thousand impressions: a creative's install efficiency |
| CPM | Cost per thousand impressions |
| CTR | Click-through rate |
| Scale | How much spend a creative or campaign absorbs while holding efficiency. A key creative metric |
| ROAS | Return on ad spend. Platform-reported ROAS is operating data, not truth |
| D7 / D30 ROAS | ROAS over the first 7 or 30 days. Secondary for now |
| Payback | Time for a cohort's value to recover its acquisition cost. Secondary for now |
| NGR / GGR | Net / gross gaming revenue |
| D7, D28, D90, D365 | Cohort value windows, measured from the FTD date |
| Incumbent | The current top-performing creative on a channel that a challenger must beat |
| Challenger | A new creative or concept tested against the incumbent |
| KYC | Know your customer: identity verification before a user can deposit |

## Measurement and tooling

| Term | Meaning |
|---|---|
| AppsFlyer | The MMP. Primary source for attribution and creative reporting |
| MMP | Mobile measurement partner (AppsFlyer, Branch) |
| Branch | An MMP / deep-linking provider |
| Hex | Data notebooks and dashboards over the warehouse. Primary internal data source |
| Sigma | Secondary BI tool, occasional use |
| BigQuery | The data warehouse |
| dbt | Transformation layer that builds warehouse models |
| Amplitude | Product analytics |
| Hightouch (`ht_*`) | Reverse-ETL that delivers backend events to platforms and AppsFlyer |
| SKAN | Apple SKAdNetwork: private, delayed, aggregated iOS attribution |
| CV | SKAN conversion value (fine and coarse) |
| SSOT | AppsFlyer Single Source of Truth: dedupes SKAN and MMP attribution |
| S2S | Server-to-server events |
| CAPI | Meta Conversions API: server-side events to Meta |
| Pixel | Browser-side conversion tag (Meta and others) |
| OneLink / Smart Script | AppsFlyer links that carry web campaign parameters into the app store journey |
| VTA | View-through attribution: credit for an impression without a click |
| Web-to-app | Ad → website → app store → install path; attribution breaks without OneLink / Smart Script |
| MMM | Marketing mix model: channel contribution and response curves for allocation |
| Holdout / geo lift | Turning spend off in matched markets to measure incremental effect |
| Measured | Third-party incrementality testing vendor |
| INCRMNTAL | Always-on incrementality model vendor |
| Protect360 | AppsFlyer fraud protection |
| Andromeda | Meta's ad retrieval system; post-Andromeda, creative does most of the targeting |

## Channels and buying

| Term | Meaning |
|---|---|
| ASA | Apple Search Ads |
| DSP | Demand-side platform: programmatic buying (Liftoff, Moloco, RZR) |
| Liftoff | Programmatic mobile DSP |
| Moloco | Programmatic mobile DSP |
| RZR | Programmatic mobile DSP, formerly Aarki. Either name refers to the same partner |
| tCPA / tROAS | Google target CPA / target ROAS bidding |
| AC · Installs / AC · Actions | Google App campaign optimization tiers |
| PMax | Google Performance Max |
| rMAX | Reddit campaign optimization beta |
| Pangle | TikTok's ad network (placement beyond TikTok itself) |
| RAF | Refer-a-friend |

## Business and market

| Term | Meaning |
|---|---|
| Prediction markets | Underdog product where users trade on event outcomes. A focus product |
| Fantasy | Underdog's daily fantasy products (including Pick'em). A focus product |
| Pick'em | Fantasy format where users pick over/under on player stats |
| Real-money gaming | The regulated category Underdog competes in |
| Kalshi | Competitor, prediction markets |
| Polymarket | Competitor, prediction markets |
| FanDuel | Competitor, sportsbook and fantasy |
| DraftKings | Competitor, sportsbook and fantasy |

## Tags

Flat, lowercase, hyphenated. Only these, until a new one is added here.

- Products: `prediction-markets`, `fantasy`
- Channels: `tiktok`, `meta`, `snapchat`, `google`, `reddit`, `apple-search-ads`, `liftoff`, `moloco`, `rzr`
- Test types: `creative`, `offer`, `landing-page`, `app-store`, `experiment`
