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
| Lever block | Saw / Did / Expected / Happened / Call: the standard reporting unit. See [[reporting-format]] |
| MAINTAIN / CHANGE | The only two allowed Calls in a lever block |
| Mix | Lever 1: budget allocation across channels (daily) |
| Day parting | Lever 3: scheduling spend by hour or day of week |
| Island games | Standalone primetime NFL games, e.g. Thursday Night and Monday Night Football: the only game in that window, so demand concentrates into one slate. A key day-parting and pulse moment |
| Pulse | Lever 4: an incremental spend push around an event, slate, or moment; report any post-pulse hangover |
| State levers | Lever 5: geo weighting, on/off, and reallocation by state |
| Watch list | Items with an owner (role) and a decision date, ending every report |
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
| Sensor Tower | App intelligence: downloads, rankings, and Ad Intelligence (competitor networks and creatives). Planned API connection |
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
| Andromeda | Meta's ad retrieval system; post-Andromeda, creative does most of the targeting |
| SRN | Self-reporting network: attributes itself when AppsFlyer queries it (Meta, Google, Apple Ads, TikTok, Snap). See [[appsflyer-attribution-model]] |
| Advanced SRN | An SRN that also measures non-consented iOS users through aggregated privacy measurement (TikTok, Snap) |
| Link-based network | A partner that reports clicks and impressions through AppsFlyer attribution links (Reddit, Liftoff, Moloco, RZR) |
| Lookback window | Maximum time from ad engagement to install for the install to be credited to that engagement |
| Re-attribution window | Period after first install during which a reinstall is not a new install. AppsFlyer default is 90 days |
| Engaged click / engaged view | Interaction inside an ad (playable, video threshold) without leaving it; ranks with clicks |
| Enhanced attribution model | AppsFlyer's flooding-aware attribution: only eligible engagements compete |
| CTIT | Click-to-install time; very short CTIT signals install hijacking |
| AAP | AppsFlyer Aggregated Advanced Privacy: withholds user-level data for non-consented iOS users |
| AEM | Meta Aggregated Event Measurement: Meta's modeled iOS measurement |
| AdAttributionKit | Apple's successor attribution framework alongside SKAN |
| Conversion Studio | Where the AppsFlyer SKAN CV schema is configured |
| Fine / coarse CV | SKAN 4 values: fine (64 values, window 1 only) and coarse (low, medium, high, all windows) |
| CUID | Customer user ID set in the AppsFlyer SDK; maps internal user IDs to AppsFlyer IDs |
| af_revenue | AppsFlyer revenue parameter; feeds all revenue metrics and partner postbacks |
| LTV view / activity view | AppsFlyer counting modes: events by install date vs. by event date |
| My Dashboards | AppsFlyer's analytics UI since legacy dashboards were retired on June 30, 2026 |
| Creative Optimization | AppsFlyer cross-channel creative reporting with visual asset matching |
| ROI360 | AppsFlyer cost and revenue aggregation product |
| Data Locker | AppsFlyer delivery of reports to cloud storage or BigQuery |
| Protect360 | AppsFlyer fraud protection: real-time blocking plus post-attribution detection. See [[appsflyer-protect360]] |
| Incrementality factor | Incremental conversions divided by attributed conversions, from an AppsFlyer geo experiment |
| TBR | Time-based regression, the method behind AppsFlyer geo experiments |
| AppsFlyer MCP | Beta connector letting Claude query AppsFlyer directly. See [[appsflyer-mcp]] |
| Web Performance Measurement | AppsFlyer web measurement product replacing PBA |
| PBA | People-Based Attribution, AppsFlyer's legacy web measurement |

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
| X | X (formerly Twitter) Ads. Channel tag `x` |
| ACi / ACe | Google App campaigns for installs / for engagement |
| Audience signals | Google ACi hints about who high-value users are |
| Advantage+ app campaigns | Meta's automated app install campaigns |
| Incremental attribution (Meta) | Meta attribution model that optimizes and reports on predicted *caused* conversions |
| Smart+ | TikTok's automated campaign type (app and web) |
| SAN | TikTok Self-Attributing Network; replaced the legacy MMP integration on Mar 31, 2025 |
| AEO | App event optimization: optimize delivery to a post-install event such as FTD (TikTok, Reddit) |
| EVTA | TikTok engaged view-through attribution: 6+ seconds watched, then a conversion |
| EVC | Moloco engaged view conversion: 10+ seconds watched, sent to MMPs on the click link |
| Engaged view (Snap) | 5-second video views that Snap sends to MMPs as clicks (since Nov 2024) |
| GBB | Snap goal-based bidding |
| SKOverlay | Apple's in-ad store sheet; Snap's iOS Install Card uses it |
| Max campaigns | Reddit's automated campaign type (beta) |
| CPP | Apple custom product page; the basis of Apple Search Ads ad variations |
| Maximize Conversions (ASA) | Apple Search Ads auto-bidding to a weekly target CPA |
| Search Match | Apple Search Ads automatic query matching |
| DCM | CFTC Designated Contract Market; one of the two eligibility routes for Google's prediction-markets ads |
| NFA | National Futures Association; an NFA-authorized brokerage is Google's other eligibility route |
| RMG | Real Money Gaming app flag (Moloco registration, Google Play policy) |
| Cortex | Liftoff's AI bidding models |
| Vungle | Liftoff's owned supply SDK |

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
- Channels: `tiktok`, `meta`, `snapchat`, `google`, `reddit`, `x`, `apple-search-ads`, `liftoff`, `moloco`, `rzr`
- Test types: `creative`, `offer`, `landing-page`, `app-store`, `experiment`
