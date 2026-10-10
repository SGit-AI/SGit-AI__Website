#!/usr/bin/env node
/* test_meter.mjs — SG Meter in a real browser, against the built site.
 *
 *   node admin/build/test_meter.mjs
 *
 * Serves the repo root on a local port, opens it in Chromium and drives the meter the way a
 * reader would: read by depth, decline, reload, go below zero, return from a payment, add a
 * persona, keep and reject articles, read as that persona, export and restore into a fresh
 * browser. No mocks: the component, its config and articles/graphs.json are the published ones.
 * Skips (exit 0) when Playwright or Chromium is not available, as the estate's tests do.
 */
import http from 'http'
import fs from 'fs'
import path from 'path'
import os from 'os'
import { execSync } from 'child_process'

const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname), '../..')
let chromium
try {
    ({ chromium } = await import('playwright'))
} catch (e) {
    try {
        const g = execSync('npm root -g').toString().trim()
        ;({ chromium } = await import(path.join(g, 'playwright', 'index.mjs')))
    } catch (e2) { console.log('SKIP: playwright is not installed'); process.exit(0) }
}

const TYPES = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json',
                '.tpl': 'text/plain', '.webp': 'image/webp', '.jpg': 'image/jpeg', '.svg': 'image/svg+xml' }
const server = http.createServer((req, res) => {
    const p = path.join(ROOT, decodeURIComponent(new URL(req.url, 'http://x').pathname))
    if (!p.startsWith(ROOT) || !fs.existsSync(p) || fs.statSync(p).isDirectory()) { res.writeHead(404); res.end(); return }
    res.writeHead(200, { 'content-type': TYPES[path.extname(p)] || 'application/octet-stream' })
    fs.createReadStream(p).pipe(res)
})
await new Promise(r => server.listen(0, '127.0.0.1', r))
const B = `http://127.0.0.1:${server.address().port}/`

let browser
try { browser = await chromium.launch() } catch (e) { console.log('SKIP: Chromium is not available'); server.close(); process.exit(0) }

let failed = 0
const check = (ok, what) => { console.log(`${ok ? 'ok  ' : 'FAIL'} ${what}`); if (!ok) failed++ }
const ctx = await browser.newContext({ viewport: { width: 1200, height: 800 } })
const pg = await ctx.newPage()
const errors = []
pg.on('pageerror', e => errors.push(e.message))
pg.on('console', m => { if (m.type() === 'error') errors.push(m.text()) })
const state = () => pg.evaluate(() => JSON.parse(localStorage.getItem('sgit.meter.v1') || 'null'))
const shadow = (sel, q) => pg.evaluate(([s, q]) => {
    const e = document.querySelector(s)
    return e && e.shadowRoot ? (q ? [...e.shadowRoot.querySelectorAll(q)].length : e.shadowRoot.textContent) : null
}, [sel, q])
const scrollTo = d => pg.evaluate(d => {
    const m = document.querySelector('main'), r = m.getBoundingClientRect()
    window.scrollTo(0, r.top + scrollY + r.height * d - innerHeight)
}, d)
const wait = ms => pg.waitForTimeout(ms)
const feed = JSON.parse(fs.readFileSync(path.join(ROOT, 'articles/graphs.json'), 'utf8')).articles
const art = feed.slice().sort((a, b) => b.date < a.date ? -1 : 1)
const today = new Date().toISOString().slice(0, 10)
const older = art.find(a => (Date.parse(today) - Date.parse(a.date)) / 86400000 > 8)

try {
    // depth
    await pg.goto(B + `articles/${older.slug}.html`); await wait(1200)
    let s = await state()
    check(s && s.log[0].price === 5 && s.log[0].cost === 0.5, `opening an older article charges a tenth of 5p (${s && s.log[0].cost})`)
    await scrollTo(0.5); await wait(900)
    s = await state()
    check(s.log[0].cost > 0.5 && s.log[0].cost < 5, `half way down costs part of the price (${s.log[0].cost}p)`)
    // images load lazily and lengthen the page, so the end is reached the way a reader reaches it:
    // keep scrolling until the page stops growing
    for (let i = 0; i < 4; i++) { await pg.evaluate(() => window.scrollTo(0, document.body.scrollHeight)); await wait(700) }
    s = await state()
    check(s.log[0].cost === 5 && s.balance === 495, `the end costs the whole price (balance ${s.balance}, spent ${s.spent}, cost ${s.log[0].cost}, log ${s.log.length}, reads ${s.reads})`)
    // the reader card: usefulness sets the price, and the article is in the reading list
    const rate = n => pg.evaluate(n => document.querySelector('sg-meter[view=page]').shadowRoot.querySelectorAll('.seg')[0].querySelectorAll('button')[n - 1].click(), n)
    check((await state()).personas[0].on.includes(older.slug), 'an article opened for the first time joins the reading list')
    await rate(5); await wait(300); s = await state()
    check(s.log[0].cost === 10 && s.balance === 490, `rated excellent, it costs double (${s.log[0].cost}p)`)
    await rate(1); await wait(300); s = await state()
    check(s.log[0].cost === 0 && s.balance === 500, 'rated not useful, it is free')
    await rate(3); await wait(300)
    // decline
    await pg.evaluate(() => document.querySelector('sg-meter[view=page]').shadowRoot.querySelector('button.link').click()); await wait(200)
    await pg.evaluate(() => document.querySelector('sg-meter[view=page]').shadowRoot.querySelector('.reasons button').click()); await wait(300)
    s = await state()
    check(s.balance === 500 && s.log[0].declined && s.log[0].declined.reason === 'clickbait', 'declining refunds the page and keeps the reason')
    await pg.reload(); await wait(1000)
    s = await state()
    check(s.log.length === 1 && s.balance === 500, 'a reload in the same session does not charge again')
    // below zero, nothing blocked
    await pg.evaluate(() => { const s = JSON.parse(localStorage.getItem('sgit.meter.v1')); s.balance = 2; localStorage.setItem('sgit.meter.v1', JSON.stringify(s)) })
    await pg.goto(B + `articles/${art[0].slug}.html`); await wait(1000)
    await pg.evaluate(() => window.scrollTo(0, document.body.scrollHeight)); await wait(900)
    s = await state()
    check(s.balance < 0, `the balance goes below zero (${s.balance})`)
    check(await pg.evaluate(() => document.querySelector('sg-meter.meter-nav').shadowRoot.querySelector('a').classList.contains('neg')), 'the top bar marks a negative balance')
    // the payment return page, once per reference
    const before = s.balance
    await pg.goto(B + 'account/topped-up.html?session_id=cs_test_1'); await wait(1000)
    await pg.reload(); await wait(1000)
    s = await state()
    check(Math.abs(s.balance - (before + 500)) < 0.01 && s.topups.length === 1, 'the return page adds a top-up once per reference')
    // personas
    await pg.goto(B + 'account/newsroom.html'); await wait(2000)
    check((await shadow('sg-meter[view=newsroom]', '.preset')) >= 5, 'the newsroom offers the starting personas')
    await pg.evaluate(() => document.querySelector('sg-meter[view=newsroom]').shadowRoot.querySelector('.preset button').click()); await wait(1200)
    s = await state()
    const pid = s.active
    check(pid !== 'me' && s.personas.length === 2, `adding a preset makes it active (${pid})`)
    check((await shadow('sg-meter[view=newsroom]', '.pickwrap')) > 0, 'the new persona has picks')
    await pg.evaluate(() => { const r = document.querySelector('sg-meter[view=newsroom]').shadowRoot; r.querySelectorAll('.pact')[0].querySelectorAll('button')[1].click() }); await wait(800)
    await pg.evaluate(() => { const r = document.querySelector('sg-meter[view=newsroom]').shadowRoot; r.querySelectorAll('.pact')[0].querySelectorAll('button')[0].click() }); await wait(800)
    s = await state()
    const p = s.personas.find(x => x.id === pid)
    check(p.on.length === 1 && p.off.length === 1, 'Keep and Not for this persona curate the active persona')
    check(await pg.evaluate(() => {
        const g = document.querySelector('sg-meter[view=newsroom]').shadowRoot.querySelector('sg-meter[view=graph]')
        return !!(g && g.shadowRoot && g.shadowRoot.querySelector('svg.graph'))
    }), 'the newsroom draws the persona graph')
    await pg.goto(B + `articles/${art[1].slug}.html`); await wait(900)
    s = await state()
    check(s.log[0].persona === pid, 'a page read is credited to the active persona')
    // export and restore into a fresh browser
    const file = path.join(os.tmpdir(), `sg-meter-export-${process.pid}.json`)
    fs.writeFileSync(file, JSON.stringify(s))
    const fresh = await browser.newContext()
    const p2 = await fresh.newPage()
    p2.on('dialog', d => d.accept())
    await p2.goto(B + 'account/index.html'); await p2.waitForTimeout(1500)
    const input = await p2.evaluateHandle(() => document.querySelector('sg-meter[view=account]').shadowRoot.querySelector('input.file'))
    await input.asElement().setInputFiles(file); await p2.waitForTimeout(1500)
    const r = await p2.evaluate(() => JSON.parse(localStorage.getItem('sgit.meter.v1')))
    check(r.reads === s.reads && r.personas.length === 2, 'an export restores balance, history and personas in another browser')
    fs.unlinkSync(file)
    // sharing: the page shows exactly what would be sent, and copies it
    await pg.goto(B + 'account/share.html'); await wait(1500)
    const preview = await pg.evaluate(() => document.querySelector('sg-meter[view=share]').shadowRoot.querySelector('textarea.preview').value)
    check(/^My reading on /.test(preview) && /\nData:\n\{/.test(preview) && !/cs_test_1/.test(preview), 'the share preview has the summary and data, and no payment references')
    await ctx.grantPermissions(['clipboard-read', 'clipboard-write'])
    await pg.evaluate(() => [...document.querySelector('sg-meter[view=share]').shadowRoot.querySelectorAll('button')].find(b => /Copy to clipboard/.test(b.textContent)).click()); await wait(600)
    check((await pg.evaluate(() => navigator.clipboard.readText())) === preview, 'Copy puts exactly the preview on the clipboard')
    // phones
    const m = await browser.newPage({ viewport: { width: 390, height: 800 } })
    for (const u of ['account/newsroom.html', 'account/personas.html', 'account/share.html', 'account/index.html', `articles/${art[0].slug}.html`]) {
        await m.goto(B + u); await m.waitForTimeout(1200)
        const w = await m.evaluate(() => document.documentElement.scrollWidth)
        check(w <= 390, `no sideways scroll at 390px: ${u} (${w})`)
    }
    check(errors.length === 0, `no console errors${errors.length ? ': ' + errors.join(' | ') : ''}`)
} finally {
    await browser.close()
    server.close()
}
console.log(failed ? `${failed} FAILED` : 'ALL METER CHECKS PASS')
process.exit(failed ? 1 : 0)
