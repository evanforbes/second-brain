---
title: AppsFlyer MCP Connector
type: doc
status: living
created: 2026-09-26
updated: 2026-09-26
owners: [evan]
tags: []
last_verified: 2026-09-26
verified_by: claude
related: ["[[appsflyer-reporting-and-data]]", "[[appsflyer-incrementality]]", "[[ua-daily-report]]"]
references:
  - https://support.appsflyer.com/hc/en-us/articles/36349070304785--Beta-AppsFlyer-MCP
  - https://support.appsflyer.com/hc/en-us/articles/40967933109649--Beta-Agent-Hub-overview
  - https://support.appsflyer.com/hc/en-us/articles/38423389662609-AI-Assistant
  - https://github.com/AppsFlyerKnowledge/appsflyer-ai-agents-examples
---

## Summary

AppsFlyer MCP is a beta connector that lets Claude query your AppsFlyer account directly: performance, incrementality experiments, OneLink, audiences, and AppsFlyer's own documentation. **This is the connector that makes "pull the data on test X, what won?" work without exporting anything.** It's on by default, and an admin can disable it.

## How it works

**Endpoint:** `https://mcp.appsflyer.com/auth/mcp`

**Authentication:**
- **Claude Desktop and claude.ai:** browser OAuth. Add it as a custom connector under Settings, then Connectors.
- **Claude Code:** a bearer token. Create an MCP token under Account menu, Security Center, AppsFlyer Tokens, then run:
  `claude mcp add-json appsflyer '{"type":"http","url":"https://mcp.appsflyer.com/auth/mcp","headers":{"Authorization":"Bearer <TOKEN>"}}'`
- **The token is account-level and has the permissions of the admin who created it.** Treat it as a secret.

**Tools:**

| Area | Tools |
|---|---|
| Performance | `fetch_aggregated_data`: dashboard data with custom dates, groupings, metrics, and filters |
| Incrementality | `incrementality_list_experiments`, `incrementality_get_experiment_results` (lift, incremental conversions, incrementality factor, cost per incremental) |
| Apps and settings | `get_apps`, `get_app_settings` |
| Cost and ad revenue | `get_active_cost_integrations`, `list_cost_supported_media_source`, `get_active_adrevenue_integrations`, `list_adrevenue_supported_media_sources` |
| OneLink and banners | `get_onelink_templates`, `get_onelink_template_links`, `get_onelink_details`, `discover_onelink`, `list_banners`, `get_smart_banner_performance` |
| Audiences | `list_active_audiences`, `list_audiences_connections`, `get_audience_connections` |
| Docs | `get_public_knowledge` |
| Users | `get_users` |

**Limits:**
- It uses the default account only. Multiple accounts need separate connections.
- `get_onelink_template_links` only covers links made in the OneLink UI. `discover_onelink` works on any link.

AppsFlyer also publishes a Claude Cowork starter kit for marketers on GitHub (linked in references).

## Gotchas

- **The token must never be committed.** Put it in Claude Code's user-level config on the work machine, never in this repo. The `claude mcp add-json` command above writes to user config by default; don't add `--scope project`.
- It's a beta, so tool names and behavior may change. Re-verify this note when it breaks.

## What it means for Underdog

- **Set this up early on the work machine, right after Slack, Gmail, and Calendar.** Of all the connectors, it saves the most time pulling data.
- **Test readouts:** use `fetch_aggregated_data` grouped by campaign, ad set, and ad, filtered to the test's date range and the FTD event. The warehouse still decides true CPFTD through Hex.
- **Fits the vault's rules:** numbers from the MCP connector go into chat, never into files (CLAUDE.md 7a). Only direction and relative results get written to `tests/` notes.
- **Use `get_app_settings` to answer most of [[appsflyer-underdog-setup-audit]]** in one pass once it's connected.
