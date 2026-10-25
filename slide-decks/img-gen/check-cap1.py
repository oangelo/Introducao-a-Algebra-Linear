import re, os, html

d = "/opt/data/workspace/Introducao-a-Algebra-Linear/worktrees/slides/slide-decks"
html_t = open(f"{d}/cap1-telas.html", encoding="utf-8").read()
cap = open(f"{d}/CAPITULO-1.md", encoding="utf-8").read()
sb = open(f"{d}/STORYBOARD-CAP1.md", encoding="utf-8").read()

def norm(s):
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s)
    s = s.replace("*", "").replace("\u00a0", " ")
    s = re.sub(r"\s+", " ", s).strip().strip(".")
    return s.lower()

h_frases = {}
for tag, body in re.findall(r"<!--\s*(Q\d\d)\s*-->(.*?)</section>", html_t, re.S):
    m = re.search(r'class="frase">(.*?)</p>', body, re.S)
    h_frases[tag] = norm(re.sub(r'<span class="menor">.*', '', m.group(1))) if m else None
    im = re.search(r'<img src="(img/[^"]+)" alt="([^"]*)"', body)
    if im and not os.path.exists(os.path.join(d, im.group(1))):
        print("IMG AUSENTE:", tag, im.group(1))
    if im and len(im.group(2)) < 20:
        print("ALT CURTO:", tag)

c_frases = {}
for m in re.finditer(r"\*\*(C\d+) · IMAGEM:\*\*.*?\n\*\*FRASE:\*\* \*(.*?)\*", cap, re.S):
    c_frases[m.group(1)] = norm(m.group(2))

s_frases = {}
for m in re.finditer(r"### (Q\d\d) ·.*?\n\*\*FRASE:\*\* \*(.*?)\*", sb, re.S):
    s_frases[m.group(1)] = norm(m.group(2))

ok = True
for i in range(1, 11):
    q, c = f"Q{i:02d}", f"C{i}"
    vals = {"html": h_frases.get(q), "capitulo": c_frases.get(c), "storyboard": s_frases.get(q)}
    base = vals["html"]
    dif = {k: v for k, v in vals.items() if base is None or v is None or v != base}
    if dif:
        ok = False
        print("DIVERGE", q)
        for k, v in vals.items():
            print("   %-11s %s" % (k, v))

print("FRASES:", "todas iguais nos tres arquivos" if ok else "ha divergencias")
print("cartelas:", len(h_frases), len(c_frases), len(s_frases))
