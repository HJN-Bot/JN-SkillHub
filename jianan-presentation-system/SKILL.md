---
name: jianan-presentation-system
description: "Jianan's end-to-end presentation creation system for enterprise AI project pitches. Use this skill whenever Jianan asks to create a presentation, slide deck, pitch deck, or PPT — especially for R·Agent, AI PoC demos, executive presentations, or any technical project requiring stakeholder buy-in. Also trigger when Jianan asks to draft oral scripts, speaker notes, or bilingual (Chinese+English) presentation content, create animated diagrams (Manim 3D architecture flows, HTML/CSS particle animations with SVG offset-path), generate GIFs for PPT embedding via QuickTime+FFmpeg or Puppeteer, or produce explainer animations. Also trigger for: '做个流程动图', '节点流动的GIF', '把架构图做成动图', '循环流程GIF', '做个能嵌PPT的动图'. This skill captures the VISUAL DESIGN SYSTEM (layout, color, typography, component patterns), the CONTENT LOGIC SYSTEM (narrative structure, slide-to-speech mapping, bilingual strategy), and the ANIMATION SYSTEM (Manim 3D scenes, HTML CSS animations, GIF export workflow). Use even for partial requests like 'help me design one slide', 'write the oral script for this section', 'make an architecture animation', or 'turn this into a GIF for my PPT'."
---

# Jianan Presentation System

A comprehensive skill for creating enterprise-grade presentations matching Jianan's proven visual style and content logic. Produces two synchronized deliverables: **PPT slides** and **companion oral scripts** (in both Chinese and English).

## Quick Reference

| Need | Read |
|------|------|
| Visual design rules (colors, layout, components, diagrams) | [references/visual-style.md](references/visual-style.md) |
| Content logic & narrative structure | [references/content-logic.md](references/content-logic.md) |
| Slide-type templates with specifications | [references/slide-templates.md](references/slide-templates.md) |
| Oral script writing rules | [references/oral-script-guide.md](references/oral-script-guide.md) |
| Animation workflow (Manim / HTML / GIF export) | [references/animation-workflow.md](references/animation-workflow.md) |
| HTML/CSS 动图完整制作指南（模板+录制+PPT嵌入） | [references/html-animation-guide.md](references/html-animation-guide.md) |

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

When asked to create a presentation:

1. **Read ALL four reference files** before starting any content creation.
2. **Determine slide count and narrative arc** using the content-logic guide.
3. **For each slide**: select the appropriate slide-type template, populate with content, and write the companion oral script.
4. **Produce deliverables**:
   - **PPTX file** (LAYOUT_WIDE 13.3"×7.5"): editable in PowerPoint — titles, bullets, tables, charts as native elements
   - **HTML files** for complex diagrams: funnel architectures, color-coded comparison tables, flow diagrams with rounded connectors — screenshot and embed into PPTX as images
   - **HTML CSS animations** for node-relation flows with SVG offset-path particles — record/screenshot to GIF
   - **Manim 3D animations** for architecture data flows, layer-traversal effects — render to MP4 then convert to GIF
   - **GIF files** for all animated content — embed into PPTX slides via addImage/addMedia
   - **Companion oral script** in Markdown (Chinese + English versions)

   > Animation type decision: data flow across layers → **Manim 3D**; node network with particle connections → **HTML CSS**; static diagram → **PPTX native**. See [references/animation-workflow.md](references/animation-workflow.md).
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
