---
title:
type: test
status: briefed        # briefed | live | read-out | scaled | killed | archived
created:               # YYYY-MM-DD
updated:               # YYYY-MM-DD
owners: []
tags: []
test_name:             # per [[naming-taxonomy]]
test_type:             # creative | offer | landing-page | app-store | experiment
channel:               # tiktok | meta | snapchat | google | reddit | x | apple-search-ads | liftoff | moloco | rzr
product:               # prediction-markets | fantasy
incumbent: ""          # "[[incumbent-note-or-channel-playbook]]" for what the challenger must beat
variable:              # concept | iteration (one variable per test)
hypothesis:
launch_date:           # YYYY-MM-DD
target_date:           # YYYY-MM-DD, readout / kill date
last_verified:         # YYYY-MM-DD, last time results were re-pulled
verdict:               # pending | scale | kill | inconclusive
sources: []            # AppsFlyer report and Hex notebook URLs, creative brief link
related: []
---

## Hypothesis

What we believe, and why the challenger should beat the incumbent.

## Setup

Test ramp campaign and BAU campaign (for creative tests, per [[creative-testing-method]]), challenger vs. incumbent, audience, geo, placements, optimization event, dates, budget split (relative until numbers are allowed). Policy check: fantasy or prediction-markets creative ([[ad-policy-matrix]]).

## Results

Read from AppsFlyer / Hex at `last_verified`, relative to the incumbent. Scale leads; the diagnostics explain it (CPI = CPM ÷ IPM).

| Metric | Challenger vs incumbent |
|---|---|
| Scale (spend absorbed at efficiency) | |
| CPI | |
| IPM | |
| CPM | |
| CTR | |
| Install → FTD / CPFTD (quality gate) | |

## Verdict

A Creative lever block per [[reporting-format]]: Saw / Did / Expected / Happened / Call (graduate to BAU, kill, or iterate).

## Learning

One line for [[learnings]].
