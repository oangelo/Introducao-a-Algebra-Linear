#!/usr/bin/env python3
"""Tipografa um letreiro de fliperama sobre uma area da cena (ex.: WIN! no monitor).

Por que nao pedir o texto ao gerador: modelo de difusao escreve pseudo-texto. Aqui o texto
e desenhado por codigo, com fonte pixel de verdade (Press Start 2P), entao sai correto,
alinhado e reproduzivel.

Uso:
  uv run --with pillow python overlay-emblem.py \
      --img img/c3-vitoria.png --bbox 606,419,903,630 --text "WIN!" --out img/c3-vitoria.png
"""
import argparse
import sys

from PIL import Image, ImageDraw, ImageFont, ImageFilter

FONTE = "/opt/data/assets/fonts/PressStart2P-Regular.ttf"


def carregar(px):
    return ImageFont.truetype(FONTE, px)


def ajustar(texto, caixa_l, caixa_a, max_frac=0.34, frac_larg=0.70):
    """Maior tamanho em que o texto cabe na largura e na altura pedidas da caixa."""
    alvo_l, alvo_a = caixa_l * frac_larg, caixa_a * max_frac
    px = 8
    while px < 400:
        f = carregar(px + 1)
        l, a = f.getbbox(texto)[2], f.getbbox(texto)[3]
        if l > alvo_l or a > alvo_a:
            break
        px += 1
    return carregar(px)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--img", required=True)
    ap.add_argument("--out", default=None)
    ap.add_argument("--bbox", required=True, help="x1,y1,x2,y2")
    ap.add_argument("--text", required=True)
    ap.add_argument("--cor", default="#ffffff")
    ap.add_argument("--glow", default="#ffb03a")
    ap.add_argument("--frac", type=float, default=0.34)
    ap.add_argument("--largura", type=float, default=0.70,
                    help="fracao da largura da caixa que o texto pode ocupar")
    ap.add_argument("--frame", action="append", default=[],
                    help="x1,y1,x2,y2 de uma moldura; repetir para varias")
    ap.add_argument("--frame-cor", default="#0b0c10")
    ap.add_argument("--frame-larg", type=int, default=6)
    ap.add_argument("--oclui", action="store_true",
                    help="texto atras do que estiver na frente: so aparece no vidro, "
                         "medido por flood fill a partir das bordas do bbox")
    ap.add_argument("--tol", type=int, default=26)
    a = ap.parse_args()

    x1, y1, x2, y2 = [int(v) for v in a.bbox.split(",")]
    larg, alt = x2 - x1, y2 - y1
    if larg < 20 or alt < 10:
        sys.exit("bbox suspeita: %r" % a.bbox)

    base = Image.open(a.img).convert("RGBA")

    for espec in a.frame:
        fx1, fy1, fx2, fy2 = [int(v) for v in espec.split(",")]
        ImageDraw.Draw(base).rectangle(
            [fx1, fy1, fx2, fy2], outline=a.frame_cor, width=a.frame_larg)

    fonte = ajustar(a.text, larg, alt, a.frac, a.largura)

    camada = Image.new("RGBA", base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(camada)
    bb = d.textbbox((0, 0), a.text, font=fonte)
    tw, th = bb[2] - bb[0], bb[3] - bb[1]
    tx = x1 + (larg - tw) // 2 - bb[0]
    ty = y1 + (alt - th) // 2 - bb[1]

    d.text((tx, ty), a.text, font=fonte, fill=a.cor, stroke_width=max(2, fonte.size // 14),
           stroke_fill="#0b0c10")

    brilho = camada.filter(ImageFilter.GaussianBlur(max(3, fonte.size // 8)))
    halo = Image.new("RGBA", base.size, (0, 0, 0, 0))
    halo.paste(Image.new("RGBA", base.size, a.glow), (0, 0), brilho)

    saida = Image.alpha_composite(base, halo)
    saida = Image.alpha_composite(saida, camada)

    if a.oclui:
        # o vidro e uma cor chapada: flood fill das bordas do bbox marca so ele.
        # quem nao foi alcancado (jogador na frente) volta a ser o pixel original.
        px = base.convert("RGB").load()
        visto = [[False] * (y2 - y1 + 1) for _ in range(x2 - x1 + 1)]
        pilha = []
        for x in range(x1, x2 + 1):
            pilha += [(x, y1, 0, 0, 0), (x, y2, 0, 0, 0)]
        for y in range(y1, y2 + 1):
            pilha += [(x1, y, 0, 0, 0), (x2, y, 0, 0, 0)]
        while pilha:
            x, y, pr, pg, pb = pilha.pop()
            if not (x1 <= x <= x2 and y1 <= y <= y2):
                continue
            i, j = x - x1, y - y1
            if visto[i][j]:
                continue
            r, g, b = px[x, y]
            # comparacao com o pixel VIZINHO, nao com uma cor fixa: acompanha o degrade do vidro
            # e para na linha preta do contorno do jogador.
            if (pr or pg or pb) and abs(r - pr) + abs(g - pg) + abs(b - pb) > a.tol:
                continue
            visto[i][j] = True
            pilha += [(x + 1, y, r, g, b), (x - 1, y, r, g, b),
                      (x, y + 1, r, g, b), (x, y - 1, r, g, b)]
        mascara = Image.new("L", base.size, 0)
        mp = mascara.load()
        for i in range(x2 - x1 + 1):
            for j in range(y2 - y1 + 1):
                if visto[i][j]:
                    mp[x1 + i, y1 + j] = 255
        saida = Image.composite(saida, base, mascara)

    saida.convert("RGB").save(a.out or a.img)
    print("ok %s  fonte=%dpx  caixa=%dx%d" % (a.out or a.img, fonte.size, larg, alt))


if __name__ == "__main__":
    main()
