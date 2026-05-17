# Guizang Absorption for Frontend Slides

Borrow the durable principles from guizang-ppt-skill:

## Style systems

- Editorial / electronic-ink mode: warm, human, narrative, magazine-like.
- Swiss / international mode: grid, high contrast, information hierarchy, strong structure.

Do not treat style as only color. A style includes typography, grid, page rhythm, component library, image slots, and QA rules.

## Pre-build checks

For substantial decks, define:

- style family;
- audience;
- duration/page count;
- source materials;
- image/screenshot needs;
- theme palette;
- hard constraints.

Ask only for blocking unknowns. Otherwise assume and state assumptions.

## Image generation and screenshot handling

- Ask before generating non-trivial images.
- Pick slot ratio before generation: 21:9, 16:10, 16:9, 4:3, 1:1, 3:4.
- For screenshots, preserve truth first. Frame/clean them before redesigning.
- For diagrams/info graphics, match deck language and theme.
- Save assets under `images/{page}-{semantic-name}.{ext}`.
- Generated image must not include slide chrome: no footer, title, page number, corner badge, or decorative border.

## Visual QA

- no emoji-as-icon in serious decks;
- no generic AI gradient unless explicitly chosen;
- no unreadable small text;
- no image overflow or nav collision;
- no style drift across sections;
- no random one-off layout when a known page type fits.
