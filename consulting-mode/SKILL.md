---
name: consulting-mode
description: "进入咨询模式：用SCQA→MECE/Issue Tree→分析与证据→金字塔输出的结构化流程，进行创造性探讨、趋势研究、抽象问题拆解；并在需要时调用多视角辩论/一性原理/决策树/Agent架构类skills辅助。触发：用户说‘进入咨询模式’或要求SCQA/MECE/金字塔/issue tree/高阶思维。"
---

# 咨询模式（SCQA × MECE × 金字塔）

## 使用方式（触发词）
用户说：**“进入咨询模式：<你的问题>”**

规则：
- **强制分步**（每一步结束等用户确认/补信息）
- **结论先行**，但每条结论都要配“证据/假设/下一步验证”
- 输出同时给：**30秒版**（给同事/老板）+ **深入版**（给自己写方案）

---

## Step 0：先选一种问题类型（决定提问方式）
- 创造/趋势：要“发散→收敛→行动”
- 方案/产品：要“目标→约束→路径→里程碑”
- 决策：要“选项→概率→价值→风险→止损”

只问 1~2 个关键澄清：目标、约束、时间。

---

## Step 1：SCQA（界定问题）
输出并请用户确认：
- S：情景（大家都认同的背景）
- C：冲突（痛点/变化/反常）
- Q：疑问（要回答的核心问题）
- A：核心观点（Answer，先给一个可被证伪的判断）

---

## Step 2：Issue Tree + MECE（结构化拆解）
- 建 3~5 个一级驱动（Key Drivers），要求 MECE
- 对每个驱动列：
  - 需要的证据类型（数据/案例/对比/用户访谈/实验）
  - 可执行的下一步动作（最小验证）

> 如果用户在做“选项决策”，可调用 decision-trees。

---

## Step 3：分析与验证（Why / Evidence / How-to）
对每个一级驱动：
- Why：为什么会这样（机制/因果）
- Evidence：证据与反例（缺证据就标注为假设）
- How-to：对策、里程碑、风险与止损

> 如需打破固有假设，可调用 first-principles-decomposer。
> 如需多视角冲突暴露盲点，可调用 multi-viewpoint-debates。

---

## Step 4：金字塔输出（两种版本）
1) **30秒版**：结论（1-2句）→ 3条论据 → 下一步
2) **深入版**：按一级驱动展开（小标题+核心句+细节），最后给行动清单

---

## 可选：Agent/AI 架构评审子流程（默认开启，C = 你的六层框架 + 通用工程 checklist）

触发条件：问题包含 Agent / RAG / 工作流 / 平台 / 架构 / 部署 / 评测 等关键词。

### 子流程 A：按你的“六层框架”快速过一遍
1) 交互层：入口/权限/人审体验/失败反馈
2) 工作流层：LangGraph(or Temporal)/暂停点/checkpoint/rerun/trace
3) 工具层：tools/skills 原子化、可组合、可审计
4) 记忆层：Job/Project/Org；Memory-as-FS；写入治理
5) 元数据层：证据链、索引、成本、可观测
6) 治理层：RBAC、审计、网络边界、备份、质量回归

### 子流程 B：通用工程 checklist（大厂实践对齐）
- 数据流：输入→中间表示→产物；版本化；可回滚
- 安全：最小权限、网络白名单、密钥管理、审计日志
- 可靠性：幂等、重试、降级、限流、失败隔离
- 观测：结构化日志、trace id、指标、告警
- 评测：fixtures/evals、回归、错误分类（taxonomy）
- 成本：tokens/cost、缓存策略、召回与压缩
- 部署：环境隔离、CI/CD、配置管理、灰度

输出要求：
- 给出“最大风险 Top3 + 证据/假设”
- 给出“2周最小落地计划”（MVP里程碑）

---

## 可选：何时调用其它 skills（路由）
- 多视角辩论：multi-viewpoint-debates（盲点/争议大）
- 一性原理：first-principles-decomposer（需要从底层重建）
- 决策树：decision-trees（多选项+不确定性）
- 认知偏差审计：munger-observer（复盘/纠偏）
- 创业心态教练：founder-coach（创业/心态/周挑战）
- Agent架构类：architecture-designer / agent-builder / agent-development / agent-orchestrator / agent-council（当问题是AI/Agent/系统设计/架构评审）
