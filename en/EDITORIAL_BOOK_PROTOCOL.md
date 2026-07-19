# Editorial Book Protocol

## Mandatory Instruction for AI Assistants

Before modifying a book project, read:

1. `README.md`;
2. `history-chat.md`;
3. relevant documents in `docs/`;
4. `global-history-chat.md`, when it exists in the parent folder;
5. `legacy/global-history-chat.md`, when the raw global history has been archived in this repository;
6. the manuscript source identified by the README.

Do not claim that a book is ready without objective validation of the final artifacts.

## Core Philosophy

A book is a long-term project. It needs preserved authorship, clear history, navigable structure, recorded decisions, human review, and final artifacts that can be validated.

AI work should help the author organize, revise, explain, strengthen, and validate the text without erasing authorship or turning a long work into a short synthesis when the request is professional editorial revision.

Raw conversation history and reusable lessons may be preserved under `legacy/`, but the active operating rules should be consolidated in this protocol and in `docs/`. The protocol must not depend on implicit conversation memory.

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
- `global-history-chat.md`: when present in a parent folder, records reusable cross-book lessons, not book-specific changes.
- `legacy/`: stores raw histories, old extracts, and audit material that must be preserved but must not be confused with current operational sources.
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

## Consolidated Rules From The Global History

### History And Authorship

- The local `history-chat.md` records decisions, actions, validations, pending work, and risks for one specific book.
- The global or archived history records reusable lessons across books, such as workflows, scripts, warnings, technical limits, and editorial standards.
- Before editing important files, register the intent when the change is relevant; afterwards, register what was actually done and validated.
- Never overwrite originals by default. Create `backups/`, `old/`, or a separate working folder before risky changes.

### Editorial Rewriting

- Professional rewriting is not a short summary. It must preserve broad coverage of the original while improving clarity, grammar, structure, didactic progression, references, and reading experience.
- Before rewriting a long work, create a coverage map: every relevant block, thesis, example, or chapter from the original needs an explicit editorial destination.
- Cut only real repetition, serious error, corrupted translation, unrecoverable noise, or out-of-scope material. Authorial theses, values, and arguments must be preserved and explained better.
- Strengthen defensible arguments and explicitly correct scientific, ethical, legal, or logical overstatements.
- Do not call a clean base, extracted copy, literary map, or partial proof a publishable book.

### Conversion And Layout

- Prefer a canonical source in Markdown, DOCX, or another editable format; do not edit the final PDF directly except for specific post-processing tasks.
- For a large DOCX where Pandoc fails, extract `word/document.xml` or use `python-docx` as a textual fallback, marking possible loss of images, tables, and styles.
- Pandoc helps, but technical conversion is not editorial layout. Validate title pages, blank pages, table of contents, start of body matter, headers, footers, page numbering, margins, and visual hierarchy.
- For A5 PDF via LaTeX/Pandoc, validate size with `pdfinfo`. A5 is expected around `419.528 x 595.276 pts`.
- If the Markdown already contains title, subtitle, and author in the body, avoid duplicating a visual title block through Pandoc metadata; use metadata only when it does not duplicate presentation.
- In A5 PDFs using the LaTeX `book` class, default `chapter` spacing may be too large. Use `titlesec` or equivalent control when chapter titles create excessive vertical margins.
- The final table of contents must reflect real pagination. A manual TOC may help in pilots, but the final version should be updated by the layout engine or the editor.

### Objective Validation

- Validate DOCX and EPUB with `unzip -t`.
- Validate PDF with `pdfinfo`.
- Extract text with `pdftotext` and search for title, chapters, bibliography, QR-code text, required terms, forbidden terms, old names, and AI residues.
- Render samples with `pdftoppm` or an equivalent tool: cover, title page, table of contents, first chapter, image page, references, and final page.
- Regenerate every format after any final textual or structural change, even a small one.
- A serious final review must end with evidence: commands run, counts, pages, artifact integrity, clean searches, and human-review pending items.

### UICLAP, Interior File, And Covers

- The `miolo` is the internal book PDF, without the complete external cover. A complete UICLAP cover must not be inserted into the PDF/EPUB/DOCX reading file.
- A printed UICLAP cover must be treated as a separate upload file, in one image with back cover on the left, spine in the center, and front cover on the right.
- Recalculate the spine from the final page count of the interior file. If only an estimate exists, mark it as `estimativa_nao_final`.
- Reserve space for the platform barcode and validate bleed, safety margin, trim, readability, and 3D preview.
- Keep separate: simple front cover, textless base art, complete cover, back-cover copy, spine, QR Code, marketing assets, and metadata.
- Use explicit states:
  - `template_sem_capa_base`: technical placeholder;
  - `capa_candidata_estilo_curado`: reviewable thematic art;
  - `prova_tecnica_com_capa_base`: proof with selected art and pending official spine;
  - `pronta_para_upload`: only after final interior file, official spine, approved back cover, barcode/QR review, and visual validation.
- Before generating covers in bulk, inventory the full catalog by language, confirm counts, and search for PDFs newer than the final files selected as interior files.

### Visual Cover Quality

- A technically assembled cover is not necessarily a commercial cover. Correct dimensions, valid JPG, spine, QR Code, and metadata do not prove visual quality.
- When curated covers exist in the project, analyze them before creating new covers. Compare composition, genre, scene, character/object focus, lighting, texture, palette, contrast, thumbnail readability, and editorial promise.
- Abstract script-generated covers, with geometric icons, networks, frames, and thematic backgrounds, must be classified as `rascunho_tecnico_visual` or `capa_candidata_baixa_fidelidade` when they lack a narrative scene, commercial image, or concrete visual subject.
- Do not call a cover `curated style` when it only replaces a placeholder with a graphic pattern. Use that label only when the result is visually close to curated covers approved by the author.
- For novels, fiction, fantasy, biography, strong authorial products, or sales-oriented covers, the preferred rule is: generate or select textless narrative base art; then compose title, subtitle, author, spine, and back-cover text locally.
- For technical, academic, or essayistic books, typographic or symbolic covers may work, but they still need visual direction, hierarchy, contrast, thumbnail readability, and coherence with the topic.
- If a cover pilot is visually weak, do not scale the batch. Record the failure, adjust briefing/prompt/reference, or admit that the current automation only serves as a technical proof.
- A batch of 50, 100, or 150 covers without individual visual review must be treated as triage or draft work, not as a final publication delivery.

### QR Code And Promotional Material

- Promotional QR Codes should be post-textual material at the end of PDF/EPUB reading files, with a visible URL and a clear invitation to other works.
- In EPUB, include the QR Code as an internal resource with alt text and an equivalent clickable link.
- Visually validate at least one PDF and one EPUB before processing batches.

### AI-Generated Covers

- For generative-AI covers, generate textless base art whenever possible. Title, subtitle, author, spine, and back-cover text should be composed locally to guarantee typographic accuracy.
- The good practice demonstrated by commercial covers is: write a complete visual brief, generate a textless narrative image, choose the best attempt, preserve the base art, apply typography by script, and derive digital cover, back cover, marketing, and UICLAP files from that base.
- The prompt should specify genre, purpose, scene, main subject, narrative objects, composition, negative space for title, lighting, palette, materials, constraints, and forbidden elements. It should explicitly request `no text` when typography will be local.
- AI-generated covers can be good when the image communicates content and reading promise; they can be bad when they look like generic stock, decorative abstraction, empty symbolism, or texture unrelated to the book.
- Record prompt, negative prompts, tool, presence or absence of reference images, number of attempts, reason for selection, base file, dimensions, hash, commit, and derivative scripts.
- Preserve the original base art. Derivatives may lose C2PA metadata; auditability should also rely on README, hash, Git history, and scripts.
- Do not confuse an AI-generated image, licensed photograph, manual collage, and local composition. Each origin needs its own record.
- When C2PA credentials exist, `exiftool` can help prove origin, generating agent, and digital source type. Missing C2PA in derivatives does not invalidate the origin if the chain is documented by base file, hash, README, Git, and scripts.

### Generative Cover Pilot Workflow

- Before scaling a batch, create a pilot in a separate folder, for example `covers/generative-pilots/<book-slug>/`.
- The pilot should contain at minimum:
  - textless base art, for example `<slug>-generative-base-v1.png`;
  - front cover with local typography, for example `<slug>-front-cover-pilot-v2.png`;
  - clean complete cover for upload review, for example `<slug>-complete-uiclap-cover-pilot-v2.jpg`;
  - validation preview with guides, for example `<slug>-complete-uiclap-cover-pilot-v2-validation-preview.jpg`;
  - `README.md` with status, interior-file source, method, and limitations;
  - prompt file, for example `generative-base-prompt.md`;
  - reproducible composition script, for example `build_pilot_cover.py`;
  - metadata, dimensions, and hashes, for example `metadata-v2.json`.
- The clean complete cover must not contain guides, trim lines, technical warnings, `pilot`, `preview`, `validation`, `not final`, or internal explanations. Those details belong in the README, metadata, and separate validation preview.
- If an intermediate version leaves technical text visible inside the cover, preserve it only as an intermediate attempt or remove it from the primary deliverable; generate a clean version before recommending the pilot.
- Back-cover copy should be editorial/commercial and coherent with the book, with a reserved barcode/ISBN area. Do not use the back cover to explain the technical process to the final reader.
- Validate the clean cover and the preview separately: pixel dimensions, color mode, format, DPI, file size, thumbnail readability, contrast, bleed, safety margin, spine, barcode area, and absence of accidental AI-generated text.
- If the spine comes from a visual reference, generic rule, or page-count estimate, record `estimativa_nao_final`. The official spine must be confirmed after the final interior file is uploaded to UICLAP.
- For very short interiors, verify whether the platform allows printed spine text or requires a cover without spine text; do not assume that a 16 mm reference applies to every book.
- Scale to other books only after the author visually approves the pilot and the team confirms that the workflow produces commercial art, not only a technical proof.

### Sensitive Topics And Rigor

- In health, neuropsychiatry, depression, suicide, sexuality, childhood, and nutrition, separate moral thesis, metaphor, speculation, and scientific evidence.
- Self-care and lifestyle may be framed as protective and supportive factors, not as guaranteed cures or single causes of illness.
- Suicide and psychological crisis require multifactorial language, no romanticization, no graphic detail, and current help guidance for the intended audience.
- In religious texts, preserve the author's conviction without dehumanizing people. In secular texts, remove devotional residue when the reading contract requires a secular tone.
- In technical or speculative books, classify ideas as metaphor, hypothesis, prototype, specification, validated algorithm, or product. Do not sell conjecture as proof.
- Use real and verifiable references. Never invent bibliography.

### Heavy Processes

- For large Pandoc, LibreOffice, LaTeX, translation, or DOCX-extraction batches, prefer sequential execution, cache, logs, and resumable batches.
- When memory risk exists, use preventive limits, for example `systemd-run --user --scope -p MemoryMax=4G -p CPUQuota=200% ...`.
- At the end, check that no heavy processes remain, such as `pandoc`, `pdflatex`, `xelatex`, `libreoffice`, `soffice`, or batch Python scripts.

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
- original coverage has been preserved or losses have been justified;
- public artifacts have been regenerated;
- PDF, DOCX, and EPUB have passed technical validation;
- cover, table of contents, margins, images, QR Code, metadata, and final page have been checked;
- for UICLAP, the interior file and complete external cover have been validated separately;
- the final cover has been compared against curated references, not only validated by dimensions/integrity;
- human-review pending items are documented;
- local history is updated.

## Generator Usage

```bash
python3 templates/create_book_project.py "My Book" --author "Author Name" --genre "novel" --language en --target-dir .
```

The generator creates a book project with a standardized editorial structure.
