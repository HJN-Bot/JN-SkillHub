# Oral Script Guide — Jianan Presentation System

This document captures Jianan's oral presentation style, bilingual code-switching strategy, and script-to-slide mapping methodology.

---

## 1. Script Format Standard

Each slide's oral script follows this Markdown structure:

```markdown
## 【Slide N】Title (约X分钟)

[Chinese narration body]

[Optional English-only paragraphs in bold for strategic emphasis]

---
```

### Timing Annotations
- Every slide section includes a time estimate: `(约45秒)`, `(约1分钟)`
- Total presentation targets: 12-15 minutes
- Slide timing breakdown:
  - Opening/context slides: 45s - 1min each
  - Feature demo slides: 45s - 1min each
  - UI walkthrough (4 slides combined): 45s total
  - Impact/results slides: 45s each
  - Roadmap/plan slides: 30s - 1min each
  - Closing: 45s

---

## 2. Bilingual Code-Switching Strategy

Jianan uses a **strategic bilingual approach** — NOT random mixing. The rules are precise:

### Chinese is the Default Narration Language
All explanatory context, transitions, emotional appeals, and audience interaction are in Chinese.

### English is Used in These Specific Situations:

#### Situation A: Technical Terms (inline)
Technical terms stay in English within Chinese sentences. Never translate these:
- Product names: R·Agent, CER, PTR, NMPA, BU, eRPS
- Technical concepts: AI, LLM, Prompt Engineering, RAG, SFT/DPO, Reranking
- Architecture terms: Hand Layer, Brain Layer, UI Layer
- Metrics: false positive, false negative, tokens/sec
- Methodology: human-in-the-loop, one-click generation

**Example**: "我们的AI方案自动完成，具体带来四个功能" — 四个功能's details can use English labels.

#### Situation B: Full English Paragraphs (strategic emphasis)
Certain high-impact sections are delivered ENTIRELY in English. These are marked in **bold** in the script. This happens when:

1. **Quoting the slide's key argument** that is written in English on the slide
2. **Describing technical methodology** that would lose precision in translation
3. **Presenting the roadmap progression** where English maintains professional gravitas
4. **Closing impact statement** for maximum memorability

**Example from Slide 8**:
> "**We first trained the AI to detect whether differences exist; utilized past data to have this experience-driven categorization, such as structure difference, software difference, or parameter difference. Finally, we designed the AI to combine product knowledge, clinical knowledge, and understand how those elements will affect the clinical impact to make judgments, like completely mimicking the reasoning process of a CUC expert.**"

#### Situation C: English Bridge Phrases (conversational)
Short English phrases embedded in Chinese flow for natural bilingual cadence:
- "meet our expectations"
- "promising准确率"
- "low-hanging fruits"
- "human-in-the-loop"

### What to NEVER Do
- Don't translate technical terms into awkward Chinese equivalents
- Don't switch to English mid-sentence for non-technical content
- Don't deliver the entire presentation in English (loses connection with Chinese-speaking executives)
- Don't use English for emotional/persuasive appeals (Chinese is more impactful for this audience)

---

## 3. Narration Voice & Tone

### Confident but Not Arrogant
- Use "我们" (we) not "我" (I) for accomplishments
- Acknowledge limitations: "当然毕竟是一个月产出的工具原型" (Of course, this is still a one-month prototype)
- Credit the team: "非常感谢BU、DTI、Innovation等团队"

### Data-Driven Persuasion
- Always cite specific numbers: "FY25约有25份报告，单份CER报告平均2个月"
- Use vivid comparisons: "2分钟解决原本需要2天的手工任务"
- Deploy memorable analogies: "你去倒杯咖啡，回来时30页比对表已经生成好了"

### Emotional Escalation for Closing
The emotional intensity increases toward the end:
- Middle slides: Factual, methodical
- Results slides: Confident, assertive
- Closing: Personal, passionate, slightly urgent

Key emotional beats:
1. Personal motivation: "我就在想,能不能用AI加速注册文档？"
2. User validation: "CUC的专家也在问：这个工具什么时候能正式用？"
3. Urgency call: "AI时代最大的风险不是试错，是犹豫"
4. The ask: "就差领导的一个Go"

---

## 4. Slide-to-Script Mapping Patterns

### Pattern A: Problem → Solution → Bridge
Used for feature introduction slides.

```
[State the old way / pain point]
→ "传统流程是什么样的呢？...至少需要2天时间"

[Present the AI solution]  
→ "现在我们的AI方案自动完成，具体带来四个功能..."

[Bridge to next slide]
→ "这只是开胃菜，证明AI确实能理解监管语言"
```

### Pattern B: Challenge → Demo → Metric → Impact
Used for technical capability slides.

```
[State why this is hard]
→ "要知道，差异比对表占整个CER报告55%的体量"

[Describe what AI does]
→ "AI全自动完成资源分析、信息提取、差异识别、格式调整——一气呵成"

[Present the metric]
→ "实测数据：准确率90%以上，4分钟生成20到30页"

[Make it vivid]
→ "打个比方：你去倒杯咖啡，回来时30页比对表已经生成好了"

[State the significance]
→ "这不是效率提升，这是工作方式的革命"
```

### Pattern C: Quick Walkthrough
Used for UI demo slides (multiple slides narrated quickly).

```
[Step label] + [Action] + [Time/Result]

"第一步，上传提取——拖拽上传PTR、注册证等文件，2到3秒完成信息抓取。"
"第二步，人工验证——AI提取的关键信息自动展示，用户快速核对，错了点击修改即可。"
```

### Pattern D: Strategic Summary → Ask
Used for roadmap and closing slides.

```
[Summarize what was achieved]
→ "CER工具能完成70%的自动化，给出promising准确率，效率提升40倍"

[External pressure]
→ "NMPA在推，竞争对手在做，我们不能只是观望"

[Risk framing]
→ "AI时代最大的风险不是试错，是犹豫"

[Readiness statement]
→ "我们团队准备好了，技术验证完了，用户需求有了"

[The ask]
→ "现在，就差领导的一个Go"
```

---

## 5. Key Rhetorical Devices

### The "Three-Signal" Framework
Open with 3 validating signals from different levels:
- "第一...第二...第三..." structure
- National → Industry → Internal (macro to micro)
- Used in opening to establish urgency

### The "Not X, but Y" Reframe
Turn a potential objection into a strength:
- "我们不是在创造需求;我们是在响应需求" 
- "CER不是终点，是起点"
- "这不是效率提升，这是工作方式的革命"
- "最大的风险不是试错，是犹豫"

### The "Coffee Break" Vivid Analogy
Make abstract efficiency gains tangible:
- "你去倒杯咖啡，回来时30页比对表已经生成好了"
- "你只需要花30分钟review，而不是4小时从零开始"

### The "User Quote" Validation
Quote real user feedback as social proof:
- "CUC的专家也在问：这个工具什么时候能正式用？我们下个项目就想用。"
- "这句话告诉我：我们做的事情是有价值的，是被需要的。"

### The "Risk Mitigation" Reassurance
Address executive concerns about investment risk:
- "小步快跑，降低决策风险"
- "每季度可验收成果，Q2交付不达标，可以调整或暂停后续投入"

---

## 6. Dual-Language Script Deliverable Format

When producing oral scripts, always deliver TWO files:

### File 1: `Presentation_Chinese_Oral.md`
- Primary narration in Chinese
- English technical terms inline
- English paragraphs in **bold** where strategic
- Timing annotations for each slide
- Total estimated duration at the end

### File 2: `Presentation_English_Oral.md`
- Full English translation/adaptation (NOT word-for-word)
- Same structure and timing annotations
- English version tends to be slightly more formal and concise
- Strategic emphasis sections match the Chinese bold sections
- Maintains the same rhetorical devices adapted for English

### Key Differences Between Versions
| Aspect | Chinese Version | English Version |
|--------|----------------|-----------------|
| Tone | More personal, emotional closing | More professional, measured |
| Technical depth | Embedded naturally | Slightly more explicit |
| Analogies | Chinese cultural references OK | Universalized analogies |
| Opening | "各位领导早上好" | "Good morning, everyone" |
| Closing | "就差领导的一个Go" | "We just need the Go decision" |
| Transitions | More colloquial bridges | Cleaner, more structured bridges |
