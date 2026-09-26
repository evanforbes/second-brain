---
title: RZR (formerly Aarki) Playbook
type: doc
status: living
created: 2026-09-26
updated: 2026-09-26
owners: [evan]
tags: [rzr]
channel: rzr
last_verified: 2026-09-26
verified_by: claude
related: ["[[appsflyer-channel-integrations]]", "[[appsflyer-attribution-model]]", "[[moloco]]", "[[liftoff]]"]
references:
  - https://www.rzr.com/mobile-ua/mobile-ua-dsp
  - https://www.rzr.com/retargeting/mobile-retargeting
  - https://www.rzr.com/ctv/connected-tv-mobile
  - https://www.rzr.com/case-studies/how-rzr-cut-deblocks-cpa-by-50-and-doubled-spend-in-6-weeks
  - https://support.appsflyer.com/hc/en-us/articles/360000423105-RZR-formerly-Aarki-campaign-configuration
  - https://finance.yahoo.com/news/aarki-rebrands-rzr-signaling-expansion-120400453.html
---

## Job

A programmatic DSP (formerly Aarki) with three products:

- **UA,** bidding on predicted lifetime value (LTV)
- **Retargeting,** built around proving incrementality
- **CTV-to-mobile,** turning connected-TV reach into mobile installs and in-app events

It's incremental reach that has to prove itself. RZR has no public advertiser help center (its site is product pages and case studies), so account detail comes from the rep and the AppsFlyer integration docs.

## Account structure

- **UA DSP:** RZR's models bid on install probability, purchase likelihood, and expected revenue from the first impression (a "target LTV" pitch).
- **Retargeting DSP:** matches lapsed users against live inventory. On iOS it uses probabilistic, contextual models for opted-out users. Segments RZR highlights:
  - lapsed high-value users
  - **installed but never converted**
  - dormant spenders
  - loyal users approaching drop-off
- **CTV-to-mobile:** builds audiences from TV viewing signals, serves on streaming inventory, and measures mobile installs, events, and ROAS after exposure.

## Bidding and optimization levers

- Goals are presented as target LTV, lower CPA, higher ROAS, and scale. The model needs value postbacks to bid on LTV.
- Retargeting is sold with a "prove impact with incrementality" frame. Ask for holdout design as part of any retargeting test.

## Signal and measurement setup

- **Link-based network in AppsFlyer:** click and view-through attribution, plus click-based retargeting.
- **Pass `af_ad`** on attribution links for creative-level reads.
- **The re-engagement window** can be set from 1 to 90 days, or lifetime (`af_reengagement_window`).
- See [[appsflyer-channel-integrations]].

## Creative specs and what works

- **RZR's case studies lean on segment-specific creative.** Example: a crypto-banking app used a "welcome bonus unlock" 3D animation aimed at users who started onboarding but never finished.
- **Non-English localized versions** of the site exist, so RZR supports global campaigns.

## Known issues and gotchas

- **Very little public documentation.** Settings and supply details have to come from the rep.
- **DSP view-through and CTV-to-mobile attribution are easy to over-credit.** CTV-to-mobile attribution in particular depends on probabilistic or IP-based matching. Require an incrementality read before trusting it.

## What it means for Underdog

- **Retarget installed-but-no-FTD users.** This is RZR's clearest fit: users who installed, maybe registered or passed KYC, but never deposited. It's a separate budget line from UA. Read it on incremental FTDs with a holdout, and keep it out of new-user CPFTD.
- **UA:** optimize to the canonical FTD event. Check view-through share and Protect360 before scaling (see [[appsflyer-protect360]]).
- **CTV-to-mobile:** interesting for tentpole sports moments, but only with a geo holdout. It's the hardest channel in the mix to measure honestly.
- **Rebrand hygiene:** AppsFlyer and older reports may still say Aarki. Keep "RZR (formerly Aarki)" in the glossary and map both names together in Hex.

## Current incumbent

(Record the winning creative and the test that crowned it.)

## Rep notes and betas

(None yet. Ask for: optimization goals available for FTD, view-through defaults, supply and compliance controls for real-money gaming, and retargeting holdout design.)

## Test log

(None yet.)
