# Projeto Romance Com Orelhas

Exemplo de estrutura editorial para romance ou ficcao.

> **Aviso de escopo:** as imagens deste diretorio sao wireframes tecnicos
> deterministas. Elas demonstram a arquitetura de capa, contracapa, lombada e
> orelhas. Nao sao uma referencia de qualidade artistica nem uma capa comercial
> pronta para a UICLAP.

Este exemplo demonstra:

- estrutura de projeto narrativo;
- capa frontal;
- capa completa com contracapa, lombada e capa;
- capa completa com orelha esquerda e orelha direita;
- separacao entre arquivo limpo e preview de validacao;
- metadados e hashes dos arquivos gerados.

## Gerar Capas

Na raiz do repositorio:

```bash
python3 examples/scripts/render_cover_examples.py --project projeto-romance-com-orelhas
```

Ou dentro deste projeto:

```bash
python3 scripts/build_covers.py
```

## Saidas

As imagens geradas ficam em `publicacao/capas/`.

O arquivo `publicacao/capas/metadata-capas.json` registra dimensoes, papeis dos arquivos, hashes e status.

## Status

`exemplo_tecnico_didatico_nao_final`

As capas deste exemplo mostram somente o fluxo tecnico. Em publicacao real, a
arte de venda deve ser curada, gerada ou contratada e revisada visualmente.
Consulte `../projeto-piloto-generativo-anthropology/` para um exemplo de piloto
generativo com qualidade visual comercial e composicao local.
