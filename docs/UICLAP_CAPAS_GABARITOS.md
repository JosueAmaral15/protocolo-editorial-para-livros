# UICLAP: Capas, Lombadas, Contracapas e Orelhas

## Regra principal

Nao existe uma medida universal pronta para todas as capas UICLAP. O gabarito
oficial deve ser obtido no Portal depois do upload do miolo final: formato,
numero de paginas e papel determinam a lombada. A calculadora serve para
planejamento; o guia de tamanho e o SVG gerados pelo Portal sao a referencia de
producao e prevalecem sobre qualquer medida anotada neste repositorio.

## Criatividade e qualidade comercial

Cada livro deve ter uma direcao de arte propria, coerente com genero, tese,
publico e promessa de leitura. IA generativa pode criar arte-base narrativa
unica, mas nao deve copiar obras, estilos identificaveis de artistas ou capas de
terceiros. A arte-base deve ser sem texto; titulo, subtitulo, autor, contracapa,
lombada, QR Code e elementos obrigatorios devem ser compostos localmente.

O resultado precisa ser profissional em miniatura e em tamanho completo. Nao
escalar uma estetica repetitiva, decorativa ou fraca apenas porque o arquivo tem
dimensoes tecnicamente validas.

## Arquivo sem orelhas

Ordem do arquivo externo unico, da esquerda para a direita:

```text
sangria | contracapa | lombada | capa | sangria
```

Para planejamento, usando `W` como largura fechada do livro, `H` como altura
fechada e `S` como a largura oficial da lombada:

```text
largura total = W + S + W + 10 mm
altura total  = H + 10 mm
```

Os 10 mm representam sangria de 5 mm em cada borda externa. A formula nao
substitui o gabarito UICLAP, pois `S` deve vir do Portal apos o miolo final.

## Arquivo com orelhas

Ordem do arquivo externo unico, da esquerda para a direita:

```text
sangria | orelha esquerda | contracapa | lombada | capa | orelha direita | sangria
```

Use duas orelhas de mesma largura. A UICLAP informa faixa de 5 a 10 cm por
orelha; no editor do Portal aparecem as opcoes de 5, 7 e 10 cm. Para
planejamento, usando `F` como largura de cada orelha:

```text
largura total = F + W + S + W + F + 10 mm
altura total  = H + 10 mm
```

Nao derive automaticamente uma capa com orelhas de uma capa sem orelhas. Ative
`Tem orelha?` no Portal, use o gabarito correspondente e confira as dobras no
visualizador 3D. A UICLAP informa que a face interna da capa nao recebe imagem
nem texto; trate a arte externa e qualquer especificacao de dobra conforme o
template disponibilizado no Portal.

## Sangria, margem e reservas obrigatorias

- Fundo e imagens de borda devem invadir 5 mm de sangria em todas as bordas.
- Titulos, nomes, logotipos e outras informacoes essenciais devem ficar pelo
  menos 10 mm para dentro da linha de corte.
- Reserve na contracapa a area do codigo de barras interno: 7 x 2 cm, na
  posicao indicada pelo Portal. A orientacao oficial informa 1 cm acima da
  margem inferior e 1 cm a esquerda da dobra da lombada ou grampo.
- Se o ISBN for informado no Portal, a plataforma gera codigo adicional de
  7 x 5 cm acima do codigo interno. Nao desenhar texto ou imagem nessa area.
- O uso do logo UICLAP e opcional; quando usado, a plataforma o oferece para
  capa ou lombada, nao para a contracapa.

## Formato e limites verificados

- Capa externa: JPG, ate 50 MB.
- Resolucao: minimo de 300 DPI; 600 DPI e o alvo recomendado pela UICLAP.
- Largura maxima da capa: 43 cm.
- A capa e o miolo sao uploads distintos.
- A plataforma informa que a lombada impressa exige ao menos 60 paginas; abaixo
  disso o livro e grampeado. Nao assumir texto de lombada sem conferir o caso.

## Fluxo obrigatorio por livro

1. Finalizar o miolo e registrar caminho, formato, papel e paginas.
2. Fazer upload do miolo no Portal e baixar o Guia de Tamanho de Capa/SVG.
3. Registrar as medidas oficiais e o hash do miolo em metadados do piloto.
4. Criar ou selecionar uma arte-base sem texto, unica para aquela obra.
5. Compor localmente a frente, contracapa, lombada e, se aplicavel, orelhas.
6. Exportar JPG limpo e preview separado com guias; nunca enviar o preview.
7. Fazer upload, conferir enquadramento, dobras, area de barras, logo e leitura
   no visualizador 3D da UICLAP.
8. Reenviar a arte se a plataforma mostrar conflito. Somente marcar
   `pronta_para_upload` depois dessa validacao e de revisao humana.

## Fontes oficiais consultadas em 2026-07-21

- UICLAP Suporte. [Capa: formato, tipo de arquivo e material](https://suporte.uiclap.com/support/solutions/articles/67000705782-capa-formato-tipo-de-arquivo-e-material).
- UICLAP Suporte. [Capa: do Miolo ao Gabarito, com Sangria e Margem de Seguranca](https://suporte.uiclap.com/support/solutions/articles/67000747899-capa-do-miolo-ao-gabarito-com-sangria-e-margem-de-seguranca).
- UICLAP Suporte. [Upload da capa](https://suporte.uiclap.com/support/solutions/articles/67000705794-upload-da-capa).
- UICLAP Suporte. [Como fazer e publicar a capa com orelha?](https://suporte.uiclap.com/support/solutions/articles/67000556802-como-fazer-e-publicar-a-capa-com-orelha-tutorial-).
- Blog UICLAP. [Criacao de capa com as informacoes geradas pelo Portal](https://blog.uiclap.com/guia-como-criar-a-capa/).
