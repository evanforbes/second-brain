---
title: Ad Policy Matrix — Fantasy and Prediction Markets
type: doc
status: living
created: 2026-09-26
updated: 2026-09-26
owners: [evan]
tags: [fantasy, prediction-markets]
last_verified: 2026-09-26
verified_by: claude
related: ["[[google]]", "[[meta]]", "[[tiktok]]", "[[snapchat]]", "[[reddit]]", "[[x]]", "[[apple-search-ads]]", "[[moloco]]", "[[liftoff]]", "[[rzr]]"]
references:
  - https://support.google.com/adspolicy/answer/15132179?hl=en
  - https://support.google.com/adspolicy/answer/16757872?hl=en
  - https://support.google.com/adspolicy/answer/17230476?hl=en
  - https://support.google.com/googleplay/android-developer/answer/16902027?hl=en
  - https://www.facebook.com/business/help/345214789920228
  - https://transparency.meta.com/policies/ad-standards/restricted-goods-services/gambling-games/
  - https://ads.tiktok.com/help/article/tiktok-ads-policy-gambling-and-games?lang=en
  - https://ads.tiktok.com/help/article/tiktok-ads-policy-other-products-and-services?lang=en
  - https://values.snap.com/policy/ads-category-requirements/gaming-gambling-lotteries
  - https://businesshelp.snapchat.com/s/article/snap-gaming-terms?language=en_US
  - https://business.reddithelp.com/s/article/gambling-and-gaming-related-services-policy
  - https://business.x.com/en/help/ads-policies/ads-content-policies/gambling-content
  - https://help.moloco.com/hc/en-us/articles/8838808037527-Troubleshoot-creatives
---

## Summary

Whether and how each Underdog product can advertise on each channel, as of the Sep 26, 2026 crawl. **Policies change often, especially the state lists and prediction-market rules.** Re-verify monthly and before any launch in a new state. This is a working summary, not legal advice. Legal and compliance sign off on the actual approach.

## Matrix (U.S.)

| Channel | Fantasy / DFS | Prediction markets | Age floor | Must-dos |
|---|---|---|---|---|
| **Google** | Certification required. A state license where required, otherwise licensed in at least one state that requires it. DFS opened state by state (Colorado since Jul 1, 2026) | **Dedicated policy** since Jan 21, 2026: certification, and the advertiser must be a **CFTC DCM** or **NFA-authorized brokerage**. **U.S. only, excluding MI, NV, NY, OH** (MI and NY explicitly banned from Jul 13, 2026). A separate application per location | 18 (DFS); 21 (sports betting on YouTube) | DFS: adult-only disclaimer on the landing page, and problem-gambling info in the ad or on the landing page. Google Play: real-money prediction-market apps had to join the Play pilot by Jun 1, 2026 (gambling-licensed ones fall under the RMG policy instead) |
| **Meta** | Online gambling and games authorization per ad account, per territory, per gaming type (fantasy is explicitly covered) | Not named in the help center. **Ask the rep** whether it's gambling authorization or financial services | 18 | Declare intent in Meta Business Suite before targeting any new jurisdiction. No unsupported markets |
| **TikTok** | Allowed with permission through a **sales rep**, a local license, and age targeting | **Allowed with restrictions** (U.S. is eligible): rep application, age targeting, disclaimers. **Must use trading and event-contract language. No "bets," gambling terms, or sportsbook-style odds** | Appropriate audience (age-targeted) | Policy updated Jul and Aug 2026 |
| **Snapchat** | Pre-approval: gambling application, Snap Gambling Terms, license proof per territory | Not named. **Ask the rep** | Legal gambling age per territory; set a minimum age | No glorifying, no play beyond means, no tipster or odds services. Tell Snap about license changes immediately |
| **Reddit** | Pre-approval, **account managed by a Reddit sales rep**. Fantasy is explicitly covered | Not named in the gambling policy. **Ask the rep** (financial vs. gambling) | 18; never target support communities | Only serve in permitted communities. **Terms and odds-of-winning info** in the creative or on the landing page |
| **X** | Pre-approval and certification. U.S. fantasy is "permitted with restrictions." Accept X Gambling Terms | Not named. **Ask the rep** | Per law; geo- and age-target | Warrant compliance with every state law, and report regulatory rulings to X immediately |
| **Apple Search Ads** | Governed by Apple's ad policies and App Store rules (not in the help-center crawl). **Check Apple's policy** | Same | App age rating | Use location refinement to stay inside legal states |
| **Moloco** | Mark the app as **Real Money Gaming** at registration. Google AdX supply needs the app **Google-certified** for gambling, and Kakao prohibits gambling | Ask the rep | Per law | Keep the RMG flag and certifications current, or supply drops |
| **Liftoff** | Liftoff runs iGaming and DFS programs (for example, PrizePicks). Ask about inventory compliance controls | Ask the rep | Per law | Confirm excluded exchanges and placements for underage audiences |
| **RZR** | No public policy. Ask the rep | Ask the rep | Per law | — |

## Patterns across channels

1. **Every major channel requires pre-approval for fantasy,** through a certification, authorization, or sales-rep process. Licenses are checked **per state or territory.**
2. **Prediction markets are becoming their own category.** Google and TikTok now have dedicated rules built on financial-regulator status (CFTC and NFA) and **trading language, not betting language.** Expect the other platforms to follow, and keep prediction-markets creative, landing pages, and accounts separate from fantasy.
3. **State lists move monthly.** Examples: Google's DFS expansion, Colorado (Jul 2026), and the Michigan and New York prediction-market bans (Jul 2026). Campaign geo-exclusions have to be maintained, not set once.
4. **Disclosures that often apply:** adult-only notices, problem-gambling resources, terms, and odds-of-winning information. Build them into landing-page templates once.

## What it means for Underdog

- **Keep a per-channel approval register.** For each channel, track the approved entity, products, states, and renewal date. It's a candidate for a small table in this note, filled in by Evan (settings only).
- **Two creative systems:** fantasy creative (gambling-policy compliant) and prediction-markets creative (trading and event-contract language). Every creative test declares which one it uses.
- **Geo hygiene checklist before any launch:** is the product legal in the state, is the channel approved for the state, and is the channel's own list (Google, for example) allowing the state?

## Open questions

- [ ] Which Underdog entity, or which partner exchange, qualifies for Google's prediction-markets certification (CFTC DCM or NFA brokerage)?
- [ ] How do Meta, Snap, Reddit, X, and Apple classify prediction markets: gambling or financial services?
- [ ] Is Underdog's Android prediction-markets app enrolled in the Google Play pilot, or covered under the RMG policy?
