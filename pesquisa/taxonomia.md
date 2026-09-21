# Taxonomia de assuntos — Concurso CMB 6º ano

Rótulos fixos para classificar cada questão das provas antigas. Derivados do programa
oficial do Edital nº 1/2026 (Art. 123 e 124). **Usar exatamente estes códigos.**

## Matemática
| Código | Assunto | Item do edital |
|---|---|---|
| M01 | Sistema de numeração: classes e ordens, valor posicional, numeração romana | 1a, 1b, 1n |
| M02 | Operações com números naturais (as 4 operações em problemas) | 1c |
| M03 | Expressões numéricas com naturais | 1d |
| M04 | Múltiplos, divisores, primos, critérios de divisibilidade | 1e |
| M05 | MMC | 1f |
| M06 | MDC | 1g |
| M07 | Frações: leitura, comparação, equivalência, operações, fração de quantidade | 1h, 1i, 1k |
| M08 | Decimais: leitura, comparação, operações, fração↔decimal | 1h, 1j, 1k |
| M09 | Expressões numéricas com frações e decimais | 1l |
| M10 | Porcentagem | 1m |
| M11 | Figuras planas: elementos, classificação de polígonos, ângulos | 2a, 2b |
| M12 | Perímetro e área de figuras planas | 2c |
| M13 | Sólidos geométricos: classificação, elementos (vértices/arestas/faces), planificação, vistas | 2d, 2e, 2f |
| M14 | Volume de paralelepípedos | 2g |
| M15 | Medidas de comprimento, superfície, volume, capacidade, massa + transformação de unidades | 3a, 3b, 3c |
| M16 | Medidas de tempo (horas, minutos, calendário, fuso) | 3a |
| M17 | Sistema monetário (dinheiro, troco, câmbio) | 3d |
| M18 | Leitura e organização de tabelas e gráficos | 4a, 4b |
| M19 | Média aritmética | 4c |
| M20 | Probabilidade | 4d |

## Língua Portuguesa
| Código | Assunto | Item do edital |
|---|---|---|
| P01 | Localizar informação explícita | 1a |
| P02 | Inferir sentido de palavra ou expressão pelo contexto | 1b, 1c |
| P03 | Inferir informação implícita | 1d |
| P04 | Elementos da narrativa (narrador, foco, personagens, enredo, tempo, espaço) | 1e |
| P05 | Interpretar texto com material gráfico (tirinha, charge, propaganda, foto) — verbal + não verbal | 1f |
| P06 | Finalidade do texto / gênero textual | 1g |
| P07 | Relações entre partes do texto: retomadas, substituições, coesão | 1h |
| P08 | Distinguir fato de opinião | 1i |
| P09 | Identificar o tema do texto | 1j |
| P10 | Ironia e humor | 2a |
| P11 | Vírgula: efeito de sentido / justificativa | 2b |
| P12 | Sinonímia e antonímia (efeito de sentido) | 2c |
| P13 | Outros sinais de pontuação (reticências, aspas, travessão, dois-pontos…) | 2d |
| P14 | Linguagem figurada (sem nomenclatura) | 2e |
| P15 | Classes de palavras (substantivo, adjetivo, artigo, numeral, advérbio, preposição…) | 2f |
| P16 | Flexão e derivação: formação de palavras, gênero/número/grau | 2g |
| P17 | Sílaba tônica, tonicidade e acentuação | 2h |
| P18 | Verbos: tempos e modos (indicativo e subjuntivo) | 2i |
| P19 | Pronomes pessoais (reto/oblíquo), demonstrativos e possessivos | 2j |
| P20 | Ortografia e outros (fora dos itens acima) | 3 |

## Formato do CSV (`classificacao/<ano>.csv`)
```
ano,questao,disciplina,primario,secundarios,resumo
2025,5,MAT,M14,M15|M08|M17,"volume da mala em litros (cm/dm/mm) + taxa por kg excedente"
```
- `primario` = o assunto principal (o que a questão pede no fim).
- `secundarios` = outros assuntos que a criança precisa dominar para resolver (0 a 3, separados por `|`). Vazio se não houver.
- `resumo` = 6–15 palavras, sem aspas internas.
