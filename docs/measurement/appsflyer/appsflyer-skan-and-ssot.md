---
title: AppsFlyer SKAN, Conversion Studio, and SSOT
type: doc
status: living
created: 2026-09-26
updated: 2026-09-26
owners: [evan]
tags: []
last_verified: 2026-09-26
verified_by: claude
related: ["[[appsflyer-attribution-model]]", "[[appsflyer-events-and-s2s]]", "[[appsflyer-discrepancies]]"]
references:
  - https://support.appsflyer.com/hc/en-us/articles/360011420698-SKAdNetwork-SKAN-solution-guide
  - https://support.appsflyer.com/hc/en-us/articles/4403727223185-SKAN-Conversion-Studio
  - https://support.appsflyer.com/hc/en-us/articles/4410634145425-Single-Source-of-Truth-SSOT-guide-for-iOS-attribution
  - https://support.appsflyer.com/hc/en-us/articles/26542697382417-Single-Source-of-Truth-SSOT-Data-Locker-report-for-marketers
  - https://support.appsflyer.com/hc/en-us/articles/28968432692241-SKAN-conversion-schema-templates
  - https://support.appsflyer.com/hc/en-us/articles/7078169815057-SKAN-recommendations
  - https://support.appsflyer.com/hc/en-us/articles/7086372479505-SKAN-modeled-data
  - https://support.appsflyer.com/hc/en-us/articles/360011307357-SKAdNetwork-SKAN-overview-dashboard-by-AppsFlyer
  - https://support.appsflyer.com/hc/en-us/articles/4402320969617-Send-SKAN-and-AdAttributionKit-postback-copies-directly-to-AppsFlyer-iOS-15
  - https://support.appsflyer.com/hc/en-us/articles/360018515798-Apply-Aggregated-Advanced-Privacy-framework
  - https://support.appsflyer.com/hc/en-us/articles/46643660055057-Bulletin-Event-Overview-and-Activity-dashboards-deprecation
---

## Summary

On iOS, Apple decides attribution through SKAN and reports it late, in aggregate, and with limited quality data. AppsFlyer's job is the **conversion value (CV) schema**: deciding which early user actions get encoded into the few values Apple allows. **SSOT** (Single Source of Truth) then dedupes SKAN against AppsFlyer's other methods so the same iOS user isn't counted twice.

The CV schema *is* the iOS measurement strategy. Treat it that way.

## How it works

**SKAN 4 windows** (the default mode in Conversion Studio):

| Window | Post-install period | Values available |
|---|---|---|
| 1 | days 0–2 | Fine CV, 64 values (6 bits), plus a coarse CV |
| 2 | days 3–7 | Coarse only: low, medium, high |
| 3 | days 8–35 | Coarse only |

- Each window covers only its own period. Window 2 measures days 3–7, not days 0–7.
- **Apple's crowd anonymity** decides whether a postback carries the fine value, only the coarse value, or nothing. Low volume means less data.
- **The low coarse value must be a session.** Otherwise the postback may not send.
- **Lock window** (optional) closes a window early, based on time or on reaching a coarse value. Earlier locks mean faster postbacks.

**Conversion Studio modes:**
- **SKAN 4:** revenue, in-app event, and priority components, set per window.
- **Custom:** a single activity window of 12 hours to 63 days.
- **Decode:** you set the CVs yourself, and S2S events are not supported.
- **Fixed modes:** legacy, and unavailable to apps created after June 2024.

In SKAN 4 and Custom modes, **S2S events are always on**, so server-reported events can count toward the CV.

**SSOT:**
- **Setup:** turn it on in Conversion Studio (Custom settings). It has billing implications.
- **Dedupe flag:** SKAN installs that another method also matched are flagged with `af_attribution_flag = true` and left out of totals.
- **Where to read it:** the help article describes an SSOT switch in the Overview dashboard (Lite overview), with data appearing 3–5 days after enabling. **But the legacy Overview dashboard was retired on June 30, 2026, and replaced by My Dashboards.** Find the SSOT view in My Dashboards, or use the SSOT Data Locker report.
- **Modeled data:** null CVs are modeled, and D2/D7 revenue includes modeled values.
- **Longer cohorts** (D14–D30) come from the SSOT Data Locker report.
- **Best practice:** leave the most recent 3 days out of any SSOT read.
- **Google's SKAN installs can arrive up to 45 days late.**
- **The SKAN dashboard lags installs by 48–72 hours.**
- **Apple Search Ads installs don't appear in the SKAN dashboard,** because Apple Ads has its own API.

**Platform views differ.** TikTok Ads Manager shows only SKAN results for iOS. Meta adds AEM, its modeled measurement, and can send AppsFlyer modeled claims that never appear in Ads Manager.

**AdAttributionKit.** On iOS 15 and later, postback copies can be sent directly to AppsFlyer, covering both SKAN and AdAttributionKit.

**Aggregated Advanced Privacy (AAP).** When on, user-level attribution for non-consented iOS 14.5+ users is withheld from raw data, the Pull API, and partner postbacks. Aggregate reports are unaffected.

## Gotchas

- Changing the schema changes what the SKAN dashboard means from the next day (the layout updates daily based on the mode active at midnight UTC). Log every schema change in [[decision-log]], or week-over-week iOS reads silently break.
- Fine values exist only in window 1. Anything you want measured precisely has to happen within 48 hours of install.
- Small campaigns and ad sets get nulls or coarse-only values. A fragmented iOS campaign structure loses data.

## What it means for Underdog

- **Build the schema on the value ladder.** In priority order: revenue and retention, then FTD and first entry, then KYC, then registration, then install or open.
  - Window 1 fine values should separate registration, KYC, FTD, and first entry, and ideally bucket the first deposit's size.
  - Coarse values in windows 2 and 3 should capture repeat deposits and entries.
- **FTD is confirmed on the server,** so it only reaches the CV if the Hightouch/S2S event lands quickly and is mapped. Confirm with the AppsFlyer CSM that server-sent FTDs are updating CVs inside window 1 (48 hours).
- **Revenue in the CV is deposit value, not NGR,** if deposits are sent as `af_revenue`. That's a decent early LTV proxy, but label it as such everywhere (see [[appsflyer-events-and-s2s]]).
- **Read iOS channel performance from the SSOT view** (in My Dashboards or the SSOT Data Locker report), not the classic numbers. Always leave out the last 3 days, and treat Google iOS as incomplete for up to 45 days.
- **Keep iOS campaign structure consolidated,** especially in state-restricted campaigns where volume is thin, so crowd anonymity passes more fine values.
- **Channel-level iOS truth still comes from experiments.** SKAN is a directional signal, to be triangulated with SSOT, holdouts, and MMM.

## Open questions

Tracked in [[appsflyer-underdog-setup-audit]].
