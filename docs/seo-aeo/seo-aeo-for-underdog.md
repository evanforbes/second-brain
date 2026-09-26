---
title: SEO and AEO for Underdog
type: doc
status: living
created: 2026-09-26
updated: 2026-09-26
owners: [evan]
tags: [fantasy, prediction-markets]
last_verified: 2026-09-26
verified_by: claude
related: ["[[seo-aeo-fundamentals]]", "[[content-and-eeat]]", "[[aeo-answer-engines]]", "[[seo-aeo-measurement]]", "[[ad-policy-matrix]]"]
references: []
---

## Summary

Applying SEO and AEO to Underdog's products (fantasy and prediction markets) and competitive set (Kalshi, Polymarket, PrizePicks, FanDuel, DraftKings). **Everything here is a proposal**, derived from the sourced notes in this section. None of it is validated on Underdog data yet. Anything about legality, odds, or financial claims needs legal and compliance review before publishing.

## The opportunity

- **AI answers appear mostly on informational, question-style, long-tail, non-branded queries.** That's exactly how people learn a new category: "how do prediction markets work," "is pick'em legal in [state]," "what's the difference between fantasy and sports betting," "how are event contracts regulated."
- **Prediction markets are new and confusing,** so explanation queries are growing and **whoever is the clearest, most trusted explainer gets cited.** That's a brand-building AEO play, not just traffic.
- **Branded and navigational queries** ("Underdog app," "Underdog promo") are classic SEO and ASO: protect them, don't neglect them.

## The constraint: YMYL and trust

Real-money products are YMYL (see [[content-and-eeat]]). So:
- **Show who stands behind the product:** legal entity, licensing and regulatory status per product, responsible-gaming resources, clear terms, contact.
- **Expert authorship:** named authors with relevant credentials for regulatory, how-it-works, and strategy content.
- **Accuracy and freshness:** state legality changes monthly (see [[ad-policy-matrix]]). Stale legality content is a trust *and* compliance risk. Add "last updated" dates and a review owner.
- **Language:** use trading and event-contract terminology for prediction markets, consistent with how Google and TikTok ad policies and the regulatory posture frame them. Confirm with legal.

## Content pillars *(proposed)*

1. **Explainers:** how prediction markets and event contracts work, how pick'em works, fantasy vs. prediction markets vs. sports betting, how payouts work. These are the main AEO targets.
2. **Legality and availability hub:** one maintained page per product, plus state pages **only if each has unique, accurate, maintained content.** Near-identical state pages risk doorway and scaled-content abuse.
3. **Timely event content:** NFL slates, island games (TNF, MNF), and other tentpoles, with real analysis, published early and updated. Use IndexNow for fast Bing pickup.
4. **Original data** (aggregate, non-PII trends, for example what users predict most): the kind of thing press and communities cite. That builds the off-site mentions AEO rewards.
5. **Help and FAQ content** answering real user questions directly. It's quotable by assistants.

## Off-site mentions: the biggest AEO lever

- **PR and expert commentary** on prediction-market regulation and trends.
- **Community presence** where people ask questions (Reddit, sports communities), following each community's rules.
- **Consistent entity data:** app-store listings, company profiles, knowledge panels.
- **Affiliates:** require added-value content. Thin affiliate and site-reputation-abuse placements risk penalties for the host, and brand risk for Underdog (see [[content-and-eeat]]).

## Technical must-dos

- Allow all AI **search** bots, including through the CDN and WAF, and decide on training bots separately (see [[aeo-answer-engines]]).
- Server-render key content. Sitemaps plus IndexNow.
- **App Links / Universal Links** so search opens the app for existing users, plus **Smart Script** on landing pages for new users. Then AppsFlyer can attribute SEO and AEO re-engagements and web-to-app installs (see [[seo-aeo-measurement]]).

## Competitive monitoring *(proposed)*

Run the AEO prompt panel ([[seo-aeo-measurement]]) with Underdog vs. Kalshi, Polymarket, PrizePicks, FanDuel, and DraftKings. Track share of mentions, citations, and how each brand is described. **Sensor Tower** covers the app-store side on the work machine.

## Open questions for Evan

- [ ] Who owns SEO and web content at Underdog today (a team, an agency, nobody)? Which domains and subdomains matter?
- [ ] Current robots.txt and CDN bot policy: are AI search bots allowed?
- [ ] Are App Links / Universal Links and AppsFlyer SEO/AEO attribution set up?
- [ ] Legal's position on publishing state-legality and prediction-market explainer content.
