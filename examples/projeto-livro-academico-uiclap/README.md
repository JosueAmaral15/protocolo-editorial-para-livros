# Projeto Livro Academico UICLAP

Exemplo pratico de projeto editorial para livro academico, tecnico ou ensaistico.

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

As capas deste exemplo nao sao capas comerciais finais. Elas demonstram o protocolo e precisam ser substituidas por arte curada ou generativa revisada antes de publicacao real.
