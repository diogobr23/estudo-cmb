// Valida cada fórmula \( \) e \[ \] do index.html com o próprio KaTeX (throwOnError).
const fs = require('fs');
const katex = require('./vendor/katex/katex.min.js');
let h = fs.readFileSync(__dirname + '/index.html', 'utf8');
h = h.replace(/<script[\s\S]*?<\/script>/g, '');
const decode = s => s.replace(/&gt;/g, '>').replace(/&lt;/g, '<').replace(/&amp;/g, '&');
const B = '\\'; // uma barra invertida
function scan(open, close) {
  const out = [];
  let i = 0;
  while (true) {
    const a = h.indexOf(B + open, i); if (a < 0) break;
    const b = h.indexOf(B + close, a + 2); if (b < 0) break;
    out.push(h.slice(a + 2, b)); i = b + 2;
  }
  return out;
}
let n = 0, bad = 0;
for (const [open, close, display] of [['[', ']', true], ['(', ')', false]]) {
  for (const tex of scan(open, close)) {
    n++;
    try { katex.renderToString(decode(tex), { throwOnError: true, displayMode: display, strict: 'ignore' }); }
    catch (e) { bad++; console.log('ERRO:', tex.slice(0, 90), '->', e.message.slice(0, 120)); }
  }
}
console.log(`fórmulas: ${n}, com erro: ${bad}`);
process.exit(bad ? 1 : 0);
