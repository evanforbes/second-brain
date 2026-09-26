---
title: AppsFlyer Protect360 and Fraud
type: doc
status: living
created: 2026-09-26
updated: 2026-09-26
owners: [evan]
tags: []
last_verified: 2026-09-26
verified_by: claude
related: ["[[appsflyer-attribution-model]]", "[[appsflyer-channel-integrations]]", "[[appsflyer-discrepancies]]"]
references:
  - https://support.appsflyer.com/hc/en-us/articles/218254203-Protect360-anti-fraud-guide
  - https://support.appsflyer.com/hc/en-us/articles/360011793077-Protect360-dashboard
  - https://support.appsflyer.com/hc/en-us/articles/360015179337-Protect360-raw-data-reports
  - https://support.appsflyer.com/hc/en-us/articles/115004703926-Implement-validation-rules-to-prevent-fraud
  - https://support.appsflyer.com/hc/en-us/articles/115004745523-Protect360-for-integrated-partners
  - https://support.appsflyer.com/hc/en-us/articles/41442782045073-About-the-Enhanced-attribution-model
---

## Summary

Protect360 stops fraudsters from *stealing attribution credit*. It works in two layers: real-time blocking before attribution, and detection after attribution. It does not stop the install itself. Bonus abuse, multi-accounting, and KYC fraud in real-money gaming are a separate problem owned by internal risk teams.

## How it works

- **Real-time blocking.** A fraudulent source is blocked before attribution, and that user's later events are blocked too. Blocked installs are reported separately.
- **Post-attribution detection.** Fraud can be identified from the day of install through 7 days after. The install stays attributed but is labeled, future clicks from the source are blocked, and AppsFlyer credits the attribution fees.
- **What it catches:** bots and behavioral anomalies, click flooding, install hijacking (very short click-to-install times, or CTIT, checked against Google Play server data), and low-conversion sources with long CTITs.
- **Validation rules:** advertiser-defined rules, for example on geo, CTIT, or site ID. These now support bulk uploads and can apply to future apps.
- **Partner postbacks:** partners can receive rejected-install postbacks.
- **Also in the dashboards:** fraud from organic sources and AI-generated sub-reasons.
- **The Enhanced attribution model** (see [[appsflyer-attribution-model]]) adds flooding-aware attribution. Protect360 dashboards split compromised and non-compromised installs.

## Gotchas

- Platforms keep counting installs that Protect360 blocked or rejected, which creates a discrepancy.
- Post-attribution fraud stays in the numbers, labeled. Leaving the label out of a CPFTD read makes a fraudulent source look cheap.

## What it means for Underdog

- **The risk for Underdog is stolen credit, not fake users.** Warehouse FTDs are real deposits, so fake installs don't inflate CPFTD much. Click injection and flooding, though, let a DSP or affiliate claim organic FTDs, making a partner look cheap while buying nothing.
- **For each DSP and link-based partner, check monthly:**
  - the blocked and post-attribution rates
  - the ratio of total candidates to contributors
  - the share of very short CTITs
- **When a partner's attributed CPFTD looks too good,** check it against Protect360 and the `engagement_type` mix before scaling. Then prove it with a holdout (see [[appsflyer-incrementality]]).
