# CLAUDE.md — Estudo CMB (6º ano)

Plano de estudo para uma criança que presta o **Concurso de Admissão ao 6º ano do
Colégio Militar de Brasília** em **18/10/2026** (domingo). Projeto pessoal do Diogo —
**não é Belo Coffee nem UCS**; nada daqui vai para nenhum repositório dos dois negócios.

## Idioma
Sempre responder em português brasileiro.

## Ao abrir uma sessão aqui
1. Ler `progress.md` (estado atual e próximo passo) antes de responder qualquer coisa.
2. Ler `PLANO.md` (desenho aprovado + critério de "pronto" de cada fase).

## Quem usa o quê
- **A criança** usa **só** `roteiro/index.html` — sozinha, sem adulto por perto.
- **Diogo** prepara o material com o Claude e manda as redações dela para correção.
- `pesquisa/` é a "cozinha": nunca é mostrada à criança.

## Regras do material
- Linguagem de criança de 10 anos em tudo que vai para o roteiro.
- Teoria em vídeo: **Khan Academy primeiro**; YouTube só onde a Khan não tem (Português, redação).
- **Nada fora do programa do edital** — não inventar assunto, dica ou exigência que não esteja na fonte.
- Todo link é testado antes de entrar (abre, é o assunto certo, duração anotada).
- Toda tarefa tem "como sei que terminei" (gabarito ou autocorreção).
- **Nenhum dado pessoal da criança em lugar nenhum** — nem nome, nem apelido, nem escola/unidade, nem turno, nem foto, nem letra dela. Não em arquivo do projeto, não em memória do Claude, não em mensagem de commit, não em prompt de agente. Ordem explícita do Diogo (22/09). Ao se referir a ela: "a criança" / "ela".
- **Material escaneado do cursinho** (`material/`, ignorado pelo git): as folhas trazem nome manuscrito, unidade e correção à caneta. Nunca versionar, nunca copiar trecho com nome, e **apagar as imagens renderizadas** (PNG do scratchpad) assim que a análise terminar. No roteiro, referenciar só por "lista 14, questões 3 a 7".
- **Resolução de questão do CMB** segue o padrão aprovado (🎯 o que ela quer → balões numerados → ✅ resposta → 💡 atalho → ⚠️ escorregão → 🎬 vídeo se existir), fórmulas em KaTeX; validar com `node roteiro/check_katex.js` antes de publicar.
- **Toda resolução que troca unidade desenha a escada** (`div.escada`, unidades de partida e chegada marcadas com `.aqui`) antes de fazer a conta — a criança não lembrou da escada na 2ª questão do Dia 1 (pedido do Diogo, 21/09). Comprimento, massa e capacidade: ×10/÷10 por degrau. **Área: ×100/÷100 por degrau; volume: ×1000/÷1000 por degrau** — e nessas duas vai uma explicação de 1 linha do porquê (1 m = 10 dm → 1 m² = 10 × 10 = 100 dm² → 1 m³ = 10 × 10 × 10 = 1000 dm³). Ponte capacidade↔volume quando aparecer: 1 L = 1 dm³, 1 mL = 1 cm³, 1 m³ = 1000 L.

## Freios (risco baixo: não gasta dinheiro, não fala com terceiros)
- Checagem automática de links antes de entregar o roteiro.
- Revisão do roteiro por agente separado antes de ir para a criança.

## Git e publicação
Repo **público** `diogobr23/estudo-cmb`, publicado no GitHub Pages (a página da criança e as provas em PDF ficam acessíveis pela URL).
⚠️ Por ser público: **nenhum dado da criança** aqui — nem nome, nem foto, nem redação. `.gitignore` bloqueia fotos e a pasta `redacoes/`; redações corrigidas ficam fora do repo.
