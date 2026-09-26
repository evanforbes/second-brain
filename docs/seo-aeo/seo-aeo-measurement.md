---
title: Measuring SEO and AEO
type: doc
status: living
created: 2026-09-26
updated: 2026-09-26
owners: [evan]
tags: []
last_verified: 2026-09-26
verified_by: claude
related: ["[[aeo-answer-engines]]", "[[technical-seo]]", "[[appsflyer-web-to-app]]", "[[measurement-principles]]"]
references:
  - https://developers.google.com/search/docs/appearance/ai-features
  - https://support.google.com/webmasters/answer/10268906?hl=en
  - https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview
  - https://help.openai.com/en/articles/12627856-publishers-and-developers-faq
  - https://support.appsflyer.com/hc/en-us/articles/15123194526353-Set-up-organic-search-SEO-and-organic-AI-answers-AEO-re-engagement-attribution
  - https://ahrefs.com/blog/ai-visibility-audit/
---

## Summary

SEO has mature measurement. AEO doesn't yet. Combine **search console data, analytics referrals, AI-visibility tracking, and AppsFlyer app attribution,** and judge business impact on **warehouse FTDs by landing-page and referral cohort,** in line with [[measurement-principles]].

## The toolkit

| Question | Tool | Notes |
|---|---|---|
| Google impressions, clicks, queries, pages | **Google Search Console** Performance report | **AI Overviews and AI Mode are counted inside the "Web" search type.** They can't be cleanly separated |
| Indexing and crawl health | Search Console (Pages, URL Inspection, sitemaps, Crawl stats) | Check before blaming content |
| Bing, plus **Copilot and Bing AI citations** | **Bing Webmaster Tools**, including **AI Performance** (preview since Feb 2026) | The first first-party report of AI citations by URL |
| ChatGPT referrals | Analytics (GA4 or similar) | ChatGPT adds **`utm_source=chatgpt.com`** to referral links |
| Other AI referrals | Analytics referrers (perplexity.ai, copilot, gemini, claude.ai…) | Some AI traffic arrives with no referrer, and assistants link far less often than they mention |
| Brand **mentions and citations** in AI answers | Third-party AI-visibility tools (for example Ahrefs Brand Radar), or a fixed prompt set checked on a schedule | Track share of voice against competitors on a fixed prompt list |
| Search → **app** opens (existing users) | **AppsFlyer organic search (SEO) and AI answers (AEO) re-engagement attribution** | Requires App Links / Universal Links and SDK 6.12.1+. It attributes app opens to the search or answer engine |
| Search → **new user** installs | AppsFlyer web-to-app (Smart Script, Smart Banners) on landing pages | iOS attribution is probabilistic, so treat it as directional (see [[appsflyer-web-to-app]]) |
| Business outcome | Warehouse FTDs by landing page, referrer, and cohort (Hex) | The truth layer |

## Build an AEO prompt panel *(proposed)*

- **A fixed list of 50–100 prompts** real users would ask. Mix informational, comparison, "is it legal in <state>", and brand vs. competitor.
- **Run it monthly** across ChatGPT, Perplexity, Google AI Mode and AI Overviews, Copilot, and Claude. Record whether Underdog is **mentioned**, **cited (linked)**, and **how it's described,** next to competitors.
- **Keep the prompts stable** so trends mean something. Answers are volatile, so look at multi-week trends, not single runs.

## Reporting

Report SEO and AEO movements as lever blocks per [[reporting-format]]:
- **Saw:** ranking, citation, or referral change
- **Did:** content, technical, or PR action
- **Expected:** a number and a date
- **Happened / Call**

Label every number with its source (Search Console, Bing, analytics, visibility tool, AppsFlyer, warehouse).
