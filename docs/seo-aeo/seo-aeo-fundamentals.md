---
title: SEO and AEO Fundamentals
type: doc
status: living
created: 2026-09-26
updated: 2026-09-26
owners: [evan]
tags: []
last_verified: 2026-09-26
verified_by: claude
related: ["[[technical-seo]]", "[[content-and-eeat]]", "[[aeo-answer-engines]]", "[[seo-aeo-measurement]]", "[[seo-aeo-for-underdog]]"]
references:
  - https://developers.google.com/search/docs/fundamentals/how-search-works
  - https://developers.google.com/search/docs/fundamentals/seo-starter-guide
  - https://developers.google.com/search/docs/appearance/ai-features
  - https://developers.google.com/search/docs/fundamentals/creating-helpful-content
  - https://ahrefs.com/blog/llm-search/
  - https://moz.com/beginners-guide-to-seo
---

## Summary

- **SEO** (search engine optimization) earns visibility in classic search results.
- **AEO** (answer engine optimization, also called GEO or LLMO) earns *mentions and citations* inside AI-generated answers: Google AI Overviews and AI Mode, ChatGPT, Perplexity, Copilot, Claude, Gemini, and Siri.

**They're mostly the same discipline.** Google says AI features need no special optimization beyond SEO fundamentals, and AI assistants retrieve from search indexes. **The differences are where the work shifts:** off-site brand mentions matter more, citations churn fast, clicks per answer drop, and measurement is harder.

## How search works (Google)

1. **Crawl.** Googlebot discovers URLs through links and sitemaps and fetches them. robots.txt and CDN or firewall rules can block it.
2. **Index.** Google renders the page (including JavaScript), understands its content, and picks a canonical among duplicates. Not everything crawled gets indexed.
3. **Serve.** For each query, Google ranks indexed pages on relevance, quality, usability, and context (location, language, device).

**Nothing is guaranteed.** Meeting every requirement makes a page *eligible*, not ranked.

## How AI answers work

- **Retrieval-augmented generation.** The model runs searches (often several: Google calls it **"query fan-out"**), reads the results, and writes an answer with links to its sources.
- **So you need to be retrievable** (crawlable by that engine's bot, indexed, and ranking somewhere for the fan-out sub-queries) **and quotable** (clear, specific, trustworthy text).
- **Each engine uses its own index and bots.** See [[aeo-answer-engines]].

## What's the same

Crawlability, indexing, helpful people-first content, E-E-A-T and trust, page experience, internal links, and freshness. Doing SEO well is most of AEO. See [[technical-seo]] and [[content-and-eeat]].

## What's different in AEO (evidence in [[aeo-answer-engines]])

| | Classic SEO | AEO |
|---|---|---|
| **Unit of success** | A ranking position and a click | A mention or citation inside an answer |
| **What predicts it most** | Relevance, links, quality | **Off-site brand mentions** correlate most strongly with AI Overview visibility (more than backlinks, in Ahrefs' 75K-brand study) |
| **Stability** | Rankings move gradually | AI Overview content changes very often, and citations turn over, even when the answer's meaning stays stable |
| **Clicks** | Position-based CTR | AI Overviews correlate with a lower CTR for the top result on informational queries (Ahrefs) |
| **Traffic quality** | Baseline | Early evidence that AI referrals convert at a higher rate (Ahrefs' own site) |
| **Query type** | All intents | AI Overviews appear mostly on **informational, question-style, long-tail, non-branded** queries |
| **Measurement** | Search Console, analytics | Partial: Search Console mixes AI features into Web, plus Bing's AI Performance, `utm_source=chatgpt.com`, and third-party AI visibility tools |

## Myths to avoid

- **"You need an llms.txt file."** No major provider has committed to reading it, and Ahrefs found almost no requests for it. It's harmless, but not a lever. Google says no AI-specific files or markup are needed.
- **"Schema markup gets you cited by AI."** In a controlled Ahrefs test, adding schema barely moved AI citations. Use schema for rich results where it's eligible, not as an AEO lever.
- **"AI answers want long content" (or short content).** Length didn't predict citation in Ahrefs' data. Answer the question well.
- **"Generate lots of AI pages to cover every query."** That's **scaled content abuse** under Google's spam policies (see [[content-and-eeat]]).
