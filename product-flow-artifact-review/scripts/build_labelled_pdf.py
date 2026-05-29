#!/usr/bin/env python3
"""Build a large labelled screenshot PDF from a JSON spec.

Spec shape:
{
  "title": "Product labelled walkthrough",
  "subtitle": "Optional subtitle",
  "output_pdf": "/absolute/path/out.pdf",
  "pages": [
    {
      "title": "Active task",
      "subtitle": "Why this page exists",
      "image": "/absolute/path/screenshot.png",
      "crop": [left, top, right, bottom],
      "callouts": [{"n": 1, "x": 100, "y": 220}],
      "issues": [{"n": 1, "title": "Issue", "body": "Fix recommendation"}],
      "recommendation": "One-line direction"
    }
  ]
}
Coordinates are in source image pixels. Crop is optional.
"""

import json
import sys
from pathlib import Path

from PIL import Image
from reportlab.lib import colors
from reportlab.lib.pagesizes import A3, landscape
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import stringWidth


PAGE_W, PAGE_H = landscape(A3)
INK = colors.HexColor("#111827")
MUTED = colors.HexColor("#6B7280")
FAINT = colors.HexColor("#EEF2F7")
PANEL = colors.HexColor("#F8FAFC")
RED = colors.HexColor("#EF3340")
BLUE = colors.HexColor("#2563EB")
GREEN_BG = colors.HexColor("#ECFDF5")
GREEN = colors.HexColor("#059669")


def wrap(text, font, size, width):
    words = str(text).split()
    lines, line = [], ""
    for word in words:
        trial = word if not line else f"{line} {word}"
        if stringWidth(trial, font, size) <= width:
            line = trial
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def draw_wrapped(c, text, x, y, width, font="Helvetica", size=10.5, leading=14, color=INK):
    c.setFont(font, size)
    c.setFillColor(color)
    for line in wrap(text, font, size, width):
        c.drawString(x, y, line)
        y -= leading
    return y


def marker(c, x, y, n, r=13):
    c.setFillColor(RED)
    c.circle(x, y, r, stroke=0, fill=1)
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(x, y - 4, str(n))


def draw_cover(c, spec):
    c.setFillColor(colors.HexColor("#0F172A"))
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 32)
    c.drawString(70, PAGE_H - 130, spec.get("title", "Labelled Product Walkthrough"))
    c.setFillColor(colors.HexColor("#CBD5E1"))
    c.setFont("Helvetica", 16)
    c.drawString(70, PAGE_H - 160, spec.get("subtitle", "UX/UI issues, flow continuity, and product recommendations"))

    summary = spec.get("summary", [])
    if summary:
        c.setFillColor(colors.HexColor("#1E293B"))
        c.roundRect(70, 145, PAGE_W - 140, 390, 24, stroke=0, fill=1)
        y = 485
        for item in summary:
            c.setFillColor(BLUE)
            c.setFont("Helvetica-Bold", 11)
            c.drawString(110, y, item.get("label", "NOTE").upper())
            y = draw_wrapped(c, item.get("body", ""), 110, y - 22, PAGE_W - 220, size=17, leading=24, color=colors.white)
            y -= 22
    c.showPage()


def build(spec_path):
    spec_path = Path(spec_path)
    spec = json.loads(spec_path.read_text())
    out = Path(spec["output_pdf"])
    out.parent.mkdir(parents=True, exist_ok=True)
    work = out.parent / f".{out.stem}-crops"
    work.mkdir(parents=True, exist_ok=True)

    c = canvas.Canvas(str(out), pagesize=landscape(A3))
    c.setTitle(spec.get("title", "Labelled Product Walkthrough"))
    draw_cover(c, spec)

    for page_no, page in enumerate(spec.get("pages", []), start=2):
        c.setFillColor(INK)
        c.setFont("Helvetica-Bold", 22)
        c.drawString(46, PAGE_H - 48, page["title"])
        c.setFillColor(MUTED)
        c.setFont("Helvetica", 10)
        c.drawString(46, PAGE_H - 66, page.get("subtitle", ""))

        img = Image.open(page["image"]).convert("RGB")
        crop = page.get("crop") or [0, 0, img.width, img.height]
        cropped = img.crop(tuple(crop))
        crop_path = work / f"page-{page_no}.png"
        cropped.save(crop_path)

        image_x = 58
        max_h = PAGE_H - 220
        max_w = 420
        scale = min(max_w / cropped.width, max_h / cropped.height)
        draw_w = cropped.width * scale
        draw_h = cropped.height * scale
        image_y = 60 + (max_h - draw_h) / 2

        c.setFillColor(colors.white)
        c.roundRect(image_x - 10, image_y - 10, draw_w + 20, draw_h + 20, 18, stroke=0, fill=1)
        c.setStrokeColor(colors.HexColor("#D9E6F8"))
        c.roundRect(image_x - 10, image_y - 10, draw_w + 20, draw_h + 20, 18, stroke=1, fill=0)
        c.drawImage(ImageReader(str(crop_path)), image_x, image_y, width=draw_w, height=draw_h)

        panel_x = 540
        panel_y = PAGE_H - 132
        panel_w = PAGE_W - panel_x - 52
        panel_h = PAGE_H - 230
        c.setFillColor(PANEL)
        c.roundRect(panel_x - 20, 58, panel_w + 40, panel_h, 18, stroke=0, fill=1)
        c.setStrokeColor(FAINT)
        c.roundRect(panel_x - 20, 58, panel_w + 40, panel_h, 18, stroke=1, fill=0)
        c.setFillColor(BLUE)
        c.setFont("Helvetica-Bold", 11)
        c.drawString(panel_x, panel_y + 8, "ISSUES AND FIXES")

        y = panel_y - 34
        for issue in page.get("issues", []):
            marker(c, panel_x + 12, y - 7, issue["n"], r=11)
            c.setFillColor(INK)
            c.setFont("Helvetica-Bold", 13)
            c.drawString(panel_x + 34, y - 3, issue["title"])
            y = draw_wrapped(c, issue.get("body", ""), panel_x + 34, y - 25, panel_w - 34, color=MUTED)
            c.setStrokeColor(FAINT)
            c.line(panel_x, y - 6, panel_x + panel_w, y - 6)
            y -= 22

        c.setStrokeColor(colors.HexColor("#CBD5E1"))
        for callout in page.get("callouts", []):
            sx = image_x + (callout["x"] - crop[0]) * scale
            sy = image_y + draw_h - (callout["y"] - crop[1]) * scale
            marker(c, sx, sy, callout["n"])
            c.line(sx + 16, sy, panel_x - 24, panel_y - 30 - (callout["n"] - 1) * 84)

        if page.get("recommendation"):
            c.setFillColor(GREEN_BG)
            c.roundRect(panel_x, 78, panel_w, 58, 14, stroke=0, fill=1)
            c.setFillColor(GREEN)
            c.setFont("Helvetica-Bold", 10)
            c.drawString(panel_x + 16, 116, "RECOMMENDED DIRECTION")
            draw_wrapped(c, page["recommendation"], panel_x + 16, 100, panel_w - 32, color=INK)

        c.setFillColor(MUTED)
        c.setFont("Helvetica", 9)
        c.drawRightString(PAGE_W - 46, 28, f"{spec.get('footer', 'Product walkthrough')} - {page_no}")
        c.showPage()

    c.save()
    print(out)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: build_labelled_pdf.py spec.json", file=sys.stderr)
        sys.exit(2)
    build(sys.argv[1])

