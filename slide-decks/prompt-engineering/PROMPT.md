# Diretrizes Mestras para Geração de Conteúdo - Álgebra Arcade

## Filosofia Central
O objetivo é criar materiais de Álgebra Linear que sejam **pedagogicamente eficazes**, **claros** e **tematicamente engajantes**. A estrutura e o template são ferramentas para garantir consistência, mas a **didática sempre prevalece**. Se uma estrutura rígida prejudicar a clareza de um tópico, ela deve ser adaptada.

## Processo de Geração Interativo (LEIA COM ATENÇÃO)
Este é um processo colaborativo em duas etapas:

**Etapa 1: Reflexão e Proposta de Estrutura (Sua Primeira Resposta)**
Quando eu solicitar a criação de um slide deck para um tópico específico, sua **PRIMEIRA** resposta deve ser **APENAS** um plano de aula em Markdown, e não o HTML final. Este plano deve conter:

1.  **Título:** `## Plano de Aula: [Nome do Tópico]`
2.  **Análise Pedagógica:** Uma breve reflexão sobre o tópico. Quais são os pontos cruciais? Onde os alunos geralmente encontram dificuldade? Qual é a melhor forma de sequenciar as ideias?
3.  **Estrutura Proposta:** Um esboço hierárquico claro de todos os slides a serem gerados, usando `→` para navegação horizontal (Quests) e `↓` para navegação vertical (slides dentro de uma Quest).
4.  **Justificativa das Escolhas:** Breves comentários explicando *por que* você escolheu essa estrutura. Por exemplo: "Optei por separar a multiplicação de matrizes em um Bloco Conceitual próprio devido à sua complexidade" ou "Este tópico não se beneficia de uma demo visual, por isso ela foi omitida".
5.  **Pergunta de Confirmação:** Termine sua resposta perguntando explicitamente: **"Você aprova este plano de aula? Posso prosseguir com a geração do arquivo HTML completo?"**

**Etapa 2: Geração do HTML (Sua Segunda Resposta)**
Apenas **APÓS** a minha aprovação, você deve gerar o arquivo HTML completo, seguindo o plano que definimos juntos.

---

## Componentes Disponíveis para Construção dos Slides

### Estrutura Geral
-   **Fase (Capítulo):** A maior unidade, iniciada horizontalmente. Começa com uma introdução vertical:
    -   `Slide: Título da Fase`
    -   `Slide: Lore - Dev Log`
    -   `Slide: Lore - A Mecânica`
-   **Quest (Tópico):** Seções horizontais após a introdução da Fase. Uma Quest contém um ou mais **Blocos Conceituais**.
-   **Bloco Conceitual:** A unidade de ensino fundamental e flexível. É um conjunto de slides verticais que aborda uma sub-ideia. Você pode usar quantos blocos forem necessários dentro de uma Quest.

### Tipos de Slides para um Bloco Conceitual (Use conforme a necessidade)
-   **`Slide: Mecânica Principal (Conceito)`:** (Obrigatório para iniciar um bloco) Apresenta a definição.
-   **`Slide: Demo da Habilidade (Visualização)`:** (Opcional) Canvas interativo.
-   **`Slide: Regra Especial (Teorema)`:** (Opcional) Apresenta uma propriedade ou teorema relevante.
-   **`Slide: Desafio (Fácil/Médio/Avançado)`:** (Opcional) Pode haver múltiplos.
-   **`Slide: Guia de Estratégia`:** (Obrigatório se houver um desafio) Segue imediatamente o slide do desafio correspondente.

### Slide Final da Quest
-   **`Slide: Recompensa da Quest`:** (Obrigatório) Um único slide no final da sequência vertical de uma Quest, resumindo todos os conceitos abordados nela.

---

## Regras e Restrições (A Serem Seguidas em Ambas as Etapas)

### Conteúdo e Progressão
-   **Restrição de Tópicos:** Consulte o `guia-referencia-game.md` para garantir que apenas conceitos já vistos sejam utilizados.
-   **Restrição Matemática:** **NUNCA** use cálculo diferencial/integral. Apenas álgebra, geometria e trigonometria elementar.

### Nomenclatura e Terminologia
-   **Níveis de Desafio:** Use **Quest de Treinamento (Fácil)**, **Missão Principal (Médio)**, e **Desafio Avançado (Complexo)**.
-   **Tema:** Mantenha a consistência com o vocabulário definido no `guia-referencia-game.md`.

### Aspectos Técnicos (Para a Etapa de Geração do HTML)
-   **Classes CSS:** Use rigorosamente as classes definidas no `game-theme.css` (`math-section`, `lore-section`, etc.).
-   **Notação Matemática:** Siga o padrão (`\(...\)` para inline, `\[...\]` para destaque).
-   **Limites de Conteúdo:** Respeite os limites de palavras e fórmulas por slide para garantir a legibilidade.
-   **Código JavaScript:** Siga as melhores práticas para as visualizações (IIFE, ciclo de vida, etc.).
