# CLAUDE.md: UA Second Brain

This is a markdown notes vault, opened in Obsidian by a human and used by Claude as a knowledge base. Evan leads user acquisition at Underdog Sports, owning paid spend across TikTok, Meta, Snapchat, Google, Reddit, Apple Search Ads, Liftoff, Moloco, and RZR, accountable for cost per first-time deposit (CPFTD) and a fast creative and conversion testing program for prediction markets and fantasy. This is a personal vault.

If you are Claude reading this, these rules govern every action you take in this repo.

## 1. What this place is

- A markdown notes vault. **Code does not live here.**
- Obsidian is the primary reading surface. **Wikilinks** (`[[note-name]]`) are how the graph connects. **Frontmatter** drives the queries.
- Folder lineup:
  - `tests/`: one note per test (creative, offer, landing-page, app-store, experiment). `backlog/` holds briefed tests not yet live; `_archive/` holds archived ones.
  - `docs/`: durable knowledge. `channels/`, `creative/`, `measurement/`, `budget/`, `conversion/`, `market/`, plus `glossary.md` and `routines/`.
  - `meetings/`: prep and notes for the COO 1:1, creative sync, team standup, and channel rep calls.
  - `daily/`: daily rollups written by the daily routine.
  - `weekly/`: the weekly channel review owed to the COO.
  - `templates/`: one template per note type.
  - `raw/`: gitignored staging for exports, screenshots, and scraped platform docs.
  - `personal/`: gitignored private notes.

## 2. Truth model, or how to decide what to trust

Every note has a `status` and either a `last_verified` or a `captured_at` date in frontmatter. Use them.

| Folder | Lifecycle | Rule |
|---|---|---|
| `docs/` | living | Trust if `last_verified` is within 90 days. Older: flag before relying on it and offer to re-verify. Platform playbooks in `docs/channels/` drift fastest; check the platform's current docs before quoting a spec or policy. |
| `tests/` | briefed, live, read-out, scaled, killed, then archived | While not archived, trust if `last_verified` is within 7 days (tests turn over in under a week). Older: re-pull from AppsFlyer or Hex before quoting status or results. |
| `meetings/`, `daily/`, `weekly/` | point-in-time | Never re-verified. True as of `captured_at`, and say that date when citing it. |
| `_archive/` | archived | Historical only. Never cite as current. |

When two sources conflict, say so out loud rather than silently picking one. A conflict usually means something was learned and never written down in the canonical place. For performance, **platform-reported numbers are operating data, not truth**: AppsFlyer and the warehouse outrank platform dashboards, a valid experiment outranks any model, and platform ROAS or CPA is never treated as incremental.

## 2a. Working memory

`MEMORY.md` at the root is working memory. **Read it at the start of every session.** Treat it as authoritative for "what was I working on" and "what have I told you."

Three ways to write to it:

1. **Silent save.** When the request contains "remember this," "park this," "save for later," or "add to memory," just update it.
2. **Offer to save.** When something looks memory-worthy but is not obviously so, propose a pre-drafted one-line entry.
3. **Detect and flag.** Watch for: a fact that contradicts a canonical note, a session ending mid-task, substantive work finishing, or a piece of jargon defined in passing. Offer the appropriate save.

Bias toward asking rather than staying silent. Memory offers come at the **end** of a response, never before the substance of the actual question.

**Promotion.** When a fact in memory clearly maps to a canonical note, offer to write it there in the same turn. If accepted, edit the note and mark the memory entry as promoted.

**What does not go in memory:** shared vocabulary goes to `docs/glossary.md`. Anything personal goes to `personal/`. Content owned by an outside system stays there and gets fetched.

## 3. Writing rules

- Every new note uses a template from `templates/`. No bare files.
- Every note has frontmatter. **If a required field is missing, refuse to save and ask.**
- **Wikilinks** for internal references: `[[some-note]]`. **Markdown links** for external URLs.
- Wikilinks inside frontmatter arrays must be quoted: `related: ["[[some-note]]"]`.
- New tags go in `docs/glossary.md` in the same change that introduces them. Tags are flat, lowercase, hyphenated.
- Filenames are lowercase-hyphenated with no dates, except `meetings/`, `daily/`, and `weekly/` which use `YYYY-MM-DD-slug.md`.
- Test names follow [[naming-taxonomy]].

## 4. The `personal/` rule, which is non-negotiable

- `personal/` is gitignored and reserved for private notes.
- **Never** write to `personal/` unless the request explicitly contains the word "personal" or "private."
- **Never** copy content out of `personal/` to anywhere else without explicit confirmation.
- For ambiguous questions, search outside `personal/` first. Only read it if the answer requires it.

## 5. Ingestion rules, for capturing from outside systems

> **Folders represent purpose, not provenance.** A note's home is decided by what it is *about*, not where it came from. Provenance lives in frontmatter (`source_url`, `references`). There is no parallel snapshot tree.

| Source | Treatment | Destination |
|---|---|---|
| AppsFlyer | Fetch on demand. Never mirror reports; write the verdict and a link. | The relevant `tests/` note, `docs/channels/`, or `docs/measurement/` |
| Hex | Fetch on demand; link the notebook or query in `sources`. | Same as AppsFlyer |
| Sigma | Occasional. Link, do not copy. | Same as AppsFlyer |
| Slack | Summarize decisions, asks, and learnings; link the thread. | The note the thread is about; otherwise `daily/` |
| Gmail | Summarize commitments and partner updates; never paste full threads. | The note it is about; otherwise `daily/` |
| Google Calendar | Read for meeting prep and daily reconstruction. | `meetings/`, `daily/` |
| Google Drive / Sheets | Link briefs and readouts; synthesize, do not copy. | `tests/`, `docs/creative/` |
| Platform docs and rep material | Stage in `raw/`, then compile into the channel playbook. | `docs/channels/<channel>.md` |

After folding something into its destination, propose wikilinks to related notes and **ask before adding them**.

**Do not background-sync.** Every capture is an explicit request. Where an outside system is the source of truth, this vault holds a pointer plus your own synthesis, never a mirrored copy. The source system is always more current than a mirror, and a mirror is a maintenance burden that silently rots.

## 6. Default behaviors

- **"Pull the data on test X" or "what won?":** open the test note, fetch results live from AppsFlyer or Hex, and judge the challenger against the incumbent on CPFTD first, then scale, CPI, IPM, CPM, and CTR. Lead with a one-line verdict (scale, kill, or needs more time) and your confidence. Offer to write the verdict to the test note and a line to [[learnings]].
- **COO update or weekly channel review:** build from `weekly/`, recent `daily/` notes, `tests/`, and [[decision-log]]. Per channel: what is working, what is not, what we are doing about it.
- **Meeting prep:** read the last note for that meeting in `meetings/`, open items, and anything new in `tests/` or [[decision-log]] since.
- **Budget moves:** when a reallocation is discussed or made, offer a [[decision-log]] entry with the evidence behind it.
- **Drafting anything:** search `docs/` first, then `tests/`, then the dated folders. Cite which notes informed the draft.
- **Unknown topic:** propose creating the note from the right template before writing into a folder that does not fit.
- **Stale sources:** if a `docs/` note is past its freshness rule, say so before relying on it and offer to re-verify.

## 7. Forbidden

- No deletes. Archive via `status: archived`, and move to `_archive/` where one exists.
- No edits to existing meeting, daily, or weekly notes. They are an append-only record. Corrections go in a new note that links back. One exception: the daily routine may re-run on the same day and merge into that day's daily note.
- No pushing to GitHub without an explicit request.
- No writing to `personal/` without the words "personal" or "private" in the request.

## 7a. Handling constraints

- **No colleague names.** Refer to people by role only: COO, Manager, Associate, creative team, data team, channel rep.
- **The external job search is separate. Do not include it in this codebase.** Nothing about job searching, interviews, or other companies' hiring goes anywhere in this vault, including `personal/`.
- **Frameworks now, numbers later.** No real spend, CPFTD, CAC or iCAC, targets, or internal table names in any file until this repo moves to the work machine and Evan lifts this rule. Relative results are fine (for example, "challenger CPFTD roughly 15% better than incumbent"). Show live numbers in chat; do not save them.
- **No player-level data.** No PII, account IDs, or individual deposits. Aggregates only; this is regulated real-money gaming.

When in doubt about whether something falls under these constraints, ask before writing it to a file. A question costs a few seconds. A leak into git history is permanent.

## 7b. Active routines

- **Daily report:** see [[ua-daily-report]]. Skill: `.claude/skills/ua-daily-report/`. Activate once connectors are live on the work machine.
- **Weekly channel review:** see [[ua-weekly-review]]. Skill: `.claude/skills/ua-weekly-review/`.

Routines are prompts the human runs, not background daemons. Each one is documented in `docs/routines/`. Never invent a routine or run one unprompted.

## 8. Origin

Scaffolded by the bootstrap-second-brain setup file on 2026-09-26. The `knowledge-base-audit` skill lives at `.claude/skills/knowledge-base-audit/`. Run it once this vault passes roughly 30 notes to find out what is missing.
