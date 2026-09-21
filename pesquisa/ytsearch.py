# Busca vídeos no YouTube e lista id | duração | canal | título. Uso: python ytsearch.py "termo 1" "termo 2"
import re, json, sys, urllib.parse, urllib.request
sys.stdout.reconfigure(encoding='utf-8')
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/128.0 Safari/537.36",
      "Accept-Language": "pt-BR,pt;q=0.9"}
def busca(q, n=6):
    url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote(q)
    raw = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read().decode('utf-8', 'ignore')
    m = re.search(r'var ytInitialData = (\{.*?\});</script>', raw, re.S)
    data = json.loads(m.group(1)); out = []
    def walk(o):
        if isinstance(o, dict):
            if 'videoRenderer' in o:
                r = o['videoRenderer']
                title = ''.join(x.get('text', '') for x in r.get('title', {}).get('runs', []))
                ch = ''.join(x.get('text', '') for x in r.get('ownerText', {}).get('runs', []))
                dur = r.get('lengthText', {}).get('simpleText', '')
                out.append((r['videoId'], dur, ch, title))
            for v in o.values(): walk(v)
        elif isinstance(o, list):
            for v in o: walk(v)
    walk(data); return out[:n]
for q in sys.argv[1:]:
    print(f"\n### {q}")
    for vid, dur, ch, title in busca(q): print(f"  {vid} | {dur:>6} | {ch} | {title}")
