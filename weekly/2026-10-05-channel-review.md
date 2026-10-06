---
title: Weekly Channel Review, Sep 29-Oct 5
type: weekly
status: living
created: 2026-10-06
updated: 2026-10-06
owners: [evan]
tags: []
date: 2026-10-05
captured_at: 2026-10-06
sources: ["AppsFlyer MCP, aggregated data and creative performance, pulled 2026-10-06 (Sep 29-Oct 5 vs Sep 22-28 re-pulled at 7-13 days of maturity)"]
related: ["[[reporting-format]]", "[[decision-log]]", "[[creative-testing-method]]", "[[meta]]", "[[moloco]]", "[[naming-taxonomy]]"]
---

## Headline

Spend roughly halved week over week and blended paid CPFTD (AppsFlyer, first_deposit) roughly halved with it, landing back near the Sep 15-21 level on about 10% less spend. Every scaled channel improved except Apple Search Ads (flat) and Remerge retargeting (worse). X is still the weakest large channel; Reddit was cut about 90%. Two things drive the improvement and neither is proven incremental: Meta BAU got far cheaper once the CreativeRamp campaigns were shut off, and a Moloco CTV campaign now carries more than half of Moloco's FTDs at a fraction of any other line's CPFTD. Rips has flipped on TikTok and Liftoff (now better than channel norm), stays behind on Meta and RZR.

**Provisional:** this week's cohorts are 0-6 days old. Re-pulling the prior week after another 7 days moved channel CPFTD about 7-10% lower, so expect this week to improve a similar amount. Offer Test 2 and the Oct 2 RZR CTV launch are 0-3 days old. Per [[reporting-format]], this file carries relative figures only.

**Source conflict:** the Sep 22-28 blended CPFTD recomputed from this pull is well above the blended figure in the earlier read, and I cannot reproduce that figure (likely scope or definition). Channel-level CPFTD does reconcile (matured values are 7-10% lower). All week-over-week comparisons here use one pull with the same definition in both weeks.

## 1. Mix, channels

**X and Reddit (last week's scale-ups)**
- **Saw:** X spend down ~52% WoW with CPFTD ~61% better than matured Sep 22-28, but still ~2.5x blended paid and about a fifth of paid spend for under a tenth of FTDs. The new UDX X campaign (launched Sep 30) is ~40% better than the MIX X campaign. Reddit spend down ~90%, CPFTD ~87% better but still ~3.5x blended; the new UDX Reddit campaign (Oct 1) is better than the older one on thin FTDs.
- **Did:** Both cut hard; a new X campaign took over delivery.
- **Expected:** CPFTD within ~2x of blended by the Oct 5 read, or cut.
- **Happened:** No on X (2.5x), no on Reddit (3.5x), though the cut itself was the right move.
- **Call:** CHANGE, shift remaining X spend to the UDX campaign, hold Reddit at current small spend until the UDX campaign has ~50 FTDs, cut if it stays above 2x.

**Efficiency channels (Google, Moloco, Aarki, Liftoff, Snap)**
- **Saw:** All five cut ~43-48% on spend and CPFTD improved 33-61%. Google ~34% better, Aarki ~44%, Snap ~50% (new UDX Snap campaign ~25% better than the MIX one), Liftoff ~33%, Moloco ~61% (driven by CTV, see below). Liftoff is still the weakest of the five.
- **Did:** Spend pulled back to roughly the Sep 15-21 run rate.
- **Expected:** Google and Moloco within ~1.5x of the prior-week level.
- **Happened:** Yes, all within and better.
- **Call:** MAINTAIN spend; CHANGE on Liftoff only if the matured gap stays above ~1.5x of Google.

**Meta, TikTok, ASA**
- **Saw:** Meta spend down ~44% and CPFTD ~72% better. The CreativeRamp campaigns (a fifth of last week's Meta spend and almost no FTDs) are off, and BAU spend fell ~53% while its FTDs roughly tripled. TikTok spend down ~49%, CPFTD ~52% better. ASA spend down ~41%, CPFTD flat (+3%); Brand carries the efficiency, Non-brand and Competitor are 2.5-5x Brand. Awareness reach campaigns on Meta (up ~23%) and TikTok produce almost no FTDs by design.
- **Did:** Cut CreativeRamp, cut BAU, launched UDX and Rips campaigns on Sep 30.
- **Happened:** Yes for Meta and TikTok; ASA unchanged.
- **Call:** MAINTAIN Meta and TikTok. CHANGE ASA: cut Competitor, trim Non-brand. Treat the Meta BAU step-change as unexplained until someone can say what changed (audience, creative, or bid), because an unexplained 4x swing is as likely to revert as to hold.

**Remerge retargeting**
- **Saw:** Spend flat, CPFTD ~40% worse, ~5x blended. The iOS Active segment is the efficient one; the HV and LV Inactive segments and all Android segments are several times worse.
- **Did:** Spend held while inactive segments ran.
- **Call:** CHANGE, cut the inactive and Android segments, keep iOS Active.

**Moloco CTV (new campaign, launched Sep 25)**
- **Saw:** Roughly a fifth of Moloco spend and over half of its FTDs, at CPI ~75% below the Moloco UA campaign and CPFTD ~80% below it. Ex-CTV, Moloco is unchanged WoW. RZR launched two CTV campaigns on Oct 2 and shows the same pattern in their first 3 days. Attribution type is install, not view-through, but CTV installs are device-graph matched and prone to over-credit. Organic installs and invite installs did not move, so there is no visible cannibalization yet.
- **Did:** CTV scaled on Moloco, launched on RZR.
- **Expected:** No expectation set.
- **Happened:** Too good to trust yet. AppsFlyer incrementality for UA is not enabled on this account, so it cannot be checked there.
- **Call:** CHANGE, do not scale CTV on CPFTD alone. Design a holdout (geo or Moloco's own lift test) before adding budget.

**Data flag:** DV360 spent ~62% less than last week and again produced almost no installs and no FTDs. It has now run two weeks at material spend with no attributed return. **Call:** CHANGE, pause until there is a measurement plan.

## 2. Creative (live and in test)

Read is on CPI and IPM, network-mixed; creative-level CPFTD is not available in this tool. Quality gate on FTD is still owed for every winner.

- **Saw:** The Rips and P5G100 statics lead on volume at CPI ~2-4x better than the animated offer creative: RipsYellow static 9x16 was the best at scale. P5G100Yellow animated 6s took the largest spend share and had ~4x the CPI of the Rips static with ~90% lower IPM. DepositMatch animated variants (Yellow, Blue, DarkBlue, 50) are all 2-3x the CPI of the statics. Graphical v7 shifted to UDX at scale (UDX v7 KYM 6s) and v6 UDX dropped by ~70%; DFS v6 and v7 still have the lowest CPI in the Graphical set. A DFS Dirt Keep Your Milly 6s 16x9 shows CPI ~60% below the Rips statics, which matches the Moloco CTV delivery.
- **Did:** Offer statics and Graphical v7 got the spend; UDX v6 was cut. WinUpTo10000x, TheDog 60s, and OfficeHours kept running.
- **Expected:** Last week called for cutting WinUpTo10000x and CFB static, and moving Graphical spend off UDX v6.
- **Happened:** Partial. v6 shift: yes. WinUpTo10000x: no, still live at CPI far above anything else, and TheDog 60s and OfficeHours are also high-CPI spend.
- **Call:** CHANGE, cut WinUpTo10000x, TheDog 60s, OfficeHours and the DepositMatch animated set; move the P5G100Yellow animated budget to the Rips and P5G100 statics. Run the FTD quality gate on the static set before treating CPI as a win (the offer copy may attract low-intent installs).

## 3. Day parting

**Meta game day parting**
- **Saw:** Effectively no spend this week; the GameDayParting campaign is dormant. Last week's CPFTD was unreadable on a handful of FTDs.
- **Call:** CHANGE, close the test as no read (never reached readable spend) and decide whether to relaunch at real budget; ask the Meta rep.

**Moloco GDP vs control**
- **Saw:** CPFTD at parity this week (GDP ~1% better), with matured Sep 22-28 showing control ~6% better. Two-week combined, control is ~3% better. Spend is roughly 40% GDP, 60% control. No evidence of a redesign to full game day since last week.
- **Happened:** No winner; GDP has not beaten control on CPFTD in either week.
- **Call:** MAINTAIN control as default; CHANGE the GDP arm only once the rep confirms the redesign, otherwise fold it back into control.

## 4. Pulse

Skipped: no pulse identifiable in this pull.

## 5. State levers

Skipped: AppsFlyer geo is US-only (plus unattributed awareness spend). A state cut needs the warehouse (Hex).

## Offer test (Meta)

**Test 1 (Sep 17-28), matured read**
- **Saw:** Rips CPFTD is ~5% better than DM250 (parity) at ~55% lower CPI. DM1000 is ~2.5x DM250's CPFTD; DM50 and KYM are ~6-6.5x on small counts. All five adsets are now off.
- **Happened:** Rips is the install engine with no CPFTD win. Source conflict from last week (an earlier read had Rips ~59% under DM250 on CAC) is still unreconciled.
- **Call:** CHANGE (closed). DM50, KYM, and DM1000 are dead; Rips and DM250 survive.

**Test 2 (OfferTest2, launched Oct 2), day 1-3**
- **Saw:** Rips CPFTD ~18% better than P5G100 (the UDX offer adset). DM50 and DM25 are ~10x worse on about 5 FTDs each.
- **Expected:** No expectation set. Set one: 50+ cohort FTDs per adset before judging.
- **Happened:** Pending: check Oct 9. Too early on everything.
- **Call:** MAINTAIN, kill DM50 and DM25 at the Oct 9 check unless they gain scale.

## Rips-specific campaigns (launched Sep 25, relaunched on Meta and TikTok Sep 30)

- **Saw:** **TikTok:** the Sep 30 Rips campaign has ~95 FTDs at CPFTD ~50% better than the other TikTok UA campaigns and CPI ~35% better; the original Sep 25 campaign is dead. **Liftoff:** ~35 FTDs, CPFTD ~45% better than every Liftoff campaign and CPI better, thin. **Meta:** the Sep 30 Rips campaign has ~135 FTDs at CPFTD ~25% worse than Meta BAU and ~20% worse than the UDX campaign launched the same day (the combined Rips total ~40% worse than BAU). **RZR:** ~25 FTDs, CPFTD ~65% worse than RZR norm and CPI ~35% worse.
- **Expected:** Rips reaches BAU-parity CPFTD (within ~1.2x of channel incumbent) on at least 50 cohort FTDs by Oct 5, or no more budget.
- **Happened:** Yes on TikTok (the only channel passing both bars). Liftoff beats incumbent but under 50 FTDs. No on Meta (~1.4x) and RZR (<50 FTDs and ~1.65x).
- **Call:** CHANGE, scale TikTok Rips, hold Liftoff until 50 FTDs, cut Meta Rips to the offer-test adset level (do not scale on CPI), stop RZR Rips. Rips retargeting on Remerge is covered above.

## Watch list

- Moloco and RZR CTV incrementality design, owner: UA lead with the data team, decision Oct 9
- Meta BAU step-change: what changed vs the Sep 22-28 campaigns, owner: Meta channel rep, Oct 8
- Re-pull matured CPFTD for Sep 29-Oct 5 and the TikTok and Liftoff Rips counts, owner: UA lead, Oct 12
- DV360 pause or measurement plan, owner: UA lead with the data team, Oct 8
- X UDX campaign and Reddit UDX campaign vs 2x blended, owner: channel manager (role), Oct 9
- Offer Test 2 read (50+ cohort FTDs per adset), owner: UA lead, Oct 9
- Reconcile Rips CAC definition (first_deposit vs ht_first_deposit) and the earlier blended figure, owner: data team, Oct 8
- Creative FTD quality gate for the Rips and P5G100 statics, owner: data team, Oct 9
- Moloco GDP redesign and Meta game day parting relaunch, owner: channel reps, Oct 9
