# Session Protocol 详细规范

## 开场 Prompt 模板（复制到 VS Code snippet）

```
你是这个项目的 AI pair programmer，遵循 claw-vibe-project skill 协议。

请先完成以下开场步骤：
1. 读取 PROJECT.md，理解当前架构和状态
2. 读取 CHANGELOG.md 最后 5 条，了解近期变动
3. 读取 skills.yaml，确认本 session 启用的 skill 列表
4. 确认你理解了项目状态，输出一句「当前状态摘要」

本次任务：[在此填写]

约束：
- 不修改 harness/ 目录（除非我明确说「更新 harness」）
- 只调用 skills.yaml 白名单内的 skill
- 每个重要决策都要说出来，不要静默执行
```

---

## 收尾 Prompt 模板

```
本次 session 结束，请执行收尾协议：

1. 生成 CHANGELOG 条目（格式严格按照 changelog-format.md）
2. 更新 PROJECT.md：
   - 「当前状态」改为今天做完的状态
   - 「下一步」改为你建议的下一个任务
   - 如果有新的架构决策，追加到 ADR 区块
3. 列出本次 session 的遗留问题（如果有）
4. 说出「收尾完成，项目状态已更新」
```

---

## Session 类型与对应行为

### 类型 A：Feature Session（新功能开发）
- 开场：读 PROJECT.md + 最后 3 条 changelog
- 结束：必须跑 smoke eval，更新 PROJECT.md 功能列表

### 类型 B：Bugfix Session（修 bug）
- 开场：读相关 CHANGELOG 条目，理解 bug 上下文
- 结束：写明 root cause 和 fix 方案，标注 `[BUGFIX]`

### 类型 C：Refactor Session（重构）
- 开场：读 harness/HARNESS.md，明确红线
- 结束：必须说明 harness 是否需要同步更新，标注 `[REFACTOR]`

### 类型 D：Exploration Session（探索/实验）
- 开场：明确说明这是实验，结果不一定进主线
- 结束：输出「是否采纳」的建议，采纳则写正式 changelog，不采纳则写 `[DISCARDED]`

---

## 中断恢复协议

当 session 意外中断或隔了很久再继续：

```
恢复 prompt:
"我们继续上次的项目。请读取 PROJECT.md 和最近的 CHANGELOG，
告诉我上次停在哪里，然后我们继续。"
```

Claude 应该输出：
1. 上次做了什么
2. 遗留了什么问题
3. 建议从哪里继续
4. 询问用户是否有新的优先级变化

---

## Sprint Contract（冲刺契约）

来源：Anthropic Engineering Blog — Harness design for long-running apps

**在每次 session 开始写代码之前，先完成契约对齐：**

```
Generator（Claude/Copilot）提案：
- 本次我计划实现：[具体功能列表]
- 完成的可验证标准：[具体可测试的行为]
- 不包含在本次范围内：[明确排除项]

Evaluator（Claude）确认：
- ✅ 同意 / ⚠️ 建议调整：[修改意见]
- 评估标准：[本次用哪几个维度评估输出质量]
```

**契约格式（写入 SESSION_HANDOFF.md）：**

```markdown
## Sprint Contract — Session #N

### 本次交付范围
- [ ] [功能1，含可测试的成功标准]
- [ ] [功能2，含可测试的成功标准]

### 明确排除
- [不做的事，防止 scope creep]

### 评估维度
- 功能完整性：[具体检查点]
- 接口稳定性：[是否动了 harness]
- 代码质量：[函数级健康指标]
```

---

## Generator-Evaluator 分离协议

在 copilot 模式下，这两个角色天然分离：

```
Copilot = Generator（生成代码）
Claude  = Evaluator（评估输出）
```

**Evaluator（Claude）的评估标准——不能只说「不错」：**

每次 session 结束，Claude 必须按以下维度评分，不允许笼统夸奖：

| 维度 | 检查内容 | 评级 |
|------|---------|------|
| **功能完整性** | Sprint Contract 里的每一条是否真正完成，不是 stub | ✅/⚠️/❌ |
| **接口稳定性** | 是否动了 harness/，有没有隐式改变模块间契约 | ✅/⚠️/❌ |
| **无后处理堆叠** | 有没有新增补丁函数修别的模块输出（AP-001）| ✅/⚠️/❌ |
| **中间态可观测** | 关键节点有没有中间态输出，能独立复现 | ✅/⚠️/❌ |

**任意一项 ❌，session 不算完成，需要修复后重新评估。**

---

## SESSION_HANDOFF.md 规范

每次 session 结束时生成，专门为下一次 session 的上下文重置设计。
比 PROJECT.md 更聚焦，只包含「下一个 session 必须知道的」。

```markdown
# SESSION_HANDOFF.md
> 本文件由每次 session 结束时自动更新，供下次 session 开场读取。
> 读完即可丢弃本文件对话，PROJECT.md 是长期记忆。

## 上次停在哪
[一句话描述]

## 已完成 ✅
- [Sprint Contract 里完成的条目]

## 未完成 / 遗留 ⚠️
- [具体的未完成项，含失败原因]

## 下次 session 的 Sprint Contract 草案
- 建议实现：[...]
- 成功标准：[...]
- 建议排除：[...]

## 需要注意的上下文
- [任何下次 session 容易踩的坑]
- [当前架构中不稳定的地方]
```
