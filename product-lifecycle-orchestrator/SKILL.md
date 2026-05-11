---
name: product-lifecycle-orchestrator
description: Full-cycle product lifecycle orchestrator (PLO). Use as the single entry point for T2+ product, design, content, automation, and release work. Detects mode (B2B Enterprise Automation vs B2B Content/Influence vs ToC Consumer vs Personal/Internal), routes to the correct lifecycle path, maps phases to role-lanes and skills, enforces quality gates, and records evolution hooks.
aliases: [PLO, product-lifecycle, lifecycle-orchestrator]
---

# Product Lifecycle Orchestrator (PLO)

SAM reads this skill to route every project through the correct development lifecycle.

---

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


### Phase 1: Stakeholder & Constraint
**Goal:** Understand who cares, what they want, and what constraints exist (both stated and implicit).
**When to exit:** You can state the 3 key stakeholders, their 1 top need each, the non-negotiable constraints, AND a written list of budget, timeline, tech requirements, compliance/security needs, integration points.

| Skill | What It Does |
|-------|-------------|
| `grill-me` | Probe stakeholder assumptions, surface hidden constraints, resolve conflicting requirements |
| `web_search` | Background research on stakeholder organization, industry, regulatory context |
| Internal docs | Read existing specs, contracts, email threads for implicit constraints |

### Phase 2: Technical Architecture
**Goal:** Design the system, choose the stack, decompose into tasks. Identify unique capabilities and agent matching.
**When to exit:** Architecture diagram exists, technology decisions are justified, tasks are decomposed, system superpowers are defined, and agent→skill mapping is complete.

| Skill | What It Does |
|-------|-------------|
| `first-principles-decomposer` | Break down the problem to first principles; justify architecture decisions from fundamentals |
| `superpower` | Identify the system's unique strengths and comparative advantages; define what makes this architecture special vs alternatives |
| `agent-skill` | Map required capabilities to available agents and skills; define which agent owns which subsystem and which skills they need |
| `web_search` | Research tech choices, benchmarks, and architectural patterns |

**Methodology references (external libraries to consult during architecture design):**
- [`obra/superpowers`](https://github.com/obra/superpowers) — Jesse Vincent's agentic development methodology: brainstorming → plan → subagent-dev → TDD → verify → review → ship. Core principles: design before code, evidence before claims, TDD as non-negotiable.
- [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills) — Addy Osmani's 20 production-grade engineering skills: DEFINE → PLAN → BUILD → VERIFY → REVIEW → SHIP. Use as a reference for skill design patterns and quality gate structures.
| `context7-cli` / `get-api-docs` | Pull external API docs and integration specs |
| `codebase-to-course` | Understand existing codebases that will be extended or referenced (if applicable) |
| `claw-vibe-project` | Long-term project coordination, session management |
| MAE pipeline | Multi-agent task decomposition and parallel execution |

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

| Skill | What It Does |
|-------|-------------|
| `coding-agent` | Code generation and iteration |
| `test-driven-development` | Write tests before implementation; enforce TDD discipline |
| `subagent-driven-development` | Staged multi-subagent implementation for complex features |
| `github-pr` | PR workflow, review, and merge management |
| MAE pipeline | Multi-step code → test → review → fix workflows |

**Quality Gates (NON-NEGOTIABLE):**

| Gate | Enterprise (CER-type) | Standard B2B |
|------|----------------------|-------------|
| **TDD** | Tests before every function. ≥90% coverage target. Integration tests for all external APIs. | Tests before implementation. Core paths covered. |
| **Evals** | LLM-as-judge on every output batch. Score ≥ 0.85. Trace replay for regression. | LLM-as-judge on critical outputs. Score ≥ 0.75. |
| **Code Review** | Duplication, security, permissions, error handling, audit trail, data integrity. | Duplication, security, permissions, error handling. |
| **Type Safety** | mypy/pyright strict mode in CI. | mypy/pyright passes in CI. |
| **CI/CD** | GitHub Actions: push → test → evals → review → merge. Block merge on any failure. | GitHub Actions: push → test → review → merge. |

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
Same as Path A Phase 2 (includes `superpower` + `agent-skill`).

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
Same as Path A Phase 2 (includes `superpower` + `agent-skill`).

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
| 3 | Product Architecture / Work Packages | Narrative Architecture | Architecture (+superpower +agent-skill) | Architecture (+superpower +agent-skill) |
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
- [`obra/superpowers`](https://github.com/obra/superpowers) — Agentic development methodology (brainstorming → plan → subagent-dev → TDD → verify → review → ship).
- [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills) — 20 production-grade engineering skills (DEFINE → PLAN → BUILD → VERIFY → REVIEW → SHIP).

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
| `first-principles-decomposer` | JN-SkillHub | ✅ ready |
| `test-driven-development` | ok-skills | ✅ ready |
| `subagent-driven-development` | ok-skills | ✅ ready |
| `tdd` | 📚 External: mattpocock/skills | Reference methodology |
| `diagnose` | 📚 External: mattpocock/skills | Reference methodology |
| `improve-codebase-architecture` | 📚 External: mattpocock/skills | Reference methodology |
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
| `superpower` | 📚 External: [`obra/superpowers`](https://github.com/obra/superpowers) | Reference methodology |
| `agent-skill` | 📚 External: [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills) | Reference methodology |

---

## Usage

SAM reads this skill at the start of every new project or significant task. The skill provides the map; SAM provides the judgment on which path and which phase.

**Gate rule (as confirmed 2026-05-07):**
- T0/T1 tasks: skip PLO, lightweight review only
- T2+ product/design/release tasks: must pass through PLO
- ToC products with screenshots/prototypes/demos: must additionally pass `product-sense-review`
- On first real T2+ PLO trigger → notify Jianan
