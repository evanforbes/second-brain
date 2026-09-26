---
title: AppsFlyer Web-to-App, OneLink, and Web Measurement
type: doc
status: living
created: 2026-09-26
updated: 2026-09-26
owners: [evan]
tags: [landing-page]
last_verified: 2026-09-26
verified_by: claude
related: ["[[appsflyer-attribution-model]]", "[[appsflyer-channel-integrations]]"]
references:
  - https://support.appsflyer.com/hc/en-us/articles/360000677217-OneLink-Smart-Script-overview
  - https://support.appsflyer.com/hc/en-us/articles/4413588932241-Set-up-Smart-Script-to-convert-web-visitors
  - https://support.appsflyer.com/hc/en-us/articles/360001237818-Convert-your-mobile-web-visitors-to-app-users
  - https://support.appsflyer.com/hc/en-us/articles/115005248543-OneLink-guide
  - https://support.appsflyer.com/hc/en-us/articles/360000764837-Smart-Banners-mobile-web-to-app-for-marketers
  - https://support.appsflyer.com/hc/en-us/articles/43521734577809-Web-Performance-Measurement-Overview
  - https://support.appsflyer.com/hc/en-us/articles/49156441281425-Migrate-from-PBA-to-Web-Performance-Measurement
  - https://support.appsflyer.com/hc/en-us/articles/19228737402129-Meta-Ads-Aggregate-Event-Measurement-AEM-for-iOS
  - https://support.appsflyer.com/hc/en-us/articles/39686956300433-Bulletin-Consolidated-Web-App-reporting-for-Meta-Ads-and-Google-Ads
---

## Summary

Web-to-app adds a second click, from the landing page to the app store. Without a bridge, the install looks organic or gets credited to the wrong source. **OneLink Smart Script** is the bridge. It reads the incoming ad URL on the landing page and writes a unique outgoing OneLink per visitor, so the install inherits the original campaign.

## How it works

**Smart Script:**
- Maps incoming parameters (media source, campaign, click IDs, UTMs) onto outgoing OneLink parameters.
- Works for ad networks, SRNs, Google clicks, and owned media.
- Can also carry a deep-link destination.

**OneLink:**
- Templates, branded domains, short or long URLs (short-link TTLs now extend automatically), and bulk creation through the API or CSV.
- On iOS, owned-media and Smart Script installs are attributed **probabilistically**.

**Smart Banners:** an app-install banner on the mobile site that supports multiple media sources for attribution.

**Web measurement:** People-Based Attribution (PBA) is being replaced by **Web Performance Measurement**. It uses the same Web SDK with no website code change, but reports and S2S fields change, and AppsFlyer publishes a migration field map.

**Web campaigns in each platform:** AppsFlyer has setup guides for "web-based campaigns" and "web campaigns for website apps" on Meta, TikTok, Snap, and Google. **Consolidated Web+App reporting:** new Meta Web attributions (`metaweb_int`) now report as Facebook Ads, and Google Web (`googleads_int`) as `googleadwords_int`. Their web cost rolls up under the main media source. This isn't applied to past data, so web and app volume blend in channel totals from the change onward.

**Meta AEM re-engagement (iOS):** Meta appends campaign IDs to deep links. The AppsFlyer SDK must share deep links from all domains for this to work.

## Gotchas

- A landing-page variant missing Smart Script leaks installs to organic. That leak makes the variant *look* worse in AppsFlyer while making organic look better.
- iOS web-to-app attribution is probabilistic, so treat it as directional.
- Once a platform "web campaign" credits its own conversion through Pixel or CAPI, it will never match AppsFlyer's app-install credit.

## What it means for Underdog

- **Every landing-page test** (`test_type: landing-page`) must confirm that each variant loads the same Smart Script configuration before launch. Otherwise the readout compares measurement coverage, not the pages. Add this to the test's Setup section.
- **Prediction-markets and fantasy web funnels:** preserve the chain ad → site → store → install → FTD. Where the chain breaks, fall back to warehouse FTDs by landing-page cohort rather than AppsFlyer credit.
- **If PBA is still in use, plan the Web Performance Measurement migration** before it's forced. Ask the AppsFlyer CSM for the deadline.

## Open questions

Tracked in [[appsflyer-underdog-setup-audit]].
