# Slide Type Templates — Jianan Presentation System

Each template below is a reusable pattern extracted from Jianan's actual slides. When creating a new presentation, select the appropriate template for each slide's purpose, then populate with content.

---

## Template 1: Strategic Context Slide

**Purpose**: Establish external urgency / market signals
**Used in**: Slides 1-2 (NMPA Strategy, Industry Trends)
**Layout**: Pattern E (Photo Collage + Summary Cards)

### Structure
```
TOP ZONE (60%):
  - 2-4 screenshots/photos of external evidence
  - Slight rotation (-3° to +3°) for visual dynamism
  - Sources: government websites, news articles, competitor announcements

BOTTOM ZONE (40%):
  - 3 summary cards in a row
  - Card 1: Dark background (#333) — Policy interpretation
  - Card 2: Medium gray background (#666) — Market context
  - Card 3: Orange border — Implications for our company
  - Each card: 3-4 lines of text, 12-14pt
```

### Content Formula
```
Title: [Topic] + [Strategic Framing]
  Example: "NMPA AI Development Strategy"
  Example: "Industry Trends and Internal Needs"

Photo zone: Real screenshots from authoritative sources
  - Government policy documents
  - Competitor product screenshots
  - Internal workshop photos

Card 1: "What authorities are doing"
Card 2: "What competitors are doing" 
Card 3: "What our internal teams are saying"
```

---

## Template 2: Feature Demo Slide (Core Pattern)

**Purpose**: Present one AI capability with evidence
**Used in**: Slides 3, 4, 6, 7, 8
**Layout**: Pattern A (Left-Explain / Right-Prove)

### Structure
```
LEFT COLUMN (40%):
  ┌──────────────────────┐
  │ 📊 Chapter Scope     │  ← Scope indicator
  │ "Chapters 1-3  10%"  │
  │ [====........] 10%   │  ← Progress bar
  ├──────────────────────┤
  │ ⚙️ Technical         │
  │    Challenges        │  ← 3 challenge boxes
  │ ┌────┐┌────┐┌────┐  │
  │ │ C1 ││ C2 ││ C3 │  │
  │ └────┘└────┘└────┘  │
  ├──────────────────────┤
  │ 🔄 Process Flow      │  ← Numbered steps
  │ ①→②→③→④            │
  ├──────────────────────┤
  │ ✅ Quality Gate       │  ← Metric callouts
  │ >95%  <3s   ✓       │
  │ Acc.  Speed  Friendly│
  └──────────────────────┘

RIGHT COLUMN (60%):
  ┌──────────────────────────────┐
  │                              │
  │  [AI-Generated Output]       │
  │  - Real document content     │
  │  - Color-coded highlights    │
  │  - Table with actual data    │
  │                              │
  │  (Screenshot of actual       │
  │   product output or          │
  │   HTML-rendered demo)        │
  │                              │
  └──────────────────────────────┘
```

### Sub-component Specifications

**Chapter Scope Block**:
- Header: "Chapter Scope" at **18pt bold** with document icon 📄 (orange, 0.28")
- Chapter range: "Chapters 1-3" or "Chapter 4" at 12pt gray
- Percentage: Teal number at **34pt bold**, right-aligned — e.g., "10%", "55%", "70%"
- Progress bar below: Orange fill for completed portion on #F0F0F0 gray track, 0.2" height, rounded

**Technical Challenges Block**:
- Header: "Technical Challenges" at **18pt bold** with gear icon ⚙️ (orange, 0.28")
- 3 boxes side-by-side, each with:
  - **White background (#FFFFFF) + 2px orange border (#E87722)** — NOT gray background
  - 2-line description, centered, **12pt**
  - Border-radius: 8px
  - Width: ~1/3 of left column each, with 0.1" gaps between boxes
  - Height: ~1.0"

**Process Flow Block**:
- Header: "Process Flow" at **18pt bold** with cycle icon 🔄 (teal, 0.28")
- Numbered orange circles at **0.35" diameter** (NOT tiny), containing white numbers
- Thin gray → arrows (16pt) between circles — subtle connectors, NOT focal points
- Label text below each circle: **12pt**, centered
- Horizontal layout, left-to-right, ~1.25" center-to-center spacing

**Quality Gate Block**:
- Teal horizontal line (1.2px) as top separator
- 2-3 metric columns below the line
- Metric number: **28-36pt bold**, orange or teal — the "HERO" element
- Metric label: **12pt**, gray (#888888), below the number
- Standard metrics: Accuracy / Speed / Intervention-Friendliness

---

## Template 3: Pain Point & Solution Slide

**Purpose**: Present the problem and map it to AI solutions
**Used in**: Slide 5 (CER User Pain Points)
**Layout**: Two-column with problem-solution mapping

### Structure
```
LEFT COLUMN (50%):
  Title: "[Document Type]" in bold
  Subtitle: 1-2 sentence context (why this document matters)
  
  Pain point badges:
  (A) Heavy Workload  (B) Numerous Input
  (C) Slow Comparison (D) Difficult Judgment
  
  Volume chart: Bar chart showing FY demand
  Caption: "Average of X files per FY, requiring ~Y man-months per project"
  
  Foundation blocks:
  [Data] "SSME has rich data resources..."
  [Expert] "Experts own specialized know-how..."
  
  Summary sentence (bold, orange): Confidence statement

RIGHT COLUMN (50%):
  Pain-to-solution mapping:
  [Structured Sessions] ──→ "Reduce manual extraction and review"
  [Numerous Sources]    ──→ "Replace manual entry and formatting"
  [Slow Comparison]     ──→ "Reduce human effort in highlighting"
  [Difficult Judgment]  ──→ "Enable draft by feature & clinical perspective"
  
  Workflow arrow chain:
  [Data Processing] → [Formatting] → [Diff Checking] → [Evaluation]
  
  Coverage statement: "Covers over 70% of overall workflow"
```

---

## Template 4: UI Demo Slide

**Purpose**: Show actual product interface
**Used in**: Slides 9-12
**Layout**: Pattern F (Full-Screen UI Screenshot)

### Structure
```
FULL SLIDE:
  - Screenshot of actual web application
  - Left sidebar: Navigation menu with active state highlighted
  - Top area: Step progress bar showing current stage
  - Main area: Actual product content/interaction

  Optional overlay annotations:
  - Small callout boxes pointing to key UI elements
  - Step number indicators if showing a multi-step flow
```

### Content Rules
- Screenshots must be REAL product output, not mockups
- UI should show Chinese language interface (actual user context)
- Navigation sidebar should be visible to show product scope
- Progress indicators should reflect the step being demonstrated
- Color-coded highlights in the product should use the standard diff colors

---

## Template 5: Architecture / Tech Slide

**Purpose**: Explain technical system design
**Used in**: Slide 13 (Tech)
**Layout**: Pattern A variant — Left diagram + Right explanation cards

### Structure
```
LEFT (40%): Architecture Diagram (HTML-rendered)
  ┌─────────────────────┐
  │     UI LAYER        │ ← Input zone
  │  Multi-source Upload│
  ├─────────────────────┤
  │     HAND LAYER      │ ← Traditional processing
  │  Organization +     │
  │  Keyword Extraction │
  ├─────────────────────┤
  │     BRAIN           │ ← LLM processing (diamond shape)
  │  Diff Highlight     │
  │  Classification     │
  ├─────────────────────┤
  │     UI LAYER        │ ← Output zone
  │  Modification +     │
  │  Monitoring         │
  ├─────────────────────┤
  │     HAND LAYER      │ ← Post-processing
  │  Data Coordination  │
  └─────────────────────┘

RIGHT (60%): Two explanation cards
  ┌─────────────────────────┐
  │ 模块化架构              │  ← Card 1: Architecture
  │ Modular Architecture    │
  │                         │
  │ Overview: ...           │
  │ Approach: a. ..., b. ...│
  └─────────────────────────┘
  
  ┌─────────────────────────┐
  │ 结构化Prompt包          │  ← Card 2: Prompt Design
  │ Structured Prompt Pkg   │
  │                         │
  │ Overview: ...           │
  │ Approach: a. ..., b. ...│
  └─────────────────────────┘
  
  BOTTOM: Next Step arrow chain
  [Next Step] ▶ LLMs Post-training ▶ Architecture Enhancement ▶ Expanded Dataset
```

---

## Template 6: Effectiveness / KPI Dashboard Slide

**Purpose**: Quantify project impact
**Used in**: Slide 14 (Project Effectiveness)
**Layout**: Pattern B (Three-Column KPI Banner + Detail)

### Structure
```
TOP BANNER: Three KPI cards in a row
  ┌──────────────┐ ┌────────────────┐ ┌──────────────────┐
  │ Slow Manual  │ │ Complex        │ │ Professional     │
  │ Process      │ │ Comparison     │ │ Threshold        │
  │ -8Day ⚡     │ │ 70% Auto 🔄   │ │ >80% Accuracy ☑ │
  └──────────────┘ └────────────────┘ └──────────────────┘

LEFT DETAIL (50%): Before/After comparison table
  "AI+ Paradigm"
  | Actions | Manual | AI Augmented | Improvement |
  | Data    | 3 hrs  | 5 min+Review | >40 times   |
  | Content | 4 hrs  | 8 min+Review | >24 times   |
  | Format  | 2 hrs  | 2 min+Review | >30 times   |
  
  Gantt chart: Project timeline comparison
  CUC Team: [----10D----][Review]
  AI+ Team: [2D][Review]  → "-8 Days" annotation

RIGHT DETAIL (50%): Functional applicability
  "V1+V3 Functional Applicability"
  • Strong functional applicability
  • Easily replicable architecture
  
  Stacked bar chart by chapter:
  CH1, CH2, CH3, CH4 broken into:
  - Template (orange segment)
  - Content (teal segment)  
  - Comparison (dark segment)
```

---

## Template 7: Ecosystem / Organization Slide

**Purpose**: Show the team, resources, and process that enable success
**Used in**: Slide 15 (AI PoC Ecosystem)
**Layout**: Pattern C (Central Diagram + Flanking Cards)

### Structure
```
CENTER: Circular agile process diagram
  - Outer ring: Design → Test → (cycle)
  - Inner circles: BU/User, PM, Dev (3 gray circles)
  
  Left of cycle: "Traditional" → "Pain Points" (teal circle)
  Right of cycle: "Solution" → "AI-Augmented" (dark pill)

FLANKING CARDS:
  Top-left: [Orange card] "Business Layer" — expert feedback, data input
  Bottom-left: [Orange card] "PoC Team" — passionate team description
  Top-right: [Orange card] "Strategic Layer" — cross-BU alignment
  Bottom-right: [White card] "Leadership Layer" — strategic guidance
```

---

## Template 8: Timeline / Plan Slide

**Purpose**: Show phased delivery with dates
**Used in**: Slide 16 (FY26 Plan)
**Layout**: Pattern D (Horizontal Chevron Flow)

### Structure
```
TOP ROW: 3 phase summary blocks (with connecting arrows)
  [Project Kickoff] → [PTR Gen CT Release] → [BUs Transfer]
  Each block: bullets of key deliverables

MIDDLE: Chevron timeline
  [01 Project Kickoff] ▶ [02 CER Gen CT Release] ▶ [03 PTR Gen CT Release] ▶ [04 Consistency Check] ▶ [05 CER+PTR BUs Transfer]
  2026.1-TBD          2026.2-2026.3           2026.3-2026.6           2026.6-2026.9         2026.9-2026.12

BOTTOM: Expanded detail for 2 key milestones
  [CER Gen CT Release] ← detail bullets
  [Consistency Check] ← detail bullets
```

### Chevron Specifications
- Height: ~60px per chevron
- Number circle: 32px, white on phase-appropriate color
- Colors cycle: Orange → Dark Orange → Teal → Gray → Black
- Date labels: Below each chevron, **12pt** gray
- Connection: Chevrons physically overlap/abut (not separate)

---

## Template 9: Transferability / Methodology Slide

**Purpose**: Explain why the system is reusable, or present a methodology framework
**Used in**: Slide 17 (Project Transferability), also adapted for Harness Engineering concept page
**Layout**: Three-column — Left info card + Center funnel + Right info card

### Structure
```
LEFT: Slide-13 Information Card
  [Orange header: 设计原则 / Design Principles]
  ✓ (teal checkmark)
  [Overview] a. b. c. points
  [Approach] a. b. points with bold keywords

CENTER: Funnel diagram (layers TOUCH, no gaps)
  ┌──────────────────────────────┐
  │ 01  Context Engineering      │  ← Widest, orange
  │     What AI sees             │
  ├────────────────────────────┤   ← layers touch!
  │   02  Architectural Constr.  │  ← Medium, teal
  │       How AI operates        │
  ├──────────────────────────┤     ← layers touch!
  │     03  Entropy Mgmt.      │  ← Narrowest, dark
  │         What AI outputs    │
  └──────────────────────────┘
  [Converging Control] ← orange pill below

RIGHT: Slide-13 Information Card
  [Teal header: 核心指标 / Core Metrics]
  ✓ (teal checkmark)
  >92%  Output consistency rate
  >90%  Context utilization eff.
  [Key Insight] a. b. points
```

### Critical construction rules:
1. **Funnel layers MUST touch** — zero gap, no arrows between layers
2. **Progressive narrowing**: Each layer ~0.35" narrower per side than the one above
3. **Color gradient**: Orange → Teal → Dark (smooth transition, not random)
4. **Left/right cards use Slide-13 pattern**: Colored header block (20pt Chinese + 12pt English) → checkmark → pills → a.b.c. lettered content
5. **White numbered circles** (0.4" diameter) inside each layer, left-aligned
6. **Each layer has 3 text lines**: Bold title (18pt) + subtitle (12pt) + keyword detail (10pt)
7. **Bottom pill**: Orange rounded rectangle with 12pt bold white label

---

## Template 10: Roadmap Matrix Slide

**Purpose**: Show long-term vision across multiple dimensions
**Used in**: Slide 18 (Function Plan)
**Layout**: Pattern G (Matrix Table)

### Structure
```
TOP: Maturity level labels with connecting arrow
  Intern Level → Entry Level → Senior Level → Manager Level → Expert Auditor Level
  V1            V2             V3              V4              V5

MATRIX ROWS:
  | Dimension | V1 | V2 | V3 | V4 | V5 |
  |-----------|----|----|----|----|-----|
  | Features  | .. | .. | .. | .. | ..  |
  | ROI       | .. | .. | .. | .. | ..  |
  | Tech&Cost | .. | .. | .. | .. | ..  |
  | Resources | .. | .. | .. | .. | ..  |

COLUMN COLORS:
  V1: White/light    V2: Light orange
  V3: Teal           V4: Dark teal
  V5: Dark/gradient

ROW LABEL COLUMN:
  Bold labels in black rounded pills: "ROI", "Tech & Cost", "Required Resources"

FOOTNOTE: 
  Explanation of abbreviations (e.g., "RAG*: Retrieval-Augmented Generation")
```

---

## Template Selection Guide

| Slide Purpose | Template | Key Visual Element |
|---------------|----------|-------------------|
| External urgency / market context | Template 1 | Photo collage + summary cards |
| AI feature demonstration | Template 2 | Left-explain / Right-prove with Quality Gate |
| Problem definition / pain points | Template 3 | A-B-C-D badges + solution mapping |
| Product UI walkthrough | Template 4 | Full-screen screenshot |
| Technical architecture | Template 5 | Layer diagram + explanation cards |
| Business impact / KPIs | Template 6 | Three-column KPI banner + detail |
| Team / ecosystem / process | Template 7 | Central cycle diagram + flanking cards |
| Phased timeline / plan | Template 8 | Horizontal chevron flow |
| Reusability / methodology | Template 9 | Funnel + stable/variable cards |
| Long-term roadmap matrix | Template 10 | Multi-row, multi-column progression table |
