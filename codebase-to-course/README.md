# Codebase-to-Course (Extended)

A Claude Code skill that turns any codebase into a beautiful, interactive single-page HTML course — extended with **Deep Dive Mode** for multi-layer code understanding.

> **Original**: [zarazhangrui/codebase-to-course](https://github.com/zarazhangrui/codebase-to-course)
> **Extended by**: Jianan — added Deep Dive Mode, Package Anatomy Cards, Data Pipeline Tracer, Git Diff Overlay

## What it does

Point it at a repo. Get back a stunning, self-contained course that teaches how the code works — with scroll-based navigation, animated visualizations, embedded quizzes, and code-with-plain-English side-by-side translations.

### Extended capabilities (new)

- **Deep Dive Mode** — Five-layer progressive zoom: module map → package anatomy → data flow tracing → function-level code → git diff tracking
- **Package Anatomy Cards** — Expandable interactive cards showing each package's I/O contract, core functions, dependencies, and output data shapes
- **Data Pipeline Tracer** — Animated step-by-step data transformation visualization with clickable stages and intermediate state inspection (Data IN / Data OUT / Code tabs)
- **Git Diff Overlay** — Visualize what changed between commits, highlight affected data paths on the architecture diagram, show downstream impact analysis

## Two modes

### Standard Mode
The original experience. 5-8 module course covering the full codebase. Best for first-time understanding.

### Deep Dive Mode
Triggered by "deep dive into [module]" or "trace the pipeline." Focused 3-5 module course on a specific package or pipeline, going much deeper:

| Layer | Shows | Element |
|-------|-------|---------|
| L1 | Module collaboration map | Interactive architecture diagram |
| L2 | Package anatomy (purpose, functions, I/O) | Package Anatomy Card |
| L3 | Data flow with intermediate states | Data Pipeline Tracer |
| L4 | Function-level code reading | Code ↔ English translations |
| L5 | What changed (git diff) | Diff overlay on architecture |

## Installation

### For Claude Code
```bash
cp -r codebase-to-course ~/.claude/skills/
```

### For Claude.ai (web interface)
Upload as a user skill in Claude's skill settings, or reference the files directly in conversation.

## File structure

```
codebase-to-course/
├── SKILL.md                              # Main skill instructions (extended)
├── README.md                             # This file
└── references/
    ├── design-system.md                  # CSS tokens, typography, colors, layout
    ├── interactive-elements.md           # Standard interactive element patterns
    └── deep-dive-elements.md             # NEW: Package Anatomy, Pipeline Tracer, Git Diff
```

## Who this is for

**"Vibe coders"** — people who build software by instructing AI coding tools in natural language. You've built something. It works. But you don't really understand how it works under the hood.

The Deep Dive extension is especially useful for:
- **AI/Product owners** who need to understand data pipelines they didn't write
- **Teams** where multiple developers touch different modules and you need to see who changed what
- **Post-processing heavy systems** (like LLM pipelines) where data transforms through many layers before reaching the final output

## Design principles

- Every screen is at least 50% visual
- Max 2-3 sentences per text block
- Real code from the project, never modified
- Metaphors first, then reality
- Quizzes test application, not memory
- Single HTML file output — no dependencies, works offline
