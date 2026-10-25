## Questão 1:

**Passo 1: Escrever o sistema como um produto de matrizes**

O sistema de equações lineares dado é:

\[
\begin{cases}
5x_1 + 3x_2 + 2x_3 = 4 \\
3x_1 + 3x_2 + 2x_3 = 2 \\
0x_1 + 1x_2 + 1x_3 = 5
\end{cases}
\]

Podemos representar este sistema na forma matricial \( AX = B \), onde:

- \( A \) é a matriz dos coeficientes,
- \( X \) é o vetor das incógnitas,
- \( B \) é o vetor dos termos constantes.

Escrevendo as matrizes:

\[
A = \begin{bmatrix}
5 & 3 & 2 \\
3 & 3 & 2 \\
0 & 1 & 1 \\
\end{bmatrix}, \quad
X = \begin{bmatrix}
x_1 \\
x_2 \\
x_3 \\
\end{bmatrix}, \quad
B = \begin{bmatrix}
4 \\
2 \\
5 \\
\end{bmatrix}
\]

**Passo 2: Encontrar a inversa da matriz dos coeficientes \( A \)**

Para encontrar a inversa de \( A \), vamos utilizar o método de Gauss-Jordan. Montamos a matriz aumentada \([A | I]\), onde \( I \) é a matriz identidade de ordem 3.

\[
\left[ \begin{array}{ccc|ccc}
5 & 3 & 2 & 1 & 0 & 0 \\
3 & 3 & 2 & 0 & 1 & 0 \\
0 & 1 & 1 & 0 & 0 & 1 \\
\end{array} \right]
\]

**Passo 3: Escalonamento para obter a matriz identidade à esquerda**

*Objetivo:* Transformar a matriz \( A \) na matriz identidade usando operações elementares de linha, aplicando as mesmas operações na matriz identidade que se tornará \( A^{-1} \).

**Operação 1: Eliminar o elemento na posição \( (1,2) \) usando a linha 3**

- Subtraímos 3 vezes a linha 3 da linha 1:
  \[
  L1 = L1 - 3L3
  \]
- Cálculo:
  \[
  \begin{array}{lcl}
  L1 & = & L1 - 3L3 \\
  & = & \left( 5, 3, 2 \, |\, 1, 0, 0 \right) - 3 \times \left( 0, 1, 1 \, |\, 0, 0, 1 \right) \\
  & = & \left( 5 - 0, 3 - 3, 2 - 3 \, |\, 1 - 0, 0 - 0, 0 - 3 \right) \\
  & = & \left( 5, 0, -1 \, |\, 1, 0, -3 \right)
  \end{array}
  \]
- A matriz resultante é:
  \[
  \left[ \begin{array}{ccc|ccc}
  5 & 0 & -1 & 1 & 0 & -3 \\
  3 & 3 & 2 & 0 & 1 & 0 \\
  0 & 1 & 1 & 0 & 0 & 1 \\
  \end{array} \right]
  \]

**Operação 2: Eliminar o elemento na posição \( (2,2) \) usando a linha 3**

- Subtraímos 3 vezes a linha 3 da linha 2:
  \[
  L2 = L2 - 3L3
  \]
- Cálculo:
  \[
  \begin{array}{lcl}
  L2 & = & L2 - 3L3 \\
  & = & \left( 3, 3, 2 \, |\, 0, 1, 0 \right) - 3 \times \left( 0, 1, 1 \, |\, 0, 0, 1 \right) \\
  & = & \left( 3 - 0, 3 - 3, 2 - 3 \, |\, 0 - 0, 1 - 0, 0 - 3 \right) \\
  & = & \left( 3, 0, -1 \, |\, 0, 1, -3 \right)
  \end{array}
  \]
- A matriz resultante é:
  \[
  \left[ \begin{array}{ccc|ccc}
  5 & 0 & -1 & 1 & 0 & -3 \\
  3 & 0 & -1 & 0 & 1 & -3 \\
  0 & 1 & 1 & 0 & 0 & 1 \\
  \end{array} \right]
  \]

**Operação 3: Eliminar o elemento na posição \( (2,1) \) usando a linha 1**

- Calculamos o fator \( \frac{3}{5} \) e subtraímos \( \frac{3}{5} \) vezes a linha 1 da linha 2:
  \[
  L2 = L2 - \left( \frac{3}{5} \right) L1
  \]
- Cálculo:
  \[
  \begin{array}{lcl}
  L2 & = & L2 - \left( \frac{3}{5} \right) L1 \\
  & = & \left( 3, 0, -1 \, |\, 0, 1, -3 \right) - \left( \frac{3}{5} \times \left( 5, 0, -1 \, |\, 1, 0, -3 \right) \right) \\
  & = & \left( 3 - 3, 0 - 0, -1 - \left( -\frac{3}{5} \right) \, |\, 0 - \left( \frac{3}{5} \cdot 1 \right), 1 - 0, -3 - \left( -\frac{9}{5} \right) \right) \\
  & = & \left( 0, 0, -1 + \frac{3}{5} \, |\, -\frac{3}{5}, 1, -3 + \frac{9}{5} \right) \\
  & = & \left( 0, 0, -\frac{2}{5} \, |\, -\frac{3}{5}, 1, -\frac{6}{5} \right)
  \end{array}
  \]
- A matriz resultante é:
  \[
  \left[ \begin{array}{ccc|ccc}
  5 & 0 & -1 & 1 & 0 & -3 \\
  0 & 0 & -\frac{2}{5} & -\frac{3}{5} & 1 & -\frac{6}{5} \\
  0 & 1 & 1 & 0 & 0 & 1 \\
  \end{array} \right]
  \]

**Operação 4: Normalizar a linha 2 para obter 1 como pivô na posição \( (2,3) \)**

- Multiplicamos a linha 2 por \( -\frac{5}{2} \):
  \[
  L2 = \left( -\frac{5}{2} \right) L2
  \]
- Cálculo:
  \[
  L2 = \left( 0, 0, 1 \, \Big|\, \frac{3}{2}, -\frac{5}{2}, 3 \right)
  \]
- A matriz resultante é:
  \[
  \left[ \begin{array}{ccc|ccc}
  5 & 0 & -1 & 1 & 0 & -3 \\
  0 & 0 & 1 & \frac{3}{2} & -\frac{5}{2} & 3 \\
  0 & 1 & 1 & 0 & 0 & 1 \\
  \end{array} \right]
  \]

**Operação 5: Eliminar o elemento na posição \( (1,3) \) usando a linha 2**

- Somamos a linha 2 à linha 1:
  \[
  L1 = L1 + L2
  \]
- Cálculo:
  \[
  \begin{array}{lcl}
  L1 & = & L1 + L2 \\
  & = & \left( 5, 0, -1 \, |\, 1, 0, -3 \right) + \left( 0, 0, 1 \, |\, \frac{3}{2}, -\frac{5}{2}, 3 \right) \\
  & = & \left( 5 + 0, 0 + 0, -1 + 1 \, |\, 1 + \frac{3}{2}, 0 - \frac{5}{2}, -3 + 3 \right) \\
  & = & \left( 5, 0, 0 \, |\, \frac{5}{2}, -\frac{5}{2}, 0 \right)
  \end{array}
  \]
- A matriz resultante é:
  \[
  \left[ \begin{array}{ccc|ccc}
  5 & 0 & 0 & \frac{5}{2} & -\frac{5}{2} & 0 \\
  0 & 0 & 1 & \frac{3}{2} & -\frac{5}{2} & 3 \\
  0 & 1 & 1 & 0 & 0 & 1 \\
  \end{array} \right]
  \]

**Operação 6: Eliminar o elemento na posição \( (3,3) \) usando a linha 2**

- Subtraímos a linha 2 da linha 3:
  \[
  L3 = L3 - L2
  \]
- Cálculo:
  \[
  \begin{array}{lcl}
  L3 & = & L3 - L2 \\
  & = & \left( 0, 1, 1 \, |\, 0, 0, 1 \right) - \left( 0, 0, 1 \, |\, \frac{3}{2}, -\frac{5}{2}, 3 \right) \\
  & = & \left( 0 - 0, 1 - 0, 1 - 1 \, |\, 0 - \frac{3}{2}, 0 - \left( -\frac{5}{2} \right), 1 - 3 \right) \\
  & = & \left( 0, 1, 0 \, |\, -\frac{3}{2}, \frac{5}{2}, -2 \right)
  \end{array}
  \]
- A matriz resultante é:
  \[
  \left[ \begin{array}{ccc|ccc}
  5 & 0 & 0 & \frac{5}{2} & -\frac{5}{2} & 0 \\
  0 & 0 & 1 & \frac{3}{2} & -\frac{5}{2} & 3 \\
  0 & 1 & 0 & -\frac{3}{2} & \frac{5}{2} & -2 \\
  \end{array} \right]
  \]

**Operação 7: Normalizar a linha 1 para obter 1 como pivô na posição \( (1,1) \)**

- Dividimos a linha 1 por 5:
  \[
  L1 = \frac{1}{5} L1
  \]
- Cálculo:
  \[
  L1 = \left( 1, 0, 0 \, \Big|\, \frac{1}{2}, -\frac{1}{2}, 0 \right)
  \]
- A matriz resultante é:
  \[
  \left[ \begin{array}{ccc|ccc}
  1 & 0 & 0 & \frac{1}{2} & -\frac{1}{2} & 0 \\
  0 & 0 & 1 & \frac{3}{2} & -\frac{5}{2} & 3 \\
  0 & 1 & 0 & -\frac{3}{2} & \frac{5}{2} & -2 \\
  \end{array} \right]
  \]

**Operação 8: Trocar as linhas 2 e 3 para obter 1 como pivô na posição \( (2,2) \)**

- Trocamos as linhas 2 e 3:
  \[
  L2 \leftrightarrow L3
  \]
- A matriz resultante é:
  \[
  \left[ \begin{array}{ccc|ccc}
  1 & 0 & 0 & \frac{1}{2} & -\frac{1}{2} & 0 \\
  0 & 1 & 0 & -\frac{3}{2} & \frac{5}{2} & -2 \\
  0 & 0 & 1 & \frac{3}{2} & -\frac{5}{2} & 3 \\
  \end{array} \right]
  \]

Agora, a matriz à esquerda é a matriz identidade, e a parte direita é a inversa da matriz \( A \):

\[
A^{-1} = \begin{bmatrix}
\frac{1}{2} & -\frac{1}{2} & 0 \\
-\frac{3}{2} & \frac{5}{2} & -2 \\
\frac{3}{2} & -\frac{5}{2} & 3 \\
\end{bmatrix}
\]

**Passo 4: Calcular o vetor solução \( X = A^{-1}B \)**

Multiplicamos \( A^{-1} \) pelo vetor \( B \):

\[
X = A^{-1}B = \begin{bmatrix}
\frac{1}{2} & -\frac{1}{2} & 0 \\
-\frac{3}{2} & \frac{5}{2} & -2 \\
\frac{3}{2} & -\frac{5}{2} & 3 \\
\end{bmatrix}
\begin{bmatrix}
4 \\
2 \\
5 \\
\end{bmatrix}
\]

Calculando cada componente de \( X \):

1. \( x_1 = \left( \frac{1}{2} \times 4 \right) + \left( -\frac{1}{2} \times 2 \right) + \left( 0 \times 5 \right) = 2 - 1 + 0 = 1 \)

2. \( x_2 = \left( -\frac{3}{2} \times 4 \right) + \left( \frac{5}{2} \times 2 \right) + \left( -2 \times 5 \right) = -6 + 5 - 10 = -11 \)

3. \( x_3 = \left( \frac{3}{2} \times 4 \right) + \left( -\frac{5}{2} \times 2 \right) + \left( 3 \times 5 \right) = 6 - 5 + 15 = 16 \)

**Solução:**

\[
x_1 = 1, \quad x_2 = -11, \quad x_3 = 16
\]

**Passo 5: Verificar a solução nas equações originais**

1. **Primeira equação:**

   \[
   5x_1 + 3x_2 + 2x_3 = 5(1) + 3(-11) + 2(16) = 5 - 33 + 32 = 4
   \]

2. **Segunda equação:**

   \[
   3x_1 + 3x_2 + 2x_3 = 3(1) + 3(-11) + 2(16) = 3 - 33 + 32 = 2
   \]

3. **Terceira equação:**

   \[
   x_2 + x_3 = -11 + 16 = 5
   \]

Os valores encontrados satisfazem todas as equações originais, confirmando que a solução está correta.

**Conclusão:**

Resolvemos o sistema invertendo a matriz dos coeficientes e encontramos a solução \( x_1 = 1 \), \( x_2 = -11 \) e \( x_3 = 16 \). Verificamos a solução substituindo os valores nas equações originais e confirmamos que estão corretos.


## Questão 2:


Para determinar os valores de \( x \) que tornam a matriz \( A \) invertível, precisamos encontrar quando o determinante da matriz \( A \) é diferente de zero, pois uma matriz é invertível se, e somente se, seu determinante não é zero.

A matriz \( A \) é:

\[
A = \begin{pmatrix}
x - \frac{1}{2} & 0 & 0 \\
x & x - \frac{1}{3} & 0 \\
x^2 & x^3 & x + \frac{1}{4}
\end{pmatrix}
\]

Observamos que \( A \) é uma matriz triangular inferior, pois todos os elementos acima da diagonal principal são zero. Para matrizes triangulares (superior ou inferior), o determinante é igual ao produto dos elementos da diagonal principal.

Assim, o determinante de \( A \) é:

\[
\det(A) = \left( x - \frac{1}{2} \right) \left( x - \frac{1}{3} \right) \left( x + \frac{1}{4} \right)
\]

Para encontrar os valores de \( x \) que tornam \( \det(A) = 0 \), resolvemos:

\[
\left( x - \frac{1}{2} \right) \left( x - \frac{1}{3} \right) \left( x + \frac{1}{4} \right) = 0
\]

Isso ocorre quando:

1. \( x - \frac{1}{2} = 0 \) → \( x = \frac{1}{2} \)
2. \( x - \frac{1}{3} = 0 \) → \( x = \frac{1}{3} \)
3. \( x + \frac{1}{4} = 0 \) → \( x = -\frac{1}{4} \)

Portanto, a matriz \( A \) não é invertível nos valores \( x = \frac{1}{2}, \frac{1}{3}, -\frac{1}{4} \).

**Resposta:** Todos os números reais \( x \) exceto \( x = \frac{1}{2},\ \frac{1}{3} \) e \( x = -\dfrac{1}{4} \).


## Questão 3:

Para resolver o determinante dado, vamos utilizar propriedades de determinantes e manipulações de linhas.

**Passo 1: Analisar a matriz dada e o determinante conhecido**

Sabemos que:

\[
D = \det \begin{pmatrix} a & b & c \\ d & e & f \\ g & h & i \end{pmatrix} = -6
\]

Precisamos calcular:

\[
\det \begin{pmatrix} -3a & -3b & -3c \\ d & e & f \\ g - 4d & h - 4e & i - 4f \end{pmatrix}
\]

**Passo 2: Fatorar constantes das linhas**

Observamos que a primeira linha da nova matriz é \(-3\) vezes a primeira linha da matriz original.

Podemos fatorar \(-3\) da primeira linha:

\[
\det \begin{pmatrix} -3a & -3b & -3c \\ d & e & f \\ g - 4d & h - 4e & i - 4f \end{pmatrix} = (-3) \times \det \begin{pmatrix} a & b & c \\ d & e & f \\ g - 4d & h - 4e & i - 4f \end{pmatrix}
\]

**Passo 3: Simplificar a terceira linha usando operações entre linhas**

Percebemos que a terceira linha é a terceira linha original menos 4 vezes a segunda linha:

\[
\text{Linha 3} = \text{Linha 3 original} - 4 \times \text{Linha 2}
\]

**Passo 4: Utilizar a propriedade de determinantes sobre operações entre linhas**

Uma propriedade fundamental dos determinantes é que adicionar ou subtrair um múltiplo de uma linha a outra não altera o valor do determinante. Portanto:

\[
\det \begin{pmatrix} a & b & c \\ d & e & f \\ g - 4d & h - 4e & i - 4f \end{pmatrix} = \det \begin{pmatrix} a & b & c \\ d & e & f \\ g & h & i \end{pmatrix} = D = -6
\]

**Passo 5: Calcular o determinante final**

Substituindo o valor de \(D\):

\[
\det \begin{pmatrix} -3a & -3b & -3c \\ d & e & f \\ g - 4d & h - 4e & i - 4f \end{pmatrix} = (-3) \times D = (-3) \times (-6) = 18
\]

**Resposta Final:**

\[
\det \begin{pmatrix} -3a & -3b & -3c \\ d & e & f \\ g - 4d & h - 4e & i - 4f \end{pmatrix} = 18
\]

**Portanto, o determinante é 18.**

**Resposta:** 18

## Questão 4

Para resolver o sistema usando a Regra de Cramer, precisamos calcular os determinantes da matriz dos coeficientes e das matrizes obtidas ao substituir cada coluna pelo vetor dos termos independentes. Para simplificar os cálculos dos determinantes, aplicaremos operações elementares para transformar as matrizes em triangulares superiores.

**Matriz dos coeficientes (A):**
\[
A = \begin{pmatrix}
1 & -3 & 1 \\
2 & -1 & 0 \\
4 & 0 & -3 \\
\end{pmatrix}
\]

**Calculando \(\det(A)\):**

1. **Operação:** \(L2 = L2 - 2L1\)
   
   Matriz após a operação:
   \[
   \begin{pmatrix}
   1 & -3 & 1 \\
   0 & 5 & -2 \\
   4 & 0 & -3 \\
   \end{pmatrix}
   \]

2. **Operação:** \(L3 = L3 - 4L1\)
   
   Matriz após a operação:
   \[
   \begin{pmatrix}
   1 & -3 & 1 \\
   0 & 5 & -2 \\
   0 & 12 & -7 \\
   \end{pmatrix}
   \]

3. **Operação:** \(L3 = L3 - \frac{12}{5}L2\)
   
   Matriz após a operação:
   \[
   \begin{pmatrix}
   1 & -3 & 1 \\
   0 & 5 & -2 \\
   0 & 0 & -\frac{11}{5} \\
   \end{pmatrix}
   \]

**Determinante de A:**
\[
\det(A) = 1 \times 5 \times \left(-\frac{11}{5}\right) = -11
\]

---

**Matriz para \(x_1\) (\(A_1\)):**
Substituímos a primeira coluna de A pelo vetor dos termos independentes.

\[
A_1 = \begin{pmatrix}
4 & -3 & 1 \\
-2 & -1 & 0 \\
0 & 0 & -3 \\
\end{pmatrix}
\]

**Calculando \(\det(A_1)\):**

1. **Operação:** \(L2 = L2 + \frac{1}{2}L1\)
   
   Matriz após a operação:
   \[
   \begin{pmatrix}
   4 & -3 & 1 \\
   0 & -2.5 & 0.5 \\
   0 & 0 & -3 \\
   \end{pmatrix}
   \]

**Determinante de \(A_1\):**
\[
\det(A_1) = 4 \times (-2.5) \times (-3) = 30
\]

---

**Matriz para \(x_2\) (\(A_2\)):**
Substituímos a segunda coluna de A pelo vetor dos termos independentes.

\[
A_2 = \begin{pmatrix}
1 & 4 & 1 \\
2 & -2 & 0 \\
4 & 0 & -3 \\
\end{pmatrix}
\]

**Calculando \(\det(A_2)\):**

1. **Operação:** \(L2 = L2 - 2L1\)
   
   Matriz após a operação:
   \[
   \begin{pmatrix}
   1 & 4 & 1 \\
   0 & -10 & -2 \\
   4 & 0 & -3 \\
   \end{pmatrix}
   \]

2. **Operação:** \(L3 = L3 - 4L1\)
   
   Matriz após a operação:
   \[
   \begin{pmatrix}
   1 & 4 & 1 \\
   0 & -10 & -2 \\
   0 & -16 & -7 \\
   \end{pmatrix}
   \]

3. **Operação:** \(L3 = L3 - \frac{8}{5}L2\)
   
   Matriz após a operação:
   \[
   \begin{pmatrix}
   1 & 4 & 1 \\
   0 & -10 & -2 \\
   0 & 0 & -\frac{19}{5} \\
   \end{pmatrix}
   \]

**Determinante de \(A_2\):**
\[
\det(A_2) = 1 \times (-10) \times \left(-\frac{19}{5}\right) = 38
\]

---

**Matriz para \(x_3\) (\(A_3\)):**
Substituímos a terceira coluna de A pelo vetor dos termos independentes.

\[
A_3 = \begin{pmatrix}
1 & -3 & 4 \\
2 & -1 & -2 \\
4 & 0 & 0 \\
\end{pmatrix}
\]

**Calculando \(\det(A_3)\):**

1. **Operação:** \(L2 = L2 - 2L1\)
   
   Matriz após a operação:
   \[
   \begin{pmatrix}
   1 & -3 & 4 \\
   0 & 5 & -10 \\
   4 & 0 & 0 \\
   \end{pmatrix}
   \]

2. **Operação:** \(L3 = L3 - 4L1\)
   
   Matriz após a operação:
   \[
   \begin{pmatrix}
   1 & -3 & 4 \\
   0 & 5 & -10 \\
   0 & 12 & -16 \\
   \end{pmatrix}
   \]

3. **Operação:** \(L3 = L3 - \frac{12}{5}L2\)
   
   Matriz após a operação:
   \[
   \begin{pmatrix}
   1 & -3 & 4 \\
   0 & 5 & -10 \\
   0 & 0 & 8 \\
   \end{pmatrix}
   \]

**Determinante de \(A_3\):**
\[
\det(A_3) = 1 \times 5 \times 8 = 40
\]

---

**Solução do sistema:**

\[
\begin{cases}
x_1 = \dfrac{\det(A_1)}{\det(A)} = \dfrac{30}{-11} = -\dfrac{30}{11} \\
x_2 = \dfrac{\det(A_2)}{\det(A)} = \dfrac{38}{-11} = -\dfrac{38}{11} \\
x_3 = \dfrac{\det(A_3)}{\det(A)} = \dfrac{40}{-11} = -\dfrac{40}{11} \\
\end{cases}
\]

Portanto, a solução do sistema é:

\[
x_1 = -\dfrac{30}{11}, \quad x_2 = -\dfrac{38}{11}, \quad x_3 = -\dfrac{40}{11}
\]

Para verificar que a solução encontrada satisfaz o sistema, vamos substituir os valores de \( x_1, x_2 \) e \( x_3 \) nas equações originais e verificar se as igualdades são verdadeiras.

**Valores encontrados:**
\[
x_1 = -\dfrac{30}{11}, \quad x_2 = -\dfrac{38}{11}, \quad x_3 = -\dfrac{40}{11}
\]

---

### **Primeira equação:**
\[
x_1 - 3x_2 + x_3 = 4
\]

**Substituindo os valores:**
\[
\begin{aligned}
\left(-\dfrac{30}{11}\right) - 3\left(-\dfrac{38}{11}\right) + \left(-\dfrac{40}{11}\right) &= 4 \\
\end{aligned}
\]

**Calculando passo a passo:**

1. **Multiplicando \(-3\) por \( x_2 \):**
   \[
   -3\left(-\dfrac{38}{11}\right) = \dfrac{114}{11}
   \]

2. **Somando os termos:**
   \[
   \left(-\dfrac{30}{11}\right) + \dfrac{114}{11} + \left(-\dfrac{40}{11}\right) = \dfrac{-30 + 114 - 40}{11} = \dfrac{44}{11} = 4
   \]

**Resultado:**
\[
4 = 4 \quad \text{(Verdadeiro)}
\]

---

### **Segunda equação:**
\[
2x_1 - x_2 = -2
\]

**Substituindo os valores:**
\[
2\left(-\dfrac{30}{11}\right) - \left(-\dfrac{38}{11}\right) = -2
\]

**Calculando passo a passo:**

1. **Multiplicando \(2\) por \( x_1 \):**
   \[
   2\left(-\dfrac{30}{11}\right) = -\dfrac{60}{11}
   \]

2. **Somando os termos:**
   \[
   \left(-\dfrac{60}{11}\right) + \dfrac{38}{11} = \dfrac{-60 + 38}{11} = \dfrac{-22}{11} = -2
   \]

**Resultado:**
\[
-2 = -2 \quad \text{(Verdadeiro)}
\]

---

### **Terceira equação:**
\[
4x_1 - 3x_3 = 0
\]

**Substituindo os valores:**
\[
4\left(-\dfrac{30}{11}\right) - 3\left(-\dfrac{40}{11}\right) = 0
\]

**Calculando passo a passo:**

1. **Multiplicando \(4\) por \( x_1 \):**
   \[
   4\left(-\dfrac{30}{11}\right) = -\dfrac{120}{11}
   \]

2. **Multiplicando \(-3\) por \( x_3 \):**
   \[
   -3\left(-\dfrac{40}{11}\right) = \dfrac{120}{11}
   \]

3. **Somando os termos:**
   \[
   \left(-\dfrac{120}{11}\right) + \dfrac{120}{11} = 0
   \]

**Resultado:**
\[
0 = 0 \quad \text{(Verdadeiro)}
\]

---

**Conclusão:**

As substituições dos valores de \( x_1, x_2 \) e \( x_3 \) nas três equações originais confirmam que as igualdades são verdadeiras. Portanto, a solução encontrada satisfaz o sistema:

\[
\boxed{\begin{cases}
x_1 = -\dfrac{30}{11} \\
x_2 = -\dfrac{38}{11} \\
x_3 = -\dfrac{40}{11}
\end{cases}}
\]

## Quesão 5

**Análise do Sistema Linear por Meio de Matriz Aumentada e Escalonamento**

Considere o sistema linear:

\[
\begin{cases}
x + 2y - 3z = 4 \quad \quad (1) \\
3x - y + 5z = 2 \quad \quad (2) \\
4x + y + (a^2 - 14)z = a + 2 \quad \quad (3)
\end{cases}
\]

Nosso objetivo é determinar os valores de \( a \) para os quais o sistema:

1. Não tem solução.
2. Tem uma solução única.
3. Tem infinitas soluções.
4. E analisar o que acontece com as soluções se o sistema for homogeneizado (ou seja, se os termos independentes forem zero).

---

### **Passo 1: Montando a Matriz Aumentada**

A matriz aumentada do sistema é:

\[
\left[ \begin{array}{ccc|c}
1 & 2 & -3 & 4 \\
3 & -1 & 5 & 2 \\
4 & 1 & a^2 - 14 & a + 2
\end{array} \right]
\]

---

### **Passo 2: Escalonamento da Matriz**

Vamos utilizar operações elementares de linha para escalonar a matriz aumentada e analisar os possíveis casos em função de \( a \).

---

#### **Etapa 1: Zerando os elementos abaixo do pivô na coluna 1**

**Operação em \( L2 \):**

\[
L2 \leftarrow L2 - 3L1
\]

Matriz após a operação:

\[
\left[ \begin{array}{ccc|c}
1 & 2 & -3 & 4 \\
0 & -7 & 14 & -10 \\
4 & 1 & a^2 - 14 & a + 2
\end{array} \right]
\]

**Operação em \( L3 \):**

\[
L3 \leftarrow L3 - 4L1
\]

Matriz após a operação:

\[
\left[ \begin{array}{ccc|c}
1 & 2 & -3 & 4 \\
0 & -7 & 14 & -10 \\
0 & -7 & a^2 - 2 & a - 14
\end{array} \right]
\]

---

#### **Etapa 2: Zerando o elemento abaixo do pivô na coluna 2**

**Operação em \( L3 \):**

\[
L3 \leftarrow L3 - L2
\]

Matriz após a operação:

\[
\left[ \begin{array}{ccc|c}
1 & 2 & -3 & 4 \\
0 & -7 & 14 & -10 \\
0 & 0 & a^2 - 16 & a - 4
\end{array} \right]
\]

---

### **Passo 3: Análise dos Casos em Função de \( a \)**

Observe que o elemento \( a_{33} \) é \( a^2 - 16 \), que pode ser fatorado como:

\[
a^2 - 16 = (a - 4)(a + 4)
\]

Então, o elemento \( a_{33} \) será zero quando \( a = 4 \) ou \( a = -4 \).

Vamos analisar três casos:

1. **Caso 1:** \( a \neq \pm4 \)
2. **Caso 2:** \( a = 4 \)
3. **Caso 3:** \( a = -4 \)

---

#### **Caso 1: \( a \neq \pm4 \)**

Neste caso, \( a^2 - 16 \neq 0 \), então o elemento \( a_{33} \) é diferente de zero.

**Equação da terceira linha:**

\[
(a^2 - 16) z = a - 4
\]

Resolvendo para \( z \):

\[
z = \frac{a - 4}{a^2 - 16}
\]

Como \( a \neq \pm4 \), o denominador não é zero.

**Equação da segunda linha:**

\[
-7y + 14z = -10
\]

Substituindo o valor de \( z \):

\[
-7y + 14\left( \frac{a - 4}{a^2 - 16} \right) = -10
\]

Resolvendo para \( y \):

\[
-7y = -10 - \frac{14(a - 4)}{a^2 - 16}
\]

\[
y = \frac{10}{7} + \frac{2(a - 4)}{a^2 - 16}
\]

**Equação da primeira linha:**

\[
x + 2y - 3z = 4
\]

Substituindo \( y \) e \( z \):

\[
x + 2\left( \frac{10}{7} + \frac{2(a - 4)}{a^2 - 16} \right) - 3\left( \frac{a - 4}{a^2 - 16} \right) = 4
\]

Resolvendo para \( x \).

**Conclusão:**

- Para \( a \neq \pm4 \), o sistema tem uma única solução.

---

#### **Caso 2: \( a = 4 \)**

Substituindo \( a = 4 \) na matriz escalonada:

O elemento \( a_{33} = (4)^2 - 16 = 0 \), então a terceira linha é:

\[
\left[ \begin{array}{ccc|c}
0 & 0 & 0 & 0
\end{array} \right]
\]

A terceira equação se torna \( 0 = 0 \), que é sempre verdadeira.

Temos então duas equações independentes com três variáveis:

**Equação da segunda linha:**

\[
-7y + 14z = -10
\]

Resolvendo para \( y \):

\[
y = 2z + \frac{10}{7}
\]

**Equação da primeira linha:**

\[
x + 2y - 3z = 4
\]

Substituindo \( y \):

\[
x + 2\left( 2z + \frac{10}{7} \right) - 3z = 4

\implies x + 4z + \frac{20}{7} - 3z = 4

\implies x + z + \frac{20}{7} = 4

\]

Resolvendo para \( x \):

\[
x = 4 - \frac{20}{7} - z = \frac{8}{7} - z
\]

**Solução geral:**

\[
\begin{cases}
x = \dfrac{8}{7} - z \\
y = \dfrac{10}{7} + 2z \\
z = z
\end{cases}
\]

Onde \( z \) é um parâmetro real qualquer.

**Conclusão:**

- Para \( a = 4 \), o sistema tem infinitas soluções.

---

#### **Caso 3: \( a = -4 \)**

Substituindo \( a = -4 \) na matriz escalonada:

O elemento \( a_{33} = (-4)^2 - 16 = 0 \), então a terceira linha é:

\[
\left[ \begin{array}{ccc|c}
0 & 0 & 0 & -8
\end{array} \right]
\]

A terceira equação se torna:

\[
0x + 0y + 0z = -8
\]

Que é uma contradição, pois \( 0 = -8 \) é falso.

**Conclusão:**

- Para \( a = -4 \), o sistema não tem solução.

---

### **Passo 4: Sistema Homogeneizado**

Homogeneizando o sistema (tornando os termos independentes zero):

\[
\begin{cases}
x + 2y - 3z = 0 \\
3x - y + 5z = 0 \\
4x + y + (a^2 - 14)z = 0
\end{cases}
\]

Montando a matriz aumentada homogeneizada:

\[
\left[ \begin{array}{ccc|c}
1 & 2 & -3 & 0 \\
3 & -1 & 5 & 0 \\
4 & 1 & a^2 - 14 & 0
\end{array} \right]
\]

---

#### **Escalonamento da Matriz Homogeneizada**

**Operação em \( L2 \):**

\[
L2 \leftarrow L2 - 3L1
\]

Matriz após a operação:

\[
\left[ \begin{array}{ccc|c}
1 & 2 & -3 & 0 \\
0 & -7 & 14 & 0 \\
4 & 1 & a^2 - 14 & 0
\end{array} \right]
\]

**Operação em \( L3 \):**

\[
L3 \leftarrow L3 - 4L1
\]

Matriz após a operação:

\[
\left[ \begin{array}{ccc|c}
1 & 2 & -3 & 0 \\
0 & -7 & 14 & 0 \\
0 & -7 & a^2 - 2 & 0
\end{array} \right]
\]

**Operação em \( L3 \):**

\[
L3 \leftarrow L3 - L2
\]

Matriz após a operação:

\[
\left[ \begin{array}{ccc|c}
1 & 2 & -3 & 0 \\
0 & -7 & 14 & 0 \\
0 & 0 & a^2 - 16 & 0
\end{array} \right]
\]

---

### **Análise do Sistema Homogeneizado**

#### **Caso 1: \( a \neq \pm4 \)**

O elemento \( a_{33} = a^2 - 16 \) é diferente de zero.

**Terceira equação:**

\[
(a^2 - 16) z = 0
\]

Como \( a^2 - 16 \neq 0 \), temos:

\[
z = 0
\]

**Segunda equação:**

\[
-7y + 14z = 0 \implies -7y = 0 \implies y = 0
\]

**Primeira equação:**

\[
x + 2y - 3z = 0 \implies x = 0
\]

**Conclusão:**

- A única solução é \( x = y = z = 0 \).

#### **Caso 2: \( a = 4 \) ou \( a = -4 \)**

O elemento \( a_{33} = 0 \).

**Terceira linha:**

- Para \( a = 4 \) ou \( a = -4 \):

\[
\left[ \begin{array}{ccc|c}
0 & 0 & 0 & 0
\end{array} \right]
\]

A terceira equação é \( 0 = 0 \), sempre verdadeira.

**Segunda equação:**

\[
-7y + 14z = 0 \implies y = 2z
\]

**Primeira equação:**

\[
x + 2y - 3z = 0 \implies x + 2(2z) - 3z = 0 \implies x + 4z - 3z = 0 \implies x + z = 0 \implies x = -z
\]

**Solução geral:**

\[
\begin{cases}
x = -z \\
y = 2z \\
z = z
\end{cases}
\]

Onde \( z \) é um parâmetro real qualquer.

**Conclusão:**

- Para \( a = \pm4 \), o sistema homogeneizado tem infinitas soluções não triviais.

---

### **Respostas Finais**

1. **O sistema não tem solução quando \( a = -4 \)**

   - Porque ocorre uma contradição na terceira equação após o escalonamento.

2. **O sistema tem uma única solução quando \( a \neq \pm4 \)**

   - Pois o escalonamento leva a um sistema com soluções únicas para \( x \), \( y \) e \( z \).

3. **O sistema tem infinitas soluções quando \( a = 4 \)**

   - Porque a terceira equação é redundante, resultando em infinitas soluções parametrizadas por \( z \).

4. **No sistema homogeneizado:**

   - **Para \( a \neq \pm4 \):** A única solução é \( x = y = z = 0 \) (solução trivial).
   - **Para \( a = \pm4 \):** Existem infinitas soluções não triviais, dadas por \( x = -z \), \( y = 2z \), com \( z \) real.

---

**Conclusão sobre o Determinante e as Soluções**

Ao calcular o determinante da matriz dos coeficientes em função de \( a \):

\[
\det(A) = -7(a - 4)(a + 4)
\]

- **Quando \( \det(A) \neq 0 \) (\( a \neq \pm4 \))**: O sistema tem uma única solução.
- **Quando \( \det(A) = 0 \) (\( a = \pm4 \))**: O sistema pode ter infinitas soluções ou não ter solução, dependendo da consistência das equações.

O escalonamento da matriz aumentada permite visualizar claramente como o valor de \( a \) afeta as soluções do sistema, sem a necessidade de cálculos intermediários detalhados em cada operação.

---
