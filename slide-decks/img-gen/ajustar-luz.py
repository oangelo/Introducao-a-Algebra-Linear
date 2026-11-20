#!/usr/bin/env python3
"""Corrige exposicao de cena gerada sem repintar: gama nas sombras + saturacao.

Por que existe: pedir "mais claro" ao gerador muda a composicao inteira, e a cena ja estava
certa no desenho. Ajustar a curva aqui e deterministico e reversivel (basta rodar de novo
a partir do raw).

Uso:
  uv run --with pillow python img-gen/ajustar-luz.py --img raw.png --out saida.png --gama 0.75
"""
import argparse

from PIL import Image, ImageEnhance

ap = argparse.ArgumentParser()
ap.add_argument("--img", required=True)
ap.add_argument("--out", required=True)
ap.add_argument("--gama", type=float, default=1.0, help="<1 clareia as sombras, >1 escurece")
ap.add_argument("--ganho", type=float, default=1.0, help="exposicao geral: <1 escurece a cena inteira")
ap.add_argument("--sat", type=float, default=1.0)
ap.add_argument("--contraste", type=float, default=1.0)
a = ap.parse_args()

img = Image.open(a.img).convert("RGB")
if a.ganho != 1.0:
    img = ImageEnhance.Brightness(img).enhance(a.ganho)
if a.gama != 1.0:
    lut = [min(255, int(round(255 * (i / 255) ** a.gama))) for i in range(256)]
    img = img.point(lut * 3)
if a.sat != 1.0:
    img = ImageEnhance.Color(img).enhance(a.sat)
if a.contraste != 1.0:
    img = ImageEnhance.Contrast(img).enhance(a.contraste)
img.save(a.out)
print("ok %s gama=%s sat=%s" % (a.out, a.gama, a.sat))
