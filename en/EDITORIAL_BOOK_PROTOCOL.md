# Editorial Book Protocol

## Mandatory Instruction for AI Assistants

Before modifying a book project, read:

1. `README.md`;
2. `history-chat.md`;
3. relevant documents in `docs/`;
4. `global-history-chat.md`, when it exists in the parent folder;
5. the manuscript source identified by the README.

Do not claim that a book is ready without objective validation of the final artifacts.

## Core Philosophy

A book is a long-term project. It needs preserved authorship, clear history, navigable structure, recorded decisions, human review, and final artifacts that can be validated.

AI work should help the author organize, revise, explain, strengthen, and validate the text without erasing authorship or turning a long work into a short synthesis when the request is professional editorial revision.

## Required Project Structure

```text
book-name/
├── README.md
├── history-chat.md
├── docs/
├── manuscrito/
├── assets/
├── scripts/
├── build/
├── publicacao/
├── backups/
└── old/
```

## Folder Rules

- `README.md`: explains the book, status, main source, commands, and validations.
- `history-chat.md`: records project-specific book memory.
- `docs/`: stores tasks, decisions, style, structure, references, and validation.
- `manuscrito/`: stores original, working, revised, and final manuscript sources.
- `assets/`: stores images, covers, fonts, and QR codes.
- `scripts/`: stores automation scripts.
- `build/`: stores reconstructible intermediate files.
- `publicacao/`: stores PDF, DOCX, EPUB, and other final artifacts.
- `backups/`: stores copies made before risky changes.
- `old/`: stores old versions that are no longer the main source.

## Markdown Rule

Documentation Markdown belongs in `docs/`.

Manuscript Markdown belongs in `manuscrito/`, `working/`, or an equivalent manuscript folder.

This distinction is essential because editorial process documentation must not be confused with the book text itself.

## Work Cycle

1. Read documentation and history.
2. Identify the main source.
3. Register a plan or task when the change is relevant.
4. Create a backup before risky changes.
5. Edit the manuscript source or structural files.
6. Update `history-chat.md`.
7. Regenerate affected public artifacts.
8. Validate PDF, DOCX, EPUB, and metadata.
9. Register pending human-review items.

## Minimum Validation

Use commands such as:

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

## Work Types

### Fiction and Novels

Add when needed:

- `docs/CHARACTERS.md`;
- `docs/CONTINUITY.md`;
- `docs/TIMELINE.md`;
- `docs/WORLD-BUILDING.md`;
- `docs/PLOT-THREADS.md`.

### Reportage and Journalism

Add when needed:

- `docs/SOURCES.md`;
- `docs/FACT-CHECK.md`;
- `docs/INTERVIEWS.md`;
- `docs/RIGHTS-AND-PERMISSIONS.md`;
- `docs/LEGAL-REVIEW.md`.

### Academic Books, Articles, and Essays

Add when needed:

- `docs/METHODOLOGY.md`;
- `docs/CITATION-STYLE.md`;
- `docs/BIBLIOGRAPHY.md`;
- `docs/ARGUMENT-MAP.md`;
- `docs/PEER-REVIEW-NOTES.md`.

### Technical and Didactic Books

Add when needed:

- `docs/EXAMPLES.md`;
- `docs/EXERCISES.md`;
- `docs/ERRATA.md`;
- `docs/GLOSSARY.md`;
- `docs/TECHNICAL-VALIDATION.md`.

## Editorial Readiness

A book can be considered ready for final human review when:

- the manuscript source is defined;
- major decisions are recorded;
- public artifacts have been regenerated;
- PDF, DOCX, and EPUB have passed technical validation;
- cover, table of contents, margins, images, and final page have been checked;
- human-review pending items are documented;
- local history is updated.

## Generator Usage

```bash
python3 templates/create_book_project.py "My Book" --author "Author Name" --genre "novel" --language en --target-dir .
```

The generator creates a book project with a standardized editorial structure.

