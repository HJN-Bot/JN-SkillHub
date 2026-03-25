# FFmpeg 拼接与处理命令参考

## 基础拼接（多片段顺序合并）

```bash
# 方法1：concat 协议（推荐，快速）
# 先建 filelist.txt：
# file 'clip1.mp4'
# file 'clip2.mp4'
# file 'clip3.mp4'
ffmpeg -f concat -safe 0 -i filelist.txt -c copy output.mp4

# 方法2：filter_complex（需要重编码，质量更好）
ffmpeg -i clip1.mp4 -i clip2.mp4 -i clip3.mp4 \
  -filter_complex "[0:v][1:v][2:v]concat=n=3:v=1:a=0[outv]" \
  -map "[outv]" output.mp4
```

## 添加背景音乐

```bash
# 将视频与音乐合并，音乐循环直到视频结束
ffmpeg -i output.mp4 -i bgm.mp3 \
  -filter_complex "[1:a]volume=0.6[a]" \
  -map 0:v -map "[a]" \
  -shortest -c:v copy output_with_music.mp4
```

## 调整帧率（平滑处理）

```bash
# 将视频转换为 60fps（结合帧插值效果更好）
ffmpeg -i input.mp4 -vf "fps=60" -c:v libx264 -preset slow -crf 18 output_60fps.mp4
```

## 格式转换

```bash
# MP4 → 适合小红书/抖音的竖版 9:16（裁剪居中）
ffmpeg -i input.mp4 -vf "crop=ih*9/16:ih:(iw-ih*9/16)/2:0" -c:a copy output_916.mp4

# 调整分辨率到 1080x1920（抖音标准竖版）
ffmpeg -i input.mp4 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black" output_1080x1920.mp4
```

## 加速/减速（营造节奏感）

```bash
# 2x 加速
ffmpeg -i input.mp4 -vf "setpts=0.5*PTS" -an output_2x.mp4

# 0.5x 减速（丝滑慢放）
ffmpeg -i input.mp4 -vf "setpts=2.0*PTS" -an output_slow.mp4
```

## 添加转场效果（简单淡入淡出）

```bash
# 两段视频之间加 1 秒黑场淡入淡出
ffmpeg -i clip1.mp4 -i clip2.mp4 \
  -filter_complex "\
    [0:v]fade=t=out:st=4:d=1[v0]; \
    [1:v]fade=t=in:st=0:d=1[v1]; \
    [v0][v1]concat=n=2:v=1:a=0[outv]" \
  -map "[outv]" output_fade.mp4
```

## 批量下载 fal.ai 生成的视频

```bash
# 从 URL 列表批量下载
while IFS= read -r url; do
    filename=$(basename "$url" | cut -d'?' -f1)
    wget -q -O "$filename" "$url"
    echo "Downloaded: $filename"
done < video_urls.txt
```
