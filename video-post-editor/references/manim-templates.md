# Manim 解析动画模板库

## 模板索引

| 编号 | 类型 | 适用场景 |
|------|------|---------|
| T1 | 概念拆解 | 展示某个功能/组件的内部逻辑 |
| T2 | 流程图/架构图 | 系统流程、数据流向、模块关系 |
| T3 | 对比展示 | Before/After，两种方案对比 |
| T4 | 公式/数学推导 | 算法解析、数学概念 |
| T5 | 数据可视化 | 图表、进度、增长趋势 |
| T6 | 高亮+标注 | 配合视频截图，解释界面元素 |
| T7 | 时间轴 | 事件序列、步骤演示 |

---

## 全局样式配置

```python
# style_config.py - 所有模板共用
DARK_BG = "#0d1117"       # GitHub深色背景
ACCENT = "#58a6ff"         # 强调蓝
WHITE = "#e6edf3"          # 主文字色
GRAY = "#8b949e"           # 次要文字
GREEN = "#3fb950"          # 成功/正向
RED = "#f85149"            # 错误/负向
YELLOW = "#d29922"         # 警告/标注

FONT_CN = "PingFang SC"    # 中文字体
FONT_EN = "SF Pro Display" # 英文字体（macOS）

TITLE_SIZE = 0.7
BODY_SIZE = 0.5
CAPTION_SIZE = 0.4
```

---

## T1：概念拆解动画

```python
from manim import *

class ConceptBreakdown(Scene):
    """
    用途：把一个复杂概念拆成几个组成部分，逐一展示
    适合：解释AI产品功能、技术架构、用户流程
    """
    def construct(self):
        self.camera.background_color = "#0d1117"

        # 主标题
        title = Text("核心概念", font="PingFang SC",
                     color="#e6edf3").scale(0.7)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title, shift=DOWN*0.3))
        self.wait(0.5)

        # 三个组成部分（可调整数量）
        parts = [
            ("① 数据输入", "#58a6ff", "用户提供原始视频和描述"),
            ("② AI 理解", "#3fb950", "分析内容，识别关键片段"),
            ("③ 生成输出", "#d29922", "字幕、标注、动画合成输出"),
        ]

        boxes = VGroup()
        for i, (label, color, desc) in enumerate(parts):
            # 框
            rect = RoundedRectangle(
                corner_radius=0.15,
                width=3.5, height=1.8,
                color=color, fill_opacity=0.1,
                stroke_width=2
            )
            # 标签
            label_text = Text(label, font="PingFang SC",
                              color=color).scale(0.5)
            label_text.move_to(rect).shift(UP*0.35)
            # 描述
            desc_text = Text(desc, font="PingFang SC",
                             color="#8b949e").scale(0.35)
            desc_text.move_to(rect).shift(DOWN*0.3)

            group = VGroup(rect, label_text, desc_text)
            boxes.add(group)

        boxes.arrange(RIGHT, buff=0.4)
        boxes.next_to(title, DOWN, buff=0.8)

        # 逐个出现
        for box in boxes:
            self.play(FadeIn(box, shift=UP*0.2), run_time=0.6)
            self.wait(0.3)

        # 连接箭头
        arrows = VGroup()
        for i in range(len(boxes)-1):
            arrow = Arrow(
                boxes[i].get_right(),
                boxes[i+1].get_left(),
                buff=0.1,
                color="#8b949e",
                stroke_width=2,
                max_tip_length_to_length_ratio=0.15
            )
            arrows.add(arrow)

        self.play(Create(arrows), run_time=0.5)
        self.wait(2)
```

---

## T2：流程图/架构图

```python
from manim import *

class FlowDiagram(Scene):
    """
    用途：展示数据流向或系统架构
    适合：技术讲解、产品Demo中的后台逻辑
    """
    def construct(self):
        self.camera.background_color = "#0d1117"

        # 节点定义
        nodes_data = [
            ("用户输入", "#58a6ff"),
            ("处理层", "#3fb950"),
            ("输出结果", "#d29922"),
        ]

        nodes = VGroup()
        for label, color in nodes_data:
            rect = RoundedRectangle(
                corner_radius=0.2,
                width=2.5, height=1.0,
                color=color, fill_opacity=0.15,
                stroke_width=2
            )
            text = Text(label, font="PingFang SC", color=color).scale(0.45)
            text.move_to(rect)
            nodes.add(VGroup(rect, text))

        nodes.arrange(DOWN, buff=0.8)
        nodes.center()

        # 逐个出现
        for node in nodes:
            self.play(Create(node[0]), Write(node[1]), run_time=0.5)
            self.wait(0.2)

        # 连接线
        for i in range(len(nodes)-1):
            arrow = Arrow(
                nodes[i].get_bottom(),
                nodes[i+1].get_top(),
                buff=0.1,
                color="#8b949e",
                stroke_width=2
            )
            label = Text("→", color="#8b949e").scale(0.4)
            self.play(Create(arrow), run_time=0.4)

        self.wait(2)
```

---

## T3：对比展示（Before / After）

```python
from manim import *

class BeforeAfterComparison(Scene):
    """
    用途：左右对比两种方案
    适合：产品改进展示、功能对比
    """
    def construct(self):
        self.camera.background_color = "#0d1117"

        # 分隔线
        divider = Line(UP*3, DOWN*3, color="#30363d", stroke_width=1)
        self.play(Create(divider))

        # Before（左侧）
        before_title = Text("Before", font="SF Pro Display",
                            color="#f85149").scale(0.6)
        before_title.to_edge(LEFT, buff=1.5).to_edge(UP, buff=0.8)

        before_items = VGroup(*[
            Text(f"• {item}", font="PingFang SC",
                 color="#8b949e").scale(0.4)
            for item in ["手动操作", "效率低", "容易出错"]
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        before_items.next_to(before_title, DOWN, buff=0.4, aligned_edge=LEFT)

        # After（右侧）
        after_title = Text("After", font="SF Pro Display",
                           color="#3fb950").scale(0.6)
        after_title.to_edge(RIGHT, buff=1.5).to_edge(UP, buff=0.8)

        after_items = VGroup(*[
            Text(f"✓ {item}", font="PingFang SC",
                 color="#3fb950").scale(0.4)
            for item in ["自动化处理", "10x 效率", "零错误率"]
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        after_items.next_to(after_title, DOWN, buff=0.4, aligned_edge=LEFT)

        self.play(
            FadeIn(before_title), FadeIn(after_title),
            run_time=0.5
        )
        for b, a in zip(before_items, after_items):
            self.play(FadeIn(b, shift=RIGHT*0.2),
                      FadeIn(a, shift=LEFT*0.2), run_time=0.4)
            self.wait(0.2)

        self.wait(2)
```

---

## T4：公式/数学推导

```python
from manim import *

class FormulaExplainer(Scene):
    """
    用途：展示公式或算法推导过程
    适合：AI模型解释、数据分析方法说明
    """
    def construct(self):
        self.camera.background_color = "#0d1117"

        # 初始公式
        formula = MathTex(
            r"y = \sigma\left(\sum_{i} w_i x_i + b\right)",
            color="#e6edf3"
        ).scale(1.2)

        label = Text("神经元激活函数", font="PingFang SC",
                     color="#8b949e").scale(0.45)
        label.next_to(formula, DOWN, buff=0.4)

        self.play(Write(formula), run_time=1.5)
        self.play(FadeIn(label))
        self.wait(1)

        # 高亮各部分
        self.play(formula.animate.set_color_by_tex(r"\sigma", "#58a6ff"))
        sigma_note = Text("激活函数（如ReLU）", font="PingFang SC",
                          color="#58a6ff").scale(0.35)
        sigma_note.next_to(formula, UP, buff=0.3)
        self.play(FadeIn(sigma_note))
        self.wait(0.8)

        self.play(formula.animate.set_color_by_tex("w", "#3fb950"))
        self.wait(2)
```

---

## T5：数据可视化

```python
from manim import *

class DataVisualization(Scene):
    """
    用途：展示数据、指标、对比图表
    适合：效果展示、ROI说明
    """
    def construct(self):
        self.camera.background_color = "#0d1117"

        title = Text("性能对比", font="PingFang SC",
                     color="#e6edf3").scale(0.65)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # 条形图
        chart = BarChart(
            values=[30, 75, 90],
            bar_names=["方案A", "方案B", "我们的方案"],
            y_range=[0, 100, 20],
            y_length=4,
            x_length=7,
            bar_colors=["#8b949e", "#58a6ff", "#3fb950"],
        )
        chart.center().shift(DOWN*0.3)

        self.play(Create(chart), run_time=1.5)
        self.wait(2)
```

---

## T6：界面截图标注动画

```python
from manim import *

class ScreenAnnotation(Scene):
    """
    用途：对产品截图进行动态标注说明
    适合：Demo视频、功能讲解
    注意：需要提前截图并放到 ./assets/ 目录
    """
    def construct(self):
        self.camera.background_color = "#0d1117"

        # 加载截图（替换为实际路径）
        screenshot = ImageMobject("./assets/screenshot.png")
        screenshot.scale(0.7).center()
        self.play(FadeIn(screenshot))
        self.wait(0.5)

        # 标注框（坐标需根据实际截图调整）
        # Manim坐标系：屏幕中心为(0,0)，单位是"Manim单位"
        annotation_box = Rectangle(
            width=2.5, height=1.5,
            color=WHITE,
            stroke_width=3,
            fill_opacity=0
        ).move_to(RIGHT*1.5 + UP*0.5)

        annotation_text = Text("关键功能区域",
                               font="PingFang SC",
                               color=WHITE).scale(0.4)
        annotation_text.next_to(annotation_box, UP, buff=0.15)

        self.play(
            Create(annotation_box),
            FadeIn(annotation_text),
            run_time=0.6
        )
        self.wait(1.5)

        # 箭头指向
        arrow = Arrow(
            LEFT*2 + DOWN,
            annotation_box.get_left(),
            color="#58a6ff",
            stroke_width=2.5
        )
        explanation = Text("点击后触发AI分析",
                           font="PingFang SC",
                           color="#58a6ff").scale(0.38)
        explanation.next_to(arrow.get_start(), LEFT, buff=0.1)

        self.play(Create(arrow), FadeIn(explanation))
        self.wait(2)
```

---

## 渲染命令

```bash
# 低质量预览（快速）
manim -pql scene.py ClassName

# 高质量 1080p（最终输出）
manim -pqh scene.py ClassName

# 4K输出
manim -pqk scene.py ClassName

# 渲染特定时间段（调试用）
manim -pql scene.py ClassName -n 10,50

# 输出到指定目录
manim -pqh scene.py ClassName --media_dir ./output/animations/
```

---

## Claude 生成 Manim 脚本的提示词

```
你是Manim动画专家。根据以下内容生成完整可运行的Python脚本。

【内容描述】
[粘贴PPT截图/文字描述]

【动画类型】
[从T1-T7中选择，或描述自定义需求]

【技术要求】
- 背景色：#0d1117（深色）
- 主色调：白色文字，蓝/绿/黄作为强调
- 中文用 Text(font="PingFang SC")
- 公式用 MathTex()
- 总时长：约[X]秒
- 风格：简洁、现代，参考3Blue1Brown

【输出要求】
- 完整Python文件，包含所有import
- 类名：CustomScene
- 结尾 self.wait(2) 留剪辑空间
- 添加注释说明各段动画的意图
```
