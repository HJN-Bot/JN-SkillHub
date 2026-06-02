---
name: feedback-to-spec-loop
description: Use when turning messy human feedback or a PRD into shipped changes across multiple sessions — when the user gives a long multi-part request, says "fix all these", "redo the plan", "I'll review later", or "remember this", or when resuming work and you need to recall what's done and pending. Keeps a durable in-repo dev-memory, turns raw requirements into a tracked TODO, and writes a small spec per change before coding.
---

# Feedback → TODO → Spec Loop

## Overview

A repeatable loop for turning a human's raw words (PRD, scattered chat feedback, "this feels off") into shipped, reviewable changes — TDD-style, but for product work. Two rules:

1. **The user's own words are the source of truth.** Capture them verbatim before you paraphrase or code.
2. **No change without a tiny spec first.** Each modification point gets a 4-section spec, linked both ways to the TODO, before implementation.

## When to Use

- Long multi-part feedback ("change A, also B, C feels important too").
- "Redo the plan", "fix all these", "I'll review tomorrow", "remember this".
- Resuming a multi-session project with cold context.

Not for: trivial one-off edits in a single session.

## The Loop

```
human feedback / PRD
  └─► 1. CAPTURE verbatim          → dev-memory/TODO.md (📦 archive section)
  └─► 2. PLAN into roadmap         → north star + per-theme items + priorities
  └─► 3. SPEC the next change      → Design/specs/<date>-<topic>.md (4 sections)
  └─► 4. user approves spec
  └─► 5. IMPLEMENT small + verify  → tsc/build/tests green
  └─► 6. UPDATE memory + links     → status flips to ✅🧪; user verifies in app
```

## In-repo dev-memory folder

`<repo>/Design/dev-memory/` (or `docs/dev-memory/`):

| File | Holds |
|------|-------|
| `PROJECT-MEMORY.md` | Stable facts: product, locked decisions/red-lines, stack, key files. |
| `SESSION-WIP.md` | This session: done / WIP / to-verify / deferred / next. Read first when resuming. |
| `TODO.md` | North star → per-theme roadmap (priorities) → Specs index → done archive → **verbatim feedback archive**. |

Drop a one-line pointer in your persistent memory so future sessions open this folder.

## The per-change Spec (keep it short)

`Design/specs/YYYY-MM-DD-<topic>.md`, four sections, a few sentences each:

1. **修改建议 / Suggestion** — what & why (in the user's framing).
2. **解决思路 / Approach** — root cause + the idea.
3. **技术方案 / Plan** — files, functions, key edits.
4. **验证测试 / Verification** — commands + manual checks.

Link both ways: TODO keeps a **Specs index** table (spec ↔ TODO item ↔ status); the spec header links back to its TODO item. This gives every change a traceable spec + version record.

## Status legend (use consistently)

`⬜` not started/needs spec · `✅` implemented + self-tested (tsc/build) · `🧪` needs the user's manual verification · `⏸` deferred (note why) · priority `🔴/🟡/🟢`.

`✅` never means "user-verified" — that's `🧪` until they confirm in the running app.

## Common Mistakes

- **Paraphrasing away the user's words.** They won't recognize their own ask at review. Preserve phrasing and any chosen copy/decisions verbatim in the archive.
- **Dropping "by the way" asks.** Side-comments are requirements too.
- **Coding before the spec.** The spec + approval is the gate, like writing the test first.
- **Letting the TODO sprawl.** When feedback piles up, re-plan around a north star and themes; archive raw feedback below, keep the active plan on top.
- **Putting volatile status in PROJECT-MEMORY.** "What's done" lives in SESSION-WIP; only stable facts in PROJECT-MEMORY.

## Relationship to other skills

This is the outer loop; it composes with planning/spec/TDD skills. Where a real test suite exists, the spec's verification section drives it; where it's product/UX, verification is build + manual checks the user runs.
