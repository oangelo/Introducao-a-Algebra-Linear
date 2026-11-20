#!/usr/bin/env python3
"""Desenha, na capa do caderno fechado, DUAS LINHAS IDENTICAS e um risco sobre elas.

Por que isto existe: a Q10 fecha o capitulo com "duas coisas que sempre andam
juntas sao uma so" -- e o que a Fase 1 vai chamar de dependencia linear. Isso so
funciona na imagem se as duas linhas forem *literalmente* iguais, e o gerador de
difusao nunca repete: ele varia cada traco. Entao a cena vem do gerador e as
duas linhas vem de codigo, com a mesma semente de tremor nas duas.

Uso:
  python fecho.py --img base.png --out saida.png [--cx 0.30] [--cy 0.62]
"""
import argparse
import random

from PIL import Image, ImageDraw, ImageFilter

from marcas_contagem import queimar, traco


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--img", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--cx", type=float, default=0.30,
                   help="centro horizontal das linhas (fracao da largura)")
    p.add_argument("--cy", type=float, default=0.62,
                   help="centro vertical das linhas (fracao da altura)")
    p.add_argument("--largura", type=float, default=0.30,
                   help="comprimento de cada linha (fracao da largura)")
    p.add_argument("--semente", type=int, default=11)
    p.add_argument("--giro", type=float, default=0.0)
    args = p.parse_args()

    base = Image.open(args.img).convert("RGB")
    w, h = base.size
    camada = Image.new("RGBA", base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(camada)
    grafite = (58, 55, 50, 232)
    vermelho = (152, 36, 30, 220)

    comprimento = w * args.largura
    x0 = w * args.cx - comprimento / 2
    y0 = h * args.cy
    vao = h * 0.080                      # distancia entre as duas linhas

    acaso = random.Random(args.semente)
    # o tremor e sorteado UMA vez e usado nas duas linhas: e o que as torna
    # identicas. Sortear de novo por linha faria duas linhas parecidas, nao iguais.
    altura_tique = h * 0.030
    passo = comprimento / 8
    inclina_tique = -altura_tique * 0.28   # tique de mao inclina; a 90 graus exatos
    #                                       todos eles formam um gradil e a linha
    #                                       le como torta (ilusao de Zollner)
    forma = []
    for i in range(8):
        forma.append((x0 + passo * (i + 0.5) + acaso.uniform(-1.5, 1.5),
                      acaso.uniform(-1.6, 1.6),
                      acaso.uniform(-1.4, 1.4)))

    for linha in range(2):
        yy = y0 + linha * vao
        for (bx, dy0, dy1) in forma:
            traco(d, bx + dy0, yy,
                  bx + dy1 + inclina_tique, yy + altura_tique,
                  grafite, 4, acaso, tremor=0.8)

    # um risco por linha, cada um dentro da sua faixa: um risco UNICO entre as
    # duas lia como divisoria (ou como tique comprido cortado), nao como "riscado".
    for linha in range(2):
        yy = y0 + linha * vao
        traco(d, x0 - comprimento * 0.04, yy + altura_tique + h * 0.010,
              x0 + comprimento * 1.04, yy - h * 0.010,
              vermelho, 4, acaso, tremor=1.6)

    if args.giro:
        camada = camada.rotate(args.giro, resample=Image.BICUBIC,
                               center=(w / 2, h / 2))

    camada = camada.filter(ImageFilter.GaussianBlur(0.55))
    queimar(base, camada, args.semente).save(args.out)
    print(f"ok {args.out} linhas em ({x0:.0f},{y0:.0f}) comprimento={comprimento:.0f}")


if __name__ == "__main__":
    main()
