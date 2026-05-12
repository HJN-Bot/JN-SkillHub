# Architecture Lens × Matt Execution Fusion

Use this when a PLO project reaches architecture or development planning.

## Decision

Do not choose between `superpower`/`agent-skill` and Matt-style skills.

- `superpower` + `agent-skill` = Architecture Lens. They improve thinking quality: what capability matters, why this architecture is special, which agent/skill owns which subsystem, and what tradeoffs exist.
- Matt-style skills = Execution Chain. They improve shipping quality: clarify requirements, write PRD, split issues, TDD, diagnose, review, ship, and handoff.

## Default Sequence

```text
PLO route
→ Architecture Lens
   - unique capability / leverage point
   - capability package map
   - owner → agent/skill map
   - key tradeoffs and constraints
→ Matt-style Execution Chain
   - grill-with-docs
   - prototype if uncertainty remains
   - to-prd
   - to-issues
   - tdd/build
   - diagnose if broken
   - improve-codebase-architecture / zoom-out if architecture drifts
   - review
   - ship
   - handoff
```

## Why This Fusion Works

| Risk | Architecture Lens handles | Matt Execution handles |
|---|---|---|
| Building the wrong system | capability and stakeholder fit | grill / PRD acceptance |
| Shallow architecture | superpower / capability packages | architecture improvement |
| Confused ownership | agent-skill ownership map | issue owner / handoff |
| Analysis paralysis | time-boxed lens only | issues, tests, ship |
| Vibe coding | design before code | TDD, diagnose, review |

## Hit-rate Rule

- If user asks broad project/product/system questions → PLO triggers, then Architecture Lens may apply.
- If user asks concrete coding/debug/review/shipping questions → Matt-style atomic skill should trigger directly.
- If both apply, start with the smallest Architecture Lens pass, then move quickly to Matt execution.

## Quality Gates

Before coding:
- unique capability is named;
- capability package and owner map exist;
- acceptance criteria are known;
- vertical issue slices are defined or intentionally skipped;
- test/eval route is known.

Before completion:
- tests/evals/review evidence exists;
- architecture drift is checked if the change was broad;
- handoff or durable artifact exists for long-running work.
