---
title: AppsFlyer In-App Events and S2S
type: doc
status: living
created: 2026-09-26
updated: 2026-09-26
owners: [evan]
tags: []
last_verified: 2026-09-26
verified_by: claude
related: ["[[appsflyer-skan-and-ssot]]", "[[appsflyer-channel-integrations]]", "[[appsflyer-discrepancies]]"]
references:
  - https://support.appsflyer.com/hc/en-us/articles/115005544169-In-app-events-Overview
  - https://support.appsflyer.com/hc/en-us/articles/4410481112081-In-app-events-Event-structure
  - https://support.appsflyer.com/hc/en-us/articles/4410672219025-Recommended-sports-betting-events
  - https://support.appsflyer.com/hc/en-us/articles/207034486-Server-to-server-events-API-for-mobile-S2S-mobile
  - https://support.appsflyer.com/hc/en-us/articles/207032016-Customer-User-ID-field-CUID
  - https://support.appsflyer.com/hc/en-us/articles/4410480904081-Meta-ads-in-app-event-mapping
---

## Summary

Events are "what happened." AppsFlyer ties every in-app event back to the install's attributed source, whether the event came from the SDK or from the server (S2S). For Underdog, the FTD event is the most important signal AppsFlyer carries. It sets attributed CPFTD, feeds the SKAN CV, and is what the platforms bid on through postbacks. How it's sent matters more than any dashboard setting.

## How it works

**Revenue parameters:**
- **`af_revenue`** feeds every AppsFlyer revenue metric (LTV, ROAS, ARPU, ROI) **and is sent to partners in postbacks.**
  - Negative values are allowed, for refunds.
  - Numbers only: no commas or currency symbols. Up to 5 decimal places.
  - The range is ±1,000,000. Values outside it appear in raw data but not in aggregates.
- **`af_net_revenue`** is optional and sent *in addition to* `af_revenue`. It powers the Net metrics in My Dashboards.
- **`af_price`** is a monetary value that doesn't count as revenue.
- **`af_currency`** defaults to USD. AppsFlyer converts currencies hourly using Open Exchange Rates.

**AppsFlyer's recommended sports-betting events:** `af_login`, `af_complete_registration`, `first_time_deposit` (with `af_revenue` set to the deposit amount), `deposit`, `placed_bet`, and withdrawals. Note that **AppsFlyer's own template treats the deposit as revenue.**

**S2S API (mobile):**
- **`appsflyer_id` is mandatory.** Set the CUID (customer user ID) in the app so backend user IDs map to AppsFlyer IDs. On iOS, the `os` parameter is required.
- **Timestamping:** an event keeps its `eventTime` only if it arrives by **02:00 UTC the next day**. Later arrivals are stamped with their arrival time.
- **One event per request.** Revenue values must be stringified correctly.
- **Racing the install:** an S2S event that arrives before AppsFlyer finishes processing the install (about 20–30 seconds or more) can be recorded as unattributed or organic. AppsFlyer recommends a short delay for events fired right after install.
- **Meta CAPI:** S2S events forwarded to Meta must include the user agent (`ua`) and IP address (`ip`), which the SDK adds automatically but S2S does not.
- **Incrementality measurement** (remarketing) needs the advertising ID in the S2S payload.
- **Endpoint upgrade:** AppsFlyer upgraded the S2S in-app events API in December 2023 and plans to deprecate the old endpoint. Only an admin can make the switch, and AppsFlyer is working on a separate path for third-party senders like Hightouch.

**Partner postbacks:**
- Each partner has an in-app event mapping, where you choose which events are sent and whether revenue goes with them.
- SRNs need the device ID in a postback, so iOS users who haven't consented produce fewer postbacks to SRNs.
- Click-based networks use their own transaction IDs, so this limitation doesn't affect them.

**Double counting:** if the Meta SDK and AppsFlyer both send the same event, Meta does not dedupe it.

## Gotchas

- Dashboards count events against the **install date** (LTV view), not the event date, unless you're in an activity view. See [[appsflyer-discrepancies]].
- Sending the same funnel step through the SDK and through S2S/Hightouch double counts it. Keep **one canonical event per funnel stage.**

## What it means for Underdog

- **A deposit is not revenue.** If `first_time_deposit` carries the deposit amount in `af_revenue`, three things follow:
  - AppsFlyer's revenue, ROAS, and ARPU are deposit-based.
  - Partner value bidding optimizes toward deposit size.
  - SKAN revenue buckets encode deposit size.

  That can be a sensible early value signal, but it must be labeled "deposit value" everywhere. NGR truth lives in the warehouse. This is a decision to make on purpose (see [[appsflyer-underdog-setup-audit]]).
- **CPFTD in AppsFlyer and in the warehouse will never match exactly.** The internal FTD model is the financial truth. AppsFlyer's FTD is a marketing signal. Late Hightouch batches that miss the 02:00 UTC cutoff shift FTDs to the day they arrived.
- **Watch the organic share of S2S events.** Registration and KYC events that fire within seconds of install are the ones most likely to be marked organic by mistake.
- **Confirm Hightouch uses the upgraded S2S endpoint** and the current API V2 bearer token. When the old endpoint is retired, events sent to it will stop arriving and the FTD signal will go dark.
- **Meta optimization depends on S2S carrying `ua` and `ip`** whenever events reach Meta through AppsFlyer rather than CAPI directly.
- **Event mapping per partner is the lever that actually trains each algorithm.** Confirm that every channel receives the same canonical FTD event, and check whether revenue goes with it.

## Open questions

Tracked in [[appsflyer-underdog-setup-audit]].
