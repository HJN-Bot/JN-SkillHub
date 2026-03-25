---
name: claw-vibe-project
description: >
  Jianan 的项目制 Vibe Coding 管理系统，结合 OpenClaw 框架与 Harness Engineering，
  用于长期开发项目的 AI 辅助编码会话管理。当 Jianan 提到「vibe coding」「开始新项目」
  「继续上次的开发」「帮我做 session 开场」「更新 changelog」「项目 harness」
  「skill 白名单」「evals 复用」或「项目记忆」时，必须触发此 skill。
  适用于 VS Code 环境的单人或 OpenClaw 多 agent 协作项目。
---

# Claw Vibe Project — 项目制 Vibe Coding 管理系统

## 核心设计原则

| 层级 | 职责 | 核心文件 |
|------|------|---------|
| **记忆层** | 跨会话项目状态 | `PROJECT.md` |
| **变动层** | 每次 AI 操作的审计轨迹 | `CHANGELOG.md` |
| **约束层** | 架构红线，AI 不可随意修改 | `harness/` |
| **能力层** | 本项目启用的 skill 白名单 | `skills.yaml` |
| **验证层** | 可复用的 eval 测试集 | `evals/` |

---

## 两种使用模式

| 模式 | 触发词 | 适用场景 | 注入文件 |
|------|-------|---------|---------|
| **轻量模式** | `vibe-light` | 日常小改动、修 bug、加字段 | 只读 `CURRENT_STATE.md` |
| **完整模式** | `vibe-start` | 新功能、重构、漂移检测、周期性健康检查 | 读全套文档 + 三层扫描 |

> **原则**：小改动用轻量，5 分钟内能说清楚的任务不需要走完整流程。
> 每天结束时用 `vibe-day` 收尾，更新 `CURRENT_STATE.md`——这是明天轻量模式的燃料。

---

## 四个核心文档的分工

| 文档 | 性质 | 更新方式 | 用途 |
|------|------|---------|------|
| `CURRENT_STATE.md` | 活文档，反映「现在」 | 每日覆盖 | 轻量注入的唯一来源 |
| `SESSION_HANDOFF.md` | 交接文档，反映「下次」 | 每次 session 覆盖 | 完整模式开场读 |
| `CHANGELOG.md` | 历史流水账，反映「过去」 | 每次 session 追加 | 审计、回溯 |
| `PROJECT.md` | 设计意图，反映「应该是」 | 有架构变更时更新 | 漂移检测的基准 |

---

## 快速启动：项目初始化

### 当用户说「初始化项目」或「新建 vibe 项目」

执行以下步骤：

1. **读取模板**：从 `assets/templates/` 复制所有模板文件到目标项目目录
2. **填充 PROJECT.md**：向用户询问项目一句话、技术栈、目录约定
3. **建立 CHANGELOG.md**：写入第一条 `[INIT]` 记录
4. **配置 skills.yaml**：根据项目类型推荐初始白名单
5. **创建 harness/ 骨架**：建立接口契约目录

详细模板见 → `assets/templates/`

---

## Session 生命周期协议

### Session 开始（必须执行）

```
步骤 1: 读取 SESSION_HANDOFF.md（如存在）— 获取上次 session 的交接状态
步骤 2: 读取 PROJECT.md — 理解长期架构和约定
步骤 3: 读取 skills.yaml — 确认 runtime.mode 和启用的 skill
步骤 4: 读取 references/anti-patterns.md — 加载历史踩坑记录
步骤 5: 执行三层架构风险扫描（见下方）
步骤 6: 与用户协商 Sprint Contract（本次做什么、完成标准是什么）
步骤 7: 确认后输出开场摘要，开始执行
```

> **重要**：如果 PROJECT.md 不存在，先走初始化流程，不要直接开始编码。

### 三层架构风险扫描（每次 Session 开场必做）

扫描目的：在动手前发现已有的架构健康问题，防止在腐化的地基上继续叠加。

#### 架构层（Architecture Layer）
检查整体数据流和模块边界：
- 是否有清晰的模块边界图（PROJECT.md 架构部分有记录）？
- 各模块之间的接口是否在 `harness/interfaces/` 有契约定义？
- 关键节点是否有中间态输出（CSV/JSON）？没有则标记为风险
- 是否存在「万能主脚本」承担了多个层的职责？

**腐化信号**：主脚本 > 200 行 / 单文件承担调用+处理+输出 / 没有中间态文件

#### 模块层（Module Layer）
检查每个模块是否职责单一：
- 每个模块是否只做一件事（单一职责）？
- 模块之间是否有未声明的隐式依赖？
- 是否有「补丁模块」——专门用来修另一个模块输出的临时代码？
- 新功能是否被正确放进对应模块，而不是追加到最近修改的文件里？

**腐化信号**：文件名含 `utils` / `misc` / `helper` 且功能复杂 / 模块间有循环依赖

#### 功能层（Function Layer）
检查函数级别的可测试性：
- 核心函数是否有对应的 UT（`evals/` 或 `harness/contracts/`）？
- 函数是否有隐藏副作用（修改外部状态、写文件、调接口但没有声明）？
- 是否有「补丁函数」——专门在某个函数输出后再修一遍？
- 函数签名是否稳定（入参/出参类型有没有随意变过）？

**腐化信号**：函数超过 50 行 / 函数名含 `fix_` / `patch_` / `workaround_` / 没有类型注解

#### 扫描结果输出格式

```
=== 三层架构风险扫描 ===

架构层：✅ 健康 / ⚠️ 有风险 / ❌ 需要处理
- [发现的问题或确认健康的理由]

模块层：✅ 健康 / ⚠️ 有风险 / ❌ 需要处理
- [发现的问题或确认健康的理由]

功能层：✅ 健康 / ⚠️ 有风险 / ❌ 需要处理
- [发现的问题或确认健康的理由]

建议：本次 session [可以直接开始 / 建议先处理 X 再开始 / 强烈建议先重构 X]
```

### Session 结束（必须执行）

```
步骤 1: 执行 Evaluator 四维评估（功能完整性/接口稳定性/无后处理堆叠/中间态可观测）
步骤 2: 如有任意 ❌，提出修复方案，等用户确认后修复
步骤 3: 生成本次 CHANGELOG 条目（格式见 references/changelog-format.md）
步骤 4: 更新 SESSION_HANDOFF.md（含评分结果 + 下次 Sprint Contract 草案）
步骤 5: 更新 PROJECT.md 的「当前状态」和「下一步」（如架构有变则追加 ADR）
步骤 6: 说出「收尾完成，SESSION_HANDOFF.md 已更新」
```

完整 Session Protocol 见 → `references/session-protocol.md`

---

## Changelog 格式规范

每次 AI 编码操作结束后，生成标准条目：

```markdown
## [YYYY-MM-DD] Session #N — <任务简称>

**触发者**: Jianan / OpenClaw-FORGE  
**AI 模型**: claude-sonnet-4-20250514  
**任务类型**: Feature / Bugfix / Refactor / Config / Docs  

### 变动摘要
- 新增：`src/xxx.ts` — [功能描述]
- 修改：`harness/interfaces/xxx.ts` — [修改原因]  
- 删除：[如有]

### 关键决策
- 决定用 X 而不是 Y，原因：[...]
- 暂时跳过 Z，因为：[...]

### 遗留问题
- [ ] [未解决问题]

### 漂移警告
- [如有：实际实现与 PROJECT.md 设计的偏差]
```

完整 Changelog 规范见 → `references/changelog-format.md`

---

## Skill 白名单系统

每个项目维护一个 `skills.yaml`，声明本项目启用的 skill：

```yaml
# skills.yaml — 项目级 skill 白名单
project: my-project
version: "1.0"

skills:
  core:                          # 所有项目默认启用
    - claw-vibe-project          # 本 skill（必选）
    - file-reading
    - frontend-design

  project_specific:              # 按需启用
    - jianan-presentation-system  # 如需出 PPT
    - docx                        # 如需出 Word
    - pdf                         # 如需处理 PDF

  disabled:                      # 明确禁用
    - ai-morphing-video           # 与本项目无关

# Skill 调用约束
constraints:
  require_confirmation_before:   # 这些 skill 调用前需用户确认
    - docx
    - pdf
  max_skill_chain_depth: 3       # 防止 skill 套 skill 过深
```

> **使用规则**：Session 开始时读取 `skills.yaml`，只调用白名单内的 skill。
> 如果任务需要白名单外的 skill，先向用户确认是否加入白名单。

---

## Evals 复用系统

项目级 `evals/` 目录结构：

```
evals/
├── README.md              # eval 集说明
├── core/
│   ├── smoke.json         # 核心功能冒烟测试
│   └── regression.json    # 回归测试集
└── features/
    ├── auth.json          # 功能模块 eval
    └── api.json
```

### Eval 条目格式

```json
{
  "id": "eval-001",
  "description": "用户登录成功流程",
  "input": { "scenario": "...", "context": "..." },
  "assertions": [
    { "type": "contains", "value": "token" },
    { "type": "not_contains", "value": "error" }
  ],
  "tags": ["auth", "happy-path"],
  "last_run": "2026-03-20",
  "status": "passing"
}
```

### Eval 触发时机

| 时机 | 操作 |
|------|------|
| Session 结束前 | 跑 `evals/core/smoke.json` |
| 修改 harness/ 后 | 跑所有 regression eval |
| 漂移检测时 | 全量跑并对比上次结果 |

详细规范见 → `references/evals-guide.md`

---

## Harness 结构规范

```
harness/
├── interfaces/         # TypeScript / Python 接口定义（AI 不可随意改）
│   └── *.ts / *.py
├── contracts/          # 行为契约测试
│   └── *.test.ts
├── fixtures/           # 稳定测试数据
│   └── *.json
└── HARNESS.md          # 说明哪些是红线，原因是什么
```

**红线规则**：
- `harness/` 内的文件修改需要**用户显式确认**
- AI 应先建议修改方案，等用户批准后再动
- 每次 harness 修改必须在 CHANGELOG 中标注 `[HARNESS CHANGE]`

---

## 运行模式开关

**Session 开场时，先读取 `skills.yaml` 中的 `mode` 字段，所有后续行为以此为准。**

```yaml
# skills.yaml 中的开关
runtime:
  mode: copilot   # "openclaw" | "copilot"
```

### 两种模式的行为差异

| 行为 | `mode: openclaw` | `mode: copilot` |
|------|-----------------|----------------|
| **编码执行** | OpenClaw FORGE agent 通过 Discord/Lambda 执行 | GitHub Copilot 在 VS Code 内直接执行，Claude 只做规划和审查 |
| **Session 开场** | SAM 协调，SCOUT 生成摘要 | Claude 自己读 PROJECT.md + CHANGELOG，无 agent 分工 |
| **Changelog 触发者** | `OpenClaw-FORGE` / `OpenClaw-SAM` | `Jianan + Copilot` |
| **AI 模型字段** | `claude-sonnet-4-20250514` | `GitHub Copilot (GPT-4o)` |
| **Eval 执行** | AUX agent 跑批 | Claude 逐条检查，Copilot 执行代码验证 |
| **漂移检测** | LENS agent 扫描 | Claude 做文档对比，Copilot 做代码扫描 |
| **Skill 白名单** | 完整 skill 体系 | 仅 `claw-vibe-project` 核心框架有效，其余 skill 降级为 prompt 建议 |

### Copilot 模式下的 Claude 定位

在公司环境（`mode: copilot`）：
- **Claude 是架构师 + 审查员**，不直接写代码
- **Copilot 是代码执行手**，在 VS Code 内完成实际编码
- Claude 的职责：读状态 → 规划任务 → 审查 Copilot 输出 → 更新文档
- 开场时 Claude 输出「任务分解」给 Jianan，Jianan 把子任务喂给 Copilot

### Copilot 模式开场输出格式

```
=== Session #N 开场（Copilot 模式）===
当前状态：[PROJECT.md 摘要]
上次停在：[CHANGELOG 最后条目]

本次任务分解（给 Copilot 的子任务）：
1. [具体到文件级的任务描述]
2. ...

建议 Copilot Prompt：
> [可以直接复制给 Copilot 的 inline chat prompt]

架构约束提醒：
- harness/ 红线：[本次涉及的接口]
- 不要改：[列出]
```

---

## OpenClaw 角色映射（仅 `mode: openclaw` 生效）

| Agent | 在项目 vibe session 中的职责 |
|-------|----------------------------|
| **SAM** | 管理 session 生命周期，协调开场/收尾 |
| **SCOUT** | 读取 PROJECT.md + CHANGELOG，生成现状摘要 |
| **FORGE** | 执行实际编码任务，遵守 skills.yaml 白名单 |
| **LENS** | session 结束后做 diff review，检测架构漂移 |
| **INK** | 更新 CHANGELOG.md 和 PROJECT.md |
| **AUX** | 执行 eval 跑批，输出 pass/fail 报告 |

---

## VS Code 集成

项目目录包含 `.vscode/` 配置：
- `session-start.code-snippets` — 快速触发 session 开场 prompt
- `tasks.json` — 一键跑 eval 和漂移检测

详见 → `assets/templates/.vscode/`

---

## 漂移检测（每周或每 10 次 session）

```
触发词: "帮我做漂移检测" / "drift check"

执行:
1. 读取 PROJECT.md 中的架构描述
2. 扫描 src/ 实际代码结构
3. 对比并输出漂移报告：
   - 设计有但代码没有的
   - 代码有但设计没说的
   - 命名/结构不一致的
4. 询问用户：改代码 or 改文档？
5. 更新对应内容，写 CHANGELOG [DRIFT FIX] 条目
```
