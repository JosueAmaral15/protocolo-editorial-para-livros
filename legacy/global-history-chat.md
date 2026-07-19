## 2026-06-03 - Práticas reutilizáveis para edição de livros com IA

- Sempre que um projeto de livro tiver histórico próprio, manter também um histórico global apenas para aprendizados reutilizáveis entre obras. O histórico local registra decisões e mudanças específicas do livro; o global registra fluxos, validações, padrões editoriais, scripts e cuidados que podem ajudar outros livros.
- Para livros em Markdown, preservar uma fonte principal em `working/` e gerar os formatos finais em `public/`. Evitar sobrescrever a fonte original em português quando criar traduções; gerar um Markdown traduzido separado.
- Para edição em página A5, um fluxo robusto é usar Pandoc para LaTeX com `documentclass=book`, `papersize=a5`, margem de 15mm, sumário automático, cabeçalho com título/autor e rodapé com número de página. Validar o PDF com `pdfinfo`; tamanho A5 esperado: aproximadamente `419.528 x 595.276 pts`.
- Para DOCX A5, usar `--reference-doc` com um arquivo de referência A5 quando disponível. Validar o tamanho da página no DOCX inspecionando `word/document.xml` e procurando `w:pgSz`; A5 costuma aparecer como `w:w="8391" w:h="11906"` em twips.
- Para EPUB/DOCX, validar integridade com `unzip -t`. Para EPUB, conferir metadados no `EPUB/content.opf`, especialmente `dc:title`, `dc:creator` e `dc:language`.
- Para tradução automática de livros inteiros, preferir um script com cache por segmento. Segmentar o Markdown por blocos de parágrafos, traduzir em lotes menores e salvar cache por hash do texto original. Isso permite retomar a tradução sem refazer tudo em caso de falha de rede ou limite do serviço.
- Traduções automáticas devem receber pós-processamento global para proteger título, nome do autor, nomes próprios, marcas fictícias, idioma do EPUB e termos recorrentes. Mesmo assim, registrar explicitamente que a tradução automática precisa de revisão literária humana antes de publicação comercial.
- Ao traduzir, verificar termos residuais do idioma original com buscas direcionadas. Exemplo: procurar cabeçalhos antigos, nomes de seções, dias da semana, termos técnicos e fragmentos com acentos ou palavras frequentes do idioma de origem.
- Para revisões de coerência narrativa, validar datas com script contra o calendário real quando o texto usa dia da semana, dia, mês, ano e horário. Isso reduz erros silenciosos em romances com alternância temporal.
- Quando houver mudanças de tempo, especialmente flashbacks ou saltos para o futuro, inserir data/hora explícita sempre que a ausência puder confundir a leitura.
- Para temas técnicos recorrentes em ficção científica, manter decisões conceituais consistentes: se duas tecnologias são diferentes, evitar explicar uma como componente da outra; concentrar a apresentação da tecnologia no ponto narrativo em que ela passa a existir de fato.
- Antes de commit final, checar marcadores acidentais como `TODO`, `FIXME`, conflitos de merge, grafias antigas de nomes e termos removidos por decisão editorial.
- Quando houver arquivos obsoletos em `public/`, remover ou renomear para evitar que produtos finais não atualizados sejam confundidos com versões publicáveis.

## 2026-06-03 - Checklist reutilizável de prontidão para publicação

- Para declarar um manuscrito como tecnicamente pronto para publicação, combinar checagens de texto e de artefatos finais: contagem de palavras/linhas, estrutura de capítulos, datas, marcadores acidentais, termos editoriais removidos, integridade de DOCX/EPUB e metadados de PDF/EPUB.
- Em livros com datas explícitas, validar automaticamente dia da semana, dia, mês e ano. A ausência de erro de calendário não prova qualidade literária, mas remove uma classe comum de inconsistência.
- Em manuscritos revisados muitas vezes, procurar grafias antigas de personagens, nomes trocados, termos removidos por decisão editorial e marcas de edição (`TODO`, `FIXME`, conflitos de merge).
- Em livros com conceitos técnicos, fazer busca por termos antes do ponto narrativo em que eles deveriam aparecer. Isso ajuda a evitar spoilers conceituais e inconsistência de progressão.
- A publicação "hoje" pode ser tecnicamente possível quando os arquivos estão íntegros e coerentes; ainda assim, manter como etapa final recomendada uma leitura visual/folheio do PDF em dispositivo real para detectar quebras ruins, viúvas/órfãs, páginas visualmente pobres e preferências de acabamento.
- Diferenciar prontidão técnica de prontidão literária/comercial: uma tradução automática validada tecnicamente pode gerar DOCX/PDF/EPUB corretos, mas ainda deve exigir revisão literária humana antes de publicação comercial.

## 2026-06-03 - Diretriz de uso do histórico global

- O usuário solicitou que `/home/josue/Documents/josue-writter-workspace/global-history-chat.md` seja usado, sempre que necessário, para registrar aprendizados relevantes e reutilizáveis sobre modificação de livros com inteligência artificial.
- O histórico global deve receber informações que possam ajudar outros livros, outros projetos, outras inteligências artificiais e seres humanos: padrões editoriais, fluxos técnicos, validações, limites de memória, estratégias de tradução, cuidados ABNT, organização de arquivos, auditorias e decisões recorrentes.
- O histórico local de cada projeto deve continuar registrando ações específicas daquele livro. O histórico global deve evitar excesso de detalhes circunstanciais e registrar apenas o que tiver valor de reaproveitamento.
- Sempre que uma tarefa gerar um método útil, uma prevenção importante, um erro corrigido ou uma prática aplicável a outros livros, avaliar se vale acrescentar um resumo no histórico global.
- A decisão de registrar no histórico global deve ser criteriosa: nem toda alteração pequena precisa ir para lá; devem entrar principalmente padrões, aprendizados, scripts, validações e cautelas que economizem trabalho ou evitem erros em futuras publicações.

## 2026-06-03 - Aprendizado reutilizável: tradução complementar de arquivos individuais

- Quando livros consolidados já foram traduzidos, traduções posteriores de arquivos individuais devem reaproveitar o mesmo cache de tradução. Isso evita retraduzir parágrafos repetidos e reduz tempo, rede e risco de variações terminológicas.
- Mesmo com cache, arquivos de anos novos ou complementares podem conter trechos inéditos e mistos. Rodar auditoria textual final com padrões do idioma de origem é indispensável.
- Uma boa validação para traduções em lote deve conferir, no mínimo:
  - contagem esperada de arquivos por formato;
  - PDF em A5 com `pdfinfo`;
  - integridade de EPUB com `zipfile.testzip()` ou `unzip -t`;
  - ausência de marcadores internos de tradução;
  - ausência de cabeçalhos ou termos estruturais do idioma original;
  - ausência de locks e temporários do LibreOffice;
  - inexistência de processos pesados remanescentes.
- Para livros grandes traduzidos automaticamente, pode ser necessário combinar tradução por blocos marcados, cache por segmento e reparo dirigido de linhas residuais. Depois de qualquer reparo textual no Markdown final, regenerar DOCX, PDF e EPUB para manter os formatos sincronizados.

## 2026-06-03 - Aprendizado reutilizável: rebranding editorial de livros

- Quando um livro muda de título, subtítulo ou nomes centrais de personagens, tratar a alteração como rebranding completo, não como simples busca e troca no manuscrito.
- A troca deve sincronizar: Markdown fonte, traduções, plano editorial, scripts de exportação, metadados YAML/Pandoc, cabeçalhos de PDF, nomes públicos de DOCX/PDF/EPUB e nomes internos de build.
- Depois de gerar os novos formatos, remover artefatos antigos em `public/` e `build/` para evitar que versões com identidade anterior sejam usadas como produto final.
- Validar a mudança com buscas por sobrenomes antigos, títulos antigos como cabeçalhos, nomes antigos de arquivos e metadados antigos. Conferir também `pdfinfo`, integridade de DOCX/EPUB com `unzip -t` e metadados do EPUB.

## 2026-06-03 - Aprendizado reutilizável: extração de DOCX grande quando Pandoc falha

- Em DOCX grandes ou complexos, a conversão direta com Pandoc pode falhar sem gerar Markdown. Uma alternativa segura é extrair `word/document.xml` do DOCX e converter os parágrafos em Markdown por script.
- O fluxo recomendado é: mover o DOCX original para `old/`, copiar para `backup/`, extrair para um Markdown em `working/`, separar capítulos em `build/chapters/` e gerar um relatório de análise antes de reescrever.
- Para reescritas de continuação, verificar continuidade de nomes, sobrenomes, títulos e eventos do livro anterior antes de criar a nova versão.
- Uma primeira reescrita condensada pode funcionar como mapa literário de alto impacto: preserva todo o arco, corrige direção dramática e serve de base para expansão capítulo por capítulo até tamanho publicável.

## 2026-06-03 - Aprendizado reutilizável: reescrita longa publicável com base filosófica

- Quando o objetivo é publicação comercial, uma reescrita condensada não substitui o manuscrito. A nova versão deve manter volume, contexto, episódios, personagens, problema e solução em densidade equivalente ao original.
- Antes de reescrever um livro longo com imagens, separar imagens embutidas do Markdown/DOCX para uma pasta `imagens/` e gerar uma fonte limpa em `working/` com links relativos. Isso facilita exportar DOCX/PDF/EPUB depois.
- Quando o usuário fornece obras filosóficas próprias como referência, transformar os conceitos em um guia editorial de aplicação narrativa. A filosofia deve aparecer por conflito, escolha, consequência, diálogo e amadurecimento de personagens, não como colagem ensaística.
- Para romances de ficção científica com salto temporal, registrar data e hora em mudanças relevantes de tempo, local ou arco narrativo, especialmente quando houver alternância entre passado, presente e futuro.
- Para manter padrão de publicação, trabalhar capítulo por capítulo, com validação de estrutura, imagens, continuidade de nomes e coerência temática antes de commit.
- Não chamar uma base limpa, uma cópia adaptada ou uma versão apenas estrutural de "reescrita publicável". Em livros longos, a entrega deve distinguir três estados: fonte original organizada, base de trabalho com continuidade/metadados ajustados e reescrita literária real.
- Antes de exportar `docx`, `pdf` ou `epub`, confirmar que os capítulos prometidos foram de fato reescritos. Se a base ainda está crua, remover exports incompletos de `public/` para não confundir rascunho com produto final.

## 2026-06-04 - Aprendizado reutilizável: encerramento ético em ficção científica

- Em histórias com tecnologias de vida, morte, teletransporte, recuperação biológica ou vigilância, o fechamento deve resolver o arco dramático sem normalizar soluções autoritárias apenas porque a tecnologia permite.
- Evitar finais em que criminosos são apagados, mortos, transformados ou privados de processo por conveniência narrativa. Mesmo em ficção especulativa, devido processo, registro público e governança fortalecem a persuasão ética do livro.
- Relações afetivas após trauma devem amadurecer com cuidado: gratidão, resgate e vulnerabilidade não devem virar namoro ou casamento instantâneo sem escolha, tempo e reciprocidade.
- Expansões empresariais em planos narrativos devem ser apresentadas como parcerias auditáveis, regulação, licenciamento e governança quando o tema envolve saúde, corpos, dados ou reanimação. Compra de empresa para mitigar crime ou calar processo enfraquece a credibilidade moral.
- Ao revisar ficção científica, pesquisar termos removidos com cuidado para evitar falso positivo: palavras como `maçã` podem aparecer dentro de `informação`. Preferir buscas com fronteira de palavra quando o objetivo é achar sobras literais.

## 2026-06-04 - Aprendizado reutilizável: exportação A5 com Pandoc sem duplicar título

- Quando um Markdown já contém título, subtítulo e autor no corpo do texto, passar `--metadata title=...` ao Pandoc pode gerar um bloco de título visual duplicado no PDF/DOCX.
- Para PDF com metadados sem duplicação visual, usar variáveis LaTeX como `-V title-meta='Título'` e `-V author-meta='Autor'`, mantendo o título textual no próprio Markdown.
- Para PDF A5, um comando funcional é usar `-V papersize=a5 -V geometry:margin=1.8cm`; validar com `pdfinfo` para confirmar `Page size: 419.528 x 595.276 pts`.
- Em instalações LaTeX antigas, `--metadata lang='pt-BR'` pode falhar com erro de Babel (`Unknown option 'brazil'`). Nesses casos, evitar esse metadado no PDF e aplicar idioma principalmente no EPUB/DOCX quando necessário.
- Pandoc não garante tamanho de página A5 no DOCX sem `reference-doc`. Uma alternativa é ajustar `word/document.xml` após a geração, definindo `w:pgSz` para A5 (`w=8391`, `h=11906`) e margens em twips.
- Antes de publicar, validar formatos com `unzip -t` para DOCX/EPUB, `pdfinfo` para PDF, inspeção de metadados e renderização rápida de páginas-chave com `pdftoppm`.

## 2026-06-04 - Aprendizado reutilizável: conversão técnica não é diagramação editorial

- Um arquivo DOCX/PDF/EPUB pode estar tecnicamente íntegro e ainda assim estar ruim para publicação. Validações como `unzip -t`, `pdfinfo` e presença de imagens não verificam qualidade editorial de folha de rosto, sumário, brancos, quebras de seção, hierarquia visual e experiência de leitura.
- Para livros impressos, especialmente A5, separar claramente: folha de rosto, folha em branco, sumário, dedicatória, personagens/elementos pré-textuais e miolo. Não deixar sumário, dedicatória e lista de personagens colados à primeira página do título.
- Descrições de acessibilidade de imagens são úteis na fonte, mas não devem aparecer como parágrafos visíveis no PDF impresso comercial. Na fonte de exportação, removê-las ou convertê-las em metadado/alt text.
- Quando existir um livro anterior com padrão aprovado, reaproveitar seus scripts, `reference-doc`, fluxo LaTeX e inspeções visuais antes de entregar a nova obra. Não assumir que o padrão mínimo do Pandoc é equivalente ao padrão editorial anterior.
- Renderizar páginas-chave do PDF antes de finalizar: capa/folha de rosto, página em branco, sumário, primeiro capítulo, página com imagem e última página. Essa inspeção visual deve ser obrigatória, não opcional.
## Reescrita editorial de livros com IA para publicação

Ao reescrever livros com IA para publicação comercial, especialmente em plataformas como UICLAP, recomenda-se:

- nunca sobrescrever os originais;
- criar uma pasta de saída separada para versões reescritas;
- trabalhar por fases: inventário, extração textual, diagnóstico editorial, reestruturação, reescrita, normalização ABNT, referências, geração de DOCX/PDF/EPUB e auditoria final;
- não prometer "best-seller" como resultado garantido, pois isso depende de mercado, distribuição, capa, nicho, preço, reputação e divulgação;
- buscar "potencial comercial forte" com título, subtítulo, promessa editorial clara, capítulos coesos, linguagem mais fluida, exemplos, aplicação prática, sumário, referências verificáveis e acabamento compatível com venda;
- usar apenas referências reais e verificáveis, evitando citações inventadas;
- separar livros grandes em partes para reduzir consumo de memória e permitir revisão.

### Fluxo DOCX -> Markdown intermediário

Para projetos editoriais grandes, é útil converter DOCX para Markdown antes da reescrita:

- usar Pandoc quando possível, com `--wrap=none` e `--extract-media`;
- aplicar limite de memória ao Pandoc quando houver arquivos grandes;
- usar prefixos numéricos ou identificadores únicos para evitar colisão de nomes;
- manter log de conversão;
- quando Pandoc falhar, usar `python-docx` como fallback textual;
- marcar arquivos convertidos por fallback para revisão de imagens, tabelas e formatação no DOCX original.

### Sumário em DOCX/PDF gerado por Pandoc

Em DOCX gerado por Pandoc, `--toc` pode criar campo automático que depende de atualização no LibreOffice/Word. Ao exportar diretamente para PDF por LibreOffice headless, o sumário pode não aparecer expandido como esperado. Para versões piloto de revisão, um sumário manual visível no Markdown pode ser mais previsível. Para versão final ABNT, o ideal é atualizar o sumário automático no editor antes da exportação final.

### Reescrita como inspeção argumentativa, não autoria substitutiva

Quando o usuário pede reescrita editorial de livros autorais para venda, a tarefa pode significar revisão profunda dos argumentos, não criação de livro novo. Nesses casos:

- preservar a tese do autor como eixo;
- explicar a mesma ideia com linguagem mais clara e publicável;
- organizar, estruturar, eliminar redundâncias e melhorar transições;
- fortalecer argumentos quando forem defensáveis;
- corrigir criticamente quando houver generalização, risco científico, ético, jurídico ou lógico;
- sinalizar hipóteses, especulações e afirmações fortes;
- usar referências para sustentar ou delimitar o argumento original, sem substituir a autoria;
- manter estilo final com rigor acadêmico, como tese, mas voltado ao leitor consumidor.

## 2026-06-04 - Aprendizado reutilizável: travessão, matéria principal e ética autoral

- Em manuscritos Markdown, falas iniciadas com `- ` podem ser convertidas pelo Pandoc em listas/bullets. Antes de exportar romances, normalizar diálogos para travessão (`— `) na fonte ou no script de limpeza.
- Em PDF de livro com pré-textuais, a numeração árabe deve começar no miolo. No LaTeX, inserir `\mainmatter` e `\setcounter{page}{1}` imediatamente antes do primeiro capítulo, não antes de dedicatória, personagens ou outros pré-textuais.
- O sumário deve ser validado depois da segunda compilação LaTeX, porque o arquivo `.toc` pode preservar paginação antiga se a transição para matéria principal mudou.
- Em revisão narrativa, não impor uma interpretação moral externa ao projeto do autor. Quando o autor entende justiça como punição proporcional, pública e fundamentada, o texto pode distinguir punição legítima de vingança, falsa misericórdia e impunidade sem enfraquecer a posição filosófica do livro.
- Resíduos de estilo visual, como `cyberpunk` em obra que deve ser `solarpunk`, precisam ser buscados tanto na narrativa quanto em descrições de imagem, metadados, prompts e textos auxiliares.

## 2026-06-04 - Aprendizado reutilizável: solarpunk narrativo e imagens subordinadas à história

- Em ficção científica, `solarpunk` não é apenas estética de jardins, painéis solares e cidades verdes. Pode funcionar como direção ética da história: otimismo científico, tecnologia a favor da saúde, bem-estar, reparação, justiça, convivência humana e dignidade.
- Imagens, descrições de acessibilidade e prompts visuais não devem determinar a narrativa. Se uma imagem contradiz uma decisão melhor de enredo, ajustar a descrição ou trocar a imagem depois; a história vem primeiro.
- Ao buscar potencial comercial forte em romance, protagonistas muito solenes podem perder naturalidade. Humor leve, autoconsciência, pequenas falhas sociais e respostas ponderadas ajudam a aproximar o leitor sem enfraquecer profundidade ética.
- Para diferenciar personagens próximos, mostrar contraste em ação: um pai pode agir por amor com mais pânico e impulso; o filho pode amar com igual intensidade, mas demonstrar prudência, escuta e capacidade de decidir em equipe.
- Quando um vilão não aceita captura e escolhe suicídio, evitar que isso vire encerramento conveniente: manter investigação, responsabilização de cúmplices, preservação de provas e consequências patrimoniais/históricas.

## 2026-06-04 - Aprendizado reutilizável: auditoria sem imagens

- Quando imagens ficam inconsistentes com a narrativa, remover as referências de imagem e descrições da fonte Markdown antes de regenerar DOCX/PDF/EPUB. Esconder imagens apenas no exportador pode deixar a fonte orientada por cenas visuais erradas.
- Depois de remover imagens, validar também os artefatos: DOCX/EPUB com contagem de mídia zero e PDF sem entradas em `pdfimages -list`.
- A remoção de imagens pode reduzir muito a paginação; refazer sumário e conferir a página inicial do Capítulo 1 depois da conversão.
- Em auditoria de continuidade, procurar pares de contradição concretos: personagem morto/depois vivo, desaparecido/depois retornado, carro/objeto atribuído à pessoa errada, sentença/julgamento incompatível com morte anterior, e datas com fuso horário misturado.
- Ao corrigir inconsistências, preferir preservar o arco já aprovado: ajustar o detalhe causal menor em vez de reescrever um capítulo inteiro sem necessidade.

## 2026-06-04 - Aprendizado reutilizável: morte seguida de reanimação não é contradição automática

- Em romances com ressuscitação, reanimação ou tecnologias de reversão da morte, `personagem morto` e `personagem vivo depois` não deve ser tratado automaticamente como erro de continuidade.
- Antes de corrigir esse tipo de arco, comparar com o original e com a intenção autoral. A morte anterior pode ser parte deliberada da lógica do enredo.
- A solução editorial adequada é tornar explícita a cadeia causal: morte, impossibilidade de resgate imediato, recuperação do corpo, reanimação posterior e consequências psicológicas/morais.
- Em histórias com tecnologia de vida/morte, a auditoria deve distinguir inconsistência real de evento extraordinário validado pelas regras internas da obra.

## 2026-06-04 - Aprendizado reutilizável: amizade inicial antes de romance e desaparecimento

- Quando um interesse afetivo é recém-apresentado, fortalecer a relação antes de um sequestro/desaparecimento não exige romance acelerado. Pequenas falas, humor contextual, limites claros e sinais de curiosidade mútua tornam a perda mais sentida sem parecer posse.
- Para personagens prudentes, a química pode aparecer em brincadeiras de área profissional, piadas internas simples e correções gentis de comportamento. Isso preserva naturalidade e evita declarações grandes demais cedo demais.
- Uma boa solução é nomear a fase como possibilidade, não promessa: amizade em teste, conversa inicial, confiança sendo construída. Assim o drama posterior pesa porque interrompe um futuro possível, não porque inventa intimidade artificial.

## 2026-06-04 - Aprendizado reutilizável: amor altruísta que amadurece para romance

- Para evitar romance possessivo, mostrar o personagem deixando de querer `ter` a pessoa para querer que ela esteja viva, saudável, livre e bem, mesmo sem recompensa afetiva.
- O amor conjugal pode nascer depois disso sem contradição: o cuidado altruísta cria segurança; a outra pessoa percebe que não está sendo cobrada; a aproximação romântica passa a ser escolha, não dívida.
- Abraços graduais ajudam a marcar evolução: primeiro acolhimento respeitoso, depois abraço de amizade segura, depois contato romântico espontâneo quando ambos reconhecem reciprocidade.
- Em cenas pós-trauma, evitar que o romance pareça recompensa por salvamento. Inserir uma conversa intermediária ou testemunho de terceiro pode mostrar que a paixão surge por caráter, cuidado e liberdade preservada.

## 2026-06-04 - Aprendizado reutilizável: títulos de capítulos alinhados ao conteúdo

- Em romance de ficção científica, títulos de capítulos funcionam melhor quando nomeiam conflito, virada dramática ou função narrativa, não apenas temas abstratos.
- Títulos genéricos como `assuntos preocupantes`, `descobertas` ou `tentativas` podem ser substituídos por formulações que indiquem quem age, o que está em jogo e qual tensão conduz o capítulo.
- Ao renomear capítulos, conferir início e fim de cada capítulo: o título deve representar o arco inteiro, não apenas a primeira cena.
- Depois de renomear, atualizar sumário manual, âncoras Markdown e exportações finais, validando o sumário do PDF/DOCX/EPUB.

## 2026-06-04 - Aprendizado reutilizável: normalidade social depois do trauma

- Depois de capítulos de sequestro, guerra, resgate ou atentado, cenas de convivência comum ajudam o leitor a sentir que os personagens continuam vivos fora da crise.
- Confraternizações, eventos acadêmicos, fins de semana, festas pequenas e encontros casuais podem mostrar amizade, humor e recuperação emocional sem precisar criar novo conflito grave.
- Para romance em amadurecimento, encontros por coincidência funcionam melhor quando a pessoa amada aparece vivendo a própria vida, não como recompensa narrativa do protagonista.
- Cenas sociais também diferenciam personagens secundários: um amigo pode amadurecer, outro pode brincar, outro pode filosofar, outro pode aprender limites. Isso fortalece o grupo e torna o salto temporal mais convincente.

## 2026-06-04 - Aprendizado reutilizável: amizade como recomendação, não coerção

- Em grupos de protagonistas éticos, amizade forte não precisa virar imposição. Personagens podem sugerir caminhos, oferecer conselhos, criar oportunidades e apontar riscos, preservando o livre-arbítrio de quem decide.
- Humor com `regras` ou `missões obrigatórias` pode soar controlador se o tema do livro é maturidade moral. Uma solução é trocar por `propostas`, `recomendações`, `convites` e escolhas explicitamente aceitas.
- Para amadurecimento convincente, mostrar que cada amigo contribui por uma virtude própria: técnica, prudência, ética, saúde, visão de futuro ou reflexão filosófica. A decisão final deve continuar pertencendo ao personagem que precisa crescer.
- Em romance ou amizade pós-trauma, evitar encontros fabricados como manipulação. Convites abertos e coincidências verossímeis preservam autonomia e tornam a aproximação mais natural.

## 2026-06-04 - Aprendizado reutilizável: imortalidade precisa de sentido moral

- Em narrativas sobre vida prolongada, reanimação ou sobrevivência eterna, a pergunta filosófica não deve ficar apenas em `como viver mais`, mas em `para quê viver mais`.
- Um eixo forte é tratar a preservação da humanidade como virtude orientada por amor próprio e amor fraternal: cuidar de si para não se destruir, cuidar do outro para preservar vidas humanas concretas e preservar a espécie sem transformar pessoas em propriedade.
- Romance altruísta combina bem com esse tema quando o personagem aprende a amar sem forçar reciprocidade, sem esperar pagamento afetivo e sem usar o cuidado como domínio.
- Quando uma ideia filosófica ficar pesada em uma única fala, distribuir em camadas: primeiro uma formulação breve diante do grupo; depois uma conversa íntima em que os personagens relacionam a ideia com experiência, medo, trauma, desejo e escolha. Isso preserva profundidade sem sacrificar naturalidade.

## 2026-06-04 - Aprendizado reutilizável: namoro pós-trauma com carinho e autonomia

- Quando um romance nasce depois de resgate, sequestro ou trauma, o pedido de namoro fica mais convincente se houver antes uma rotina pequena: refeições, mensagens, caminhadas, silêncios confortáveis e gestos de cuidado sem cobrança.
- A aceitação pode incluir limites explícitos. Isso preserva autonomia da pessoa resgatada e impede que gratidão seja confundida com obrigação amorosa.
- Para deixar a relação carinhosa sem infantilizar, usar detalhes cotidianos: bilhetes, humor interno, apoio em provas, respeito a dias difíceis, pequenas correções, contato físico consentido e brincadeiras dos amigos.
- Mostrar que a pessoa beneficiada pelo amor floresce com mais segurança, sem se tornar dependente. Amor maduro ajuda, mas não promete curar tudo.
- Contato físico mais íntimo deve avançar em etapas: primeiro proximidade simples, depois cabeça no ombro, depois carícias ou acolhimento mais explícito, sempre com consentimento verbal ou contextual claro. Em personagens traumatizados, perguntar antes de tocar pode ser romântico porque demonstra cuidado e segurança.
- Se o arco exige namoro gradual, o primeiro beijo real costuma funcionar melhor depois de uma decisão explícita de reciprocidade. Antes disso, um abraço, quase-beijo ou desejo contido pode preservar tensão romântica sem acelerar a intimidade.
- Para protagonistas inteligentes, a imaturidade afetiva não precisa parecer burrice. Uma boa alternativa é mostrar a pessoa começando a avançar demais, percebendo o erro no meio da fala ou do gesto, aceitando ser corrigida e ajustando o comportamento rapidamente.
- Sub-romances podem nascer de amizade indireta: dois personagens convivem por causa do casal principal, tornam-se amigos, e só depois um deles percebe interesse. Se o flerte começa com quem se apaixonou primeiro, o outro personagem pode identificar os sinais e seguir com cuidado, sem parecer perseguição romântica.

## 2026-06-04 - Aprendizado reutilizável: amizade intelectual entre superdotados

- Quando dois personagens superdotados têm afinidade técnica, a amizade pode nascer de reconhecimento intelectual, não de intimidade sentimental imediata.
- Um personagem mais velho pode funcionar como mentor sem absolver erros: reconhecer talento, explicar riscos éticos e oferecer desafios técnicos que exigem responsabilidade.
- Para evitar culto ao gênio, equilibrar capacidade com legitimidade e consequência. A conversa profunda deve mostrar que saber fazer não autoriza fazer sozinho.

## 2026-06-04 - Aprendizado reutilizável: recuperar worldbuilding sem voltar à exposição

- Quando uma reescrita reduz demais a descrição de mundo, recuperar elementos do original em fragmentos distribuídos por cena, não em blocos enciclopédicos.
- Bons pontos de inserção: deslocamento do personagem, entrada em prédio público, refeição, aula, reunião corporativa, atendimento médico, painel de notícia ou conversa casual.
- Cada fragmento deve fazer dupla função: descrever o mundo e revelar uma tensão moral, social ou emocional percebida pelo personagem.

## 2026-06-04 - Aprendizado reutilizável: revisão de textos psicológicos sensíveis

- Em livros ensaísticos sobre psicologia, infância, sexualidade, saúde mental e comportamento social, separar tese moral, crença religiosa, metáfora interpretativa e evidência científica.
- Preservar a preocupação autoral com autocuidado, prudência, limites, maturidade e responsabilidade, mas retirar determinismos que ligam um único hábito a crime, orientação sexual, transtorno mental ou destino moral.
- Preferir `comportamentos abusivos` ou `padrões tóxicos` a rótulos definitivos sobre pessoas. Isso mantém a crítica ética sem transformar indivíduos em caricaturas clínicas.
- Em saúde mental, sempre qualificar: autocuidado ajuda, mas não substitui psicoterapia, psiquiatria, medicina, proteção contra abuso ou avaliação profissional quando há sofrimento persistente, risco ou prejuízo funcional.
- Em sexualidade infantil e adolescente, deslocar o foco para proteção, prevenção de abuso, orientação adequada à idade, responsabilidade familiar e cuidado profissional, evitando estigmatização de grupos humanos.

## 2026-06-04 - Aprendizado reutilizável: ciência atual, especulação e finitude

- Em livros sobre envelhecimento, morte, consciência, IA, medicina regenerativa e tecnologias futuras, separar três camadas: ciência estabelecida, hipótese filosófica e especulação tecnológica.
- Preservar ideias autorais radicais quando elas funcionam como horizonte filosófico, mas qualificá-las explicitamente quando não são prática médica atual.
- Não prometer imortalidade, rejuvenescimento, ressurreição, cura total ou recuperação de consciência original. Formular como pergunta, hipótese ou imaginação científica futura.
- Em tanatologia, equilibrar luta pela vida com dignidade no morrer: cuidado paliativo, luto, memória, legado e alívio de sofrimento precisam aparecer ao lado de qualquer esperança tecnológica.
- Relatos extremos de longevidade devem ser tratados como anedotas ou alegações, não como evidência suficiente para tese biomédica.

## 2026-06-04 - Aprendizado reutilizável: ética sexual conservadora sem estigmatização

- Em livros que defendem castidade, fidelidade, casamento, abstinência ou crítica ao sexo casual, preservar a tese moral do autor como proposta ética, não como diagnóstico universal sobre pessoas.
- Distinguir sempre: infidelidade, abuso, coerção, exploração, compulsão e violência são problemas éticos e/ou clínicos; orientação sexual, por si só, não é doença, crime ou parafilia.
- Críticas à pornografia, masturbação ou sexo casual ficam mais publicáveis quando formuladas como riscos possíveis, danos relacionais, perda de coerência com um projeto conjugal ou necessidade de autocontrole, não como causalidade inevitável para transtornos ou crimes.
- Em sexualidade, incluir consentimento claro, prevenção de ISTs, testagem, responsabilidade reprodutiva, honestidade sobre vínculos e busca de ajuda profissional quando há sofrimento, trauma, compulsão ou prejuízo funcional.
- Papéis masculinos e femininos podem ser apresentados como visão moral do autor, mas devem ser acompanhados de dignidade recíproca: proteção não é controle; provisão não é domínio; diferença biológica não reduz a pessoa a função.

## 2026-06-04 - Aprendizado reutilizável: textos técnicos com código corrompido ou multilíngue

- Quando um manuscrito técnico mistura idiomas, traduções automáticas e código sintaticamente quebrado, não publicar o código como exemplo executável. Tratar como intenção algorítmica ou hipótese de design.
- Em livros de programação, separar definição formal, metáfora didática e especulação técnica. Metáforas com realidade, linguagem natural, cérebro ou circuitos ajudam, mas não substituem conceitos formais.
- Corrigir explicitamente erros lógicos quando afetam a tese: por exemplo, bicondicional equivale a XNOR/equivalência lógica, não a NOR.
- Se o material tem valor conceitual, transformar blocos quebrados em princípios: abstração, decomposição, modularização, requisitos, validação, eficiência, legibilidade e manutenção.

## 2026-07-16 - Aprendizado reutilizável: rebranding editorial completo exige renomear arquivos e saídas

- Quando um livro muda de título, não basta alterar o conteúdo interno. Renomear também o manuscrito principal, os nomes públicos dos artefatos gerados, os caminhos dos scripts e as referências documentais evita que versões antigas continuem parecendo válidas.
- O rebranding editorial deve abranger, em conjunto: Markdown fonte, scripts de exportação, metadados, nomes de EPUB/DOCX/PDF/HTML, nome da capa UICLAP e qualquer arquivo de apoio que seja apresentado como produto final.
- Depois da troca, remover ou sobrescrever artefatos antigos em `build/` e `publicacao/` para não deixar duas identidades coexistindo. Se o nome antigo continuar disponível, ele pode ser confundido com a versão oficial.
- Validar a migração com busca textual por nomes antigos, conferência do caminho do manuscrito no script de build e inspeção dos diretórios de saída. Se sobrar referência antiga em um script, o rebuild vai regenerar o erro com nome novo apenas pela metade.
- Quando o nome do livro muda, a documentação histórica pode continuar citando o nome antigo apenas como registro do que aconteceu. O que não deve ficar antigo são os caminhos operacionais do produto final.

## 2026-07-16 - Aprendizado reutilizável: build de livro com Pandoc e capa UICLAP precisa de limpeza automática

- Um fluxo útil para livros em Markdown é manter a fonte em um arquivo principal e gerar EPUB, DOCX, HTML e PDF de prova a partir dele com Pandoc. Isso facilita manter formatos sincronizados sem editar manualmente cada saída.
- Para PDF de prova em A5, uma configuração compacta com `documentclass=book`, `papersize=a5`, margens moderadas e fonte de miolo consistente ajuda a medir o tamanho real do livro antes da publicação.
- Se a prova usa uma fonte específica, como Lexend, convém embutir a fonte localmente ou garantir disponibilidade no ambiente. Isso reduz divergência tipográfica entre máquinas.
- Em capa UICLAP, a estimativa de lombada deve depender da contagem real de páginas do miolo atual. Um valor padrão antigo pode continuar funcionando tecnicamente, mas produzirá uma capa errada se a paginação tiver mudado.
- Scripts de capa e publicação devem apagar versões antigas com basename obsoleto antes de gerar os artefatos novos. Isso evita lixo de build, reduz confusão visual e deixa claro qual é a entrega atual.
- Depois de qualquer alteração estrutural de título ou paginação, reconstruir os artefatos e revisar os nomes em disco. O teste mais simples e mais útil é verificar se a pasta de saída contém apenas os basenames esperados.
- Em eficiência de software, evitar absolutos. Operações booleanas, bits e aritmética podem ajudar em certos contextos, mas legibilidade, algoritmo, dados, linguagem, compilador, hardware e medição real determinam a qualidade da otimização.

## 2026-06-04 - Aprendizado reutilizável: nutrição como autocuidado sem prescrição

- Em livros sobre nutrição, preservar metáforas fortes como `alimentação é algoritmo do corpo`, mas qualificar que o organismo humano não responde como máquina simples e que dieta individual depende de contexto.
- Separar princípios gerais de prescrição: variedade, hidratação, moderação, alimentos minimamente processados e limitação de ultraprocessados são orientações amplas; suplementos, jejum e dietas terapêuticas exigem avaliação profissional.
- Não afirmar que nutrição cura doenças psiquiátricas, neurodegenerativas, obesidade, diabetes ou insônia. Formular como influência, apoio, prevenção ou parte de cuidado integrado.
- Sinais como urina, fezes, gases, azia e desconforto podem orientar atenção, mas não devem ser tratados como diagnóstico isolado.
- Em obesidade, evitar culpa simplista e negação de balanço energético. Tratar como fenômeno multifatorial: alimentação, gasto físico, sono, medicamentos, genética, ambiente, renda, saúde mental, hormônios e acompanhamento clínico.

## 2026-06-04 - Aprendizado reutilizável: pedagogia sensível sem determinismo

- Em livros sobre pedagogia, infância, família e escola, preservar teses sobre caráter, estudo, rotina, saúde e responsabilidade, mas evitar atribuir dificuldades infantis a uma causa única.
- Hiperatividade, tristeza, isolamento, baixa autoestima e baixo rendimento escolar devem ser tratados como sinais que pedem investigação de contexto, não como culpa automática da criança ou dos pais.
- Críticas à parentalidade irresponsável ficam mais publicáveis quando formuladas como preparo, apoio, maturidade e responsabilidade, não como proposta de controle estatal discriminatório sobre quem pode ter filhos.
- Tecnologia educacional deve ser avaliada por finalidade, mediação, idade, tempo de uso e qualidade do conteúdo. Nem toda tela é ruim; nem todo jogo educativo ensina bem.
- Não tratar brincadeira, fantasia ou histórias infantis como desperdício por si mesmas. Brincadeira pode desenvolver linguagem, corpo, imaginação, cooperação e pensamento simbólico quando mediada com qualidade.

## 2026-06-04 - Aprendizado reutilizável: aumentar volume literário com cenas funcionais

- Quando uma reescrita literária fica menor que o original, priorizar cenas que façam dupla função: avançar enredo, revelar personagem, reforçar tema e esclarecer consequência institucional.
- Evitar preencher páginas com explicação abstrata. Preferir dramatizar investigação, sobrevivência, bastidores decisórios, dilemas jurídicos, rotina social, conflitos de equipe e consequências pós-clímax.
- Para ficção científica com instituições fortes, cenas de cadeia de custódia, auditoria, autorização judicial, privacidade, perícia e controle externo aumentam plausibilidade sem quebrar ritmo.
- Para romances e amizades, aumentar volume por microações progressivas: humor moderado, cuidado, escolhas livres, pequenos gestos, respeito, hesitação, pedido claro e mudança gradual de confiança.
- Em histórias com punição severa, a persuasão melhora quando a narrativa mostra prova, defesa, revisão, proporcionalidade, vítimas e risco social, em vez de apenas declarar a pena.

## 2026-06-04 - Aprendizado reutilizável: protagonista com vida comum

- Para um protagonista parecer publicável e humano, equilibrar cenas de crise com cenas de rotina: família, trabalho, estudo, descanso, obrigações pequenas e conversas sem ameaça imediata.
- Cenas com pais e avós ajudam a mostrar origem moral, limites, humor doméstico e heranças emocionais sem depender de narração explicativa.
- Cenas acadêmicas ou profissionais devem mostrar tarefa concreta: revisar texto, corrigir planilha, apresentar projeto, receber crítica, cumprir prazo, lidar com superior ou ajudar colega.
- Boas cenas de rotina não são filler quando revelam como o personagem decide antes da crise, como aceita crítica e como amadurece em ambientes normais.

## 2026-06-04 - Aprendizado reutilizável: capítulos finais com respiro editorial

- Em manuscritos que acumulam clímax, julgamento, consequências, romance, cenas familiares e gancho de continuação em um único capítulo final, dividir em capítulos menores melhora ritmo e orientação do leitor.
- Uma sequência final mais publicável costuma separar: retorno/resgate, justiça/reparação, vida comum pós-crise, resolução afetiva e gancho de continuação.
- Quando há filosofia ou ética no desfecho, cortar repetições e manter uma cena concreta por tese evita que o final pareça palestra.
## 2026-06-04 - Aprendizado reutilizável: IA como ferramenta sem idolatria tecnológica

- Em livros sobre inteligência artificial, separar três camadas: técnica demonstrada, analogia neurobiológica e especulação filosófica sobre consciência, IA geral ou sentimentos artificiais.
- Preservar a tese de que IA deve servir a sociedade por produtos, serviços, conhecimento e trabalho responsável, mas evitar promessas de substituição humana total ou de consciência artificial demonstrada.
- Em saúde, educação, justiça, crédito e trabalho, tratar IA como apoio supervisionado, não como autoridade final. Diagnóstico, decisão clínica, avaliação moral e responsabilidade jurídica continuam humanos.
- Evitar comparações estigmatizantes com autismo, TDAH ou neurodivergência. Quando o autor quiser falar de modelos especializados, usar termos como especialização funcional, foco restrito, arquitetura de tarefa específica ou limitação de domínio.
- Em governança de IA, usar referências institucionais como NIST AI RMF, OECD AI Principles, UNESCO Ethics of AI e AI Act europeu para sustentar risco, transparência, supervisão humana e responsabilização.
## 2026-06-04 - Aprendizado reutilizável: hipóteses algorítmicas precisam de estágio de maturidade

- Em livros técnicos com propostas autorais de estruturas de dados, compressão, IA ou algoritmos, preservar a intuição original, mas classificar o estágio: metáfora, hipótese, especificação, protótipo, algoritmo validado ou produto.
- Não apresentar pseudocódigo corrompido, multilíngue ou incompleto como implementação executável. Converter em intenção arquitetural, lista de requisitos ou plano de implementação.
- Promessas de compressão, desempenho ou inteligência precisam ser condicionadas a prova, teste, complexidade, uso de memória, taxa de erro, reversibilidade e comparação com métodos existentes.
- Quando o próprio manuscrito reconhece limitação técnica, preservar essa autocrítica: ela aumenta credibilidade e evita vender hipótese como solução comprovada.
- Estruturas de dados autorais ficam mais publicáveis quando são ligadas a conceitos reconhecíveis: árvore, grafo, trie, tabela hash, busca binária, codificação diferencial, prefixo, índice, nó, terminal, aresta e invariantes.
## 2026-06-04 - Aprendizado reutilizável: timidez, introversão e saúde mental sem estigma

- Em textos sobre timidez e interação social, separar introversão, timidez, ansiedade social e transtornos clínicos. Introversão não é doença; timidez não é falta de caráter; ansiedade social intensa pode exigir avaliação profissional.
- Preservar teses sobre prática social, amor, empatia, autoestima, limites e maturidade, mas evitar dizer que pessoas tímidas são incapazes de namorar, casar, trabalhar ou formar família por definição.
- Autismo, TDAH, depressão, ansiedade, trauma e psicopatia não devem ser usados como explicações genéricas para timidez. Quando aparecerem, tratar como condições distintas que pedem linguagem cuidadosa e, se houver sofrimento, avaliação profissional.
- Conselhos sobre confiança devem ser formulados como prudência relacional: confiança gradual, observação de caráter, limites claros e afastamento de abuso, sem transformar todo desconhecido em ameaça.
- Em comunicação social, um caminho publicável é: aceitar a personalidade, praticar gradualmente, começar por temas comuns, respeitar níveis de intimidade, afirmar limites e buscar vínculos com pessoas maduras.
## 2026-06-04 - Aprendizado reutilizável: lógica formal e metáfora neurocognitiva

- Em livros sobre raciocínio lógico que misturam lógica formal, neurociência, psicologia e comportamento, separar os níveis: validade formal, evidência empírica, hipótese neurocognitiva e aplicação ética.
- Preservar a tese de que raciocinar é organizar premissas em direção a sentido, mas corrigir termos formais quando necessário: equivalência não é mera semelhança; implicação não é causalidade; dedução não é conjectura provável.
- Leitura de comportamento, microexpressões e tom de voz deve ser tratada como indício falível, nunca como prova automática de mentira, intenção ou caráter.
- Em investigação, o mais rigoroso é suspender juízo e comparar premissas com evidências, não presumir que toda afirmação de suspeitos, testemunhas ou advogados é falsa.
- Fórmulas autorais e teoremas práticos devem vir com condições de validade explícitas; se a ordem, custo, risco ou dependência mudam, a conclusão pode deixar de valer.

## 2026-06-04 - Aprendizado reutilizável: fórmulas matemáticas autorais como protótipos

- Em livros com fórmulas autorais, separar identidade matemática conhecida, definição operacional, conjectura, heurística, exemplo didático, protótipo e prova.
- Toda fórmula publicável precisa declarar domínio, contradomínio, parâmetros, limites de validade e comportamento nos casos extremos, especialmente quando usa divisão inteira, módulo, logaritmo, arredondamento ou constantes pequenas.
- Fórmulas que simulam condicionais por valor absoluto ou seletores devem mencionar descontinuidade, precisão numérica, custo computacional, divisão por zero e comparação com funções indicadoras, funções de etapa e métodos tradicionais.
- Contagem de uns em binário deve dialogar com conceitos conhecidos como peso de Hamming, popcount, representação binária e coeficientes binomiais; reconhecer a tradição fortalece a contribuição autoral.
- Exemplos numéricos não equivalem a prova geral. Para evoluir protótipos técnicos, usar tabela de testes, comparação com algoritmo conhecido, análise de complexidade e, quando possível, demonstração formal.

## 2026-06-04 - Aprendizado reutilizável: revisão de livros matemáticos heterogêneos

- Quando um manuscrito matemático reúne notas de estudo, fórmulas práticas, conjecturas, grafos, constantes e computação, organizar por função intelectual: proporção, prova, representação, modelagem, estrutura discreta e limite computacional.
- Corrigir explicitamente afirmações técnicas que afetem credibilidade: grau máximo + 1 em coloração é cota superior, não número cromático exato; critérios simples de Hamiltonianidade raramente são suficientes; normalidade de pi não está provada; Binet exige denominador sqrt(5).
- Fórmulas práticas de geometria, rolos, bobinas e recipientes precisam de unidades, hipóteses físicas, distinção entre exato e aproximado e aviso contra regra de três quando o volume não cresce linearmente com a altura.
- Para DOCX/PDF de consumo, fórmulas essenciais devem ter versão textual linear junto da notação, pois conversões podem degradar sobrescritos, frações e símbolos matemáticos na extração textual.

## 2026-06-04 - Aprendizado reutilizável: neuropsiquiatria sem determinismo ou estigma

- Em manuscritos sobre saúde mental, separar ciência estabelecida, hipótese autoral, metáfora computacional, doutrina moral/religiosa e orientação prática de autocuidado.
- Estilo de vida, sono, alimentação, atividade física, vínculos e espiritualidade podem ser fatores de proteção, mas não devem ser apresentados como causa única, prevenção absoluta ou cura garantida de TEA, TDAH, esquizofrenia, depressão, demência ou Alzheimer.
- Evitar linguagem estigmatizante como `louco`, `insano`, `normal/anormal` como julgamento de valor. Preferir sofrimento psíquico, condição clínica, neurodivergência, sintomas, necessidade de suporte e funcionamento típico/atípico quando necessário.
- Neurotransmissores isolados não explicam diagnósticos psiquiátricos. Serotonina, dopamina, glutamato, GABA e cortisol devem aparecer como partes de sistemas complexos, não como chaves únicas de doença ou cura.
- Dietas, suplementos, remédios naturais e práticas religiosas devem ser descritos como apoio possível e individualizado, nunca como substituto de psicoterapia, psiquiatria, neurologia, medicação indicada, cuidado social ou atendimento de crise.

## 2026-06-04 - Aprendizado reutilizável: neurociência autoral e metáforas computacionais

- Em livros de neurociência que usam IA, circuitos, hardware/software, hash, FPGA, portas lógicas ou redes artificiais, preservar a metáfora quando ela ajuda a explicar associação, memória e atenção, mas declarar que o cérebro não funciona literalmente como computador digital comum.
- Evitar equivalências diretas como `sinapse = memória`, `consciência = software` ou `pensamento = leitura neural` como fato. Formular como modelo interpretativo autoral ou hipótese filosófico-neurocognitiva.
- Memória deve ser tratada como processo distribuído de redes, plasticidade e reativação, não como arquivo isolado. Esquecimento pode ser normal, adaptativo ou clínico, dependendo de frequência, progressão, prejuízo e contexto.
- Ao relacionar neurociência e IA, usar a ponte como inspiração de pesquisa: atenção, integração sensorial, memória episódica/semântica, generalização e economia de energia. Não prometer AGI humana apenas por copiar conceitos neurobiológicos.
## 2026-06-04 - Aprendizado reutilizável: física especulativa, grafos e publicação responsável

- Em livros de física autoral com cosmologia especulativa, separar explicitamente física estabelecida, analogia didática, hipótese filosófica, modelo matemático, previsão testável e ficção tecnológica. Essa separação preserva ousadia intelectual sem publicar erro como fato.
- Modelos por grafos são fortes como representação de relações entre partes, conexões, níveis e sistemas, mas não substituem física clássica, relatividade ou mecânica quântica sem equações próprias, domínio definido e previsões observáveis.
- Corrigir pontos físicos básicos antes de exportar: energia potencial gravitacional aumenta com altura em `U=mgh`, mas o peso próximo à superfície da Terra permanece aproximadamente `P=mg`; órbitas planetárias são principalmente gravitacionais, não eletromagnéticas; interferência de ondas não transforma Wi-Fi em radiação ionizante; flutuação depende de empuxo e densidade média do objeto em relação ao fluido deslocado.
- Buracos negros não devem ser tratados como fogo apagável por química. Se o texto especula sobre intervenção, registrar como ficção teórica ou hipótese remota e recolocar a discussão em massa, carga, momento angular, horizonte de eventos, acreção e limites causais.
- Teletransporte quântico não equivale a teletransporte humano nem telecinese macroscópica. A melhor solução editorial é preservar a intuição como manipulação informacional da matéria, mas declarar o limite físico e tecnológico.

## 2026-06-05 - Aprendizado reutilizável: unificação física por escala, não por declaração

- Em manuscritos que tentam unificar gravidade, eletromagnetismo, grafos e complexidade, evitar verbos de conclusão forte como `demonstrar`, `estabelecer` ou `redefinir` quando o texto apresenta hipótese autoral. Preferir `propõe`, `sugere`, `investiga`, `interpreta` e `funciona como programa de pesquisa`.
- A formulação mais publicável não é `o eletromagnetismo causa a gravidade`, mas: o eletromagnetismo participa da organização microestrutural da matéria; matéria organizada contribui para energia, pressão e tensões; e esses elementos entram no tensor energia-momento que se relaciona à geometria na relatividade geral.
- Em teses sobre gravidade emergente, declarar o que falta para virar teoria física: variáveis mensuráveis, equações próprias, domínio de validade, previsões novas e comparação com relatividade geral e cosmologia observacional.
- O conceito de `geometria divergente` pode ser preservado como categoria interpretativa para expansão, pressão negativa ou dinâmica cosmológica, mas não deve ser apresentado como substituto comprovado da energia escura ou da constante cosmológica.
- Campo magnético planetário, efeito dínamo e limite de Curie ajudam a corrigir reducionismos: campo magnético terrestre não explica rotação ou translação; escalas planetárias exigem gravitação, conservação do momento angular e dinâmica interna, não analogia direta com ímãs comuns.

## 2026-06-05 - Aprendizado reutilizável: saúde comportamental sem culpa moral

- Em livros sobre decisões pessoais e saúde, preservar a tese de responsabilidade preventiva, mas separar escolha, vulnerabilidade, doença, acesso a cuidado e determinantes sociais. Adoecimento não deve ser tratado como prova de ignorância, hipocrisia, pecado, fraqueza moral ou falta de caráter.
- Estilo de vida deve aparecer como fator de proteção, redução de risco e apoio ao tratamento, não como causa única nem cura garantida de depressão, ansiedade, TEA, TDAH, esquizofrenia, Alzheimer, demências ou transtornos de personalidade.
- Em crianças e adolescentes, recomendações sobre telas devem considerar sono, atividade física, conteúdo, horário, vínculo familiar e substituição de atividades essenciais. Limite rígido sem contexto pode empobrecer a orientação.
- Fórmulas ou métricas autorais de `sanidade`, `precisão mental` ou `imprecisão lógica` devem ser apresentadas como metáforas ou protótipos de reflexão, não como instrumentos diagnósticos.
- Em saúde mental, linguagem de publicação deve trocar `loucura`, `insanidade`, `mente quebrada`, `normal/anormal` e categorias morais por sofrimento psíquico, funcionamento, sintomas, vulnerabilidade, suporte, avaliação profissional e tratamento.

## 2026-06-05 - Aprendizado reutilizável: suicídio e crise em textos autorais

- Quando um manuscrito menciona suicídio, autoagressão ou crise psíquica, incluir nota de segurança com orientação de emergência e canais atuais de apoio conforme o público-alvo. Para Brasil, CVV 188; para Estados Unidos, 988.
- Não reduzir suicídio a estilo de vida, falta de fé, falta de maturidade, tristeza simples ou decisão isolada. Usar linguagem multifatorial: depressão, trauma, isolamento, substâncias, dor, perdas, acesso a meios letais, desesperança, violência, discriminação, falta de cuidado e fatores sociais.
- Evitar descrições gráficas, romantização ou causalidade simplista. A redação deve enfatizar sinais de alerta, presença, escuta, redução de risco imediato e busca de ajuda qualificada.
- Em livros de saúde mental, autocuidado deve ser apresentado como fator de proteção e complemento; crise suicida exige suporte urgente, não apenas meditação, dieta, sono ou força de vontade.
- Ao revisar textos longos com hipóteses neuropsiquiátricas, preservar metáforas úteis como `economia da energia mental` e `imprecisão lógica`, mas impedir que virem diagnóstico, escala clínica ou culpa moral.

## 2026-06-05 - Aprendizado reutilizável: teologia moral sem desumanização

- Em manuscritos cristãos com forte doutrina de juízo, pecado e salvação, preservar a convicção bíblica do autor, mas evitar linguagem que transforme pessoas em pragas, câncer, objetos descartáveis ou inimigos ontológicos. Juízo divino pode ser afirmado sem autorizar desprezo humano.
- A relação entre fé e obras deve ser formulada com equilíbrio: obras não compram salvação; obras revelam a direção da fé, a transformação do caráter e a obediência amorosa.
- Quando o autor usa lógica, matemática ou computação para falar de Deus, manter como analogia filosófica, não como prova formal exaustiva do ser divino.
- Críticas a mídia, redes sociais e amizades funcionam melhor como discernimento pelos frutos: se edifica amor, verdade, sobriedade e justiça, aproxima do bem; se normaliza crueldade, mentira, impureza ou desprezo, exige cautela.
- Em textos religiosos, remover especulações políticas ou sanitárias que desviem da tese central, a menos que sejam comprovadas e indispensáveis. A força editorial deve permanecer na teologia, no caráter e na prática cristã.

## 2026-06-05 - Aprendizado reutilizável: desejo, aparência e consentimento em ficção especulativa

- Em romances de ficção científica com rejuvenescimento, imortalidade ou aparência corporal modificada, separar aparência, idade cronológica, história pessoal, estado civil, vínculos familiares e autonomia.
- Cenas de atração podem ser tensas e dramáticas sem transformar personagens em caricaturas: mostrar impulso, erro, vergonha e aprendizado é mais forte do que narrar apenas condenação moral externa.
- Presentes, elogios, portfólios, roupas, beleza e simpatia não devem funcionar como autorização automática para intimidade. Quando o tema é limite corporal, deixar a regra clara dentro da ação e do diálogo.
- Para preservar maturidade narrativa, personagens respeitosos não forçam escolhas; oferecem caminhos, aceitam recusas e aprendem a distinguir desejo pessoal de cuidado real pelo outro.
- Em mundos tecnologicamente avançados, a tese ética continua simples: ciência pode preservar vida e juventude, mas dignidade depende de consentimento, consciência e limites.

## 2026-06-05 - Aprendizado reutilizável: cenas empresariais com IA preditiva

- Em ficção tecnológica, reuniões empresariais ficam mais fortes quando números, risco e governança entram em conflito dramático, não apenas em exposição.
- Empresas de IA preditiva devem ser apresentadas com promessa e perigo: antecipar demanda, reduzir erro e salvar recursos, mas também manipular comportamento, explorar vulnerabilidades e concentrar poder informacional.
- Para evitar palestra disfarçada, transformar teses éticas em perguntas de negociação, condições contratuais, auditorias, limites de acesso, métricas e decisões com custo profissional para o personagem.
- Um protagonista jovem pode parecer maduro sem parecer arrogante quando admite incerteza, defende dados verificáveis, recusa mentir para agradar superiores e aceita consequências.
- Parcerias com tecnologias poderosas devem exigir finalidade, escopo, retenção de dados, responsabilidade humana e revisão independente; isso cria verossimilhança e reforça o tema moral sem quebrar a narrativa.

## 2026-06-05 - Aprendizado reutilizável: prova, cadeia de custódia e investigação em thriller

- Em tramas investigativas, uma prova precisa ter origem, meio de captura, tentativa de preservação, falha plausível e consequência narrativa; arquivos corrompidos devem ter causa dramática, não apenas conveniência.
- Personagens que agem fora do procedimento legal podem continuar interessantes se o texto reconhecer o risco jurídico, moral e profissional da escolha.
- Ferramentas de leitura mental, polígrafo avançado ou IA forense devem ser tratadas como indício técnico falível, não como verdade absoluta; a cadeia de custódia preserva credibilidade.
- Testemunhas secundárias devem aparecer no evento que denunciam, mesmo que por cena curta, para evitar sensação de prova surgida do nada.
- Em thriller tecnológico, tensão aumenta quando criminosos tentam destruir provas, mas fragmentos sobrevivem com limitações que exigem reconstrução, perícia e validação jurídica.

## 2026-06-05 - Aprendizado reutilizável: diagramação ABNT/piloto com Pandoc

- `--reference-doc` no Pandoc ajuda estilos de DOCX, mas não garante sozinho capa, páginas pré-textuais, sumário paginado, cabeçalho, rodapé, paginação reiniciada e fluxo de livro publicável.
- Quando houver piloto em PDF/TeX, preferir criar template LaTeX explícito e reexecutável para a etapa final de publicação, preservando DOCX/PDF preliminares em pasta separada.
- Sumário manual em markdown deve ser removido antes da geração final; o sumário de publicação precisa ser gerado automaticamente pelo motor de diagramação, com paginação real.
- Para livros A5 no padrão usado por Josué, uma estrutura robusta é: capa, página em branco, sumário, página em branco, miolo com `mainmatter`, página reiniciada e cabeçalho central.
- Em livros técnicos, habilitar matemática Pandoc/LaTeX e prever Unicode comum, como superscritos, antes do lote; validar primeiro uma amostra e só depois processar todos os livros.
- Em DOCX, o sumário deve ser campo `TOC`, não texto fixo; depois da geração, avisar que Word/LibreOffice pode exigir atualização de campos para recalcular paginação conforme o editor local.
- Em PDFs A5 feitos com LaTeX `book`, o espaçamento padrão de `\chapter` tende a ser grande demais; usar `titlesec` ou controle equivalente para reduzir margem superior/inferior dos títulos antes de considerar o arquivo diagramado.

## 2026-06-05 - Aprendizado reutilizável: reescrita abrangente não é síntese

- Quando o usuário pedir reescrita editorial de livros, não assumir que uma síntese curta cumpre a tarefa. Reescrita profissional deve preservar cobertura ampla do original, melhorando clareza, gramática, estrutura, progressão didática e bibliografia.
- Para evitar perda de conteúdo, criar mapa de cobertura antes de reescrever: cada bloco relevante do original deve ter destino editorial explícito.
- Só cortar repetição real, erro grave, tradução corrompida, ruído irrecuperável ou material fora do escopo; teses, valores, exemplos e argumentos autorais precisam ser preservados e explicados melhor.
- Antes de diagramar, validar cobertura entre original, mapa e versão reescrita. PDF bonito não compensa amputação de conteúdo.

## 2026-06-06 - Aprendizado reutilizável: continuidade entre volumes de ficção

- Em continuações, personagens, instituições e tecnologias plantados no volume anterior precisam aparecer, ser mencionados ou ter ausência explicada quando seriam naturalmente relevantes.
- Protagonista de uma continuação não deve apagar autoridades técnicas já estabelecidas; a maturidade dele pode ser mostrada justamente por ouvir especialistas mais velhos, aceitar correções e aprender a atuar dentro de hierarquias coerentes.
- Ao conectar livros, reforçar continuidade em três níveis: referência breve no início, consequência institucional no meio e presença discreta no fechamento. Isso evita enxerto artificial e cria sensação de mundo vivo.
- Listas de personagens devem ser reconciliadas entre volumes quando alguém passa a ter função importante no universo narrativo, especialmente em sagas com empresas, famílias e equipes científicas.
- Quando o primeiro volume já está mais consolidado, ele deve ter prioridade sobre a continuação em sobrenomes, família, termos centrais e regras do mundo. A continuação deve se ajustar ao cânone do volume anterior; no primeiro volume, plantar apenas sementes leves que melhorem sua própria coerência e facilitem o futuro, sem sobrecarregá-lo com elenco ou trama do livro seguinte.

## 2026-06-07 - Diretriz reutilizável: histórico, memória e dúvidas operacionais

- Em projetos com histórico local, atualizar `history-chat.md` no início e no fim de cada sessão relevante, registrando objetivo, decisões, ações executadas, pendências, commits e cuidados importantes.
- Atualizar também `/home/josue/Documents/josue-writter-workspace/global-history-chat.md` sempre que surgir um aprendizado reutilizável para outros livros, outros projetos, outras inteligências artificiais ou outros fluxos editoriais.
- Evitar processos, threads e comandos que possam ultrapassar os limites de execução da memória principal. Em tarefas grandes, preferir lotes menores, leitura incremental, commits frequentes e validação por partes.
- Processos ou threads que consumam muita memória e façam a memória principal ultrapassar 95% de uso devem ser interrompidos para evitar travamentos, perda de execução e comprometimento do trabalho das inteligências artificiais.
- Sempre fazer perguntas quando houver dúvida real que possa mudar o resultado, gerar risco, causar perda de conteúdo, afetar autoria, alterar arquivos importantes ou exigir uma decisão do usuário.

## 2026-06-07 - Aprendizado reutilizável: fallback DOCX para PDF quando LaTeX falha

- Em conversões Markdown -> PDF com Pandoc, `lualatex` pode falhar em ambientes com fontes LaTeX ausentes, por exemplo erro envolvendo `lmroman10-regular`.
- Um fallback prático é gerar primeiro os DOCX com Pandoc e depois converter DOCX -> PDF com LibreOffice headless, usando um perfil temporário (`-env:UserInstallation=file:///tmp/...`) para evitar conflitos com sessões abertas.
- Para lotes grandes, converter sequencialmente, registrar log por arquivo e validar no fim: `unzip -t` para DOCX, `pdfinfo` para PDF e contagem esperada de arquivos por formato.

## 2026-06-07 - Aprendizado reutilizável: estrutura ABNT em DOCX/PDF gerados

- Um DOCX/PDF com margens, fonte e espaçamento ABNT ainda pode estar incompleto como livro ou relatório se faltar estrutura editorial: folha de rosto, página em branco, sumário isolado, página em branco antes do miolo, cabeçalho e numeração.
- Para Pandoc -> DOCX, uma solução robusta é combinar `reference-doc` para estilos com pós-processamento OpenXML para inserir quebras de página, cabeçalho, rodapé e campo `PAGE`.
- Em versões antigas do Pandoc, `--toc-title` pode não existir e `toc-title` por metadado pode causar instabilidade em arquivos grandes. Alternativa estável: gerar o TOC normalmente e trocar o texto visível `Table of Contents` por `Sumário` no XML do DOCX.
- Ao validar, conferir não só integridade (`unzip -t`, `pdfinfo`), mas também presença de quebras de página, `headerReference`, `footerReference`, campo `PAGE`, tamanho A4 e título visível do sumário.
- Quando o campo automático de sumário não aparece de forma confiável no PDF convertido por LibreOffice, uma alternativa pragmática é materializar um sumário manual no Markdown temporário antes do miolo. Para ficar legível no DOCX/PDF, cada entrada precisa ser parágrafo separado e numeração inicial como `1.` deve ser escapada no Markdown (`1\.`), senão pode ser interpretada como lista.
- Para paginação ABNT em DOCX sem LaTeX, é possível pós-processar OpenXML criando duas seções: pré-textual com `w:pgNumType w:fmt="roman"` e miolo com `w:pgNumType w:fmt="decimal"`, ambos com `w:start="1"`, e rodapés separados alinhados à direita.
- Em organização de ideias, títulos de subcapítulos não devem simplesmente copiar o começo do parágrafo. Preferir títulos semânticos que expressem domínio, intenção e escopo do bloco, mesmo que sejam mais genéricos, por exemplo `Saúde mental e orientação pessoal`, `Agenda inteligente de rotinas e tarefas` ou `Segurança pública, defesa e tecnologias sensíveis`.
- Em documentos com muitos requisitos numerados, sumários manuais ficam mais utilizáveis quando incluem apenas capítulos de primeiro nível; requisitos/subcapítulos devem permanecer no corpo, mas não necessariamente no sumário.
- Em lotes Pandoc longos, `segmentation fault` pode ocorrer de modo transitório mesmo sem pressão crítica de memória. Para geração automatizada, registrar o erro e retentar o arquivo uma vez pode concluir o lote sem intervenção manual.

## 2026-06-07 - Diretriz de marca: Vita Ethos

- Nos documentos de empreendedorismo de Josué, a marca empresarial principal de healthtech/ecossistema vital passou a ser `Vita Ethos`.
- Em revisões futuras, preferir `Vita Ethos` como marca-mãe para a família de softwares e aplicativos voltados a vida, ética, saúde, educação, organização pessoal e preservação humana.
- Evitar reintroduzir nomes empresariais antigos ligados a `HealthTech`, `Health Care` ou `Healthcare`, exceto quando o contexto exigir histórico explícito de renomeação.

## 2026-06-17 - Diretriz reutilizável: não remendar apresentações com redaction sem revisão visual

- Em PDFs de apresentação, imagens, slides, capas e materiais visuais, não usar redaction/texto sobreposto como método padrão para trocar marca ou corrigir texto. Esse método pode criar caixas brancas, tapar arte, ocultar informações e piorar o design.
- Priorizar sempre a fonte editável (`.pptx`, `.docx`, `.xcf`, `.svg`, `.odg`, etc.) ou uma versão limpa/original para regenerar o PDF/imagem.
- Quando uma edição direta em PDF/imagem for inevitável, renderizar páginas/amostras com `pdftoppm` ou ferramenta equivalente e revisar visualmente antes de considerar a tarefa concluída.
- Se houver uma pasta original/atualizada paralela, comparar e restaurar a partir dela em vez de tentar cobrir texto antigo com caixas de redaction.

## 2026-06-20 - Diretriz reutilizável: restauração visual deve abranger derivados e fontes editáveis

- Ao corrigir uma substituição de marca defeituosa, auditar todos os derivados relacionados: PNG/JPEG exportados, XCF ou outra fonte editável, variantes horizontal/quadrada, imagens arquivadas e artes incorporadas a formulários.
- Não considerar a restauração concluída apenas porque a imagem mais evidente foi corrigida; usar datas de modificação, nomes correlatos, dimensões, comparação visual e hashes para localizar o lote inteiro alterado na mesma operação.
- Quando houver backup confiável, restaurar por correspondência explícita e validar com SHA-256. Artefatos gerados sem correspondente original devem ser removidos ou isolados, pois podem reintroduzir a versão defeituosa em exportações futuras.
- Em disco próximo da capacidade, inspecionar o tamanho descompactado e extrair somente a subpasta necessária. Não expandir automaticamente um backup completo de vários gigabytes.

## 2026-06-21 - Diretriz reutilizável: reduzir Google Forms preservando endereço e respostas

- Para reduzir ou reformular um Google Forms sem mudar seus endereços, usar `FormApp.openById` no formulário existente; `FormApp.create` gera outro formulário e outros URLs.
- Antes de remover itens de um formulário que pode conter respostas, exportar as respostas para uma planilha de backup. A criação do backup deve ocorrer antes de qualquer chamada a `deleteItem`.
- Em formulários com consentimento, configurar navegação para que a recusa leve diretamente ao envio e para que a rota aceita não atravesse acidentalmente uma página de rejeição localizada no fim do formulário.
- Validar scripts geradores contando títulos numerados, verificando ausência de `FormApp.create`, revisando a ordem backup/remoção e executando uma checagem sintática local antes de aplicar a alteração na conta Google.

## 2026-06-21 - Diretriz reutilizável: questionários de validação para investidores

- Um questionário usado em captação não deve apenas confirmar que o público deseja saúde, organização ou bem-estar. Deve medir comportamento: frequência recente da dor, consequências, alternativas já tentadas, gasto realizado, insuficiência das soluções atuais e compromisso concreto com teste, pagamento ou piloto.
- Apresentar o problema e colher experiências antes de descrever a startup reduz viés de confirmação. Separar explicitamente a seção de experiência atual da seção de avaliação do conceito.
- Alinhar segmentos, módulos e faixas de preço ao plano executivo vigente. Perguntas filosóficas podem explicar a marca, mas não substituem evidência de problema monetizável.
- Resultados de survey são evidência de descoberta e intenção. Não os apresentar como equivalentes a usuários ativos, pagamentos, retenção, cartas de intenção ou contratos.
- Em Google Forms, `PageBreakItem.setGoToPage` configura a navegação da página anterior à quebra, não da página iniciada por ela. Revisar o fluxo completo ao combinar consentimento, saltos condicionais e envio.

## 2026-06-21 - Diretriz reutilizável: remover itens de Google Forms com navegação condicional

- Não apagar diretamente, em ordem reversa, um formulário que contém perguntas ou páginas com saltos condicionais. O Forms pode retornar `Invalid data updating form` quando uma página ainda está referenciada.
- Antes da exclusão, converter escolhas de múltipla escolha com navegação em escolhas comuns e redefinir quebras de página para `PageNavigationType.CONTINUE`.
- Remover em duas fases: primeiro perguntas e itens regulares; depois quebras de página. Pequenas esperas e tentativas limitadas ajudam com a consistência eventual da API.
- Registrar o URL do backup imediatamente após criá-lo, e não apenas no fim do script, para que uma falha posterior não esconda a localização dos dados preservados.

## 2026-06-07 - Aprendizado reutilizável: contenção rígida de processos pesados no Linux

- Trabalhos editoriais com IA, tradução, Pandoc, LibreOffice, LaTeX, extração de DOCX e reescrita em lote podem criar pressão severa de memória, processos e threads. Se houver vazamento de memória ou criação rápida de threads, o Linux pode entrar em `thrashing`: o sistema fica ocupado paginando entre RAM e disco, o mouse e teclado travam, e até comandos de emergência podem não receber tempo de CPU.
- A interpretação operacional é que não basta tentar matar processos pesados depois que eles já fugiram do controle. A defesa correta deve ser preventiva: iniciar rotinas pesadas dentro de limites rígidos que o processo não consiga ultrapassar.
- Antes de rodar qualquer lote grande, preferir `systemd-run --user --scope` com cgroup temporário e limites explícitos de RAM/CPU. Exemplo base: `systemd-run --user --scope -p MemoryMax=4G -p CPUQuota=200% python script.py`. Se o processo tentar passar do limite de memória, o kernel deve encerrar apenas aquele escopo, preservando o restante do sistema.
- Para tarefas de publicação, tradução e conversão, adotar como padrão: rodar em lotes pequenos, sequenciais, retomáveis e com cache; evitar paralelismo amplo; limitar CPU/RAM; registrar PID/log; validar ao fim de cada bloco; e verificar que não sobraram processos `pandoc`, `pdflatex`, `libreoffice`, `soffice` ou scripts Python pesados.
- Configurar `earlyoom` de forma mais agressiva pode reduzir travamentos quando a defesa por cgroup falhar. Exemplo de configuração mencionada pelo usuário: `EARLYOOM_ARGS="-m 10 -s 10 -r 1"`, para agir antes de RAM e swap esgotarem. Essa configuração deve ser aplicada com consciência do ambiente, porque pode encerrar processos grandes legitimamente em vez de esperar o sistema congelar.
- Manter o recurso de emergência do kernel como última linha de defesa: `Alt + SysRq + f` invoca o OOM Killer para matar o processo mais pesado quando a interface gráfica está travada. Isso é preferível a desligar pelo botão, pois reduz risco de corrupção de arquivos.
- Em qualquer novo script ou pipeline pesado, incluir uma etapa explícita de segurança antes da execução: estimar volume, definir limite de memória, escolher tamanho de lote, desativar concorrência desnecessária e documentar o comando seguro. Para este ecossistema, `systemd-run` com `MemoryMax` e `CPUQuota` deve ser tratado como solução principal para impedir novos travamentos.

## 2026-07-05 - Diretriz reutilizável: QR Code promocional em livros

- Quando o autor quiser divulgar uma página de venda, catálogo ou bio editorial dentro de livros, inserir o QR Code como material pós-textual, no final do PDF/EPUB, e não como parte do miolo argumentativo ou literário.
- A página do QR Code deve ter função clara de convite à leitura de outras obras, preservando a diagramação principal do livro, o padrão ABNT e a separação entre conteúdo autoral e propaganda editorial.
- Para EPUB, preferir inserir a imagem como recurso interno com texto alternativo e link clicável equivalente. Para PDF impresso, garantir tamanho suficiente para leitura por celular, margens adequadas, contraste alto e URL visível por extenso para o caso de falha na leitura do QR Code.
- Antes de gerar lote final, validar o QR Code em pelo menos um PDF e um EPUB: abrir o arquivo, conferir se a imagem aparece ao final, testar o link e confirmar que o sumário, paginação e metadados não foram corrompidos.

## 2026-07-12 - Diretriz reutilizável: atualizar livros quando só existe PDF final

- Quando a fonte editável de um livro não aparece localmente e só há PDF final exportado de Google Docs ou ferramenta similar, evitar sobrescrever o PDF original ou reconstruir 200+ páginas por extração textual sem autorização explícita.
- Uma alternativa segura é criar uma pasta separada com Markdown da atualização, gerar páginas novas no mesmo tamanho do PDF original e inserir a atualização como seção complementar antes de material promocional final, mantendo o QR Code ou chamada comercial como última página.
- Registrar claramente a limitação: essa estratégia preserva o miolo e a diagramação original, mas não recalcula sumário nem paginação interna. Para publicação final plenamente integrada em ABNT, localizar a fonte editável ou reconstruir o livro inteiro em Markdown/DOCX.
- Validar a cópia derivada com `pdfinfo`, extração textual, checagem da última página e renderização visual de pelo menos uma página nova; em textos em português, conferir acentuação no PDF extraído e visualizado.

## 2026-07-12 - Diretriz reutilizável: reconstrução integral a partir de PDF final

- Quando a fonte editável não existe localmente, uma reconstrução integral pode usar o PDF final como fonte-base, extraindo o texto por intervalos reais de páginas e removendo cabeçalhos, números de página, sumário antigo e legendas de imagens antes de gerar um Markdown mestre.
- Para preservar autoria e evitar síntese curta, marcar claramente o reaproveitamento como `Texto-base reconstruído do livro original` e adicionar camadas editoriais novas: tese central, chaves de leitura por capítulo, sínteses, programa de aplicação e referências.
- Quando uma tese autoral precisa dominar a nova edição, criar um capítulo de eixo conceitual antes dos capítulos originais e repetir, em cada capítulo, uma chave de leitura que conecte o conteúdo-base à tese. Isso reorganiza o livro sem apagar o material do autor.
- Produzir Markdown como fonte canônica e derivar PDF/DOCX/EPUB dele. Validar com contagem de palavras, `pdfinfo`, `pdftotext`, `unzip -t` para DOCX/EPUB e renderização visual de capa e página final.

## 2026-07-12 - Diretriz reutilizável: acabamento editorial leve para PDF A5

- Para uma etapa de acabamento sem depender de LaTeX, é viável renderizar PDF A5 diretamente com PyMuPDF: capa textual, folha de rosto, sumário paginado, cabeçalho, rodapé, numeração e página final com QR Code.
- Quando o mesmo Markdown também gera DOCX/EPUB via Pandoc, tratar o PDF como renderização própria: remover do PDF seções pré-textuais duplicadas que existem no Markdown para os outros formatos, como folha de rosto.
- Sumário paginado em PDF pode ser feito em duas passagens: renderizar o miolo para descobrir páginas dos títulos, renderizar o sumário com os números definitivos e então montar capa, folha de rosto, sumário e miolo.
- Validar acabamento visualmente, não apenas por texto: renderizar capa, primeira página do sumário e última página com QR Code para conferir espaçamento, legibilidade e ausência de sobreposição.

## 2026-07-12 - Diretriz reutilizável: converter versão de revisão em versão de publicação

- Antes de chamar um livro de publicável, remover marcas de bastidor editorial do miolo, como `texto-base`, `chave de leitura`, `síntese editorial`, nomes de ferramentas usadas no processo e avisos técnicos sobre PDF/fonte local. Esses detalhes pertencem ao histórico ou aos scripts, não ao livro vendido.
- Para temas sensíveis, substituir formulações de culpa total, estigma ou desumanização por linguagem de responsabilidade compartilhada, separando comportamento criminoso de condição social e distinguindo tese autoral de afirmação causal absoluta.
- Se o livro preserva trechos originalmente apoiados por IA, remover menções operacionais como `perguntando ao ChatGPT` e reforçar a bibliografia com fontes institucionais ou acadêmicas verificáveis. Não basta trocar o nome da ferramenta; é preciso deixar a fundamentação conferível.
- Em PDFs gerados por renderização própria, validar URLs longas nas referências por imagem renderizada. URLs podem ultrapassar margens se o algoritmo de quebra não dividir tokens longos.

## 2026-07-15 - Aprendizado reutilizável: pacote editorial para UICLAP, capas e arte promocional

- Para este fluxo, a fonte canônica do miolo ficou em Markdown e os derivados foram gerados com Pandoc:
  - EPUB e DOCX por `scripts/build_publicacao.sh`;
  - PDF de prova A5 por `pandoc` + `xelatex`;
  - validação final com `pdfinfo` no PDF e `unzip -t` no DOCX/EPUB quando necessário.
- O PDF de prova A5 passou a usar `publicacao/pdf-prova-a5.tex` com `fontspec` e Lexend local, e o comando de build foi ajustado para `fontsize=12pt` quando o objetivo é a diagramação pedida para a UICLAP.
- O arquivo de fonte da capa precisa ficar separado por função:
  - frente oficial: `publicacao/capa/capa-oficial-v1.png`;
  - base visual sem texto: `publicacao/capa/capa-base-frontal-v1.png`;
  - variante de marketing: `publicacao/capa/capa-digital-v2.png`;
  - contracapa textual: `publicacao/contracapa.md`;
  - post social quadrado: `publicacao/marketing/post-social-v1.png`;
  - capa completa UICLAP: `publicacao/uiclap/A-Maldicao-do-Anel-da-Rainha-UICLAP-A5-v1.jpg`.
- A UICLAP, nos artigos oficiais que foram verificados, não mostrou API pública ou CLI de publicação. O fluxo documentado é portal/upload. As páginas oficiais enfatizam:
  - a capa é um JPG de até 50 MB;
  - a capa depende do miolo;
  - a estrutura impressa pode incluir capa, contracapa, lombada e orelhas;
  - a lombada só existe a partir de 60 páginas;
  - a sangria recomendada é 5 mm;
  - o código de barras interno da UICLAP fica fixo na contracapa.
- Para A5 na UICLAP, a capa completa precisa ser planejada como um arquivo único de frente + lombada + contracapa, com área reservada para o código de barras interno. O verso não deve ser tratado como arte separada se o objetivo for upload final no portal.
- No caso desta obra, a prova A5 foi primeiro gerada em 503 páginas com fonte menor e depois alinhada ao pedido do usuário para Lexend 12, o que levou a 688 páginas. Com isso, a lombada estimada para upload ficou em cerca de 35,4 mm.
- A capa UICLAP foi montada em JPG com dimensões finais de cerca de 341,40 mm x 220 mm para o estado atual do miolo e da sangria. A forma correta de reproduzir o pacote é partir do PDF A5 atual para recalcular a spine, depois regenerar o JPG.
- A Lexend oficial do Google Fonts foi útil para completar o pacote localmente quando a fonte não estava instalada. O caminho adotado foi copiar `Lexend-Medium.ttf` e `Lexend-Bold.ttf` para `publicacao/fonts/` e usá-los em `fontspec` e na montagem da capa.
- A geração da capa de marketing quadrada funciona melhor quando o fundo é a arte base frontal sem texto, não a capa já textualizada. O post social ficou melhor com:
  - composição quadrada;
  - fundo escurecido;
  - chamada curta;
  - bloco de payoff e assinatura discreta.
- Para a capa impressa UICLAP, o verso deve ser curto e legível. Textos longos demais perdem funcionalidade porque a contracapa impressa precisa competir com lombada, código de barras e área de sangria. A melhor prática aqui foi usar a sinopse curta, uma frase de apoio e uma chamada central forte.
- Em capas e pôsteres, testar visualmente a arte final com `view_image` é mais confiável do que confiar só em dimensões numéricas. A primeira versão da capa UICLAP mostrou problema de verso escuro demais e texto pequeno demais; isso foi corrigido após revisão visual.
- Scripts úteis criados neste fluxo:
  - `scripts/build_marketing_post.sh` para o post social quadrado;
  - `scripts/build_uiclap_cover.sh` para a capa completa da UICLAP;
  - `scripts/build_publicacao.sh` para EPUB/DOCX/HTML e prova A5.
- O número de páginas do PDF A5 afeta diretamente a lombada. Para este projeto, o ajuste foi calculado como `spine = pages / 20 + 1` como aproximação operacional, mas o valor final precisa sempre ser conferido no gabarito do portal da UICLAP antes do upload definitivo.
- Quando um projeto de livro pede uma etapa de publicação impressa, vale manter a separação entre:
  - miolo publicável;
  - prova A5 para leitura;
  - capa impressa UICLAP;
  - peças promocionais menores;
  - histórico local do livro;
  - histórico global reutilizável.
- Para o fluxo de conversão, a ordem prática que funcionou foi:
  1. gerar miolo em PDF A5, DOCX e EPUB;
  2. medir a paginação do PDF de prova;
  3. recalcular a lombada;
  4. gerar a capa completa UICLAP;
  5. validar visualmente a arte;
  6. só então preparar o upload no portal.
- Para novos livros, este pacote pode ser reaproveitado como modelo base se houver A5, contracapa impressa e capa UICLAP similar. Se o miolo mudar de paginação, a primeira ação deve ser regenerar a prova e recalcular a spine antes de mexer na arte final.

## 2026-07-16 - Diretriz reutilizável: romance cristão, saúde, fé e publicação em A5

Aprendizados derivados da produção de `Destinos Guiados por Deus`, aplicáveis a outros livros cristãos, romances edificantes, obras com saúde comportamental e projetos de publicação com IA:

- Antes de escrever ou revisar um livro com base espiritual, filosófica e comportamental, ler primeiro as fontes do autor, o resumo da história, o protótipo, o plano de ação e o histórico local. A IA não deve começar pela própria imaginação quando o autor já forneceu base doutrinária, estilo, valores, decisões e materiais de referência.
- Manter três documentos com funções distintas: o manuscrito como fonte literária, o plano de ação como mapa vivo de intenção editorial e o `history-chat.md` como memória operacional da obra. O `global-history-chat.md` deve receber apenas aprendizados reaproveitáveis por outros livros, evitando excesso de detalhes circunstanciais.
- Registrar abertura e fechamento de sessões relevantes no histórico local e fazer commits por sessão. Isso protege a continuidade quando outra IA ou outro ser humano retoma o projeto, reduz retrabalho e permite rastrear quando uma decisão entrou no livro.
- Em romance cristão, a transformação dos protagonistas precisa ser gradual e causal. Não basta declarar que alguém mudou: o texto deve mostrar o confronto com a Palavra, a resistência, a tentativa de obedecer, a falha, o arrependimento, a correção e a consequência visível no modo de falar, cuidar, trabalhar, comer, descansar, orar e amar.
- O romance deve nascer como fruto da maturidade, não como atalho emocional. Em obras cristãs, amor conjugal publicável combina entrega, serviço, honra, fidelidade, proteção, liberdade, respeito e responsabilidade. Proteção não é controle; provisão não é domínio; auxílio não é apagamento da mulher; submissão cristã não autoriza abuso nem passividade narrativa.
- A mulher amada precisa ter arco próprio. Mesmo quando a história valoriza complementaridade, esposa, maternidade, cuidado e delicadeza, a personagem feminina deve continuar pensando, escolhendo, servindo a Deus, corrigindo o homem quando necessário e amadurecendo por convicção, não apenas por função romântica.
- A Bíblia deve funcionar como eixo vivo de interpretação, não como decoração religiosa. Passagens bíblicas ganham força quando mudam decisões concretas: palavra que edifica, perdão, confissão, temperança, cuidado do corpo, pureza, trabalho, hospitalidade, oração, amor sacrificial e perseverança.
- Evitar transformar capítulos em sermões disfarçados. A doutrina deve aparecer por cena, conflito, gesto, diálogo, silêncio, arrependimento, decisão e consequência. Quando for necessário explicar uma tese, distribuir a explicação em pequenas camadas e aterrissá-la numa ação concreta.
- Símbolos recorrentes fortalecem a unidade do livro quando carregam mudança real: Bíblia herdada, água, refeição simples, jardim, carta, caderno, exames médicos, aliança, cabelo, biblioteca, mesa, luz, fogo e silêncio. O símbolo deve reaparecer com novo sentido à medida que os personagens amadurecem.
- Em temas de saúde, usar linguagem responsável. Estilo de vida saudável, alimentação simples, água, sono, exercício, sol, ar puro, temperança, repouso, confiança em Deus e jejum prudente podem ser apresentados como mordomia do corpo, fatores de proteção, apoio ao tratamento e caminhos de disciplina. Não devem ser vendidos como cura garantida de câncer, transtornos mentais, doenças neurodegenerativas ou qualquer enfermidade grave.
- Quando mencionar os oito remédios naturais associados à tradição adventista ou a práticas naturais, preservar o valor espiritual e comportamental sem transformar o texto em prescrição médica. O cuidado com o corpo pode ser parte da obediência e do amor próprio cristão, mas doença não deve virar prova automática de pecado, ignorância ou falta de fé.
- Jejum pode aparecer como disciplina espiritual e hábito de saúde, inclusive com referência prudente a descanso gastrointestinal, clareza mental, educação dos desejos, equilíbrio metabólico e autofagia. Se citar Yoshinori Ohsumi e o Nobel de Fisiologia ou Medicina de 2016 pelos mecanismos da autofagia, deixar claro que isso não transforma jejum em promessa clínica de cura. Em personagens doentes, jejum deve ser adaptado e acompanhado por médico ou nutricionista.
- Ao tratar câncer, cura, remissão ou milagre, separar fé, medicina e estilo de vida. Deus pode operar milagres, mas a narrativa não deve encorajar abandono de exame, cirurgia, quimioterapia, acompanhamento, nutrição clínica ou orientação profissional. O milagre pode ser narrado como misericórdia extraordinária, não como fórmula replicável.
- Evitar culpabilizar pessoas enfermas. Uma história pode ensinar responsabilidade, amor próprio e escolhas saudáveis sem sugerir que todo sofrimento físico ou mental existe porque a pessoa falhou moralmente.
- Quando o livro defende alimentação saudável, preferir termos e cenas coerentes com a tese: água, refeição da manhã, frutas, raízes, hortaliças, alimentos simples, mesa limpa e hospitalidade sóbria. Evitar que símbolos alimentares contraditórios, como café em excesso ou ultraprocessados celebrados, apareçam nos capítulos finais como se fossem hábitos ideais.
- Para aproximar pessoas de Deus sem perder qualidade literária, manter dupla promessa narrativa: o leitor acompanha uma história de amor conjugal e, ao mesmo tempo, enxerga que seguir Cristo traz sentido, ordem, arrependimento, serviço e esperança. O romance não deve competir com a fé; deve ser consequência visível dela.
- Capítulos precisam orientar o leitor. Em romances publicáveis, usar títulos explícitos como `Capítulo 1: O encontro improvável` ajuda navegação, sumário, revisão, leitura digital e referência em conversas editoriais.
- Para publicação, cuidar de metadados desde o manuscrito: título, subtítulo, autores, ano, idioma, sumário e padrão de capítulo. Quando houver coautoria, atualizar capa, folha de rosto, YAML/Pandoc, DOCX, PDF, EPUB e qualquer arte promocional.
- Em A5/ABNT, não confiar apenas no texto bonito. Validar artefatos: `pdfinfo` para tamanho e páginas do PDF, `unzip -t` para DOCX/EPUB, metadados do EPUB, sumário, capa, folha de rosto, numeração, quebras de capítulo e renderização visual de páginas-chave.
- Depois de qualquer alteração no manuscrito que afete conteúdo, autores, título, subtítulo, capítulos ou metadados, regenerar todos os artefatos de publicação. PDF, DOCX, EPUB e arquivos derivados não podem ficar em versões diferentes da fonte.
- Não declarar "pronto para publicação" sem leitura de prova, revisão visual e conferência de consistência. Prontidão técnica não é igual a prontidão editorial. Um arquivo pode abrir corretamente e ainda ter problema de ritmo, repetição, argumento médico arriscado, excesso de sermão, quebra ruim de página ou capa desalinhada.
- Admoestação editorial: não usar tese moral forte para atropelar humanidade. Personagens cristãos convincentes não parecem perfeitos; eles parecem pessoas sendo corrigidas por Deus. O leitor deve reconhecer luta, vergonha, medo, desejo, erro, arrependimento e aprendizado.
- Admoestação teológica: não transformar masculinidade cristã em dureza, posse ou autoritarismo. O homem que ama como Cristo serve, protege, honra, escuta, trabalha, pede perdão e se entrega. Sacrifício não é teatro de heroísmo; é fidelidade concreta no cotidiano.
- Admoestação literária: não deixar o clímax espiritual resolver tudo sem cenas posteriores. A mudança precisa aparecer depois: em exames, rotina, casamento, conflitos pequenos, mesa, dinheiro, sono, saúde, fala, oração e serviço sem plateia.
- Admoestação operacional: quando outra IA assumir o projeto, ela deve ler `history-chat.md`, o plano de ação e o manuscrito atual antes de continuar. Se começar direto pela última solicitação, há alto risco de desfazer decisões já tomadas sobre fé, saúde, romance, autoria, capa, formato A5 e publicação.

## 2026-07-16 - Diretriz reutilizável: ficção científica filosófica, continuidade entre volumes e fechamento editorial

Aprendizados derivados de revisões de romances de ficção científica filosófica com tecnologia de vida, morte, ressuscitação, empresas, ética, romance conjugal e continuidade entre volumes:

- Em séries literárias, definir qual volume é fonte canônica quando há divergência entre livros. Se o primeiro volume já está consolidado, ele deve prevalecer sobre a continuação em sobrenomes, parentesco, termos centrais, empresas, regras de mundo e arco de origem. A continuação deve ser ajustada para herdar o cânone, não o contrário, salvo decisão explícita do autor.
- Ao usar uma continuação como referência para revisar o primeiro volume, não importar tudo. Plantar apenas sementes leves: lugares, instituições, educação de personagens, termos de mundo e linhas de futuro que aumentem coerência sem transformar o primeiro livro em prólogo da continuação.
- Em romances filosóficos, repetição conceitual não é erro automático. Ideias centrais podem retornar como reforço temático, desde que cada retorno mude contexto, consequência, pressão emocional, risco ou decisão. Cortar filosofia demais pode destruir a identidade do livro; o melhor alvo costuma ser progressão dramática, não redução mecânica.
- Para potencial comercial maior, a revisão final deve melhorar a experiência de leitura sem descaracterizar a obra: plantar tensão mais cedo, variar cenas densas com cenas concretas, fortalecer secundários em pontos onde já aparecem e deixar ameaça/suspense crescer de forma gradual.
- Evitar "edição por fórmula" em protagonistas já complexos. Nem todo personagem precisa de mais defeitos visíveis para ser interessante. Se o protagonista já tem obsessão, culpa, rigidez, medo, controle ou imprudência, forçar novas falhas pode enfraquecer coerência.
- Secundários ficam mais vivos com poucas marcas bem colocadas: uma forma de humor, uma prioridade moral, uma competência prática, uma frase recorrente ou uma reação específica diante do risco. Não é necessário criar subtramas novas se o objetivo é acabamento comercial.
- Ameaças corporativas ou conspiratórias funcionam melhor quando aparecem antes como tendência social, linguagem de mercado, notícia aparentemente comum, campanha publicitária, contrato, tentativa de sondagem ou pressão institucional. Isso evita que o vilão surja como bloco isolado.
- Em ficção científica com tecnologia poderosa, a credibilidade aumenta quando o texto mostra limites: o que a máquina faz, quando para, quem audita, quem autoriza, quais riscos permanecem e quais usos são proibidos. Limites bem narrados tornam a tecnologia mais forte, não mais fraca.
- Para tecnologias de vida/morte, ética deve ser arquitetura narrativa: logs, auditoria, consentimento, revisão cruzada, direito de recusa, preservação de provas, acompanhamento psicológico e governança pública precisam ter função dramática, não apenas aparecer em discursos.
- Em cenas de assédio, flerte ou ambiguidade social, calibrar a narração com justiça. A primeira interação pode ser neutra ou apenas socialmente ambígua; não antecipar julgamento moral se o leitor ainda não viu comportamento grave. Deixar a escalada real aparecer por insistência, mensagens fora de horário, isolamento, toque não consentido, minimização do "não" e registro formal.
- Quando um personagem prudente evita uma conversa ambígua, a narração pode mostrar preferência por encerrar o expediente, voltar para casa ou não alimentar intimidade desnecessária, sem transformar o outro personagem em vilão antes da hora.
- Conversas conjugais sobre pequenas ambiguidades sociais devem ser proporcionais ao evento. Se a cena foi leve, tratar como curiosidade de trabalho; se a cena foi grave, tratar como limite, transparência e proteção. Linguagem exagerada pode fazer o casal parecer dramático ou acusatório sem necessidade.
- Em romances conjugais maduros, as cenas mais fortes frequentemente são cotidianas: lavar louça, arrumar uma bolsa, preparar comida, corrigir uma gola, caminhar sem pressa, rir de uma piada ruim, cuidar sem plateia. O amor fica mais convincente quando aparece no comum recuperado, não só em declarações grandiosas.
- Um prólogo técnico pode ganhar força se abrir com uma âncora emocional curta. Um microflash de 1 a 3 parágrafos com diálogo íntimo pode dar ao leitor motivo humano para acompanhar a hipótese científica.
- Cuidado com "lembrança futura". Se o personagem ainda não viveu algo, chamar de lembrança pode soar impossível ou spoiler estranho. Para abrir um prólogo, preferir memória real anterior, imagem de desejo, prenúncio narrativo impessoal ou reflexão do narrador, conforme o ponto de vista do livro.
- Se o prólogo usa uma memória íntima, manter a plausibilidade temporal: não incluir filhos, eventos ou consequências que ainda não existiam para o personagem naquele momento, a menos que o narrador esteja claramente em outro tempo.
- Ao inserir cenas românticas no prólogo, não alongar demais nem substituir o conflito principal. A função é criar promessa emocional: mostrar o que a morte roubou ou o que o protagonista deseja preservar.
- Depois de qualquer ajuste de tom em uma cena, revisar cenas dependentes. Se uma primeira conversa foi suavizada, o diálogo posterior sobre ela também precisa ser suavizado. Coerência de intensidade importa tanto quanto coerência factual.
- Em listas de personagens, usar função canônica e institucional, não atalhos relacionais imprecisos. Por exemplo, "sócio da empresa" costuma ser mais claro e menos personalista que "sócio de Fernanda", quando a organização tem estrutura corporativa própria.
- Listas finais de personagens também precisam de acabamento editorial: agrupar familiares relacionados quando fizer sentido, evitar descrições longas demais em um único item, corrigir títulos institucionais e manter termos alinhados ao volume anterior.
- Dedicatórias devem soar humanas e naturais. Frases como "enquanto estão vivos" podem parecer duras ou involuntariamente estranhas; revisar dedicatórias com o mesmo cuidado do miolo, pois elas estão entre as primeiras impressões do leitor.
- Ao avaliar um DOCX final de publicação, distinguir integridade técnica de perfeição editorial. Um DOCX pode passar em `unzip -t`, ter A5 correto e metadados limpos, mas ainda precisar de ajustes em dedicatória, lista de personagens, quebras de parágrafo, organização visual ou pequenos termos canônicos.
- Para checar DOCX final sem depender de editor gráfico, extrair `word/document.xml`, ler parágrafos, contar capítulos, buscar termos proibidos, inspecionar `docProps/core.xml`, verificar `w:pgSz`, procurar revisões (`w:ins`, `w:del`), comentários, estilos e quebras de página.
- Em obras longas revisadas por muitas IAs, sempre rodar buscas negativas: nomes antigos, lugares reais removidos, moedas reais, grafias antigas, termos que foram substituídos, comentários de revisão, `TODO`, `FIXME`, placeholders e expressões antigas que mudaram de tom.
- Quando uma alteração muda o manuscrito fonte, regenerar todos os derivados públicos. Nunca deixar `working/`, `build/` e `public/` divergirem, especialmente quando o usuário pergunta se a versão está pronta para publicação.
- Validações úteis para fechamento: capítulos sequenciais, zero linhas absurdamente longas no Markdown, integridade DOCX/EPUB, `pdfinfo` para PDF A5, metadados corretos, busca limpa de termos proibidos e confirmação de que trechos novos aparecem nos exports.
- Admoestação editorial: não declarar "perfeito" com facilidade. É mais honesto dizer "publicável", "tecnicamente pronto", "muito próximo" ou "pronto após ajustes pontuais", conforme o caso. Perfeição editorial é rara; prontidão publicável é uma decisão prática.
- Admoestação narrativa: tecnologia extraordinária não substitui humanidade ordinária. Em histórias sobre imortalidade, o leitor costuma ser convencido não apenas pela máquina, mas pela mesa, pela casa, pela louça, pela pessoa amada implicando com nossos excessos e pelo direito de continuar vivendo o pequeno.
- Admoestação operacional: antes de modificar livro pronto para publicação, criar backup, fazer mudança cirúrgica, validar, regenerar artefatos e registrar no histórico local. Mudanças pequenas no fim podem melhorar muito, mas também podem introduzir inconsistência se não forem rastreadas.

## 2026-07-16 - Conselhos reutilizáveis: revisão final de série, tom e resíduos de versões antigas

Aprendizados derivados da revisão final de um segundo volume de ficção científica após muitas rodadas de adaptação, continuidade, romance e fechamento técnico:

- Quando o usuário define que apenas um volume deve ser editado, respeitar o escopo com rigor. Mesmo que o livro anterior contenha informações úteis, ele deve funcionar como referência canônica, não como alvo de alteração, até o autor pedir explicitamente.
- Antes de qualquer nova correção em fase final, reler o histórico local e o histórico global. Em projetos longos, a última solicitação pode depender de dezenas de decisões anteriores sobre nomes, família, empresas, tom religioso/secular, formato A5, geração de artefatos e relação entre volumes.
- Se outro revisor ou outra IA estiver trabalhando em um volume paralelo, não tentar "sincronizar" os dois por edição direta. Registrar o diagnóstico, ajustar apenas o volume autorizado e preservar a divisão de responsabilidades.
- Em obras que nasceram de versões antigas com soluções moralmente fortes, procurar resíduos de linguagem defensiva. Se uma versão antiga transformava criminosos, executava culpados ou usava punição espetacular, a versão final pode ficar contaminada por excesso de explicações do tipo "não matamos", "não transformamos" ou "preservamos vivos". O melhor acabamento é integrar a nova solução com naturalidade: custódia, prova, supervisão, processo e consequência.
- Não deixar a narrativa parecer pedido de desculpas pela versão anterior. O leitor final não conhece o rascunho antigo; ele precisa receber uma cena coesa, não um debate invisível com a história que foi descartada.
- Quando o autor pede tom secular, remover não só referências diretas a Deus, religião ou alma, mas também imagens e vocabulários que puxem a leitura para registro devocional. A substituição deve preservar densidade moral com termos como consciência, responsabilidade, dignidade, solidariedade, propósito, método, clemência e limite institucional.
- O inverso também vale: quando o livro é religioso, não secularizar por reflexo. Cada obra deve obedecer ao pacto de leitura definido pelo autor e pelo gênero.
- Em romance pós-trauma, calibrar paixão com autonomia emocional. O personagem que ama não deve parecer escravo, zumbi, salvador absoluto ou dependente de aprovação; a pessoa amada também não deve parecer prêmio, dívida, troféu ou paciente moral. O casal precisa caminhar em igualdade, com liberdade real de escolha, reciprocidade e possibilidade humana de magoar sem que a narrativa inferiorize um dos dois.
- Presentes românticos têm cronologia moral. Um objeto íntimo antes de haver reciprocidade clara pode soar como pressão ou argumento; depois do namoro, o mesmo objeto pode funcionar como carinho legítimo, memória de cuidado e símbolo de presença.
- Repetições de autonomia, independência, "não mande em mim", "sem posse" ou "por escolha" podem começar corretas e terminar didáticas. Depois que o conceito estiver claro, trocar explicações por comportamento: pausa, consentimento, humor, silêncio aceito, cuidado prático e decisão compartilhada.
- Pais, mentores e gênios técnicos precisam de humanidade proporcional. Um personagem muito inteligente pode soar frio, rabugento ou socialmente incapaz se só fala em regra, risco e autoridade. Humor doméstico, escuta, autocrítica discreta, cuidado prático e respeito à cadeia de comando tornam a prudência mais humana.
- Ao suavizar uma relação familiar, revisar cenas dependentes. Se a primeira conversa pai-filho fica mais empática, cenas posteriores não devem continuar tratando o pai como se ele ainda fosse duro, controlador ou emocionalmente ausente.
- Em listas finais de personagens, evitar descrições que reduzam estruturas institucionais a relações pessoais. "Sócio da Universe Corp" é mais canônico e reutilizável que "sócio de Fernanda" quando a empresa é uma instituição com conselho, presidente, executivos e responsabilidades próprias.
- Dedicatória, lista de personagens, sumário e títulos de capítulos fazem parte da experiência literária. Não os tratar como anexos menores: uma frase estranha na dedicatória ou um título que carrega resíduo de versão antiga pode enfraquecer a impressão de acabamento.
- Títulos de capítulos devem acompanhar a tese editorial atual. Se um título preserva um termo que a revisão decidiu reduzir, como "suspeitos vivos", ele reintroduz a ênfase removida do miolo.
- Em fase final, usar duas buscas: busca negativa para termos proibidos ou antigos, e busca positiva para confirmar que os novos trechos chegaram aos exports. Não basta o Markdown estar certo; PDF, DOCX e EPUB precisam conter a versão correta.
- Cuidado com falsos positivos em buscas textuais. Palavras curtas podem aparecer dentro de outras, como `alma` dentro de `calma`. Usar fronteiras de palavra e conferir o contexto antes de corrigir.
- Validar também detalhes mecânicos do Markdown, como trailing whitespace, linhas longas e quebras de poema. Espaços finais podem ser intencionais para hard break, mas, em fase final, é mais robusto usar sintaxe explícita e deixar `git diff --check` limpo.
- Regenerar todos os formatos depois de qualquer mudança textual final, mesmo que pequena. Um ajuste de título, frase ou poema pode alterar paginação, sumário, EPUB, DOCX e PDF.
- Admoestação editorial: não consertar um exagero criando outro. Reduzir violência não exige transformar o texto em excesso de cautela; reforçar autonomia não exige transformar o casal em debate jurídico; remover religião não exige esvaziar a moral; amadurecer um personagem não exige retirar sua paixão.
- Admoestação operacional: uma revisão final séria deve terminar com evidência, não impressão. Registrar quais buscas foram limpas, quais artefatos foram regenerados, qual tamanho/paginação do PDF saiu e se DOCX/EPUB passaram em integridade.

## 2026-07-16 - Registro prévio: estudo de estrutura padrão para projetos de livros

Foi iniciada uma investigação da estrutura real dos projetos de livros em `/home/josue/Documents/josue-writter-workspace`, com leitura orientadora do `PROTOCOLO_SIMPLICIDADE_3.md`, para consolidar aqui uma padronização reutilizável de pastas, arquivos de histórico, documentação, fontes, artefatos de publicação e validações. O objetivo é criar um equivalente editorial ao esqueleto de um projeto de software, como ocorre em estruturas geradas por ferramentas do tipo `create-react-app`, mas adaptado à escrita de livros, romances, reportagens, artigos e obras acadêmicas.

## 2026-07-16 - Padronização recomendada para projetos de livros

Estudo realizado nos projetos de livros do workspace identificou padrões reais já usados: `history-chat.md`, `public/`, `publicacao/`, `build/`, `backup/`, `backups/`, `old/`, `working/`, `manuscrito/`, `imagens/`, `media/`, `scripts/`, saídas em `pdf/`, `docx/`, `epub/`, `latex/` e subpastas de validação. A recomendação é consolidar esses padrões em um esqueleto editorial estável, equivalente conceitual ao que uma ferramenta de programação faz ao criar um projeto novo.

Princípio central: um projeto de livro deve ser navegável por qualquer pessoa ou IA no futuro sem depender da memória da conversa. A raiz precisa explicar o que é a obra, onde está o texto-fonte, como gerar os artefatos, o que já foi decidido, o que ainda falta validar e quais arquivos são fonte, intermediários, publicação ou histórico.

Estrutura base recomendada:

```text
nome-do-livro/
├── README.md
├── history-chat.md
├── docs/
│   ├── TASKS.md
│   ├── DECISIONS.md
│   ├── STYLE-GUIDE.md
│   ├── STRUCTURE.md
│   ├── VALIDATION.md
│   ├── REFERENCES.md
│   └── RELEASE-CHECKLIST.md
├── manuscrito/
│   ├── original/
│   ├── trabalho/
│   ├── revisado/
│   └── final/
├── assets/
│   ├── imagens/
│   ├── capas/
│   ├── fontes/
│   └── qr/
├── scripts/
├── build/
│   ├── tmp/
│   ├── chapters/
│   ├── exports/
│   └── logs/
├── publicacao/
│   ├── pdf/
│   ├── docx/
│   ├── epub/
│   ├── markdown/
│   ├── latex/
│   └── metadata/
├── backups/
└── old/
```

Variações aceitáveis:

- `public/` pode ser usado no lugar de `publicacao/` quando o projeto já segue esse padrão, mas a função deve ser a mesma: conter artefatos finais ou artefatos claramente publicáveis.
- `working/` pode substituir `manuscrito/trabalho/` em projetos já existentes, desde que o README explique que é o manuscrito ativo.
- `imagens/` pode substituir `assets/imagens/` quando o projeto já está assim, mas imagens, capas, QR codes e fontes devem ficar separados de manuscritos e saídas finais.
- `backup/` e `backups/` devem ter uma regra clara. Recomenda-se `backups/` para snapshots manuais e datados; `old/` para versões obsoletas preservadas por referência histórica.
- Se o projeto usa muitos idiomas, criar subpastas `pt/`, `en/`, etc. em `manuscrito/`, `publicacao/`, `build/` ou `assets/`, mas sempre com a mesma lógica de fonte, intermediário e saída.

Função de cada parte:

- `README.md`: porta de entrada. Deve informar título, gênero, finalidade, status editorial, fonte principal, comandos de geração, formatos esperados, regra de validação e onde ficam os artefatos finais.
- `history-chat.md`: memória específica daquele livro. Deve registrar solicitações do autor, decisões, mudanças feitas por IA, pendências, validações e alertas. Não deve virar diário genérico; deve ser útil para continuidade editorial.
- `global-history-chat.md`: deve ficar no diretório pai ou ancestral combinado e receber apenas aprendizados reutilizáveis entre projetos, como esta padronização de estrutura.
- `docs/`: documentação de gestão editorial, não manuscrito. Deve conter tarefas, decisões, estilo, estrutura, validação, referências e checklist de lançamento.
- `manuscrito/` ou `working/`: texto-fonte da obra. Markdown de manuscrito pertence aqui, não em `docs/`, porque é conteúdo editorial e não documentação de processo.
- `assets/`, `imagens/` ou `media/`: ativos usados pela obra, como imagens internas, capa, contracapa, QR code, fontes e materiais de divulgação.
- `scripts/`: automações reprodutíveis para conversão, validação, extração, inserção de QR code, geração de PDF/DOCX/EPUB e auditorias.
- `build/`: intermediários gerados, temporários, capítulos separados, logs e arquivos técnicos que podem ser reconstruídos. Não deve ser tratado como fonte definitiva.
- `publicacao/` ou `public/`: saídas destinadas a leitura, prova, venda ou envio para plataforma. Precisa separar `pdf/`, `docx/`, `epub/`, `markdown/`, `latex/` e metadados quando houver.
- `backups/`: cópias antes de alterações arriscadas. Devem ser datadas e explicadas.
- `old/`: versões antigas que não são mais a fonte principal. Não usar como base sem registrar a decisão em `docs/DECISIONS.md` ou `history-chat.md`.

Adaptação do `PROTOCOLO_SIMPLICIDADE_3.md` para livros:

- A documentação deve ser escrita para o "eu futuro" que abrirá o projeto sem contexto. Isso vale ainda mais para livros longos, porque decisões de continuidade, tom, formatação, ABNT, UICLAP, personagens, bibliografia e versões podem se perder facilmente.
- A regra de manter `README.md`, `history-chat.md` e `docs/` é diretamente aplicável a projetos editoriais.
- A regra de colocar Markdown em `docs/` precisa ser adaptada: Markdown de documentação vai para `docs/`; Markdown de manuscrito vai para `manuscrito/`, `working/` ou equivalente.
- Decisões importantes devem ir para `docs/DECISIONS.md`: mudança de nome de personagem, corte de capítulo, alteração de tese, escolha de formato A5/A4, adoção de ABNT, uso de Pandoc/LaTeX/LibreOffice, inclusão de QR code, idioma-base e padrão bibliográfico.
- Tarefas devem ir para `docs/TASKS.md`, com estado claro: pendente, em andamento, concluído, bloqueado ou precisa de revisão humana.
- A etapa final de qualquer ciclo deve incluir validação objetiva, não apenas impressão subjetiva de que "ficou bom".

Documentos mínimos em `docs/`:

- `TASKS.md`: lista operacional do que falta fazer, com evidência de conclusão.
- `DECISIONS.md`: decisões editoriais e técnicas importantes, com data e motivo.
- `STYLE-GUIDE.md`: tom, público, regras de linguagem, termos proibidos, termos preferidos, tratamento de citações, uso de primeira/terceira pessoa e padrão de títulos.
- `STRUCTURE.md`: sumário planejado, capítulos, subcapítulos, ordem da argumentação ou arco narrativo.
- `VALIDATION.md`: comandos e critérios para conferir PDF, DOCX, EPUB, sumário, margens, cabeçalhos, imagens, links, metadados e presença de trechos esperados.
- `REFERENCES.md`: bibliografia, fontes, leituras, normas ABNT, entrevistas, links e materiais de apoio.
- `RELEASE-CHECKLIST.md`: checklist antes de publicar, vender, enviar para UICLAP ou compartilhar com leitores.

Documentos adicionais por tipo de obra:

- Ficção, romance e fantasia: `CHARACTERS.md`, `CONTINUITY.md`, `TIMELINE.md`, `WORLD-BUILDING.md`, `PLOT-THREADS.md`.
- Notícias, reportagens e entrevistas: `SOURCES.md`, `FACT-CHECK.md`, `INTERVIEWS.md`, `RIGHTS-AND-PERMISSIONS.md`, `LEGAL-REVIEW.md`.
- Acadêmicos, artigos e ensaios: `METHODOLOGY.md`, `CITATION-STYLE.md`, `BIBLIOGRAPHY.md`, `ARGUMENT-MAP.md`, `PEER-REVIEW-NOTES.md`.
- Técnicos e didáticos: `EXAMPLES.md`, `EXERCISES.md`, `ERRATA.md`, `GLOSSARY.md`, `TECHNICAL-VALIDATION.md`.

Padrão recomendado para o README de livro:

```markdown
# Título do Livro

## Resumo rápido
- Gênero:
- Autor:
- Idioma-base:
- Status:
- Formato-alvo:
- Fonte principal:
- Saídas finais:

## Estrutura do projeto
- `manuscrito/`: texto-fonte.
- `docs/`: planejamento, decisões, validações e referências.
- `assets/`: imagens, capas, fontes e QR codes.
- `scripts/`: automações.
- `build/`: intermediários reconstruíveis.
- `publicacao/`: PDF, DOCX, EPUB e outros artefatos finais.

## Como gerar
Comandos exatos, dependências e observações.

## Como validar
Comandos e critérios mínimos antes de chamar o livro de pronto.

## Estado editorial
O que está concluído, o que falta revisar e quais riscos permanecem.
```

Qualidade e validação antes de considerar uma obra pronta:

- Validar DOCX e EPUB com `unzip -t`.
- Validar PDF com `pdfinfo`.
- Extrair texto com `pdftotext` e procurar título, capítulos, QR code textual quando existir, bibliografia, termos obrigatórios e termos proibidos.
- Renderizar amostras de páginas com `pdftoppm` ou abrir visualmente para conferir capa, sumário, margens, cabeçalhos, rodapés, imagens e última página.
- Conferir se `publicacao/` ou `public/` foi regenerado depois da última alteração no manuscrito.
- Conferir se `build/` não está sendo confundido com versão final.
- Procurar resíduos: `TODO`, `FIXME`, comentários de IA, nomes antigos, caminhos quebrados, links locais indevidos, placeholders, capítulos duplicados, sumário manual obsoleto e páginas finais sem acabamento.
- Registrar no `history-chat.md` o que foi alterado, o que foi validado, quais artefatos foram gerados e o que ainda exige leitura humana.

Regra operacional para IAs e revisores:

- Antes de editar: ler `README.md`, `history-chat.md`, documentos relevantes em `docs/` e, quando existir, `global-history-chat.md`.
- Antes de alteração arriscada: criar backup datado ou preservar cópia em `backups/`.
- Durante a edição: alterar o manuscrito-fonte, não o PDF final diretamente, salvo tarefas específicas de pós-processamento.
- Depois de editar: atualizar `history-chat.md`, regenerar saídas necessárias e validar artefatos.
- Depois de aprender algo reutilizável entre livros: registrar em `global-history-chat.md`, sem copiar detalhes privados ou irrelevantes de um projeto específico.

Observação final: padronizar a estrutura não significa apagar a história dos projetos existentes. Para livros já em andamento, a migração deve ser gradual: primeiro documentar a estrutura atual no README, depois introduzir `docs/`, depois separar fontes, intermediários e saídas finais. O objetivo é reduzir ambiguidade, preservar autoria, facilitar revisão humana e impedir que arquivos de trabalho sejam confundidos com arquivos prontos para publicação.

Registro posterior: a investigação foi concluída com leitura de exemplos reais do workspace, leitura de trechos operacionais do `PROTOCOLO_SIMPLICIDADE_3.md` e consolidação da recomendação acima. Em tarefas futuras de livros, esta padronização deve ser usada como referência inicial antes de criar, reorganizar, revisar ou publicar obras.

## 2026-07-16 - Registro prévio: criação de diretório-template editorial

Foi solicitado criar primeiro um diretório-template físico para projetos de livros e, depois, um programa Python capaz de gerar esse mesmo esqueleto. A ordem correta para esta tarefa é: 1) materializar o template em `templates/book-project-template/`; 2) validar sua estrutura; 3) criar o algoritmo Python de geração a partir desse padrão; 4) registrar o resultado neste histórico global.

Registro posterior: foi criado o template editorial em `templates/book-project-template/`, com `README.md`, `history-chat.md`, `docs/`, `manuscrito/`, `assets/`, `scripts/`, `build/`, `publicacao/`, `backups/` e `old/`. Tambem foi criado o gerador `templates/create_book_project.py`, que copia o template, substitui placeholders (`{{BOOK_TITLE}}`, `{{BOOK_SLUG}}`, autor, genero, idioma, data, formato e status) e cria um manuscrito inicial em `manuscrito/trabalho/`. Validacoes executadas: `python3 -m py_compile templates/create_book_project.py`, execucao em modo `--dry-run` e criacao real temporaria com conferencia de arquivos essenciais e substituicao de placeholders.

## 2026-07-16 - Registro prévio: consolidação em diretório dedicado de protocolo editorial

Foi solicitado copiar o conteúdo genérico reutilizável sobre estrutura de livros, incluindo os aprendizados do `global-history-chat.md`, o template editorial e o gerador Python, para um diretório dedicado que possa depois ser transformado em repositório Git e enviado ao GitHub. A decisão operacional é criar uma pasta independente em `/home/josue/Documents/Informática/programming/protocolos/protocolos-escrita-livros`, inspirada na organização de `protocolos-simplicidade`, preservando o `global-history-chat.md` original no workspace e levando para o novo projeto apenas o extrato reutilizável e publicável.

Registro posterior: foi criado o projeto dedicado `/home/josue/Documents/Informática/programming/protocolos/protocolos-escrita-livros`, com `README.md`, `history-chat.md`, `.gitignore`, `docs/`, `pt/`, `en/` e `templates/`. O template editorial e o gerador Python foram copiados para `templates/`; o conteudo reutilizavel do historico global foi consolidado em `docs/GLOBAL_HISTORY_EXTRACT.md`; e o protocolo inicial foi criado em `pt/PROTOCOLO_EDITORIAL_LIVROS.md`. Validacoes executadas no novo diretorio: listagem estrutural, checagem de sintaxe do gerador com `compile()`, execucao `--dry-run`, criacao real temporaria de projeto de livro, busca por caches Python e busca por marcadores pendentes.

## 2026-07-16 - Registro prévio: licença, bilinguismo, Git e GitHub do protocolo editorial

Foi solicitado finalizar a primeira versão publicável do projeto `/home/josue/Documents/Informática/programming/protocolos/protocolos-escrita-livros` com licença MIT, remoto `https://github.com/JosueAmaral15/protocolo-editorial-para-livros.git`, documentação bilíngue PT/EN, `README.md` raiz em inglês, READMEs próprios em `pt/` e `en/`, inicialização Git, primeiro commit e push.

Registro posterior: o projeto dedicado recebeu licença MIT, README raiz em inglês, documentação bilíngue em `pt/PROTOCOLO_EDITORIAL_LIVROS.md` e `en/EDITORIAL_BOOK_PROTOCOL.md`, READMEs próprios em `pt/` e `en/`, Git inicializado em `main`, primeiro commit `7d5215f Initial editorial book protocol`, remoto `origin` configurado para `https://github.com/JosueAmaral15/protocolo-editorial-para-livros.git` e push inicial concluído com sucesso para `origin/main`. Depois do push, o histórico local e os documentos operacionais do repositório foram atualizados para registrar a publicação; essa documentação posterior foi enviada em `03e3310 Document initial GitHub publication` e ajustada em `c0af963 Clarify GitHub publication history`, ambos com push concluído para `origin/main`.

## 2026-07-16 - Registro prévio: livro de consumo derivado do histórico global

Foi solicitado transformar o conteúdo reutilizável do `global-history-chat.md` em um livro separado dentro de `books`, com PDF e EPUB para leitor final/Kindle. A regra editorial definida é não publicar o histórico bruto: o material deve ser curado em capítulos, removendo ruído operacional, caminhos excessivos e registros de bastidor, mantendo apenas aprendizados úteis sobre revisão editorial com IA, padronização de projetos de livros, validação de artefatos e publicação.

Registro posterior: foi criado o livro separado `books/memoria-editorial-com-inteligencia-artificial`, com manuscrito curado em português, script de geração, PDF A5, EPUB, DOCX e Markdown exportado. O livro se chama `Memória Editorial com Inteligência Artificial` e transforma aprendizados do histórico global em ensaio de consumo para autores, revisores e leitores interessados em escrita com IA. Validações executadas: PDF A5 com 27 páginas por `pdfinfo`, EPUB e DOCX íntegros por `unzip -t`, texto extraído confirmando título/termos-chave/URL UICLAP e inspeção visual da capa textual e da página final com QR Code. Cópias publicáveis foram colocadas também nas pastas centrais de PDF, EPUB e DOCX em `books`.

## 2026-07-16 - Registro prévio: capa gráfica para livro derivado de histórico

Foi solicitado criar uma capa gráfica para o livro `Memória Editorial com Inteligência Artificial`, derivado do `global-history-chat.md`, e incrementar o acabamento editorial quando pertinente. A estratégia será gerar uma capa reprodutível como asset do projeto, integrá-la ao PDF/EPUB/DOCX e validar visualmente a capa e a página final com QR Code.

Registro posterior: a capa gráfica foi criada de forma reprodutível por script local, salva em PNG e PDF dentro de `assets/capas/`, integrada como primeira página do PDF, registrada como capa do EPUB e inserida no DOCX. O livro também recebeu `contracapa.md` e `metadata.yaml`. O PDF final passou a ter 28 páginas A5; EPUB e DOCX passaram em `unzip -t`; a capa e a página final com QR Code foram renderizadas e conferidas visualmente. As cópias centrais em `books` foram atualizadas e confirmadas por checksum.

Aprendizado reutilizável: separar `validação técnica` de `revisão humana` evita falsa pendência e falsa aprovação. A validação técnica pode confirmar integridade, sumário, capa, QR Code e formatos por ferramentas; a revisão humana continua responsável por julgamento editorial, comercial e bibliográfico.

## 2026-07-16 - Registro prévio: metodologia reutilizável de capas para livros

Foi solicitado examinar capas existentes em `/home/josue/Documents/Escritos de Josué/Livros de Josué/Capas` e avaliar como aproveitá-las nos livros de `/home/josue/Documents/josue-writter-workspace/books`. A metodologia desejada é inventariar capas, mapear cada capa ao livro correspondente, preservar originais, organizar capas externas em `books/capas/` e preparar arquivos de upload/marketing separados do miolo.

Registro posterior: foi criado `books/capas/` como acervo central, com cópia preservada das capas originais em `books/capas/originais/` e inventário técnico em `books/capas/inventarios/2026-07-16/`. O resultado confirmou que a metodologia é replicável, mas não deve ser aplicada cegamente: capas com título idêntico podem ser reaproveitadas diretamente como arte externa; capas genéricas ou com título divergente devem virar base de nova arte; e a capa completa UICLAP deve ser gerada somente depois de confirmar a paginação final do miolo para calcular lombada e contracapa.

Correção conceitual posterior: capas completas com frente, lombada e contracapa são artefatos externos de publicação, não parte do miolo do livro. Para UICLAP, a estrutura recomendada é manter um acervo central como `books/capas/`, separado de `publicacao/pdf`, `publicacao/epub`, `publicacao/docx` e do manuscrito. A integração dessas capas significa preparar arquivos de upload/marketing e metadados, não inserir a capa completa dentro do conteúdo PDF/EPUB/DOCX.

Registro posterior da correção: o acervo central foi materializado em `books/capas/`, com `originais/`, `inventarios/` e `obras/`. O inventário anterior foi realocado para `books/capas/inventarios/2026-07-16/`, as capas originais foram copiadas para `books/capas/originais/`, e a metodologia documentada foi corrigida para separar capa UICLAP externa de miolo PDF/EPUB/DOCX.

Registro prévio: iniciou-se a curadoria das capas copiadas para `books/capas/originais/`. O critério reutilizável é selecionar capas por correspondência forte com obra real, legibilidade de título, utilidade para UICLAP e ausência de duplicata visual/hash, mantendo variações e bases genéricas fora da seleção principal até revisão humana.

Registro posterior: a curadoria criou `books/capas/selecionadas/` com 25 capas relevantes e não redundantes, manifesto TSV, folha de contato e relatório de alternativas. O aprendizado reutilizável é separar a seleção principal das bases genéricas: capas com título claro e correspondência forte entram na seleção; variações, duplicatas e artes sem título permanecem preservadas como material de base ou revisão futura.

Registro prévio: será criado um plano de ação em Markdown para padronizar a produção de capas UICLAP por livro. A diretriz reutilizável é: confirmar miolo final e paginação antes de calcular lombada; produzir capa completa como arquivo externo; manter capa frontal, capa completa, fontes, metadados e validações em pastas separadas; e nunca misturar contracapa/lombada ao miolo PDF/EPUB/DOCX.

Registro posterior: o plano `books/capas/PLANO_ACAO_CAPAS_UICLAP.md` foi criado. Ele padroniza a execução por fases: fila de trabalho, validação do miolo, escolha de capa-base, pasta da obra, contracapa, cálculo de lombada, montagem da capa completa, validação técnica, revisão humana e pacote final. O aprendizado reutilizável é tratar `pronta_para_upload` como status posterior à validação técnica e à revisão humana, não como simples existência de uma imagem de capa.

Registro prévio: a próxima execução do plano de capas UICLAP será criar uma fila real de obras e preparar pilotos. A regra reutilizável permanece: pilotos podem organizar metadados, capa-base e validação de miolo, mas não podem gerar capa definitiva nem status `pronta_para_upload` sem confirmação do gabarito atual da plataforma e revisão humana.

Registro posterior: a fila real de capas UICLAP foi criada com 25 itens e três pilotos estruturais foram preparados: Manifesto Humanismo Naturalista Vitalista, Por que existem pobres e desigualdades sociais, e A Mente Humana. A validação confirmou miolos A5 e metadados/checklists por piloto. A regra reutilizável foi preservada: piloto estrutural não é capa pronta; `pronta_para_upload` exige gabarito UICLAP, cálculo de lombada, capa completa exportada, validação visual/técnica e revisão humana.

Registro prévio: o usuário forneceu um gabarito visual de capa UICLAP com medidas: largura total `310,0 mm + 10 mm` (`7559 px`), altura total `210,0 mm + 10 mm` (`5197 px`), capa/frente `147,0 mm + 5 mm` (`3591 px`), contracapa `147,0 mm + 5 mm` (`3591 px`), lombada `16,0 mm` (`378 px`), sangria `5 mm` e margem de segurança `10 mm`. Aprendizado reutilizável: esse tipo de gabarito deve ser tratado como referência de capa completa externa; a lombada observada vale para aquele exemplo, mas deve ser recalculada por obra a partir do miolo final e das regras atuais da plataforma.

Registro posterior: a metodologia reutilizável foi formalizada em `books/capas/gabaritos/uiclap-a5-147x210-lombada-16mm/` e em `books/capas/scripts/calcular_gabarito_uiclap.py`. Aprendizado reutilizável: quando a conversa ou ferramenta falhar com `image_url` invalido, evitar reenviar/embutir imagem no chat e trabalhar com arquivo local, `identify`, `file`, hash, YAML/JSON e documentação textual. Outro ponto: o arquivo visual recebido pode ser apenas screenshot de referencia, não o arquivo final na resolução exigida pela plataforma. Portanto, registrar dimensões reais do gabarito em metadados e gerar as dimensões finais por script, recalculando lombada para cada livro.

Registro posterior: para preparar capas externas sem assumir valores finais, foram separados dois tipos de automacao: calculo de dimensoes quando a lombada real ja e conhecida, e estimativa operacional marcada como `estimativa_nao_final` quando so existe a paginacao. Aprendizado reutilizavel: guias SVG tecnicos sao uma alternativa segura quando ha falhas de imagem no chat; eles documentam zonas, sangria, area segura e lombada em arquivo texto validavel, sem declarar capa pronta nem substituir a revisao humana.

Registro posterior: contracapas para capas impressas devem passar por dois estados distintos: `preliminar` e `final aprovada humanamente`. A versão preliminar pode ser redigida a partir de trechos extraídos do miolo e servir para layout; a versão final deve ser revisada quanto a fidelidade, tom comercial, promessas indevidas, espaço disponível, QR Code, código de barras e legibilidade em tamanho impresso.

Registro posterior: frentes de capa copiadas a partir de artes existentes devem ser marcadas como `frente_provisoria` até haver revisão visual. Preservar a imagem original em `fonte/`, criar cópia candidata em `frontal/`, registrar hash/dimensões em metadados e manter separado o status de frente aprovada, capa completa UICLAP e arquivo pronto para upload.

Registro posterior: em fluxos editoriais com IA, criar um pacote textual de revisão humana antes da arte final reduz risco de falsa aprovação. Esse pacote deve listar miolo, frente, contracapa, lombada, guia técnico, QR Code/código de barras, decisões pendentes e bloqueios explícitos. A regra de status deve impedir `pronta_para_upload` enquanto qualquer decisão humana ou validação técnica estiver pendente.

Registro posterior: no fluxo deste workspace, a pasta `frontal/` pode conter arquivos que visualmente ja incluem capa, lombada e contracapa. Quando o autor apontar esse uso, a IA deve respeitar a convencao local e registrar o tipo real do arquivo em metadados, em vez de assumir que `frontal/` significa sempre "frente isolada". Tambem foi reforcado que PDFs A5 gerados com a classe LaTeX `book` podem criar titulos de capitulo com fonte e margem vertical grandes demais; uma solucao reutilizavel e aplicar um header LaTeX com `titlesec`, `fancyhdr`, margens A5 controladas e `secnumdepth=-1`, validando depois com `pdfinfo`, `pdftotext -layout`, renderizacao por `pdftoppm` e amostras de posicionamento visual.

Registro prévio: para montar capas completas UICLAP localmente, a automação deve gerar uma única imagem externa com contracapa à esquerda, lombada no centro e capa à direita. Quando só houver paginação e não houver gabarito oficial do portal, a saída deve ser marcada como prova técnica ou estimativa, nunca como arte final pronta para upload. A pasta `books/capas` deve concentrar fonte, metadados, validações e imagens completas, sem inserir essa arte no miolo do livro.

Registro posterior: a montagem em lote de capas completas deve tratar `slug` duplicado como risco real de sobrescrita. A automação precisa criar um `slug_saida` único quando duas obras compartilham o mesmo `slug_livro`, por exemplo acrescentando idioma e ID da capa. Outra regra reutilizável: provas técnicas com lombada estimada podem ser úteis para revisão visual em massa, mas devem salvar `metadata.json`, preview com divisões de contracapa/lombada/capa e manifesto central. Validar sempre quantidade esperada de obras, integridade dos JPGs, tamanho máximo do arquivo, JSONs e memória consumida. Mesmo quando o JPG estiver tecnicamente válido e abaixo do limite da plataforma, o status final só deve ser concedido depois de confirmar o gabarito oficial da UICLAP com o miolo final e revisar o preview 3D.

Registro posterior: antes de gerar capas em lote, nunca assumir que uma curadoria parcial de capas representa o catalogo inteiro de livros. A ordem reutilizavel correta e: 1) inventariar `final-public-pdf` por idioma; 2) contar o total real de PDFs finais; 3) pesquisar PDFs mais recentes em toda a pasta do projeto por `mtime`, `ctime` e, quando disponivel, `birth time`; 4) gerar fila completa separada da fila curada; 5) marcar itens sem capa-base como `template_sem_capa_base` ou `sem_capa_base_mapeada`; 6) gerar provas tecnicas em pasta separada; 7) nao promover nenhuma prova a upload final enquanto houver candidato de miolo mais recente, capa-base provisoria ou lombada estimada. Em catalogos grandes, relatorios resumidos para revisao humana sao tao importantes quanto os JPGs, porque evitam repetir o erro de tratar uma amostra como total.

Registro posterior: para capas em lote, separar quatro categorias evita confusao editorial: 1) `template_sem_capa_base`, que e apenas placeholder tecnico; 2) `capa_candidata_estilo_curado`, que melhora a apresentacao visual com arte tematica, texto correto e metadados, mas ainda exige revisao humana; 3) `prova_tecnica_com_capa_base`, que usa uma arte selecionada mas ainda depende de lombada oficial e preview; 4) `pronta_para_upload`, que so deve existir depois de miolo final, lombada oficial da plataforma, contracapa aprovada, codigo de barras/QR Code revisados e validacao visual. Em lotes grandes, e preferivel compor texto de capa por script local quando a exatidao de titulos importa, porque geracao puramente visual pode produzir letras distorcidas ou texto inconsistente. A arte tematica automatica pode reduzir placeholders, mas nao substitui arte final curada quando o padrao esperado e equivalente a uma capa comercial ilustrada.

## 2026-07-19 - Auditoria detalhada da origem da capa de O Juramento da Herdeira de Vinterholm

### Resposta direta sobre a mulher e o leão

A mulher que representa Kayla e o leão que representa Scarface foram criados juntos, do zero, por inteligência artificial generativa a partir de uma descrição textual.

- Não foi usada fotografia de uma mulher real.
- Não foi usada fotografia de um leão real.
- Não foi feito download de ilustração, banco de imagens, site, rede social ou capa de terceiro.
- A mulher não foi recortada de uma imagem e o leão não foi recortado de outra.
- Não houve colagem de dois arquivos independentes.
- Não foi fornecida imagem de referência ao gerador.
- A chamada registrada contém somente o prompt textual.
- O castelo, a neve, o mar, o vestido, o anel, a iluminação e a paisagem também foram sintetizados na mesma geração.

Portanto, `inventados` é a descrição correta no sentido visual: Kayla, Scarface e o cenário foram interpretados e sintetizados pelo modelo a partir dos personagens fictícios e das exigências narrativas. Eles não existiam antes como aqueles indivíduos específicos em um arquivo-fonte conhecido.

Isso não significa que seja possível conhecer todas as imagens usadas no treinamento do sistema generativo. Significa que, neste projeto, não foi escolhida, baixada nem fornecida uma fotografia ou ilustração específica como origem da mulher ou do leão.

### Qual ferramenta e qual API foram usadas

A geração foi acionada dentro da sessão do Codex pelo recurso embutido:

```text
namespace: image_gen
tool: imagegen
modo: text-to-image
imagens de referência: nenhuma
argumento fornecido: prompt textual
```

Em termos equivalentes, a operação registrada foi:

```javascript
image_gen.imagegen({
  prompt: "descrição completa da capa sem texto"
})
```

Não foi escrito um programa com o SDK da OpenAI. Também não houve comando `curl`, chave de API, URL de endpoint ou requisição HTTP manual no terminal. O Codex enviou o prompt ao serviço de imagem por meio da ferramenta integrada.

O próprio arquivo PNG preserva credenciais C2PA que permitem auditar a origem. A inspeção com `exiftool` mostrou:

```text
Claim_Generator_InfoName: OpenAI Media Service API
softwareAgent name: gpt-image
softwareAgent version: 2.0
digitalSourceType: trainedAlgorithm
action: c2pa.created
```

Essa é a evidência mais precisa disponível sobre a API e o agente gerador. O registro da chamada não informa um identificador público de modelo como `gpt-image-1`, nem expõe a URL interna do serviço. Por isso, não se deve inventar um endpoint ou afirmar um ID de modelo que não foi registrado. A formulação tecnicamente segura é:

> A arte foi gerada pela ferramenta `image_gen.imagegen` do Codex, atendida pela `OpenAI Media Service API`; a credencial C2PA identifica o agente como `gpt-image`, versão `2.0`.

### Como a imagem foi planejada

Antes da geração, foram lidos o manuscrito e os documentos de capa. A direção visual foi derivada de elementos reais da história:

- Kayla como protagonista e herdeira em formação;
- vestido amarelo ou dourado ligado à infância, à poesia e à apresentação real;
- postura serena, corajosa e humilde, sem sensualização ou arrogância;
- Scarface como leão livre, aliado por escolha, com cicatriz visível;
- anel de âmbar como objeto narrativo central;
- castelo de Vinterholm e paisagem medieval nórdica;
- atmosfera fria depois da tempestade, contrastada por luz de esperança;
- fantasia leve, sem horror e sem magia explosiva;
- espaço visual limpo na parte superior para inserir o título depois.

O critério não foi apenas produzir uma imagem bonita. A capa precisava comunicar personagem, gênero, tom moral e elementos reconhecíveis da narrativa sem transformar Scarface em animal domesticado nem Kayla em guerreira sombria.

### As duas tentativas

Foram feitas duas gerações textuais.

Na primeira, o prompt já pedia Kayla, Scarface, castelo, paisagem nórdica e anel de âmbar. A imagem foi tecnicamente produzida, mas a representação do objeto na mão ficou ambígua: o anel podia ser lido como moeda, medalhão ou objeto solto.

Em vez de tentar corrigir o objeto por edição manual, foi feita uma segunda geração com instruções mais explícitas:

- mostrar a mão direita;
- colocar o anel em um dedo;
- deixar claro que era um anel utilizável;
- proibir moeda, medalhão e pingente;
- manter o anel em escala natural;
- manter Scarface livre, sem coleira, sela, rédeas ou armadura.

A segunda versão foi escolhida porque resolveu o problema do anel e preservou os demais critérios.

### Prompt exato da versão escolhida

O prompt original foi escrito em inglês porque a ferramenta visual respondia de forma consistente às especificações estruturadas nesse idioma. Ele foi preservado em `publicacao/capa/README.md` e é reproduzido aqui para que o método seja compreensível:

```text
Use case: illustration-story
Asset type: front book cover base art, no text, vertical portrait composition
Primary request: Create a refined second cover-base image for a Christian medieval romance with light fantasy. No letters, no title, no typography, no logos, no signature, no watermark.
Scene/backdrop: Vinterholm, a northern medieval stone castle in the background with pine trees, cold gray rock, distant cold sea or pale snowy sky after a storm, clear hopeful atmosphere.
Subject: Kayla, a young queen in formation, serene and determined, humble rather than arrogant, wearing a medieval yellow-gold gown or light armor with subtle gold details. Her right hand is visible near the lower middle of the composition, wearing an ancient amber gemstone ring on one finger; the ring is clearly a wearable ring, not a coin, not a medallion, not a pendant. The amber gemstone has a subtle lion motif or warm lion-shaped reflection. Beside her stands Scarface, a large lion with a visible facial scar, calm, imposing, free, and undomesticated.
Style/medium: realistic editorial digital painting, polished book cover art, noble and emotional, cinematic but restrained, not dark fantasy.
Composition/framing: vertical cover layout. Kayla is the main focus slightly off center. Scarface stands beside her as a free ally, not as a pet, not as a mount. The amber ring is readable but natural in scale. Leave clean natural negative space in the upper third for title placement later, but include absolutely no text.
Lighting/mood: soft cinematic light after a storm, warm amber glow on the ring, cool northern blue-gray atmosphere, hope, faith, courage, providence, humility.
Color palette: amber gold, cool blue, gray stone, white snow or pale sky, natural skin tones.
Materials/textures: medieval fabric, aged amber set in metal, stone castle, lion fur, pine forest, cold air.
Text (verbatim): none.
Constraints: no text of any kind; keep Scarface free and undomesticated; Kayla must not look arrogant, seductive, or vengeful; lion must not have a collar, saddle, reins, armor, or domestic posture; the image should read as Christian medieval romance with light fantasy through mood and virtue, not through literal symbols.
Avoid: text, letters, words, typographic marks, logos, signature, watermark, horror, skulls, excessive blood, sensualization, exaggerated armor, arrogant pose, domesticated lion, collar, saddle, mount/riding composition, dark aggressive fantasy, cartoon style, glowing evil eyes, explosive magic, army of animals, visible cross jewelry, excessive literal religious symbols, coin, medallion, pendant.
```

### O que foi salvo como fonte

A segunda geração foi salva sem texto como:

```text
O Juramento da Herdeira de Vinterholm/publicacao/capa/capa-base-frontal-v1.png
```

Dados auditados:

```text
formato: PNG
dimensões: 1024 x 1536 px
cor: RGB 8-bit sRGB
SHA-256: 917c84e8f00fc7538203056cfeda7017d1b1ba8667ee0c04b7eff8ca42161910
commit de entrada: 2d5a4a5e4d4c4cdc97aeb3580bb7ac68dfe31bdb
mensagem do commit: Add first cover base art
```

O histórico Git mostra que esse arquivo-base entrou uma única vez e não foi substituído durante a mudança de título do livro. A identidade editorial mudou, mas a ilustração gerada permaneceu a mesma.

### O que foi modificado depois

É necessário distinguir `arte-base gerada por IA` de `capas derivadas compostas localmente`.

| Arquivo ou elemento | Origem | Modificação posterior |
|---|---|---|
| Mulher/Kayla | Gerada por IA | Não foi recortada nem trocada |
| Leão/Scarface | Gerado por IA na mesma imagem | Não foi recortado nem trocado |
| Castelo, céu, neve e mar | Gerados por IA na mesma imagem | Receberam apenas efeitos globais nas derivações |
| Anel | Gerado por IA na segunda tentativa | Não foi desenhado manualmente depois |
| Título, subtítulo e autores | Não vieram do gerador | Aplicados localmente com ImageMagick |
| Contracapa | Composição local | Fundo derivado da arte-base, escurecido e desfocado, com texto local |
| Lombada | Composição local | Fundo sólido, título e autores aplicados por script |
| Post social | Composição local | Corte quadrado, escurecimento e textos |

Não houve retoque individual do rosto da mulher ou da anatomia do leão em Photoshop, GIMP, máscara seletiva ou nova edição generativa. As derivações usaram operações globais como redimensionar, recortar, escurecer, desfocar o fundo da contracapa e sobrepor tipografia.

### Como cada capa derivada foi construída

`publicacao/capa/capa-oficial-v1.png`:

- usa `capa-base-frontal-v1.png`;
- acrescenta gradiente escuro superior e inferior;
- cria título, subtítulo e autores em imagens transparentes;
- compõe essas camadas com ImageMagick;
- é reproduzida por `scripts/build_capa_oficial.sh`.

`publicacao/capa/capa-digital-v1.png` e `capa-digital-v2.png`:

- usam a mesma arte-base;
- acrescentam título, subtítulo, autores e, na v2, chamada opcional;
- são reproduzidas por `scripts/build_capa_digital.sh`.

`publicacao/marketing/post-social-v1.png`:

- redimensiona e recorta a arte-base para 1080 x 1080 px;
- escurece o fundo;
- acrescenta chamada, payoff e autoria;
- é reproduzida por `scripts/build_marketing_post.sh`.

`publicacao/uiclap/O-Juramento-da-Herdeira-de-Vinterholm-UICLAP-A5-v1.jpg`:

- usa a capa oficial como painel frontal;
- usa a arte-base escurecida, dessaturada e levemente desfocada como fundo da contracapa;
- cria lombada e textos localmente;
- reserva área branca para o código de barras;
- monta contracapa à esquerda, lombada no centro e frente à direita;
- é reproduzida por `scripts/build_uiclap_cover.sh`.

Nenhuma dessas composições exigiu uma API de imagens. Depois da geração inicial, todo o trabalho foi feito localmente com Bash, ImageMagick, fontes instaladas ou armazenadas no projeto e cálculos de dimensões.

### Por que o texto não foi pedido à IA

O gerador recebeu a instrução explícita de produzir uma imagem sem letras. Essa separação foi intencional:

- modelos de imagem podem deformar palavras;
- o título mudou posteriormente;
- autoria e subtítulo precisam ser exatos;
- texto em camada local pode ser corrigido sem gerar outra Kayla ou outro Scarface;
- o rebranding pôde ser feito apenas regenerando as composições tipográficas.

Esse é um princípio reutilizável: gerar a ilustração sem texto e tratar tipografia, lombada, contracapa e código de barras como engenharia editorial local.

### Como auditar a origem no futuro

Comandos úteis:

```bash
identify publicacao/capa/capa-base-frontal-v1.png
sha256sum publicacao/capa/capa-base-frontal-v1.png
exiftool -G1 -a -s publicacao/capa/capa-base-frontal-v1.png
git log -- publicacao/capa/capa-base-frontal-v1.png
git show 2d5a4a5e4d4c4cdc97aeb3580bb7ac68dfe31bdb:publicacao/capa/README.md
```

Observação: programas de composição ou exportação podem remover as credenciais C2PA das imagens derivadas. Por isso, a arte-base original, seu hash, seu prompt, seu README e seu commit devem ser preservados. A ausência de metadados C2PA numa capa derivada não transforma a imagem em download externo; a cadeia de derivação deve ser comprovada pelo arquivo-base e pelos scripts.

### Limite de reprodutibilidade

O prompt e o procedimento são reproduzíveis, mas a imagem exata não é garantida em uma nova geração. Sistemas generativos são probabilísticos, e o serviço ou o agente podem mudar. Para preservar exatamente esta Kayla e este Scarface, a referência correta é o PNG versionado e seu SHA-256, não a expectativa de que o mesmo prompt recrie os mesmos pixels.

### Regra para futuros projetos

Toda capa que use IA generativa deve registrar, no mínimo:

- se houve geração textual, edição de imagem ou download;
- ferramenta, serviço e evidência técnica disponíveis;
- prompt e prompts negativos;
- existência ou ausência de imagens de referência;
- quantidade de tentativas e motivo da escolha;
- arquivo-fonte sem texto;
- dimensões, hash e commit;
- scripts das derivações;
- mudanças feitas após a geração;
- limites do que não pode ser comprovado.

Esse registro evita que uma capa gerada, uma fotografia licenciada, uma colagem e uma composição local sejam tratadas como se fossem a mesma coisa.
