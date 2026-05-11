# Hermes Evolution for PLO

Use this reference after a real PLO-guided task to improve the skill package without polluting it.

## Principle

Hermes evolution is controlled improvement, not autonomous rewriting.

PLO should evolve only when real usage shows repeated gaps.

## Evolution Loop

1. Observe
- Record which PLO path was used.
- Record which reference/template was used.
- Record what output was weak or missing.

2. Detect Pattern
- 1 occurrence: record only.
- 2 occurrences: generate dry-run suggestion.
- 3 occurrences: propose a patch.

3. Patch Proposal
A patch proposal must include:
- source examples
- exact file to update
- reason for update
- expected improvement
- risk of adding complexity

4. Human Confirmation
Do not write until Jianan confirms.

5. Write + Verify
After confirmation:
- update reference/template/SKILL.md
- commit and push if repository-backed
- log the usage source and commit
- test on next real task

## Where to Patch

| Repeated Gap | Patch Target |
|---|---|
| B2B enterprise architecture confusion | `references/b2b-enterprise.md` or `references/workflow-architecture-workpackage.md` |
| Boss brief / content narrative gaps | `references/b2b-content.md` or content templates |
| ROI calculation gaps | `templates/roi-assumption.md` |
| QA / Evals gaps | `templates/evals-qa-plan.md` |
| Meeting / owner / risk gaps | `templates/b2b-enterprise-meeting-plan.md` |
| Routing confusion | `SKILL.md` |

## Quality Guardrails

Do not add a new template if:
- the pattern appeared only once;
- an existing template can handle it with a small edit;
- the new file would duplicate another reference;
- the task is too project-specific and not reusable.

Prefer:
- small reference updates;
- reusable templates;
- examples from real projects;
- concise routing instructions in `SKILL.md`.

## Evolution Record Template

Use `templates/hermes-evolution-log.md` after each meaningful PLO use.
