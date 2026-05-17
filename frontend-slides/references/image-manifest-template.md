# Image Manifest Template

Use when a deck contains screenshots, generated images, covers, diagrams, or visual proof.

```md
# IMAGE_MANIFEST

## P01 — cover visual
- Type: cover / documentary photo / diagram / screenshot frame / data poster
- Slot ratio: 16:9 / 21:9 / 16:10 / 4:3 / 1:1 / 3:4
- Source: user / generated / screenshot / web / existing asset
- Must preserve: text / UI / brand / data / none
- Style: follow STYLE_LOCK
- File: images/01-cover.png
- Instruction/prompt:
```

Rules:

- one manifest entry per meaningful image;
- never generate a beautiful but unusable ratio;
- never put page titles/footers inside generated images;
- Chinese deck diagrams use Chinese labels;
- screenshots containing real proof should not be hallucinated or redrawn unless explicitly requested.
```
