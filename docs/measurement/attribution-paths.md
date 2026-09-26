---
title: Attribution Paths — App, Web, Web-to-App
type: doc
status: living
created: 2026-09-26
updated: 2026-09-26
owners: [evan]
tags: []
last_verified: 2026-09-26
verified_by: evan
related: ["[[measurement-principles]]", "[[appsflyer-web-to-app]]", "[[appsflyer-events-and-s2s]]", "[[appsflyer-attribution-model]]"]
references: []
---

## Summary

Three acquisition paths, one framework: **media → credit → signals → truth.** Ad exposure happens; AppsFlyer or the platform decides which touch gets credit; Pixel, SDK, CAPI, S2S, and Hightouch carry the events; the warehouse calculates actual CAC and ROAS.

## Path 1: App (ad → store → install → in-app events)

- The install is the attribution boundary. Downstream events inherit the install's source.
- **Client side:** the AppsFlyer SDK (registration, login, first entry). **Server side:** S2S and Hightouch send backend-confirmed events.
- **Setup:**
  1. Partner integrations and windows
  2. The SDK
  3. Map AppsFlyer ID to user ID
  4. Backend events via S2S or Hightouch
  5. Exclude secondary re-engagement copies
  6. Warehouse for GGR, NGR, and ROAS
- **Avoid:** adding SDK, S2S, and Hightouch equivalents together.
- **Main risk:** event mapping and duplication.

## Path 2: Web (ad → site → Pixel/CAPI → platform)

- No install. The platform matches Pixel and CAPI events to clicks and impressions.
- **Setup:**
  1. Pixel on key pages
  2. Standard and custom events
  3. URL parameters on every ad
  4. CAPI from the backend or Hightouch
  5. **Deduplicate with shared event IDs**
  6. Check event match quality
- **Avoid:** treating Pixel or CAPI conversions as final revenue. Validate deposits and NGR in the warehouse.
- **Main risk:** Pixel loss and identity matching.

## Path 3: Web-to-app (where attribution breaks)

- The user starts on the web and converts after the store and install. Without a bridge, the install looks organic or gets credited to the wrong source.
- **The bridge:**
  1. Capture campaign, ad set, ad, placement, and click IDs on the web session.
  2. **Smart Script / OneLink** carries them into the store link.
  3. AppsFlyer attributes the install, and SDK, S2S, or Hightouch attaches registration, KYC, FTD, and entry.
- The platform still reports its web-side conversions via Pixel and CAPI. AppsFlyer owns app install attribution. The warehouse joins it all to FTD and NGR.
- See [[appsflyer-web-to-app]].

## Comparison

| | App | Web | Web → App |
|---|---|---|---|
| Primary attribution | AppsFlyer install | Platform web attribution | AppsFlyer install + preserved web context |
| Client signal | AppsFlyer SDK | Pixel | Pixel + AppsFlyer SDK |
| Server signal | S2S / Hightouch | CAPI / Hightouch | CAPI + S2S / Hightouch |
| Main handoff risk | Event mapping / duplication | Pixel loss / identity match | Site → store attribution break |
| Financial truth | Warehouse + P&L | Warehouse + P&L | Warehouse + P&L |

## Click-through vs. view-through

- **Click-through:** they clicked before converting, within the click window.
- **View-through (VTA):** they saw it before converting, within the view window. Lower confidence.
- **Governance:** windows, last-touch and priority rules (click beats view), Pixel and CAPI dedupe, primary vs. secondary attribution, and SKAN modeled vs. observed.
- **Only incrementality testing tells you VTA's true lift.**

## Setup checklist

1. **Event taxonomy:** one canonical event per stage (install, signup, KYC, FTD, first entry, repeat deposit, handle).
2. **Attribution settings:** aligned windows, partner rules, re-engagement logic, primary-attribution filters.
3. **Web tags:** Pixel, plus CAPI or Hightouch.
4. **App tracking:** SDK, OneLink/Smart Script, user-ID mapping, S2S/Hightouch.
5. **Dedupe:** event IDs for Pixel and CAPI; no SDK/S2S/Hightouch equivalents.
6. **ROAS source of truth:** AppsFlyer and platforms assign credit; the warehouse calculates CAC, GGR, NGR, and ROAS.
