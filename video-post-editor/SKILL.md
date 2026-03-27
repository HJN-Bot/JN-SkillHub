---
name: video-post-editor
description: >
  视频后期处理技能，覆盖三大核心场景：
  ①双语字幕（中文在上/英文在下，Whisper识别+翻译+FFmpeg烧录）；
  ②智能对比色标注（自动检测背景亮度，深色背景用白框，浅色背景用黑框）；
  ③解析类动画生成（结合PPT/截图/文字描述，用Manim生成公式/流程/模型动画并渲染输出）。
  当用户说「加字幕」「双语字幕」「标注这个片段」「做解析动画」「帮我做Demo视频」
  「结合我的PPT做视频」「科普动画」「Manim」「解说视频」「后期处理」时，必须触发此技能。
---

# Video Post-Editor Skill

## 场景速判（第一步）

| 场景 | 典型需求 | 核心工具 |
|------|---------|---------|
| **A·双语字幕** | 给视频加中英双语字幕 | Whisper → DeepL/Claude → FFmpeg |
| **B·片段标注** | 指定时间段加高亮框/箭头/文字 | 背景分析 → FFmpeg drawbox/drawtext |
| **C·解析动画** | 根据PPT或文字描述生成动画插入视频 | Claude读稿 → Manim脚本 → 渲染 → FFmpeg合成 |
| **混合** | 以上任意组合 | 按顺序执行各模块 |

---

## 交互层：需求收集

**接到用户需求，按轮次收集，每次最多3问：**

### 第一轮：任务类型
```
1. 这次主要做什么？（可多选）
   A) 加双语字幕
   B) 给特定片段加标注
   C) 生成解析/解说动画
   D) 以上都要

2. 视频语言是什么？
   · 中文 → 字幕走 Whisper zh → 英文翻译
   · 英文 → 字幕走 Whisper en → 中文翻译
   · 中英混合 → Whisper auto模式

3. 视频大概多长？（决定处理策略）
```

### 第二轮（选B标注时）
```
4. 标注位置是时间码还是描述？
   · 时间码：如 00:01:23 - 00:01:45
   · 描述：如「第一次点击按钮的地方」（我来定位）

5. 标注内容？
   · 只需要框（矩形高亮）
   · 框+文字说明
   · 箭头指向
   · 全部

6. 视频背景是深色还是浅色？（或让我自动检测）
```

### 第二轮（选C动画时）
```
7. 动画内容来源？
   · PPT文件（请提供路径或截图）
   · 文字描述（直接说）
   · 两者结合

8. 动画类型？
   · 公式推导 → Manim MathTex
   · 流程图/架构图 → Manim Diagram
   · 数据可视化 → Manim BarChart/Graph
   · 概念演示（高亮、展开、对比）→ Manim Scene
   · 参考某个风格（发图给我）

9. 动画插入位置？
   · 替换原视频某段
   · 插入到某个时间点之后
   · 作为独立片段，不合并
```

---

## 模块A：双语字幕流程

> 详细步骤见 `references/subtitle-workflow.md`

### 快速执行路径

```bash
# Step 1: 语音识别
whisper input.mp4 --model medium --language auto --output_format srt --output_dir ./subs/

# Step 2: 翻译（Claude处理SRT，保留时间码）
# 中→英 或 英→中，见subtitle-workflow.md

# Step 3: 生成双语SRT（中文在上，英文在下）
# 合并两个SRT，中文条目 + 空行 + 英文条目，同时间码

# Step 4: 烧录进视频
ffmpeg -i input.mp4 \
  -vf "subtitles=bilingual.srt:force_style='
    FontName=PingFang SC,
    FontSize=22,
    PrimaryColour=&H00FFFFFF,
    OutlineColour=&H00000000,
    Outline=2,
    Shadow=1,
    MarginV=30,
    Alignment=2'" \
  -c:a copy output_subtitled.mp4
```

### 双语布局规则
- **中文**：屏幕下方，字号22，白色+黑色描边
- **英文**：中文上方一行，字号18，浅灰色+黑色描边
- 间距：英文与中文间隔6px
- 若视频背景浅色，自动切换为黑色字+白色描边

---

## 模块B：智能对比色标注

> 详细参数见 `references/smart-annotation.md`

### 背景亮度自动检测

```python
# 分析指定时间段的帧平均亮度
import subprocess, json

def get_frame_brightness(video_path, timestamp):
    cmd = [
        "ffprobe", "-v", "quiet",
        "-select_streams", "v:0",
        "-show_entries", "frame=pkt_pts_time,pix_fmt",
        "-of", "json",
        "-ss", str(timestamp),
        "-frames:v", "1",
        video_path
    ]
    # 提取帧 → PIL分析均值亮度
    # 亮度 < 128 → 深色背景 → 用白框
    # 亮度 >= 128 → 浅色背景 → 用黑框

def get_annotation_color(brightness):
    if brightness < 128:
        return "white"   # 深色背景
    else:
        return "black"   # 浅色背景
```

### FFmpeg标注命令模板

```bash
# 矩形高亮框（x,y,w,h为区域坐标）
ffmpeg -i input.mp4 \
  -vf "drawbox=
    enable='between(t,START,END)':
    x=X:y=Y:w=W:h=H:
    color=COLOR@0.9:
    t=3" \
  output_annotated.mp4

# 框+文字标注
ffmpeg -i input.mp4 \
  -vf "drawbox=enable='between(t,START,END)':x=X:y=Y:w=W:h=H:color=COLOR@0.9:t=3,
       drawtext=enable='between(t,START,END)':
         text='LABEL':
         x=X:y=Y-30:
         fontsize=20:fontcolor=COLOR:
         box=1:boxcolor=COLOR@0.3:boxborderw=5" \
  output_annotated.mp4
```

### 标注风格规范
- **线宽**：3px（细腻，不喧宾夺主）
- **颜色逻辑**：深背景→白框，浅背景→黑框，自动检测
- **淡入淡出**：标注出现/消失各0.3s渐变
- **文字位置**：默认在框的左上角外侧

---

## 模块C：解析动画生成

> Manim模板库见 `references/manim-templates.md`

### 工作流

```
用户提供内容
    ↓
Claude 读取PPT截图/文字描述
    ↓
生成 Manim Python 脚本
    ↓
本地渲染（需要Manim环境）
    ↓
输出 MP4 动画片段
    ↓
FFmpeg 合成进原视频
```

### Manim环境要求

```bash
# 安装
pip install manim

# 验证
manim --version

# 渲染脚本
manim -pql scene.py SceneName        # 低质量预览
manim -pqh scene.py SceneName        # 高质量输出（1080p）
manim -pqk scene.py SceneName        # 4K输出
```

### 标准场景模板

```python
from manim import *

class ExplainerScene(Scene):
    """解析类动画基础模板"""
    def construct(self):
        # 背景色：深色（匹配用户视频风格）
        self.camera.background_color = "#1a1a2e"

        # 标题
        title = Text("概念标题", font="PingFang SC", color=WHITE).scale(0.8)
        title.to_edge(UP)
        self.play(Write(title))

        # 内容区域（子类覆盖此方法）
        self.build_content()

        self.wait(2)

    def build_content(self):
        pass
```

### Claude生成Manim脚本的提示词模板

```
你是Manim动画专家。根据以下内容生成可直接运行的Python脚本：

内容描述：[用户的PPT截图/文字]
动画类型：[公式/流程/架构/概念]
视频背景色：[深色#1a1a2e / 浅色#ffffff]
时长要求：[X秒]
风格参考：简洁、现代、3Blue1Brown风格

要求：
- 输出完整可运行的Python文件
- 包含所有import
- 中文用Text()，公式用MathTex()
- 动画节奏：每个元素出现间隔0.5s
- 结尾留白2s供剪辑
```

---

## 输出规范

| 产物 | 格式 | 位置 |
|------|------|------|
| 字幕文件 | `.srt` + `.ass` | `./output/subs/` |
| 标注视频 | `_annotated.mp4` | `./output/` |
| Manim动画 | `_animation.mp4` | `./output/animations/` |
| 最终合成 | `_final.mp4` | `./output/` |

---

## 依赖清单

```bash
# 必装
brew install ffmpeg
pip install openai-whisper
pip install manim

# 翻译（可选，也可用Claude直接翻译SRT）
pip install deep-translator

# 图像分析（亮度检测）
pip install Pillow opencv-python
```
