---
title: AppsFlyer Attribution Model
type: doc
status: living
created: 2026-09-26
updated: 2026-09-26
owners: [evan]
tags: []
last_verified: 2026-09-26
verified_by: claude
related: ["[[appsflyer-skan-and-ssot]]", "[[appsflyer-channel-integrations]]", "[[appsflyer-discrepancies]]", "[[appsflyer-incrementality]]"]
references:
  - https://support.appsflyer.com/hc/en-us/articles/207447053-AppsFlyer-attribution-model
  - https://support.appsflyer.com/hc/en-us/articles/41442782045073-About-the-Enhanced-attribution-model
  - https://support.appsflyer.com/hc/en-us/articles/360001546905-Self-reporting-networks-SRNs
  - https://support.appsflyer.com/hc/en-us/articles/208338403-Set-up-lookback-windows
  - https://support.appsflyer.com/hc/en-us/articles/115002587066-Set-up-re-attribution-window
  - https://support.appsflyer.com/hc/en-us/articles/210084473-Measure-view-through-engagements
  - https://support.appsflyer.com/hc/en-us/articles/207040506-Measure-assisted-installs
  - https://support.appsflyer.com/hc/en-us/articles/10164066030737-Measure-reinstalls
---

## Summary

AppsFlyer gives full credit for an install to one touchpoint, usually the last one. Clicks beat impressions, and deterministic matches beat probabilistic ones. This is the **"who gets credit"** layer. It says nothing about what the spend caused (see [[appsflyer-incrementality]]).

One definition catches people out: **in AppsFlyer, the install happens at first app launch.** Ad networks timestamp the ad engagement, and app stores timestamp the download. These three clocks never line up exactly.

## How it works

**Attribution methods**, roughly in priority order:

| Method | How it matches | Where it applies |
|---|---|---|
| Install referrer | The store passes the clicked URL (deterministic) | Android. The main Android method. Includes the Meta install referrer |
| Device ID matching | The network passes IDFA or GAID on the click or impression | iOS only with ATT consent; Android |
| SRN query | AppsFlyer asks self-reporting networks whether they touched this device ID | Meta, Google, Snap, TikTok, Apple Ads, X, Amazon |
| Probabilistic modeling | Aggregate, statistical, no IDs. Window 0–24h, adaptive | iOS without consent; owned media |
| SKAN | Apple attributes privately and sends delayed postbacks | iOS. See [[appsflyer-skan-and-ssot]] |
| Apple Ads API | Apple's own attribution API | iOS, Apple Ads only |
| Deep link | Parameters carried on the link that opens the app | Re-engagement only |

**Engagement types and default lookback windows** (the platform side can differ; align them deliberately):

| Type | Range | Default |
|---|---|---|
| Click-through (referrer, ID match) | 1–30 days | 7 days |
| View-through (ID match) | up to 24h | 24h (1 day) |
| Engaged click (stayed inside a playable or interactive ad) | 1–7 days | 2 days |
| Engaged view (watched past a threshold or interacted without clicking) | selected partners | 2 days deterministic |
| Probabilistic, any type | 0–24h | adaptive |

Engaged clicks and engaged views rank alongside clicks, above plain views.

**SRNs vs. link-based networks.**
- **Self-reporting networks (SRNs)** attribute themselves. When a new install arrives, AppsFlyer queries them with the device ID, and each SRN says whether it touched that device. Examples: Meta, Google, Apple Ads.
- **Advanced SRNs** (TikTok and Snapchat) also measure users who haven't consented, through AppsFlyer's Aggregated Advanced Privacy framework.
- **Link-based networks** report clicks and impressions through attribution links. Reddit, Liftoff, Moloco, and RZR work this way.

**Enhanced attribution model.** When AppsFlyer detects click or impression flooding on a device, it only lets *eligible* engagements compete. The winner is then the last eligible click, which is not necessarily the most recent one. Raw data shows **Total candidates for attribution**; a count far above the number of contributors signals flooding.

**Assisted installs.** Touches inside the lookback window that did not win are reported as contributors. This is a free, rough view of multi-touch attribution.

**Reinstalls and the re-attribution window.**
- **The window:** it opens at first install. The default is 90 days, and the range is 1–24 months.
- **Reinstall inside the window after a retargeting touch:** AppsFlyer records a re-attribution.
- **Reinstall inside the window after a UA touch or no touch:** AppsFlyer records no new install. The *Post Reinstall Events Attribution* setting then decides whether later events credit the original source or organic.
- **Reinstall after the window:** AppsFlyer records a new install.

**First-install mode for post-reinstall events.** For apps added from July 31, 2024, events after a reinstall credit the original install, but only when the user consented to share the device ID at both install and reinstall. Otherwise the events are "organic unattributed." Apps added before that date must ask AppsFlyer to migrate.

**Engagement type in raw data.** `engagement_type` (and `contributor1-3_engagement_type`) takes the values click_to_download, click_to_app, engaged_click, engaged_view, view, or preload. When the type is missing, it has defaulted since Dec 2024 to click_unspecified or impression_unspecified. This field shows, per partner, how much of their credit comes from views.

**SRN mistargeting.** When one SRN runs both UA and retargeting with retargeting enabled, existing users get re-attributed from UA campaigns. AppsFlyer's own analysis of Meta UA campaigns found about 1 in 10 targeted users were already users.

## Gotchas

- AppsFlyer lookback windows shorter than the platform's mean the platform claims installs AppsFlyer calls organic. Longer windows mean AppsFlyer credits the network more generously.
- Turning view-through on for a DSP with a long window is the fastest way to inflate that DSP's attributed installs.
- AppsFlyer attributes a single device. Meta and TikTok also attribute cross-device, for example a desktop view followed by a phone install.

## What it means for Underdog

- **Attribution is for operating campaigns, not for deciding budget.** A channel's attributed CPFTD is a credit claim. Budget moves need an experiment behind them (see [[decision-log]]).
- **Split your nine channels by how they're measured.**
  - SRNs, which claim credit themselves: Meta, Google, Apple Search Ads, plus the Advanced SRNs TikTok and Snap.
  - Link-based: Reddit, Liftoff, Moloco, RZR.
  - The DSPs are where view-through and flooding inflate credit, so check each DSP's share of `view` and `engaged_view` in the raw data `engagement_type` field, and its "total candidates" count, before believing a cheap CPFTD.
- **Lookback window policy is a decision, not a default.** Aligning to each platform's windows reduces discrepancies but raises platform credit. Pick a policy, write it in [[appsflyer-underdog-setup-audit]], and apply it the same way across channels so CPFTD comparisons are fair.
- **Reinstall logic can hide returning users.** A lapsed user who reinstalls from a UA ad inside the re-attribution window is not a new install. Internal FTD logic (first valid deposit per user) is unaffected, so the warehouse and AppsFlyer can disagree on who is "new." Check the Post Reinstall Events setting.

## Open questions

Tracked in [[appsflyer-underdog-setup-audit]].
