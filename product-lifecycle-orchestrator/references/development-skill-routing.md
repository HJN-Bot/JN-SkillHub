# Development Skill Routing

Use this file on company computers to route real development work after PLO handoff.

Purpose:

- make the development stage explicit
- reduce duplicate or conflicting skill usage
- stop Copilot from skipping steps or mixing planning with execution

Default chain:

```
spec → plan → build/test → review → ship
```

Do not force every task to start from `spec`. Enter at the earliest stage that is still genuinely unresolved.

---

## 1. Discover / Define

### When to use

Use this stage when requirements, business rules, interfaces, source truth, or acceptance criteria are still unclear.

Typical triggers:

- "what exactly are we building?"
- "the API or input/output contract is not clear"
- "the business rule is ambiguous"
- "the user request is still too fuzzy to implement safely"

### Preferred skills

- `spec`
- `idea-refine`
- `source-driven-development`
- `api-and-interface-design`
- `context-engineering`

### Expected outputs

- spec
- input / output definition
- API or interface contract
- acceptance criteria
- non-goals

### Do not do

- do not start coding before the core contract is clear
- do not jump into implementation because the task "looks simple"
- do not mix architecture exploration with low-level bug fixing

---

## 2. Plan

### When to use

Use this stage when the request is clear enough, but the implementation steps, affected files, risks, or verification path are not yet decomposed.

Typical triggers:

- "we know what to build, but not how to sequence it"
- "the change touches multiple files or modules"
- "the risk is not in coding, it is in decomposition"

### Preferred skills

- `plan`
- `writing-plans`
- `planning-and-task-breakdown`
- `doubt-driven-development`

### Expected outputs

- task breakdown
- affected files or systems
- implementation sequence
- risk list
- verification plan

### Do not do

- do not turn planning into architecture drift or broad research
- do not create giant task lists with no acceptance criteria
- do not start parallel implementation before boundaries are clear

---

## 3. Build

### When to use

Use this stage when you are ready to make code changes, implement features, perform migrations, or land a planned slice.

Typical triggers:

- "start implementing"
- "make the code change"
- "apply the migration"
- "execute the next planned task"

### Preferred skills

- `build`
- `incremental-implementation`
- `executing-plans`
- `using-git-worktrees`
- `subagent-driven-development`

### Expected outputs

- small reversible code changes
- validation after each meaningful slice
- implementation notes when needed
- project changelog updates when the project process expects them

### Do not do

- do not batch large unverified edits
- do not mix unrelated refactors into the same slice
- do not widen scope before validating the first substantive edit

---

## 4. Verify / Debug

### When to use

Use this stage when behavior must be proven, a bug must be reproduced, a regression is suspected, or quality is uncertain.

Typical triggers:

- "prove it works"
- "there is a bug"
- "the result is flaky or suspicious"
- "run the tests / evals / root-cause analysis"

### Preferred skills

- `test`
- `test-driven-development`
- `verification-before-completion`
- `systematic-debugging`
- `debugging-and-error-recovery`

### Expected outputs

- test result
- eval result
- reproduction case
- root cause
- regression evidence

### Do not do

- do not claim success without executable validation
- do not patch symptoms before the bug is reproduced
- do not replace evidence with reasoning-only reassurance

---

## 5. Review

### When to use

Use this stage before PR, before merge, after important implementation, or when a significant change needs structured quality review.

Typical triggers:

- "review this change"
- "prepare for PR"
- "check risks before merge"
- "document architecture impact"

### Preferred skills

- `review`
- `requesting-code-review`
- `receiving-code-review`
- `code-review-and-quality`
- `security-and-hardening`
- `documentation-and-adrs`

### Expected outputs

- review comments
- ADR or docs when architecture changed
- risk assessment
- fix list

### Do not do

- do not collapse review into a vague summary
- do not ignore security, permissions, or regression risk on important changes
- do not skip documentation when the architecture or public contract changed

---

## 6. Ship

### When to use

Use this stage when preparing release, merge, deployment, delivery communication, or production readiness checks.

Typical triggers:

- "can this ship?"
- "prepare the PR / merge / rollout"
- "check CI/CD and release status"
- "finish the branch"

### Preferred skills

- `ship`
- `shipping-and-launch`
- `finishing-a-development-branch`
- `ci-cd-and-automation`
- `git-workflow-and-versioning`

### Expected outputs

- go / no-go decision
- release note
- CI/CD status
- migration note
- stakeholder update

### Do not do

- do not treat shipping as only a git action
- do not ignore rollback, migration, or monitoring concerns
- do not bypass review or verification just because the code already exists

---

## Practical Routing Rules

Start with two questions:

1. Is this still PLO work, or has it become real development work?
2. Inside development, which stage is actually unresolved right now?

Quick examples:

- unclear requirement -> `spec` / `idea-refine`
- unclear interface contract -> `api-and-interface-design`
- implementation sequencing needed -> `plan` / `writing-plans`
- planned feature execution -> `build` / `incremental-implementation` / `executing-plans`
- complex multi-part implementation -> `subagent-driven-development` / `dispatching-parallel-agents`
- bug or unstable behavior -> `systematic-debugging` / `test`
- before claiming done -> `verification-before-completion`
- before PR or after review feedback -> `requesting-code-review` / `review` / `receiving-code-review`
- release or merge readiness -> `ship` / `finishing-a-development-branch` / `ci-cd-and-automation`

## What Not To Do Globally

- do not let PLO micromanage every coding step
- do not use many overlapping skills at once without a clear stage owner
- do not reopen discovery once the task has already entered a verified execution slice unless validation falsifies the path
- do not skip from build straight to ship without verification and review