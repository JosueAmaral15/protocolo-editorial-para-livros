# Extrato reutilizavel do global-history-chat

Este arquivo contem apenas aprendizados genericos que podem ser reutilizados em outros projetos editoriais. Ele nao e uma copia integral do `global-history-chat.md` original.

## Padronizacao recomendada para projetos de livros

Um projeto de livro deve ser navegavel por qualquer pessoa ou IA no futuro sem depender da memoria da conversa. A raiz precisa explicar o que e a obra, onde esta o texto-fonte, como gerar artefatos, o que ja foi decidido, o que falta validar e quais arquivos sao fonte, intermediarios, publicacao ou historico.

Estrutura base recomendada:

```text
nome-do-livro/
├── README.md
├── history-chat.md
├── docs/
│   ├── TASKS.md
│   ├── DECISIONS.md
│   ├── STYLE-GUIDE.md
│   ├── STRUCTURE.md
│   ├── VALIDATION.md
│   ├── REFERENCES.md
│   └── RELEASE-CHECKLIST.md
├── manuscrito/
│   ├── original/
│   ├── trabalho/
│   ├── revisado/
│   └── final/
├── assets/
│   ├── imagens/
│   ├── capas/
│   ├── fontes/
│   └── qr/
├── scripts/
├── build/
│   ├── tmp/
│   ├── chapters/
│   ├── exports/
│   └── logs/
├── publicacao/
│   ├── pdf/
│   ├── docx/
│   ├── epub/
│   ├── markdown/
│   ├── latex/
│   └── metadata/
├── backups/
└── old/
```

## Funcoes principais

- `README.md`: porta de entrada do projeto.
- `history-chat.md`: memoria especifica daquele livro.
- `global-history-chat.md`: memoria ampla de uma colecao de projetos, quando combinado.
- `docs/`: gestao editorial, decisoes, tarefas, validacao, estilo e referencias.
- `manuscrito/` ou `working/`: texto-fonte da obra.
- `assets/`: imagens, capas, fontes e QR codes.
- `scripts/`: automacoes de conversao, validacao e publicacao.
- `build/`: intermediarios reconstruiveis.
- `publicacao/` ou `public/`: artefatos de leitura, prova, venda ou entrega.
- `backups/`: copias antes de alteracoes arriscadas.
- `old/`: versoes antigas preservadas por referencia historica.

## Adaptacao do Protocolo Simplicidade para livros

- Documentacao deve ser escrita para o "eu futuro" que abrira o projeto sem contexto.
- `README.md`, `history-chat.md` e `docs/` sao diretamente aplicaveis a projetos editoriais.
- Markdown de documentacao fica em `docs/`.
- Markdown de manuscrito fica em `manuscrito/`, `working/` ou equivalente.
- Decisoes importantes devem ir para `docs/DECISIONS.md`.
- Tarefas devem ir para `docs/TASKS.md`.
- A etapa final de cada ciclo deve incluir validacao objetiva.

## Validacao antes de considerar uma obra pronta

- Validar DOCX e EPUB com `unzip -t`.
- Validar PDF com `pdfinfo`.
- Extrair texto com `pdftotext` e procurar titulo, capitulos, bibliografia, termos obrigatorios e termos proibidos.
- Renderizar amostras com `pdftoppm` ou fazer revisao visual.
- Conferir se os artefatos em `publicacao/` foram regenerados depois da ultima mudanca no manuscrito.
- Procurar residuos como `TODO`, `FIXME`, comentarios de IA, nomes antigos, placeholders, capitulos duplicados e sumario manual obsoleto.
- Registrar no `history-chat.md` o que foi alterado, validado e ainda exige leitura humana.

## Regra operacional para IAs e revisores

- Antes de editar: ler `README.md`, `history-chat.md`, documentos relevantes em `docs/` e, quando existir, `global-history-chat.md`.
- Antes de alteracao arriscada: criar backup datado.
- Durante a edicao: alterar o manuscrito-fonte, nao o PDF final diretamente, salvo tarefas especificas de pos-processamento.
- Depois de editar: atualizar `history-chat.md`, regenerar saidas necessarias e validar artefatos.
- Depois de aprender algo reutilizavel entre livros: registrar em `global-history-chat.md` ou em documentacao equivalente do repositorio metodologico.

## Template e gerador

Foi criado um template editorial em `templates/book-project-template/` e um gerador Python em `templates/create_book_project.py`. O gerador copia o template, substitui placeholders e cria um manuscrito inicial em `manuscrito/trabalho/`.

