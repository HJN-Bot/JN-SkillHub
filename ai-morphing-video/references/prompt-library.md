# AI Morphing Video Prompt 库

## Persona 5 风格提示词（完整版）

### 核心 Style Prompt（英文，FLUX 效果最佳）

```
Persona 5 style, bold cel-shaded illustration, stark red black white color palette,
high contrast pop art comic aesthetic, thick black outlines, dynamic diagonal composition,
Japanese urban scene, graphic novel panel, Shoji Meguro visual direction,
no gradients, flat color fills, shadow as solid shapes, speech bubble elements,
halftone dot patterns in shadows, bold typography elements in background,
```

### 配套 Negative Prompt

```
realistic photography, soft gradients, pastel colors, watercolor painting,
3D render, CGI, blurry edges, low contrast, brown tones, green tones,
natural lighting, photorealistic skin, depth of field bokeh, lens flare,
muted colors, desaturated, vintage filter, sepia
```

---

## 场景专用提示词

### 城市/建筑类

```
# 日本城市夜景
Tokyo Shibuya crossing at night, red traffic lights, yellow taxi, neon signs in Japanese,
wet pavement reflections stylized as flat color shapes, Persona 5 pop art style

# 欧洲历史建筑（如爱丁堡）
Edinburgh Old Town stone architecture silhouette, red telephone box iconic,
Scottish castle on hill, cobblestone street, bold graphic treatment,
high contrast black shadows, accent red elements

# 地铁/交通场景
Tokyo subway platform, rush hour crowd as graphic silhouettes,
train arrival dynamic motion lines, departure board as stylized element,
P5 HUD aesthetic overlay
```

### 人物/角色类

```
# 主角风格
Ren Amamiya Joker style protagonist, school uniform with hidden rebel aesthetic,
phantom thief transformation sequence, red gloves and mask reveal,
dramatic low angle shot, speed lines emanating from center

# 群像
Phantom Thieves group pose, dynamic diagonal layout, each character in bold silhouette,
color-coded outfits, overlapping composition, manga action spread style
```

### 室内/氛围类

```
# 咖啡馆
Cozy attic coffee shop, warm amber against black graphic shadows,
bookshelves and vinyl records as decorative elements, jazz atmosphere,
Leblanc cafe inspired, single warm light source creating dramatic contrast

# 调查室
Detective investigation board, red string connecting evidence,
newspaper clippings as flat graphic elements, dramatic spotlight,
conspiracy thriller aesthetic in P5 style
```

---

## Morphing 转场 Prompt 模板

### 场景切换类

```
# 万花筒擦除式
Kaleidoscopic wipe transition, Persona 5 geometric shapes exploding outward,
bold red diamonds and black triangles filling frame, smooth morphing between scenes,
no flickering, consistent cel-shaded style, dynamic speed lines, 24fps feel

# 墨水晕染式
Ink wash reveal transition, black ink spreading across frame like calligraphy,
revealing new scene through ink shapes, Japanese brush stroke aesthetic,
red accent lines cutting through darkness, smooth and organic motion

# 斜切快闪式
Sharp diagonal slash cut, speed lines suggesting katana strike,
scene A splits along diagonal revealing scene B, red flash at cut point,
dynamic manga action panel transition aesthetic

# 粒子分解式（高级）
Scene A fragmenting into geometric shards, black and red mosaic pieces,
each shard independently rotating to reveal scene B underneath,
smooth particle physics, Persona 5 UI element aesthetic
```

### 人物转化类

```
# 幻影窃贼变身
Phantom Thief transformation morph, everyday clothes dissolving into costume,
mask appearing with burst of red energy, pose changing dynamically,
cel-shaded animation frames, bold outline pulsing
```

---

## LoRA 触发词参考

### CivitAI 常用 P5 LoRA 触发词

| LoRA 名称 | 触发词 | 推荐权重 |
|----------|--------|---------|
| Persona 5 Style | `persona5`, `p5style` | 0.8-0.9 |
| P5R Art Style | `p5r art style` | 0.75-0.85 |
| Anime Pop Art | `pop art anime`, `bold outline` | 0.7 |
| Bold Comic Style | `comic style`, `thick outline` | 0.8 |

### 搜索关键词（CivitAI）

- `"Persona 5"` - 直接搜索游戏风格
- `"cel shaded"` + `"anime"` - 找赛璐璐动画风格
- `"pop art"` + `"bold outline"` - 找波普艺术轮廓风格

---

## 其他风格提示词

### 蜘蛛侠：平行宇宙风格

```
Into the Spider-Verse animation style, comic book halftone dot patterns,
multiple color printing misalignment effect, kinetic energy lines,
bold black outlines, primary color pops against white, 
dynamic action pose, Ben-Day dots in shadows

Negative: smooth gradients, photorealistic, 3D CGI, clean digital art
```

### 攻壳机动队风格

```
Ghost in the Shell 1995 film style, detailed cyberpunk cityscape,
blue-green bioluminescent neon, rain-soaked night streets,
manga crosshatching in shadows, technical schematic overlays,
philosophical atmosphere, Mamoru Oshii visual direction

Negative: bright colors, day scenes, soft lighting, simple composition
```

### 赛博朋克 2077 宣传美术风格

```
Cyberpunk 2077 official art style, Night City neon yellow-orange palette,
chrome and neon contrast, dystopian corporate advertising aesthetic,
holographic billboards as graphic elements, rain and fog,
Johnny Silverhand rebel energy

Negative: clean future, utopian, pastel, natural scenes
```
