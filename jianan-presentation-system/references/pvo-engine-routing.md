# PVO Engine Routing for Jianan Presentation System

`jianan-presentation-system` remains Jianan's high-stakes presentation skill. PVO adds the routing layer for visual expression and output engine selection.

## Engine choices

| Need | Route |
|---|---|
| Formal editable PowerPoint | native PPTX / pptxgenjs / PPT Master-style execution |
| High-aesthetic browser sharing | PVO → `frontend-slides` |
| One-off slide or diagram | PVO page plan + selected execution route |
| Cover/social visual | PVO image route |
| Speaker script only | content/oral script references; no visual engine |

## Before execution

For T2+ decks, create or update:

- Project Brief
- Style Lock
- Page Plan
- Image Manifest if visual assets are involved
- Visual QA checklist

## Native PPTX preference

Prefer native PPTX when:

- boss/client/customer expects PowerPoint;
- collaborators must edit text, charts, or shapes;
- charts/tables need to remain editable;
- enterprise environment discourages HTML delivery.

Prefer HTML deck when:

- delivery is a live/web sharing;
- strong visual identity and motion matter;
- screenshots/videos/proof walls are central;
- single-file browser delivery is acceptable.
