/* capture_shots.mjs — drive a published vault in a real browser and save cropped
   screenshots for the site's walkthrough rows.

   Why this exists: the walkthrough explains things a new reader cannot infer from a
   live embed alone (that clicking a photo opens a carousel; that the app ships a
   debug pane with a REPL; that the source is readable in the browser). Each claim
   needs a picture of the actual product, not a mock-up — so this drives the real
   UI with only a PUBLISHED READ KEY, performs the navigation, and crops the result.

   Read-only by construction: every shot opens with a read key. No vault key is ever
   passed to this tool.

     node admin/build/capture_shots.mjs [--mirror] [--vault <slug>] [--only <name>]

   --mirror routes *.sgraph.ai through a local curl-backed proxy on :8898 (needed in
   sandboxes whose browser cannot egress; omit it on a normal machine).

   Selectors are documented where they are non-obvious — the HUD and the debug pane
   live in shadow DOM, and the app itself runs in a nested frame. */
import { chromium } from 'playwright';
import sharp from 'sharp';
import fs from 'fs';
import path from 'path';

const ROOT     = path.resolve(path.dirname(new URL(import.meta.url).pathname), '../..');
// One folder per vault, images inside it: demos/vaults/<slug>/images/<name>.webp —
// so a vault's page and its pictures are a single self-contained unit.
const outDir   = slug => path.join(ROOT, 'demos/vaults', slug, 'images');
const ORIGIN   = 'https://dev.vault.sgraph.ai';
const MIRROR   = process.argv.includes('--mirror');
const ONLY     = process.argv.includes('--only') ? process.argv[process.argv.indexOf('--only') + 1] : null;
const VAULT    = process.argv.includes('--vault') ? process.argv[process.argv.indexOf('--vault') + 1] : null;
const HOSTS    = new Set(['dev.vault.sgraph.ai', 'dev.send.sgraph.ai', 'dev.sgraph.ai', 'dev.tools.sgraph.ai']);

// The Algarve gallery vault — read key published on /vaults/algarve-photos.html.
const ALGARVE = 'sgit_rk1_0a0f34839d737eef0f8f66e5236990b1f397af064763e3f71dca2717015f9d15:3d04e6b9ca98';

const RISK = 'sgit_rk1_a702fba803faac4369eb5d5a320b4dfa017af62bd2425fb298aac4b99e95c0ae:4zf6pf2z';

const RISKGRAPH = 'sgit_rk1_92cad4cea8f58c55f59b686c71c935225a1ba7c41ecb6922a8aa570467604f6e:0610gsp9';

const EXPLORER = 'sgit_rk1_1c1b95f5903e35850a9bc0541ffa09c6b5d4017cbf18817d2ad6f894127e5638:3simlnqe';

const SUPPLEMENT = 'sgit_rk1_047186b559528058c66d1792b7345639b1238cb95c166d1d5f5b65c59813c2ee:r7zes477';

/* Each shot: which surface to open, what to do, and what to crop.
   target: 'app'   → an element inside the vault app's own frame
           'page'  → an element (or shadow path) on the SG/App or SG/Vault page
           'clip'  → an explicit viewport rectangle */
const SHOTS = [
  { name: 'gallery-row', vault: 'algarve-may-2026', cred: ALGARVE, surface: 'app', viewport: [1600, 1000],
    steps: [{ appScroll: '.grid-row' }, { wait: 1200 }],
    target: 'app', sel: '.grid-row' },

  { name: 'lightbox', vault: 'algarve-may-2026', cred: ALGARVE, surface: 'app', viewport: [1600, 1000],
    // Clicking a figure opens the app's own lightbox: .lb with prev/next and a caption.
    steps: [{ appClick: '.grid-row figure' }, { wait: 1800 }],
    target: 'clip', clip: [0, 0, 1600, 1000] },

  { name: 'hud-vault', vault: 'algarve-may-2026', cred: ALGARVE, surface: 'app', viewport: [1800, 1000],
    // The HUD's "more" menu is hidden in minimal mode, but its debug button still
    // works when clicked through the shadow root — that is how the pane opens.
    steps: [{ shadowClick: ['app-hud', '.hud-debug-btn'] }, { wait: 3000 }],
    target: 'page', shadowSel: ['app-debug-pane'], trim: 0.42 },

  { name: 'hud-repl', vault: 'algarve-may-2026', cred: ALGARVE, surface: 'app', viewport: [1800, 1000],
    steps: [{ shadowClick: ['app-hud', '.hud-debug-btn'] }, { wait: 2500 },
            { shadowClickText: ['app-debug-pane', '.dp-tab', 'REPL'] }, { wait: 1200 },
            { replType: ['vfs.list', 'vfs.list /photos'] }, { wait: 1500 }],
    target: 'page', shadowSel: ['app-debug-pane'], trim: 0.46 },

  { name: 'source-view', vault: 'algarve-may-2026', cred: ALGARVE, surface: 'vault', viewport: [1700, 1000],
    // The vault browser: expand photos/originals, then open index.html as source.
    steps: [{ wait: 2500 }, { clickText: ['.sb-tree__folder-name', 'photos'] }, { wait: 1500 },
            { clickText: ['.sb-tree__folder-name', 'originals'] }, { wait: 1500 },
            { clickText: ['.sb-action-btn', 'Source'] }, { wait: 2500 }],
    target: 'clip', clip: [0, 0, 1700, 1000] },

  { name: 'sgit-history', vault: 'algarve-may-2026', cred: ALGARVE, surface: 'vault', viewport: [1700, 1000],
    steps: [{ wait: 1500 }, { navView: 'sgit' }, { wait: 3500 }],
    target: 'clip', clip: [0, 0, 1700, 1000] },

  // ---- Supplement Stack (r7zes477) — the patient-held record ----
  { name: 'today', vault: 'supplement-stack', cred: SUPPLEMENT, surface: 'app', viewport: [1500, 1000],
    steps: [{ appClickText: ['button', 'Today'], frameHas: '#p-today' }, { wait: 1500 }],
    target: 'app', sel: '#p-today' },

  { name: 'stack', vault: 'supplement-stack', cred: SUPPLEMENT, surface: 'app', viewport: [1500, 1100],
    steps: [{ appClickText: ['button', 'Stack'], frameHas: '#p-stack' }, { wait: 2500 }],
    target: 'app', sel: '#p-stack', trim: 0.5 },

  { name: 'totals', vault: 'supplement-stack', cred: SUPPLEMENT, surface: 'app', viewport: [1500, 1100],
    steps: [{ appClickText: ['button', 'Totals'], frameHas: '#p-totals' }, { wait: 2000 }],
    target: 'app', sel: '#p-totals', trim: 0.55 },

  { name: 'briefing', vault: 'supplement-stack', cred: SUPPLEMENT, surface: 'app', viewport: [1500, 1100],
    steps: [{ appClickText: ['button', 'Briefing'], frameHas: '#p-briefing' }, { wait: 2000 }],
    target: 'app', sel: '#p-briefing', trim: 0.6 },

  // ---- Risk Mandate (4zf6pf2z) — a software project built inside a vault ----
  { name: 'app-open', vault: 'risk-mandate', cred: RISK, surface: 'app', viewport: [1500, 1000],
    steps: [{ wait: 4000 }],
    target: 'clip', clip: [0, 0, 1500, 1000] },

  // The whole privilege claim in one file: LLM use granted, key never granted,
  // and write scoped to one workspace folder.
  { name: 'permissions', vault: 'risk-mandate', cred: RISK, surface: 'vault', viewport: [1700, 1000],
    steps: [{ wait: 2500 }, { clickText: ['.sb-tree__file-name', 'app.json'] }, { wait: 2500 }],
    target: 'clip', clip: [0, 0, 1700, 820] },

  { name: 'history', vault: 'risk-mandate', cred: RISK, surface: 'vault', viewport: [1700, 1000],
    steps: [{ wait: 2000 }, { navView: 'sgit' }, { wait: 4000 }],
    target: 'clip', clip: [0, 0, 1700, 1000] },

  // ---- Agentic Browser Isolation (0610gsp9) — a living risk graph ----
  { name: 'app-open', vault: 'agentic-browser-isolation', cred: RISKGRAPH, surface: 'app', viewport: [1500, 1050],
    steps: [{ wait: 5000 }],
    target: 'clip', clip: [0, 0, 1500, 1050] },

  { name: 'stakeholders', vault: 'agentic-browser-isolation', cred: RISKGRAPH, surface: 'app', viewport: [1500, 1050],
    steps: [{ wait: 4000 }, { appClickLink: 'people.html' }, { wait: 5000 }],
    target: 'clip', clip: [0, 0, 1500, 1050] },

  { name: 'graph', vault: 'agentic-browser-isolation', cred: RISKGRAPH, surface: 'app', viewport: [1500, 1050],
    steps: [{ wait: 4000 }, { appClickLink: 'graphviz.html' }, { wait: 6000 }],
    target: 'clip', clip: [0, 0, 1500, 1050] },

  { name: 'permissions', vault: 'agentic-browser-isolation', cred: RISKGRAPH, surface: 'vault', viewport: [1700, 1000],
    steps: [{ wait: 2500 }, { clickText: ['.sb-tree__file-name', 'app.json'] }, { wait: 2500 }],
    target: 'clip', clip: [0, 0, 1700, 780] },

  // ---- Risk graph explorer (3simlnqe) — public by design ----
  // The two states are the app's argument: nothing at stake -> a short register.
  { name: 'empty', vault: 'risk-graph-explorer', cred: EXPLORER, surface: 'app', viewport: [1500, 1050],
    steps: [{ wait: 5000 }],
    target: 'clip', clip: [0, 0, 1500, 1050] },

  { name: 'exposed', vault: 'risk-graph-explorer', cred: EXPLORER, surface: 'app', viewport: [1500, 1050],
    steps: [{ wait: 4500 }, { appClickText: ['button', 'Exposed'] }, { wait: 4000 }],
    target: 'clip', clip: [0, 0, 1500, 1050] },

  // Its own publication rules, written in the vault and enforced by its build.
  { name: 'public-md', vault: 'risk-graph-explorer', cred: EXPLORER, surface: 'vault', viewport: [1700, 1000],
    steps: [{ wait: 2500 }, { clickText: ['.sb-tree__file-name', 'PUBLIC.md'] }, { wait: 3000 }],
    target: 'clip', clip: [0, 0, 1700, 1000] },

  { name: 'permissions', vault: 'risk-graph-explorer', cred: EXPLORER, surface: 'vault', viewport: [1700, 1000],
    steps: [{ wait: 2500 }, { clickText: ['.sb-tree__file-name', 'app.json'] }, { wait: 2500 }],
    target: 'clip', clip: [0, 0, 1700, 760] },

  // The scoped-write claim, shown in the vault's own app.json rather than asserted.
  { name: 'permissions', vault: 'supplement-stack', cred: SUPPLEMENT, surface: 'vault', viewport: [1700, 1000],
    steps: [{ wait: 2500 }, { clickText: ['.sb-tree__file-name', 'app.json'] }, { wait: 2500 }],
    target: 'clip', clip: [0, 0, 1700, 760] },
];

async function route(ctx) {
  if (!MIRROR) return;
  await ctx.route('**/*', async r => {
    const u = new URL(r.request().url());
    if (!HOSTS.has(u.hostname)) return r.continue();
    if (r.request().method() !== 'GET') return r.abort();
    try {
      let res;
      for (let a = 0; a < 5; a++) {
        try { res = await fetch(`http://localhost:8898/PROXY/${u.hostname}${u.pathname}${u.search}`); break; }
        catch (e) { if (a === 4) throw e; await new Promise(s => setTimeout(s, 300 * (a + 1))); }
      }
      r.fulfill({ status: res.status, body: Buffer.from(await res.arrayBuffer()),
        headers: { 'content-type': res.headers.get('content-type') || 'application/octet-stream',
                   'access-control-allow-origin': '*' } });
    } catch (e) { r.abort(); }
  });
}

// The vault app renders in a nested frame with no URL of its own (srcdoc). Identify
// it by a selector the app is known to contain — the /en-gb/app shell frame also has
// text, so "first frame with content" picked the wrong one.
async function appFrame(page, must = null, timeout = 90000) {
  const t0 = Date.now();
  while (Date.now() - t0 < timeout) {
    for (const f of page.frames()) {
      if (f === page.mainFrame()) continue;
      const ok = await f.evaluate(m => {
        if (m) return !!document.querySelector(m);
        // no selector given: any frame that has rendered real content. The /en-gb/app
        // shell frame stays empty, so this distinguishes it from the vault's own app.
        return !!document.body && document.body.innerText.trim().length > 30;
      }, must).catch(() => false);
      if (ok) return f;
    }
    await page.waitForTimeout(1000);
  }
  return null;
}

// Query through arbitrarily nested shadow roots (the REPL input is two deep:
// app-debug-pane -> app-debug-repl -> input).
const DEEP_QUERY = `(sel) => {
  function walk(root) {
    const hit = root.querySelector(sel);
    if (hit) return hit;
    for (const el of root.querySelectorAll('*')) {
      if (el.shadowRoot) { const r = walk(el.shadowRoot); if (r) return r; }
    }
    return null;
  }
  return walk(document);
}`;

async function runStep(page, step) {
  if (step.wait) return page.waitForTimeout(step.wait);

  if (step.appScroll || step.appClick) {
    const sel = step.appScroll || step.appClick;
    const f = await appFrame(page, sel.split(' ')[0]);
    if (!f) throw new Error('app frame not found for ' + sel);
    const act = step.appScroll ? 'scroll' : 'click';
    return f.evaluate(([s, a]) => {
      const el = document.querySelectorAll(s)[a === 'scroll' ? 1 : 0];
      if (!el) throw new Error('no ' + s);
      if (a === 'scroll') el.scrollIntoView({ block: 'center' }); else el.click();
    }, [sel, act]);
  }

  if (step.appClickText) {
    const [sel, text] = step.appClickText;
    const f = await appFrame(page, step.frameHas || sel.split(' ')[0]);
    if (!f) throw new Error('app frame not found');
    return f.evaluate(([s, t]) => {
      const el = [...document.querySelectorAll(s)].find(x => (x.textContent || '').trim() === t);
      if (!el) throw new Error('no control "' + t + '"');
      el.click();
    }, [sel, text]);
  }

  if (step.appClickLink) {
    const f = await appFrame(page, step.frameHas || null);
    if (!f) throw new Error('app frame not found');
    await f.evaluate(h => {
      const a = [...document.querySelectorAll('a[href]')].find(x => (x.getAttribute('href') || '').endsWith(h));
      if (!a) throw new Error('no link ending ' + h);
      a.click();
    }, step.appClickLink);
    return;
  }

  if (step.shadowClick) {
    const [host, sel] = step.shadowClick;
    return page.evaluate(([h, s]) => {
      const el = document.querySelector(h);
      const b = el && el.shadowRoot && el.shadowRoot.querySelector(s);
      if (!b) throw new Error('no ' + h + ' >> ' + s);
      b.click();
    }, [host, sel]);
  }

  if (step.shadowClickText) {
    const [host, sel, text] = step.shadowClickText;
    return page.evaluate(([h, s, t]) => {
      const el = document.querySelector(h);
      const root = el && el.shadowRoot;
      if (!root) throw new Error('no shadow ' + h);
      const b = [...root.querySelectorAll(s)].find(x => (x.textContent || '').includes(t));
      if (!b) throw new Error('no tab ' + t);
      b.click();
    }, [host, sel, text]);
  }

  if (step.replType) {
    // Playwright's selector engine pierces open shadow roots, so the REPL input is
    // addressable directly and can be typed into for real rather than by dispatching
    // synthetic events — what gets captured is what a visitor would produce.
    const input = page.locator('app-debug-repl input').first();
    await input.waitFor({ state: 'visible', timeout: 30000 });
    for (const cmd of step.replType) {
      await input.click();
      await input.fill(cmd);
      await input.press('Enter');
      await page.waitForTimeout(1200);
    }
    return;
  }

  if (step.clickText) {
    const [sel, text] = step.clickText;
    return page.evaluate(([s, t]) => {
      const cand = [...document.querySelectorAll(s)]
        .filter(e => (e.textContent || '').trim().toLowerCase().includes(t.toLowerCase()));
      // the shallowest match is the row itself rather than an ancestor container
      cand.sort((a, b) => (a.textContent || '').length - (b.textContent || '').length);
      if (!cand[0]) throw new Error('no row matching ' + t);
      cand[0].click();
    }, [sel, text]);
  }

  if (step.navView) {
    return page.evaluate(v => {
      const nav = document.querySelector('vault-nav');
      const root = nav ? (nav.shadowRoot || nav) : document;
      const el = root.querySelector(`.vn-item[data-view="${v}"]`);
      if (!el) throw new Error('no nav item ' + v);
      el.click();
    }, step.navView);
  }
}

async function capture(browser, shot) {
  const ctx = await browser.newContext({ viewport: { width: shot.viewport[0], height: shot.viewport[1] }, deviceScaleFactor: 2 });
  await route(ctx);
  const page = await ctx.newPage();
  page.setDefaultTimeout(120000);
  page.setDefaultNavigationTimeout(120000);

  // Read-key open: the root inbox for App Mode, /en-gb/vault for the browser surface.
  await page.goto(ORIGIN + '/#' + encodeURIComponent(shot.cred), { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(9000);
  if (shot.surface === 'vault') {
    await page.goto(ORIGIN + '/en-gb/vault/', { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(14000);
  } else {
    const must = shot.frameHas || (shot.target === 'app' ? shot.sel : null);
    if (!await appFrame(page, must)) throw new Error('app never rendered');
  }

  for (const step of shot.steps) await runStep(page, step);

  let buf;
  if (shot.target === 'clip') {
    buf = await page.screenshot({ clip: { x: shot.clip[0], y: shot.clip[1], width: shot.clip[2], height: shot.clip[3] } });
  } else if (shot.target === 'app') {
    const f = await appFrame(page, shot.sel.split(' ')[0]);
    buf = await f.locator(shot.sel).first().screenshot();
  } else {
    // element in the top-level page, possibly a custom element with shadow content
    buf = await page.locator(shot.shadowSel[0]).first().screenshot();
  }

  const dir = outDir(shot.vault);
  fs.mkdirSync(dir, { recursive: true });
  const out = path.join(dir, shot.name + '.webp');
  let img = sharp(buf);
  if (shot.trim) {
    const m = await img.metadata();
    img = sharp(buf).extract({ left: 0, top: 0, width: m.width, height: Math.round(m.height * shot.trim) });
  }
  await img.resize({ width: 1500, withoutEnlargement: true }).webp({ quality: 76 }).toFile(out);
  const kb = (fs.statSync(out).size / 1024).toFixed(0);
  console.log(`  ✓ ${shot.vault}/${shot.name.padEnd(14)} ${kb} KB`);
  await ctx.close();
}

const browser = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium' });
console.log('capturing vault walkthrough shots' + (MIRROR ? ' (through the local mirror)' : '') + ':');
for (const shot of SHOTS) {
  if (ONLY && shot.name !== ONLY) continue;
  if (VAULT && shot.vault !== VAULT) continue;
  try { await capture(browser, shot); }
  catch (e) { console.log(`  ✗ ${shot.name.padEnd(14)} ${String(e.message).slice(0, 90)}`); }
}
await browser.close();
