---
name: presentation-visual-orchestrator
description: Route and govern high-quality presentation/deck work before execution. Use for PPT, HTML deck, pitch deck, boss deck, public sharing, demo deck, slide redesign, visual QA, image-generation planning, screenshot treatment, native PPTX vs HTML deck engine selection, or when Jianan mentions PVO.
---

# Presentation Visual Orchestrator (PVO)

PVO is the presentation director above concrete slide engines. It decides audience, narrative, style, page type, image strategy, output engine, and visual QA before `frontend-slides`, `jianan-presentation-system`, PPTX tools, or image generation execute.

## Core rule

Do not start by making slides. Start by routing the expression.

```text
User request
→ presentation type
→ audience + takeaway
→ output engine
→ style lock
→ page plan
→ image manifest
→ execution skill
→ visual QA
→ delivery + memory
```

## When to use

Use PVO for T2+ or quality-sensitive presentation work:

- public sharing / internal sharing / training deck
- boss decision deck / executive update / budget ask
- product demo / launch / wow-moment deck
- technical architecture/codebase analysis deck
- aesthetic/style-gallery deck
- PPT/image/cover/screenshot redesign
- any deck where visual quality, image handling, or narrative fit matters

Skip PVO for one-off wording edits unless the user asks for structural/visual judgment.

## Quick routing

| User intent | Default route |
|---|---|
| high-aesthetic web deck / live sharing | `frontend-slides` after PVO locks style/page plan |
| native editable PowerPoint required | `jianan-presentation-system` or PPTX/native PPT route |
| boss/customer decision | PVO + decision logic + native PPTX if editability matters |
| public knowledge sharing | PVO + frontend HTML deck or PPTX depending delivery context |
| image/cover/screenshot treatment | PVO image manifest + image generation/editing route |
| only narrative/script | PVO brief + narrative outline, no visual execution yet |

## Required gates

### 1. Presentation type
Pick one primary type. Do not mix goals casually.

1. Codebase / architecture hard-core analysis
2. Product promotion / wow demo
3. Knowledge sharing / teaching
4. Aesthetic design showcase
5. Boss decision deck
6. Internal execution plan

### 2. Project brief
Capture:

- audience
- current belief
- desired belief after the deck
- one key takeaway
- one action/decision requested
- output format: HTML deck / PPTX / images / outline only

If ambiguous, ask at most 1–3 questions. If not blocking, make assumptions and state them.

### 3. Output engine

| Need | Engine |
|---|---|
| polished browser presentation, strong visual identity, easy sharing | HTML deck / `frontend-slides` |
| real editable PowerPoint shapes/text/charts | native PPTX route / PPT Master-style pipeline |
| social cover / article cover / visual asset | image route |
| screenshot proof / product UI evidence | screenshot treatment route |

### 4. Style lock
For T2+ decks, create or update a `STYLE_LOCK.md` with:

- style family
- palette
- typography
- layout system
- density level
- image rules
- motion rules
- forbidden styles

Style lock exists to prevent long-deck drift.

### 5. Page plan
Before execution, write one short record per page:

```text
P03
Type: evidence page
Goal: prove the system runs end-to-end
Layout: Big Screenshot Tabs / Image Hero / Comparison / Timeline
Image slot: 21:9 screenshot proof
Takeaway: AI can produce a complete asset pipeline, not just isolated copy
```

### 6. Image manifest
For generated or transformed visuals, create `IMAGE_MANIFEST.md`:

```text
page: P05
type: system diagram / documentary photo / screenshot redesign / data poster / cover
slot_ratio: 21:9
source: user / generated / screenshot / web
must_preserve: UI text / data / brand / none
style: match deck style lock
file: images/05-system-loop.png
prompt_or_instruction: ...
```

Rules:

- decide slot ratio before generating images;
- images are embedded assets, not mini-slides: no title, footer, page number, corner mark, border decoration;
- Chinese decks use Chinese labels inside information graphics;
- preserve real screenshots unless the user asks for redesign or the screenshot is unusable;
- generated files go into `images/` with `{page}-{semantic-name}` naming.

### 7. Visual QA
Before delivery, check:

- every slide has one takeaway;
- no viewport overflow or unreadable tiny text;
- screenshots are legible;
- images fit slots and do not collide with nav/footer;
- style does not drift;
- information density matches deck type;
- user phrases/constraints are preserved;
- repo hygiene is clean.

## References

- `references/guizang-ppt-absorption.md` — rules absorbed from guizang-ppt-skill.
- `references/ppt-master-absorption.md` — rules absorbed from PPT Master-style native PPTX pipeline.
- `references/pvo-artifacts.md` — templates for brief, style lock, page plan, image manifest, QA.
