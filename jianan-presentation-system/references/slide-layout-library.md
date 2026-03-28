# Slide Layout Library — Commercial Template Resource

> **使用说明（重要）**：
> 这个文件是从商业模板提炼的**布局资源库**，不是默认参考。
> 优先使用 `visual-style.md`（基于 Jianan 真实 PPT）和 `slide-templates.md`。
> 只有当那两个文件没有覆盖所需布局时，才从这里挑选合适的原型。
> 商业模板里有一些布局 Jianan 原始 PPT 里也用了（如甘特图、TOC 编号列表），
> 这些是认可的模式；其他布局按需判断是否适用。

**颜色替换规则（以 visual-style.md 为唯一权威）：**
| Template color | Jianan 对应颜色 |
|----------------|-----------------|
| Blue `#0070C0` | Orange `#E87722` |
| Dark blue panels | Black `#1a1a1a` 或 Teal `#009999` |
| Gray accent | Teal `#009999` |
| White text on color | White `#FFFFFF` |

---

## Layout 01 — Cover: Left Sidebar + Right Title Block

**Use for:** Opening slide, major section dividers requiring a "full reset" feel.

```
┌─────────────┬─────────────────────────────────┐
│             │  LOGO                           │
│  SIDEBAR    │                                 │
│  COLOR      │  主标题（45pt Bold）             │
│  BLOCK      │  副标题                          │
│  (left 40%) │                                 │
│             │  汇报人 ────────────────         │
│             │  汇报日期                        │
└─────────────┴─────────────────────────────────┘
```

**Key measurements (13.33" × 7.5"):**
- Left sidebar: `x=0, y=0, w=5.0", h=7.5"` — fill: Jianan Orange `#E87722` or Black
- Right content area: `x=5.5", y=0` — white background
- Title: `x=5.8", y=1.6", w=7.0"` — 40-45pt Bold, White (if on colored sidebar) or Black
- Subtitle: `y=3.5"` — 16pt Regular
- Date/Person: `y=6.5"` — 14pt Regular, gray

**Jianan adaptation:** Orange sidebar is striking; use Black sidebar for more formal decks.

---

## Layout 02 — Cover: Right Photo + Left Text

**Use for:** Visually rich cover when a product screenshot or demo image is available.

```
┌──────────────────┬───────────────────────────────┐
│  LOGO            │                               │
│                  │   [ PHOTO / SCREENSHOT        │
│  主标题           │     RIGHT HALF                │
│  (45pt Bold)     │     x=6.67", w=6.02"          │
│                  │     h=6.3"                    │
│  副标题           │                               │
│  汇报日期         │                               │
└──────────────────┴───────────────────────────────┘
```

**Key measurements:**
- Photo: `x=6.67", y=0.6", w=6.02", h=6.3"` — full bleed right half
- Left text area: `x=0.5", y=1.6", w=5.5"` — no background box needed
- Title: 40-45pt Bold Orange
- Optional thin teal rule line below title

---

## Layout 03 — Cover: Full-Bleed Background + Centered Overlay

**Use for:** High-impact opening when a dramatic landscape/scene photo is available.

```
┌───────────────────────────────────────────────┐
│  [FULL SLIDE BACKGROUND PHOTO]               │
│                                               │
│         ╔═══════════════════════╗             │
│         ║  主标题（45pt Bold）   ║             │
│         ║  副标题（16pt）        ║             │
│         ╚═══════════════════════╝             │
│                                               │
└───────────────────────────────────────────────┘
```

**Key measurements:**
- BG photo: `x=0, y=0, w=13.33", h=7.5"`
- Overlay card: semi-transparent dark or orange bar, `y=2.5", h=2.5"`, full width or centered `w=10"`
- Title: White 45pt Bold centered
- Add thin Orange bottom-border rule on overlay card

---

## Layout 04 — TOC: Vertical Numbered List (Right Panel)

**Use for:** 4-item table of contents — the most standard and clean TOC format.

```
┌────────────────────┬────────────────────────────────┐
│                    │  目录｜Contents  (44pt Bold)   │
│  [PHOTO or         │                                │
│   COLOR BLOCK      │  01─  工作完成情况              │
│   LEFT HALF]       │       work completion (14pt)   │
│                    │                                │
│                    │  02─  工作不足之处              │
│                    │       ...                      │
│                    │  03─  业绩成果展示              │
│                    │  04─  明年工作计划              │
└────────────────────┴────────────────────────────────┘
```

**Key measurements:**
- Photo/color block: `x=0, y=0, w=6.5", h=7.5"`
- Right panel: `x=6.5", y=0, w=6.83", h=7.5"` — white bg
- Section title "目录｜Contents": `x=7.4", y=1.1", size=44pt Bold`
- Numbers "01─": `x=7.5", y=2.6"` — 32pt, Orange `#E87722`; spacing ~1.17" between items
- Chinese title: `x=8.6", y=2.54"` — 18pt Bold Black; same y as number
- English subtitle: `x=8.6", y=2.92"` — 14pt Regular Teal `#009999`

**Jianan adaptation:** Replace left photo with a dark/orange color block for the "no-photo" version.

---

## Layout 05 — TOC: Circle Icon Grid (2×3 or 3×2)

**Use for:** 6-item TOC where items are equally weighted (no hierarchy).

```
┌──────────────────────────────────────────────────┐
│  LEFT: 目录                                       │
│        CONTENTS (large text)                      │
│                                                   │
│  ○ 01    ○ 02    ○ 03                           │
│  Item    Item    Item                             │
│  ○ 04    ○ 05    ○ 06                           │
│  Item    Item    Item                             │
└──────────────────────────────────────────────────┘
```

**Key measurements (template used):**
- Circle: `w=1.56", h=1.56"` oval, stroke = item color; no fill or slight fill
- Number inside circle: 45pt Bold, Orange or Teal
- Circle center row 1: `y≈1.45"`, center row 2: `y≈4.21"`
- Circles spaced at `x = 5.36", 8.15", 10.94"` (gap ~2.79")
- Title label below each circle: `y = circle_y + 1.7"`, 18pt Bold
- English sublabel: 11pt Teal

**Jianan adaptation:** Fill circles with Orange gradient; use teal for even-numbered items.

---

## Layout 06 — Section Header: Number Watermark

**Use for:** Every chapter/section opener. Creates strong visual identity and rhythm.

```
┌───────────────────────────────────────────────┐
│  [GIANT NUMBER partially off-screen left]    │
│  "2" at 400-450pt, x≈-0.5", clipped by edge  │
│                                               │
│              SECTION TITLE (54pt Bold)        │
│              English subtitle (24pt)          │
│              ─────────────────── (thin line)  │
│              Chapter description (12pt)       │
└───────────────────────────────────────────────┘
```

**Key measurements:**
- Giant number: `x=-0.5", y=0.15", size=400-450pt, Bold` — Orange `#E87722`, partially clipped
- Section title: `x=6.5", y=1.3", size=40pt Bold Black`
- English subtitle: `x=6.5", y=2.5", size=20pt` — Teal `#009999`
- Thin horizontal rule: `x=6.5", y=3.2", w=6"` — 0.5pt Orange
- Description text: `x=6.5", y=3.5"` — 14pt Regular

**Jianan adaptation:** Number color = Orange. If using dark background, number = White.

---

## Layout 07 — Content: Two-Column Left/Right

**Use for:** Feature explanation slides (methodology on left, evidence/results on right). The core Jianan slide format.

```
┌─────────────────────────┬──────────────────────────┐
│  SLIDE TITLE (32-40pt)  │                          │
├─────────────────────────┤                          │
│  Left: EXPLAIN          │  Right: PROVE            │
│  ─────────────          │  ─────────────           │
│  ● Approach/method      │  [Screenshot, data,      │
│  ● Key logic            │   metrics, evidence]     │
│  ● Context              │                          │
│                         │  KPI: 28-36pt Bold       │
│  Technical Challenge:   │  Label: 12pt Gray        │
│  ┌─────────────────┐    │                          │
│  │ orange border   │    │  Quality Gate:           │
│  └─────────────────┘    │  ✓ Metric + Value        │
└─────────────────────────┴──────────────────────────┘
```

**Key measurements:**
- Left column: `x=0.5", y=1.2", w=5.8", h=5.8"`
- Right column: `x=6.8", y=1.2", w=6.0", h=5.8"`
- Slide title: `x=0.5", y=0.3", size=32-40pt Bold Orange`
- Challenge box: `w=5.0", border=2px Orange #E87722, bg=white, padding=12pt`
- KPI number: 28-36pt Bold, Orange or Teal

---

## Layout 08 — Content: 3-Column Card Grid

**Use for:** Parallel items of equal weight (3 principles, 3 features, 3 benefits).

```
┌─────────────────────────────────────────────────────┐
│  SLIDE TITLE                                         │
├────────────────┬────────────────┬───────────────────┤
│  ┌──────────┐ │  ┌──────────┐  │  ┌──────────┐     │
│  │ COLORED  │ │  │ COLORED  │  │  │ COLORED  │     │
│  │ HEADER   │ │  │ HEADER   │  │  │ HEADER   │     │
│  └──────────┘ │  └──────────┘  │  └──────────┘     │
│  ● Point 1   │  ● Point 1    │  ● Point 1          │
│  ● Point 2   │  ● Point 2    │  ● Point 2          │
│  ● Point 3   │  ● Point 3    │  ● Point 3          │
└──────────────┴────────────────┴───────────────────┘
```

**Key measurements:**
- Card width: `w=3.8"` with `0.2"` gaps between cards
- Card header: `h=0.8"`, fill = Orange / Teal / Dark alternating
- Header title: 16pt Bold White
- Card body bg: white, border: 1pt gray, padding: 12pt
- Bullet text: 12pt Regular

**Jianan adaptation:** Use Slide-13 Information Card pattern (colored header + teal checkmark + pills + lettered points) instead of plain bullets.

---

## Layout 09 — Gantt Chart / Project Timeline

**Use for:** Project plan, FY roadmap, quarterly work arrangement.

```
┌────────────────────────────────────────────────────┐
│  TITLE: 项目时间安排                                 │
│  ─────────────────────────────────────────────────│
│  TASK LABEL │  Q1  │  Q2  │  Q3  │  Q4            │
│  ─────────── ╪──────╪──────╪──────╪───────         │
│  项目组A    │██████│      │      │                │
│  - Task 01  │  ████│      │      │                │
│  - Task 02  │      │██████│      │                │
│  - Task 03  │      │   ███│██    │                │
│  ─────────── ╪──────╪──────╪──────╪───────         │
│  项目组B    │      │      │██████│██████          │
└────────────────────────────────────────────────────┘
```

**Key measurements:**
- Full slide area: `x=0.5", y=1.0", w=12.3", h=6.0"`
- Quarter header bar: `h=0.42"`, fill = Orange/Teal alternating
- Quarter labels (Q1-Q4): 13pt Bold White, centered in each column
- Task group rows: `h=1.54"` (contains 3 sub-tasks)
- Task bar (Rounded Rectangle): `h=0.42"`, corner radius small; fill = Orange/Teal/Dark per project
- Task label column: `w=1.5"` left side, 13pt Regular
- Vertical dividers between quarters: thin 0.5pt Gray lines

---

## Layout 10 — Work Task Matrix (4-Column Card Grid)

**Use for:** Quarterly work breakdown, multi-department task assignment.

```
┌──────────────────────────────────────────────────────┐
│  TITLE     Q1────────│Q2────────│Q3────────│Q4─────  │
│  ┌────────┐┌────────┐┌────────┐┌────────┐           │
│  │Task 01 ││Task 01 ││Task 01 ││Task 01 │           │
│  │ desc   ││ desc   ││ desc   ││ desc   │           │
│  └────────┘└────────┘└────────┘└────────┘           │
│  ┌────────┐          ┌────────┐┌────────┐           │
│  │Task 02 │          │Task 02 ││Task 02 │           │
│  └────────┘          └────────┘└────────┘           │
└──────────────────────────────────────────────────────┘
```

**Key measurements:**
- Column width: `w=2.63"`, gap ~0.15" between columns
- Task card: `w=2.63", h=0.78"`, Rounded Rectangle corner ~8pt
- Task title: 10pt Bold (inside card, top)
- Task description: 8pt Regular Gray (inside card, below title)
- Quarter header stripe: `h=0.42"` at top, fill = Orange/Teal for active, Dark for completed
- Quarter section label: 12pt Bold, bottom of each column

---

## Layout 11 — Process Flow: Horizontal Steps

**Use for:** Workflow, implementation phases, sequential process (4-5 steps).

```
┌────────────────────────────────────────────────────┐
│  TITLE                                              │
│                                                     │
│  [①] ──→── [②] ──→── [③] ──→── [④] ──→── [⑤]  │
│   STEP       STEP      STEP      STEP      STEP    │
│   label      label     label     label     label   │
│                                                     │
│  Below each step: description text 12pt             │
└────────────────────────────────────────────────────┘
```

**Key measurements (from template swim-lane pattern):**
- Step block: `w=2.47", h=2.86"` Freeform/Rounded Rectangle
- Step header accent bar: `w=2.47", h=0.45"` at top of each block, colored
- Connector arrow area: `h=0.91"` between top-bar and block body
- Colors: alternate Orange (#E87722) → Teal (#009999) → Dark → Orange pattern
- Step number: 28pt Bold White inside colored header bar
- Step title: 14pt Bold below number
- Description: 12pt Regular, Gray, inside block

---

## Layout 12 — KPI / Metrics Dashboard

**Use for:** Project results, quality gate summary, effectiveness proof slide.

```
┌────────────────────────────────────────────────────┐
│  TITLE: 项目成效                                    │
├────────────────────────────────────────────────────┤
│                                                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐         │
│  │   85%    │  │  3×      │  │  10+     │         │
│  │ accuracy │  │ faster   │  │ modules  │         │
│  └──────────┘  └──────────┘  └──────────┘         │
│                                                     │
│  ┌─────────────────────────────────────────────┐   │
│  │  Chart or comparison table evidence panel   │   │
│  └─────────────────────────────────────────────┘   │
└────────────────────────────────────────────────────┘
```

**Key measurements:**
- KPI card: `w=3.5", h=2.0"`, white bg, Orange bottom border 3pt
- KPI number: 36pt Bold Orange or Teal (HERO element, centered)
- KPI unit/label: 12pt Regular Gray, below number
- KPI metric name: 14pt Bold, below unit
- Evidence panel: `x=0.5", y=4.5", w=12.3", h=2.5"` with light Gray border

---

## Layout 13 — Comparison: Two-Side (Before / After)

**Use for:** Problem → Solution, Old Process → New Process, Manual → AI-Assisted.

```
┌─────────────────────┬─────────────────────────────┐
│  LEFT: BEFORE / ❌  │  RIGHT: AFTER / ✅           │
│  ─────────────────  │  ──────────────────────────  │
│  Orange header      │  Teal header                 │
│  "传统方式"          │  "AI赋能"                    │
│                     │                              │
│  ● Point A          │  ● Point A (improved)        │
│  ● Point B          │  ● Point B (improved)        │
│  ● Pain point       │  ● Quantified improvement    │
└─────────────────────┴─────────────────────────────┘
```

**Key measurements:**
- Left panel: `x=0.5", y=1.2", w=5.9", h=5.5"`, bg=light Orange tint `#FFF5ED`, border=2pt Orange
- Right panel: `x=7.0", y=1.2", w=5.9", h=5.5"`, bg=light Teal tint `#E8F5F5`, border=2pt Teal
- Panel headers: `h=0.8"`, fill = Orange (left) / Teal (right), text = 16pt Bold White
- Divider: thin vertical line `x=6.5"` OR VS badge centered at `x=6.5", y=3.5"`

---

## Summary: When to Use Each Layout

| Situation | Use Layout |
|-----------|-----------|
| Opening slide / title | 01 (sidebar), 02 (photo), or 03 (full-bleed) |
| Table of contents | 04 (vertical list, ≤4 items) or 05 (circle grid, 6 items) |
| Chapter/section start | 06 (number watermark) |
| Feature explanation | 07 (two-column left/right) |
| Parallel concepts | 08 (3-column cards) |
| Project timeline | 09 (Gantt) or 10 (task matrix) |
| Process/workflow | 11 (horizontal steps) |
| Results/impact proof | 12 (KPI dashboard) |
| Before/after comparison | 13 (two-side comparison) |

---

## Color Application Rules

When adapting any layout to Jianan's brand:

1. **Primary accent = Orange `#E87722`**: Slide titles, section numbers, primary headers, KPI numbers, left-side challenge boxes
2. **Secondary accent = Teal `#009999`**: English subtitles, check marks, right-side evidence labels, secondary cards
3. **Text = Near-black `#1a1a1a`**: All body text, chart labels
4. **Background = White `#FFFFFF`**: All content areas (not dark-bg slides)
5. **Borders = 1-2pt, use the element's own accent color**: Cards, boxes, panels
6. **Gray `#888888` / `#CCCCCC`**: Captions, footnotes, grid lines, decorative rules

**NEVER use the template's blue `#0070C0` in Jianan slides.**
