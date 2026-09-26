---
title: Why AppsFlyer, Platform, and Warehouse Numbers Differ
type: doc
status: living
created: 2026-09-26
updated: 2026-09-26
owners: [evan]
tags: []
last_verified: 2026-09-26
verified_by: claude
related: ["[[appsflyer-attribution-model]]", "[[appsflyer-channel-integrations]]", "[[appsflyer-skan-and-ssot]]", "[[appsflyer-events-and-s2s]]"]
references:
  - https://support.appsflyer.com/hc/en-us/articles/115005600889-Troubleshooting-discrepancies-in-AppsFlyer-dashboards-and-reports
  - https://support.appsflyer.com/hc/en-us/articles/4410481130641-Meta-ads-discrepancies
  - https://support.appsflyer.com/hc/en-us/articles/19733501619473-Attribution-discrepancies-between-TikTok-for-Business-and-AppsFlyer
  - https://support.appsflyer.com/hc/en-us/articles/4417686973841-Snapchat-integration-discrepancies
  - https://support.appsflyer.com/hc/en-us/articles/4417303339921-Google-Ads-AdWords-FAQ-and-discrepancies
  - https://support.appsflyer.com/hc/en-us/articles/207040726-Resolve-AppsFlyer-App-stores-discrepancies
  - https://support.appsflyer.com/hc/en-us/articles/14038324952465-Campaign-name-changes
---

## Summary

Three layers count differently by design:

- **Platforms** claim credit using their own rules.
- **AppsFlyer** assigns credit using neutral last-touch rules.
- **The warehouse** records what actually happened (the internal FTD).

A gap between them is normal. Only a gap that *moves* is a signal.

## The checklist, in order of how often it's the cause

1. **Lookback windows.** Platform click and view windows differ from AppsFlyer's. Snap's defaults are the longest.
2. **View-through.** The platform counts views that AppsFlyer ignores, or the reverse.
3. **Timezone.** Meta and Snap default to PST, TikTok's is fixed at account creation, and AppsFlyer defaults to UTC.
4. **Cross-device.** Meta and TikTok credit cross-device conversions; AppsFlyer credits a single device.
5. **Install definition.** AppsFlyer uses first launch, networks use the engagement time, and stores use the download time.
6. **LTV vs. activity view.** AppsFlyer's LTV views count events against the install date; platforms count on the event date. Compare against an activity view (now in My Dashboards).
7. **Re-engagement vs. new install.** A reinstall inside the re-attribution window shows as a re-attribution in AppsFlyer but as a new install on the platform.
8. **Protect360 and validation rules.** AppsFlyer blocks or rejects installs that the platform still counts.
9. **iOS methods.** Platforms show SKAN or modeled numbers (TikTok is SKAN-only; Meta adds AEM modeling). AppsFlyer shows classic, SKAN, and SSOT views. Compare like with like.
10. **Late data.** The SKAN dashboard lags 48–72 hours, Google SKAN up to 45 days, and SSOT reads should leave out the last 3 days.
11. **S2S timing.** Events that arrive after 02:00 UTC the next day are stamped with their arrival date, and events that race the install land as organic.
12. **Duplicate events.** The same event sent through the Meta SDK and AppsFlyer, or through the SDK and S2S.
13. **Cost timing and currency.** Cost ETL restates the previous 6 days plus days 14, 29, and 88. Currency conversion happens hourly.
14. **Campaign renames.** These split history unless handled.

## Diagnosing a gap in five steps

1. Make the date range, timezone, platform (iOS or Android), and view (LTV or activity) the same on both sides.
2. Compare installs before events. If installs match but events don't, the problem is event mapping or timing.
3. Check the windows and view-through settings for that partner in AppsFlyer against the platform.
4. Check the Protect360 blocked and post-attribution reports for that partner.
5. For iOS, compare SKAN to SKAN first, then look at what SSOT adds.

## What it means for Underdog

- **The trust order is:**
  1. Warehouse FTDs, for the financial truth
  2. AppsFlyer, for neutral credit
  3. Platform dashboards, for in-channel optimization

  A valid experiment overrides all three.
- **Track the ratio of platform-reported to AppsFlyer-attributed FTDs** for each channel. A stable ratio is fine. A sudden jump means a setting changed, the platform's modeling changed, or fraud.
- **Never quote platform CPA as CPFTD.** In the weekly review, label platform-sourced numbers as such (see [[ua-weekly-review]]).
