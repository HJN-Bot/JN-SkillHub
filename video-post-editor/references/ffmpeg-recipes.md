# FFmpeg 常用配方

## 视频信息查询

```bash
# 查看视频基本信息（时长、分辨率、帧率、编码）
ffprobe -v quiet -print_format json -show_streams input.mp4 | python3 -m json.tool

# 快速查看时长
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 input.mp4
```

---

## 基础剪辑

```bash
# 截取片段（精确到秒）
ffmpeg -ss 00:01:30 -to 00:02:45 -i input.mp4 -c copy segment.mp4

# 截取片段（毫秒精度，需重编码）
ffmpeg -ss 90.5 -to 165.3 -i input.mp4 -c:v libx264 -crf 18 -c:a aac segment.mp4

# 删除某段，保留前后（两步法）
ffmpeg -ss 0 -to 30 -i input.mp4 -c copy part1.mp4
ffmpeg -ss 60 -i input.mp4 -c copy part2.mp4
# 然后用concat合并
```

---

## 视频合并

```bash
# 合并多个视频片段（编码相同时）
# 先创建文件列表
cat > filelist.txt << EOF
file 'part1.mp4'
file 'part2.mp4'
file 'part3.mp4'
EOF

ffmpeg -f concat -safe 0 -i filelist.txt -c copy merged.mp4

# 不同编码的视频合并（重编码）
ffmpeg -f concat -safe 0 -i filelist.txt \
  -c:v libx264 -crf 18 -c:a aac merged.mp4
```

---

## 在指定时间点插入动画片段

```bash
# 方案：拆分原视频 → 插入动画 → 重新合并
# 假设在 t=45s 处插入 animation.mp4

# Step 1: 截取前半段
ffmpeg -ss 0 -to 45 -i original.mp4 -c:v libx264 -crf 18 -c:a aac before.mp4

# Step 2: 截取后半段
ffmpeg -ss 45 -i original.mp4 -c:v libx264 -crf 18 -c:a aac after.mp4

# Step 3: 统一分辨率（若动画分辨率不同）
ffmpeg -i animation.mp4 -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2" \
  -c:v libx264 -crf 18 -c:a aac animation_scaled.mp4

# Step 4: 合并
cat > filelist.txt << EOF
file 'before.mp4'
file 'animation_scaled.mp4'
file 'after.mp4'
EOF
ffmpeg -f concat -safe 0 -i filelist.txt -c copy final.mp4
```

---

## 画中画（视频叠加）

```bash
# 将小视频叠加到主视频右下角
ffmpeg -i main.mp4 -i overlay.mp4 \
  -filter_complex "[1:v]scale=480:270[ov];[0:v][ov]overlay=W-w-20:H-h-20" \
  -c:v libx264 -crf 18 -c:a copy output.mp4

# 在指定时间段显示叠加
ffmpeg -i main.mp4 -i overlay.mp4 \
  -filter_complex "[1:v]scale=480:270[ov];[0:v][ov]overlay=W-w-20:H-h-20:enable='between(t,10,30)'" \
  -c:v libx264 -crf 18 -c:a copy output.mp4
```

---

## 分辨率与格式转换

```bash
# 统一为 1920x1080
ffmpeg -i input.mp4 -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1" \
  -c:v libx264 -crf 18 -c:a aac output_1080p.mp4

# 压缩文件大小（牺牲部分质量）
ffmpeg -i input.mp4 -c:v libx264 -crf 28 -preset slow -c:a aac -b:a 128k compressed.mp4

# 转换帧率（30fps）
ffmpeg -i input.mp4 -r 30 -c:v libx264 -crf 18 output_30fps.mp4
```

---

## 音频处理

```bash
# 提取音频
ffmpeg -i input.mp4 -vn -c:a aac audio.aac

# 替换音频
ffmpeg -i video.mp4 -i new_audio.mp3 -map 0:v -map 1:a -c:v copy -shortest output.mp4

# 调整音量（2倍）
ffmpeg -i input.mp4 -af "volume=2.0" -c:v copy output.mp4

# 添加背景音乐（混合）
ffmpeg -i video.mp4 -i bgm.mp3 \
  -filter_complex "[1:a]volume=0.3[bgm];[0:a][bgm]amix=inputs=2:duration=first[aout]" \
  -map 0:v -map "[aout]" -c:v copy output.mp4
```

---

## 字幕相关

```bash
# 烧录 SRT 字幕（软烧，可搜索）
ffmpeg -i input.mp4 -c:v copy -c:a copy -s:s "subtitle_track" output.mp4

# 硬烧字幕（画面内嵌，通用）
ffmpeg -i input.mp4 -vf "subtitles=subtitle.srt" -c:v libx264 -crf 18 output.mp4

# 带样式的硬烧
ffmpeg -i input.mp4 \
  -vf "subtitles=subtitle.srt:force_style='FontName=PingFang SC,FontSize=24,PrimaryColour=&H00FFFFFF,Outline=1'" \
  -c:v libx264 -crf 18 -c:a copy output.mp4

# 提取内嵌字幕
ffmpeg -i input.mp4 -map 0:s:0 output.srt
```

---

## 批量处理

```bash
# 批量添加字幕（Shell脚本）
for f in *.mp4; do
    name="${f%.mp4}"
    ffmpeg -i "$f" \
      -vf "subtitles=${name}.srt" \
      -c:v libx264 -crf 18 -c:a copy \
      "output/${name}_subtitled.mp4"
done
```

---

## 质量参数参考

| CRF值 | 质量 | 文件大小 | 适用场景 |
|-------|------|---------|---------|
| 18 | 近无损 | 大 | 最终输出存档 |
| 23 | 高质量 | 中 | 一般输出（默认） |
| 28 | 中等 | 小 | 分享/上传 |
| 35 | 低 | 很小 | 预览 |
