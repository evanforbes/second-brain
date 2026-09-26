---
title: Creative Testing Method
type: doc
status: living
created: 2026-09-26
updated: 2026-09-26
owners: [evan]
tags: [creative]
last_verified: 2026-09-26
verified_by: evan
related: ["[[naming-taxonomy]]", "[[learnings]]", "[[reporting-format]]", "[[measurement-principles]]", "[[ad-policy-matrix]]", "[[appsflyer-reporting-and-data]]"]
references: []
---

## Summary

**Challenger vs. incumbent.** New, untested creative ideas (challengers) run in dedicated **test ramp campaigns** against what's currently scaled and winning in **BAU campaigns** (the incumbent). **Scale is the biggest factor**: a creative that can take spend while holding efficiency. **CPI, IPM, CPM, and CTR** are read alongside it, always within a channel, using each channel's own testing mechanics (see Per-channel test mechanics below).

Sections marked *(proposed)* are additions beyond Evan's core method, for him to keep, change, or cut.

## The flow

```
Brief (creative team) → Test ramp campaign (challenger vs. incumbent)
   → read on scale + CPI / IPM / CPM / CTR
   → [proposed] quality gate on FTD
   → Graduate to BAU  or  Kill  or  Iterate
   → Confirm it scales in BAU → becomes the new incumbent
   → Log the verdict in tests/ and a line in [[learnings]]
```

- **Test ramp campaigns** are dedicated campaigns where challengers get controlled exposure without disrupting BAU delivery.
- **BAU campaigns** are the scaled, always-on campaigns where the incumbent lives.
- Every test note records its `incumbent` and the ramp and BAU campaigns involved (see `templates/test.md`).

## What decides a winner

**1. Scale, the lead metric.** Can the challenger absorb meaningful spend at or better than the incumbent's efficiency? A creative that wins on cost at tiny spend hasn't won yet.

**2. The diagnostic metrics** explain *why* scale did or didn't happen:

| Metric | What it tells you | Weak here usually means |
|---|---|---|
| **CPM** | What the auction charges to reach this audience with this creative | Low platform quality or relevance score, or an expensive audience |
| **CTR** | Whether the hook stops the scroll and earns the click | Weak opening seconds or offer, or a mismatch with the audience |
| **IPM** (installs per 1,000 impressions) | Overall install efficiency: CTR × click-to-install | Good CTR with low IPM points to a store-page or promise mismatch |
| **CPI** | The combined outcome | — |

**How they connect:** **CPI = CPM ÷ IPM** (with IPM per 1,000 impressions), and **IPM = CTR × click-to-install rate × 1,000.** So a CPI change always traces back to the auction (CPM), the hook (CTR), or the post-click promise (click-to-install). The readout should say which one moved.

## *(Proposed)* Quality gate before graduation

**Top-funnel winners can be quality losers.** The vault's first principle is optimizing to the customer, not the install ([[measurement-principles]]). Before a challenger graduates:

- Check the **install → FTD rate and CPFTD** for its cohort against the incumbent, once enough FTDs have matured to read it.
- A challenger that wins on CPI and IPM but loses on FTD rate is usually an offer or promise that attracts the wrong users. Iterate it; don't scale it.
- Scale and CPI decide *whether it can grow.* FTD quality decides *whether growth is worth it.*

## *(Proposed)* Read rules

The thresholds below are Evan's to set per channel. Record them here once agreed; until then, readouts state what was used.

- **Minimum exposure before any call:** spend, impressions, and installs per challenger, and FTDs for the quality gate.
- **Maximum test budget per challenger** before an automatic kill if it isn't trending.
- **Win margin:** how much better than the incumbent (on the lead metric) counts as a win versus noise.
- **Read window:** respect each platform's learning phase before reading (Meta, TikTok Smart+ about 7 days, Snap 1–7 days, X 3–5 days). Tests usually conclude in under a week.

## *(Proposed)* Test hygiene

- **One variable per test.** Label it either a **new concept** (a new angle or idea) or an **iteration** (same concept, a new hook, format, or offer). Concept wins and iteration wins teach different things.
- **Same audience, placements, window, and optimization event** for the challenger and incumbent. Otherwise you're comparing setups, not creative.
- **Name it per [[naming-taxonomy]]:** concept_format_hook_offer_channel_date. That's how the readout finds it in AppsFlyer, Hex, and the platform.
- **Separate ads, not blended assets.** AppsFlyer can't split Meta Advantage+ dynamic assets or Google UAC assets individually ([[appsflyer-reporting-and-data]]).
- **Policy check before launch.** Is it a fantasy or prediction-markets creative? Prediction-markets creative must use trading and event-contract language on TikTok and Google ([[ad-policy-matrix]]).

## *(Proposed)* Graduation to BAU

- **A ramp win isn't a BAU win.** BAU auctions, audiences, and budgets differ. Move the challenger into BAU *alongside* the incumbent.
- **It becomes the incumbent** when it takes meaningful spend share in BAU at equal or better efficiency. Update the channel playbook's "Current incumbent" section and the test note.
- **Keep the old incumbent running** until the new one proves itself in BAU. Don't hard-swap.

## *(Proposed)* When to test: fatigue triggers

Incumbents decay. Start a new challenger cycle when fatigue shows. For example, TikTok's own signals are about 2× CPA versus normal, or CTR or CVR falling for 2 straight days ([[tiktok]]). Test continuously, so a challenger is ready *before* the incumbent fatigues.

## Per-channel test mechanics

From the channel playbooks. Always compare challenger vs. incumbent **within** a channel, because CPM and CTR differ structurally across channels.

| Channel | Test harness | Watch-outs |
|---|---|---|
| [[meta]] | Challenger as a separate ad (not a dynamic asset) inside the campaign; up to 50 assets per upload | Flexible and Advantage+ assets report only the best asset in AppsFlyer; Meta rotates delivery toward predicted winners fast |
| [[tiktok]] | Smart+ with 4–6+ creatives, adding challengers in batches of 2–5; formal Split Test (90% confidence) for concept reads | Hook in the first 6 seconds; SKAN iOS campaigns need about 90 installs a day for clean reads |
| [[google]] | New asset groups or campaigns per concept; the asset report rates assets Low/Good/Best | Ratings are relative within the campaign; add assets rather than removing them; conversion delay |
| [[snapchat]] | One format per ad set | 3–5 second ads and an early offer (seconds 2–3) often win; engaged views count as clicks |
| [[reddit]] | Headline variants (keep at least 1/3 unique); Max campaigns rank asset combinations | Refresh headlines every 3–4 weeks; community tone matters |
| [[apple-search-ads]] | Custom product pages as ad variations per keyword theme | Also counts as an app-store test; the CPP is the landing page |
| [[moloco]] | Built-in A/B tests on creative groups | Same-format comparisons only; iOS needs probabilistic attribution enabled |
| [[liftoff]] | Multi-creative optimization, up to 6 at once | The vendor's pick isn't the verdict; read CPFTD yourself |
| [[rzr]], [[x]] | Standard ad-level rotation | Low volume, so read over longer windows |

## Reporting

A creative readout is a **Creative lever block** per [[reporting-format]]:

- **Saw:** the winner, fatigue signal, or test result
- **Did:** scaled, killed, or launched
- **Expected:** lift and where
- **Happened:** the actual result
- **Call:** MAINTAIN or CHANGE

Every concluded test adds one line to [[learnings]], so patterns (hooks, formats, and offers that win by channel) build up over time.

## Open questions for Evan

- [ ] Read thresholds per channel: minimum spend and installs, maximum test budget, win margin.
- [ ] Is the FTD quality gate part of graduation today, or should it be?
- [ ] How are test ramp campaigns structured per channel (budget share, audiences)? Record this in each playbook.
