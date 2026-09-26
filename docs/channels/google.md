---
title: Google App Campaigns (UAC) Playbook
type: doc
status: living
created: 2026-09-26
updated: 2026-09-26
owners: [evan]
tags: [google]
channel: google
last_verified: 2026-09-26
verified_by: claude
related: ["[[appsflyer-channel-integrations]]", "[[appsflyer-skan-and-ssot]]", "[[ad-policy-matrix]]"]
references:
  - https://support.google.com/google-ads/answer/6247380?hl=en
  - https://support.google.com/google-ads/answer/6167162?hl=en
  - https://support.google.com/google-ads/answer/15997092?hl=en
  - https://support.google.com/google-ads/answer/9176652?hl=en
  - https://support.google.com/adspolicy/answer/15132179?hl=en
  - https://support.google.com/adspolicy/answer/16757872?hl=en
  - https://support.google.com/adspolicy/answer/17230476?hl=en
  - https://support.google.com/adspolicy/answer/17117810?hl=en
  - https://support.google.com/googleplay/android-developer/answer/16902027?hl=en
  - https://support.google.com/googleplay/android-developer/answer/9877032?hl=en
  - https://support.google.com/google-ads/answer/4417303339921
---

## Job

**Intent capture.** App campaigns serve across Search, Google Play, YouTube, Discover, Gmail, and the Display Network from one set of assets. Google's AI chooses the channel, audience, and asset. Brand-search demand is the part that needs guarding.

## Account structure

**Three subtypes:**
- **App campaigns for installs (ACi):** optionally with **audience signals**, which hint at who high-value users are. They work with every bid strategy and help with cold starts.
- **App campaigns for engagement (ACe):** re-engages installed users, for example users who installed but never converted.
- **Pre-registration:** Android only.

**Google's recommended ladder:**
1. **Install volume, all users,** with target CPI. Budget at least **50×** the target CPI.
2. **Install volume aimed at users likely to perform an in-app action,** with target CPI at least 20% higher.
3. **In-app actions with tCPA.** Pick an action completed by **10+ users a day in the campaign.** Budget at least **10×** tCPA.
4. **tROAS,** once value data is stable.

**Don't run competing App campaigns in the same geography.** They compete in the auction against each other.

## Bidding and optimization levers

- **Conversion delay.** CPI and CPA look inflated in the first days or weeks. Evaluate against a realistic conversion window.
- **Stability rules:**
  - Don't switch campaign type after launch.
  - **Don't change budget or targets by more than 20% at a time.**
  - Don't over-restrict locations or placements.
- **Google suggests a "view-through adjusted CPI"** that counts view-through conversions. Underdog should read that against a holdout (see below).

## Signal and measurement setup

- Import conversions (`first_open` plus in-app events) from AppsFlyer, or use Firebase. **Send the deep value event server-side with a real value.**
- **iOS:**
  - On-device conversion measurement and SKAN. Google SKAN installs can arrive **up to 45 days late** in AppsFlyer.
  - GBRAID and WBRAID URL parameters are used for iOS attribution.
- **App Connect:** a hub for web-to-app deep linking and in-app conversion measurement.
- **In AppsFlyer, Google is an SRN.** Google accepts events inside its own 30–90 day window, and Creative Optimization must be connected by the same user who connected ROI360. See [[appsflyer-channel-integrations]].

## Creative specs and what works

- **Assets are the targeting.**
  - **Video:** several lengths and all orientations (16:9, 1:1, 2:3). Google says portrait converts about 60% better than landscape. Show real product use, with a clear CTA.
  - **Text:** use all four text lines, with at most one exclamation mark.
  - **HTML5:** run it through the validator first.
- **Asset report ratings:** Waiting, Learning, Low, Good, Best. These are relative to other assets. **Add assets instead of removing "Good" or "Low" ones,** because two assets beat one.
- **AI labels:** ads with AI-generated or AI-edited assets may need AI disclosure labels in some jurisdictions, including New York. Use Google's AI label setting where relevant.

## Policy (see [[ad-policy-matrix]])

**Daily Fantasy Sports (U.S.):**
- Needs Google certification, and a state license where required. If a state doesn't require one, the advertiser must be licensed in at least one state that does.
- No targeting under 18.
- **An adult-only disclaimer on the landing page.**
- **Problem-gambling info in the ad or on the landing page.**
- No implied school or university affiliation.
- Google has opened DFS ads state by state (July 2024 expansion; **Colorado since July 1, 2026**).

**Prediction markets (U.S.):**
- Allowed since Jan 21, 2026, **only with Google certification.** The advertiser must be either:
  - a **CFTC Designated Contract Market (DCM)** whose primary business is listing event contracts, or
  - an **NFA-authorized brokerage** giving access to such a DCM's products.
- **Approved locations:** the U.S. excluding Michigan, Nevada, New York, and Ohio. Michigan and New York were explicitly prohibited from July 13, 2026. **A separate application is needed per location.**
- **Disallowed:** binary or fixed-return options, anything legally defined as gambling locally, and tips or signals sites.

**Sports betting:** allowed only for state-licensed operators. National targeting is allowed on YouTube only if under-21s and unlicensed states are excluded, and a problem-gambling warning is shown.

**Google Play:**
- Real-money prediction-market apps had to enroll in Google Play's **prediction-markets pilot by June 1, 2026.** Requirements include organization verification, 18+/AO rating, age gating, responsible-use tools, and CFTC-style licensing.
- **Apps that offer prediction markets under a gambling license are out of scope for the pilot.** They fall under Play's Real-Money Gambling, Games and Contests policy instead.

## Known issues and gotchas

- **Brand cannibalization.** App campaigns serve on branded Search queries. Without brand exclusions and a dedicated brand Search campaign, "App campaign CPFTD" includes branded demand.
- **Changing more than 20% at once resets learning.**
- **The Google iOS SKAN lag** of up to 45 days makes recent iOS reads incomplete.

## What it means for Underdog

- **Run fantasy and prediction markets as separate certification tracks.** DFS falls under the gambling and games policy (with disclaimers and problem-gambling info). Prediction markets fall under the Prediction Markets policy (CFTC DCM or NFA brokerage, per-location applications, and no MI/NV/NY/OH).
  - **Open question:** which Underdog entity, or which partner exchange, qualifies for the prediction-markets certification?
- **Exclude non-approved states** at campaign level, and re-check the state lists monthly. They change often.
- **Ladder:** start on FTD tCPA, with enough FTD volume per campaign (10+ a day) and budget at least 10× tCPA. Move to tROAS only once a real value signal exists.
- **Brand firewall:** brand exclusions on App campaigns, plus a dedicated brand Search campaign. Read App campaigns against a geo holdout before crediting them.
- **Creative tests:** new asset groups or campaigns per challenger concept. Read the asset report as directional and CPFTD in AppsFlyer and Hex as the verdict.

## Current incumbent

(Record the winning asset set and the test that crowned it.)

## Rep notes and betas

(None yet. Ask for: prediction-markets certification path, DFS state list updates, and audience signals for FTD users.)

## Test log

(None yet.)
