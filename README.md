# JN-SkillHub

Jianan 的私有 SkillHub。这里放长期维护、可跨 Agent 复用的自定义 skills，作为多 Agent 系统的共享能力层（source of truth）。

## Current Skills

| Skill | Purpose | Primary Agent | Typical Use |
|---|---|---|---|
| `jianan-presentation-system` | PPT / 路演 / 口播稿 / 页面结构与美化 | Rex | 路演、汇报、方案表达、双语演讲稿 |
| `video-post-editor` | 视频后期、字幕、注释、重组、ffmpeg/manim 工作流 | Lulu | 视频成稿、字幕润色、后期编辑 |
| `ai-morphing-video` | AI 变形视频、视觉变换、风格迁移型视频工作流 | Lulu | AI 视觉短片、风格化视频制作 |
| `design-front` | 高质量前端设计与视觉实现 | Rex | 着陆页、产品页、视觉设计、前端展示 |
| `codebase-to-course` | 将代码库讲解为课程/教程/交互页面 | Andrew | 框架梳理、代码教学、系统理解 |
| `claw-vibe-project` | 项目制 vibe coding、session/harness/changelog/skills 管理 | Andrew / Rex | 项目初始化、长期开发、会话协作 |

## Principles

1. **Shared, not private**: skills 默认给所有子 Agent 可见，不绑定单一 Agent。
2. **Primary-agent mapping**: 每个 skill 有主用 Agent，但其他 Agent 也可以调用。
3. **Role-first reuse**: 用户在子频道提出任务时，优先由最匹配的 Agent 调用对应 skill。
4. **Hub first**: 如果 skill 已在这里，优先复用这里的版本，而不是重新定义一套。

## Activation Rule

所有 Agent 应将本仓库视为：
> 私有共享 skill 源（shared source of truth）

当用户提出与以下场景相关的任务时，应优先联想到本仓库：
- presentation / pitch / PPT / 口播稿
- 视频成稿 / 字幕 / 后期编辑
- 前端设计 / 页面美化 / landing page
- 框架梳理 / codebase 讲解 / interactive course
- vibe coding / 项目制 session 管理

See: `AGENT_MAPPING.md`
