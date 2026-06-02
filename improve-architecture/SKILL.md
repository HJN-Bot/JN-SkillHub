---
name: improve-architecture
description: Find and fix shallow modules in a codebase by exploring with AI's perspective, then spawning 3 parallel subagents to design independent interface proposals. Use weekly or when the user says "improve the codebase architecture", "deepen these modules", "refactor for AI readability".
---

# Improve Codebase Architecture

Make your codebase more navigable for AI agents by finding and deepening shallow modules.

## Why

AI agents struggle with codebases that have many small, undifferentiated files. When modules have unclear boundaries, the AI:
- Doesn't know what's responsible for what
- Can't figure out dependencies
- Doesn't know where to write tests

When the codebase has **deep modules** (complex internals, thin interfaces), the AI naturally knows where to test and how to navigate.

## Process

### 1. Explore — find confusions

Walk through the codebase as an AI would. Ask:

- Where does understanding one concept require **bouncing between many small files**?
- Where have **pure functions been extracted just for testability**, but the real bugs hide in how they're called?
- Where do **tightly coupled modules create integration risk** in the seams between them?

### 2. Present deepening candidates

Numbered list of opportunities to deepen shallow modules:

```
1. `src/utils/formatters.ts` + `src/utils/validators.ts` + `src/utils/parsers.ts`
   → These 3 modules are always used together. Candidate: merge into `src/formatting/` with a single public interface.
   
2. ...
```

### 3. Parallel design — spawn 3 subagents

For each approved candidate, spawn **3 independent subagents**:

```
Subagent A: Design proposal A (minimal change, preserve existing)
Subagent B: Design proposal B (aggressive refactor, deep module)
Subagent C: Design proposal C (novel approach, different abstraction)
```

Each produces:
- New module boundary and public interface
- Migration path from current to proposed
- Impact on test suite and callers

### 4. User selects — or mixes

Present all 3 proposals. User picks the strongest, or mixes across proposals. "These decisions do require taste."

### 5. Create refactor RFC (GitHub Issue)

Document the chosen design as a GitHub Issue:
- Current vs. proposed architecture
- Interface contract (public exports)
- Migration steps
- Benefit: reduced AI confusion, clearer test boundaries

## Cadence

- **Weekly**: run exploration, present 1-3 candidates
- **Per candidate**: 1-2 hours for design + review
- **Implementation**: one refactor at a time, never in bulk

## Relationship to other skills

- Runs **between** feedback-to-spec-loop cycles (not during active feature work)
- Outputs feed into TDD (better module boundaries = clearer test boundaries)
- Architecture decisions inform PRD major modules sketch
