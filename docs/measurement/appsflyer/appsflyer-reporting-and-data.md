---
title: AppsFlyer Reporting, Creative Optimization, and Data Access
type: doc
status: living
created: 2026-09-26
updated: 2026-09-26
owners: [evan]
tags: [creative]
last_verified: 2026-09-26
verified_by: claude
related: ["[[appsflyer-mcp]]", "[[appsflyer-discrepancies]]", "[[appsflyer-skan-and-ssot]]", "[[naming-taxonomy]]"]
references:
  - https://support.appsflyer.com/hc/en-us/articles/23461861877009-My-Dashboards
  - https://support.appsflyer.com/hc/en-us/articles/46643660055057-Bulletin-Event-Overview-and-Activity-dashboards-deprecation
  - https://support.appsflyer.com/hc/en-us/articles/18564718580625-Creative-Optimization-guide
  - https://support.appsflyer.com/hc/en-us/articles/18565403047569-Creative-Optimization-partner-integrations
  - https://support.appsflyer.com/hc/en-us/articles/18565941422993-Creative-Optimization-Discovery-AI-dashboard
  - https://support.appsflyer.com/hc/en-us/articles/19253873174801-Creative-Optimization-ETL-reporting
  - https://support.appsflyer.com/hc/en-us/articles/207040526-ROI360-cost-aggregation-overview
  - https://support.appsflyer.com/hc/en-us/articles/360008849238-Set-up-and-use-ROI360-cost-ETL-reports
  - https://support.appsflyer.com/hc/en-us/articles/360000877538-Data-Locker-for-marketers
  - https://support.appsflyer.com/hc/en-us/articles/360017603577-Data-Locker-cloud-service-setup
  - https://support.appsflyer.com/hc/en-us/articles/213223166-Master-API-user-acquisition-metrics-via-API
  - https://support.appsflyer.com/hc/en-us/articles/360004799057-Cohort-API
  - https://support.appsflyer.com/hc/en-us/articles/208387843-Raw-data-field-dictionary
  - https://support.appsflyer.com/hc/en-us/articles/4415473374865-Data-availability-windows
  - https://support.appsflyer.com/hc/en-us/articles/15557418667537-Historical-aggregate-data-availability
---

## Summary

The places AppsFlyer data can be read, and what each is good for. For Underdog, three paths matter:

- **Creative Optimization,** for the weekly creative readout.
- **Data Locker to BigQuery,** for the warehouse and Hex.
- **The AppsFlyer MCP connector,** for asking questions in plain language (see [[appsflyer-mcp]]).

## How it works

**Dashboards:**
- **My Dashboards** has been the main analytics experience since the legacy Events, Overview, and Activity dashboards were retired on **June 30, 2026**. It shows clicks through cohort, retention, SKAN, SSOT, and in-app event metrics side by side, and supports custom widgets and metrics (with some limits on cohort metrics).
- **LTV views** count events against the install date. **Activity views** count events on the day they happened. Pick deliberately: LTV for cohort CPFTD, activity for "what happened yesterday."
- **The Retention dashboard** was retired in October 2025. Cohort data has included unattributed sessions and events since May 2024.

**Creative Optimization:**
- Pulls creative assets and performance from every connected channel into one place, either the dashboards or Creative ETL into your BI tool.
- **AI and computer vision match the same asset across channels and campaigns, regardless of naming.**
- Data is LTV-based, and the Discovery dashboard adds AI-driven pattern finding.
- **Multi-asset ads aren't broken down by asset** (Meta Advantage+ and dynamic creative, Google UAC). For Meta Flexible ads, only the best-performing asset is reported.
- **Partner connections are made per user:**
  - Google must be connected by the same user who connected ROI360.
  - Meta needs ad account permissions.
  - Liftoff needs reporting API credentials from its CSM.
- **Cost data:** with ROI360, cost comes from ROI360. Creative ETL cost requires ROI360 Advanced.

**Cost (ROI360):**
- Pulls cost by API from each network.
- **Cost ETL restates the current day and the previous 6 days, plus days 14, 29, and 88.** Recent CPFTD will move as cost corrections land.
- Moloco's cost for the previous day lands around 4am in the account's timezone.

**Data Locker:**
- Delivers report data to cloud storage: AWS, GCS, **BigQuery**, or Snowflake.
- Most data is written hourly; reports like uninstalls are daily.
- Includes raw data, cohort, SSOT, SKAN, and advanced aggregated reports.

**APIs:**
- **Master API:** aggregate UA metrics.
- **Cohort API**
- **Pull API:** raw data, with limited history windows.
- **SKAN APIs:** aggregated performance and postback arrival date.

**Raw data:** the field dictionary defines every column, including `engagement_type`, the contributor fields, and `af_attribution_flag` (SSOT).

## Gotchas

- Any saved views or bookmarks pointing at the legacy Overview or Activity dashboards are dead. Rebuild them in My Dashboards.
- Creative Optimization can't compare single assets inside Advantage+ or UAC. Asset-level tests on those channels need separate ads or ad sets.
- Recent days of cost are provisional because of the ROI360 restatement schedule.

## What it means for Underdog

- **Weekly creative readout:** if Creative Optimization is licensed, it's the fastest cross-channel source of scale, CPI, IPM, CPM, and CTR. Cross-channel visual matching means an asset's results roll up even when its names differ. For CPFTD by creative, confirm the FTD event appears as an event metric in Creative Optimization.
- **Creative tests on Meta and Google must be structured** so the challenger and incumbent sit in separate ads. Otherwise AppsFlyer can't separate them. Add this to the test Setup section (see [[naming-taxonomy]]).
- **Data Locker to BigQuery is how AppsFlyer attribution reaches the warehouse,** where it joins internal FTDs for true CPFTD. Hex reads from there.
- **For "pull the data on test X":** the AppsFlyer MCP connector's `fetch_aggregated_data` covers campaign, ad set, and ad breakdowns. Hex covers anything that needs warehouse FTDs.
