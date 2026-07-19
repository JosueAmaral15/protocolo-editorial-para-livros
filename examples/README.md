# Practical Book Project Examples

This folder contains complete, lightweight examples for applying the editorial protocol to real book-project structures.

The examples are intentionally deterministic and small enough for Git. They demonstrate project organization, cover file roles, validation metadata, and reproducible scripts.

## Examples

- `projeto-livro-academico-uiclap/`: academic/nonfiction book project with front cover, complete cover, and complete cover with flaps.
- `projeto-romance-com-orelhas/`: fiction project demonstrating the same cover outputs with a more literary visual direction.

## Generate Covers

From the repository root:

```bash
python3 examples/scripts/render_cover_examples.py
```

Generate only one example:

```bash
python3 examples/scripts/render_cover_examples.py --project projeto-livro-academico-uiclap
python3 examples/scripts/render_cover_examples.py --project projeto-romance-com-orelhas
```

## Output Types

Each example generates:

- `*-capa-frontal-exemplo.png`: front cover only.
- `*-capa-lombada-contracapa-exemplo.jpg`: back cover + spine + front cover.
- `*-capa-lombada-contracapa-preview-validacao.jpg`: validation preview with guides.
- `*-capa-lombada-contracapa-orelhas-exemplo.jpg`: flap + back cover + spine + front cover + flap.
- `*-capa-lombada-contracapa-orelhas-preview-validacao.jpg`: validation preview with guides.
- `metadata-capas.json`: dimensions, hashes, status, and file roles.

## Important

These are technical examples. They show the protocol and file structure. They are not commercial final covers.
