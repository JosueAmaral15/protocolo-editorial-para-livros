# DECISIONS - {{BOOK_TITLE}}

Use este arquivo para decisoes editoriais ou tecnicas que uma pessoa pode esquecer no futuro.

## Modelo de decisao

```markdown
## {{YYYY-MM-DD}} - Titulo da decisao

**Status:** aceito | substituido | pendente

**Contexto:** explique o problema em poucas linhas.

**Decisao:** diga exatamente o que foi escolhido.

**Motivo:** explique por que essa escolha e melhor para este livro.

**Alternativas consideradas:** liste opcoes rejeitadas, se houver.

**Impacto:** diga quais arquivos, capitulos, formatos ou validacoes dependem disso.
```

## {{YYYY-MM-DD}} - Criacao do projeto editorial

**Status:** aceito

**Contexto:** o livro precisa de uma estrutura clara e reutilizavel.

**Decisao:** usar o template editorial com `README.md`, `history-chat.md`, `docs/`, `manuscrito/`, `assets/`, `scripts/`, `build/`, `publicacao/`, `backups/` e `old/`.

**Motivo:** separar fonte, documentacao, intermediarios, artefatos finais e historico reduz ambiguidade e facilita revisao humana.

**Impacto:** todo novo trabalho deve atualizar `history-chat.md` e manter `docs/` coerente com o estado real do livro.

