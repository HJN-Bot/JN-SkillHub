# Content Logic Guide — Jianan Presentation System (v2)

This document defines the narrative structure, persuasion arc, and content organization philosophy for any deck Jianan creates.

**v2 change**: The system now operates in two layers:
- **Layer 1 — 5-Beat Universal Arc** (default for all decks): a general-purpose persuasion structure adapted from YC pitch coaching, Apple keynotes, and Stripe Press / a16z memos.
- **Layer 2 — 6-Phase Internal Expansion** (specialized): the original v1 structure, retained as the detailed expansion pattern for *internal proposal / budget-ask* scenarios. It now lives inside Beats 3-4 of the 5-Beat arc.

Both layers are kept. The 5-Beat decides the macro shape; the 6-Phase fills in the middle when the audience is internal.

---

## 0. Decision: which layer to use?

Before drafting any deck, answer three questions:

| Question | If answer = | Layer to use |
|---|---|---|
| **Audience** | Internal leadership who already know you | Layer 2 (6-Phase) inside Layer 1 |
| **Audience** | External / investors / cross-org / public | Layer 1 (5-Beat) only |
| **Goal** | Budget approval / title / resource ask | Layer 2 inside Layer 1 |
| **Goal** | Mindset shift / product launch / inspiration | Layer 1 only |
| **Length** | 3 minutes (elevator) | Layer 1 only, compressed |
| **Length** | 15 minutes (standard) | Layer 1, with Layer 2 if internal |
| **Length** | 45 minutes (deep-dive) | Layer 1 + Layer 2 + objection backup slides |

Rule of thumb: **5-Beat is always the spine. 6-Phase is the muscle that fills out Beats 3-4 when the audience is internal.**

---

## 1. Layer 1 — The 5-Beat Universal Arc

This is the default narrative spine. Every deck Jianan creates should map cleanly onto these five beats, regardless of length or audience.

### Beat 1 — Hook (Cold Open + Why Now)
**Job**: Capture attention in 30 seconds; establish urgency in the next 60.

**Components**:
- **Cold Open** (1 slide): one of the four archetypes from `pitch-archetypes.md` — Painful Status Quo, Inevitable Future, Counterintuitive Insight, or Loaded Question.
- **Why Now** (0-2 slides): the forcing function — a regulatory deadline, a capability unlock, a competitive move, an internal pain spike. Audience should feel "if not now, when?"

**Discipline**:
- First sentence ≤12 words.
- First concrete number must appear within 90 seconds.
- No self-introduction in the Cold Open. Introduce after the hook lands (YC's classic move).

### Beat 2 — Insight (the thesis that reframes the problem)
**Job**: Update the audience's mental model so the rest of the deck lands harder.

**Components**:
- **One thesis sentence** displayed at hero size (28-36pt+).
- **Supporting context** (1 slide): why the conventional approach is wrong, what the better frame is.

**Discipline**:
- The thesis must be defensible in one sentence. If it takes a paragraph, it's not a thesis — it's a topic.
- Insight must be **non-obvious**. If the audience would have agreed before you said it, it's not an insight.
- Examples for Jianan's domain:
  - "Machine Learning's bottleneck is Human Teaching."
  - "Don't pursue 100% accuracy — engineer structured failure modes."
  - "Cross-disciplinary teams aren't a gap, they're the moat."

### Beat 3 — Wow Moment + Proof
**Job**: Make the result undeniable, then explain how it's possible.

**Components**:
- **Wow Moment slide** (1 slide, REQUIRED): three-act structure (Setup → Reveal → Pause) per `pitch-archetypes.md`.
- **Proof depth** (variable): everything that explains how the Wow was achieved.

**Internal scenarios — expand Beat 3 with v1 6-Phase Phases 2-4**:
- 6-Phase Phase 2 (Capability Demonstration): the escalating-difficulty ladder showing technical capability.
- 6-Phase Phase 3 (Live Product Demo): the 4-step UI walkthrough.
- 6-Phase Phase 4 (Impact Quantification): the architecture + numbers combo.

**Discipline**:
- The Wow Moment goes **first** in Beat 3. Audience sees the result before the explanation. v1's order (capability → demo → numbers) is reversed: **numbers first as a Wow, then capability and demo as slow-motion replay.**
- Pause for 5-10 seconds after the Wow reveal. Resist the urge to fill silence.
- One Wow per deck. Multiple Wows = zero Wows.

### Beat 4 — Why Us / Why Now (the unfair-advantage close)
**Job**: Convert "interested" into "committed" by showing the advantage is structural.

**Components**:
- **Why Us matrix** (1 slide, REQUIRED): three-column comparison per `pitch-archetypes.md`.
- **Why Now timeline** (1 slide, optional but strongly recommended for high-stakes pitches).

**Internal scenarios — expand Beat 4 with v1 6-Phase Phase 5**:
- 6-Phase Phase 5 (Scalability & Roadmap): ecosystem, near-term plan, transferability, long-term roadmap. These slides are framed as "evidence that our advantage compounds."

**Discipline**:
- "Why Us" must be **structural**, not "we work harder." Focus on what competitors structurally cannot replicate within the relevant time horizon.
- Pair with quarterly de-risking ("if we don't deliver, you can adjust or pause") for risk-averse audiences.

### Beat 5 — Ask (specific request + emotional close)
**Job**: Give the audience exactly one decision to make.

**Components**:
- **The Ask slide** (1 slide): a single concrete request — not a wish list. "Approve 4 FTE headcount and Q2 budget of X" not "support this initiative."
- **Three-beat close** (oral, on the same slide or the closing slide):
  1. Personal connection ("when I first saw this problem...")
  2. User validation quote ("the SMEs are asking when they can use this")
  3. Urgency + Ask ("the risk isn't trying — it's waiting. We need your go.")

**Discipline**:
- One Ask per deck. Multiple asks = zero asks.
- Ask must be **decidable in the room** (binary: yes/no), not "go think about it."
- Save thanks and acknowledgements for AFTER the ask, not before. Gratitude before ask weakens the ask.

---

## 2. Three-Tier Length Compression

Every deck gets produced in three durations. Decide upfront which one is needed; do not retrofit.

| Beat | 3 min (Elevator) | 15 min (Standard) | 45 min (Deep-dive) |
|---|---|---|---|
| **1. Hook** | 30s / 1 slide | 2 min / 2 slides | 5 min / 3 slides |
| **2. Insight** | 30s / 1 slide | 2 min / 1-2 slides | 5 min / 2-3 slides |
| **3. Wow + Proof** | 1 min / 1 slide | 5 min / 3-4 slides | 15 min / 6-8 slides |
| **4. Why Us / Why Now** | 30s / 1 slide | 4 min / 4-5 slides | 12 min / 8-10 slides |
| **5. Ask** | 30s / 1 slide | 2 min / 1-2 slides | 8 min / 3 slides + Q&A |
| **Backup (Q&A)** | 0 | 2-3 hidden slides | 5-8 hidden objection slides |
| **Total slides** | ~5 | ~10-14 | ~22-30 + backup |

### Compression rules

**3 min (Elevator)**:
- Drop everything except the Wow Moment, the Insight, and the Ask.
- No Why Us matrix — just one line in the oral script: "we're the only team with X+Y+Z."
- No backup slides; if asked a hard question, redirect to follow-up meeting.

**15 min (Standard)**:
- Full 5-Beat structure.
- For internal audiences, expand Beat 3 with 6-Phase Phases 2-4 (capability ladder + demo + numbers).
- 2-3 backup slides for the top objections from `objection-handling.md`.

**45 min (Deep-dive)**:
- Full 5-Beat + full 6-Phase expansion if internal.
- All 5 objections from `objection-handling.md` get backup slides.
- Add a "Lessons & Learnings" section between Beat 3 and Beat 4 for retrospective audiences.
- Q&A is a planned beat, not an afterthought.

### Anti-pattern: "the same deck, longer"
A 45-min deck is **NOT** a 15-min deck with more bullets per slide. It's a 15-min deck with more *evidence* per claim. Slide count grows; words-per-slide does not.

---

## 3. Layer 2 — The 6-Phase Internal Expansion (preserved from v1)

This is the original v1 structure. It now operates as a **specialized expansion pattern inside Beats 3-4** when the audience is internal leadership and the goal is budget/title/resource approval.

When to invoke Layer 2:
- Audience has institutional context (knows you, knows the company, knows the problem)
- Goal is approval of a concrete ask, not mindset change
- Length is 15+ minutes
- Risk-averse decision-making culture (medical device, finance, regulated industries)

### Phase 1 — Strategic Urgency (becomes Beat 1's "Why Now" expansion)
**Three-signal validation framework**:
1. National/Policy level — government is pushing this direction
2. Industry/Competition level — competitors are already moving
3. Internal/Business level — our own teams have validated the pain

Key sentence pattern: "我们不是在创造需求；我们是在响应需求。" (We're not creating demand; we're responding to it.)

### Phase 2 — Capability Demonstration (becomes Beat 3's "Proof" depth)
**Escalating difficulty ladder**:
- V1 Easy: Framework generation (e.g., 2 days → 2 minutes)
- V1 Medium: Consistency checking (manual cross-check → automated)
- V3 Hard: Content generation (the "hardest nut to crack")
  - Step 1: Template-based (low % of report)
  - Step 2: Comparison & highlighting (mid % of report)
  - Step 3: Expert reasoning (the "soul" of the document)

Each capability slide uses the **Left-Explain / Right-Prove** layout. The left side never stands alone without evidence on the right.

### Phase 3 — Live Product Demo (becomes Beat 3's "slow-motion replay")
**4-step user flow walkthrough**:
1. Upload & Extract
2. Manual Verification
3. Difference Highlighting
4. Difference Analysis

Full-screen UI screenshots with minimal overlay text. Let the product speak; the oral script provides walk-through.

### Phase 4 — Impact Quantification (becomes Beat 3's metrics close)
**Architecture + Numbers combo**:
- Architecture slide: HOW it works under the hood
- Effectiveness slide: WHAT it achieves in numbers

Key metrics always include time savings, automation coverage, accuracy threshold, efficiency multiplier.

Key sentence pattern: "X 不是终点，是起点。攻克 X，就打通了整个 Y 的技术路径。"

### Phase 5 — Scalability & Roadmap (becomes Beat 4's depth)
**Four-layer argument**:
1. Ecosystem: We have the team, data, and process to iterate fast
2. Near-term plan: Quarterly deliverables with concrete dates
3. Transferability: % reusable + % customizable architecture
4. Long-term roadmap: V1→V5 progression

Every phase carries a "risk mitigation" message: "每季度可验收成果，交付不达标可调整或暂停."

### Phase 6 — Call to Action (becomes Beat 5)
Already mapped 1:1 to Beat 5. Three-beat closing remains identical.

---

## 4. Slide content composition rules (carried forward from v1)

### Rule 1: Title = Conclusion, Not Topic
- BAD: "Technical Architecture"
- GOOD: "Tech" (short) — with the architecture diagram doing the talking
- BAD: "Project Results"
- GOOD: "Project Effectiveness" — with KPI banner showing -8Day / 70% / >80%

### Rule 2: Every Feature Slide Has Four Sections
```
┌──────────────────────────┐
│ 📊 Chapter Scope         │  ← What portion of the document this covers
├──────────────────────────┤
│ ⚙️ Technical Challenges  │  ← What makes this hard (3 boxes)
├──────────────────────────┤
│ 🔄 Process Flow          │  ← How the AI does it (numbered steps)
├──────────────────────────┤
│ ✅ Quality Gate          │  ← Proof it works (2-3 metrics)
└──────────────────────────┘
```

### Rule 3: Pain Point Slides Use the A-B-C-D Pattern
Lettered badges (A, B, C, D) in orange circles, each followed by a bold 2-word label. Map each pain point to a solution on the right side with arrow connections.

### Rule 4: Numbers Are Heroes
When a number tells the story, make it the LARGEST element on the slide:
- "55%" at 72pt bold tells the audience this is the bulk of the work
- "-8Day" at 48pt bold with a lightning icon tells the audience this saves real time
- "0%" false-negative rate is more powerful than any paragraph of text

### Rule 5: Transition Sentences Bridge Slides
Each oral script section ends with a forward-looking sentence:
- "这只是开胃菜..." → bridges to harder features
- "我们的目标不止于此..." → bridges to the next capability
- "让我们看看 AI 是否能 meet our expectations" → bridges to demo results

### Rule 6 (NEW in v2): Wow Before Why
For Beat 3, the order is **Wow Moment FIRST, explanation SECOND**. v1's order ("here's our approach → here's the demo → here are the numbers") is the teaching order. The persuasion order is reversed: "here's the result → here's how → here's what makes it possible."

### Rule 7 (NEW in v2): Name the Elephant
For each deck, identify 2-3 likely objections and surface them proactively in-deck. See `objection-handling.md` for the full discipline. The standard surfacing locations:
- Right after the Wow Moment ("but is this real?" doubts)
- During Beat 4 ("but why can't HQ team do this?")
- Just before Beat 5 ("but what if we fail?")

---

## 5. Content granularity standards

### What Goes ON the Slide (PPT)
- Short titles (2-6 words)
- Numbered lists (max 3-4 items, each 1 line)
- Metric callouts (number + label)
- Process flow diagrams
- Screenshots / evidence
- Tables (max 4-5 rows visible)
- Progress bars with percentages

### What Goes IN the Oral Script Only
- Context and backstory
- Analogies and metaphors
- Emotional appeals
- Detailed methodology explanations
- Acknowledgements
- Transition sentences
- **NEW: Cold Open setup**
- **NEW: Wow Moment pause discipline**
- **NEW: Objection one-liners**

### What NEVER Goes on the Slide
- Full sentences / paragraphs of prose (except in evidence screenshots)
- Generic labels like "Introduction" or "Summary"
- More than 3 bullet points without visual structure
- Unsupported claims without accompanying data
- The Cold Open hook (it lives in the oral script — the slide is one image or one short sentence)

---

## 6. Data presentation standards (carried forward from v1)

### Time Savings
Format: `[Original Time] → [AI Time]` or `-[Saved Days]/Project`
Example: "2-4 hours → 4 minutes" or "-8Day/Project"

### Accuracy Metrics
Format: `>[Percentage]%` with label. Always show alongside companion metrics (speed + accuracy + intervention-friendliness).

### Comparison (Before/After)
Use a 4-column table: `Actions | Manual | AI Augmented | Improvement`

### Volume/Scope
Use stacked bar charts or progress bars to show how much of the document AI covers, how many documents across BUs, chapter-by-chapter breakdown.

---

## 7. Stakeholder-aware messaging (carried forward from v1)

### For Technical Audience
- Show architecture diagrams (Hand Layer / Brain Layer)
- Mention specific tech: SFT/DPO, RAG, Reranking, Modular SLM chains
- Include Quality Gate metrics with decimal precision

### For Business / Executive Audience
- Lead with time savings and ROI numbers
- Use the "coffee break" analogy
- Emphasize risk mitigation: "quarterly deliverables, pause if not meeting targets"
- Frame as competitive advantage

### For Mixed Audience (Jianan's typical scenario)
- Structure slides so business messages are visually dominant (large numbers, bold titles)
- Embed technical depth in the left-side explanation area or oral script
- Use the right-side evidence panel to satisfy technical reviewers
- The oral script handles the emotional/strategic layer that executives respond to

### For External / Investor Audience (NEW in v2)
- Lead with the Inevitable Future Cold Open
- Front-load the Wow Moment — this audience has lower patience for buildup
- Why Us matrix is mandatory and must include named competitors
- Why Now timeline is mandatory; without it, the pitch reads as "interesting but not urgent"
- Drop or compress the 6-Phase Internal Expansion entirely

---

## 8. Pre-deck checklist (NEW in v2)

Before drafting any deck, complete this checklist:

- [ ] Audience identified (internal / external / investor / cross-org / public)
- [ ] Length confirmed (3 / 15 / 45 min)
- [ ] Goal stated in one sentence ("get X to approve Y")
- [ ] Cold Open archetype selected (Painful / Inevitable / Counterintuitive / Loaded)
- [ ] Insight thesis written in one sentence
- [ ] Wow Moment identified (the t-shirt-line for the talk)
- [ ] Why Us matrix drafted (3 columns minimum)
- [ ] Top 3 objections workshopped per `objection-handling.md`
- [ ] The Ask written as a single binary decision
- [ ] If internal: 6-Phase expansion mapped to Beats 3-4
- [ ] If external: 6-Phase explicitly NOT used; check Beat 3 isn't padded with internal ladder logic

Skipping this checklist produces decks that win the friendly room and lose the political one.
