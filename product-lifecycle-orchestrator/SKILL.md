---
name: product-lifecycle-orchestrator
description: Full-cycle product development orchestrator (PLO). Detects project mode (B2B vs ToC vs Personal), routes to the correct 7-phase path, maps each phase to available skills, integrates search + inspiration matching, and tracks attention distribution. SAM's mandatory entry point for any T2+ project or task.
aliases: [PLO, product-lifecycle, lifecycle-orchestrator]
---

# Product Lifecycle Orchestrator (PLO)

SAM reads this skill to route every project through the correct development lifecycle.

---

## Pre-flight: Mode Detection

Before entering any phase, determine which path applies.

| Question | B2B Answer | ToC Answer | Personal Answer |
|----------|------------|------------|-----------------|
| Who makes the decisions? | A client, boss, or external stakeholder | End users / market behavior | I make all decisions |
| Where does key information live? | Internal docs, meetings, stakeholder conversations | User behavior, onboarding, retention, reviews | Public tools, my own experimentation |
| What is the dominant risk? | Misalignment, veto, compliance, ROI | Activation, trust, emotion, habit, conversion | Scope creep, taste drift, maintenance burden |

**If ≥2 B2B answers → B2B Path. If ≥2 ToC answers → ToC Path. Otherwise → Personal Path.**

Plus: `web_search` for market context, category state, and recent launches before committing to a path.

---

## Path A: B2B / Stakeholder-Driven

```
Phase 1 → Phase 2 → Phase 3 → Phase 4 → Phase 5 → Phase 6 → Phase 7
```

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
| `product-sense-review` | Product personality, UX risk, launch blocker, and user psychology review; mandatory at prototype/screenshot stage |
| **Output-type skill matrix:** | |
| Web / Landing page | `open-design` (React + Tailwind) |
| Slide deck | `frontend-slides` (scroll-snap HTML pages) |
| PPT / Roadshow / Pitch | `jianan-presentation-system` |
| UI components | `design-front` |
| High-end visual design | `impeccable-design` |
| Architecture diagrams | `excalidraw-handnote-style` |

### Phase 4: Development
**Goal:** Build, test, review, iterate.
**When to exit:** Code passes all quality gates.

| Skill | What It Does |
|-------|-------------|
| `coding-agent` | Code generation and iteration |
| `test-driven-development` | Write tests before implementation; enforce TDD discipline |
| `subagent-driven-development` | Staged multi-subagent implementation for complex features |
| `github-pr` | PR workflow, review, and merge management |
| MAE pipeline | Multi-step code → test → review → fix workflows |

**Quality Gates (NON-NEGOTIABLE):**
1. **TDD Gate:** Tests written before implementation. Tests pass before Phase 4 exit.
2. **Evals Gate:** LLM output quality scored (LLM-as-judge). Score ≥ threshold before merge.
3. **Code Review Gate:** Self-review checklist: duplication, security, permissions, error handling.
4. **Type Safety Gate:** mypy/pyright passes in CI (once typed state dataclass is implemented).
5. **CI/CD Gate:** GitHub Actions: push → test → evals → review → merge.

### Phase 5: Delivery
**Goal:** Publish, notify, document.
**When to exit:** Deliverable is accessible, stakeholders are notified, documentation exists, deployment verified.

| Skill | What It Does |
|-------|-------------|
| `github` | Release management, tag, changelog |
| `feishu-write-shared` | Write to Feishu Wiki with structured format |
| `airtable-dashboard` | Sync task status to Dashboard |
| `feishu-agent-workflow` | Route deliverables to correct Feishu space |
| Deployment verification | Confirm the deliverable is live and accessible; smoke-test key paths |

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

### Phase 5-7: Same as Path A Phases 4-6
(Development → Delivery → Review & Evolve, identical skill mapping. `product-sense-review` recommended as pre-launch gate.)

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

### Phase 3-7: Same as Path A Phases 2-6
(Architecture → Design → Development → Delivery → Review, identical skill mapping)

---

## Phase Summary (All Paths)

| Phase | B2B | ToC | Personal |
|-------|-----|-----|----------|
| 1 | Stakeholder & Constraint | User Pull & Emotional Job | Feature Fusion |
| 2 | Architecture (+superpower +agent-skill) | Activation & Trust | Scope Definition |
| 3 | Design & UX | Architecture (+superpower +agent-skill) | Architecture (+superpower +agent-skill) |
| 4 | Development | Design & UX (+ToC gates) | Design & UX |
| 5 | Delivery | Development | Development |
| 6 | Review & Evolve | Delivery | Delivery |
| 7 | — | Review & Evolve | Review & Evolve |

> Note: B2B merges Stakeholder+Constraint into Phase 1, so it uses 6 phases (1-6). ToC and Personal use full 7 phases. All paths converge on Architecture (Phase 2/3) and remain shared through Review.

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
| `superpower` | JN-SkillHub | ⚠️ to be created |
| `agent-skill` | JN-SkillHub | ⚠️ to be created |

---

## Usage

SAM reads this skill at the start of every new project or significant task. The skill provides the map; SAM provides the judgment on which path and which phase.

**Gate rule (as confirmed 2026-05-07):**
- T0/T1 tasks: skip PLO, lightweight review only
- T2+ product/design/release tasks: must pass through PLO
- ToC products with screenshots/prototypes/demos: must additionally pass `product-sense-review`
- On first real T2+ PLO trigger → notify Jianan
