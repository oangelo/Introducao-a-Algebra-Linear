#!/usr/bin/env python3
"""Rasga a cena ao meio e poe um relogio no rasgo: "mesmo personagem, dois tempos".

Por que por codigo: o que precisa ser legivel e a RELACAO (mesma pessoa, tempos diferentes),
e isso e estrutura, nao pintura. Um raio desenhado por difusao sai torto e nao alinha as duas
metades. Aqui as metades sao deslocadas de verdade e a junta e uma polilinha fixa (seed travada),
entao o corte e reproduzivel.

Uso:
  uv run --with pillow python img-gen/corte-tempo.py --img in.png --out out.png
"""
import argparse
import random

from PIL import Image, ImageDraw, ImageFilter

ap = argparse.ArgumentParser()
ap.add_argument("--img", required=True)
ap.add_argument("--out", required=True)
ap.add_argument("--raio", type=int, default=52, help="raio do relogio em px")
ap.add_argument("--desloca", type=int, default=9, help="quanto as metades se afastam")
ap.add_argument("--girar", type=float, default=0.0, help="graus de inclinacao de cada metade")
ap.add_argument("--seed", type=int, default=7)
ap.add_argument("--sem-relogio", action="store_true")
a = ap.parse_args()

base = Image.open(a.img).convert("RGBA")
RESAMPLE = getattr(getattr(Image, "Resampling", Image), "BICUBIC")
W, H = base.size

# ---- junta: caminho serrilhado do topo ao fundo ----
random.seed(a.seed)
passo = 46
junta = [(W // 2, 0)]
y = 0
lado = 1
while y < H:
    y = min(H, y + passo)
    desvio = random.randint(4, 17) * lado
    lado = -lado
    x = max(40, min(W - 40, junta[-1][0] + desvio))
    junta.append((x, y))

# ---- mascaras das duas metades ----
# ordem importa: junta (topo->fundo) + canto inferior direito + canto superior direito.
# invertido, o poligono se auto-intersecta e o PIL fatia uma cunha na diagonal.
mascara_d = Image.new("L", (W, H), 0)
ImageDraw.Draw(mascara_d).polygon(junta + [(W, H), (W, 0)], fill=255)
mascara_e = mascara_d.point(lambda v: 255 - v)

d = a.desloca
giro = (W // 2, H // 2)
fonte_e = base.rotate(-a.girar, center=giro, resample=RESAMPLE) if a.girar else base
fonte_d = base.rotate(a.girar, center=giro, resample=RESAMPLE) if a.girar else base
metade_e = Image.new("RGBA", (W, H), (0, 0, 0, 0))
metade_e.paste(fonte_e, (-d // 2, -d // 3))
metade_d = Image.new("RGBA", (W, H), (0, 0, 0, 0))
metade_d.paste(fonte_d, (d - d // 2, d - d // 3))

# fundo do vao: quase preto azulado, para o rasgo nao ficar transparente
fundo = Image.new("RGBA", (W, H), (11, 12, 20, 255))
fundo.paste(metade_e, (0, 0), mascara_e)
fundo.paste(metade_d, (0, 0), mascara_d)

# ---- o raio na junta: contorno preto grosso + nucleo claro ----
raio = Image.new("RGBA", (W, H), (0, 0, 0, 0))
dr = ImageDraw.Draw(raio)
dr.line(junta, fill=(8, 8, 12, 255), width=13, joint="curve")
dr.line(junta, fill=(246, 243, 232, 255), width=6, joint="curve")
brilho = raio.filter(ImageFilter.GaussianBlur(9))
halo = Image.new("RGBA", (W, H), (0, 0, 0, 0))
halo.paste(Image.new("RGBA", (W, H), (255, 236, 200)), (0, 0), brilho)
fundo = Image.alpha_composite(fundo, halo)
fundo = Image.alpha_composite(fundo, raio)

# ---- relogio no rasgo ----
if not a.sem_relogio:
    cx, cy = W // 2, int(H * 0.46)
    r = a.raio
    rel = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    dl = ImageDraw.Draw(rel)
    sombra = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sombra).ellipse([cx - r - 6, cy - r + 4, cx + r + 6, cy + r + 16],
                                   fill=(0, 0, 0, 140))
    rel = Image.alpha_composite(rel, sombra.filter(ImageFilter.GaussianBlur(7)))
    dl = ImageDraw.Draw(rel)
    dl.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(245, 240, 228, 255),
               outline=(8, 8, 12, 255), width=6)
    dl.ellipse([cx - r + 12, cy - r + 12, cx + r - 12, cy + r - 12],
               outline=(120, 112, 104, 255), width=2)
    # 12 marcas, sem numeral: relogio analógico, nenhuma letra inventada
    import math
    for k in range(12):
        ang = math.radians(k * 30)
        r1 = r - 14
        r2 = r - (22 if k % 3 == 0 else 18)
        dl.line([cx + r1 * math.sin(ang), cy - r1 * math.cos(ang),
                 cx + r2 * math.sin(ang), cy - r2 * math.cos(ang)],
                fill=(8, 8, 12, 255), width=4 if k % 3 == 0 else 2)
    # ponteiros: horas e minutos em posicoes distintas, sem numeros
    for ang_graus, comp, larg in ((0, 0.55, 7), (72, 0.80, 4)):
        ang = math.radians(ang_graus)
        dl.line([cx, cy, cx + comp * r * math.sin(ang), cy - comp * r * math.cos(ang)],
                fill=(8, 8, 12, 255), width=larg + 3)
        dl.line([cx, cy, cx + comp * r * math.sin(ang), cy - comp * r * math.cos(ang)],
                fill=(214, 62, 48, 255) if larg < 6 else (30, 30, 36, 255), width=larg)
    dl.ellipse([cx - 7, cy - 7, cx + 7, cy + 7], fill=(214, 62, 48, 255),
               outline=(8, 8, 12, 255), width=3)
    fundo = Image.alpha_composite(fundo, rel)

fundo.convert("RGB").save(a.out, quality=95)
print("ok %s  junta=%d pontos  desloca=%d" % (a.out, len(junta), a.desloca))
