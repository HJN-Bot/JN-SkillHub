# Trigger Guide for JN-SkillHub

## Purpose

This file defines **when to think of a skill**, **whether to ask first**, and **which agent should usually take the lead**.

The goal is **not** to force every task into a skill.
The goal is to ensure that when a task strongly matches a skill, the agent can:
1. recognize the match,
2. link back to the shared skill,
3. ask Jianan for confirmation when needed,
4. then execute with the correct workflow.

---

## Trigger Modes

### 1. Ask-First
Agent should proactively recognize the match and ask Jianan whether to use the skill.

Use for:
- low-cost but workflow-shaping skills
- tasks where applying the skill changes the output format or process
- shared reusable skills that should not be forced by default

### 2. Explicit-Only
Only use when Jianan explicitly names the skill or clearly asks for that exact workflow.

Use for:
- heavier workflows
- special-purpose or experimental skills
- tasks with higher execution cost or stronger format lock-in

### 3. Shared-Default (Rare)
Can be used without asking if the task is almost exactly the skill's intended use and cost/risk is low.

Current policy: use this mode very sparingly.

---

## Skill Trigger Matrix

| Skill | Primary Agent | Trigger Clues | Cost Class | Trigger Mode |
|---|---|---|---|---|
| `jianan-presentation-system` | Rex | PPT, slides, pitch, deck, oral script, roadshow, presentation structure | Free / Low | Ask-First |
| `design-front` | Rex | landing page, visual page, frontend design, polished UI, page style, visual expression | Free / Low | Ask-First |
| `codebase-to-course` | Andrew | explain this codebase, turn repo into course, walkthrough, interactive teaching, architecture explanation | Free / Low | Ask-First |
| `claw-vibe-project` | Andrew / Rex | vibe coding, project harness, session protocol, changelog, project workflow, startup structure | Free / Low | Ask-First |
| `video-post-editor` | Lulu | subtitle editing, post-production, annotation, ffmpeg workflow, short-video polishing, video restructuring | Medium | Ask-First |
| `ai-morphing-video` | Lulu | AI morphing video, style-transfer video, visual transformation, generative video workflow | Medium / High | Explicit-Only or Ask-First |

---

## Agent-Specific Guidance

### Andrew
When the request is about:
- framework clarification
- codebase explanation
- turning system logic into teachable structure
- long-lived project/session workflows

Andrew should think of:
- `codebase-to-course`
- `claw-vibe-project`

Suggested confirmation line:
> This matches a JN-SkillHub workflow. Do you want me to use the codebase/course or vibe-project skill structure for this?

---

### Rex
When the request is about:
- PPT
- deck
- pitch
- roadshow
- structured outward communication
- visual project expression

Rex should think of:
- `jianan-presentation-system`
- `design-front`

Suggested confirmation line:
> This is a strong match for the JN-SkillHub presentation/design workflow. Do you want me to execute in that structure?

---

### Lulu
When the request is about:
- video post-editing
- subtitles
- annotation
- short video restructuring
- AI-style visual video

Lulu should think of:
- `video-post-editor`
- `ai-morphing-video`

Suggested confirmation line:
> This fits the JN-SkillHub video workflow. Do you want me to use the post-editor / morphing-video skill for this?

---

### Alex
Alex does not yet have a strongly dedicated JN-SkillHub skill, but may reuse shared skills when tasks need:
- visual expression
- structured writing / communication
- workflow framing

---

## Important Rule

Agents should **not** assume that every matching task must use a skill.

Instead:
1. detect likely match,
2. mention the relevant skill,
3. ask Jianan if he wants that workflow,
4. then proceed.

Only use heavy or specialized skills automatically when Jianan explicitly requests them.

---

## One-line Policy

> Think of skills early, but ask before committing unless Jianan explicitly names the workflow.
