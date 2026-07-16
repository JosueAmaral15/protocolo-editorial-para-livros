#!/usr/bin/env python3
"""Create a book project from the editorial template."""

from __future__ import annotations

import argparse
import shutil
import sys
import unicodedata
from datetime import date
from pathlib import Path


TEMPLATE_DIR = Path(__file__).resolve().parent / "book-project-template"
TEXT_SUFFIXES = {
    ".md",
    ".txt",
    ".yml",
    ".yaml",
    ".json",
    ".tex",
    ".py",
    ".gitignore",
}


def slugify(value: str) -> str:
    """Return a filesystem-friendly slug using ASCII characters."""
    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii")
    chars: list[str] = []
    previous_dash = False

    for char in ascii_value.lower():
        if char.isalnum():
            chars.append(char)
            previous_dash = False
        elif not previous_dash:
            chars.append("-")
            previous_dash = True

    slug = "".join(chars).strip("-")
    return slug or "livro"


def build_placeholders(args: argparse.Namespace, slug: str) -> dict[str, str]:
    today = date.today().isoformat()
    return {
        "{{BOOK_TITLE}}": args.title,
        "{{BOOK_SLUG}}": slug,
        "{{AUTHOR}}": args.author,
        "{{GENRE}}": args.genre,
        "{{LANGUAGE}}": args.language,
        "{{STATUS_EDITORIAL}}": args.status,
        "{{FORMAT_TARGET}}": args.format_target,
        "{{YYYY-MM-DD}}": today,
    }


def render_text(text: str, placeholders: dict[str, str]) -> str:
    for marker, replacement in placeholders.items():
        text = text.replace(marker, replacement)
    return text


def is_text_file(path: Path) -> bool:
    if path.name == ".gitignore":
        return True
    return path.suffix.lower() in TEXT_SUFFIXES


def copy_template(target: Path, placeholders: dict[str, str]) -> None:
    for source in sorted(TEMPLATE_DIR.rglob("*")):
        relative = source.relative_to(TEMPLATE_DIR)
        destination = target / relative

        if source.is_dir():
            destination.mkdir(parents=True, exist_ok=True)
            continue

        destination.parent.mkdir(parents=True, exist_ok=True)

        if is_text_file(source):
            try:
                text = source.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                shutil.copy2(source, destination)
            else:
                destination.write_text(render_text(text, placeholders), encoding="utf-8")
        else:
            shutil.copy2(source, destination)


def create_starter_manuscript(target: Path, title: str, slug: str) -> None:
    manuscript = target / "manuscrito" / "trabalho" / f"{slug}.md"
    if manuscript.exists():
        return
    manuscript.write_text(
        f"# {title}\n\n"
        "## Nota de trabalho\n\n"
        "Este e o manuscrito inicial do livro. Substitua esta nota pelo texto da obra "
        "ou registre aqui a rota para o arquivo-fonte principal.\n",
        encoding="utf-8",
    )


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a structured book project from templates/book-project-template.",
    )
    parser.add_argument("title", help="Book title.")
    parser.add_argument(
        "--target-dir",
        type=Path,
        default=Path.cwd(),
        help="Parent directory where the project folder will be created. Default: current directory.",
    )
    parser.add_argument("--slug", help="Project folder name. Default: slug generated from title.")
    parser.add_argument("--author", default="A definir", help="Author name.")
    parser.add_argument("--genre", default="A definir", help="Book genre.")
    parser.add_argument("--language", default="pt", help="Base language, for example pt or en.")
    parser.add_argument("--status", default="em desenvolvimento", help="Editorial status.")
    parser.add_argument("--format-target", default="A5", help="Target format, for example A5 or A4.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be created without writing files.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])

    if not TEMPLATE_DIR.is_dir():
        print(f"Template directory not found: {TEMPLATE_DIR}", file=sys.stderr)
        return 2

    slug = args.slug or slugify(args.title)
    target_parent = args.target_dir.expanduser().resolve()
    target = target_parent / slug

    if target.exists() and not target.is_dir():
        print(f"Target already exists and is not a directory: {target}", file=sys.stderr)
        return 1

    if target.exists() and any(target.iterdir()):
        print(f"Target already exists and is not empty: {target}", file=sys.stderr)
        return 1

    if args.dry_run:
        print(f"Template: {TEMPLATE_DIR}")
        print(f"Target:   {target}")
        print(f"Title:    {args.title}")
        print(f"Slug:     {slug}")
        print("No files written because --dry-run was used.")
        return 0

    placeholders = build_placeholders(args, slug)
    target.mkdir(parents=True, exist_ok=True)
    copy_template(target, placeholders)
    create_starter_manuscript(target, args.title, slug)

    print(f"Book project created: {target}")
    print(f"Main manuscript: {target / 'manuscrito' / 'trabalho' / (slug + '.md')}")
    print("Next step: fill README.md, docs/TASKS.md and history-chat.md.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
