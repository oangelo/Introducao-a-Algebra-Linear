# Visão Holística da História — Introdução à Álgebra Linear

Documento de desenho. Nada implementado.
**Branch:** `feature/slides` · **Data:** 2026-10-22

> Escrito depois da correção do professor: "a gente precisa ter uma visão holística da
> história, para não ficar as coisas desconectadas nem repetidas". Cota numérica de
> palavras/slides **não** entra aqui — o limiar é por matéria e se calibra no storyboard.

---

## 1. Diagnóstico: três ficções simultâneas

O curso conta três histórias em três gêneros, e elas não se reconhecem.

| Gênero | Marcas | Onde |
|---|---|---|
| **Fantasia medieval** | guilda, poções, grimório, arquimago, Portoveloz, dragão ancião, anões engenheiros, elfos economistas, gnomos programadores, dungeon, tesouro | `scripts/matrizes_e_sistemas.md`; 13 exercícios |
| **Cyberpunk** | "hackers do ciberespaço", megacorporações numéricas, Matrix, neon, backdoors, código-fonte, crash, infovias | `scripts/determinantes.md`; todos os 10 decks |
| **Arcade** | Jogador, Fase, Quest, Mini-Chefe, Chefe, XP, Ctrl+Z | `quiz/`, 28 exercícios, rótulos dos decks |

**Sobreposição:** 8 arquivos de exercício e 1 deck (`eliminacao_gaussiana.html`) contêm
marcas de medieval **e** cyberpunk ao mesmo tempo.

### Por que isso importa

Não é incoerência de gosto — é incoerência de **promessa**. Cada moldura diz ao aluno para
que serve a matemática:

- fantasia → "isto serve para gerir inventário e negociar com mercadores"
- cyberpunk → "isto serve para quebrar criptografia e invadir sistemas"
- arcade → "isto é um jogo, e você é o jogador"

Nenhuma é falsa, mas elas competem. E no modelo definido pelo professor — slide como
**âncora de estado** para o aluno que se distraiu — uma âncora que aponta para três mundos
diferentes não ancora nada.

O sintoma aparece na narração de abertura: o aluno ouve um arquimago na Fase 1, um hacker
na Fase 2, e abre um slide com "DEV LOG — Desenvolvedores Originais".

---

## 2. A ficção unificadora: o fliperama

A saída não é escolher uma das três e jogar as outras fora — é **hierarquizar**.

> **O curso é um fliperama. Cada fase é um gabinete.**

O Jogador entra no fliperama ("Pronto, Jogador 1?"), escolhe um gabinete e joga. Cada
gabinete tem seu gênero, sua paleta e sua voz — um é RPG de fantasia, outro é cyberpunk,
outro é arcade puro. **O arcade não é um quarto gênero: é o saguão que contém os outros.**

Isso resolve o problema sem descartar material:

- a narração de fantasia da Fase 1 vira a voz do **gabinete 1**;
- a narração cyberpunk da Fase 2 vira a voz do **gabinete 2**;
- os decks param de ser cyberpunk "sem querer" e passam a ser cyberpunk **porque a Fase 2
  é um gabinete cyberpunk** — decisão, não acidente;
- as Fases 3 a 6 ganham gênero escolhido no storyboard, não herdado por acidente.

### A regra que decorre

> **Um gabinete, um gênero, do primeiro ao último slide da fase.**

Fronteira dura: nenhuma marca de outro gênero dentro do gabinete. O aluno pode trocar de
mundo, mas só na porta — nunca no meio da explicação. É isso que impede o arquivo de
exercício de misturar guilda com backdoor.

---

## 3. O fio condutor (a história que atravessa as seis fases)

Um fliperama com seis gabinetes ainda precisa de uma razão para o jogador ir de um ao
outro. A pergunta que atravessa o curso:

> **"O que este sistema faz com o espaço?"**

Cada fase responde um pedaço a mais, e o pedaço novo depende do anterior:

| Fase | Gabinete | O que acrescenta | A pergunta que fecha |
|---|---|---|---|
| 1 | Sistemas e Matrizes | a máquina: coeficientes, incógnitas, o que entra e o que sai | "dá para resolver?" |
| 2 | Determinantes | a máquina tem impressão digital: pode ser desfeita ou não | "dá para voltar?" |
| 3 | Vetores Euclidianos | o espaço onde a máquina age ganha distância, ângulo, direção | "onde estou?" |
| 4 | Transformações | a máquina **move** o espaço: estica, gira, projeta, achata | "o que ela faz com o espaço?" |
| 5 | Espaços Vetoriais | o espaço deixa de ser seta e vira estrutura: base, dimensão, núcleo | "de que o espaço é feito?" |
| 6 | Autovalores | há direções que a máquina não muda — só estica | "o que ela **não** consegue mudar?" |

**Por que esse fio funciona:** ele é o fio matemático real, não uma alegoria colada. A
sequência sistemas → determinante → vetores → transformações → espaços → autovalores é
exatamente a progressão de Anton, e a pergunta "o que este sistema faz com o espaço?" é a
que liga a Fase 2 (determinante = quanto o volume muda) à Fase 4 (a transformação age) à
Fase 6 (as direções invariantes). O aluno que guarda só a pergunta reconstitui o curso.

**E resolve o "repetido":** cada fase é uma resposta **nova** à mesma pergunta. Nada se
repete porque o objeto da resposta muda — máquina, impressão digital, espaço, movimento,
estrutura, invariante.

---

## 4. A camada do jogador — disciplina, dúvida e emoção

O professor pediu que a visão holística não ficasse superficial: juntar estratégias cognitivas
para vencer — disciplina, hábito, dúvida, problema emocional. A condição para isso não virar
pôster motivacional:

> **A lição só entra se for consequência do conceito daquela fase. A matemática é a
> metáfora, não o enfeite.**

Nada de "seja disciplinado". Disciplina não se prescreve; ela aparece como **propriedade
matemática** que o aluno vê funcionar.

| Fase | Conceito | A lição que o conceito já contém |
|---|---|---|
| 1 | sistema possível / impossível / indeterminado | Nem todo problema tem solução, e alguns têm infinitas. Distinguir isso é habilidade, não fracasso — **dúvida honesta vale mais que resposta inventada**. |
| 2 | \(\det A \neq 0 \iff A\) invertível | **Reversibilidade.** Há erro que se desfaz e decisão que colapsa o espaço. Antes de agir: dá para voltar? |
| 3 | norma, distância, direção | **Progresso se mede por distância, não por velocidade.** Esforço grande na direção errada afasta do objetivo. |
| 4 | composição de transformações | **Hábitos atômicos.** Ninguém muda de uma vez: \(T = T_3 \circ T_2 \circ T_1\). Pequenas operações que se compõem — e **a ordem importa**, porque matrizes não comutam. |
| 5 | base, dimensão, span | **Escolher a base é escolher o que carregar.** Poucos elementos geram muito espaço. Dimensão é o mínimo necessário — não o máximo suportável. |
| 6 | autovetor | **O que não muda quando tudo muda.** Identidade sob transformação: as direções que a máquina estica mas não desvia. |

### Os veículos (diegéticos, não palestra)

1. **Dica de tela de carregamento** — uma por fase, curta, no canto do slide de abertura.
   É o formato clássico do arcade: o jogo ensina enquanto carrega.
2. **Menu de pausa** — um slide de pausa no meio de cada fase: "PAUSA — como você está
   jogando?". Ali entram as perguntas de metacognição (o que você já sabe fazer sozinho? o
   que você está evitando?). Duas por fase, no máximo.

Nenhum dos dois é slide de conteúdo: são **estado do jogador**, não estado da matéria.

### O que essa camada não é

Não é a camada crítica dos cursos irmãos. Lá o eixo é social (Freire, herói como produto de
PR, tecnologia não neutra). Aqui o eixo é **metacognitivo**: como se aprende, como se
sustenta o esforço, como se lida com não saber. As duas convivem — são perguntas diferentes
— mas não se misturam no mesmo slide.

---

## 5. O DEV LOG dentro dessa estrutura

O DEV LOG ("Desenvolvedores Originais: Leibniz 1678, Cramer 1750") é a voz do
**desenvolvedor do gabinete** — quem programou aquela mecânica.

Mantido, ele diz: *"esta mecânica tem autor, e o autor é um gênio solitário"*.
Reenquadrado como **créditos do jogo**, ele diz: *"esta mecânica foi construída por muita
gente, e o nome na caixa é o que sobrou"*.

A segunda versão é mais interessante **e** mais verdadeira: Cramer publicou a regra, mas o
resultado já circulava; Gauss não inventou a eliminação; Grassmann foi ignorado em vida.
O DEV LOG pode mostrar isso — é changelog, e changelog tem bug, autor esquecido e dívida
técnica.

> **Proposta:** DEV LOG vira **créditos com dívida técnica** — quem construiu, quem ficou
> de fora, e o que ainda não funciona direito.

---

## 6. O que fica para o storyboard (próxima etapa)

A visão holística para aqui. O storyboard, fase por fase, define:

1. **Gênero e paleta do gabinete** (Fases 3–6 ainda não têm).
2. **Os tópicos de exercício** da fase e a ordem em que entram.
3. **A pergunta de cada tópico** — a versão local da pergunta do curso.
4. **Onde entra a cena** (a imagem gerada) e o que ela mostra.
5. **O limiar de texto daquele tópico** — calibrado aqui, não imposto de fora. Um tópico de
   definição formal aceita mais texto que um de intuição geométrica; o número sai do
   storyboard, não de uma regra global.

O storyboard é o artefato que o professor aprova antes de qualquer slide ser escrito.
