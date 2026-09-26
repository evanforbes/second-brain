---
title: Underdog AppsFlyer Setup Audit
type: doc
status: living
created: 2026-09-26
updated: 2026-09-26
owners: [evan]
tags: []
last_verified: 2026-09-26
verified_by: evan
related: ["[[appsflyer-attribution-model]]", "[[appsflyer-skan-and-ssot]]", "[[appsflyer-events-and-s2s]]", "[[appsflyer-channel-integrations]]", "[[appsflyer-web-to-app]]", "[[appsflyer-reporting-and-data]]", "[[appsflyer-protect360]]", "[[appsflyer-incrementality]]", "[[appsflyer-mcp]]"]
references: []
---

## Summary

The questions that turn general AppsFlyer knowledge into knowledge of Underdog's own setup. Record **settings and decisions only, never figures or internal table names** (CLAUDE.md 7a).

Answers come from **Evan's measurement document**, filed as [[measurement-principles]], [[user-value-architecture]], [[attribution-paths]], and [[incrementality-and-mmm]]. Some are marked *approach*: the document describes how the setup is designed or how Evan would configure it, not a setting read from the account. Confirm those once in the AppsFlyer UI or through the MCP connector's `get_app_settings`.

Priorities: **P1** can bias CPFTD or budget decisions right now. **P2** affects accuracy or speed. **P3** is housekeeping.

## Answered

### Measurement architecture
- **Source of truth.** AppsFlyer assigns credit only. The warehouse and P&L measure the outcome. Actual CAC is spend divided by attributed FTDs, calculated in the warehouse at cohort grain. AppsFlyer deposit events are marketing signals; the internal payment and FTD model is the financial truth. → [[appsflyer-discrepancies]]
- **Identity.** A bridge table maps AppsFlyer installs to Underdog user IDs. It's incomplete by design (ATT opt-outs, multi-device use, reinstalls), and ambiguous mappings are nulled, never guessed. Use the user ID for value and AppsFlyer for acquisition evidence. → [[appsflyer-events-and-s2s]]
- **FTD attribution in the warehouse** follows a waterfall: partner or RAF first, then AppsFlyer paid, then organic. The warehouse FTD source can therefore differ from AppsFlyer's attribution. → [[appsflyer-discrepancies]]
- **Data flow.** AppsFlyer is a raw source into BigQuery (staging, then marts, then reporting), and Hex reads the finished tables. Numbers restate when AppsFlyer or SKAN data arrives late, attributions are restated, or refunds land. → [[appsflyer-reporting-and-data]]

### Events and S2S
- **Channels.** AppsFlyer SDK events run client-side. Backend-confirmed events go through S2S, and newer events go through Hightouch (`ht_*`). → [[appsflyer-events-and-s2s]]
- **One canonical event per funnel stage:** install, signup, KYC, FTD, first entry, repeat deposit, handle. SDK, S2S, and Hightouch equivalents are never summed; legacy variants are for QA only. → [[appsflyer-events-and-s2s]]
- **Revenue.** NGR is calculated in BigQuery from transactions and is *not* imported as an AppsFlyer revenue value. → [[appsflyer-events-and-s2s]]
- **Re-engagement.** Secondary re-engagement copies are excluded from the canonical events. → [[appsflyer-attribution-model]]

### SKAN and SSOT (*approach*)
- **Conversion Studio** on, in SKAN 4.0 mode, with a schema built from events plus revenue. Partner postback copies are enabled where relevant. → [[appsflyer-skan-and-ssot]]
- **Schema priority** follows the value ladder: revenue and retention, then FTD and first entry, then KYC, then registration, then install or open. Window 1 covers early quality (registration, KYC, FTD, first entry, early revenue); windows 2–3 cover continued value. → [[appsflyer-skan-and-ssot]]
- **SSOT** is used to reduce double counting. iOS is read directionally, alongside incrementality and MMM, never from SKAN alone. → [[appsflyer-skan-and-ssot]]

### Web-to-app
- **Web.** Pixel runs on key pages, with backend-confirmed events sent through CAPI or Hightouch and deduped by event ID.
- **Bridge.** Smart Script and OneLink carry campaign, ad set, ad, placement, and click IDs from the web session into the store journey. AppsFlyer attributes the install, and SDK, S2S, and Hightouch events attach downstream. → [[appsflyer-web-to-app]]

### Channels
- **Apple Search Ads.** Apple proposed view-through attribution and it was rejected as over-crediting. A measured ASA cell drifted brand-heavy and was paused. → [[appsflyer-channel-integrations]]
- **TikTok.** A value-optimization beta mapped TikTok's purchase event to FTD. → [[appsflyer-channel-integrations]]
- **Meta.** One broad campaign, with CAPI sending real funded-account values from day one. → [[appsflyer-channel-integrations]]

### Incrementality
- **Truth layers.** Incrementality runs through geo holdouts and lift tests (including Measured), an experiment-calibrated in-house Bayesian MMM, and INCRMNTAL as the always-on model. When they conflict, the experiment wins. The document doesn't mention AppsFlyer's own Incrementality for UA. → [[appsflyer-incrementality]]

## Partly answered

- [ ] **P1** *Deposit value in `af_revenue`.* NGR isn't sent to AppsFlyer, but the document doesn't say whether the FTD event carries the deposit amount as `af_revenue`, or which value Meta CAPI's "real funded-account values" uses. That decides what AppsFlyer revenue, ROAS, and the SKAN revenue buckets actually represent.
- [ ] **P1** *Current CV schema.* The document gives the design principle but not the live mapping table. Download it from Conversion Studio to confirm it matches.
- [ ] **P2** *Partner postback mapping.* The document confirms one canonical FTD. It doesn't confirm that all nine partners receive that same event, with or without revenue.
- [ ] **P2** *SSOT reading.* SSOT is used, but where is it read now that the Overview dashboard is retired: a My Dashboards view or the SSOT Data Locker report into BigQuery?

## Open (not covered by the document; these are account settings)

### Attribution settings ([[appsflyer-attribution-model]])
- [ ] **P1** What are the click and view-through lookback windows for each of the nine partners, and are they aligned with each platform on purpose?
- [ ] **P1** Which DSPs and link-based partners (Reddit, Liftoff, Moloco, RZR) have view-through on? What's their share of `view` and `engaged_view` in `engagement_type`?
- [ ] **P2** What's the re-attribution window, and is the app on first-install mode for post-reinstall events?
- [ ] **P2** Is retargeting enabled on any SRN that also runs UA?
- [ ] **P3** What's the AppsFlyer app timezone, and which platform timezone do daily reads get compared against?

### Recent platform changes ([[appsflyer-channel-integrations]])
- [ ] **P1** Do any ASA ad groups use age or gender targeting? Since Sep 1, 2026 those return no attribution.
- [ ] **P2** Is the June 23, 2026 TikTok iOS data-sharing change treated as a trend break?

### Events and S2S ([[appsflyer-events-and-s2s]])
- [ ] **P2** Does Hightouch use the upgraded S2S endpoint and a V2 token? When do its batches land relative to the 02:00 UTC cutoff?
- [ ] **P2** What share of registration and KYC S2S events land as organic because they raced the install?

### Web-to-app ([[appsflyer-web-to-app]])
- [ ] **P2** Is every landing-page test variant running the same Smart Script configuration? Is PBA still in use?

### Reporting and data ([[appsflyer-reporting-and-data]])
- [ ] **P2** Is Creative Optimization licensed, and which channels are connected? Does FTD show as an event metric in it?
- [ ] **P2** What's the ROI360 tier, and which partners have working cost APIs?

### Fraud ([[appsflyer-protect360]])
- [ ] **P2** Is Protect360 on, and which validation rules exist? (The document mentions Protect360-class screening only in general terms.)

### Incrementality ([[appsflyer-incrementality]])
- [ ] **P3** Is AppsFlyer Incrementality for UA licensed? Is it worth adding as another independent read?

### MCP ([[appsflyer-mcp]])
- [ ] **P2** On the work machine: is MCP enabled, and who can create the token?
