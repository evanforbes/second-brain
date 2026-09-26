---
name: appsflyer-docs
description: Use for any AppsFlyer question and for keeping the AppsFlyer knowledge base current. Trigger phrasings include "how does AppsFlyer ...", "why doesn't AppsFlyer match Meta/TikTok/...", "what's our AppsFlyer setup", "SKAN", "SSOT", "conversion value", "lookback window", "S2S", "OneLink", "Smart Script", "Protect360", "Data Locker", "refresh the AppsFlyer docs", "recheck AppsFlyer", "what changed in AppsFlyer". Answers from the compiled notes first, then the local help-center crawl, then the live docs, and files new answers back into the vault.
---

# AppsFlyer Docs

The vault's AppsFlyer knowledge lives in `docs/measurement/appsflyer/`, which holds compiled notes with source URLs. A full local crawl of the help center lives in `raw/appsflyer/`, which is gitignored and may be missing on a new machine.

## Answering a question

1. **Compiled notes first.** Read `docs/measurement/appsflyer/README.md` and the relevant note. Check `last_verified`, and flag the note if it's more than 90 days old.
2. **Then the local crawl.** Grep `raw/appsflyer/help-center/` for the term, for example `grep -ril "lookback" raw/appsflyer/help-center | head`. `raw/appsflyer/INDEX.md` maps titles to files and URLs. If `raw/appsflyer/` is missing, run the refresh first or fetch live.
3. **Then live.** Fetch the article's `source_url`, or the AppsFlyer MCP `get_public_knowledge` tool if it's connected (see [[appsflyer-mcp]]).
4. **Answer with Underdog framing:**
   - What AppsFlyer does
   - What it means for CPFTD, FTD signal, or budget decisions
   - The source URL
5. **File it back.** If the answer isn't in a compiled note, offer to add it to the right note, and to add any question about Underdog's own setup to [[appsflyer-underdog-setup-audit]]. Ask before editing.

## Refreshing ("refresh the AppsFlyer docs")

1. From the vault root, run `python3 .claude/skills/appsflyer-docs/crawl.py`. It crawls the public help-center API at about one request per second, rewrites `raw/appsflyer/`, and writes `raw/appsflyer/CHANGES.md` listing articles whose content changed since the last crawl.
2. Cross-reference `CHANGES.md` against the `references:` URLs in `docs/measurement/appsflyer/*.md`. Also scan any new or changed "Bulletin:" articles for dates in the last 90 days.
3. For each changed article that a note cites, read the new version and propose a specific edit to the note. Apply edits only after approval, then bump `updated` and `last_verified`.
4. Report in five lines or fewer: how many articles changed, which notes are affected, and any bulletin that could bias CPFTD.

## Rules

- Obey CLAUDE.md 7a. Record settings and decisions, never Underdog figures. Live numbers from the MCP connector stay in chat.
- Summarize AppsFlyer content in your own words, and keep quotes short. The crawl stays in `raw/` and is never committed.
- Don't invent AppsFlyer behavior. If the docs don't say, say so and add the question to the setup audit.
