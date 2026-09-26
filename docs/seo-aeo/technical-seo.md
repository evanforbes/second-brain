---
title: Technical SEO
type: doc
status: living
created: 2026-09-26
updated: 2026-09-26
owners: [evan]
tags: []
last_verified: 2026-09-26
verified_by: claude
related: ["[[seo-aeo-fundamentals]]", "[[aeo-answer-engines]]", "[[seo-aeo-measurement]]", "[[appsflyer-web-to-app]]"]
references:
  - https://developers.google.com/search/docs/essentials
  - https://developers.google.com/search/docs/crawling-indexing
  - https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag
  - https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls
  - https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics
  - https://developers.google.com/search/docs/appearance/page-experience
  - https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
  - https://www.indexnow.org/documentation
  - https://www.bing.com/webmasters/help/webmasters-guidelines-30fba23a
---

## Summary

Make pages **crawlable, indexable, fast, and unambiguous** to Google, Bing, and AI crawlers. Technical SEO is the eligibility layer. It doesn't make content rank, but failures here block everything else, AI answers included.

## Google's technical requirements

A page must:
- not block Googlebot,
- return HTTP 200, and
- have indexable content.

Beyond that come the Search Essentials (technical requirements, spam policies, key best practices). Check everything with Search Console's URL Inspection.

## Checklist

**Crawling**
- `robots.txt` allows the search crawlers you want: Googlebot, Bingbot, and AI search bots such as OAI-SearchBot and PerplexityBot (see [[aeo-answer-engines]]). **Also check CDN and bot-protection rules:** a WAF that blocks AI bots' published IP ranges silently removes you from their answers.
- **XML sitemaps** list canonical, indexable URLs, with accurate `lastmod`. Submit them in Search Console and Bing Webmaster Tools.
- **Internal links** use crawlable `<a href>` anchors with descriptive text. Important pages stay a few clicks from the homepage.
- **IndexNow** pings Bing and other participating engines immediately when URLs change. That helps time-sensitive pages (slates, events, odds-style content).

**Indexing and controls**
- **`noindex`** keeps a page out of search. robots.txt only blocks crawling; a blocked URL can still be indexed without its content.
- **Preview controls:** `nosnippet`, `data-nosnippet`, and `max-snippet` limit what Google shows, **including in AI Overviews and AI Mode.** Googlebot's robots.txt rules are the *only* control over crawling for Search's AI features. **`Google-Extended` does not affect Search.** It governs other Google AI uses such as Gemini training and grounding.
- **Canonicals:** consolidate duplicates (parameters, tracking URLs, state variants that repeat content) with `rel=canonical`, redirects, and consistent internal links.

**Rendering**
- JavaScript is rendered, but it's slower and riskier. **Put critical content and links in the initial HTML** (server-side rendering or prerendering). Many AI crawlers don't execute JavaScript well, so client-only content may be invisible to them.

**Page experience**
- Core Web Vitals (loading, interactivity, visual stability), HTTPS, mobile-friendliness, and no intrusive interstitials. These are tie-breakers, not trump cards.

**Structured data**
- Use it for **eligible rich results** (Organization, Article, FAQ where eligible, Breadcrumb, SoftwareApplication, Event, and so on). **It must match the visible content.**
- It isn't a proven AEO lever (see [[seo-aeo-fundamentals]]).

**Bing**
- Bing's index feeds Copilot and partner experiences, and **Bing Webmaster Tools now reports AI Performance** (citations in Copilot and Bing AI answers). Treat Bing as a first-class engine for AEO.

## App-specific: search to app

- **Android App Links and iOS Universal Links** let a search result open the app directly for users who have it installed. AppsFlyer can attribute those opens to the search or answer engine (see [[seo-aeo-measurement]]).
- **Users without the app** land on the web page. **Smart Script and Smart Banners** carry the attribution into the store (see [[appsflyer-web-to-app]]).
