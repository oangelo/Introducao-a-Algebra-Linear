# AGENTS.md — Slides de Introdução à Álgebra Linear

Contrato operacional. **Leia antes de tocar em qualquer arquivo desta pasta.**
O *porquê* está em [`HISTORIA.md`](HISTORIA.md); o arco do curso em
[`STORYBOARD-GERAL.md`](STORYBOARD-GERAL.md); as regras da ficção em [`BIBLIA.md`](BIBLIA.md);
o desenho em [`ESTRATEGIA.md`](ESTRATEGIA.md); o que entra em cada fase em
[`MAPA-CAPITULOS.md`](MAPA-CAPITULOS.md); a parte não-matemática em
[`MAPA-JOGADOR.md`](MAPA-JOGADOR.md); o diagnóstico do que existe hoje em [`RTC.md`](RTC.md).

---

## 1. A premissa (define tudo o resto)

> "Os slides são um guia para mim e para os alunos que porventura se distraíram — para eles
> voltarem. Uma âncora na realidade e em que ponto nós estamos." — o professor

O conteúdo matemático é resolvido **no quadro, via exercício**. O slide é **HUD**: mapa de
estado, não veículo de conteúdo.

Consequências que não são negociáveis:

- Slide que **pode ser lido em voz alta** está errado. Se dá para ler, virou script.
- Slide que **explica** compete com o quadro. O quadro ganha; o slide atrapalha.
- A pergunta que todo slide responde: *onde estamos*, *qual é o problema agora*, ou *o que
  ficou*. Se não responde nenhuma, o lugar dele é o quadro.

Não há cota numérica de palavras, slides ou exemplos. **Cota numérica vira camisa de força e
foi explicitamente rejeitada pelo professor.** O limiar se calibra no storyboard de cada fase.

---

## 2. A ficção: um concurso dentro de um fliperama

O curso **é um concurso deixado por quem construiu o jogo**. Seis portões (as fases), seis
chaves (uma por portão), uma última porta (a sala da máquina). Cada fase é um **gabinete** com
gênero próprio.

> **Regra dura: um gabinete, um gênero, do primeiro ao último slide da fase.**

**As narrações em áudio estão descartadas** (out/2026): são antigas e defasadas. Nenhum
documento usa narração gravada como razão para manter gênero, cena ou fala. Os `scripts/*.md`
ficam como registro, não como fonte.

**O que não se copia de *Ready Player One*** (a referência de espírito): OASIS, Halliday/Anorak,
o ovo, os nomes das chaves, a cultura pop dos anos 80. Fica a estrutura — concurso, portões,
chaves, prêmio desconhecido — que é domínio público.

Hoje o repositório viola a regra do gênero: há três ficções simultâneas (fantasia medieval,
cyberpunk e arcade), 8 exercícios misturam medieval com cyberpunk no mesmo arquivo, e o deck
`eliminacao_gaussiana.html` também. Ver `RTC.md` §3.

| Portão | Gabinete | Gênero |
|---|---|---|
| P1 | Sistemas e Matrizes | **em aberto** |
| P2 | Determinantes | cyberpunk |
| P3 | Vetores Euclidianos | FPS |
| P4 | Transformações | plataforma com gravidade variável |
| P5 | Espaços Vetoriais | construção/estratégia |
| P6 | Autovalores | corrida |

**Fio condutor do curso:** *"O que este sistema faz com o espaço?"* Cada fase acrescenta uma
resposta nova — ver `HISTORIA.md` §3. Ao escrever qualquer slide, saiba qual é o pedaço da
resposta que aquela fase entrega.

**Camada do jogador:** é **foco**, não enfeite. Um **instrumento** (capítulo 1: como se sabe
que algo funciona) e **seis temas**, um por fase. Ver [`MAPA-JOGADOR.md`](MAPA-JOGADOR.md) e
[`CAPITULO-1.md`](CAPITULO-1.md).

A lição só entra se for **ocasião do conceito** da fase — a matemática dá o gancho, a evidência
vem citada (com DOI), nunca alegada pela metáfora. Nada de motivação genérica.

Veículos: **capítulo 1 com 10 cartelas** (Q01–Q10, antes do primeiro portão), **6 dicas de
carregamento** (uma por fase, cada uma um achado diferente) e **12 pausas** (2 por fase,
sobreposição, pergunta calibrada pelo tema da fase — nenhuma se repete).

---

## 3. As duas camadas visuais — e a fronteira

> **Se o slide tem fórmula ou número, a imagem é SVG. Se o slide tem história, a imagem é
> gerada. Não existe slide com as duas.**

### Camada A — diagrama (SVG / canvas), gerado por código

- **SVG inline** para estrutura: span, base, núcleo, imagem, grade deformada.
- **`<canvas>` + JS** só quando há interação (arrastar vetor, ver a transformação agir).
- SVG inline (não arquivo em `img/`) para herdar o CSS do tema e manter diff legível.
- `fragment` do Reveal para revelar o diagrama **um passo por clique** — é o que faz o slide
  virar roteiro do quadro.

**Nunca** use imagem gerada para objeto matemático: modelo de difusão erra número e erra
estrutura, silenciosamente. Erro silencioso em slide de matemática é pior que slide feio.

### Camada B — cena (imagem gerada, Qwen-Image)

- **Uma por fase, seis no curso.**
- Nunca carrega conteúdo matemático verificável.
- Marcada como fabricada.
- Nunca no mesmo slide que diagrama ou fórmula — a cena tem slide próprio.

> **BLOQUEIO ATUAL:** não há gerador de imagem exposto ao agente. llama.cpp não gera imagem;
> Qwen-Image em GGUF roda em **stable-diffusion.cpp** (`/sdapi/v1/txt2img`), provavelmente em
> container separado. Falta a porta/comando — ver `RTC.md` §9 / issue.

---

## 4. Estrutura de uma fase

```
00-capa        → nome do portão, 1 linha de missão, o gabinete aceso e a fechadura
01-cena        → imagem gerada (uma por fase, nunca com matemática)
02-dica        → carga: a técnica de estudo que a fase possui
03-estado      → HUD: onde estamos, o que já foi feito
04..NN         → um slide por tópico de exercício, o exercício que será resolvido no quadro
NN+1-chave     → a chave do portão (ver STORYBOARD-GERAL.md, Ato 7)
```

- **HUD fixo em todo slide**, com portão, tópico, exercício e chaves. Se poluir, reduz a
  faixa — não remove.
- **Sem `01-historia` de slide inteiro.** A história entra como **cena** (Camada B), uma por
  fase. É fio, não enredo.
- O slide de cada tópico mostra **o exercício que vai ser resolvido**, não a solução.
- **Nenhuma fase termina com chefe.** O curso tem um único **confronto**, na F6. As outras
  cinco terminam com uma chave na mão.
- **Pausas** são sobreposição, não tela: 2 por fase, no meio e no fim do miolo.

---

## 5. O que NÃO importar dos cursos irmãos

Geometria e Cálculo têm um pipeline que **não se aplica aqui**, porque lá o slide carrega
conteúdo:

| Mecanismo | Por que fica de fora |
|---|---|
| PDI em 4 camadas | Pressupõe slide como veículo de conteúdo |
| Insert obrigatório no V1 de todo tópico | Idem — estoura o limiar de texto |
| Fragmento em `dual-panel` ao lado de exemplos | Duas colunas = dois objetos competindo |
| Arco narrativo com começo/meio/fim | "Não pode ser história comprida" |

**O que fica:** o RTC (diagnóstico) e a disciplina de verificação. Nada além.

---

## 6. DEV LOG

Deixa de celebrar o gênio individual e vira **créditos com dívida técnica**: quem construiu,
quem ficou de fora, o que ainda não funciona. Cramer publicou a regra, mas o resultado já
circulava; Gauss não inventou a eliminação; Grassmann foi ignorado em vida.

---

## 7. Verificação antes de commitar

Verificável por script:

```bash
grep -c 'style="' arquivo.html      # deve ser 0
grep -c '\\\\(' arquivo.html        # deve ser 0 (LaTeX quebrado)
```

Verificação manual obrigatória:

1. CSS do tema carregou (não é HTML cru)?
2. MathJax renderizou?
3. Navegação do Reveal funciona nas duas direções?
4. Links relativos (`game-theme.css`, `css/`, `js/`) resolvem?
5. O slide responde onde estamos / qual é o problema / o que ficou?

O limiar de texto **não** é verificável por script — é julgamento na revisão, com o
storyboard ao lado.

---

## 8. Onde estamos (2026-10-23)

- Nada foi implementado. Nenhum slide novo, nenhum deck alterado.
- Decidido: premissa HUD, ficção do fliperama, fio condutor, camada do jogador, HUD fixo,
  DEV LOG como créditos, sem cota numérica, piloto = **Fase 1**.
- Feito: [`MAPA-CAPITULOS.md`](MAPA-CAPITULOS.md) — o que entra em cada fase e **qual
  capítulo é dono de cada conceito** (regra R1: um conceito tem um dono).
- Feito: [`CAPITULO-1.md`](CAPITULO-1.md) — a abertura: os cinco instrumentos do método, o caso
  da teoria que virou livro e não se replicou, e as 10 cartelas (imagem + frase).
- Feito: [`MAPA-JOGADOR.md`](MAPA-JOGADOR.md) — um instrumento (capítulo 1) e seis temas, um por
  fase, com dica, ocasião no conteúdo e referência com DOI.
- Feito: [`STORYBOARD-GERAL.md`](STORYBOARD-GERAL.md) — os 46 quadros do curso, na ordem, com
  as chaves, o capítulo 1 e as 12 pausas.
- Feito: [`BIBLIA.md`](BIBLIA.md) — as regras: concurso, chaves, registros, orçamentos
  (4 telas de manual, 2 interstícios, 6 cenas, 6 dicas, 12 pausas, 1 confronto, 6 chaves).
- Feito: [`STORYBOARD-F1.md`](STORYBOARD-F1.md) — piloto com 9 telas, 2 pausas e o inventário
  de imagem de cada tela (1 gerada, 8 SVG).
- Próximo passo: aprovar a Fase 1 → `slide-spec.md` → implementar as 8 telas SVG (a cena
  espera o gerador).
- Bloqueado: gerador de imagem (Camada B).
