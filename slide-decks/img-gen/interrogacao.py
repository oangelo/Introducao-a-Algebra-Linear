#!/usr/bin/env python3
"""Escreve uma INTERROGACAO a lapis na capa do caderno fechado (cartela Q10).

Por que isto existe: a cena vem do gerador, mas o sinal -- "?" -- tem de ser
desenhado. Pedir "um ponto de interrogacao escrito na capa" ao difusor devolve
texto ilegivel (e texto ilegivel e proibido em Camada B).

Tres coisas fazem o sinal parecer escrito a mao e nao plotado:
 1. espessura varia ao longo do traco (fina na entrada e na saida, cheia no meio);
 2. inclinacao de escrita (shear), somada ao giro que acompanha a capa;
 3. duas passadas levemente deslocadas -- o lapis volta por cima do proprio traco.
"""
import argparse
import math
import random

from PIL import Image, ImageDraw, ImageFilter

from marcas_contagem import queimar


def _bezier(p0, p1, p2, p3, n):
    pts = []
    for i in range(n):
        t = i / n
        u = 1 - t
        pts.append((u**3 * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0] + t**3 * p3[0],
                    u**3 * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1] + t**3 * p3[1]))
    return pts


def _catmull(ancoras, amostras=14):
    """Spline de Catmull-Rom por pontos-ancora.

    Arco + bezier costurados davam quina no encontro do gancho com a haste ("bico").
    O spline passa por todos os pontos com tangente continua: o gancho vira curva
    de verdade e a entrada da haste nao tem aresta.
    """
    p = [ancoras[0]] + list(ancoras) + [ancoras[-1]]
    pts = []
    for i in range(len(p) - 3):
        p0, p1, p2, p3 = p[i], p[i + 1], p[i + 2], p[i + 3]
        for j in range(amostras):
            t = j / amostras
            t2, t3 = t * t, t * t * t
            pts.append(tuple(0.5 * ((2 * p1[k]) +
                                    (-p0[k] + p2[k]) * t +
                                    (2 * p0[k] - 5 * p1[k] + 4 * p2[k] - p3[k]) * t2 +
                                    (-p0[k] + 3 * p1[k] - 3 * p2[k] + p3[k]) * t3)
                             for k in (0, 1)))
    pts.append(ancoras[-1])
    return pts


def glifo(r):
    """Pontos do "?" em coordenadas locais (y para baixo): gancho, haste, ponto."""
    ancora = [(-0.74, 0.16),      # entrada, a esquerda e abaixo do centro
              (-0.56, -0.52),
              (-0.02, -0.94),     # topo do gancho
              (0.58, -0.44),
              (0.44, 0.10),       # volta pelo lado direito
              (0.00, 0.58)]       # desemboca na haste, sem quina
    pts = _catmull([(x * r, y * r) for x, y in ancora])
    pts += [(0.0, r * (0.58 + 1.02 * i / 12)) for i in range(1, 13)]
    return pts


def escrever(d, pts, cor, peso, acaso, tremor=0.7, passadas=2):
    """Traco com espessura variavel: fino nas pontas, cheio no meio do gancho."""
    n = len(pts)
    for passada in range(passadas):
        ox, oy = acaso.uniform(-0.9, 0.9), acaso.uniform(-0.9, 0.9)
        for i in range(n - 1):
            f = i / (n - 1)
            # bojo: maximo por volta de 35% do traco (meio do gancho); afina no fim
            bojo = 0.52 + 0.78 * math.sin(math.pi * min(1.0, f * 1.22)) ** 0.7
            larg = max(1, int(peso * bojo * (0.7 if passada else 1.0)))
            x0, y0 = pts[i]
            x1, y1 = pts[i + 1]
            d.line([(x0 + ox + acaso.uniform(-tremor, tremor),
                     y0 + oy + acaso.uniform(-tremor, tremor)),
                    (x1 + ox + acaso.uniform(-tremor, tremor),
                     y1 + oy + acaso.uniform(-tremor, tremor))],
                   fill=cor, width=larg, joint="curve")

    # ponto: batidas sobrepostas, redondas (tracinho horizontal le como virgula)
    px, py = pts[-1][0] + peso * 1.1, pts[-1][1] + peso * 3.2
    for _ in range(3):
        rr = peso * acaso.uniform(0.5, 0.72)
        cx2 = px + acaso.uniform(-1.2, 1.2)
        cy2 = py + acaso.uniform(-1.2, 1.2)
        d.ellipse((cx2 - rr, cy2 - rr, cx2 + rr, cy2 + rr), fill=cor)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--img", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--cx", type=float, default=0.43)
    p.add_argument("--cy", type=float, default=0.50)
    p.add_argument("--raio", type=float, default=0.072, help="fracao da largura")
    p.add_argument("--giro", type=float, default=18.0, help="graus: inclinacao da capa")
    p.add_argument("--inclinacao", type=float, default=9.0,
                   help="graus de shear: a mao escreve inclinada")
    p.add_argument("--peso", type=float, default=8.0, help="espessura base em px")
    p.add_argument("--vermelho", action="store_true")
    p.add_argument("--semente", type=int, default=23)
    a = p.parse_args()

    base = Image.open(a.img).convert("RGB")
    w, h = base.size
    r = w * a.raio
    pts = glifo(r)

    # shear (inclinacao de escrita) + giro (inclinacao da capa), nos pontos: rodar
    # a camada depois borraria o traco, e o traco e o assunto da cartela.
    k = math.tan(math.radians(a.inclinacao))
    t = math.radians(a.giro)
    ct, st = math.cos(t), math.sin(t)
    transf = []
    for x, y in pts:
        xs = x - k * y
        transf.append((xs * ct - y * st, xs * st + y * ct))

    camada = Image.new("RGBA", base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(camada)
    acaso = random.Random(a.semente)
    cor = (168, 40, 32, 228) if a.vermelho else (52, 49, 45, 236)
    escrever(d, [(x + w * a.cx, y + h * a.cy) for x, y in transf], cor, a.peso, acaso)

    camada = camada.filter(ImageFilter.GaussianBlur(0.45))
    queimar(base, camada, a.semente).save(a.out)
    print(f"ok {a.out} centro=({w * a.cx:.0f},{h * a.cy:.0f}) raio={r:.0f} "
          f"peso={a.peso} giro={a.giro} shear={a.inclinacao}")


if __name__ == "__main__":
    main()
