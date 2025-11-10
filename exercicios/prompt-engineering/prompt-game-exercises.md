# Diretrizes Mestras para Geração de Exercícios - Álgebra Arcade

## Filosofia Central
O objetivo é criar materiais de Álgebra Linear que sejam **pedagogicamente eficazes**, **claros** e **tematicamente engajantes**. A didática e a clareza sempre prevalecem sobre a adesão cega a um template.

## Processo de Geração Interativo (LEIA COM ATENÇÃO)
Este é um processo colaborativo em duas etapas:

**Etapa 1: Plano de Missões (Sua Primeira Resposta)**
Quando eu solicitar a criação de uma lista de exercícios para um tópico específico, sua **PRIMEIRA** resposta deve ser **APENAS** um plano de missões em Markdown, e não o HTML final. Este plano deve conter:

1.  **Título:** `## Plano de Missões: [Nome do Tópico]`
2.  **Análise Pedagógica:** Uma breve reflexão sobre os pontos-chave do tópico e como a lista de exercícios abordará a progressão de aprendizado.
3.  **Estrutura Proposta (Tabela):** Um esboço claro dos 12 exercícios em uma tabela com as seguintes colunas:
    *   `Missão`: O identificador (ex: "1-A (Treinamento)").
    *   `Título Temático`: O nome da missão (ex: "Movimento do Avatar").
    *   `Conceito Principal`: O foco matemático (ex: "Soma de Vetores").
    *   `Objetivo da Missão`: O que o aluno vai praticar (ex: "Praticar a adição de vetores componente a componente").
    *   `Contexto do Problema`: Uma breve descrição do cenário do jogo (ex: "Calcular a posição final de um personagem após dois movimentos.").
4.  **Pergunta de Confirmação:** Termine sua resposta perguntando explicitamente: **"Este plano de missões está alinhado com o objetivo pedagógico? Posso prosseguir com a geração do arquivo HTML completo?"**

**Etapa 2: Geração do HTML (Sua Segunda Resposta)**
Apenas **APÓS** a minha aprovação do plano, você deve gerar o arquivo HTML completo, seguindo rigorosamente o plano que definimos juntos e as regras abaixo.

---

## Regras e Restrições (A Serem Seguidas em Ambas as Etapas)

### Conteúdo e Progressão
-   **Restrição de Tópicos:** Consulte o `guia-tematico-arcade.md` para garantir que apenas conceitos já vistos sejam utilizados.
-   **Restrição Matemática:** **NUNCA** use cálculo diferencial/integral.
-   **Contexto de Jogo:** Relacione a temática à **Era dos Videogames** apropriada do `guia-tematico-arcade.md`.

### Estrutura e Formato (Para a Etapa de Geração do HTML)
-   Siga **EXATAMENTE** a estrutura do `template-game-exercises.html`.
-   **Objetivo da Missão:** Cada exercício deve começar com uma `div.mission-objective`.
-   **Ajuda Opcional:** A dica (`div.hint`) deve estar dentro de uma `<details class="hint-container">` com o sumário `Pedir Dica ao Mestre do Jogo...`. Omitir para a série "Boss Fights".
-   **Solução como Guia:** O detonado (`details > ol.solution-steps`) **NÃO** deve conter a resposta numérica. Deve apenas descrever os passos lógicos do raciocínio.
-   **Vocabulário:** O termo matemático formal é sempre o principal. O termo temático é um "apelido" usado em títulos e contexto.

### Níveis de Dificuldade
-   **Exercícios 1-3:** Training Quests (Básico)
-   **Exercícios 4-6:** Main Missions (Intermediário)
-   **Exercícios 7-9:** Elite Challenges (Avançado)
-   **Exercícios 10-12:** Boss Fights (Complexo, sem dicas)
