# Generative Cover Pilot Template

Use this folder model before scaling AI-assisted cover generation to a book catalog.

The goal is to validate one complete editorial workflow:

1. generate or curate textless base art;
2. preserve the base art;
3. compose all typography locally;
4. export a clean complete cover;
5. export a separate validation preview with guides;
6. record prompt, dimensions, hashes, status, and pending platform checks.

## Recommended Folder

```text
capas/pilotos-generativos/<book-slug>/
├── README.md
├── prompt-base-generativa.md
├── build_pilot_cover.py
├── metadata-v1.json
├── <slug>-base-generativa-v1.png
├── <slug>-capa-frontal-piloto-v1.png
├── <slug>-capa-completa-uiclap-piloto-v1.jpg
├── <slug>-capa-completa-uiclap-piloto-v1-preview-validacao.jpg
├── <slug>-capa-completa-com-orelhas-piloto-v1.jpg
└── <slug>-capa-completa-com-orelhas-piloto-v1-preview-validacao.jpg
```

Use language-appropriate filenames if the project is English-first, but keep the same separation of roles.

## Non-Negotiable Rules

- The base art should be textless.
- The clean complete cover should not contain guides or internal status text.
- The validation preview should be separate from the clean cover.
- The back cover should speak to the reader, not explain the production process.
- Flaps should be included only when the printer or platform provides a compatible template.
- The spine must remain `estimativa_nao_final` until confirmed by the publishing platform.
- Do not scale a batch until the pilot is visually approved.
