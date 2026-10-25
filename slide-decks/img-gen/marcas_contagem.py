#!/usr/bin/env python3
"""Desenha marcas de contagem (tallies) numa pagina de caderno gerada vazia.

Por que isto existe: o gerador de imagem nao conta. Pedir "dois blocos QUASE
iguais, com a diferenca pequena circulada" produz marcas aleatorias e um circulo
vermelho em lugar nenhum. Entao a cena (caderno vazio, luz de luminaria) vem do
gerador e as marcas vem de codigo -- assim a diferenca e exatamente a que a
cartela precisa mostrar.

Uso:
  python marcas-contagem.py --img base.png --out saida.png [--esq 40] [--extras 2]
"""
import argparse
import math
import random

from PIL import Image, ImageDraw, ImageFilter


def pagina(img):
    """Retangulo da pagina: faixa clara e pouco saturada no miolo da imagem."""
    import numpy as np

    a = np.asarray(img.convert("HSV"))
    h, w = a.shape[:2]
    claro = (a[:, :, 2] > 120) & (a[:, :, 1] < 110)
    claro[: int(h * 0.04)] = False
    claro[int(h * 0.96):] = False
    claro[:, : int(w * 0.04)] = False
    claro[:, int(w * 0.96):] = False
    linhas = np.where(claro.sum(axis=1) > w * 0.25)[0]
    colunas = np.where(claro.sum(axis=0) > h * 0.25)[0]
    if len(linhas) < 10 or len(colunas) < 10:
        return int(w * 0.12), int(h * 0.12), int(w * 0.88), int(h * 0.88)
    return int(colunas[0]), int(linhas[0]), int(colunas[-1]), int(linhas[-1])


def traco(d, x0, y0, x1, y1, cor, largura, acaso, tremor=1.6):
    """Linha levemente torta, como lapis."""
    passos = max(2, int(math.dist((x0, y0), (x1, y1)) / 9))
    pontos = []
    for i in range(passos + 1):
        t = i / passos
        pontos.append((x0 + (x1 - x0) * t + acaso.uniform(-tremor, tremor),
                       y0 + (y1 - y0) * t + acaso.uniform(-tremor, tremor)))
    d.line(pontos, fill=cor, width=largura, joint="curve")


class Grade:
    """Posicao de cada marca: linhas de grupos de cinco, quebrando no fim da coluna."""

    def __init__(self, x, y, largura, altura, passo_linha):
        self.x, self.y = x, y
        self.altura = altura
        self.passo = altura * 0.20
        self.grupo = self.passo * 4 + self.passo * 0.9
        self.por_linha = max(1, int(largura // self.grupo))
        self.passo_linha = passo_linha

    def pos(self, i):
        n = self.por_linha * 5
        linha, col = divmod(i, n)
        grupo, dentro = divmod(col, 5)
        return (self.x + grupo * self.grupo + dentro * self.passo,
                self.y + linha * (self.altura + self.passo_linha),
                dentro)


def desenhar(d, grade, quantos, cor, acaso):
    """Marca por marca; a quinta de cada grupo fecha com a diagonal."""
    for i in range(quantos):
        x, y, dentro = grade.pos(i)
        if dentro == 4:
            traco(d, x - grade.passo * 4.45, y + grade.altura * 0.94,
                  x + grade.passo * 0.45, y + grade.altura * 0.16,
                  cor, 4, acaso, tremor=2.2)
        inclina = acaso.uniform(-1.8, 1.8)
        dx = acaso.uniform(-1.2, 1.2)
        traco(d, x + dx, y + abs(inclina),
              x + dx + inclina, y + grade.altura - abs(inclina),
              cor, 3, acaso)


def circulo(d, cx, cy, rx, ry, cor, acaso, largura=4):
    """Elipse a mao livre: o raio varia ao longo da volta."""
    pontos = []
    voltas = 96
    for i in range(voltas + 1):
        a = 2 * math.pi * i / voltas
        r = 1 + acaso.uniform(-0.035, 0.035)
        pontos.append((cx + math.cos(a) * rx * r, cy + math.sin(a) * ry * r))
    d.line(pontos, fill=cor, width=largura, joint="curve")


def queimar(base, camada, semente=7):
    """Compoe a camada por MULTIPLICACAO, com grao de papel.

    Grafite nao cobre o papel: escurece, e falha onde o dente do papel nao pega.
    Com alfa o traco vira adesivo por cima da imagem gerada e denuncia o codigo;
    multiplicando e quebrando a opacidade com um grao, o risco acompanha a
    sombra e a textura do papel, como lapis de verdade.
    """
    import numpy as np

    b = np.asarray(base.convert("RGB"), dtype=np.float32) / 255.0
    c = np.asarray(camada, dtype=np.float32) / 255.0
    alfa = c[:, :, 3:4]

    rng = np.random.default_rng(semente)
    h, w = alfa.shape[:2]
    # dois graos: um fino (dente do papel) e um grosso (pressao da mao)
    fino = rng.normal(1.0, 0.18, (h, w)).clip(0.35, 1.25)[:, :, None]
    grosso = Image.fromarray((rng.normal(1.0, 0.10, (h // 8, w // 8)).clip(0.6, 1.3)
                              * 128).astype("uint8")).resize((w, h), Image.BICUBIC)
    grosso = (np.asarray(grosso, dtype=np.float32) / 128.0)[:, :, None]

    alfa = (alfa * fino * grosso).clip(0.0, 1.0)
    pintado = b * c[:, :, :3]
    saida = b * (1.0 - alfa) + pintado * alfa
    return Image.fromarray((saida * 255.0).clip(0, 255).astype("uint8"))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--img", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--esq", type=int, default=40)
    p.add_argument("--extras", type=int, default=2)
    p.add_argument("--semente", type=int, default=7)
    p.add_argument("--espaco-extra", type=float, default=1.9)
    p.add_argument("--giro", type=float, default=0.0,
                   help="graus: gira as marcas junto com a pagina fotografada")
    args = p.parse_args()

    acaso = random.Random(args.semente)
    base = Image.open(args.img).convert("RGB")
    x0, y0, x1, y1 = pagina(base)
    largura, altura_pag = x1 - x0, y1 - y0

    camada = Image.new("RGBA", base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(camada)
    grafite = (96, 92, 86, 200)
    vermelho = (168, 46, 38, 210)

    altura_marca = altura_pag * 0.075
    topo = y0 + altura_pag * 0.17
    passo_linha = altura_marca * 0.85
    coluna_larg = largura * 0.36
    esq_x = x0 + largura * 0.06
    dir_x = x0 + largura * 0.55

    # uma regua de lapis separando as duas colunas (nada nas bordas: linha de
    # margem nas duas pontas le como caderno pautado, e o papel aqui e liso)
    bx = x0 + largura * 0.53
    traco(d, bx, topo - altura_marca, bx, y1 - altura_pag * 0.10,
          (118, 112, 104, 130), 2, acaso, tremor=1.0)

    ge = Grade(esq_x, topo, coluna_larg, altura_marca, passo_linha)
    gd = Grade(dir_x, topo, coluna_larg, altura_marca, passo_linha)

    desenhar(d, ge, args.esq, grafite, acaso)
    desenhar(d, gd, args.esq, grafite, acaso)

    # as marcas extras ficam mais ESPACADAS que o normal: com o passo do grupo
    # (10 px) as duas colam e o circulo le como um risco so.
    esq_extra = gd.passo * args.espaco_extra
    x0x, y0x, _ = gd.pos(args.esq)
    xs, ys = [], []
    for i in range(args.extras):
        x = x0x + i * esq_extra
        inclina = acaso.uniform(-1.8, 1.8)
        dx = acaso.uniform(-1.2, 1.2)
        traco(d, x + dx, y0x + abs(inclina),
              x + dx + inclina, y0x + altura_marca - abs(inclina),
              grafite, 3, acaso)
        xs += [x, x + esq_extra]
        ys += [y0x, y0x + altura_marca]
    xs = xs[:-1]  # a ultima posicao ja e o fim da ultima marca

    # circulo vermelho apenas em volta das marcas extras
    cx, cy = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2
    circulo(d, cx, cy, (max(xs) - min(xs)) / 2 + gd.passo * 0.9,
            (max(ys) - min(ys)) / 2 + altura_marca * 0.32, vermelho, acaso)

    if args.giro:
        centro = ((x0 + x1) / 2, (y0 + y1) / 2)
        camada = camada.rotate(args.giro, resample=Image.BICUBIC, center=centro)

    camada = camada.filter(ImageFilter.GaussianBlur(0.55))
    saida = queimar(base, camada, args.semente)
    saida.save(args.out)
    print(f"ok {args.out} pagina=({x0},{y0},{x1},{y1}) esq={args.esq} "
          f"dir={args.esq + args.extras} por_linha={ge.por_linha}")


if __name__ == "__main__":
    main()
