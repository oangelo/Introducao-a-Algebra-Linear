# Quiz sobre Autovalores e Autovetores

1. Defina autovalor e autovetor de uma matriz $A$.

<details>
<summary>Ver resposta</summary>

Um autovetor $\vec{v}$ de uma matriz $A$ é um vetor não nulo que, ao ser multiplicado por $A$, resulta em um múltiplo escalar de si mesmo. Esse escalar $\lambda$ é chamado de autovalor associado ao autovetor. Matematicamente:

$A\vec{v} = \lambda\vec{v}$, onde $\vec{v} \neq \vec{0}$ e $\lambda$ é um escalar.
</details>

2. Qual a relação entre a equação característica de uma matriz e seus autovalores?

<details>
<summary>Ver resposta</summary>

Os autovalores de uma matriz são as raízes da sua equação característica, que é obtida calculando o determinante da matriz $(\lambda I - A)$, onde $\lambda$ é uma variável escalar e $I$ é a matriz identidade. A equação característica é dada por:

$\det(\lambda I - A) = 0$
</details>

3. Descreva o processo para encontrar os autovetores correspondentes a um dado autovalor.

<details>
<summary>Ver resposta</summary>

Para encontrar os autovetores correspondentes a um dado autovalor $\lambda$, substituímos o autovalor na equação $(\lambda I - A)\vec{x} = \vec{0}$ e resolvemos o sistema linear homogêneo para encontrar os vetores não nulos $\vec{x}$ que satisfazem a equação.
</details>

4. O que significa dizer que uma matriz é diagonalizável?

<details>
<summary>Ver resposta</summary>

Uma matriz $A$ é diagonalizável se for semelhante a uma matriz diagonal, ou seja, se existir uma matriz invertível $P$ tal que $P^{-1}AP = D$, onde $D$ é uma matriz diagonal.
</details>

5. Qual a condição necessária e suficiente para que uma matriz seja diagonalizável?

<details>
<summary>Ver resposta</summary>

Uma matriz quadrada de ordem $n$ é diagonalizável se, e somente se, possuir $n$ autovetores linearmente independentes.
</details>

6. Como os autovalores e autovetores podem ser usados para calcular potências de uma matriz?

<details>
<summary>Ver resposta</summary>

Se $A$ é diagonalizável, então $A^n = PD^nP^{-1}$, onde $D$ é a matriz diagonal dos autovalores de $A$ e $P$ é a matriz cujas colunas são os autovetores correspondentes. Como $D$ é diagonal, $D^n$ é obtida elevando cada elemento da diagonal à potência $n$, o que simplifica o cálculo de $A^n$.
</details>

7. Explique o conceito de multiplicidade algébrica e geométrica de um autovalor.

<details>
<summary>Ver resposta</summary>

A multiplicidade algébrica de um autovalor é o número de vezes que ele aparece como raiz da equação característica. 

A multiplicidade geométrica é a dimensão do autoespaço associado a esse autovalor, ou seja, o número de autovetores linearmente independentes associados a ele. Matematicamente, é a dimensão do núcleo de $(A - \lambda I)$, onde $\lambda$ é o autovalor em questão.
</details>

8. O que são autovalores e autovetores complexos?

<details>
<summary>Ver resposta</summary>

Autovalores e autovetores complexos são extensões desses conceitos para o domínio dos números complexos $\mathbb{C}$. Eles surgem quando a equação característica de uma matriz possui raízes complexas. Um autovalor complexo $\lambda = a + bi$ satisfaz $A\vec{v} = (a + bi)\vec{v}$, onde $\vec{v}$ é um autovetor complexo.
</details>

9. Como interpretar geometricamente os autovalores complexos de uma matriz 2x2 real?

<details>
<summary>Ver resposta</summary>

Geometricamente, os autovalores complexos de uma matriz 2x2 real representam uma rotação e uma dilatação ou contração no plano. Se $\lambda = a + bi$ é um autovalor complexo:

- O ângulo de rotação é dado por $\theta = \arg(\lambda) = \arctan(\frac{b}{a})$
- O fator de dilatação/contração é dado pelo módulo $|\lambda| = \sqrt{a^2 + b^2}$
</details>

10. Cite uma aplicação de autovalores e autovetores na resolução de problemas.

<details>
<summary>Ver resposta</summary>

Uma aplicação de autovalores e autovetores é na resolução de sistemas de equações diferenciais lineares de primeira ordem. 

Para um sistema da forma $\frac{d\vec{x}}{dt} = A\vec{x}$, onde $A$ é uma matriz constante, diagonalizando $A$ como $A = PDP^{-1}$, podemos desacoplar as equações e resolvê-las independentemente na forma $\frac{d\vec{y}}{dt} = D\vec{y}$, onde $\vec{y} = P^{-1}\vec{x}$.
</details>
