# PVO Routing for Frontend Slides

Use this reference when a HTML deck is part of a PVO-governed presentation.

## Role boundary

- PVO decides: audience, deck type, output engine, style lock, page plan, image manifest, QA gates.
- `frontend-slides` executes: single-file HTML deck, viewport fit, visual system, animations, browser-ready delivery.

## Required inputs from PVO

Before building a T2+ HTML deck, look for or create:

- `PROJECT_BRIEF.md`
- `STYLE_LOCK.md`
- `PAGE_PLAN.md`
- `IMAGE_MANIFEST.md` if images/screenshots/generated visuals are involved

If these do not exist and the deck is simple, create a compact version inline before coding.

## HTML deck execution rules

1. Do not collapse rich Jianan content into empty slogan slides.
2. Preserve one clear takeaway per page.
3. Respect viewport fit: no scroll inside slides.
4. If using a rigid style such as Swiss, use named layout/page types rather than freeform page invention.
5. Screenshots are evidence; keep them readable.
6. Generated images are embedded assets; they should not contain slide titles, page numbers, or footers.
7. Run visual QA before delivery.

## When not to use frontend-slides

If the user needs native editable PPTX for PowerPoint handoff, route through `jianan-presentation-system` or native PPTX tooling instead of HTML-first execution.
