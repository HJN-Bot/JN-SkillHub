---
name: write-prd
description: Turn a grilled/understood idea into a structured PRD submitted as a GitHub Issue. Use after grill-me or when the user says "write a PRD", "document this feature", "create a spec".
---

# Write PRD → GitHub Issue

Turn a clarified idea into a durable, linkable, closeable PRD — submitted as a GitHub Issue.

## The PRD Template

```markdown
# PRD: [Feature Name]

## Problem Statement
[What problem exists today. Measurable pain if possible.]

## Solution
[What we're building. Keep implementation decisions light — durable, not over-prescriptive.]

## User Stories
[List desired behaviors. Each = one user-facing capability.]

## Implementation Decisions
[Key decisions from Grill Me phase. Lightweight guidance, not a contract.]

## Major Modules
[Sketch the modules/components affected or to be built. Feeds into issue breakdown.]
```

## Process

1. Get a **long detailed description** from the user
2. **Explore the codebase** to verify assertions
3. **Grill the user relentlessly** (use grill-me skill) if not already done
4. **Sketch major modules** you'll need to build or modify
5. Write the PRD using the template above
6. **Submit as a GitHub Issue** — mark with `PRD` label

## Principles

- The PRD describes the **destination**, not the journey
- Implementation decisions should be **durable** — if the PRD goes out of date, it causes problems at implementation time
- User stories come from Agile methodology: describe desired system behavior in plain language
- If the user has preferences on format (Gherkin/cucumber), use those
