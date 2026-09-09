/* sgit.ai — decks and PDFs read live out of a vault, with the viewer owned by the site.
 *
 * The split this file exists to make:
 *
 *   FROM THE VAULT (data)     decks/decks.json, decks/<id>.js, decks/shell.html (its <style>
 *                             only), deck/img/*.jpg, deck/*.pdf — fetched as ciphertext with a
 *                             published READ key and decrypted in the browser.
 *   FROM THE SITE (viewer)    every control you can click: the deck tabs, the slide list, prev
 *                             and next, speaker notes, the PDF button, the deep links. None of
 *                             it comes out of the vault, so a vault cannot change this page's
 *                             behaviour — only what is displayed inside the frame.
 *
 * Vault content is never trusted with this origin. It reaches the page through exactly two
 * opaque-origin iframes, both `sandbox`ed and both carrying their own CSP:
 *
 *   parse frame    sandbox="allow-scripts", CSP default-src 'none'; script-src 'unsafe-inline'
 *                  'unsafe-eval'. decks/<id>.js is JavaScript — it builds its slides by calling
 *                  S.push(...) — so it has to RUN somewhere. It runs here, in a frame with no
 *                  origin and no network, and posts back a plain array. The site never evals it.
 *   render frame   sandbox="" — no allow-scripts at all — CSP default-src 'none'; img-src data:;
 *                  style-src 'unsafe-inline'. Slide markup is static by design, so scripting is
 *                  simply switched off, and the only thing that can load is a data: image the
 *                  host decrypted and put there itself. Nothing in a slide can phone home.
 *
 * The 1600x900 stage is the decks/v2 contract (decks/shell.html). The frame is that size in CSS
 * pixels and the PARENT scales the element, so the inner document is always exactly the viewport
 * the deck's own CSS was written against, at any width, with no reflow and no script inside.
 *
 * PDFs are downloads, not embeds, and that is a measured constraint rather than a preference:
 * Chrome refuses to render a PDF in a sandboxed frame at all — "Failed to load 'blob:...' as a
 * plugin, because the frame into which the plugin is loading is sandboxed" — so an inline PDF
 * would mean handing vault bytes this page's origin. The bytes are decrypted here, wrapped in a
 * blob, and handed to the browser's own download; the slides are the thing to read on the page.
 *
 * Usage:  SGVaultDeck.mount(el, { endpoint, vault_id, read_key })
 * Needs assets/vault-embed.js loaded first (for SGVaultEmbed.Reader).
 */
(function () {
  'use strict';

  var CSP_PARSE  = "default-src 'none'; script-src 'unsafe-inline' 'unsafe-eval'";
  var CSP_RENDER = "default-src 'none'; img-src data:; style-src 'unsafe-inline'; font-src data:";
  var STAGE_W    = 1600, STAGE_H = 900;

  function esc(s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }
  function bytesToB64(bytes) {
    var bin = '', CH = 0x8000;
    for (var i = 0; i < bytes.length; i += CH) bin += String.fromCharCode.apply(null, bytes.subarray(i, i + CH));
    return btoa(bin);
  }

  /* ---------------------------------------------------------------- the parse frame
   * decks/<id>.js is executable vault content. It runs here and nowhere else.
   * The source is handed over by postMessage rather than baked into the srcdoc, so a deck
   * containing the characters "</script>" cannot break out of the bootstrap that runs it.
   */
  function parseDeck(src) {
    return new Promise(function (resolve, reject) {
      var token = 'sgd' + Math.random().toString(36).slice(2);
      var boot =
        '<meta http-equiv="Content-Security-Policy" content="' + CSP_PARSE + '">' +
        '<script>(function(){"use strict";' +
        'window.addEventListener("message",function(ev){' +
        'var m=ev.data; if(!m||m.t!==' + JSON.stringify(token) + '||typeof m.src!=="string")return;' +
        // The decks/v2 globals, reimplemented here from the contract — img() emits a symbolic
        // data-img reference, never a path, which is what lets the host resolve it to a
        // decrypted data: URI without the slide ever naming a URL.
        // On window, not in this closure: a deck is a classic script that reads S, img and the
        // rest as globals, and (0,eval) runs in global scope. Declaring them locally is how the
        // first attempt failed, with "S is not defined".
        'window.S=[]; window.IMG={}; window.VERSION=""; window.DECK={}; window.DECKS=[];' +
        'window.img=function(name,style){return \'<div class="shot" style="\'+(style||\'\')+\'">\'+' +
        '\'<img alt="\'+name+\'" data-img="\'+name+\'"></div>\';};' +
        // The harvest runs INSIDE the same eval as the deck, appended to its source, because a
        // built deck declares `const S` and `const IMG` at its own top level — those are scoped
        // to the eval and are invisible from out here. A deck source declares neither and uses
        // the window globals above. One line covers both.
        'window.__sgd=function(S,IMG){parent.postMessage({t:' + JSON.stringify(token) + ',' +
        'slides:(S||[]).map(function(s){return {t:String(s&&s.t||""),' +
        'notes:String(s&&s.notes||""),html:String(s&&s.html||"")};}),imgs:IMG||{}},"*");};' +
        'var tail="\\n;try{window.__sgd(typeof S!==\\"undefined\\"?S:window.S,' +
        'typeof IMG!==\\"undefined\\"?IMG:window.IMG);}catch(e){}";' +
        'try{(0,eval)(m.src+tail);}catch(e){' +
        'parent.postMessage({t:m.t,err:String(e&&e.message||e)},"*");}' +
        '},false);' +
        'parent.postMessage({t:' + JSON.stringify(token) + ',ready:1},"*");' +
        '})();<' + '/script>';

      var f = document.createElement('iframe');
      f.setAttribute('sandbox', 'allow-scripts');
      f.setAttribute('referrerpolicy', 'no-referrer');
      f.setAttribute('aria-hidden', 'true');
      f.style.cssText = 'position:absolute;width:0;height:0;border:0;visibility:hidden';

      var done = false;
      function finish(fn, arg) {
        if (done) return; done = true;
        window.removeEventListener('message', onMsg);
        try { f.remove(); } catch (e) {}
        fn(arg);
      }
      function onMsg(ev) {
        if (ev.source !== f.contentWindow) return;
        var m = ev.data;
        if (!m || m.t !== token) return;
        if (m.ready) { f.contentWindow.postMessage({ t: token, src: src }, '*'); return; }
        if (m.slides) return finish(resolve, { slides: m.slides, imgs: m.imgs || {} });
        if (m.err) return finish(reject, new Error('deck source failed: ' + m.err));
      }
      window.addEventListener('message', onMsg, false);
      setTimeout(function () { finish(reject, new Error('deck source timed out')); }, 15000);

      document.body.appendChild(f);
      f.srcdoc = boot;
    });
  }

  /* ---------------------------------------------------------------- the viewer */
  function Deck(el, cfg) {
    this.el       = el;
    this.cfg      = cfg;
    this.imgCache = {};      // name -> data: URI, decrypted once per page
    this.slideCache = {};    // deck id -> slides
    this.deckId   = null;
    this.i        = 0;
    this.notesOn  = false;
  }

  Deck.prototype.status = function (msg, bad) {
    var n = this.el.querySelector('.vdk-status');
    if (n) { n.textContent = msg; n.className = 'vdk-status' + (bad ? ' bad' : ''); }
  };

  Deck.prototype.boot = async function () {
    var cfg = this.cfg;
    this.el.innerHTML = '<div class="vdk-boot">opening vault ' + esc(cfg.vault_id) +
                        ' — deriving ids, fetching ciphertext, decrypting…</div>';
    if (!(window.SGVaultEmbed && window.SGVaultEmbed.Reader))
      throw new Error('assets/vault-embed.js must load before assets/vault-deck.js');

    this.reader = await new window.SGVaultEmbed.Reader(cfg).init();
    await this.reader.open();

    // decks/v2 puts the manifest in one of two places depending on whether the vault published
    // its deck sources or only the built decks. Try both before giving up.
    var manifest = null, tried = [];
    var where = cfg.manifest ? [cfg.manifest] : ['decks/decks.json', 'decks.json'];
    for (var w = 0; w < where.length; w++) {
      try { manifest = JSON.parse(await this.reader.readText(where[w])); this.manifestPath = where[w]; break; }
      catch (e) { tried.push(where[w]); }
    }
    if (!manifest) throw new Error('no deck manifest — looked for ' + tried.join(' and '));
    this.decks = (manifest.decks || []).filter(function (d) { return d && d.id; });
    // A page dedicated to one deck names it, and the tab strip is then noise.
    if (cfg.only) {
      this.decks = this.decks.filter(function (d) { return d.id === cfg.only; });
      if (!this.decks.length) throw new Error('no deck "' + cfg.only + '" in the manifest');
    }
    if (!this.decks.length) throw new Error('no decks in the manifest');

    // The deck's own look, taken as CSS and never as script: the vault's script IS the vault's
    // viewer, and the vault's viewer is exactly what this file replaces. A vault that published
    // its sources has decks/shell.html; one that published only built decks carries the same
    // <style> inside each of them, so fall back to the first deck's file.
    this.deckCss = await this.styleFrom(['decks/shell.html', this.decks[0].file]);

    this.chrome();
    var want = this.fromHash();
    await this.showDeck(want.deck || this.decks[0].id, want.slide || 0);
    window.addEventListener('resize', this.fit.bind(this));
  };

  Deck.prototype.styleFrom = async function (paths) {
    for (var i = 0; i < paths.length; i++) {
      if (!paths[i]) continue;
      try {
        var m = (await this.reader.readText(paths[i])).match(/<style[^>]*>([\s\S]*?)<\/style>/i);
        if (m) return m[1];
      } catch (e) {}
    }
    return '';
  };

  /* Two published shapes, one frame. Prefer the SOURCE (decks/<id>.js — tens of KB, with the
   * screenshots fetched lazily and only the ones a slide uses). Fall back to the BUILT deck
   * (deck-<id>.html — hundreds of KB, because its screenshots are already base64 inside it),
   * truncated at the shell boundary so only the declarations and the S.push calls are run:
   * everything after that comment is the vault's own viewer touching a DOM that is not there.
   */
  Deck.prototype.loadSlides = async function (d) {
    try {
      var src = await this.reader.readText('decks/' + d.id + '.js');
      return await parseDeck(src);
    } catch (e) {
      if (!d.file) throw e;
    }
    var html   = await this.reader.readText(d.file);
    var blocks = [];
    (html.match(/<script[^>]*>[\s\S]*?<\/script>/gi) || []).forEach(function (b) {
      blocks.push(b.replace(/^<script[^>]*>/i, '').replace(/<\/script>$/i, ''));
    });
    if (!blocks.length) throw new Error('no script in ' + d.file);
    var script = blocks.sort(function (a, b) { return b.length - a.length; })[0];
    var cut    = script.indexOf('/* ---------- shell */');
    return await parseDeck(cut > 0 ? script.slice(0, cut) : script);
  };

  Deck.prototype.fromHash = function () {
    var h = String(location.hash || '').replace(/^#/, ''), out = {};
    h.split('&').forEach(function (kv) {
      var p = kv.split('='), k = p[0], v = decodeURIComponent(p[1] || '');
      if (k === 'deck') out.deck = v;
      if (k === 's') out.slide = Math.max(0, (parseInt(v, 10) || 1) - 1);
    });
    return out;
  };

  Deck.prototype.chrome = function () {
    var self = this;
    this.el.innerHTML =
      '<div class="vdk">' +
        '<div class="vdk-tabs" role="tablist"></div>' +
        '<div class="vdk-bar">' +
          '<span class="vdk-title"></span>' +
          '<span class="vdk-count"></span>' +
          '<span class="vdk-sp"></span>' +
          '<button class="vdk-b" data-a="prev" type="button">&larr; prev</button>' +
          '<button class="vdk-b" data-a="next" type="button">next &rarr;</button>' +
          '<button class="vdk-b" data-a="notes" type="button">notes</button>' +
          '<button class="vdk-b" data-a="focus" type="button" title="hide the slide list — for presenting and recording">focus</button>' +
          '<button class="vdk-b vdk-pdf" data-a="pdf" type="button">PDF &darr;</button>' +
        '</div>' +
        '<div class="vdk-body">' +
          '<div class="vdk-list" role="tablist"></div>' +
          '<div class="vdk-stagewrap"><div class="vdk-scaler"></div></div>' +
        '</div>' +
        '<div class="vdk-notes" hidden></div>' +
        '<p class="vdk-status"></p>' +
      '</div>';

    if (this.cfg.only) this.el.querySelector('.vdk-tabs').hidden = true;
    this.el.querySelector('.vdk-tabs').innerHTML = this.decks.map(function (d) {
      return '<button class="vdk-tab" type="button" data-deck="' + esc(d.id) + '">' +
             esc(d.short || d.title || d.id) +
             (d.level ? '<span class="vdk-lv">L' + esc(d.level) + '</span>' : '') + '</button>';
    }).join('');

    this.el.addEventListener('click', function (ev) {
      // Scoped to the tab strip on purpose: the mount element itself carries data-deck on a
      // single-deck page, so an unscoped closest() matched it for every click in the viewer
      // and swallowed prev, next, notes, focus and the PDF button.
      var t = ev.target.closest('.vdk-tab');
      if (t) return self.showDeck(t.getAttribute('data-deck'), 0);
      var s = ev.target.closest('[data-slide]');
      if (s) return self.show(parseInt(s.getAttribute('data-slide'), 10));
      var b = ev.target.closest('[data-a]');
      if (!b) return;
      var a = b.getAttribute('data-a');
      if (a === 'prev')  self.show(self.i - 1);
      if (a === 'next')  self.show(self.i + 1);
      if (a === 'notes') self.toggleNotes();
      if (a === 'focus') self.toggleFocus();
      if (a === 'pdf')   self.pdf();
    });
  };

  Deck.prototype.showDeck = async function (id, slide) {
    var self = this, d = this.decks.filter(function (x) { return x.id === id; })[0] || this.decks[0];
    this.deckId = d.id;
    this.meta   = d;
    this.el.querySelectorAll('.vdk-tab').forEach(function (t) {
      t.classList.toggle('on', t.getAttribute('data-deck') === d.id);
    });
    this.el.querySelector('.vdk-title').textContent = d.title || d.id;
    this.status('reading decks/' + d.id + '.js from the vault…');

    if (!this.slideCache[d.id]) {
      var got = await this.loadSlides(d);
      this.slideCache[d.id] = got.slides;
      // A built deck hands back its screenshots inline; adopt them so nothing is refetched.
      Object.keys(got.imgs || {}).forEach(function (n) {
        if (!this.imgCache[n]) this.imgCache[n] = 'data:image/jpeg;base64,' + got.imgs[n];
      }.bind(this));
    }
    this.slides = this.slideCache[d.id];

    this.el.querySelector('.vdk-list').innerHTML = this.slides.map(function (s, i) {
      return '<button class="vdk-it" type="button" data-slide="' + i + '">' +
             '<span class="vdk-n">' + String(i + 1).padStart(2, '0') + '</span>' +
             '<span>' + esc(s.t) + '</span></button>';
    }).join('');

    var pdf = d.pdf ? d.pdf.split('/').pop() : '';
    this.el.querySelector('.vdk-pdf').hidden = !d.pdf;
    if (pdf) this.el.querySelector('.vdk-pdf').title = 'download ' + pdf + ' from the vault';

    await this.show(slide || 0);
    self.status(this.slides.length + ' slides, read live from vault ' + this.cfg.vault_id +
                ' — the deck source ran in a sandboxed frame, the slide is rendered in another with scripting off.');
  };

  // Resolve the decks/v2 <img data-img="NAME"> placeholders to decrypted data: URIs.
  // Only the images this slide actually uses are fetched, and each is decrypted once.
  Deck.prototype.withImages = async function (html) {
    var names = [], re = /data-img="([A-Za-z0-9_.-]+)"/g, m;
    while ((m = re.exec(html))) if (names.indexOf(m[1]) === -1) names.push(m[1]);
    for (var i = 0; i < names.length; i++) {
      var n = names[i];
      if (!this.imgCache[n]) {
        try {
          var bytes = await this.reader.readBytes('deck/img/' + n + '.jpg');
          this.imgCache[n] = 'data:image/jpeg;base64,' + bytesToB64(bytes);
        } catch (e) { this.imgCache[n] = ''; }
      }
    }
    var cache = this.imgCache;
    return html.replace(/<img([^>]*?)data-img="([A-Za-z0-9_.-]+)"([^>]*)>/g, function (all, a, name, b) {
      var uri = cache[name];
      return uri ? '<img' + a + 'src="' + uri + '"' + b + '>'
                 : '<img' + a + 'alt="missing: ' + name + '"' + b + '>';
    });
  };

  Deck.prototype.show = async function (i) {
    if (!this.slides || !this.slides.length) return;
    this.i = Math.max(0, Math.min(this.slides.length - 1, i));
    var s = this.slides[this.i];

    this.el.querySelectorAll('.vdk-it').forEach(function (b, n) {
      b.classList.toggle('on', n === this.i);
    }.bind(this));
    this.el.querySelector('.vdk-count').textContent = (this.i + 1) + ' / ' + this.slides.length;

    var body   = await this.withImages(s.html);
    var ground = this.cfg.slide_bg || '#fff';
    var doc =
      '<meta http-equiv="Content-Security-Policy" content="' + CSP_RENDER + '">' +
      '<style>' + this.deckCss + '</style>' +
      // The slide ground is white by default. The deck CSS above ships a cream --paper for the
      // vault's own full-screen viewer; on a site page a white slide sits correctly on the page.
      '<style>html,body{margin:0;overflow:hidden;background:' + ground + '}' +
      '#stage{position:relative;width:' + STAGE_W + 'px;height:' + STAGE_H + 'px;overflow:hidden;' +
      'background:' + ground + '}.slide{display:flex}</style>' +
      '<div id="stage"><section class="slide on">' + body + '</section></div>';

    var scaler = this.el.querySelector('.vdk-scaler');
    var frame  = scaler.querySelector('iframe');
    if (!frame) {
      frame = document.createElement('iframe');
      // No allow-scripts: slide markup is static, so scripting is simply off. Opaque origin,
      // no referrer, and the CSP above means the only loadable thing is a data: image.
      frame.setAttribute('sandbox', '');
      frame.setAttribute('referrerpolicy', 'no-referrer');
      frame.setAttribute('title', 'slide');
      frame.width = STAGE_W; frame.height = STAGE_H;
      frame.style.cssText = 'width:' + STAGE_W + 'px;height:' + STAGE_H + 'px;border:0;display:block;' +
                            'transform-origin:top left';
      scaler.appendChild(frame);
    }
    frame.srcdoc = doc;

    var notes = this.el.querySelector('.vdk-notes');
    notes.textContent = s.notes || '(no speaker notes on this slide)';
    this.fit();
    this.hash();
  };

  // The frame is 1600x900 in its own CSS pixels — exactly the viewport the deck's CSS was
  // written against — and the ELEMENT is scaled to the column. No reflow, no script inside.
  Deck.prototype.fit = function () {
    var wrap = this.el.querySelector('.vdk-stagewrap'), scaler = this.el.querySelector('.vdk-scaler');
    if (!wrap || !scaler) return;
    var frame = scaler.querySelector('iframe');
    if (!frame) return;
    var w = wrap.clientWidth || STAGE_W, k = w / STAGE_W, h = STAGE_H * k;
    frame.style.transform = 'scale(' + k + ')';
    scaler.style.height = h + 'px';
    // Keep the slide list the same height as the stage beside it, so a long deck scrolls
    // instead of stretching the row and leaving a dead strip under the slide.
    var list = this.el.querySelector('.vdk-list');
    if (list && w > 760 && !this.focusOn) list.style.maxHeight = h + 'px';
  };

  Deck.prototype.toggleNotes = function () {
    this.notesOn = !this.notesOn;
    this.el.querySelector('.vdk-notes').hidden = !this.notesOn;
    this.el.querySelectorAll('[data-a="notes"]').forEach(function (b) { b.classList.toggle('on', this.notesOn); }.bind(this));
  };

  // Focus drops the slide list so the stage takes the full width — for presenting, and for
  // recording a screen capture where the chrome is just noise. The stage is re-fitted after,
  // because the column it scales against has just changed size.
  Deck.prototype.toggleFocus = function () {
    this.focusOn = !this.focusOn;
    this.el.querySelector('.vdk').classList.toggle('focus', this.focusOn);
    this.el.querySelectorAll('[data-a="focus"]').forEach(function (b) {
      b.classList.toggle('on', this.focusOn);
    }.bind(this));
    this.fit();
  };

  Deck.prototype.hash = function () {
    try {
      history.replaceState(null, '', '#deck=' + encodeURIComponent(this.deckId) + '&s=' + (this.i + 1));
    } catch (e) {}
  };

  // Decrypt the PDF here, in the page, and hand the bytes to the browser's own download.
  // Not an iframe: Chrome will not render a PDF inside a sandboxed frame, and rendering it
  // outside one would give vault bytes this origin.
  Deck.prototype.pdf = async function () {
    var d = this.meta;
    if (!d || !d.pdf) return;
    var name = d.pdf.split('/').pop();
    this.status('decrypting ' + name + '…');
    try {
      var bytes = await this.reader.readBytes(d.pdf);
      var url   = URL.createObjectURL(new Blob([bytes], { type: 'application/pdf' }));
      var a     = document.createElement('a');
      a.href = url; a.download = name; a.rel = 'noopener';
      document.body.appendChild(a); a.click(); a.remove();
      setTimeout(function () { URL.revokeObjectURL(url); }, 30000);
      this.status(name + ' — ' + (bytes.length / 1048576).toFixed(1) +
                  ' MB decrypted in your browser and handed to your downloads.');
    } catch (e) {
      this.status('could not read ' + d.pdf + ': ' + (e && e.message || e), true);
    }
  };

  async function mount(el, cfg) {
    var deck = new Deck(el, cfg);
    try { await deck.boot(); }
    catch (e) {
      el.innerHTML = '<div class="vdk-boot bad">could not open the decks in vault ' +
                     esc(cfg.vault_id) + ': ' + esc(e && e.message || e) + '</div>';
      throw e;
    }
    return deck;
  }

  window.SGVaultDeck = { mount: mount };

  // Declarative mount, matching the other embeds on this site.
  document.querySelectorAll('.sgv-deck').forEach(function (el) {
    mount(el, {
      endpoint: el.getAttribute('data-endpoint') || 'https://dev.send.sgraph.ai',
      vault_id: el.getAttribute('data-vault'),
      read_key: el.getAttribute('data-readkey'),
      // No default here: leaving it unset is what lets boot() try both published shapes.
      manifest: el.getAttribute('data-manifest') || undefined,
      only:     el.getAttribute('data-deck') || undefined
    }).catch(function () {});
  });
})();
