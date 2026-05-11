# Evals / QA Plan Template

Use for enterprise AI systems where output quality must be repeatable and reviewable.

## 1. Scope

| Field | Value |
|---|---|
| Module / package |  |
| Output type |  |
| Critical risks |  |
| Release / milestone |  |

## 2. Quality Layers

| Layer | Purpose | Owner | Required? | Evidence |
|---|---|---|---|---|
| Rule / code checks | deterministic format/data validation |  | Yes / No |  |
| LLM eval | semantic quality / completeness |  | Yes / No |  |
| SME review | domain/regulatory correctness |  | Yes / No |  |
| User acceptance | workflow/usability fit |  | Yes / No |  |
| Regression replay | ensure changes do not break old cases |  | Yes / No |  |

## 3. Eval Cases

| Case ID | Input | Expected output / criteria | Risk covered | Reviewer | Status |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## 4. Scoring

| Metric | Threshold | Method | Owner |
|---|---:|---|---|
| Completeness |  | rule / LLM / SME |  |
| Accuracy |  | rule / LLM / SME |  |
| Traceability |  | rule / audit |  |
| Usability |  | user review |  |
| Regression pass rate |  | automated replay |  |

## 5. Release Gate

A version can move forward only if:
- critical rule checks pass;
- regression cases pass or exceptions are documented;
- SME review has no blocking issue;
- user acceptance is confirmed for target workflow;
- open risks are documented.

## 6. Open Issues

| Issue | Severity | Owner | Next action | Due |
|---|---|---|---|---|
|  |  |  |  |  |
