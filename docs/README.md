# docs

Durable knowledge: the things that outlive any single test. This is the master index. **When answering a question, route through here first**, then open the section index.

## Where to look for what

| Question is about… | Go to |
|---|---|
| What to trust, how CAC/CPFTD is built, holdouts, MMM | [measurement](measurement/README.md) → [[measurement-principles]], [[user-value-architecture]], [[incrementality-and-mmm]] |
| Why AppsFlyer ≠ the platform ≠ the warehouse | [[appsflyer-discrepancies]] |
| Anything AppsFlyer (SKAN, S2S, OneLink, windows) | [measurement/appsflyer](measurement/appsflyer/README.md) |
| How a platform works, or how to optimize it | [channels](channels/README.md) → the channel's playbook |
| Can we advertise fantasy or prediction markets on X? | [[ad-policy-matrix]] |
| What worked before, and why | [[measurement-case-studies]], [[learnings]], [[decision-log]] |
| Creative testing: how a winner is called | [[creative-testing-method]], [[naming-taxonomy]] |
| Budget moves and the evidence behind them | [budget](budget/README.md) → [[decision-log]] |
| App store, landing pages, offers | [conversion](conversion/README.md) |
| Competitors and regulation | [market](market/README.md) |
| How to present data and answers | [[reporting-format]] |
| Jargon | [[glossary]] |
| A specific test | `tests/` |
| What happened on a day or week, or in a meeting | `daily/`, `weekly/`, `meetings/` |

## Sections

- [channels](channels/README.md): 10 playbooks plus the ad policy matrix
- [measurement](measurement/README.md): 5 core notes plus the AppsFlyer knowledge base
- [creative](creative/README.md): testing method, naming, learnings
- [budget](budget/README.md): allocation, pacing, decision log
- [conversion](conversion/README.md): app store, landing pages, offers
- [market](market/README.md): competitors and regulation
- [routines](routines/): daily report and weekly review
- [[glossary]]

## Deep sources (local only, gitignored)

`raw/appsflyer/` and `raw/channels/<platform>/` hold the full crawled help centers. The `appsflyer-docs` and `channel-docs` skills search them when a playbook doesn't cover a question. On a new machine, re-crawl with those skills.
