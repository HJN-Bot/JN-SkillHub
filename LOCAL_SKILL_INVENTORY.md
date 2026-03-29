# Local Skill Inventory

This file is the consolidated skill ledger for Jianan's current OpenClaw system.

It combines three layers:
1. **JN-SkillHub** — Jianan's private, shared, long-term skill source of truth
2. **Legacy local skills** — previously accumulated local workspace skills
3. **Selected ok-skills** — shared community skills worth incorporating into the operating system

The purpose is not to make every agent use every skill by default.
The purpose is to make the full capability map visible, so that matching skills can be recognized, suggested, and reused with confirmation.

---

## Layer A — JN-SkillHub (Private Shared Skills)

These are Jianan-owned, shared private skills and should be treated as the preferred reusable layer when strongly matched.

| Skill | Recommended Primary Agent | Role |
|---|---|---|
| `jianan-presentation-system` | Rex | PPT / deck / oral script / structured presentation workflow |
| `video-post-editor` | Lulu | post-editing / subtitle / annotation / edit workflow |
| `ai-morphing-video` | Lulu | AI visual transformation / morphing video workflow |
| `design-front` | Rex | visual frontend / page expression / polished UI |
| `codebase-to-course` | Andrew | explain codebase / interactive teaching / structural breakdown |
| `claw-vibe-project` | Andrew / Rex | project workflow / session protocol / harness / changelog |

---

## Layer B — Legacy Local Skills (Workspace Skills)

These are previously accumulated local skills already present in the OpenClaw workspace.
They are important because many of them encode Jianan's working style and historical workflows.

| Skill | Suggested Main Owner | Short Role |
|---|---|---|
| `agent-browser-clawdbot` | Rex / Andrew | browser-based ClawBot interaction |
| `agent-builder` | Andrew | building agents / agent scaffolding |
| `agent-council` | Rex | multi-agent discussion / council pattern |
| `agent-development` | Andrew | agent creation / development workflow |
| `agent-orchestrator` | Rex | orchestrating multiple agents |
| `architecture-designer` | Andrew / Rex | architecture design |
| `bird` | Lulu | content / light creative usage |
| `blogwatcher` | Lulu / Andrew | content radar / blog monitoring |
| `coding-agent` | Rex | implementation / coding execution |
| `consulting-mode` | Rex | strategic consulting output |
| `conventional-commits` | Rex | commit hygiene |
| `decision-trees` | Andrew | structured reasoning |
| `deepwork-tracker` | Alex / Andrew | deep work / focus tracking |
| `first-principles-decomposer` | Andrew | first-principles breakdown |
| `founder-coach` | Rex / Alex | founder support |
| `frontend-design` | Rex | frontend design |
| `frontend-slides` | Rex / Lulu | slide-like frontend presentation |
| `github` | Rex | GitHub workflow |
| `github-pr` | Rex | PR workflow |
| `humanizer` | Lulu / Alex | text naturalization |
| `impeccable-design` | Rex | higher-end design discipline |
| `markdown-converter` | Andrew | markdown transformation |
| `multi-viewpoint-debates` | Andrew | structured debate / alternative views |
| `munger-observer` | Andrew | analysis / observer role |
| `nano-banana-pro` | Lulu | content / experimental creative flow |
| `nano-pdf` | Andrew | PDF handling |
| `obsidian` | Andrew / Alex | knowledge management |
| `personal-consulting-router` | Alex | personal support routing |
| `self-improving-agent` | Andrew | agent improvement workflow |
| `skill-vetter` | Andrew | evaluate new skills |
| `summarize` | Andrew | summarization |
| `video-transcript-downloader` | Lulu / Andrew | transcript extraction |
| `weekly-synthesis` | Andrew | weekly review / synthesis |
| `youtube-watcher` | Lulu / Andrew | YouTube monitoring |

---

## Layer C — Selected ok-skills Worth Incorporating

These are community or imported skills that are especially useful to Jianan's operating system and should be considered part of the extended capability layer.

| Skill | Suggested Main Owner | Short Role |
|---|---|---|
| `brainstorming` | Andrew / Rex | clarify intent / requirements / design before implementation |
| `planning-with-files` | Andrew | structured planning with artifacts |
| `subagent-driven-development` | Rex | staged multi-subagent implementation |
| `test-driven-development` | Rex | TDD workflow |
| `skill-creator` | Andrew | create/update skills |
| `pptx` | Rex / Lulu | PPTX generation support |
| `docx` | Rex / Andrew | DOCX generation support |
| `pdf` | Andrew | PDF handling |
| `remotion-best-practices` | Lulu | video rendering workflow |
| `prompt-engineering-patterns` | Andrew | reusable prompting structures |
| `context7-cli` | Rex / Andrew | external docs / context retrieval |
| `get-api-docs` | Rex / Andrew | API docs retrieval |
| `find-skills` | Andrew | discover matching skills |
| `opencli` | Rex | CLI-centered workflows |
| `gh-address-comments` | Rex | GitHub review comment resolution |
| `gh-fix-ci` | Rex | CI fixing |
| `vercel-react-best-practices` | Rex | React/frontend delivery |
| `agent-browser` | Rex | browser-based execution |
| `ai-elements` | Rex / Lulu | UI / visual element generation |
| `better-icons` | Rex | design polish |
| `electron` | Rex | desktop-app oriented work |
| `exa-search` | Andrew | research/search |
| `pinchtab` | Rex | browser / tab workflow |
| `xlsx` | Andrew / Rex | spreadsheet artifacts |

---

## Recommended Operating Policy

### 1. JN-SkillHub first for strong matches
If a request strongly matches a private JN-SkillHub skill, agents should think of it first.

### 2. Ask-first, not force-first
Matching a skill does **not** mean auto-apply it.
The normal pattern should be:
- detect likely fit
- mention the skill/workflow
- ask Jianan if he wants to use it
- proceed after confirmation

### 3. Legacy + ok-skills as supporting layer
Older local skills and selected ok-skills are the extended capability map.
They should be available for reuse, but not all should be made default behavior.

### 4. Agent specialization matters
The same skill may be callable by all, but should still have a preferred owner to reduce duplication and confusion.

---

## Priority Mapping (Short Version)

### Andrew
- Core: `codebase-to-course`, `claw-vibe-project`
- Supporting: `summarize`, `skill-vetter`, `weekly-synthesis`, `brainstorming`, `planning-with-files`

### Rex
- Core: `jianan-presentation-system`, `design-front`
- Supporting: `github`, `github-pr`, `subagent-driven-development`, `test-driven-development`, `pptx`

### Lulu
- Core: `video-post-editor`, `ai-morphing-video`
- Supporting: `frontend-slides`, `video-transcript-downloader`, `youtube-watcher`, `remotion-best-practices`

### Alex
- Core: shared skill layer for now
- Supporting: `personal-consulting-router`, `deepwork-tracker`, `obsidian`, `humanizer`

---

## One-line Summary

> JN-SkillHub is the private shared skill layer; legacy local skills and selected ok-skills form the extended operating capability layer for Jianan's multi-agent system.
