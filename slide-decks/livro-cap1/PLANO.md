# Plano — o livro do capítulo 1 (HTML)

Objetivo: **um arquivo HTML que se lê como capítulo de livro**, sobre a matéria do capítulo 1
(equações lineares, sistemas, matrizes, eliminação). Não é deck, não é portão, não é jogo: o texto
fala de matemática. A história do capítulo 1 entra como **abertura**, em prosa, e sai de cena.

Este plano existe por uma razão operacional: o livro é longo demais para um agente só. Ele é
**montado por fragmentos**, cada um escrito por uma tarefa isolada, e costurado por um script.

---

## 1. A regra que resolve o contexto

```
livro-cap1/
  CONTRATO.md            ← voz, notação, classes, regras. Lido por TODA tarefa.
  partes/
    00-abertura.html     ← prosa (a história do instrumento, sem jogo)
    10-s1-1.html … 19-s1-12.html
    20-exemplos-a.html   ← 1.13 exemplos resolvidos (blocos A e B)
    21-exemplos-b.html   ← 1.13 exemplos resolvidos (blocos C, D, E)
    30-exercicios.html   ← 1.14, colhidos dos 4 arquivos de exercícios que já existem
    40-fim.html          ← glossário, notação, fontes
  build.py               ← monta livro-cap1.html (índice automático a partir dos <h2>)
  verificar.py           ← checa o contrato no arquivo montado
  livro-cap1.css         ← derivado de f1-matematica.css
  livro-cap1.html        ← GERADO. nunca editado à mão.
```

Nenhuma tarefa escreve `livro-cap1.html`, e nenhuma lê mais de **dois** arquivos de fonte.
O agente revisor é o único que lê o livro inteiro — e ele não escreve, só aponta.

---

## 2. O contrato (resumo; o completo vai em CONTRATO.md)

- **Voz:** português do Brasil, direto, sem motivação genérica, sem "vamos juntos". Trata o
  leitor por "você" só em exercício; no corpo, impessoal.
- **Vocabulário proibido no livro:** portão, chave, fase, quest, chefe, jogador, HUD, gabinete.
  A história aparece uma vez, na abertura, e conta um caso — não um jogo.
- **Matemática:** `\(…\)` inline e `\[…\]` bloco, **uma barra**. Proibido `\\(`, `\\[`.
- **Sem `style=` inline, sem `<style>`, sem imagem na v1.**
- **Fragmento é:** `<section class="sec" id="s-1-5">` + `<h2><span class="num">1.5</span>…</h2>`
  + conteúdo. Só classes do `livro-cap1.css`.
- **Referência cruzada:** `<a class="ref" href="#s-1-9">1.9</a>` — nunca "veja acima".
- **Cabeçalho do fragmento:** `<!-- fonte: f1-matematica.html §1.5–1.6 -->`, para rastrear de onde
  veio cada trecho.
- **Tamanho:** 120–250 linhas por fragmento. Acima disso, divide.
- **Números:** os exemplos do livro são **os mesmos do quadro** (as 19 fichas de
  `f1-matematica.html`), para o aluno reencontrar o que copiou no caderno. Não inventar exercício
  novo resolvido.

---

## 3. As tarefas

Cada linha é uma tarefa que cabe num agente isolado. "Lê" é o orçamento de contexto; o resto do
repositório é proibido.

| # | Tarefa | Lê | Escreve | Critério de pronto |
|---|---|---|---|---|
| T0 | Contratos, CSS, build, verificador | `f1-matematica.css`, §2 deste plano | `CONTRATO.md`, `livro-cap1.css`, `build.py`, `verificar.py` | `build.py` roda em árvore vazia e gera índice |
| T1 | Abertura em prosa | `STORYBOARD-CAP1.md` §1–2, `CAPITULO-1.md` | `partes/00-abertura.html` | conta o arco (teoria → uma vitória → os três instrumentos → o caso → o fecho) em ~1 página, sem vocabulário de jogo |
| T2 | §1.1–1.4 equação, reta, conjunto, escala | `f1-matematica.html` §1.1–1.4 | `partes/10..13` | notação de conjuntos explícita; a transição geometria→álgebra fecha 1.4 |
| T3 | §1.5–1.6 sistema e as três respostas | `f1-matematica.html` §1.5–1.6 | `partes/14..15` | prova de que "exatamente duas" não existe, em 3 linhas |
| T4 | §1.7–1.8 matriz e operações | `f1-matematica.html` §1.7–1.8 | `partes/16..17` | cada operação com a razão da reversibilidade |
| T5 | §1.9–1.12 escada, protocolo, pivô, leitura | `f1-matematica.html` §1.9–1.12 | `partes/18..19` | as quatro leituras da forma, cada uma com um exemplo de 1 linha |
| T6 | §1.13 exemplos A e B | fichas A1–A3, B1–B4 de `f1-matematica.html` | `partes/20` | cada exemplo: enunciado, passo a passo, conferência |
| T7 | §1.13 exemplos C, D, E | fichas C0–C5, D1–D2, E1–E3 | `partes/21` | idem; retangular e 4×4 com a leitura da forma ao final |
| T8 | §1.14 exercícios | `exercicios/capitulo-1/*.html` (4 arquivos, 75 exercícios) | `partes/30` | 20–24 exercícios escolhidos, com gabarito em `<details>`, sem inventar |
| T9 | Glossário, notação, fontes | as fichas e `AGENTS.md` | `partes/40` | todo símbolo usado no livro está na tabela de notação |
| T10 | Revisão cruzada (read-only) | `livro-cap1.html` **montado** | relatório em `livro-cap1/REVISAO.md` | lista, por seção, o que um leitor que só tem o arquivo não entende |
| T11 | Build final + QA + commit | tudo, mas só executa | `livro-cap1.html` final | `verificar.py` verde + os 4 checks do `AGENTS.md` §7 + PDF opcional |

**Ordem:** T0 → (T1…T5 em paralelo) → (T6…T9 em paralelo) → T10 → correções pontuais → T11.

---

## 4. O que o verificador checa (e por que cada um)

```python
# verificar.py — roda sobre livro-cap1.html montado
1. todo href="#s-..." tem destino          # referência cruzada quebrada é o erro nº1 de texto montado
2. nenhum id repetido
3. nenhum 'style=' e nenhum '<style'        # regra do repo
4. nenhuma barra dupla '\\(' ou '\\['       # MathJax quebra silenciosamente
5. parênteses de math balanceados por arquivo  # \( sem \) come o resto da página
6. seções numeradas em sequência 1.1..1.13
7. toda palavra do vocabulário proibido ausente  # portão, chave, fase, quest, chefe, HUD
8. toda fórmula em \[...\] tem \] correspondente
```

Os itens 1, 5 e 7 não existem nos outros documentos porque lá não havia texto montado por
fragmentos. São o preço da divisão em tarefas.

---

## 5. Duas decisões que precisam de você antes do T1

1. **Figuras:** v1 sai **sem figura nenhuma** (só texto e fórmula). As três que fariam falta —
   reta×sistema com os três casos, a escada de pivôs, e o conjunto-solução com variável livre —
   entram na v2 como **SVG desenhado por código**, nunca imagem gerada (Camada A do AGENTS.md).
2. **Exercícios:** colher dos 4 arquivos que já existem em `exercicios/capitulo-1/` (75 no total),
   escolhendo por tópico. O livro **não cria exercício novo** — se faltar um caso, ele entra como
   exemplo resolvido, não como exercício inédito.

---

## 6. O que este plano recusa

- **Um agente escrevendo o livro inteiro.** É o modo como o contexto entope: o agente reescreve o
  que já existia porque não consegue reler.
- **Fragmento sem contrato.** Sem `CONTRATO.md`, cada agente inventa classe, numeração e voz, e a
  costura vira colagem.
- **Duas fontes de verdade.** O livro não copia texto de `f1-matematica.html`: ele **reescreve**
  para leitura contínua, citando a origem no comentário. Se as duas divergirem, o livro erra — por
  isso o T10 confere a matemática contra as fichas.
