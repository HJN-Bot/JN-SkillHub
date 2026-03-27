# 双语字幕工作流

## 完整流程

```
原始视频
  → Whisper 语音识别 → 原语言 SRT
  → Claude/DeepL 翻译 → 目标语言 SRT
  → 合并为双语 SRT（中文在上，英文在下）
  → FFmpeg 烧录
  → 输出视频
```

---

## Step 1：Whisper 语音识别

```bash
# 中文视频
whisper input.mp4 --model medium --language zh --output_format srt --output_dir ./subs/

# 英文视频
whisper input.mp4 --model medium --language en --output_format srt --output_dir ./subs/

# 语言不确定（自动检测）
whisper input.mp4 --model medium --language auto --output_format srt --output_dir ./subs/

# 长视频用large模型（更准确）
whisper input.mp4 --model large-v3 --output_format srt --output_dir ./subs/
```

### 模型选择参考
| 模型 | 速度 | 准确率 | 适用场景 |
|------|------|--------|---------|
| tiny | 最快 | 低 | 快速预览 |
| medium | 快 | 中高 | 日常使用 |
| large-v3 | 慢 | 最高 | 最终输出 |

---

## Step 2：SRT 翻译

### 用 Claude 翻译 SRT（保留时间码）

```
系统提示：
你是专业字幕翻译。将以下SRT字幕翻译成[目标语言]。
规则：
1. 只翻译文字内容，不修改序号和时间码
2. 保持与原文相同的分行方式
3. 每条字幕不超过两行
4. 翻译要口语化、自然，不要逐字直译
5. 输出格式与输入完全一致（标准SRT格式）

输入：[粘贴SRT文件内容]
```

---

## Step 3：合并为双语 SRT

### 双语合并脚本

```python
#!/usr/bin/env python3
"""
合并两个SRT文件为双语字幕
中文在上，英文在下（或反之）
"""
import re

def parse_srt(content):
    """解析SRT文件为列表"""
    pattern = r'(\d+)\n(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})\n([\s\S]*?)(?=\n\n|\Z)'
    entries = []
    for m in re.finditer(pattern, content.strip()):
        entries.append({
            'index': int(m.group(1)),
            'start': m.group(2),
            'end': m.group(3),
            'text': m.group(4).strip()
        })
    return entries

def merge_bilingual(primary_srt, secondary_srt, output_path,
                    primary_lang='zh', secondary_lang='en'):
    """
    primary: 显示在上方的语言（通常是中文）
    secondary: 显示在下方的语言（通常是英文）
    """
    with open(primary_srt, 'r', encoding='utf-8') as f:
        primary = parse_srt(f.read())
    with open(secondary_srt, 'r', encoding='utf-8') as f:
        secondary = parse_srt(f.read())

    # 以primary为基准，匹配secondary
    output = []
    for i, p in enumerate(primary):
        sec_text = secondary[i]['text'] if i < len(secondary) else ''
        # 双语格式：主语言\n次语言
        merged_text = f"{p['text']}\n{sec_text}"
        output.append(f"{i+1}\n{p['start']} --> {p['end']}\n{merged_text}\n")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output))

    print(f"✅ 双语字幕已生成：{output_path}")

# 使用示例
# merge_bilingual('./subs/zh.srt', './subs/en.srt', './subs/bilingual.srt')
```

---

## Step 4：FFmpeg 烧录字幕

### 双语字幕样式（深色背景视频）

```bash
ffmpeg -i input.mp4 \
  -vf "subtitles=bilingual.srt:force_style='
    FontName=PingFang SC,
    FontSize=22,
    PrimaryColour=&H00FFFFFF,
    SecondaryColour=&H00CCCCCC,
    OutlineColour=&H00000000,
    BackColour=&H80000000,
    Bold=0,
    Outline=1,
    Shadow=1,
    MarginV=40,
    Alignment=2'" \
  -c:v libx264 -crf 18 -c:a copy \
  output_subtitled.mp4
```

### 双语字幕样式（浅色背景视频）

```bash
ffmpeg -i input.mp4 \
  -vf "subtitles=bilingual.srt:force_style='
    FontName=PingFang SC,
    FontSize=22,
    PrimaryColour=&H00000000,
    OutlineColour=&H00FFFFFF,
    Outline=2,
    Shadow=0,
    MarginV=40,
    Alignment=2'" \
  -c:v libx264 -crf 18 -c:a copy \
  output_subtitled.mp4
```

### 颜色代码参考（ASS格式：&HAABBGGRR）
| 颜色 | 代码 |
|------|------|
| 白色 | `&H00FFFFFF` |
| 黑色 | `&H00000000` |
| 浅灰 | `&H00CCCCCC` |
| 黄色 | `&H0000FFFF` |
| 半透明黑背景 | `&H80000000` |

---

## 常见问题

**中文字幕乱码**
→ 确保SRT文件编码为UTF-8，FFmpeg命令加 `-sub_charenc UTF-8`

**字幕位置偏移**
→ 调整 `MarginV` 参数（数值越大，离底部越远）

**两语言行间距太小**
→ 在合并脚本中，在两行之间加入 `\N`（ASS换行符）代替 `\n`
