#!/usr/bin/env python3
"""Gera o PDF de revisão da parte matemática da Fase 1 a partir de f1-matematica.html.

Fonte única: o HTML. Se o texto mudar lá, o PDF muda aqui — não existe cópia.
Uso: uv run --with reportlab python f1-matematica-pdf.py
"""
import os
import re
import sys
from html.parser import HTMLParser

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

AQUI = os.path.dirname(os.path.abspath(__file__))

# As fontes padrão do ReportLab não têm seta nem ≠ nem expoente: usamos DejaVu.
FONTE_DIR = "/usr/share/fonts/truetype/dejavu"
ROMANO, ROMANO_B, ROMANO_I = "DejaVu", "DejaVu-Bold", "DejaVu-Oblique"
MONO, MONO_B = "DejaVuMono", "DejaVuMono-Bold"


def registrar_fontes():
    pares = [
        (ROMANO, "DejaVuSans.ttf"), (ROMANO_B, "DejaVuSans-Bold.ttf"),
        ("DejaVu-Oblique", "DejaVuSans.ttf"), (MONO, "DejaVuSansMono.ttf"),
        (MONO_B, "DejaVuSansMono-Bold.ttf"),
    ]
    for nome, arq in pares:
        caminho = os.path.join(FONTE_DIR, arq)
        if os.path.exists(caminho):
            pdfmetrics.registerFont(TTFont(nome, caminho))
    pdfmetrics.registerFontFamily(ROMANO, normal=ROMANO, bold=ROMANO_B,
                                  italic=ROMANO, boldItalic=ROMANO_B)
import sys
RODAPE = "Fase 1"
ENTRADA = os.path.join(AQUI, (sys.argv[1] if len(sys.argv) > 1 else "f1-matematica.html"))
SAIDA = ENTRADA[:-5] + ".pdf"

TINTA = HexColor("#111318")
FRACO = HexColor("#5a6172")
AZUL = HexColor("#2b5f8a")
AMBAR = HexColor("#8a5a12")
VERMELHO = HexColor("#a3352c")
LINHA = HexColor("#c9ccd4")
FUNDO = HexColor("#f2eee6")

MACROS = [
    (r"\\leftarrow", "\u2190"),
    (r"\\rightarrow", "\u2192"),
    (r"\\neq", "\u2260"),
    (r"\\times", "\u00d7"),
    (r"\\cdot", "\u00b7"),
    (r"\\dots", "\u2026"),
    (r"\\operatorname\{sen\}", "sen"),
    (r"\\varnothing", "\u2205"),
    (r"\\mathbb\{R\}", "\u211d"),
    (r"\\in\b", "\u2208"),
    (r"\\cap\b", "\u2229"),
    (r"\\neq", "\u2260"),
    (r"\\\{", "{"),
    (r"\\\}", "}"),
    (r"\\dots", "\u2026"),
]


def tex_para_texto(t):
    r"""Retira os delimitadores \( \) e traduz os macros que o PDF não desenha."""
    for a, b in MACROS:
        t = re.sub(a, b, t)
    SUP = str.maketrans("0123456789-", "\u2070\u00b9\u00b2\u00b3\u2074\u2075\u2076\u2077\u2078\u2079\u207b")
    SUB = str.maketrans("0123456789", "\u2080\u2081\u2082\u2083\u2084\u2085\u2086\u2087\u2088\u2089")
    t = t.replace("^{-1}", "\u207b\u00b9")
    t = re.sub(r"\_\{([^}]*)\}", lambda m: m.group(1).translate(SUB), t)
    t = re.sub(r"\_(\w)", lambda m: m.group(1).translate(SUB), t)
    t = re.sub(r"\^\{([^}]*)\}", lambda m: m.group(1).translate(SUP), t)
    t = re.sub(r"\^(\d)", lambda m: m.group(1).translate(SUP), t)
    t = t.replace("\\(", "").replace("\\)", "").replace("\\[", "").replace("\\]", "")
    return re.sub(r"\s+", " ", t).strip()


class Blocos(HTMLParser):
    """Lê o documento em blocos desenháveis, na ordem em que aparecem."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.blocos = []
        self.pilha = []
        self.campo = None
        self.atual = None
        self.em_pre = False
        self.em_h3 = False

    # ---- helpers ----
    def _novo(self, tipo, **kw):
        b = {"tipo": tipo}
        b.update(kw)
        self.blocos.append(b)
        self.atual = b
        return b

    def _ultimo(self):
        b = self.atual
        if b is None:
            return ""
        if self.campo == "h3":
            return b.get("titulo", "")
        if self.campo == "txt":
            return b.get("txt", "")
        if self.campo == "li" and b.get("itens"):
            return b["itens"][-1]
        if self.campo == "p" and b.get("paras"):
            return b["paras"][-1][0]
        if self.campo == "dt" and b.get("campos"):
            return b["campos"][-1][0]
        if self.campo == "dd" and b.get("campos"):
            return b["campos"][-1][1]
        if self.campo == "rp" and b.get("paras"):
            return b["paras"][-1]
        return ""

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = a.get("class", "")
        self.pilha.append(tag)

        if tag == "h1":
            self._novo("h1", txt="")
            self.campo = "txt"
        elif tag == "p" and "sub" in cls:
            self._novo("sub", txt="")
            self.campo = "txt"
        elif tag == "div" and "aviso" in cls:
            self._novo("aviso", itens=[], titulo="")
            self.campo = None
        elif tag == "h2" and "parte" in cls:
            self._novo("parte", txt="")
            self.campo = "txt"
        elif tag == "p" and "intro" in cls:
            self._novo("intro", txt="")
            self.campo = "txt"
        elif tag == "section" and "conceito" in cls:
            self._novo("conceito", num="", titulo="", paras=[])
            self.campo = None
        elif tag == "section" and "ficha" in cls:
            self._novo("ficha", num="", titulo="", selo="", forma="", sistema="", campos=[])
            self.campo = None
        elif tag == "h3":
            self.em_h3 = True
            self.campo = "h3"
        elif tag == "span" and "num" in cls:
            self.campo = "num"
        elif tag == "span" and "selo" in cls:
            self.campo = "selo"
        elif tag == "span" and "forma" in cls:
            self.campo = "forma"
        elif tag == "li" and self.atual and self.atual["tipo"] == "aviso":
            self.atual["itens"].append("")
            self.campo = "li"
        elif tag == "pre":
            self.em_pre = True
            self.campo = "pre"
        elif tag == "dt":
            self.campo = "dt"
            # o dt vem antes do dd: o par nasce aqui, senão o rótulo cai no par anterior
            if self.atual and self.atual["tipo"] == "ficha":
                self.atual["campos"].append(["", ""])
        elif tag == "dd":
            self.campo = "dd"
        elif tag == "p" and self.atual and self.atual["tipo"] == "conceito":
            self.atual["paras"].append(["", "curto" in cls])
            self.campo = "p"
        elif tag == "p" and self.atual and self.atual["tipo"] == "rodape":
            self.atual["paras"].append("")
            self.campo = "rp"
        elif tag == "footer":
            self._novo("rodape", paras=[])
            self.campo = None

    def handle_endtag(self, tag):
        if self.pilha:
            self.pilha.pop()
        if tag == "pre":
            self.em_pre = False
        if tag == "span" and self.em_h3:
            # <span class="num">A1</span>uma solução — o título continua depois do span
            self.campo = "h3"
            return
        if tag == "h3":
            self.em_h3 = False
        if tag in ("h1", "h2", "h3", "p", "li", "dt", "dd", "span", "pre"):
            self.campo = None

    def handle_data(self, data):
        if self.campo is None or self.atual is None:
            return
        if self.em_pre:
            bruto = data
        else:
            bruto = re.sub(r"\s+", " ", data)
            if not bruto.strip():
                return
            # <b>x.</b> Conta: o espaço depois da tag não pode desaparecer
            ant = self._ultimo()
            if ant and not ant.endswith(" ") and not bruto.startswith(" ") \
                    and bruto.lstrip()[:1] not in (",", ".", ";", ":", "!", "?", ")", "\u2014"):
                bruto = " " + bruto
            if not ant:
                bruto = bruto.lstrip()
        if not bruto.strip():
            return
        b = self.atual
        if self.campo == "txt":
            b["txt"] += bruto
        elif self.campo == "h3":
            b["titulo"] += bruto
        elif self.campo == "num":
            b["num"] += bruto.strip()
        elif self.campo == "selo":
            b["selo"] += bruto.strip()
        elif self.campo == "forma":
            b["forma"] += bruto.strip()
        elif self.campo == "li":
            b["itens"][-1] += bruto
        elif self.campo == "pre":
            b["sistema"] += data
        elif self.campo == "dt":
            if b["campos"]:
                b["campos"][-1][0] += bruto
        elif self.campo == "dd":
            if b["campos"]:
                b["campos"][-1][1] += bruto
        elif self.campo == "p":
            b["paras"][-1][0] += bruto
        elif self.campo == "rp":
            b["paras"][-1] += bruto


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


class Doc:
    def __init__(self):
        self.c = canvas.Canvas(SAIDA, pagesize=A4)
        self.c.setTitle("Fase 1 — a parte matemática")
        self.c.setAuthor("Prof. Angelo Mondaini Calvão — IPRJ/UERJ")
        self.larg, self.alt = A4
        self.esq, self.dir = 20 * mm, 20 * mm
        self.topo = self.alt - 18 * mm
        self.base = 18 * mm
        self.y = self.topo
        self.pagina = 1
        self.largura = self.larg - self.esq - self.dir

    def nova_pagina(self):
        self.rodape_pagina()
        self.c.showPage()
        self.pagina += 1
        self.y = self.alt - 16 * mm

    def rodape_pagina(self):
        self.c.setFillColor(FRACO)
        self.c.setFont(ROMANO, 6.4)
        self.c.drawString(self.esq, 10 * mm, RODAPE.upper())
        self.c.drawRightString(self.larg - self.dir, 10 * mm, "p. %d" % self.pagina)

    def espaco(self, precisa):
        if self.y - precisa < self.base:
            self.nova_pagina()

    def titulo_ficha(self, b):
        self.espaco(38 * mm)
        x = self.esq
        y = self.y
        if b["num"]:
            etiqueta = b["num"]
            w = stringWidth(etiqueta, MONO_B, 8) + 3 * mm
            self.c.setFillColor(AMBAR)
            self.c.rect(x, y - 1.6 * mm, w, 5 * mm, fill=1, stroke=0)
            self.c.setFillColor(HexColor("#ffffff"))
            self.c.setFont(MONO_B, 8)
            self.c.drawString(x + 1.5 * mm, y, etiqueta)
            x += w + 2 * mm
        self.c.setFillColor(TINTA)
        self.c.setFont(ROMANO_B, 10)
        self.c.drawString(x, y, b["titulo"].strip())
        x += stringWidth(b["titulo"].strip(), ROMANO_B, 10) + 3 * mm
        if b["selo"]:
            self.c.setFillColor(VERMELHO)
            self.c.setFont(MONO_B, 6.4)
            self.c.drawString(x, y, b["selo"].upper())
            x += stringWidth(b["selo"].upper(), MONO_B, 6.4) + 3 * mm
        if b["forma"]:
            self.c.setFillColor(AZUL)
            self.c.setFont(MONO_B, 6.6)
            self.c.drawString(x, y, b["forma"].upper())
        self.y = y - 4.6 * mm

    def bloco_sistema(self, texto):
        linhas = [l.rstrip() for l in texto.strip("\n").split("\n") if l.strip()]
        if not linhas:
            return
        alto = len(linhas) * 4.1 * mm + 3.4 * mm
        self.espaco(alto + 6 * mm)
        self.c.setFillColor(FUNDO)
        self.c.rect(self.esq, self.y - alto, self.largura, alto, fill=1, stroke=0)
        self.c.setFillColor(AMBAR)
        self.c.rect(self.esq, self.y - alto, 1.6 * mm, alto, fill=1, stroke=0)
        self.c.setFillColor(TINTA)
        self.c.setFont(MONO, 7.6)
        yy = self.y - 4.4 * mm
        for ln in linhas:
            self.c.drawString(self.esq + 4 * mm, yy, ln)
            yy -= 4.1 * mm
        self.y -= alto + 3 * mm

    def desenhar(self, b):
        c = self.c
        tipo = b["tipo"]

        if tipo == "h1":
            self.espaco(24 * mm)
            c.setFillColor(TINTA)
            c.setFont(MONO_B, 16)
            c.drawString(self.esq, self.y, tex_para_texto(b["txt"]))
            self.y -= 7 * mm

        elif tipo == "sub":
            c.setFillColor(FRACO)
            c.setFont(ROMANO, 8.6)
            for ln in wrap(tex_para_texto(b["txt"]), ROMANO, 8.6, self.largura):
                c.drawString(self.esq, self.y, ln)
                self.y -= 4.2 * mm
            self.y -= 4 * mm

        elif tipo == "aviso":
            itens = [tex_para_texto(i) for i in b["itens"] if i.strip()]
            linhas = []
            for it in itens:
                linhas.extend(wrap("• " + it, ROMANO, 8.2, self.largura))
            alto = len(linhas) * 4 * mm + 5 * mm
            self.espaco(alto)
            c.setFillColor(FUNDO)
            c.rect(self.esq - 3 * mm, self.y - alto + 2 * mm, self.largura + 6 * mm, alto, fill=1, stroke=0)
            c.setFillColor(TINTA)
            c.setFont(ROMANO, 8.2)
            yy = self.y
            for ln in linhas:
                c.drawString(self.esq, yy, ln)
                yy -= 4 * mm
            self.y -= alto + 4 * mm

        elif tipo == "parte":
            self.espaco(20 * mm)
            if self.y < self.topo - 2 * mm:
                self.y -= 3 * mm
            c.setFillColor(TINTA)
            c.setFont(MONO_B, 10.5)
            c.drawString(self.esq, self.y, tex_para_texto(b["txt"]).upper())
            self.y -= 2.2 * mm
            c.setStrokeColor(TINTA)
            c.setLineWidth(1)
            c.line(self.esq, self.y, self.larg - self.dir, self.y)
            self.y -= 5 * mm

        elif tipo == "intro":
            c.setFillColor(FRACO)
            c.setFont(ROMANO, 8.4)
            for ln in wrap(tex_para_texto(b["txt"]), ROMANO, 8.4, self.largura):
                self.espaco(6 * mm)
                c.drawString(self.esq, self.y, ln)
                self.y -= 4.1 * mm
            self.y -= 2 * mm

        elif tipo == "conceito":
            self.espaco(24 * mm)
            x = self.esq
            if b["num"]:
                c.setFillColor(AMBAR)
                c.setFont(MONO_B, 8)
                c.drawString(x, self.y, b["num"])
                x += 11 * mm
            c.setFillColor(TINTA)
            c.setFont(ROMANO_B, 9.4)
            for ln in wrap(tex_para_texto(b["titulo"]), ROMANO_B, 9.4, self.largura - (x - self.esq)):
                c.drawString(x, self.y, ln)
                self.y -= 4.4 * mm
            for texto, curto in b["paras"]:
                if not texto.strip():
                    continue
                fonte = ROMANO if curto else ROMANO
                c.setFillColor(FRACO if curto else TINTA)
                c.setFont(fonte, 8.3)
                for ln in wrap(tex_para_texto(texto), fonte, 8.3, self.largura - 4 * mm):
                    self.espaco(6 * mm)
                    c.drawString(self.esq + 4 * mm, self.y, ln)
                    self.y -= 4.1 * mm
            c.setStrokeColor(LINHA)
            c.setLineWidth(0.7)
            c.line(self.esq, self.y + 1 * mm, self.larg - self.dir, self.y + 1 * mm)
            self.y -= 4 * mm

        elif tipo == "ficha":
            self.titulo_ficha(b)
            if b["sistema"].strip():
                self.bloco_sistema(b["sistema"])
            for rotulo, corpo in b["campos"]:
                corpo = tex_para_texto(corpo)
                if not corpo:
                    continue
                self.espaco(12 * mm)
                c.setFillColor(AZUL)
                c.setFont(MONO_B, 6.4)
                c.drawString(self.esq, self.y, rotulo.upper().strip())
                self.y -= 3.4 * mm
                c.setFillColor(TINTA)
                c.setFont(ROMANO, 8.4)
                for ln in wrap(corpo, ROMANO, 8.4, self.largura):
                    self.espaco(6 * mm)
                    c.drawString(self.esq, self.y, ln)
                    self.y -= 4.2 * mm
                self.y -= 1.2 * mm
            self.y -= 3 * mm

        elif tipo == "rodape":
            self.y -= 3 * mm
            for texto in b["paras"]:
                c.setFillColor(FRACO)
                c.setFont(ROMANO, 7.6)
                for ln in wrap(tex_para_texto(texto), ROMANO, 7.6, self.largura):
                    self.espaco(6 * mm)
                    c.drawString(self.esq, self.y, ln)
                    self.y -= 3.8 * mm
                self.y -= 2 * mm


def main():
    global RODAPE
    if not os.path.exists(ENTRADA):
        sys.exit("nao achei " + ENTRADA)
    p = Blocos()
    with open(ENTRADA, encoding="utf-8") as fh:
        p.feed(fh.read())

    h1 = [b for b in p.blocos if b["tipo"] == "h1"]
    RODAPE = h1[0].get("txt") or "Fase 1"

    fichas = [b for b in p.blocos if b["tipo"] == "ficha"]
    if not fichas:
        sys.exit("nenhuma ficha encontrada em " + ENTRADA)

    registrar_fontes()
    d = Doc()
    for b in p.blocos:
        d.desenhar(b)
    d.rodape_pagina()
    d.c.save()
    print("ok %s · %d fichas · %d paginas" % (SAIDA, len(fichas), d.pagina))


if __name__ == "__main__":
    main()
