---
name: qt-wiki-framework
description: Question-Driven Thinking (QT) — a structured decision framework that replaces gut-feeling decisions with mandatory questions at each product stage. Every phase is a set of questions that MUST be answered before proceeding. Can't answer = not ready to move forward. Pairs with PLO for T2+ project execution.
aliases: [QT, question-tree, qt-framework]
---

# QT Wiki：Question-Driven Thinking 框架

**用结构化提问替代拍脑袋决策。** 产品设计的每一个阶段，不是一个"我觉得该做 X"的直觉判断，而是一组必须回答的问题。答不上来 = 还没想清楚 = 不能进入下一阶段。

---

## QT 决策树

```
产品想法出现
  │
  ▼
┌─────────────────────────────────────┐
│ Q0: 这是什么类型的项目？              │
│ → B2B (有外部决策者)                  │
│ → ToC (面向消费者)                    │
│ → Personal (我自己决定)               │
└───────────────┬─────────────────────┘
                │
     ┌──────────┼──────────┐
     ▼          ▼          ▼
┌──────────┐ ┌──────────┐ ┌──────────┐
│ B2B Path │ │ ToC Path │ │ Personal │
│  7 问    │ │  7 问   │ │  7 问   │
└──────────┘ └──────────┘ └──────────┘
```

---

## Path A：B2B / 利益方驱动

### Q1: Stakeholder Alignment
**核心问题：谁在乎这个项目？他们真正要什么？**

| # | 必须回答 | 答不上来的后果 |
|---|---------|-------------|
| 1 | 谁是这个项目的最终决策者？ | 做完了发现根本没人在乎 |
| 2 | 他们最关心的 1 个指标是什么？ | 方向对了但优先级全错 |
| 3 | 有什么没说出口的约束？ | 做到一半被叫停 |
| 4 | 如果这个项目不做了，谁的损失最大？ | 无法判断真实需求 vs 随口一提 |

**判断标准：** 能写出 3 个 stakeholder，每人 1 个核心诉求，所有非明面约束已记录。

**使用 Skill：** `grill-me` · `web_search`

---

### Q2: Constraint Elicitation
**核心问题：什么会杀死这个项目？**

| # | 必须回答 | 答不上来的后果 |
|---|---------|-------------|
| 1 | 预算是多少？时间线是什么？ | 无限期开发 |
| 2 | 必须对接的系统/平台有哪些？ | 做完发现接不上 |
| 3 | 合规/安全/法务要求？ | 上线前被拦住 |
| 4 | 团队里谁有 veto 权？ | 一个人说不行就全推翻 |

**判断标准：** 约束清单已写，利益相关方确认。没有人能事后说"我以为你知道"。

**使用 Skill：** `grill-me`

---

### Q3: Architecture Decision
**核心问题：用什么技术栈？为什么？**

| # | 必须回答 | 答不上来的后果 |
|---|---------|-------------|
| 1 | 为什么选这个栈而不是其他？ | 技术债从第一行代码开始 |
| 2 | 数据流是什么样的？存储方案是什么？ | 改需求 = 重建 |
| 3 | 哪些模块可以独立开发/测试？ | 一人卡住全员等待 |
| 4 | 失败模式是什么？怎么恢复？ | 出问题只能人工救 |
| 5 | 系统的独特优势是什么？（vs 替代方案） | 做完了发现不必要 |

**判断标准：** 架构图存在。技术决策有理由。每个模块有 owner。数据存储策略已定。

**使用 Skill：** `first-principles-decomposer` · `web_search` · `claw-vibe-project` · MAE pipeline

**外部参考：** [`obra/superpowers`](https://github.com/obra/superpowers) · [`addyosmani/agent-skills`](https://github.com/addyosmani/agent-skills)

---

### Q4: Design & UX
**核心问题：用户看到什么？怎么交互？**

| # | 必须回答 | 答不上来的后果 |
|---|---------|-------------|
| 1 | 用户进来的第一屏是什么？ | 迷失 |
| 2 | 核心操作需要几步？ | 操作路径太长 |
| 3 | 审美方向是什么？（选一个极端） | AI-slop 风格 |
| 4 | 移动端怎么适配？ | 手机打不开 |

**判断标准：** 设计系统定义（颜色/字体/间距）。关键页面已设计。移动端断点已处理。

**使用 Skill：** `grill-me` · 按输出类型选 → Web/`open-design` · Slide/`frontend-slides` · PPT/`jianan-presentation-system` · UI/`design-front` · 高端/`impeccable-design`

---

### Q5: Development
**核心问题：怎么造出来？怎么保证质量？**

| # | 必须回答 | 答不上来的后果 |
|---|---------|-------------|
| 1 | 测试策略是什么？（TDD? 集成测试？覆盖率目标？） | 回归全是手工 |
| 2 | 怎么验证 LLM 输出质量？（Evals 阈值？） | 模型说好就是好 |
| 3 | 代码审查机制是什么？ | 垃圾代码累积 |
| 4 | CI/CD 怎么跑？ | 每次部署靠人肉 |
| 5 | 企业级（CER 类）：审计追踪够了吗？Evals ≥ 0.85？ | 合规风险 |

**判断标准：** 测试写完了。Evals 阈值设定了。CI 在跑。企业项目额外：审计追踪就位。

**使用 Skill：** `coding-agent` · `test-driven-development` · `subagent-driven-development` · `github-pr` · MAE pipeline

---

### Q6: Delivery
**核心问题：怎么交出去？怎么让人知道完成了？**

| # | 必须回答 | 答不上来的后果 |
|---|---------|-------------|
| 1 | 交付物在哪？（Vercel? Supabase? npm?） | 做了但没人看得见 |
| 2 | 部署验证做了吗？（smoke test → data check → env check） | 上线的可能是坏的 |
| 3 | 谁需要被通知？ | 做好了没人知道 |
| 4 | 用户怎么开始用？（onboarding） | 产品存在但没人用 |
| 5 | 数据存储是什么？备份策略？ | 数据丢了没法恢复 |

**判断标准：** 交付物可访问且已验证。通知已发。用户可以自己上手。数据持久化方案就位。

**使用 Skill：** `github` · `feishu-write-shared` · `airtable-dashboard`

---

### Q7: Review & Evolve
**核心问题：这次学到了什么？下次怎么更好？**

| # | 必须回答 | 答不上来的后果 |
|---|---------|-------------|
| 1 | 哪些决策是对的？证据是什么？ | 下次还会踩同一个坑 |
| 2 | 哪些技能该更新了？（SKILL.md） | Skill 资产永不增长 |
| 3 | 哪些模块可以复用到下一个项目？ | 每次从零开始 |

**判断标准：** 复盘文档存在。Skill 已更新。可复用资产已提取。

**使用 Skill：** `eight-d-optimization` · `interaction-self-reflection` · `skill-creator`

---

## Path B：ToC / 消费者产品

（Q3-Q7 与 B2B 相同）

### Q1: User Pull & Emotional Job
**核心问题：用户为什么现在会想用？用了以后应该感觉到什么？**

| # | 必须回答 | 答不上来的后果 |
|---|---------|-------------|
| 1 | 目标用户是谁？触发场景是什么？ | 没人下载 |
| 2 | 用户当前最强烈的情绪/压力是什么？ | 解决了一个不存在的问题 |
| 3 | 产品承诺的转变是什么？ | 用户试了就走 |
| 4 | 产品绝不能让用户感觉到什么？ | 触怒用户 |

**判断标准：** 能说出目标用户、触发时刻、期望转变、情感红线。

**使用 Skill：** `grill-me` · `product-sense-review` · `web_search` · `gbrain`

---

### Q2: Activation Loop & Trust Boundary
**核心问题：第一次使用怎样产生价值并获得信任？**

| # | 必须回答 | 答不上来的后果 |
|---|---------|-------------|
| 1 | 首次成功体验是什么？ | 用户不知道能干嘛 |
| 2 | 哪些隐私/安全/评价边界必须说清楚？ | 信任崩溃 |
| 3 | 用户卡住时产品怎么帮，而不是评价？ | 挫败感 → 卸载 |
| 4 | 下一次回来用的触发是什么？ | 一次性产品 |

**判断标准：** 首次成功路径、隐私边界、回访触发、失败兜底均已写清。

**使用 Skill：** `grill-me` · `product-sense-review`

---

## Path C：Personal / 个人项目

（Q3-Q7 与 B2B 相同）

### Q1: Feature Fusion
**核心问题：哪些已有产品做得好？我能偷学什么？**

| # | 必须回答 | 答不上来的后果 |
|---|---------|-------------|
| 1 | 参考了哪 3 个产品？ | 重复造轮子 |
| 2 | 从每个产品里偷了哪个具体 feature/交互？ | 做得比别人差 |
| 3 | 我做的版本比他们好在哪里？ | 没有存在的理由 |

**判断标准：** 功能融合地图存在：Product X 的 {feature} + Product Y 的 {UX} + Product Z 的 {performance}。

**使用 Skill：** `gbrain` · `web_search` · `grill-me`

---

### Q2: Scope Definition
**核心问题：做多少算够？**

| # | 必须回答 | 答不上来的后果 |
|---|---------|-------------|
| 1 | MVP 包含什么？不含什么？ | 范围蔓延 |
| 2 | 成功的标准是什么？（个人指标） | 不知道什么时候算"做完" |
| 3 | 什么时候该停？（防止过度工程） | 永远在做 |

**判断标准：** MVP 范围已写定，排除清单已写，成功标准已定义。

**使用 Skill：** `grill-me`

---

## QT 与 Skill 的映射（全路径）

| Q | B2B | ToC | Personal | 核心 Skill |
|---|-----|-----|----------|-----------|
| 0 | 模式检测 | 模式检测 | 模式检测 | `grill-me` |
| 1 | Stakeholder | User Pull | Feature Fusion | `grill-me` + `web_search` |
| 2 | Constraint | Activation | Scope | `grill-me` (+ `product-sense-review` for ToC) |
| 3 | Architecture | Architecture | Architecture | `first-principles-decomposer` + `web_search` + `claw-vibe-project` |
| 4 | Design | Design (+ToC gates) | Design | 按输出类型：`open-design` / `frontend-slides` / `jianan-presentation-system` / `design-front` / `impeccable-design` |
| 5 | Development | Development | Development | `coding-agent` + `test-driven-development` + `subagent-driven-development` + `github-pr` |
| 6 | Delivery | Delivery | Delivery | `github` + `feishu-write-shared` + `airtable-dashboard` |
| 7 | Review | Review | Review | `eight-d-optimization` + `interaction-self-reflection` + `skill-creator` |

---

## Product Sense Review 嵌入点

`product-sense-review` 不是单独一个 Q，而是在以下节点嵌入审查：

| 阶段 | 用法 | Exit Gate |
|-----|------|-----------|
| Q1/Q2（ToC） | 审查产品人格、用户心理、定位风险 | 无 P0 定位/心理风险，或已进入 grill-me 澄清 |
| Q4 Design | 对截图/PDF/原型做 labelled review | P0/P1 已修或明确接受风险 |
| Q6 Delivery 前 | Launch risk review | 隐私、反馈、失败态、onboarding、指标均有 guardrail |
| Q7 Review | 把高价值发现写回 skill | skill / checklist 有增量更新 |

---

## Grill Me 配合方式

`product-sense-review` 负责**指出风险**；`grill-me` 负责把无法回答的战略问题**逐个逼清楚**。

例：
- review 发现"像 judge，不像 coach"
- grill-me 追问："用户最怕被怎样评价？反馈应该帮他下一句继续说，还是总结他哪里错？"
- 答案回写为产品 guardrail 和 implementation TODO

---

## QT 核心操作规则

1. **逐问推进，不可跳过。** Q1 答不上来，不能进入 Q2。
2. **每问必答，不可含糊。** "大概""应该""可能是" = 没答。
3. **每问留痕。** 答案写入文档/issue/Airtable。下次 project 可直接复用 Q3-Q7 的答案框架。
4. **答不上来 ≠ 停滞。** 答不上来 = 触发 `grill-me` 对话，挖掘到能答为止。
5. **Q7 是必选项。** 不做复盘的 project 不视为完成。
6. **企业项目强化 Q5。** CER 类项目：Evals ≥ 0.85、审计追踪、≥90% 测试覆盖率。

---

## QT ↔ PLO 关系

| 维度 | QT | PLO |
|------|-----|-----|
| 定位 | **决策框架**：每阶段必须回答的问题 | **执行框架**：每阶段用什么 skill、怎么推进 |
| 粒度 | 问题级（每 Q 4-5 个必答题） | 阶段级（每 Phase 有 exit condition） |
| 触发 | 产品想法出现时 | T2+ 任务进入时 |
| 输出 | 答案文档 | 交付物 + skill 映射 + attention tracking |
| 关系 | QT 定义"想清楚了没"，PLO 定义"怎么做" | QT 是 PLO 每个 Phase 的决策前置检查 |

**协同使用：** PLO Phase 1 开始前 → 先跑 QT Q1-Q2 确保决策清晰 → 再进入 PLO 执行流。

---

## Skill 清单

| Skill | 位置 | 状态 |
|-------|------|------|
| `grill-me` | Andrew workspace | ✅ |
| `product-sense-review` | Andrew workspace | ✅ |
| `first-principles-decomposer` | JN-SkillHub | ✅ |
| `open-design` | Andrew workspace | ✅ |
| `frontend-slides` | Andrew workspace | ✅ |
| `jianan-presentation-system` | JN-SkillHub | ✅ |
| `design-front` | JN-SkillHub | ✅ |
| `impeccable-design` | JN-SkillHub | ✅ |
| `claw-vibe-project` | JN-SkillHub | ✅ |
| `coding-agent` | Andrew workspace | ✅ |
| `test-driven-development` | ok-skills | ✅ |
| `subagent-driven-development` | ok-skills | ✅ |
| `github-pr` | JN-SkillHub | ✅ |
| `github` | JN-SkillHub | ✅ |
| `eight-d-optimization` | Andrew workspace | ✅ |
| `interaction-self-reflection` | Andrew workspace | ✅ |
| `skill-creator` | OpenClaw built-in | ✅ |
| `feishu-write-shared` | Andrew workspace | ✅ |
| `airtable-dashboard` | Andrew workspace | ✅ |
| External: `obra/superpowers` | GitHub | 📚 |
| External: `addyosmani/agent-skills` | GitHub | 📚 |
