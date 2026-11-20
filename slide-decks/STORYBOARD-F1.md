# Storyboard — Fase 1 · Sistemas e Matrizes

Piloto. Se este formato funcionar, as outras cinco fases seguem iguais.

**Herda** os quadros Q11–Q15 de [`STORYBOARD-GERAL.md`](STORYBOARD-GERAL.md). Este documento
abre esses cinco quadros em **nove telas**, acrescenta **duas pausas** e **nomeia a imagem de
cada tela**.

**Tema não-matemático desta fase:** atenção e calibração
([`MAPA-JOGADOR.md`](MAPA-JOGADOR.md)). A dica (Q13) traz o corpo — atenção é pré-requisito de
perceber; as duas pausas trazem a calibração.

---

## 1. Inventário de imagem da fase

Nove telas. **Uma** imagem gerada; o resto é diagrama em SVG. Isso não é economia — é a
fronteira da [`BIBLIA.md`](BIBLIA.md) §3: se o slide tem conta, a imagem é SVG.

| Tela | Tipo de imagem | O que é |
|---|---|---|
| F1-01 capa | SVG (silhueta) | o saguão com o gabinete 1 aceso e a fechadura vazia |
| F1-02 cena | **gerada** | a sala de interrogatório, as três pastas |
| F1-03 dica | reaproveita F1-02 | a mesma cena, escurecida |
| F1-04 estado | SVG | o mapa dos 4 problemas da fase |
| F1-05 tópico | SVG | matriz aumentada |
| F1-06 tópico | SVG | a escada dos pivôs |
| F1-07 tópico | SVG | \(AB \neq BA\) |
| F1-08 tópico | SVG | a ida e a volta \(A \to A^{-1}\) |
| F1-09 chave | SVG | a fechadura com o primeiro buraco aceso |

**Regra da fase:** nenhuma fórmula dentro de imagem gerada. A cena nunca mostra número, letra
legível nem equação — modelo de difusão inventa símbolo e o aluno acredita.

---

## 2. Quadro por quadro

### F1-01 · Capa
- **Tela:** silhueta do saguão, escuro; só o gabinete 1 aceso, em âmbar. A fechadura de seis buracos ao lado, vazia. Título grande, centralizado no alto.
- **Imagem (SVG):** seis retângulos em perspectiva, um preenchido em âmbar com brilho, os outros cinco em contorno cinza; à direita, um aro com seis furos escuros. Sem personagem.
- **Texto:** *PORTÃO 1 — SISTEMAS E MATRIZES*
- **HUD:** `P1 · CHAVES 0/6` — aparece pela primeira vez no curso.
- **Em sala:** o professor não lê a capa. Ela fica enquanto ele diz o que a fase resolve.

### F1-02 · Cena
- **Tela:** a imagem ocupa tudo. Uma linha de texto no canto inferior esquerdo.
- **Imagem (gerada):** sala de interrogatório à noite. Uma lâmpada baixa sobre a mesa; **três pastas abertas** em leque; **uma cadeira vazia** do outro lado. Persiana ao fundo, a luz da rua cortando o ar em faixas finas. Silhueta de um detetive de chapéu, de costas para a câmera, **sem rosto**. Fumaça fina. Preto e âmbar, contraste alto, grão de filme.
  **Negativo:** nenhum texto legível, nenhum numeral, nenhuma fórmula, nenhuma escrita em pasta, quadro ou papel. Se o modelo escrever algo, a imagem é descartada.
- **Texto:** *três depoimentos. ninguém viu tudo.*
- **HUD:** `P1 · CHAVES 0/6`
- **Por que esta cena:** as três pastas são as três equações; a cadeira vazia é a incógnita. A cena tem que ser o **problema**, não a metáfora dele — ver §5.

### F1-03 · Dica de carregamento — corpo
- **Tela:** a mesma cena de F1-02, com véu escuro a 60%. A dica no canto inferior, sozinha.
- **Imagem:** reaproveita F1-02 — zero custo.
- **Texto:** *Atenção vem antes de calibração. Vinte minutos de caminhada antes de sentar mudam o que você consegue notar.*
- **HUD:** `P1 · CHAVES 0/6`
- **Camada do jogador:** é a única dica da fase. A fase possui **atenção e calibração** — o corpo dá a atenção, as pausas dão a calibração com a autoexplicação: dizer em voz alta *por que* aquele sistema não tem solução.

### F1-04 · Estado
- **Tela:** o mapa da fase. Quatro caixas em fila, a primeira destacada — onde estamos agora.
- **Imagem (SVG):** quatro retângulos com rótulo curto: *sistema*, *escada*, *produto*, *volta*. O primeiro aceso em âmbar.
- **Texto:** *quatro problemas, quatro telas. Nenhum deles é uma conta longa.*
- **HUD:** `P1 · CHAVES 0/6`
- **Função:** é o quadro que o aluno olha ao voltar do celular. Responde "onde eu estou" em dois segundos.

### F1-05 · Tópico — sistemas lineares
- **Tela:** uma matriz aumentada grande, à esquerda; à direita, três rótulos curtos empilhados.
- **Imagem (SVG):** colchetes, três linhas de coeficientes, barra vertical separando a coluna dos termos independentes. Os três rótulos: *uma solução · infinitas · nenhuma*.
- **Texto:** o enunciado do exercício que vai ao quadro.
- **HUD:** `P1 · SISTEMAS · CHAVES 0/6`
- **Em sala:** o slide fica; a classificação é construída no quadro, não revelada aqui.

> **Pausa 1** (sobreposição, véu escuro sobre esta tela): *Qual destes quatro você resolve sem
> olhar? Qual você evita?* — a pergunta existe para o aluno separar o que ele **sabe** do que ele
> **reconhece**.

### F1-06 · Tópico — eliminação gaussiana
- **Tela:** a matriz com os pivôs destacados e a escada desenhada por cima.
- **Imagem (SVG):** os números da matriz em cinza; os pivôs em âmbar; uma linha fina ligando os pivôs em degraus, descendo da esquerda para a direita. **Sem** seta indicando operação — a operação é do quadro, não do slide.
- **Texto:** o enunciado do exercício.
- **HUD:** `P1 · ELIMINAÇÃO · CHAVES 0/6`

### F1-07 · Tópico — produto de matrizes
- **Tela:** duas multiplicações lado a lado, uma riscada.
- **Imagem (SVG):** à esquerda \(AB\), à direita \(BA\), com sinal de diferente entre elas e um traço diagonal sobre a segunda. Sem números — só as letras.
- **Texto:** *a ordem importa.*
- **HUD:** `P1 · PRODUTO · CHAVES 0/6`
- **Nota:** é a semente da Fase 4, onde a composição de transformações cobra o preço. Não explicar agora.

### F1-08 · Tópico — matriz inversa
- **Tela:** um ciclo de três paradas.
- **Imagem (SVG):** \(A \to A^{-1} \to I\), seta curvada voltando de \(I\) para \(A\) por baixo, formando o laço. A volta em âmbar; a ida em cinza.
- **Texto:** o enunciado do exercício.
- **HUD:** `P1 · INVERSA · CHAVES 0/6`
- **Nota:** o laço é a imagem que a Fase 2 reabre com o determinante. Mesma forma, outra pergunta.

> **Pausa 2** (sobreposição): *O que você explicaria hoje que não explicava ontem?* — a pergunta
> mede progresso por compreensão, não por horas.

### F1-09 · Chave
- **Tela:** a fechadura, com o primeiro buraco aceso. Nada mais.
- **Imagem (SVG):** o aro de seis furos; o primeiro em âmbar, os cinco em cinza escuro.
- **Texto:** *chave 1 — o estado*
- **HUD:** `CHAVES 1/6`
- **Em sala:** nenhum som, nenhuma animação de comemoração. O professor segue para o exercício seguinte.

---

## 3. O que não tem imagem

- **Nenhuma grade deformada.** Ela é da Fase 4, uma única vez no curso (Q30). Aqui seria decoração.
- **Nenhuma cena por tópico.** A fase tem uma cena, em F1-02. Repetir cena a cada tópico é o erro que a versão atual comete.
- **Nenhum retrato de matemático.** O DEV LOG virou créditos com dívida técnica (BÍBLIA §6); isso é uma tela por fase, não um retrato por tópico.
- **Nada de sono ou estudo em grupo.** São das Fases 3 e 2 — aqui o corpo aparece como atenção, não como saúde. O capítulo 1 (Q01–Q10) entrega o método; esta fase não o reensina.

---

## 4. Checagem contra as outras fases

Antes de aprovar esta fase, conferir que ela não invade:

- **F2** — determinante não aparece em nenhuma tela; nem a palavra, nem o símbolo \(|A|\).
- **F3** — nenhuma interpretação geométrica do conjunto-solução. A matriz é tabela, não plano.
- **F4** — nenhuma transformação, nenhuma grade, nenhuma seta no espaço.
- **F5** — as palavras *posto*, *nulidade*, *base*, *span* não aparecem.
- **Capítulo 1 (Q01–Q10)** — o método não volta aqui: esta fase aplica, não reensina.

E que ela **entrega** o que as outras vão usar: escalonamento (F2, F5), inversa (F4),
não comutatividade (F4).

---

## 5. A história da fase — noir

**O cenário.** Delegacia, madrugada. Uma lâmpada, uma mesa, três pastas, uma cadeira vazia. O
jogador é o detetive — chapéu, sem rosto, de costas.

**O caso.** Uma noite, três testemunhas. Nenhuma viu tudo: cada uma descreve um pedaço. Juntas,
os pedaços fecham o caso — ou não.

**As três armadilhas, que são a fase inteira:**

1. **Um depoimento repete o outro.** Duas testemunhas contam a mesma história com palavras
   diferentes. Parece informação nova; não é. O caso fica **em aberto** — não por falta de
   testemunha, mas por falta de informação **independente**.
2. **Um depoimento contradiz os outros dois.** Não existe cena que satisfaça os três ao mesmo
   tempo. O caso **não fecha** — e insistir nele é o erro, não a dificuldade.
3. **Os depoimentos que sobram se sustentam.** Um culpado, um caminho. O caso **fecha**.

**O que isso é, em matemática:** depoimento = equação; testemunha redundante = linha dependente;
contradição = sistema impossível; caso que fecha = solução única.

**A fala do fim.** O detetive não pergunta quem foi:

> *"Não perguntei quem foi. Perguntei se dá para saber."*

É por isso que a chave é **o estado**.

**Regra de ouro:** a cena não contém número e os slides de tópico não contêm história. A história
dá a ocasião; o exercício dá o problema. Se o slide de tópico precisar da história para
funcionar, ele está errado.

### O que não se herda do material antigo

As narrações em áudio foram descartadas (out/2026): antigas e defasadas. O
`scripts/matrizes_e_sistemas.md` fica como registro — não é fonte de gênero, de cena nem de
fala.

O conflito de terminologia continua válido, e não depende do áudio: **"Chefe" já significa
prova** (`AGENTS.md` da raiz). Se o beat da F6 também se chamasse "chefe", o aluno não
distinguiria o confronto narrativo da prova. **Decisão:** o beat da F6 chama-se **confronto
final**; "Chefe" fica reservado para prova.

---

## 6. Pendências

- **Gerador de imagem bloqueado.** F1-02 é a única tela que depende dele. As outras oito são
  SVG e podem ser implementadas hoje.
- As duas pausas são sobreposição no Reveal (`fragment` + véu), não telas próprias. Se o
  Reveal complicar a sobreposição, viram telas — custa dois cliques a mais.
- A cena de F1-02 (noir) é a única tela que depende do gerador. As outras oito são SVG.
