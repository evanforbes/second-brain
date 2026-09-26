---
title: TikTok Playbook
type: doc
status: living
created: 2026-09-26
updated: 2026-09-26
owners: [evan]
tags: [tiktok]
channel: tiktok
last_verified: 2026-09-26
verified_by: claude
related: ["[[appsflyer-channel-integrations]]", "[[appsflyer-skan-and-ssot]]", "[[ad-policy-matrix]]"]
references:
  - https://ads.tiktok.com/help/article/about-self-attribution-transition?lang=en
  - https://ads.tiktok.com/help/article/tiktok-ads-best-practices?lang=en
  - https://ads.tiktok.com/help/article/split-testing?lang=en
  - https://ads.tiktok.com/help/article/tiktok-ads-policy-gambling-and-games?lang=en
  - https://ads.tiktok.com/help/article/tiktok-ads-policy-other-products-and-services?lang=en
  - https://ads.tiktok.com/help/article/tiktok-ad-policy-change-log-2026?lang=en
  - https://support.appsflyer.com/hc/en-us/articles/6722785184913-TikTok-for-Business-Advanced-SRN-integration-setup
  - https://support.appsflyer.com/hc/en-us/articles/19733501619473-Attribution-discrepancies-between-TikTok-for-Business-and-AppsFlyer
---

## Job

**Demand creation.** Entertainment-first video, native-feeling creative, and fast-moving trends. Evan's own history: a five-week geo holdout showed TikTok meaningfully incremental even though the attribution model called it expensive. **The experiment overruled the model, and TikTok scaled.**

## Account structure

- **Smart+ App campaigns** are TikTok's automated app campaigns (targeting, bidding, creative mixing).
  - **Let them run at least 7 days,** and 50 conversions, to exit the learning phase. Avoid pausing or editing.
  - **Load at least 4–6 creatives at launch.** Keep the multilingual creative tool on.
  - Multiple Smart+ campaigns need genuinely different targeting or creative.
- **Manual campaigns:**
  - **Don't bulk-copy or duplicate ad groups,** especially new ones.
  - Keep learning-phase and post-learning ad groups in balance.
  - Diversify targeting, OS, and creative across ad groups.
  - When performance drops, adjust the existing ad group instead of spawning new ones.
- **iOS 14.5+:** dedicated SKAN campaigns (with a quota) and a dedicated campaign objective setup.

## Bidding and optimization levers

- **Maximum Results** (spend-based, maximum volume): start the daily budget at **10× historical CPA** or more. Expect CPA volatility during competitive periods.
- **Target Cost per Result** (goal-based; recommended on Smart+ Android, with iOS coming):
  - Set the target from the **last 7 days' CPA.** Too low a target starves delivery.
  - Budget more than 3× usual, or **30× target CPA.**
  - Monitor the bidding ratio (real CPA divided by bid).
- **Fatigue signals:** 2× CPA or half the ROAS vs. normal, or CTR or CVR falling for 2 days. Fix by **adding 2–5 creatives while keeping existing ones,** and budget to match. Judge after 3 or more days. Relaunch only as a last resort.
- **App Event Optimization (AEO):** optimize to FTD. Allow the learning phase. **On iOS SKAN AEO campaigns, aim for 90+ installs per day per campaign,** or Apple's privacy threshold returns null conversions.

## Signal and measurement setup

- **Self-Attributing Network (SAN).** TikTok's legacy MMP integration was **discontinued on March 31, 2025.** Apps must be on SAN, where TikTok self-attributes (AppsFlyer's Advanced SRN integration is `tiktokglobal_int`).
- **Attribution windows in TikTok Ads Manager:** click-through 1 or 7 days, **engaged view-through (EVTA) 1 or 7 days**, view-through off or 1 day. These windows only change TikTok's own reporting, not AppsFlyer's. Keep the two consistent to reduce discrepancies.
- **EVTA:** credit after **6+ seconds watched** (or the full video if it's shorter). Break it out from CTA and VTA with custom columns.
- **Unattributed events:** send them from AppsFlyer (organic and other-network events) to power retargeting audiences **and TikTok's optimization models.**
- **June 23, 2026:** AppsFlyer began sharing all iOS conversions with TikTok regardless of IDFA, which is a trend break (see [[appsflyer-channel-integrations]]).
- **On iOS, TikTok Ads Manager shows only SKAN.** Compare SKAN to SKAN.

## Creative specs and what works

- **TikTok-first:** sound on, 9:16, 720p or higher, inside UI safe zones.
- **Show people** (creators, employees, customers), in a DIY style. Use trends, memes, and challenges.
- **Structure:** hook in the first 6 seconds, value proposition in the first 3 seconds, captions at 5–10 words per second, end with a clear CTA.
- **Tools:** Creative Center for trends and the music library, and Symphony Creative Studio (AI creative).
- **Split testing** gives a statistically tested A/B (90% confidence) on targeting, placement, bidding, budget, creative, or Smart+.

## Policy (see [[ad-policy-matrix]])

- **Fantasy sports and daily fantasy:** allowed in the U.S. **only with permission through a TikTok sales rep,** a valid local license, and age targeting. Policy last updated August 2026, with changes to online gambling and fantasy sports in July 2026.
- **Prediction markets:** allowed with restrictions in the U.S. and some other markets. It requires a rep application, age targeting, and disclosures and disclaimers. **Creative must use trading and event-contract language:**
  - **Allowed:** financial-trading or event-contract terminology, regulated event-trading platforms, users trading contracts with each other.
  - **Not allowed:** calling it "placing bets", gambling terminology, or odds-based or sportsbook-style presentation.

## Known issues and gotchas

- **SKAN AEO below about 90 installs a day** produces null conversions and misleading TikTok iOS reads.
- **TikTok counts cross-device and EVTA conversions.** AppsFlyer counts single-device conversions. Expect TikTok's claims to run higher.
- **Duplicating ad groups hurts learning,** as does keeping most ad groups in learning at once.

## What it means for Underdog

- **Prediction-markets creative needs its own copy system.** Every prediction-markets TikTok ad must say "trade," "contracts," or "predict," never "bet," "odds," or "wager." Add this as a checklist item for the creative team, and to `test_type: creative` Setup for any prediction-markets test.
- **Keep fantasy and prediction markets as separate approvals, campaigns, and creative.** They're governed by different policies.
- **Consolidate iOS** to clear 90+ installs a day per SKAN campaign. Treat state-restricted splits carefully.
- **Send unattributed FTD events** from AppsFlyer, if privacy review allows, to improve TikTok optimization.
- **Creative is the lever.** Use Smart+ with 4–6 or more creatives and add challengers in batches of 2–5. Run formal split tests for concept-level reads, and read CPFTD in Hex before calling a winner.
- **Keep EVTA consistent** between TikTok and AppsFlyer (both engaged-view windows), and treat engaged-view credit as directional.

## Current incumbent

(Record the winning creative and the test that crowned it.)

## Rep notes and betas

(Evan's history: a TikTok value-optimization beta mapped the purchase event to FTD. Ask for: current value-optimization eligibility for FTD, and prediction-markets approval status.)

## Test log

(None yet.)
