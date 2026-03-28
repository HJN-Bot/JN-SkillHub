# Animation Workflow for Presentations

## Layer 3 动图能力总览

动图分两大类：**静态数据可视化**（看数据/结构）和**动态流程动效**（看流转/过程）。

```
Layer 3 动图
├── 静态数据可视化（PPTX 原生 / HTML 截图）
│   ├── 图表类：柱状图、折线图、饼图、散点图
│   ├── 甘特图 / 时间轴
│   ├── 对比表格 / 热力表
│   └── KPI 仪表盘
│
└── 动态流程动效（GIF 嵌入 PPT）
    ├── HTML/CSS 节点流（粒子沿路径流动，循环动效）
    └── Manim 3D（架构层级穿越，数据包流动，3D 场景）
```

## 五种产出类型速判

| 类型 | 适用场景 | 工具 | 最终形式 |
|------|---------|------|---------|
| **PPTX 原生图表** | 柱图/折线/饼图/散点，数据可修改 | pptxgenjs `addChart()` | PPTX 原生，可编辑 |
| **PPTX 原生甘特** | 项目时间轴，季度计划 | pptxgenjs 矩形组合 | PPTX 原生，可编辑 |
| **HTML 静态截图** | 复杂表格、对比图、无动效框图 | HTML+CSS → 截图 | 图片嵌入 PPTX |
| **HTML/CSS 动效 GIF** | 节点流动、循环流程、粒子连线 | HTML offset-path → GIF | GIF 嵌入 PPTX |
| **Manim 3D 动效 GIF** | 架构数据流、3D 层级、抽象概念 | Manim ThreeDScene → GIF | GIF 嵌入 PPTX |

**决策树（含环境降级）：**
```
需要动效？
├── 否 → 数据图表用 pptxgenjs 原生；复杂布局用 HTML 截图
└── 是 →
    ├── 节点网络 / 循环流程 / 粒子连线
    │   → HTML/CSS GIF（只需浏览器 + QuickTime 或 Puppeteer）
    │
    └── 架构层级 / 数据穿越 / 3D 场景
        ├── 有 Manim 环境 → Manim GIF（最佳效果）
        └── 没有 Manim   → HTML/CSS 平面替代方案（见下方降级模板）
```

### Manim 降级：用 HTML/CSS 替代 3D 架构动画

当没有 Manim 环境时，用这个 HTML 方案替代三层架构流动效果：
- 三个垂直排列的节点卡片（HAND / BRAIN / UI）
- SVG 虚线连接 + offset-path 粒子流动
- 节点接收数据时 pulse 动效
- 参考：[html-animation-guide.md](html-animation-guide.md) 三节点模板，颜色改为 `#38bdf8 / #c084fc / #34d399`

---

## 类型A：Manim 3D架构动画

### 典型场景
- AI系统三层架构（如HAND/BRAIN/UI Layer数据穿越流动）
- 数据包从输入到输出的旅程
- 模型层级、管道可视化

### 标准项目结构

```
project/
  main.py              # 主场景文件
  final_main.py        # 最终渲染版本
  utils/
    colors.py          # 统一色彩配置
  media/               # Manim自动生成的渲染产物
    images/
    videos/
```

### 色彩配置模板（utils/colors.py）

```python
# CER/项目专属配色 - 根据项目替换
from manim import *

BG_COLOR = "#0d1117"         # 深色背景
HAND_COLOR = "#3b82f6"       # 蓝 - 数据处理层
BRAIN_COLOR = "#f59e0b"      # 金 - 分析/AI层
UI_COLOR = "#10b981"         # 绿 - 界面/输出层
PIPE_COLOR = "#60a5fa"       # 管道色
HIGHLIGHT_COLOR = "#fbbf24"  # 数据包高亮
TEXT_COLOR = "#e2e8f0"       # 主文字
```

### 3D架构场景模板

```python
from manim import *
from utils.colors import *

class ArchitectureFlow(ThreeDScene):
    """
    三层架构数据流动画模板
    适配：AI系统/产品架构的Pitch演示
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        # 视角：稍微俯视，偏左前方，营造立体感
        self.set_camera_orientation(
            phi=55 * DEGREES,
            theta=-30 * DEGREES,
            zoom=0.8
        )

        self.create_layers()
        self.create_pipeline()
        self.animate_data_flow()
        self.wait(2)

    def create_layers(self):
        """三层Prism结构，依次展现"""
        # 层A（顶层）- 宽度最大
        self.layer_a = Prism(
            dimensions=[6, 1.8, 2.8],
            fill_color=HAND_COLOR,
            fill_opacity=0.25,
            stroke_color=HAND_COLOR,
            stroke_width=3
        ).move_to(UP * 2.5 + IN * 0.3)

        label_a = Text("LAYER A\nData Processing",
                      font_size=20, color=TEXT_COLOR)
        label_a.next_to(self.layer_a, IN * 2.5, buff=0.2)
        self.group_a = VGroup(self.layer_a, label_a)

        # 层B（中层）
        self.layer_b = Prism(
            dimensions=[6.2, 1.8, 2.8],
            fill_color=BRAIN_COLOR,
            fill_opacity=0.25,
            stroke_color=BRAIN_COLOR,
            stroke_width=3
        ).move_to(ORIGIN)

        label_b = Text("LAYER B\nAI Analysis",
                      font_size=20, color=TEXT_COLOR)
        label_b.next_to(self.layer_b, IN * 2.5, buff=0.2)
        self.group_b = VGroup(self.layer_b, label_b)

        # 层C（底层）
        self.layer_c = Prism(
            dimensions=[6.4, 1.8, 2.8],
            fill_color=UI_COLOR,
            fill_opacity=0.25,
            stroke_color=UI_COLOR,
            stroke_width=3
        ).move_to(DOWN * 2.5 - IN * 0.3)

        label_c = Text("LAYER C\nUI & Export",
                      font_size=20, color=TEXT_COLOR)
        label_c.next_to(self.layer_c, IN * 2.5, buff=0.2)
        self.group_c = VGroup(self.layer_c, label_c)

    def create_pipeline(self):
        """中心数据管道（外层发光 + 内核流动球）"""
        outer = Cylinder(
            radius=0.35, height=7.5,
            fill_color=PIPE_COLOR, fill_opacity=0.1,
            stroke_color=PIPE_COLOR, stroke_width=2
        ).rotate(PI/2, axis=RIGHT)

        inner = Cylinder(
            radius=0.25, height=7.3,
            fill_color=PIPE_COLOR, fill_opacity=0.3,
            stroke_color=WHITE, stroke_width=2
        ).rotate(PI/2, axis=RIGHT)

        self.pipeline = VGroup(outer, inner)

    def animate_data_flow(self):
        """数据流全程动画"""
        # 管道先出现
        self.play(FadeIn(self.pipeline), run_time=1.2)

        # 三层依次从上到下出现
        self.play(FadeIn(self.group_a, shift=UP*0.3), run_time=0.8)
        self.play(FadeIn(self.group_b, shift=UP*0.2), run_time=0.8)
        self.play(FadeIn(self.group_c, shift=UP*0.1), run_time=0.6)
        self.wait(0.5)

        # 数据包从顶部进入，逐层处理
        packet = Square(
            side_length=0.25,
            fill_color=HIGHLIGHT_COLOR,
            fill_opacity=0.9,
            stroke_color=WHITE,
            stroke_width=2
        ).move_to(UP * 4)

        self.play(FadeIn(packet))

        # 穿越Layer A
        self.play(
            self.layer_a.animate.set_fill(HAND_COLOR, opacity=0.6),
            packet.animate.move_to(self.layer_a.get_bottom()),
            run_time=1.0
        )
        self.play(
            self.layer_a.animate.set_fill(HAND_COLOR, opacity=0.25),
            run_time=0.4
        )

        # 穿越Layer B
        self.play(
            self.layer_b.animate.set_fill(BRAIN_COLOR, opacity=0.6),
            packet.animate.move_to(self.layer_b.get_bottom()),
            run_time=1.0
        )
        self.play(
            self.layer_b.animate.set_fill(BRAIN_COLOR, opacity=0.25),
            run_time=0.4
        )

        # 穿越Layer C并输出
        self.play(
            self.layer_c.animate.set_fill(UI_COLOR, opacity=0.6),
            packet.animate.move_to(self.layer_c.get_bottom() + DOWN * 0.8),
            run_time=1.0
        )

        output_label = Text("OUTPUT", font_size=18, color=UI_COLOR)
        output_label.next_to(packet, DOWN, buff=0.2)
        self.play(FadeIn(output_label))
        self.wait(1)
```

### 渲染命令

```bash
# 低质量预览（开发调试用）
manim -pql main.py ArchitectureFlow

# 高质量1080p（最终渲染）
manim -pqh final_main.py FinalCERWorkflow

# 输出到指定目录
manim -pqh main.py ArchitectureFlow --media_dir ./output/
```

---

## 类型B：HTML CSS动画

### 典型场景
- 节点关系图（圆角矩形 + SVG连线 + 粒子流动）
- 循环数据流（UI → Brain → Hand → UI 闭环）
- 需要嵌入浏览器展示或截图入PPT的静态动效图

### 核心技术模式（来自CER项目实战）

**1. SVG offset-path粒子动画**（节点间流动效果）

```css
/* 粒子沿SVG路径流动 */
.dot {
    position: absolute;
    width: 10px; height: 10px;
    border-radius: 50%;
    offset-rotate: auto;
}

.dot-a-to-b {
    background: #10b981;
    /* 路径：从节点A中心 → 节点B中心（贝塞尔曲线） */
    offset-path: path("M 310 860 Q 340 700 475 650");
    animation: flow 2s linear infinite;
}

@keyframes flow {
    0%   { offset-distance: 0%;   opacity: 0; }
    15%  { opacity: 1; }
    85%  { opacity: 1; }
    100% { offset-distance: 100%; opacity: 0; }
}
```

**2. 文件/数据块下落动画**

```css
.files-drop {
    position: absolute;
    opacity: 0;
    animation: dropFiles 2s infinite;
}

@keyframes dropFiles {
    0%   { top: 50px;  opacity: 0; }
    20%  { opacity: 1; }
    90%  { opacity: 1; }
    100% { top: 80px;  opacity: 0; }
}
```

**3. 节点标准样式**

```css
.node {
    position: absolute;
    background: white;
    border: 2px solid;
    border-radius: 14px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.05);
    padding: 15px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
}

.node-title {
    font-size: 22px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 8px;
}
```

### 布局坐标系规范

```
固定画布尺寸：950px × 1100px（竖版，适合PPT嵌图）
中心轴 X = 475px

常用节点位置：
  顶部中央：  left: 50%, transform: translateX(-50%), top: 80px
  中部中央：  left: 50%, transform: translateX(-50%), top: 260px
  底部左：    left: 180px, top: 860px  (width 260px)
  底部右：    left: 510px, top: 860px  (width 260px)
  中心菱形：  left: 50%, transform: translateX(-50%), top: 530px
              + inner rotate(45deg)

SVG连线路径（Center X=475 规则）：
  顶→中：  M 475 190 L 475 260
  中→菱形：M 475 390 L 475 520
  左底→菱形：M 310 860 Q 340 700 475 650
  菱形→右底：M 520 650 Q 640 700 680 860
```

### 色彩规范（与PPT一致）

```css
:root {
    --ui-color:   #10b981;   /* 绿 - UI层 */
    --hand-color: #3b82f6;   /* 蓝 - 处理层 */
    --brain-color:#f59e0b;   /* 金 - AI层 */
    --text-main:  #1f2937;   /* 主文字 */
    --bg-color:   #ffffff;   /* 白色背景（浅色版） */
}
```

---

## GIF导出工作流

### 方法1：Manim MP4 → GIF（推荐，质量最好）

```bash
# Step 1: 渲染为MP4
manim -pqh scene.py SceneName

# Step 2: 用FFmpeg转GIF（带抖动算法，色彩更准）
ffmpeg -i input.mp4 \
  -vf "fps=15,scale=960:-1:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors=128[p];[s1][p]paletteuse=dither=bayer" \
  -loop 0 \
  output.gif

# Step 3: 压缩GIF大小（可选）
ffmpeg -i output.gif -vf "scale=720:-1" output_compressed.gif
```

### 方法2：HTML动画 → GIF（Puppeteer录屏）

```bash
# 安装依赖
npm install puppeteer

# 录制脚本（record_gif.js）
const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.setViewport({ width: 950, height: 1100 });
  await page.goto(`file://${__dirname}/animation.html`);

  // 截图序列（每帧间隔50ms = 20fps）
  const frames = [];
  for (let i = 0; i < 60; i++) {  // 60帧 = 3秒
    const screenshot = await page.screenshot({ type: 'png' });
    frames.push(screenshot);
    await new Promise(r => setTimeout(r, 50));
  }

  await browser.close();

  // 转GIF（需要 gif-encoder）
  // 或将frames保存为PNG序列后用FFmpeg合成
})();
```

### 方法3：QuickTime + FFmpeg（最简单，macOS）

```bash
# 1. QuickTime → 录制屏幕选区（⌘+Shift+5 → 选定区域录制）
# 2. 保存为 .mov

# 3. mov转GIF
ffmpeg -i recording.mov \
  -vf "fps=15,scale=960:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" \
  -loop 0 \
  output.gif
```

---

## 嵌入PPT规范

### GIF嵌入（推荐：保持动效）

```python
# pptxgenjs（JavaScript/Node.js）
slide.addImage({
    path: './output/animation.gif',
    x: 0.5, y: 1.0,
    w: 5.0, h: 4.0  # 单位：英寸
})

# pptx（Python）
from pptx.util import Inches
pic = slide.shapes.add_picture(
    'output/animation.gif',
    left=Inches(0.5), top=Inches(1.0),
    width=Inches(5.0), height=Inches(4.0)
)
```

### 视频嵌入（MP4，需PowerPoint 2016+）

```python
# pptxgenjs
slide.addMedia({
    type: 'video',
    path: './output/animation.mp4',
    x: 0.5, y: 1.0, w: 8.0, h: 4.5,
    extn: 'mp4'
})
```

### 尺寸规范

| PPT画布 | 宽 | 高 | 嵌图推荐尺寸 |
|---------|----|----|------------|
| 标准宽屏 | 13.3" | 7.5" | 全幅：12"×5.5" / 半幅：6"×5" |
| 动画图（右侧） | — | — | w=6.5", h=5.0" |
| 动画图（全幅） | — | — | w=11", h=5.5", 居中 |

---

## 类型C：静态数据可视化（pptxgenjs 原生图表）

### 原则：能原生就原生，数据必须可修改

所有数据图表优先使用 pptxgenjs `addChart()`，生成 PowerPoint 原生图表对象，用户可在 PPT 中直接修改数据。

### 常用图表类型速查

```javascript
// 柱状图（工作量对比、阶段分布）
slide.addChart(pres.ChartType.bar, [
  { name: '完成', labels: ['Q1','Q2','Q3','Q4'], values: [65,72,80,85] },
  { name: '目标', labels: ['Q1','Q2','Q3','Q4'], values: [70,75,80,90] }
], {
  x: 0.5, y: 1.2, w: 6.0, h: 4.5,
  barDir: 'col',          // 竖柱：col；横柱：bar
  chartColors: ['E87722','009999'],   // 橙+青
  showLegend: true, legendPos: 'b',
  showValue: true, dataLabelFontSize: 11,
});

// 折线图（趋势、准确率变化）
slide.addChart(pres.ChartType.line, dataRows, {
  x: 0.5, y: 1.2, w: 6.0, h: 4.0,
  chartColors: ['E87722'],
  lineSize: 2,
  showMarker: true,
});

// 饼图（占比分布）
slide.addChart(pres.ChartType.pie, [
  { name: '分布', labels: ['A','B','C'], values: [40,35,25] }
], {
  x: 3.5, y: 1.5, w: 4.5, h: 4.5,
  chartColors: ['E87722','009999','1a1a1a'],
  showPercent: true,
});

// 堆叠柱图（工作量构成）
slide.addChart(pres.ChartType.barStacked, dataRows, {
  barGrouping: 'stacked',
  chartColors: ['E87722','009999','888888'],
});
```

### 甘特图（pptxgenjs 矩形组合）

甘特图无原生 Chart 类型，使用 Rounded Rectangle 矩形拼装。这是原生可编辑形状。

```javascript
// 甘特图结构：行标签 + 季度格子 + 彩色进度条
const GANTT_TOP    = 1.5;   // 表格起始 Y
const ROW_H        = 0.45;  // 每行高度
const LABEL_W      = 1.8;   // 左侧标签列宽
const Q_W          = 2.7;   // 每个季度列宽（13.33 - 1.8 - 0.5*2 ≈ 10.8 / 4 = 2.7）
const QUARTERS     = ['Q1','Q2','Q3','Q4'];

// 季度表头
QUARTERS.forEach((q, i) => {
  slide.addShape(pres.ShapeType.rect, {
    x: LABEL_W + i * Q_W, y: GANTT_TOP, w: Q_W, h: ROW_H,
    fill: { color: i % 2 === 0 ? 'E87722' : '009999' },
    line: { color: 'FFFFFF', width: 1 },
  });
  slide.addText(q, {
    x: LABEL_W + i * Q_W, y: GANTT_TOP, w: Q_W, h: ROW_H,
    align: 'center', valign: 'middle',
    bold: true, fontSize: 13, color: 'FFFFFF',
  });
});

// 任务行示例：[任务名, 开始Q(0-based), 跨越Q数, 颜色]
const tasks = [
  ['项目组A - Task 01', 0, 2, 'E87722'],
  ['项目组A - Task 02', 1, 2, 'F5A559'],
  ['项目组B - Task 01', 2, 2, '009999'],
];

tasks.forEach(([label, startQ, spanQ, color], rowIdx) => {
  const y = GANTT_TOP + ROW_H * (rowIdx + 1);
  // 行背景（白/浅灰交替）
  slide.addShape(pres.ShapeType.rect, {
    x: 0.5, y, w: LABEL_W + Q_W * 4, h: ROW_H,
    fill: { color: rowIdx % 2 === 0 ? 'FFFFFF' : 'F9F9F9' },
    line: { color: 'EEEEEE', width: 0.5 },
  });
  // 任务标签
  slide.addText(label, {
    x: 0.5, y, w: LABEL_W - 0.1, h: ROW_H,
    fontSize: 11, valign: 'middle', color: '1a1a1a',
  });
  // 进度条
  slide.addShape(pres.ShapeType.roundRect, {
    x: LABEL_W + startQ * Q_W + 0.1, y: y + 0.07,
    w: Q_W * spanQ - 0.2, h: ROW_H - 0.14,
    rectRadius: 0.05,
    fill: { color },
    line: { color: 'FFFFFF', width: 0.5 },
  });
});
```

---

## 动画制作触发词

以下需求需启动此动画工作流：

- 「帮我做一个架构动画」「把这个流程做成动图」
- 「帮我做甘特图」「项目时间轴」「季度计划图」
- 「帮我做柱状图 / 折线图 / 饼图」「数据可视化」
- 「参考这个HTML，帮我做类似效果」
- 「做粒子流动效果」「节点流转动图」
- 「帮我渲染Manim」「3D架构动画」
