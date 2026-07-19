# VALIDATION - Projeto Livro Academico UICLAP

## Validar imagens

Na raiz do repositorio:

```bash
python3 examples/scripts/render_cover_examples.py --project projeto-livro-academico-uiclap
python3 - <<'PY'
from pathlib import Path
from PIL import Image

root = Path("examples/projeto-livro-academico-uiclap/publicacao/capas")
for path in sorted(root.glob("*.*")):
    if path.suffix.lower() in {".png", ".jpg", ".jpeg"}:
        image = Image.open(path)
        print(path.name, image.format, image.mode, image.size, image.info.get("dpi"))
PY
python3 -m json.tool examples/projeto-livro-academico-uiclap/publicacao/capas/metadata-capas.json >/dev/null
```
