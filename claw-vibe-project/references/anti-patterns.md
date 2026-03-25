# Anti-Patterns — Vibe Coding 踩坑记录

> 每次项目出现架构问题时，在这里记录「反模式 → 症状 → 正确做法」。
> Session 开场时 Claude 会读取此文件，主动提醒风险。

---

## AP-001：后处理层污染信号链

**来源**：2026-03 LLM AB 测试失败复盘

**反模式**
```
LLM输出 → [补丁A] → [补丁B] → [补丁C] → 最终结果
```
每次 LLM 输出有点奇怪，就在主脚本里加一层后处理修掉。
久而久之，最终结果里既有 LLM 的贡献，也有后处理的贡献，无法区分。

**症状**
- 想做 AB 测试时，发现无法还原「纯 LLM 输出」
- 改了 LLM，不知道效果变化是来自 LLM 还是后处理
- 主脚本越来越长，没人敢动

**正确做法**

```
架构层：物理隔离
LLM调用层  →  [中间态存储: CSV/JSON]  →  后处理层  →  结果层
    ↑                  ↑                      ↑
 独立模块           可观测锚点              独立模块

模块层：职责单一
- llm_caller.py      # 只负责调 LLM，存原始输出
- postprocess.py     # 只做后处理，读中间态输入
- evaluator.py       # 只做结果评估

功能层：每个后处理函数独立可测
def clean_output(raw: str) -> str: ...   # 单独 UT
def format_result(cleaned: str) -> dict: ...  # 单独 UT
```

**Session 扫描触发词**：主脚本、后处理、补丁、format、clean、strip、replace（出现在非专用模块里）

---

## AP-002：接口约定缺失导致全链路耦合

**反模式**
模块之间没有明确的数据格式约定，A 模块的输出格式随时可能变，B 模块随时跟着改。

**症状**
- 改一个模块，另一个模块莫名其妙报错
- 不知道某个字段是「必须有」还是「可能有」

**正确做法**
- 在 `harness/interfaces/` 里定义模块间的数据契约（TypedDict / Pydantic / TypeScript interface）
- 契约变更走 Harness Change 流程，不能静默修改

---

## AP-003：无中间态导致无法回溯

**反模式**
流水线全程在内存里跑，没有任何节点把中间结果持久化。

**症状**
- 出了问题不知道是哪一层出的
- 想重跑某一层，必须从头跑整个流水线
- 无法做 AB 测试（没有可对比的基准输出）

**正确做法**
- 每个关键节点输出中间态文件（CSV / JSON / Parquet）
- 命名规范：`{run_id}_{stage}_{timestamp}.csv`
- 中间态文件路径在 PROJECT.md 的架构部分声明

---

<!-- 在此追加新的反模式 -->

## AP-004：自评偏差（Self-Evaluation Bias）

**来源**：Anthropic Engineering Blog — Harness design for long-running apps，2026-03-24

**反模式**
让同一个 AI 生成代码然后评估自己的输出。

**症状**
- AI 生成了有问题的代码，但在自我检查时说「看起来不错」
- 补丁和 workaround 被评估为「合理的实现选择」
- Session 结束时 Changelog 里全是正面总结，没有真实问题记录

**正确做法**
- Copilot 模式：Copilot 生成，Claude 评估（天然分离）
- OpenClaw 模式：FORGE 生成，LENS 评估（agent 分工）
- 评估时必须按维度打分，不允许笼统夸奖
- 任意维度 ❌ 则 session 不算完成

---

## AP-005：Harness 过度工程化（Over-engineered Harness）

**来源**：同上

**反模式**
堆积了很多 harness 组件，但没有定期检查哪些还是必要的。

**症状**
- 每次新 session 都要走很多「仪式」但感觉没什么用
- Harness 里的约束已经和当前代码现实脱节
- 模型能力提升了，但旧的脚手架还在

**正确做法**
每 10 次 session 或每月做一次「Harness 减负检查」：
- 哪些约束是模型现在已经能自己做到的？→ 删掉
- 哪些文档已经和代码脱节？→ 更新或删掉
- Skill 白名单里有没有从未用过的？→ 移出

> 原则：Harness 里的每个组件都是「模型做不到某件事」的假设。
> 定期验证这些假设，过期的就清理掉。
