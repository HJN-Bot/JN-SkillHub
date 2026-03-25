# Content Logic Guide — Jianan Presentation System

This document captures Jianan's presentation narrative structure, persuasion arc, and content organization philosophy. It is extracted from the R·Agent presentation (18 slides + bilingual oral scripts).

---

## 1. Macro Narrative Arc

Jianan's presentations follow a **6-phase persuasion arc**. This is NOT a generic "intro-body-conclusion" — it's a carefully designed funnel that moves stakeholders from "why should I care?" to "give us the go."

### Phase 1: Strategic Urgency (Slides 1-2) — "为什么此刻必须做？"
**Goal**: Establish that inaction is the real risk.

**Pattern**: Three-signal validation framework:
1. **National/Policy level** — Government is pushing this direction
2. **Industry/Competition level** — Competitors are already moving
3. **Internal/Business level** — Our own teams have validated the pain

**Key sentence pattern**: "我们不是在创造需求;我们是在响应需求。" (We're not creating demand; we're responding to it.)

**Visual approach**: Photo collage of policy documents + bullet-point cards summarizing each signal.

### Phase 2: Capability Demonstration (Slides 3-8) — "我们做了什么？"
**Goal**: Show progressive technical capability, from simple to complex.

**Pattern**: Escalating difficulty ladder:
- V1 Easy: Framework generation (2 days → 2 minutes)
- V1 Medium: Consistency checking (manual cross-check → automated)
- V3 Hard: CER content generation (the "hardest nut to crack")
  - Step 1: Template-based (Chapters 1-3, 10% of report)
  - Step 2: Comparison & highlighting (Chapter 4, 55% of report)
  - Step 3: Expert reasoning / difference analysis (the "soul" of CER)

**Key principle**: Each capability slide uses the **Left-Explain / Right-Prove** layout. The left side NEVER stands alone without evidence on the right.

### Phase 3: Live Product Demo (Slides 9-12) — "实际操作什么样？"
**Goal**: Make it tangible — show the actual UI people will interact with.

**Pattern**: 4-step user flow walkthrough:
1. Upload & Extract
2. Manual Verification
3. Difference Highlighting
4. Difference Analysis

**Key principle**: Full-screen UI screenshots with minimal overlay text. Let the product speak for itself. Oral narration provides the walk-through.

### Phase 4: Impact Quantification (Slides 13-14) — "效果如何？"
**Goal**: Convert capability into business metrics.

**Pattern**: Architecture + Numbers combo:
- Slide 13: Technical architecture (HOW it works under the hood)
- Slide 14: Business effectiveness (WHAT it achieves in numbers)

**Key metrics always include**:
- Time savings (e.g., -8 days per project)
- Automation coverage (e.g., 70%)
- Accuracy threshold (e.g., >80%)
- Efficiency multiplier (e.g., 20-40x improvement)

**Key sentence pattern**: "CER不是终点,是起点。攻克CER,就打通了整个注册文档AI化的技术路径。" (CER is not the endpoint — it's the starting point.)

### Phase 5: Scalability & Roadmap (Slides 15-18) — "怎么扩展？"
**Goal**: Demonstrate this isn't a one-off experiment but a repeatable system.

**Pattern**: Four-layer argument:
1. **Ecosystem** (Slide 15): We have the team, data, and process to iterate fast
2. **Near-term plan** (Slide 16): Quarterly deliverables with concrete dates
3. **Transferability** (Slide 17): 50% reusable + 50% customizable architecture
4. **Long-term roadmap** (Slide 18): V1→V5 progression with increasing maturity

**Key principle**: Every phase has a "risk mitigation" message: "每季度可验收成果，交付不达标可调整或暂停" (Quarterly deliverables — if we don't deliver, you can adjust or pause.)

### Phase 6: Call to Action (Slide 19 / Closing) — "我们需要什么？"
**Goal**: Emotional close + concrete ask.

**Pattern**: Three-beat closing:
1. **Personal story**: "在24年有幸参与MP RA项目的时候我就在想..." (When I was fortunate to participate in...)
2. **User validation quote**: "CUC的专家也在问：这个工具什么时候能正式用？" (Experts are asking: When can we use this?)
3. **Urgency + Ask**: "AI时代最大的风险不是试错，是犹豫。我们团队准备好了...就差领导的一个Go。" (The greatest risk isn't trying — it's waiting. We're ready. We just need your "Go.")

---

## 2. Slide Content Composition Rules

### Rule 1: Title = Conclusion, Not Topic
BAD: "Technical Architecture"
GOOD: "Tech" (short) — with the architecture diagram doing the talking
BAD: "Project Results"
GOOD: "Project Effectiveness" — with KPI banner showing -8Day / 70% / >80%

### Rule 2: Every Feature Slide Has Three Sections

```
┌──────────────────────────┐
│ 📊 Chapter Scope         │  ← What portion of the document this covers
│    Progress bar + %      │
├──────────────────────────┤
│ ⚙️ Technical Challenges  │  ← What makes this hard (3 boxes)
│    [box1] [box2] [box3]  │
├──────────────────────────┤
│ 🔄 Process Flow          │  ← How the AI does it (numbered steps)
│    ①→②→③→④              │
├──────────────────────────┤
│ ✅ Quality Gate           │  ← Proof it works (2-3 metrics)
│    >90% | 4min | ✓       │
└──────────────────────────┘
```

This four-block structure repeats on Slides 6, 7, and 8 — creating a consistent visual rhythm that makes the audience feel the progression.

### Rule 3: Pain Point Slides Use the A-B-C-D Pattern
When presenting pain points, use lettered badges (A, B, C, D) in orange circles, each followed by a bold 2-word label:
- A: Heavy Workload
- B: Numerous Input
- C: Slow Comparison
- D: Difficult Judgment

Then map each pain point to a solution on the right side with arrow connections.

### Rule 4: Numbers Are Heroes
When a number tells the story, make it the LARGEST element on the slide:
- "55%" at 72pt bold tells the audience Chapter 4 is the bulk of the work
- "-8Day" at 48pt bold with a lightning icon tells the audience this saves real time
- "0%" false negative rate is more powerful than any paragraph of text

### Rule 5: Transition Sentences Bridge Slides
Each oral script section ends with a forward-looking sentence that bridges to the next slide:
- "这只是开胃菜..." (This is just the appetizer...) → bridges to harder features
- "我们的目标不止于此..." (Our goal doesn't stop here...) → bridges to CER
- "让我们来看看AI是否能meet our expectations" → bridges to demo results

---

## 3. Content Granularity Standards

### What Goes ON the Slide (PPT)
- Short titles (2-6 words)
- Numbered lists (max 3-4 items, each 1 line)
- Metric callouts (number + label)
- Process flow diagrams
- Screenshots / evidence
- Tables (max 4-5 rows visible)
- Progress bars with percentages

### What Goes IN the Oral Script Only
- Context and backstory ("传统流程是什么样的呢？")
- Analogies and metaphors ("打个比方：你去倒杯咖啡，回来时30页比对表已经生成好了")
- Emotional appeals ("最让我感动的是...")
- Detailed explanations of methodology
- Acknowledgments and thanks
- Transition sentences between slides

### What NEVER Goes on the Slide
- Full sentences / paragraphs of prose (except in evidence screenshots)
- Generic labels like "Introduction" or "Summary"
- More than 3 bullet points without visual structure
- Unsupported claims without accompanying data

---

## 4. Data Presentation Standards

### Time Savings
Format: `[Original Time] → [AI Time]` or `-[Saved Days]/Project`
Example: "2-4 hours → 4 minutes" or "-8Day/Project"

### Accuracy Metrics
Format: `>[Percentage]%` with label
Always show alongside companion metrics (speed + accuracy + intervention-friendliness)

### Comparison (Before/After)
Use a 4-column table: `Actions | Manual | AI Augmented | Improvement`
Example row: `Data Process | 3 hrs | 5 mins + Human Review | >40 times`

### Volume/Scope
Use stacked bar charts or progress bars to show:
- How much of the document AI covers
- How many documents across BUs
- Chapter-by-chapter breakdown (Template/Content/Comparison segments)

---

## 5. Stakeholder-Aware Messaging

### For Technical Audience
- Show architecture diagrams (Hand Layer / Brain Layer)
- Mention specific tech: SFT/DPO, RAG, Reranking, Modular SLM chains
- Include Quality Gate metrics with decimal precision

### For Business/Executive Audience
- Lead with time savings and ROI numbers
- Use the "coffee break" analogy (grab coffee → 30 pages ready)
- Emphasize risk mitigation: "quarterly deliverables, pause if not meeting targets"
- Frame as competitive advantage: "competitors are already doing this"

### For Mixed Audience (Jianan's typical scenario)
- Structure slides so business messages are visually dominant (large numbers, bold titles)
- Embed technical depth in the left-side explanation area or oral script
- Use the Right-side evidence panel to satisfy technical reviewers
- The oral script handles the emotional/strategic layer that executives respond to
