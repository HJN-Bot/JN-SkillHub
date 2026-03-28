---
name: jianan-presentation-system
description: "Jianan's end-to-end presentation creation system: Startup Intake + 3-layer workflow. TRIGGER for any presentation, slide deck, pitch deck, PPT, oral script, speaker notes, bilingual content, animated diagrams, data charts, Gantt charts, GIFs for PPT, or content beautification/translation. Layers: (1) Content Beautify — optimize/translate MD scripts, extract GitHub repos into content; (2) PPT Design — generate fully editable PPTX with native shapes/charts/text using pptxgenjs; (3) Animation — static charts (pptxgenjs native), Gantt/timeline, HTML/CSS particle flow GIFs, Manim 3D architecture GIFs. Also trigger for: '帮我做PPT', '优化这个稿子', '翻译成英文', '帮我做甘特图', '节点流动GIF', '架构动画', '把GitHub项目做成动图', '做个能嵌PPT的动图', '起始交互'."
---

# Jianan Presentation System

End-to-end presentation creation: from raw notes to fully editable PPTX + companion oral scripts + embedded GIF animations.

## Workflow Architecture

```
启动 → Startup Intake（起始交互层）
         ↓
         ├── Layer 1: Content Beautify（内容美化/优化/翻译）
         ├── Layer 2: PPT Design（设计生成可编辑 PPTX）
         └── Layer 3: Animation（静态图表 + 动效 GIF）
```

Each layer can be used independently or in sequence.

## Quick Reference

| Need | Read |
|------|------|
| **[START HERE]** 起始交互问卷 + Session Brief | [references/startup-intake.md](references/startup-intake.md) |
| Layer 1: 内容美化/翻译/GitHub提炼 | [references/content-beautify.md](references/content-beautify.md) |
| Layer 2: Visual design rules (colors, layout, components) | [references/visual-style.md](references/visual-style.md) |
| Layer 2: Content logic & narrative structure | [references/content-logic.md](references/content-logic.md) |
| Layer 2: Slide-type templates with specifications | [references/slide-templates.md](references/slide-templates.md) |
| Layer 2: Slide layout archetypes (13 types with measurements) | [references/slide-layout-library.md](references/slide-layout-library.md) |
| Layer 2: Oral script writing rules | [references/oral-script-guide.md](references/oral-script-guide.md) |
| Layer 3: Animation workflow (charts / Gantt / HTML / Manim / GIF) | [references/animation-workflow.md](references/animation-workflow.md) |
| Layer 3: HTML/CSS 动图完整制作指南 | [references/html-animation-guide.md](references/html-animation-guide.md) |

---

## PPTX Editability — Iron Rules

**All deliverables must be fully editable in PowerPoint. No exceptions.**

| Element | Must be | Implementation |
|---------|---------|---------------|
| Slide titles | Native text box | pptxgenjs `addText()` |
| Body text / bullets | Native text box | pptxgenjs `addText()` |
| Tables | Native table | pptxgenjs `addTable()` |
| Data charts (bar/line/pie) | Native chart | pptxgenjs `addChart()` |
| Gantt chart bars | Native shapes | pptxgenjs `addShape()` |
| Simple flow diagrams | Native shapes + text | pptxgenjs `addShape()` + `addText()` |
| Complex HTML diagrams | Embedded image (acceptable) | Screenshot → `addImage()` |
| Animated GIFs | Embedded media | `addImage()` with .gif |

**Fonts**: All text must use explicit `fontSize` matching the hierarchy below. Never leave font size unset.

**Speaker Notes**: Always add oral script as `addNotes()` for every slide.

---

## Core Philosophy

### "Structure, not shrinkage"
Information density is achieved through **structured visual components** (tables, charts, flow diagrams, card grids), NOT by shrinking fonts. If content doesn't fit at 12pt minimum, restructure the layout or split across slides.

### "Evidence on the right"
The left side explains methodology; the right side PROVES it with real output, screenshots, or data. No claim on the left should stand without evidence on the right.

### "Every slide is a self-contained exhibit"
Following McKinsey exhibit thinking, each slide should be understandable without narration — title delivers the conclusion, evidence shows proof, Quality Gate quantifies the claim.

---

## Font Size Hierarchy (NON-NEGOTIABLE)

This hierarchy was validated across three design iterations. Violating it produces slides that look unprofessional.

| Element | Size | Weight | Notes |
|---------|------|--------|-------|
| Slide title | 32-40pt | Bold | Orange #E87722, top-left |
| Section header (inside slide) | **18pt** | Bold | Must be visibly larger than body text. Bold alone is NOT enough — size difference must be obvious |
| Subtitle / card header | 14-16pt | Bold | Used in evidence panel titles, card titles |
| Body text / bullets | 14pt | Regular | Black, round bullet (●) |
| Challenge box text | 12pt | Regular | Centered in white+orange-border box |
| Table body | 12pt | Regular | All table cells |
| Metric labels | 12pt | Regular | Gray #888888, below metric numbers |
| Workflow step labels | 12pt | Regular | Below numbered circles |
| KPI metric numbers | 28-36pt | Bold | Orange or Teal, HERO element |
| Tag pill text | 9pt | Bold | White on colored pill (only exception below 12pt) |
| Source footnote | 10pt | Regular | Gray, bottom of slide |

**ABSOLUTE MINIMUM: 12pt for any readable text.** Only tag pills (9pt) and source footnotes (10pt) may go below.

---

## Diagram & Visual Drawing Rules

These rules were learned through iteration — each one addresses a specific failure mode.

### Rule 1: Layers MUST physically touch
In funnel/architecture diagrams, stacked layers must have ZERO gap between them. The visual flow comes from proximity and progressive width reduction — NOT from arrows. Remove all ▼ arrows between stacked layers.

### Rule 2: Progressive narrowing creates hierarchy
Each layer should be ~0.35"/side narrower than the layer above (or ~10-12% width reduction). The visual tapering IS the communication of convergence. Colors should also progress: warm/bright (top) → cool/neutral (middle) → dark (bottom).

### Rule 3: White numbered circles inside colored blocks
Use white-background circles (32-40px) with dark text for layer numbering (01, 02, 03). Position left-aligned within each layer. These circles create visual anchoring and rhythm.

### Rule 4: Orange-border boxes, NOT gray-background boxes
Technical Challenge boxes MUST be: white background + 2px orange border (#E87722) + 8px border-radius. NEVER gray background — it loses brand identity and looks generic.

### Rule 5: Cards follow the Slide-13 pattern
For methodology/principle cards, use the Information Card pattern: colored header block (20pt Chinese title + 12pt English subtitle) → teal checkmark circle → "Overview" teal pill → lettered points (a. b. c. in teal bold) → "Approach" teal pill → lettered points with bold keywords. This is Jianan's signature card style from Slide 13 (Tech page), also used for 模块化架构 and 结构化Prompt包.

### Rule 6: All containers need internal padding
Every card, box, panel, and bordered region must have ≥0.15" internal padding in PPTX (≥12px in HTML). Content must NEVER touch container edges. For nested containers (e.g., context structure inside evidence panel), add a white sub-card with its own border and padding.

### Rule 7: Charts over static shapes
For data distribution (budget allocation, workload breakdown), use native pptxgenjs charts (stacked bar, pie) rather than manually positioned rectangles. Charts are editable in PowerPoint and look more professional.

### Rule 8: Bottom-of-slide content must justify its existence
If text at the bottom of a slide is too small to read comfortably, it's either not important enough to include OR it should be integrated into the main content area at full size. Don't waste space on decorative taglines — either make them 14pt+ or remove them entirely.

### Rule 9: Flow arrows and connectors
Workflow arrows between numbered step circles should use thin gray → characters at 16pt, NOT large bold arrows or ▼ triangles. Keep them subtle — they are connectors, not focal points.

### Rule 10: Refer to Jianan's original slides for visual quality
When in doubt about how a diagram should look, reference these specific slides from the R·Agent deck:
- **Slide 13 (Tech)**: Left-side architecture flow with UI Layer → Hand Layer → Brain (diamond) → UI Layer → Hand Layer; Right-side Slide-13 Information Cards with colored headers, checkmarks, pills
- **Slide 17 (Transferability)**: 4-layer funnel with gray gradient, white numbered circles, left "Unchanged" orange cards, right "Variable" teal cards
- **Slide 15 (Ecosystem)**: Central circular diagram (Design → BU/PM/Dev → Test cycle) with flanking explanation cards
- **Slides 6/7/8 (Feature Demos)**: Chapter Scope + Technical Challenges (orange-border white boxes) + Process Flow (numbered circles) + Quality Gate (metric numbers)

---

## Creation Workflow

### Step 0: Startup Intake（每次必做）

Run the startup questionnaire from [references/startup-intake.md](references/startup-intake.md).
Output a **Session Brief** and wait for confirmation before proceeding.

### Step 1 (Layer 1): Content Beautification

If user provides MD draft / oral notes / GitHub link:
- Run content diagnosis → optimize → output refined MD
- Translate to English or produce bilingual version if needed
- See [references/content-beautify.md](references/content-beautify.md)

### Step 2 (Layer 2): PPT Design

1. Read layout-library + visual-style + content-logic before starting
2. Determine slide count and narrative arc
3. For each slide: pick layout archetype → populate native elements → add speaker notes
4. **Output**: `.js` script using pptxgenjs → run → produce `.pptx` file

**Deliverables checklist per slide:**
- [ ] Title: native text box, 32-40pt Bold Orange
- [ ] Body: native text boxes, 12-14pt Regular
- [ ] Tables: `addTable()` — never screenshots
- [ ] Charts: `addChart()` — never manual rectangles
- [ ] Speaker notes: `addNotes()` with full oral script

### Step 3 (Layer 3): Animation

For each slide needing visual enhancement:

| Need | Tool | Output |
|------|------|--------|
| Bar / line / pie chart | pptxgenjs `addChart()` | Native PPTX (editable) |
| Gantt / timeline | pptxgenjs `addShape()` grid | Native PPTX (editable) |
| Complex static diagram | HTML → screenshot | Image embedded in PPTX |
| Node flow / particle animation | HTML/CSS → GIF | GIF embedded in PPTX |
| Architecture layer traversal | Manim → GIF | GIF embedded in PPTX |

> See [references/animation-workflow.md](references/animation-workflow.md) for all code templates.
5. **QA every slide**: Convert to image, check for alignment, text overflow, spacing issues, container padding.

---

## Common Pitfalls (from 3 rounds of iteration)

| Pitfall | What went wrong | Correct approach |
|---------|----------------|-----------------|
| Font too small | Used 8-10pt to fit more content | Restructure layout at 12pt minimum |
| Section headers same size as body | 14pt bold headers, 14pt regular body — no visible hierarchy | Headers 18pt, body 12-14pt |
| Gray challenge boxes | #F7F7F7 background — looks generic | White bg + 2px orange border |
| Arrows between funnel layers | Added ▼ between layers — looks clunky | Layers touch directly, zero gap |
| Content touching container edges | No padding inside panels or sub-cards | ≥0.15" padding, use white sub-cards |
| Static rectangles for data viz | Manually positioned colored rectangles | Use pptxgenjs stacked bar chart (editable) |
| Decorative bottom taglines | Small text at page bottom — unreadable | Integrate into main content or remove |
| Wrong bullet symbols | Used ▸ or custom unicode | Round dot ● (code "25CF" in pptxgenjs) |
| Flat architecture blocks | Same-width rectangles — no hierarchy | Progressive narrowing + color gradient |
| Generic card style | Plain bordered rectangle with text | Slide-13 pattern: header + pills + a.b.c. |
| Converging control too close to tagline | Elements stacked at bottom without breathing room | Ensure ≥0.15" spacing between bottom elements |
| Evidence panel too cramped | Multiple sections squeezed without separation | Use sub-section titles at 16pt bold + white sub-cards |

---

## Key Design Principles Summary

### DO:
- **12pt minimum for ALL body text** — structure creates density, not small fonts
- **18pt for section headers** — must be visibly larger than 12-14pt body
- Use **left-explain / right-prove** two-column for feature slides
- Use **white + orange-border boxes** for Technical Challenge blocks
- Use **Slide-13 Information Card** pattern for methodology cards
- Make funnel layers **touch with zero gap** and progressively narrow
- Use **native pptxgenjs charts** for data distribution
- Ensure **≥0.15" padding** inside every container
- Use **round bullet ●** for all bullet lists
- Use **thin gray → arrows** between workflow steps

### DON'T:
- **NEVER go below 12pt** for readable text
- **NEVER use gray background** for challenge boxes
- **NEVER put arrows between stacked funnel layers**
- **NEVER let content touch container edges**
- **NEVER put small decorative text at slide bottom** — integrate or remove
- Don't create text-only slides with just bullets
- Don't use generic blue — stick to orange/teal/black palette
