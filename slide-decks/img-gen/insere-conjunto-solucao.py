import re

p = "/opt/data/workspace/Introducao-a-Algebra-Linear/worktrees/slides/slide-decks/f1-matematica.html"
s = open(p, encoding="utf-8").read()

# 1) renumeração descendente: abrimos espaço para três blocos novos depois de 1.1
mapa = {9: 12, 8: 11, 7: 10, 6: 9, 5: 8, 4: 7, 3: 6, 2: 5}
for velho in sorted(mapa, reverse=True):
    novo = mapa[velho]
    s = re.sub(r"\b1\.%d\b" % velho, "1.%d" % novo, s)

s = s.replace("Nove blocos curtos.", "Doze blocos curtos.")

novos = '''
<section class="conceito">
  <h3><span class="num">1.2</span>De onde viemos: a reta da Geometria Analítica</h3>
  <p>Em Geometria Analítica, \(ax + by = c\), com \(a\) e \(b\) não ambos nulos, é uma <b>reta</b> no
  plano. O conjunto de todos os pares que satisfazem a equação é
  \(S = \\{(x, y) \\in \\mathbb{R}^2 : ax + by = c\\}\) — e ele tem <b>infinitos</b> pontos.</p>
  <p>Resolver um sistema de duas equações é, em geometria, perguntar pela <b>interseção</b> de duas
  retas. Três casos, e só três: se elas se cruzam, a interseção é <b>um ponto</b>; se coincidem, a
  interseção é a <b>reta inteira</b>; se são paralelas distintas, a interseção é <b>vazia</b>.</p>
  <p class="curto">O erro que se ouve: "paralelas dão infinitas soluções". Não dão nenhuma — paralelas
  distintas não têm ponto em comum. Coincidentes, sim, é que dão infinitas.</p>
</section>

<section class="conceito">
  <h3><span class="num">1.3</span>O conjunto-solução: a resposta é um conjunto</h3>
  <p>Solução não é uma lista de números: é um <b>conjunto</b>. E a notação importa, porque ela é o
  que permite dizer "não tem solução" sem soar como "não consegui":</p>
  <p>\(\\{(3, 1)\\}\) — conjunto unitário, uma solução. &nbsp; \(S = \\{(x,y) : x + y = 3\\}\) —
  infinitos pontos, a reta. &nbsp; \(\\varnothing\) — conjunto vazio, nenhuma solução.</p>
  <p>Com isso, o sistema deixa de ser uma conta e passa a ser uma <b>interseção</b>:
  \(S = S_1 \\cap S_2 \\cap \\dots \\cap S_m\), onde cada \(S_i\) é o conjunto-solução de uma equação.
  Achar a solução do sistema é achar o que sobrou de comum a todas.</p>
  <p class="curto">Contar soluções, então, é perguntar quantos elementos tem \(S\): zero, um, ou
  infinitos. Não existe "dois" — e o motivo é algébrico (ver 1.6).</p>
</section>

<section class="conceito">
  <h3><span class="num">1.4</span>Por que desenhar não escala</h3>
  <p>Duas variáveis: retas no plano, desenho fácil. Três variáveis: planos no espaço, já é difícil
  enxergar. Quatro: não há desenho. E o curso inteiro trabalha com quatro, cinco, \(n\).</p>
  <p>A geometria continua valendo — mas como <b>conferência</b> do resultado em \(\\mathbb{R}^2\), não
  como método. Daqui para frente o caminho é algébrico: guardar só os coeficientes na matriz e
  aplicar operações que <b>não mudam o conjunto-solução</b>. É esse o método que funciona em qualquer
  dimensão.</p>
  <p class="curto">É a razão de a matriz existir: ela não é uma notação bonita, é o desenho que
  sobrevive quando não dá mais para desenhar.</p>
</section>
'''

marcador = '''  <p class="curto">O teste prático: se você consegue escrever como \\(a_1x_1 + a_2x_2 + \\dots = b\\),
  é linear. Se precisa de gráfico torto para descrever, não é.</p>
</section>
'''
assert marcador in s, "não achei o fim de 1.1"
s = s.replace(marcador, marcador + novos, 1)

open(p, "w", encoding="utf-8").write(s)
print("3 blocos novos inseridos; numeração 1.1–1.12")
