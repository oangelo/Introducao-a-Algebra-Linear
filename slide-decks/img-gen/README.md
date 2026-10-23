# img-gen — harness de imagem do curso

Gera as cenas da Camada B em lote, com o personagem fixo por **imagem de referência**.

Inspirado no que o Emm (scenario.com) descreveu ao fazer um quadrinho de 908 páginas com
personagens consistentes: **reference images, agents and a tight harness**. A ideia que vale
copiar não é a ferramenta dele — é a separação:

- o **agente** escreve o manifesto (texto, sem GPU);
- o **harness** executa em lote, com parâmetros travados;
- a **referência** é um arquivo, não uma descrição.

## Por que harness e não chamada solta

Cada chamada ao `qwen-image.sh` **para e religa o llama-cpp** (o modelo de chat ocupa ~25 GB
dos 24 GiB da 7900 XTX). Dezesseis cenas chamadas soltas = dezesseis ciclos, e o chat dos
agentes cai dezesseis vezes.

`gen.sh` faz um ciclo só: para no começo, gera tudo com `--no-cycle`, religa no fim — com
`trap`, inclusive se for interrompido ou der erro no meio.

## Uso

```bash
# no Oráculo
cd /mnt/Volatil/sdcpp
./gen.sh cenas.tsv                 # todas
./gen.sh cenas.tsv --only f1       # só o que começa com "f1"

# de volta no agente
../img-gen/fetch.sh                # traz os PNG de out/ para img/
```

## O manifesto (`cenas.tsv`)

Tab-separado, uma cena por linha:

| coluna | o que é |
|---|---|
| `name` | nome do arquivo de saída, sem extensão. Use o nome do quadro (`f1-02`, `c7-estante`) |
| `model` | `turbo` (padrão, composição limpa) ou `flux3` (mais rico, arrisca pseudo-texto) |
| `w` `h` | resolução. Teto ~1,4 MP; `1152x864` é o formato de slide |
| `seed` | **fixo por cena**. Mudar a seed muda o desenho; se a cena ficar boa, a seed é o que permite regerar |
| `ref` | `y` passa `jogador-capuz.png` como referência; `n` não passa |
| `prompt` | descrição da cena, em inglês. **Nunca** pede texto |
| `extra_negativo` | negativo específico da cena, somado ao base |

**Quando `ref=y`:** só quando o jogador aparece. Referência de personagem injeta o personagem —
passar num plano de objeto devolve o moletom no meio de uma pilha de papéis.

## As regras que não são negociáveis

1. **Texto nunca vem do modelo.** Ele inventa letra e o aluno acredita. O negativo base já
   proíbe `text, letters, words, writing`; ainda assim, se aparecer qualquer letra legível, a
   imagem é **descartada**, não corrigida.
2. **Nada de número, fórmula ou objeto matemático em imagem gerada.** Diagrama é SVG.
3. **O rosto não existe.** Capuz, sombra, costas. É o que mantém a pessoa a mesma entre cenas.
4. **Prompt não menciona a história do curso.** A cena mostra o **problema**, não a metáfora
   dele. Se a legenda precisar explicar a imagem, a imagem está errada.
5. **Seed é registro.** Se uma cena for aprovada, a seed dela não muda mais — é o que permite
   regerar idêntico quando o modelo for trocado.

## O personagem

`img/personagens/jogador-capuz.png` — três vistas, capuz, sem rosto. É a referência canônica do
curso inteiro. Cópia de trabalho no Oráculo em `/mnt/Volatil/sdcpp/ref/jogador-capuz.png`.

**Regra:** o capuz é a assinatura dele. O mundo muda a roupa (sobretudo no noir, armadura no
FPS), o capuz fica. É o que faz o aluno reconhecer o mesmo jogador nas seis fases.

## Checklist antes de aprovar uma cena

- [ ] tem texto, número ou letra legível? → descartar
- [ ] o rosto aparece? → descartar
- [ ] o personagem é o mesmo da referência? → conferir capuz e silhueta
- [ ] a cena é o problema, ou é decoração? → se é decoração, não entra
- [ ] a composição deixa espaço para a linha de texto do slide? → a legenda vive no canto
