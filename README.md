# Curso de Introdução à Álgebra Linear

Bem-vindo ao repositório do curso de Introdução à Álgebra Linear! Este curso foi desenvolvido para fornecer aos alunos uma base sólida nos conceitos fundamentais da álgebra linear.

## Sobre o Curso

Este curso aborda os princípios básicos da álgebra linear, uma área fundamental da matemática com aplicações em diversas disciplinas, incluindo física, engenharia, economia e ciência da computação.

<details>
  <summary>Como não passar nesta matéria</summary>

  # Como não passar nesta matéria

  Olá, queridos alunos! Vamos falar sobre como ter sucesso neste curso? Não? Ah, você quer saber como não passar?
  Aqui vai um guia infalível para garantir que você não passe nesta matéria. Siga estas dicas e o insucesso será seu fiel companheiro!

  ## 1. Estude só na véspera da prova - o segredo do fracasso!

  Lembre-se: a universidade é igualzinha ao ensino médio! Aquelas matérias complexas e extensas? Pfff, besteira! Você consegue absorver todo esse conteúdo em uma única noite de estudos intensos. Afinal, quem precisa de tempo para processar informações, não é mesmo?

  Ignore completamente o fato de que o cérebro precisa de tempo para consolidar memórias e criar conexões entre conceitos. A neurociência? Ora, isso é só um modismo passageiro!

  ## 2. Sono é para os fracos!

  Dormir é perda de tempo. Quem precisa de sono quando se tem café e energéticos? Esqueça tudo o que ouviu sobre a importância do sono para a consolidação da memória e para o bom funcionamento cognitivo. 

  Afinal, o que os neurocientistas sabem? Eles só estudam o cérebro há décadas. Você, com sua sagacidade de última hora, certamente sabe mais do que eles.

  ## 3. Consistência? Que bobagem!

  Estudar um pouquinho todos os dias? Que ideia mais absurda! É muito melhor acumular todo o conteúdo para uma maratona de estudos na véspera da prova. Seu cérebro vai adorar essa sobrecarga de informações de última hora.

  Ignore completamente as pesquisas que mostram que o aprendizado espaçado é mais eficaz. Afinal, o que é a ciência cognitiva comparada à sua intuição infalível?

  ## Conclusão

  Seguindo essas dicas, você estará no caminho certo para não passar nesta matéria. Mas hey, se por algum motivo você decidir fazer o oposto do que foi sugerido aqui - estudar consistentemente, dormir bem e respeitar os processos de aprendizagem do seu cérebro - bem, aí a responsabilidade é toda sua se acabar passando com louvor!

</details>


<details>
  <summary>Livro Adotado</summary>

O curso é baseado no livro:

**"Álgebra Linear com Aplicações"** de Howard Anton

- 📢 Atenção, alunos! 📢
- 📖 LEITURA OBRIGATÓRIA do livro texto! 🔍
- 🎓 Em aula, abordaremos os temas mais complexos.
- 🏠 Outros tópicos importantes são para estudo individual no livro.
</details>

## Ementa Detalhada do Curso

### [CAPÍTULO 3: Espaços Vetoriais Euclidianos](https://oangelo.github.io/Introducao-a-Algebra-Linear)
- Vetores bi, tri e n–dimensionais
- Norma, produto escalar e distância em $R^n$
- Ortogonalidade
- A geometria de sistemas lineares
- Produto vetorial

### CAPÍTULO 1: Sistemas de Equações Lineares e Matrizes
<details>
<summary>Glossário de Termos Chave</summary>

# Glossário de Termos Chave

* **Sistema Linear:** Conjunto de equações lineares com as mesmas variáveis.
* **Matriz:** Tabela retangular de elementos dispostos em linhas e colunas.
* **Vetor:** Matriz com apenas uma linha ou uma coluna.
* **Matriz Aumentada:** Matriz que representa um sistema linear, contendo os coeficientes das variáveis e os termos independentes.
* **Operações Elementares com Linhas:** Operações que podem ser aplicadas a uma matriz para transformá-la em uma forma equivalente, sem alterar a solução do sistema linear associado.
* **Forma Escalonada:** Uma matriz está na forma escalonada quando:
  1. O primeiro elemento não nulo de cada linha (pivô) é igual a 1;
  2. Os pivôs de linhas consecutivas estão em colunas diferentes e cada pivô está à direita do pivô da linha anterior;
  3. As linhas nulas estão abaixo das linhas não nulas.
* **Forma Escalonada Reduzida por Linhas:** Uma matriz está na forma escalonada reduzida por linhas quando está na forma escalonada e:
  4. Cada pivô é o único elemento não nulo da sua coluna.
* **Variável Livre:** Variável que pode assumir qualquer valor real na solução de um sistema linear indeterminado.
* **Matriz Inversa:** Matriz que, quando multiplicada pela matriz original, resulta na matriz identidade.
* **Matriz Transposta:** Matriz obtida trocando as linhas pelas colunas da matriz original.
* **Matriz Diagonal:** Matriz quadrada onde os elementos fora da diagonal principal são nulos.
* **Matriz Triangular Superior:** Matriz quadrada onde os elementos abaixo da diagonal principal são nulos.
* **Matriz Triangular Inferior:** Matriz quadrada onde os elementos acima da diagonal principal são nulos.
* **Matriz Identidade:** Matriz diagonal onde os elementos da diagonal principal são iguais a 1.

</details>

- [Introdução aos sistemas de equações lineares e Eliminação gaussiana](https://oangelo.github.io/Introducao-a-Algebra-Linear/eliminacao_gaussiana.html)
- [Matrizes e propriedades das operações matriciais](https://oangelo.github.io/Introducao-a-Algebra-Linear/propriedades.html)
- [Matrizes Inversas](https://oangelo.github.io/Introducao-a-Algebra-Linear/inversas.html)
- [Quiz](quiz/matrizes_e_sitemas.md)

### [CAPÍTULO 2: Determinantes](https://oangelo.github.io/Introducao-a-Algebra-Linear/determinante.html)
<details>
<summary>Glossário de Termos Chave</summary>

# Glossário de Termos Chave

* **Determinante:** Função que associa um número real a uma matriz quadrada, sendo útil para determinar propriedades da matriz, como invertibilidade.
* **Menor:** Determinante da submatriz obtida ao remover uma linha e uma coluna de uma matriz quadrada.
* **Cofator:** Produto do menor pelo fator (-1)^(i+j), levando em consideração a posição (i, j) do elemento na matriz.
* **Expansão em cofatores:** Método para calcular o determinante de uma matriz utilizando os cofatores de uma linha ou coluna.
* **Matriz triangular:** Matriz quadrada onde os elementos acima ou abaixo da diagonal principal são todos zero (superior ou inferior, respectivamente).
* **Matriz elementar:** Matriz obtida aplicando-se uma única operação elementar com linhas à matriz identidade.
* **Operações elementares com linhas:** Operações que modificam uma matriz sem alterar suas soluções (trocar linhas, multiplicar linha por escalar, somar múltiplo de linha a outra).
* **Matriz de cofatores:** Matriz onde cada elemento é o cofator correspondente da matriz original.
* **Adjunta:** Matriz transposta da matriz de cofatores, utilizada no cálculo da inversa da matriz original.
* **Regra de Cramer:** Fórmula que utiliza determinantes para solucionar sistemas de equações lineares com 'n' equações e 'n' incógnitas, quando a matriz de coeficientes é invertível.

</details>

- Determinantes por expansão em cofatores
- Calculando determinantes por meio de redução por linhas
- Propriedades dos determinantes; regra de Cramer
- [Quiz](quiz/determinantes.md)

### [CAPÍTULO 4: ESPAÇOS VETORIAIS EUCLIDIANOS](https://oangelo.github.io/Introducao-a-Algebra-Linear/transformacoes.html)
- Espaço Euclidiano n-dimensional
- Transformações Lineares de $R^n$ em $R^m$
- Propriedades das Transformações Lineares de $R^n$ em $R^m$

## 👆 A matéria da primeira prova vai até aqui! 📚✅
- 🎉 Lembre-se: O importante é praticar! 💪
- 📝 Faça os exercícios do livro recomendado 📘
- 🧠 Isso ajudará a fixar o conteúdo 🌟

### [CAPÍTULO 5: Espaços Vetoriais Arbitrários](https://oangelo.github.io/Introducao-a-Algebra-Linear/espacos.html)
- Espaços vetoriais reais
- Subespaços
- Independência linear
- Coordenadas e bases
- Dimensão
- Mudança de bases
- Espaço linha, espaço coluna e espaço nulo
- Posto, nulidade e os espaços matriciais fundamentais
- Transformações matriciais de $R^n$ em $R^m$
- Propriedades das transformações matriciais
- A geometria de operadores matriciais de $R^2$

### CAPÍTULO 7: Autovalores e Autovetores
- Autovalores e autovetores
- Diagonalização

### Monitoria 2024 - 2
- Segunda-feira, T2 e T3, na sala 203.
- Monitor: Arthur Tavares 

<details>
  <summary>Calendário de Provas</summary>
  <ul>
    <li>P1: 08/10/09</li>
    <li>PF: 17/12/24</li>
  </ul>
  <img src="img/prova.png" alt="meme cachorro">
</details>


📝 Bons estudos e boa sorte! 🍀📐🔢
