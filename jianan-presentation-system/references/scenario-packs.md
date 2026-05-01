# Scenario Packs — 6 个场景的演讲方法库

这是 v3 引入的场景路由层。v2 的 5-Beat 是**通用引擎**，但同一引擎在不同场景下的**调参**完全不同 —— 一份给管理层的立项汇报和一份产品发布会用同样的 5-Beat 结构会两边都不对。

本文件定义 6 个高频场景，每个场景包含：理论根基、操作框架、AI 工具建议、5-Beat 调参参数、Jianan 项目实例。

---

## 0. 场景路由决策树

接到任务时，先用这棵树定位场景：

```
谁是听众？
├── 决策者（批资源/做选择）── 怎么决策？
│   ├── 风险规避型（医疗/金融/政府）→ ① 管理层汇报
│   ├── 回报寻找型（VC/天使）         → ④ 投资人路演
│   └── 解决方案寻找型（采购/客户）    → ⑤ 营销卖货
│
├── 同行/学习者（评议/学习） ── 来干嘛？
│   ├── 评议你的工作（HQ/同行）       → ② 技术分享
│   └── 学会自己做（培训/新人）       → ⑥ 培训教学
│
└── 期待者（被惊喜/被启发）           → ③ 产品发布
```

**当听众身份混合时**：选**最难说服**的那一类作为主场景，其他听众用 backup slides 补足。

---

## 场景包 ①：管理层立项汇报（Executive Pitch）

**一句话定位**：让风险厌恶的决策者批准一个具体诉求。

**理论根基**：
- **McKinsey Pyramid Principle**（Barbara Minto）—— 结论先行，自上而下展开
- **MECE 原则** —— 论据分组不重不漏
- **Risk Narrative Theory**（Daniel Kahneman, *Thinking Fast and Slow*）—— 损失厌恶 2.5 倍于获得，"不做的代价" > "做的收益"
- **Eisenhower Matrix** —— 紧急/重要四象限定位你的请求

**5-Beat 调参**：
| Beat | 该场景下的权重 | 关键动作 |
|---|---|---|
| 1 Hook | 中 | 用"三信号"（政策+行业+内部）建立紧迫 |
| 2 Insight | 低 | 一句话核心论断即可 |
| 3 Wow + Proof | 高 | PoC 数据 + 数字对比 |
| 4 Why Us / Why Now | **极高** | quarterly checkpoint + 暂停机制 |
| 5 Ask | **极高** | 单一二元决策 |

**操作框架（5 步）**：
1. **Frame the Decision** —— 开场就把会议定性："今天我需要从您这里拿到一个 yes/no 决定"
2. **Lead with the Conclusion** —— 第一张幻灯片就是结论 + Ask
3. **Build Pyramid Down** —— 3 个论据展开（紧迫性 + 可行性 + 风险可控）
4. **De-risk Aggressively** —— 季度可拆、达不到目标可暂停
5. **Single Binary Ask** —— 最后一张幻灯片只有一个决策

**AI 作图建议**：
- **风险热力图**：让 Claude 生成 5×5 风险矩阵（影响 × 概率），用 HTML/CSS 渲染
- **决策树**：napkin.ai 一键生成"如果 yes 怎样 / 如果 no 怎样"
- **季度甘特**：Excel + Mermaid 显示 checkpoint，每季度可终止

**Jianan 实例**：你的 R·Agent PoC 收尾汇报就是这个场景。值得在 v3 里做的优化：开场加 Cold Open（"上周三晚上 11 点..."），中间压缩成一个 Wow Moment（8h → 4min），最后只留一个 Ask（不要既要 title 又要预算又要人）。

---

## 场景包 ②：技术分享（Tech Talk）

**一句话定位**：让同行评议你做对了，并且想跟你学。

**理论根基**：
- **Feynman Technique** —— 能用本科生听懂的话讲清楚才算真懂
- **Curse of Knowledge 反向规避**（Heath Brothers, *Made to Stick*）—— 专家忘了自己曾经不懂什么
- **Bret Victor "Inventing on Principle"** —— 用 live demo 替代静态幻灯片
- **同行评议隐形规则** —— 工程师不要 marketing，要可证伪的细节和失败路径

**5-Beat 调参**：
| Beat | 权重 | 关键动作 |
|---|---|---|
| 1 Hook | 低 | Counterintuitive Insight 原型最佳 |
| 2 Insight | **极高** | 一个反直觉论断作为整场支柱 |
| 3 Wow + Proof | **极高** | 可复现的代码/数据/失败案例 |
| 4 Why Us | 低 | 不要卖团队，让作品说话 |
| 5 Ask | 低 | 给 GitHub/文档链接，不强 push |

**操作框架（4 步）**：
1. **One Counterintuitive Thesis** —— 一个反直觉论断（"我们花 3 个月才学会：不该追求 100% 准确率"）
2. **Reproduce Before Generalize** —— 先讲一个具体可复现例子，再抽象成原理
3. **Show the Failure** —— 展示失败路径，建立 credibility（"我们也试过 RAG，结果是..."）
4. **Open the Code** —— 结尾给 GitHub/文档/SOP 链接

**AI 作图建议**：
- **Excalidraw**（手绘风）—— 工程师爱这种"未完成感"
- **Mermaid** in Markdown —— sequence diagram、flowchart、gantt
- **Manim**（3Blue1Brown 用的）—— 关键算法动画
- **Carbon.now.sh** —— 生成漂亮代码截图

**Jianan 实例**：5 月份给 HQ 技术团队那场 15 分钟，用这个场景包。Cold Open："做 LLM 自动化最大的认知误区是追求 100% 准确率"，主线讲 Graceful Degradation 的 L1/L2/L3 设计，给 GitHub 仓库链接收尾。

---

## 场景包 ③：产品发布（Product Launch）

**一句话定位**：在听众心智中烙下一个不会忘的瞬间。

**理论根基**：
- **Apple Keynote 模式**（Steve Jobs）—— Setup → Conflict → Resolution → Delight
- **Pixar 故事曲线** —— Once upon a time / Every day / Until one day / Because of that ×2 / Until finally
- **Endowment Effect**（Richard Thaler）—— 让听众"提前拥有"产品才会认同它
- **Peak-End Rule**（Daniel Kahneman）—— 人记忆的是峰值瞬间和结尾

**5-Beat 调参**：
| Beat | 权重 | 关键动作 |
|---|---|---|
| 1 Hook | 高 | Painful Status Quo 把痛刻画到极致 |
| 2 Insight | 中 | 暗示有解法但不揭晓 |
| 3 Wow + Proof | **极高** | 整场围绕 Reveal 那一刻编排 |
| 4 Why Us | 低 | 让产品说话 |
| 5 Ask | 中 | "什么时候能用" + 一句记忆点 |

**操作框架（5 步）**：
1. **Status Quo Pain** —— 把现状之痛刻画到极致（像 Apple 讲 iPhone 之前怎么吐槽 BlackBerry）
2. **Hint at Magic** —— 暗示有解法但不揭晓（"我们想，如果可以..."）
3. **The Reveal** —— 揭晓时刻，配 Wow Moment 三幕（Setup → Reveal → Pause）
4. **Live Demo** —— 让产品自己演讲，演讲者只做"翻译"
5. **Availability + Tagline** —— 什么时候能用 + 一句记忆点（"think different" / "1000 songs in your pocket"）

**AI 作图建议**：
- **Figma + Magic** / **Galileo AI** —— AI 生成高保真 Mockup
- **Runway / Pika / Sora** —— AI 生成产品演示短视频
- **Midjourney / Flux** —— 发布会主视觉海报、英雄镜头
- **Tone.js** —— 演示页面里加音效（按 Apple 的细节标准）

**Jianan 实例**：R·Agent Knowledge Platform 上线时用这个场景包。Cold Open 用 Painful Status Quo（"上周三晚上 11 点..."），主轴是 Reveal "把同一份 PDF 让旧流程和新平台同时跑"，最后给 tagline："Knowledge that compiles itself."

---

## 场景包 ④：投资人路演（VC Pitch）

**一句话定位**：在 10 分钟里让投资人相信你能 100x 回报。

**理论根基**：
- **YC's "10 slides in 10 minutes"** 经典模板
- **Sequoia "Writing a Business Plan" 9 字真言**：Company purpose / Problem / Solution / Why now / Market / Competition / Product / Business model / Team
- **Crossing the Chasm**（Geoffrey Moore）—— 从早期采用者到主流市场的鸿沟论证
- **TAM-SAM-SOM 三圈估算** —— 市场规模可信化

**5-Beat 调参**：
| Beat | 权重 | 关键动作 |
|---|---|---|
| 1 Hook | **极高** | Inevitable Future 原型；前 30 秒决定一切 |
| 2 Insight | 高 | 你独家看到的市场机会 |
| 3 Wow + Proof | **极高** | Traction（用户/收入/增速）即 Wow |
| 4 Why Us / Why Now | **极高** | 团队 + 时机窗口 |
| 5 Ask | **极高** | 多少钱、换多少股、用来做什么 |

**操作框架（YC 经典 10 张）**：
1. Cover  2. Problem  3. Solution  4. Why Now  5. Market Size
6. Product  7. Business Model  8. Traction  9. Team  10. The Ask

**AI 作图建议**：
- **Tome / Gamma** —— AI 生成 pitch deck 初稿
- **Beautiful.ai** —— TAM 圈图、增长曲线模板
- **Notion AI** —— 整理 cap table、unit economics
- **Pitch.com** —— 协作编辑 + 数据嵌入

**Jianan 实例**：未来如果创业，这个场景包是核心。当下不写示范，但提前做好框架储备。

---

## 场景包 ⑤：营销卖货 / 内部销售（Sales Pitch）⭐

**一句话定位**：把客户变成英雄，让他们因为你而成功。

**这是 Jianan 最缺的场景包**。详细方法见同名书章节 `book/chapters/ch09-sales-pitch.md`。这里只放骨架。

**理论根基**：
- **StoryBrand 框架**（Donald Miller, *Building a StoryBrand*）—— 客户是英雄，你是向导
- **Jobs-to-be-Done**（Clayton Christensen）—— 客户不买产品，买"完成某个任务的进步"
- **Challenger Sale**（Matthew Dixon）—— 教育客户、量身定制、掌控对话
- **AIDA 漏斗** —— Attention / Interest / Desire / Action
- **SPIN 提问法**（Neil Rackham）—— Situation / Problem / Implication / Need-payoff

**5-Beat 调参**：
| Beat | 权重 | 关键动作 |
|---|---|---|
| 1 Hook | 高 | 站在客户视角描绘他们的"今天" |
| 2 Insight | **极高** | 让客户意识到他们没意识到的问题 |
| 3 Wow + Proof | **极高** | 客户证言 + 客户用了之后的样子 |
| 4 Why Us | 中 | 你是向导不是英雄 |
| 5 Ask | **极高** | 直接 CTA：试用/采购/签约 |

**操作框架（StoryBrand 7 步）**：
1. **A Character** —— 客户是主角
2. **Has a Problem** —— 外在 + 内在 + 哲学三层
3. **Meets a Guide** —— 你是甘道夫，不是 Frodo
4. **Who Gives Them a Plan** —— 明确 3 步行动
5. **And Calls Them to Action** —— 直接 CTA
6. **That Helps Them Avoid Failure** —— 损失厌恶钩子
7. **And Ends in Success** —— 成功画面

**AI 作图建议**：
- **HeyGen / Synthesia** —— 客户证言视频、AI 数字人 walkthrough
- **ChatGPT / Claude** —— 生成 customer journey map
- **Loom + AI Summary** —— 异步销售视频

**Jianan 实例**：跨部门推广 R·Agent 给其他 BU 时用这个场景包。详细案例见书章节。

---

## 场景包 ⑥：培训教学（Teaching / Workshop）

**一句话定位**：让学员能离开会议室之后自己做一遍。

**理论根基**：
- **Cognitive Load Theory**（John Sweller）—— 工作记忆只有 4±1 块
- **ADDIE 模型** —— Analyze / Design / Develop / Implement / Evaluate
- **Bloom's Taxonomy** —— 记忆 → 理解 → 应用 → 分析 → 评估 → 创造（依次升级）
- **Spaced Repetition**（Hermann Ebbinghaus）—— 间隔重复

**5-Beat 调参**：
| Beat | 权重 | 关键动作 |
|---|---|---|
| 1 Hook | 中 | 学员痛点共鸣 |
| 2 Insight | 高 | 一个核心心法 |
| 3 Wow + Proof | **极高** | Demo + 学员动手 |
| 4 Why Us | 低 | 不需要 |
| 5 Ask | 中 | 给作业 + 资源链接 |

**操作框架（Tell-Show-Do-Review）**：
1. **Tell**（讲原理，1/4 时间）
2. **Show**（演示一遍，1/4 时间）
3. **Do**（学员动手，**1/2 时间**）—— 这是和其他场景最大区别
4. **Review**（回顾 + 答疑）

**AI 作图建议**：
- **Loom + AI Summary** —— 异步课程
- **Khanmigo / Claude Tutor** —— AI 辅导生成练习题
- **Anki** + AI 自动出卡片 —— spaced repetition

**Jianan 实例**：给 SME 培训"如何写 business_rules.yaml"用这个场景包。

---

## 场景使用频率与优先级（给 Jianan 当下的）

| 场景 | 当下频率 | 未来 12 个月预期 | 优先建设 |
|---|---|---|---|
| ① 管理层汇报 | 高 | 高 | ⭐⭐⭐ 已成熟，持续优化 |
| ② 技术分享 | 中 | 高（HQ 对齐） | ⭐⭐⭐ 5 月就要用 |
| ③ 产品发布 | 低 | 中（Knowledge Platform） | ⭐⭐ 提前储备 |
| ④ 投资人路演 | 零 | 低（创业可能） | ⭐ 暂缓，框架储备即可 |
| ⑤ 营销卖货 | **中（被低估）** | **高（跨 BU 推广）** | ⭐⭐⭐ **最大缺口** |
| ⑥ 培训教学 | 低 | 高（团队扩张后） | ⭐⭐ 团队增长后就要用 |

---

## 跨场景的通用原则（无论哪个场景都不能违反）

不论你处在哪个场景，v2 SKILL 的以下原则都生效：

1. **12pt 字号下限不动**（视觉统一）
2. **Wow Moment 永远集中，不分散**（Apple 模式）
3. **Name the Elephant**（主动认领反对意见）
4. **One Ask per deck**（一次只做一个决定）
5. **PAUSE 标注**（在剧本里用 `[PAUSE 5s]` 强制守护）

场景差的是**重点和路径**，不变的是**说服力的物理学**。
