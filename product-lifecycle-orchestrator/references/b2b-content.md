# B2B Content / Influence Reference

Use this for stakeholder-facing artifacts: boss brief, executive update, internal sharing, whitepaper, case study, methodology article, sales/customer enablement, playbook, or Feishu wiki.

## Difference from B2B Enterprise Automation

B2B Enterprise produces a working system/process.
B2B Content produces a decision/influence artifact.

Success is not “content exists.” Success is stakeholder understanding, decision, buy-in, reuse, or follow-up action.

## Lifecycle

### Phase 1 — Audience & Objective

Answer:
- Who is the primary audience?
- What level are they: peer, boss, big boss, HQ, customer, user, team?
- What should they decide/do after reading?
- What constraints exist: time, politics, evidence, confidentiality?

Outputs:
- audience map
- decision/action target
- constraints

### Phase 2 — Message & Evidence

Answer:
- What is the one-line thesis?
- What data/proof supports it?
- What objections will the audience have?
- What evidence is missing?

Outputs:
- thesis
- proof points
- evidence table
- objection/answer list

### Phase 3 — Narrative Architecture

Choose structure:
- Problem → Solution → Ask
- Fact → Gap → Decision
- Before → After → ROI
- Case → Method → Reuse
- Risk → Mitigation → Resource
- Vision → Roadmap → Next Step

Outputs:
- narrative arc
- section outline
- message hierarchy

### Phase 4 — Asset Production

Choose format:
- 1-page brief
- PPT / deck
- memo
- Feishu wiki
- case study
- whitepaper
- internal sharing
- playbook

Outputs:
- draft asset
- visual/diagram needs
- version owner


## Video / Visual Asset Production

When the artifact is an internal sharing video, explainer, product/system promo, social cover, or AI-generated visual asset, route Asset Production through `ai-video-production-pack`.

Default split:

| Need | Route | Minimum Output |
|---|---|---|
| Company sharing / methodology explainer | `ai-video-production-pack` → internal-sharing-video + storyboard-core | scene plan, visual language lock, per-scene prompt notes |
| Software/system product ad | product-system-ad | JSON-style sequence prompt, hero shot, negative constraints |
| Xiaohongshu / video cover | social-cover | 3 title options, 3 subtitle options, one core visual hook |
| Viral/reversal opening | hook-reversal | 12s hook structure, conflict/turn/payoff |
| Animate existing image/screenshot | image-to-video | first-frame prompt, motion level, anti-warp constraints |

Rules:
- Do not pollute formal B2B videos with short-drama tropes unless the user asks for a viral/social tone.
- Use generated video for atmosphere/metaphor; use real screenshots or HTML/motion graphics for exact UI and text.
- For internal sharing, prefer light-tech, credible, controlled motion over dark cyberpunk or chaotic particles.

### Phase 5 — Review & Stakeholder Fit

Review gates:
- Does it fit the stakeholder level?
- Is the ask clear?
- Is there enough evidence?
- Is the language too technical or too vague?
- Are objections addressed?
- Is there a concrete next action?

Outputs:
- reviewed draft
- decision-ready version

### Phase 6 — Delivery & Impact Loop

After delivery, record:
- who received it
- feedback
- decision/action triggered
- follow-up task
- reusable template/pattern

## Common Artifact Types

| Artifact | Best For | Must Include |
|---|---|---|
| Boss brief | Direction/resources/decision | conclusion, evidence, ask, next step |
| Executive update | higher-level alignment | business value, risk, ROI, timeline |
| Internal sharing | influence and knowledge transfer | narrative, examples, takeaways |
| Case study | proof and reuse | context, problem, solution, impact, reusable method |
| Whitepaper | methodology/IP | thesis, framework, evidence, application |
| Playbook | repeated execution | steps, roles, templates, checks |

## Output Quality Rules

A good B2B content artifact:
- has one clear audience;
- asks for one clear action or decision;
- separates facts from opinions;
- links claims to evidence;
- anticipates objections;
- has a next step;
- leaves behind a reusable asset.
