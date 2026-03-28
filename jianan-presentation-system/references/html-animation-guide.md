# HTML/CSS 动图制作指南（Presentation专用）

## 适用场景

- 节点关系图：多个模块/组件之间有数据流动（粒子沿路径流动）
- 循环流程图：A→B→C→A 闭环结构
- 状态切换动效：模块激活/高亮切换
- 不需要 Manim 环境，浏览器直接运行，录屏转 GIF 嵌入 PPT

**与 Manim 的区别：**
| | HTML/CSS | Manim |
|--|---------|-------|
| 适合 | 节点网络、循环流、界面展示 | 层级穿越、数学推导、3D场景 |
| 环境 | 只需浏览器 | 需安装 Python + Manim |
| 修改 | 改 CSS/JS 即可实时预览 | 改完需重新渲染 |
| 输出 | 录屏→GIF | 渲染→MP4→GIF |

---

## 画布尺寸规范（与PPT对齐）

```
竖版（适合流程图、架构图）：950px × 1100px
横版（适合全幅插图）：       1280px × 720px
PPT 嵌入推荐尺寸：           6" × 5"（竖）/ 10" × 5.6"（横）
```

---

## 完整 HTML 动图模板

以下是一个可直接运行的三节点数据流动图模板，基于 CER 项目实战经验提炼。

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Flow Diagram</title>
  <style>
    /* ── 全局 ──────────────────────────────────── */
    :root {
      --color-a: #3b82f6;   /* 节点A：蓝 */
      --color-b: #f59e0b;   /* 节点B：金 */
      --color-c: #10b981;   /* 节点C：绿 */
      --bg:      #ffffff;
      --text:    #1f2937;
      --dim:     #6b7280;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      width: 950px;
      height: 1100px;
      background: var(--bg);
      font-family: 'Segoe UI', -apple-system, sans-serif;
      overflow: hidden;
      display: flex;
      justify-content: center;
      align-items: center;
    }

    /* ── SVG 连线层（在节点之下） ────────────────── */
    .svg-layer {
      position: absolute;
      top: 0; left: 0;
      width: 950px; height: 1100px;
      z-index: 0;
      pointer-events: none;
    }

    /* ── 节点卡片 ────────────────────────────────── */
    .node {
      position: absolute;
      width: 260px;
      background: white;
      border: 2px solid;
      border-radius: 14px;
      padding: 18px 20px;
      z-index: 10;
      box-shadow: 0 8px 24px rgba(0,0,0,0.06);
      text-align: center;
    }

    .node-title {
      font-size: 20px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 6px;
    }

    .node-desc {
      font-size: 13px;
      color: var(--dim);
      line-height: 1.5;
    }

    /* 三个节点位置（中心轴 X=475） */
    .node-a {
      top: 120px;
      left: 50%; transform: translateX(-50%);
      border-color: var(--color-a);
      height: 110px;
    }
    .node-a .node-title { color: var(--color-a); }

    .node-b {
      top: 480px;
      left: 50%; transform: translateX(-50%);
      border-color: var(--color-b);
      height: 130px;
    }
    .node-b .node-title { color: var(--color-b); }

    .node-c {
      top: 860px;
      left: 50%; transform: translateX(-50%);
      border-color: var(--color-c);
      height: 110px;
    }
    .node-c .node-title { color: var(--color-c); }

    /* ── 粒子（沿 SVG 路径流动） ────────────────── */
    .particle {
      position: absolute;
      width: 10px; height: 10px;
      border-radius: 50%;
      z-index: 20;
      offset-rotate: auto;
    }

    /* A → B */
    .p-a-b {
      background: var(--color-a);
      offset-path: path("M 475 230 L 475 480");
      animation: flow 1.8s ease-in-out infinite;
    }

    /* B → C */
    .p-b-c {
      background: var(--color-b);
      offset-path: path("M 475 610 L 475 860");
      animation: flow 1.8s ease-in-out infinite 0.6s;
    }

    /* C → A（回流，走左侧弧线） */
    .p-c-a {
      background: var(--color-c);
      offset-path: path("M 345 905 Q 160 550 345 175");
      animation: flow 2.4s ease-in-out infinite 1.2s;
    }

    @keyframes flow {
      0%   { offset-distance: 0%;   opacity: 0; }
      15%  { opacity: 1; }
      85%  { opacity: 1; }
      100% { offset-distance: 100%; opacity: 0; }
    }

    /* ── 节点激活脉冲（可选） ────────────────────── */
    @keyframes pulse-a {
      0%, 100% { box-shadow: 0 8px 24px rgba(0,0,0,0.06); }
      50%       { box-shadow: 0 0 0 6px rgba(59,130,246,0.15), 0 8px 24px rgba(0,0,0,0.06); }
    }
    @keyframes pulse-b {
      0%, 100% { box-shadow: 0 8px 24px rgba(0,0,0,0.06); }
      50%       { box-shadow: 0 0 0 6px rgba(245,158,11,0.15), 0 8px 24px rgba(0,0,0,0.06); }
    }
    @keyframes pulse-c {
      0%, 100% { box-shadow: 0 8px 24px rgba(0,0,0,0.06); }
      50%       { box-shadow: 0 0 0 6px rgba(16,185,129,0.15), 0 8px 24px rgba(0,0,0,0.06); }
    }
    .node-a { animation: pulse-a 3.6s ease-in-out infinite; }
    .node-b { animation: pulse-b 3.6s ease-in-out infinite 1.2s; }
    .node-c { animation: pulse-c 3.6s ease-in-out infinite 2.4s; }

  </style>
</head>
<body>

  <!-- SVG 连线 -->
  <svg class="svg-layer" viewBox="0 0 950 1100">
    <!-- A → B 直线 -->
    <line x1="475" y1="230" x2="475" y2="480"
          stroke="#3b82f6" stroke-width="1.5" stroke-opacity="0.3"
          stroke-dasharray="6 4"/>
    <!-- B → C 直线 -->
    <line x1="475" y1="610" x2="475" y2="860"
          stroke="#f59e0b" stroke-width="1.5" stroke-opacity="0.3"
          stroke-dasharray="6 4"/>
    <!-- C → A 回流弧线 -->
    <path d="M 345 905 Q 160 550 345 175"
          fill="none" stroke="#10b981" stroke-width="1.5"
          stroke-opacity="0.25" stroke-dasharray="6 4"/>
    <!-- 箭头定义 -->
    <defs>
      <marker id="arr-blue" markerWidth="8" markerHeight="8"
              refX="6" refY="3" orient="auto">
        <path d="M0,0 L0,6 L8,3 z" fill="#3b82f6" opacity="0.5"/>
      </marker>
      <marker id="arr-gold" markerWidth="8" markerHeight="8"
              refX="6" refY="3" orient="auto">
        <path d="M0,0 L0,6 L8,3 z" fill="#f59e0b" opacity="0.5"/>
      </marker>
    </defs>
    <line x1="475" y1="230" x2="475" y2="476"
          stroke="transparent" marker-end="url(#arr-blue)"/>
    <line x1="475" y1="610" x2="475" y2="856"
          stroke="transparent" marker-end="url(#arr-gold)"/>
  </svg>

  <!-- 节点 A -->
  <div class="node node-a">
    <div class="node-title">Node A</div>
    <div class="node-desc">Data Input & Extraction</div>
  </div>

  <!-- 节点 B -->
  <div class="node node-b">
    <div class="node-title">Node B</div>
    <div class="node-desc">Processing & Analysis</div>
  </div>

  <!-- 节点 C -->
  <div class="node node-c">
    <div class="node-title">Node C</div>
    <div class="node-desc">Output & Export</div>
  </div>

  <!-- 粒子 -->
  <div class="particle p-a-b"></div>
  <div class="particle p-b-c"></div>
  <div class="particle p-c-a"></div>

</body>
</html>
```

---

## 定制化指南

### 修改节点数量

**两节点**（左右并排）：
```css
.node-left  { top: 500px; left: 150px; width: 260px; }
.node-right { top: 500px; left: 540px; width: 260px; }
/* 粒子路径：左→右 */
.p-lr { offset-path: path("M 410 550 L 540 550"); }
/* 粒子路径：右→左（回流） */
.p-rl { offset-path: path("M 540 580 L 410 580"); animation-delay: 1s; }
```

**四节点**（菱形布局）：
```
中心轴 X=475
  上：475, 100
  左：215, 530
  右：735, 530
  下：475, 960
```

### 修改颜色（与PPT配色对齐）

直接改 `:root` 里的变量：
```css
:root {
  --color-a: #E87722;   /* Jianan PPT橙 */
  --color-b: #009999;   /* Jianan PPT深青 */
  --color-c: #1a1a1a;   /* 深色 */
}
```

### 深色背景版本

```css
:root {
  --bg:   #04070d;
  --text: #f1f5f9;
  --dim:  #64748b;
}
/* 节点背景同步改 */
.node { background: #0d1117; }
```

---

## HTML → GIF 录制流程

### 方法1：QuickTime（macOS，最快）

```bash
# 1. 用 Chrome 打开 HTML 文件，调整窗口到正好 950×1100
# 2. ⌘+Shift+5 → 选区录制（只框住画布区域）
# 3. 录制 5-10 秒（至少两个完整动画循环）
# 4. 保存为 .mov，然后转 GIF：

ffmpeg -i recording.mov \
  -vf "fps=20,scale=960:-1:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors=128[p];[s1][p]paletteuse=dither=bayer" \
  -loop 0 \
  output.gif
```

### 方法2：Puppeteer 自动录制（精确，无需手动）

```bash
npm install puppeteer gifski  # 一次性安装
```

```javascript
// record_html_gif.js
const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

async function recordHtmlToFrames(htmlFile, outputDir, durationMs = 5000, fps = 20) {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();

  // 设置画布尺寸（竖版）
  await page.setViewport({ width: 950, height: 1100, deviceScaleFactor: 1 });
  await page.goto(`file://${path.resolve(htmlFile)}`);

  // 等动画稳定
  await new Promise(r => setTimeout(r, 500));

  fs.mkdirSync(outputDir, { recursive: true });
  const interval = 1000 / fps;
  const frameCount = Math.round(durationMs / interval);

  for (let i = 0; i < frameCount; i++) {
    await page.screenshot({
      path: path.join(outputDir, `frame_${String(i).padStart(4, '0')}.png`)
    });
    await new Promise(r => setTimeout(r, interval));
  }

  await browser.close();
  console.log(`✅ ${frameCount} frames saved to ${outputDir}`);
}

recordHtmlToFrames('./diagram.html', './frames', 5000, 20);
```

```bash
# 运行录制
node record_html_gif.js

# 用 FFmpeg 合成 GIF（高质量调色板方式）
ffmpeg -framerate 20 -i frames/frame_%04d.png \
  -vf "scale=960:-1:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors=128[p];[s1][p]paletteuse=dither=bayer" \
  -loop 0 \
  output.gif
```

### GIF 压缩（上传/嵌入前）

```bash
# 降低帧率到 15fps（减小文件体积）
ffmpeg -i output.gif -vf "fps=15" -loop 0 output_compressed.gif

# 缩小尺寸（PPT嵌入用 720px 宽即可）
ffmpeg -i output.gif -vf "scale=720:-1" -loop 0 output_720.gif
```

---

## 嵌入 PPT 规范

```python
# pptxgenjs（推荐，保持GIF动效）
slide.addImage({
    path: './output.gif',
    x: 3.5,    # 英寸，距左边距
    y: 0.8,
    w: 5.5,    # 宽度
    h: 6.3     # 竖版比例 950/1100 ≈ 0.86，w*1.16
})
```

**尺寸对应表（PPT 13.3" × 7.5" 画布）：**

| GIF来源 | 建议PPT尺寸 | 建议位置 |
|---------|-----------|---------|
| 竖版 950×1100 | w=4.5", h=5.2" | 右半幅 |
| 横版 1280×720 | w=10.5", h=5.9" | 全幅居中 |
| 正方形 800×800 | w=4.5", h=4.5" | 右侧留白 |

---

## 触发词

以下需求启动 HTML 动图工作流：
- 「帮我做一个流程动图」
- 「节点之间有数据流动的图」
- 「做个循环流程的 GIF」
- 「参考这个 HTML，帮我做类似的」
- 「把这个架构图做成动图」
- 「做个能嵌进 PPT 的 GIF」
