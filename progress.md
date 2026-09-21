# progress — Estudo CMB

## Estado (21/09/2026, fim da 1ª sessão)
- ✅ Desenho aprovado → `PLANO.md`. Pasta criada.
- ✅ **Fase 1 · Pesquisa — CONCLUÍDA.**
  - Edital oficial 2026/2027 (DOU) em `pesquisa/edital-2026-2027.txt`; programa e regras resumidos em `pesquisa/01-o-que-cai.md`.
  - 6 provas (2020–2025) + gabaritos em `pesquisa/provas/`. Só a 2025 tem texto extraível; as outras são imagem.
  - 198 questões classificadas por assunto (`pesquisa/classificacao/<ano>.csv`, taxonomia em `pesquisa/taxonomia.md`), tabela em `classificacao/frequencia.md` (regenerar: `python pesquisa/frequencia.py`).
  - Prioridades (faixas A/B/C/D) e uso de cada prova antiga: seção final do `01-o-que-cai.md`.
- ✅ **Fase 1b · Roteiro provisório** — `roteiro/index.html` com Dias 1–3 (**seg 21, ter 22, qua 23/09** — ela começou no dia 21): frações → decimais → porcentagem, Khan + 2 questões do CMB por dia (2020 Q9/Q11/Q4, 2021 Q8/Q9/Q4, PDF abrindo na página, resposta escondida em "Ver respostas"; gabaritos conferidos por resolução própria). Revisado por agente separado: **PODE IR COM AJUSTES PEQUENOS** — 9 ajustes aplicados (meta explícita "tela de resultado, mais da metade certa", timer, aviso de login, vídeo de pré-álgebra trocado pelo 1º vídeo da unidade de porcentagem do 6º ano, aviso de legenda nos 2 links do curso americano); item "5% e 6%" descartado porque vem da Q16 de 2025.
- ⏳ **Fase 2 · Aulas** — não começou. Pendência: a partir do **Dia 4 (qui 24/09)** a criança fica sem roteiro → Fase 2 + 4 precisam entregar até **quarta 23/09 à noite**.

## Próximo passo
1. Fase 2: para cada assunto das faixas A e B, achar vídeo (Khan; YouTube para Português) + exercício autocorrigido + duração. Enumerar as lições da Khan.
2. Fase 3: separar as questões de 2020/2021 por assunto (renderizar as páginas em PNG; usar os CSVs como índice) e achar vídeos de resolução das provas no YouTube.
3. Fase 4: estender `roteiro/index.html` até o Dia 27 (calendário no `PLANO.md`).

## Publicação (21/09)
- ✅ Repo público `diogobr23/estudo-cmb` + GitHub Pages: **https://diogobr23.github.io/estudo-cmb/** (redireciona para `roteiro/`). PDFs das provas servidos pela mesma URL. Atualizar = `git push` (Pages reconstrói em ~1 min).
- ✅ Pedido do Diogo: toda questão do CMB com resolução (vídeo curto se existir; senão escrita, revisada por agente). 6 resoluções escritas nos Dias 1–3; vídeos só para 2020 (canal Matemática para Vencer). Levantamento em `pesquisa/03-pratica.md`.

## Limitações conhecidas
- 2 links do Dia 1 e Dia 2 (soma de frações / soma de decimais) são do curso `arithmetic` (americano): pode haver vídeo em inglês com legenda. Testar 1 antes de terça; se estiver em inglês, trocar pelo equivalente BR na Fase 2.
- **Khan Academy bloqueia robôs** (curl/WebFetch recebem só a casca; até endereço inventado devolve 200). Checagem de link da Khan por curl NÃO vale. Evidência usada: URL + título indexados pelo buscador. Para checagem de verdade: navegador (claude-in-chrome, com autorização do Diogo) ou testar na mão.
- Os cadernos de 2022, 2023 e 2024 não trazem a proposta de redação (era caderno separado). Propostas disponíveis: 2020 (herói, 1ª pessoa, 20–30 linhas), 2021 (faz de conta, 1ª pessoa, 20–30 linhas), 2025 (água, 3ª pessoa, 15–30 linhas).
- Ressalvas dos leitores: 2020 Q3 e Q5 anuladas; 2021 Q12 provável erro de enunciado; 2024 Q13 com duas alternativas verdadeiras (gabarito D). Evitar essas questões no banco.

## Decisões
- 21/09: fórmulas desenhadas com **KaTeX 0.18.7 auto-hospedado** em `roteiro/vendor/katex/` (sem CDN; funciona no Pages e offline). Antes de publicar: `node roteiro/check_katex.js` (valida toda fórmula `\( \)` / `\[ \]` da página). Pedido do Diogo: fração desenhada, contas em pé, formatação melhor.
- 21/09: formato A (página única com cards). Khan Academy primeiro, YouTube só onde faltar.
- 21/09: criança estuda sozinha; redação corrigida pelo Claude via foto enviada pelo Diogo.
- 21/09: peso da frequência = principal 1 + secundário 0,5 (assunto "de carona" conta metade).
- 21/09: uso das provas: 2020–2021 = banco por assunto; 2022 = diagnóstico (26–27/09); 2023 e 2024 = simulados dos fins de semana 2 e 3; 2025 = ensaio geral 4h30 no feriado de 12/10; 17/10 só revisão leve.
- 21/09: tempo ≈ Mat 55% · Port 30% · Redação 15%.
