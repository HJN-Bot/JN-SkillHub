#!/usr/bin/env python3
"""
compile.py — 把一本书编译成 Epub + HTML 预览

用法:
    python3 compile.py <book-dir>

例子:
    python3 compile.py books/cer-methodology

输入:
    <book-dir>/BOOK.md           — 元数据 + TOC
    <book-dir>/chapters/*.md     — 章节正文
    <book-dir>/assets/images/    — 图片资源（可选）

输出:
    <book-dir>/dist/<book-id>-<YYYYMMDD>.epub
    <book-dir>/dist/preview.html
"""

import sys
import os
import re
import datetime
from pathlib import Path

import yaml
import markdown
from ebooklib import epub


# ============================================================
# 1. 读 BOOK.md 元数据
# ============================================================

def parse_book_meta(book_dir: Path) -> dict:
    """从 BOOK.md 解析元数据。"""
    book_md = book_dir / "BOOK.md"
    if not book_md.exists():
        raise FileNotFoundError(f"找不到 {book_md}")

    text = book_md.read_text(encoding="utf-8")

    meta = {
        "book_id": book_dir.name,
        "title": "未命名书",
        "author": "Jianan",
        "thesis": "",
        "audience": "",
    }

    # 从 markdown 列表中粗解析
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("- **book_id**:"):
            meta["book_id"] = line.split(":", 1)[1].strip()
        elif line.startswith("- **作者**:"):
            meta["author"] = line.split(":", 1)[1].strip()
        elif line.startswith("- **核心命题**:"):
            meta["thesis"] = line.split(":", 1)[1].strip()
        elif line.startswith("- **目标读者**:"):
            meta["audience"] = line.split(":", 1)[1].strip()

    # 从一级标题取书名
    m = re.search(r"^#\s+《(.+?)》", text, re.MULTILINE)
    if m:
        meta["title"] = m.group(1)

    return meta


# ============================================================
# 2. 读章节并解析 frontmatter
# ============================================================

def parse_chapter(md_path: Path) -> dict:
    """读单个章节文件，分离 frontmatter 和正文。"""
    text = md_path.read_text(encoding="utf-8")
    fm = {}
    body = text

    # 解析 YAML frontmatter
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            fm_text = text[4:end]
            body = text[end + 5:]
            try:
                fm = yaml.safe_load(fm_text) or {}
            except yaml.YAMLError as e:
                print(f"  ⚠ YAML 解析失败 {md_path.name}: {e}")

    return {
        "path": md_path,
        "frontmatter": fm,
        "body": body,
        "chapter_num": fm.get("chapter", "?"),
        "title": fm.get("title", md_path.stem),
        "teaching_mode": fm.get("teaching_mode", "case_first"),
        "completion": fm.get("completion", 0),
    }


def collect_chapters(book_dir: Path) -> list:
    """收集所有章节，按文件名排序。"""
    chapters_dir = book_dir / "chapters"
    if not chapters_dir.exists():
        return []

    md_files = sorted(chapters_dir.glob("*.md"))
    chapters = [parse_chapter(p) for p in md_files]
    return chapters


# ============================================================
# 3. Markdown → HTML
# ============================================================

def md_to_html(md_text: str) -> str:
    """Markdown → HTML，启用代码块、表格、脚注、TOC 等扩展。"""
    md = markdown.Markdown(
        extensions=[
            "fenced_code",
            "tables",
            "footnotes",
            "toc",
            "attr_list",
            "def_list",
            "abbr",
            "md_in_html",
            "sane_lists",
        ],
        extension_configs={
            "footnotes": {"BACKLINK_TEXT": "↩"},
        }
    )
    return md.convert(md_text)


# ============================================================
# 4. 组装 Epub
# ============================================================

def build_epub(book_dir: Path, meta: dict, chapters: list, css_text: str, out_path: Path):
    """用 ebooklib 组装 Epub。"""
    book = epub.EpubBook()
    book.set_identifier(f"jianan-{meta['book_id']}-{datetime.date.today().isoformat()}")
    book.set_title(meta["title"])
    book.set_language("zh-CN")
    book.add_author(meta["author"])

    if meta.get("thesis"):
        book.add_metadata("DC", "description", meta["thesis"])

    # CSS 资源
    css_item = epub.EpubItem(
        uid="style_main",
        file_name="style/tech-book.css",
        media_type="text/css",
        content=css_text,
    )
    book.add_item(css_item)

    # 封面页
    cover_html = f"""
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>{meta['title']}</title>
        <link rel="stylesheet" type="text/css" href="style/tech-book.css"/>
    </head>
    <body>
        <div class="cover">
            <div class="title">{meta['title']}</div>
            <div class="subtitle">{meta.get('thesis', '')}</div>
            <div class="author">— {meta['author']} —</div>
        </div>
    </body>
    </html>
    """
    cover = epub.EpubHtml(title="封面", file_name="cover.xhtml", lang="zh-CN")
    cover.content = cover_html
    cover.add_item(css_item)
    book.add_item(cover)

    # 章节
    epub_chapters = []
    for ch in chapters:
        body_html = md_to_html(ch["body"])

        # 章节首页加 meta 标记
        ch_num = ch["chapter_num"]
        ch_title = ch["title"]
        meta_line = f'<div class="chapter-meta">CH {ch_num:0>2} · {ch["teaching_mode"]}</div>' if ch_num != "?" else ""

        chapter_html = f"""
        <html xmlns="http://www.w3.org/1999/xhtml">
        <head>
            <title>{ch_title}</title>
            <link rel="stylesheet" type="text/css" href="style/tech-book.css"/>
        </head>
        <body>
            {meta_line}
            {body_html}
        </body>
        </html>
        """

        ch_item = epub.EpubHtml(
            title=ch_title,
            file_name=f"chapter_{ch_num:0>2}.xhtml" if isinstance(ch_num, int) else f"chapter_{ch['path'].stem}.xhtml",
            lang="zh-CN",
        )
        ch_item.content = chapter_html
        ch_item.add_item(css_item)
        book.add_item(ch_item)
        epub_chapters.append(ch_item)

    # 图片资源
    images_dir = book_dir / "assets" / "images"
    if images_dir.exists():
        for img_path in images_dir.iterdir():
            if img_path.suffix.lower() in [".png", ".jpg", ".jpeg", ".gif", ".svg"]:
                ext = img_path.suffix.lower().lstrip(".")
                media_type = f"image/{ext if ext != 'jpg' else 'jpeg'}"
                if ext == "svg":
                    media_type = "image/svg+xml"
                img_item = epub.EpubItem(
                    uid=f"img_{img_path.stem}",
                    file_name=f"images/{img_path.name}",
                    media_type=media_type,
                    content=img_path.read_bytes(),
                )
                book.add_item(img_item)

    # 目录与 spine
    book.toc = tuple(epub_chapters)
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    book.spine = ["cover", "nav"] + epub_chapters

    # 写出
    out_path.parent.mkdir(parents=True, exist_ok=True)
    epub.write_epub(str(out_path), book)
    return out_path


# ============================================================
# 5. HTML 单文件预览
# ============================================================

def build_html_preview(meta: dict, chapters: list, css_text: str, out_path: Path):
    """生成单文件 HTML 预览，方便不开 Epub 阅读器也能扫一眼。"""
    parts = [
        "<!DOCTYPE html>",
        '<html lang="zh-CN">',
        "<head>",
        '<meta charset="UTF-8">',
        f"<title>{meta['title']} — Preview</title>",
        "<style>",
        css_text,
        "</style>",
        "</head>",
        "<body>",
        '<div class="cover">',
        f'<div class="title">{meta["title"]}</div>',
        f'<div class="subtitle">{meta.get("thesis", "")}</div>',
        f'<div class="author">— {meta["author"]} —</div>',
        "</div>",
    ]

    for ch in chapters:
        body_html = md_to_html(ch["body"])
        ch_num = ch["chapter_num"]
        if ch_num != "?":
            parts.append(f'<div class="chapter-meta">CH {ch_num:0>2} · {ch["teaching_mode"]}</div>')
        parts.append(body_html)

    parts.extend(["</body>", "</html>"])

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(parts), encoding="utf-8")
    return out_path


# ============================================================
# Main
# ============================================================

def main():
    if len(sys.argv) < 2:
        print("用法: python3 compile.py <book-dir>")
        sys.exit(1)

    book_dir = Path(sys.argv[1]).resolve()
    if not book_dir.exists():
        print(f"❌ 找不到目录: {book_dir}")
        sys.exit(1)

    print(f"📖 编译: {book_dir.name}")

    # 1. 元数据
    meta = parse_book_meta(book_dir)
    print(f"   书名: 《{meta['title']}》")
    print(f"   作者: {meta['author']}")

    # 2. 章节
    chapters = collect_chapters(book_dir)
    print(f"   章节数: {len(chapters)}")
    for ch in chapters:
        ch_num = ch["chapter_num"]
        print(f"     - Ch {ch_num:0>2}: {ch['title']} ({ch['completion']}%)")

    if not chapters:
        print("⚠ 没有章节，无法编译。请先在 chapters/ 下创建 .md 文件。")
        sys.exit(1)

    # 3. CSS
    # 优先使用 skill 自带 CSS，找不到时报错
    skill_css = Path(__file__).parent.parent / "assets" / "styles" / "tech-book.css"
    if not skill_css.exists():
        # 回退：在 book_dir 同级找
        skill_css = book_dir.parent.parent / "skills" / "writing-book" / "assets" / "styles" / "tech-book.css"

    if not skill_css.exists():
        print(f"⚠ 找不到 CSS: {skill_css}，使用空白样式")
        css_text = ""
    else:
        css_text = skill_css.read_text(encoding="utf-8")
        print(f"   样式: {skill_css.name}")

    # 4. Epub
    today = datetime.date.today().strftime("%Y%m%d")
    epub_out = book_dir / "dist" / f"{meta['book_id']}-{today}.epub"
    build_epub(book_dir, meta, chapters, css_text, epub_out)
    print(f"✅ Epub: {epub_out.relative_to(book_dir.parent.parent) if book_dir.parent.parent in epub_out.parents else epub_out}")

    # 5. HTML 预览
    html_out = book_dir / "dist" / "preview.html"
    build_html_preview(meta, chapters, css_text, html_out)
    print(f"✅ HTML 预览: {html_out.relative_to(book_dir.parent.parent) if book_dir.parent.parent in html_out.parents else html_out}")

    print("\n🎉 编译完成。")


if __name__ == "__main__":
    main()
