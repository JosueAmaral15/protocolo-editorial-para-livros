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

## Validacao de piloto de capa generativa

Conferir dimensoes, formato, modo de cor e DPI:

```bash
python3 - <<'PY'
from pathlib import Path
from PIL import Image

root = Path("capas/pilotos-generativos/exemplo")
for name in [
    "base-generativa-v1.png",
    "capa-frontal-piloto-v2.png",
    "capa-completa-uiclap-piloto-v2.jpg",
    "capa-completa-uiclap-piloto-v2-preview-validacao.jpg",
]:
    path = root / name
    image = Image.open(path)
    print(name, image.format, image.mode, image.size, image.info.get("dpi"))
PY
```

Checklist especifico:

- [ ] A arte-base esta preservada sem texto, logo, assinatura ou marca d'agua.
- [ ] A capa completa limpa nao contem guias, linhas de corte, avisos tecnicos ou a palavra `piloto`.
- [ ] O preview com guias esta separado do arquivo limpo.
- [ ] Titulo, subtitulo, autor, lombada e contracapa foram compostos localmente.
- [ ] A contracapa apresenta texto editorial/comercial, nao explicacao tecnica do processo.
- [ ] Ha reserva visual para codigo de barras/ISBN quando aplicavel.
- [ ] `README.md`, prompt, metadados e hashes estao presentes.
- [ ] A lombada esta marcada como `estimativa_nao_final` quando ainda nao foi confirmada pela plataforma.
- [ ] O resultado foi revisado visualmente em tamanho completo e miniatura.
- [ ] O piloto foi aprovado antes de qualquer geracao em lote.

## Validacao dos exemplos praticos

Compilar scripts sem criar cache permanente:

```bash
python3 - <<'PY'
from pathlib import Path

for path in [
    Path("examples/scripts/render_cover_examples.py"),
    Path("examples/projeto-livro-academico-uiclap/scripts/build_covers.py"),
    Path("examples/projeto-romance-com-orelhas/scripts/build_covers.py"),
]:
    compile(path.read_text(encoding="utf-8"), str(path), "exec")
    print("compile ok:", path)
PY
```

Gerar e validar os exemplos:

```bash
python3 examples/scripts/render_cover_examples.py
python3 -m json.tool examples/projeto-livro-academico-uiclap/publicacao/capas/metadata-capas.json >/dev/null
python3 -m json.tool examples/projeto-romance-com-orelhas/publicacao/capas/metadata-capas.json >/dev/null
python3 - <<'PY'
from pathlib import Path
from PIL import Image

for project in ["projeto-livro-academico-uiclap", "projeto-romance-com-orelhas"]:
    root = Path("examples") / project / "publicacao" / "capas"
    for path in sorted(root.glob("*.*")):
        if path.suffix.lower() in {".png", ".jpg", ".jpeg"}:
            image = Image.open(path)
            print(project, path.name, image.format, image.mode, image.size, image.info.get("dpi"))
PY
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
- Commit posterior de documentacao: `03e3310 Document initial GitHub publication`.
- Remoto: `https://github.com/JosueAmaral15/protocolo-editorial-para-livros.git`.
- Push inicial: OK, `main` configurada para rastrear `origin/main`.
