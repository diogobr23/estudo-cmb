"""Soma as classificações de classificacao/<ano>.csv e gera a tabela de frequência.

Peso de cada assunto por questão: primário = 1, secundário = 0,5.
Uso:  python frequencia.py            -> imprime e grava classificacao/frequencia.md
"""
import csv, glob, re, os, sys
sys.stdout.reconfigure(encoding="utf-8")
from collections import defaultdict

AQUI = os.path.dirname(os.path.abspath(__file__))
PESO_SECUNDARIO = 0.5

def ler_taxonomia():
    nomes = {}
    for linha in open(os.path.join(AQUI, "taxonomia.md"), encoding="utf-8"):
        m = re.match(r"\|\s*([MP]\d{2})\s*\|\s*(.+?)\s*\|", linha)
        if m:
            nomes[m.group(1)] = m.group(2)
    nomes["M00"] = "ilegível"; nomes["P00"] = "ilegível"
    return nomes

def ler_classificacoes():
    linhas = []
    for arq in sorted(glob.glob(os.path.join(AQUI, "classificacao", "*.csv"))):
        with open(arq, encoding="utf-8-sig") as f:
            for r in csv.DictReader(f):
                r["secundarios"] = [s.strip() for s in (r.get("secundarios") or "").split("|") if s.strip()]
                linhas.append(r)
    return linhas

def tabela(linhas, disciplina, nomes):
    anos = sorted({r["ano"] for r in linhas if r["disciplina"] == disciplina})
    prim = defaultdict(int); sec = defaultdict(int)
    por_ano = defaultdict(lambda: defaultdict(float))   # codigo -> ano -> peso
    total_q = defaultdict(int)
    for r in linhas:
        if r["disciplina"] != disciplina:
            continue
        total_q[r["ano"]] += 1
        p = r["primario"].strip()
        prim[p] += 1; por_ano[p][r["ano"]] += 1
        for s in r["secundarios"]:
            sec[s] += 1; por_ano[s][r["ano"]] += PESO_SECUNDARIO
    codigos = sorted(set(prim) | set(sec), key=lambda c: -(prim[c] + PESO_SECUNDARIO * sec[c]))
    out = []
    out.append(f"### {'Matemática' if disciplina=='MAT' else 'Língua Portuguesa'} — "
               f"{sum(total_q.values())} questões em {len(anos)} provas ({', '.join(anos)})\n")
    out.append("| # | Código | Assunto | Principal | Secundário | Peso | " + " | ".join(anos) + " |")
    out.append("|---|---|---|---|---|---|" + "---|" * len(anos))
    for i, c in enumerate(codigos, 1):
        peso = prim[c] + PESO_SECUNDARIO * sec[c]
        celulas = " | ".join(f"{por_ano[c][a]:g}" if por_ano[c][a] else "·" for a in anos)
        out.append(f"| {i} | {c} | {nomes.get(c, '?')} | {prim[c]} | {sec[c]} | {peso:g} | {celulas} |")
    return "\n".join(out), codigos, prim, sec

def main():
    nomes = ler_taxonomia()
    linhas = ler_classificacoes()
    if not linhas:
        print("nenhum CSV em classificacao/"); return
    partes = ["# Tabela de frequência — provas CMB 6º ano\n",
              f"Gerada por `frequencia.py`. Peso: principal = 1, secundário = {PESO_SECUNDARIO}. "
              "Colunas por ano mostram o peso somado naquele ano (· = não apareceu).\n"]
    for d in ("MAT", "PORT"):
        t, *_ = tabela(linhas, d, nomes)
        partes.append(t + "\n")
    texto = "\n".join(partes)
    with open(os.path.join(AQUI, "classificacao", "frequencia.md"), "w", encoding="utf-8") as f:
        f.write(texto)
    print(texto)

if __name__ == "__main__":
    main()
