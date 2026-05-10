---
name: grill-with-docs
description: >
  Grill a plan/spec against the repo's domain language and documented decisions.
  Updates CONTEXT.md (glossary) inline as terms crystallize, and writes ADRs sparingly.
  Use for team engineering work (PM/FE/BE/FS) to converge on shared language and prevent
  "code keeps growing messy" drift.
aliases: [grill-with-dogs, grill-with-docs]
---

# Grill With Docs (Team Mode)

This skill is based on Matt Pocock's public `mattpocock/skills` methodology, adapted to Jianan's workflow.

## Goal

Relentlessly clarify terms, boundaries, and invariants **and** persist the result into repo docs so that:

- PM / FE / BE / FS share the same vocabulary
- future agents (and humans) stop re-asking the same questions
- architecture decisions don't get silently re-litigated

## Repo doc layout

Default (single context):

```
/
├── CONTEXT.md
├── docs/
│   └── adr/
└── src/
```

If the repo has multiple contexts, add a `CONTEXT-MAP.md` at repo root and put `CONTEXT.md` per context.

Create files lazily: only when you have something real to write.

## Session rules

1) Ask questions **one at a time**, wait for user feedback.
2) If a question can be answered by exploring the codebase, explore first.
3) If user language conflicts with `CONTEXT.md`, call it out immediately and resolve.
4) When a term is resolved, update `CONTEXT.md` **right now** (don't batch).

## ADR policy (write sparingly)

Only propose an ADR when all are true:

1. Hard to reverse
2. Surprising without context
3. Result of a real trade-off

Put ADRs in `docs/adr/`.

## Output format

At the end, return:

1) A short "Decisions" summary (5-10 bullets)
2) Links/paths to files updated (CONTEXT.md + ADRs)
3) Any open questions / TODOs

