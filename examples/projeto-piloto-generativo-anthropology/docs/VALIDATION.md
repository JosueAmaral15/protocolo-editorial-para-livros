# VALIDATION - Projeto Piloto Generativo Anthropology

## Validar arquivos

Na raiz do repositorio:

```bash
python3 -m json.tool examples/projeto-piloto-generativo-anthropology/publicacao/capas/metadata-v2.json >/dev/null
python3 - <<'PY'
from pathlib import Path
from PIL import Image

paths = [
    "examples/projeto-piloto-generativo-anthropology/assets/capas/en-anthropology-base-generativa-v1.png",
    "examples/projeto-piloto-generativo-anthropology/publicacao/capas/en-anthropology-capa-frontal-piloto-v2.png",
    "examples/projeto-piloto-generativo-anthropology/publicacao/capas/en-anthropology-capa-completa-uiclap-piloto-v2.jpg",
    "examples/projeto-piloto-generativo-anthropology/publicacao/capas/en-anthropology-capa-completa-uiclap-piloto-v2-preview-validacao.jpg",
]

for item in paths:
    path = Path(item)
    image = Image.open(path)
    print(path.name, image.format, image.mode, image.size, image.info.get("dpi"))
PY
```
