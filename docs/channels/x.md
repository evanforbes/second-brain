---
title: X (Twitter) Playbook
type: doc
status: living
created: 2026-09-26
updated: 2026-09-26
owners: [evan]
tags: [x]
channel: x
last_verified: 2026-09-26
verified_by: claude
related: ["[[appsflyer-channel-integrations]]", "[[appsflyer-attribution-model]]"]
references:
  - https://business.x.com/en/help/ads-policies/ads-content-policies/gambling-content
  - https://business.x.com/en/help/ads-policies/ads-content-policies/gambling-content/gambling-tcs
  - https://business.x.com/en/help/campaign-editing-and-optimization/optimizing-app-campaigns
  - https://business.x.com/en/help/campaign-setup/create-an-app-installs-campaign/mobile-app-measurement-and-attribution
  - https://business.x.com/en/help/overview/twitter-ios14-resource-center
  - https://business.x.com/en/help/campaign-setup/campaign-targeting/optimized-targeting
  - https://business.x.com/en/help/campaign-setup/campaign-targeting/post-engager-targeting
  - https://business.x.com/en/help/campaign-setup/campaign-targeting/keyword-targeting
  - https://support.appsflyer.com/hc/en-us/articles/4410464316049
---

## Job

**Surgical.** Real-time conversation around live sports and events. It's small and targeted, not a scale channel: reach people *during* the game, around specific keywords, handles, and moments. It's also listed as premium inventory on Moloco (see [[moloco]]).

## Account structure

- **Objectives for Underdog:** App installs and App re-engagements. Website traffic and website conversions are available for web funnels.
- **Campaign → ad group → ads.** App campaigns need an **App Card**, which powers App Buttons on image and video posts (preview, ratings, install or open straight from the timeline).
- **Gambling pre-approval is required.** X's gambling policy covers sports betting, **online fantasy sports**, bonus codes, and tips, odds, and picks services. It's prohibited except in listed countries, where advertisers must be **certified and pre-approved** and accept X's Gambling Terms. For the **U.S.**, fantasy sports, sports betting, lotteries, online casinos, and affiliates are each "permitted with restrictions." Licensed operators must warrant compliance with every applicable state law and hold the required licenses, and must tell X immediately about regulatory rulings against them.

## Bidding and optimization levers

- **Learning period is 3–5 days.** Don't edit a new campaign for about 5 days. If it's still weak after that, raise bids, widen targeting, or refresh creative.
- **Bid types:** Automatic bid (recommended for scale) or Maximum bid. X's ATT guidance: if using Max bid, keep it at **no more than 5× the KPI**, and err conservative. Max bid risks little or no delivery.
- **Video app campaigns usually need higher bids** than image.
- **Targeting:**
  - keywords (real-time intent)
  - follower look-alikes and interests
  - **post engager retargeting:** retarget people who saw or engaged with your posts, for 15 days after organic impressions, 30 days after promoted impressions, and 45 days after organic engagements
  - custom audiences (lists, app activity, website activity)
  - device, carrier, and new-mobile-user targeting
  - geo, gender, language, and age targeting
- **Optimized Targeting** extends delivery beyond your selections.

## Signal and measurement setup

- **An approved MMP is required to bid in app install campaigns.** X calls this MACT (Mobile App Conversion Tracking). SKAdNetwork is supported for opted-out iOS users.
- **In AppsFlyer, X Ads is an SRN.** See [[appsflyer-channel-integrations]].
- **Web:** X Pixel plus the conversion API, with an adjustable attribution window per event.

## Creative specs and what works

- **Images and video complemented by App Buttons** qualify visitors before the store.
- Lean into real-time moments: game-day, line-move, and matchup creative timed to live events. This is inference from X's "real-time intent" positioning; test it.
- Specs: see X Ads creative specs (`raw/channels/x/`).

## Known issues and gotchas

- **Gambling certification comes before any spend.** Uncertified gambling ads get rejected, and fantasy sports falls under the gambling policy.
- **Small, noisy volume** makes CPFTD reads unstable. Judge at monthly grain or with an on/off test.
- **As an SRN,** X claims its own conversions. Compare against AppsFlyer and warehouse FTDs (see [[appsflyer-discrepancies]]).

## What it means for Underdog

- **Confirm X gambling certification** covers both fantasy and prediction markets, and the states targeted. Prediction markets may be classified differently from fantasy or betting, so ask the X account team and record the answer here.
- **Use X for moments, not baseline:** keyword and handle targeting around live games, plus post-engager retargeting of people who engaged with Underdog's organic posts during games.
- **Geo-target to legal states** at ad group level. X supports geo and age targeting, which is required for compliance.
- **Read on incrementality.** Its SRN self-attribution and small volume make attributed CPFTD the least reliable of the channels.

## Current incumbent

(Record the winning creative and the test that crowned it.)

## Rep notes and betas

(None yet.)

## Test log

(None yet.)
