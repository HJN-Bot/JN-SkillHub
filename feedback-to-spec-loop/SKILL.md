---
name: feedback-to-spec-loop
description: Use when turning messy human feedback or a PRD into shipped changes across multiple sessions — when the user gives a long multi-part request, says "fix all these", "redo the plan", "I'll review later", or "remember this", or when resuming work and you need to recall what's done and pending. Incorporates Grill-Me design-tree interviewing, vertical-slice issue breakdown, TDD red-green-refactor, and autonomous Ralph Loop execution.
---

# Feedback → TODO → Spec Loop (Enhanced)

## Overview

A repeatable loop for turning a human's raw words (PRD, scattered chat feedback, "this feels off") into shipped, reviewable changes. Three core rules:

1. **The user's own words are the source of truth.** Capture verbatim before paraphrasing or coding.
2. **Grill before you plan.** Walk the design tree — every undecided branch is a future rework.
3. **No change without a tiny spec. Vertical slices, not horizontal layers.**

## When to Use

- Long multi-part feedback ("change A, also B, C feels important too").
- "Redo the plan", "fix all these", "I'll review tomorrow", "remember this".
- Resuming a multi-session project with cold context.
- Any non-trivial feature where the scope spans >1 file or >1 session.

Not for: trivial one-off edits in a single session.

---

## The Full Loop

```
human feedback / PRD / "this feels off"
  │
  ├─► Phase 0: GRILL                   → design tree walk; 3-sentence skill, 16+ questions
  ├─► Phase 1: CAPTURE verbatim         → dev-memory/TODO.md (📦 archive section)
  ├─► Phase 2: WRITE PRD               → GitHub Issue: Problem/Solution/UserStories/ImplDecisions
  ├─► Phase 3: PRD → ISSUES            → vertical slices + blocking relationships
  ├─► Phase 4: SPEC per-issue          → Design/specs/<date>-<topic>.md (4 sections)
  ├─► Phase 5: user approves priority   → reorder/merge/delete slices before any code
  ├─► Phase 6: RALPH LOOP              → autonomous: read→TDD→implement→test→commit→close
  ├─► Phase 7: HUMAN QA                → QA plan from recent commits → new issues → loop back
  └─► Phase 8: UPDATE memory + links   → status flips; user verifies in app
```

---

## Lightweight Mode (TODO + Spec spine) — the default

Most projects don't have GitHub Issues or a test suite. Run the loop with files only — this is the everyday path; the heavy machinery (GitHub Issues, formal TDD) is opt-in for projects with CI.

| Full phase | Lightweight equivalent |
|---|---|
| GRILL | Same — ask before planning (fewer questions for small asks). |
| CAPTURE | `TODO.md` 📦 verbatim archive. |
| PRD | A north-star line + themes at the top of `TODO.md` (skip the GitHub Issue). |
| PRD → Issues | Rows in a `TODO.md` table (per-page / per-theme), with priority + status — not GitHub Issues. |
| SPEC per-issue | `Design/specs/YYYY-MM-DD-<topic>.md`, 4 sections, linked both ways to TODO. **This is the heart of the "TODO + Spec" feel.** |
| APPROVE | User OKs the spec (or the plan order) before code. |
| RALPH LOOP | spec → implement → `tsc`/`build` green → `git commit` → flip status to ✅🧪. |
| HUMAN QA | A `REVIEW-<date>.md` checklist (what changed / where to look / 🧪 verify / ⚠️ key decisions). |
| UPDATE | Update `TODO.md` Specs index + `SESSION-WIP.md`; user verifies in app. |

Scale up to the full phases (real Issues, test-first TDD, parallel Ralph Loops) only when the project has the infrastructure for it.

---

## Phase 0: Grill Me (Design Tree Interview)

**Before you capture, plan, or code — walk the design tree.**

Use this 3-sentence prompt (self-contained — works without any other skill installed; if a `grill`/`grill-with-docs` skill is present it deepens this):

> Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one by one. Finally, if a question can be answered by exploring the codebase, explore the codebase instead.

**What happens:**
- The agent asks questions until every design branch is walked
- Each decision node (e.g. "advanced search vs text box") spawns child questions (filters, sorting, etc.)
- Expect 10-50 questions for non-trivial features
- Codebase exploration replaces guesswork: if the answer exists in code, read it
- Session length: 5-45 minutes depending on scope

**When to skip:** Single-file fixes with zero ambiguity. Even then, ask "any edge cases?"

**Source concept:** Frederick P. Brooks, *The Design of Design* — the design tree. "Walk down all branches before committing to code."

---

## Phase 1: Capture Verbatim

Archive the user's raw words **exactly** into `TODO.md`'s 📦 archive section. Do not paraphrase. Side-comments ("by the way…") are requirements too.

Format:
```markdown
## 📦 Verbatim Feedback Archive

### 2026-06-02 — [topic]
> [user's exact words, including emojis and "btw" asides]

### 2026-06-01 — [topic]
> ...
```

---

## Phase 2: Write PRD → GitHub Issue

Use this template. The PRD itself is submitted **as a GitHub Issue** (so it's linkable, closeable, searchable).

```markdown
# PRD: [Feature Name]

## Problem Statement
[What problem exists today. Measurable pain if possible.]

## Solution
[What we're building. Keep implementation decisions light — durable, not over-prescriptive.]

## User Stories
[List desired behaviors in Agile user-story language. Each = one user-facing capability.]

## Implementation Decisions
[Key decisions made during Grill Me. Lightweight — this is guidance, not a contract.
Out-of-date PRDs cause problems at implementation time, so keep durable.]

## Major Modules
[Sketch the modules/components affected or to be built. Used by Phase 3 for slicing.]
```

**Important:** The PRD describes the **destination**, not the journey. Phase 3 handles the journey.

---

## Phase 3: PRD → Issues (Vertical Slice Breakdown)

**Core principle — vertical slices, not horizontal layers:**

> Each issue is a thin vertical slice that cuts through all integration layers.
> Do NOT slice horizontally (one issue for DB, one for UI, one for API).

**Tracer bullet prioritization:**
1. Identify the **riskiest unknown** (new integration, untested pattern, unclear feasibility)
2. Make that Issue #1 — flush out unknown unknowns early
3. If it fails, you learn fast without wasting time on dependent work

**Output format** in `TODO.md`:

```markdown
## 🗺️ Issues Kanban

| # | Issue | Blocks | Blocked By | Priority | Status |
|---|-------|--------|------------|----------|--------|
| 1 | [title] | — | — | 🔴 | ⬜ |
| 2 | [title] | — | — | 🟡 | ⬜ |
| 3 | [title] | 1 | — | 🟡 | ⬜ |
| 4 | [title] | 2,3 | — | 🟢 | ⬜ |

Parent PRD: [link to GitHub Issue #N]
```

**Blocking rules:**
- Unblocked issues can be picked up in parallel (fire multiple Ralph Loops at once)
- Blocked issues auto-unlock when their dependency closes
- New issues (from QA, bugs, scope creep) can be inserted with new blocking relationships

---

## Phase 4: Spec Per-Issue (4 Sections)

Each issue gets a small spec before implementation. `Design/specs/YYYY-MM-DD-<topic>.md`:

1. **修改建议 / Suggestion** — what & why (in the user's framing, linked to user story).
2. **解决思路 / Approach** — root cause + the strategy.
3. **技术方案 / Plan** — files, functions, key edits. **Confirm interface changes first** — they're the most important decisions.
4. **验证测试 / Verification** — TDD entry point: what test proves this works, plus manual checks.

Link both ways: TODO keeps a Specs index (spec ↔ Issue ↔ status); the spec header links back to its Issue.

---

## Phase 5: User Approves Priority

Before ANY code is written:

- Present the Issues Kanban to the user
- Let user reorder, merge, or delete slices
- Confirm: "Does this order flush out the biggest unknown unknowns first?"
- User says "go" → move to Phase 6

---

## Phase 6: Ralph Loop (Autonomous Implementation)

Named after the autonomous agent that executes one issue at a time.

```
┌───────────────────────────────────────────────┐
│  RALPH LOOP (runs per issue, can be parallel)  │
│                                                │
│  1. Read the GitHub Issue + its linked Spec     │
│  2. Red-green-refactor (TDD skill if present;   │
│     else follow the inlined beats below)        │
│  3. Write ONE failing test first                │
│  4. Write minimal code to pass                  │
│  5. Refactor (preferably with fresh context)    │
│  6. Run full test suite; tsc/build green        │
│  7. git commit -m "feat: X (closes #N)"         │
│  8. Comment on Issue with test count + summary  │
│  9. Issue auto-closes; next unblocked starts    │
│                                                │
└───────────────────────────────────────────────┘
```

**TDD integration — the red-green-refactor beat:**
- "Red green refactor with agents is incredible" — video source
- Confirm interface changes with user first — they're the most important decisions
- Design interfaces for testability (test at module boundaries, not internals)
- Write ONE test at a time, then code, then refactor
- LLMs are reluctant to refactor their own code — clear context between refactor passes, or spawn a fresh agent

**Interface-first principle:**
> When an AI faces a codebase with many small undifferentiated modules, it struggles to understand relationships and test boundaries. When the codebase has larger modules with thin interfaces, testing and implementation become natural. **Confirm interface changes before coding.**

---

## Phase 7: Human QA

After 3-5 commits accumulate:

1. **Generate QA Plan** from recent commits:
   - Each commit's functional description
   - Expected behavior vs. failure modes
   - Specific test steps (manual or scripted)
   - Regression checklist (did previously fixed bugs resurface?)

2. **User executes** QA Plan locally:
   - Mark each test pass/fail
   - Failed → new Issue (goes back into Kanban, Phase 3)

3. **Feedback loop closes:**
   - QA Issues enter the same Kanban with blocking relationships
   - Ralph Loop picks them up on next cycle

---

## In-Repo dev-memory Folder

`<repo>/Design/dev-memory/` (or `docs/dev-memory/`):

| File | Holds |
|------|-------|
| `PROJECT-MEMORY.md` | Stable facts: product, locked decisions/red-lines, stack, key files. Never volatile status. |
| `SESSION-WIP.md` | This session: done / WIP / to-verify / deferred / next. Read first when resuming. |
| `TODO.md` | North star → Issues Kanban → Specs index → done archive → 📦 verbatim feedback archive. |

Drop a one-line pointer in your persistent memory so future sessions open this folder.

---

## Status Legend

`⬜` not started · `✅` implemented + self-tested (tsc/build/tests green) · `🧪` needs user verification · `⏸` deferred (note why) · `❌` blocked (link to blocker)

Priority: `🔴` risky/urgent · `🟡` important · `🟢` nice-to-have

`✅` never means "user-verified" — that's `🧪` until confirmed in the running app.

---

## Common Mistakes

- **Skipping Grill Me.** The 5 extra minutes of questioning saves hours of rework. Every undecided branch = future rework.
- **Horizontal slicing.** "DB layer → API layer → UI layer" is wrong. Each issue should deliver a user-visible capability end-to-end.
- **Paraphrasing away the user's words.** They won't recognize their own ask at review. Preserve phrasing verbatim.
- **Dropping "by the way" asks.** Side-comments are requirements too.
- **Coding before the spec.** The spec + approval is the gate, like writing the test first.
- **Letting the TODO sprawl.** When feedback piles up, re-plan around a north star and themes; archive raw feedback below, keep the active plan on top.
- **Putting volatile status in PROJECT-MEMORY.** "What's done" lives in SESSION-WIP; only stable facts in PROJECT-MEMORY.
- **Skipping interface confirmation.** Interface changes are the highest-leverage decisions — confirm them with the user before implementation.

---

## Relationship to Other Skills

This is the outer loop and is **fully self-contained** — every phase's essential content is inlined above, so it runs on a bare machine with no other skills installed. The skills below are **optional enhancers**: used automatically if present, silently skipped if not. None is a hard dependency.

- **Grill Me** → Phase 0 design tree walk
- **TDD** → Phase 6 red-green-refactor engine
- **Improve Architecture** → when a Spec's 技术方案 touches a shared interface or a file that's grown too big: before coding, spawn 2-3 subagents to draft competing interface/module designs, compare, pick one, and record the choice in the Spec. Run it between Ralph Loop cycles, not mid-issue.
- **Skill Vetter** → review spec quality before implementation

Where a real test suite exists, the spec's verification section drives it; where it's product/UX, verification is build + manual checks.
