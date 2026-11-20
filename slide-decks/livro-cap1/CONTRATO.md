# CONTRATO — o livro do capítulo 1

Vale para **todo** fragmento em `partes/`. Se algo aqui não responde à sua dúvida, escolha a
opção mais simples e registre no comentário de fonte do fragmento. Não invente classe nova.

---

## 1. O que este livro é

Um **capítulo de livro** sobre a matéria do capítulo 1: equações lineares, o conjunto-solução,
sistemas, matrizes, eliminação gaussiana. Lê-se do começo ao fim, em prosa contínua, com
definições, exemplos resolvidos e exercícios.

O que ele **não** é: deck, roteiro de aula, HUD, aventura. A história do capítulo (o rapaz que
virou a noite, venceu uma vez e concluiu que a teoria funcionava) aparece **uma vez**, em prosa,
na abertura — e sai de cena. Depois disso o livro fala de matemática.

## 2. Voz

- Português do Brasil. Frases curtas. Nada de "vamos juntos nessa jornada".
- Trata o leitor por **você** apenas em exercício ("resolva", "confira"). No corpo do texto,
  impessoal: "uma equação linear é", "note que", "o conjunto-solução é".
- Toda afirmação matemática precisa ser verdadeira e verificável. Se não tiver certeza, não
  escreve — o revisor pega, mas a correção custa duas rodadas.
- **Sem motivacional.** Nada de "isso vai mudar sua vida" ou "no mundo real". O interesse vem do
  problema, não do anúncio.
- Analogias: só se você conseguir dizer, na mesma página, **onde ela para de valer**.

## 3. Vocabulário proibido no livro

`portão`, `chave`, `quest`, `chefe`, `jogador`, `HUD`, `gabinete`, `fliperama`,
`missão`, `pódio`.

**Exceção declarada (25/out):** `jogo` e `fase` são permitidos **apenas na moldura** — abertura
e fecho —, como analogia do curso, e não como aparelho da ficção. Nos interlúdios e nas seções
de matemática, não aparecem. A analogia não pode substituir explicação: onde ela para de valer
tem de estar dito na mesma página.

O verificador reprova o livro se qualquer uma aparecer. A ficção não entra aqui: se um trecho
precisa dela para fazer sentido, o trecho está errado.

## 4. Estrutura de um fragmento

```html
<!-- fonte: f1-matematica.html §1.5–1.6 -->
<section class="sec" id="s-1-5">
  <h2><span class="num">1.5</span>Sistema e solução</h2>
  <p>...</p>
</section>
```

- **Um arquivo = uma ou mais seções**, cada uma com `id="s-<número com hífen>"`: `s-1-5`, `s-1-13`.
- O `id` é o destino das referências cruzadas. Não repita.
- O número no `<span class="num">` é o mesmo do `id`, com ponto: `1.5`.
- A abertura (`00-abertura.html`) **não** é seção numerada: usa `<section class="sec" id="s-abertura">`
  e `<h2>` sem `num`.

## 4b. O mapa de seções (fixo — use estes ids e números)

| arquivo | id | número | assunto |
|---|---|---|---|
| `00-abertura.html` | `s-abertura` | — | abertura em prosa (sem número, `<h2>` sem `num`) |
| `10-s1-1.html` | `s-1-1` | 1.1 | equação linear |
| `11-s1-2.html` | `s-1-2` | 1.2 | a reta da geometria analítica |
| `12-s1-3.html` | `s-1-3` | 1.3 | o conjunto-solução |
| `13-s1-4.html` | `s-1-4` | 1.4 | por que desenhar não escala |
| `14-s1-5.html` | `s-1-5` | 1.5 | sistema e solução |
| `15-s1-6.html` | `s-1-6` | 1.6 | as três respostas |
| `16-s1-7.html` | `s-1-7` | 1.7 | matriz aumentada |
| `17-s1-8.html` | `s-1-8` | 1.8 | operações elementares |
| `18-s1-9.html` | `s-1-9` | 1.9 | forma escalonada e pivô |
| `19-s1-10.html` | `s-1-10` | 1.10 | protocolo de registro |
| `20-s1-11.html` | `s-1-11` | 1.11 | o pivô é escolhido |
| `21-s1-12.html` | `s-1-12` | 1.12 | o que a forma já diz |
| `22-s1-13.html` | `s-1-13` | 1.13 | exemplos resolvidos: 2×2 |
| `23-s1-14.html` | `s-1-14` | 1.14 | exemplos resolvidos: 3×3 |
| `24-s1-15.html` | `s-1-15` | 1.15 | exemplos resolvidos: retangulares |
| `25-s1-16.html` | `s-1-16` | 1.16 | exemplos resolvidos: 4×4 |
| `26-s1-17.html` | `s-1-17` | 1.17 | exemplos resolvidos: matrizes |
| `30-s1-18.html` | `s-1-18` | 1.18 | exercícios |
| `40-fim.html` | `s-fim` | — | glossário, notação e fontes |

Referência cruzada que aponta para seção inexistente **reprova** o livro. Só use ids desta tabela.

## 5. Classes permitidas (e só estas)

| Classe | Uso |
|---|---|
| `sec` | toda seção |
| `num` | número da seção, dentro do `h2`/`h3` |
| `def` | caixa de definição; dentro dela, `<span class="titulo">Definição</span>` |
| `ex` | caixa de exemplo; `<span class="titulo">Exemplo 3</span>` |
| `conta` | bloco monoespaçado (`<pre class="conta">`) para conta alinhada |
| `passos` | `<ol class="passos">` para passo a passo de eliminação |
| `obs` | observação à margem do texto, com `<b>Observação.</b>` |
| `cuidado` | armadilha/erro comum; `<span class="titulo">Cuidado</span>` |
| `gabarito` | `<details class="gabarito"><summary>Gabarito</summary>…</details>` |
| `ref` | link interno: `<a class="ref" href="#s-1-9">1.9</a>` |
| `fim` | só em `40-fim.html` |
| `titulo` | rótulo dentro de `def`/`ex`/`cuidado` |

Proibido: `<style>`, `style="..."`, `<font>`, `<center>`, `<br>` para espaçar, tabela para layout,
`<img>` (a v1 não tem figura).

## 6. Matemática

- Inline: `\( … \)`. Bloco: `\[ … \]`. **Uma barra.** `\\(` quebra o MathJax e o verificador reprova.
- Conta alinhada de sistema → `<pre class="conta">` com texto puro (sem `\(`), colunas alinhadas
  por espaço. É o que garante o alinhamento no papel e no PDF.
- Os números decimais usam vírgula: `0{,}5`.
- Nomes de função em `\operatorname{}`: `\operatorname{sen}`, `\operatorname{det}`.

## 7. A matemática é a mesma do quadro

Os exemplos resolvidos são **as 19 fichas** de `f1-matematica.html`, com os mesmos números, para
o aluno reencontrar o que copiou no caderno. Não invente exemplo novo com números diferentes; se
faltar um caso, use os que existem.

Todo resultado já foi conferido por `img-gen/grade-f1.py`. Não recalcule "de cabeça" e não
corrija um número que o script aprovou — se algo parecer errado, **pare e registre** no
comentário do fragmento.

## 8. Tamanho e ritmo

- Fragmento: **120 a 250 linhas**. Acima disso, divida em dois arquivos (o `build.py` ordena pelo
  nome, então `18-s1-9.html` vem antes de `19-s1-10.html`).
- Seção: 2 a 6 parágrafos, mais as caixas. Se passar de ~7 parágrafos, procure um subtítulo `h3`.
- Cada seção termina ligando na próxima por uma frase, não por "no próximo capítulo veremos".

## 9. O que o leitor precisa poder fazer ao fim de cada seção

Uma frase concreta, do tipo "dado um sistema 3×3, escrever a matriz aumentada e dizer se ele tem
uma, nenhuma ou infinitas soluções". Se a seção não entrega isso, ela está incompleta — mesmo que
esteja bonita.
