---
name: ai-morphing-video
description: >
  AI风格化视频创作完整技能，覆盖两大主流流派：
  ①「风格化场景旅拍」（P5/漫画风照片+Ken Burns运镜，类似爱丁堡P5案例）；
  ②「AI产品特效广告」（实拍产品+科技感光效/全息文字，类似相机案例）。
  当用户说「做AI视频」「风格化转场」「产品特效视频」「复刻这种效果」「Ken Burns」
  「P5风格」「全息光效」「做个宣传片」「libtv」「可灵」时，必须触发此技能。
  即便用户只是发了一张照片说「帮我做成视频」，也要触发并通过引导对话明确需求。
---

# AI 风格化视频创作 Skill

## 流派速判（第一步）

| 流派 | 典型效果 | 核心技术 | 推荐工具 |
|------|---------|---------|---------|
| **A·风格化旅拍** | 照片→P5漫画风+缓慢运镜 | 照片风格化 + Ken Burns | fal.ai FLUX→可灵O3 |
| **B·产品科技特效** | 产品图+全息光效+悬浮文字 | 可灵O3「全能参考」模式 | LibTV / fal.ai |
| **C·叙事TVC** | 多场景故事+角色+音乐 | 分镜脚本+多镜头 | LibTV 全流程 |

---

## 交互层：引导式问卷

**接到用户需求，信息不完整时，按轮次收集，每次最多2问：**

### 第一轮：框架定位
```
1. 视频类型？
   A) 风格化旅拍（照片变漫画/电影风，加运镜）
   B) 产品特效广告（产品加光效、全息数据、科幻感）
   C) 叙事短片/TVC（有故事线，多场景）

2. 素材情况？
   A) 已有原始照片（几张？）
   B) 只有产品照片
   C) 从零生成，暂无素材
```

### 第二轮：视觉基调
```
3. 目标风格？（可多选）
   · P5/女神异闻录 → 红黑白高对比波普漫画
   · 赛博朋克 → 蓝紫霓虹黑暗未来
   · 电影感写实 → 奉俊昊/诺兰调色
   · 日系胶片 → 暖调 Lo-fi 质感
   · Apple极简科技 → 冷白高饱和度品牌
   · 其他（请描述）

4. 情绪节奏？
   · 沉浸缓慢（旅拍/艺术短片）
   · 节奏感强（广告/MV）
   · 戏剧张力（叙事短片）
```

### 第三轮：流派专属细节

**流派A：**
```
5. 场景数量 + 每个场景描述（地点/时间/氛围）？
6. 转场风格？
   · Ken Burns平移（最丝滑，静止感）
   · 形变Morph（场景间流体过渡）
   · 混合两种
```

**流派B：**
```
5. 产品名称 + 核心卖点（1-3条）？
6. 特效风格？
   · 蓝色科技圆环（适合相机/圆形产品）
   · 金色高端光晕（手表/奢品）
   · 数字能量爆发（手机/耳机/电子）
   · Apple极简品牌（白底/极简）
```

### 第四轮：技术收尾
```
7. 平台偏好？
   A) fal.ai（国际/API/精细控制）
   B) LibTV（国内/可灵O3/一站式）
   C) 按效果选

8. 成片时长目标？
   · 15-30秒（短视频钩子）
   · 30-60秒（完整短片）
   · 1-3分钟（TVC广告）
```

---

## 流派A：风格化旅拍

### 技术本质

视频1（爱丁堡案例）的效果 **不是 Morphing**，而是：
> **「风格化静态图 + Ken Burns Effect（极缓慢摄像机推拉平移）」**

Ken Burns = 对静态图做极其缓慢的运镜（推/拉/平移），制造"镜头在动"的假象。
真正的场景间 Morphing 可选加在转场处。

### 技术流程

```
原始照片
  ↓ Step 1：FLUX + ControlNet Canny + P5 LoRA（fal.ai）
风格化图（红黑白漫画风，保留建筑构图）
  ↓ Step 2a：可灵O3 单帧图生视频 + Ken Burns Prompt
每个场景的5秒运镜片段
  ↓ Step 2b（可选）：Kling O3 双关键帧 Morphing 转场
  ↓ Step 3：ffmpeg 拼接 + 帧插值 + 音乐
最终成片
```

### Step 1：风格化（fal.ai）

```javascript
const result = await fal.subscribe("fal-ai/flux-general/image-to-image", {
  input: {
    image_url: "YOUR_PHOTO_URL",
    prompt: buildStylePrompt(scene, style),  // 见 prompt-library.md
    strength: 0.82,
    guidance_scale: 7.5,
    num_inference_steps: 30,
    controlnets: [{
      path: "InstantX/FLUX.1-dev-Controlnet-Canny",
      image_url: "YOUR_PHOTO_URL",
      control_weight: 0.65,     // 0.5-0.8：越高越保留建筑轮廓
      end_percentage: 0.75
    }],
    loras: [{
      path: "YOUR_P5_LORA_URL", // 见 lora-sources.md
      scale: 0.85               // 0.75-0.95：P5风格强度
    }]
  }
});
// 费用：约 $0.04-0.075/张
```

**strength 调优指南：**
- 0.70-0.75：保留更多原照片特征，风格化较轻
- 0.80-0.85：推荐区间，构图保留+风格充分
- 0.88-0.95：风格最强，构图变化较大

### Step 2a：Ken Burns 运镜（可灵O3）

```javascript
const result = await fal.subscribe("fal-ai/kling-video/v2.6/pro/image-to-video", {
  input: {
    image_url: "STYLED_IMAGE_URL",
    prompt: buildKenBurnsPrompt(cameraMotion, style),
    duration: "5",
    aspect_ratio: "9:16",
    cfg_scale: 0.4   // 低cfg更自然
  }
});
```

**Ken Burns Prompt 模板：**
```
[运镜指令], Persona 5 bold comic art style, red black white color palette,
static scene with only camera movement, no character animation,
smooth cinematic motion, stable, no flickering

运镜指令替换表：
· 向右平移 → "slow pan right, revealing the full cityscape"
· 向前推进 → "slow push in toward the cathedral, depth increasing"
· 仰拍上摇 → "slow tilt up from cobblestone street to dramatic crimson sky"
· 旋转揭示 → "slow orbital move around the monument"
· 拉镜揭示 → "slow pull back, widening to reveal grand architecture"
```

### Step 2b：场景间 Morphing（可选）

```javascript
const result = await fal.subscribe("fal-ai/kling-video/o3/standard/image-to-video", {
  input: {
    image_url: "SCENE_A_LAST_FRAME",
    tail_image_url: "SCENE_B_FIRST_FRAME",
    prompt: "[转场类型], P5 red black geometric shapes dissolving and reforming",
    duration: "5",
    aspect_ratio: "9:16"
  }
});

转场类型替换：
· kaleidoscopic wipe（万花筒擦除）
· ink brush reveal（墨水晕染揭示）
· diagonal slash cut（斜切速线）
· particle dissolve（粒子分解）
```

---

## 流派B：产品科技特效广告

### 技术本质

视频2（Sony相机案例）的核心：
> **「产品实拍图 + 可灵O3「全能参考」模式 + 科技光效 Prompt」**

无需风格化步骤。直接产品图 + 特效描述 → 可灵O3 生成带光效的视频。
国内用户推荐：**LibTV**（内置可灵O3，还有多角度打光工具）

### LibTV 操作路径（无代码）

```
1. 上传产品图 → 新建图片节点
2. 可选：用「打光」工具调整光源角度/颜色
3. 可选：用「多角度」工具生成不同视角
4. 连线到视频节点 → 选「全能参考」模式
5. 模型选：可灵O3
6. 输入特效 Prompt（见下方）
7. 生成 5 秒视频
8. 多镜头后在剪映拼接
```

### 产品特效 Prompt 模板库

**蓝色科技圆环（相机/圆形产品）：**
```
cinematic product reveal, glowing cyan-blue energy ring orbiting the lens,
holographic UI elements floating around the camera,
technical specs text appearing in air: "[产品名]", "[规格1]", "[规格2]",
volumetric light beams from the lens, particle trails, dark studio bokeh background,
premium commercial TVC aesthetic, slow heroic rotation
```

**金色高端光晕（手表/奢品）：**
```
luxury product showcase, warm golden light particles orbiting elegantly,
soft deep bokeh background, dramatic single key light,
brand name "[品牌名]" appearing in elegant serif typography,
subtle god rays through darkness, slow reverent rotation,
premium watchmaking photography aesthetic
```

**数字能量爆发（手机/耳机/电子）：**
```
tech product launch reveal, electric energy explosion radiating outward,
holographic data streams flowing across the surface,
Matrix-style digital rain in [产品主色] tone,
product floating in dark void, technical spec callouts appearing,
promotional launch film quality, dramatic lighting
```

**Apple 极简品牌：**
```
minimalist product shot, pure white or soft grey background,
single precise key light with controlled shadow,
product name "[产品名]" appearing in clean Helvetica sans-serif,
ultra-slow rotation with perfect chrome reflections,
Apple-style product film aesthetic, quiet and precise motion
```

### fal.ai API 版本

```javascript
const result = await fal.subscribe("fal-ai/kling-video/o3/standard/image-to-video", {
  input: {
    image_url: "PRODUCT_IMAGE_URL",
    prompt: productFXPrompt,
    duration: "5",
    aspect_ratio: "16:9",   // 横版广告
    cfg_scale: 0.35         // 给模型更多创意空间生成光效
  }
});
// 费用：约 $0.42/5秒片段
```

---

## 流派C：LibTV 叙事 TVC

适合有故事性、多角色、多场景的完整作品。

### OpenClaw 接入 LibTV（重要！）

LibTV 有官方 Skill 包，可直接被 OpenClaw 调用：
- GitHub: `github.com/libtv-labs/libtv-skills`
- 安装后可用自然语言一句话驱动 LibTV 完成从剧本到成片全流程

**LibTV 标准工作流：**
```
① 脚本节点：输入主题 → 自动生成分镜脚本（景别/运镜/情绪15字段）
② 25宫格分镜：批量生成多角度关键帧，抽卡选最佳
③ 精修：打光/多角度/扩图/重绘
④ 逐镜头生视频（可灵O3 / Wan 2.6 / Seedance 1.5 按场景选）
⑤ 画面延展：前3秒/后5秒推演，自动补全过渡
⑥ 音频节点：生成背景音乐
⑦ 剪映/PR 最终拼接输出
```

**模型选择指南：**
- 可灵O3：声画同出，主体一致性强，旗舰首选
- Wan 2.6：成本最低，开源稳定，适合大批量
- Seedance 1.5：写实/古风/中文场景更好
- Hailuo 2.3：运动流畅度强

---

## 高级动效参数

### 运镜类型全表
```
推镜 Push In    → "slow push in, zoom toward [subject]"
拉镜 Pull Out   → "slow pull back, revealing wider scene"
平移 Pan        → "slow pan left/right"
摇镜 Tilt       → "slow tilt up/down"
环绕 Orbit      → "slow orbital camera movement around [subject]"
手持 Handheld   → "subtle handheld shake, documentary feel"
航拍 Aerial     → "slow aerial descent from top-down to eye level"
```

### 转场特效词典
```
硬切   → "sharp cut, instant transition"
形变   → "morphing wipe, ink spread reveal, paint brush"
冲击   → "flash cut, white flash, glitch transition"
遮幕   → "iris wipe, diagonal slash, curtain reveal"
流体   → "liquid pour, smoke dissolve, sand particle"
```

### cfg_scale 光效强度
```
0.3-0.4 → 极强光效，模型自由发挥（产品爆款/夸张特效）
0.5     → 适中（标准广告）
0.6-0.7 → 保守贴近Prompt（艺术旅拍/写实）
```

---

## 费用速查

| 操作 | 工具 | 单价 |
|------|------|------|
| 风格化图（1MP） | fal.ai FLUX+LoRA | ~$0.04-0.075 |
| 5秒视频（Ken Burns/特效） | fal.ai 可灵O3 | ~$0.42 |
| 5秒视频 | LibTV 可灵O3 | 订阅制，极低 |

---

## 参考文件索引

- `references/prompt-library.md` — 完整Prompt模板库
- `references/lora-sources.md` — LoRA获取与训练指南
- `references/ffmpeg-commands.md` — 视频拼接命令
- `references/libtv-workflow.md` — LibTV详细手册与OpenClaw接入
