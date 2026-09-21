#!/usr/bin/env node
/* make_og_cards.mjs — build the link-preview images.
 *
 * Why this exists as a separate tool rather than part of build_pages.py: the site's
 * figures are WebP, and LinkedIn's crawler does not read WebP. An og:image pointing at
 * a .webp is silently dropped and the post renders as a title-and-domain card with no
 * picture, which is exactly what happened to the SaaS article. So every page that wants
 * a preview needs a JPEG twin, and JPEG encoding lives with the other image tooling
 * (capture_shots.mjs) rather than in the page generator.
 *
 * Output is 1200x630. That is the size LinkedIn documents for the large card; below
 * 1200x627 it may fall back to the small one. Our heroes are wider than 1.91:1, so they
 * are fitted rather than cropped, on a background sampled from each image's own corner,
 * which makes the letterbox invisible on the cream covers we use.
 *
 * Run after adding or changing an article hero:  node admin/build/make_og_cards.mjs
 * validate.js fails the build if a referenced card is missing, so a forgotten run is
 * caught before it ships rather than discovered on LinkedIn.
 */
import sharp from 'sharp';
import fs from 'fs';
import path from 'path';

const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname), '../..');
const OUT  = path.join(ROOT, 'og');
const W = 1200, H = 630;

fs.mkdirSync(OUT, { recursive: true });

/* Every article's first !shot becomes that article's card. Parsed from the same
   markdown the page is built from, so the two cannot disagree. */
const articlesDir = path.join(ROOT, 'admin/content/articles');
const jobs = [];
for (const f of fs.readdirSync(articlesDir).filter(f => f.endsWith('.md'))) {
  const src = fs.readFileSync(path.join(articlesDir, f), 'utf8');
  const m = src.match(/^!shot\s+([^\s|]+)\s*\|\s*([^\s|]+)/m);
  if (!m) continue;
  const img = path.join(ROOT, 'articles', m[2], m[1]);
  if (!fs.existsSync(img)) { console.log('  SKIP (no such figure):', m[1]); continue; }
  jobs.push({ slug: f.replace(/\.md$/, ''), img });
}

for (const j of jobs) {
  const corner = await sharp(j.img).extract({ left: 2, top: 2, width: 8, height: 8 }).stats();
  const [r, g, b] = corner.channels.slice(0, 3).map(c => Math.round(c.mean));
  const out = path.join(OUT, `${j.slug}.jpg`);
  const info = await sharp(j.img)
    .resize(W, H, { fit: 'contain', background: { r, g, b } })
    .jpeg({ quality: 88, mozjpeg: true })
    .toFile(out);
  console.log(`  ${j.slug}.jpg  ${info.width}x${info.height}  ${(info.size / 1024).toFixed(0)} KB  bg rgb(${r},${g},${b})`);
}

/* The fallback for every page that is not an article with a hero. Drawn here rather
   than hand-made so it restyles with the site and never goes stale on the version. */
const card = `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}">
  <rect width="${W}" height="${H}" fill="#faf9f5"/>
  <rect x="0" y="0" width="${W}" height="10" fill="#0f766e"/>
  <text x="90" y="250" font-family="Georgia,'Times New Roman',serif" font-size="92" font-weight="700" fill="#101114">sgit<tspan fill="#0f766e">.ai</tspan></text>
  <text x="90" y="330" font-family="system-ui,-apple-system,'Segoe UI',sans-serif" font-size="38" fill="#34363c">Git for encrypted vaults,</text>
  <text x="90" y="384" font-family="system-ui,-apple-system,'Segoe UI',sans-serif" font-size="38" fill="#34363c">for humans and AI agents.</text>
  <text x="90" y="470" font-family="ui-monospace,SFMono-Regular,Menlo,monospace" font-size="25" fill="#5b6170">Version it like git. Hand it over with a single read key.</text>
  <text x="90" y="508" font-family="ui-monospace,SFMono-Regular,Menlo,monospace" font-size="25" fill="#5b6170">The server that stores it cannot read it.</text>
  <rect x="90" y="556" width="250" height="2" fill="#e3e0d8"/>
  <text x="90" y="590" font-family="ui-monospace,SFMono-Regular,Menlo,monospace" font-size="22" fill="#8b909c" letter-spacing="2">pip install sgit-ai</text>
</svg>`;
const d = await sharp(Buffer.from(card)).jpeg({ quality: 90, mozjpeg: true }).toFile(path.join(OUT, 'default.jpg'));
console.log(`  default.jpg  ${d.width}x${d.height}  ${(d.size / 1024).toFixed(0)} KB`);
console.log(`\nwrote ${jobs.length + 1} cards to og/`);
