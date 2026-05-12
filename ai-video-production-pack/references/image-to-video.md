# Image-to-Video Director

Use when the user already has an image, screenshot, generated first frame, cover, or diagram and wants it animated.

## First Decide

- Is the source an exact UI/screenshot? If yes, keep motion subtle and overlay text in post.
- Is the source a metaphor/illustration? AI video motion can be stronger.
- Is identity preservation critical? Use source image as first frame/reference, not only in prompt text.

## Prompt Pattern

```text
Use @Image1 as the first frame and preserve its composition, style, color palette, and main objects.
Animate with [slow push / parallax depth / gentle card flow / node pulse / timeline snap].
Keep all UI elements stable. Do not invent readable text. No warping, no melting, no extra logos.
Duration [5s/7s], aspect ratio [16:9/9:16]. Clean premium motion, controlled energy.
```

## Motion Levels

- Level 1: subtle parallax / slow push. Best for screenshots and diagrams.
- Level 2: card movement / glow pulse / flowing lines. Best for system metaphors.
- Level 3: dramatic reveal / particles / morph. Use only for hooks or ads.

## Common Failure Fixes

- UI text becomes gibberish → remove text from model generation; overlay in editing.
- Screenshot warps → lower motion level, say “preserve layout exactly”.
- Too cyberpunk → specify light-tech, white/cyan, no dark neon.
- Too chaotic → specify controlled, slow, elegant, minimal particles.
