# Markdown → Epub 编译流程

## 编译指令

```bash
python3 skills/writing-book/scripts/compile.py books/<book-id>
```

## 编译阶段

```
[1] parse_book_meta(BOOK.md)
        ↓
[2] collect_chapters(chapters/*.md)
        ↓ 每章解析 frontmatter + body
[3] md_to_html(body)
        ↓ 启用 fenced_code / tables / footnotes / toc 扩展
[4] build_epub
        ↓ 加 cover + 章节 + CSS + 图片
[5] build_html_preview
        ↓ 单文件 HTML 备份
[6] 输出 dist/<book-id>-<YYYYMMDD>.epub + dist/preview.html
```

## 章节文件的命名

`chapters/ch<NN>-<slug>.md`

- `NN` 是 0-padded 两位数：00, 01, 02, ..., 99
- `slug` 是英文短描述
- 例：`ch00-introduction.md`, `ch01-pipeline-discipline.md`

编译会按文件名字典序排，所以用 0-padded 数字保证顺序。

## 章节 frontmatter

```yaml
---
chapter: 1                    # 整数
title: Pipeline 工程纪律        # 显示用标题
teaching_mode: case_first     # first_principles | case_first | dialogue
status: drafting              # drafting | refined | done
fragments_used:               # 编排用到的 fragment 文件名
  - research/2026-04-03_anchor-verify.md
last_updated: 2026-05-07
completion: 60                # 0-100
---
```

## 自定义样式

编辑 `skills/writing-book/assets/styles/tech-book.css`。

如果想给某本书单独换样式，把 `tech-book.css` 复制到 `books/<book-id>/style.css`，
然后编译脚本会优先使用书目录下的版本（待扩展）。

## 验证

编译完成后：
1. 用 Apple Books / Calibre / 微信读书 打开 `.epub`
2. 用浏览器打开 `dist/preview.html` 快速扫一遍
3. 检查代码块是否正确渲染（黑底白字）
4. 检查表格是否完整保留

## 故障排查

| 现象 | 原因 | 解决 |
|------|------|------|
| 章节顺序乱了 | 文件名没用 0-padded 数字 | `ch1.md` → `ch01.md` |
| YAML 解析失败 | frontmatter 里有未转义的 `:` | 给值加引号 `"value: with colon"` |
| 中文字体没生效 | 阅读器没装思源宋体 | CSS 已 fallback 到系统 SC 字体 |
| 图片不显示 | 路径不对 | 必须放 `assets/images/` 下，引用用 `images/xxx.png` |
