---
name: dev-memory-and-todos
description: Use when a coding project spans multiple sessions, when the user gives a long multi-part request, when the user says they will review changes later, or when continuing work and you need to recall what was done and what is pending. Symptoms: "continue development", "what's left?", "I'll review tomorrow", "remember this", lost context between sessions, requirements scattered across chat messages.
---

# Dev Memory and TODOs

## Overview

Multi-session projects lose context: what was decided, what's half-done, which of the user's asks are still open. Fix it with a durable in-repo `dev-memory/` folder plus one rule: **turn the user's own words into a reviewable backlog before you start coding.**

Core principle: **the user's raw requirements are the source of truth — capture them verbatim as TODO items, never only as your paraphrase.**

## When to Use

- Project work continues across sessions (you'll be re-invoked later with cold context).
- The user sends a long message bundling many asks ("change A, also B, and C feels important too").
- The user says they'll review/audit the work later.
- You're resuming and ask yourself "what was I doing / what's still open?"

Not for: one-off single-session tasks, or facts the repo already records (code structure, git history → those go in AGENTS.md or stay in code).

## The Folder

Create `<repo>/Design/dev-memory/` (or `docs/dev-memory/`) with three files:

| File | Holds | Volatility |
|------|-------|-----------|
| `PROJECT-MEMORY.md` | Stable facts: what the product is, locked decisions/red-lines, tech stack, backend, key files. | Rarely changes |
| `SESSION-WIP.md` | This session: done / in-progress / to-verify / deferred / next-up. Read first when resuming. | Every session |
| `TODO.md` | Every requirement as a checkbox, grouped by area, with status + priority markers. | Continuous |

Also drop a one-line pointer in your persistent memory (`MEMORY.md`) so future sessions know to open this folder.

## Workflow

1. **Resume:** read `SESSION-WIP.md` then `TODO.md` before touching code.
2. **Capture (do this BEFORE coding):** for each thing the user asked, add a TODO item. Quote or closely preserve their wording — including the "this also feels important" asides. Group by area (page/module). If the user enumerated items (P4-1, #3...), keep their IDs.
3. **Mark status** with a consistent legend, e.g.:
   - `[ ]` not started · `[x]` done & self-tested · `⏸` deferred (note why) · `🧪` needs the user's manual verification
   - priority `🔴 high` / `🟡 medium`
4. **Annotate for review:** when the user will review later, add a top "review checklist" table: commit hash · what changed · where to look · what to verify. Convert relative dates to absolute.
5. **Update `SESSION-WIP.md`** at the end of meaningful work, and commit the dev-memory alongside the code change.

## Quick Reference

```
Design/dev-memory/
  PROJECT-MEMORY.md   # stable: product, red-lines, stack, key files
  SESSION-WIP.md      # done / WIP / to-verify / deferred / next
  TODO.md             # review checklist + every ask as a checkbox
```

## Common Mistakes

- **Paraphrasing away the user's words.** You lose nuance and they can't recognize their own ask at review. Preserve their phrasing and any chosen copy/decisions verbatim.
- **Dropping the "by the way" asks.** Side-comments ("X also feels important") are requirements too — capture them.
- **Letting `[x]` imply verified.** Self-tested (tsc/build) ≠ user-verified. Use a separate `🧪` marker.
- **Putting volatile status in PROJECT-MEMORY.** Keep "what's done" in SESSION-WIP; keep only stable facts in PROJECT-MEMORY.
- **Duplicating the repo.** Don't restate code structure or git history; link to AGENTS.md/code instead.

## Relationship to Other Skills

Complements, doesn't replace: planning skills (task breakdown), spec-driven-development (formal specs), context-engineering (rules files). This skill is specifically about the durable in-repo memory folder + verbatim-requirement-to-TODO capture for review handoff.
