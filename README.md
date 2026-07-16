# Editorial Protocol for Book Projects

Methodology, project structure, and tools for organizing books with AI assistance while preserving authorship, editorial traceability, revision history, and publication readiness.

This repository is designed as a dedicated protocol project, separated from individual books and manuscripts.

## Purpose

This project provides a reusable standard for creating, revising, validating, and publishing editorial projects, including:

- fiction books;
- novels;
- reportage and journalistic books;
- academic books;
- articles;
- essays;
- technical books;
- works being prepared for publishing platforms such as UICLAP.

## Quick Start

Create a new book project from the template:

```bash
python3 templates/create_book_project.py "My Book" --author "Author Name" --genre "novel" --language en --target-dir .
```

Preview the operation without writing files:

```bash
python3 templates/create_book_project.py "My Book" --dry-run
```

## Languages

- Portuguese protocol: [pt/PROTOCOLO_EDITORIAL_LIVROS.md](pt/PROTOCOLO_EDITORIAL_LIVROS.md)
- English protocol: [en/EDITORIAL_BOOK_PROTOCOL.md](en/EDITORIAL_BOOK_PROTOCOL.md)

Each language directory has its own `README.md`.

## Repository Structure

```text
.
├── README.md
├── LICENSE
├── history-chat.md
├── docs/
│   ├── DECISIONS.md
│   ├── GLOBAL_HISTORY_EXTRACT.md
│   ├── README.md
│   ├── TASKS.md
│   └── VALIDATION.md
├── pt/
│   ├── README.md
│   └── PROTOCOLO_EDITORIAL_LIVROS.md
├── en/
│   ├── README.md
│   └── EDITORIAL_BOOK_PROTOCOL.md
└── templates/
    ├── README.md
    ├── create_book_project.py
    └── book-project-template/
```

## Relation to the Simplicity Protocols

This repository was inspired by the organization of the `protocolos-simplicidade` project, but it is adapted for books and editorial work.

The core idea is the same: clear documentation, project history, traceable tasks, justified decisions, and objective validation before claiming that a deliverable is ready.

Important adaptation:

- documentation Markdown belongs in `docs/`;
- manuscript Markdown belongs in `manuscrito/`, `working/`, or an equivalent manuscript folder inside each book project.

## Book Project Standard

A generated book project includes:

- `README.md`: entry point for the book project;
- `history-chat.md`: project-specific AI/human work memory;
- `docs/`: editorial tasks, decisions, style, structure, validation, and references;
- `manuscrito/`: original, working, revised, and final manuscript sources;
- `assets/`: images, covers, fonts, QR codes, and supporting assets;
- `scripts/`: conversion, validation, and publication automation;
- `build/`: reconstructible intermediate files;
- `publicacao/`: PDF, DOCX, EPUB, Markdown, LaTeX, and publication metadata;
- `backups/`: dated backups before risky changes;
- `old/`: old versions kept for historical reference.

## Generator

The generator is available at:

```text
templates/create_book_project.py
```

It copies `templates/book-project-template/`, replaces placeholders, and creates an initial manuscript file in `manuscrito/trabalho/`.

## Validation

Recommended validation before publishing a generated or revised book:

```bash
unzip -t "publicacao/docx/book.docx"
unzip -t "publicacao/epub/book.epub"
pdfinfo "publicacao/pdf/book.pdf"
pdftotext "publicacao/pdf/book.pdf" -
```

Also search for residual markers:

```bash
rg -n "TODO|FIXME|PLACEHOLDER|ChatGPT|texto-base|revisar depois" manuscrito docs publicacao || true
```

## License

MIT License. See [LICENSE](LICENSE).

## Current Status

First public repository version prepared with Portuguese and English protocol documentation, MIT license, template, and Python generator.

