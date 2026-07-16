# VALIDATION

## Validacao do gerador Python

Compilar:

```bash
python3 -m py_compile templates/create_book_project.py
```

Simular criacao:

```bash
python3 templates/create_book_project.py "Livro de Teste Editorial" --author "Josue Amaral" --genre "teste" --language pt --dry-run
```

Criar em uma pasta temporaria:

```bash
tmpdir="$(mktemp -d)"
python3 templates/create_book_project.py "Livro de Teste Editorial" --target-dir "$tmpdir"
find "$tmpdir/livro-de-teste-editorial" -maxdepth 3 -type f | sort
```

## Validacao de estrutura do repositorio

```bash
find . -maxdepth 3 -type f | sort
find . -maxdepth 3 -type d | sort
```

## Checklist antes de publicar

- [ ] `README.md` explica objetivo, uso e estrutura.
- [ ] `history-chat.md` esta atualizado.
- [ ] `docs/DECISIONS.md` justifica decisoes principais.
- [ ] `docs/TASKS.md` mostra pendencias reais.
- [ ] `docs/GLOBAL_HISTORY_EXTRACT.md` nao contem dados sensiveis.
- [ ] `templates/create_book_project.py` compila.
- [ ] `templates/create_book_project.py --dry-run` funciona.
- [ ] O template cria um projeto de livro completo.
- [ ] Nao ha `__pycache__` nem arquivos temporarios.

## Validacao Git e GitHub

Comandos planejados:

```bash
git init
git branch -M main
git add .
git commit -m "Initial editorial book protocol"
git remote add origin https://github.com/JosueAmaral15/protocolo-editorial-para-livros.git
git push -u origin main
```

## Registro de validacao da publicacao inicial

### 2026-07-16

- Licenca MIT: `LICENSE` criado.
- README raiz em ingles: conferido.
- Documentacao PT/EN: `pt/PROTOCOLO_EDITORIAL_LIVROS.md` e `en/EDITORIAL_BOOK_PROTOCOL.md` criados/conferidos.
- Sintaxe do gerador Python: OK via `compile()`.
- `--dry-run` do gerador: OK.
- Criacao temporaria de projeto: OK, com conferencia de arquivos essenciais e substituicao de placeholders.
- Cache Python e projetos de teste permanentes: nao encontrados.
- Busca por `TODO`, `FIXME` e `PLACEHOLDER`: apenas ocorrencias intencionais em exemplos de validacao.
- Git init: OK.
- Branch principal: `main`.
- Primeiro commit: `7d5215f Initial editorial book protocol`.
- Remoto: `https://github.com/JosueAmaral15/protocolo-editorial-para-livros.git`.
- Push inicial: OK, `main` configurada para rastrear `origin/main`.
