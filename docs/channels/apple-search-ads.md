---
title: Apple Search Ads Playbook
type: doc
status: living
created: 2026-09-26
updated: 2026-09-26
owners: [evan]
tags: [apple-search-ads]
channel: apple-search-ads
last_verified: 2026-09-26
verified_by: claude
related: ["[[appsflyer-channel-integrations]]", "[[appsflyer-skan-and-ssot]]", "[[appsflyer-attribution-model]]"]
references:
  - https://ads.apple.com/app-store/best-practices/campaign-structure
  - https://ads.apple.com/app-store/best-practices/keywords
  - https://ads.apple.com/app-store/best-practices/manual-bidding
  - https://ads.apple.com/app-store/best-practices/maximize-conversions
  - https://ads.apple.com/app-store/best-practices/redownloads
  - https://ads.apple.com/app-store/help/ad-groups/0021-modify-audience-settings
  - https://ads.apple.com/app-store/help/ads/0077-create-ad-variations
  - https://ads.apple.com/app-store/help/ad-placements/0071-search-tab
  - https://ads.apple.com/app-store/help/attribution/0028-measuring-ad-performance
  - https://ads.apple.com/app-store/help/attribution/0093-adattributionkit-to-measure-performance
  - https://ads.apple.com/app-store/help/reporting/0092-tips-for-evaluating-performance
  - https://ads.apple.com/app-store/help/bids-and-budget/0063-set-and-adjust-your-CPA-cap
---

## Job

Intent capture on the App Store. People searching the App Store are close to downloading. **This is also the channel most likely to drift into buying branded demand that would have converted anyway,** so it needs the most scrutiny on incrementality.

## Account structure

Apple recommends **four campaign types, separated by keyword theme:**

| Campaign | Keywords | Match | Search Match | Bids |
|---|---|---|---|---|
| Brand | App and company name | Exact | Off | Most aggressive on top performers |
| Category | Non-brand terms for what the app does | Exact | Off | Aggressive |
| Competitor | Similar apps' names | Exact | Off | Aggressive |
| Discovery | Mining for new terms | Broad ad group, plus a separate Search Match ad group with no keywords | On only in the Search Match group | Moderate |

- **Promote winners.** Search terms that perform in Discovery get added as exact keywords to Brand, Category, or Competitor, and as negatives in Discovery so campaigns don't compete with each other.
- **Keep broad and exact apart.** Separate ad groups or campaigns, so bids can be managed independently. Most traffic should come from exact match.
- **Budgets and countries are set at campaign level.** Keywords, bids, audiences, and ad variations are set at ad group level.

## Bidding and optimization levers

- **Manual max CPT (cost per tap).** Start from Apple's suggestion and use the Recommendations page, which shows impression share, rank, search popularity, and estimated installs and CPA. Bid highest on exact match and moderately on broad and Search Match.
- **Maximize Conversions.** An auto-bidder plus Search Match, aimed at a **target CPA measured weekly.** Daily cost moves around the target. Apple recommends a daily budget that allows **at least 5 conversions a day.** Manual keyword bids can still be set.
- **CPA cap (legacy).** A hard ceiling on each query match. Apple positions Maximize Conversions as more flexible, because a cap blocks high-value queries.
- **Customer type:** All users (the default), New users, Returning users, or Users of my other apps. Audiences below **5,000 people** put the ad group on hold.
- **Location refinement** below country level is available in the U.S. and some other countries, but not in campaigns that span multiple countries.
- **Device type:** iPhone or iPad, with separate bids per device through separate ad groups.
- **Current audience settings list only device, location, and customer type. There is no age or gender.** Since Sep 1, 2026, any legacy ad group with age or gender targeting returns no attribution in AppsFlyer (see [[appsflyer-channel-integrations]]).

## Placements

- **Search results:** the main placement, keyword-based.
- **Search tab:** top of the suggested apps list before the user types. Built from product page assets.
- **Today tab:** prime placement on the App Store front page.
- **Product pages:** the "You might also like" section on other apps' product pages.

The Ad Placements report in Insights compares installs, tap-through rate, conversion rate, and CPA across placements. It can also show **view-through** installs within 24 hours of an impression; see the Underdog notes before counting those.

## Creative specs and what works

- **Ad variations come from custom product pages** (CPPs), up to 70 per app. They're built in App Store Connect with no app update needed, and each can have its own screenshots, preview video, promo text, and deep link (deep links need iOS 18+).
- **Match each CPP to a keyword theme or audience** for relevance. The tap then lands on the same page the ad showed.
- **Default ads use the default product page,** so product page quality is also ASA creative quality (see `docs/conversion/`).

## Signal and measurement setup

- **Two Apple methods:**
  - the **AdServices attribution API**, which MMPs like AppsFlyer read
  - **AdAttributionKit**, which Apple Ads registered with on **April 10, 2025.** The same last-click logic applies as for every other registered network. The ad network ID is `com.apple.ads`, and placements map to campaign IDs (search results = 10, search tab = 20, and so on).
- **In AppsFlyer, ASA has its own integration** and doesn't appear in the SKAN dashboard. Click and impression-based attribution are both supported, and every claim has carried an exact timestamp since Sep 1, 2026.

## Known issues and gotchas

- **Brand campaigns look like the best CPFTD in the account because they're closest to conversion.** Much of that is demand that other channels created or that would have come organically.
- **View-through installs** in Apple's reporting, and Apple's proposals to credit them, over-credit ASA.
- **Returning users show up as redownloads.** For an FTD-focused program, decide on purpose whether to pay for reacquisition, and read it separately from new-user CPFTD.
- **Search Match and broad match** leak spend into irrelevant or competitor-brand queries without tight negatives.

## What it means for Underdog

- **Hold brand to a higher standard.** Evan's own history: a measured ASA cell drifted brand-heavy and was paused, and Apple's view-through proposal was rejected as over-crediting. Keep Brand in its own campaign and read it against a holdout or a time-based on/off test, never on attributed CPFTD alone.
- **Use location refinement for legal footprint.** Where prediction markets or fantasy are only live in some states, refine at ad group level so spend doesn't go to searches from ineligible states. Keep these as single-country (U.S.) campaigns, since refinement doesn't work across multiple countries.
- **Competitor campaigns:** bidding on Kalshi, Polymarket, FanDuel, and DraftKings names is a standard ASA tactic. Check it against legal and brand policy and Apple's ad policies first.
- **Customer type:** run New users for FTD acquisition, and consider a separate Returning users ad group for lapsed-user reacquisition, read on its own economics.
- **Test custom product pages per theme** (prediction markets vs. fantasy, offer-led vs. product-led) as ASA creative tests. They count as `test_type: app-store` in `tests/`.
- **Check first:** any legacy ad groups with age or gender targeting (see [[appsflyer-underdog-setup-audit]]).

## Current incumbent

(Record the current winning custom product page per keyword theme and the test that crowned it.)

## Rep notes and betas

(None yet.)

## Test log

(None yet.)

## Open questions

- What is Apple's current ad policy on real-money gaming, prediction markets, and fantasy in the App Store? It's not in the help-center crawl; check Apple's ad policies and App Store Review Guidelines, or ask the Apple rep.
