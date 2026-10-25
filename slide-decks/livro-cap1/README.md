# CAPÍTULO 1 — edição de leitura

**Arquivo publicado:** [`capitulo-1.html`](capitulo-1.html)

Uma leitura contínua do capítulo 1: a história e a matemática no mesmo fio, com as dez cenas
intercaladas. Não tem sumário, glossário, exercícios nem apêndice — só o texto, na ordem em que
se lê.

## Como é montado

```
capitulo.json   ← o manifesto: título, capa e a ORDEM dos blocos (partes e cenas)
partes/         ← o texto, um fragmento por seção (fonte: CONTRATO.md)
tema.css        ← o template visual; troque --acento para o próximo capítulo
build.py        ← monta capitulo-1.html a partir do manifesto
verificar.py    ← confere o contrato no arquivo montado
nao-usados/     ← o que ficou fora desta edição (exercícios, glossário) e a v1 do build
```

Montar: `python3 build.py && python3 verificar.py capitulo-1.html`

## Para o próximo capítulo

1. `cp capitulo.json capitulo-2.json` e troque título, kicker, capa e a lista de blocos.
2. Escreva os fragmentos em `partes/` seguindo o `CONTRATO.md`.
3. Se quiser outra cor de acento: `--acento` no `tema.css` (ou um `tema-cap2.css` que importa o base).
4. `python3 build.py capitulo-2.json`.

O build **falha** se faltar fragmento ou se alguma imagem referenciada não existir no disco.

## Qualidade: rubrica, baseline e anti-regressão

O problema que isso resolve: melhorar uma parte e piorar outra. Cada fragmento narrativo tem nota
em oito critérios, e a nota fica gravada em `baseline.json`.

```
rubrica.json      ← critérios, pesos, vocabulário proibido, padrões motivacionais
interludios.json  ← o mapa: onde cada fragmento entra, que conceito amarra, que objeto entrega
avaliar.py        ← mede o que é medível; lê criticas.json (julgamento dos críticos) e funde
baseline.json     ← a versão aceita: notas por fragmento + impressão do texto de matemática
qualidade.json    ← o resultado da última avaliação
```

Rodar: `python3 avaliar.py` (falha se média < 7,5, se algum critério < 6, ou se qualquer nota cair
em relação ao baseline). Congelar uma versão aprovada: `python3 avaliar.py --congelar`.

**Camada determinística** (C3 vocabulário, C6 entrega, C7 tamanho, C8 legibilidade, parte de C2 e
C4): `avaliar.py`. **Camada de julgamento** (C1 amarração, C2 fonte, C4 motivação, C5
continuidade): críticos cegos, que devolvem só defeito localizado — trecho, critério, gravidade.

As **17 seções de matemática são congeladas por impressão digital do texto**. Se alguém editar uma
delas (ou se a integração mexer sem querer), o avaliador reprova até que a mudança seja autorizada
com `--permitir-matematica`.
