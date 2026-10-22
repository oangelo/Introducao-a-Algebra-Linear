# AGENTS.md — Slides de Introdução à Álgebra Linear

Contrato operacional. **Leia antes de tocar em qualquer arquivo desta pasta.**
O *porquê* está em [`HISTORIA.md`](HISTORIA.md); o arco do curso em
[`STORYBOARD-GERAL.md`](STORYBOARD-GERAL.md); o desenho em [`ESTRATEGIA.md`](ESTRATEGIA.md);
o que entra em cada fase em [`MAPA-CAPITULOS.md`](MAPA-CAPITULOS.md); o diagnóstico do que
existe hoje em [`RTC.md`](RTC.md).

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

## 2. A ficção: um fliperama, seis gabinetes

O curso **é um fliperama**. Cada fase é um **gabinete** com gênero próprio.

> **Regra dura: um gabinete, um gênero, do primeiro ao último slide da fase.**

Hoje o repositório viola isso: há três ficções simultâneas (fantasia medieval, cyberpunk e
arcade), 8 exercícios misturam medieval com cyberpunk no mesmo arquivo, e o deck
`eliminacao_gaussiana.html` também. Ver `RTC.md` §3.

| Fase | Gabinete | Gênero |
|---|---|---|
| 1 | Sistemas e Matrizes | fantasia medieval (narração pronta) |
| 2 | Determinantes | cyberpunk (narração pronta) |
| 3 | Vetores Euclidianos | FPS — a definir no storyboard |
| 4 | Transformações | plataforma — a definir no storyboard |
| 5 | Espaços Vetoriais | construção/estratégia — a definir no storyboard |
| 6 | Autovalores | corrida — a definir no storyboard |

**Fio condutor do curso:** *"O que este sistema faz com o espaço?"* Cada fase acrescenta uma
resposta nova — ver `HISTORIA.md` §3. Ao escrever qualquer slide, saiba qual é o pedaço da
resposta que aquela fase entrega.

**Camada do jogador:** disciplina, hábito, dúvida. A lição **só entra se for consequência do
conceito da fase** (matriz = composição = hábito atômico; autovetor = o que não muda). Nada
de motivação genérica. Veículos: dica de tela de carregamento (1 por fase) e menu de pausa
(no máximo 2 por fase). Ver `HISTORIA.md` §4.

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
00-capa        → nome da fase, 1 linha de missão, o gabinete aceso no saguão
01-estado      → HUD: onde estamos, o que já foi feito
02..NN         → um slide por tópico de exercício, o exercício que será resolvido no quadro
NN+1-peça      → a peça coletada nesta fase (ver STORYBOARD-GERAL.md §3)
```

- **HUD fixo em todo slide**, com fase, tópico, exercício e peças coletadas. Se poluir, reduz
  a faixa — não remove.
- **Sem `01-historia` de slide inteiro.** A história entra como **cena** (Camada B), uma por
  fase. É fio, não enredo.
- O slide de cada tópico mostra **o exercício que vai ser resolvido**, não a solução.
- **Nenhuma fase termina com chefe.** O curso tem um único confronto, na F6. As outras cinco
  terminam com uma peça na mão.

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

## 8. Onde estamos (2026-10-22)

- Nada foi implementado. Nenhum slide novo, nenhum deck alterado.
- Decidido: premissa HUD, ficção do fliperama, fio condutor, camada do jogador, HUD fixo,
  DEV LOG como créditos, sem cota numérica, piloto = **Fase 1**.
- Feito: [`MAPA-CAPITULOS.md`](MAPA-CAPITULOS.md) — o que entra em cada fase e **qual
  capítulo é dono de cada conceito** (regra R1: um conceito tem um dono).
- Feito: [`STORYBOARD-GERAL.md`](STORYBOARD-GERAL.md) — os 36 quadros do curso, na ordem
  (a lista que se lê de uma vez para achar repetição).
- Feito: [`BIBLIA.md`](BIBLIA.md) — as regras que justificam o arco: registros, peças,
  orçamentos (4 saguões, 6 cenas, 6 dicas, ≤12 pausas, 1 confronto).
- Feito: [`STORYBOARD-F1.md`](STORYBOARD-F1.md) — piloto com 9 telas e o inventário de imagem
  de cada uma (1 gerada, 8 SVG).
- Próximo passo: aprovar a Fase 1 → `slide-spec.md` → implementar as 8 telas SVG (a cena
  espera o gerador).
- Bloqueado: gerador de imagem (Camada B).
