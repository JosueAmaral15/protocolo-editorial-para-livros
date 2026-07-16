# VALIDATION - {{BOOK_TITLE}}

## Objetivo

Registrar comandos e criterios usados para validar os artefatos de publicacao.

## Comandos recomendados

### DOCX

```bash
unzip -t "publicacao/docx/{{BOOK_TITLE}}.docx"
```

### EPUB

```bash
unzip -t "publicacao/epub/{{BOOK_TITLE}}.epub"
```

### PDF

```bash
pdfinfo "publicacao/pdf/{{BOOK_TITLE}}.pdf"
pdftotext "publicacao/pdf/{{BOOK_TITLE}}.pdf" -
```

### Amostras visuais do PDF

```bash
mkdir -p build/tmp/pdf-pages
pdftoppm -png -f 1 -l 3 "publicacao/pdf/{{BOOK_TITLE}}.pdf" build/tmp/pdf-pages/page
```

## Buscas negativas

```bash
rg -n "TODO|FIXME|PLACEHOLDER|ChatGPT|texto-base|revisar depois" manuscrito docs publicacao || true
```

## Checklist editorial

- [ ] Capa conferida.
- [ ] Folha de rosto conferida.
- [ ] Sumario conferido.
- [ ] Capitulos em ordem.
- [ ] Margens e cabecalhos conferidos.
- [ ] Imagens renderizadas.
- [ ] Bibliografia presente quando aplicavel.
- [ ] Ultima pagina conferida.
- [ ] QR code conferido quando existir.
- [ ] Arquivos finais regenerados apos a ultima mudanca no manuscrito.

## Registro de validacoes

### {{YYYY-MM-DD}}

- Comandos executados:
- Resultado:
- Pendencias:

