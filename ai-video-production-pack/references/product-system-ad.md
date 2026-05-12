# Product / System Ad

Use for software product demos, dashboard promos, AI agent systems, commercial-feeling explainers.

Absorbs useful structure from Seedance/Jimeng product-ad prompts, but adapts from physical products to software/system products.

## Required Inputs

- Product/system name
- Target user
- Core promise
- 1–3 visible features
- Required screenshots / logos
- Target duration and aspect ratio

## JSON Prompt Shape

```json
{
  "title": "...",
  "model_target": "Jimeng/Seedance/Kling/Runway style video generation",
  "system_reference": {
    "input_assets": ["@Image1 dashboard screenshot", "@Image2 logo if available"],
    "must_preserve": ["UI layout", "brand color", "logo shape"],
    "do_not_generate_text": true
  },
  "commercial_goal": {
    "core_message": "...",
    "target_audience": "...",
    "selling_points": ["..."]
  },
  "global_settings": {
    "duration": "7s/10s/15s",
    "aspect_ratio": "16:9/9:16/3:4",
    "style": "premium software product cinematography",
    "motion_intensity": "controlled",
    "text_policy": "overlay exact text in post"
  },
  "sequence": [],
  "negative_prompt": ["distorted UI", "fake text", "wrong logo", "chaotic particles", "cheap cyberpunk"]
}
```

## Software Product Shot Ideas

- Hero dashboard reveal
- Task cards flowing into automation pipeline
- Agent nodes coordinating around a central hub
- Before/after split: scattered docs → structured dashboard
- Evidence links lighting up
- Final clean end card
