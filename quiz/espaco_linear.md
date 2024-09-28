# Quiz sobre Espaços Vetoriais e Transformações Lineares

1. O que significa dizer que um conjunto de vetores é linearmente independente? E linearmente dependente?

<details>
<summary>Ver resposta</summary>

Um conjunto de vetores é linearmente independente se nenhum vetor pode ser escrito como combinação linear dos outros. É linearmente dependente se pelo menos um vetor pode ser escrito como combinação linear dos outros.
</details>

2. Qual a relação entre o conceito de base e o de dimensão de um espaço vetorial?

<details>
<summary>Ver resposta</summary>

Uma base é um conjunto linearmente independente que gera o espaço vetorial. A dimensão é o número de vetores em uma base.
</details>

3. O que é uma matriz de transição e para que serve?

<details>
<summary>Ver resposta</summary>

Uma matriz de transição permite mudar de uma base para outra. Multiplicando o vetor de coordenadas na base antiga pela matriz de transição, obtemos o vetor de coordenadas na nova base.
</details>

4. Qual a diferença entre um espaço vetorial de dimensão finita e um espaço vetorial de dimensão infinita? Dê um exemplo de cada.

<details>
<summary>Ver resposta</summary>

Um espaço vetorial de dimensão finita possui uma base com um número finito de vetores, como $\mathbb{R}^n$. Um espaço vetorial de dimensão infinita não possui uma base finita, como o espaço de todas as funções contínuas.
</details>

5. O que é o espaço gerado por um conjunto de vetores? Dê um exemplo.

<details>
<summary>Ver resposta</summary>

O espaço gerado por um conjunto de vetores é o conjunto de todas as combinações lineares possíveis desses vetores. Por exemplo, o espaço gerado por (1,0) e (0,1) é $\mathbb{R}^2$.
</details>

6. O que significa dizer que um vetor v é uma combinação linear dos vetores v1, v2, ..., vn?

<details>
<summary>Ver resposta</summary>

Significa que v pode ser escrito na forma $c_1v_1 + c_2v_2 + ... + c_nv_n$, onde $c_1, c_2, ..., c_n$ são escalares.
</details>

7. O que é uma transformação matricial?

<details>
<summary>Ver resposta</summary>

Uma transformação matricial é uma função entre espaços vetoriais definida pela multiplicação de um vetor por uma matriz.
</details>

8. Explique a diferença entre posto e nulidade de uma matriz.

<details>
<summary>Ver resposta</summary>

O posto de uma matriz é a dimensão do seu espaço coluna (ou linha), que representa o número de linhas (ou colunas) linearmente independentes. A nulidade é a dimensão do espaço nulo da matriz, que representa o número de soluções linearmente independentes para $Ax=0$.
</details>

9. Dê um exemplo de um operador linear em $\mathbb{R}^2$ e descreva seu efeito geométrico.

<details>
<summary>Ver resposta</summary>

Um exemplo é a rotação em torno da origem em $\mathbb{R}^2$. Ela gira cada vetor por um ângulo fixo, mantendo o comprimento do vetor.
</details>

10. Explique o conceito de span (espaço gerado) e como ele se relaciona com a ideia de base de um espaço vetorial.

<details>
<summary>Ver resposta</summary>

O span de um conjunto de vetores $S = \{v_1, v_2, ..., v_r\}$ é o conjunto de todas as combinações lineares possíveis desses vetores. Uma base é um conjunto de vetores linearmente independentes cujo span é igual ao espaço vetorial inteiro. Assim, a base é o menor conjunto de vetores que gera todo o espaço vetorial.
</details>

11. O que são o espaço linha, espaço coluna e espaço nulo de uma matriz? Como eles se relacionam?

<details>
<summary>Ver resposta</summary>

Para uma matriz $A_{m \times n}$:
- Espaço Linha: Subespaço de $\mathbb{R}^n$ gerado pelos vetores linha de $A$
- Espaço Coluna: Subespaço de $\mathbb{R}^m$ gerado pelos vetores coluna de $A$
- Espaço Nulo: Subespaço de $\mathbb{R}^m$ que é solução de $Ax = 0$

Eles se relacionam através do Teorema do Posto-Nulidade: $posto(A) + nulidade(A) = n$, onde o posto é a dimensão comum do espaço linha e do espaço coluna.
</details>

12. Enuncie e explique o Teorema da Solução Geral para sistemas lineares.

<details>
<summary>Ver resposta</summary>

O Teorema da Solução Geral afirma que se $x_0$ é uma solução particular de $Ax = b$, e $v_1, v_2, ..., v_k$ formam uma base para o espaço nulo de $A$, então toda solução do sistema é da forma:

$x = x_0 + c_1v_1 + c_2v_2 + ... + c_kv_k$

onde os $c_i$'s são constantes reais. Isso significa que a solução geral é composta de uma solução particular mais qualquer combinação linear de vetores do espaço nulo.
</details>

13. Como o conceito de posto (rank) de uma matriz se relaciona com a solução de sistemas lineares?

<details>
<summary>Ver resposta</summary>

O posto de uma matriz está diretamente relacionado à solução de sistemas lineares. Para um sistema consistente $Ax = b$ com $m$ equações, $n$ incógnitas e $A$ de posto $r$:

- Se $r = n$, o sistema tem uma única solução.
- Se $r < n$, o sistema tem infinitas soluções, com $n-r$ parâmetros livres.
- Se $r < m$, algumas equações são redundantes.

O posto determina o número de equações linearmente independentes e, consequentemente, a natureza da solução do sistema.
</details>

14. O que são autovalores e autovetores de uma matriz? Como eles são calculados?

<details>
<summary>Ver resposta</summary>

Autovalores ($\lambda$) e autovetores ($v$) de uma matriz $A$ são escalares e vetores não-nulos que satisfazem a equação $Av = \lambda v$. Para encontrá-los:

1. Resolva a equação característica $det(A - \lambda I) = 0$ para encontrar os autovalores.
2. Para cada autovalor $\lambda$, resolva $(A - \lambda I)v = 0$ para encontrar os autovetores correspondentes.

Autovetores representam direções especiais em que a transformação linear associada à matriz $A$ age apenas como uma multiplicação por escalar.
</details>
