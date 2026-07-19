# VALIDATION - Projeto Romance Com Orelhas

## Validar imagens

Na raiz do repositorio:

```bash
python3 examples/scripts/render_cover_examples.py --project projeto-romance-com-orelhas
python3 - <<'PY'
from pathlib import Path
from PIL import Image

root = Path("examples/projeto-romance-com-orelhas/publicacao/capas")
for path in sorted(root.glob("*.*")):
    if path.suffix.lower() in {".png", ".jpg", ".jpeg"}:
        image = Image.open(path)
        print(path.name, image.format, image.mode, image.size, image.info.get("dpi"))
PY
python3 -m json.tool examples/projeto-romance-com-orelhas/publicacao/capas/metadata-capas.json >/dev/null
```
