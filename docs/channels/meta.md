---
title: Meta Playbook
type: doc
status: living
created: 2026-09-26
updated: 2026-09-26
owners: [evan]
tags: [meta]
channel: meta
last_verified: 2026-09-26
verified_by: claude
related: ["[[appsflyer-channel-integrations]]", "[[appsflyer-events-and-s2s]]", "[[appsflyer-skan-and-ssot]]", "[[ad-policy-matrix]]"]
references:
  - https://www.facebook.com/business/help/309994246788275
  - https://www.facebook.com/business/help/711378409718185
  - https://www.facebook.com/business/help/317364032619502
  - https://www.facebook.com/business/help/1153577308409919
  - https://www.facebook.com/business/help/460276478298895
  - https://www.facebook.com/business/help/387440828988900
  - https://www.facebook.com/business/help/345214789920228
  - https://www.facebook.com/business/help/4740325989340856
  - https://transparency.meta.com/policies/ad-standards/restricted-goods-services/gambling-games/
  - https://developers.facebook.com/docs/marketing-api/conversions-api/app-events
  - https://developers.facebook.com/docs/app-events/
  - https://support.appsflyer.com/hc/en-us/articles/4410481130641-Meta-ads-discrepancies
---

## Job

**Demand creation at scale.** Broad reach across Facebook, Instagram, Messenger, and Audience Network. Machine learning finds the users; **creative is the targeting.**

## Account structure

- **Advantage+ app campaigns** (now merged with Advantage+ catalog ads) are Meta's default for app installs and in-app actions. Meta's AI handles bidding, audience, and placement.
  - **Inputs are simplified:** country, language, app store. Advantage+ placements covers Facebook, Instagram, Messenger, and Audience Network.
  - **Multiple campaigns are fine** for separate apps, events, creative tests, or regions. **Ads Manager blocks duplicate setups.**
  - **Don't run manual app ads and Advantage+ to the same audience at the same time.** The overlap hurts delivery. To compare them, split-test manual vs. Advantage+ with no overlap, and move fully to the winner.
- **Evan's operating approach:** one broad campaign, CAPI sending real funded-account values from day one, and creative as the targeting lever after Andromeda (Meta's ad-retrieval system).

## Bidding and optimization levers

**Optimization goal, by primary KPI:**

| Primary KPI | Optimization |
|---|---|
| Cost per install | App installs |
| Cost per event (FTD) | App events |
| ROAS | Value optimization (lowest-cost bid only) |

**Bid types:**
- **Highest volume (lowest cost):** Meta recommends it, with **no bid cap**.
- **Cost per result goal:** holds costs around a target, but isn't guaranteed.
- **Bid cap:** only if you can calculate predicted conversion rates.

**Attribution model (set per ad set):**
- **Standard:** chosen windows, plus click, view, or engaged-view credit.
- **Incremental:** delivery and reporting optimize to conversions Meta's models predict were *caused* by the ad.
- **Custom:** share your own attribution logic with Meta for delivery.
- Results can't be compared across ad sets with different attribution models. Use Compare Attribution Settings.

## Signal and measurement setup

- **App events** come from the Facebook SDK, the App Events API (including MMPs like AppsFlyer), or the **Conversions API for App Events**. CAPI sends server events to a single dataset linked to the app.
- **iOS 14.5+:**
  - **SKAdNetwork** is configured in Events Manager (up to 63 event mappings), and **value sets** are needed to keep value optimization on iOS.
  - **Aggregated Event Measurement (AEM)** does modeled iOS measurement and deep-link re-engagement attribution.
  - Ads Manager reports AEM and SKAN differently (see [[appsflyer-skan-and-ssot]]).
- **In AppsFlyer, Meta is an SRN:**
  - Meta defaults to 7-day click and 1-day view, and Ads Manager defaults to PST.
  - Meta counts cross-device conversions.
  - AEM can claim modeled conversions that never appear in Ads Manager.
  - Events sent through both the SDK and AppsFlyer are **not** deduped.
  - S2S events sent on to Meta need `ua` and `ip`.

  See [[appsflyer-channel-integrations]].

## Creative specs and what works

- **Upload volume.** Up to 50 images, videos, playables, or Instant Experiences at once, each with up to 5 primary texts and 5 headlines. Meta recommends many creative elements.
- **Creative is the targeting.** Diversify concepts, formats, and hooks rather than cloning winners. Refresh before fatigue.
- **Reporting caveat:** AppsFlyer Creative Optimization can't break Advantage+ or dynamic creative down to the single asset, and for Flexible ads it reports only the best asset. Test challengers as separate ads (see [[appsflyer-reporting-and-data]]).

## Policy (see [[ad-policy-matrix]])

- **Online gambling and games need Meta authorization.** This covers betting, **fantasy sports**, skill tournaments, and anything where money is part of entry and prize.
  - Apply in Meta Business Suite, under Authorizations and Verifications.
  - Authorization is granted **per ad account ID, per territory, per gaming type.**
  - **Declare intent before targeting any new jurisdiction.**
- **No targeting under 18**, and no unsupported markets. Target only where Underdog is licensed or lawful.
- **Prediction markets:** Meta's help center has no dedicated prediction-markets policy (as of Sep 2026). Confirm with the Meta rep whether the gambling authorization covers the prediction-markets product, or whether it sits under financial services.

## Known issues and gotchas

- **Meta-reported and AppsFlyer numbers differ** because of windows, timezone, cross-device credit, and AEM modeling (see [[appsflyer-discrepancies]]).
- **The Meta SDK plus AppsFlyer** can double-count events inside Meta.
- **Account restrictions:** gambling ads without authorization get the ad account restricted, and ads can be "approved, then rejected."

## What it means for Underdog

- **Optimize to the FTD app event.** Move to value optimization only with an agreed value (deposit value is not NGR; see [[appsflyer-events-and-s2s]]), and set up SKAN value sets for iOS.
- **Test the incremental attribution model.** Split-test standard vs. incremental attribution on the same audience and read the result against a Meta geo holdout (Underdog has run one before). If it holds up, it's the most direct way to point Meta at incremental FTDs.
- **Keep the authorization map current.** When prediction markets or fantasy launch in a new state, declare the jurisdiction in Meta Business Suite *before* targeting it.
- **Creative tests:** separate ads for the challenger vs. incumbent inside one Advantage+ campaign, read on CPFTD. Log them in `tests/`.

## Current incumbent

(Record the winning creative and the test that crowned it.)

## Rep notes and betas

(None yet. Ask for: prediction-markets policy classification, incremental attribution for app campaigns, value sets for iOS.)

## Test log

(None yet.)
