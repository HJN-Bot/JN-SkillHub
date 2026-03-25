# Changelog 格式规范

## 设计原则

Changelog 是 AI vibe coding 的**审计轨迹**，不是 git commit log。
它记录的是：为什么这么做、做了什么决定、留下了什么问题。

---

## 完整条目格式

```markdown
## [YYYY-MM-DD] Session #N — <任务简称（≤20字）>

**触发者**: Jianan / OpenClaw-FORGE / OpenClaw-SAM  
**AI 模型**: claude-sonnet-4-20250514  
**任务类型**: Feature | Bugfix | Refactor | Config | Docs | Exploration | Drift-Fix  
**关联任务**: #issue-id 或 N/A  
**耗时估计**: ~30min  

### 变动摘要
<!-- 每一行是一个具体变动，带文件路径 -->
- 新增：`src/agents/forge.py` — 实现 FORGE agent 基础框架
- 修改：`harness/interfaces/agent.ts` — 添加 `reasoning_trace` 字段 [HARNESS CHANGE]
- 删除：`src/deprecated/old-orchestrator.py` — 已被新架构替代
- 配置：`.env.example` — 添加 SQS_FIFO_URL 变量

### 关键决策
<!-- 记录"为什么"，这是最有价值的部分 -->
- ✅ 选择 SQS FIFO 而非 EventBridge，原因：任务顺序必须严格保证
- ⏸️ 暂时跳过 reward signal 集成，因为 eval 数据集还没准备好
- ❌ 放弃用 Redis 做状态缓存，公司网络限制无法使用外部 Redis

### 架构变化
<!-- 如果本次 session 改变了架构，在这里说明 -->
- 新增了 L3 Context Layer 的 `project_memory` 字段
- FORGE 现在依赖 SCOUT 的摘要输出，形成单向依赖

### 遗留问题
<!-- 未解决的，下次需要处理的 -->
- [ ] FORGE 的错误重试逻辑还未实现
- [ ] `agent.ts` 的 `max_retries` 字段类型需要讨论（number vs enum）

### 漂移记录
<!-- 实际实现与 PROJECT.md 设计不一致的地方 -->
- ⚠️ PROJECT.md 说 FORGE 是无状态的，但实现中加了 session_cache，需要更新文档
```

---

## 简化条目格式（快速修改用）

```markdown
## [YYYY-MM-DD] Quickfix — <描述>

- 修改：`文件路径` — 原因
- 决策：选择 X 因为 Y
- 遗留：[ ] 待处理事项
```

---

## Changelog 文件结构

```markdown
# CHANGELOG — <项目名>

<!-- 最新的在最上面 -->

## [2026-03-25] Session #12 — ...
...

## [2026-03-20] Session #11 — ...
...

---
<!-- 归档分割线（每季度归档一次） -->
## Archive: Q1 2026
[旧条目链接或折叠]
```

---

## 条目类型标签说明

| 标签 | 含义 |
|------|------|
| `[FEATURE]` | 新功能 |
| `[BUGFIX]` | Bug 修复 |
| `[REFACTOR]` | 重构，不改功能 |
| `[HARNESS CHANGE]` | 修改了 harness/ 红线文件 |
| `[DRIFT FIX]` | 修复了代码与文档的漂移 |
| `[DISCARDED]` | 本次探索被放弃，不进主线 |
| `[INIT]` | 项目初始化 |
| `[CONFIG]` | 配置变更 |
| `[DOCS]` | 只改了文档 |

---

## 与 git 的关系

- CHANGELOG 记录「AI 决策过程」，git log 记录「代码快照」
- 建议：每次 session 结束时 commit，commit message 引用 session 编号
- 示例：`git commit -m "feat: FORGE base framework [Session #12]"`
