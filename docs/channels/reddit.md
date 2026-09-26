---
title: Reddit Playbook
type: doc
status: living
created: 2026-09-26
updated: 2026-09-26
owners: [evan]
tags: [reddit]
channel: reddit
last_verified: 2026-09-26
verified_by: claude
related: ["[[appsflyer-channel-integrations]]", "[[appsflyer-attribution-model]]", "[[ad-policy-matrix]]"]
references:
  - https://business.reddithelp.com/s/article/app-install-ads
  - https://business.reddithelp.com/s/article/mmp-postbacks
  - https://business.reddithelp.com/s/article/app-event-optimization
  - https://business.reddithelp.com/s/article/skadnetwork
  - https://business.reddithelp.com/s/article/max-campaigns
  - https://business.reddithelp.com/s/article/Creative-Best-Practices
  - https://business.reddithelp.com/s/article/reddit-audiences
  - https://business.reddithelp.com/s/article/gambling-and-gaming-related-services-policy
  - https://business.reddithelp.com/s/article/Reddit-Advertising-Policy-Targeting-Guidelines
  - https://support.appsflyer.com/hc/en-us/articles/360011016138-Reddit-campaign-configuration
---

## Job

**High-intent communities.** People on Reddit are actively researching and discussing sports, fantasy, trading, and prediction topics. Target by community and keyword, not just by demographics. It's a smaller channel where relevance to the community matters more than polish.

## Account structure

- **App Promotion objective** needs **separate ad groups for Android and iOS.**
- **Max campaigns (beta):** automated bidding, creative-combination selection, and budget allocation to minimize CPA. You provide targeting and assets; there are no ad groups to manage. Reporting is by asset, placement, interest, community, and AI-generated audience persona.
- **Simple Create** uses lowest-cost bidding and optimizes for clicks.
- **Targeting:**
  - communities (subreddits)
  - keywords (Reddit claims keyword targeting drives far more incremental conversions per dollar than run-of-site)
  - interests
  - custom audiences
  - **automated targeting**, which Reddit recommends turning on to expand reach
- **Exclude existing users:** "Automatically exclude users who have installed your app" drops people who used the app in the last 90 days and haven't opted out of tracking. It works best when **all** postbacks are sent, attributed and unattributed.

## Bidding and optimization levers

- **App event optimization (AEO):** choose an in-app event goal with **lowest cost** bidding. Only events received through MMP postbacks in the last 7 days can be picked, and install is always available.
- **The event goal can't be changed after the ad group is saved.** Create a new ad group to change it.
- **App promotion bills on clicks.** Budgets are lifetime or daily per ad group, with an optional campaign spend cap.
- **Expect a learning phase** after launch or big edits.

## Signal and measurement setup

- **MMP postbacks are recommended for iOS and Android.** Generate Reddit click and impression tracker URLs in AppsFlyer, which come pre-templated. Events take 3–4 hours to appear in the Reddit dashboard.
- **In AppsFlyer, Reddit is a link-based network,** with a view-through toggle, cost API, and SKAN transaction-ID sharing (see [[appsflyer-channel-integrations]]).
- **SKAN is supported.** In Reddit's reporting, MMP reporting shows only MMP-attributed conversions and SKAN reporting shows only SKAN-attributed ones. Don't add them together.
- **Web:** Reddit Pixel plus Conversions API with deduplication. The default window counts view-through conversions within 1 day.

## Creative specs and what works

From Reddit's study of over 100,000 ads, the top headline features:

- Short: headlines of 150 characters or less.
- Variety: keep at least a third of headlines unique, and refresh every 3–4 weeks.
- **Mention the brand name** (Reddit reports a conversion-rate and CPA lift).
- Use **"you" and "your"**.
- A clear CTA framed around when, where, or how.

Reddit says **adopting even three of these can lift conversion rate noticeably.** Match community tone: native, conversational, no hard sell.

## Policy (see [[ad-policy-matrix]])

- **Gambling and gaming, which explicitly includes fantasy sports and "tips and advice for gambling, sports, betting",** requires **pre-approval and a Reddit sales rep** managing the account. It's only available in certain countries.
- **Required:**
  - comply with local law, licensing, and the gaming authority's ad standards
  - **only serve in communities Reddit permits**
  - **include terms and conditions, including odds-of-winning information, in the creative or on the landing page**
  - avoid minors and support-related subreddits
- **Prohibited:** glorifying gambling, unrealistic claims of winning, appeal to minors, and imagery of vulnerable groups or controlled substances.
- **Targeting guidelines:** never target users under 18, or addiction-support, mature, or medical communities.
- **Prediction markets:** not named in the gambling policy. Check whether Reddit treats them under Financial/Cryptocurrency Products and Services or under gambling (ask the rep).

## Known issues and gotchas

- **Reddit's reporting won't match AppsFlyer.** Reddit has a help article on third-party reporting mismatches: windows, view-through, and the SKAN vs. MMP split.
- **The event goal is locked per ad group,** so plan the FTD goal from the start.
- **Community allowlists for gambling** limit reach compared with standard campaigns.

## What it means for Underdog

- **Community and keyword targeting is the edge:** fantasy, specific sports, sports-trading, and prediction-topic communities, within Reddit's permitted list for gambling advertisers.
- **Optimize to the FTD event** from day one (AEO, lowest cost). Send all postbacks, including organic and unattributed, so existing-user exclusion works.
- **Add terms and odds disclosures** to Reddit landing pages or creative, as the policy requires. Check with legal how "odds of winning" applies to fantasy and prediction markets.
- **Test Max campaigns** against the incumbent manual structure as a split, not in parallel on the same audience.
- **Keep Reddit's job clear:** high-intent communities. Read it on incrementality given its small volume. Evan's history includes running Reddit's automated campaign beta (rMAX) as an early tester.

## Current incumbent

(Record the winning creative and the test that crowned it.)

## Rep notes and betas

(None yet. Ask for: prediction-markets classification, permitted community list for gambling advertisers, Max campaigns for app promotion.)

## Test log

(None yet.)
