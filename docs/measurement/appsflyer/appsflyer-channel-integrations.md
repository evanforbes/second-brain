---
title: AppsFlyer Channel Integrations
type: doc
status: living
created: 2026-09-26
updated: 2026-09-26
owners: [evan]
tags: [tiktok, meta, snapchat, google, reddit, apple-search-ads, liftoff, moloco, rzr]
last_verified: 2026-09-26
verified_by: claude
related: ["[[appsflyer-attribution-model]]", "[[appsflyer-discrepancies]]", "[[appsflyer-events-and-s2s]]"]
references:
  - https://support.appsflyer.com/hc/en-us/articles/207033826-Meta-ads-integration-setup
  - https://support.appsflyer.com/hc/en-us/articles/4410481130641-Meta-ads-discrepancies
  - https://support.appsflyer.com/hc/en-us/articles/19228737402129-Meta-Ads-Aggregate-Event-Measurement-AEM-for-iOS
  - https://support.appsflyer.com/hc/en-us/articles/6722785184913-TikTok-for-Business-Advanced-SRN-integration-setup
  - https://support.appsflyer.com/hc/en-us/articles/19733501619473-Attribution-discrepancies-between-TikTok-for-Business-and-AppsFlyer
  - https://support.appsflyer.com/hc/en-us/articles/211011983-Snapchat-Advanced-SRN-integration-setup
  - https://support.appsflyer.com/hc/en-us/articles/4417686973841-Snapchat-integration-discrepancies
  - https://support.appsflyer.com/hc/en-us/articles/115002504686-Google-Ads-AdWords-Integration-setup-for-advertisers
  - https://support.appsflyer.com/hc/en-us/articles/4417303339921-Google-Ads-AdWords-FAQ-and-discrepancies
  - https://support.appsflyer.com/hc/en-us/articles/213747963-Apple-Ads-integration-setup
  - https://support.appsflyer.com/hc/en-us/articles/360011016138-Reddit-campaign-configuration
  - https://support.appsflyer.com/hc/en-us/articles/209731633-Liftoff-campaign-configuration-in-AppsFlyer
  - https://support.appsflyer.com/hc/en-us/articles/360000691978-MOLOCO-campaign-configuration
  - https://support.appsflyer.com/hc/en-us/articles/360000423105-RZR-formerly-Aarki-campaign-configuration
  - https://support.appsflyer.com/hc/en-us/articles/360012640377-SKAN-integrated-partners-list
  - https://support.appsflyer.com/hc/en-us/articles/50216486847249-Bulletin-Apple-Ads-adds-timestamps-to-all-attribution-claims
  - https://support.appsflyer.com/hc/en-us/articles/17798585594641-Bulletin-Snapchat-has-become-an-Advanced-SRN
---

## Summary

How each of the nine channels connects to AppsFlyer, and the measurement caveat that matters most for each. Channel strategy lives in the channel playbooks (`docs/channels/`); this note covers only the AppsFlyer side.

## By channel

| Channel | AppsFlyer integration | Key measurement facts |
|---|---|---|
| **Meta** | SRN | Meta defaults to 7-day click and 1-day view. Ads Manager defaults to PST, AppsFlyer to UTC. On iOS, Meta's AEM sends modeled claims that may not appear in Ads Manager. On Android, the Meta install referrer enables raw data (AppsFlyer has an action-required bulletin on this). Meta counts cross-device, and duplicate events sent through both the Meta SDK and AppsFlyer are not deduped. S2S events sent on to Meta need `ua` and `ip`. For Flexible ads, creative reporting shows only the best-performing asset |
| **TikTok** | Advanced SRN (`tiktokglobal_int`, since Jan 2023; the legacy `bytedanceglobal_int` is retired) | 7-day click and 1-day view by default; the view window is configurable from 1 to 48 hours in AppsFlyer. TikTok's timezone is fixed when the ad account is created. On iOS, TikTok Ads Manager shows **only SKAN**, so only SKAN is expected to match. TikTok counts cross-device. **From June 23, 2026, the Advanced Data Sharing toggle replaced Advanced Privacy on iOS, and AppsFlyer shares all conversion events with TikTok whether or not an IDFA is present**, so more iOS conversions get attributed to TikTok from that date |
| **Snapchat** | Advanced SRN | Snap's default windows are longer (28-day in-app event attribution), and Snap can allowlist an account to match MMP windows through its CSM. Ads Manager defaults to PST |
| **Google** | SRN | Conversions are imported into Google Ads (`first_open` plus in-app events). Google accepts events inside its own 30–90 day window. SKAN installs from Google can arrive up to 45 days late. The Creative Optimization integration must be set up by the same user who set up ROI360. Google recommends App campaigns |
| **Apple Search Ads** | Apple Ads API | Click-based attribution, plus impression-based since Mar 27, 2025. **From Sep 1, 2026, Apple adds an exact timestamp to every attribution claim, and ad groups using age or gender targeting return no attribution, so those installs can't be credited to Apple Ads in AppsFlyer.** The view window is 24h max. There's no re-engagement retargeting, and installs don't appear in the SKAN dashboard. Cost data needs ROI360 |
| **Reddit** | Link-based | View-through is a toggle (the window is set on the attribution link tab). Custom events like `rdt_ad_click`. Cost comes through the API. The SKAN transaction ID can be shared. No ad revenue |
| **Liftoff** | Link-based | Click and view-through attribution, plus retargeting. Cost comes through the API. Creative Optimization uses reporting API credentials from the Liftoff CSM |
| **Moloco** | Link-based | View-through is a toggle. Cost API: the previous day's cost arrives around 4am in the account's timezone |
| **RZR (formerly Aarki)** | Link-based | Click and view-through attribution, plus click-based retargeting. Pass `af_ad` for creative-level reads. The re-engagement window is 1–90 days or lifetime |

## Gotchas

- **Different windows:** every SRN has default windows and a timezone that differ from AppsFlyer's. Differences come first from the windows, then the timezone, then cross-device counting (see [[appsflyer-discrepancies]]).
- **Advanced SRNs change how iOS numbers look.** TikTok and Snap claim non-consented iOS users through aggregated privacy measurement, so their AppsFlyer numbers sit between the classic view and SKAN.
- **DSP view-through is where over-credit hides.** Liftoff, Moloco, and RZR all offer it.

## What it means for Underdog

- **Every channel should receive the same canonical FTD event** in its postback mapping. Decide once whether revenue goes with it (see [[appsflyer-events-and-s2s]]).
- **Mark June 23, 2026 as a trend break for TikTok iOS.** A jump in TikTok-attributed iOS volume after that date comes from the change in data sharing, not from performance, so don't let it drive a budget move without the warehouse agreeing.
- **Treat TikTok iOS as a SKAN-only read inside TikTok,** and use the AppsFlyer SSOT view for the blended picture.
- **Apple Search Ads, top priority to check.** Since Sep 1, 2026, any ASA ad group with age or gender targeting returns no attribution, so its installs and FTDs fall to organic in AppsFlyer. If Underdog age-gates ASA ad groups for real-money gaming compliance, ASA's attributed CPFTD looks worse and organic looks better starting that date. Compare ASA installs in Apple's console with AppsFlyer before and after Sep 1, and ask the Apple rep whether age gating can move to another control. Claims also carry exact timestamps now, so re-check any ASA reconciliation logic built before then.
- **Audit the DSPs (Liftoff, Moloco, RZR):**
  - their view-through setting and window
  - their share of engaged and view attributions
  - their Protect360 rejections

  Each DSP's job is incremental reach that has to prove itself, so their attributed CPFTD gets the most skepticism.
- **The AppsFlyer app timezone should match** whichever platform timezone the daily CPFTD reads are compared against. Otherwise day-level numbers never tie out.

## Open questions

Tracked in [[appsflyer-underdog-setup-audit]].
