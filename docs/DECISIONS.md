# DECISIONS

## 2026-07-16 - Criar projeto dedicado fora do workspace de livros

**Status:** aceito

**Contexto:** o usuario quer transformar a metodologia de estrutura editorial em um material independente, com README e organizacao semelhante a `protocolos-simplicidade`, para futuro commit e push ao GitHub.

**Decisao:** criar `/home/josue/Documents/Informática/programming/protocolos/protocolos-escrita-livros`.

**Motivo:** a pasta `protocolos/` ja agrupa materiais metodologicos e e mais adequada para um repositorio de protocolo do que a raiz do workspace de livros.

**Impacto:** o projeto fica separado dos manuscritos e pode virar repositorio Git proprio.

## 2026-07-16 - Copiar em vez de mover

**Status:** aceito

**Contexto:** o `global-history-chat.md`, os templates e o script gerador ainda sao uteis no workspace original.

**Decisao:** copiar o que e reutilizavel para o novo projeto, sem mover os arquivos originais.

**Motivo:** preservar a continuidade operacional dos livros e evitar quebrar referencias existentes.

**Impacto:** o novo repositorio nasce com conteudo proprio, mas o workspace original continua funcionando.

## 2026-07-16 - Extrair o historico global em vez de copiar integralmente

**Status:** aceito

**Contexto:** `global-history-chat.md` contem memoria viva e registros especificos de muitos projetos.

**Decisao:** criar `docs/GLOBAL_HISTORY_EXTRACT.md` com o conteudo generico reutilizavel.

**Motivo:** um repositorio publico deve conter metodologia reaproveitavel, nao todo o historico operacional do workspace.

**Impacto:** reduz risco de publicar informacao privada, especifica demais ou desnecessaria.

## 2026-07-16 - Usar licenca MIT

**Status:** aceito

**Contexto:** o projeto sera publicado no GitHub como protocolo e ferramenta reutilizavel.

**Decisao:** usar licenca MIT.

**Motivo:** MIT e simples, permissiva e adequada para modelos, documentacao e scripts reutilizaveis.

**Impacto:** foi criado `LICENSE` na raiz do projeto.

## 2026-07-16 - README raiz em ingles e documentacao bilingue

**Status:** aceito

**Contexto:** o usuario pediu projeto bilingue com README raiz em ingles e READMEs especificos em `pt/` e `en/`.

**Decisao:** manter `README.md` raiz em ingles, `pt/PROTOCOLO_EDITORIAL_LIVROS.md` em portugues e `en/EDITORIAL_BOOK_PROTOCOL.md` em ingles.

**Motivo:** ingles melhora apresentacao internacional no GitHub, enquanto portugues preserva o idioma original do usuario e do protocolo inicial.

**Impacto:** a primeira versao publica passa a ter documentacao principal PT/EN.

## 2026-07-16 - Remoto GitHub

**Status:** aceito

**Contexto:** o usuario informou o remoto do repositorio.

**Decisao:** configurar `origin` como `https://github.com/JosueAmaral15/protocolo-editorial-para-livros.git`.

**Motivo:** este e o destino definido pelo usuario para commit e push.

**Impacto:** apos `git init`, o primeiro commit deve ser enviado para esse remoto.

## 2026-07-19 - Pilotos generativos antes de capas em lote

**Status:** aceito

**Contexto:** uma prova tecnica de capa pode ter dimensoes corretas, lombada e metadados, mas ainda assim nao funcionar como capa comercial. O piloto `Anthropology` mostrou que o fluxo correto precisa separar arte generativa sem texto, composicao local e validacao visual.

**Decisao:** antes de gerar capas em lote, criar pelo menos um piloto por metodologia/tema em pasta separada, com arte-base preservada, prompt, script de composicao, metadados, hashes, capa completa limpa e preview separado com guias.

**Motivo:** o piloto permite identificar problemas de promessa visual, tipografia, contracapa, lombada, texto tecnico visivel e requisitos UICLAP antes de multiplicar o erro em dezenas de livros.

**Impacto:** arquivos com guias ou avisos tecnicos nao devem ser confundidos com capas limpas. Status como `piloto`, `preview`, `validacao` e `estimativa_nao_final` pertence a README/metadados, nao ao arquivo limpo destinado a revisao de upload.
