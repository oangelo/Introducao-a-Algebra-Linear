# Especificação e consultoria: a folha como documento de engenharia

**Status:** ideia registrada em 18/11/2026, na branch `feature/spec-consultoria`. Não aprovada
para a `main`; discussão na issue #— (esta mesma).
**Onde se aplica:** atividades de sala escritas (as folhas), em todos os três cursos.

---

## A tese em uma frase

A folha de sala já é uma especificação — definição em palavras, a fórmula, o que é cada símbolo,
um exemplo resolvido, por que funciona são os campos de uma spec de componente. Falta o **nome** e,
com ele, o **contrato de aceite**; a revisão do colega, pelo mesmo movimento, deixa de ser "olhar o
do colega" e passa a ser **consultoria com laudo**.

Não é camada nova de ficção: é o registro certo numa peça que já existe. É isso que separa imersão
de fantasia colada por cima.

## O que o frame conserta

- **O "ok, bom trabalho" morre por regra de ofício.** Laudo sem apontamento não é laudo. Todo
  laudo traz cláusula (qual critério, qual título), evidência (o ponto exato que não fecha),
  severidade e recomendação de uma linha.
- **A versão final vira revisão B, com changelog.** Cada correção cita a NC que a originou. O
  ganho deixa de ser "ficou melhor" e passa a ser contável: quantas NCs bloqueantes fecharam.
- **Severidade ganha significado matemático.** Bloqueante = a definição não decide um caso (o
  colega não consegue usar aquilo para resolver); menor = forma, clareza, letra.

## As três peças

1. **Especificação (revisão A)** — o rascunho, com consulta aberta.
2. **Laudo de consultoria** — o formulário de revisão: critérios de aceite marcados conforme/não
   conforme, e cada "não conforme" virando NC com evidência. Assinado.
3. **Especificação (revisão B)** — a versão sem consulta, com changelog de três linhas por NC.

O desenho atual não muda em nada além do nome e da obrigação de evidência: três tempos, tempos de
aula, colega da direita/esquerda, aceite/recusa, laudo não pontua, revisor não julga correção.

## Regras que impedem virar burocracia

- **Uma página de spec, meia de laudo.** Slot fixo; o formato não pontua, o critério pontua.
- **Três palavras só:** escopo, critério de aceite, não conformidade. Sem "stakeholder", sem
  requisito não funcional, sem empresa fictícia como cliente.
- **O cliente não é ficção:** é quem usa o documento depois do autor — o consultor naquela aula e
  ele mesmo na prova, sem consulta. É a resposta honesta para "por que escrever à mão, de cabeça".

## Onde encaixa no tema do curso

Convive com o gênero de cada repo no mesmo cabeçalho: **"Fase 3 — Especificação: a reta no plano"**.
"Fase" é vocabulário do curso e fica; "especificação" é o tipo de documento. O gênero da frente não
muda.

## Evidência e aposta (separadas de propósito)

- **Medido:** revisão com critério aproxima a nota do par da nota do professor — Falchikov &
  Goldfinch, *Review of Educational Research*, 2000, doi:10.3102/00346543070003287. Quem revisa
  aprende mais que quem é revisado — Lundstrom & Baker, *Journal of Second Language Writing*,
  2009, doi:10.1016/j.jslw.2008.06.002.
- **Não medido (aposta de desenho):** "spec de engenharia" como formato de recuperação em
  disciplina de matemática. Não há literatura. O frame se sustenta pela economia interna — critério,
  evidência, rastreabilidade — e é assim que ele deve ser julgado depois do piloto.

## Em aberto (decisões do Angelo)

- [ ] O laudo substitui o checklist atual ou convive com ele? (a proposta é conviver: o checklist
      é o critério de aceite, a NC é o que sai dele).
- [ ] Severidade em dois níveis (bloqueante / menor) ou três (+ "observação")?
- [ ] As NCs viram a metade anunciada da prova, como as lacunas do "o que eu li e não entendi"?
- [ ] Como isso conversa com a planilha de 10 atividades: a planilha conta entrega, a spec é o
      instrumento do capítulo. São registros diferentes — decidir se o capítulo consome uma
      coluna das 10 ou fica fora delas.
- [ ] Piloto: uma aula, medir tempo, NCs por laudo, % de NC sem evidência, % de bloqueantes
      fechadas na revisão B.
