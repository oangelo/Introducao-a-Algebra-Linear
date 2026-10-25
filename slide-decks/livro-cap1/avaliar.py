#!/usr/bin/env python3
"""Avalia os fragmentos narrativos contra a rubrica e compara com o baseline.

Camada determinística (script): vocabulário, chavão, tamanho, legibilidade, presença de
conceito/entidade/entrega, números sem fonte.
Camada de julgamento: lida de criticas.json (saída dos críticos cegos) e sobrepõe os
critérios C1, C2, C4 e C5 quando existe.

Uso:
  python3 avaliar.py              # avalia e compara com baseline.json
  python3 avaliar.py --congelar   # grava o resultado atual como baseline (só com aprovação)
"""

import glob
import json
import os
import re
import sys
from datetime import datetime

AQUI = os.path.dirname(os.path.abspath(__file__))
RUBRICA = json.load(open(os.path.join(AQUI, "rubrica.json"), encoding="utf-8"))
MAPA = json.load(open(os.path.join(AQUI, "interludios.json"), encoding="utf-8"))
CRITICAS = os.path.join(AQUI, "criticas.json")
BASELINE = os.path.join(AQUI, "baseline.json")
SAIDA = os.path.join(AQUI, "qualidade.json")

FAIXA = MAPA["faixa_palavras"]
ENTIDADES = [e.lower() for e in MAPA["entidades_fio"]]

TAGS = re.compile(r"<[^>]+>")
MATH = re.compile(r"\\\(.*?\\\)|\\\[.*?\\\]", re.S)


def prosa(html):
    txt = MATH.sub(" ", html)
    txt = TAGS.sub(" ", txt)
    return re.sub(r"\s+", " ", txt).strip()


def frases(txt):
    return [f.strip() for f in re.split(r"(?<=[.!?])\s+", txt) if f.strip()]


def limitar(v, lo=0.0, hi=10.0):
    return max(lo, min(hi, v))


def avaliar_script(html, spec):
    p = prosa(html)
    baixo = p.lower()
    palavras = len(re.findall(r"\w+", p))
    notas, achados = {}, []

    # C3 vocabulário
    hits = [t for t in RUBRICA["proibidas_ficcao"] + RUBRICA["proibidas_chavao"]
            if re.search(r"\b%s\b" % re.escape(t.lower()), baixo)]
    notas["C3"] = limitar(10 - 2.5 * len(hits))
    if hits:
        achados.append("vocabulário proibido: " + ", ".join(sorted(set(hits))))

    # C4 (parte automática): chavão motivacional, exclamação
    mot = [pat for pat in RUBRICA["padroes_motivacionais"] if re.search(pat, p)]
    notas["C4_script"] = limitar(10 - 4 * len(mot))
    if mot:
        achados.append("padrão motivacional: %d" % len(mot))

    # C5 (parte automática): entidade do fio
    ent = [e for e in ENTIDADES if e in baixo]
    notas["C5_script"] = 10 if ent else 3
    if not ent:
        achados.append("não retoma nenhuma entidade do fio")

    # C6 entrega: última frase aponta o objeto matemático
    termo_entrega = [t.lower() for t in spec.get("entrega_termo", [])]
    if not termo_entrega:
        notas["C6"] = 10
    else:
        ult = " ".join(frases(p)[-2:]).lower()
        notas["C6"] = 10 if any(t in ult for t in termo_entrega) else 2
        if notas["C6"] < 10:
            achados.append("a última frase não entrega %r" % (spec.get("entrega"),))

    # C7 tamanho
    lo, hi = spec.get("faixa", FAIXA)
    if lo <= palavras <= hi:
        notas["C7"] = 10
    else:
        dist = (lo - palavras) if palavras < lo else (palavras - hi)
        notas["C7"] = limitar(10 - 10.0 * dist / 150)
        achados.append("fora da faixa: %d palavras (faixa %d-%d)" % (palavras, lo, hi))

    # C8 legibilidade
    fs = frases(p)
    media = sum(len(f.split()) for f in fs) / max(1, len(fs))
    longas = sum(1 for f in fs if len(f.split()) > 38) / max(1, len(fs))
    notas["C8"] = limitar(10 - max(0, media - 24) * 0.7 - longas * 20)
    if media > 30:
        achados.append("frase média de %.0f palavras" % media)

    # C1 (parte automática): conceito nomeado
    conc = [c.lower() for c in spec.get("conceito", [])]
    achou = sum(1 for c in conc if c in baixo)
    notas["C1_script"] = 10 if achou >= 2 else (6 if achou == 1 else 0)
    if achou == 0:
        achados.append("não nomeia o conceito da seção vizinha")

    # C2 (parte automática): número sem fonte
    nums = len(re.findall(r"\b\d{2,}\b", p))
    tem_fonte = ("doi:" in baixo) or bool(re.search(r"\b(19|20)\d{2}\b", p))
    notas["C2_script"] = 10 if nums == 0 else (8 if tem_fonte else 3)
    if nums and not tem_fonte:
        achados.append("%d números sem fonte citada" % nums)

    return notas, palavras, round(media, 1), achados


def carregar_criticas():
    if not os.path.exists(CRITICAS):
        return {}
    d = json.load(open(CRITICAS, encoding="utf-8"))
    return d.get("fragmentos", d)


def secoes_matematicas():
    """Fragmentos que não são narrativos: o texto que já foi aceito e não deve mudar."""
    narrativos = {os.path.basename(s["arquivo"]) for s in MAPA["fragmentos"]}
    arquivos = []
    for caminho in sorted(glob.glob(os.path.join(AQUI, "partes", "*.html"))):
        nome = os.path.basename(caminho)
        if nome.startswith("_") or nome.startswith("90") or nome in narrativos:
            continue
        arquivos.append(caminho)
    return arquivos


def impressao(html):
    import hashlib
    return hashlib.sha256(prosa(html).encode("utf-8")).hexdigest()[:16]


def main():
    criticas = carregar_criticas()
    base = {}
    if os.path.exists(BASELINE):
        base = json.load(open(BASELINE, encoding="utf-8")).get("fragmentos", {})
    base_math = {}
    if os.path.exists(BASELINE):
        base_math = json.load(open(BASELINE, encoding="utf-8")).get("matematica", {})

    resultado, falhas = {}, []
    pesos = {c["id"]: c["peso"] for c in RUBRICA["criterios"]}

    for spec in MAPA["fragmentos"]:
        caminho = os.path.join(AQUI, spec["arquivo"])
        if not os.path.exists(caminho):
            falhas.append("%s: arquivo ausente" % spec["id"])
            continue
        html = open(caminho, encoding="utf-8").read()
        notas, palavras, media_frase, achados = avaliar_script(html, spec)

        # sobrepõe com o julgamento dos críticos, quando existe
        crit = criticas.get(spec["id"], {})
        for cid in ("C1", "C2", "C4", "C5"):
            if cid in crit:
                notas[cid] = float(crit[cid])
            else:
                notas[cid] = notas.get(cid + "_script", notas.get(cid, 5))

        media = sum(notas[cid] * pesos[cid] for cid in pesos) / sum(pesos.values())
        resultado[spec["id"]] = {
            "arquivo": spec["arquivo"],
            "palavras": palavras,
            "frase_media": media_frase,
            "criterios": {cid: round(notas[cid], 1) for cid in pesos},
            "media": round(media, 2),
            "achados": achados,
        }

        if media < RUBRICA["regra_aceitacao"]["media_minima"]:
            falhas.append("%s: média %.2f < %.1f" % (spec["id"], media,
                                                     RUBRICA["regra_aceitacao"]["media_minima"]))
        for cid, v in resultado[spec["id"]]["criterios"].items():
            if v < RUBRICA["regra_aceitacao"]["minimo_por_criterio"]:
                falhas.append("%s: %s = %.1f abaixo do mínimo" % (spec["id"], cid, v))

        # anti-regressão: nenhuma seção aceita pode cair
        if spec["id"] in base:
            for cid, v in resultado[spec["id"]]["criterios"].items():
                antes = base[spec["id"]]["criterios"].get(cid)
                if antes is not None and v < antes - RUBRICA["regra_aceitacao"]["sem_regressao"]:
                    falhas.append("%s: REGRESSÃO em %s (%.1f -> %.1f)"
                                  % (spec["id"], cid, antes, v))

    saida = {"gerado_em": datetime.now().isoformat(timespec="seconds"),
             "fragmentos": resultado}

    # camada congelada: o texto de matemática já aceito não pode mudar sem aprovação
    saida["matematica"] = {os.path.basename(c): impressao(open(c, encoding="utf-8").read())
                           for c in secoes_matematicas()}
    if base_math and "--permitir-matematica" not in sys.argv:
        for nome, sha in saida["matematica"].items():
            antes = base_math.get(nome)
            if antes and antes != sha:
                falhas.append("seção de matemática ALTERADA sem autorização: " + nome)
    else:
        for nome in saida["matematica"]:
            if not base_math.get(nome):
                print("  (congelando) %s" % nome)

    json.dump(saida, open(SAIDA, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    for fid, r in resultado.items():
        print("%-12s média %5.2f  palavras %4d  frase %4.1f  %s"
              % (fid, r["media"], r["palavras"], r["frase_media"],
                 " ".join("%s=%.1f" % (k, v) for k, v in r["criterios"].items())))
        for a in r["achados"]:
            print("             - " + a)

    if "--congelar" in sys.argv:
        json.dump(saida, open(BASELINE, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print("\nbaseline congelado em baseline.json")
        return 0

    if falhas:
        print("\n%d BLOQUEIO(S):" % len(falhas))
        for f in falhas:
            print("  - " + f)
        return 1
    print("\nrubrica OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
