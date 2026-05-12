# Matt Pocock Engineering Pack inside PLO

Use this reference when PLO has routed a task into software development and Matt Pocock-style skills are available.

Core idea: this pack is not a replacement for PLO. It is a vertical execution plugin. PLO decides project type, phase, stakeholder intent, work package, quality gates, and delivery loop. The engineering pack provides narrow software protocols that prevent common coding-agent failure modes.

## Absorption Rule

Use the narrowest protocol that matches the current failure mode. Do not run a giant end-to-end ceremony by default.

| Failure mode / trigger | Protocol to invoke | PLO boundary | Minimum output |
|---|---|---|---|
| Requirement or design is fuzzy | `grill-with-docs` for repo-aware work; `grill-me` for non-code or early framing | Phase 1/2 alignment | answered decision tree, assumptions, open questions |
| Domain language is noisy or inconsistent | `grill-with-docs`, ubiquitous-language/CONTEXT pattern | Phase 1/2 shared language | canonical terms, glossary/context update, ambiguity list |
| Current conversation needs a formal product artifact | `to-prd` | Phase 2/3 work-package intent | PRD with scope, non-goals, acceptance criteria |
| Plan must become executable tickets | `to-issues` | Phase 3/4 handoff | vertical-slice issues, each independently grabbable |
| Incoming bugs/features need sorting | `triage` | Phase 4/6 project control | issue state, owner/next action, labels |
| Feature/bug is ready to implement | `tdd` | Phase 4 execution | failing test → implementation → refactor evidence |
| Behavior is broken or slow | `diagnose` | Phase 4 verify/debug | reproduction, minimal case, hypothesis, instrumentation, regression test |
| Architecture feels muddy | `improve-codebase-architecture` | Phase 2/4 architecture quality | deepening opportunities, refactor slices, risk/benefit |
| Agent is lost in a code area | `zoom-out` | Phase 2/4 context recovery | module/caller map using domain language |
| Need to test a design before committing | `prototype` | Phase 2/3/4 risk reduction | throwaway prototype answering one explicit question |
| A branch/diff needs quality check | `review` | Phase 4/5 gate | standards review + spec review + fix list |
| Context must move to another agent/session | `handoff` | Any phase transition | compact handoff with links to durable artifacts |
| Need a new repeatable workflow | `write-a-skill` | Phase 6 evolution | small composable skill, not a mega-framework |
| Communication overhead is too high | `caveman` | Any phase | compressed but accurate updates |
| Git operations are risky in Claude Code | `git-guardrails-claude-code` | Phase 4/5 safety | hooks/guardrails before destructive git operations |
| Repo needs pre-commit quality gates | `setup-pre-commit` | Phase 4/5 safety | formatting/typecheck/test hook |

## Default Software Route

If the user asks for a software feature and nothing is clearly resolved yet:

```
PLO route → grill-with-docs → to-prd → to-issues → tdd/build → diagnose if broken → review → ship → handoff/evolution log
```

Skip resolved steps. For example, if a clean PRD and issues already exist, enter directly at `tdd/build`. If a bug is already reproducible, enter at `diagnose`.

## PLO Quality Gates Imported from the Pack

1. **Shared language before speed** — prefer `CONTEXT.md`/glossary/ADR updates when terminology or decisions will recur.
2. **Vertical slices over architecture layers** — issues should be independently grabbable tracer bullets.
3. **Red-green-refactor for behavior changes** — tests describe public behavior, not implementation details.
4. **Diagnosis before patching** — reproduce and instrument before fixing hard bugs.
5. **Architecture entropy is a lifecycle risk** — run architecture review periodically, especially after fast agent-built changes.
6. **Durable artifacts over chat memory** — PRD, issues, ADRs, CONTEXT, handoff, and review notes are first-class outputs.

## Installation / Availability Check

Before relying on these names, inspect the local agent environment. If the pack is not installed, PLO should still apply the protocol semantics using available local skills (`spec`, `plan`, `build`, `test`, `review`, `ship`) rather than pretending the exact slash command exists.

If installing is appropriate, the upstream source is `mattpocock/skills`. Keep any imported or adapted material small, attributed, and reshaped to PLO's lifecycle boundaries.

## Anti-patterns

- Do not replace PLO with a coding-only workflow; PLO must still handle stakeholder, ROI, delivery, and evolution loops.
- Do not run all protocols every time; choose by trigger.
- Do not let PRD/issue generation become waterfall. Keep slices small and feedback fast.
- Do not claim completion without evidence: tests, evals, review, CI, screenshot, or explicit blocker.
