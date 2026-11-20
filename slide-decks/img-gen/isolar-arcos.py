#!/usr/bin/env python3
"""Cartela "isolar a variavel": um salto, varios desfechos.

A cena vem do gerador; as trajetorias NAO. Arco por difusao sai errado e nao fecha no alvo.
Aqui cada parabola e uma quadratica de verdade, e as silhuetas dos desfechos sao recortes da
propria personagem (fundo removido por flood fill a partir da borda do recorte).

Uso:
  python isolar-arcos.py --img base.png --out final.png \
      --boneco 246,116,356,236 --pe 400,232
"""
import argparse, math, sys
from PIL import Image, ImageDraw

ap = argparse.ArgumentParser()
ap.add_argument("--img", required=True)
ap.add_argument("--out", required=True)
ap.add_argument("--boneco", required=True, help="x1,y1,x2,y2 do recorte da personagem")
ap.add_argument("--pe", default="0,0", help="ignorado: o pe e medido no recorte")
ap.add_argument("--placar", default="plataforma",
                choices=["plataforma", "penhasco"])
a = ap.parse_args()

X0, Y0 = [int(v) for v in a.pe.split(",")]
CX1, CY1, CX2, CY2 = [int(v) for v in a.boneco.split(",")]

base = Image.open(a.img).convert("RGBA")
W, H = base.size


RESAMPLE = getattr(getattr(Image, "Resampling", Image), "BICUBIC")


def recortar(caixa, tol=26):
    """Fundo removido por flood fill a partir da borda; o que sobra e a personagem."""
    x1, y1, x2, y2 = caixa
    c = base.crop((x1, y1, x2, y2)).convert("RGBA")
    px = c.load()
    w, h = c.size
    fundo = [[False] * w for _ in range(h)]
    pilha = []
    for x in range(w):
        pilha += [(x, 0), (x, h - 1)]
    for y in range(h):
        pilha += [(0, y), (w - 1, y)]
    ref = px[0, 0][:3]
    while pilha:
        x, y = pilha.pop()
        if x < 0 or y < 0 or x >= w or y >= h or fundo[y][x]:
            continue
        r, g, b, _ = px[x, y]
        if abs(r - ref[0]) + abs(g - ref[1]) + abs(b - ref[2]) > tol:
            continue
        fundo[y][x] = True
        pilha += [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

    # a grama que sobra entre os pes nao e personagem: derruba qualquer verde-dominante
    for y in range(h):
        for x in range(w):
            r, g, b, _ = px[x, y]
            if g > r + 14 and g > b + 6:
                fundo[y][x] = True

    m = c.copy()
    mp = m.load()
    for y in range(h):
        for x in range(w):
            if fundo[y][x]:
                mp[x, y] = (0, 0, 0, 0)
    return m


sprite = recortar((CX1, CY1, CX2, CY2))

# pe da personagem medido no proprio recorte: uniao das ultimas linhas com pixel (os dois pes)
_sp = sprite.load()
_w, _h = sprite.size
_alt_min = max(6, int(_h * 0.10))
_base_y = max(y for y in range(_h) if any(_sp[x, y][3] > 40 for x in range(_w)))
_baixo = [x for y in range(_base_y - _alt_min, _base_y + 1)
          for x in range(_w) if _sp[x, y][3] > 40]
PE_X = (min(_baixo) + max(_baixo)) // 2
PE_Y = _base_y

X0, Y0 = CX1 + PE_X, CY1 + PE_Y


def curva(p0, p1, apex):
    """Parabola de p0 a p1 com o topo `apex` pixels acima da corda. y cresce para baixo."""
    def f(t):
        x = p0[0] + (p1[0] - p0[0]) * t
        y = p0[1] + (p1[1] - p0[1]) * t - 4 * apex * t * (1 - t)
        return x, y
    return f


def tracejado(d, f, cor, larg=4, passo=16, traco=9):
    n = 400
    pts = [f(i / n) for i in range(n + 1)]
    acc, ligado = 0.0, True
    ultimo = pts[0]
    for p in pts[1:]:
        acc += math.dist(p, ultimo)
        if ligado:
            d.line([ultimo, p], fill=cor, width=larg)
        if acc >= (traco if ligado else passo - traco):
            ligado = not ligado
            acc = 0.0
        ultimo = p


def fantasma(pos, ang, alfa=155):
    # gira em torno do proprio pe: o pe fica exatamente no ponto da trajetoria
    folga = sprite.height
    big = Image.new("RGBA", (sprite.width * 3, sprite.height * 3), (0, 0, 0, 0))
    big.alpha_composite(sprite, (folga, folga))
    anc = (folga + PE_X, folga + PE_Y)
    g = big.rotate(ang, center=anc, resample=RESAMPLE)
    g.putalpha(g.split()[3].point(lambda v: int(v * alfa / 255)))
    base.alpha_composite(g, (int(pos[0] - anc[0]), int(pos[1] - anc[1])))


# desfechos: (destino, apex, rotacao) -- curto, quase, passa direto
DESFECHOS = [
    ((560, 762), 95, 100),    # cai: chega na agua
    ((736, 430), 150, 72),    # quase: morre no ar, logo antes da quina da plataforma
    ((1100, 520), 200, 118),  # passa direto: ultrapassa a plataforma
]

for alvo, apex, ang in DESFECHOS:
    fantasma(alvo, ang)

# a que acerta, na plataforma: personagem com halo sob os pes
ALVO = (900, 378) if a.placar == "plataforma" else (900, 380)
halo = Image.new("RGBA", base.size, (0, 0, 0, 0))
dh = ImageDraw.Draw(halo)
for i in range(9, 0, -1):
    dh.ellipse([ALVO[0] - 19 * i / 9, ALVO[1] - 7 * i / 9,
                ALVO[0] + 19 * i / 9, ALVO[1] + 7 * i / 9],
               fill=(255, 176, 58, 26))

# trajetorias: desenhadas atras do personagem, fechando no pe de cada desfecho
camada = Image.new("RGBA", base.size, (0, 0, 0, 0))
d = ImageDraw.Draw(camada)
for alvo, apex, _ in DESFECHOS:
    tracejado(d, curva((X0, Y0), alvo, apex), (240, 240, 245, 165), larg=4)
f = curva((X0, Y0), ALVO, 150)
d.line([f(i / 400) for i in range(401)], fill=(255, 176, 58, 235), width=7, joint="curve")
base.alpha_composite(camada)

# halo e personagem por cima: a trajetoria entra por baixo dos pes
base.alpha_composite(halo)
base.alpha_composite(sprite, (int(ALVO[0] - PE_X), int(ALVO[1] - PE_Y)))

base.convert("RGB").save(a.out, quality=95)
print("ok %s  pe=(%d,%d)" % (a.out, X0, Y0))
