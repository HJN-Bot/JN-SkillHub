# Agent Mapping for JN-SkillHub

## Goal

让 JN-SkillHub 中的 skills 不只是“存在”，而是能被各子 Agent 真正调用、复用、活起来。

---

## Agent → Skill Priority Mapping

### Andrew 🌸
**定位**：学习 / 框架整理 / 方法论 / 协议沉淀

**Primary skills**
- `codebase-to-course`
- `claw-vibe-project`

**Secondary skills**
- `jianan-presentation-system`（当任务偏框架表达 / 内容整理时）
- `design-front`（当任务需要把结构转成 UI/页面表达时）

**Typical triggers**
- 帮我把这个框架理清楚
- 帮我解释这个代码库
- 做一版课程化讲解
- 整理项目结构 / 协议 / session 规则

---

### Rex 💼
**定位**：项目推进 / CER / 表达 / 对外沟通 / 方案可视化

**Primary skills**
- `jianan-presentation-system`
- `design-front`

**Secondary skills**
- `claw-vibe-project`
- `codebase-to-course`

**Typical triggers**
- 帮我做 PPT / deck / 路演稿
- 帮我做一版对外表达
- 帮我做一页产品方案图
- 帮我把项目进展讲清楚

---

### Lulu ✍️
**定位**：内容输出 / 视频成稿 / 后期组织 / 传播表达

**Primary skills**
- `video-post-editor`
- `ai-morphing-video`

**Secondary skills**
- `jianan-presentation-system`（内容表达型页面/脚本）
- `design-front`

**Typical triggers**
- 帮我把这段做成视频稿
- 帮我整理字幕 / 注释 / 视频结构
- 帮我做一个 AI 风格视频
- 帮我润色视频表达

---

### Alex 💗
**定位**：个人支持 / 关系 / 生活整理 / personal workflow

**Primary skills**
- 暂无完全专用 skill，优先共享使用

**Shared skills**
- `jianan-presentation-system`（做个人表达/梳理时）
- `design-front`（需要视觉表达时）
- `claw-vibe-project`（需要结构化工作流时）

---

## Shared Skills (All Agents Can Use)

- `design-front`
- `claw-vibe-project`
- `jianan-presentation-system`（按任务侧重点差异调用）

---

## Operating Rule

1. 每个 Agent 都应知道 JN-SkillHub 的存在与位置。
2. 每个 Agent 都应优先回链到这里，而不是临时重新发明工作流。
3. 用户在不同子频道提出类似需求时，应复用同一套 skill，而不是每个 Agent 各写一套。
4. 如需新增 skill，优先放入 JN-SkillHub，再同步到各 Agent 的本地说明。

---

## Local Path

```bash
/home/ubuntu/.agents/skills/JN-SkillHub
```

This repo is the shared private skill source for Jianan's multi-agent system.


---

## Cost / Trigger Policy

| Skill | Cost Class | Trigger Mode | Confirmation Rule |
|---|---|---|---|
| `jianan-presentation-system` | Free / Low | Ask-First | Mention the skill when task strongly matches PPT/deck/roadshow structure |
| `design-front` | Free / Low | Ask-First | Mention when task is clearly design/front-end expression oriented |
| `codebase-to-course` | Free / Low | Ask-First | Mention when task is educational/codebase explanation oriented |
| `claw-vibe-project` | Free / Low | Ask-First | Mention when task is clearly long-lived project/session workflow work |
| `video-post-editor` | Medium | Ask-First | Mention before using for post-production / subtitles / edit workflow |
| `ai-morphing-video` | Medium / High | Explicit-Only or Ask-First | Prefer explicit confirmation before using |

### Policy Note
These skills should not be forcibly applied to every relevant task. Instead, agents should detect likely fit and ask Jianan whether to use the linked skill workflow.
