# Projeto Livro Academico UICLAP

Exemplo de estrutura editorial para livro academico, tecnico ou ensaistico.

> **Aviso de escopo:** as imagens deste diretorio sao wireframes tecnicos
> deterministas. Elas servem para explicar paineis, sangria, lombada e arquivos
> de validacao. Nao sao uma referencia de qualidade artistica nem uma capa
> comercial pronta para a UICLAP.

Este exemplo demonstra:

- estrutura de projeto de livro;
- separacao entre manuscrito, assets e publicacao;
- capa frontal;
- capa completa com contracapa, lombada e capa;
- capa completa com orelhas;
- metadados e hashes dos arquivos de capa.

## Gerar Capas

Na raiz do repositorio:

```bash
python3 examples/scripts/render_cover_examples.py --project projeto-livro-academico-uiclap
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

As capas deste exemplo nao sao capas comerciais finais. Para uma referencia de
qualidade visual, consulte `../projeto-piloto-generativo-anthropology/`, que
preserva arte-base generativa, composicao tipografica local e uma capa completa
limpa separada do preview de validacao.
