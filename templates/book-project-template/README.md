# {{BOOK_TITLE}}

## Resumo rapido

- Titulo: {{BOOK_TITLE}}
- Subtitulo:
- Autor(es): {{AUTHOR}}
- Genero: {{GENRE}}
- Idioma-base: {{LANGUAGE}}
- Publico-alvo:
- Status editorial: {{STATUS_EDITORIAL}}
- Formato-alvo: {{FORMAT_TARGET}}
- Fonte principal: `manuscrito/trabalho/{{BOOK_SLUG}}.md`
- Saidas finais:

## Estrutura do projeto

- `history-chat.md`: memoria especifica deste livro.
- `docs/`: tarefas, decisoes, estilo, estrutura, referencias e validacao.
- `manuscrito/`: texto-fonte da obra.
- `assets/`: imagens, capas, fontes, QR codes e materiais de apoio.
- `scripts/`: automacoes de conversao, validacao e publicacao.
- `build/`: intermediarios reconstruiveis, logs e arquivos temporarios.
- `publicacao/`: PDF, DOCX, EPUB, Markdown, LaTeX e metadados de entrega.
- `backups/`: copias datadas antes de alteracoes arriscadas.
- `old/`: versoes antigas preservadas por referencia historica.

## Fonte principal

Indique aqui qual arquivo deve ser tratado como fonte autoritativa do livro.

```text
manuscrito/trabalho/{{BOOK_SLUG}}.md
```

## Como gerar

Registre aqui os comandos reais de geracao quando existirem.

```bash
# Exemplo futuro:
# python3 scripts/build_book.py
```

## Como validar

Antes de considerar uma versao pronta, atualize `docs/VALIDATION.md` com os comandos usados e registre o resultado em `history-chat.md`.

Validacoes minimas recomendadas:

- Integridade de DOCX e EPUB.
- Metadados e tamanho do PDF.
- Sumario, margens, cabecalhos, rodapes e ultima pagina.
- Presenca de bibliografia quando aplicavel.
- Busca por residuos como `TODO`, `FIXME`, comentarios de IA, placeholders e nomes antigos.

## Estado editorial

- [ ] Manuscrito original preservado.
- [ ] Manuscrito de trabalho criado.
- [ ] Estrutura de capitulos definida.
- [ ] Estilo editorial definido.
- [ ] Referencias organizadas.
- [ ] Saidas de publicacao geradas.
- [ ] Revisao humana concluida.
- [ ] Artefatos finais validados.
