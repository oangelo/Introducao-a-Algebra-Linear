#!/usr/bin/env python3
"""Compõe a cartela Q10 alternativa: três cenas nos degraus, o troféu no alto.

Por que compor e não gerar: pedir "pódio com três cenas e um troféu" numa geração
só devolve uma papa — o modelo não mantém três cenas distintas dentro de um
enquadramento. Aqui as quatro peças vêm do FLUX (mesmo personagem, mesma paleta)
e o arranjo é geometria de montagem, que é trabalho de código.

Layout, em frações de 1152x864:
  - painel grande (pódio) no alto, centrado;
  - três painéis pequenos embaixo, o do meio mais alto: degraus.
"""
import argparse

from PIL import Image, ImageDraw, ImageFilter

FUNDO = (18, 16, 14)
MOLDURA = (12, 11, 10)
LINHA = (232, 226, 214)


def painel(base, cam, caminho, caixa, borda, sombra):
    im = Image.open(caminho).convert("RGB")
    larg, alt = caixa[2] - caixa[0], caixa[3] - caixa[1]
    # preenche a caixa cortando o excesso (center crop): esticar deformaria
    r = max(larg / im.width, alt / im.height)
    im = im.resize((int(im.width * r + 0.5), int(im.height * r + 0.5)), Image.LANCZOS)
    x0 = (im.width - larg) // 2
    y0 = (im.height - alt) // 2
    im = im.crop((x0, y0, x0 + larg, y0 + alt))

    if sombra:
        s = Image.new("RGBA", cam.size, (0, 0, 0, 0))
        ImageDraw.Draw(s).rectangle((caixa[0] + 6, caixa[1] + 8, caixa[2] + 6, caixa[3] + 8),
                                    fill=(0, 0, 0, 150))
        s = s.filter(ImageFilter.GaussianBlur(10))
        cam.alpha_composite(s)

    cam.paste(im, (caixa[0], caixa[1]))
    d = ImageDraw.Draw(cam)
    d.rectangle(caixa, outline=MOLDURA, width=borda)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--dir", default="img")
    p.add_argument("--modo", choices=["degraus", "tira"], default="tira",
                   help="degraus: o do meio mais alto (le como ranking). "
                        "tira: os tres com o mesmo peso, encostados (le como um bloco so)")
    p.add_argument("--out", required=True)
    a = p.parse_args()
    W, H = 1152, 864

    base = Image.new("RGB", (W, H), FUNDO)
    # vinheta: cantos escuros, centro claro — o olho vai para o troféu
    vin = Image.new("L", (W, H), 0)
    vd = ImageDraw.Draw(vin)
    vd.ellipse((-W * 0.15, -H * 0.25, W * 1.15, H * 1.15), fill=90)
    vin = vin.filter(ImageFilter.GaussianBlur(160))
    base = Image.composite(Image.new("RGB", (W, H), (34, 30, 26)), base, vin)

    cam = base.convert("RGBA")

    # painel grande: o pódio, no alto e centrado
    painel(cam, cam, f"{a.dir}/c10p-podio.png", (256, 36, 896, 516), 8, True)

    if a.modo == "degraus":
        # o do meio mais alto: le como ranking, e ranking aqui e atribuicao falsa
        painel(cam, cam, f"{a.dir}/c10p-dormindo2.png", (60, 600, 360, 825), 6, True)
        painel(cam, cam, f"{a.dir}/c10p-estudando.png", (426, 560, 726, 785), 6, True)
        painel(cam, cam, f"{a.dir}/c10p-correndo2.png", (792, 600, 1092, 825), 6, True)
        d = ImageDraw.Draw(cam)
        d.line([(48, 832), (1104, 832)], fill=LINHA, width=3)
    else:
        # tira: tres paineis do mesmo tamanho, encostados — um bloco so, sem hierarquia
        y0, y1 = 588, 816
        for x0, nome in ((132, "dormindo2"), (426, "estudando"), (720, "correndo2")):
            painel(cam, cam, f"{a.dir}/c10p-{nome}.png", (x0, y0, x0 + 296, y1), 5, True)
        d = ImageDraw.Draw(cam)
        # colchete: os tres estao amarrados, nao enfileirados
        d.line([(132, 838), (1016, 838)], fill=LINHA, width=3)
        d.line([(132, 830), (132, 846)], fill=LINHA, width=3)
        d.line([(1016, 830), (1016, 846)], fill=LINHA, width=3)

    cam.convert("RGB").save(a.out)
    print(f"ok {a.out}")


if __name__ == "__main__":
    main()
