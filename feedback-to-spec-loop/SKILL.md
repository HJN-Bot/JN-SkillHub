---
name: feedback-to-spec-loop
description: Turn messy human feedback or a PRD into shipped changes across multiple sessions. Bridges Claude's dev-memory-and-todos (memory layer) with Matt's 7 Vibe Coding skills (execution layer). Use when the user gives a long multi-part request, says "fix all these", or when resuming work with cold context.
---

# Feedback → TODO → Spec → Delivery Loop

## 融合逻辑

```
                    dev-memory-and-todos
                    ┌─────────────────────┐
用户原始需求  ──→  │ TODO.md 逐条登记    │  ←─ Claude 写的，你喜欢的 TODO 形式
                    │ Session-WIP 续跑    │
                    │ Project-Memory 稳定 │
                    └──────┬──────────────┘
                           │ 每条 TODO item
                           ▼
                    ┌──────────────────────┐
                    │  grill-me            │  ←─ Matt：设计树追问，澄清需求边界
                    │  write-prd           │  ←─ Matt：问题陈述 + 方案 + 模块
                    │  prd-to-issues       │  ←─ Matt：垂直切片拆 Issue
                    └──────┬───────────────┘
                           │ 每个 Issue
                           ▼
                    ┌──────────────────────┐
                    │  4-section Spec      │  ←─ Claude：修改建议/思路/方案/验证
                    │  Design/specs/       │
                    │  TODO.md Spec Index  │
                    └──────┬───────────────┘
                           │
                    ┌───────┴───────┐
                    ▼               ▼
              ralph-loop    tdd-red-green-refactor
              (自动循环)     (红绿重构)
                    │               │
                    └───────┬───────┘
                            ▼
                    ┌──────────────────────┐
                    │  human-qa            │  ←─ Matt：commit → QA Plan → 回流
                    │  improve-arch        │  ←─ Matt：周期重构，深化模块
                    └──────────────────────┘
```

## 为什么这样融合

| 层 | 负责 | 谁写的 | 为什么好用 |
|----|------|--------|-----------|
| **记忆层** | 记什么、做到哪了 | Claude（dev-memory-and-todos） | verbatim 归档不丢信息，Session-WIP 跨 session 续跑 |
| **澄清层** | 需求长什么样 | Matt（grill-me） | 16-50 个问题走完整棵设计树，比直接写 PRD 省返工 |
| **规划层** | 怎么拆、谁先做 | Matt（write-prd + prd-to-issues） | 垂直切片 + 阻塞关系，Tracer Bullet 优先 |
| **规范层** | 每个变更的小契约 | Claude（feedback-to-spec-loop 原版） | 4 节 Spec，TODO ↔ Spec 双向链接，和你的 TODO 形式精确匹配 |
| **执行层** | 写代码、跑测试 | Matt（ralph-loop + tdd） | 红绿重构自动关 Issue |
| **验证层** | 人工 QA、架构健康 | Matt（human-qa + improve-architecture） | commit → QA Plan → Issue 回流 |

## 完整工作流（一次走到底）

### 第 0 步：建立项目骨架
**调用：** `dev-memory-and-todos`
```
<repo>/Design/dev-memory/
  PROJECT-MEMORY.md    ← 产品是什么、技术栈、红线
  SESSION-WIP.md       ← 本 session 状态
  TODO.md              ← 这里是一切的核心
```

**TODO.md 结构（你的格式）：**

```markdown
# 🧭 North Star
[一句话：这个项目最终要交付什么]

# 📋 Active Plan

## 🔴 P0 — 阻塞项
## 🟡 P1 — 本周
## 🟢 P2 — 后续

# 🗺️ Specs Index
| Spec | TODO Item | Issue | Status |
|------|-----------|-------|--------|

# ✅ Done
[已完成的 TODO 项目移到这]

---

# 📦 Verbatim Feedback Archive
### 2026-06-03 — [来源]
> [用户原话，包括 emoji 和 "btw" 旁白]
```

### 第 1 步：捕获（每次收需求做一次）
**调用：** `dev-memory-and-todos` 的 capture 逻辑

- 把用户原始需求原文扔进 `TODO.md` 的 📦 Verbatim Feedback Archive
- 每条需求拆成独立 TODO item，放到 Active Plan
- 不改写、不合并，保持原话

### 第 2 步：追问澄清
**调用：** `grill-me`（Matt）
- 在写任何代码或 PRD 前，走完整棵设计树
- 每个决定节点问到底（"如果选 X，那 Y 和 Z 怎么处理？"）
- 代码里有答案的，直接读代码，不问人
- 产出：`SESSION-WIP.md` 里追加设计树结论

### 第 3 步：写 PRD
**调用：** `write-prd`（Matt）
- 产出 GitHub Issue，不是飞书文档
- 内容：问题陈述 + 方案（轻量）+ 用户故事 + 关键实现决定 + 模块草图
- PRD 描述 **到达什么地方**，不描述怎么一步一步走

### 第 4 步：拆为垂直切片
**调用：** `prd-to-issues`（Matt）
- 每个 Issue 是一条贯穿所有层的垂直切片
- 标阻塞关系（谁依赖谁）
- 第一个 Issue = 最大未知风险（Tracer Bullet）
- 写入 `TODO.md` 的 `🗺️ Specs Index` 表

```
| # | Spec | TODO Item | Issue | Status |
|---|------|-----------|-------|--------|
| 1 | 2026-06-03-search-api.md | P1-1 搜索接口 | #42 | ⬜ |
| 2 | 2026-06-03-split-pane.md | P1-2 分屏编辑器 | #43 | ⬜ (blocks 1) |
```

### 第 5 步：逐条写 Spec
**调用：** `feedback-to-spec-loop` 的 spec 部分（Claude 原版）

每 Issue 一个 `Design/specs/YYYY-MM-DD-<topic>.md`，4 节：

1. **修改建议** — 什么 & 为什么（关联用户原文引用）
2. **解决思路** — 根因 + 策略
3. **技术方案** — 文件、函数、关键修改。**先确认接口变更，再实现**
4. **验证测试** — 哪个测试证明它工作了 + 手动检查项

Spec 头尾双向链接回 TODO.md 的 Specs Index 和 GitHub Issue。

### 第 6 步：用户确认优先级
先把 TODO.md 的 🗺️ Specs Index 表发给用户。
- 调整顺序、合并、删除
- 确认："最大未知风险是不是第一个？"
- 用户说"go"→ 进入第 7 步

### 第 7 步：自动化实现
**调用：** `ralph-loop` + `tdd-red-green-refactor`（Matt）
```
对每个未阻塞 Issue：
  RED   → 写一个失败的测试
  GREEN → 写最少的代码让它过
  REFACTOR → 清空上下文，重构
  → tsc/build 全绿
  → git commit + close Issue
  → 下一个
```

### 第 8 步：人工 QA
**调用：** `human-qa`（Matt）

每 3-5 个 commit 生成 QA Plan → 人工验证 → 失败的回流新增 Issue → 回到 Specs Index

### 第 9 步：架构周期检查
**调用：** `improve-architecture`（Matt）

每周跑一次：探查 shallow modules → 3 个 subagent 并行设计 → 人选最优 → GitHub Issue 记录

## 关键差异：这个融合版 vs 纯 Matt 版

| 方面 | 纯 Matt Enhanced 版 | 这个融合版 |
|------|---------------------|-----------|
| 起点 | PRD 开始 | **TODO 开始**（你的习惯） |
| 记忆 | 隐含在 Phase 里 | **显式 dev-memory 文件夹**（Claude 设计） |
| Spec | PRD 的一部分 | **独立 4 节 Spec + TODO 双向链接** |
| TODO 格式 | Issues Kanban | **North Star → Active Plan → Specs Index → Archive** |
| 可追溯 | Issue ↔ commit | **用户原话 → TODO → Spec → Issue → commit → QA** |

## 什么时候用哪个 Skill

| 场景 | 调哪个 |
|------|--------|
| 新项目搭建骨架 | `dev-memory-and-todos` |
| 收到一大段需求 | `dev-memory-and-todos` capture → 拆 TODO |
| 需求不清晰 | `grill-me` |
| TODO 太多需要规划 | `write-prd` + `prd-to-issues` |
| 某个 Issue 要开始写 | 写 4-section Spec → `ralph-loop` + `tdd` |
| 跨 session 回来续跑 | 读 `dev-memory-and-todos` 的 SESSION-WIP.md |
| 积累了几次提交 | `human-qa` |
| 每周检查代码健康 | `improve-architecture` |

## 注意事项

- **dev-memory-and-todos 要全员读写。** Matt skill 产出的结果必须写回 TODO.md 和 SESSION-WIP.md，否则跨 session 全丢。
- **grill-me 不省。** 5 分钟追问省 5 小时返工。
- **Spec 不是过场。** 每条 TODO item 没 Spec 不写码。Spec 就是你和 AI 之间的小契约。
- **TODO.md 是唯一真相源。** 不在 Issue、不在 PRD、不在 IM 聊天记录里，就在这个文件里。
