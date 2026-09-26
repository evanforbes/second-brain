---
title: AppsFlyer Incrementality for UA
type: doc
status: living
created: 2026-09-26
updated: 2026-09-26
owners: [evan]
tags: [experiment]
last_verified: 2026-09-26
verified_by: claude
related: ["[[appsflyer-attribution-model]]", "[[appsflyer-mcp]]", "[[decision-log]]"]
references:
  - https://support.appsflyer.com/hc/en-us/articles/41021758795025-Incrementality-for-UA-Guide
  - https://support.appsflyer.com/hc/en-us/articles/360009360978-Incrementality-for-remarketing-overview
  - https://support.appsflyer.com/hc/en-us/articles/36349070304785--Beta-AppsFlyer-MCP
---

## Summary

AppsFlyer's Incrementality for UA runs **geo experiments**: exposed regions against holdout regions, analyzed with time-based regression (TBR). The result is causal lift, not credit. It's one of the independent reads the vault's measurement hierarchy puts above attribution: "dashboards operate campaigns; experiments move money."

## How it works

- **Design.** Historical install or event data is used to pick statistically similar sets of exposed and holdout regions, tested across thousands of random candidate splits.
- **Pretest.** Both groups see ads, and a regression model learns how the two regions relate.
- **Test.** The measured campaigns stop serving in the holdout regions. For Meta, Google Ads, and TikTok, the platforms support this natively.
- **Result.** The model predicts what the exposed region would have done without the campaign (the "counterfactual"). Lift is the cumulative difference between that prediction and what actually happened.
- **Volume guideline:** at least **5,000 monthly installs or events per measured campaign**, counted on the main KPI.
- **Multi-cell tests** compare channels, creative strategies, or bidding types head to head.
- **Outputs:**
  - lift
  - incremental conversions
  - cost per incremental conversion
  - the **incrementality factor**: incremental conversions divided by classic attributed conversions. Above 100% means attribution *under*-credits the campaign; below 100% means it over-credits.
- **MCP tools:** the MCP connector can list experiments and pull their results (see [[appsflyer-mcp]]).
- **Remarketing** has its own incrementality product, and its S2S events need advertising IDs.

## Gotchas

- Comparing lift across campaigns with very different reach or spend is misleading. Compare like with like.
- Holdouts cost volume. Run them when the decision is big enough to justify it.

## What it means for Underdog

- **Calibrated CPFTD.** A channel's incrementality factor turns attributed CPFTD into an incremental read. Divide attributed CPFTD by the factor, measured on the FTD event. Keep factors per channel, refresh them periodically, and log the budget moves they justify in [[decision-log]].
- **Geo design must respect the legal footprint.** Prediction markets and fantasy aren't live in every state, and availability differs by product. The experiment's region pool should only include states where the product being measured is live, or the holdout is contaminated.
- **Use the FTD event as the KPI,** not installs. Check that each tested campaign clears the volume guideline on FTDs. If not, test at channel level or run longer.
- **Treat this as one independent read among several.** Where Measured, the in-house MMM, or INCRMNTAL disagree with it, the disagreement tells you where to test next. It is not a tiebreak by vendor.
