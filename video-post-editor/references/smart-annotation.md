# 智能对比色标注

## 设计原则

- **自动适配**：检测目标帧平均亮度，自动选择高对比色
- **克制简洁**：线条细（3px），不加阴影，不花哨
- **淡入淡出**：出现和消失各0.3s，避免突兀

---

## 背景亮度检测

```python
#!/usr/bin/env python3
"""
分析视频指定时间段的背景亮度
返回推荐标注颜色
"""
import subprocess
import os
from PIL import Image

def extract_frame(video_path: str, timestamp: float, output_path: str) -> str:
    """从视频中提取指定时间的帧"""
    cmd = [
        "ffmpeg", "-y",
        "-ss", str(timestamp),
        "-i", video_path,
        "-frames:v", "1",
        "-q:v", "2",
        output_path
    ]
    subprocess.run(cmd, capture_output=True)
    return output_path

def get_region_brightness(frame_path: str, region: tuple = None) -> float:
    """
    计算帧（或指定区域）的平均亮度
    region: (x, y, width, height) 像素坐标，None则分析整帧
    返回 0-255 的亮度值
    """
    img = Image.open(frame_path).convert('L')  # 转灰度
    if region:
        x, y, w, h = region
        img = img.crop((x, y, x+w, y+h))
    pixels = list(img.getdata())
    return sum(pixels) / len(pixels)

def get_annotation_color(video_path: str, timestamp: float,
                          region: tuple = None) -> dict:
    """
    综合判断，返回标注颜色配置
    """
    frame_path = "/tmp/annotation_check_frame.jpg"
    extract_frame(video_path, timestamp, frame_path)
    brightness = get_region_brightness(frame_path, region)
    os.remove(frame_path)

    if brightness < 100:
        # 深色背景 → 白色标注
        return {
            "box_color": "white",
            "text_color": "white",
            "ffmpeg_color": "white",
            "background": "dark"
        }
    elif brightness < 180:
        # 中间色背景 → 根据偏向选择
        return {
            "box_color": "white" if brightness < 140 else "black",
            "text_color": "white" if brightness < 140 else "black",
            "ffmpeg_color": "white" if brightness < 140 else "black",
            "background": "mid"
        }
    else:
        # 浅色背景 → 黑色标注
        return {
            "box_color": "black",
            "text_color": "black",
            "ffmpeg_color": "black",
            "background": "light"
        }
```

---

## FFmpeg 标注命令模板

### 基础矩形框

```bash
# 变量说明：
# START/END: 时间（秒），如 83.0 / 105.0
# X Y W H: 框的位置和大小（像素）
# COLOR: white 或 black

ffmpeg -i input.mp4 \
  -vf "drawbox=
    enable='between(t,START,END)':
    x=X:y=Y:w=W:h=H:
    color=COLOR@0.85:
    t=3" \
  -c:v libx264 -crf 18 -c:a copy \
  output_annotated.mp4
```

### 框 + 标签文字

```bash
ffmpeg -i input.mp4 \
  -vf "
    drawbox=enable='between(t,START,END)':x=X:y=Y:w=W:h=H:color=COLOR@0.85:t=3,
    drawtext=enable='between(t,START,END)':
      text='LABEL_TEXT':
      x=X:y=Y-28:
      fontfile=/System/Library/Fonts/PingFang.ttc:
      fontsize=18:fontcolor=COLOR:
      box=1:boxcolor=COLOR@0.15:boxborderw=6
  " \
  -c:v libx264 -crf 18 -c:a copy \
  output_annotated.mp4
```

### 多段标注（一次处理）

```bash
# 多个时间段，多个位置
ffmpeg -i input.mp4 \
  -vf "
    drawbox=enable='between(t,10,25)':x=100:y=200:w=300:h=150:color=white@0.85:t=3,
    drawbox=enable='between(t,45,60)':x=500:y=100:w=200:h=200:color=white@0.85:t=3,
    drawtext=enable='between(t,10,25)':text='注意这里':x=100:y=172:fontsize=16:fontcolor=white
  " \
  -c:v libx264 -crf 18 -c:a copy \
  output_annotated.mp4
```

---

## 标注描述 → 时间码转换

当用户用自然语言描述位置时，用Claude Vision分析：

```
提示词模板：
请分析这个视频截图，找到"[用户描述的内容]"在画面中的位置。
返回格式：
- 大约在视频的第几秒？
- 在画面的哪个区域？（请给出大致的 x, y 坐标和宽高，基于1920x1080分辨率）
```

---

## 标注风格规范

| 参数 | 值 | 说明 |
|------|-----|------|
| 线宽 | 3px | 克制，不粗 |
| 透明度 | 0.85 | 略微透明，不遮挡内容 |
| 颜色 | 自动 | 深背景→白，浅背景→黑 |
| 文字字号 | 16-20px | 清晰但不抢镜 |
| 标签位置 | 框左上角外侧 | 默认，可调 |
| 淡入淡出 | 各0.3s | 用opacity滤镜实现 |

---

## 坐标系参考

```
(0,0)─────────────────────(1920,0)
  │                              │
  │    (x,y)                     │
  │      ┌──────────┐            │
  │      │  W×H     │            │
  │      └──────────┘            │
  │                              │
(0,1080)──────────────────(1920,1080)
```

常见区域速查（1920×1080基准）：
- 屏幕正中央：`x=760:y=390:w=400:h=300`
- 左上角：`x=50:y=50:w=400:h=300`
- 右下角：`x=1470:y=730:w=400:h=300`
- 顶部横条：`x=0:y=0:w=1920:h=120`
