#!/usr/bin/env node
/* make_banners.mjs — the 1920x1080 cover for every article and newsletter issue.
 *
 * Why: a piece posted as a LinkedIn article needs a cover image, and the covers that work
 * carry the title and the key ideas on the image itself (the reader sees the cover first,
 * often without the title under it). Making one by hand per article does not scale to an
 * article a day, so the cover is rendered from data the article already has: its title,
 * its teaser, the claims in its graph, and its own hero infographic. A newsletter issue
 * gets a mosaic of the cards of the articles it covers instead of a hero.
 *
 * Input: articles/banners/manifest.json, written by build_pages.py (run the build first).
 * Output: articles/banners/<slug>.jpg, 1920x1080. A banner is re-rendered only when its
 * manifest entry or its source image changes (articles/banners/.hashes.json).
 *
 *     node admin/build/make_banners.mjs            render what changed
 *     node admin/build/make_banners.mjs --all      render everything
 *     node admin/build/make_banners.mjs --only <slug>
 *
 * Uses the Playwright Chromium that the screenshot tooling already uses; nothing external
 * is loaded, system fonts only, like the site.
 */
import { createRequire } from 'module';
import fs from 'fs';
import path from 'path';
import crypto from 'crypto';
import { pathToFileURL } from 'url';

const require = createRequire(import.meta.url);
let chromium;
try { ({ chromium } = require('playwright')); }
catch (e) {
  const g = path.join(process.execPath, '..', '..', 'lib', 'node_modules', 'playwright');
  ({ chromium } = require(g));
}

const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname), '../..');
const DIR = path.join(ROOT, 'articles', 'banners');
const MAN = JSON.parse(fs.readFileSync(path.join(DIR, 'manifest.json'), 'utf8'));
const HASHES = path.join(DIR, '.hashes.json');
const ALL = process.argv.includes('--all');
const ONLY = process.argv.includes('--only') ? process.argv[process.argv.indexOf('--only') + 1] : null;
const [W, H] = MAN.size;

const esc = s => String(s || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const url = p => pathToFileURL(path.join(ROOT, p)).href;
const fmtDate = d => new Date(d + 'T00:00:00Z').toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric', timeZone: 'UTC' });

function hashOf(e) {
  const h = crypto.createHash('sha256').update(JSON.stringify(e));
  for (const p of [e.hero, ...(e.mosaic || [])].filter(Boolean)) {
    const f = path.join(ROOT, p);
    if (fs.existsSync(f)) h.update(String(fs.statSync(f).size) + ':' + crypto.createHash('sha256').update(fs.readFileSync(f)).digest('hex'));
  }
  return h.digest('hex').slice(0, 16);
}

function html(e) {
  const visual = e.mosaic && e.mosaic.length
    ? `<div class="mosaic n${Math.min(e.mosaic.length, 4)}">${e.mosaic.slice(0, 4).map(m => `<img src="${url(m)}">`).join('')}</div>`
    : e.hero ? `<div class="hero"><img src="${url(e.hero)}"></div>` : `<div class="hero empty"></div>`;
  const ideas = (e.ideas || []).map((t, i) => `<li><span class="n">${i + 1}</span><span>${esc(t)}</span></li>`).join('');
  return `<!doctype html><html><head><meta charset="utf-8"><style>
  *{box-sizing:border-box;margin:0;padding:0}
  html,body{width:${W}px;height:${H}px;background:#faf9f5;color:#17181c;font-family:ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;overflow:hidden}
  .frame{position:absolute;inset:0;display:grid;grid-template-columns:1.05fr .95fr;gap:70px;padding:90px 100px 140px}
  .top{position:absolute;left:0;right:0;top:0;height:14px;background:#0f766e}
  .kick{font-size:26px;letter-spacing:.2em;text-transform:uppercase;font-weight:800;color:#0f766e;margin-bottom:28px}
  .kick span{color:#8a8d94;font-weight:600;letter-spacing:.08em}
  h1{font-family:ui-serif,Georgia,"Times New Roman",serif;font-weight:700;letter-spacing:-.02em;line-height:1.06;color:#101114}
  .teaser{font-family:ui-serif,Georgia,serif;font-style:italic;font-size:31px;line-height:1.38;color:#3d4047;margin-top:26px;border-left:5px solid #b45309;padding-left:22px}
  ul{list-style:none;margin-top:34px;display:grid;gap:18px}
  li{display:grid;grid-template-columns:52px 1fr;gap:18px;align-items:start;font-size:30px;line-height:1.28;font-weight:600;color:#1c1d21}
  li .n{width:52px;height:52px;border-radius:50%;background:#0f766e;color:#fff;display:flex;align-items:center;justify-content:center;font-size:26px;font-weight:800}
  .left{display:flex;flex-direction:column;min-height:0}
  .right{display:flex;align-items:center;justify-content:center;min-height:0}
  .hero{width:100%;max-height:100%;background:#fff;border:1px solid #e5e1d5;border-radius:18px;box-shadow:0 18px 50px rgba(28,29,33,.13);padding:18px;display:flex;align-items:center;justify-content:center}
  .hero img{width:100%;height:auto;max-height:${H - 90 - 140 - 40}px;object-fit:contain;display:block;border-radius:6px}
  .hero.empty{height:100%;background:linear-gradient(135deg,#e7f3f1,#faf9f5)}
  .mosaic{width:100%;display:grid;gap:22px;grid-template-columns:1fr;align-content:center}
  .mosaic.n3 img:last-child{display:none}
  .mosaic img{width:100%;aspect-ratio:720/378;object-fit:cover;border-radius:14px;border:1px solid #e5e1d5;box-shadow:0 10px 30px rgba(28,29,33,.12);background:#fff}
  .mosaic.n4{grid-template-columns:1fr 1fr}
  .foot{position:absolute;left:100px;right:100px;bottom:48px;display:flex;justify-content:space-between;align-items:center;border-top:2px solid #17181c;padding-top:20px;font-size:26px;color:#5c5f66}
  .foot b{color:#17181c;font-weight:800}.foot b i{color:#0f766e;font-style:normal}
  .foot code{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:24px}
  </style></head><body><div class="top"></div><div class="frame">
  <div class="left"><p class="kick">${esc(e.kicker)} <span>&middot; ${esc(fmtDate(e.date))}</span></p>
  <h1 id="t">${esc(e.title)}</h1><p class="teaser" id="q">${esc(e.teaser)}</p><ul id="i">${ideas}</ul></div>
  <div class="right">${visual}</div></div>
  <div class="foot"><span><b>sgit<i>.ai</i></b> &nbsp;&middot;&nbsp; <code>${esc(e.url)}</code></span><span>${esc(e.author)}</span></div>
  <script>
  // fit: shrink the title until the left column fits; drop the teaser, then ideas, if it never does
  (function(){var left=document.querySelector('.left'),t=document.getElementById('t'),max=${H}-90-140;
   var s=86; t.style.fontSize=s+'px';
   function over(){return left.scrollHeight>max;}
   while(over()&&s>50){s-=2;t.style.fontSize=s+'px';}
   var lis=[].slice.call(document.querySelectorAll('#i li'));
   while(over()&&lis.length>1){lis.pop().remove();}
   if(over()){document.getElementById('q').remove();}
   while(over()&&s>40){s-=2;t.style.fontSize=s+'px';}
  })();
  </script></body></html>`;
}

const old = fs.existsSync(HASHES) ? JSON.parse(fs.readFileSync(HASHES, 'utf8')) : {};
const next = { ...old };
const todo = MAN.entries.filter(e => (!ONLY || e.slug === ONLY) &&
  (ALL || ONLY || old[e.slug] !== hashOf(e) || !fs.existsSync(path.join(ROOT, e.out))));
console.log(`banners: ${todo.length} to render of ${MAN.entries.length}`);
if (todo.length) {
  const b = await chromium.launch();
  const pg = await b.newPage({ viewport: { width: W, height: H } });
  const tmp = path.join(DIR, '.render.html');
  for (const e of todo) {
    fs.writeFileSync(tmp, html(e));
    await pg.goto(pathToFileURL(tmp).href, { waitUntil: 'load' });
    await pg.evaluate(() => Promise.all([...document.images].map(i => i.complete ? 0 : new Promise(r => { i.onload = i.onerror = r; }))));
    await pg.screenshot({ path: path.join(ROOT, e.out), type: 'jpeg', quality: 86 });
    next[e.slug] = hashOf(e);
    console.log('  wrote', e.out);
  }
  fs.rmSync(tmp, { force: true });
  await b.close();
}
for (const k of Object.keys(next)) if (!MAN.entries.some(e => e.slug === k)) delete next[k];
fs.writeFileSync(HASHES, JSON.stringify(next, null, 1) + '\n');
