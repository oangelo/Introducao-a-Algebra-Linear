# AGENTS.md — Guia para Agentes de IA

Repositório do curso **Introdução à Álgebra Linear** ("Pronto, Jogador 1?"), de autoria do
Prof. Angelo Mondaini Calvão para os cursos de engenharia do IPRJ/UERJ.

Todos os materiais seguem um **tema de arcade/jogo**: o aluno é um "Jogador", os capítulos
são "Fases", os exercícios são "Quests" e as provas são "Chefes". O tom é sério no conteúdo
matemático e leve na embalagem.

Livro adotado: **ANTON, Howard. _Álgebra Linear com Aplicações_.**

---

## Estrutura de Diretórios

| Diretório | Conteúdo |
|-----------|----------|
| `exercicios/` | Listas de exercícios em HTML, uma pasta por capítulo (`capitulo-1/` … `capitulo-6/`) |
| `slide-decks/` | Apresentações Reveal.js (HTML soltos na raiz + `css/`, `js/`, `plugin/` do framework) |
| `quiz/` | Mini-chefes (quizzes) em Markdown, um por tópico |
| `Provas/` | Provas antigas em PDF, organizadas por ano/semestre |
| `PROVAS.md` | Índice e histórico das provas |
| `notas/` | Notas de acompanhamento por semestre (Markdown) |
| `audio/` | Narrações em MP3 usadas como abertura das fases |
| `memes/` | Imagens de apoio (humor interno do curso) |
| `pesquisas-discente/` | Questionários e dados de pesquisa com discentes |
| `scripts/` | Roteiros das narrações em Markdown |
| `img/` | Imagens e SVGs do curso |
| `roleta.html` | Sorteio de temas/alunos em sala |
| `worktrees/` | Git worktrees (ignorado pelo git) |

Capítulos (Fases):

| Cap | Tema | Pasta |
|-----|------|-------|
| 1 | Sistemas e Matrizes | `exercicios/capitulo-1/` |
| 2 | Determinantes | `exercicios/capitulo-2/` |
| 3 | Vetores Euclidianos | `exercicios/capitulo-3/` |
| 4 | Transformações Lineares | `exercicios/capitulo-4/` |
| 5 | Espaços Vetoriais | `exercicios/capitulo-5/` |
| 6 | Autovalores e Autovetores | `exercicios/capitulo-6/` |

---

## Git Worktrees (branches de conteúdo)

Este repositório usa a mesma organização dos repositórios de Geometria Analítica e Cálculo
Vetorial: cada tipo de conteúdo tem um worktree com branch própria, para permitir trabalho
paralelo sem misturar commits.

### Estrutura

```
Introducao-a-Algebra-Linear/
├── worktrees/
│   ├── exercicios/      → branch 'feature/exercicios'
│   ├── exercicios-aula/ → branch 'feature/exercicios-aula'
│   ├── slides/          → branch 'feature/slides'
│   └── provas/          → branch 'feature/provas'
└── (raiz)               → branch 'main'
```

### Regra crítica de criação

Sempre criar o worktree **dentro de `worktrees/`**:

```bash
# Correto
git worktree add worktrees/minha-branch -b minha-branch

# Errado — cria fora do repo e embaralha a raiz
git worktree add ../minha-branch
```

### Workflow

1. **Navegue até o worktree** correspondente ao conteúdo:
   - Exercícios de casa → `worktrees/exercicios/`
   - Exercícios de sala → `worktrees/exercicios-aula/`
   - Slides → `worktrees/slides/`
   - Provas → `worktrees/provas/`
2. **Edite e commite dentro do worktree** (cada branch tem histórico próprio).
3. **Integre na `main`** por merge, a partir da raiz:
   ```bash
   git merge feature/exercicios
   ```
4. **Nunca commite a pasta `worktrees/`** — ela está no `.gitignore`.

> O deploy do GitHub Pages dispara **só em push para `main`**. Trabalho em branch não
> publica nada até ser integrado.

---

## Build/Test/Lint

O projeto usa **gulp** (Reveal.js e empacotamento) e não tem suíte de testes de conteúdo.

```bash
npm install          # primeira vez

npm run build        # gulp build — js, css e plugins do Reveal
npm start            # gulp serve — servidor local de desenvolvimento
npm test             # gulp test — eslint + qunit (do próprio Reveal.js)
```

Para testar exercícios e slides sem o gulp:

```bash
python3 -m http.server 8080
# http://localhost:8080/exercicios/capitulo-1/sistemas-lineares.html
# http://localhost:8080/slide-decks/eliminacao_gaussiana.html
```

Verificação manual obrigatória após qualquer mudança visual:

1. O CSS carregou (tema arcade, não HTML cru)?
2. O MathJax renderizou as fórmulas?
3. A interatividade funciona (canvas, botões, navegação do Reveal em todas as direções)?
4. Os links relativos (`../game-theme-exercises.css`, `game-theme.css`) resolvem?

---

## Convenções

### Nomenclatura

- Tudo em **kebab-case**: `sistemas-lineares.html`, `matrizes-inversas.html`.
- Exercícios de casa: `exercicios/capitulo-N/nome-do-topico.html`
- Slides: `slide-decks/nome-do-topico.html` (HTML solto na raiz de `slide-decks/`)
- Quiz: `quiz/nome_do_topico.md` (estes usam snake_case, por legado)
- Idiomas: todo o conteúdo em **pt-BR**.

### CSS

- Exercícios: `game-theme-exercises.css` (raiz de `exercicios/`)
- Slides: `game-theme.css` (raiz de `slide-decks/`)
- **Não crie CSS novo nem `<style>` inline** — use as classes existentes.
- Fontes: `Press Start 2P` (títulos) e `VT323` (corpo), via Google Fonts.

### MathJax (regra crítica)

- Delimitadores: `\(...\)` para inline e `\[...\]` para bloco — **uma barra** no arquivo.
- **Nunca** `\\(`, `\\[` ou `\\frac`: barra dupla quebra a renderização.
- Após escrever cada arquivo, verifique:
  ```bash
  grep -c '\\\\' arquivo.html   # deve ser 0
  ```

---

## Regras por Diretório

### Exercícios (`exercicios/`)

1. Um arquivo HTML autocontido por tópico (não há padrão de três arquivos neste repo).
2. Estrutura narrativa: motivação → conceito → exemplo → exercícios progressivos.
3. Progressão de dificuldade: básico com dica explícita → intermediário → avançado.
4. Cada exercício deve ter **motivação clara** (por que aquele cálculo importa), não apenas
   o enunciado seco.
5. Use apenas conceitos já cobertos na progressão dos capítulos — não antecipe conteúdo.
6. Soluções em `<details><summary>...</summary>` para não entregar a resposta de imediato.

### Slides (`slide-decks/`)

1. Reveal.js 4.3.1 via CDN + `game-theme.css` local. HTML solto, sem loader por capítulo.
2. Navegação: horizontal entre tópicos, vertical para aprofundamento.
3. Um conceito por slide; nada de slide-enciclopédia.
4. **Necessidade antes da definição**: mostre o problema que cria a demanda pela ferramenta
   antes de formalizar.
5. Canvas 2D para visualizações; não introduza Three.js.
6. Zero CSS inline — tudo em `game-theme.css`.

### Provas (`Provas/` + `PROVAS.md`)

1. Provas antigas ficam em PDF, por ano/semestre (`Provas/2025-1/`, …).
2. `PROVAS.md` é o índice: mantenha atualizado ao adicionar arquivos.
3. Antes de gerar prova nova, colete tipo (P1, P2, PS, PF) e tópicos, **proponha o plano e
   aguarde aprovação explícita** do professor.

### Quiz (`quiz/`)

1. Markdown, um arquivo por tópico.
2. Perguntas curtas de verificação conceitual (mini-chefe), não contas longas.

---

## Checklist de Qualidade

Antes de qualquer commit:

- [ ] MathJax com barra simples — `grep -c '\\\\'` retorna 0
- [ ] Nenhum CSS novo e nenhum `style=` inline
- [ ] Classes do tema arcade existentes (`console-header`, etc.) — não inventar
- [ ] Números decimais com vírgula (`0{,}5`)
- [ ] Notação: vetores com `\vec{v}`, pontos em maiúscula
- [ ] Links relativos corretos para CSS/JS
- [ ] Nenhum conceito de capítulo posterior antecipado
- [ ] Arquivos em kebab-case
- [ ] Verificação visual feita no navegador

---

## O que Evitar

- NÃO quebrar links existentes (o README aponta para o GitHub Pages).
- NÃO renomear IDs/classes CSS sem atualizar todos os arquivos que as usam.
- NÃO misturar temas visuais entre exercícios e slides.
- NÃO usar jQuery — DOM nativo.
- NÃO commitar `worktrees/`, `node_modules/`, `dist/` nem arquivos `.env`.
- NÃO fazer merge de branch na `main` sem revisão: o push na `main` publica o site.

---

## Referências

- `README.md` — visão do curso, ementa e índice de links públicos
- `calendario.md` — cronograma do semestre
- `PROVAS.md` — histórico de provas
- `slide-decks/game-theme.css` — classes e paleta do tema
- `exercicios/game-theme-exercises.css` — classes e paleta dos exercícios
- Repositórios irmãos (mesmo padrão de worktrees): `oangelo/Geometria-Analitica-Sobrevivencia-Geometrica`
  e `oangelo/Calculo-Vetorial-Exploracao-Espacial`
