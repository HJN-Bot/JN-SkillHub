# Skill Usage Monitoring

Use this lightweight monitor to observe how PLO and related skills perform in real projects.

## Purpose

This is not a heavy analytics system. It is a small reflection loop:

- what skill was used;
- for what task;
- what output it produced;
- what feedback Jianan gave;
- whether the skill/template should be improved.

## When to Log

Log only meaningful uses:

- PLO used for a T2+ task;
- a reference/template was used to produce a real deliverable;
- Jianan gave explicit feedback such as “this is right”, “too much”, “missing X”, “not useful”; 
- a task crossed from planning into development handoff;
- a repeated pattern/gap appeared.

Do not log trivial one-shot use.

## Weekly Review

Once per week, summarize:

1. Which skills were used most?
2. Which references/templates produced useful outputs?
3. Which outputs received correction from Jianan?
4. Which gaps repeated 2+ times?
5. Which patch should be proposed as dry-run?
6. Which projects are active and need maintenance?

## Lightweight Scoring

| Score | Meaning |
|---|---|
| 5 | Directly useful, reusable, little correction needed |
| 4 | Useful with minor edits |
| 3 | Partially useful, needs structure improvement |
| 2 | Misrouted or too verbose / too vague |
| 1 | Not useful; should not trigger this way |

## Patch Rule

- 1st gap: record only.
- 2nd repeated gap: dry-run recommendation.
- 3rd repeated gap: propose patch to reference/template.
- Write only after human confirmation.

## Output

Use `templates/skill-usage-monitoring-log.md` for individual records and weekly summaries.
