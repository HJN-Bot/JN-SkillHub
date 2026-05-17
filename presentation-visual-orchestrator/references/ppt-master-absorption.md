# PPT Master Absorption Notes

PPT Master contributes a native-PPTX execution pattern, not just visual taste.

## Useful ideas

1. Separate strategy from execution.
2. Use a project folder with durable artifacts.
3. Confirm canvas/page count/audience/style/color/icon/font/image strategy before generating.
4. Use a lock file so long deck generation does not drift.
5. Use live preview / visual edit loops when available.
6. Prefer native editable PPTX when the deliverable must be modified by humans in PowerPoint.

## PVO adaptations

Create these artifacts for T2+ deck work:

- `PROJECT_BRIEF.md`
- `STYLE_LOCK.md`
- `PAGE_PLAN.md`
- `IMAGE_MANIFEST.md`
- `VISUAL_QA.md`

## Engine routing

Choose native PPTX when:

- boss/client/customer deck requires PowerPoint handoff;
- other people will edit text, charts, or shapes;
- formal enterprise context prefers PPTX;
- native charts/shapes matter.

Choose HTML deck when:

- public sharing / demo / web delivery;
- visual identity and browser animation matter more than editability;
- single-file presentation is acceptable;
- screenshots/videos/interactive proof are central.

## Spec lock discipline

For long decks, reread `STYLE_LOCK.md` and current page entry before each major page batch or page edit. Do not rely on memory for colors, fonts, density, or image rules.
