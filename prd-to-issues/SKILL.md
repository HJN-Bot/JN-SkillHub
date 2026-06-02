---
name: prd-to-issues
description: Break a PRD (GitHub Issue) into independently executable vertical-slice issues with blocking relationships. Use when a PRD is ready and you need an implementation plan, or when the user says "break this down", "create the issues", "what's the plan".
---

# PRD → Issues — Vertical Slice Breakdown

Turn a PRD (the destination) into an executable Kanban (the journey). Each issue is a **thin vertical slice** through all integration layers.

## Core Principles

### Vertical slices, NOT horizontal

```
✅ Vertical: Issue = "Add split-pane editing" → touches UI + engine + state + tests
❌ Horizontal: Issue = "Database layer" → Issue = "API layer" → Issue = "UI layer"
```

### Tracer bullet prioritization

1. Identify the **riskiest unknown** (new integration, untested pattern, unclear feasibility)
2. Make that Issue #1 — flush out unknown unknowns fast
3. If it fails, you learn without wasting time on dependent work

## Output: Issues Kanban

```markdown
## 🗺️ Issues Kanban

| # | Issue | Blocks | Blocked By | Priority | Status |
|---|-------|--------|------------|----------|--------|
| 1 | Editing Engine + Tests | — | — | 🔴 | ⬜ |
| 2 | UI Layout | — | — | 🟡 | ⬜ |
| 3 | Monaco Editor Integration | 1 | — | 🟡 | ⬜ |
| 4 | Editor Toggle | 2,3 | — | 🟢 | ⬜ |

Parent PRD: closes #[PRD-Issue-Number]
```

**Blocking rules:**
- Unblocked issues = can be picked up in **parallel**
- Blocked issues = auto-unlock when dependency closes
- New issues (from QA, bugs) can be inserted with new blocking relationships

## Process

1. **Locate the PRD** — fetch it if not in context
2. **Explore codebase** if needed to understand affected modules
3. **Draft vertical slices** — each one a thin vertical cut through all layers
4. **Establish blocking relationships** between issues
5. **Present to user** for priority confirmation before any code
