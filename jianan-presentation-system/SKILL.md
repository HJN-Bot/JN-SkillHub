---
name: jianan-presentation-system
description: "Jianan's end-to-end presentation creation system for high-persuasion pitches and decks. Use this skill whenever Jianan asks to create a presentation, slide deck, pitch deck, or PPT — for R·Agent, AI PoC demos, executive presentations, investor pitches, product launches, or any technical project requiring stakeholder buy-in. Also trigger when Jianan asks to draft oral scripts, speaker notes, bilingual (Chinese+English) presentation content, objection-handling backup slides, or asks how to improve a pitch's structure / hook / wow moment / unfair advantage. Use even for partial requests like 'help me design one slide' or 'write the oral script for this section.'"
---

# Jianan Presentation System (v2)

A comprehensive skill for creating high-persuasion presentations matching Jianan's proven visual style and content logic. Produces synchronized deliverables: **PPT slides** + **companion oral scripts** (Chinese + English) + **objection-handling backup slides**.

**v2 upgrade**: This system now handles the full range of pitch scenarios — from internal budget asks to investor pitches to product launches — through a layered architecture:
- **5-Beat Universal Arc** as the spine of every deck
- **6-Phase Internal Expansion** (the original v1 structure) preserved for internal scenarios
- **Three pitch archetypes** (Cold Open / Wow Moment / Why Us-Why Now) drawn from YC pitch coaching, Apple keynotes, and Stripe Press / a16z memos
- **Objection-handling discipline** that pre-empts adversarial questions

---

## Quick Reference

| Need | Read |
|------|------|
| **Scenario routing & 6 scenario packs (NEW v3)** | [references/scenario-packs.md](references/scenario-packs.md) |
| Visual design rules (colors, layout, components, diagrams) | [references/visual-style.md](references/visual-style.md) |
| Content logic & narrative structure (5-Beat + 6-Phase + 3-tier compression) | [references/content-logic.md](references/content-logic.md) |
| Cold Open / Wow Moment / Why Us archetypes | [references/pitch-archetypes.md](references/pitch-archetypes.md) |
| Objection handling & R·Agent objection library | [references/objection-handling.md](references/objection-handling.md) |
| Slide-type templates with specifications | [references/slide-templates.md](references/slide-templates.md) |
| Oral script writing rules | [references/oral-script-guide.md](references/oral-script-guide.md) |

---

## Step 0: Scenario routing (NEW in v2)

Before doing anything else, answer these three questions. The answers determine which beats expand, which compress, and which archetypes deploy.

```
1. WHO IS LISTENING?
   ├── Internal leadership (knows you, knows the company)        → invoke 6-Phase inside 5-Beat
   ├── HQ / cross-org technical team                             → 5-Beat + complementarity framing
   ├── External investor / VC                                    → 5-Beat only, full archetypes
   ├── Industry conference / public talk                         → 5-Beat, Insight-heavy
   └── Product launch / press / customer event                   → 5-Beat, Wow-centered

2. HOW LONG?
   ├── 3 min  (elevator)         → ~5 slides,  Wow + Insight + Ask only
   ├── 15 min (standard)         → ~10-14 slides, full 5-Beat
   └── 45 min (deep-dive)        → ~22-30 slides + 5-8 backup slides

3. WHAT IS THE GOAL?
   ├── Budget / title / headcount approval → Layer 2 (6-Phase) inside Beats 3-4
   ├── Mindset shift / mental model        → Layer 1 only, lead with Insight
   ├── Product launch / new capability     → Layer 1, Wow Moment is centerpiece
   └── Inspirational / TED-style           → Layer 1, Cold Open is centerpiece
```

If unclear, **ask Jianan before starting**. Do not default — the wrong default produces the wrong deck.

---

## Core Philosophy (v2)

### "Wow before Why" (NEW)
Persuasion structure inverts teaching structure. v1 ordered slides as approach → demo → numbers. v2 orders them as **result first, explanation second**. The audience must see the undeniable Wow before the methodology, otherwise they're informed but not gripped.

### "Name the Elephant" (NEW)
Proactively surfacing the audience's strongest objection makes it weaker. Every deck identifies 2-3 elephants and answers them before the audience can ask. See `objection-handling.md`.

### "Structure, not shrinkage" (preserved from v1)
Information density is achieved through **structured visual components** (tables, charts, flow diagrams, card grids), NOT by shrinking fonts. If content doesn't fit at 12pt minimum, restructure the layout or split across slides.

### "Evidence on the right" (preserved from v1)
The left side explains methodology; the right side PROVES it with real output, screenshots, or data. No claim on the left should stand without evidence on the right.

### "Every slide is a self-contained exhibit" (preserved from v1)
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
| Wow Moment headline (NEW) | 44-60pt | Bold | Dominates the Wow Moment slide |
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

### Rule 10: Wow Moment slides break the visual grid (NEW in v2)
The Wow Moment slide is intentionally minimal: no logo, no title bar, no agenda hints. Just the before/after visual + the t-shirt sentence. Breaking the grid signals "this is the moment that matters."

### Rule 11: Refer to Jianan's original slides for visual quality
When in doubt about how a diagram should look, reference these specific slides from the R·Agent deck:
- **Slide 13 (Tech)**: Left-side architecture flow with UI Layer → Hand Layer → Brain (diamond) → UI Layer → Hand Layer; Right-side Slide-13 Information Cards with colored headers, checkmarks, pills
- **Slide 17 (Transferability)**: 4-layer funnel with gray gradient, white numbered circles, left "Unchanged" orange cards, right "Variable" teal cards
- **Slide 15 (Ecosystem)**: Central circular diagram (Design → BU/PM/Dev → Test cycle) with flanking explanation cards
- **Slides 6/7/8 (Feature Demos)**: Chapter Scope + Technical Challenges (orange-border white boxes) + Process Flow (numbered circles) + Quality Gate (metric numbers)

---

## Creation Workflow (v2)

When asked to create a presentation:

1. **Step 0 — Scenario routing**: confirm audience, length, goal (see above). If ambiguous, ask before proceeding.
2. **Read ALL six reference files** before starting any content creation. New files in v2: `pitch-archetypes.md` and `objection-handling.md`.
3. **Pre-deck checklist** (from `content-logic.md` Section 8): complete every box before drafting.
4. **Workshop the objections** (from `objection-handling.md`): list 5 candidate objections, score them, identify top 3 for in-deck surfacing.
5. **Determine slide count and beat structure** using the 5-Beat arc and the 3-tier length table.
6. **For each slide**: select the appropriate slide-type template, populate with content, and write the companion oral script.
7. **Produce deliverables**:
   - **PPTX file** (LAYOUT_WIDE 13.3"×7.5"): editable in PowerPoint — titles, bullets, tables, charts as native elements
   - **HTML files** for complex diagrams: funnel architectures, color-coded comparison tables, flow diagrams with rounded connectors — screenshot and embed into PPTX as images
   - **Companion oral script** in Markdown (Chinese + English versions), with `[PAUSE 5s]` markers at Wow Moment
   - **Backup slides** for top 3-5 objections (hidden from main flow)
8. **QA every slide**: convert to image, check for alignment, text overflow, spacing issues, container padding.

---

## Common Pitfalls (from 3 rounds of iteration + v2 additions)

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
| **NEW: No Cold Open** | Started with self-introduction or agenda slide | Open with one of the four archetypes |
| **NEW: Distributed Wow** | Spread evidence across multiple "interesting" slides | Compress into ONE Wow Moment slide |
| **NEW: Multiple Asks** | Ended with 3-4 things to approve | Pick exactly one binary decision |
| **NEW: Filling the pause** | Speaker keeps talking through the Wow reveal | Mark `[PAUSE 5-10s]` and hold silence |
| **NEW: Generic "Why Us"** | "We have a great team" | Three-column matrix vs. named competitors |
| **NEW: No objection prep** | Q&A becomes improvisation | Workshop top 3-5 objections before delivery |
| **NEW: 6-Phase for external audience** | Walked investor through internal capability ladder | Compress 6-Phase into Beat 3 only |

---

## Key Design Principles Summary

### DO:
- **Run Step 0 (scenario routing) before any content work** — wrong audience model breaks the deck
- **Open with a Cold Open archetype** — never with self-intro or agenda
- **Make the Wow Moment the gravitational center** — one slide, three acts (Setup → Reveal → Pause)
- **Use the Why Us three-column matrix** for any high-stakes pitch
- **Workshop 3-5 objections** before drafting
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
- **NEVER skip Step 0** — defaulting produces the wrong deck
- **NEVER open with self-introduction or agenda** — Cold Open first
- **NEVER explain during the Wow Reveal** — the pause is the moment
- **NEVER have multiple Wow Moments** — pick one, demote the rest
- **NEVER pitch externally with the 6-Phase structure** — it's the wrong rhythm for unfamiliar audiences
- **NEVER end with multiple Asks** — one binary decision only
- **NEVER go below 12pt** for readable text
- **NEVER use gray background** for challenge boxes
- **NEVER put arrows between stacked funnel layers**
- **NEVER let content touch container edges**
- **NEVER put small decorative text at slide bottom** — integrate or remove
- Don't create text-only slides with just bullets
- Don't use generic blue — stick to orange/teal/black palette
