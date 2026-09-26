---
title: Test and Creative Naming Taxonomy
type: doc
status: living
created: 2026-09-26
updated: 2026-09-26
owners: [evan]
tags: []
last_verified: 2026-09-26
verified_by: evan
related: ["[[learnings]]"]
references: []
---

## Summary

Every test and every creative gets a name built from the same fields, in the same order, so a test can be found in AppsFlyer, Hex, and the ad platforms by name alone. A consistent name is what makes "pull the data on test X" work.

## Detail

Pattern: `concept_format_hook_offer_channel_date`

| Field | What it holds | Example values |
|---|---|---|
| concept | The creative idea or angle | lowercase, hyphenated, short |
| format | Asset type | ugc, static, motion, native, carousel |
| hook | The opening line or visual | short slug |
| offer | The promo or value prop shown | slug, or `none` |
| channel | Where it runs | tiktok, meta, snapchat, google, reddit, asa, liftoff, moloco, rzr |
| date | Launch date | YYYYMMDD |

Rules still to confirm with the team: the allowed values for each field, and whether product (prediction markets or fantasy) belongs in the name or only in the campaign. Update this note and set `last_verified` when confirmed.
