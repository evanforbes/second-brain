---
title: Snapchat Playbook
type: doc
status: living
created: 2026-09-26
updated: 2026-09-26
owners: [evan]
tags: [snapchat]
channel: snapchat
last_verified: 2026-09-26
verified_by: claude
related: ["[[appsflyer-channel-integrations]]", "[[appsflyer-skan-and-ssot]]", "[[appsflyer-attribution-model]]", "[[ad-policy-matrix]]"]
references:
  - https://businesshelp.snapchat.com/s/article/bidding-strategies?language=en_US
  - https://businesshelp.snapchat.com/s/article/goal-basedbidding?language=en_US
  - https://businesshelp.snapchat.com/s/article/attribution-window?language=en_US
  - https://businesshelp.snapchat.com/s/article/specs-app-install?language=en_US
  - https://businesshelp.snapchat.com/s/article/skad-network-campaign?language=en_US
  - https://businesshelp.snapchat.com/s/article/app-attribution-troubleshooting?language=en_US
  - https://businesshelp.snapchat.com/s/article/snap-ads-practices?language=en_US
  - https://businesshelp.snapchat.com/s/article/snap-gaming-terms?language=en_US
  - https://values.snap.com/policy/ads-category-requirements/gaming-gambling-lotteries
  - https://support.appsflyer.com/hc/en-us/articles/4417686973841-Snapchat-integration-discrepancies
---

## Job

**The younger first-time audience.** Snap reaches people who don't show up as cheaply elsewhere.

**Evan's history is the key lesson for this channel:**
1. An early holdout showed no lift, and D2/D7 looked weak.
2. Diagnosis showed the account was heavy on Story Ads, an impression-led path. Moving to native Snap Ads raised CTR and click-to-install sharply.
3. An independent retest came back well above program-average FTD efficiency. **Cohorts maturing from D14 to D60 flipped the read.**

**Don't judge Snap on early-window metrics.**

## Account structure

- **Objectives:** App Installs (install goals: install, install plus event, sign-up, purchase), App Re-engagement, and Sales for app or web conversions.
- **An MMP or Snap's Conversions API integration is required** to optimize to installs or events and to report them. Snap App ID required.
- **iOS:** dedicated SKAdNetwork campaign setup. The Install Card uses Apple's **SKOverlay** (for SKAN-enabled app install campaigns from May 2024, extended to all SKAN-enabled goals from Sep 2024).

## Bidding and optimization levers

- **Auto-Bid:** Snap sets bids for the most goal actions within budget.
- **Target Cost:** best effort to keep average CPA at or below target by the ad set's end date.
- **Max Bid:** a ceiling. Snap recommends bidding toward the high end of the suggested range so the budget spends.
- **Learning phase:** usually **1–7 days**, driven by the ability to spend. It runs longer for lower-funnel goals and when the budget underdelivers.
- **Evaluate after 30–50 conversions** on the bid goal.
- **Lower-funnel goals** (purchase, sign-up) work better with broader targeting. Small audiences plus low-funnel goals struggle to scale.

## Signal and measurement setup

- **Snap's default and recommended windows are 28-day click / 1-day view.** Snap also recommends a **0-day inactivity window** for retargeting.
- **Since November 2024, Snap sends 5-second video views to MMPs *as clicks*** (engaged-view attribution) for all ad formats. In AppsFlyer, Snap's click share rises and its view share falls. Since February 2025, Ads Manager can split click-through, view-through, and engaged view.
- **In AppsFlyer, Snap is an Advanced SRN.** Ads Manager defaults to PST, and Snap can allowlist accounts to match MMP windows (see [[appsflyer-channel-integrations]]).
- **SKAN:**
  - Privacy thresholds produce NULL conversions, which Snap may **model** in its post-install columns.
  - **Conversion value advice:** focus on events within 24 hours of first open. Give bottom-funnel events *higher* values, because Apple keeps only the highest value. Map earlier funnel events into later values (for example, CV3 = sign-up + add-to-cart + purchase).

## Creative specs and what works

- **Vertical video,** with Dynamic CTAs where eligible. Live action, motion graphics, stop-motion, GIF-like clips, stills, and cinemagraphs are all accepted.
- **A "hero" message in the opening frame.** **3–5 second ads often drive action.** Put the offer message around seconds 2–3.
- **Test all formats, one per ad set,** then keep the winners. Match creative to targeting.
- **Avoid:** reusing other platforms' creative unchanged, clutter (stickers, multiple CTAs), and generic creative.
- **Evan's lesson:** native Snap Ads beat an impression-led Story Ads mix for app installs.

## Policy (see [[ad-policy-matrix]])

- **Gaming and gambling (including daily fantasy sports) needs Snap pre-approval.** Complete the Advertising of Gambling Services Application, agree to the Snap Gambling Terms, and provide proof of license or registration for every targeted territory, kept valid for the whole campaign. **Notify Snap immediately of license changes.**
- **Don't:**
  - target unlicensed territories
  - target or appeal to under-age audiences (set a **minimum age**)
  - glorify gambling or encourage play beyond one's means
  - promote tipster or odds services
- **Snap's Community Guidelines** separately prohibit organic promotion of gambling and prediction services. That matters for creators and organic posts, not paid ads.
- **Prediction markets:** not named in Snap's ad policy (as of Sep 2026). Confirm the classification with the Snap rep (gambling vs. financial products).

## Known issues and gotchas

- **The 28/1 default vs. AppsFlyer's windows** is the biggest discrepancy source. Align on purpose.
- **Engaged views reported as clicks** make Snap's AppsFlyer click CPFTD look stronger than a pure click read.
- **Modeled SKAN NULLs** in Snap reporting aren't AppsFlyer data.

## What it means for Underdog

- **Judge Snap on matured cohorts** (D30+ FTD quality and value) and holdouts, never on the D2/D7 read. That's the lesson Underdog already paid for once.
- **Keep native Snap Ads as the default format.** Test Story and Collection formats as challengers, one format per ad set.
- **Set Public Profile and ad minimum ages** to match the legal age for each product and state. Keep gambling-approval proof current per state.
- **Read engaged-view credit carefully** in AppsFlyer. Use the Ads Manager breakdown and `engagement_type` before crediting Snap clicks.

## Current incumbent

(Record the winning creative and the test that crowned it.)

## Rep notes and betas

(None yet. Ask for: prediction-markets classification, MMP window allowlisting, CAPI for app events.)

## Test log

(None yet.)
