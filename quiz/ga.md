# Quiz sobre Vetores e Geometria Analítica

1. Explique a diferença entre vetores equivalentes e vetores iguais.

<details>
<summary>Ver resposta</summary>

Vetores equivalentes possuem o mesmo comprimento, direção e sentido, mas podem ter diferentes pontos iniciais. Vetores iguais são equivalentes e possuem o mesmo ponto inicial.
</details>

2. Descreva geometricamente a adição de vetores usando a regra do paralelogramo.

<details>
<summary>Ver resposta</summary>

Para somar dois vetores geometricamente usando a regra do paralelogramo, posicione os vetores de forma que seus pontos iniciais coincidam. Em seguida, construa um paralelogramo usando esses vetores como lados adjacentes. A diagonal do paralelogramo que se origina no ponto inicial comum dos vetores representa a soma vetorial.
</details>

3. O que acontece com o comprimento e o sentido de um vetor quando ele é multiplicado por um escalar negativo?

<details>
<summary>Ver resposta</summary>

Quando um vetor $\vec{v}$ é multiplicado por um escalar negativo $k$, seu comprimento é multiplicado pelo valor absoluto do escalar $|k|$, e seu sentido é invertido. Matematicamente: $k\vec{v} = (k\vec{v}_x, k\vec{v}_y, k\vec{v}_z)$.
</details>

4. Como você pode determinar se dois vetores em $\mathbb{R}^n$ são colineares?

<details>
<summary>Ver resposta</summary>

Dois vetores $\vec{u}$ e $\vec{v}$ em $\mathbb{R}^n$ são colineares se um for um múltiplo escalar do outro. Isso significa que existe um escalar $k$ tal que $\vec{u} = k\vec{v}$ ou $\vec{v} = k\vec{u}$.
</details>

5. Qual é a relação entre as coordenadas de um ponto e os componentes de um vetor que vai da origem até esse ponto?

<details>
<summary>Ver resposta</summary>

As coordenadas de um ponto $P(x, y, z)$ e os componentes do vetor $\vec{OP}$ que vai da origem $O(0, 0, 0)$ até esse ponto são numericamente iguais: $\vec{OP} = (x, y, z)$.
</details>

6. Como os vetores unitários canônicos são definidos em $\mathbb{R}^n$?

<details>
<summary>Ver resposta</summary>

Os vetores unitários canônicos em $\mathbb{R}^n$ são denotados por $\vec{e}_1, \vec{e}_2, ..., \vec{e}_n$, onde cada $\vec{e}_i$ possui um 1 na $i$-ésima posição e 0 nas demais. Por exemplo, em $\mathbb{R}^3$: $\vec{e}_1 = (1,0,0)$, $\vec{e}_2 = (0,1,0)$, $\vec{e}_3 = (0,0,1)$.
</details>

7. Explique como a distância entre dois pontos em $\mathbb{R}^n$ é calculada.

<details>
<summary>Ver resposta</summary>

A distância $d$ entre dois pontos $P_1(x_1, y_1, ..., z_1)$ e $P_2(x_2, y_2, ..., z_2)$ em $\mathbb{R}^n$ é calculada usando a fórmula da distância euclidiana:

$d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2 + ... + (z_2-z_1)^2}$
</details>

8. O que significa dizer que dois vetores não nulos em $\mathbb{R}^n$ são ortogonais?

<details>
<summary>Ver resposta</summary>

Dois vetores não nulos $\vec{u}$ e $\vec{v}$ em $\mathbb{R}^n$ são ortogonais se o produto escalar entre eles for igual a zero: $\vec{u} \cdot \vec{v} = 0$. Geometricamente, isso significa que os vetores formam um ângulo reto entre si.
</details>

9. Escreva a fórmula para o produto escalar de dois vetores em $\mathbb{R}^n$, tanto em termos de seus componentes quanto em termos de seus comprimentos e do ângulo entre eles.

<details>
<summary>Ver resposta</summary>

O produto escalar de dois vetores $\vec{u} = (u_1, u_2, ..., u_n)$ e $\vec{v} = (v_1, v_2, ..., v_n)$ em $\mathbb{R}^n$ pode ser calculado de duas maneiras:

* Componentes: $\vec{u} \cdot \vec{v} = u_1v_1 + u_2v_2 + ... + u_nv_n$
* Comprimentos e ângulo: $\vec{u} \cdot \vec{v} = \|\vec{u}\| \|\vec{v}\| \cos \theta$, onde $\theta$ é o ângulo entre $\vec{u}$ e $\vec{v}$.
</details>

10. Qual é a relação geométrica entre um vetor $\vec{u}$, um vetor não nulo $\vec{a}$ e a projeção ortogonal de $\vec{u}$ sobre $\vec{a}$?

<details>
<summary>Ver resposta</summary>

A projeção ortogonal de $\vec{u}$ sobre $\vec{a}$ é um vetor $\vec{w}_1$ que é um múltiplo escalar de $\vec{a}$ e é paralelo a $\vec{a}$. O vetor diferença $\vec{w}_2 = \vec{u} - \vec{w}_1$ é ortogonal a $\vec{a}$. Matematicamente, a projeção é dada por:
$$\vec{w}_1 = proj_{\vec{a}}\vec{u} = $$
$$= \frac{\vec{u} \cdot \vec{a}}{\|\vec{a}\|^2}\vec{a}$$
</details>


