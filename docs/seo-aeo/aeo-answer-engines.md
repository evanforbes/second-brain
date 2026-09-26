---
title: AEO — AI Answer Engines
type: doc
status: living
created: 2026-09-26
updated: 2026-09-26
owners: [evan]
tags: []
last_verified: 2026-09-26
verified_by: claude
related: ["[[seo-aeo-fundamentals]]", "[[technical-seo]]", "[[seo-aeo-measurement]]", "[[seo-aeo-for-underdog]]"]
references:
  - https://developers.google.com/search/docs/appearance/ai-features
  - https://developers.openai.com/api/docs/bots
  - https://help.openai.com/en/articles/12627856-publishers-and-developers-faq
  - https://help.openai.com/en/articles/9237897-chatgpt-search
  - https://docs.perplexity.ai/guides/bots
  - https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler
  - https://support.apple.com/en-us/119829
  - https://blogs.bing.com/search/April-2025/Introducing-Copilot-Search-in-Bing
  - https://about.ads.microsoft.com/en/blog/post/october-2025/optimizing-your-content-for-inclusion-in-ai-search-answers
  - https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview
  - https://llmstxt.org/
  - https://ahrefs.com/blog/ai-overview-citations-top-10/
  - https://ahrefs.com/blog/ai-search-overlap/
  - https://ahrefs.com/blog/ai-overview-brand-correlation/
  - https://ahrefs.com/blog/schema-ai-citations/
  - https://ahrefs.com/blog/what-is-llms-txt/
  - https://ahrefs.com/blog/ai-overviews-reduce-clicks/
  - https://ahrefs.com/blog/ai-overview-triggers/
  - https://ahrefs.com/blog/ai-overviews-vs-ai-mode/
  - https://ahrefs.com/blog/ai-overview-change/
  - https://ahrefs.com/blog/ai-citations-vs-impressions-study/
  - https://ahrefs.com/blog/is-chatgpt-really-powered-by-google/
  - https://ahrefs.com/blog/ai-search-traffic-conversions-ahrefs/
---

## Summary

Each AI answer engine retrieves from its own index with its own crawler, then cites sources. **To show up you must be crawlable by that engine, indexed, and worth citing.** Evidence (mostly Ahrefs' large-sample studies, which are third-party and correlational) says **off-site brand mentions and existing search visibility matter most.** Special files and markup matter little.

## Engine by engine

| Engine | How it sources | Crawler(s) to allow | Controls and notes |
|---|---|---|---|
| **Google AI Overviews / AI Mode** | Google's index, with **query fan-out** across subtopics | **Googlebot** (no separate bot) | No special requirements. The page must be indexed and snippet-eligible. `nosnippet`, `max-snippet`, and `noindex` limit it. **`Google-Extended` doesn't affect Search.** AI Overviews and AI Mode cite largely *different* URLs (about 14% overlap in Ahrefs' 730K-pair study) while giving similar answers |
| **ChatGPT search** | Its own search, sometimes drawing on third-party providers | **OAI-SearchBot** (search inclusion). **GPTBot** is training-only, and each is set independently. **ChatGPT-User** is for user-initiated visits | Allow OAI-SearchBot, **and let OpenAI's published IP ranges through your CDN.** Referrals carry **`utm_source=chatgpt.com`**. Disallowed pages may still show as a bare link unless they're `noindex` |
| **Perplexity** | Its own index | **PerplexityBot** (search, not model training); **Perplexity-User** for user actions | The highest overlap with Google's top 10 among assistants (Ahrefs) |
| **Claude** | Web search | **Claude-SearchBot** (search quality); **Claude-User** (user requests); **ClaudeBot** (training) | Each is controlled separately in robots.txt, and `Crawl-delay` is supported |
| **Microsoft Copilot / Bing AI** | Bing's index | **Bingbot** | **Bing Webmaster Tools' AI Performance** (preview since Feb 2026) shows citations in Copilot and Bing AI answers. Microsoft's guidance: fresh, authoritative, structured, semantically clear content |
| **Apple (Siri, Apple Intelligence)** | Applebot | **Applebot** (search); **Applebot-Extended** controls use in AI model training | — |

**Recommended robots.txt policy:** allow every *search* bot (Googlebot, Bingbot, OAI-SearchBot, PerplexityBot, Claude-SearchBot, Applebot) and the *user* agents. Decide on *training* bots (GPTBot, ClaudeBot, Google-Extended, Applebot-Extended) as a separate business and legal call. **Blocking training bots doesn't remove you from AI search answers.**

## What the evidence says (Ahrefs studies, 2025–26)

- **Rankings help but don't guarantee.** In the latest update, about 38% of AI Overview citations also rank in the top 10, and the rest are spread across positions 11–100 and beyond. An earlier Ahrefs study found about 76%; the update used a larger sample and improved parsing, and AI Overviews moved to Gemini 3 in January 2026. Treat the share as unstable. For ChatGPT, Gemini, and Copilot, only about 12% of cited URLs rank in Google's top 10 for the same prompt. Perplexity overlaps most.
- **Brand web mentions are the strongest correlate** of brand visibility in AI Overviews. They correlate far more strongly than backlinks, and brands with the most mentions got far more AI mentions. Branded search volume helps moderately, and **ads don't buy AI visibility.**
- **What triggers AI Overviews:** mostly **informational** queries, question-style queries, long queries (7+ words), and non-branded queries. They rarely appear on navigational or local queries.
- **Clicks:** AI Overviews correlated with a notably lower CTR for the #1 result on informational queries. But on Ahrefs' own site, AI-referred visitors converted at a much higher rate.
- **Assistants mention brands far more often than they link to them.** Track mentions, not just links.
- **Volatility:** AI Overview content changes very often, and many citations rotate, while the answer's meaning stays stable. Visibility has to be maintained, not won once.
- **Doesn't move the needle:** adding schema (a controlled test showed no citation lift), llms.txt (97% of sites with one got zero requests for it), and content length.
- **What ChatGPT cites most:** Wikipedia leads by a wide margin, and many top-cited pages aren't something marketers can influence. Freshness is prominent.

## Playbook

1. **Be crawlable by every AI search bot**, including at the CDN and WAF level (see [[technical-seo]]).
2. **Win the underlying searches.** Rank for the fan-out sub-questions your topic spawns, not just the head term.
3. **Earn off-site mentions:** PR, data others cite, expert quotes, community presence (Reddit, forums), app-store listings, Wikipedia accuracy (only where notability exists, never promotional edits).
4. **Write quotable answers:** a direct answer first, then depth, clear headings, specific facts, dates, and sources.
5. **Keep it fresh** and consistent across your own and third-party profiles (entity clarity).
6. **Measure mentions and citations, not just clicks** (see [[seo-aeo-measurement]]).
