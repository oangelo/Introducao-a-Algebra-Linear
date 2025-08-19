Crie uma lista de exercícios de Álgebra Linear sobre [TÓPICO ESPECÍFICO] usando o estilo de um videogame retrô ("Álgebra Arcade"), seguindo RIGOROSAMENTE as diretrizes abaixo.

### Filosofia Pedagógica Aprimorada
O objetivo é criar um material que promova o aprendizado ativo. Para isso, cada exercício deve seguir três princípios:
1.  **Propósito Explícito:** Cada missão deve ter um "Objetivo" claro que informa ao aluno qual habilidade específica ele está praticando.
2.  **Ajuda Sob Demanda:** Tanto a dica quanto o guia de solução devem estar ocultos por padrão, permitindo que o aluno tente resolver o problema sem auxílio primeiro.
3.  **Foco no Processo:** A solução ("Detonado") **NÃO** deve fornecer a resposta numérica final. Em vez disso, deve descrever cada passo lógico da resolução, explicando *o que* fazer e *por que* fazer, guiando o raciocínio do aluno.

### IMPORTANTE: RESPEITAR A PROGRESSÃO DOS TÓPICOS
- Consulte o `guia-tematico-arcade.md`. Os exercícios DEVEM usar APENAS conceitos já abordados até o tópico atual. NUNCA antecipe conceitos.
- Relacione o contexto temático à **Era dos Videogames** apropriada (ex: tópicos iniciais com a Era Arcade, mais avançados com a Era 3D).

### IMPORTANTE: USO CORRETO DO TEMPLATE E HTML
- Gere um **único arquivo HTML**.
- Siga EXATAMENTE a estrutura do arquivo `template-game-exercises.html` e suas classes CSS.
- Use a classe `mission` para cada exercício. A numeração será automática via CSS.

### Estrutura Exata do Documento
1.  **Cabeçalho (`<header class="console-header">`)**: Título Principal e Título da Fase.
2.  **Introdução Conceitual (`<div class="mission-intro">`)**: Manual da Fase e fórmula principal.
3.  **Lista de Exercícios (`<main id="mission-board">`)**: Exatamente 12 exercícios.

### Progressão de 12 Exercícios
1.  **Training Quests (Exercícios 1-3)**: Nível básico.
2.  **Main Missions (Exercícios 4-6)**: Nível intermediário.
3.  **Elite Challenges (Exercícios 7-9)**: Nível avançado.
4.  **Boss Fights (Exercícios 10-12)**: Nível complexo, sem dicas.

### Formato Padrão de Cada Exercício (`div.mission`)
-   **Título (`<h3>`)**: `MISSÃO X-Y: [TÍTULO TEMÁTICO] ([TÓPICO MATEMÁTICO])`
-   **Objetivo da Missão (`<div class="mission-objective">`)**: `<strong>Objetivo da Missão:</strong> [O que o aluno vai praticar neste exercício.]`
-   **Enunciado (`<p>`)**: Descrição do problema com aplicação prática no contexto de um jogo.
-   **Dica (`<details class="hint-container">`)**: Deve estar dentro de um `<details>`. O sumário deve ser `Pedir Dica ao Mestre do Jogo...`. Omitir para a série "Boss Fights".
-   **Detonado (`<details>`)**: O sumário deve ser `Ver Detonado...`.
    -   **CONTEÚDO DO DETONADO**:
        -   Use `<ol class="solution-steps">` para descrever os passos lógicos.
        -   **NÃO EXECUTE AS OPERAÇÕES NUMÉRICAS.** Apenas explique como fazê-las.
        -   *Exemplo RUIM:* `\[ \vec{v} = \begin{pmatrix} 2 \\ 3 \end{pmatrix} + \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 3 \\ 4 \end{pmatrix} \]`
        -   *Exemplo BOM:* `<li>Para encontrar o vetor resultante, some as componentes correspondentes dos vetores \(\vec{v}_1\) e \(\vec{v}_2\). Some a primeira componente de \(\vec{v}_1\) com a primeira de \(\vec{v}_2\), e repita para a segunda componente.</li>`
    -   Termine com `<p class="game-connection"><strong>Conexão com o Mundo dos Jogos:</strong> [Explicação]</p>`.

### Restrições Finais
-   **NUNCA** utilize cálculo diferencial ou integral.
-   Todas as fórmulas matemáticas devem usar LaTeX/MathJax.
-   Use `\vec{v}` para vetores e o ambiente `pmatrix` para matrizes.
