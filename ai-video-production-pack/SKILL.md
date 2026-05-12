---
name: ai-video-production-pack
description: Route and produce AI-assisted video assets: internal sharing/explainer videos, product/system ads, Xiaohongshu/short-video covers, reversal/hook openings, and image-to-video prompts for Jimeng/Seedance/Kling/Runway-style tools. Use when the user wants to make a video, storyboard scenes, generate video prompts, create covers, animate screenshots/images, or improve video visual language.
---

# AI Video Production Pack

Use this as the video asset-production layer under PLO B2B Content / Personal / Product work.

Core rule: first route the video type, then use the narrowest production lane. Do not mix Xiaohongshu hooks into formal internal-sharing videos unless the user asks for a more viral tone.

## 1. Route First

| User intent | Lane | Read next |
|---|---|---|
| company sharing, methodology explainer, internal training, PLO/OpenClaw/CER/PTR explanation | B2B Internal Sharing / Explainer | `references/internal-sharing-video.md` |
| product demo, software/system promo, dashboard/agent product video, commercial-feeling ad | Product / System Ad | `references/product-system-ad.md` |
| cover image, Xiaohongshu/Douyin/Bilibili/WeChat video thumbnail, high-click title visual | Social Cover | `references/social-cover.md` |
| strong opening, reversal, before/after story, viral short intro, ordinary-person-to-AI-power contrast | Hook / Reversal | `references/hook-reversal.md` |
| user already has a first frame/image/screenshot and wants it animated | Image-to-Video Director | `references/image-to-video.md` |
| 30s+ multi-shot video, scene list, storyboard, visual consistency | Storyboard Core | `references/storyboard-core.md` |

## 2. Default Workflow

```text
brief → route → lock visual language → storyboard → per-shot prompts → reference images/first frames → image-to-video prompts → review → assembly notes
```

Minimum outputs:
- video lane and target platform;
- visual language lock;
- shot list with each shot's information job;
- prompt per shot or image-to-video instruction;
- negative constraints;
- review checklist.

## 3. PLO Integration

- B2B Content/Internal Sharing: route to `internal-sharing-video` + `storyboard-core`.
- Product/System work: route to `product-system-ad`.
- Social distribution: route to `social-cover` and optionally `hook-reversal`.
- Personal/demo work: start with `storyboard-core` or `image-to-video`.

## 4. Tool-Agnostic Prompt Policy

Prefer tool-agnostic prompts first, then adapt to Jimeng/Seedance/Kling/Runway:
- Subject and information job
- Composition and camera movement
- Lighting and color palette
- Motion intensity and timing
- Reference asset usage
- Text policy
- Negative constraints

For Seedance/Jimeng, explicitly state reference roles such as `@Image1 as first frame`, `@Image2 as UI screenshot reference`, or `@Video1 as camera rhythm reference`.

## 5. Review Before Generation

Before spending generation credits, check:
- Does each shot explain one idea only?
- Are all shots visually consistent?
- Are text overlays short enough?
- Is the motion too chaotic for a business audience?
- Is this better as HTML/motion graphics rather than AI video?
- Are screenshots/logos/product identities protected from distortion?
