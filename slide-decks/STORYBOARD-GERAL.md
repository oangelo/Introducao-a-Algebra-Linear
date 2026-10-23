# Storyboard Geral — Introdução à Álgebra Linear

**O que é isto:** a lista dos quadros do curso, na ordem em que o aluno os vê, do primeiro
slide ao último. Cada linha é uma tela.

**O que isto não é:** não são as regras do mundo ([`BIBLIA.md`](BIBLIA.md)), nem os conceitos
de cada fase ([`MAPA-CAPITULOS.md`](MAPA-CAPITULOS.md)), nem a parte não-matemática
([`MAPA-JOGADOR.md`](MAPA-JOGADOR.md)), nem os slides da Fase 1
([`STORYBOARD-F1.md`](STORYBOARD-F1.md)).

**Para que serve:** lendo a lista inteira de uma vez, vê-se onde dois quadros fazem a mesma
coisa. É o único jeito de garantir que a Fase 4 não repete a Fase 1 — um quadro por vez, não
se enxerga.

**O motor:** um concurso deixado por quem construiu o jogo. Seis portões, seis chaves, uma
última porta. Atrás dela não há troféu — há a sala da máquina, e a máquina é a mesma nos seis
gabinetes.

Como ler cada quadro:

- **Tela** — o que está desenhado.
- **Texto** — o que está escrito no slide.
- **HUD** — o canto: portão, tópico e chaves.

**Pausas** são sobreposições (véu escuro sobre a tela corrente), não telas novas — é o que um
menu de pausa faz. Não entram na contagem de quadros.

---

## ATO 0 — A ENTRADA (6 quadros)

### Q01 · Saguão apagado
- **Tela:** preto. Seis silhuetas de gabinete enfileiradas, nenhuma acesa. Uma ficha girando no chão.
- **Texto:** *Uma ficha. Seis máquinas.*
- **HUD:** não existe ainda.

### Q02 · As seis acendem
- **Tela:** a ficha cai na fenda. Os seis acendem em sequência — âmbar, magenta, laranja, roxo, azul, vermelho — e apagam juntos. Fica um seis na tela, como uma fechadura de seis buracos.
- **Texto:** *Nenhuma delas diz o que faz. Todas têm uma fechadura.*
- **HUD:** não existe ainda.

> **Manual do Jogador — quatro telas.** É a plaquinha de instruções que todo gabinete tinha
> colada. Só existe aqui, no começo; nunca mais no curso.

### Q03 · Manual 1 — sono
- **Tela:** silhueta de um gabinete desligado, um travesseiro apoiado nele. SVG, traço chapado.
- **Texto:** *O que você estuda de manhã é decidido à noite.*
- **HUD:** não existe ainda.

### Q04 · Manual 2 — corpo
- **Tela:** a mesma silhueta, com uma pegada de tênis na frente e um leve borrão de movimento.
- **Texto:** *O corpo não é pausa do estudo — é parte dele.*
- **HUD:** não existe ainda.

### Q05 · Manual 3 — gente
- **Tela:** duas silhuetas de jogador frente a frente, cada uma com seu caderno. Nenhuma olhando o caderno do outro.
- **Texto:** *Junto, mas cada um resolve antes.*
- **HUD:** não existe ainda.

### Q06 · Manual 4 — as regras do jogo
- **Tela:** a fechadura de seis buracos, em corte, com o mecanismo visível.
- **Texto:** *A prova não mede o que você sabe. Mede o que você recupera sem consulta, em duas horas.*
- **HUD:** não existe ainda.

> O aluno sai da primeira aula sabendo quatro coisas que ninguém costuma dizer: durma, mexa-se,
> estude junto do jeito certo, e a prova mede outra coisa que não "saber".

---

## ATO 1 — PORTÃO 1 · SISTEMAS E MATRIZES (âmbar, fantasia medieval)

### Q07 · Capa
- **Tela:** o saguão escuro; o gabinete 1 aceso em âmbar. A fechadura com seis buracos, nenhum preenchido.
- **Texto:** *PORTÃO 1 — SISTEMAS E MATRIZES*
- **HUD:** nasce aqui. `P1 · CHAVES 0/6`

### Q08 · Cena
- **Tela:** imagem gerada. A banca do mercador em Portoveloz; três tiras de pergaminho lado a lado — as três compras. Nenhum número, nenhuma letra legível.
- **Texto:** *três compras. três totais. nenhum preço.*
- **HUD:** `P1 · CHAVES 0/6`

### Q09 · Dica de carregamento — autoexplicação
- **Tela:** a cena com véu escuro a 60%; a dica no canto inferior, sozinha.
- **Texto:** *Antes de calcular, diga em voz alta por que este sistema não vai ter solução. Se você não consegue explicar, reconheceu — não entendeu.*
- **HUD:** `P1 · CHAVES 0/6`

### Q10 · Miolo — 4 telas de tópico
- **Tela:** uma por tópico (sistemas, escalonamento, propriedades, inversa). Cada uma traz o exercício que será resolvido no quadro.
- **Texto:** o enunciado.
- **HUD:** `P1 · SISTEMAS` … `P1 · INVERSA`, `CHAVES 0/6`

- **Pausa 1** (sobreposição no 2º tópico): *Qual destes quatro você resolve sem olhar? Qual você evita?*
- **Pausa 2** (sobreposição no 4º tópico): *O que você explicaria hoje que não explicava ontem?*

### Q11 · Chave 1
- **Tela:** o primeiro buraco da fechadura se acende em âmbar. Nada mais.
- **Texto:** *chave 1 — o estado*
- **HUD:** `CHAVES 1/6`

---

## ATO 2 — PORTÃO 2 · DETERMINANTES (magenta, cyberpunk)

### Q12 · Capa
- **Tela:** gabinete 2 aceso; o 1 continua aceso. Um buraco preenchido de seis.
- **Texto:** *PORTÃO 2 — DETERMINANTES*
- **HUD:** `P2 · CHAVES 1/6`

### Q13 · Cena
- **Tela:** imagem gerada. Corredor de servidores; um cadeado físico numa porta de vidro; reflexo de neon.
- **Texto:** *nem todo sistema tem volta.*
- **HUD:** `P2 · CHAVES 1/6`

### Q14 · Dica de carregamento — recuperação
- **Tela:** a cena com véu escuro.
- **Texto:** *Feche o caderno e refaça de memória. Reler dá a sensação de saber; refazer dá a informação.*
- **HUD:** `P2 · CHAVES 1/6`

### Q15 · Miolo — 4 telas de tópico
- **Tela:** cofatores, redução, propriedades, Cramer.
- **Texto:** o enunciado.
- **HUD:** `P2 · … · CHAVES 1/6`

- **Pausa 1:** *Qual foi seu último erro? Você sabe por que errou?*
- **Pausa 2:** *Você conferiu substituindo — ou só achou que estava certo?*

### Q16 · Chave 2
- **Texto:** *chave 2 — a impressão digital*
- **HUD:** `CHAVES 2/6`

---

## SAGUÃO 1 (1 quadro)

### Q17 · Atravessando
- **Tela:** os dois gabinetes acesos vistos de longe; o resto no escuro. A câmera passa entre eles.
- **Texto:** *o resto do fliperama também é o mesmo espaço.*
- **HUD:** `CHAVES 2/6`

> Existe porque o que vem a seguir **não** é mais sobre a máquina responder. É sobre o espaço
> onde ela está.

---

## ATO 3 — PORTÃO 3 · VETORES EUCLIDIANOS (laranja, FPS)

### Q18 · Capa
- **Texto:** *PORTÃO 3 — VETORES EUCLIDIANOS*
- **HUD:** `P3 · CHAVES 2/6`

### Q19 · Cena
- **Tela:** imagem gerada. Primeira pessoa: a mira, a linha de tiro, a distância marcada até o alvo.
- **Texto:** *onde estou.*
- **HUD:** `P3 · CHAVES 2/6`

### Q20 · Dica de carregamento — prática distribuída
- **Texto:** *Vinte minutos por dia batem três horas na véspera. O que decide é o intervalo, não a força.*
- **HUD:** `P3 · CHAVES 2/6`

### Q21 · Miolo — 6 telas de tópico
- **Tela:** vetores, norma e distância, ortogonalidade, produto vetorial, retas e planos, leitura geométrica dos sistemas da Fase 1. A fase mais densa do curso.
- **Texto:** o enunciado.
- **HUD:** `P3 · … · CHAVES 2/6`

- **Pausa 1:** *Quanto você avançou esta semana — não quanto você estudou?*
- **Pausa 2:** *Onde você está em relação a onde precisa chegar?*

### Q22 · Chave 3
- **Texto:** *chave 3 — a régua*
- **HUD:** `CHAVES 3/6`

---

## ATO 4 — PORTÃO 4 · TRANSFORMAÇÕES LINEARES (roxo, plataforma)

### Q23 · Capa
- **Texto:** *PORTÃO 4 — TRANSFORMAÇÕES LINEARES*
- **HUD:** `P4 · CHAVES 3/6`

### Q24 · Cena
- **Tela:** imagem gerada. Uma plataforma vista de lado; o chão se inclina e o horizonte entorta.
- **Texto:** *o mundo não é rígido.*
- **HUD:** `P4 · CHAVES 3/6`

### Q25 · Dica de carregamento — intenção de implementação
- **Texto:** *Se for terça às 19h, então eu resolvo dois exercícios. Sem dia e hora, intenção não é plano.*
- **HUD:** `P4 · CHAVES 3/6`

### Q26 · A grade
- **Tela:** **o único diagrama de grade deformada do curso.** A malha quadrada e, ao lado, a mesma malha depois da transformação, com o vetor que não mudou de direção destacado.
- **Texto:** *o que ela faz com o espaço.*
- **HUD:** `P4 · CHAVES 3/6`

### Q27 · Miolo — 3 telas de tópico
- **Tela:** transformações, aplicações, composição e reversão.
- **Texto:** o enunciado.
- **HUD:** `P4 · … · CHAVES 3/6`

- **Pausa 1:** *Em que momento do seu dia isso vai acontecer? Já tem hora?*
- **Pausa 2:** *Qual é a menor versão disso que você faria num dia ruim?*

### Q28 · Chave 4
- **Texto:** *chave 4 — a mão*
- **HUD:** `CHAVES 4/6`

---

## SAGUÃO 2 (1 quadro)

### Q29 · A fiação
- **Tela:** os quatro gabinetes acesos vistos por trás. A fiação sai de todos e entra no mesmo ponto do chão.
- **Texto:** *a mesma tomada.*
- **HUD:** `CHAVES 4/6`

> Existe porque a seguir a máquina deixa de agir e passa a ser **aberta**.

---

## ATO 5 — PORTÃO 5 · ESPAÇOS VETORIAIS (azul-planta, construção)

### Q30 · Capa
- **Texto:** *PORTÃO 5 — ESPAÇOS VETORIAIS*
- **HUD:** `P5 · CHAVES 4/6`

### Q31 · Cena
- **Tela:** imagem gerada. Uma planta baixa aberta sobre a mesa; poucas vigas sustentando um vão enorme.
- **Texto:** *pouca coisa sustenta tudo.*
- **HUD:** `P5 · CHAVES 4/6`

### Q32 · Dica de carregamento — intercalação
- **Texto:** *Misture os tipos de exercício. Bloco do mesmo tipo treina reconhecer, não escolher.*
- **HUD:** `P5 · CHAVES 4/6`

### Q33 · Miolo — 5 telas de tópico
- **Tela:** espaços vetoriais, subespaços, independência, coordenadas e bases, dimensão e posto.
- **Texto:** o enunciado.
- **HUD:** `P5 · … · CHAVES 4/6`

- **Pausa 1:** *O que você está carregando que não precisa?*
- **Pausa 2:** *Se tivesse metade do tempo, o que você cortaria?*

### Q34 · Chave 5
- **Texto:** *chave 5 — o esqueleto*
- **HUD:** `CHAVES 5/6`

---

## ATO 6 — PORTÃO 6 · AUTOVALORES (vermelho, corrida)

### Q35 · Capa
- **Tela:** o sexto gabinete aceso em vermelho. Cinco acesos ao fundo — o saguão quase todo iluminado.
- **Texto:** *PORTÃO 6 — AUTOVALORES E AUTOVETORES*
- **HUD:** `P6 · CHAVES 5/6`

### Q36 · Cena
- **Tela:** imagem gerada. A curva vista de dentro do carro; a linha do asfalto nítida, o resto borrado.
- **Texto:** *há uma direção em que nada derrapa.*
- **HUD:** `P6 · CHAVES 5/6`

### Q37 · Dica de carregamento — dificuldade desejável
- **Texto:** *Se está confortável, provavelmente não está aprendendo. O desconforto de não saber é o sinal de que a recuperação está acontecendo.*
- **HUD:** `P6 · CHAVES 5/6`

### Q38 · O confronto — o único do curso
- **Tela:** a equação característica que **não fatora** em números redondos. Sem saída bonita.
- **Texto:** *a máquina não quer ser entendida. E nem todo problema tem solução elegante.*
- **HUD:** `P6 · CHAVES 5/6`

- **Pausa 1:** *O que ainda é verdade quando a nota aperta?*
- **Pausa 2:** *O que te derruba na prova: o conteúdo ou a véspera?*

### Q39 · Chave 6
- **Texto:** *chave 6 — o eixo*
- **HUD:** `CHAVES 6/6`

---

## ATO 7 — A ÚLTIMA PORTA (3 quadros)

### Q40 · As seis chaves
- **Tela:** a fechadura de seis buracos, agora completa, girando. A porta atrás dela abre.
- **Texto:** *as seis abrem a mesma porta.*
- **HUD:** some.

### Q41 · A sala da máquina
- **Tela:** o saguão inteiro iluminado; no centro, a placa aberta — a mesma nos seis gabinetes. Seis setas saindo dela.
- **Texto:** *era a mesma placa. tudo o que ela pode fazer, ela faz esticando as direções que não consegue mudar.*
- **HUD:** ausente.

### Q42 · Fim
- **Tela:** escuro. A placa ainda ligada, sozinha, com um ponto de luz.
- **Texto:** *o concurso nunca foi pelo prêmio.*
- **HUD:** ausente.

---

## Checagem de repetição — leia esta lista de novo

**Constantes deliberadas** (a âncora):
- posição e desenho do HUD em Q07…Q39
- a sequência capa → cena → dica → miolo → chave em todas as fases

**Variações deliberadas:**

| Fase | Registro | Miolo | O que a fase possui |
|---|---|---|---|
| F1 | descoberta | 4 telas | diagnóstico e calibração |
| F2 | desconfiança | 4 telas | erro e verificação |
| F3 | orientação | 6 telas | progresso e distribuição |
| F4 | vertigem | 3 telas | hábito e ambiente |
| F5 | clareza | 5 telas | seleção e economia |
| F6 | quietude | 2 telas | pressão e identidade |

**Quadros que só existem uma vez no curso inteiro:** a grade (Q26), o confronto (Q38), a
fechadura girando (Q40), a sala da máquina (Q41), a placa sozinha (Q42).

**Quadros que se repetem de propósito:** o gabinete aceso — seis vezes, mas cada vez com mais
vizinhos acesos (1, 2, 3, 4, 5, 6). É acúmulo, não repetição.

**Pausas:** 12 no curso, 2 por fase, e **nenhuma pergunta se repete** — cada par é calibrado
pelo tópico que a fase possui (`MAPA-JOGADOR.md` §1).

**Quadros que NÃO existem:**
- boas-vindas a cada fase
- tela de vitória ao fim de cada fase
- chefe ao fim de cada fase
- grade deformada em toda fase
- a mesma dica reescrita

**Contagem:** 42 quadros, sendo 4 de Manual do Jogador (Q03–Q06), mais 12 pausas sobrepostas.
Uma imagem gerada por fase, seis no curso.
