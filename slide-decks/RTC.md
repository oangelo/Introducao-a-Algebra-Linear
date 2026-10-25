# RTC — Slide Decks de Introdução à Álgebra Linear

Diagnóstico no padrão do pipeline dos repos Geometria Analítica e Cálculo Vetorial.
**Branch:** `feature/slides` · **Base:** `e16a71e` · **Data:** 2026-10-22

> Documento de diagnóstico. Não é plano de ação.

---

## 1. Inventário

10 decks monolíticos, 4.090 linhas de HTML no total (410 tags `<section>`), sem pasta por
capítulo e sem loader.

| Deck | Linhas | `<section>` | Fase | Título interno |
|---|---|---|---|---|
| `eliminacao_gaussiana.html` | 412 | 38 | 1 | Fase 1 - Eliminação Gaussiana |
| `propriedades.html` | 289 | 36 | 1 | Fase 1 - Aritmética e Propriedades |
| `inversas.html` | 333 | 26 | 1 | As Regras do Jogo |
| `determinante.html` | 489 | 43 | 2 | A Chave da Assinatura |
| `espacos-vetoriais-euclidianos.html` | 502 | 42 | 3 | Explorando o Espaço |
| `transformacoes.html` | 190 | 51 | 4 | Álgebra Arcade - Fase 4 |
| `espaco-vetorial-pt1.html` | 362 | 33 | 5 | As Leis do Universo (Parte 1) |
| `espaco-vetorial-pt2.html` | 403 | 40 | 5 | As Leis do Universo (Parte 2) |
| `espacos.html` | 650 | 72 | 5 | Espaços Vetoriais |
| `eigenbase.html` | 460 | 29 | 6 | O Código-Fonte |

---

## 2. Gap analysis — slides ↔ exercícios

24 tópicos de exercício para 10 decks.

| Fase | Tópicos de exercício | Decks | Situação |
|---|---|---|---|
| 1 | 4 | 3 | `sistemas-lineares` **sem deck** |
| 2 | 4 | 1 | 4 tópicos agregados em 1 deck |
| 3 | 6 | 1 | 6 tópicos em 1 deck de 42 seções |
| 4 | 3 | 1 | razoável |
| 5 | 5 | 3 | possível redundância (ver §5) |
| 6 | 2 | 1 | `diagonalizacao` provavelmente descoberto |

**Lacuna mais grave:** Fase 3. Seis tópicos (`vetores`, `norma-e-distancia`,
`ortogonalidade`, `produto-vetorial`, `retas-e-planos`, `geometria-sistemas-lineares`)
cabem em um único deck. Um conceito por slide não sobrevive a essa compressão.

---

## 3. Análise de história

**O embrião existe e é bom.** O tema arcade tem camada diegética real:
`lore-section` + `lore-label` com os rótulos **DEV LOG**, **A MECÂNICA**, **EASTER EGG**,
**LOG DA MISSÃO**, **DICA DO MESTRE DO JOGO**.

O DEV LOG enquadra os matemáticos como "Desenvolvedores Originais" do código do universo:

> "Desenvolvedores Originais: G. Leibniz (1678), G. Cramer (1750). Os 'programadores'
> originais do nosso universo matemático precisavam de uma ferramenta para entender a
> essência de um sistema linear."

Esse é um achado forte de design: história como *changelog* do jogo, não como contexto
colado. É mais original que a moldura de facções do Cálculo Vetorial.

**O problema:** é exatamente o inverso da diretriz "herói como produto de PR" dos outros
dois cursos. O DEV LOG canoniza o gênio individual — Leibniz, Cramer, Gauss, Cauchy,
Grassmann — sem o coletivo que sustentou cada um. Hoje a camada narrativa **celebra** o
que os outros cursos **desmontam**.

Quantidade: 1 bloco de lore por deck (10 no total). Não há arco entre fases — cada deck
conta uma anedota isolada, não um capítulo de uma história.

Faltam as três camadas de inserção dos outros repos:
- slide `01-historia` dedicado → não existe
- insert no V1 de cada tópico → não existe
- fragmento em `dual-panel` ao lado de exemplos → não existe

---

## 4. Análise de navegação

- Horizontal: usado como lista de tópicos (correto em intenção).
- Vertical: existe, mas sem fluxo pedagógico fixo. Não há garantia de
  motivação → conceito → formalização → exemplo → fechamento.
- Sem `00-capa` / `NN-resumo` / `NN-reflexao`: todo deck começa no conteúdo e termina
  sem síntese nem pergunta aberta.

---

## 5. Problemas técnicos

**Inline styles:** 18 ocorrências em 5 arquivos.

| Arquivo | `style="` | Bloco `<style>` |
|---|---|---|
| `transformacoes.html` | 11 | sim |
| `espacos.html` | 3 | sim |
| `determinante.html` | 2 | — |
| `inversas.html` | 1 | — |
| `eigenbase.html` | 1 | — |
| `propriedades.html` | 0 | sim |

Os 11 de `transformacoes.html` são layout de verdade: `flex`, `padding`, `font-size`,
`background-color`. Não são SVG legítimo.

**LaTeX quebrado:** `propriedades.html` — 2 ocorrências de `\\(` (barra dupla).

**Framework:** 9 decks em Reveal.js **4.3.1 via CDN** (cdnjs). O repo de Geometria já
migrou para **5.1.0**. `espacos.html` mistura `dist/reveal.js` local com plugins de CDN —
híbrido inconsistente.

**MathJax:** `tex-mml-chtml` em 9 decks (Geometria usa `tex-svg`). Um deck usa KaTeX.

**`espacos.html` é corpo estranho:** 72 seções, 650 linhas, título genérico
("Espaços Vetoriais"), sem numeração de fase, framework híbrido. Provável deck legado a
ser absorvido por `espaco-vetorial-pt1` + `pt2` — ou aposentado. Antes de mexer, precisa
de decisão: qual dos três é a fonte de verdade da Fase 5?

---

## 6. Comparação com o padrão dos repos irmãos

| Item | Geometria | Cálculo | Álgebra Linear |
|---|---|---|---|
| Pasta por capítulo + loader | sim | sim | **não** |
| `00-capa` / `01-historia` / `resumo` / `reflexao` | sim | sim | **não** |
| Insert no V1 de todo tópico | sim | sim | **não** |
| Fragmento em dual-panel | sim | sim | **não** |
| `narrative-spec` | sim | sim | **não** |
| `pedagogical-spec` | sim | sim | **não** |
| `template-spec` | sim | sim | **não** |
| `visual-design-spec` | sim | sim | **não** |
| `section-checklist` | sim | sim | **não** |
| Pipeline RTC → PDI 4 camadas → verificação | sim | sim | **não** |
| CSS externo, zero inline | sim | sim | 18 inline |
| Reveal.js | 5.1.0 | local | 4.3.1 CDN |

---

## 7. Prioridades

**CRÍTICA**
1. Decidir o destino da Fase 5 (três decks para cinco tópicos).
2. Corrigir o LaTeX quebrado de `propriedades.html` (2 ocorrências).
3. Remover os 18 inline styles e os 3 blocos `<style>`.

**ALTA**
4. Fase 3: 6 tópicos em 1 deck — dividir por tópico.
5. Criar `sistemas-lineares` (Fase 1) e `diagonalizacao` (Fase 6), hoje sem deck.
6. Escrever o arco narrativo do curso: transformar o DEV LOG em arco que atravessa as
   6 fases e corrigir o viés de gênio individual.

**MÉDIA**
7. Migrar Reveal 4.3.1 CDN → cópia local (ou 5.1.0, como a Geometria).
8. Padronizar MathJax (`tex-svg`).
9. Adotar pasta por capítulo + loader.

**BAIXA**
10. `00-capa` / `NN-resumo` / `NN-reflexao` por deck.

---

## 8. Observações de método

- Contagem de `style="` é bruta: pega também atributos legítimos em SVG e `<canvas>`.
  Conferir arquivo por arquivo antes de tratar como violação.
- A contagem de `<section>` inclui aninhadas (verticais), não só seções horizontais.
- Nada foi alterado no repositório. Este documento está **não commitado** na worktree.
