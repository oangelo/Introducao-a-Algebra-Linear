#!/usr/bin/env python3
"""Monta o capítulo de leitura a partir de capitulo.json.

O manifesto é a única fonte da ordem: ele diz quais seções e quais cenas entram, e em que
ordem. O próximo capítulo é um manifesto novo — não um build novo.

Uso: python3 build.py [capitulo.json]
"""

import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
MANIFESTO = sys.argv[1] if len(sys.argv) > 1 else os.path.join(AQUI, "capitulo.json")
BS = chr(92)          # barra invertida, dos delimitadores de math

MODELO = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo} · capítulo 1</title>
<meta name="description" content="{descricao}">
<link rel="stylesheet" href="tema.css">
</head>
<body class="leitura">

<header class="capa">
  <img src="{capa_img}" alt="{capa_alt}">
  <div class="texto">
    <p class="kicker">{kicker}</p>
    <h1>{titulo}</h1>
    <p class="sub">{subtitulo}</p>
    <p class="autor">{autor}</p>
  </div>
</header>

<main class="coluna">

{corpo}

</main>

<script>
window.MathJax = {{
  tex: {{ inlineMath: [['{bs}(', '{bs})']], displayMath: [['{bs}[', '{bs}]']] }},
  options: {{ skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'] }}
}};
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" defer></script>
</body>
</html>
"""


def figura(cena, base):
    return """<figure class="cena">
  <img src="{src}" alt="{alt}" loading="lazy" decoding="async">
  <figcaption>{frase}</figcaption>
</figure>""".format(src=base + cena["img"], alt=cena["alt"], frase=cena["frase"])


def main():
    with open(MANIFESTO, encoding="utf-8") as fh:
        cfg = json.load(fh)

    base = cfg.get("img_base", "../img/")
    partes = []

    for bloco in cfg["blocos"]:
        if "cena" in bloco:
            partes.append(figura(bloco["cena"], base))
        elif "parte" in bloco:
            caminho = os.path.join(AQUI, bloco["parte"])
            if not os.path.exists(caminho):
                sys.exit("falta o fragmento " + bloco["parte"])
            with open(caminho, encoding="utf-8") as fh:
                partes.append(fh.read().strip())
        else:
            sys.exit("bloco sem 'cena' nem 'parte': %r" % bloco)

    corpo = "\n\n".join(partes)

    # imagem quebrada é erro silencioso: confere cada src contra o disco
    faltando = [src for src in re.findall(r'<img src="([^"]+)"', corpo)
                if not os.path.exists(os.path.normpath(os.path.join(AQUI, src)))]
    if faltando:
        sys.exit("imagens que nao existem: " + ", ".join(sorted(set(faltando))))

    n_cenas = len(re.findall(r'class="cena"', corpo))
    n_sec = len(re.findall(r'<section class="sec"', corpo))

    html = MODELO.format(
        titulo=cfg["titulo"],
        descricao=cfg.get("subtitulo", "").replace('"', "'"),
        kicker=cfg["kicker"],
        subtitulo=cfg["subtitulo"],
        autor=cfg["autor"],
        capa_img=base + cfg["capa"]["img"],
        capa_alt=cfg["capa"]["alt"],
        corpo=corpo,
        bs=BS,
    )

    saida = os.path.join(AQUI, cfg["saida"])
    with open(saida, "w", encoding="utf-8") as fh:
        fh.write(html)

    print("ok %s" % cfg["saida"])
    print("  blocos: %d · secoes: %d · cenas: %d" % (len(cfg["blocos"]), n_sec, n_cenas))
    print("  tamanho: %d KB" % (len(html) // 1024))


if __name__ == "__main__":
    main()
