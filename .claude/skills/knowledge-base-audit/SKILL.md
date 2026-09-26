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
