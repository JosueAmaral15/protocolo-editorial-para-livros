# Assets

Use esta pasta para arquivos usados pelo livro, mas que nao sao o manuscrito.

As subpastas abaixo fazem parte do template para que a estrutura seja visivel
apos uma criacao via Git. Elas sao pontos de entrada, nao assets editoriais
prontos. Nunca reutilize uma arte generica como se fosse capa final de outra
obra.

- `imagens/`: imagens internas.
- `capas/`: capas, contracapas, lombadas, orelhas e artes-base.
- `fontes/`: fontes tipograficas autorizadas.
- `qr/`: QR codes e imagens de chamada externa.

Registre origem, permissao e uso de cada asset relevante em `docs/REFERENCES.md`.

Para uma capa comercial assistida por IA, crie primeiro uma arte-base sem texto
em `capas/`, preserve o prompt e a origem, aplique tipografia localmente e
exporte a capa completa limpa separada do preview com guias. Consulte o modelo
`docs/templates/generative-cover-pilot/` e o exemplo
`examples/projeto-piloto-generativo-anthropology/` no repositorio do protocolo.
