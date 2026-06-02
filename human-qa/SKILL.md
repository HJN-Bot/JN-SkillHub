---
name: human-qa
description: Generate a structured QA plan from recent git commits, execute manual testing, and feed discovered issues back into the development loop. Use after 3-5 commits accumulate, or when the user says "QA this", "test the recent changes", "let me review".
---

# Human QA — Commit-Driven Quality Loop

Human-driven quality assurance with AI-generated test plans. Closes the loop between implementation and verification.

## The Loop

```
Recent 3-5 commits
      ↓
Generate QA Plan
      ↓
Human reviews + adjusts plan
      ↓
Execute tests locally
      ↓
Pass → mark verified 🧪→✅
Fail → New GitHub Issue → Back to Kanban
```

## Generating a QA Plan

For each recent commit, produce:

```markdown
## QA Plan — [date range]

### Commit 1: feat: add split-pane editor (closes #42)
- **What changed:** Split-pane document editing in article writer
- **Expected behavior:** Chat left, document right, edits sync in real-time
- **What could break:** Old single-pane mode, mobile responsiveness, save behavior
- **Test steps:**
  1. Open article writer → verify split pane appears
  2. Edit document → verify chat doesn't reload
  3. Resize window → verify responsive layout
  4. Save → verify both panes saved
- **Regression checks:**
  - [ ] Single-pane still works for non-document articles
  - [ ] Mobile view doesn't break
```

### Scope rules:
- **5 commits**: full plan
- **10+ commits**: group by feature, highlight cross-cutting risks
- **1-2 commits**: quick checklist, 3-5 checks each

## Execution

1. User reviews QA Plan → marks items to test
2. User tests locally, marking each ✅ or ❌
3. **Failed tests → new GitHub Issues** with:
   - Link to the QA Plan
   - Reproduction steps
   - Expected vs actual behavior
   - Severity (🔴🟡🟢)
4. New Issues enter the prd-to-issues Kanban with blocking relationships

## Reactivation pattern

```
QA Issue #50 (found in QA) → blocks original Issue #42
→ Ralph Loop picks up #50
→ commits "fix: handle mobile split-pane layout (closes #50)"
→ verified in next QA cycle
```

## When to run

- After 3-5 commits accumulate (not after every commit)
- Before merging a feature branch
- After a Ralph Loop completes a batch of issues
- Weekly: review all merged commits for regression
