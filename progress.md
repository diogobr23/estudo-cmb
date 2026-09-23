# progress — Estudo CMB

## Estado (21/09/2026, fim da 2ª sessão)
- ✅ Desenho aprovado → `PLANO.md`. Pasta criada.
- ✅ **Fase 1 · Pesquisa — CONCLUÍDA.**
  - Edital oficial 2026/2027 (DOU) em `pesquisa/edital-2026-2027.txt`; programa e regras resumidos em `pesquisa/01-o-que-cai.md`.
  - 6 provas (2020–2025) + gabaritos em `pesquisa/provas/`. Só a 2025 tem texto extraível; as outras são imagem.
  - 198 questões classificadas por assunto (`pesquisa/classificacao/<ano>.csv`, taxonomia em `pesquisa/taxonomia.md`), tabela em `classificacao/frequencia.md` (regenerar: `python pesquisa/frequencia.py`).
- ✅ **Fase 1b · Roteiro provisório** — Dias 1–3 (seg 21 a qua 23/09), revisado por agente separado, 9 ajustes aplicados.
- ✅ **Fase 2 · Aulas — CONCLUÍDA** (21/09): vídeo + exercício por assunto das faixas A e B em `pesquisa/02-aulas.md`. Khan primeiro; YouTube para Português, redação, escada, romanos, média e vistas. 34 vídeos do YouTube conferidos por oEmbed (`pesquisa/ytcheck.py`).
- ✅ **Fase 3 · Prática — CONCLUÍDA** (21/09): banco 2020+2021 esgotado, 43 questões com resolução escrita no padrão aprovado; tabela do que foi usado em `pesquisa/03-pratica.md`. Vídeos por questão só existem para 2020 (Matemática).
- ✅ **Fase 4 · Roteiro completo — PUBLICADO** (21/09): `roteiro/index.html` com 28 cards (Dia 1 seg 21/09 → Dia 27 sáb 17/10 + "Dia da prova"). 141 fórmulas KaTeX validadas, HTML balanceado, ids únicos, 10 PDFs locais existentes. Revisão por 2 agentes separados (Matemática / Português+fins de semana) — resultado e ajustes registrados abaixo em "Revisões".
- ⏳ **Fase 5 · Anki** — opcional, só se sobrar tempo. As 27 "dicas do dia" já são as cartas.

## Calendário do roteiro (como ficou)
| Semana | seg | ter | qua | qui | sex | sáb | dom |
|---|---|---|---|---|---|---|---|
| S1 21–27/09 | D1 frações | D2 decimais | D3 porcentagem | D4 Port interpretação | D5 Port vírgula | D6 diagnóstico 2022 | D7 redação 1 (herói) + revisão |
| S2 28/09–04/10 | D8 escada de unidades | D9 área e volume | D10 Port sentido das palavras | D11 classes/ordens/romanos | D12 Port conectivos | D13 simulado 2023 | D14 redação 2 (faz de conta) |
| S3 05–11/10 | D15 MMC/divisores | D16 gráficos/média | D17 Port tirinhas | D18 probabilidade/vistas | D19 Port poema | D20 simulado 2024 | D21 reescrita + revisão |
| S4 12–18/10 | D22 ensaio geral 2025 (feriado, 4h30 com redação) | D23 revisão Mat | D24 revisão Port | D25 revisão simulados | D26 leve + mochila | D27 véspera sem estudo | **PROVA** |

Padrão de dia de semana: 🎬 (10–14 min) → ✏️ Khan ou 📖 leitura (10–15) → 📝 2–5 questões do CMB com resolução (25) → 💡 dica (5). Simulado: 🧰 → 📝 (2h30/3h/4h30) → ✅ gabarito → 📓 anota conta/pergunta/assunto + ⭐ → 💡. Redação: 🎬/📖 correção → 📖 proposta + esqueleto → ✍️ 40 min → ✔ lista → 📷 foto → 🔁 revisão do simulado.

## Fluxo com o Diogo durante as 4 semanas
1. **Redações** (dom 27/09, dom 04/10, dom 11/10 reescrita, seg 12/10 ensaio): adulto fotografa → Diogo manda ao Claude → correção com a rubrica do edital (5 competências + 9 eliminatórias) em linguagem de 10 anos → Diogo entrega antes do domingo seguinte. Redações NÃO entram no repo (`.gitignore`).
2. **⭐ dos simulados** (2022, 2023, 2024, 2025): a criança marca as questões que não entendeu; Diogo manda "ano + número" → resolução escrita no padrão do roteiro, publicada num card de revisão.
3. Dia 22: confirmar com a criança o horário de início da prova (o roteiro manda "perguntar pro Diogo"); Dia 26: qual documento de identificação é aceito (Manual do Candidato do CMB).

## Publicação
- Repo público `diogobr23/estudo-cmb` + GitHub Pages: **https://diogobr23.github.io/estudo-cmb/** (redireciona para `roteiro/`). PDFs das provas servidos pela mesma URL. Atualizar = `git push` (Pages reconstrói em ~1 min).
- Antes de publicar mudança no roteiro: `node roteiro/check_katex.js` (fórmulas) + checagem de HTML balanceado/ids/links locais (script no scratchpad da sessão; refazer se precisar: html.parser + regex).

## Limitações conhecidas
- 🔴 **23/09 — Diogo testou e achou link quebrado no Dia 3**: a unidade `numeros-porcentagem-6ano` da Khan **não tem vídeo**, só exercício. Corrigido: teoria virou 3 vídeos do YouTube (verificados por oEmbed) e a prática aponta para dois exercícios específicos (`/e/`), com **treino de caderno + gabarito** como plano B dentro do próprio passo. **Lição: nunca mais linkar unidade da Khan ("assiste o primeiro vídeo da lista") — só link direto de vídeo `/v/` ou exercício `/e/`, e sempre com plano B.**
- ⚠️ Ainda restam 3 links de UNIDADE (mesmo risco), nos Dias 1 e 2: `arithmetic/...add-and-subtract-fractions-different-denominators`, `arithmetic/...add-and-subtract-decimals` e `pt-5-ano/numeros-numeros-decimais-5ano`. Ela já passou por esses dias; testar e trocar quando der.
- 2 links do Dia 1 e Dia 2 (soma de frações / soma de decimais) são do curso `arithmetic` (americano): pode haver vídeo em inglês com legenda. Também o Pratique "cálculo da média" (Dia 16) pode vir em inglês — avisado no próprio passo.
- **Khan Academy bloqueia robôs** (curl/WebFetch recebem só a casca; até endereço inventado devolve 200). Checagem de link da Khan por curl NÃO vale. Evidência usada: URL + título indexados pelo buscador. Para checagem de verdade: navegador ou testar na mão. Links novos da Fase 2 que valem testar na mão antes do dia: Dia 11 (valor posicional 6º ano), Dia 16 (gráficos de imagens, média), Dia 15 (dois Pratiques).
- Os cadernos de 2022, 2023 e 2024 não trazem a proposta de redação. Propostas usadas: 2020 (herói, 1ª pessoa) no Dia 7; 2021 (faz de conta, 1ª pessoa) no Dia 14; 2025 (água, 3ª pessoa, 15–30 linhas) no ensaio do Dia 22. Dia 21 = reescrita da pior das duas primeiras.
- Ressalvas: 2020 Q3 e Q5 anuladas; 2020 Q6 exige raiz/potência (fora); 2020 Q18 gabarito retificado (pulada, avisado no Dia 5); 2021 Q12 erro de enunciado; 2024 Q13 duas alternativas verdadeiras (avisado no Dia 20).
- Vídeos de correção de prova inteira (2022 Azambuja 1h, 2023 Prof. Vilmar 10 questões) só servem com adulto achando o minuto — o roteiro diz isso.
- Não consigo renderizar a página nesta sessão (sem navegador): visual conferido pelo Diogo no aparelho (21/09, "ficou bom").

## Decisões
- 21/09 (noite): **escada de conversão** desenhada (`div.escada`) em toda resolução que troca unidade — pedido do Diogo depois que a criança não lembrou da escada na Q8/2021 do Dia 1. Área ×100 e volume ×1000 com a explicação de 1 linha (1 m = 10 dm → 1 m² = 100 dm² → 1 m³ = 1000 dm³). Regra no `CLAUDE.md`.
- 21/09 (noite): simulados de fim de semana não ganham resolução escrita de todas as 30–40 questões — inviável e desnecessário. Fluxo: ⭐ → Diogo → resolução sob demanda. Vídeo de prova inteira fica como opcional.
- 21/09 (tarde): Diogo aprovou o visual v3 ("ficou bom"). Padrão de resolução (🎯 → balões → ✅ → 💡 → ⚠️ → 🎬, KaTeX) vale para todas as questões. Em Português: balões por alternativa (A–E) ou por passo, com a linha do texto citada.
- 21/09: fórmulas com **KaTeX 0.18.7 auto-hospedado** em `roteiro/vendor/katex/`. Antes de publicar: `node roteiro/check_katex.js`.
- 21/09: formato A (página única com cards). Khan Academy primeiro, YouTube só onde faltar.
- 21/09: criança estuda sozinha; redação corrigida pelo Claude via foto enviada pelo Diogo.
- 21/09: peso da frequência = principal 1 + secundário 0,5.
- 21/09: uso das provas: 2020–2021 = banco por assunto (esgotado); 2022 = diagnóstico (26/09); 2023 e 2024 = simulados (03 e 10/10); 2025 = ensaio geral 4h30 no feriado de 12/10; 17/10 só descanso.
- 21/09: tempo ≈ Mat 55% · Port 30% · Redação 15%.
- 22/09: **card fixo "📋 Regras da redação do CMB"** (`<section class="ref" id="regras-redacao">`, antes do Dia 1), com as 9 irregularidades que tornam INAPTO, a rubrica das 5 competências (4+4+5+3+4 = 20, APTO com 10) e o checklist de antes de entregar — tudo copiado do Art. 125 do edital. Linkado do "Como funciona" e dos Dias 7, 14, 21, 22, 24 e 28. Pedido do Diogo. O card NÃO usa a classe `.dia` de propósito: o script de progresso percorre `.dia` e exige um `.prog` em cada.
- 22/09: **a página mostra só a semana atual (seg–dom)** e troca sozinha pela data do aparelho — pedido do Diogo (ver 27 dias de uma vez assusta a criança). Cada card tem `data-data="AAAA-MM-DD"` (Dia N = 20/09 + N); o JS calcula a segunda da semana, esconde o resto com `.fora`, marca o card de hoje e escreve "Semana N de 4 · dd/mm a dd/mm". Botão "👀 Ver o plano inteiro" alterna `body.tudo`. Diogo não precisa rodar nada aos domingos. Antes de 21/09 mostra a semana 1; depois de 18/10, a semana 4. Lógica simulada em 12 datas.
- 22/09: card de regras da redação agora vem **recolhido** (`<details class="abrir">`) — era grande demais aberto.
- 22/09: Diogo confirmou que **os links da Khan abrem OK** (pendência do dia 21 encerrada). Correção das redações: outra pessoa vai corrigir; Diogo pode repassar depois — o roteiro continua mandando fotografar.
- 21/09 (noite): Português = interpretação (~75% do peso) + conectivos (1 questão/ano) — os dois já cobertos. **"Uso dos porquês" não entra**: 0 questões em 6 provas, fora do programa do edital; Diogo mandou seguir a pesquisa. Listas de exercícios do cursinho: Diogo manda fotos depois (antes de 13/10); só entram as que baterem com a frequência e tiverem gabarito, referenciadas sem subir o material pro repo.

## Revisões (agentes separados)
- Dias 1–3 (21/09, tarde): PODE IR COM AJUSTES PEQUENOS → 9 aplicados; 2ª revisão das resoluções: 0 erros de matemática, 10 pontes de linguagem aplicadas.
- Dias 4–28 (21/09, noite), dois agentes em paralelo, cada um refazendo contas e citações contra os PNGs das provas:
  - **Matemática** (Dias 8, 9, 11, 15, 16, 18, 23): PODE IR COM AJUSTES PEQUENOS — 15/15 respostas batem, **0 erros de conta**; 1 ajuste médio (Dia 18, Q10/2020: eu tinha descrito errado por que a alternativa A é falsa — é a coluna verde com 2, não a 2ª coluna com 4) + 6 de clareza (atalho "corta quatro zeros", letra C na Q1/2021, passo do MDC mostrado, "expoente" explicado, atalho da Q10). **8 trocas aplicadas.**
  - **Português + fins de semana** (Dias 4–7, 10, 12–14, 17, 19–22, 24–28): PODE IR COM AJUSTES PEQUENOS — 24/24 respostas e todas as citações/linhas batem; 6 médios (truque da vírgula e do "como" reescritos pelo teste da troca, não pela posição; Q16-B/2021 apontava pro parágrafo errado; truque "procura refletir" trocado por "combina com o desenho"; "ponto e vírgula" ambíguo; Dia 21 sem plano B) + 12 pequenos. **19 trocas aplicadas.**
  - Após os ajustes: 145 fórmulas KaTeX válidas, HTML balanceado, ids únicos. Publicado.

## Na fila (depois do CMB)
- **OBMEP — 2ª fase, 5º ano**: Diogo pediu (22/09) a mesma análise "o que cai" para a segunda fase da OBMEP. Fazer só depois de terminar a integração do material do cursinho. ⚠️ A lista "soma de sequências" do cursinho, **descartada para o CMB** (fora do edital), é material típico de OBMEP — guardar para essa frente.

## Próximo passo
1. Diogo: testar na mão os links da Khan dos Dias 8, 9, 11, 15, 16 e 18 (abrem? em português?) — 10 minutos. Trocar pelo equivalente se algum falhar.
2. Correção da 1ª redação (dom 27/09) e primeira leva de ⭐ do diagnóstico de 2022 (seg 28/09).
