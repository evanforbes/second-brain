---
name: channel-docs
description: Use for any question about how an ad platform works or what its policies allow, and for keeping the channel playbooks current. Covers Google App campaigns (UAC), Meta, TikTok, Snapchat, Reddit, X, Apple Search Ads, Liftoff, Moloco, RZR (Aarki). Trigger phrasings include "how does <channel> bidding work", "best practices for <channel>", "can we advertise prediction markets on <channel>", "what's <channel>'s gambling policy", "why won't this ad get approved", "Smart+", "Advantage+", "tCPA", "learning phase", "refresh the channel docs", "recheck <channel> policy". Answers from the playbooks first, then the local crawl, then live docs, and files new answers back.
---

# Channel Docs

Channel playbooks live in `docs/channels/<channel>.md`, plus `docs/channels/ad-policy-matrix.md` for fantasy and prediction-market policy. Crawled help-center pages live in `raw/channels/<name>/` (gitignored; may be missing on a new machine).

Crawl source names: `google`, `meta`, `meta-dev`, `tiktok`, `snap`, `reddit`, `x`, `apple-ads`, `liftoff`, `rzr`. Moloco uses the Zendesk crawler.

## Answering a question

1. **Playbook first.** Read the channel's note, and [[ad-policy-matrix]] for anything about policy or approvals. Check `last_verified`. **Policy content older than 30 days gets re-checked live before you rely on it,** because state lists and prediction-market rules change monthly.
2. **Then the local crawl.** Grep `raw/channels/<name>/pages/` (for example, `grep -ril "learning phase" raw/channels/tiktok/pages | head`). Each crawl's `INDEX.md` maps titles to URLs.
3. **Then live.** Fetch the `source_url`, or search the platform's help center.
4. **Answer with Underdog framing:**
   - What the platform does
   - What it means for FTD optimization, CPFTD reads, or policy for fantasy vs. prediction markets
   - The source URL
5. **File it back.** Offer to add new facts to the playbook, and open questions to its "Rep notes" or the matrix's open questions. Ask before editing.

## Refreshing ("refresh the channel docs")

1. From the vault root:
   - `python3 .claude/skills/channel-docs/crawl.py google meta meta-dev tiktok x apple-ads liftoff rzr`. Run it in the background; it's slow and polite.
   - `python3 .claude/skills/channel-docs/crawl.py snap reddit`. These use headless Chrome at about 45 seconds a page, so they're slower still.
   - `ZD_BASE="https://help.moloco.com/api/v2/help_center/en-us" ZD_OUT="raw/channels/moloco" python3 .claude/skills/appsflyer-docs/crawl.py`
   - Policy pages linked only from search go through `python3 .claude/skills/channel-docs/fetch_extra.py <name> <render 0|1> <urls…>`. The policy URLs in each playbook's `references` are the list to re-fetch.
2. Read each `raw/channels/<name>/CHANGES.md`, and cross-reference it against the playbooks' `references`.
3. **Policies first.** Diff gambling, fantasy, and prediction-market policy pages, and update [[ad-policy-matrix]] with approval.
4. Report in five lines or fewer: what changed, which playbooks are affected, and any policy change that affects where Underdog can advertise.

## Rules

- Obey CLAUDE.md 7a. Settings and decisions only, no Underdog figures. Vendor case-study numbers are the vendor's claims; label them that way.
- Summarize platform content in your own words, and keep quotes short. Crawls stay in `raw/`, never committed.
- Respect sites that block crawlers (for example, redditinc.com). Use the help center or ask Evan instead.
- Policy summaries are not legal advice. Flag launches in new states or products for legal and compliance review.
