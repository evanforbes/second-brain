---
title: Second Brain Bootstrap
type: doc
status: archived
created: 2026-09-26
updated: 2026-09-26
last_verified: 2026-09-26
verified_by: evan
owners: [evan]
tags: []
related: []
---

# Bootstrap Your Second Brain

A setup file for building a personal, Claude-native knowledge base out of an empty GitHub repo.

This file has two audiences. The first section is for you, the human. Everything from "Instructions for Claude" onward is written for Claude and you can skip it.

---

## For you, the human

### What this is

A "second brain" here means one folder on your machine, tracked in GitHub, that Claude works out of every single time you talk to it. Instead of re-explaining your job at the start of every conversation, the folder holds it: what you own, who you work with, what you are in the middle of, what your team's jargon means, and how you like things written.

The payoff compounds. Week one it saves you some retyping. Month three Claude drafts things in your voice, knows which stakeholder cares about which metric, and can answer "what did I commit to last Tuesday" without being told.

### What you will have when this is done

- A `CLAUDE.md` file, which is the operating manual Claude reads on every prompt. Think of it as the standard operating procedures you would hand a new hire.
- An `AGENTS.md` pointer, so non-Claude tools land on the same rules.
- A folder structure shaped around your actual job, not a generic template.
- Frontmatter templates so every note you write is machine-readable.
- A glossary of your team's vocabulary.
- A `MEMORY.md` working-memory file, if you want one.
- A daily routine that keeps Claude's context current without you doing anything.
- A guided path to building your first skill.

### Before you start

Five things, in order. None of them take long.

1. **Create a new, empty GitHub repository.** Private. Name it whatever you like ("second-brain" is fine).
2. **Install GitHub Desktop** and clone that repo to `~/Documents/GitHub/<repo-name>`.
3. **Install Claude Desktop** if you do not have it, and open the cloned folder as a project (Code tab, then open the folder).
4. **Put this file in the root of that folder.** Just drag it in.
5. **Paste the prompt below** into Claude and answer its questions.

That is it. Claude does the rest, but it will ask you a lot of questions first, which is the point.

### The prompt to paste

```
Read BOOTSTRAP-SECOND-BRAIN.md in this folder, top to bottom, before doing
anything else. Then run it on me.

I'm starting from an empty repo and I want you to set up my second brain.
Interview me stage by stage. Don't assume anything about my job, my tools, or
how I work, and don't write a single file until you've shown me the plan and
I've said yes. If an answer of mine is vague, ask a follow-up instead of guessing.
```

### Two tips that matter more than they sound like they do

**Use voice-to-text.** The single biggest speed-up in working this way is rambling context at Claude instead of typing it. Aqua Voice is good and cheap (Wispr Flow is the better-known alternative). The interview below goes much faster spoken, and long rambling answers produce a better vault than short typed ones.

**Always work out of this same folder.** The whole value is accumulation. If you start a Claude conversation somewhere else, it does not know you. Keep coming back here and it gets better on its own.

### After the interview

Claude will hand you a short "first week" list. The two things that actually matter:

1. Set up your data connectors. Claude cannot do this for you, since each one needs you to log in. Claude will tell you which ones are worth it for your role.
2. Build one skill for something you do over and over. Claude will walk you through it.

---

# Instructions for Claude

Everything below this line is addressed to Claude. The human has pasted a prompt asking you to run this file on them.

## How to run this

1. **Read this entire file before you do anything.** Including the literal file blocks near the end. You need the whole shape in mind before the interview, because the interview's answers decide what you write.

2. **Interview first. Do not assume.** The person running this has been told explicitly to tell you not to assume anything. Honor that. You do not know their job. You do not know what their team calls things. You do not know which tools they use. Every one of those is an interview question, not an inference.

3. **Hard gate: write no files until the plan is approved.** Section "The plan gate" below defines the checkpoint. Do not create a directory, do not write `CLAUDE.md`, do not `git init` anything until the human has said yes to an explicit plan.

4. **Stage the interview.** Eight stages, defined below. Ask one stage at a time, and echo back what you heard before moving to the next. Do not dump all forty questions in one message, and do not ask one single question per message either. A stage is the right unit.

5. **Follow up on vagueness.** If someone answers "the usual stuff" or "I dunno, reporting I guess," that is not an answer. Ask again, concretely, with a for-instance.

## First, check the room

Before the interview:

- Confirm the working directory. If it is not where the vault should live, ask.
- If a `CLAUDE.md` already exists here, **stop and ask.** They may want an audit of what exists rather than a fresh bootstrap.
- If the directory has existing markdown files, note the count. Do not touch them. Offer batched triage at the very end, after the scaffold exists.
- If the directory is empty apart from this file, say so and go straight to the interview.

## The pattern this encodes

Two sources, both deliberate, and you do not need to explain either one to the human unless they ask.

**Karpathy's LLM knowledge base pattern.** Raw documents get staged in a `raw/` tier. An LLM compiles them into a wiki of markdown files: summaries, wikilinks, categorized articles, a master index and per-section indexes. Question-answering runs against the wiki, not against embeddings. The LLM also runs lint passes looking for missing data, inconsistencies, and candidate articles, and files its outputs back into the wiki.

**The 7-level knowledge base rubric.** Level 1 is automemory, level 2 is a CLAUDE.md, level 3 is multiple markdown state files, **level 4 is the Obsidian/Karpathy wiki**, levels 5 through 7 are naive RAG, graph RAG, and agentic multimodal RAG. A solo operator or small team should target a polished level 4 and stop. Level 4 scales to thousands of notes.

What you build here is deliberately level 4. If the human asks about RAG, tell them level 4 has to demonstrably fail first, and that the bundled audit skill will tell them when.

## Core principles, which you do not relax without asking

1. **Folders represent purpose, not provenance.** Where a note lives is decided by what it is *about*, never by where it came from. A summary of a Slack thread about a campaign lives with the campaign, not in a `slack/` folder. Provenance goes in frontmatter (`source_url`, `references`).

2. **Frontmatter is non-negotiable.** Every note gets a template, every template has required fields. If a required field is missing, refuse to save and ask.

3. **Wikilinks for internal references, markdown links for external URLs.** `[[some-note]]` is what makes the graph traversable, both for a human in Obsidian and for you via grep.

4. **Less is more in CLAUDE.md.** It loads on every single prompt, so every byte is a recurring cost and a dilution of signal. Bias hard toward pointing at a sub-file instead of inlining reference material. Target under 10KB.

5. **No background sync.** Captures from outside systems are explicit human requests. The one exception is a routine the human opts into, which is a prompt they run, not a daemon.

6. **Truth model on every note.** A `status` plus either `last_verified` or `captured_at`. Staleness warnings happen at retrieval time, when you are about to rely on something old.

7. **Personal stays personal.** A gitignored `personal/` folder is the default. Never write there unless the request contains the word "personal" or "private." Never copy content out of it without explicit confirmation.

8. **No deletes.** Archive by setting `status: archived` and moving to an `_archive/` subfolder.

## The interview

Eight stages. Ask a stage, listen, echo back a one-line summary of what you heard, then move on. If an answer is thin, push once before moving on.

**A rule about your examples.** When you offer a for-instance, span at least three unrelated kinds of work. If every example you give is drawn from the same field, you will steer the answer and end up building a vault shaped like that field instead of like this person's job. Rotate through things like paid media, finance, operations, support, design, recruiting, legal.

### Stage 1: Who you are and what you are accountable for

- What is your role, in your own words? Not your title, what you actually do all day.
- What are you accountable for? What would make a good quarter versus a bad one?
- What do you produce? The concrete artifacts: decks, briefs, reports, models, campaigns, contracts, designs.
- Who do you report to, and who asks you for things? Names and roles.
- Is this vault just for you, or shared with a team?

### Stage 2: The unit of work

This is the most important stage, so do not rush it. Most templates assume the unit of work is a "project." For plenty of roles it is not.

- What are the recurring things you work on, and what do you call them? Campaigns, accounts, close cycles, cases, requisitions, experiments, launches, channels, clients, incidents, matters, releases.
- Roughly how many of those are live at once? Three, thirty, three hundred?
- Do they have a lifecycle with named stages? For instance a campaign might go brief, in flight, wrapped; a hiring req might go open, interviewing, closed; a deal might go a pipeline sequence.
- Do several of them get grouped under something bigger? A quarter, a client, a product line, a region.

The noun they use in answer to the first question becomes a top-level folder, named as a lowercase plural. The lifecycle stages become the values of a status field in that folder's template. Do not translate their noun into "projects" for them. If they say campaigns, the folder is `campaigns/`.

### Stage 3: Cadence and reporting

- What does a normal week look like? What is daily, what is weekly, what is monthly or quarterly?
- Which meetings recur, and do any of them need prep from you?
- What reports or updates do you owe, to whom, and how often?
- When someone asks "what is the status of X," where do you go to answer that today?

This decides whether the vault gets `daily/`, `weekly/`, `meetings/`, and which routines are worth setting up.

### Stage 4: Durable topic areas

- What are the three to seven areas of your work that will still exist a year from now?

These are the things that outlive any individual unit of work. Examples across different kinds of role: a media buyer might say the ad platforms they run, plus creative, plus measurement. A controller might say close, forecasting, audit, tax. A support lead might say tooling, staffing, escalation policy, quality. A designer might say the design system, research, accessibility, brand.

These become subfolders under `docs/` and the canonical anchors everything else wikilinks to. If they name more than seven, ask which are genuinely durable and which are this quarter's initiatives. Initiatives are units of work, not topic areas.

### Stage 5: Where information lives today

- Where does the information you need actually live right now? Walk me through it.
- Which of those do you check daily versus occasionally?
- Is there anything you find yourself manually copying between systems?

Let them describe it before you name tools. Then map what they said onto specific connectors and tell them which are worth wiring up, using the connector section near the end of this file. Be honest that some of what they name may have no connector, and that a `references:` URL plus a fetch on demand is a fine substitute.

### Stage 6: What you do over and over

- What do you do repeatedly, the same way, more than once a month?
- Which of those has a right way to do it that you would have to explain to a new hire?
- Is there something you dread because it is tedious rather than hard?

Every answer here is a candidate skill. Capture the list. You will use it in the first-skill section. Do not build any of them during the bootstrap, and pick the single best candidate to offer at the end.

### Stage 7: Sensitivity and privacy

- Is any of your work confidential, regulated, or under legal hold?
- Do you handle personal data about customers or employees?
- Is there anything that must never be written into a file that syncs to GitHub?

If anything here is a yes, the vault gets an explicit constraint in `CLAUDE.md`. Ask them to phrase the rule and write it close to their words. This is not a place to improvise.

### Stage 8: Options

- Do you want a `MEMORY.md` working-memory file? It lets you say "remember this" and have it persist across sessions. It costs roughly 1 to 2KB loaded on every prompt. Default yes.
- What should the vault be called?
- Anything else I should know about how you work, or how you want me to behave, that I have not asked?

## Derivation rules

Turn the answers into structure mechanically. Do not invent folders nobody asked for.

**Top-level folders.**

| Folder | Create when |
|---|---|
| `<their-work-unit>/` | Always. Named from stage 2, lowercase plural. Gets `backlog/` and `_archive/` subfolders if stage 2 described a lifecycle. |
| `docs/` | Always. One subfolder per stage 4 topic area, each with a `README.md` acting as that section's index. |
| `templates/` | Always. |
| `personal/` | Always. Gitignored. |
| `raw/` | Always. Gitignored. The staging tier for PDFs, screenshots, exports. |
| `meetings/` | If stage 3 surfaced recurring meetings worth recording. |
| `daily/` | If stage 3 or stage 5 justifies a daily rollup, or if they want the daily routine. |
| `weekly/` | Only if stage 3 named a weekly report they actually owe someone. |
| `people/` | If stage 1 named more than two or three recurring humans. |

Anything else, only if they asked for it by name. Resist adding a folder because they might want it later. They will make it the day they need it.

**Templates.** One per note type that the folder lineup implies, and nothing more. Every template carries this common core:

```
title:
type:          # matches the folder it lives in
status:        # living | archived (work units use their lifecycle stages, plus archived)
created:       # YYYY-MM-DD
updated:       # YYYY-MM-DD
owners: []
tags: []
```

Then add per-type fields:

- The work-unit template gets a status field whose allowed values are the stage 2 lifecycle stages **plus `archived`**, so anything can be archived the same way. It also gets `target_date`, `last_verified`, and a pointer field to whatever tracker they named in stage 5.
- `docs/` notes get `last_verified`, `verified_by`, and `related: []` for wikilinks.
- Meeting and daily notes get `date`, `captured_at`, and `attendees` or `sources`, and are named `YYYY-MM-DD-slug.md`.
- `people/` notes get `last_verified`.
- Every other filename is lowercase-hyphenated with no date in it.

Do not ship a template for a note type they have no folder for.

**Freshness rules.** These fill `{{TRUTH_MODEL_ROWS}}`, one row per folder that exists. Use these defaults unless the human gave a different cadence in stage 3:

| Folder | Lifecycle | Rule |
|---|---|---|
| `docs/` | living | Trust if `last_verified` is within 90 days. Older: flag before relying on it and offer to re-verify. |
| `<work-unit>/` | lifecycle stages, then archived | While not archived, trust if `last_verified` is within 30 days. Older: check the tracker before quoting status. |
| `meetings/`, `daily/` | point-in-time | Never re-verified. True as of `captured_at`, and say that date when citing it. |
| `people/` | living | Trust if `last_verified` is within 180 days. Roles and owners drift. |
| `_archive/` | archived | Historical only. Never cite as current. |

**Glossary.** Seed `docs/glossary.md` with the jargon they actually used during the interview. Every acronym, internal tool name, and piece of shorthand they said without explaining, you ask about and write down. This is one of the highest-value artifacts in the vault and it starts nearly empty in most bootstraps because nobody bothers. Bother.

**Folder READMEs.** Each top-level folder and each `docs/` subfolder gets a short `README.md` saying what lives there and holding a placeholder index. These are the per-section indexes in the Karpathy pattern. Keep them to a paragraph plus a stub list. Do not stuff them.

## The plan gate

Render the plan as a tree with a file count and a size estimate for `CLAUDE.md`, then stop and wait.

```
Here's what I'd build, based on what you told me:

  CLAUDE.md                      ~6 KB   operating manual, loaded every prompt
  AGENTS.md                      ~1 KB   pointer to CLAUDE.md for other tools
  README.md                      ~2 KB   human-facing map
  MEMORY.md                      ~1 KB   working memory          [if stage 8 = yes]
  .gitignore
  <work-unit>/
    README.md
    backlog/  _archive/                                          [if lifecycle]
  docs/
    README.md  glossary.md
    <topic-1>/README.md
    <topic-2>/README.md
    ...
  meetings/README.md                                             [if applicable]
  daily/README.md                                                [if applicable]
  people/README.md                                               [if applicable]
  personal/.gitkeep                gitignored
  raw/.gitkeep                     gitignored
  templates/
    <one per note type>
  docs/routines/
    <routine>.md                                                 [if applicable]
  .claude/skills/
    knowledge-base-audit/SKILL.md
    <daily-routine-skill>/SKILL.md                               [if applicable]
  .agents/skills -> ../.claude/skills   symlink
  docs/_archive/bootstrap-second-brain.md   this setup file, moved here at the end

Total: N new files. Nothing existing gets touched, except this setup file,
which gets archived into docs/_archive/ once everything is verified.

Proceed, tweak, or cancel?
```

If they say tweak, take it and re-render. If they cancel, stop and leave the directory alone.

## Literal file blocks

These are written verbatim with placeholders substituted. Do not improvise their structure. The rules in here are load-bearing and hard-won, which is exactly why they are literal rather than left to you to re-derive.

### Placeholder substitution table

| Placeholder | Source |
|---|---|
| `{{VAULT_NAME}}` | Stage 8, the vault name |
| `{{ROLE_LINE}}` | Stage 1, one sentence on role and accountability |
| `{{WORK_UNIT}}` | Stage 2, lowercase plural folder name |
| `{{OWNER_HANDLE}}` | Stage 1, the human's name as a lowercase handle |
| `{{TEAM_OR_SOLO}}` | Stage 1, either `shared with a team` or `a personal vault` |
| `{{FOLDER_LINEUP}}` | Derived folder list, rendered as a bulleted list |
| `{{TRUTH_MODEL_ROWS}}` | One table row per folder that exists, from the freshness rules in the derivation section |
| `{{INGESTION_ROWS}}` | Stage 5, one table row per tool, per the ingestion rules |
| `{{DEFAULT_BEHAVIORS}}` | Derived from stages 3 and 5, as bullets |
| `{{MEMORY_SECTION}}` | If stage 8 wants memory, inline the memory section block below, else empty |
| `{{SENSITIVITY_SECTION}}` | If stage 7 surfaced constraints, inline the sensitivity block below, else empty |
| `{{ROUTINES_SECTION}}` | If any routine was set up, inline the routines block below, else empty |
| `{{SENSITIVITY_RULES}}` | Stage 7, the human's constraints in close to their own words, as bullets |
| `{{ROUTINE_LIST}}` | One bullet per routine set up, each pointing at its `docs/routines/` file |
| `{{DATE_TODAY}}` | Today's date, `YYYY-MM-DD` |

Every placeholder in this table appears in a block below, and every placeholder in a block below appears in this table. If you find yourself wanting a placeholder that is not here, you are improvising. Stop and ask instead.

### `CLAUDE.md`

```markdown
# CLAUDE.md: {{VAULT_NAME}}

This is a markdown notes vault, opened in Obsidian by a human and used by Claude as a knowledge base. {{ROLE_LINE}} This is {{TEAM_OR_SOLO}}.

If you are Claude reading this, these rules govern every action you take in this repo.

## 1. What this place is

- A markdown notes vault. **Code does not live here.**
- Obsidian is the primary reading surface. **Wikilinks** (`[[note-name]]`) are how the graph connects. **Frontmatter** drives the queries.
- Folder lineup:
{{FOLDER_LINEUP}}

## 2. Truth model, or how to decide what to trust

Every note has a `status` and either a `last_verified` or a `captured_at` date in frontmatter. Use them.

| Folder | Lifecycle | Rule |
|---|---|---|
{{TRUTH_MODEL_ROWS}}

When two sources conflict, say so out loud rather than silently picking one. A conflict usually means something was learned and never written down in the canonical place.

{{MEMORY_SECTION}}

## 3. Writing rules

- Every new note uses a template from `templates/`. No bare files.
- Every note has frontmatter. **If a required field is missing, refuse to save and ask.**
- **Wikilinks** for internal references: `[[some-note]]`. **Markdown links** for external URLs.
- Wikilinks inside frontmatter arrays must be quoted: `related: ["[[some-note]]"]`.
- New tags go in `docs/glossary.md` in the same change that introduces them. Tags are flat, lowercase, hyphenated.
- Filenames are lowercase-hyphenated with no dates, except `meetings/` and `daily/` which use `YYYY-MM-DD-slug.md`.

## 4. The `personal/` rule, which is non-negotiable

- `personal/` is gitignored and reserved for private notes.
- **Never** write to `personal/` unless the request explicitly contains the word "personal" or "private."
- **Never** copy content out of `personal/` to anywhere else without explicit confirmation.
- For ambiguous questions, search outside `personal/` first. Only read it if the answer requires it.

## 5. Ingestion rules, for capturing from outside systems

> **Folders represent purpose, not provenance.** A note's home is decided by what it is *about*, not where it came from. Provenance lives in frontmatter (`source_url`, `references`). There is no parallel snapshot tree.

| Source | Treatment | Destination |
|---|---|---|
{{INGESTION_ROWS}}

After folding something into its destination, propose wikilinks to related notes and **ask before adding them**.

**Do not background-sync.** Every capture is an explicit request. Where an outside system is the source of truth, this vault holds a pointer plus your own synthesis, never a mirrored copy. The source system is always more current than a mirror, and a mirror is a maintenance burden that silently rots.

## 6. Default behaviors

{{DEFAULT_BEHAVIORS}}
- **Drafting anything:** search `docs/` first, then `{{WORK_UNIT}}/`, then the dated folders. Cite which notes informed the draft.
- **Unknown topic:** propose creating the note from the right template before writing into a folder that does not fit.
- **Stale sources:** if a `docs/` note is past its freshness rule, say so before relying on it and offer to re-verify.

## 7. Forbidden

- No deletes. Archive via `status: archived`, and move to `_archive/` where one exists.
- No edits to existing meeting or daily notes. They are an append-only record. Corrections go in a new note that links back. One exception: the daily routine may re-run on the same day and merge into that day's daily note.
- No pushing to GitHub without an explicit request.
- No writing to `personal/` without the words "personal" or "private" in the request.

{{SENSITIVITY_SECTION}}

{{ROUTINES_SECTION}}

## 8. Origin

Scaffolded by the bootstrap-second-brain setup file on {{DATE_TODAY}}. The `knowledge-base-audit` skill lives at `.claude/skills/knowledge-base-audit/`. Run it once this vault passes roughly 30 notes to find out what is missing.
```

### `AGENTS.md`

```markdown
# AGENTS.md: {{VAULT_NAME}}

**The rules for this repo live in [CLAUDE.md](CLAUDE.md). Read that file now and follow it exactly.**

This file is a pointer, not a second rulebook. Whatever agent you are, Claude or Codex or Gemini or anything else that looks for an `AGENTS.md`, `CLAUDE.md` is the single source of truth for how to read, write, and cite notes in this vault. Substitute your own name wherever it says "Claude."

Do not copy rules back into this file. Two copies of a rulebook drift apart, and the drift is invisible until it bites. If a rule needs changing, change it in `CLAUDE.md`.
```

After writing `AGENTS.md`, also create the symlink so agent tooling that looks for `.agents/skills` finds the same single copy of the skills:

```bash
mkdir -p .agents && ln -s ../.claude/skills .agents/skills
```

### `.gitignore`

```
# Private notes. Never pushed.
personal/*
!personal/.gitkeep

# Raw staging tier. Unprocessed inputs get folded into the vault, then removed.
raw/*
!raw/.gitkeep

# Obsidian local state
.obsidian/

# Claude Code local settings (machine-specific permissions)
.claude/settings.local.json

# OS and editor noise
.DS_Store
Thumbs.db
*.swp
.vscode/
.idea/
```

### `MEMORY.md`, only if stage 8 asked for it

```markdown
# MEMORY.md: {{VAULT_NAME}}

Working memory. Claude reads this at the start of every session. Keep it short: it loads on every prompt.

## Open threads

Things in flight, with enough context to pick back up. Format: `YYYY-MM-DD: what, and where it stalled`.

## Facts

Things learned that are not yet written into a canonical note. When a fact clearly belongs in a `docs/` note, promote it there and mark it here as `promoted YYYY-MM-DD to [[the-note]]`.

## Recently done

Rolling log of substantive finished work. Prune past a month.

## Conversation log

Pointers to longer session summaries, if any exist.
```

### The memory section, inlined into `CLAUDE.md` when memory is on

```markdown
## 2a. Working memory

`MEMORY.md` at the root is working memory. **Read it at the start of every session.** Treat it as authoritative for "what was I working on" and "what have I told you."

Three ways to write to it:

1. **Silent save.** When the request contains "remember this," "park this," "save for later," or "add to memory," just update it.
2. **Offer to save.** When something looks memory-worthy but is not obviously so, propose a pre-drafted one-line entry.
3. **Detect and flag.** Watch for: a fact that contradicts a canonical note, a session ending mid-task, substantive work finishing, or a piece of jargon defined in passing. Offer the appropriate save.

Bias toward asking rather than staying silent. Memory offers come at the **end** of a response, never before the substance of the actual question.

**Promotion.** When a fact in memory clearly maps to a canonical note, offer to write it there in the same turn. If accepted, edit the note and mark the memory entry as promoted.

**What does not go in memory:** shared vocabulary goes to `docs/glossary.md`. Anything personal goes to `personal/`. Content owned by an outside system stays there and gets fetched.
```

### The sensitivity section, inlined into `CLAUDE.md` when stage 7 surfaced constraints

```markdown
## 7a. Handling constraints

{{SENSITIVITY_RULES}}

When in doubt about whether something falls under these constraints, ask before writing it to a file. A question costs a few seconds. A leak into git history is permanent.
```

### The routines section, inlined into `CLAUDE.md` when a routine exists

```markdown
## 7b. Active routines

{{ROUTINE_LIST}}

Routines are prompts the human runs, not background daemons. Each one is documented in `docs/routines/`. Never invent a routine or run one unprompted.
```

## Skills to install

A skill is a folder under `.claude/skills/<name>/` holding a `SKILL.md` with YAML frontmatter (`name` and `description`) followed by instructions. Claude loads it when the description matches what is being asked. Think of a skill as the briefing you would give someone before they attempt a task for the first time.

Install two at bootstrap. Build the third with the human afterwards.

### 1. `knowledge-base-audit`, written literally

Write this to `.claude/skills/knowledge-base-audit/SKILL.md`, verbatim.

````markdown
---
name: knowledge-base-audit
description: Use when the user wants to audit how this markdown vault is organized for retrieval and get recommendations. Trigger phrasings include "audit my knowledge base", "review my retrieval setup", "is this set up to scale", "optimize the vault structure", "should I add RAG". Maps the vault to the 7-level knowledge base rubric, identifies gaps against the Karpathy pattern, and produces a prioritized recommendation set. Honors the "less is more" principle and does not propose changes that bloat what loads on every prompt. Never modifies a file.
---

# Knowledge Base Audit

A read-and-recommend skill. It writes nothing.

## Procedure

1. **Read what should be true.** `CLAUDE.md`, `README.md`, `docs/glossary.md`, and `templates/`. The audit measures what *is* true against what these claim.

2. **Inventory.** File counts per top-level folder and per `docs/` subfolder. Which folders have a README acting as an index, and whether it is current. Wikilink density: where is it too thin for graph traversal to pay off. Rough token size (bytes divided by 4) of everything loaded every prompt. Frontmatter spot-check on 5 to 10 random notes against the templates. Staleness count: `docs/` notes whose `last_verified` is missing or more than 90 days old.

   Exclude `personal/`, `raw/`, and `_archive/` from the live inventory. Count archives separately.

3. **Classify on the rubric.** Level 1 automemory, 2 CLAUDE.md, 3 multiple markdown state files, 4 Karpathy/Obsidian wiki, 5 naive RAG, 6 graph RAG, 7 agentic multimodal RAG. Pick the single most accurate level, including half-steps like "3.5" or "4, partial."

4. **Map against the Karpathy primitives.** For each, mark Have, Partial, or Missing with one line of evidence: raw staging tier, compiled derived wiki, master index, per-section indexes, wikilink backlinks, derived synthesis articles, lint/health-check pass, outputs filed back into the wiki, extra tools wired up.

5. **Find retrieval bottlenecks specific to this vault.** This is where the audit earns its keep, because generic pattern advice misses the domain. Probe: recency retrieval ("what happened last week"), per-work-unit retrieval ("status of X"), per-topic retrieval ("what depends on Y"), per-person retrieval ("who owns Z"), and whether the freshness rule is checkable or purely aspirational.

6. **Score context-rot risk.** Flag sections of always-loaded files that read like reference material rather than always-relevant guidance. The fix is almost never "delete." It is "move to a sub-file and replace the inline copy with a pointer."

7. **Report.** Lead with a 2 to 3 sentence TL;DR: current level, top three changes, and whether to consider RAG (default: no). Then the rubric classification, the primitive coverage table, the inventory snapshot, the bottlenecks, and the context-rot notes. Rank recommendations by leverage over effort, and mark which need approval.

8. **Offer to persist.** Do not auto-write. Offer to leave it in chat, or save to `docs/audits/<date>-knowledge-base-audit.md`.

## Pushback rules

- **Level 4 is the target.** Do not recommend embeddings, vector databases, or graph RAG unless the audit shows concrete level-4 failure: queries missing obviously relevant notes, retrieval cost becoming material, sources that cannot be represented as text. Even then, frame it as contingent, not prescriptive.
- **The bar for adding to `CLAUDE.md` is high.** If a recommendation grows it, identify the compensating cut. Net tokens-per-prompt should not increase.
- **Vault shape beats generic advice.** "Add wikilinks everywhere" is generic. "Traversal from the topic index would save a vault-wide grep on this specific recurring question" is useful.
- **Honor the existing truth model** rather than inventing a parallel one.
- **No deletes.** Recommend archiving or relocating.
- **An index that gets read on every query but only sometimes helps is net negative.** Count cost in tokens, not lines.

## What NOT to do

- Do not modify any file, including `MEMORY.md`.
- Do not read `personal/` under any circumstances.
- Do not auto-create the index files you recommend. Propose the structure and let the human approve it.
- Do not invent rubric levels or pattern primitives. If something does not fit, name it as a vault-specific addition rather than mislabeling it.
````

### 2. The daily routine skill, generated from the interview

This one cannot be literal, because it depends entirely on which connectors exist. Build it from the stage 5 answers.

**Why this exists.** The routine's output is not really for the human to read. Its job is to keep your context current so that tomorrow you already know what happened today. That reframing matters: a daily note that nobody reads is still doing its job.

Write `.claude/skills/<name>-report/SKILL.md` with:

- **Frontmatter.** A `description` listing the trigger phrasings the human would actually say. Include their own words from the interview, plus "EOD report" and "what did I do today."
- **Sources.** One section per connector they confirmed in stage 5, each with what to pull and the time window. Only connectors they actually have. A routine that references a tool they never connected will fail silently and teach them the system is unreliable.
- **Output.** A single dated file in `daily/`, named `YYYY-MM-DD-<slug>.md`, using the daily template. Same-day re-runs merge into and improve that file, never spawn a second one. This is the only permitted edit to an existing daily note; once the day is over, the note is append-only like the rest.
- **What to extract.** Action items assigned to them, asks from the specific stakeholders named in stage 1, decisions made, and anything that contradicts what the vault already believes.
- **Close-out.** Offer memory promotions at the end if `MEMORY.md` exists. Commit quietly. Never push.

If stage 3 named a weekly report they genuinely owe someone, add a second skill that rolls up the week's dailies. Do not build a weekly report nobody asked for.

### 3. Their first real skill, built with them afterwards

Do not build this during the bootstrap. Offer it once the scaffold is verified.

Take the strongest candidate from stage 6 and offer it by name:

```
You mentioned <the task> is something you do over and over. That's a good
first skill. Here's how it works: you give me the reference material, the
rules you'd tell a new hire, and one example of the finished thing done
right. I turn that into a skill, and from then on I follow it without you
re-explaining.

Want to build it now? Bring whatever documentation exists, even if it's messy.
```

When they say yes:

1. **Gather the raw material.** Vendor or platform documentation, their own past examples of the output, and the unwritten rules they carry in their head. The unwritten rules are the valuable part and they will not think to mention them, so ask directly: what mistakes does a new person make?
2. **Write the skill to `.claude/skills/<name>/SKILL.md`.** A specific `description` with real trigger phrasings, a procedure, and a "what not to do" section drawn from those mistakes.
3. **Test it immediately** on a real instance of the task, with them watching.
4. **Fix what was wrong** and tell them plainly that skills get better by being corrected, so the right instinct when output is off is to say what was wrong rather than to fix it by hand.

## Routines

A routine is a prompt the human runs, not a daemon. Document each one in `docs/routines/<name>.md` so it is reproducible and disable-able:

- **What it does**, as a bulleted list of concrete effects.
- **How to run it**, as a prompt to paste verbatim into a fresh session, including the absolute working directory.
- **How to disable it**: stop pasting the prompt. Say so explicitly so it never feels like infrastructure.
- **Troubleshooting**, left as a stub to fill in the first time it misbehaves.

Tell the human that once a routine is stable they can move it onto a schedule so it runs on its own while the machine is awake, and that the way to build a new one is to describe the task, have Claude write the prompt, and paste that prompt into the scheduler. Do not set up a schedule during the bootstrap.

## Verify before you hand it over

Run these and report the results plainly:

```bash
ls -la
find . -type d -not -path './.git*' | sort
wc -c CLAUDE.md AGENTS.md README.md MEMORY.md 2>/dev/null
```

Then check four things:

1. **`CLAUDE.md` is under 10KB.** If it is over, do not shrug. Find the section that reads like reference material, move it to a file under `docs/`, and replace it with a pointer.
2. **No placeholder survived.** Grep for `{{` and for `TODO` across everything you wrote, excluding this setup file, which is full of them by design. A shipped `{{WORK_UNIT}}` is a broken vault.
3. **Every template parses.** Each one opens with `---`, closes with `---`, and every field the truth model relies on is present.
4. **Every wikilink resolves or is deliberate.** A `[[link]]` to a note that does not exist yet is fine, and marks something worth writing. A `[[link]]` with a typo is a dead end. Check them.

Then initialize git and make the first commit, but **do not push.** Pushing is their call.

## Connectors

Connectors are what turn the vault from a filing cabinet into something that can answer questions. **You cannot set these up.** Each one needs the human to log in through Claude Desktop's own settings. Say that plainly rather than trying and failing.

What you can do is tell them which ones are worth it, based on stage 5, and in what order. Roughly:

- **Start with wherever their conversations happen.** For most people that is their chat tool and their email. This is the highest-value connector because it is where commitments get made and forgotten.
- **Then their calendar,** which is what makes a daily routine able to reconstruct a day.
- **Then their meeting-notes tool,** if they use one. Automatic meeting notes flowing into the vault is the closest thing to free context there is.
- **Then whatever holds their team's documents.**
- **Then their tracker,** if their work units live in one.
- **Then their analytics or data tools,** which are the ones that feel like magic but only pay off once the rest is in place.

Two honest caveats to pass along. Some tools they named will have no connector, and for those a `references:` URL in frontmatter plus fetching on demand works fine. And a connector they authorize can read real data, so anything that lands in a note is a note they should be willing to have in git.

## Pushback rules

- **Do not inflate `CLAUDE.md`.** When asked for "more guidance," prefer a referenced sub-file. It loads on every prompt, so bytes are a recurring cost and a dilution of signal.
- **Do not create folders nobody asked for.** The urge to add one "in case" is strong. Resist it.
- **Do not mirror an outside system into the vault.** Frontmatter holds the pointer, the body holds their synthesis. A mirror rots invisibly.
- **Do not recommend RAG.** Point at the audit skill.
- **Do not create example notes.** The scaffold ships templates, not samples. Examples go stale and then pollute retrieval, which is worse than having none.
- **Do not add tags nobody asked for.** Every new tag goes in the glossary in the same change.
- **Do not auto-build the wikilink graph.** Suggest the obvious links as you scaffold, then let them accrue naturally as notes get written. That is how the graph stays signal-rich instead of becoming noise.
- **Do not promise a background sync.** Routines are prompts they run.
- **Do not skip the interview,** even if the human says "just do whatever Ben has." Their job is not Ben's job. Ask anyway, and say why: the whole value is that the vault matches *their* work.

## What NOT to do

- Do not write a single file before the plan is approved.
- Do not overwrite anything that already exists. If a target path is occupied, stop and ask.
- Do not import their existing notes as part of the bootstrap. Offer batched triage afterwards, 5 to 10 notes at a time, with approval per move.
- Do not add Obsidian configuration. Obsidian writes its own on first open.
- Do not attempt to install connectors or MCP servers.
- Do not push to GitHub.
- Do not explain the Karpathy pattern or the rubric unprompted. It is encoded in the structure. Nobody needs the theory to use the vault.

## Last step: retire this file

Once the vault is verified, this file has done its job and should stop sitting in the root looking like part of the vault.

Move it to `docs/_archive/bootstrap-second-brain.md` (lowercase-hyphenated, per the vault's filename rule, and in `_archive/` because it is archived) and add frontmatter so it obeys the vault's own rules:

```
---
title: Second Brain Bootstrap
type: doc
status: archived
created: {{DATE_TODAY}}
updated: {{DATE_TODAY}}
last_verified: {{DATE_TODAY}}
verified_by: {{OWNER_HANDLE}}
owners: [{{OWNER_HANDLE}}]
tags: []
related: []
---
```

The audit skill already excludes `_archive/`, so its placeholders will not be mistaken for a broken note. Commit the move with everything else.

Then tell the human what to do next, in five lines or fewer. Something like:

```
Done. Your vault is set up and committed locally, not pushed.

Next, in order:
1. Open this folder in Obsidian (File > Open Vault). The graph gets useful
   around 10 notes.
2. Set up the connectors I listed. I can't do those, they need your login.
3. Write one real note from a template, about something you're working on now.
4. When you're ready, say "let's build my <task> skill" and we'll do it.

Push to GitHub whenever you want. I've left that to you.
```
