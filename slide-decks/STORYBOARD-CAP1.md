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
**A imagem mostra:** a mesma sala, mais tarde. Ele caído sobre a mesa, caneca vazia, o relógio
de perfil (de propósito: o mostrador não aparece — número gerado é número errado).
**Por que essa imagem:** a teoria dele não é uma ideia, é um comportamento. A aula mostra o
comportamento porque é o que o aluno também faz.
**Transição:** Q03 é a consequência, e é onde o capítulo arma a pegadinha.

### Q03 · `img/c3-vitoria.png`
**FRASE:** *Funcionou uma vez. Isso não é evidência.*
**A imagem mostra:** ele de costas, os dois braços erguidos diante da tela estourada de branco.
**Por que essa imagem:** o gesto de vitória é o momento em que **qualquer pessoa** conclui a
causa. A imagem tem que ser comemorativa, porque a frase tem que doer.
**Nota:** o gesto é de costas, sem rosto — o triunfo é do aluno, não de um personagem.
**Transição:** a virada. Daqui em diante o capítulo não conta história, ensina a desmontar.

### Q04 · `img/c4-caderno.png`
**FRASE:** *Para saber, tem que comparar.*
**A imagem mostra:** caderno aberto, duas colunas traçadas a régua, ambas vazias. Lápis ao lado.
**Por que essa imagem:** as duas colunas vazias **são** o instrumento 1. A imagem é a pergunta
"comparado com quê?" antes de qualquer número existir.
**Transição:** se comparar é o instrumento, comparar errado é a armadilha seguinte.

### Q05 · `img/c5-semanas.png`
**FRASE:** *Uma coisa de cada vez.*
**A imagem mostra:** duas grades semanais lado a lado; à esquerda luas, à direita sóis; uma
única linha difere entre as duas.
**Por que essa imagem:** a diferença de uma linha é o instrumento 2 (isolar a variável) visto de
cima, sem texto. Quem mexeu em tudo não sabe o que causou o quê.
**Transição:** falta a régua — comparar com quem não mudou nada.

### Q06 · `img/c6-dois-jogadores.png`
**FRASE:** *Alguém que não mudou nada.*
**A imagem mostra:** dois homens diferentes, de costas, cada um na sua mesa. Caderno novo à
esquerda, caderno gasto à direita.
**Por que essa imagem:** o grupo de controle é uma **pessoa que continua igual**, não uma
coluna. A imagem tem dois corpos porque a ideia é relacional.
**Nota de geração:** sem referência de personagem e com negativo anti-clone — o modelo já
devolveu três homens idênticos nesta cena.
**Transição:** com o instrumento completo, o capítulo volta ao começo — mas agora com cientistas.

### Q07 · `img/c7-estante.png`
**FRASE:** *Virou livro. Não se repetiu.*
**A imagem mostra:** uma prateleira; um livro grosso com lombada dourada de pé, e ao lado uma
folha fina grampeada.
**Por que essa imagem:** a assimetria é o argumento. O livro vendeu; a replicação não.
**Nota:** a lombada **não tem título legível**, por regra. O livro é "um livro", não um livro
identificável — a identificação vem da fala do professor, com a referência.
**Transição:** se o livro não basta, o que basta? Volume.

### Q08 · `img/c8-pilhas.png`
**FRASE:** *Uma noite é anedota. Trinta são dados.*
**A imagem mostra:** mesa coberta por uma pilha alta de folhas soltas; uma mão apoiada no topo.
**Por que essa imagem:** a pilha tem **altura** — o instrumento 4 é quantidade, e quantidade
precisa ser vista, não lida.
**Transição:** trinta noites ainda podem ser trinta noites de sorte.

### Q09 · `img/c9-colunas.png`
**FRASE:** *A diferença é maior do que o acaso?*
**A imagem mostra:** página de caderno com dois blocos de marcas de contagem quase iguais, e
uma diferença pequena circulada a lápis vermelho.
**Por que essa imagem:** é o único lugar do capítulo em que o aluno **vê** uma diferença
pequena — e a frase pergunta se ela é real. A resposta (d = 0,04, IC contendo o zero) é dita em
sala, com a referência na mão; a imagem não pode carregar número.
**Transição:** o instrumento está completo. Falta dizer para que ele serve fora deste capítulo.

### Q10 · `img/c10-fecho.png`
**FRASE:** *Antes de saber o que funciona, saiba como se sabe.*
**LINHA MENOR, embaixo:** *Duas coisas que sempre andam juntas são uma só.*
**A imagem mostra:** o caderno fechado na mesa; ao fundo, a tela do jogo ainda acesa. Duas linhas
idênticas riscadas na capa.
**Por que essa imagem:** o capítulo fecha com o caderno fechado e o jogo ligado — o método
terminou, o jogo continua. A tela acesa é o próximo capítulo.
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
