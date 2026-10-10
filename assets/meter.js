/* meter.js — a reading meter that lives entirely in the reader's browser.
 *
 * Every page on sgit.ai has a price, set by what it is and how old it is (the rules come from
 * the build, window.SGIT_METER, so the published price table and this file cannot disagree).
 * Opening a page debits a balance held in localStorage. A new reader starts with £5.00 of
 * credit; when it runs out, a top-up page takes them through a cart and a checkout that has
 * every step except the payment. The reading history the meter keeps is also what personalises
 * the site: the account page and the front page pick unread articles from the topics a reader
 * has paid for most.
 *
 * WHAT IT IS NOT, said first on every page that shows it: it charges nothing, takes no card,
 * and sends nothing anywhere. The balance, the history and the receipts are this browser's
 * localStorage. A new browser, a private window or clearing site data starts again with £5.00,
 * and also starts again with no history, so no personalisation. That trade is the experiment.
 *
 * Rules carried over from pt.newsroom.sgit.ai's pt-wallet, because they were right there:
 *   - it never blocks reading. Out of credit, the page is still shown and the read is recorded
 *     as unpaid, with an offer to top up;
 *   - one debit per page per browser session, so the back button is not a second purchase;
 *   - storage is allowed to fail. A browser that refuses localStorage gets a working page and
 *     a meter that says it cannot keep a balance.
 */
(function () {
  var CFG = window.SGIT_METER;
  if (!CFG || window.__sgitMeter) return;
  window.__sgitMeter = true;

  var KEY = 'sgit.meter.v1', SEEN = 'sgit.meter.v1.seen', LOG_MAX = 500;
  var ROOT = document.documentElement.getAttribute('data-root') || '';
  var noStorage = false;

  // ------------------------------------------------------------------ money and storage
  function gbp(p) { return (p < 0 ? '-' : '') + '£' + (Math.abs(p) / 100).toFixed(2); }
  function pence(p) { return p === 0 ? 'free' : p + 'p'; }
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function fresh() {
    return { v: 1, created: new Date().toISOString(), balance: CFG.start, spent: 0, reads: 0, unpaid: 0,
             paused: false, log: [], topups: [], cart: [] };
  }
  function read() {
    try {
      var raw = localStorage.getItem(KEY);
      if (!raw) return fresh();
      var s = JSON.parse(raw), f = fresh();
      for (var k in f) if (!(k in s)) s[k] = f[k];
      return s;
    } catch (e) { noStorage = true; return fresh(); }
  }
  function write(s) { try { localStorage.setItem(KEY, JSON.stringify(s)); } catch (e) { noStorage = true; } }
  var S = read();

  // ------------------------------------------------------------------ the price of this page
  var M = document.getElementById('sgit-meter') || { getAttribute: function () { return ''; } };
  var META = { kind: M.getAttribute('data-kind') || 'page', date: M.getAttribute('data-date') || '',
               title: M.getAttribute('data-title') || document.title, topics: (M.getAttribute('data-topics') || '').split(' ').filter(Boolean) };
  function ageDays(d) { return d ? Math.floor((Date.now() - Date.parse(d + 'T00:00:00Z')) / 86400000) : 9999; }
  function priceOf(meta) {
    if (meta.kind === 'article') return ageDays(meta.date) <= CFG.new_days ? CFG.prices.article_new : CFG.prices.article;
    return CFG.prices[meta.kind] != null ? CFG.prices[meta.kind] : CFG.prices.page;
  }
  var PRICE = priceOf(META);
  var PATH = location.pathname.replace(/index\.html$/, '') || '/';

  // ------------------------------------------------------------------ the charge
  var charged = null;   // what happened on this page view: 'paid' | 'unpaid' | 'seen' | 'free' | 'paused'
  (function charge() {
    if (PRICE === 0) { charged = 'free'; return; }
    if (S.paused) { charged = 'paused'; return; }
    var seen = [];
    try { seen = JSON.parse(sessionStorage.getItem(SEEN) || '[]'); } catch (e) { /* ok */ }
    if (seen.indexOf(PATH) >= 0) { charged = 'seen'; return; }
    var paid = S.balance >= PRICE;
    if (paid) { S.balance -= PRICE; S.spent += PRICE; } else { S.unpaid += PRICE; }
    S.reads += 1;
    S.log.unshift({ at: new Date().toISOString(), path: PATH, title: META.title, kind: META.kind,
                    topics: META.topics, cost: PRICE, paid: paid });
    S.log = S.log.slice(0, LOG_MAX);
    write(S);
    try { sessionStorage.setItem(SEEN, JSON.stringify(seen.concat([PATH]).slice(-300))); } catch (e) { /* ok */ }
    charged = paid ? 'paid' : 'unpaid';
  }());

  // ------------------------------------------------------------------ the badge, on every page
  function badge() {
    var a = document.createElement('a');
    a.className = 'meter-pill' + (S.paused ? ' paused' : S.balance <= 0 ? ' empty' : S.balance < CFG.start * 0.2 ? ' low' : '');
    a.href = ROOT + 'account/index.html';
    a.title = 'Your reading account: a simulated meter kept in this browser. Nothing is charged.';
    var what = charged === 'paid' ? 'this page ' + pence(PRICE) : charged === 'seen' ? 'already paid this visit'
             : charged === 'unpaid' ? 'unpaid ' + pence(PRICE) : charged === 'paused' ? 'meter paused' : 'this page is free';
    a.innerHTML = '<b>' + gbp(S.balance) + '</b><span>' + esc(what) + '</span>';
    document.body.appendChild(a);
  }

  function outOfCredit() {
    if (charged !== 'unpaid') return;
    var bar = document.createElement('div');
    bar.className = 'meter-bar';
    bar.innerHTML = '<b>Out of credit.</b> This page would cost ' + pence(PRICE) + '. It is shown anyway and noted as unpaid, '
      + 'because this meter is a simulation and never blocks reading. <a href="' + ROOT + 'account/top-up.html">Top up (simulated) &rarr;</a>'
      + ' <button type="button" aria-label="Dismiss">&times;</button>';
    bar.querySelector('button').addEventListener('click', function () { bar.remove(); });
    var main = document.querySelector('main') || document.body;
    main.insertBefore(bar, main.firstChild);
  }

  // ------------------------------------------------------------------ personalisation
  var GRAPHS = null;
  function graphs(cb) {
    if (GRAPHS) return cb(GRAPHS);
    fetch(ROOT + 'articles/graphs.json').then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
      .then(function (g) { GRAPHS = g; cb(g); }, function () { cb(null); });
  }
  function profile() {
    var w = {}, n = 0;
    S.log.forEach(function (e) { (e.topics || []).forEach(function (t) { w[t] = (w[t] || 0) + e.cost; n += e.cost; }); });
    return { weights: w, total: n };
  }
  function picks(g, k) {
    var p = profile(), read = {};
    S.log.forEach(function (e) { read[e.path] = 1; });
    return g.articles.filter(function (a) { return !read['/articles/' + a.slug + '.html'] && !read[location.pathname.replace(/[^/]*$/, '') + a.slug + '.html']; })
      .map(function (a) { var sc = 0; (a.topics || []).forEach(function (t) { sc += p.weights[t] || 0; }); return { a: a, s: sc }; })
      .filter(function (x) { return x.s > 0; })
      .sort(function (x, y) { return y.s - x.s || (y.a.date > x.a.date ? 1 : -1); })
      .slice(0, k).map(function (x) { return x.a; });
  }
  function topicLabel(g, id) { var t = (g.topics || []).filter(function (x) { return x.id === id; })[0]; return t ? t.label : id; }
  function pickHtml(g, list) {
    return '<div class="meter-picks">' + list.map(function (a) {
      return '<a class="meter-pick" href="' + ROOT + 'articles/' + esc(a.slug) + '.html"><span class="acard-date">' + esc(a.date)
        + ' &middot; ' + esc(topicLabel(g, a.topics[0])) + ' &middot; ' + pence(priceOf({ kind: 'article', date: a.date })) + '</span><b>'
        + esc(a.title) + '</b><span>' + esc(a.teaser) + '</span></a>';
    }).join('') + '</div>';
  }

  // the front page's "Picked for you" band: filled only once there is a history to pick from
  function forYou() {
    var el = document.getElementById('meter-foryou');
    if (!el || profile().total === 0) return;
    graphs(function (g) {
      if (!g) return;
      var list = picks(g, 4);
      if (!list.length) return;
      el.innerHTML = '<h2 class="fsect">Picked for you <a href="' + ROOT + 'account/index.html">from your reading, in this browser only &rarr;</a></h2>' + pickHtml(g, list);
      el.hidden = false;
    });
  }

  // ------------------------------------------------------------------ the account page
  function account() {
    var el = document.getElementById('meter-account');
    if (!el) return;
    function paint() {
      var p = profile(), unpaidLine = S.unpaid ? ' &middot; <b class="meter-red">' + gbp(S.unpaid) + ' unpaid</b>' : '';
      var rows = S.log.slice(0, 60).map(function (e) {
        return '<tr><td>' + esc(e.at.slice(0, 16).replace('T', ' ')) + '</td><td><a href="' + esc(e.path) + '">' + esc(e.title.replace(/, (sgit\.ai|SGit Newsroom)$/, '')) + '</a></td><td>'
          + esc(e.kind) + '</td><td>' + (e.paid ? pence(e.cost) : '<span class="meter-red">' + pence(e.cost) + ' unpaid</span>') + '</td></tr>';
      }).join('');
      var tops = S.topups.map(function (t) {
        return '<li><b>' + esc(t.ref) + '</b> ' + esc(t.at.slice(0, 16).replace('T', ' ')) + ': ' + gbp(t.credit) + ' of credit for ' + gbp(t.price) + ' (simulated, nothing charged)</li>';
      }).join('');
      var bars = Object.keys(p.weights).sort(function (a, b) { return p.weights[b] - p.weights[a]; }).map(function (t) {
        var pc = Math.round(100 * p.weights[t] / p.total);
        return '<div class="meter-topic"><span data-topic="' + esc(t) + '">' + esc(t) + '</span><i style="width:' + pc + '%"></i><em>' + pc + '%</em></div>';
      }).join('');
      el.innerHTML =
        '<div class="meter-card"><div><span class="small dim">Balance</span><b class="meter-big">' + gbp(S.balance) + '</b>'
        + '<span class="small dim">' + S.reads + ' page' + (S.reads === 1 ? '' : 's') + ' read &middot; ' + gbp(S.spent) + ' spent' + unpaidLine
        + (S.paused ? ' &middot; <b>meter paused</b>' : '') + '</span></div>'
        + '<div class="meter-actions"><a class="meter-btn primary" href="' + ROOT + 'account/top-up.html">Top up</a>'
        + '<button type="button" class="meter-btn" data-act="pause">' + (S.paused ? 'Resume the meter' : 'Pause the meter') + '</button>'
        + '<button type="button" class="meter-btn" data-act="export">Export as JSON</button>'
        + '<button type="button" class="meter-btn" data-act="reset">Start again with £' + (CFG.start / 100).toFixed(2) + '</button></div></div>'
        + (noStorage ? '<p class="meter-red">This browser is not keeping a balance (storage is blocked), so the meter starts again on every page.</p>' : '')
        + '<h2 id="foryou">Picked for you</h2><div id="meter-acc-picks"><p class="dim">' + (p.total ? 'Working it out from your history&hellip;'
          : 'Nothing yet. Read a few articles and this fills with unread ones from the topics you read most.') + '</p></div>'
        + '<h2 id="topics">What you have paid to read, by topic</h2>' + (bars || '<p class="dim">No articles read yet.</p>')
        + '<h2 id="history">History</h2>' + (rows ? '<div class="tablewrap"><table><tr><th>When</th><th>Page</th><th>Kind</th><th>Cost</th></tr>' + rows + '</table></div>'
          : '<p class="dim">No pages read yet in this browser.</p>')
        + '<h2 id="receipts">Top-ups</h2>' + (tops ? '<ul>' + tops + '</ul>' : '<p class="dim">None yet. You started with £' + (CFG.start / 100).toFixed(2) + ' of credit.</p>');
      [].forEach.call(el.querySelectorAll('[data-act]'), function (b) {
        b.addEventListener('click', function () {
          var act = b.getAttribute('data-act');
          if (act === 'pause') { S.paused = !S.paused; write(S); paint(); }
          if (act === 'reset' && confirm('Clear the balance, the history and the receipts kept in this browser, and start again with £' + (CFG.start / 100).toFixed(2) + '?')) {
            S = fresh(); write(S); try { sessionStorage.removeItem(SEEN); } catch (e) { /* ok */ } paint();
          }
          if (act === 'export') {
            var blob = new Blob([JSON.stringify(S, null, 2)], { type: 'application/json' }), a = document.createElement('a');
            a.href = URL.createObjectURL(blob); a.download = 'sgit-reading-account.json'; document.body.appendChild(a); a.click(); a.remove();
          }
        });
      });
      if (p.total) graphs(function (g) {
        var box = document.getElementById('meter-acc-picks');
        if (!g || !box) return;
        [].forEach.call(el.querySelectorAll('[data-topic]'), function (s) { s.textContent = topicLabel(g, s.getAttribute('data-topic')); });
        var list = picks(g, 6);
        box.innerHTML = list.length ? '<p class="small dim">Unread articles from the topics you have read most, newest first among equals. Worked out here, from the history below; nothing is sent anywhere.</p>' + pickHtml(g, list)
          : '<p class="dim">You have read everything in your topics. Impressive.</p>';
      });
    }
    paint();
  }

  // ------------------------------------------------------------------ the top-up page: a cart with every step but the payment
  function topup() {
    var el = document.getElementById('meter-topup');
    if (!el) return;
    var step = 'cart', receipt = null;
    function packOf(id) { return CFG.packs.filter(function (p) { return p.id === id; })[0]; }
    function totals() {
      var price = 0, credit = 0;
      S.cart.forEach(function (l) { var p = packOf(l.id); if (p) { price += p.price * l.qty; credit += (p.price + p.bonus) * l.qty; } });
      return { price: price, credit: credit };
    }
    function paint() {
      var t = totals(), h = '';
      if (step === 'done' && receipt) {
        h = '<div class="meter-card"><div><span class="small dim">Receipt ' + esc(receipt.ref) + '</span><b class="meter-big">' + gbp(receipt.credit) + ' added</b>'
          + '<span class="small dim">New balance ' + gbp(S.balance) + '. Simulated: nothing was charged and no payment details were asked for.</span></div>'
          + '<div class="meter-actions"><a class="meter-btn primary" href="' + ROOT + 'account/index.html">Your account</a><a class="meter-btn" href="' + ROOT + 'articles/index.html">Back to reading</a></div></div>';
        el.innerHTML = h; return;
      }
      h += '<div class="meter-packs">' + CFG.packs.map(function (p) {
        return '<div class="meter-pack"><b>' + gbp(p.price) + '</b><span>' + gbp(p.price + p.bonus) + ' of credit' + (p.bonus ? ', ' + gbp(p.bonus) + ' extra' : '') + '</span>'
          + '<span class="small dim">about ' + Math.floor((p.price + p.bonus) / CFG.prices.article_new) + ' new articles, or ' + Math.floor((p.price + p.bonus) / CFG.prices.page) + ' other pages</span>'
          + '<button type="button" class="meter-btn" data-add="' + esc(p.id) + '">Add to cart</button></div>';
      }).join('') + '</div>';
      h += '<h2 id="cart">Cart</h2>';
      if (!S.cart.length) h += '<p class="dim">Empty. Pick a pack above.</p>';
      else {
        h += '<div class="tablewrap"><table><tr><th>Pack</th><th>Qty</th><th>Credit</th><th>Price</th><th></th></tr>' + S.cart.map(function (l, i) {
          var p = packOf(l.id);
          return '<tr><td>' + gbp(p.price) + ' pack</td><td><button type="button" class="meter-q" data-q="' + i + ':-1">&minus;</button> ' + l.qty
            + ' <button type="button" class="meter-q" data-q="' + i + ':1">+</button></td><td>' + gbp((p.price + p.bonus) * l.qty) + '</td><td>' + gbp(p.price * l.qty)
            + '</td><td><button type="button" class="meter-q" data-q="' + i + ':0">remove</button></td></tr>';
        }).join('') + '<tr><th>Total</th><th></th><th>' + gbp(t.credit) + '</th><th>' + gbp(t.price) + '</th><th></th></tr></table></div>';
        if (step === 'cart') h += '<p><button type="button" class="meter-btn primary" data-go="review">Checkout &rarr;</button></p>';
        else h += '<div class="meter-card meter-review"><div><b>Review and pay</b><span class="small">' + gbp(t.credit) + ' of credit for ' + gbp(t.price)
          + '. Your balance becomes ' + gbp(S.balance + t.credit) + '.</span><span class="small dim">Payment: <b>simulated</b>. This is where a card form or a wallet button would go. '
          + 'None is shown, nothing is charged, and nothing leaves this browser.</span></div>'
          + '<div class="meter-actions"><button type="button" class="meter-btn primary" data-go="pay">Confirm (simulated)</button><button type="button" class="meter-btn" data-go="cart">Back to cart</button></div></div>';
      }
      el.innerHTML = h;
      [].forEach.call(el.querySelectorAll('[data-add]'), function (b) {
        b.addEventListener('click', function () {
          var id = b.getAttribute('data-add'), l = S.cart.filter(function (x) { return x.id === id; })[0];
          if (l) l.qty += 1; else S.cart.push({ id: id, qty: 1 });
          step = 'cart'; write(S); paint();
        });
      });
      [].forEach.call(el.querySelectorAll('[data-q]'), function (b) {
        b.addEventListener('click', function () {
          var q = b.getAttribute('data-q').split(':'), i = +q[0], d = +q[1];
          if (d === 0) S.cart.splice(i, 1); else { S.cart[i].qty += d; if (S.cart[i].qty <= 0) S.cart.splice(i, 1); }
          write(S); paint();
        });
      });
      [].forEach.call(el.querySelectorAll('[data-go]'), function (b) {
        b.addEventListener('click', function () {
          var go = b.getAttribute('data-go');
          if (go === 'pay') {
            var tt = totals();
            receipt = { ref: 'SIM-' + Date.now().toString(36).toUpperCase(), at: new Date().toISOString(), price: tt.price, credit: tt.credit,
                        lines: S.cart.map(function (l) { return { pack: l.id, qty: l.qty }; }) };
            S.balance += tt.credit; S.topups.unshift(receipt); S.cart = []; write(S); step = 'done';
          } else step = go;
          paint();
        });
      });
    }
    paint();
  }

  badge();
  outOfCredit();
  forYou();
  account();
  topup();
}());
