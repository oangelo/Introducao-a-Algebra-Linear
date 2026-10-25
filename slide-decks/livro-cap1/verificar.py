#!/usr/bin/env python3
"""Confere livro-cap1.html montado contra o CONTRATO.md.

Sai com código 1 se qualquer checagem falhar. Cada checagem existe por um erro real de
texto montado por fragmentos — ver PLANO.md §4.

Uso: python3 verificar.py [arquivo]
"""

import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
ALVO = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
    AQUI,
    json.load(open(os.path.join(AQUI, "capitulo.json"), encoding="utf-8"))["saida"],
)

PROIBIDAS = ["portão", "portoes", "portões", "chave", "chaves", "quest",
             "chefe", "jogador", "hud", "gabinete", "fliperama", "missão", "missao", "pódio",
             "podio"]

erros = []
avisos = []


def erro(msg):
    erros.append(msg)


def aviso(msg):
    avisos.append(msg)


def main():
    if not os.path.exists(ALVO):
        sys.exit("nao achei %s — rode build.py" % ALVO)
    html = open(ALVO, encoding="utf-8").read()
    texto = re.sub(r"<script.*?</script>", " ", html, flags=re.S)
    texto = re.sub(r"<[^>]+>", " ", texto)

    # 1. referências cruzadas resolvem
    ids = re.findall(r'id="([^"]+)"', html)
    for href in set(re.findall(r'href="#([^"]+)"', html)):
        if href not in ids:
            erro("referencia quebrada: #%s" % href)

    # 2. ids únicos
    vistos = set()
    for i in ids:
        if i in vistos:
            erro("id repetido: %s" % i)
        vistos.add(i)

    # 3. sem CSS inline nem <style>
    if re.search(r"<style", html, re.I):
        erro("tem <style> — proibido")
    for m in re.finditer(r'style="([^"]*)"', html):
        erro('style inline: "%s"' % m.group(1)[:40])

    # 4. barra dupla quebra MathJax
    for padrao in (r"\\\\\(", r"\\\\\[", r"\\\\frac"):
        if re.search(padrao, html):
            erro("barra dupla em LaTeX: %s ocorrencias" % len(re.findall(padrao, html)))

    # 5. delimitadores de math balanceados, por fragmento
    partes = os.path.join(AQUI, "partes")
    if os.path.isdir(partes):
        for nome in sorted(os.listdir(partes)):
            if not nome.endswith(".html") or nome.startswith("_"):
                continue
            txt = open(os.path.join(partes, nome), encoding="utf-8").read()
            for abre, fecha in ((r"\(", r"\)"), (r"\[", r"\]")):
                a, f = txt.count(abre), txt.count(fecha)
                if a != f:
                    erro("%s: %s abre %d e fecha %d" % (nome, abre, a, f))

    # 6. seções numeradas em ordem crescente
    # float("1.10") == 1.1 e quebraria a ordem: comparar como par de inteiros
    numeros = [(int(a), int(b)) for a, b in re.findall(
        r'<h2[^>]*>\s*<span class="num">(\d+)\.(\d+)</span>', html)]

    for antes, depois in zip(numeros, numeros[1:]):
        if depois <= antes:
            erro("numeracao fora de ordem: %d.%d antes de %d.%d" % (antes[0], antes[1], depois[0], depois[1]))

    # 7. vocabulário da ficção
    baixo = texto.lower()
    for p in PROIBIDAS:
        if re.search(r"\b%s\b" % re.escape(p), baixo):
            erro("vocabulario proibido no livro: '%s'" % p)

    # 8. bloco \[ sem \] correspondente (fora do item 5, que é por arquivo)
    if html.count(r"\[") != html.count(r"\]"):
        erro("blocos \\[ ... \\] desbalanceados no arquivo montado")

    # 9. configuração do MathJax: NUNCA redeclarar delimitadores.
    # Uma barra dentro de string JS ('\(') vira '(' e o MathJax passa a tratar todo
    # parêntese do texto como fórmula — a página inteira sai com erro de renderização.
    if "inlineMath" in html or "displayMath" in html:
        erro("o arquivo reconfigura delimitadores do MathJax: use os padrões "
             "\\( \\) e \\[ \\], sem declarar inlineMath/displayMath")
    if re.search(r"inlineMath\s*:\s*\[\s*\[\s*'[^'\\\\]", html):
        erro("delimitador sem barra escapada na configuracao do MathJax")

    # avisos (não reprovam)
    for nome in sorted(os.listdir(partes)) if os.path.isdir(partes) else []:
        if nome.endswith(".html") and not nome.startswith("_"):
            txt = open(os.path.join(partes, nome), encoding="utf-8").read()
            if "fonte:" not in txt[:200]:
                aviso("%s sem comentario de fonte na primeira linha" % nome)

    if numeros and numeros[0] != (1, 1):
        aviso("a primeira secao numerada e %d.%d, nao 1.1" % numeros[0])

    print("arquivo: %s (%d KB)" % (os.path.basename(ALVO), len(html) // 1024))
    print("secoes numeradas: %d" % len(numeros))
    print("ids: %d · links internos: %d" % (len(ids), len(re.findall(r'href="#', html))))
    for a in avisos:
        print("  aviso: %s" % a)
    if erros:
        print("\n%d ERRO(S):" % len(erros))
        for e in erros:
            print("  - %s" % e)
        sys.exit(1)
    print("\ncontrato OK")


if __name__ == "__main__":
    main()
