#!/usr/bin/env node
/* sgit.ai site validation — run before every push: node admin/build/validate.js */
'use strict';
const fs = require('fs'), path = require('path'), vm = require('vm');

let root = __dirname;
while (!fs.existsSync(path.join(root, 'app.json'))) {
  const parent = path.dirname(root);
  if (parent === root) { console.error('vault root not found'); process.exit(2); }
  root = parent;
}

let fails = 0;
function walk(d) {
  return fs.readdirSync(d, { withFileTypes: true }).flatMap(e => {
    if (e.name === '.sg_vault' || e.name === '.git') return [];
    const p = path.join(d, e.name);
    return e.isDirectory() ? walk(p) : [p];
  });
}
const files = walk(root);

for (const f of files.filter(f => f.endsWith('.html'))) {
  const html = fs.readFileSync(f, 'utf8');
  const rel = path.relative(root, f);

  // 1. every inline script must parse
  [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].forEach((m, i) => {
    try { new vm.Script(m[1]); }
    catch (e) { fails++; console.log('JS FAIL', rel, 'script', i, e.message); }
  });

  // 2. authoring contract: no declarative refs to vault files
  const bad = html.match(/<link[^>]*href=(?!"data:)|<script[^>]+src=|<img[^>]+src=/g);
  if (bad) { fails++; console.log('CONTRACT FAIL', rel, bad); }

  // 3. internal links must resolve
  for (const m of html.matchAll(/href="([^"#]+\.(?:html|md))(#[^"]*)?"/g)) {
    const target = m[1];
    if (/^https?:/.test(target)) continue;
    if (!fs.existsSync(path.join(path.dirname(f), target))) {
      fails++; console.log('LINK FAIL', rel, '->', target);
    }
  }
}

// 4. shared JS must parse
try { new vm.Script(fs.readFileSync(path.join(root, 'assets/site.js'), 'utf8')); }
catch (e) { fails++; console.log('JS FAIL assets/site.js', e.message); }

// 5. banned words in content (retired concepts / legacy naming / stale stage)
const BANNED = [/dolt/i, /simple[\s_-]token/i, /word-word/i, /alpha(?![a-z])/i, /military[- ]grade/i,
  // no format-valid vault keys in site content — they are squattable namespaces on any SG/Send
  // server (24 lowercase-alnum : 4-24 lowercase-alnum = the real key shape). This is a PATTERN,
  // not a secret — never hardcode an actual passphrase here (that would be the leak this guards
  // against). The live vault's own passphrase is caught by the derived scan below.
  /\b[a-z0-9]{24}:[a-z0-9]{4,24}\b/];

// 5b. the passphrase tripwire, done safely: read the secret from the gitignored local/ tier
// (never present it in this tracked file) and scan the tree for it. Skips when local/ is absent
// (e.g. CI without the key) — the structural check above still applies there.
let SECRET = null;
try {
  const vk = fs.readFileSync(path.join(root, '.sg_vault/local/vault_key'), 'utf8').trim();
  const pass = vk.split(':')[0];
  if (pass && pass.length >= 12) SECRET = pass;
} catch (e) { /* local/ not present — structural check still covers key-shaped strings */ }

// the design brief quotes banned phrases in order to prohibit them — mention, not use.
// skills/ ships canonical upstream agent artifacts verbatim — not site copy, never edited here.
const EXEMPT = ['admin/build/validate.js', 'admin/brief-design-improvements.md'];
const EXEMPT_DIRS = ['skills/'];
for (const f of files.filter(f => /\.(html|css|js|md|json)$/.test(f)
    && !EXEMPT.some(x => f.replace(/\\/g, '/').endsWith(x))
    && !EXEMPT_DIRS.some(d => f.replace(/\\/g, '/').includes('/' + d)))) {
  const text = fs.readFileSync(f, 'utf8');
  for (const re of BANNED) {
    const m = text.match(re);
    if (m) { fails++; console.log('BANNED-WORD FAIL', path.relative(root, f), '->', JSON.stringify(m[0])); }
  }
  if (SECRET && text.includes(SECRET)) {
    fails++; console.log('SECRET-LEAK FAIL', path.relative(root, f), '-> vault passphrase present in a tracked file');
  }
}

console.log(fails === 0 ? `ALL CHECKS PASS (${files.length} files)` : `FAILURES: ${fails}`);
process.exit(fails === 0 ? 0 : 1);
