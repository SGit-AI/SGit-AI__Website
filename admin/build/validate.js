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
    // admin/content holds the page bodies the generator reads — source fragments, not
    // published pages. They have no <head>, no nav, and their links are checked in the
    // built output, so validating them here would only produce false failures.
    // node_modules is the capture harness's own dependencies (playwright, sharp) —
    // gitignored, never published, and full of vendored HTML and prose that would
    // otherwise fail every check here.
    if (e.name === '.sg_vault' || e.name === '.git' || e.name === 'node_modules') return [];
    if (e.name === 'content' && path.basename(d) === 'admin') return [];
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

  // 2. authoring contract: no declarative refs to vault files.
  // The contract exists because the vault host cannot serve a declarative fetch of a vault
  // path — stylesheets, scripts and images must come through the bridge. <link rel="canonical">
  // and rel="alternate" fetch nothing; they are metadata a crawler reads, so they are exempt.
  const bad = html.match(/<link(?![^>]*rel="(?:canonical|alternate)")[^>]*href=(?!"data:)|<script[^>]+src=|<img[^>]+src=/g);
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

// 3b. orphan check — every page must be reachable from at least one other page.
// (A page can be written, built, and pushed while nothing links to it; that happened
// with briefs.html in v0.1.13. Unreachable is the same as unpublished.)
{
  const pages = files.filter(f => f.endsWith('.html'));
  const linkedTo = new Set();
  for (const f of pages) {
    const html = fs.readFileSync(f, 'utf8');
    for (const m of html.matchAll(/href="([^"#]+\.html)(#[^"]*)?"/g)) {
      if (/^https?:/.test(m[1])) continue;
      linkedTo.add(path.resolve(path.dirname(f), m[1]));
    }
  }
  for (const f of pages) {
    if (path.resolve(f) === path.resolve(root, 'index.html')) continue;   // the front door
    if (!linkedTo.has(path.resolve(f))) {
      fails++; console.log('ORPHAN FAIL', path.relative(root, f), '-> generated but nothing links to it');
    }
  }
}

// 3c. markdown mirrors — agents are a first-class audience for this site, so every page
// must have a .md twin, and the links inside the markdown (which are rewritten .html -> .md)
// must resolve too. A dangling .md link is invisible from the HTML site and fatal to an agent.
{
  const pages = files.filter(f => f.endsWith('.html'));
  for (const f of pages) {
    const md = f.replace(/\.html$/, '.md');
    if (!fs.existsSync(md)) { fails++; console.log('MD-MIRROR FAIL', path.relative(root, f), '-> no .md twin'); }
  }
  for (const f of files.filter(f => f.endsWith('.md') && fs.existsSync(f.replace(/\.md$/, '.html')))) {
    const text = fs.readFileSync(f, 'utf8');
    for (const m of text.matchAll(/\]\(([^)\s]+\.md)(#[^)]*)?\)/g)) {
      if (/^https?:/.test(m[1])) continue;
      if (!fs.existsSync(path.join(path.dirname(f), m[1]))) {
        fails++; console.log('MD-LINK FAIL', path.relative(root, f), '->', m[1]);
      }
    }
    if (/<[a-z]+[ >]/.test(text.replace(/`[^`]*`/g, ''))) {
      fails++; console.log('MD-HTML FAIL', path.relative(root, f), '-> raw HTML leaked into the markdown');
    }
  }
}

// 3d. crawl surface. The fade-in that hides the unstyled flash once left the body at
// opacity:0 for any client that did not run the bootstrap — invisible to a reader and a
// hidden-text signal to an indexer. An agent reported the site not ranking for its own
// language; this is the regression guard for the fix, plus the files a crawler looks for.
{
  for (const f of files.filter(f => f.endsWith('.html'))) {
    const html = fs.readFileSync(f, 'utf8'), rel = path.relative(root, f);
    if (/opacity:0/.test(html) && !/<noscript><style>body\{opacity:1/.test(html)) {
      fails++; console.log('NOJS FAIL', rel, '-> body can stay invisible without JS');
    }
    if (/opacity:0/.test(html) && !/animation:sg-reveal/.test(html)) {
      fails++; console.log('NOJS FAIL', rel, '-> no CSS-only reveal failsafe');
    }
    if (!/rel="canonical"/.test(html)) { fails++; console.log('CANONICAL FAIL', rel); }
    for (const m of html.matchAll(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/g)) {
      try { JSON.parse(m[1]); }
      catch (e) { fails++; console.log('JSONLD FAIL', rel, e.message); }
    }
    if (!/application\/ld\+json/.test(html)) { fails++; console.log('JSONLD FAIL', rel, '-> no structured data'); }
  }
  const need = ['robots.txt', 'sitemap.xml', 'llms.txt', 'llms-full.txt'];
  for (const n of need) {
    if (!fs.existsSync(path.join(root, n))) { fails++; console.log('CRAWL FAIL', n, '-> missing'); }
  }
  const sitemap = fs.existsSync(path.join(root, 'sitemap.xml'))
    ? fs.readFileSync(path.join(root, 'sitemap.xml'), 'utf8') : '';
  for (const f of files.filter(f => f.endsWith('.html'))) {
    const rel = path.relative(root, f).replace(/\\/g, '/');
    if (sitemap && !sitemap.includes('/' + rel)) {
      fails++; console.log('SITEMAP FAIL', rel, '-> not listed');
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
  /\b[a-z0-9]{24}:[a-z0-9]{4,24}\b/,
  // the sgit CLI's canonical WRITE-credential prefix. New CLI output prints keys prefixed, so
  // a pasted key arrives self-labelled — a cheap, high-signal tripwire.
  //
  // Note the trailing [A-Za-z0-9]. The bare prefix is a NAME, not a key, and the site has to be
  // able to print it: guidance that cannot show readers what a write credential looks like
  // cannot teach them to spot one. A real key always carries its passphrase, so requiring one
  // following CREDENTIAL character catches every actual leak while letting documentation write
  // the prefix — where it is followed by markup (</code>, a backtick) rather than a secret.
  // (\S was tried first and failed for exactly that reason. This rule has caught its own author
  // three times, each time writing the prefix in prose, which is what prompted the precision.)
  // Belt and braces: the bare passphrase:vault_id shape above catches the body independently.
  // Its read-only sibling sgit_rk1_ is deliberately NOT banned: we publish those on purpose.
  /sgit_vk1_[A-Za-z0-9]/];

// 5b. the passphrase tripwire, done safely: read the secret from the gitignored local/ tier
// (never present it in this tracked file) and scan the tree for it. Skips when local/ is absent
// (e.g. CI without the key) — the structural check above still applies there.
const SECRETS = [];
try {
  const vk = fs.readFileSync(path.join(root, '.sg_vault/local/vault_key'), 'utf8').trim();
  const pass = vk.split(':')[0];
  if (pass && pass.length >= 12) SECRETS.push(pass);
} catch (e) { /* local/ not present — structural check still covers key-shaped strings */ }
// demo vaults: their write keys live in the same gitignored tier; every one is scanned for.
// (Read keys are deliberately published and are exempt by design — different shape entirely.)
try {
  const dk = path.join(root, '.sg_vault/local/demo-keys');
  for (const f of fs.readdirSync(dk)) {
    if (!/vault-key$/.test(f)) continue;
    const pass = fs.readFileSync(path.join(dk, f), 'utf8').trim().split(':')[0];
    if (pass && pass.length >= 12) SECRETS.push(pass);
  }
} catch (e) { /* no demo keys yet */ }

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
  for (const secret of SECRETS) {
    if (text.includes(secret)) {
      fails++; console.log('SECRET-LEAK FAIL', path.relative(root, f), '-> a vault passphrase is present in a tracked file');
    }
  }
}

console.log(fails === 0 ? `ALL CHECKS PASS (${files.length} files)` : `FAILURES: ${fails}`);
process.exit(fails === 0 ? 0 : 1);
