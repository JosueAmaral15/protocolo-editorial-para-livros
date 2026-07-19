# Protocolo Editorial de Livros

## Instrucao obrigatoria para IAs

Antes de modificar um projeto de livro, leia:

1. `README.md`;
2. `history-chat.md`;
3. documentos relevantes em `docs/`;
4. `global-history-chat.md`, quando existir no diretorio pai;
5. `legacy/global-history-chat.md`, quando o historico global bruto tiver sido arquivado neste repositorio;
6. o manuscrito-fonte indicado pelo README.

Nao declare um livro pronto sem validacao objetiva dos artefatos finais.

## Filosofia central

Um livro e um projeto de longo prazo. Ele precisa de autoria preservada, historico claro, estrutura navegavel, decisoes registradas, revisao humana e artefatos finais validaveis.

O trabalho de IA deve ajudar o autor a organizar, revisar, explicar, fortalecer e validar o texto, sem apagar a autoria nem transformar uma obra longa em sintese curta quando o pedido e revisao editorial.

O historico bruto de conversas e aprendizados pode ser preservado em `legacy/`, mas as regras operacionais vivas devem ser consolidadas neste protocolo e nos documentos de `docs/`. O protocolo nao deve depender de memoria implicita da conversa.

## Estrutura obrigatoria de projeto

```text
nome-do-livro/
├── README.md
├── history-chat.md
├── docs/
├── manuscrito/
├── assets/
├── scripts/
├── build/
├── publicacao/
├── backups/
└── old/
```

## Regras por pasta

- `README.md`: explica o livro, status, fonte principal, comandos e validacoes.
- `history-chat.md`: registra memoria especifica do livro.
- `global-history-chat.md`: quando existir em um diretorio pai, registra aprendizado reutilizavel entre obras, nao mudancas especificas de um livro.
- `legacy/`: guarda historicos brutos, extratos antigos e materiais preservados por valor de auditoria, mas que nao devem ser confundidos com fonte operacional atual.
- `docs/`: guarda tarefas, decisoes, estilo, estrutura, referencias e validacao.
- `manuscrito/`: guarda texto-fonte, original, trabalho, revisado e final.
- `assets/`: guarda imagens, capas, fontes e QR codes.
- `scripts/`: guarda automacoes.
- `build/`: guarda intermediarios reconstruiveis.
- `publicacao/`: guarda PDF, DOCX, EPUB e outros artefatos finais.
- `backups/`: guarda copias antes de alteracoes arriscadas.
- `old/`: guarda versoes antigas que nao sao mais fonte principal.

## Regra de Markdown

Markdown de documentacao vai para `docs/`.

Markdown de manuscrito vai para `manuscrito/`, `working/` ou equivalente.

Essa distincao e essencial para nao confundir processo editorial com texto da obra.

## Ciclo de trabalho

1. Ler documentacao e historico.
2. Identificar fonte principal.
3. Registrar plano ou tarefa quando a mudanca for relevante.
4. Criar backup antes de alteracao arriscada.
5. Editar o manuscrito-fonte ou os arquivos de estrutura.
6. Atualizar `history-chat.md`.
7. Regenerar artefatos publicos afetados.
8. Validar PDF, DOCX, EPUB e metadados.
9. Registrar pendencias de revisao humana.

## Regras consolidadas do historico global

### Historico e autoria

- O `history-chat.md` local registra decisoes, acoes, validacoes, pendencias e riscos de um livro especifico.
- O historico global ou arquivado registra aprendizados reutilizaveis entre livros, como fluxos, scripts, alertas, limites tecnicos e padroes editoriais.
- Antes de editar arquivos importantes, registrar a intencao quando a mudanca for relevante; depois, registrar o que foi realmente feito e validado.
- Nunca sobrescrever originais por padrao. Criar `backups/`, `old/` ou uma pasta de trabalho separada antes de alteracoes arriscadas.

### Reescrita editorial

- Reescrita profissional nao e resumo curto. Ela deve preservar a cobertura ampla do original, melhorar clareza, gramatica, estrutura, progressao didatica, referencias e experiencia de leitura.
- Antes de reescrever obra longa, criar mapa de cobertura: cada bloco, tese, exemplo ou capitulo relevante do original deve ter destino editorial claro.
- Cortar apenas repeticao real, erro grave, traducao corrompida, ruido irrecuperavel ou material fora de escopo. Teses, valores e argumentos autorais devem ser preservados e explicados melhor.
- Fortalecer argumentos quando defensaveis e corrigir explicitamente generalizacoes, riscos cientificos, eticos, juridicos ou logicos.
- Nao declarar uma base limpa, copia extraida, mapa literario ou prova parcial como livro publicavel.

### Conversao e diagramacao

- Preferir fonte canonica em Markdown, DOCX ou outro formato editavel; PDF final nao deve ser editado diretamente salvo pos-processamento especifico.
- Para DOCX grande em que Pandoc falha, extrair `word/document.xml` ou usar `python-docx` como fallback textual, marcando perda possivel de imagens, tabelas e estilos.
- Pandoc ajuda, mas conversao tecnica nao e diagramacao editorial. Validar folha de rosto, paginas em branco, sumario, inicio do miolo, cabecalho, rodape, numeracao, margens e hierarquia visual.
- Para PDF A5 via LaTeX/Pandoc, validar tamanho com `pdfinfo`. Em A5, espera-se aproximadamente `419.528 x 595.276 pts`.
- Se o Markdown ja contem titulo, subtitulo e autor no corpo, evitar duplicar bloco visual de titulo por metadados Pandoc; usar metadados apenas quando nao duplicarem a apresentacao.
- Em PDF A5 com classe LaTeX `book`, o espacamento padrao de `chapter` pode ficar grande demais. Usar `titlesec` ou controle equivalente quando os titulos ocuparem margem excessiva.
- Sumario final deve refletir paginacao real. Sumario manual pode servir para piloto, mas versao final deve ser atualizada pelo motor de diagramacao ou pelo editor.

### Validacao objetiva

- Validar DOCX e EPUB com `unzip -t`.
- Validar PDF com `pdfinfo`.
- Extrair texto com `pdftotext` e buscar titulo, capitulos, bibliografia, QR Code textual, termos obrigatorios, termos proibidos, nomes antigos e residuos de IA.
- Renderizar amostras com `pdftoppm` ou ferramenta equivalente: capa, folha de rosto, sumario, primeiro capitulo, pagina com imagem, referencias e ultima pagina.
- Regenerar todos os formatos depois de qualquer mudanca textual ou estrutural final, mesmo pequena.
- Uma revisao final seria deve terminar com evidencia: comandos executados, contagens, paginas, integridade dos artefatos, buscas limpas e pendencias humanas.

### UICLAP, miolo e capas

- `miolo` e o PDF interno do livro, sem capa completa externa. Capa completa UICLAP nao deve ser inserida dentro do PDF/EPUB/DOCX de leitura.
- A capa impressa UICLAP deve ser tratada como arquivo separado de upload, em uma unica imagem com contracapa a esquerda, lombada no centro e capa a direita.
- Recalcular lombada a partir da paginacao final do miolo. Se houver apenas estimativa, marcar como `estimativa_nao_final`.
- Reservar area para codigo de barras interno da plataforma e validar sangria, margem de seguranca, corte, legibilidade e preview 3D.
- Manter separados: frente simples, arte-base sem texto, capa completa, contracapa, lombada, QR Code, marketing e metadados.
- Usar estados explicitos:
  - `template_sem_capa_base`: placeholder tecnico;
  - `capa_candidata_estilo_curado`: arte tematica revisavel;
  - `prova_tecnica_com_capa_base`: prova com arte selecionada e lombada ainda pendente;
  - `pronta_para_upload`: somente depois de miolo final, lombada oficial, contracapa aprovada, codigo de barras/QR revisados e validacao visual.
- Antes de gerar capas em lote, inventariar o catalogo completo por idioma, confirmar contagens e pesquisar se ha PDFs mais recentes que os arquivos finais usados como miolo.

### Qualidade visual de capas

- Uma capa tecnicamente montada nao e necessariamente uma capa comercial. Medidas corretas, JPG valido, lombada, QR Code e metadados nao provam qualidade visual.
- Quando houver capas curadas no projeto, analisar essas referencias antes de criar novas capas. Comparar composicao, genero, cena, personagem/objeto central, luz, textura, paleta, contraste, legibilidade e promessa editorial.
- Capas abstratas geradas por script, com icones geometricos, redes, molduras e fundos tematicos, devem ser classificadas como `rascunho_tecnico_visual` ou `capa_candidata_baixa_fidelidade` quando nao tiverem cena narrativa, imagem comercial ou assunto visual concreto.
- Nao chamar de `estilo curado` uma capa que apenas substitui placeholder por padrao grafico. O termo so deve ser usado quando o resultado estiver visualmente proximo das capas curadas aprovadas pelo autor.
- Para livros de romance, ficcao, fantasia, biografia, produto autoral forte ou capa de venda, a regra preferencial e: gerar ou selecionar uma arte-base narrativa sem texto; depois aplicar titulo, subtitulo, autor, lombada e contracapa por composicao local.
- Para livros tecnicos, academicos ou ensaisticos, capa tipografica ou simbolica pode funcionar, mas ainda precisa de direcao visual, hierarquia, contraste, legibilidade em miniatura e coerencia com o tema.
- Se um piloto de capa ficar visualmente fraco, nao escalar o lote. Registrar a falha, ajustar briefing/prompt/referencia ou admitir que a automacao atual so serve para prova tecnica.
- Um lote de 50, 100 ou 150 capas sem revisao visual individual deve ser tratado como triagem ou rascunho, nao como entrega final de publicacao.

### QR Code e material promocional

- QR Code promocional deve entrar como material pos-textual no final de PDF/EPUB de leitura, com URL visivel e funcao clara de convite a outras obras.
- Em EPUB, inserir o QR Code como recurso interno com texto alternativo e link clicavel equivalente.
- Validar visualmente pelo menos um PDF e um EPUB antes de processar lotes.

### Capas geradas por IA

- Para capas com IA generativa, gerar a arte-base sem texto sempre que possivel. Titulo, subtitulo, autor, lombada e contracapa devem ser compostos localmente para garantir exatidao tipografica.
- A boa pratica demonstrada por capas comerciais e: escrever um briefing visual completo, gerar imagem narrativa sem texto, escolher a melhor tentativa, preservar a arte-base, aplicar tipografia por script e derivar capa digital, contracapa, marketing e UICLAP a partir dessa base.
- O prompt deve especificar genero, finalidade, cena, sujeito principal, objetos narrativos, composicao, espaco negativo para titulo, iluminacao, paleta, materiais, restricoes e itens proibidos. Deve pedir explicitamente `sem texto` quando a tipografia sera local.
- Capas geradas por IA podem ser boas quando a imagem comunica conteudo e promessa de leitura; podem ser ruins quando parecem stock generico, abstracao decorativa, simbolo vazio ou textura sem relacao concreta com o livro.
- Registrar prompt, prompts negativos, ferramenta, ausencia ou presenca de imagens de referencia, numero de tentativas, motivo da escolha, arquivo-base, dimensoes, hash, commit e scripts derivados.
- Preservar a arte-base original. Derivados podem perder metadados C2PA; a auditoria deve depender tambem de README, hash, historico Git e scripts.
- Nao confundir imagem gerada por IA, fotografia licenciada, colagem manual e composicao local. Cada origem exige registro proprio.
- Quando houver credenciais C2PA, `exiftool` pode ajudar a comprovar origem, agente gerador e tipo de fonte digital. A ausencia de C2PA em derivados nao invalida a origem se a cadeia estiver documentada por arquivo-base, hash, README, Git e scripts.

### Fluxo piloto de capa generativa

- Antes de escalar um lote, gerar um piloto em pasta separada, por exemplo `capas/pilotos-generativos/<slug-do-livro>/`.
- O piloto deve conter, no minimo:
  - arte-base sem texto, por exemplo `<slug>-base-generativa-v1.png`;
  - capa frontal com tipografia local, por exemplo `<slug>-capa-frontal-piloto-v2.png`;
  - capa completa limpa para revisao de upload, por exemplo `<slug>-capa-completa-uiclap-piloto-v2.jpg`;
  - preview de validacao com guias, por exemplo `<slug>-capa-completa-uiclap-piloto-v2-preview-validacao.jpg`;
  - `README.md` com status, fonte do miolo, metodo e limitacoes;
  - arquivo de prompt, por exemplo `prompt-base-generativa.md`;
  - script reprodutivel de composicao, por exemplo `build_pilot_cover.py`;
  - metadados, dimensoes e hashes, por exemplo `metadata-v2.json`.
- O arquivo limpo de capa completa nao deve conter guias, linhas de corte, avisos tecnicos, texto `piloto`, `preview`, `validacao`, `not final` ou explicacoes internas. Essas informacoes pertencem ao README, metadados e preview separado.
- Se uma versao intermediaria deixar texto tecnico visivel dentro da capa, ela deve ser preservada apenas como tentativa intermediaria ou descartada da entrega principal; gerar uma nova versao limpa antes de recomendar o piloto.
- A contracapa deve usar texto editorial/comercial coerente com o livro, com reserva para codigo de barras/ISBN. Nao usar a contracapa para explicar o processo tecnico ao leitor final.
- Validar a capa limpa e o preview separadamente: dimensoes em pixels, modo de cor, formato, DPI, tamanho de arquivo, legibilidade em miniatura, contraste, sangria, margem de seguranca, lombada, area de codigo de barras e ausencia de textos acidentais gerados por IA.
- Se a lombada vier de referencia visual, regra generica ou estimativa de paginas, registrar `estimativa_nao_final`. A lombada oficial deve ser confirmada depois do miolo final na UICLAP.
- Para miolos muito curtos, verificar se a plataforma permite lombada impressa ou exige capa sem texto de lombada; nao assumir que uma referencia de 16 mm vale para todos os livros.
- So escalar para outros livros depois que o autor aprovar o piloto visualmente e a equipe confirmar que o fluxo produz arte comercial, nao apenas prova tecnica.

### Temas sensiveis e rigor

- Em saude, neuropsiquiatria, depressao, suicidio, sexualidade, infancia e nutricao, separar tese moral, metafora, especulacao e evidencia cientifica.
- Autocuidado e estilo de vida podem ser apresentados como fatores de protecao e apoio, nao como cura garantida nem causa unica de adoecimento.
- Suicidio e crise psiquica exigem linguagem multifatorial, sem romantizacao, sem detalhes graficos e com orientacao de ajuda atualizada conforme o publico.
- Em textos religiosos, preservar a conviccao do autor sem desumanizar pessoas. Em textos seculares, remover residuo devocional quando o pacto de leitura exigir tom secular.
- Em livros tecnicos ou especulativos, classificar ideias como metafora, hipotese, prototipo, especificacao, algoritmo validado ou produto. Nao vender conjectura como prova.
- Usar referencias reais e verificaveis. Nunca inventar bibliografia.

### Processos pesados

- Para lotes grandes de Pandoc, LibreOffice, LaTeX, traducao ou extracao de DOCX, preferir execucao sequencial, cache, logs e lotes retomaveis.
- Quando houver risco de memoria, usar limites preventivos, por exemplo `systemd-run --user --scope -p MemoryMax=4G -p CPUQuota=200% ...`.
- Ao terminar, conferir que nao sobraram processos pesados como `pandoc`, `pdflatex`, `xelatex`, `libreoffice`, `soffice` ou scripts Python de lote.

## Validacao minima

Use comandos como:

```bash
unzip -t "publicacao/docx/livro.docx"
unzip -t "publicacao/epub/livro.epub"
pdfinfo "publicacao/pdf/livro.pdf"
pdftotext "publicacao/pdf/livro.pdf" -
```

Tambem procure residuos:

```bash
rg -n "TODO|FIXME|PLACEHOLDER|ChatGPT|texto-base|revisar depois" manuscrito docs publicacao || true
```

## Tipos de obra

### Ficcao e romance

Adicionar quando necessario:

- `docs/CHARACTERS.md`;
- `docs/CONTINUITY.md`;
- `docs/TIMELINE.md`;
- `docs/WORLD-BUILDING.md`;
- `docs/PLOT-THREADS.md`.

### Reportagem e noticia

Adicionar quando necessario:

- `docs/SOURCES.md`;
- `docs/FACT-CHECK.md`;
- `docs/INTERVIEWS.md`;
- `docs/RIGHTS-AND-PERMISSIONS.md`;
- `docs/LEGAL-REVIEW.md`.

### Academico, artigo e ensaio

Adicionar quando necessario:

- `docs/METHODOLOGY.md`;
- `docs/CITATION-STYLE.md`;
- `docs/BIBLIOGRAPHY.md`;
- `docs/ARGUMENT-MAP.md`;
- `docs/PEER-REVIEW-NOTES.md`.

### Tecnico e didatico

Adicionar quando necessario:

- `docs/EXAMPLES.md`;
- `docs/EXERCISES.md`;
- `docs/ERRATA.md`;
- `docs/GLOSSARY.md`;
- `docs/TECHNICAL-VALIDATION.md`.

## Prontidao editorial

Um livro pode ser considerado pronto para revisao humana final quando:

- o manuscrito-fonte esta definido;
- as decisoes principais estao registradas;
- a cobertura do original foi preservada ou as perdas foram justificadas;
- os artefatos publicos foram regenerados;
- PDF, DOCX e EPUB passaram por validacao tecnica;
- capa, sumario, margens, imagens, QR Code, metadados e ultima pagina foram conferidos;
- para UICLAP, miolo e capa completa externa foram validados separadamente;
- a capa final foi comparada com referencias curadas e nao apenas validada por dimensao/integridade;
- pendencias humanas estao documentadas;
- o historico local esta atualizado.

## Uso do gerador

```bash
python3 templates/create_book_project.py "Meu Livro" --author "Nome do Autor" --genre "romance" --language pt --target-dir .
```

O gerador cria um projeto de livro com estrutura editorial padronizada.
