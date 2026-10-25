# Storyboard — Capítulo 1 · Como se sabe que algo funciona

O capítulo de abertura: **10 telas**, uma imagem gerada e uma frase por tela, antes do primeiro
portão. É o único bloco do curso em que o slide não carrega matemática nenhuma — ele carrega o
instrumento com que o aluno vai julgar o resto.

Este documento é o contrato de implementação. A prosa está em
[`CAPITULO-1.md`](CAPITULO-1.md); as imagens, em `img/`.

---

## 0. O que é uma cartela (a definição que faltava)

Uma cartela é **uma tela inteira** com exatamente quatro coisas:

1. **uma imagem** (a cena, Camada B, gerada e marcada como fabricada);
2. **uma frase** (uma oração, no canto inferior esquerdo, sobre a área escura);
3. **a faixa de HUD** (fina, no topo: `CAPÍTULO 1 · O INSTRUMENTO` e `0/6 chaves`);
4. **nada mais.**

Uma cartela **não tem**: título, bullet, fórmula, número, legenda de figura, crédito de imagem
visível durante a leitura, ou segunda frase. Se precisar de duas frases, são duas telas.

**Por que a cartela é a unidade do capítulo 1 e não a fase.** O capítulo 1 não tem tópico de
exercício — não há exercício para resolver no quadro. Sem tópico, o HUD de fase não tem o que
mostrar. Então a unidade vira a **batida narrativa**: uma tela, um passo do argumento.

**Por que a frase fica embaixo à esquerda.** Todas as dez imagens foram compostas com a área
inferior esquerda escura e vazia para isso. A frase não fica dentro de uma caixa: ela fica
sobre a imagem, em branco, na VT323. Se a imagem não tiver área escura ali, a imagem está
errada — não a caixa.

**Orçamento de texto do capítulo inteiro: 10 frases.** Nenhuma tela tem duas.

---

## 1. O arco em quatro atos

O capítulo não é uma lista de dicas: é um homem errando o método antes de acertar.

- **Ato 1 · a anedota (Q01–Q03)** — ele tem uma teoria, ela funciona uma vez, e ele conclui que
  funciona. Aqui o aluno se reconhece.
- **Ato 2 · o instrumento (Q04–Q06)** — três perguntas que desmontam a anedota: comparar com
  quem, mudar uma coisa só, ter quem não mudou.
- **Ato 3 · o caso (Q07–Q09)** — o mesmo erro, feito por cientistas: um experimento real que
  virou livro e não sobreviveu à repetição. Volta, dados, significância.
- **Ato 4 · o fecho (Q10)** — o caderno fecha, a tela continua acesa, e o capítulo entrega a
  ponte para a Fase 1 em uma linha.

**A virada é Q03.** "Funcionou uma vez" é o que todo mundo chama de evidência. Se o aluno não
leva Q03, o resto do capítulo é decoração.

---

## 2. Os dez quadros

### Q01 · `img/c1-teoria.png`
**FRASE:** *Todo mundo tem uma teoria de como jogar melhor.*
**A imagem mostra:** quarto escuro à noite, visto por trás; um jovem sentado no chão diante do
monitor aceso, controle na mão. Cabos no chão, luz fria da tela nas paredes, luz âmbar no piso.
**Por que essa imagem:** é o grau zero — o jogador sem método. Nada na cena diz que ele está
errado, e é isso: a cena apresenta a convicção, não o erro.
**Transição para Q02:** a frase afirma que ele tem uma teoria; a próxima diz qual é.

### Q02 · `img/c2-madrugada.png`
**FRASE:** *A dele era virar a noite.*
**A imagem mostra:** a mesma sala, mais tarde. Ele caído com a cabeça sobre os braços em cima da
mesa, caneca vazia, uma mancha escura ao lado, o monitor ainda aceso. Não há relógio na cena.
**Por que essa imagem:** a teoria dele não é uma ideia, é um comportamento. A aula mostra o
comportamento porque é o que o aluno também faz.
**Transição:** Q03 é a consequência, e é onde o capítulo arma a pegadinha.

### Q03 · `img/c3-vitoria.png`
**FRASE:** *Funcionou uma vez. Isso não é evidência.*
**A imagem mostra:** ele de costas, os dois braços erguidos diante da tela azul do gabinete, que
mostra WIN! em branco — texto incidental da cena, permitido. **Texto explicativo** é que não entra
em imagem: frase, legenda ou parágrafo vão no slide em HTML.
**Por que essa imagem:** o gesto de vitória é o momento em que **qualquer pessoa** conclui a
causa. A imagem tem que ser comemorativa, porque a frase tem que doer.
**Nota:** o gesto é de costas, sem rosto — o triunfo é do aluno, não de um personagem.
**Transição:** a virada. Daqui em diante o capítulo não conta história, ensina a desmontar.

### Q04 · `img/c4-comparar.png`
**FRASE:** *Para saber, tem que comparar.*
**A imagem mostra:** díptico de plataforma separado por uma barra, o mesmo salto em dois quadros —
à esquerda o boneco de pé no penhasco, com o bloco "?" ao lado; à direita o mesmo boneco caindo
no vão, entre os peixes.
**Por que essa imagem:** dois desfechos na mesma tela **são** o instrumento 1. O que a imagem
mostra não é o resultado, é a **divisória**: sem as duas metades lado a lado não existe
comparação, e é por isso que a barra é preta e grossa.
**Como foi feita:** gerada (23/out, `raw/c4-comparar.png`) e ajustada por código
(`ajustar-luz.py`, gama nas sombras). **Seed não registrada** — a cena foi aprovada antes do
manifesto passar a exigir seed por linha.
**Transição:** se comparar é o instrumento, comparar errado é a armadilha seguinte.

### Q05 · `img/c5-isolar.png`
**FRASE:** *Uma coisa de cada vez.*
**A imagem mostra:** um único salto, muitos desfechos. Do boneco no penhasco saem trajetórias
tracejadas que caem na água; uma só, laranja, chega à plataforma.
**Por que essa imagem:** a mesma cena com desfechos diferentes só existe se **uma coisa** mudou
entre as tentativas. As trajetórias em paralelo são o instrumento 2 visto de lado: quem mexeu em
tudo de uma vez não sabe o que causou o quê.
**Como foi feita:** cena gerada (`raw/c5-isolar.png`) e as trajetórias desenhadas por código
(`img-gen/isolar-arcos.py`) — parábola de difusão sai torta e não fecha no alvo. **Seed não
registrada.**
**Transição:** falta a régua — comparar com quem não mudou nada.

### Q06 · `img/c6-dois-jogadores.png`
**FRASE:** *Alguém que não mudou nada.*
**A imagem mostra:** díptico rasgado com a **mesma pessoa em dois tempos** — jovem à esquerda,
idoso à direita —, de costas, no mesmo gabinete de fliperama, com GAME OVER nas duas telas; um
relógio analógico dentro do rasgo; caderno em branco de um lado, caderno gasto do outro.
**Por que essa imagem:** é o controle que o aluno **usa** — ele contra ele mesmo —, e é justamente
por isso que não serve: o corpo envelheceu, o resultado não mudou. A régua de verdade está na sala,
entre os colegas, e a cartela a deixa de fora de propósito.
**Nota de geração:** sem referência de personagem e com negativo anti-clone — o modelo já
devolveu três homens idênticos nesta cena.
**Transição:** com o instrumento completo, o capítulo volta ao começo — mas agora com cientistas.

### Q07 · `img/c7-palco.png`
**FRASE:** *O que funciona não é o que se divulga.*
**A imagem mostra:** díptico rasgado com o **mesmo palco** nas duas metades. À esquerda o palco
está ocupado — um homem de costas ergue um livro grosso como troféu, quatro pessoas de costas
olham para ele. À direita o mesmo palco está vazio de gente e carrega só uma pilha de maços alta
como uma pessoa, sem ninguém segurando e sem ninguém na sala.
**Por que essa imagem:** a assimetria é o argumento, e ela é de **atenção**, não de objeto: o
livro tem plateia, a evidência não tem. O palco idêntico é o que torna a comparação justa.
**Nota:** o livro **não tem título legível**, por regra. É "um livro", não um livro
identificável — a identificação vem da fala do professor, com a referência.
**Transição:** se a fama não decide, o que decide? Quantidade — e a C8 mostra a quantidade.

### Q08 · `img/c8-pilhas.png`
**FRASE:** *Uma noite é anedota. Trinta são dados.*
**A imagem mostra:** díptico rasgado da mesma mesa e da mesma pessoa, de costas. À esquerda a
mesa limpa — caderno fechado, uma folha solta, o abajur aceso. À direita a mesma mesa soterrada:
pilhas na mesa, papel no chão, a lâmpada quase encoberta.
**Por que essa imagem:** a pilha tem **altura** — o instrumento 4 é quantidade, e quantidade
precisa ser vista, não lida. O mesmo enquadramento nas duas metades transforma a diferença em
número, não em cenário.
**Nota de geração:** gerada sem corte e partida por código (`img-gen/corte-tempo.py`), porque
raio desenhado por difusão sai torto e não alinha as metades — e aí deixa de ser "a mesma pessoa".
**Transição:** trinta noites ainda podem ser trinta noites de sorte.

### Q09 · `img/c9-colunas.png`
**FRASE:** *A diferença é maior do que o acaso?*
**A imagem mostra:** caderno aberto visto de cima, sob luz de luminária; três fileiras de marcas
de contagem em cada página, em grupos de cinco. Perto da lombada, uma marca curta avulsa — a
diferença — circulada a lápis vermelho.
**Por que essa imagem:** é o único lugar do capítulo em que o aluno **vê** uma diferença
pequena — e a frase pergunta se ela é real. A resposta (d = 0,04, IC contendo o zero) é dita em
sala, com a referência na mão; a imagem não pode carregar número.
**Nota de geração:** a cena (caderno vazio, luz) é gerada; **as marcas e o círculo são desenhados
por código** (`img-gen/marcas-contagem.py`). O modelo não conta: pedido para desenhar "dois blocos
quase iguais", ele devolve ~145 riscos por bloco e circula um grupo qualquer — a diferença deixa
de ser legível. Com o código, a diferença é exatamente duas marcas.
**Transição:** o instrumento está completo. Falta dizer para que ele serve fora deste capítulo.

### Q10 · `img/c10-fecho.png`
**FRASE:** *Antes de saber o que funciona, saiba como se sabe.*
**LINHA MENOR, embaixo:** *Duas coisas que sempre andam juntas são uma só.*
**A imagem mostra:** uma montagem em quatro painéis. No alto, o jogador de capuz, de costas, no
degrau mais alto de um pódio, erguendo um troféu; salão vazio, dois holofotes, nenhuma plateia.
Embaixo, três painéis do mesmo tamanho — **dormindo** na cama, **estudando** sob o abajur,
**treinando** numa escadaria ao amanhecer — presos por um colchete, formando a base do pódio.
**Como foi feita:** quatro cenas no **FLUX** (`flux3`, seeds 5501–5506, referência
`jogador-capuz.png`) e a montagem por código (`img-gen/podio.py`). Pedir "pódio com três cenas"
numa geração só devolve papa: o modelo não sustenta três cenas distintas num enquadramento. Cada
peça é gerada sozinha; o arranjo é layout, não conteúdo.
**O que a composição evita:** a primeira montagem punha o painel do **estudo** mais alto e mais
quente. O olho concluía "estudar foi o que ganhou o troféu" — atribuição que o capítulo acabou de
dizer que não se pode fazer. Na versão aprovada os três painéis têm o mesmo tamanho e se encostam:
são **um bloco**, não um ranking. É o desenho da variável confundida, não do mérito.
**Por que essa imagem:** o troféu existe e os três jeitos de chegar nele nunca apareceram
separados — é a pergunta "qual foi?" que fica sem resposta. O capítulo fecha no resultado e não na
explicação, que é o que a Fase 1 vai cobrar.
**Transição:** a linha menor é a **única** antecipação de matemática do capítulo inteiro. Ela
não ensina independência linear; ela deixa a palavra no ar para a Fase 1 cobrar.

---

## 3. Inventário de imagem

| Camada | Quantidade | Arquivos |
|---|---|---|
| Gerada (Camada B) | 10 | `c1-teoria` … `c10-fecho` |
| SVG (Camada A) | 0 | — |
| Total de telas | 10 | |

**Zero SVG** é consequência da premissa, não economia: o capítulo não tem fórmula nem número
verificável. Qualquer diagrama que aparecesse aqui seria o slide explicando — e quem explica é
o quadro.

**Rotina de imagem:** as dez passam pelo mesmo traço (contorno preto fechado, cor chapada, cel
shading), mesma paleta (azul-cinza, carvão, âmbar), mesma luz (tela fria à frente, lâmpada
quente na lateral). O gênero noir chega na Fase 1; aqui ainda é o quarto.

---

## 4. O que a Fase 1 herda deste capítulo

O aluno sai sabendo o que é **variável confundida** sem nunca ter ouvido o nome. A Fase 1 dá o
nome em matriz: dependência linear, posto, grau de liberdade. Ver
[`MAPA-CAPITULOS.md`](MAPA-CAPITULOS.md) e [`STORYBOARD-F1.md`](STORYBOARD-F1.md).

A frase de Q05 é o que a Fase 1 formaliza. A frase de Q10 é o que a Fase 1 cobra.

---

## 5. Estado

- [x] as dez imagens geradas, verificadas (sem rosto, sem texto legível, sem clone)
- [x] manifesto em `img-gen/cenas-cap1.tsv`
- [ ] as dez telas implementadas em Reveal
- [ ] a fala do professor de cada tela — **não vai no slide**

Ver em [`AGENTS.md`](AGENTS.md) §3 e §8.
