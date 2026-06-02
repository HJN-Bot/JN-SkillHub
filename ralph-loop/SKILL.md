---
name: ralph-loop
description: Autonomous agent that reads a GitHub Issue, implements it with TDD red-green-refactor, runs tests, commits, and closes the issue — then moves to the next unblocked one. Use for automated implementation of well-spec'd issues.
---

# Ralph Loop — Autonomous Implementation

Named after the agent that executes one issue at a time, autonomously.

## The Loop

```
┌───────────────────────────────────────────────────┐
│  RALPH LOOP (one issue per cycle)                  │
│                                                    │
│  1. Read GitHub Issue + linked Spec                 │
│  2. Load TDD skill (red-green-refactor)            │
│  3. Write ONE failing test first                   │
│  4. Write minimal code to pass                     │
│  5. Refactor (with fresh context if possible)      │
│  6. Run full test suite → tsc/build green          │
│  7. git commit -m "feat: X (closes #N)"             │
│  8. Comment on Issue with summary + test count     │
│  9. Issue auto-closes; fetch next unblocked        │
│                                                    │
└───────────────────────────────────────────────────┘
```

## How to invoke

```bash
# Single issue
ralph-loop --issue 42

# All unblocked in priority order
ralph-loop --kanban TODO.md
```

## Commit message convention

```
feat: add split-pane editing engine (closes #42)

A pure function document editing engine with 28 tests
covering all acceptance criteria from the parent PRD.
```

## Parallel execution

Unblocked issues can run in parallel — spawn multiple Ralph Loop instances:

```
Issue #1 (not blocked) → Ralph Loop A
Issue #2 (not blocked) → Ralph Loop B   } both run simultaneously
Issue #3 (blocked by #1) → waits for A
Issue #4 (blocked by #2,#3) → waits for B and A
```

## Prerequisites

- GitHub Issue with linked spec (from `prd-to-issues`)
- TDD skill loaded
- Test suite in the repo
- User approval on priority order
