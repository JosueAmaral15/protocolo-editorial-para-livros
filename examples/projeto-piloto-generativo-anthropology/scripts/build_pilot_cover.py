#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "assets" / "capas" / "en-anthropology-base-generativa-v1.png"
FRONT = ROOT / "publicacao" / "capas" / "en-anthropology-capa-frontal-piloto-v2.png"
COMPLETE = ROOT / "publicacao" / "capas" / "en-anthropology-capa-completa-uiclap-piloto-v2.jpg"
PREVIEW = ROOT / "publicacao" / "capas" / "en-anthropology-capa-completa-uiclap-piloto-v2-preview-validacao.jpg"
METADATA = ROOT / "publicacao" / "capas" / "metadata-v2.json"

TITLE = "Anthropology"
SUBTITLE = "The Externalization of the Essence of Man"
AUTHOR = "Josué Amaral"
SOURCE_PDF = (
    "/home/josue/Documents/josue-writter-workspace/books/final-public-pdf/en/"
    "Anthropology - By Josué Amaral, in progress since 08_13_19, A5 paper.pdf"
)

W, H = 7559, 5197
BACK_W = 3591
SPINE_W = 378
FRONT_W = W - BACK_W - SPINE_W
SPINE_X = BACK_W
FRONT_X = BACK_W + SPINE_W
DPI = 600

FONT_SERIF = Path("/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf")
FONT_SERIF_BOLD = Path("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf")
FONT_SANS = Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
FONT_SANS_BOLD = Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")


def font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(path), size)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def cover_crop(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    target_w, target_h = size
    src_w, src_h = image.size
    scale = max(target_w / src_w, target_h / src_h)
    resized = image.resize((round(src_w * scale), round(src_h * scale)), Image.LANCZOS)
    left = (resized.width - target_w) // 2
    top = (resized.height - target_h) // 2
    return resized.crop((left, top, left + target_w, top + target_h))


def draw_vertical_gradient(
    im: Image.Image,
    top_rgba: tuple[int, int, int, int],
    bottom_rgba: tuple[int, int, int, int],
) -> None:
    overlay = Image.new("RGBA", im.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    for y in range(im.height):
        t = y / max(1, im.height - 1)
        color = tuple(round(top_rgba[i] * (1 - t) + bottom_rgba[i] * t) for i in range(4))
        draw.line((0, y, im.width, y), fill=color)
    im.alpha_composite(overlay)


def draw_box_text(
    draw: ImageDraw.ImageDraw,
    text: str,
    xy: tuple[int, int],
    max_width: int,
    font_obj: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int, int],
    line_spacing: float = 1.18,
) -> int:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = word if not current else f"{current} {word}"
        if draw.textbbox((0, 0), candidate, font=font_obj)[2] <= max_width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)

    x, y = xy
    step = round(font_obj.size * line_spacing)
    for line in lines:
        draw.text((x, y), line, font=font_obj, fill=fill)
        y += step
    return y


def fit_title(draw: ImageDraw.ImageDraw, text: str, max_width: int, start_size: int) -> ImageFont.FreeTypeFont:
    size = start_size
    while size > 90:
        f = font(FONT_SERIF_BOLD, size)
        if draw.textbbox((0, 0), text, font=f)[2] <= max_width:
            return f
        size -= 6
    return font(FONT_SERIF_BOLD, size)


def add_front_typography(front: Image.Image) -> Image.Image:
    front = front.convert("RGBA")
    draw_vertical_gradient(front, (7, 13, 15, 88), (5, 7, 8, 185))
    draw = ImageDraw.Draw(front)

    margin_x = 250
    max_w = front.width - 2 * margin_x
    title_font = fit_title(draw, TITLE, max_w, 330)
    subtitle_font = font(FONT_SERIF, 92)
    author_font = font(FONT_SERIF_BOLD, 118)

    title_bbox = draw.textbbox((0, 0), TITLE, font=title_font)
    title_x = (front.width - (title_bbox[2] - title_bbox[0])) // 2
    title_y = 650
    shadow = (0, 0, 0, 190)
    draw.text((title_x + 8, title_y + 8), TITLE, font=title_font, fill=shadow)
    draw.text((title_x, title_y), TITLE, font=title_font, fill=(248, 241, 224, 255))

    sub_bbox = draw.textbbox((0, 0), SUBTITLE, font=subtitle_font)
    sub_x = (front.width - (sub_bbox[2] - sub_bbox[0])) // 2
    sub_y = title_y + title_font.size + 42
    draw.text((sub_x + 4, sub_y + 4), SUBTITLE, font=subtitle_font, fill=shadow)
    draw.text((sub_x, sub_y), SUBTITLE, font=subtitle_font, fill=(224, 177, 105, 255))

    line_y = sub_y + subtitle_font.size + 75
    draw.line((front.width // 2 - 520, line_y, front.width // 2 + 520, line_y), fill=(218, 169, 96, 210), width=6)
    draw.ellipse((front.width // 2 - 12, line_y - 12, front.width // 2 + 12, line_y + 12), fill=(248, 230, 180, 255))

    author_bbox = draw.textbbox((0, 0), AUTHOR, font=author_font)
    author_x = (front.width - (author_bbox[2] - author_bbox[0])) // 2
    author_y = front.height - 620
    draw.text((author_x + 5, author_y + 5), AUTHOR, font=author_font, fill=shadow)
    draw.text((author_x, author_y), AUTHOR, font=author_font, fill=(248, 241, 224, 255))

    return front.convert("RGB")


def add_back_cover(canvas: Image.Image, base_art: Image.Image) -> None:
    back = cover_crop(base_art, (BACK_W, H)).convert("RGBA")
    back = back.filter(ImageFilter.GaussianBlur(8))
    back = ImageEnhance.Brightness(back).enhance(0.40)
    back = ImageEnhance.Contrast(back).enhance(0.85)
    panel = Image.new("RGBA", back.size, (10, 13, 12, 150))
    back.alpha_composite(panel)
    canvas.paste(back.convert("RGB"), (0, 0))

    draw = ImageDraw.Draw(canvas)
    title_font = font(FONT_SANS_BOLD, 118)
    body_font = font(FONT_SERIF, 82)
    quote_font = font(FONT_SERIF, 100)
    small_font = font(FONT_SANS, 52)

    x = 285
    y = 430
    gold = (220, 164, 85)
    paper = (245, 239, 224)
    muted = (222, 213, 196)
    draw.text((x, y), "About this book", font=title_font, fill=gold)
    y += 190
    draw.text((x, y), "Anthropology - By Josué Amaral", font=small_font, fill=paper)
    y += 170

    quote = "Human beings leave traces because they transform the world and are transformed by it."
    draw_box_text(draw, f"“{quote}”", (x, y), BACK_W - 2 * x, quote_font, (236, 197, 136), 1.15)
    y += 520

    paragraphs = [
        (
            "This volume presents anthropology as the study of how human essence becomes visible "
            "through culture, language, work, memory, institutions, technology, and social life."
        ),
        (
            "From everyday coexistence to the organization of civilizations, the book follows a "
            "central question: how do human beings create meaning while also being shaped by the "
            "societies they build?"
        ),
        (
            "The work invites the reader to connect individual experience with the broad history "
            "of collective life, treating culture not as ornament, but as evidence of human "
            "presence."
        ),
    ]
    for para in paragraphs:
        y = draw_box_text(draw, para, (x, y), BACK_W - 2 * x, body_font, muted, 1.24)
        y += 92

    barcode = (BACK_W - 1650, H - 660, BACK_W - 520, H - 280)
    draw.rounded_rectangle(barcode, radius=14, fill=(248, 247, 242), outline=(206, 156, 88), width=6)
    draw.text((barcode[0] + 70, barcode[1] + 135), "Barcode / ISBN area", font=small_font, fill=(62, 56, 47))


def add_spine(canvas: Image.Image) -> None:
    draw = ImageDraw.Draw(canvas)
    draw.rectangle((SPINE_X, 0, SPINE_X + SPINE_W, H), fill=(8, 10, 10))
    draw.line((SPINE_X + 20, 75, SPINE_X + 20, H - 75), fill=(217, 156, 74), width=5)
    draw.line((SPINE_X + SPINE_W - 20, 75, SPINE_X + SPINE_W - 20, H - 75), fill=(217, 156, 74), width=5)

    spine_text = "Anthropology - Josué Amaral"
    spine_font = font(FONT_SANS_BOLD, 86)
    temp = Image.new("RGBA", (H, SPINE_W), (0, 0, 0, 0))
    d = ImageDraw.Draw(temp)
    bbox = d.textbbox((0, 0), spine_text, font=spine_font)
    d.text(
        ((H - (bbox[2] - bbox[0])) // 2, (SPINE_W - (bbox[3] - bbox[1])) // 2 - 6),
        spine_text,
        font=spine_font,
        fill=(246, 239, 224, 255),
    )
    rotated = temp.rotate(270, expand=True)
    canvas.paste(rotated.convert("RGB"), (SPINE_X, 0), rotated)


def add_preview_guides(image: Image.Image) -> Image.Image:
    preview = image.copy()
    draw = ImageDraw.Draw(preview)
    red = (238, 38, 43)
    blue = (98, 198, 218)
    safe = 236
    bleed = 118
    draw.rectangle((0, 0, W - 1, H - 1), outline=(244, 196, 146), width=20)
    draw.rectangle((safe, safe, W - safe, H - safe), outline=blue, width=12)
    draw.rectangle((bleed, bleed, W - bleed, H - bleed), outline=(182, 229, 238), width=8)
    draw.line((SPINE_X, 0, SPINE_X, H), fill=red, width=10)
    draw.line((SPINE_X + SPINE_W, 0, SPINE_X + SPINE_W, H), fill=red, width=10)
    return preview


def main() -> None:
    base = Image.open(BASE).convert("RGB")
    canvas = Image.new("RGB", (W, H), (12, 13, 12))
    add_back_cover(canvas, base)
    add_spine(canvas)
    front_base = cover_crop(base, (FRONT_W, H))
    front = add_front_typography(front_base)
    canvas.paste(front, (FRONT_X, 0))

    front.save(FRONT, dpi=(DPI, DPI))
    canvas.save(COMPLETE, quality=95, dpi=(DPI, DPI), subsampling=1)
    add_preview_guides(canvas).save(PREVIEW, quality=92, dpi=(DPI, DPI), subsampling=1)

    metadata = {
        "status": "piloto_generativo_revisavel_nao_final",
        "created_at": "2026-07-19T00:00:00-03:00",
        "book": {
            "title": TITLE,
            "subtitle": SUBTITLE,
            "author": AUTHOR,
            "language": "en",
            "source_pdf": SOURCE_PDF,
            "source_pdf_pages": 23,
            "format": "A5",
        },
        "uiclap_cover_layout": {
            "dpi": DPI,
            "total_px": [W, H],
            "total_mm_from_reference": [320, 220],
            "back_px": [BACK_W, H],
            "spine_px": [SPINE_W, H],
            "front_px": [FRONT_W, H],
            "bleed_mm": 5,
            "safety_margin_mm": 10,
            "spine_mm": 16,
            "spine_note": "Spine follows the user's UICLAP reference image for this pilot; confirm official spine after final interior upload/page count.",
        },
        "methodology": [
            "AI-generated textless front cover base art",
            "local deterministic typography and complete-cover composition",
            "separate files for base art, front cover, complete UICLAP cover, and validation preview",
        ],
        "files": {
            "base_art": BASE.name,
            "front_cover": FRONT.name,
            "complete_cover": COMPLETE.name,
            "validation_preview": PREVIEW.name,
        },
        "sha256": {
            "base_art": sha256(BASE),
            "front_cover": sha256(FRONT),
            "complete_cover": sha256(COMPLETE),
            "validation_preview": sha256(PREVIEW),
        },
    }
    METADATA.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
