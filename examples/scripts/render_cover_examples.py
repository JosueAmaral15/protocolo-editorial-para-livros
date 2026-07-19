#!/usr/bin/env python3
"""Render deterministic book-cover examples for the editorial protocol repo."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


REPO_ROOT = Path(__file__).resolve().parents[2]
EXAMPLES_DIR = REPO_ROOT / "examples"
DPI = 300
FRONT_W = 1748
HEIGHT = 2480
SPINE_W = 140
FLAP_W = 620
SAFE = 95

FONT_SERIF = Path("/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf")
FONT_SERIF_BOLD = Path("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf")
FONT_SANS = Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
FONT_SANS_BOLD = Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")


@dataclass(frozen=True)
class CoverSpec:
    slug: str
    title: str
    subtitle: str
    author: str
    genre: str
    front_tag: str
    back_copy: list[str]
    flap_left: str
    flap_right: str
    palette: tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]


SPECS = {
    "projeto-livro-academico-uiclap": CoverSpec(
        slug="projeto-livro-academico-uiclap",
        title="Projeto Academico UICLAP",
        subtitle="Exemplo tecnico de miolo, capa e validacao",
        author="Nome do Autor",
        genre="academic nonfiction",
        front_tag="A5 example",
        back_copy=[
            "Este exemplo mostra como separar miolo, capa frontal, contracapa, lombada e arquivos de validacao.",
            "A estrutura foi pensada para livros academicos, tecnicos e ensaisticos que precisam de rastreabilidade editorial.",
            "Use este modelo como ponto de partida para adaptar medidas, texto de contracapa, ISBN e exigencias da plataforma.",
        ],
        flap_left="Orelha editorial: apresentar o projeto, sua tese central e o pacto de leitura do livro.",
        flap_right="Orelha do autor: incluir mini bio, credenciais relevantes e convite para outras obras.",
        palette=((20, 44, 57), (218, 179, 109), (232, 238, 236)),
    ),
    "projeto-romance-com-orelhas": CoverSpec(
        slug="projeto-romance-com-orelhas",
        title="A Casa Sobre o Vale",
        subtitle="Exemplo de romance com capa completa e orelhas",
        author="Nome do Autor",
        genre="fiction",
        front_tag="Romance example",
        back_copy=[
            "Uma casa antiga observa o vale enquanto uma familia tenta reconstruir o que o tempo deixou em silencio.",
            "Este exemplo demonstra uma capa literaria com contracapa, lombada e orelhas em uma unica arte externa.",
            "A prova e tecnica: a arte final de venda deve ser curada, revisada e aprovada visualmente.",
        ],
        flap_left="Na orelha esquerda, apresente a atmosfera do romance e uma frase de impacto.",
        flap_right="Na orelha direita, apresente o autor, a serie ou outros livros relacionados.",
        palette=((55, 40, 62), (204, 133, 90), (242, 232, 210)),
    ),
}


def font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(path), size)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def blend(a: tuple[int, int, int], b: tuple[int, int, int], t: float) -> tuple[int, int, int]:
    return tuple(round(a[i] * (1.0 - t) + b[i] * t) for i in range(3))


def gradient(size: tuple[int, int], top: tuple[int, int, int], bottom: tuple[int, int, int]) -> Image.Image:
    image = Image.new("RGB", size, top)
    draw = ImageDraw.Draw(image)
    for y in range(size[1]):
        t = y / max(1, size[1] - 1)
        draw.line((0, y, size[0], y), fill=blend(top, bottom, t))
    return image


def text_width(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont) -> int:
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0]


def wrap_text(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    line = ""
    for word in words:
        candidate = word if not line else f"{line} {word}"
        if text_width(draw, candidate, fnt) <= max_width:
            line = candidate
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def draw_centered(
    draw: ImageDraw.ImageDraw,
    text: str,
    y: int,
    fnt: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int],
    max_width: int,
    line_step: int | None = None,
) -> int:
    lines = wrap_text(draw, text, fnt, max_width)
    step = line_step or round(fnt.size * 1.15)
    for line in lines:
        x = (FRONT_W - text_width(draw, line, fnt)) // 2
        draw.text((x + 4, y + 4), line, font=fnt, fill=(0, 0, 0))
        draw.text((x, y), line, font=fnt, fill=fill)
        y += step
    return y


def draw_front(spec: CoverSpec) -> Image.Image:
    dark, accent, paper = spec.palette
    image = gradient((FRONT_W, HEIGHT), blend(dark, (0, 0, 0), 0.15), blend(dark, accent, 0.45))
    draw = ImageDraw.Draw(image)

    for i in range(10):
        radius = 220 + i * 130
        color = blend(accent, paper, i / 12)
        box = (FRONT_W // 2 - radius, 560 - radius, FRONT_W // 2 + radius, 560 + radius)
        draw.ellipse(box, outline=color, width=3)

    for i in range(18):
        x = 160 + i * 95
        y = 1290 + round(95 * math.sin(i * 0.8))
        draw.line((x, y, x + 160, y - 180), fill=blend(accent, paper, 0.25), width=5)
        draw.ellipse((x - 12, y - 12, x + 12, y + 12), fill=paper)

    draw.rectangle((115, 115, FRONT_W - 115, HEIGHT - 115), outline=accent, width=9)
    draw.rectangle((155, 155, FRONT_W - 155, HEIGHT - 155), outline=blend(paper, accent, 0.25), width=3)

    y = 420
    y = draw_centered(draw, spec.title, y, font(FONT_SERIF_BOLD, 132), paper, FRONT_W - 260, 150)
    y += 25
    y = draw_centered(draw, spec.subtitle, y, font(FONT_SERIF, 48), accent, FRONT_W - 380, 62)
    draw.line((FRONT_W // 2 - 260, y + 45, FRONT_W // 2 + 260, y + 45), fill=accent, width=5)
    draw.ellipse((FRONT_W // 2 - 10, y + 35, FRONT_W // 2 + 10, y + 55), fill=paper)

    draw_centered(draw, spec.author, HEIGHT - 420, font(FONT_SERIF_BOLD, 72), paper, FRONT_W - 300)
    draw_centered(draw, spec.front_tag, HEIGHT - 290, font(FONT_SANS, 32), accent, FRONT_W - 300)
    return image


def draw_text_block(
    draw: ImageDraw.ImageDraw,
    text: str,
    box: tuple[int, int, int, int],
    fnt: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int],
    line_step: int | None = None,
) -> int:
    x1, y1, x2, _ = box
    y = y1
    for line in wrap_text(draw, text, fnt, x2 - x1):
        draw.text((x1, y), line, font=fnt, fill=fill)
        y += line_step or round(fnt.size * 1.28)
    return y


def draw_back_panel(spec: CoverSpec, size: tuple[int, int]) -> Image.Image:
    dark, accent, paper = spec.palette
    image = gradient(size, blend(dark, (0, 0, 0), 0.25), dark)
    draw = ImageDraw.Draw(image)
    draw.rectangle((110, 110, size[0] - 110, size[1] - 110), outline=accent, width=7)
    draw.text((170, 230), "Sobre este livro", font=font(FONT_SANS_BOLD, 58), fill=accent)

    y = 380
    for paragraph in spec.back_copy:
        y = draw_text_block(draw, paragraph, (170, y, size[0] - 170, size[1] - 700), font(FONT_SERIF, 42), paper)
        y += 70

    barcode = (size[0] - 690, size[1] - 420, size[0] - 170, size[1] - 220)
    draw.rounded_rectangle(barcode, radius=12, fill=(246, 244, 238), outline=accent, width=4)
    draw.text((barcode[0] + 48, barcode[1] + 78), "ISBN / barcode", font=font(FONT_SANS, 28), fill=(55, 55, 55))
    return image


def draw_flap(spec: CoverSpec, text: str, side: str) -> Image.Image:
    dark, accent, paper = spec.palette
    image = gradient((FLAP_W, HEIGHT), blend(dark, accent, 0.16), blend(dark, (0, 0, 0), 0.08))
    draw = ImageDraw.Draw(image)
    draw.rectangle((70, 120, FLAP_W - 70, HEIGHT - 120), outline=blend(accent, paper, 0.25), width=5)
    draw.text((105, 230), side, font=font(FONT_SANS_BOLD, 38), fill=accent)
    draw_text_block(draw, text, (105, 350, FLAP_W - 105, HEIGHT - 220), font(FONT_SERIF, 34), paper)
    return image


def draw_spine(spec: CoverSpec) -> Image.Image:
    dark, accent, paper = spec.palette
    image = Image.new("RGB", (SPINE_W, HEIGHT), blend(dark, (0, 0, 0), 0.35))
    draw = ImageDraw.Draw(image)
    draw.line((24, 100, 24, HEIGHT - 100), fill=accent, width=4)
    draw.line((SPINE_W - 24, 100, SPINE_W - 24, HEIGHT - 100), fill=accent, width=4)
    label = f"{spec.title} - {spec.author}"
    fnt = font(FONT_SANS_BOLD, 38)
    temp = Image.new("RGBA", (HEIGHT, SPINE_W), (0, 0, 0, 0))
    tdraw = ImageDraw.Draw(temp)
    x = (HEIGHT - text_width(tdraw, label, fnt)) // 2
    tdraw.text((x, 46), label, font=fnt, fill=paper + (255,))
    rotated = temp.rotate(270, expand=True)
    image.paste(rotated.convert("RGB"), (0, 0), rotated)
    return image


def add_guides(image: Image.Image, panels: list[int]) -> Image.Image:
    preview = image.copy()
    draw = ImageDraw.Draw(preview)
    draw.rectangle((0, 0, preview.width - 1, preview.height - 1), outline=(245, 177, 94), width=14)
    draw.rectangle((SAFE, SAFE, preview.width - SAFE, preview.height - SAFE), outline=(65, 190, 210), width=8)
    for x in panels:
        draw.line((x, 0, x, preview.height), fill=(235, 40, 48), width=6)
    return preview


def save_image(image: Image.Image, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    kwargs = {"dpi": (DPI, DPI)}
    if path.suffix.lower() in {".jpg", ".jpeg"}:
        image.save(path, quality=94, subsampling=1, **kwargs)
    else:
        image.save(path, **kwargs)


def render_project(spec: CoverSpec) -> dict[str, object]:
    project = EXAMPLES_DIR / spec.slug
    assets = project / "assets" / "capas"
    output = project / "publicacao" / "capas"
    assets.mkdir(parents=True, exist_ok=True)
    output.mkdir(parents=True, exist_ok=True)

    front = draw_front(spec)
    back = draw_back_panel(spec, (FRONT_W, HEIGHT))
    spine = draw_spine(spec)
    left_flap = draw_flap(spec, spec.flap_left, "Orelha esquerda")
    right_flap = draw_flap(spec, spec.flap_right, "Orelha direita")

    base_path = assets / f"{spec.slug}-arte-base-tecnica-v1.png"
    front_path = output / f"{spec.slug}-capa-frontal-exemplo.png"
    complete_path = output / f"{spec.slug}-capa-lombada-contracapa-exemplo.jpg"
    complete_preview_path = output / f"{spec.slug}-capa-lombada-contracapa-preview-validacao.jpg"
    flap_path = output / f"{spec.slug}-capa-lombada-contracapa-orelhas-exemplo.jpg"
    flap_preview_path = output / f"{spec.slug}-capa-lombada-contracapa-orelhas-preview-validacao.jpg"

    complete = Image.new("RGB", (FRONT_W * 2 + SPINE_W, HEIGHT), (0, 0, 0))
    complete.paste(back, (0, 0))
    complete.paste(spine, (FRONT_W, 0))
    complete.paste(front, (FRONT_W + SPINE_W, 0))

    with_flaps = Image.new("RGB", (FLAP_W * 2 + FRONT_W * 2 + SPINE_W, HEIGHT), (0, 0, 0))
    x = 0
    with_flaps.paste(left_flap, (x, 0))
    x += FLAP_W
    with_flaps.paste(back, (x, 0))
    x += FRONT_W
    with_flaps.paste(spine, (x, 0))
    x += SPINE_W
    with_flaps.paste(front, (x, 0))
    x += FRONT_W
    with_flaps.paste(right_flap, (x, 0))

    save_image(front, base_path)
    save_image(front, front_path)
    save_image(complete, complete_path)
    save_image(add_guides(complete, [FRONT_W, FRONT_W + SPINE_W]), complete_preview_path)
    save_image(with_flaps, flap_path)
    save_image(
        add_guides(with_flaps, [FLAP_W, FLAP_W + FRONT_W, FLAP_W + FRONT_W + SPINE_W, FLAP_W + FRONT_W + SPINE_W + FRONT_W]),
        flap_preview_path,
    )

    files = {
        "base_art": base_path.relative_to(project).as_posix(),
        "front_cover": front_path.relative_to(project).as_posix(),
        "complete_cover": complete_path.relative_to(project).as_posix(),
        "complete_cover_preview": complete_preview_path.relative_to(project).as_posix(),
        "complete_cover_with_flaps": flap_path.relative_to(project).as_posix(),
        "complete_cover_with_flaps_preview": flap_preview_path.relative_to(project).as_posix(),
    }
    metadata = {
        "status": "exemplo_tecnico_didatico_nao_final",
        "created_at": "2026-07-19T00:00:00-03:00",
        "book": {
            "title": spec.title,
            "subtitle": spec.subtitle,
            "author": spec.author,
            "genre": spec.genre,
            "slug": spec.slug,
        },
        "dimensions": {
            "front_px": [FRONT_W, HEIGHT],
            "spine_px": [SPINE_W, HEIGHT],
            "flap_px": [FLAP_W, HEIGHT],
            "complete_px": [complete.width, complete.height],
            "complete_with_flaps_px": [with_flaps.width, with_flaps.height],
            "dpi": DPI,
            "spine_status": "estimativa_nao_final",
            "platform_note": "Example dimensions for protocol learning. Confirm real printer/platform template before production.",
        },
        "files": files,
        "sha256": {key: sha256(project / value) for key, value in files.items()},
    }
    metadata_path = output / "metadata-capas.json"
    metadata_path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return metadata


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", choices=["all", *sorted(SPECS)], default="all")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    slugs = sorted(SPECS) if args.project == "all" else [args.project]
    for slug in slugs:
        metadata = render_project(SPECS[slug])
        print(f"generated: {slug}")
        for role, path in metadata["files"].items():
            print(f"  {role}: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
