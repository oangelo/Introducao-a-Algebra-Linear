#!/usr/bin/env python3
"""Monta livro-cap1.html a partir dos fragmentos em partes/.

- Nenhum fragmento é editado aqui: só concatenado, na ordem do nome do arquivo.
- O sumário é gerado dos <h2> — não existe sumário escrito à mão.
- Arquivos que começam com "_" são ignorados (modelos, rascunhos).

Uso: python3 build.py
"""

import glob
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
PARTES = os.path.join(AQUI, "partes")
SAIDA = os.path.join(AQUI, "livro-cap1.html")

TITULO = "Capítulo 1 · Sistemas e matrizes"
SUBTITULO = ("Do que é uma solução até o que a forma da matriz já diz, sem desenhar reta.")
AUTOR = "Prof. Angelo Mondaini Calvão · IPRJ/UERJ"


def ler_partes():
    arquivos = sorted(
        a for a in glob.glob(os.path.join(PARTES, "*.html"))
        if not os.path.basename(a).startswith("_")
    )
    if not arquivos:
        sys.exit("nenhum fragmento em %s" % PARTES)
    return arquivos, [(os.path.basename(a), open(a, encoding="utf-8").read()) for a in arquivos]


def limpar(s):
    s = re.sub(r"<[^>]+>", "", s)
    s = s.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    return re.sub(r"\s+", " ", s).strip()


def sumario(corpo):
    itens = []
    for m in re.finditer(r'<h2[^>]*>(.*?)</h2>', corpo, re.S):
        dentro = m.group(1)
        mn = re.search(r'<span class="num">([^<]+)</span>', dentro)
        num = mn.group(1).strip() if mn else ""
        titulo = limpar(dentro)
        if num:
            titulo = re.sub(r"^" + re.escape(num) + r"\s*", "", titulo)
        itens.append((num, titulo))

    # ainda não existem âncoras: casa cada h2 com o id da section que o contém
    alvos = []
    for m in re.finditer(r'<section[^>]*id="([^"]+)"[^>]*>(.*?)</section>', corpo, re.S):
        sid, bloco = m.group(1), m.group(2)
        if re.search(r"<h2[^>]*>", bloco):
            alvos.append(sid)

    linhas = []
    for i, (num, titulo) in enumerate(itens):
        href = alvos[i] if i < len(alvos) else ""
        rotulo = '<span class="num">%s</span>' % num if num else '<span class="num">·</span>'
        linhas.append('      <li><a href="#%s">%s%s</a></li>' % (href, rotulo, titulo))
    return "\n".join(linhas), len(itens)


def main():
    arquivos, pares = ler_partes()
    corpo = "\n\n".join(txt.strip() for _, txt in pares)
    toc, n = sumario(corpo)

    html = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo}</title>
<link rel="stylesheet" href="livro-cap1.css">
</head>
<body>

<div class="pagina">

<header class="capa">
  <p class="selo">Álgebra Linear · capítulo 1</p>
  <h1>{titulo}</h1>
  <p class="sub">{sub}</p>
  <p class="autor">{autor}</p>
</header>

<nav id="sumario">
  <h2>Sumário</h2>
  <ol>
{toc}
  </ol>
</nav>

<main>
{corpo}
</main>

</div>

<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" defer></script>
</body>
</html>
""".format(titulo=TITULO, sub=SUBTITULO, autor=AUTOR, toc=toc, corpo=corpo)

    with open(SAIDA, "w", encoding="utf-8") as fh:
        fh.write(html)

    print("ok %s" % os.path.basename(SAIDA))
    print("  fragmentos: %d" % len(arquivos))
    print("  secoes no sumario: %d" % n)
    print("  linhas: %d" % html.count("\n"))
    for nome, txt in pares:
        print("    %-22s %4d linhas" % (nome, txt.count("\n") + 1))


if __name__ == "__main__":
    main()
