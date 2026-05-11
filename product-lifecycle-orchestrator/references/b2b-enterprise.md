# B2B Enterprise Automation Reference

Use for stakeholder-driven enterprise AI/product projects such as CER/PTR automation, internal workflow tools, compliance/document generation systems, or cross-team platform work.

## Key Principle

Separate three maps:

1. **Workflow Map** — how the business/user process actually works.
2. **Architecture Map** — system layers needed to support the workflow.
3. **Work Package Map** — executable deliverables assigned to the team.

Do not split development only by architecture layers. Prefer vertical capability packages that produce reviewable deliverables.

## Work Package Classification

### A. User / Business Alignment Package
Use when requirements and priority are not yet stable.

Includes:
- stakeholder / user map
- user needs alignment
- priority decision
- acceptance owner
- scope boundary

Deliverables:
- User Requirements Definition
- priority order
- decision log

Example CER/PTR:
- CT SE + Team meeting
- SE Resource Bridge Meeting
- SE User Needs Alignment
- PTR Change / PTR New / CER V2 / CER BU Transfer priority

### B. Input / Data Package
Use when source materials determine feasibility or transfer effort.

Includes:
- input document list
- format requirements
- sample completeness
- source/target mapping
- data quality risks

Deliverables:
- input material inventory
- sample set
- data gap list
- transfer-effort assumptions

Example CER/PTR:
- AT and XP historical CER
- corresponding PTR inputs
- 5–10 CER + 2 PTR docx preferred
- CT CER → BU CER transfer material set

### C. Workflow / Process Package
Use when the real working process must be understood before design.

Includes:
- current user workflow
- decision/review points
- SME review points
- handoff points
- usability requirements

Deliverables:
- workflow map
- human-in-the-loop map
- review checklist

### D. Architecture / Platform Package
Use when the team needs the technical and Agent architecture.

Includes:
- system context
- modules/components
- data flow
- LLM/Agent responsibilities
- rules/business logic
- backend/server conversion
- audit trail / permissions

Deliverables:
- architecture diagram
- module boundary
- integration points
- architecture decisions

### E. Generation / AI Function Package
Use when a specific AI capability must be implemented.

Includes:
- prompt/template design
- section generation
- extraction/mapping
- rules invocation
- fallback behavior

Deliverables:
- AI feature spec
- prompt/template spec
- expected output examples
- failure mode handling

### F. Verification / Evals / QA Package
Use when quality must be repeatable.

Includes:
- rule checks
- regression cases
- SME review checklist
- user acceptance cases
- score/threshold

Deliverables:
- Evals case list
- QA plan
- acceptance criteria
- version regression report

### G. Review / Usability / Delivery Package
Use when users must review, correct, approve, or export outputs.

Includes:
- review UI/process
- user feedback capture
- export/delivery format
- version acceptance

Deliverables:
- review flow
- usability feedback
- release note
- delivery evidence

### H. Transfer / Reuse Package
Use when proving reuse across BU/product/document type.

Includes:
- common vs different parts
- reusable modules
- new-build modules
- transfer effort
- ROI impact

Deliverables:
- reuse analysis
- transfer work packages
- effort estimate
- ROI assumptions

Example CER/PTR:
- CER → BU Transfer architecture and work packages
- PTR as reuse validation scenario

## CER/PTR Suggested Package Split

### PTR
1. PTR User Requirement Package
2. PTR Input/Data Package
3. PTR Workflow & Scope Package
4. PTR Architecture & Work Package Design
5. PTR Evals/QA Package
6. PTR ROI Package

### CER BU Transfer + Agentic Iteration
1. CER Input Material Package
2. CER Transfer Gap Analysis Package
3. CER BU Transfer Architecture Package
4. Agentic Iteration Package
5. CER Evals/QA Package
6. CER ROI / Transfer Effort Package

## Minimal Template

For each package:

| Field | Content |
|---|---|
| Package name |  |
| Goal |  |
| Scope |  |
| Inputs |  |
| Outputs |  |
| Owner |  |
| Review owner |  |
| Dependencies |  |
| Timeline |  |
| Evals/QA requirement |  |
| Done criteria |  |
| Risks |  |

## Boss / Team Decision Checklist

- Which package is P0?
- Who owns user requirement definition?
- Who owns architecture and work package draft?
- Who owns input material collection?
- Who owns QA/Evals?
- Who confirms ROI assumptions?
- Which meetings are required, and which can be merged?
