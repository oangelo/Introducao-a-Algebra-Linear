#!/usr/bin/env python3
"""Gera o PDF de revisao do capitulo 1 a partir de cap1-telas.html.

Fonte unica: o HTML. Se o texto mudar la, o PDF muda aqui — nao existe copia.
Uso: uv run --with reportlab python cap1-telas-pdf.py
"""
import os
import re
import sys
import html
from html.parser import HTMLParser

from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import stringWidth

AQUI = os.path.dirname(os.path.abspath(__file__))
ENTRADA = os.path.join(AQUI, "cap1-telas.html")
SAIDA = os.path.join(AQUI, "cap1-telas.pdf")

TINTA = HexColor("#111318")
FRACO = HexColor("#5a6172")
AZUL = HexColor("#2b5f8a")
AMBAR = HexColor("#8a5a12")
LINHA = HexColor("#c9ccd4")


class Fichas(HTMLParser):
    """Extrai, de cada <section class='ficha'>, imagem, frase e os dd rotulados."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.em_h3 = False
        self.fichas = []
        self.atual = None
        self.campo = None
        self.label = None
        self.stack = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = a.get("class", "")
        self.stack.append((tag, cls))
        if tag == "section" and "ficha" in cls:
            self.atual = {"img": "", "frase": "", "menor": "", "fonte": "", "dd": [], "h3": ""}
        if self.atual is None:
            return
        if tag == "img" and not self.atual["img"]:
            self.atual["img"] = a.get("src", "")
        elif tag == "p" and "frase" in cls:
            self.campo = "frase"
        elif tag == "span" and "menor" in cls:
            self.campo = "menor"
        elif tag == "p" and "fonte" in cls:
            self.campo = "fonte"
        elif tag == "dt":
            self.label = ""
            self.campo = "label"
        elif tag == "dd":
            self.campo = "dd"
            self.atual["dd"].append([self.label or "", "", "citacao" in cls])
        elif tag == "h3" and not self.atual["h3"]:
            self.campo = "h3"
            self.em_h3 = True

    def handle_endtag(self, tag):
        while self.stack:
            t, _ = self.stack.pop()
            if t == tag:
                break
        if tag in ("p", "span", "dt", "dd", "h3"):
            self.campo = None
        # o <h3> tem <span class="num">Q04</span> dentro: fechar o span nao pode
        # encerrar o titulo, senao a ficha sai com "Q04 ·" e nada depois
        if tag == "span" and getattr(self, "em_h3", False):
            self.campo = "h3"
        if tag == "h3":
            self.em_h3 = False
        if tag == "section" and self.atual is not None:
            self.fichas.append(self.atual)
            self.atual = None

    def handle_data(self, data):
        if self.atual is None or self.campo is None:
            return
        txt = data.replace("\u00a0", " ").replace("\n", " ").strip()
        if not txt:
            return
        if self.campo == "label":
            self.label = (self.label + " " + txt).strip()
        elif self.campo == "dd":
            if self.atual["dd"]:
                self.atual["dd"][-1][1] = (self.atual["dd"][-1][1] + " " + txt).strip()
        elif self.campo in ("frase", "menor", "fonte", "h3"):
            self.atual[self.campo] = (self.atual[self.campo] + " " + txt).strip()


def wrap(texto, fonte, tam, largura):
    palavras, linhas, atual = texto.split(), [], ""
    for p in palavras:
        teste = (atual + " " + p).strip()
        if stringWidth(teste, fonte, tam) <= largura or not atual:
            atual = teste
        else:
            linhas.append(atual)
            atual = p
    if atual:
        linhas.append(atual)
    return linhas


def desenhar_ficha(c, f, idx):
    larg, alt = landscape(A4)

    c.setFillColor(FRACO)
    c.setFont("Helvetica", 6.5)
    c.drawString(12 * mm, alt - 11 * mm, "CAPITULO 1 · AS DEZ TELAS")
    c.drawRightString(larg - 12 * mm, alt - 11 * mm, "%02d / 10" % idx)

    titulo = re.sub(r"^Q\d+\s*", "", f["h3"]).strip()
    c.setFillColor(AMBAR)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(12 * mm, alt - 19 * mm, "Q%02d · %s" % (idx, titulo))
    c.setStrokeColor(LINHA)
    c.setLineWidth(0.4)
    c.line(12 * mm, alt - 22 * mm, larg - 12 * mm, alt - 22 * mm)

    # --- coluna esquerda: o slide ---
    x, y_topo = 12 * mm, alt - 26 * mm
    w_img = 140 * mm
    h_img = w_img * 0.75
    y_img = y_topo - h_img
    caminho = os.path.join(AQUI, f["img"])
    if os.path.exists(caminho):
        c.drawImage(caminho, x, y_img, width=w_img, height=h_img,
                    preserveAspectRatio=True, anchor="c", mask=None)
    else:
        c.setFillColor(LINHA)
        c.rect(x, y_img, w_img, h_img, fill=1, stroke=0)
        c.setFillColor(FRACO)
        c.drawString(x + 4 * mm, y_img + h_img / 2, "imagem ausente: " + f["img"])

    # faixa de HUD
    c.setFillColorRGB(0, 0, 0, alpha=0.55)
    c.rect(x, y_topo - 7 * mm, w_img, 7 * mm, fill=1, stroke=0)
    c.setFillColor(HexColor("#d8dbe2"))
    c.setFont("Courier-Bold", 6.5)
    c.drawString(x + 2.5 * mm, y_topo - 4.6 * mm, "CAPITULO 1 · O INSTRUMENTO")
    c.drawRightString(x + w_img - 2.5 * mm, y_topo - 4.6 * mm, "0 / 6 CHAVES")

    # frase sobre a base escura da imagem
    linhas = wrap(f["frase"], "Courier-Bold", 12, w_img - 12 * mm)
    altura_faixa = 4 * mm + len(linhas) * 5.2 * mm + (5 * mm if f["menor"] else 0)
    c.setFillColorRGB(0, 0, 0, alpha=0.72)
    c.rect(x, y_img, w_img, altura_faixa, fill=1, stroke=0)
    c.setFillColor(HexColor("#ffffff"))
    c.setFont("Courier-Bold", 12)
    yy = y_img + altura_faixa - 4.6 * mm
    for ln in linhas:
        c.drawString(x + 3 * mm, yy, ln)
        yy -= 5.2 * mm
    if f["menor"]:
        c.setFillColor(HexColor("#c9ced9"))
        c.setFont("Courier", 8)
        for ln in wrap(f["menor"], "Courier", 8, w_img - 12 * mm)[:2]:
            c.drawString(x + 3 * mm, yy, ln)
            yy -= 4.2 * mm

    if f["fonte"]:
        c.setFillColor(HexColor("#e8eaf0"))
        c.setFont("Courier", 6.2)
        c.drawRightString(x + w_img - 2.5 * mm, y_topo - 5 * mm + 4.4 * mm, "")

    # --- coluna direita: a ficha ---
    cx = 158 * mm
    cw = larg - cx - 12 * mm
    cy = alt - 26 * mm
    for label, corpo, eh_citacao in f["dd"]:
        if not corpo:
            continue
        c.setFillColor(AZUL)
        c.setFont("Helvetica-Bold", 6.2)
        c.drawString(cx, cy, label.upper())
        cy -= 3.6 * mm
        tam, entrelinha = (7.6, 9.4) if eh_citacao else (8.3, 10.4)
        c.setFillColor(FRACO if eh_citacao else TINTA)
        c.setFont("Helvetica-Oblique" if eh_citacao else "Helvetica", tam)
        for ln in wrap(corpo, "Helvetica", tam, cw - (3 * mm if eh_citacao else 0)):
            if cy < 14 * mm:
                c.showPage()
                return
            c.drawString(cx + (3 * mm if eh_citacao else 0), cy, ln)
            cy -= entrelinha
        cy -= 3.4 * mm

    # linha-fonte do slide, canto inferior do mock
    if f["fonte"]:
        c.setFillColor(FRACO)
        c.setFont("Helvetica", 5.8)
        for i, ln in enumerate(wrap("fonte no slide: " + f["fonte"], "Helvetica", 5.8, w_img - 6 * mm)):
            c.drawString(x, y_img - 4 * mm - i * 2.6 * mm, ln)


def main():
    if not os.path.exists(ENTRADA):
        sys.exit("nao achei " + ENTRADA)
    p = Fichas()
    with open(ENTRADA, encoding="utf-8") as fh:
        p.feed(fh.read())
    if len(p.fichas) != 10:
        sys.exit("esperava 10 fichas, achei %d" % len(p.fichas))

    c = canvas.Canvas(SAIDA, pagesize=landscape(A4))
    c.setTitle("Capitulo 1 — as dez telas")
    c.setAuthor("Prof. Angelo Mondaini Calvao — IPRJ/UERJ")
    for i, f in enumerate(p.fichas, start=1):
        desenhar_ficha(c, f, i)
        c.showPage()
    c.save()
    print("ok", SAIDA, "%d fichas" % len(p.fichas))


if __name__ == "__main__":
    main()
