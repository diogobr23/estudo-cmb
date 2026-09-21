# -*- coding: utf-8 -*-
"""Confere se vídeos do YouTube existem (oEmbed): python ytcheck.py ID1 ID2 ...
Imprime `ID | canal | título` ou `ID | ERRO`. Não valida conteúdo, só existência/título."""
import sys, json, urllib.request, urllib.parse

sys.stdout.reconfigure(encoding="utf-8")

def check(vid):
    url = "https://www.youtube.com/oembed?" + urllib.parse.urlencode(
        {"url": "https://www.youtube.com/watch?v=" + vid, "format": "json"})
    try:
        with urllib.request.urlopen(url, timeout=15) as r:
            d = json.load(r)
        return f"{vid} | {d.get('author_name','?')} | {d.get('title','?')}"
    except Exception as e:
        return f"{vid} | ERRO {e}"

if __name__ == "__main__":
    for v in sys.argv[1:]:
        print(check(v))
