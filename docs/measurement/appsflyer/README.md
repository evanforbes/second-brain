# measurement / appsflyer

Everything about AppsFlyer, compiled from AppsFlyer's official help center and aimed at Underdog's setup. Each note covers how a feature works, the gotchas, what it means for Underdog, and the source URLs to re-check. A full crawl of the help center sits in `raw/appsflyer/` (gitignored, local only) for searching obscure questions. The `appsflyer-docs` skill handles questions, refreshes, and re-checks.

## Start here

- [[appsflyer-underdog-setup-audit]]: the open questions about Underdog's actual configuration, prioritized. **Answer the P1s first.**

## Notes

- [[appsflyer-attribution-model]]: how credit is assigned, windows, SRNs vs. link-based networks, reinstalls, flooding
- [[appsflyer-skan-and-ssot]]: iOS: SKAN 4 windows, the conversion value schema, SSOT dedupe
- [[appsflyer-events-and-s2s]]: FTD and revenue events, the S2S API, partner postbacks
- [[appsflyer-channel-integrations]]: the AppsFlyer side of all nine channels
- [[appsflyer-discrepancies]]: why AppsFlyer, the platforms, and the warehouse disagree, and how to diagnose it
- [[appsflyer-web-to-app]]: Smart Script, OneLink, web measurement
- [[appsflyer-reporting-and-data]]: My Dashboards, Creative Optimization, ROI360 cost, Data Locker, APIs
- [[appsflyer-protect360]]: fraud and stolen credit
- [[appsflyer-incrementality]]: geo experiments, the incrementality factor
- [[appsflyer-mcp]]: the connector that lets Claude query AppsFlyer directly

## Recent changes worth knowing (from the Sep 2026 crawl)

- **Jun 23, 2026:** TikTok iOS now receives all conversion events regardless of IDFA, so expect more TikTok iOS attribution from that date.
- **Jun 30, 2026:** the legacy Overview, Events, and Activity dashboards were retired; use My Dashboards.
- **Sep 1, 2026:** Apple Ads adds exact timestamps to all claims, and **age- or gender-targeted ad groups return no attribution.**
- **Ongoing:** PBA is being replaced by Web Performance Measurement.
- **Ongoing:** the legacy S2S in-app events endpoint is being deprecated.

## Refreshing

Say "refresh the AppsFlyer docs." The `appsflyer-docs` skill re-crawls the help center, lists articles that changed since the last crawl and are cited by these notes, and proposes updates.
