---
title: Liftoff Playbook
type: doc
status: living
created: 2026-09-26
updated: 2026-09-26
owners: [evan]
tags: [liftoff]
channel: liftoff
last_verified: 2026-09-26
verified_by: claude
related: ["[[appsflyer-channel-integrations]]", "[[appsflyer-attribution-model]]", "[[moloco]]", "[[rzr]]"]
references:
  - https://liftoff.ai/igaming-mobile-user-acquisition/
  - https://liftoff.ai/resources/case-study/prizepicks/
  - https://liftoff.ai/direct/creative-testing/
  - https://liftoff.ai/2026-creative-in-the-ai-era/
  - https://liftoff.ai/resource/2025-mobile-ad-creative-index-tile/
  - https://support.appsflyer.com/hc/en-us/articles/209731633-Liftoff-campaign-configuration-in-AppsFlyer
---

## Job

A programmatic DSP with its own in-app supply, which is **incremental reach that has to prove itself.** Liftoff is the DSP with the clearest pitch for real-money gaming: it publishes an iGaming UA guide and has a published case study with **PrizePicks** (a direct DFS and prediction-markets competitor).

Liftoff's advertiser help center sits behind a login, so this playbook comes from Liftoff's public guides and the AppsFlyer integration docs. Fill in account-level detail from the rep and the dashboard.

## Account structure

- **Products:**
  - **Accelerate:** the DSP for app-to-app UA and re-engagement.
  - **Cortex:** the AI models that predict which impressions lead to sign-up and first deposit.
  - **Vungle SDK:** Liftoff's owned supply, which Liftoff says is in 95% of top apps.
  - **Liftoff Creative:** an in-house creative studio.
- **Optimization goals, per Liftoff's iGaming guide:** CPI and CPA campaigns (typically CPA = FTD) to balance cost and volume, and ROAS campaigns for habitual spenders.
- **Compliance controls:** choose exchanges and inventory that keep ads away from underage audiences and unsafe placements. Liftoff positions its owned supply as the controllable part of the buy.

## Bidding and optimization levers

- Cortex trains on first-party attribution data and MMP postbacks to predict **sign-up and first deposit at an efficient bid.** The richer and cleaner the FTD postback, the better the model.
- **Multi-creative optimization** tests **up to six creatives at once**, automatically shifting spend away from losers.
- Retargeting is available through click and view-through, and is recorded in AppsFlyer as retargeting when links are flagged.

## Signal and measurement setup

- **Link-based network in AppsFlyer:** click and view-through attribution, cost API, retargeting, and Protect360 rejected-install postbacks (see [[appsflyer-channel-integrations]]).
- **Creative Optimization in AppsFlyer** connects to Liftoff with reporting-API credentials from the Liftoff CSM (see [[appsflyer-reporting-and-data]]).
- Send the canonical FTD event in postbacks, with revenue only if it's a deliberate value signal (see [[appsflyer-events-and-s2s]]).

## Creative specs and what works

From Liftoff's iGaming guide and case studies (these are vendor claims; treat them as hypotheses to test):

- **Interactive ads with a reward mechanic,** such as a scratch-off or bonus reveal, let users "try" the product before installing. Liftoff suggests using gen-AI to refresh familiar formats (2D to 3D, motion on statics).
- **UGC and creator content** builds trust for an unfamiliar betting app. Liftoff reports two-person skits working for sports betting, casino, and crypto. A DraftKings growth lead is quoted crediting a mix of display, video, dynamic, and interactive, with heavy UGC and influencer content.
- **FOMO and time-limited offers.** **Product ads** dynamically generate creatives with schedules, matchups, and near-live odds, deep-linking to the specific market. A LATAM iGaming case reports lower CPA and CPI and more incremental conversions on iOS.
- **Team- and event-specific creative, plus interactive "try the platform" ads,** are the core of the PrizePicks case study.
- **Offers:** bonus bets that need the user's own first bet extend engagement better than a pure free reward that invites churn.
- **Onboarding:** keep it short, show progress ("step 1 of 3"), and signal a secure deposit. This is conversion work, but Liftoff ties it directly to FTD rate.
- **Tentpoles:** Super Bowl, March Madness, and other big events need offers, event-tone creative, and live-odds creative planned in advance, not just a budget increase.

## Known issues and gotchas

- **Guides and case studies are marketing.** "Incremental conversions" in a vendor case study aren't your holdout.
- **View-through on a DSP** is where attributed installs inflate. Check `engagement_type` and Protect360 before believing a cheap CPFTD.
- **Rendering varies across inventory,** so confirm interactive ads render as intended.

## What it means for Underdog

- **PrizePicks runs a documented Liftoff program** built on team- and event-specific creative and interactive ads. Expect competition for the same DFS and prediction-markets audiences, and watch it in the market section (`docs/market/`).
- **Test product ads for prediction markets.** Live-odds, matchup-specific dynamic creative fits prediction markets naturally. Test it against the incumbent with a holdout, not attributed CPFTD alone.
- **Use multi-creative optimization (up to 6) as the creative-test harness on Liftoff,** but log the read in `tests/` against the incumbent on CPFTD, not Liftoff's pick.
- **Compliance:** confirm with the rep which exchanges and placements are excluded for age and state compliance, and write the answer here.

## Current incumbent

(Record the winning creative and the test that crowned it.)

## Rep notes and betas

(None yet. Ask for: account-level docs access, available betas such as product ads for prediction markets, and inventory compliance controls.)

## Test log

(None yet.)
