---
name: jianan-presentation-system
description: "Jianan's end-to-end presentation creation system: Startup Intake + 3-layer workflow. TRIGGER for any presentation, slide deck, pitch deck, PPT, oral script, speaker notes, bilingual content, animated diagrams, data charts, Gantt charts, GIFs for PPT, or content beautification/translation. Layers: (1) Content Beautify — optimize/translate MD scripts, extract GitHub repos into content; (2) PPT Design — generate fully editable PPTX with native shapes/charts/text using pptxgenjs; (3) Animation — static charts (pptxgenjs native), Gantt/timeline, HTML/CSS particle flow GIFs, Manim 3D architecture GIFs (if Manim installed). Also trigger for: '帮我做PPT', '优化这个稿子', '翻译成英文', '帮我做甘特图', '节点流动GIF', '架构动画', '把GitHub项目做成动图', '做个能嵌PPT的动图', '起始交互'."
---

# Jianan Presentation System

## Workflow

```
Startup Intake → Layer 1: Content → Layer 2: PPT Design → Layer 3: Animation
```

Each layer is independent. Any layer can be skipped or run alone.

---

## Reference Files

### Authoritative Sources（优先级从高到低）

| Priority | File | Purpose |
|----------|------|---------|
| **P1** | [visual-style.md](references/visual-style.md) | **颜色权威来源** + 字体层级 + 布局模式（基于 Jianan 真实 PPT）|
| **P1** | [slide-templates.md](references/slide-templates.md) | Slide 类型模板（基于 Jianan R·Agent 18 张 slides 提炼）|
| **P1** | [content-logic.md](references/content-logic.md) | 叙事结构 + 说服逻辑 |
| P2 | [slide-layout-library.md](references/slide-layout-library.md) | **布局资源库**（商业模板提炼，按需调用，不作为默认参考）|
| P2 | [oral-script-guide.md](references/oral-script-guide.md) | 演讲稿写作规则 |

### Workflow Files

| File | Purpose |
|------|---------|
| [startup-intake.md](references/startup-intake.md) | Step 0：起始交互问卷 + Session Brief |
| [content-beautify.md](references/content-beautify.md) | Layer 1：内容优化 / 翻译 / GitHub 提炼 |
| [pptx-execution-guide.md](references/pptx-execution-guide.md) | Layer 2：pptxgenjs 完整运行指南 + 示范脚本 |
| [animation-workflow.md](references/animation-workflow.md) | Layer 3：图表 / 甘特图 / HTML动效 / Manim（可选）|
| [html-animation-guide.md](references/html-animation-guide.md) | Layer 3：HTML/CSS 动图完整模板 |

---

## PPTX Editability — Iron Rules

| Element | Implementation | Never do |
|---------|---------------|---------|
| Titles / body text | `addText()` with explicit fontSize | Leave fontSize unset |
| Data charts | `addChart()` | Manual colored rectangles |
| Tables | `addTable()` | Screenshots of tables |
| Gantt bars | `addShape()` grid | Manual rectangles without text |
| Flow diagrams (simple) | `addShape()` + `addText()` | Screenshots |
| Complex HTML diagrams | Screenshot → `addImage()` | — |
| Animated GIFs | `addImage()` with .gif | — |
| Speaker notes | `addNotes()` every slide | Omit oral script |

**Colors**: Always use [visual-style.md](references/visual-style.md) as the single source of truth. Orange = `E87722`, Teal = `009999`. Never use any other value.

---

## Layout Priority Rule

When choosing a layout:
1. **First**: Check `slide-templates.md` — does this slide type exist?
2. **Then**: Check `visual-style.md` Layout Patterns (A/B/C/D/E)
3. **Only if needed**: Pull from `slide-layout-library.md` (commercial template resource) — explicitly note which archetype you're borrowing

---

## McKinsey Exhibit Principles (Why behind the rules)

These three principles explain 90% of the design decisions in this system:

**1. One message per slide** → The title is a conclusion sentence, not a topic label. If you can't state the conclusion in the title, the slide's content isn't clear enough yet.

**2. Evidence earns the right to exist** → Every claim on the left side of a Feature Demo slide must be matched by verifiable output on the right. No claim without proof.

**3. Visual hierarchy = cognitive load reduction** → Font sizes, colors, and spacing are not aesthetics — they tell the audience's eye where to look first, second, third. Violating the hierarchy forces the audience to work harder to find the main point.
