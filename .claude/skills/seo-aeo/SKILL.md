---
name: seo-aeo
description: Use for any question about SEO (search engine optimization) or AEO/GEO (answer engine optimization, AI search visibility), and for keeping that knowledge current. Trigger phrasings include "how do we rank for", "how do we show up in ChatGPT / AI Overviews / Perplexity / AI Mode", "AEO", "GEO", "LLM visibility", "AI citations", "E-E-A-T", "YMYL", "should we block GPTBot", "robots.txt for AI", "llms.txt", "schema", "Search Console", "why did organic traffic drop", "core update", "refresh the SEO docs". Answers from docs/seo-aeo first, then the local crawl, then live sources, and files new answers back.
---

# SEO & AEO

Notes live in `docs/seo-aeo/` (start at its README). Raw sources live in `raw/search/`: `google-search` (Search Central docs, updates, blog), `search-console`, `bing`, `moz`, `ahrefs` (studies), `ai-engines` (OpenAI, Perplexity, Anthropic, Apple, Microsoft, llms.txt, IndexNow), and `quality-rater/qrg.txt` (Google's Search Quality Rater Guidelines, full text).

## Answering a question

1. **Notes first.** Read the relevant `docs/seo-aeo/` note. AEO facts go stale fast: **anything citing an AI-search study or AI feature older than 60 days gets re-checked** before you rely on it.
2. **Then the crawl.** `grep -ril "<term>" raw/search/*/pages | head`. For rater-guideline questions (E-E-A-T, YMYL, page quality), search `raw/search/quality-rater/qrg.txt`.
3. **Then live.** Google Search Central (`developers.google.com/search`), the Search Status Dashboard for ranking updates, each AI engine's crawler docs, and Ahrefs' blog for new studies.
4. **Answer with the evidence tier made explicit:**
   - **Official** (Google, Bing, OpenAI, and similar)
   - **Study** (third-party data, usually correlational; name the source and the sample)
   - **Opinion or proposal**

   Then say what it means for Underdog (YMYL, fantasy vs. prediction markets, app attribution), and give the source URLs.
5. **Performance answers** (traffic, rankings, citations) use lever blocks per [[reporting-format]], labeled with the data source.
6. **File it back.** Offer to add new facts to the right note. Ask before editing.

## Refreshing ("refresh the SEO docs")

1. From the vault root: `python3 .claude/skills/channel-docs/crawl.py google-search search-console bing moz ahrefs`. Run it in the background. Bing uses headless Chrome.
2. Re-fetch the AI-engine docs listed in `aeo-answer-engines.md` references with `python3 .claude/skills/channel-docs/fetch_extra.py search/ai-engines <0|1> <urls…>` (use 1 for help.openai.com and support.claude.com).
3. **The rater guidelines PDF:** download it to `raw/search/quality-rater/qrg.pdf`, then extract it with `swift .claude/skills/seo-aeo/pdf2txt.swift raw/search/quality-rater/qrg.pdf raw/search/quality-rater/qrg.txt` (macOS PDFKit; no install needed).
4. **Check first:** new Google ranking updates (the Search Central `updates/ranking` page), changes to the AI features doc, new crawler names or user agents, and new Ahrefs AI-search studies. Update [[aeo-answer-engines]] and [[seo-aeo-fundamentals]] with approval.
5. Report in five lines or fewer: what changed, and anything affecting Underdog's crawl policy or content strategy.

## Rules

- Obey CLAUDE.md 7a: no Underdog figures in files.
- **Never recommend tactics that violate Google's spam policies** (scaled content abuse, site reputation abuse, doorways, link schemes, cloaking). This vertical draws scrutiny.
- Legality, odds, and financial claims in any proposed content need legal and compliance review. Say so.
- Respect robots.txt and sites that block crawlers (Search Engine Land blocks automated access).
