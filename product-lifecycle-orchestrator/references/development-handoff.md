# Development Handoff Reference

Use this when PLO has finished product/project planning and the work is ready to become concrete implementation.

## Core Boundary

PLO is the lifecycle and product/project entry point. It should not pretend to be the full engineering delivery workflow.

PLO owns:
- stakeholder and user needs;
- product scope and priority;
- workflow → architecture → work package mapping;
- ROI assumptions;
- Evals/QA plan;
- delivery and stakeholder communication plan.

Development workflow owns:
- implementation specifications;
- technical task planning;
- code changes;
- tests/evals execution;
- review;
- release/ship.

## Important Machine-Specific Rule

Do not assume every methodology named in PLO is installed as a local skill.

Use the two-lane fusion consistently: `superpower` / `agent-skill` are Architecture Lens references for capability thinking and agent/skill ownership mapping; Matt-style atomic skills are the execution route for PRD, issues, TDD, diagnosis, review, ship, and handoff. If exact Matt-style skills are unavailable, preserve the same execution semantics with local `spec → plan → build/test → review → ship`.

When working on a concrete machine, first inspect local available skills and route to what actually exists.

If the company computer has slash workflow skills, prefer:

`spec → plan → build/test → review → ship`

with `claw-vibe-project` for long-running project governance.

## Phase Boundary

- PLO Phase 1/2: determine what to build and why
- PLO Phase 3: convert the work into workflow / architecture / work package views
- PLO Phase 4/5: define quality gates and delivery expectations, but do not micromanage implementation
- Code development: route into the development-stage skill chain

## Handoff Decision Tree

### 1. Requirements are still unclear
Use:
- PLO B2B Enterprise / AI Product Manager lane;
- then `spec` if available.

Output before coding:
- user story / requirement;
- inputs and outputs;
- acceptance criteria;
- non-goals;
- risks.

### 2. Requirements are clear but architecture / ownership / implementation plan is unclear
Use:
- PLO Product Architect lane for architecture/work packages;
- Architecture Lens: identify unique capability (`superpower` concept), capability packages, and agent/skill ownership (`agent-skill` concept);
- then Matt-style execution planning: `grill-with-docs`, `prototype` if uncertain, `to-prd` / `to-issues`, or local `plan`.

Output before coding:
- unique capability / leverage point;
- owner → capability map;
- affected files/modules;
- vertical slice implementation steps;
- test/eval strategy;
- rollback/risk notes.

### 3. Long-running project or repo-level development
Use:
- `claw-vibe-project` if available.

It owns:
- project context;
- session handoff;
- changelog/audit trail;
- harness constraints;
- evals reuse;
- architecture drift checks.

### 4. Concrete code implementation
Use local implementation workflow:
- `build` for implementation;
- `test` or `test-driven-development` for behavior changes or bug fixes;
- `incremental-implementation` for small safe slices;
- `review` for code/architecture/quality review;
- `ship` for release go/no-go.

### 5. CER/LEFA repo-specific implementation
If the repo defines a CER/LEFA workflow, follow it after PLO handoff.

Typical CER/LEFA implementation areas:
- Stage0–Stage4 pipeline;
- extraction;
- alignment;
- whitelist;
- eval;
- report generation;
- server/UI integration.

PLO should provide the product/architecture/evals intent, then the repo workflow should govern exact implementation.

## Recommended Chain

For CER/PTR planning:

`PLO → b2b-enterprise reference → workflow/architecture/workpackage reference → ROI/Evals templates`

For CER/PTR development:

`PLO Architecture Lens (capability + owner map) → grill-with-docs → to-prd/to-issues or spec/plan → tdd/test/build → diagnose if needed → review → ship → handoff`

For CER/LEFA implementation:

`PLO planning → CER LEFA workflow → spec/plan/build/test/review/ship`

## Which Reference To Load Next

After handoff, load:

- `references/development-skill-routing.md`

That file defines:

- development stages
- trigger situations
- preferred skills
- expected outputs
- anti-patterns for each stage

## Handoff Checklist

Before leaving PLO and entering development, ensure:

- [ ] problem / feature is clear;
- [ ] stakeholder/user need is known;
- [ ] scope and non-goals are defined;
- [ ] work package is identified;
- [ ] input/output expectations are clear;
- [ ] Evals/QA requirements are known;
- [ ] owner and review owner are assigned;
- [ ] target repo/workflow is selected;
- [ ] local available dev skills are checked.

## Development Skill Mapping

| Need | Preferred Local Skill / Workflow |
|---|---|
| Long-running project governance | `claw-vibe-project` |
| Requirement/spec clarification | `spec` |
| Implementation planning | `plan` |
| Small safe implementation slices | `incremental-implementation` |
| Code implementation | `build` |
| TDD / prove behavior | `test` or `test-driven-development` |
| Quality / architecture review | `review` |
| Release / go-no-go | `ship` |

## When to Create `engineering-delivery-orchestrator`

Do not create it immediately if the local machine already has `spec/plan/build/test/review/ship`.

Create a new orchestrator only if repeated real usage shows:
- users keep asking for one development entry point;
- agents forget the handoff chain;
- repo workflows diverge too much;
- development tasks repeatedly skip tests/review/ship.

Until then, use this reference as the PLO → development handoff contract.
