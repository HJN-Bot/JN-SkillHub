---
name: tdd-red-green-refactor
description: Test-driven development with agents — red-green-refactor cycle. Write one failing test, write minimal code to pass, refactor. Interface-first, test at module boundaries. Use as the implementation engine inside ralph-loop or for manual feature development.
---

# TDD — Red-Green-Refactor

Test-driven development optimized for AI agents. "Red green refactor with agents is incredible."

## The Cycle

```
🔴 RED:    Write ONE failing test
🟢 GREEN:  Write minimal code to make it pass
🔵 REFACTOR: Improve structure without changing behavior
→ Repeat until done
```

## Critical: Interface-First

> "When an AI looks at a bad codebase, it sees many undifferentiated tiny modules and doesn't understand relationships. With larger modules and thin interfaces, testing becomes natural."

**Before writing any test:**
1. **Confirm interface changes** with the user — these are the highest-leverage decisions
2. **Design interfaces for testability** — test at module boundaries, not internals
3. Structure codebase into **deep modules** with thin interfaces on top

## Process

1. **Confirm what interface changes are needed** with the user first
2. **Design interfaces for testability** — link to existing architecture docs
3. **Write one failing test** — RED
4. **Write minimal code** to pass — GREEN
5. **Refactor** — but clear context first (LLMs are reluctant to refactor their own code while it sits in their context window)
6. **Repeat** until all acceptance criteria met

## Anti-patterns

- Testing implementation details instead of behavior
- Writing all tests first, then all code (lose the feedback loop)
- Refactoring in the same context that wrote the code
- Testing small modules individually instead of at their boundaries
- Skipping the interface confirmation step

## Mocking & deep modules

- Mock at module boundaries, not internal dependencies
- Deep modules: complex internals, simple interfaces
- Shallow modules: simple internals, complex interfaces (refactor these away)

## When NOT to use TDD

- Exploratory prototyping (tests would slow down discovery)
- Trivial glue code with no logic
- Purely visual/CSS changes (use visual regression instead)
