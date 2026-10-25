# img-gen — harness de imagem do curso

Gera as cenas da Camada B em lote, com o personagem fixo por **imagem de referência**.

Inspirado no que o Emm (scenario.com) descreveu ao fazer um quadrinho de 908 páginas com
personagens consistentes: **reference images, agents and a tight harness**. A ideia que vale
copiar não é a ferramenta dele — é a separação:

- o **agente** escreve o manifesto (texto, sem GPU);
- o **harness** executa em lote, com parâmetros travados;
- a **referência** é um arquivo, não uma descrição.

## Por que harness e não chamada solta

Cada chamada ao `qwen-image.sh` **para e religa o llama-cpp** (o modelo de chat ocupa ~25 GB
dos 24 GiB da 7900 XTX). Dezesseis cenas chamadas soltas = dezesseis ciclos, e o chat dos
agentes cai dezesseis vezes.

`gen.sh` faz um ciclo só: para no começo, gera tudo com `--no-cycle`, religa no fim — com
`trap`, inclusive se for interrompido ou der erro no meio.

## Uso

```bash
# no Oráculo
cd /mnt/Volatil/sdcpp
./gen.sh cenas.tsv                 # todas
./gen.sh cenas.tsv --only f1       # só o que começa com "f1"

# de volta no agente
../img-gen/fetch.sh                # traz os PNG de out/ para img/
```

## O manifesto (`cenas.tsv`)

Tab-separado, uma cena por linha:

| coluna | o que é |
|---|---|
| `name` | nome do arquivo de saída, sem extensão. Use o nome do quadro (`f1-02`, `c7-palco`) |
| `model` | `turbo` (padrão, composição limpa) ou `flux3` (mais rico, arrisca pseudo-texto) |
| `w` `h` | resolução. Teto ~1,4 MP; `1152x864` é o formato de slide |
| `seed` | **fixo por cena**. Mudar a seed muda o desenho; se a cena ficar boa, a seed é o que permite regerar |
| `ref` | `y` passa `jogador-capuz.png` como referência; `n` não passa |
| `prompt` | descrição da cena, em inglês. **Nunca** pede texto |
| `extra_negativo` | negativo específico da cena, somado ao base |

**Quando `ref=y`:** só quando o jogador aparece. Referência de personagem injeta o personagem —
passar num plano de objeto devolve o moletom no meio de uma pilha de papéis.

## As regras que não são negociáveis

1. **Texto explicativo nunca vem do modelo; texto incidental da cena pode ficar.** O que o
   negativo base proíbe é `paragraphs, captions, subtitles, watermark, legible paragraphs` —
   texto que **explica**. Palavra que faz parte do objeto (`WIN!` numa tela de fliperama,
   `GAME OVER` num gabinete) é decoração do cenário e pode ficar: é o que se vê na vida real.
   A fronteira é funcional: **se o texto precisa ser editado, traduzido ou atualizado, ele
   pertence ao slide em HTML** — dentro do PNG ele não se mantém. Se aparecer parágrafo,
   legenda ou frase explicativa, a imagem é **descartada**, não corrigida.
   **Símbolo se pede ao modelo, não se desenha por código**: a versão do "?" feita com spline em
   `interrogacao.py` saiu com bico, quina e espessura de plotter — geometria limpa não vira
   caligrafia. Se o símbolo for o assunto, o prompt pode pedi-lo (`?` não é palavra, e o negativo
   continua proibindo letra) — foi assim que a versão com interrogação na capa saiu boa.
   **Mas símbolo pode não ser o instrumento certo**: a Q10 acabou sem o "?" — o caderno com a
   interrogação dizia "há uma pergunta", e a montagem do pódio diz *qual* pergunta é. As duas
   versões estão em `descartados/`; a aprovada é a montagem.
2. **Nada de número, fórmula ou objeto matemático em imagem gerada.** Diagrama é SVG.
3. **O rosto não existe.** Sombra da aba, costas, silhueta. É o que mantém a pessoa a mesma.
4. **Prompt não menciona a história do curso.** A cena mostra o **problema**, não a metáfora
   dele. Se a legenda precisar explicar a imagem, a imagem está errada.
5. **Seed é registro.** Se uma cena for aprovada, a seed dela não muda mais — é o que permite
   regerar idêntico quando o modelo for trocado.
6. **Peça é modelo, montagem é código.** Pedir "um pódio com três cenas dentro" numa geração só
   devolve papa: o modelo não sustenta várias cenas distintas num enquadramento. Gere cada cena
   sozinha (`cenas-podio*.tsv`) e componha em Python (`podio.py`). A montagem é layout, não
   conteúdo — não põe nada que a cena não tenha.
7. **A primeira cena do lote falha por cold start.** Depois do `app.stop llama-cpp`, o primeiro
   `flux3` morre em `graph failed during weight preparation` — não é o prompt: a mesma seed passa
   na segunda tentativa. `gen.sh` retenta uma vez (`for tentativa in 1 2`); sem isso, todo lote
   perde a primeira cena.

## O que a geração ensinou (out/2026)

Cinco coisas que custaram ~40 imagens para aparecer:

1. **O estilo vem na PRIMEIRA frase.** No fim do prompt ele é decoração: em cena de objeto o
   modelo tem prior fotográfico e devolve foto. `Drawn illustration, comic book line art: clean
   black contour outlines, flat colour areas, shading in a few hard cel steps` abre toda linha
   do manifesto.
2. **Nome de estilo não funciona; meio físico funciona.** "Uncanny X-Men era" e "Image Comics
   1990s" viram pintura digital com clima de HQ. "Contorno preto fechado, cor chapada, cel
   shading" vira desenho. Descreva o objeto impresso, não a referência cultural.
3. **Referência de personagem clona.** "The same young man" + `-r` devolveu **três homens
   idênticos**. Escreva "one single man" e ponha `multiple people, duplicated figures, clone` no
   negativo. Em cena com duas pessoas de verdade, `ref=n` e descreva as duas.
   E a referência às vezes **apaga** o personagem: no f1-02 ele desapareceu duas vezes com `-r`.
4. **Cena sem personagem precisa de forma, não de luz.** Caderno, pilha de papéis e estante
   saíram fotorrealistas até o prompt virar "duas formas planas com contorno grosso, sem textura,
   sem brilho". Objeto pede geometria; luz pede pintura.
5. **Planta azul é foto por natureza.** "Blueprint" traz render com carimbo e pseudo-texto.
   Peça **papel branco com linhas pretas** — aí é desenho.

## O traço e os personagens

**Traço C** (decidido out/2026 comparando três clássicos noturnos): contorno preto fechado, cor
chapada, cel shading em poucos degraus. Um só no curso inteiro — o gênero muda cenário e paleta,
não a linha.

Duas referências, porque são dois lugares:

- `img/personagens/jogador-quarto.png` — o jogador no quarto (capítulo 1, o grau zero, sem gênero).
- `img/personagens/personagem-noir.png` — o detetive do P1, chapéu e sobretudo.

**Regra:** o rosto não existe em nenhum dos dois. É a assinatura que sobrevive à troca de
figurino. Cópias de trabalho no Oráculo em `/mnt/Volatil/sdcpp/ref/`.

## Quando o gerador não dá conta: código depois da geração

Duas coisas o modelo **não** faz, e insistir nele custa imagens: **contar** e **alinhar as duas
metades de um rasgo**. Nesses casos a cena é gerada uma vez, sem o detalhe impossível, e o
detalhe entra por código:

| script | o que resolve | por que não no prompt |
|---|---|---|
| `corte-tempo.py` | parte a imagem em díptico rasgado: junta serrilhada, metades deslocadas e giradas | raio desenhado por difusão sai torto e em posição aleatória; as metades não alinham e "a mesma pessoa nos dois tempos" deixa de ser verdade |
| `marcas_contagem.py` | desenha marcas de contagem (tallies) numa página de caderno gerada vazia, e circula só a diferença | o modelo não conta: devolve ~145 riscos por bloco e circula um grupo qualquer, então a "diferença pequena" some |
| `interrogacao.py` | escreve um "?" a lápis na capa do caderno (Q10) | pedir "ponto de interrogação escrito na capa" devolve rabisco ilegível, e texto ilegível é descartado em Camada B |
| `fecho.py` | duas linhas idênticas riscadas na capa (versão anterior da Q10) | o difusor nunca repete traço; duas linhas "idênticas" saem apenas parecidas |

Regra geral: **gerar o que o modelo sabe fazer (luz, objeto, enquadramento) e desenhar o que ele
não sabe (contagem, alinhamento, geometria exata)**. O resultado conta como Camada B, mas a nota
de geração da cena precisa dizer qual parte é código — sem isso, quem regerar a cena perde o
detalhe e não sabe por quê.

## O que a geração ensinou sobre corrigir

**Corrigir um item, não reescrever a cena.** Numa cartela já aprovada, trocar a frase inteira do
prompt para remover um objeto errado devolveu composição nova — o personagem que estava atrás veio
para o centro e a cena inteira mudou de sentido. Mudar **só** o objeto (e pôr o intruso no
negativo) manteve o desenho e resolveu.

**"Ignorar" é postura, não olhar.** "Ninguém olha para ele" produz gente de frente, parada, e lê
como atenção. O que funciona é **para onde o corpo aponta**: figuras de costas, viradas para o
outro lado, e o objeto atrás delas. De costas a assinatura (sem rosto) sai de graça.

**Posição relativa reescreve a cena.** "Atrás do par" trouxe o sujeito para a frente, centralizado.
Se a posição é o argumento, diga o **ângulo de câmera** ("atrás do ombro direito dele"), não a
relação entre pessoas.

**Objeto tem anatomia, e o modelo erra a que não foi dita.** "Caderno aberto visto de cima" com
"espiral na borda esquerda" devolveu a lombada na **borda externa** — fisicamente impossível: num
caderno aberto a espiral fica na **dobra central**, e as duas bordas externas são papel solto. Se
uma peça do objeto pode ir para o lugar errado, diga onde ela está *e* onde ela não está
("binding on the outer edge" no negativo), como se faz com o rosto.

## Checklist antes de aprovar uma cena

- [ ] tem texto, número ou letra legível? → descartar
- [ ] o rosto aparece? → descartar
- [ ] o traço tem contorno preto e cor chapada, ou virou pintura/render? → refazer
- [ ] a mesma pessoa aparece repetida na cena? → refazer sem `-r`
- [ ] a cena é o problema, ou é decoração? → se é decoração, não entra
- [ ] a composição deixa espaço para a linha de texto do slide? → a legenda vive no canto
