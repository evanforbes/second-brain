---
title: Moloco Playbook
type: doc
status: living
created: 2026-09-26
updated: 2026-09-26
owners: [evan]
tags: [moloco]
channel: moloco
last_verified: 2026-09-26
verified_by: claude
related: ["[[appsflyer-channel-integrations]]", "[[appsflyer-attribution-model]]", "[[appsflyer-protect360]]", "[[liftoff]]", "[[rzr]]"]
references:
  - https://help.moloco.com/hc/en-us/articles/4417515214999-Choose-the-right-campaign-goal
  - https://help.moloco.com/hc/en-us/articles/360050684813-Ad-group-settings
  - https://help.moloco.com/hc/en-us/articles/4404658994071-A-B-test-settings
  - https://help.moloco.com/hc/en-us/articles/15431693507607-What-is-an-Engaged-View-Conversion-EVC
  - https://help.moloco.com/hc/en-us/articles/4402359860631-Average-Daily-Budget-Optimizer
  - https://help.moloco.com/hc/en-us/articles/17514299166615-How-to-integrate-with-a-mobile-measurement-partner-MMP
  - https://help.moloco.com/hc/en-us/articles/30060034592919-How-to-set-up-SKAdNetwork-SKAN-attribution-for-iOS-apps
  - https://help.moloco.com/hc/en-us/articles/1500005837321-SKAdNetwork-traffic-settings
  - https://help.moloco.com/hc/en-us/articles/360050681573-Register-your-app
  - https://help.moloco.com/hc/en-us/articles/8838808037527-Troubleshoot-creatives
  - https://help.moloco.com/hc/en-us/articles/28126478930327-Anti-fraud-measures
  - https://help.moloco.com/hc/en-us/articles/22553113373335-Test-your-creatives
  - https://help.moloco.com/hc/en-us/articles/43502630422039
  - https://help.moloco.com/hc/en-us/articles/360000691978
---

## Job

A programmatic DSP (demand-side platform) buying in-app inventory across ad exchanges with machine-learning bidding. **It's incremental reach that has to prove itself:** cheap attributed CPFTD from a DSP is a hypothesis until a holdout confirms it.

## Account structure

- **Structure:** Ad account → App → Campaign → Ad group (creative groups plus targets).
- **Campaign types:** User Acquisition or Re-engagement.
- **Duplicate campaigns, since Sep 3, 2026:** new campaigns that promote the same app to the same audience can't be activated, and existing live duplicates get paused on a scheduled date (Moloco announces it in Ads Manager). Structure by genuinely different audiences, geos, or goals, not parallel copies.
- **Exchange blocking removed, since Sep 3, 2026:** exchange-level include and exclude controls are gone for new campaigns and targets. App- and content-category-level placement controls remain.
- **Impression interval** (frequency per device, per format): the default is 1 hour for UA. Moloco recommends keeping the default.

## Bidding and optimization levers

- **UA goals:**
  - **Install**, with bid control set to Budget (spend evenly). Target CPI is legacy: existing campaigns only, no new ones.
  - **In-app event:** optimize to a chosen post-install event. The event's postbacks must come from the MMP.
  - **ROAS:** needs purchase postbacks *with revenue* from the MMP.
- **Average Daily Budget Optimizer:** spend moves up to ±50% on any given day, with weekly spend capped at 7× the average daily budget, Monday to Sunday. This gives the model room to follow better auctions.
- **Postbacks feed the model.** Moloco recommends sending full postback data, including Moloco-attributed, other-network-attributed, and organic/unattributed events, because its machine learning trains on all of it.

## Signal and measurement setup

- **Probabilistic attribution (PA) in the MMP is crucial for iOS.** Without it, Moloco can only learn from IDFA-consented users. A/B tests are also unavailable on campaigns that run only on SKAN or unattributable traffic.
- **SKAN:**
  - Aim for **20–25 installs per day, per app, per SKAN campaign ID** to clear privacy thresholds and reduce null values.
  - SKAN postbacks lag 2–4 days. **Wait at least 72 hours before judging a budget change.**
  - SKAN traffic options changes take up to 72 hours to apply. The app must be registered with primary and secondary measurement methods for auto-configuration.
  - **StoreKit-rendered ads** (Apple's native in-ad store sheet) have a longer, 30-day attribution window and can lift SKAN installs.
- **Engaged View Conversions (EVCs):** a conversion after watching **10+ seconds** of a skippable video, or the whole video if it's shorter, with no click. EVCs use the click-through conversion window and are sent to MMPs through the *click* tracking link. Moloco reports engaged viewers as about 4× more likely to convert.
- **App registration** requires IAB category(s) and a **Real Money Gaming (RMG)** flag.

## Creative specs and what works

- **Formats:** video, image, native, Playable, Interactive End Card (IEC), plus auto-generated creative.
- **Auto-generated interactive ads (Sep 22, 2026):** templates turn existing video and image creatives into interactive formats at no production cost. Moloco's internal analysis claims an 8–15% lower CPI when format gaps are closed, and says over half of UA campaigns (as of June 2026) run without any interactive creative.
- **Built-in A/B tests** can compare creative groups *or* targets. Moloco advises against comparing different formats (image vs. video) because placement differences confound the result.
- **Moloco Creative Lab** (iOS and Android app) previews how videos, IEC, and playables render.

## Known issues and gotchas

- **Gambling limits the supply.** Google AdX requires gambling apps to be Google-certified before ads run there, and Kakao prohibits gambling outright. Mark the app RMG correctly, and expect exchange-level reach to depend on certification.
- **Engaged views travel on click links.** In AppsFlyer they can look like clicks unless `engagement_type` is checked (see [[appsflyer-attribution-model]]).
- **Target CPI can underspend** when the target sits below what the market supports. This is legacy but still true for existing campaigns.
- **Anti-fraud** combines data, automation, and human review. Report suspected fraud through the rep, and cross-check AppsFlyer Protect360 (see [[appsflyer-protect360]]).

## What it means for Underdog

- **Check campaign overlap now.** Under the Sep 3, 2026 duplicate rule, parallel Moloco campaigns for the same app with overlapping audiences get paused. If prediction markets and fantasy share one app, separate them by genuinely distinct targeting, or consolidate.
- **Optimize to the FTD event, not install.** Use the in-app event goal with the canonical FTD postback. Moving to ROAS only makes sense once a real value signal is sent, and deposit value is not NGR (see [[appsflyer-events-and-s2s]]).
- **Share full postbacks,** including organic and other-network FTDs, if legal and privacy review allow. The model learns faster.
- **Keep the RMG flag and Google certification current,** or AdX supply silently disappears.
- **Proof bar:** before scaling, check the engaged-view and view share of attributions and Protect360 for Moloco. Then confirm with a geo holdout or on/off test (see [[appsflyer-incrementality]]).
- **Creative tests:** use Moloco A/B tests on creative groups against the incumbent, same format only. Consider auto-generated interactive versions of incumbent videos as a cheap test cell.

## Current incumbent

(Record the winning creative group and the test that crowned it.)

## Rep notes and betas

(None yet.)

## Test log

(None yet.)
