---
title: Weekly Channel Review, Sep 22-28
type: weekly
status: living
created: 2026-09-29
updated: 2026-09-29
owners: [evan]
tags: []
date: 2026-09-28
captured_at: 2026-09-29
sources: ["AppsFlyer MCP, aggregated data and creative performance, pulled 2026-09-29 (Sep 22-28 vs Sep 15-21)"]
related: ["[[reporting-format]]", "[[decision-log]]", "[[creative-testing-method]]", "[[meta]]", "[[moloco]]", "[[naming-taxonomy]]"]
---

## Headline

Paid spend rose sharply week over week and blended CPFTD (AppsFlyer, first_deposit) got materially worse, in part because this week's FTDs have had less time to mature. The clearest deterioration is where spend scaled hardest: X and Reddit went up several-fold at CPFTD far above every other channel. Meta and TikTok held roughly flat on CPFTD. Meta's offer test says Rips is the install engine but no CPFTD win over DM250; the day-parting reads (Meta and Moloco) both favor the control so far.

**Provisional:** all CPFTD figures are AppsFlyer cumulative first_deposit, and the Sep 22-28 cohorts are 0-6 days old against 7-13 days for the prior week. Re-pull around Oct 2 before making irreversible calls. Per [[reporting-format]], this file carries relative figures only.

## 1. Mix, channels

**Scale-ups with weak CPFTD (X, Reddit)**
- **Saw:** X spend up ~280% WoW and Reddit up ~850%, with CPFTD ~230% and ~730% worse than their prior weeks (AppsFlyer, Sep 22-28 vs Sep 15-21). X CPFTD is the worst of any major channel; Reddit's is far worse still.
- **Did:** Spend was raised on both. The reason (planned test vs. drift) is not in the data. **Confirm intent.**
- **Expected:** No expectation set. Set one now: CPFTD back within ~2x of the blended paid median by the Oct 5 read, or cut.
- **Happened:** No, spend scaled and CPFTD did not hold.
- **Call:** CHANGE, cap or pause both until the intent and an expectation are confirmed.

**Efficiency channels (Google, Moloco, Aarki, Liftoff, Snap)**
- **Saw:** Google, Moloco, and Aarki are still the lowest CPFTD lines among scaled channels (ASA next), but each degraded ~120-195% WoW on more spend. Liftoff (~200% worse) and Snap (~145% worse) sit mid-pack. Spend on Google, Moloco, Aarki, Liftoff, and Snap rose roughly 1.7-2.2x (AppsFlyer, provisional).
- **Did:** Spend scaled across all five.
- **Expected:** No expectation set. Marginal CPFTD rises with scale; hold Google and Moloco within ~1.5x of the prior-week level.
- **Happened:** Partial. Part of the gap is cohort maturity, part is diminishing returns; cannot separate them until the re-pull.
- **Call:** MAINTAIN spend, re-pull Oct 2, and CHANGE only if the matured gap stays above ~1.5x.

**Meta, TikTok, ASA (held)**
- **Saw:** Meta CPFTD ~+8% and ASA ~+14% WoW; TikTok ~+22% on spend down ~38%.
- **Did:** Meta spend roughly flat; TikTok pulled back.
- **Happened:** Yes for Meta and ASA (stable). TikTok efficiency did not improve with the cut.
- **Call:** MAINTAIN Meta and ASA; TikTok CHANGE to watch (see Creative).

**Data flag:** DV360 carried a large spend line with almost no attributed installs in both weeks. Treat as awareness/view-through with no read on this dashboard; needs an incrementality answer, not a CPFTD one. Blended paid CPFTD excluding DV360: ~47% worse on ~73% more spend.

## 2. Creative (live and in test)

Read is on CPI, IPM, and CPM within category; creative-level CPFTD is not available in this tool. Category baselines are the rollup of the named creatives above the spend floor, all networks reporting creative. Judge on scale first per [[creative-testing-method]]. **Quality gate on FTD is still owed** for every winner below.

**Graphical (most efficient category, and the one carrying scale)**
- **Saw:** Category CPI is the lowest of the four. Top by CPI: PMGraphicalv4 (DFS) ~37% below category CPI on IPM ~17% above; DFSGraphicalv7 ~34% below on IPM ~54% above. Worst: UDXGraphicalv6 6s at the biggest spend of the category, CPI ~270% above the category and IPM ~80% below.
- **Did:** v6 UDX took the most spend in the category and is the least efficient; v7 and PMGraphicalv4 (DFS) carry the efficient volume.
- **Expected:** No expectation set.
- **Happened:** Partial. The winning versions are small; the spend leader is the loser.
- **Call:** CHANGE, shift spend from UDXGraphicalv6 to the DFS v7 / PMGraphicalv4 versions, then confirm UDX variants of v7 hold at scale.

**Animation**
- **Saw:** Top: DFS PhoneUIv1 ~59% below category CPI, IPM ~56% above, but small spend. Worst: KYM Kickoff CFB 10s (the largest in category), CPI ~108% above, IPM ~47% below.
- **Did:** Spend concentrated on the CFB Kickoff and PMv2 cuts.
- **Happened:** No for scale, the biggest spenders are the weakest.
- **Call:** CHANGE, cut KYM Kickoff CFB and PMv2; scale PhoneUIv1 and the DFSv3 / SFvsLA TeamPicks versions.

**Static**
- **Saw:** Largest category by spend and weakest CPI. UA-Static-Phone-Variationsv1 9x16 absorbed the most spend at roughly category-average CPI with IPM ~26% above. Worst: UDXBoostsB, CFB Static 1x1, WinUpTo10000x: CPI 80-95% above category. Paul v2 (DFS) looks cheapest at ~77% below on CPI, but with CPM 70-140% above and IPM outliers, treat as a placement-mix artifact until confirmed by channel.
- **Did:** Static took the biggest share of creative spend.
- **Happened:** No, the largest bucket is the least efficient one.
- **Call:** CHANGE, cut CFB Static 1x1, WinUpTo10000x, UDXBoostsB; hold UA-Static-Phone-Variationsv1 as the static incumbent; verify Paul v2 by channel.

**UGC**
- **Saw:** Tight spread. DonutGuy3 (UDX) and BilloGirl1 are ~4-6% below category CPI; DonutGuy2 (DFS) ~3-7% above, with the 1x1 showing IPM well above category.
- **Did:** Steady spend across the DonutGuy versions.
- **Happened:** Partial, no clear separation.
- **Call:** MAINTAIN, and use the 9x16 DonutGuy3 as the reference for the next UGC challenger.

**Data caveats:** Several rows show CPM or CTR at values that look like impression under-reporting (for example a 4x5 Graphical row with CPM roughly 5x category); their IPM and CPM are not comparable across networks. Many spend rows have no creative name attached; they are excluded from the category rollups. TheDog long-form videos (15/30/60s) ran well below the efficient categories on CPI and are omitted from the leaders and losers above.

## 3. Day parting

**Meta, game day parting (Sep 22-28, AppsFlyer)**
- **Saw:** The GameDayParting campaign spent only a small fraction of BAU. CPI was lower than the BAU campaign's, but CPFTD rests on a handful of FTDs, too few to call.
- **Did:** Live as a small test beside the BAU campaign.
- **Expected:** No expectation set. Needs enough spend for tens of FTDs before a read.
- **Happened:** Pending: check Oct 6. Directionally CPI is better, CPFTD is unreadable.
- **Call:** MAINTAIN, and ask the rep about widening from a spend curve to full game day once spend is large enough to read.

**Moloco, GDP vs. control (Sep 22-28, AppsFlyer)**
- **Saw:** The control campaign delivered CPFTD ~3% lower than the game-day-pacing (GDP) campaign, on roughly 50% more spend. CPI was ~6% lower for control. Direction matches the Meta result: pacing to game days has not beaten the control.
- **Did:** Both ran in parallel.
- **Expected:** No expectation set.
- **Happened:** Partial. Control leads but the CPFTD gap is small enough to be noise at these FTD counts.
- **Call:** MAINTAIN control; CHANGE the GDP design to full game day rather than a spend curve, pending rep input.

## 4. Pulse

Skipped: no pulse identifiable in this pull.

## 5. State levers

Skipped: no geo cut in this pull. Pull by geo for the Oct 6 review.

## Offer test (Meta, Sep 22-28)

- **Saw:** Rips is the install engine: CPI ~56% below DM250 and 80-94% below DM1000, DM50, and KYM. But install-to-FTD is roughly half of DM250's, so CPFTD is **at parity with DM250** (~1% apart, on ~150 FTDs each). DM1000 CPFTD is ~2.7x DM250's; DM50 and KYM are ~6x on thin FTD counts (~20).
- **Did:** Five offer adsets ran in the same campaign, plus a separate Rips campaign launched Sep 25.
- **Expected:** Rips would win on cost per user, not just cost per install. (Prior expectation not on file.)
- **Happened:** No on CPFTD, yes on CPI/IPM. The separate Rips campaign is too new to read.
- **Call:** CHANGE, stop scaling Rips on CPI alone; keep Rips and DM250 as the two live offers, kill DM50 and KYM, and cut DM1000 unless a cohort-quality read says otherwise. Recheck the Rips-only campaign on Oct 2.

**Source conflict:** an earlier read had Rips at CAC ~59% under DM250. That is not what AppsFlyer first_deposit shows (parity). Likely a different event (ht_first_deposit vs first_deposit), window, or maturity. Reconcile before this goes upward.

## Watch list

- X and Reddit spend intent and CPFTD, owner: channel manager (role), decision Oct 2
- Re-pull matured CPFTD for every channel (cohort maturity), owner: UA lead, Oct 2
- DV360 attribution / incrementality question, owner: UA lead with the data team, Oct 6
- Rips-only campaign FTD read (launched Sep 25), owner: UA lead, Oct 2
- Meta game day parting: spend big enough to read, owner: Meta channel rep, Oct 6
- Moloco GDP redesign to full game day, owner: Moloco channel rep, Oct 6
- Reconcile Rips CAC definition (first_deposit vs ht_first_deposit), owner: data team, Oct 1
- Creative-level FTD quality gate for Graphical v7 and PhoneUIv1 winners, owner: data team, Oct 6
