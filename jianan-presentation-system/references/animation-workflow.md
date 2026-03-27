# Animation Workflow for Presentations

## 三种动画产出类型速判

| 类型 | 适用场景 | 最终嵌入方式 |
|------|---------|------------|
| **Manim 3D动画** | 架构数据流、系统层级、抽象概念演示 | 渲染MP4 → 转GIF → 嵌入PPT |
| **HTML CSS动画** | 节点关系图、粒子流动、交互式展示 | 浏览器截图/录屏 → GIF → 嵌入PPT |
| **静态图（PPTX原生）** | 流程图、漫画/对比图、简单架构 | 直接在PPTX中绘制 |

**决策规则：**
- 有数据流动感、层级穿越感 → **Manim**
- 节点之间有粒子连线、循环动效 → **HTML**
- 只需要清晰布局、无动效 → **PPTX原生**

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

## 动画制作触发词

以下需求需启动此动画工作流：

- 「帮我做一个架构动画」
- 「把这个流程做成动图」
- 「参考这个HTML，帮我做类似效果」
- 「我要嵌入GIF到PPT」
- 「做一个数据流动画」
- 「三层架构可视化」
- 「做粒子流动效果」
- 「帮我渲染Manim」
