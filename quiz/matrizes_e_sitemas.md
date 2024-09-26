# Quiz sobre Propriedades da Aritmética de Matrizes e Sistemas Lineares

1. Qual a diferença entre um sistema linear possível e determinado (SPD) e um sistema linear possível e indeterminado (SPI)?

<details>
<summary>Ver resposta</summary>

Um SPD possui uma única solução, enquanto um SPI possui infinitas soluções. Isso ocorre porque, em um SPI, existe pelo menos uma variável livre que pode assumir qualquer valor real, gerando infinitas soluções.
</details>

2. Descreva o método de resolução de sistemas lineares por adição.

<details>
<summary>Ver resposta</summary>

O método da adição consiste em somar as equações do sistema, após multiplicá-las por constantes convenientes, de forma a eliminar uma das variáveis. Repetindo o processo, obtém-se um sistema equivalente mais simples de resolver.
</details>

3. O que é a matriz aumentada de um sistema linear e qual a sua utilidade na resolução do sistema?

<details>
<summary>Ver resposta</summary>

A matriz aumentada de um sistema linear é formada pelos coeficientes das variáveis e pelos termos independentes das equações. Ela é útil pois permite aplicar o método de Gauss ou Gauss-Jordan para encontrar a solução do sistema.
</details>

4. Defina matriz identidade e explique qual a sua função na multiplicação de matrizes.

<details>
<summary>Ver resposta</summary>

A matriz identidade é uma matriz quadrada onde todos os elementos da diagonal principal são iguais a 1 e os demais são nulos. Sua função na multiplicação de matrizes é análoga à do número 1 na multiplicação de números reais, ou seja, AI = IA = A para qualquer matriz A compatível.
</details>

5. Qual a condição para que o produto de duas matrizes esteja definido?

<details>
<summary>Ver resposta</summary>

O produto de duas matrizes A (m x n) e B (p x q) só está definido se o número de colunas de A for igual ao número de linhas de B (n = p). Nesse caso, o produto AB será uma matriz de dimensões m x q.
</details>

6. Diferencie matrizes triangulares superiores de matrizes triangulares inferiores.

<details>
<summary>Ver resposta</summary>

Matrizes triangulares superiores possuem todos os elementos abaixo da diagonal principal iguais a zero, enquanto as matrizes triangulares inferiores possuem todos os elementos acima da diagonal principal iguais a zero.
</details>

7. O que significa dizer que uma matriz quadrada é invertível? Qual a relação entre a matriz inversa e a matriz identidade?

<details>
<summary>Ver resposta</summary>

Uma matriz quadrada A é invertível se existe uma matriz B, de mesma ordem, tal que AB = BA = I, onde I é a matriz identidade. A matriz B é a inversa de A e é denotada por A⁻¹.
</details>


8. Como você explicaria a multiplicação de matrizes para alguém que está aprendendo o conceito pela primeira vez? Por que a ordem da multiplicação é importante?

<details>
<summary>Ver resposta</summary>

A multiplicação de matrizes pode ser explicada como uma série de produtos internos entre as linhas da primeira matriz e as colunas da segunda. Cada elemento do resultado é a soma dos produtos dos elementos correspondentes de uma linha da primeira matriz com uma coluna da segunda. A ordem é importante porque A×B geralmente não é igual a B×A, e às vezes uma ordem pode estar definida enquanto a outra não.
</details>

9. Na aritmética comum, se AB = AC e A ≠ 0, podemos concluir que B = C. Por que isso nem sempre é verdade na multiplicação de matrizes?

<details>
<summary>Ver resposta</summary>

Na multiplicação de matrizes, AB = AC não implica necessariamente que B = C porque as matrizes podem ter propriedades especiais que "mascaram" diferenças quando multiplicadas. Por exemplo, se A tem uma linha ou coluna de zeros, essa parte da informação de B e C será "perdida" na multiplicação, permitindo que B e C sejam diferentes mesmo que AB = AC.
</details>

10. Qual o papel da matriz zero na álgebra matricial? Como ela se comporta na adição e na multiplicação de matrizes?

<details>
<summary>Ver resposta</summary>

A matriz zero funciona como o 0 na aritmética comum. Na adição, ela é o elemento neutro (A + 0 = A). Na multiplicação, ela é um elemento absorvente (A × 0 = 0 × A = 0). Ela "zera" qualquer matriz com a qual é multiplicada.
</details>

11. O que caracteriza uma matriz simétrica e onde esse tipo de matriz pode ser encontrado em aplicações do mundo real?

<details>
<summary>Ver resposta</summary>

Uma matriz simétrica é igual à sua transposta. Visualmente, ela é simétrica em relação à diagonal principal. Matrizes simétricas aparecem frequentemente em aplicações como análise de redes sociais, onde as conexões são bidirecionais, ou em física, representando certas propriedades de sistemas.
</details>

12. Compare as matrizes diagonais com as matrizes triangulares. Quais são suas principais características e em que situações elas são úteis?

<details>
<summary>Ver resposta</summary>

Matrizes diagonais têm elementos não-nulos apenas na diagonal principal, enquanto matrizes triangulares têm elementos não-nulos na diagonal principal e acima (superiores) ou abaixo (inferiores) dela. Ambas são úteis para simplificar cálculos e aparecem em decomposições matriciais importantes.
</details>

13. Como a matriz identidade se relaciona com o número 1 na aritmética comum? Explique sua importância na álgebra matricial.

<details>
<summary>Ver resposta</summary>

A matriz identidade funciona como o número 1 na multiplicação. Multiplicar qualquer matriz por ela não altera a matriz original (AI = IA = A). Ela é crucial em conceitos como inversão de matrizes e transformações lineares que preservam vetores.
</details>

14. Por que a comutatividade vale para a adição de matrizes, mas não para a multiplicação? Dê um exemplo intuitivo.

<details>
<summary>Ver resposta</summary>

A adição de matrizes é comutativa porque somamos os elementos correspondentes, e a ordem não importa (assim como com números). Na multiplicação, a ordem importa porque estamos realizando uma série de operações mais complexas que dependem da estrutura das matrizes, assim como a composição de funções não é geralmente comutativa.
</details>
