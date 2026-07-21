# Historico do chat - Protocolos de Escrita e Publicacao de Livros

## 2026-07-16 - Criacao do projeto dedicado

O usuario solicitou copiar ou mover os dados genericos sobre estrutura de livros, historico global reutilizavel, templates e codigo gerador para uma pasta dedicada, semelhante a organizacao de `/home/josue/Documents/Informática/programming/protocolos/protocolos-simplicidade`.

Decisao operacional:

- criar o diretorio dedicado em `/home/josue/Documents/Informática/programming/protocolos/protocolos-escrita-livros`;
- copiar, nao mover, os templates e o script gerador;
- preservar o `global-history-chat.md` original no workspace de livros;
- criar um extrato reutilizavel em `docs/GLOBAL_HISTORY_EXTRACT.md`;
- preparar a estrutura para futuro commit e push no GitHub.

Arquivos principais criados:

- `README.md`;
- `history-chat.md`;
- `docs/TASKS.md`;
- `docs/DECISIONS.md`;
- `docs/VALIDATION.md`;
- `docs/GLOBAL_HISTORY_EXTRACT.md`;
- `pt/README.md`;
- `pt/PROTOCOLO_EDITORIAL_LIVROS.md`;
- `en/README.md`;
- `templates/`.

Proximos passos:

- revisar o texto do protocolo;
- decidir licenca;
- decidir se a primeira versao publica sera apenas em portugues ou bilingue;
- inicializar Git;
- criar remoto GitHub;
- fazer primeiro commit.

## 2026-07-16 - Validacao da estrutura inicial

A estrutura inicial foi validada.

Validacoes executadas:

- listagem de arquivos com `find`;
- checagem de sintaxe de `templates/create_book_project.py` com `compile()`;
- execucao do gerador em modo `--dry-run`;
- criacao real de projeto de livro em diretorio temporario;
- conferencia de arquivos essenciais do projeto temporario;
- busca por `__pycache__`, `*.pyc` e projetos de teste permanentes;
- busca por `TODO`, `FIXME` e `PLACEHOLDER`, com ocorrencias apenas em exemplos intencionais de validacao.

Estado final: o diretorio esta pronto para revisao humana antes de `git init`, commit e push.

## 2026-07-16 - Registro previo antes da publicacao inicial no GitHub

O usuario definiu:

- licenca: MIT;
- remoto: `https://github.com/JosueAmaral15/protocolo-editorial-para-livros.git`;
- documentacao bilingue PT/EN;
- `README.md` raiz em ingles;
- `README.md` proprio em `pt/` e em `en/`;
- inicializar Git;
- fazer primeiro commit;
- fazer push para o GitHub.

Plano operacional:

1. adicionar `LICENSE`;
2. reescrever `README.md` raiz em ingles;
3. completar documentacao em ingles;
4. atualizar docs de tarefas, decisoes e validacao;
5. validar sintaxe e estrutura;
6. iniciar Git;
7. commitar;
8. configurar remoto;
9. fazer push.

## 2026-07-16 - Publicacao inicial no GitHub

Resultado:

- `LICENSE` MIT criado.
- `README.md` raiz reescrito em ingles.
- Documentacao bilingue criada:
  - `pt/PROTOCOLO_EDITORIAL_LIVROS.md`;
  - `en/EDITORIAL_BOOK_PROTOCOL.md`.
- `pt/README.md` e `en/README.md` conferidos.
- Git inicializado em `main`.
- Primeiro commit criado:
  - `7d5215f Initial editorial book protocol`.
- Remoto configurado:
  - `https://github.com/JosueAmaral15/protocolo-editorial-para-livros.git`.
- Push inicial concluido com sucesso para `origin/main`.

Validacoes executadas antes do commit/push:

- sintaxe do gerador Python via `compile()`;
- `--dry-run` do gerador;
- criacao real temporaria de projeto;
- conferencia de arquivos essenciais gerados;
- busca por caches Python e projetos de teste permanentes;
- busca por `TODO`, `FIXME` e `PLACEHOLDER`, com ocorrencias apenas em exemplos intencionais de validacao.

Observacao: apos o push inicial, este historico e os documentos operacionais foram atualizados para registrar o resultado; por isso, foi feito um segundo commit pequeno de documentacao:

- `03e3310 Document initial GitHub publication`.

## 2026-07-19 - Registro previo: migracao do historico global bruto para legacy

O usuario solicitou mover o arquivo `global-history-chat.md` para `legacy/` dentro deste repositorio e atualizar os protocolos bilingues com o aprendizado reutilizavel contido nesse historico.

Plano operacional:

1. localizar e ler o `global-history-chat.md` real;
2. extrair regras reutilizaveis para o protocolo editorial, sem transformar o documento principal em copia integral do historico bruto;
3. atualizar `pt/PROTOCOLO_EDITORIAL_LIVROS.md` e `en/EDITORIAL_BOOK_PROTOCOL.md`;
4. mover o historico bruto para `legacy/global-history-chat.md`;
5. validar estrutura, diff e ausencia de residuos basicos.

Registro posterior:

- localizado o historico bruto em `/home/josue/Documents/josue-writter-workspace/global-history-chat.md`;
- lido o arquivo por blocos e mapeados seus topicos principais;
- atualizado `pt/PROTOCOLO_EDITORIAL_LIVROS.md` com regras consolidadas sobre historico local/global, `legacy/`, reescrita editorial abrangente, conversao, diagramacao ABNT, validacao objetiva, UICLAP, miolo, capas, QR Code, capas geradas por IA, temas sensiveis, referencias reais e processos pesados;
- atualizado `en/EDITORIAL_BOOK_PROTOCOL.md` com conteudo equivalente em ingles;
- movido o historico bruto para `legacy/global-history-chat.md`;
- confirmada a ausencia do arquivo no caminho antigo e a presenca do arquivo movido com 1174 linhas;
- validacoes executadas: busca por espacos finais com `rg`, `git diff --check`, leitura de trechos dos protocolos atualizados, `git status --short` e conferencia de tamanho do arquivo arquivado;
- resultado: o historico bruto ficou preservado como legado auditavel, e as regras operacionais reutilizaveis passaram a estar nos protocolos bilingues.

## 2026-07-19 - Registro previo: revisao da regra de capas com IA generativa

O usuario apontou que as tentativas automatizadas anteriores de capas em lote ficaram ruins quando comparadas a uma capa comercial realmente produzida com IA generativa, como a de `O Juramento da Herdeira de Vinterholm`.

Plano operacional:

1. analisar `/home/josue/Documents/josue-writter-workspace/O Juramento da Herdeira de Vinterholm/publicacao/capa`;
2. comparar o fluxo dessa capa com as capas candidatas geradas por script em `books/capas`;
3. registrar no protocolo que arte abstrata/scriptada nao equivale a capa comercial ilustrada;
4. reforcar que, para capas comerciais, a arte-base deve ser gerada ou curada como imagem narrativa sem texto, com tipografia aplicada localmente;
5. validar os documentos atualizados.

Registro posterior:

- analisado `publicacao/capa/README.md` de `O Juramento da Herdeira de Vinterholm`;
- conferidos `capa-base-frontal-v1.png`, `capa-oficial-v1.png` e a capa completa UICLAP derivada;
- lidos os scripts `scripts/build_capa_oficial.sh` e `scripts/build_uiclap_cover.sh`;
- confirmada com `exiftool` a presenca de metadados C2PA na arte-base, incluindo `OpenAI Media Service API`, `gpt-image` e tipo de fonte digital `trainedAlgorithmicMedia`;
- comparada visualmente a capa de Vinterholm com uma capa candidata automatizada de `books/capas/capas-candidatas-estilo-curado-final-public-pdf`;
- conclusao registrada: as capas automatizadas por script sao organizadas como prova tecnica, mas nao atingem o padrao comercial narrativo da capa de Vinterholm;
- atualizado `pt/PROTOCOLO_EDITORIAL_LIVROS.md` com a secao `Qualidade visual de capas` e regras reforcadas para `Capas geradas por IA`;
- atualizado `en/EDITORIAL_BOOK_PROTOCOL.md` com a secao equivalente `Visual Cover Quality`;
- regra consolidada: capa abstrata/scriptada sem cena, personagem, objeto narrativo ou direcao visual concreta deve ser tratada como rascunho tecnico ou candidata de baixa fidelidade, nunca como capa comercial final;
- regra consolidada: para capa comercial, gerar ou curar arte-base narrativa sem texto e aplicar tipografia/lombada/contracapa localmente.

## 2026-07-19 - Registro previo: incorporacao do piloto generativo Anthropology

O usuario aprovou o piloto gerado para `Anthropology` e pediu atualizar este repositorio de protocolo com as descobertas.

Descobertas a consolidar:

- uma capa generativa comercial precisa separar a arte-base sem texto da composicao textual local;
- status operacional como `piloto` ou `prova` deve ficar em README/metadados, nao impresso na capa limpa;
- a capa completa limpa e o preview com guias devem ser arquivos diferentes;
- a contracapa deve conter texto editorial/comercial, nao aviso tecnico de piloto;
- o diretorio piloto precisa preservar prompt, script de composicao, hashes, dimensoes e referencia do miolo;
- lombada baseada em imagem de referencia ou estimativa deve ser marcada como nao final ate confirmacao na UICLAP;
- a validacao minima deve combinar inspecao visual, dimensoes, formato RGB/JPEG, DPI, hashes e revisao humana.

Registro posterior:

- atualizado `pt/PROTOCOLO_EDITORIAL_LIVROS.md` com a secao `Fluxo piloto de capa generativa`;
- atualizado `en/EDITORIAL_BOOK_PROTOCOL.md` com a secao equivalente `Generative Cover Pilot Workflow`;
- atualizado `README.md` para destacar a regra de capa generativa e apontar para o template reutilizavel;
- atualizado `docs/DECISIONS.md` com a decisao de exigir pilotos antes de capas em lote;
- atualizado `docs/VALIDATION.md` com checklist tecnico/editorial para piloto de capa generativa;
- atualizado `docs/TASKS.md` para registrar a tarefa como concluida e manter pendencias reais;
- atualizado `docs/README.md` para indexar o novo template documental;
- criado `docs/templates/generative-cover-pilot/` com `README.md`, `CHECKLIST.md`, `metadata.example.json`, `prompt-template.pt.md` e `prompt-template.en.md`;
- validacoes executadas: `git diff --check`, busca por espacos finais/conflitos, `python3 -m py_compile templates/create_book_project.py`, remocao do cache Python gerado pela compilacao e conferencia de `git status --short`;
- resultado: o protocolo agora registra a metodologia validada no piloto `Anthropology` e fornece um modelo textual para repetir o fluxo sem confundir prova tecnica com capa comercial final.

## 2026-07-19 - Registro previo: exemplos praticos de projetos de livro e capas

O usuario pediu criar exemplos praticos de projetos de livro, incluindo:

- criacao de capa frontal;
- capa completa com contracapa, lombada e capa;
- capa completa com orelhas, contracapa, lombada e capa.

Plano operacional:

1. criar uma pasta `examples/` no repositorio;
2. adicionar projetos exemplo com estrutura editorial semelhante ao template principal;
3. criar scripts reprodutiveis para gerar capas didaticas leves;
4. gerar imagens reais de exemplo para capa frontal, capa completa sem orelhas e capa completa com orelhas;
5. documentar que os exemplos sao tecnicos e didaticos, nao capas comerciais finais;
6. atualizar README, tarefas, validacao e protocolos PT/EN quando necessario;
7. validar estrutura, imagens, JSON, scripts, ausencia de cache e Git.

Registro posterior:

- criado `examples/README.md`;
- criado o script compartilhado `examples/scripts/render_cover_examples.py`;
- criados os projetos exemplo `examples/projeto-livro-academico-uiclap/` e `examples/projeto-romance-com-orelhas/`;
- cada projeto recebeu `README.md`, `history-chat.md`, `docs/TASKS.md`, `docs/DECISIONS.md`, `docs/VALIDATION.md`, manuscrito placeholder e wrapper `scripts/build_covers.py`;
- geradas imagens reais de exemplo em `publicacao/capas/` para capa frontal, capa completa com contracapa/lombada/capa, preview de validacao, capa completa com orelhas e preview de validacao com orelhas;
- gerado `metadata-capas.json` em cada exemplo, com dimensoes, papeis dos arquivos, hashes SHA-256, status `exemplo_tecnico_didatico_nao_final` e lombada `estimativa_nao_final`;
- atualizado `README.md`, `docs/DECISIONS.md`, `docs/README.md`, `docs/TASKS.md` e `docs/VALIDATION.md` para indexar e validar os exemplos;
- atualizados os protocolos PT/EN para mencionar capas com orelhas como arquivo externo separado que depende de template proprio da grafica/plataforma;
- atualizado o template `docs/templates/generative-cover-pilot/` para contemplar opcionalmente capa completa com orelhas;
- apos alerta do usuario sobre erro `image_url` invalido, a etapa evitou `image_gen` e visualizacao inline de imagens; as capas foram geradas localmente por Pillow e validadas por comandos textuais;
- validacoes executadas ate aqui: compilacao logica dos scripts com `compile()`, execucao dos wrappers, validacao JSON, validacao de dimensoes/modo/formato/DPI das imagens e busca por caches Python.

## 2026-07-19 - Registro previo: correcao dos exemplos de capa

O usuario apontou corretamente que as capas tecnicas geradas por script em `examples/` nao se parecem com o padrao comercial de `O Juramento da Herdeira de Vinterholm` nem com o piloto generativo aprovado.

Correcao de entendimento:

- as imagens geometricas anteriores sao wireframes didaticos de composicao e nao devem ser apresentadas como exemplo comercial de capa;
- o exemplo pratico principal deve incluir a imagem piloto generativa aprovada anteriormente;
- `templates/book-project-template/assets` estava pobre como scaffold porque nao trazia subpastas reais para capas, arte-base, QR e imagens;
- o template deve indicar onde colocar assets, mas nao deve fingir que um asset generico e capa final de qualquer livro.

Plano operacional:

1. copiar para o repositorio do protocolo o piloto generativo `en-anthropology` criado em `books/capas/pilotos-generativos/en-anthropology/`;
2. criar um exemplo dedicado `examples/projeto-piloto-generativo-anthropology/`;
3. reclassificar os exemplos geometricos como wireframes tecnicos, nao capas comerciais;
4. criar subpastas README em `templates/book-project-template/assets/`;
5. atualizar README, docs e historico;
6. validar arquivos, hashes, imagens e Git sem usar visualizacao inline de imagens.

Registro posterior:

- criado `examples/projeto-piloto-generativo-anthropology/` com copia do piloto
  real de `books/capas/pilotos-generativos/en-anthropology/`;
- preservadas a arte-base, a capa frontal, a capa completa limpa, o preview de
  validacao, prompt, script de composicao e metadados do piloto;
- os exemplos `projeto-livro-academico-uiclap` e
  `projeto-romance-com-orelhas` foram rotulados de forma explicita como
  wireframes tecnicos, sem valor de referencia artistica ou de upload;
- preenchidos `assets/capas`, `assets/imagens`, `assets/fontes` e `assets/qr`
  do template com READMEs rastreaveis e regras de uso;
- atualizados README, tarefas, decisoes e validacao para separar composicao
  tecnica de direcao de arte comercial;
- a etapa nao usou `image_gen` nem visualizacao inline, evitando repetir o erro
  de `image_url` invalido reportado pelo usuario;
- pendente: validar por comandos os artefatos copiados e revisar visualmente o
  piloto em tamanho completo antes de trata-lo como qualquer coisa alem de
  referencia revisavel.

## 2026-07-21 - Validacao da correcao dos exemplos de capa

Registro posterior complementar:

- compilados sem erro `create_book_project.py`, o renderizador de wireframes,
  os dois wrappers de exemplo e `build_pilot_cover.py`;
- reconstruido localmente o piloto `Anthropology` a partir da arte-base copiada;
- confirmadas as propriedades: frente PNG RGB `3590 x 5197`, capa completa e
  preview JPEG RGB `7559 x 5197`, ambos a 600 DPI;
- confirmados hashes SHA-256 contra `metadata-v2.json` e igualdade byte a byte
  da frente, capa completa e preview em relacao ao piloto preservado em `books`;
- confirmados JSON valido, ausencia de conflitos/espacos finais via
  `git diff --check` e ausencia de cache Python;
- nenhum arquivo de miolo foi alterado; a aprovacao visual humana continua
  necessaria antes de qualquer uso como capa de upload.
