Criar slides interativos para um curso de Introdução à Álgebra Linear usando o tema de jornada do jogador/videogame retrô. A estrutura deve ter navegação horizontal entre Fases (capítulos) e navegação vertical para aprofundamento em cada Quest (tópico). O conteúdo deve apresentar uma separação clara entre o conteúdo matemático formal e a "lore" (contextualização).

Princípio do Conteúdo Atômico: Um Conceito por Slide

Para garantir clareza, legibilidade e evitar que o conteúdo exceda o espaço da tela, cada slide deve focar em uma única ideia central.

EVITE: Agrupar múltiplos problemas ou múltiplos roteiros de solução em um único slide. Um slide que tenta mostrar três estratégias de uma vez e tem o conteúdo cortado é um exemplo a ser evitado.

PREFIRA: Dividir listas e conceitos complexos em uma sequência de slides verticais, seguindo a estrutura abaixo.

Estrutura de Navegação

A apresentação utiliza uma organização hierárquica, com o guia de estratégia seguindo imediatamente seu desafio correspondente.

Navegação Horizontal: Entre diferentes Quests (tópicos principais).

Navegação Vertical: Para aprofundar cada Quest com slides atômicos.

Cada Quest (tópico principal) deve seguir esta estrutura:

Quest 1 (Horizontal →)
    ↓ (Vertical ↓)
    - Slide 1.1: Mecânica Principal (Conceito)
    - Slide 1.2: Demo da Habilidade (Visualização)
    - Slide 1.3: Regra Especial (Teorema)
    
    // Desafio e Estratégia em pares
    - Slide 1.4: Desafio: Quest de Treinamento (Fácil)
    - Slide 1.5: Guia de Estratégia (Fácil)

    - Slide 1.6: Desafio: Missão Principal (Médio)
    - Slide 1.7: Guia de Estratégia (Médio)

    - Slide 1.8: Desafio: Desafio Avançado (Complexo)
    - Slide 1.9: Guia de Estratégia (Avançado)

    - Slide 1.10: Recompensa (Síntese dos Conceitos)
Estrutura Sugerida dos Slides

Slide de título da Fase: Título principal e subtítulo temático.

Slide de Lore da Fase (Contexto): Apresenta o contexto temático e as figuras históricas como "desenvolvedores originais".

Para cada Quest (tópico principal), seguir a sequência vertical detalhada acima:

Slide de Mecânica Principal (Conceito): Definição formal e interpretação no jogo.

Slide de Demo da Habilidade (Visualização): Canvas interativo com controles.

Slide de Regra Especial (Teorema/Propriedade): Um teorema ou propriedade chave.

Slides de Desafio (Fácil, Médio, Avançado): Cada um em seu próprio slide vertical, contendo apenas o enunciado. Use a terminologia: Quest de Treinamento (Fácil), Missão Principal (Médio), e Desafio Avançado (Complexo).

Slides de Guia de Estratégia: Cada um em seu próprio slide vertical, seguindo imediatamente o desafio correspondente e descrevendo o roteiro para a solução, sem resolvê-la.

Slide de Recompensa (Síntese): Resumo dos conceitos-chave aprendidos na Quest.

Classes CSS Obrigatórias

Você DEVE usar as classes CSS específicas definidas no game-theme.css e no template.html:

math-section: Para todo conteúdo matemático formal.

lore-section: Para a contextualização temática (a "lore" do jogo).

problem-section: Para enunciados de desafios/problemas.

compact-solution: Para os Guias de Estratégia ("Detonados").

visualization-canvas, controls-container, game-interp, press-start.

Notação Matemática

A notação deve seguir estritamente as convenções:

Equações inline: \( ... \)

Equações em destaque: \[ ... \]

Vetores: \vec{v} para vetores geométricos, \mathbf{x} para vetores coluna. Seja consistente.

Matrizes: Letras maiúsculas, como A, B.

Escalares: Letras minúsculas, como a, b, \lambda.

Limites de Conteúdo (por slide)

Títulos: Máximo de 60 caracteres.

Conteúdo matemático: Máximo de 150 palavras.

Lore/Contexto: Máximo de 150 palavras.

Fórmulas: No máximo 1-2 fórmulas complexas por slide.

Padrões de Código JavaScript

Encapsulamento rigoroso com IIFE.

Gerenciamento do ciclo de vida com Reveal.on('slidechanged', ...) para init e cleanup de visualizações.

Uso de seletores DOM nativos (document.getElementById).

Preferência por Canvas 2D, usando Three.js apenas quando estritamente necessário.

Cancelamento de animações (cancelAnimationFrame) na função de limpeza.

Paleta de Cores para Visualizações

Vetores de Base (i, j, k): #E53935 (vermelho), #43A047 (verde), #1E88E5 (azul).

Vetor/Objeto Original: #FFFFFF (branco) ou #BDBDBD (cinza claro).

Vetor/Objeto Transformado: #FFB300 (amarelo/ouro).

Autovetores (Eigenvectors): #9C27B0 (roxo).

Espaço Nulo (Nullspace): Área sombreada com opacidade, cor #424242.

Espaço Coluna (Column Space/Image): Área sombreada com opacidade, cor #1E88E5.

Progressão Temática (Lore do Jogo)

Fase 1 (Sistemas e Matrizes): O Tutorial.

Fase 2 (Determinantes): A Chave Secreta.

Fase 3 (Espaços Vetoriais Euclidianos): Explorando o Mundo.

Fase 4 (Transformações Lineares): Portais e Habilidades.

Fase 5 (Espaços Vetoriais Arbitrários): As Leis do Universo do Jogo.

Fase Final (Autovalores/Autovetores): O Código-Fonte.

Foco dos Exemplos

O tema de jogo serve para emoldurar e motivar. Os desafios matemáticos devem ser clássicos e fundamentais. As conexões diretas com o tema devem aparecer nos slides de Lore e Easter Eggs (aplicações em computação gráfica, IA, etc.).
