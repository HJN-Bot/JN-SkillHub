---
name: codebase-to-course
description: "Turn any codebase into a beautiful, interactive single-page HTML course that teaches how the code works. Use this skill whenever someone wants to create an interactive course, tutorial, or educational walkthrough from a codebase or project. Also trigger when users mention 'turn this into a course,' 'explain this codebase interactively,' 'teach this code,' 'interactive tutorial from code,' 'codebase walkthrough,' 'learn from this codebase,' 'make a course from this project,' 'show me the data flow,' 'how do these modules connect,' 'what changed in this update,' 'trace the pipeline,' 'package anatomy,' 'explain this script,' or 'what does this function do.' This skill produces a stunning, self-contained HTML file with scroll-based navigation, animated visualizations, embedded quizzes, and code-with-plain-English side-by-side translations. Extended with Deep Dive Mode for multi-layer code understanding: module collaboration maps, per-package data flow tracing, function-level anatomy, and git diff change tracking."
---

# Codebase-to-Course (Extended)

Transform any codebase into a stunning, interactive single-page HTML course. The output is a single self-contained HTML file (no dependencies except Google Fonts) that teaches how the code works through scroll-based modules, animated visualizations, embedded quizzes, and plain-English translations of code.

**Extended capabilities** (beyond the original skill):
- **Deep Dive Mode** — five-layer progressive zoom from module map → package anatomy → data flow → function-level code
- **Git Diff Tracking** — visualize what changed between commits/versions, highlight affected data paths
- **Package Anatomy Cards** — expandable interactive cards showing each package's I/O, core logic, and call graph
- **Data Pipeline Tracer** — animated step-by-step data transformation visualization with intermediate state inspection

## First-Run Welcome

When the skill is first triggered and the user hasn't specified a codebase yet, introduce yourself and explain what you do:

> **I can turn any codebase into an interactive course that teaches how it works — no coding knowledge required.**
>
> Just point me at a project:
> - **A local folder** — e.g., "turn ./my-project into a course"
> - **A GitHub link** — e.g., "make a course from https://github.com/user/repo"
> - **The current project** — if you're already in a codebase, just say "turn this into a course"
>
> I'll read through the code, figure out how everything fits together, and generate a beautiful single-page HTML course with animated diagrams, plain-English code explanations, and interactive quizzes. The whole thing runs in your browser — no setup needed.
>
> **Deep Dive Mode**: Want to understand a specific script or pipeline in depth? Say "deep dive into [file/module]" and I'll trace every data transformation, map every function call, and show you the exact I/O at each stage.

If the user provides a GitHub link, clone the repo first (`git clone <url> /tmp/<repo-name>`) before starting the analysis. If they say "this codebase" or similar, use the current working directory.

## Who This Is For

The target learner is a **"vibe coder"** — someone who builds software by instructing AI coding tools in natural language, without a traditional CS education. They may have built this project themselves (without looking at the code), or they may have found an interesting open-source project on GitHub and want to understand how it's built. Either way, they don't yet understand what's happening under the hood.

**Assume zero technical background.** Every CS concept — from variables to APIs to databases — needs to be explained in plain language as if the learner has never encountered it. No jargon without definition. No "as you probably know." The tone should be like a smart friend explaining things, not a professor lecturing.

**Their goals are practical, not academic:**
- Have enough technical knowledge to effectively **steer AI coding tools** — make better architectural and tech stack decisions
- **Detect when AI is wrong** — spot hallucinations, catch bad patterns, know when something smells off
- **Intervene when AI gets stuck** — break out of bug loops, debug issues, unblock themselves
- Build more advanced software with **production-level quality and reliability**
- Be **technically fluent** enough to discuss decisions with engineers confidently
- **Acquire the vocabulary of software** — learn the precise technical terms so they can describe requirements clearly and unambiguously to AI coding agents (e.g., knowing to say "namespace package" instead of "shared folder thing")
- **Understand what changed** — when a collaborator updates a module, know exactly which data flows are affected and what broke

**They are NOT trying to become software engineers.** They want coding as a superpower that amplifies what they're already good at. They don't need to write code from scratch — they need to *read* it, *understand* it, and *direct* it.

## Why This Approach Works

This skill inverts traditional CS education. The old model is: memorize concepts for years → eventually build something → finally see the point (most people quit before step 3). This model is: **build something first → experience it working → now understand how it works.**

The learner already has context that traditional students don't — they've *used* the app, they know what it does, they may have even described its features in natural language. The course meets them where they are: "You know that button you click? Here's the journey your data takes after you click it."

Every module answers **"why should I care?"** before "how does it work?" The answer to "why should I care?" is always practical: *because this knowledge helps you steer AI better, debug faster, or make smarter architectural decisions.*

The single-file constraint is intentional: one HTML file means zero setup, instant sharing, works offline, and forces tight design decisions.

---

## Two Modes of Operation

### Standard Mode (default)
The original codebase-to-course experience: 5-8 module course covering the full codebase from user experience down to code details. Best for first-time understanding of a project.

### Deep Dive Mode
Triggered when the user says "deep dive into [file/module/pipeline]" or asks questions like "how does the data flow through this script" or "what does each function in this file do." Produces a focused, single-module or multi-module course on one specific package or pipeline, going much deeper than Standard Mode.

**Deep Dive produces five progressive layers:**

| Layer | What it shows | Key interactive element |
|---|---|---|
| L1: Module collaboration map | Which packages/scripts call which — the general interaction graph | Interactive Architecture Diagram with clickable nodes |
| L2: Package anatomy | For each core package: purpose, main functions, I/O contract | Package Anatomy Card (expandable, interactive) |
| L3: Data flow tracing | Input → transform₁ → transform₂ → ... → output, with intermediate data shapes | Data Pipeline Tracer (animated, inspectable) |
| L4: Function-level code reading | The actual `def` / `class` — what each core function does line by line | Code ↔ English Translation Blocks |
| L5: Git diff tracking | What changed between versions, which data paths are affected | Diff Highlight Overlay on the architecture/flow diagrams |

**When to use Deep Dive vs Standard:**
- User says "turn this into a course" → Standard Mode
- User says "explain this script" / "trace the pipeline" / "what changed" → Deep Dive Mode
- User says "deep dive" explicitly → Deep Dive Mode
- User pastes a single file and asks "explain this" → Deep Dive Mode (single-package focus)

---

## The Process (5 Phases)

### Phase 0: Input Classification & Reasoning (THINK FIRST)

**Before ANY analysis or code generation, stop and classify what you received.** This is the most important step. Different inputs demand fundamentally different approaches. Do NOT jump to building — first reason about what you're looking at.

**Step 1 — Identify the input type:**

| Input Type | How to Detect | Example |
|---|---|---|
| **Full project (GitHub repo)** | Has `package.json` / `pyproject.toml` / `docker-compose.yml` / multiple directories | `git clone https://github.com/user/project` |
| **Multi-file bundle** | 3+ files pasted or uploaded, mixed types | User drops `main.py`, `config.yaml`, `utils.py` |
| **Single code file** | One `.py` / `.js` / `.ts` / `.sh` file | User pastes `pipeline_runner.py` |
| **Single data file** | One `.json` / `.yaml` / `.csv` / `.env` file | User pastes a `config.json` |
| **Single document** | One `.md` / `.html` / `.sql` file | User pastes a `README.md` or `schema.sql` |

**Step 2 — Determine the presentation strategy:**

| Input Type | Mode | Architecture Depth | Primary Focus |
|---|---|---|---|
| Full project | Standard Mode | All 4 layers (Architecture → Module → Detail → Unit) | System structure, how modules collaborate, full data flow |
| Multi-file bundle | Deep Dive Mode | Layers 2-4 (Module → Detail → Unit) | How the files relate to each other, cross-file call graph |
| Single `.py` / `.js` | Deep Dive Mode | Layers 3-4 (Detail → Unit) | Function inventory, internal call flow, I/O per function, data transformations |
| Single `.json` / `.yaml` | Deep Dive Mode | Layer 3 only | Schema structure, who consumes it, field meanings, validation rules |
| Single `.csv` | Deep Dive Mode | Layer 3 only | Column analysis, data types, sample rows, which code processes it |
| Single `.html` | Deep Dive Mode | Layers 3-4 | DOM structure, template variables, linked resources, render result |
| Single `.md` | Deep Dive Mode | Layer 3 only | Document structure, whether it describes architecture, key decisions it captures |
| Single `.sql` | Deep Dive Mode | Layers 3-4 | Tables, relationships, key queries, migration sequence |

**Step 3 — Choose the right visualization elements:**

| What You're Explaining | Best Visualization | Library/Technique |
|---|---|---|
| Module dependencies (who imports who) | Force-directed graph or Chord diagram | D3.js force layout or d3-chord |
| Data transformation pipeline | Sankey diagram or Data Pipeline Tracer | D3-sankey or custom step animation |
| Function call sequence | Numbered step cards or animated flow | CSS animation with step-by-step reveal |
| File tree with roles | Interactive file tree with type dots | Custom HTML with expand/collapse |
| JSON/YAML schema | Collapsible tree with type annotations | Custom HTML accordion |
| CSV data profile | Mini data table + column type badges | HTML table with sparklines |
| Git changes over time | Timeline with commit dots | SVG timeline or step cards |
| Architecture overview | Structural block diagram | SVG or HTML grid layout |
| Circular dependencies | Chord diagram | D3-chord |
| Data flow volume | Sankey diagram | D3-sankey |

**Step 4 — Write your reasoning (internal, before building):**

Before generating any HTML, write a brief internal plan:
```
INPUT TYPE: [what was detected]
MODE: [Standard / Deep Dive]
ARCHITECTURE DEPTH: [which layers apply]
KEY QUESTIONS TO ANSWER:
  1. [What is the main thing the user needs to understand?]
  2. [What's the most confusing part that visualization will clarify?]
  3. [What data flow or dependency is most important?]
VISUALIZATION PLAN:
  Module 1: [element type] for [purpose]
  Module 2: [element type] for [purpose]
  ...
```

**Only after completing Phase 0 should you proceed to Phase 1.**

### Phase 1: Codebase Analysis

Before writing course HTML, deeply understand the codebase. Read all the key files, trace the data flows, identify the "cast of characters" (main components/modules), and map how they communicate. Thoroughness here pays off — the more you understand, the better the course.

**What to extract:**
- The main "actors" (components, services, modules) and their responsibilities
- The primary user journey (what happens when someone uses the app end-to-end)
- Key APIs, data flows, and communication patterns
- Clever engineering patterns (caching, lazy loading, error handling, etc.)
- Real bugs or gotchas (if visible in git history or comments)
- The tech stack and why each piece was chosen

**Additional extraction for Deep Dive Mode:**
- **Call graph**: For each core file, which functions call which other functions (internal and cross-file)
- **I/O contract per function**: What does each function take as input (args, types, data shapes) and what does it return
- **Data shape at each stage**: If the pipeline processes data (e.g., LLM output → post-processing → final output), capture what the data looks like at each transformation step — column names, JSON structure, key fields
- **Post-processing chain**: Identify every transformation layer between raw input and final output. This is critical — many bugs come from not knowing how many layers of transformation exist
- **Git history** (if available): Run `git log --oneline -20` and `git diff HEAD~1` (or between specified commits) to identify recent changes. Map changed files to the module collaboration graph

**Figure out what the app does yourself** by reading the README, the main entry points, and the UI code. Don't ask the user to explain the product — they may not be familiar with it either. The course should open by explaining what the app does in plain language (a brief "here's what this thing does and why it's interesting") before diving into how it works. The first module should start with a concrete user action — "imagine you paste a YouTube URL and click Analyze — here's what happens under the hood."

#### File-Type Aware Analysis

Different file types serve different roles and need different analysis approaches. During Phase 1, classify every file you encounter and apply the appropriate analysis lens:

| File Type | Role in Project | What to Extract |
|---|---|---|
| `.py` | Logic / processing | Functions (name, args, return), class hierarchy, imports, call graph, data transformations |
| `.js` / `.ts` | Frontend logic / API | Components, event handlers, API calls, state management, DOM manipulation |
| `.html` | Structure / templates | Page structure, template variables, component slots, form fields, linked resources |
| `.css` / `.scss` | Presentation | Layout patterns, responsive breakpoints, component class naming, theme variables |
| `.json` | Configuration / data | Schema structure, key fields and their meanings, nesting depth, which code reads this |
| `.csv` / `.tsv` | Tabular data | Column names, data types per column, row count estimate, which code consumes it |
| `.md` | Documentation | What it documents, whether it's up-to-date, key decisions or architecture notes it captures |
| `.yaml` / `.yml` | Configuration / pipelines | Structure hierarchy, which service/tool consumes it, environment-specific overrides |
| `.env` / `.toml` / `.ini` | Environment config | Variables defined, which ones are secrets, which code references them |
| `.sql` | Database | Tables defined, relationships, key queries, migration sequence |
| `.sh` / `.bat` | Automation | What it automates, execution order, dependencies, error handling |

**When analyzing a file, always surface:**
1. What TYPE of file is this (from the table above)
2. WHO consumes this file (which other files import/read/reference it)
3. WHAT is its role in the overall data flow

#### Four-Layer Architecture Model (for projects)

When analyzing a full project (not a single file), organize your understanding into four nested layers. This is the "zoom" structure — the course should let the learner navigate from the outermost layer inward:

**Layer 1 — Architecture layer (the 30,000ft view)**
What are the major subsystems? How do they relate? What's the tech stack?
- Example: "This project has a Python backend (FastAPI), a React frontend, a PostgreSQL database, and an LLM service layer."
- Visual: High-level block diagram with 3-5 blocks and arrows showing data direction
- File types here: README.md, docker-compose.yml, project root configs

**Layer 2 — Module layer (the building blocks)**
Within each subsystem, what are the packages/directories? What does each one own?
- Example: "The backend has 4 packages: `api/` (route handlers), `services/` (business logic), `models/` (data schemas), `utils/` (shared helpers)."
- Visual: Expanded block diagram — each subsystem opens into its constituent packages
- File types here: `__init__.py`, `package.json`, directory-level READMEs

**Layer 3 — Detail layer (the working parts)**
Within each module, what are the key files? What does each file do? How do they call each other?
- Example: "`services/pipeline.py` orchestrates the CER generation. It calls `services/llm_client.py` for model inference and `services/formatter.py` for output."
- Visual: File tree with annotations + Package Anatomy Cards + cross-file call arrows
- File types here: All `.py`, `.js`, `.html`, `.yaml` files that contain actual logic

**Layer 4 — Unit layer (the code itself)**
Within each key file, what are the functions/classes? What are their I/O contracts? How does data transform step by step?
- Example: "`process_chapter(chapter_id, context)` takes a chapter ID and pipeline context, calls the LLM, then runs 3 post-processing steps, and returns a ChapterResult."
- Visual: Code ↔ English translations + Data Pipeline Tracer
- File types here: Individual functions within files

**The course should navigate these layers progressively** — start at Layer 1, then the user can "zoom in" to any block to see Layer 2, then further into Layer 3, and finally Layer 4 for specific functions.

#### Single-File Analysis Protocol

When analyzing a SINGLE file (user says "explain this file" or pastes one file), apply a file-type-specific deep analysis. Every single-file analysis must cover these aspects, adapted to the file type:

**For code files (`.py`, `.js`, `.ts`, `.sh`):**
1. **Purpose** — What is this file's job in one sentence?
2. **Imports / dependencies** — What does it pull in and why?
3. **Function inventory** — List every `def` / `function` with: name, input args (with types if available), return value, one-line purpose
4. **Call flow** — Which functions call which? Show the internal call graph
5. **Data flow** — Trace input → transformation → output through the main functions. What does the data look like at each stage?
6. **Entry point** — How is this file invoked? (CLI? imported? called by another script?)
7. **Side effects** — Does it write files, call APIs, modify databases?
8. **Core logic spotlight** — Pick the 2-3 most important functions and do full Code ↔ English translations

**For data/config files (`.json`, `.yaml`, `.csv`, `.env`):**
1. **Schema** — What's the structure? Key fields and their purposes
2. **Consumer** — Which code files read this? How do they parse it?
3. **Sensitivity** — Are there secrets, environment-specific values, or user data?
4. **Example** — Show a real sample with annotations explaining each field
5. **Validation** — Are there constraints? Required fields? Format rules?

**For markup/template files (`.html`, `.md`, `.sql`):**
1. **Structure** — What sections/components does it define?
2. **Dynamic parts** — Template variables, conditional blocks, loops
3. **Relationships** — What data feeds into this? What renders/consumes it?

### Phase 2: Curriculum Design

#### Standard Mode Curriculum

Structure the course as 5-8 modules. The arc always starts from what the learner already knows (the user-facing behavior) and moves toward what they don't (the code underneath). Think of it as zooming in: start wide with the experience, then progressively peel back layers.

| Module Position | Purpose | Why it matters for a vibe coder |
|---|---|---|
| 1 | "Here's what this app does — and what happens when you use it" | Start with the product (what it does, why it's interesting), then trace a core user action into the code. Grounds everything in something concrete. |
| 2 | Meet the actors | Know which components exist so you can tell AI "put this logic in X, not Y" |
| 3 | How the pieces talk | Understand data flow so you can debug "it's not showing up" problems |
| 4 | The outside world (APIs, databases) | Know what's external so you can evaluate costs, rate limits, and failure modes |
| 5 | The clever tricks | Learn patterns (caching, chunking, error handling) so you can request them from AI |
| 6 | When things break | Build debugging intuition so you can escape AI bug loops |
| 7 | The big picture | See the full architecture so you can make better decisions about what to build next |

Not every codebase needs all 7. A simple CLI tool might only need 4-5 modules. A microservices app might need 8. Adapt the arc to the codebase's complexity — use your judgment on which modules are worth including based on what would actually help the learner steer AI and debug better.

#### Deep Dive Mode Curriculum

Structure as 3-5 focused modules that follow the five layers. Not every Deep Dive needs all five layers — adapt to what the user actually asked about.

| Module | Layer | Content |
|---|---|---|
| 1: The landscape | L1 | Interactive architecture diagram: all packages/scripts as clickable nodes, arrows showing call relationships. Click a node to jump to its anatomy. |
| 2: Package X-ray | L2 | One Package Anatomy Card per core package. Each card expands to show: purpose (1 sentence), main functions list, I/O contract (what goes in, what comes out), dependencies (what it imports). |
| 3: Data pipeline | L3 | Animated Data Pipeline Tracer for the main data flow. Shows the data shape at each transformation stage. User can click any stage to inspect the intermediate data format. |
| 4: Under the hood | L4 | Code ↔ English Translation Blocks for the 3-5 most important functions. Pick the functions that do the actual work — not boilerplate, not imports, not config. |
| 5: What changed | L5 | Git Diff View showing recent changes overlaid on the architecture diagram. Changed files glow. Affected data paths highlighted. Only include this module if git history is available and the user cares about changes. |

**The key principle:** Every module should connect back to a practical skill — steering AI, debugging, making decisions. If a module doesn't help the learner DO something better, cut it or reframe it until it does.

**Each module should contain:**
- 3-6 screens (sub-sections that flow within the module)
- At least one code-with-English translation
- At least one interactive element (quiz, visualization, or animation)
- One or two "aha!" callout boxes with universal CS insights
- A metaphor that grounds the technical concept in everyday life — but NEVER reuse the same metaphor across modules, and NEVER default to the "restaurant" metaphor (it's overused). Pick metaphors that organically fit the specific concept. The best metaphors feel *inevitable* for the concept, not forced.

**Mandatory interactive elements (every course must include ALL of these):**
- **Group Chat Animation** — at least one across the course. These are the iMessage/WeChat-style conversations between components. They're one of the most engaging elements and must always appear, even if you have to creatively frame a module's concept as a conversation between actors.
- **Message Flow / Data Flow Animation** — at least one across the course. The step-by-step packet animation between actors. If the codebase has any kind of request/response, data pipeline, or multi-step process, animate it. Every codebase has data flowing somewhere — find it.
- **Code ↔ English Translation Blocks** — at least one per module (already required above, but reiterating: this is non-negotiable).
- **Quizzes** — at least one per module (multiple-choice, scenario, drag-and-drop, or spot-the-bug — any quiz type counts).
- **Glossary Tooltips** — on every technical term, first use per module.

**Deep Dive Mode adds these mandatory elements:**
- **Package Anatomy Card** — at least one per core package identified in the analysis
- **Data Pipeline Tracer** — at least one for the main data flow path
- **Git Diff Overlay** — if git history is available and relevant

These five element types (plus the three Deep Dive additions when applicable) are the backbone of every course. Other interactive elements (architecture diagrams, layer toggles, pattern cards, etc.) are optional and should be added when they fit. But the mandatory ones must ALWAYS be present — no exceptions.

**Do NOT present the curriculum for approval — just build it.** The user wants a course, not a planning document. Design the curriculum internally, then go straight to generating the HTML. If they want changes, they'll tell you after seeing the result.

### Phase 3: Build the Course

Generate a single HTML file with embedded CSS and JavaScript. Read `references/design-system.md` for the complete CSS design tokens, typography, and color system. Read `references/interactive-elements.md` for implementation patterns of every interactive element type. Read `references/deep-dive-elements.md` for Package Anatomy Cards, Data Pipeline Tracers, and Git Diff Overlays.

**Build order (task by task):**

1. **Foundation first** — HTML shell with all module sections (empty), complete CSS design system, navigation bar with progress tracking, scroll-snap behavior, keyboard navigation, and scroll-triggered animations. After this step, you should have a working skeleton you can scroll through.

2. **One module at a time** — Fill in each module's content, code translations, and interactive elements. Don't try to write all 8 modules in one pass — the quality drops. Build Module 1, verify it works, then Module 2, etc.

3. **Polish pass** — After all modules are built, do a final pass for transitions, mobile responsiveness, and visual consistency.

**Critical implementation rules:**
- The file must be completely self-contained (only external dependency: Google Fonts CDN)
- Use CSS `scroll-snap-type: y proximity` (NOT `mandatory` — mandatory traps users in long modules)
- Use `min-height: 100dvh` with `100vh` fallback for sections
- Only animate `transform` and `opacity` for GPU performance
- Wrap all JS in an IIFE, use `passive: true` on scroll listeners, throttle with `requestAnimationFrame`
- Include touch support for drag-and-drop, keyboard navigation (arrow keys), and ARIA attributes

### Phase 4: Review and Open

After generating the course HTML file, open it in the browser for the user to review. Walk them through what was built and ask for feedback on content, design, and interactivity.

---

## Content Philosophy

These principles are what separate a great course from a generic tutorial. They should guide every content decision:

### Show, Don't Tell — Aggressively Visual
People's eyes glaze over text blocks. The course should feel closer to an infographic than a textbook. Follow these hard rules:

**Text limits:**
- Max **2-3 sentences** per text block. If you're writing a fourth sentence, stop and convert it into a visual instead.
- No text block should ever be wider than the content width AND taller than ~4 lines. If it is, break it up with a visual element.
- Every screen must be **at least 50% visual** (diagrams, code blocks, cards, animations, badges — anything that isn't a paragraph).

**Convert text to visuals:**
- A list of 3+ items → **cards with icons** (pattern cards, feature cards)
- A sequence of steps → **flow diagram with arrows** or **numbered step cards**
- "Component A talks to Component B" → **animated data flow** or **group chat visualization**
- "This file does X, that file does Y" → **visual file tree with annotations** or **icon + one-liner badges**
- Explaining what code does → **code↔English translation block** (not a paragraph *about* the code)
- Comparing two approaches → **side-by-side columns** with visual contrast
- A package's responsibilities → **Package Anatomy Card** (not a paragraph listing functions)
- A multi-step data transformation → **Data Pipeline Tracer** (not a bullet list of steps)

**Visual breathing room:**
- Use generous spacing between elements (`--space-8` to `--space-12` between sections)
- Alternate between full-width visuals and narrow text blocks to create rhythm
- Every module should have at least one "hero visual" — a diagram, animation, or interactive element that dominates the screen and teaches the core concept at a glance

### Code ↔ English Translations
Every code snippet gets a side-by-side plain English translation. Left panel: real code from the project with syntax highlighting. Right panel: line-by-line plain English explaining what each line does. This is the single most valuable teaching tool for non-technical learners.

**Critical: No horizontal scrollbars on code.** All code must use `white-space: pre-wrap` so it wraps instead of scrolling. This is a course for non-technical people, not an IDE — readability beats preserving indentation structure.

**Critical: Use original code exactly as-is.** Never modify, simplify, or trim code snippets from the codebase. The learner should be able to open the real file and see the exact same code they learned from — that builds trust. Instead of editing code to make it shorter, *choose* naturally short, punchy snippets (5-10 lines) from the codebase that illustrate the concept well. Every codebase has compact, self-contained moments — find those rather than butchering longer functions.

### One Concept Per Screen
No walls of text. Each screen within a module teaches exactly one idea. If you need more space, add another screen — don't cram.

### Metaphors First, Then Reality
Introduce every new concept with a metaphor from everyday life. Then immediately ground it: "In our code, this looks like..." The metaphor builds intuition; the code grounds it in reality.

**Critical: No recycled metaphors.** Do NOT default to "restaurant" for everything — that's the #1 crutch. Each concept deserves its own metaphor that feels natural to *that specific idea*. A database is a library with a card catalog. Auth is a bouncer checking IDs. An event loop is an air traffic controller. Message passing is a postal system. API rate limiting is a nightclub with a capacity limit. Pick the metaphor that makes the concept click, not the one that's easiest to reach for. If you catch yourself using "restaurant" or "kitchen" more than once in a course, stop and rethink.

### Learn by Tracing
Follow what actually happens when the learner does something they already do every day in the app — trace the data flow end-to-end. "You know that button you click? Here's the journey your data takes after you click it..." This works because the learner has *already experienced the result* — now they're seeing the machinery behind it. It's like watching a behind-the-scenes documentary of a movie you loved.

### Make It Memorable
Use "aha!" callout boxes for universal CS insights. Use humor where natural (not forced). Give components personality — they're "characters" in a story, not abstract boxes on a diagram.

### Glossary Tooltips — No Term Left Behind
Every technical term (API, DOM, callback, middleware, etc.) gets a dashed-underline tooltip on first use in each module. Hover on desktop or tap on mobile to see a 1-2 sentence plain-English definition. The learner should never have to leave the page to Google a term. This is the difference between a course that *says* it's for non-technical people and one that actually *is*.

**Be extremely aggressive with tooltips.** If there is even a 1% chance a non-technical person doesn't know a word, tooltip it. This includes:
- Software names they might not know (Blender, GIMP, Audacity, etc.)
- Everyday developer terms (REPL, JSON, flag, CLI, API, SDK, etc.)
- Programming concepts (function, variable, dictionary, class, module, etc.)
- Infrastructure terms (PATH, pip, namespace, entry point, etc.)
- Acronyms — ALWAYS tooltip acronyms on first use

**The vocabulary IS the learning.** One of the key goals is for learners to acquire the precise technical vocabulary they need to communicate with AI coding agents. Each tooltip should teach the term in a way that helps the learner USE it in their own instructions — e.g., "A **flag** is an option you add to a command to change its behavior — like adding '--json' to get structured data instead of plain text. When talking to AI, you'd say 'add a flag for verbose output.'"

**Cursor:** Use `cursor: pointer` on terms (not `cursor: help`). The question-mark cursor feels clinical — a pointer feels clickable and inviting.

**Tooltip overflow fix:** Translation blocks and other containers with `overflow: hidden` will clip tooltips. To fix this, the tooltip JS must use `position: fixed` and calculate coordinates from `getBoundingClientRect()` instead of relying on CSS `position: absolute` within the container. Append tooltips to `document.body` rather than inside the term element. This ensures tooltips are never clipped by any ancestor's overflow.

### Quizzes That Test Application, Not Memory

The goal of learning is practical application — being able to *do something* with what you learned. Quizzes should test whether the learner can use their knowledge to solve a new problem, not whether they can regurgitate a definition.

**What to quiz (in order of value):**
1. **"What would you do?" scenarios** — Present a new situation the learner hasn't seen and ask them to apply what they learned. e.g., "You want to add a 'save to favorites' feature. Which files would you need to change?" This is the gold standard.
2. **Debugging scenarios** — "A user reports X is broken. Based on what you learned, where would you look first?" This tests whether they understood the architecture, not just memorized file names.
3. **Architecture decisions** — "You're building a similar app from scratch. Would you put this logic in the frontend or backend? Why?" Tests whether they understood the *reasoning* behind design choices.
4. **Tracing exercises** — "When a user does X, trace the path the data takes." Tests whether they can follow the flow.
5. **Change impact analysis** (Deep Dive Mode) — "If you modify function X to change the output format, which downstream functions would break?" Tests whether they understood the dependency chain.

**What NOT to quiz:**
- Definitions ("What does API stand for?") — that's what the glossary tooltips are for
- File name recall ("Which file handles X?") — nobody memorizes file names
- Syntax details ("What's the correct way to write a fetch call?") — this isn't a coding bootcamp
- Anything that can be answered by scrolling up and copying — that tests scrolling, not understanding

**Quiz tone:**
- Wrong answers get encouraging, non-judgmental explanations ("Not quite — here's why...")
- Correct answers get brief reinforcement of the underlying principle ("Exactly! This works because...")
- Never punitive, never score-focused. No "You got 3/5!" — the quiz is a thinking exercise, not an exam
- Wrong answer explanations should teach something new, not just say "wrong, the answer was B"

**How many quizzes:** One per module, placed at the end after the learner has seen all the content. 3-5 questions per quiz. Each question should make the learner pause and *think*, not just pick the obvious answer.

**Deciding what concepts are worth quizzing:** Quiz the things that would actually help someone in practice — architecture understanding ("where does this logic live and why?"), debugging intuition ("what would cause this symptom?"), and decision-making ("what's the tradeoff here?"). If a concept won't help someone debug a problem, steer an AI assistant, or make an architectural decision, it's not worth quizzing.

---

## Design Identity

The visual design should feel like **Apple's product pages** — clean, confident, typographically rich, and almost entirely black-and-white. Read `references/design-system.md` for the full token system, but here are the non-negotiable principles:

- **Refined neutral baseline**: The entire course sits on warm ivory (#FAFAF8), never pure white. Alternating modules use a soft warm gray (#F3F3F1). The palette should feel like high-quality paper — not a hospital, not a coffee shop
- **System fonts first**: -apple-system / Inter stack. No decorative display fonts. Typography hierarchy comes from weight (300 for decorative numbers, 700 for titles) and size, not font variety
- **One accent color**: Apple blue (#0071E3) by default, used ONLY for interactive affordances — links, active states, buttons. Never for backgrounds or section headers
- **Frosted glass nav**: `backdrop-filter: blur(20px)` on the navigation bar — Apple's signature transparency
- **Module numbers in light weight**: Large (72px), thin (weight 300), gray — architectural, not attention-grabbing
- **Minimal shadows**: Prefer 1px borders over shadows. When shadows are used, they're barely visible (`rgba(0,0,0,0.04)`)
- **Content width 720px**: Tighter than typical — forces concise content and feels editorial
- **Alternating ivory / warm gray**: Modules alternate between `--color-bg` and `--color-bg-alt` — subtle rhythm, not colored sections
- **File type dots**: 6px colored dots before filenames in file trees — the ONLY place file-type color appears
- **Code blocks**: Near-black (#1C1C1E) with restrained syntax colors (no neon, no rainbow)

---

## Gotchas — Common Failure Points

These are real problems encountered when building courses. Check every one before considering a course complete.

### Tooltip Clipping
Translation blocks use `overflow: hidden` for code wrapping. If tooltips use `position: absolute` inside the term element, they get clipped by the container. **Fix:** Tooltips must use `position: fixed` and be appended to `document.body`. Calculate position from `getBoundingClientRect()`. This is already specified in the reference files but is the #1 bug that appears in every build.

### Not Enough Tooltips
The most common failure is under-tooltipping. Non-technical learners don't know terms like REPL, JSON, flag, entry point, PATH, pip, namespace, function, class, module, PR, E2E, or even software names like Blender/GIMP. **Rule of thumb:** if a term wouldn't appear in everyday conversation with a non-technical friend, tooltip it. Err heavily on the side of too many. BUT: don't tooltip terms the user already knows well from their domain (e.g., AI/ML concepts for someone in AI).

### Walls of Text
The course looks like a textbook instead of an infographic. This happens when you write more than 2-3 sentences in a row without a visual break. Every screen must be at least 50% visual. Convert any list of 3+ items into cards, any sequence into step cards or flow diagrams, any code explanation into a code↔English translation block.

### Recycled Metaphors
Using "restaurant" or "kitchen" for everything. Every module needs its own metaphor that feels inevitable for that specific concept. If you catch yourself reaching for the same metaphor twice, stop and find one that fits the concept organically.

### Code Modifications
Trimming, simplifying, or "cleaning up" code snippets from the codebase. The learner should be able to open the real file and see the exact same code. Instead of editing code to be shorter, *choose* naturally short snippets (5-10 lines) from the codebase that illustrate the point.

### Quiz Questions That Test Memory
Asking "What does API stand for?" or "Which file handles X?" — those test recall, not understanding. Every quiz question should present a new scenario the learner hasn't seen and ask them to *apply* what they learned.

### Scroll-Snap Mandatory
Using `scroll-snap-type: y mandatory` traps users inside long modules. Always use `proximity`.

### Module Quality Degradation
Trying to write all modules in one pass causes later modules to be thin and rushed. Build one module at a time and verify each before moving on.

### Missing Interactive Elements
A module with only text and code blocks, no interactivity. Every module needs at least one of: quiz, data flow animation, group chat, architecture diagram, drag-and-drop. These aren't decorations — they're how non-technical learners actually process information.

### Deep Dive: Flat Data Flow (no intermediate inspection)
In Deep Dive Mode, showing data flow as a flat arrow diagram without letting the user inspect intermediate data shapes. The whole point of the Data Pipeline Tracer is that you can click any stage and see "at this point, the data looks like THIS." Without inspectable intermediate states, the tracer is just another flow diagram.

### Deep Dive: Missing I/O Contracts
Showing a Package Anatomy Card without specifying what goes in and what comes out. Every function listed in the card must have its input args and return type visible — even if simplified to plain English like "takes a list of chapters, returns a comparison table."

### Deep Dive: Git Diff Without Context
Showing a list of changed files without connecting them to the architecture diagram. The value of git diff tracking is seeing "this file changed → it affects THIS data flow path → which means THIS downstream output might be different." Always overlay changes on the existing module map.

---

## Reference Files

The `references/` directory contains detailed implementation specs. Read them when you reach the relevant phase:

- **`references/design-system.md`** — Complete CSS custom properties, color palette, typography scale, spacing system, shadows, animations, scrollbar styling. Read this before writing any CSS.
- **`references/interactive-elements.md`** — Implementation patterns for every interactive element: drag-and-drop quizzes, multiple-choice quizzes, code↔English translations, group chat animations, message flow visualizations, architecture diagrams, pattern cards, callout boxes. Read this before building any interactive elements.
- **`references/deep-dive-elements.md`** — Implementation patterns for Deep Dive Mode elements: Package Anatomy Cards, Data Pipeline Tracers, Git Diff Overlays. Read this before building any Deep Dive module.
