# Practical Book Project Examples

This folder contains practical examples for applying the editorial protocol to real book-project structures.

There are two kinds of examples here: a real generative pilot and technical wireframes. Do not confuse them.

## Examples

- `projeto-piloto-generativo-anthropology/`: real generative-cover pilot copied from the approved `en-anthropology` workflow. This is the visual-quality reference example.
- `projeto-livro-academico-uiclap/`: technical wireframe for academic/nonfiction cover layout, including front cover, complete cover, and complete cover with flaps.
- `projeto-romance-com-orelhas/`: technical wireframe for fiction cover layout with flaps.

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

The technical wireframes generate:

- `*-capa-frontal-exemplo.png`: front cover only.
- `*-capa-lombada-contracapa-exemplo.jpg`: back cover + spine + front cover.
- `*-capa-lombada-contracapa-preview-validacao.jpg`: validation preview with guides.
- `*-capa-lombada-contracapa-orelhas-exemplo.jpg`: flap + back cover + spine + front cover + flap.
- `*-capa-lombada-contracapa-orelhas-preview-validacao.jpg`: validation preview with guides.
- `metadata-capas.json`: dimensions, hashes, status, and file roles.

## Important

The geometric examples are only technical wireframes. They show file structure and panel layout. They are not commercial final covers and should not be used as visual-quality references.

For a real visual pilot, use `projeto-piloto-generativo-anthropology/`.
