# Estratégia dos Slides — Introdução à Álgebra Linear

Documento de desenho, não de execução. Nada aqui foi implementado.
**Branch:** `feature/slides` · **Base:** `e16a71e` · **Data:** 2026-10-22

---

## 0. Premissa

O professor definiu a função do slide, e ela não é ensinar:

> "Os slides são um guia para mim e para os alunos que porventura se distraíram —
> para eles voltarem. Uma âncora na realidade e em que ponto nós estamos."

O conteúdo matemático é resolvido **no quadro, via exercício**. O slide é HUD: mapa de
estado, não veículo de conteúdo.

Tudo abaixo decorre dessa premissa. Onde ela conflita com a arquitetura dos cursos irmãos
(Geometria e Cálculo), **a premissa vence**.

---

## 1. O que a premissa implica (sem meta numérica)

Hoje: **410 tags `<section>`** em 10 decks (72 só em `espacos.html`).

Slide que explica é slide que o professor lê — e ele não pode ler. Alguma redução é
inevitável, mas **não se fixa número de slides**: cota numérica vira camisa de força,
reprova o slide que precisa de mais espaço e aprova o de cinco palavras que não diz nada.
A quantidade sai do **storyboard de cada fase**, junto com a ordem dos tópicos.

O único dado firme: 410 seções não é uma estrutura de mapa. É uma apostila fatiada.

---

## 2. Texto: princípio, não cota

- O slide **não pode ser lido em voz alta** pelo professor — se dá para ler, o slide virou script.
- **Um objeto visual por slide** (diagrama, fórmula ou figura). Dois competem pela atenção.
- Fórmula **não conta** como leitura: ela é o objeto, não o texto.

O limiar concreto — quantas palavras, quantas linhas — é **calibrado no storyboard, tópico
por tópico**. Um tópico de definição formal aceita mais texto que um de intuição geométrica.
**Não existe número global.**

---

## 3. As duas camadas visuais (e a fronteira entre elas)

Esta é a decisão central, e vem de duas observações do professor:

> "O melhor não era gerar imagem, era usar canvas e SVGs."
> "Imagem é para contar a história e chamar a atenção do aluno."

### Camada A — Diagrama: SVG e canvas, gerado por código

**O que é:** o objeto matemático ou sua estrutura, desenhado programaticamente.

**Por que não imagem gerada:** modelo de difusão erra número e erra estrutura,
silenciosamente. Um determinante desenhado por IA sai com algarismos plausíveis e falsos.
Em slide de matemática, erro silencioso é pior que slide feio.

**Por que SVG na Álgebra é mais necessário que na Geometria:** aqui o objeto é abstrato. O
diagrama não representa o vetor de R⁴ — representa a **relação**: o span como plano, a base
como conjunto de setas que gera o plano, o núcleo como o que colapsa na origem, a
transformação como grade deformada, o autovetor como a única seta que não muda de direção.

**Divisão:**

| Tipo | Tecnologia | Quando |
|---|---|---|
| Diagrama estático | SVG inline no HTML | Estrutura conceitual (span, base, núcleo, imagem) |
| Simulador | `<canvas>` + JS (IIFE) | Interação: arrastar vetor, ver a transformação agir |

SVG inline é preferível a arquivo em `img/` porque herda o CSS do tema, escala sem perda e
o diff no git é legível. Canvas só quando há movimento ou input.

**Ganho específico para o modelo "mapa":** com `fragment` do Reveal, o diagrama é revelado
**um passo por clique**. O slide vira o roteiro do quadro — o professor clica e o desenho
acompanha a lógica que ele está escrevendo no quadro. O aluno que voltou do celular refaz o
raciocínio clicando. Imagem estática não faz isso.

### Camada B — Cena: imagem gerada (Qwen-Image)

**O que é:** a história. Satírica, traço pesado, nanquim.

**Dose:** **uma por fase, seis no curso.** É a "dose baixa" da issue #95.

**Regras:**
1. Nunca carrega conteúdo matemático verificável — nenhum número, nenhuma matriz.
2. Marcada como fabricada (regra da #95).
3. **Nunca no mesmo slide que um diagrama ou fórmula.** A regra da #95 ("imagem nunca no
   mesmo campo visual da fórmula") vira regra estrutural: a cena tem slide próprio.
4. Duas funções alternadas, no máximo uma de cada por fase: abrir a fase (atenção) ou
   fechar (respiro).

### A fronteira

> Se o slide tem fórmula ou número, a imagem é SVG. Se o slide tem história, a imagem é
> gerada. Não existe slide com as duas.

---

## 4. Estrutura de uma fase

```
00-capa        → nome da fase, 1 linha de missão        (1 slide)
01-estado      → HUD: onde estamos, o que já foi feito  (1 slide, recorrente)
02..NN         → 1 slide por tópico de exercício        (N slides)
NN+1-placar    → o que foi dominado, qual é o próximo chefe (1 slide)
```

**Sem `01-historia` de slide inteiro.** A história entra como **cartão**: a cena (Camada B)
num slide só, no máximo dois por fase. Não há arco narrado — há fio.

**O HUD:** faixa persistente com fase, tópico e o exercício correspondente. É o mecanismo
de re-ancoragem que o professor descreveu, e é diegético — no tema arcade, HUD não é
adorno, é o marcador de estado do jogo.

> **Decidido:** HUD fixo em todo slide. É o mecanismo de re-ancoragem do aluno que voltou do
> celular; se poluir visualmente, reduz a faixa — não remove.

---

## 5. O DEV LOG

Hoje: 10 blocos, enquadrando Leibniz, Cramer, Gauss, Cauchy e Grassmann como
"Desenvolvedores Originais" do código do universo.

O dispositivo é bom — história como changelog do jogo, melhor que a moldura de facções do
Cálculo. **Mas é o inverso da diretriz dos cursos irmãos:** canoniza o gênio individual.

Três saídas possíveis:

- **(a) Manter como está.** Coerente com o tema, mas o curso afirma o que os outros negam.
- **(b) Virar "créditos do jogo".** O DEV LOG mostra quem *de fato* sustentou o trabalho —
  calculistas, copistas, a equipe que ficou sem nome no rodapé. Mantém o dispositivo,
  inverte o alvo.
- **(c) Aposentar.** A história fica só na cena, sem camada textual.

> **Decidido: (b).** DEV LOG vira **créditos com dívida técnica** — quem construiu, quem ficou
> de fora, o que ainda não funciona. Ver `HISTORIA-holistica.md` §5.

---

## 6. O que NÃO portar dos cursos irmãos

| Mecanismo | Por que fica de fora |
|---|---|
| PDI em 4 camadas | Pressupõe slide como veículo de conteúdo |
| Insert obrigatório no V1 de todo tópico | Idem — estoura o limiar de texto calibrado |
| Fragmento em `dual-panel` ao lado de exemplos | Duas colunas = dois objetos competindo |
| Arco narrativo com começo/meio/fim | O professor vetou: "não pode ser história comprida" |

Fica do pipeline: **RTC** (já feito: `RTC-slides.md`) e um **PDI enxuto de 2 camadas**
(núcleo mínimo + fio histórico).

---

## 7. Verificação objetiva

O que é verificável por script — e deve ser:

- nenhum `style=` inline
- nenhum `\\` (LaTeX quebrado)
- CSS do tema carregado e MathJax renderizando
- links relativos resolvendo

O limiar de texto **não** é verificável por script. É julgamento na revisão, com o
storyboard ao lado. Script não decide se um slide é legível; ele só impede os erros
mecânicos que passam batido.

---

## 8. Ordem de execução

1. ~~Fechar as decisões pendentes e o orçamento~~ — decidido: HUD fixo, DEV LOG como
   créditos, sem cota global de texto.
2. **Storyboard da Fase 1** — tópicos, ordem, a pergunta de cada tópico, onde entra a cena,
   e o limiar de texto calibrado ali.
3. `slide-spec.md` (contrato técnico: classes, estrutura, verificações) — escrito **depois**
   do storyboard, para refletir o que o storyboard exigiu.
4. Implementar a Fase 1 e rodar a verificação visual.
5. Testar a Camada B (uma cena com Qwen-Image) — bloqueado até ter a porta do gerador.
6. Só então as outras 5 fases.

> **Decidido:** piloto é a **Fase 1** — quatro tópicos, o formato mais simples do curso. Testa
> o desenho inteiro antes das outras cinco. O gênero do gabinete é **noir / investigação** —
> decidido depois de descartar a narração em áudio.

---

## 9. Bloqueio técnico

Não há gerador de imagem exposto ao agente:

- `30069` llama.cpp (`hermes`) · `30068` embeddings · `8880` Kokoro TTS · `9001` whisper
- `9377` camofox · `6000`/`6080`/`6999` respondem, mas não são API de imagem
- Nenhum provedor `image_gen` configurado no Hermes (`config.yaml` sem seção de imagem)

llama.cpp não gera imagem. Qwen-Image em GGUF roda no **stable-diffusion.cpp**, cujo
servidor expõe `/sdapi/v1/txt2img` (estilo A1111). Preciso do comando ou da porta que você
usa no Oráculo para (a) testar a Camada B e (b) montar a biblioteca de prompts.
