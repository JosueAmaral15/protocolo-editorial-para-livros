# Templates editoriais

Esta pasta guarda modelos reutilizaveis para projetos de livros.

## Template disponivel

- `book-project-template/`: estrutura base para livros, romances, reportagens, ensaios, artigos e obras academicas.

## Gerador

Use `create_book_project.py` para criar um novo projeto a partir do template.

Exemplo:

```bash
python3 templates/create_book_project.py "Meu Livro" --author "Nome do Autor" --genre "romance" --language "pt" --target-dir .
```

O script cria uma pasta com slug derivado do titulo e substitui placeholders nos arquivos Markdown.

