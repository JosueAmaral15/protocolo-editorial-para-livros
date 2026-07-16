# Protocolo Editorial de Livros

## Instrucao obrigatoria para IAs

Antes de modificar um projeto de livro, leia:

1. `README.md`;
2. `history-chat.md`;
3. documentos relevantes em `docs/`;
4. `global-history-chat.md`, quando existir no diretorio pai;
5. o manuscrito-fonte indicado pelo README.

Nao declare um livro pronto sem validacao objetiva dos artefatos finais.

## Filosofia central

Um livro e um projeto de longo prazo. Ele precisa de autoria preservada, historico claro, estrutura navegavel, decisoes registradas, revisao humana e artefatos finais validaveis.

O trabalho de IA deve ajudar o autor a organizar, revisar, explicar, fortalecer e validar o texto, sem apagar a autoria nem transformar uma obra longa em sintese curta quando o pedido e revisao editorial.

## Estrutura obrigatoria de projeto

```text
nome-do-livro/
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

## Regras por pasta

- `README.md`: explica o livro, status, fonte principal, comandos e validacoes.
- `history-chat.md`: registra memoria especifica do livro.
- `docs/`: guarda tarefas, decisoes, estilo, estrutura, referencias e validacao.
- `manuscrito/`: guarda texto-fonte, original, trabalho, revisado e final.
- `assets/`: guarda imagens, capas, fontes e QR codes.
- `scripts/`: guarda automacoes.
- `build/`: guarda intermediarios reconstruiveis.
- `publicacao/`: guarda PDF, DOCX, EPUB e outros artefatos finais.
- `backups/`: guarda copias antes de alteracoes arriscadas.
- `old/`: guarda versoes antigas que nao sao mais fonte principal.

## Regra de Markdown

Markdown de documentacao vai para `docs/`.

Markdown de manuscrito vai para `manuscrito/`, `working/` ou equivalente.

Essa distincao e essencial para nao confundir processo editorial com texto da obra.

## Ciclo de trabalho

1. Ler documentacao e historico.
2. Identificar fonte principal.
3. Registrar plano ou tarefa quando a mudanca for relevante.
4. Criar backup antes de alteracao arriscada.
5. Editar o manuscrito-fonte ou os arquivos de estrutura.
6. Atualizar `history-chat.md`.
7. Regenerar artefatos publicos afetados.
8. Validar PDF, DOCX, EPUB e metadados.
9. Registrar pendencias de revisao humana.

## Validacao minima

Use comandos como:

```bash
unzip -t "publicacao/docx/livro.docx"
unzip -t "publicacao/epub/livro.epub"
pdfinfo "publicacao/pdf/livro.pdf"
pdftotext "publicacao/pdf/livro.pdf" -
```

Tambem procure residuos:

```bash
rg -n "TODO|FIXME|PLACEHOLDER|ChatGPT|texto-base|revisar depois" manuscrito docs publicacao || true
```

## Tipos de obra

### Ficcao e romance

Adicionar quando necessario:

- `docs/CHARACTERS.md`;
- `docs/CONTINUITY.md`;
- `docs/TIMELINE.md`;
- `docs/WORLD-BUILDING.md`;
- `docs/PLOT-THREADS.md`.

### Reportagem e noticia

Adicionar quando necessario:

- `docs/SOURCES.md`;
- `docs/FACT-CHECK.md`;
- `docs/INTERVIEWS.md`;
- `docs/RIGHTS-AND-PERMISSIONS.md`;
- `docs/LEGAL-REVIEW.md`.

### Academico, artigo e ensaio

Adicionar quando necessario:

- `docs/METHODOLOGY.md`;
- `docs/CITATION-STYLE.md`;
- `docs/BIBLIOGRAPHY.md`;
- `docs/ARGUMENT-MAP.md`;
- `docs/PEER-REVIEW-NOTES.md`.

### Tecnico e didatico

Adicionar quando necessario:

- `docs/EXAMPLES.md`;
- `docs/EXERCISES.md`;
- `docs/ERRATA.md`;
- `docs/GLOSSARY.md`;
- `docs/TECHNICAL-VALIDATION.md`.

## Prontidao editorial

Um livro pode ser considerado pronto para revisao humana final quando:

- o manuscrito-fonte esta definido;
- as decisoes principais estao registradas;
- os artefatos publicos foram regenerados;
- PDF, DOCX e EPUB passaram por validacao tecnica;
- capa, sumario, margens, imagens e ultima pagina foram conferidos;
- pendencias humanas estao documentadas;
- o historico local esta atualizado.

## Uso do gerador

```bash
python3 templates/create_book_project.py "Meu Livro" --author "Nome do Autor" --genre "romance" --language pt --target-dir .
```

O gerador cria um projeto de livro com estrutura editorial padronizada.

