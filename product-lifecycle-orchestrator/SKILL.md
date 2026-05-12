---
name: product-lifecycle-orchestrator
description: Full-cycle product lifecycle orchestrator (PLO). Use as the single entry point for T2+ product, design, content, automation, and release work. Detects mode (B2B Enterprise Automation vs B2B Content/Influence vs ToC Consumer vs Personal/Internal), routes to the correct lifecycle path, maps phases to role-lanes and skills, enforces quality gates, and records evolution hooks.
aliases: [PLO, product-lifecycle, lifecycle-orchestrator]
---

# Product Lifecycle Orchestrator (PLO)

SAM reads this skill to route every project through the correct development lifecycle.

---

## Scope & Execution Notes

### Use PLO for

Use this skill for T2+ work that needs lifecycle thinking, stakeholder alignment, product/design decisions, architecture, delivery, or reusable assets:

- **B2B Enterprise Automation**: CER/PTR, internal AI workflow, document automation, compliance/quality systems, cross-team platform work.
- **B2B Content / Influence**: boss brief, executive update, whitepaper, case study, internal sharing, methodology article, playbook, Feishu wiki.
- **ToC Consumer Products**: apps, user-facing tools, activation/retention/trust/UX-heavy products.
- **Personal / Internal Tools**: personal automation, internal utilities, prototypes, sharing pages, experiments.

### Do not use PLO for

Skip or only lightly reference PLO for:

- T0/T1 simple asks that can be answered directly.
- One-off edits with no product/project lifecycle.
- Pure implementation tasks where architecture, stakeholder, delivery, and reuse are already clear.
- Sensitive external writes unless the user confirms.

### Execution Rules

1. **Start with routing**
   - First identify: B2B Enterprise / B2B Content / ToC / Personal.
   - Then identify phase and role lane.

2. **Load references only when needed**
   - Keep `SKILL.md` as the entry router.
   - Load only the relevant `references/*` and `templates/*` for the task.
   - Do not load every file by default.

3. **Keep two views separate**
   - Vertical progress view: who does what in the next 1–2 weeks.
   - Horizontal capability package view: what product/system capabilities need to exist.

4. **Prefer templates for execution**
   - If the user has meeting notes, roadmap, Gantt, or feature tasks, convert them through templates instead of free-form rewriting.

5. **Enterprise AI requires quality gates**
   - For CER/PTR-like work, always consider Evals/QA, SME review, user acceptance, and traceability.

6. **Use Hermes evolution after real use**
   - After meaningful PLO usage, fill `templates/hermes-evolution-log.md`.
   - Record gaps; do not patch skill immediately from a single occurrence.

### Company Computer / Copilot Global Use

If using Copilot or another coding agent on a company computer:

1. Pull or copy the full folder:
   `product-lifecycle-orchestrator/`

2. Put it where the agent can access global/project skills, for example:
   - global skills folder, if supported;
   - project `.github/copilot-instructions.md` references;
   - project docs / prompt library;
   - local agent workspace skills folder.

3. Use this instruction when starting a task:

   “Use `product-lifecycle-orchestrator` as the entry skill. First route this task by project type and phase. Load only the relevant references/templates. For CER/PTR, prioritize B2B Enterprise, workflow→architecture→work package mapping, ROI, Evals/QA, and Hermes evolution logging.”

   Short development routing sentence:

   “If this has become real development work rather than project framing, identify the current stage first: discover/define, plan, build, verify/debug, review, or ship; then load `references/development-handoff.md` and `references/development-skill-routing.md` and use the narrowest matching skills.”

4. For CER/PTR, start with these files:
   - `SKILL.md`
   - `references/b2b-enterprise.md`
   - `references/development-handoff.md`
   - `references/development-skill-routing.md`
   - `references/workflow-architecture-workpackage.md`
   - `templates/b2b-enterprise-meeting-plan.md`
   - `templates/feature-roadmap-to-capability-package.md`
   - `templates/roi-assumption.md`
   - `templates/evals-qa-plan.md`
   - `templates/hermes-evolution-log.md`

5. After each substantial use, write one evolution log entry. This lets Hermes-style self-improvement accumulate without polluting the skill package.


## Pre-flight: Mode Detection

Before entering any phase, determine the mode. PLO is the single input interface; paths are routed internally.

### Step 1 — Main Mode

| Question | B2B Answer | ToC Answer | Personal Answer |
|----------|------------|------------|-----------------|
| Who makes the decisions? | Client, boss, customer, partner, internal stakeholder | End users / market behavior | I make all decisions |
| Where does key information live? | Internal docs, meetings, stakeholder conversations, enterprise constraints | User behavior, onboarding, retention, reviews | Public tools, my own experimentation |
| What is the dominant risk? | Misalignment, veto, compliance, ROI, resource conflict | Activation, trust, emotion, habit, conversion | Scope creep, taste drift, maintenance burden |

**If ≥2 B2B answers → B2B. If ≥2 ToC answers → ToC. Otherwise → Personal/Internal.**

### Step 2 — B2B Sub-mode

If B2B, choose the sub-mode:

| Question | Enterprise Automation | Content / Influence |
|----------|----------------------|---------------------|
| Primary deliverable | Working system, workflow, automation, AI tool, integration | Decision/influence artifact: deck, brief, memo, whitepaper, case study, playbook |
| Success metric | Quality, cycle time, ROI, compliance, adoption by team | Stakeholder understanding, decision, buy-in, influence, reusable narrative |
| Dominant risk | Wrong output, data loss, quality regression, delivery failure | Weak audience fit, weak proof, unclear ask, no follow-up action |

**System/process deliverable → B2B Enterprise Automation. Decision/influence artifact → B2B Content/Influence.**

Plus: use `web_search` or other verified research only when market/category/external framework context is needed; save useful references into the relevant skill/reference file.

---

## Project Archetypes & Quality Emphasis

Different project types demand different quality focus. PLO adjusts gate strictness per archetype:

| Archetype | Example | Path | Dominant Risk | Quality Emphasis |
|-----------|---------|------|---------------|-----------------|
| **Enterprise Automation** | CER / PTR automation | B2B Enterprise | Data loss, wrong output, compliance, resource conflict | Evals ⬆⬆⬆, TDD ⬆⬆⬆, Audit trail, SME review, ROI |
| **ToB SaaS/Tool** | Client/internal platform | B2B Enterprise | Misalignment, scope creep | Stakeholder checkpoints, Constraint docs, RACI/RAID |
| **B2B Content / Influence** | boss brief, whitepaper, internal sharing, case study, playbook | B2B Content | Weak audience/action fit, insufficient proof, no decision | Audience fit, narrative clarity, evidence, review loop, impact follow-up |
| **ToC Product** | Consumer app | ToC | No adoption, bad UX | Product-sense-review ⬆⬆⬆, Activation metrics, Market positioning |
| **Internal Sharing** | Team slide deck, PPT | Personal | Low quality, off-brand | Aesthetic ⬆⬆⬆, Speed, Presentation polish |
| **Personal Tool** | CLI, automation | Personal | Abandonment, over-engineering | Speed, MVP scope, Taste drift check |

---

## Path A: B2B / Stakeholder-Driven

```
Phase 1 → Phase 2 → Phase 3 → Phase 4 → Phase 5 → Phase 6
```

## B2B Operating Layer: Role Lanes

B2B work needs explicit role-lane routing. These lanes can run inside any B2B phase.

| Lane | Use When | Core Question | Minimum Output |
|------|----------|---------------|----------------|
| **AI Product Manager** | User needs, pain points, priority, ROI, acceptance | What pain/job should this AI/product solve? | user needs, pain→feature map, priority, acceptance criteria, ROI assumptions |
| **AI Product Architect** | Workflow, architecture, Agent/LLM design, reuse, work packages | How should the product/system be structured? | workflow map, architecture map, work package map, evals/reuse design |
| **Project Execution Manager** | Resources, meetings, owners, timeline, risk, boss decisions | How will this become executable? | RACI, RAID, meeting plan, two-week plan, decision list |

**Do not confuse the maps:** Workflow Map = how users/business work; Architecture Map = system layers and design logic; Work Package Map = executable deliverables for the team. Development packages should usually be vertical capability slices that cut across layers, not pure architecture layers.

Common B2B AI work packages: Input/Ingestion, Parsing & Mapping, Generation, Verification/Evals, Review & Usability, Transfer/Reuse, Platform/Audit/Permissions.

For detailed enterprise templates and CER/PTR examples, read `references/b2b-enterprise.md`. For meeting/RACI/RAID planning, use `templates/b2b-enterprise-meeting-plan.md`.

When the user provides a feature roadmap, Gantt chart, or vertical task list, read `references/workflow-architecture-workpackage.md` and use `templates/feature-roadmap-to-capability-package.md` to convert it into capability packages.

When the request is a boss brief, executive update, internal sharing, whitepaper, case study, playbook, or stakeholder narrative, read `references/b2b-content.md` and choose the matching template (`templates/boss-brief.md`, `templates/case-study.md`, or `templates/internal-sharing.md`). If the asset is a video, social cover, AI-generated visual, product/system promo, or image-to-video task, use `ai-video-production-pack` as the Asset Production skill pack.

When ROI, saving, transfer effort, or BA/User validation is needed, use `templates/roi-assumption.md`.

When quality, regression, SME review, or user acceptance is needed, use `templates/evals-qa-plan.md`.

After meaningful PLO usage, use `references/hermes-evolution.md` and `templates/hermes-evolution-log.md` to record gaps and decide whether to propose a controlled patch.

For lightweight monitoring of real-world skill effectiveness, use `references/skill-usage-monitoring.md` and `templates/skill-usage-monitoring-log.md`. This records usage, Jianan feedback, scores, repeated gaps, and active project maintenance items.

When PLO planning becomes concrete implementation, read `references/development-handoff.md` to decide whether to hand off to `claw-vibe-project`, `spec`, `plan`, `build`, `test`, `review`, `ship`, or a repo-specific workflow such as CER/LEFA.

When the task is software development and the agent has Matt Pocock-style skills available, read `references/matt-pocock-engineering-pack.md`. Treat it as a vertical engineering plugin inside PLO: PLO owns lifecycle routing and work-package intent; the engineering pack owns narrow execution protocols such as grill, PRD, issue slicing, TDD, diagnosis, architecture improvement, review, prototype, and handoff.


### Phase 1: Stakeholder & Constraint
**Goal:** Understand who cares, what they want, and what constraints exist (both stated and implicit).
**When to exit:** You can state the 3 key stakeholders, their 1 top need each, the non-negotiable constraints, AND a written list of budget, timeline, tech requirements, compliance/security needs, integration points.

| Skill | What It Does |
|-------|-------------|
| `grill-me` | Probe stakeholder assumptions, surface hidden constraints, resolve conflicting requirements |
| `web_search` | Background research on stakeholder organization, industry, regulatory context |
| Internal docs | Read existing specs, contracts, email threads for implicit constraints |

### Phase 2: Technical Architecture
**Goal:** Design the system, choose the stack, decompose into capability/work packages, and decide which execution protocol should deliver each package.
**When to exit:** Architecture diagram exists, capability packages are named, agent/skill ownership is mapped, work packages are vertical slices where possible, quality gates are defined, and the PLO → engineering handoff route is clear.

Use a **two-lane fusion**:

1. **Architecture Lens (quality of thinking)** — use `superpower` / `agent-skill` concepts lightly to identify the system's unique capability, capability packages, agent/skill ownership, and architectural tradeoffs.
2. **Matt-style Execution Chain (quality of shipping)** — immediately convert the architecture intent into concrete artifacts and feedback loops: `grill-with-docs → prototype/to-prd → to-issues → tdd/build → diagnose → review → ship → handoff`.

Do not choose between the two. The Architecture Lens prevents shallow or mis-scoped design; the Matt-style chain prevents analysis from stalling before tests, issues, review, and shipping.

| Lane | Skill / Protocol | What It Does | Minimum Output |
|-------|-------------|-------------|-------------|
| Architecture Lens | `superpower` (concept) | Identify what capability makes this system special vs a normal implementation | unique capability / leverage point |
| Architecture Lens | `agent-skill` (concept) | Map which agent/skill owns which capability or subsystem | owner → capability map |
| Architecture Lens | `web_search` / external docs | Research patterns, APIs, benchmarks, constraints | cited decision notes |
| Architecture Lens | `context7-cli` / `get-api-docs` | Pull integration/API docs | verified API constraints |
| Architecture Lens | `codebase-to-course` / `zoom-out` | Understand existing codebase/module context | module/caller map |
| Execution Chain | `grill-with-docs` | Stress-test architecture assumptions against domain language and ADRs | resolved assumptions / open questions |
| Execution Chain | `prototype` | Probe uncertain state model, API shape, or UI direction | throwaway proof / decision |
| Execution Chain | `to-prd` | Convert resolved architecture/product intent into a PRD | PRD with scope/non-goals/acceptance |
| Execution Chain | `to-issues` | Break work into vertical implementation slices | independently grabbable issues |
| Execution Chain | `tdd` / local `test` | Build behavior through red-green-refactor | test evidence |
| Execution Chain | `diagnose` | Reproduce and fix bugs/regressions | root cause + regression test |
| Execution Chain | `improve-codebase-architecture` | Identify deepening opportunities when the codebase gets muddy | refactor slices |
| Execution Chain | `review` / `ship` | Verify standards/spec and release readiness | go/no-go + evidence |
| Governance | `claw-vibe-project` / MAE pipeline | Long-running project context and multi-agent execution | durable state / task split |

For detailed handoff rules, read `references/development-handoff.md`. For Matt-style stage mapping, read `references/development-skill-routing.md` and `references/matt-pocock-engineering-pack.md`. For the combined logic, read `references/architecture-execution-fusion.md`.

### Phase 3: Design & UX
**Goal:** Visual language, interaction patterns, motion design.
**When to exit:** Design system is defined (colors, fonts, spacing), key screens are designed, product-sense review passed.

| Skill | What It Does |
|-------|-------------|
| `grill-me` | Aesthetic direction exploration (choose extreme tone before converging) |
| `product-sense-review` | Product personality, UX risk, launch blocker, and user psychology review |
| **Output-type skill matrix:** | |
| Web / Landing page | `open-design` (React + Tailwind) |
| Slide deck | `frontend-slides` (scroll-snap HTML pages) |
| PPT / Roadshow / Pitch | `jianan-presentation-system` |
| UI components | `design-front` |
| High-end visual design | `impeccable-design` |
| Architecture diagrams | `excalidraw-handnote-style` |

### Phase 4: Development
**Goal:** Build, test, review, iterate.
**When to exit:** Code passes all quality gates. Gates are stricter for enterprise projects.

Do not treat PLO as the step-by-step development executor. PLO defines the work package, quality gates, and delivery expectations, then hands off execution to the development-stage skill chain. On company computers, use `references/development-handoff.md` for the boundary, `references/development-skill-routing.md` for stage routing, and `references/matt-pocock-engineering-pack.md` when Matt Pocock-style engineering skills are available.

| Skill | What It Does |
|-------|-------------|
| `coding-agent` | Code generation and iteration |
| `grill-with-docs` / `grill-me` | Resolve ambiguity before implementation; capture shared language and decisions |
| `to-prd` / `to-issues` | Convert resolved intent into PRD and vertical implementation issues |
| `prototype` | Build a throwaway probe when architecture, state model, or UI direction is uncertain |
| `tdd` / `test-driven-development` | Write tests before implementation; enforce red-green-refactor discipline |
| `diagnose` | Reproduce → minimise → hypothesise → instrument → fix → regression-test for bugs/perf regressions |
| `improve-codebase-architecture` / `zoom-out` | Reduce architecture entropy; understand module context before refactor |
| `subagent-driven-development` | Staged multi-subagent implementation for complex features |
| `review` / `github-pr` | PR workflow, two-axis review, and merge management |
| MAE pipeline | Multi-step code → test → review → fix workflows |

**Quality Gates (NON-NEGOTIABLE):**

| Gate | Enterprise (CER-type) | Standard B2B |
|------|----------------------|-------------|
| **TDD** | Tests before every function. ≥90% coverage target. Integration tests for all external APIs. | Tests before implementation. Core paths covered. |
| **Evals** | LLM-as-judge on every output batch. Score ≥ 0.85. Trace replay for regression. | LLM-as-judge on critical outputs. Score ≥ 0.75. |
| **Code Review** | Duplication, security, permissions, error handling, audit trail, data integrity. | Duplication, security, permissions, error handling. |
| **Type Safety** | mypy/pyright strict mode in CI. | mypy/pyright passes in CI. |
| **CI/CD** | GitHub Actions: push → test → evals → review → merge. Block merge on any failure. | GitHub Actions: push → test → review → merge. |

Preferred execution chain after PLO handoff:

```
spec → plan → build/test → review → ship
```

### Phase 5: Delivery & Deploy
**Goal:** Deploy, verify, document, notify stakeholders.
**When to exit:** Deliverable is live and smoke-tested, stakeholders are notified, documentation exists.

#### Step 1: Choose Deploy Target

| Target | Best For | Pattern |
|--------|----------|---------|
| **Vercel** | Frontend apps (React/Next.js), landing pages, slide decks | `vercel --prod` or GitHub integration auto-deploy |
| **Supabase** | Backend (DB + Auth + Edge Functions), API services | `supabase db push` + Edge Function deploy |
| **npm** | CLI tools, libraries, local packages | `npm publish` or `npm link` for local dev |

#### Step 2: Data Storage Strategy

| Storage Need | Solution | When to Use |
|-------------|----------|-------------|
| Relational data | Supabase (PostgreSQL) | Structured app data, user accounts, audit trails |
| File/blob storage | Supabase Storage | Uploads, generated assets, media |
| Key-value / cache | Supabase KV / Redis | Session state, rate limiting, temp data |
| Local-only | SQLite / JSON files | Personal tools, offline-first, no server needed |
| Audit trail | Supabase DB + timestamp columns | CER-type enterprise: every state change logged |

#### Step 3: Deploy & Verify

```
1. DEPLOY: Push to target (Vercel auto-deploy / supabase db push / npm publish)
2. SMOKE TEST: Hit key endpoints/pages, verify they return 200 + expected content
3. DATA CHECK: Confirm DB migrations applied, storage buckets accessible
4. ENV CHECK: Verify environment variables loaded correctly on deployed instance
5. STAKEHOLDER NOTIFY: Send Feishu/Discord notification with live URL + changelog
```

| Skill | What It Does |
|-------|-------------|
| `github` | Release management, tag, changelog, trigger CI deploy |
| `feishu-write-shared` | Write deployment docs to Feishu Wiki |
| `airtable-dashboard` | Sync task status to Dashboard |
| `feishu-agent-workflow` | Route deliverables to correct Feishu space |
| Deployment verification | Smoke-test, data check, env check → confirm live |

### Phase 6: Review & Evolve
**Goal:** Extract lessons, update skills, close the loop.
**When to exit:** Retrospective written, skills updated, task ledger closed.

| Skill | What It Does |
|-------|-------------|
| `eight-d-optimization` | Structured 8D review (what went wrong, root cause, fix) |
| `interaction-self-reflection` | Review human-agent interactions for improvement |
| `skill-creator` | Update existing skills or create new ones from lessons |

**Evolution Actions:**
- Rate each skill used in this project (1-5). Log to skill's SKILL.md metadata.
- If score ≤2 for ≥3 uses → trigger search for replacement.
- If score ≥4 for ≥3 uses → promote to recommended list.

---

## Path A2: B2B Content / Influence

Use this path when the primary deliverable is not a working system but a stakeholder-facing artifact: boss brief, executive update, internal sharing, methodology article, whitepaper, case study, sales/customer enablement, playbook, or Feishu wiki.

```
Phase 1 → Phase 2 → Phase 3 → Phase 4 → Phase 5 → Phase 6
```

### Phase 1: Audience & Objective
**Goal:** Know who the artifact is for and what action/decision it should trigger.
**When to exit:** Primary audience, stakeholder level, desired decision/action, and constraints are written.

Outputs: audience map, communication objective, decision/action target, constraints.

### Phase 2: Message & Evidence
**Goal:** Define the one-line thesis and proof.
**When to exit:** Core thesis, evidence library, data points, counterarguments, and answer logic exist.

Outputs: thesis, proof points, evidence table, objection/answer list.

### Phase 3: Narrative Architecture
**Goal:** Choose the structure that fits the audience and decision.
**When to exit:** Narrative arc, section outline, message hierarchy, and each section's job are clear.

Common structures: problem→solution→ask, fact→gap→decision, before→after→ROI, case→method→reuse, risk→mitigation→resource.

### Phase 4: Asset Production
**Goal:** Produce the artifact in the right format.
**When to exit:** Draft artifact exists: deck, memo, one-pager, article, wiki, playbook, or case study.

Recommended skills: `jianan-presentation-system`, `frontend-slides`, `impeccable-design`, `excalidraw-handnote-style`, writing/content skills.

### Phase 5: Review & Stakeholder Fit
**Goal:** Make the artifact decision-ready.
**When to exit:** Accuracy, evidence, tone, stakeholder fit, and actionability are reviewed.

Review gates: audience fit, one-line message clarity, evidence strength, objection handling, next-action clarity.

### Phase 6: Delivery & Impact Loop
**Goal:** Deliver, capture feedback, and convert learning into reusable assets.
**When to exit:** Artifact delivered, feedback captured, follow-up action recorded, reusable pattern/template identified.

Outputs: delivery note, feedback summary, follow-up task, template/skill evolution note.

---

## Path B: ToC / Consumer

```
Phase 1 → Phase 2 → Phase 3 → Phase 4 → Phase 5 → Phase 6 → Phase 7
```

### Phase 1: User Pull & Emotional Job
**Goal:** Identify the user moment, motivation, and emotional promise.
**When to exit:** You can state the target user, trigger moment, desired transformation, and what the product must never make them feel.

| Skill | What It Does |
|-------|-------------|
| `grill-me` | Probe user psychology, emotional risk, and promise clarity |
| `product-sense-review` | Catch positioning/personality mismatch early |
| `web_search` | Inspect analogous consumer products and review patterns |
| `gbrain` | Monitor GitHub trending for similar consumer tools |

### Phase 2: Activation Loop & Trust Boundary
**Goal:** Define the smallest loop that creates value and earns trust.
**When to exit:** First-session success, privacy/trust boundary, return trigger, and failure fallback are written.

| Skill | What It Does |
|-------|-------------|
| `grill-me` | Force clear answers on activation, retention, and stop conditions |
| `product-sense-review` | Review whether onboarding, feedback, and result screens reduce anxiety and increase next action |

### Phase 3: Technical Architecture
Same as Path A Phase 2: use the Architecture Lens (`superpower` / `agent-skill` concepts) for capability and ownership mapping, then route concrete execution through Matt-style atomic skills (`prototype`, `grill-with-docs`, `to-prd`, `to-issues`, `tdd`, `diagnose`, `review`) or local `spec → plan → build/test → review → ship`.

### Phase 4: Design & UX
Same skill matrix as Path A Phase 3, with ToC additions:

| Extra ToC Gate | What It Does |
|----------------|-------------|
| `grill-me` (user path) | Simulate the first-time user's emotional and cognitive journey through key screens |
| `product-sense-review` | **MANDATORY** before launch — review personality, trust signals, activation friction |
| `web_search` | Pull UX patterns from top consumer apps in the same category |

### Phase 5: Development
Same as Path A Phase 4, with ToC emphasis:

| Quality Gate | ToC Emphasis |
|-------------|-------------|
| TDD | Core user flows covered; edge cases for activation/first-run |
| Evals | UX copy, error messages, onboarding text quality |
| Code Review | Privacy, permissions, data minimization |

### Phase 6: Delivery & Deploy
Same as Path A Phase 5. ToC additions:

| Extra ToC Step | What It Does |
|----------------|-------------|
| Activation smoke test | Walk through first-run experience as new user |
| Analytics hook | Confirm event tracking fires for key activation events |
| Market positioning check | Final `product-sense-review` against live product |

### Phase 7: Review & Evolve
Same as Path A Phase 6. Extra: review activation/retention metrics if available.

---

## Path C: Personal / Self-Driven

```
Phase 1 → Phase 2 → Phase 3 → Phase 4 → Phase 5 → Phase 6 → Phase 7
```

### Phase 1: Feature Fusion
**Goal:** Survey existing products/tools. Extract the best features from each. Synthesize.
**When to exit:** You have a feature fusion map: Product X's {feature} + Product Y's {UX pattern} + Product Z's {performance}.

| Skill | What It Does |
|-------|-------------|
| `gbrain` | Monitor GitHub trending for similar tools |
| `web_search` | Find and analyze competing/adjacent products |
| `grill-me` | "What makes this product feel good? What specific interaction would I steal?" |

### Phase 2: Scope Definition
**Goal:** Define what to build and what NOT to build.
**When to exit:** Written scope: MVP features, out-of-scope features, success criteria.

| Skill | What It Does |
|-------|-------------|
| `grill-me` | "What's the smallest useful version? What's tempting but unnecessary?" |

### Phase 3: Technical Architecture
Same as Path A Phase 2: use the Architecture Lens (`superpower` / `agent-skill` concepts) for capability and ownership mapping, then route concrete execution through Matt-style atomic skills (`prototype`, `grill-with-docs`, `to-prd`, `to-issues`, `tdd`, `diagnose`, `review`) or local `spec → plan → build/test → review → ship`.

### Phase 4: Design & UX
Same skill matrix as Path A Phase 3. Personal emphasis:

| Personal Emphasis | What It Means |
|-------------------|---------------|
| **Aesthetic quality** | For internal sharing / presentation: `impeccable-design` or `jianan-presentation-system` strongly recommended |
| **Speed over polish** | For quick tools: `design-front` minimum viable, skip full design system |
| **Taste drift check** | `grill-me`: "Am I building this because it's cool or because I need it?" |

### Phase 5: Development
Same as Path A Phase 4, with personal emphasis:

| Quality Gate | Personal Emphasis |
|-------------|-------------------|
| TDD | Core logic tested; UI/visual can be manual |
| Evals | Only if output is customer-facing or data-critical |
| Code Review | Self-review OK; focus on maintainability for future-you |

### Phase 6: Delivery & Deploy
Same as Path A Phase 5. Personal emphasis:

| Deploy Target | Personal Use |
|--------------|-------------|
| Vercel | Internal sharing pages, slide decks, personal sites |
| Supabase | Personal tools with persistence |
| npm / local | CLI tools, scripts, `npm link` for local use |
| No deploy | If it's a one-off script or local-only tool, skip deployment |

### Phase 7: Review & Evolve
Same as Path A Phase 6. Extra: personal projects should log "would I use this again?" as a lightweight metric.

---

## Phase Summary (All Paths)

| Phase | B2B Enterprise Automation | B2B Content / Influence | ToC | Personal |
|-------|---------------------------|--------------------------|-----|----------|
| 1 | Stakeholder & Constraint | Audience & Objective | User Pull & Emotional Job | Feature Fusion |
| 2 | Pain → AI Feature / Architecture | Message & Evidence | Activation & Trust | Scope Definition |
| 3 | Product Architecture / Work Packages | Narrative Architecture | Architecture Lens + Matt-style engineering route | Architecture Lens + lightweight prototype/build route |
| 4 | Development / Execution Planning | Asset Production | Design & UX (+ToC gates) | Design & UX (Aesthetic emphasis) |
| 5 | Delivery & Quality Gates | Review & Stakeholder Fit | Development (ToC emphasis) | Development (Speed emphasis) |
| 6 | Review & Evolve | Delivery & Impact Loop | Delivery & Deploy (+activation check) | Delivery & Deploy (Lightweight) |
| 7 | — | — | Review & Evolve | Review & Evolve |

> PLO remains one input interface. B2B splits internally into Enterprise Automation and Content/Influence. ToC and Personal use full 7 phases. All paths share architecture, delivery, and skill-evolution principles but apply different gates.

---

## Delivery & Deploy Reference (Shared)

All paths use this deployment strategy. Pick the right target(s) for the project:

### Vercel (Frontend)
```
Best for: React/Next.js apps, landing pages, slide decks, internal sharing pages
Pattern: Push to GitHub → Vercel auto-deploy, or `vercel --prod`
Verify: Open live URL, check key pages/API routes return 200
```

### Supabase (Backend + Data)
```
Best for: Database, auth, edge functions, file storage, API backend
Pattern: `supabase db push` for schema, Edge Function deploy for APIs
Data: PostgreSQL (structured data), Storage (files/blobs), Auth (user management)
Verify: Query a known table, hit an edge function endpoint, check storage bucket
```

### npm (CLI / Library)
```
Best for: CLI tools, shared libraries, local packages
Pattern: `npm publish` for distribution, `npm link` for local dev
Verify: `npx <package>` or import from linked package, run key commands
```

### Deployment Verification Checklist
```
☐ Deploy command completed without errors
☐ Smoke test: key pages/endpoints return 200
☐ Data check: DB schema applied, storage accessible
☐ ENV check: environment variables loaded (no undefined/missing)
☐ Auth check: login/signup flow works (if applicable)
☐ Stakeholder/channel notification sent with live URL
```

---

## Data Storage Decision Tree

```
Does this project need persistent data?
  ├─ No → Skip storage, use in-memory or local files
  └─ Yes → What kind?
       ├─ Relational (users, tasks, structured records)
       │   └─ Supabase PostgreSQL
       ├─ Files / media (uploads, generated assets)
       │   └─ Supabase Storage
       ├─ Key-value / cache (sessions, rate limits, temp state)
       │   └─ Supabase KV or in-memory Redis
       ├─ Audit trail (CER-type: every state change logged)
       │   └─ Supabase DB + created_at/updated_at/actor columns
       └─ Local-only (personal tools, no server)
           └─ SQLite or JSON files
```

---

## Attention Tracking

Every task created should have a `Phase` field with one of these values:

| Phase | Tag |
|-------|-----|
| Mode Detection (pre-flight) | `mode-detect` |
| Phase 1 (discovery) | `phase-1` |
| Phase 2 (constraint / activation / architecture) | `phase-2` |
| Phase 3 (architecture / design) | `phase-3` |
| Phase 4 (design / development) | `phase-4` |
| Phase 5 (development / delivery) | `phase-5` |
| Phase 6 (delivery / review) | `phase-6` |
| Phase 7 (review) | `phase-7` |

**Weekly aggregation rule:**
If any phase has 0 tasks for 4 consecutive weeks → SAM proactively asks: "You haven't done any {phase} work in a month. Is this intentional or a blind spot?"

---

## External Discovery / Search Fallback

If a phase needs market, competitor, PM-framework, or UX-review references:
1. Try first-class `web_search` when configured.
2. If `web_search` is unavailable, use a search-capable model/session such as GLM plus `web_fetch`/GitHub README verification.
3. Treat model-search output as leads, not truth; verify top sources before writing them into skills.
4. Save useful discoveries into the relevant skill reference file, not only the chat.

Recommended external libraries to check first:
- `deanpeters/Product-Manager-Skills` — broad PM skill packs, OpenClaw/Codex compatible.
- `RefoundAI/lenny-skills` — product taste, design review, tradeoff, behavioral design, AI evals.
- `heurilens/ux-heuristics-checklist` — UX heuristics and AI audit prompts.
- `mattpocock/skills` — primary software engineering overlay for PLO: grill, PRD, issue slicing, TDD, diagnose, architecture improvement, review, handoff.
- [`obra/superpowers`](https://github.com/obra/superpowers) — Architecture Lens reference for identifying leverage, unique capability, and design-before-code thinking.
- [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills) — Agent/skill ownership and quality-gate reference. Use as thinking layer, not as a replacement for Matt-style execution.

---

## Inspiration Matching

When grill-me or any phase encounters a specific problem type, query the inspiration database:

```
Problem type examples:
  - layout-asymmetry, state-machine-design, animation-stagger,
  - prompt-engineering, eval-framework, skill-authoring,
  - pipeline-orchestration, lock-manager, degradation-chain

Query: "problem_type = {type}" → Return top 3 matches with source links
```

The inspiration database is fed by the content pipeline. Every high-signal item from the pipeline gets tagged with `phase` + `problem_type` on ingestion.

---


## Hermes / Skill Evolution Operating Loop

Hermes-style evolution is implemented as a controlled loop, not uncontrolled self-editing:

1. **Observe** — record which PLO path, phase, role lane, and templates were used.
2. **Detect Pattern** — if the same gap appears 2–3 times, generate a dry-run recommendation.
3. **Patch Proposal** — propose edits to the relevant path/reference/skill with source examples.
4. **Human Confirmation** — ask Jianan before writing.
5. **Write + Verify** — update skill/reference, log evidence, and test on the next real task.

Recommended patch targets:
- repeated CER/PTR architecture confusion → B2B Enterprise / AI Product Architect reference
- repeated boss brief/content framing → B2B Content / Influence reference
- repeated resource/meeting planning → Project Execution Manager reference
- repeated pain-to-AI-feature work → AI Product Manager reference

## Skill Evolution Rules

| Trigger | Action |
|---------|--------|
| Skill used ≥3 times, avg rating ≤2 | Search for replacement skill on ClawHub/LobeHub |
| Skill used ≥3 times, avg rating ≥4 | Promote to "recommended" tier in this mapping |
| New skill discovered externally | Install → test on 1 project → rate → decide keep/replace |
| Phase consistently empty for 4 weeks | SAM alerts user |

---

## Skill Inventory (PLO-Referenced)

| Skill | Location | Status |
|-------|----------|--------|
| `grill-with-docs` | JN-SkillHub | ✅ ready |
| `grill-me` | Andrew workspace | ✅ ready |
| `product-sense-review` | Andrew workspace | ✅ ready |
| `open-design` | Andrew workspace (ok-skills) | ✅ ready |
| `frontend-slides` | Andrew workspace | ✅ ready |
| `design-front` | JN-SkillHub | ✅ ready |
| `jianan-presentation-system` | JN-SkillHub | ✅ ready |
| `impeccable-design` | JN-SkillHub (ok-skills) | ✅ ready |
| `excalidraw-handnote-style` | Andrew workspace | ✅ ready |
| `codebase-to-course` | JN-SkillHub | ✅ ready |
| `claw-vibe-project` | JN-SkillHub | ✅ ready |
| `coding-agent` | Andrew workspace | ✅ ready |
| `test-driven-development` | ok-skills | ✅ ready |
| `subagent-driven-development` | ok-skills | ✅ ready |
| `prototype` | 📚 External: mattpocock/skills | Primary engineering overlay |
| `to-prd` | 📚 External: mattpocock/skills | Primary engineering overlay |
| `to-issues` | 📚 External: mattpocock/skills | Primary engineering overlay |
| `tdd` | 📚 External: mattpocock/skills | Primary engineering overlay |
| `diagnose` | 📚 External: mattpocock/skills | Primary engineering overlay |
| `improve-codebase-architecture` | 📚 External: mattpocock/skills | Primary engineering overlay |
| `review` | 📚 External: mattpocock/skills | Primary engineering overlay |
| `handoff` | 📚 External: mattpocock/skills | Primary engineering overlay |
| `github-pr` | JN-SkillHub | ✅ ready |
| `github` | JN-SkillHub | ✅ ready |
| `eight-d-optimization` | Andrew workspace | ✅ ready |
| `interaction-self-reflection` | Andrew workspace | ✅ ready |
| `skill-creator` | OpenClaw built-in | ✅ ready |
| `feishu-write-shared` | Andrew workspace | ✅ ready |
| `feishu-agent-workflow` | Andrew workspace | ✅ ready |
| `airtable-dashboard` | Andrew workspace | ✅ ready |
| `context7-cli` | ok-skills | ✅ ready |
| `get-api-docs` | ok-skills | ✅ ready |
| `superpower` | 📚 External: [`obra/superpowers`](https://github.com/obra/superpowers) | Architecture Lens / capability thinking |
| `agent-skill` | 📚 External: [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills) | Architecture Lens / ownership mapping |

---

## Usage

SAM reads this skill at the start of every new project or significant task. The skill provides the map; SAM provides the judgment on which path and which phase.

**Gate rule (as confirmed 2026-05-07):**
- T0/T1 tasks: skip PLO, lightweight review only
- T2+ product/design/release tasks: must pass through PLO
- ToC products with screenshots/prototypes/demos: must additionally pass `product-sense-review`
- On first real T2+ PLO trigger → notify Jianan
