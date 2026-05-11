# Workflow Map vs Architecture Map vs Work Package Map

Use this reference when a project has concrete feature tasks but the product/system architecture is unclear.

## Core distinction

| Map | Purpose | Answers | Audience |
|---|---|---|---|
| Workflow Map | Understand real work | How do users/business actually complete the job? | users, PM, SME, boss |
| Architecture Map | Design the system/product | What layers/modules/data/agents support the workflow? | architects, developers, QA |
| Work Package Map | Execute delivery | What can the team build/review/deliver? | project manager, team, boss |

## Rule

Do not directly convert every architecture layer into a development package. A good work package is usually a vertical capability slice that cuts across workflow, architecture, QA, and delivery.

Example: “PTR Input Package” may include business input definition, docx format requirement, backend ingestion, validation rules, QA cases, and review owner.

## Conversion process

1. Start from the vertical task / feature roadmap.
2. Identify the business workflow step each task belongs to.
3. Identify architecture layers touched by each task.
4. Group tasks into capability packages.
5. Add quality gate, owner, review owner, and done criteria.

## Conversion table template

| Feature Task | Phase / Timeline | Owner | Workflow Step | Architecture Layer | Capability Package | Reuse Potential | Evals Needed | Deliverable |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |

## CER example from earlier roadmap

| Feature Task | Capability Package | Architecture Layer | Reuse Potential | Evals Needed | Deliverable |
|---|---|---|---|---|---|
| Extraction logic update | Input / Parsing Package | Data + rules + backend | High for PTR/CER transfer | field extraction cases | updated extraction logic |
| 70% CER Automation Framework | Generation / Automation Package | LLM + rules + backend | High | section generation evals | automation framework |
| Enhance LLM generation speed | AI Function Package | LLM + prompt + runtime | Medium | speed/quality regression | faster generation path |
| LIMS analysis | Input / Data Package | source integration + mapping | Medium | mapping validation | LIMS mapping notes |
| Server Setup | Platform Package | backend/server/deploy | High | smoke tests | server foundation |
| 70% CER Automation Accuracy | Verification / Evals Package | evals + rules + SME review | High | regression suite | accuracy report |
| Evals/Patch/Whitelist/Few-shot | Evals / QA Package | eval harness + prompt/rules | High | eval thresholds | eval patch set |
| UI Optimization & Server Maintain | Review / Delivery + Platform | UI + backend | Medium | usability tests | optimized review flow |
| Literature Review RAG | Knowledge / RAG Package | retrieval + data + LLM | Medium | citation/relevance evals | RAG pipeline |
| Literature Review Automation | Generation / Automation Package | agent/LLM + backend | Medium | output quality evals | automation flow |
| UI with Evals functions | Review / Evals Package | UI + eval results + QA | High | user acceptance | eval-enabled UI |
| Launch + Owner Review | Review / Delivery Package | release + stakeholder flow | Medium | acceptance checklist | owner review evidence |
| Presentation to each site | B2B Content / Influence | narrative + evidence | High as content template | stakeholder fit review | site presentation |

## CER/PTR two-layer view

### Vertical progress layer
Use for meetings and execution:
- PTR user needs and priority
- PTR development architecture
- CER BU Transfer + Agentic Iteration
- ROI with User + BA

### Horizontal architecture package layer
Use for product/system design:
- User / Business Alignment
- Input / Data
- Workflow / Process
- Architecture / Platform
- AI Function / Agentic
- Verification / Evals / QA
- Review / Delivery
- Transfer / Reuse / ROI

## Sanity check

A work package is reasonable if:
- it has a business goal;
- it has clear inputs and outputs;
- it touches enough system layers to be deliverable;
- it has an owner and review owner;
- it has quality / eval / acceptance criteria;
- it can be reused or explicitly marked one-off.
