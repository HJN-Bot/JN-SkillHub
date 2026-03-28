# Visual Style Guide — Jianan Presentation System

> **⚑ AUTHORITATIVE SOURCE (P1)**: This file is the single source of truth for all colors, typography, and layout patterns. All other reference files defer to this document. When any conflict exists between this file and any other file, this file wins.

This document captures the complete visual design system extracted from Jianan's R·Agent presentation (18 slides). Every color, spacing, component, and layout pattern is documented for faithful reproduction.

---

## 1. Color System

### Primary Palette
| Role | Hex | Usage |
|------|-----|-------|
| **Brand Orange** | `#E87722` | Slide titles, accent borders, CTA buttons, chevron fills, highlight numbers |
| **Brand Teal** | `#009999` | Secondary headers, info cards, teal-filled sections, "Variable"/"Solution" blocks |
| **Black** | `#000000` | Body text, dark background blocks, footer text |
| **White** | `#FFFFFF` | Slide background, text on dark blocks |
| **Light Gray** | `#F5F5F5` | Card backgrounds, table alternating rows |
| **Medium Gray** | `#666666` | Captions, secondary labels, de-emphasized text |

### Semantic Colors (used in AI output demos)
| Role | Hex | Usage |
|------|-----|-------|
| **Diff Green** | `#4CAF50` | 新增内容 (New Content) highlights in comparison tables |
| **Diff Red** | `#E53935` | 删除内容 (Deleted Content) highlights |
| **Diff Amber** | `#FF9800` | 变化内容 (Changed Content) highlights |
| **Status Green** | `#4CAF50` | Checkmark badges ✓, "已上传" (Uploaded) status |
| **Alert Red** | `#D32F2F` | 有差异 (Has Difference) badges, warning callouts |

### Color Application Rules
- **Slide titles**: ALWAYS orange (`#E87722`), bold, 36-44pt
- **Section sub-headers inside slides**: Teal (`#009999`), bold, 20-24pt
- **Orange vs Teal decision**: Orange = primary action/emphasis; Teal = secondary info/categorization
- **Dark backgrounds**: Used sparingly — only for high-contrast callout blocks (e.g., footer summary sentences, "Next Step" badges)
- **Never use blue** as a primary color. The entire palette avoids corporate blue.

---

## 2. Typography

### Font Stack

**CRITICAL: 12pt is the absolute minimum for any visible text on a slide.** Never go below 12pt — information density is achieved through structured components, NOT by shrinking fonts.

> **10pt Exception (Progressive Roadmap Matrix only)**: When all four conditions are met — (1) N×M matrix with N≥4 columns and M≥3 rows, (2) splitting would break cross-column comparative value, (3) cell text is already maximally compressed, (4) presenter will guide verbally — 10pt is permitted. This exception applies exclusively to Template 10 (slide-templates.md). Do NOT generalize it to other slide types.

| Element | Font | Size | Weight | Color |
|---------|------|------|--------|-------|
| Slide title | Arial Black / Impact | 32-40pt | Bold | Orange `#E87722` |
| Section header (inside slide) | Arial Bold | 18pt | Bold | Black (with orange/teal icon left) |
| Body text / bullet text | Arial | 14pt | Regular | Black |
| Challenge box text | Arial | 12pt | Regular, centered | Black or Dark Gray |
| Table header | Arial Bold | 12pt | Bold | White on orange background |
| Table body | Arial | 12pt | Regular | Black |
| Metric callout number | Arial Black | 28-36pt | Bold | Orange or Teal |
| Metric label | Arial | 12pt | Regular | Medium Gray `#888888` |
| Workflow step label | Arial | 12pt | Regular | Black |
| Tag pill text | Arial Bold | 9pt | Bold | White (on colored pill) |
| Caption / source line | Arial | 10pt | Regular | Gray `#999999` |
| Chinese body text | 微软雅黑 / SimHei | 12-14pt | Regular | Black |

### Typography Rules
- **Title position**: Top-left of slide, 0.5-0.8" from top edge, left-aligned
- **Title can be multi-line**: Up to 2 lines is acceptable (see Slide 5 "User Pain Points" wrapping)
- **Header hierarchy is critical**: Section headers (Chapter Scope, Technical Challenges, Process Flow, Quality Gate) MUST be 18pt — visually larger than 12-14pt body text. Bold alone is NOT enough to establish hierarchy; the size difference must be obvious.
- **Number emphasis**: KPI metrics use 28-36pt bold number + 12pt label beneath. Never go above 36pt for metrics — the original PPT uses proportional emphasis, not enormous numbers.
- **12pt rule enforcement**: Challenge descriptions, table cells, bullet items, workflow labels, metric labels — ALL use 12pt minimum. The ONLY exceptions below 12pt are: tag pills (9pt bold), source footnotes (10pt), slide page numbers (12pt), and Progressive Roadmap Matrix cell content (10pt — see exception block above).
- **Bilingual on-slide text**: Chinese and English coexist. Headers can be English-only; detail content often Chinese. Technical terms always in English.

---

## 3. Layout System

### Grid & Margins
- **Slide dimensions**: Standard 16:9 (13.33" × 7.5")
- **Margins**: 0.5" all sides minimum
- **Company logo**: Top-right corner, Siemens Healthineers logo
- **Page number**: Bottom-right, 14pt, dark gray
- **Footer**: Bottom-right, "Restricted © Siemens Healthineers, yyyy", 10pt gray

### Master Layout Patterns

#### Pattern A: Left-Explain / Right-Prove (most common)
```
┌─────────────────────────────────────────────────────┐
│ [TITLE - Orange, Bold, 36-44pt]          [LOGO]     │
│                                                      │
│  ┌──────────────┐    ┌──────────────────────────┐   │
│  │  Methodology │    │  Evidence / Screenshot /  │   │
│  │  • Steps     │    │  AI Output / Data Table   │   │
│  │  • Process   │    │                           │   │
│  │  • Flow      │    │  (Real product output     │   │
│  │              │    │   or HTML-rendered demo)   │   │
│  │  Quality Gate│    │                           │   │
│  │  [metrics]   │    │                           │   │
│  └──────────────┘    └──────────────────────────┘   │
│                                              [PAGE#] │
└─────────────────────────────────────────────────────┘
```
**Used in**: Slides 3, 4, 6, 7, 8 (Framework Gen, Consistency Check, Template-based, Comparison, Diff Analysis)

**Split ratio**: ~40% left (explanation) / ~60% right (evidence)

#### Pattern B: Three-Column KPI Banner + Content Below
```
┌─────────────────────────────────────────────────────┐
│ [TITLE]                                    [LOGO]   │
│ ┌──────────┐ ┌──────────────┐ ┌──────────────┐     │
│ │ KPI #1   │ │ KPI #2       │ │ KPI #3       │     │
│ │ -8Day ⚡  │ │ 70% Auto 🔄  │ │ >80% Acc ☑  │     │
│ └──────────┘ └──────────────┘ └──────────────┘     │
│                                                      │
│  ┌─────────────────┐  ┌─────────────────────────┐  │
│  │  Detail Table   │  │  Chart / Breakdown      │  │
│  │  or Gantt       │  │  Stacked bar / etc.     │  │
│  └─────────────────┘  └─────────────────────────┘  │
└─────────────────────────────────────────────────────┘
```
**Used in**: Slide 14 (Project Effectiveness)

#### Pattern C: Central Diagram + Flanking Cards
```
┌─────────────────────────────────────────────────────┐
│ [TITLE]                                    [LOGO]   │
│                                                      │
│ ┌─────────┐    ┌───────────┐    ┌─────────────┐    │
│ │ Left    │    │  Central  │    │  Right      │    │
│ │ Cards   │    │  Diagram  │    │  Cards      │    │
│ │ (orange │    │  (funnel/ │    │  (teal      │    │
│ │  bg)    │    │   flow)   │    │   bordered) │    │
│ └─────────┘    └───────────┘    └─────────────────┘ │
└─────────────────────────────────────────────────────┘
```
**Used in**: Slide 15 (Ecosystem), Slide 17 (Transferability)

#### Pattern D: Horizontal Timeline / Chevron Flow
```
┌─────────────────────────────────────────────────────┐
│ [TITLE]                                    [LOGO]   │
│ ┌──────────┐                                        │
│ │ Phase 1  │  detail bullets                        │
│ └──────────┘                                        │
│                                                      │
│ [01]►─[02]►─[03]►─[04]►─[05]►                     │
│  │      │      │      │      │                      │
│  date   date   date   date   date                   │
│                                                      │
│ ┌──────────┐           ┌──────────┐                 │
│ │ Phase 2  │  detail   │ Phase 3  │  detail         │
│ └──────────┘ bullets   └──────────┘ bullets         │
└─────────────────────────────────────────────────────┘
```
**Used in**: Slide 16 (FY26 Plan)

#### Pattern E: Photo Collage + Summary Cards
```
┌─────────────────────────────────────────────────────┐
│ [TITLE]                                    [LOGO]   │
│                                                      │
│  ┌─────┐ ┌─────┐ ┌─────┐                           │
│  │ img │ │ img │ │ img │  (screenshots/photos      │
│  │     │ │     │ │     │   at slight rotation)     │
│  └─────┘ └─────┘ └─────┘                           │
│                                                      │
│ ┌──────────┐ ┌──────────┐ ┌──────────┐             │
│ │ Card 1   │ │ Card 2   │ │ Card 3   │             │
│ │ (dark bg)│ │ (gray bg)│ │ (orange  │             │
│ │          │ │          │ │  border) │             │
│ └──────────┘ └──────────┘ └──────────┘             │
└─────────────────────────────────────────────────────┘
```
**Used in**: Slide 1 (NMPA AI Development Strategy)

#### Pattern F: Full-Screen UI Screenshot
```
┌─────────────────────────────────────────────────────┐
│                                                      │
│  [Full-screen screenshot of actual product UI]      │
│  - Left sidebar navigation visible                  │
│  - Step progress bar at top                         │
│  - Main content area showing real data              │
│                                                      │
│                                              [PAGE#] │
└─────────────────────────────────────────────────────┘
```
**Used in**: Slides 9, 10, 11, 12 (UI Demo screenshots)

#### Pattern G: Matrix / Roadmap Table
```
┌─────────────────────────────────────────────────────┐
│ [TITLE]                                    [LOGO]   │
│      ┌─────────┬─────────┬─────────┬─────────┐     │
│      │ V1      │ V2      │ V3      │ V4      │     │
│ ─────┼─────────┼─────────┼─────────┼─────────┤     │
│ ROI  │ ...     │ ...     │ ...     │ ...     │     │
│ ─────┼─────────┼─────────┼─────────┼─────────┤     │
│ Tech │ ...     │ ...     │ ...     │ ...     │     │
│ ─────┼─────────┼─────────┼─────────┼─────────┤     │
│ Res  │ ...     │ ...     │ ...     │ ...     │     │
│      └─────────┴─────────┴─────────┴─────────┘     │
│ [footnote]                                   [PAGE#]│
└─────────────────────────────────────────────────────┘
```
**Used in**: Slide 18 (Function Plan / Roadmap)

---

## 4. Component Library

### 4.1 Challenge Box (Technical Challenges)
**This component is critical — it appears on every feature demo slide (Slides 6, 7, 8).**

- Shape: Rounded rectangle, `border-radius: 8px`
- Border: **2px solid #E87722** (orange) — NOT gray, NOT thin
- Background: **White (#FFFFFF)** — NOT gray
- Text: 12pt, centered, black or dark gray
- Title line (optional): 12pt bold orange text on top
- Description: 12pt regular, centered, 2-3 lines max
- Width: Equal 1/3 of left column, with 8-12px gaps between boxes
- Height: ~80-100px

```css
/* HTML rendering spec */
.challenge-box {
  background: #FFFFFF;
  border: 2px solid #E87722;
  border-radius: 8px;
  padding: 12px 14px;
  text-align: center;
  font-size: 12pt;
  color: #333333;
  min-height: 80px;
  display: flex;
  align-items: center;
  justify-content: center;
}
```

**WRONG (previous version)**: Gray background `#F7F7F7` + thin gray border → loses brand identity
**CORRECT**: White background + thick orange border → matches Slides 6/7/8 exactly

### 4.2 Chevron Arrow (Timeline Steps)
- Shape: Pentagon/chevron arrow pointing right
- Fill: Gradient from orange to dark (or solid orange/teal/gray per phase)
- Content: Two-line — top line: step number in circle ("01"), bottom line: phase name
- Below each chevron: date range in small text
- Chevrons are horizontally connected, overlapping slightly

### 4.3 Numbered Circle Badge
- Shape: Circle, 32-40px diameter (larger than before — must be visually prominent)
- Fill: Orange `#E87722` (for process steps) or White with black/teal border (for funnel layers)
- Content: Single number "1", "2", "3" in white bold text (or black on white bg)
- Usage: Flow diagrams, step indicators
- **Size matters**: These circles should be ~0.35" in PPTX, clearly visible alongside 12pt text labels
- Variation: Teal circle for secondary sequences

### 4.4 Progress Bar (Chapter Scope)
- Height: ~20px
- Segments: Multiple colored blocks representing different chapter proportions
- Labels: Percentage on top of each segment
- Colors: Orange for primary segment, teal for secondary, gray for remainder
- Example: `[10% orange][45% teal][15% gray]` = Chapter scope visualization

### 4.5 Card Block

#### Type A: Slide-13 Information Card (PREFERRED for methodology/principle cards)
This is Jianan's most polished card pattern, extracted from Slide 13 (Tech page). Structure:
1. **Orange/Teal header block** (rounded top): Chinese title (20pt bold) + English subtitle (12pt)
2. **Teal checkmark circle** (connecting header to body)
3. **"Overview" teal pill** → lettered points (a. b. c.) with 12pt text
4. **"Approach" teal pill** → lettered points with bold keywords + regular descriptions

```
┌──────────────────────────┐
│ 设计原则                  │  ← Orange/teal fill, 20pt bold white
│ Design Principles         │  ← 12pt white
└──────────────────────────┘
  ✓ (teal checkmark circle)

  [Overview]  ← teal pill
  a. Point one description
  b. Point two description

  [Approach]  ← teal pill  
  a. Bold keyword: regular description
  b. Bold keyword: regular description
```

- Orange header for primary concepts; Teal header for secondary/metrics
- Lettering (a. b. c.) in teal bold, description in black regular 12pt
- Bold keywords followed by regular descriptions within lettered items
- Pills: 10pt bold white text on teal rounded rectangle

#### Type B: Simple Filled Card
- **Orange filled card**: `background: #E87722; color: white; border-radius: 10px; padding: 20px`
  - Title: 14pt bold white
  - Subtitle: 10pt white, 80% opacity
  - Body bullets: 14pt white, with round bullet (●)
- **Teal bordered card**: `background: white; border: 2px solid #009999; border-radius: 10px; padding: 20px`
  - Title: 14pt bold teal
  - Body: 12pt black
- **Dark card**: `background: #333333; color: white; border-radius: 10px; padding: 20px`

### 4.6 Quality Gate Block
- Layout: 2-3 metric columns at bottom of feature slides, separated by teal top-border line
- Each metric: **28-36pt bold number** (orange or teal) + **12pt label** below (gray)
- Examples: ">95% / Accuracy", "<3s / Generation Speed", "✓ / Intervention Friendly"
- Background: Clean white, with a 1.5px teal horizontal line as top separator
- **Do NOT shrink these numbers below 28pt** — they are the "hero" element of each feature slide

### 4.7 Comparison Table
- Header row: Orange background (`#E87722`), white bold 12pt text
- Body rows: White background, 12pt text, no alternating colors
- Borders: 1px solid `#E0E0E0`
- Difference cells: Color-coded with semantic colors (green/red/amber highlights)
- Special badge: "有差异" in red-bordered rounded rectangle
- **Table must be readable at arm's length** — 12pt minimum for all cells

### 4.8 Flow Diagram (Process Steps)
- Horizontal flow with numbered circles connected by arrows
- Circle size: **0.35" diameter** in PPTX (not tiny — must be visually prominent)
- Each step: `[Number Circle] → [Label Text below]`
- Label: 12pt, centered below each circle
- Arrow style: Simple thin → connecting circles
- Step count: Usually 3-4 steps
- Container: Often inside a section with "Workflow" header + icon

### 4.9 Funnel Diagram (Layered Architecture)
**This is a signature visual — extracted from Slide 17.** Can be rendered in PPTX (using progressively narrower rectangles) or HTML (for trapezoid clip-path).

- Shape: Stacked rectangles, each narrower than the one above
- **Layers MUST physically touch** — no gaps, no arrows between layers. The visual flow comes from proximity and width reduction alone.
- Color progression: Orange (#E87722) → Teal (#009999) → Dark (#333333) — or gray gradient for neutral funnels
- Width reduction: Each layer is ~0.7" narrower (0.35" per side) than the layer above
- Each layer contains: White numbered circle (01-03) left-aligned + bold title + subtitle + detail line
- Layer height: ~1.5-1.6" each, giving room for 3 lines of text
- Bottom label: Orange pill "Converging Control" or equivalent, positioned 0.15" below the last layer
- Left/right flanking: Use Slide-13-style information cards (Type A) for explanation

```css
/* Funnel layer CSS spec */
.funnel-layer {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  padding: 0 24px;
  color: white;
  font-size: 14pt;
  clip-path: polygon(3% 0%, 97% 0%, 100% 100%, 0% 100%);
  /* Each subsequent layer: increase clip-path inset by 3% */
}
.funnel-layer .num-circle {
  width: 36px; height: 36px;
  background: white;
  border-radius: 50%;
  color: #333;
  font-weight: bold;
  font-size: 14px;
  display: flex; align-items: center; justify-content: center;
  margin-right: 14px;
  flex-shrink: 0;
}
```

### 4.10 Stacked Bar Chart (Budget/Proportion)
- Horizontal bar, full width of evidence panel
- Segments color-coded: orange, dark orange, teal, light teal, gray
- Each segment: Label inside if wide enough (≥15%), otherwise below
- Label: 12pt bold white (inside) or 10pt gray (outside)
- Height: ~50px
- Use pptxgenjs BAR chart (stacked horizontal) or HTML rendering
- **Prefer chart over static rectangles** — charts are more professional and editable

---

## 5. Slide Composition Rules

### Rule 1: No Empty Space
Every slide should feel "full but not cramped." If there's a large blank area, fill it with a supporting visual (chart, screenshot, or card block).

### Rule 2: Evidence Must Be Visible
For any claim on the left side, the right side must show REAL evidence — AI-generated output, product screenshots, data tables, or actual document content. Never use placeholder mockups.

### Rule 3: Maximum Three Visual Zones
Each slide has at most 3 major content zones. More than 3 creates visual chaos.

### Rule 4: Consistent Component Reuse
The same component (numbered circles, progress bars, quality gates) should appear across multiple slides to create visual coherence. Don't invent new visual metaphors for each slide.

### Rule 5: HTML-Rendered Diagrams for Complex Visuals
For complex visuals (architecture diagrams, funnel diagrams, comparison tables with color-coded highlights), **always create HTML/CSS and screenshot**. PPT native shapes cannot achieve the required polish. Simple elements (titles, bullets, basic tables, charts) go directly into PPTX.

### Rule 6: 12pt Minimum Enforcement
Every text element visible on the final slide must be ≥12pt. If content doesn't fit at 12pt, restructure the layout or split across slides — NEVER shrink the font.

### Rule 7: Internal Padding in All Containers
Every card, box, panel, and bordered region must have visible internal padding. Content should NEVER touch the edges of its container. Minimum padding: 12px in HTML, 0.15" in PPTX. For nested containers (e.g., context structure list inside evidence panel), add a white sub-card with its own border and padding to create visual separation.

---

## 6. McKinsey Exhibit Principles

These principles from McKinsey consulting methodology are integrated into Jianan's presentation system:

### 6.1 Pyramid Principle — Title = Takeaway
Every slide title should communicate the key conclusion, not just the topic. The audience should understand the slide's message from the title alone.

**BAD**: "Technical Architecture"  
**BETTER**: "Tech" (minimalist, let diagram speak)  
**BEST** (McKinsey): "Dual-layer architecture enables 50% cross-BU reuse"

Apply selectively: Use takeaway titles for impact/result slides; use short topic titles for demo/walkthrough slides where evidence speaks for itself.

### 6.2 MECE Layouts — Mutually Exclusive, Collectively Exhaustive
Each section within a slide should cover one distinct dimension without overlap:
- Left column: HOW (methodology, process, challenges)
- Right column: WHAT (evidence, output, data)
- Bottom strip: SO WHAT (metrics proving it works)

### 6.3 Exhibit Thinking — Every Slide Is Self-Contained
Each slide should be understandable WITHOUT the oral narration. Someone flipping through the deck should grasp each slide's message independently. This means:
- Title delivers the conclusion
- Evidence panel shows proof
- Quality Gate quantifies the claim
- Optional source line: "Source: R·Agent PoC V3, CT BU, Jan 2025"

### 6.4 Visual Hierarchy — 3 Levels of Reading
A well-designed slide has 3 reading speeds:
1. **3-second scan**: Title + KPI numbers tell the story
2. **15-second read**: Section headers + flow diagram + evidence summary
3. **60-second study**: Table details + full evidence content

---

## 7. Dual-Track Output Strategy

### Track A: HTML Rendering (high fidelity)
Use for: Funnel diagrams, architecture flows, color-coded comparison tables, complex multi-element layouts.

- Render at 1400×788px (16:9 ratio matching LAYOUT_WIDE)
- Screenshot at 2x resolution for crisp embedding
- Output as standalone .html file for browser viewing AND as embedded image in PPTX
- All text at CSS 14px (≈10.5pt print) minimum, which renders as 12pt+ when viewed at slide scale

### Track B: Native PPTX (editable)
Use for: Titles, bullets, simple tables, chart objects, text-only cards, Quality Gate metrics.

- pptxgenjs LAYOUT_WIDE (13.3" × 7.5")
- All addText calls use fontSize ≥ 12
- Charts via addChart (editable in PowerPoint)
- Tables via addTable (editable cells)

### Combined Approach
For a typical feature demo slide:
1. Left column: **Native PPTX** (section headers, challenge boxes as shapes, workflow as shapes+icons, Quality Gate as text)
2. Right column: **HTML screenshot** embedded as image (high-fidelity evidence panel with color-coded content, data tables, charts)
3. Result: Left side is fully editable in PowerPoint; right side is a polished image

```javascript
// Example: embed HTML screenshot into PPTX right column
slide.addImage({
  path: "evidence-panel-slide3.png",
  x: 5.4, y: 1.1, w: 7.4, h: 5.8
});
```

---

## 8. HTML Rendering Specifications

When creating HTML for screenshot capture:

```css
/* Base styles for slide-embeddable HTML */
body {
  font-family: Arial, 'Microsoft YaHei', sans-serif;
  margin: 0;
  padding: 20px;
  background: white;
}

/* 12pt minimum = 16px in CSS for slide-scale rendering */
body { font-size: 16px; }

/* Orange accent */
.accent-orange { color: #E87722; }
.bg-orange { background: #E87722; color: white; }

/* Teal accent */
.accent-teal { color: #009999; }
.bg-teal { background: #009999; color: white; }

/* Card component */
.card {
  border-radius: 10px;
  padding: 20px 22px;
  margin: 10px 0;
}

/* Challenge box - CORRECT style */
.challenge-box {
  background: #FFFFFF;
  border: 2px solid #E87722;
  border-radius: 8px;
  padding: 14px 16px;
  text-align: center;
  font-size: 16px; /* 12pt equivalent */
  min-height: 80px;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Table */
table {
  border-collapse: collapse;
  width: 100%;
  font-size: 16px; /* 12pt equivalent */
}
th {
  background: #E87722;
  color: white;
  padding: 10px 14px;
  text-align: left;
  font-weight: bold;
}
td {
  padding: 10px 14px;
  border-bottom: 1px solid #E0E0E0;
}

/* Numbered step circle */
.step-circle {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: #E87722;
  color: white;
  font-weight: bold;
  font-size: 16px;
}

/* Quality Gate metric */
.qg-number {
  font-size: 32px; /* 24pt equivalent */
  font-weight: 900;
  color: #E87722;
}
.qg-label {
  font-size: 16px; /* 12pt equivalent */
  color: #888888;
}
```

### Rendering workflow:
1. Create a single HTML file with all content
2. Set viewport to 1400×788 (matches 16:9 LAYOUT_WIDE proportion)
3. Screenshot at 2x resolution for crisp rendering
4. Trim whitespace if needed
5. Place into PPT slide's right-side content zone or use as full-slide render

---

## 9. Diagram Drawing Guide

This section captures the specific drawing techniques Jianan uses, extracted from the 18-slide R·Agent deck. Each diagram type has a reference slide and detailed construction rules.

### 9.1 Funnel / Layered Architecture Diagram
**Reference**: Slide 17 (Project Transferability)

**Construction rules:**
1. Layers are stacked rectangles with **ZERO gap** between them — they physically touch
2. Each layer is narrower than the one above: reduce width by ~0.7" total (0.35" per side)
3. Color progression should be smooth: Orange (#E87722) → Teal (#009999) → Dark (#333333). For neutral funnels: Light gray → Medium gray → Dark gray → Black
4. Each layer contains:
   - White numbered circle (01/02/03) — 0.4" diameter, left-aligned at 0.25" from layer left edge
   - Bold title (18pt white) — right of circle
   - Subtitle (12pt white) — below title
   - Detail keywords (10pt white) — optional bottom line with · separators
5. Bottom label: Orange pill "Converging Control" or equivalent, 0.15" below last layer
6. **NO arrows between layers** — the tapering shape itself communicates convergence

**In PPTX (pptxgenjs):**
```javascript
// Layer 1 (widest)
sl.addShape(pres.shapes.RECTANGLE, { x: 4.0, y: 1.2, w: 5.0, h: 1.6, fill: { color: "E87722" } });
// Layer 2 (medium) — note x shifts right, w shrinks
sl.addShape(pres.shapes.RECTANGLE, { x: 4.35, y: 2.8, w: 4.3, h: 1.6, fill: { color: "009999" } });
// Layer 3 (narrowest)
sl.addShape(pres.shapes.RECTANGLE, { x: 4.7, y: 4.4, w: 3.6, h: 1.4, fill: { color: "333333" } });
```

**In HTML (for clip-path trapezoids — higher fidelity):**
```css
.layer { clip-path: polygon(3% 0%, 97% 0%, 100% 100%, 0% 100%); }
/* Each subsequent layer: increase inset by 3% */
```

### 9.2 Architecture Flow Diagram
**Reference**: Slide 13 (Tech) — left side

**Construction rules:**
1. Vertical flow: Top → Bottom, connected by thin arrows
2. Box styles vary by function:
   - **UI Layer**: Light green background + green dashed border
   - **Hand Layer**: Beige/cream background + labeled
   - **Brain Layer**: Diamond shape (rotated square) with gradient fill
3. Small file-type badges (PDF, DOC, CSV) above the top entry point
4. Person icon at top (input) and bottom-left (monitoring)
5. Arrows: Thin (1px), dark, with small arrowheads
6. This diagram MUST be rendered in HTML — too complex for PPT shapes

**Adjacent to the flow diagram**: Slide-13 Information Cards (see Section 4.5 Type A) explaining the architecture's two key properties.

### 9.3 Circular Agile Process Diagram
**Reference**: Slide 15 (AI PoC Ecosystem)

**Construction rules:**
1. Central element: Large oval/circle outline (thin gray/teal stroke)
2. Inside: 3 gray circles side-by-side (BU/User, PM, Dev) with white labels
3. Teal "Design" pill at top of oval, "Test" pill at bottom
4. Gray directional arrows along the oval path (clockwise)
5. Left side: "Traditional" → "Pain Points" (teal circle with white text) → into oval
6. Right side: out of oval → "Solution" (teal circle) → "AI-Augmented" (dark pill)
7. Four flanking cards (orange bg): Business Layer, PoC Team, Strategic Layer, Leadership Layer

### 9.4 Process Flow (Workflow Steps)
**Reference**: Slides 6, 7, 8 — "Workflow" section

**Construction rules:**
1. Orange numbered circles: 0.35" diameter in PPTX, left-to-right
2. Circle contains white number (1, 2, 3, 4) at 14pt bold
3. Below each circle: 12pt label text, centered
4. Between circles: Thin gray → arrow at 16pt, subtle (NOT bold, NOT large)
5. Spacing: ~1.25" center-to-center between steps
6. Section header: 18pt bold "Process Flow" with teal sync icon (🔄) to the left

### 9.5 Section Icons
Every section header (Chapter Scope, Technical Challenges, Process Flow, Quality Gate) has an icon to its left:
- **Chapter Scope**: File document icon (📄) — orange
- **Technical Challenges**: Gear icon (⚙️) — orange
- **Process Flow**: Sync/cycle icon (🔄) — teal
- **Quality Gate**: Checkmark circle (✓) — teal

Icon size: 0.28" × 0.28" in PPTX. Positioned at the same x as the left column, with the 18pt header text starting 0.35" to the right.

In pptxgenjs, generate these icons using react-icons → sharp → base64 PNG:
```javascript
const { FaCog, FaSyncAlt, FaCheckCircle, FaFileAlt } = require("react-icons/fa");
// Render at 256px, then embed at 0.28" × 0.28"
```

---

## 10. PPTX Implementation Reference

### Slide dimensions
```javascript
pres.layout = "LAYOUT_WIDE"; // 13.3" × 7.5"
```

### Bullet style
```javascript
// Round dot bullet — CORRECT
{ text: "Item text", options: { bullet: { code: "25CF" }, breakLine: true } }
// NEVER use unicode • in text — causes double bullets
```

### Challenge box
```javascript
// White bg + orange border — CORRECT
sl.addShape(pres.shapes.ROUNDED_RECTANGLE, {
  x: bx, y: by, w: 1.55, h: 1.0,
  fill: { color: "FFFFFF" },
  line: { color: "E87722", width: 1.5 },
  rectRadius: 0.06
});
// Text inside: 12pt, centered
sl.addText(desc, {
  x: bx + 0.1, y: by + 0.05, w: 1.35, h: 0.9,
  fontSize: 12, fontFace: "Arial", color: "333333",
  align: "center", valign: "middle", margin: 0
});
```

### Quality Gate separator + metrics
```javascript
// Teal line separator
sl.addShape(pres.shapes.LINE, {
  x: lx, y: qy, w: lw, h: 0,
  line: { color: "009999", width: 1.2 }
});
// Metric number
sl.addText(">90%", {
  fontSize: 28, color: "E87722", bold: true, align: "center"
});
// Metric label
sl.addText("Context\nprecision", {
  fontSize: 12, color: "888888", align: "center"
});
```

### Evidence panel with nested sub-card
```javascript
// Outer evidence panel
sl.addShape(pres.shapes.ROUNDED_RECTANGLE, {
  x: 5.8, y: 1.05, w: 7.0, h: 6.0,
  fill: { color: "FAFAFA" },
  line: { color: "E87722", width: 1.2 },
  rectRadius: 0.08
});
// Inner white sub-card for nested content (adds padding)
sl.addShape(pres.shapes.ROUNDED_RECTANGLE, {
  x: 6.0, y: 5.75, w: 6.6, h: 1.2,
  fill: { color: "FFFFFF" },
  line: { color: "E0E0E0", width: 0.5 },
  rectRadius: 0.06
});
```

### Slide-13 Information Card construction
```javascript
// 1. Colored header block
sl.addShape(pres.shapes.ROUNDED_RECTANGLE, {
  x: cx, y: cy, w: 3.4, h: 0.85,
  fill: { color: "E87722" }, rectRadius: 0.08 // or "009999" for teal
});
sl.addText("设计原则", { // 20pt Chinese title
  x: cx+0.2, y: cy+0.08, w: 3.0, h: 0.4,
  fontSize: 20, color: "FFFFFF", bold: true
});
sl.addText("Design Principles", { // 12pt English subtitle
  x: cx+0.2, y: cy+0.46, w: 3.0, h: 0.25,
  fontSize: 12, color: "FFFFFF"
});
// 2. Teal checkmark (generated PNG)
sl.addImage({ data: tealCheckPng, x: cx, y: cy+0.95, w: 0.35, h: 0.35 });
// 3. "Overview" pill
sl.addShape(pres.shapes.ROUNDED_RECTANGLE, {
  x: cx+0.05, y: cy+1.45, w: 1.0, h: 0.3,
  fill: { color: "009999" }, rectRadius: 0.06
});
sl.addText("Overview", { fontSize: 10, color: "FFFFFF", bold: true, align: "center" });
// 4. Lettered points
sl.addText([
  { text: "a. ", options: { color: "009999", bold: true } },
  { text: "Description text here", options: { breakLine: true } },
  { text: "b. ", options: { color: "009999", bold: true } },
  { text: "Another point" }
], { fontSize: 12, color: "333333" });
```

