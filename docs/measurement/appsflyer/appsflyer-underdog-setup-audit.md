---
title: Underdog AppsFlyer Setup Audit
type: doc
status: living
created: 2026-09-26
updated: 2026-09-26
owners: [evan]
tags: []
last_verified: 2026-09-26
verified_by: claude
related: ["[[appsflyer-attribution-model]]", "[[appsflyer-skan-and-ssot]]", "[[appsflyer-events-and-s2s]]", "[[appsflyer-channel-integrations]]", "[[appsflyer-web-to-app]]", "[[appsflyer-reporting-and-data]]", "[[appsflyer-protect360]]", "[[appsflyer-incrementality]]", "[[appsflyer-mcp]]"]
references: []
---

## Summary

The questions that turn general AppsFlyer knowledge into knowledge of Underdog's own setup. Answer them in chat, from the AppsFlyer UI, from the CSM, or through the MCP connector's `get_app_settings` once it's connected. Record **settings and decisions only, never figures** (CLAUDE.md 7a). When an answer is in, move it to "Answered," link the note it affects, and bump `last_verified`.

Priorities: **P1** can bias CPFTD or budget decisions right now. **P2** affects accuracy or speed. **P3** is housekeeping.

## Open

### Attribution settings ([[appsflyer-attribution-model]])
- [ ] **P1** What are the click and view-through lookback windows for each of the nine partners, and do they deliberately match each platform or not?
- [ ] **P1** Which link-based partners (Reddit, Liftoff, Moloco, RZR) have view-through on, with what windows? What share of each DSP's installs are `view` or `engaged_view`?
- [ ] **P2** What's the re-attribution window? Is the app on first-install mode for post-reinstall events? (It was added before or after July 31, 2024?)
- [ ] **P2** Is retargeting enabled on any SRN that also runs UA, which creates a mistargeting risk?
- [ ] **P3** What's the AppsFlyer app timezone and currency, and which platform timezone do daily reads get compared against?

### Apple Search Ads ([[appsflyer-channel-integrations]])
- [ ] **P1** Do any ASA ad groups use age or gender targeting? Since Sep 1, 2026 those return no attribution. Compare ASA installs in Apple's console with AppsFlyer before and after that date.

### TikTok ([[appsflyer-channel-integrations]])
- [ ] **P2** Has anyone accounted for the June 23, 2026 change (AppsFlyer now shares all iOS conversions with TikTok) as a trend break in TikTok iOS reads?

### SKAN and SSOT ([[appsflyer-skan-and-ssot]])
- [ ] **P1** Which Conversion Studio mode is active (SKAN 4 or Custom), and what does the current CV schema encode per window? Download the mapping table.
- [ ] **P1** Do server-sent FTD events (Hightouch/S2S) reach the CV inside window 1, meaning within 48 hours?
- [ ] **P2** Is SSOT on? Where does the team read it now that the Overview dashboard is retired: a My Dashboards view or the SSOT Data Locker report?
- [ ] **P2** Is lock window used? Which partners receive SKAN postback copies or transaction IDs?
- [ ] **P3** Is Aggregated Advanced Privacy on, and what does that restrict in raw data?

### Events and S2S ([[appsflyer-events-and-s2s]])
- [ ] **P1** Does `first_time_deposit` (or its equivalent) carry the deposit amount in `af_revenue`? If so, is labeling AppsFlyer revenue and ROAS as "deposit value" everywhere a deliberate choice?
- [ ] **P1** Is there exactly one canonical event per funnel stage? Are any SDK, S2S, and Hightouch equivalents double counting?
- [ ] **P2** Which events does each partner's postback mapping send, with or without revenue? Do all nine partners receive the same FTD event?
- [ ] **P2** Does Hightouch use the upgraded S2S endpoint and a V2 bearer token? What's its batch timing relative to the 02:00 UTC cutoff?
- [ ] **P2** What share of registration and KYC S2S events land as organic because they raced the install?
- [ ] **P3** Do S2S events forwarded to Meta include `ua` and `ip`?

### Web-to-app ([[appsflyer-web-to-app]])
- [ ] **P2** Do all landing pages, and every LP test variant, run the same Smart Script configuration?
- [ ] **P2** Is PBA still in use? If so, what's the Web Performance Measurement migration plan and deadline?

### Reporting and data ([[appsflyer-reporting-and-data]])
- [ ] **P2** Is Creative Optimization licensed, and which of the nine channels are connected (and by which user)? Does the FTD event show in it?
- [ ] **P2** Is ROI360 on, and at which tier? Which partners have working cost APIs?
- [ ] **P2** Which Data Locker reports land in BigQuery, and how often? Does the SSOT report land too?

### Fraud ([[appsflyer-protect360]])
- [ ] **P2** Is Protect360 on? Which validation rules exist? Is anyone reviewing blocked and post-attribution rates per DSP monthly?

### Incrementality ([[appsflyer-incrementality]])
- [ ] **P2** Is Incrementality for UA licensed? Have any experiments run? Which channels clear the volume guideline on FTDs?

### MCP ([[appsflyer-mcp]])
- [ ] **P2** On the work machine: is MCP enabled at the account level, and who can create the MCP token?

## Answered

(None yet.)
