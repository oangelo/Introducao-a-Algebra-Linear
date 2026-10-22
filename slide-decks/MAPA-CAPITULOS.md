# Mapa dos Capítulos — Introdução à Álgebra Linear

Camada intermediária: **acima do slide, abaixo do storyboard.** Aqui se decide *o que vai em
cada capítulo e onde cada conceito nasce* — não quantos slides, nem em que ordem interna.

**Objetivo declarado:** clareza do que entra em cada fase e **zero repetição entre fases**.

Base: [`AGENTS.md`](AGENTS.md) (contrato) · [`HISTORIA.md`](HISTORIA.md) (fio condutor) ·
[`ESTRATEGIA.md`](ESTRATEGIA.md) (desenho)

---

## 1. A regra que resolve repetição

> **R1 — Um conceito tem um dono.** Um único capítulo o **introduz**. Todos os outros o
> **usam**, sem redefinir.

> **R2 — Revisão é permitida, reensino não.** Quando um capítulo toca num conceito de fase
> anterior, ele aparece como **ferramenta já conhecida** (uma linha de retomada, não uma
> definição nova).

> **R3 — A pergunta do capítulo é o critério de pertinência.** Se um tópico responde à
> pergunta de outro capítulo, ele está no capítulo errado.

---

## 2. Tabela de posse dos conceitos

Conceitos que aparecem em mais de um capítulo —, os que geram repetição se ninguém decidir.

| Conceito | **Dono** (introduz) | Usa, sem reensinar |
|---|---|---|
| operações elementares / escalonamento | **F1** | F2 (cálculo de det), F5 (base de núcleo e posto) |
| matriz inversa (cálculo) | **F1** | F4 (inversa como transformação que desfaz) |
| critério de invertibilidade (\(\det \neq 0\)) | **F2** | F4 (transformação reversível), F6 (equação característica) |
| não comutatividade | **F1** | F4 (ordem da composição) |
| determinante | **F2** | F3 (det \(3\times3\) no produto vetorial), F4 (fator de área/volume), F6 (equação característica) |
| vetor, soma, multiplicação por escalar | **F3** | F5 (generaliza para espaço abstrato) |
| norma, distância, ângulo | **F3** | F4 (quanto uma transformação estica) |
| leitura geométrica de sistema linear | **F3** | — (F1 resolve algebricamente; F3 interpreta) |
| transformação linear / matriz padrão | **F4** | F6 (autovetor de uma transformação) |
| núcleo e imagem (geométrico) | **F4** | F5 (formaliza como subespaço e dá dimensão) |
| subespaço, span, independência | **F5** | F6 (autoespaço) |
| base, coordenadas, dimensão | **F5** | F6 (base de autovetores) |
| posto e nulidade | **F5** | F6 (multiplicidade, quando não diagonaliza) |
| autovalor / autovetor | **F6** | — |

---

## 3. Os seis capítulos

### Fase 1 — Sistemas e Matrizes
**Gabinete:** fantasia medieval (narração pronta: `scripts/matrizes_e_sistemas.md`)

- **Pergunta:** *dá para resolver?*
- **Entra:** matriz como tabela de coeficientes; operações elementares; matriz aumentada;
  escalonamento; classificação (sistema possível determinado / possível indeterminado /
  impossível); tipos especiais (diagonal, triangular, simétrica, identidade); cálculo da
  inversa por escalonamento; produto de matrizes e não comutatividade.
- **Não entra:** determinante (nem como atalho para saber se há solução); as palavras *posto*
  e *nulidade*; leitura geométrica do conjunto-solução; transformação linear.
- **Tópicos de exercício:** `sistemas-lineares`, `eliminacao-gaussiana`,
  `propriedades-matriciais`, `matrizes-inversas`
- **Lição do jogador:** SPD/SPI/SI — distinguir é habilidade, não fracasso. *Dúvida honesta
  > resposta inventada.*
- **Cena:** a guilda e o mercador de Portoveloz.
- **Herda:** nada. **Entrega:** escalonamento e inversa.

### Fase 2 — Determinantes
**Gabinete:** cyberpunk (narração pronta: `scripts/determinantes.md`)

- **Pergunta:** *dá para voltar?*
- **Entra:** determinante como número; expansão em cofatores; propriedades (troca de linhas
  muda o sinal, escalar multiplica, soma de múltiplo não altera); efeito das operações
  elementares; \(\det = 0 \iff\) singular; regra de Cramer.
- **Não entra:** a interpretação geométrica de área e volume **como conteúdo** — ela é da
  Fase 4. Área entra no máximo como motivação de uma linha.
- **Tópicos de exercício:** `determinantes-cofatores`, `determinantes-reducao`,
  `propriedades-determinantes`, `regra-cramer`
- **Lição do jogador:** reversibilidade. Há erro que se desfaz e decisão que colapsa o espaço.
- **Cena:** o hacker / a megacorporação numérica.
- **Herda:** escalonamento. **Entrega:** critério de invertibilidade.

> ⚠️ **Conflito atual:** a narração de determinantes já entrega área e volume, que são
> conteúdo da Fase 4. É repetição a corrigir no roteiro, não só no slide.

### Fase 3 — Vetores Euclidianos
**Gabinete:** FPS *(gênero sugerido — decidir no storyboard)*

- **Pergunta:** *onde estou?*
- **Entra:** vetor em \(\mathbb{R}^2\) e \(\mathbb{R}^3\); soma e escalar; norma e distância;
  produto escalar, ângulo, ortogonalidade, projeção; produto vetorial; retas e planos; e a
  **leitura geométrica** dos sistemas da Fase 1 (interseção de retas e planos).
- **Não entra:** espaço vetorial abstrato (F5); base arbitrária (F5); transformação (F4).
- **Tópicos de exercício:** `vetores`, `norma-e-distancia`, `ortogonalidade`,
  `produto-vetorial`, `retas-e-planos`, `geometria-sistemas-lineares`
- **Lição do jogador:** progresso se mede por distância, não por velocidade. Esforço grande
  na direção errada afasta.
- **Cena:** a mira, a direção do tiro.
- **Herda:** matrizes como ferramenta de resolução. **Entrega:** a geometria do espaço.

> ⚠️ **Ponto delicado:** `geometria-sistemas-lineares` é o único tópico que reabre a Fase 1.
> Ele **só** se justifica se for geométrico (o que cada classificação SPD/SPI/SI *desenha* em
> retas e planos). Se virar resolução de sistema outra vez, é repetição — sai da fase.

### Fase 4 — Transformações Lineares
**Gabinete:** plataforma com gravidade variável *(sugerido)*

- **Pergunta:** *o que ela faz com o espaço?*
- **Entra:** transformação linear como função que preserva soma e escalar; matriz padrão;
  rotação, reflexão, escala, cisalhamento, projeção; composição e **ordem**; inversa como
  desfazer; determinante como fator de área; núcleo e imagem **geometricamente** — o que
  colapsa numa dimensão a menos.
- **Não entra:** base arbitrária e mudança de base (F5); diagonalização e autovalor (F6).
  As palavras *posto*, *nulidade* e *autoespaço* não aparecem.
- **Tópicos de exercício:** `transformacoes-lineares`, `aplicando`, `combos-e-reversoes`
- **Lição do jogador:** hábito atômico. Ninguém muda de uma vez: \(T = T_3\circ T_2\circ T_1\).
  E a ordem importa, porque matrizes não comutam.
- **Cena:** o mundo que se deforma sob os pés.
- **Herda:** vetores, determinante, inversa, não comutatividade. **Entrega:** a ação da matriz
  sobre o espaço.

### Fase 5 — Espaços Vetoriais
**Gabinete:** construção / estratégia *(sugerido)*

- **Pergunta:** *de que o espaço é feito?*
- **Entra:** axiomas; subespaço; combinação linear e span; independência linear; base;
  coordenadas; dimensão; posto e nulidade; teorema do posto.
- **Não entra:** produto interno geral; autovalor; aplicações fora do escopo.
- **Tópicos de exercício:** `espacos-vetoriais-reais`, `subespacos`, `independencia-linear`,
  `coordenadas-e-bases`, `dimensao-posto-nulidade`
- **Lição do jogador:** escolher a base é escolher o que carregar. Poucos elementos geram
  muito espaço; dimensão é o mínimo necessário.
- **Cena:** a base construída, o que se escolhe levar.
- **Herda:** vetores (não reensina soma nem escalar), núcleo e imagem geométricos da F4.
  **Entrega:** a estrutura do espaço.

> ⚠️ **Conflito atual:** `propriedades-matriciais` (F1) e `espacos-vetoriais-reais` (F5)
> listam praticamente as mesmas propriedades — uma para matrizes, outra para espaço abstrato.
> A F5 deve apresentar os axiomas como **generalização do que já se viu**, em uma tabela de
> correspondência, e não como lista nova.

### Fase 6 — Autovalores e Autovetores
**Gabinete:** corrida *(sugerido)*

- **Pergunta:** *o que ela não consegue mudar?*
- **Entra:** autovalor e autovetor; equação característica; multiplicidade algébrica e
  geométrica; diagonalização; quando **não** diagonaliza.
- **Não entra:** Jordan; SVD; aplicações avançadas.
- **Tópicos de exercício:** `autovalores-e-autovetores`, `diagonalizacao`
- **Lição do jogador:** o que não muda quando tudo muda. Identidade sob transformação.
- **Cena:** a reta em que o carro não derrapa.
- **Herda:** determinante (equação característica), transformação. **Entrega:** fecha o fio.

---

## 4. Repetições que este mapa resolve

| Onde | O que se repete | Resolução |
|---|---|---|
| Narração F2 vs F4 | área e volume | F2 só motiva; conteúdo geométrico é F4 |
| `geometria-sistemas-lineares` (F3) vs F1 | resolução de sistema | F3 só interpreta geometricamente |
| `propriedades-matriciais` (F1) vs `espacos-vetoriais-reais` (F5) | lista de propriedades | F5 generaliza por tabela de correspondência |
| Narrativas F1 (medieval), F2 (cyberpunk) e decks (cyberpunk) | gênero | fliperama: cada fase é um gabinete |
| Decks F5: `espaco-vetorial-pt1`, `pt2`, `espacos` | mesmo conteúdo, três vezes | decidir a fonte de verdade antes de migrar |

---

## 5. O que este mapa não decide

Fica para o storyboard, fase por fase: ordem interna dos tópicos, quais slides existem, onde
entra a cena, quanto texto cada slide aceita, quais diagramas são SVG e quais são canvas.
