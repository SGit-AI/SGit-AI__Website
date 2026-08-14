/* sgit.ai — live vault docs reader.
 *
 * Reads an encrypted SG/Send vault directly from the browser using a published
 * READ key: derive the ref file id (HMAC-SHA256), GET the ciphertext over CORS,
 * decrypt with AES-256-GCM (Web Crypto), walk commit → tree → blobs. No server
 * side, no build step: publishing is `sgit push`, and the next page load has it.
 *
 * Three cache tiers, mirroring what the object model allows:
 *   mem    — decrypted objects for this page session
 *   Cache  — ciphertext for obj-cas-imm-* (content-addressed ⇒ immutable ⇒ forever)
 *   none   — the ref (mutable HEAD pointer) is always refetched; that is how a
 *            new commit is noticed at all.
 */
(function () {
  'use strict';

  var enc = new TextEncoder();
  var dec = new TextDecoder();

  function hexToBytes(hex) {
    var out = new Uint8Array(hex.length / 2);
    for (var i = 0; i < out.length; i++) out[i] = parseInt(hex.substr(i * 2, 2), 16);
    return out;
  }
  function bytesToHex(b) {
    var s = ''; for (var i = 0; i < b.length; i++) s += b[i].toString(16).padStart(2, '0'); return s;
  }
  function b64ToBytes(b64) {
    var bin = atob(b64), out = new Uint8Array(bin.length);
    for (var i = 0; i < bin.length; i++) out[i] = bin.charCodeAt(i);
    return out;
  }

  // ---------------------------------------------------------------- reader
  function VaultReader(cfg) {
    this.endpoint = cfg.endpoint.replace(/\/$/, '');
    this.vaultId  = cfg.vault_id;
    this.readKey  = cfg.read_key;
    this.mem      = new Map();
    this.stats    = { fetch: 0, cacheHit: 0, memHit: 0, bytesNet: 0, bytesCache: 0, decrypts: 0, ms: 0,
                      oldestCache: null, newestCache: null };
    this.log      = [];
  }

  VaultReader.prototype.init = async function () {
    if (!(window.crypto && window.crypto.subtle)) {
      throw new Error('Web Crypto is unavailable — this page must be served over HTTPS (or localhost). ' +
                      'Decryption happens in your browser, so a secure context is required.');
    }
    var raw = hexToBytes(this.readKey);
    this.aesKey  = await crypto.subtle.importKey('raw', raw, 'AES-GCM', false, ['decrypt']);
    this.hmacKey = await crypto.subtle.importKey('raw', raw, { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']);
    try { this.cache = await caches.open('sgit-vault-docs-v1'); } catch (e) { this.cache = null; }
    return this;
  };

  VaultReader.prototype.fileId = async function (domain) {
    var mac = await crypto.subtle.sign('HMAC', this.hmacKey, enc.encode(domain));
    return bytesToHex(new Uint8Array(mac)).slice(0, 12);
  };
  VaultReader.prototype.refFileId = async function () {
    return 'ref-pid-muw-' + await this.fileId('sg-vault-v1:file-id:ref:' + this.vaultId);
  };

  VaultReader.prototype.decrypt = async function (bytes) {
    var iv = bytes.slice(0, 12), body = bytes.slice(12);
    var pt = await crypto.subtle.decrypt({ name: 'AES-GCM', iv: iv, tagLength: 128 }, this.aesKey, body);
    this.stats.decrypts++;
    return new Uint8Array(pt);
  };
  VaultReader.prototype.decryptText   = async function (bytes) { return dec.decode(await this.decrypt(bytes)); };
  VaultReader.prototype.decryptB64    = async function (b64)   { return b64 ? this.decryptText(b64ToBytes(b64)) : ''; };

  // fetch raw ciphertext for a vault path, with the cache policy the id implies
  VaultReader.prototype.raw = async function (vaultPath) {
    var url        = this.endpoint + '/api/vault/read/' + this.vaultId + '/' + vaultPath;
    var immutable  = vaultPath.indexOf('-imm-') !== -1;
    var t0         = performance.now();
    var entry      = { path: vaultPath.split('/').pop(), src: 'net', bytes: 0, ms: 0 };

    if (immutable && this.cache) {
      var hit = await this.cache.match(url);
      if (hit) {
        var stamp = parseInt(hit.headers.get('x-sg-cached-at') || '0', 10) || null;
        var bufC  = new Uint8Array(await hit.arrayBuffer());
        this.stats.cacheHit++; this.stats.bytesCache += bufC.length;
        if (stamp) {
          this.stats.oldestCache = this.stats.oldestCache ? Math.min(this.stats.oldestCache, stamp) : stamp;
          this.stats.newestCache = this.stats.newestCache ? Math.max(this.stats.newestCache, stamp) : stamp;
        }
        entry.src = 'cache'; entry.bytes = bufC.length; entry.ms = performance.now() - t0; entry.cachedAt = stamp;
        this.log.push(entry); this.stats.ms += entry.ms;
        return bufC;
      }
    }

    var resp = await fetch(url, { cache: immutable ? 'default' : 'no-store' });
    if (!resp.ok) throw new Error('HTTP ' + resp.status + ' for ' + vaultPath);
    var buf = new Uint8Array(await resp.arrayBuffer());
    if (immutable && this.cache) {
      try {
        await this.cache.put(url, new Response(buf, { headers: { 'x-sg-cached-at': String(Date.now()) } }));
        entry.cachedAt = Date.now();          // stored now, on this very request
      } catch (e) {}
    }

    this.stats.fetch++; this.stats.bytesNet += buf.length;
    entry.bytes = buf.length; entry.ms = performance.now() - t0;
    this.log.push(entry); this.stats.ms += entry.ms;
    return buf;
  };

  // a decrypted object, memoised for the session
  VaultReader.prototype.object = async function (objId) {
    if (this.mem.has(objId)) { this.stats.memHit++; return this.mem.get(objId); }
    var bytes = await this.raw('bare/data/' + objId);
    var plain = await this.decrypt(bytes);
    this.mem.set(objId, plain);
    return plain;
  };
  VaultReader.prototype.objectJson = async function (objId) {
    return JSON.parse(dec.decode(await this.object(objId)));
  };

  // open: ref → commit (+ decrypted message). Always refetches the ref.
  VaultReader.prototype.open = async function () {
    var refBytes = await this.raw('bare/refs/' + await this.refFileId());
    var ref      = JSON.parse(await this.decryptText(refBytes));
    var commit   = await this.objectJson(ref.commit_id);
    this.head    = ref.commit_id;
    this.commit  = commit;
    this.message = await this.decryptB64(commit.message_enc);
    return { commitId: ref.commit_id, commit: commit, message: this.message };
  };

  // walk the tree into a flat path → entry map
  VaultReader.prototype.tree = async function (treeId, prefix, out) {
    out = out || {}; prefix = prefix || '';
    var tree = await this.objectJson(treeId);
    for (var i = 0; i < (tree.entries || []).length; i++) {
      var e    = tree.entries[i];
      var name = await this.decryptB64(e.name_enc);
      var full = prefix ? prefix + '/' + name : name;
      if (e.tree_id) await this.tree(e.tree_id, full, out);
      else out[full] = { blob_id: e.blob_id, size: parseInt(await this.decryptB64(e.size_enc) || '0', 10) };
    }
    return out;
  };
  VaultReader.prototype.files = async function () {
    if (!this.commit) await this.open();
    if (!this._files) this._files = await this.tree(this.commit.tree_id);
    return this._files;
  };
  VaultReader.prototype.readText = async function (path) {
    var files = await this.files();
    if (!files[path]) throw new Error('not in vault: ' + path);
    return dec.decode(await this.object(files[path].blob_id));
  };
  VaultReader.prototype.resetStats = function () {         // clear the view, keep the caches
    this.log.length = 0;
    this.stats = { fetch: 0, cacheHit: 0, memHit: 0, bytesNet: 0, bytesCache: 0, decrypts: 0, ms: 0,
                   oldestCache: null, newestCache: null };
  };
  VaultReader.prototype.clearCaches = async function () {
    this.mem.clear(); this._files = null;
    if (this.cache) { try { await caches.delete('sgit-vault-docs-v1'); this.cache = await caches.open('sgit-vault-docs-v1'); } catch (e) {} }
  };

  // ------------------------------------------------------------- markdown
  function esc(s) { return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }

  function inline(s) {
    s = esc(s);
    s = s.replace(/`([^`]+)`/g, function (_, c) { return '<code>' + c + '</code>'; });
    s = s.replace(/\*\*([^*]+)\*\*/g, '<b>$1</b>');
    s = s.replace(/(^|[\s(])\*([^*]+)\*/g, '$1<em>$2</em>');
    s = s.replace(/\[([^\]]+)\]\(([^)]+)\)/g, function (_, text, href) {
      if (/^https?:/.test(href)) return '<a href="' + href + '" target="_blank" rel="noopener">' + text + '</a>';
      return '<a href="#" data-vault-link="' + href + '">' + text + '</a>';
    });
    return s;
  }

  function markdown(src, basePath) {
    var lines = src.split('\n'), out = [], i = 0;
    function resolve(href) {                                  // vault-relative → absolute vault path
      if (/^https?:|^#/.test(href)) return href;
      var base = basePath.indexOf('/') === -1 ? [] : basePath.split('/').slice(0, -1);
      var parts = href.split('/');
      for (var k = 0; k < parts.length; k++) {
        if (parts[k] === '..') base.pop();
        else if (parts[k] !== '.') base.push(parts[k]);
      }
      return base.join('/');
    }
    while (i < lines.length) {
      var ln = lines[i];
      if (/^```/.test(ln)) {                                   // fenced code
        var lang = ln.slice(3).trim(), buf = [];
        i++;
        while (i < lines.length && !/^```/.test(lines[i])) buf.push(lines[i++]);
        i++;
        out.push('<pre class="md-code"' + (lang ? ' data-lang="' + esc(lang) + '"' : '') + '>' + esc(buf.join('\n')) + '</pre>');
        continue;
      }
      if (/^\s*$/.test(ln)) { i++; continue; }
      if (/^#{1,6}\s/.test(ln)) {                              // heading
        var lvl = ln.match(/^#+/)[0].length;
        var txt = ln.replace(/^#+\s*/, '');
        var id  = txt.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
        out.push('<h' + lvl + ' id="' + id + '">' + inline(txt) + '</h' + lvl + '>');
        i++; continue;
      }
      if (/^\|/.test(ln) && i + 1 < lines.length && /^\|[\s:|-]+\|?\s*$/.test(lines[i + 1])) {  // table
        var head = ln.split('|').slice(1, -1).map(function (c) { return c.trim(); });
        i += 2;
        var rows = [];
        while (i < lines.length && /^\|/.test(lines[i])) {
          rows.push(lines[i].split('|').slice(1, -1).map(function (c) { return c.trim(); }));
          i++;
        }
        var t = '<div class="md-tablewrap"><table><tr>';
        head.forEach(function (h) { t += '<th>' + inline(h) + '</th>'; });
        t += '</tr>';
        rows.forEach(function (r) {
          t += '<tr>'; r.forEach(function (c) { t += '<td>' + inline(c) + '</td>'; }); t += '</tr>';
        });
        out.push(t + '</table></div>');
        continue;
      }
      if (/^[-*]\s|^\d+\.\s/.test(ln)) {                       // list
        var ordered = /^\d+\.\s/.test(ln), items = [];
        while (i < lines.length && /^([-*]\s|\d+\.\s)/.test(lines[i])) {
          items.push(lines[i].replace(/^([-*]\s|\d+\.\s)/, '')); i++;
        }
        var tag = ordered ? 'ol' : 'ul';
        out.push('<' + tag + '>' + items.map(function (it) { return '<li>' + inline(it) + '</li>'; }).join('') + '</' + tag + '>');
        continue;
      }
      if (/^>\s?/.test(ln)) {                                  // blockquote
        var q = [];
        while (i < lines.length && /^>\s?/.test(lines[i])) { q.push(lines[i].replace(/^>\s?/, '')); i++; }
        out.push('<blockquote>' + inline(q.join(' ')) + '</blockquote>');
        continue;
      }
      if (/^(---|\*\*\*)\s*$/.test(ln)) { out.push('<hr>'); i++; continue; }
      var para = [];                                            // paragraph
      while (i < lines.length && !/^\s*$/.test(lines[i]) && !/^(#{1,6}\s|```|\||[-*]\s|\d+\.\s|>|---)/.test(lines[i])) {
        para.push(lines[i]); i++;
      }
      if (para.length) out.push('<p>' + inline(para.join(' ')) + '</p>');
      else i++;
    }
    var html = out.join('\n');
    // rewrite vault-relative links to resolved vault paths
    return html.replace(/data-vault-link="([^"]+)"/g, function (_, href) {
      return 'data-vault-link="' + resolve(href) + '"';
    });
  }

  window.SGVaultDocs = { VaultReader: VaultReader, markdown: markdown, bytesToHex: bytesToHex };
})();

/* ----------------------------------------------------------------- app
 * Mounts the live-docs browser: nav from the vault tree, hash routing,
 * and a debug panel showing exactly which encrypted objects were fetched,
 * what came from cache, and which vault commit you are looking at.
 */
(function () {
  'use strict';
  var D = window.SGVaultDocs;

  function el(id) { return document.getElementById(id); }
  function fmtBytes(n) { return n < 1024 ? n + ' B' : (n / 1024).toFixed(1) + ' KB'; }
  function ago(ms) {
    if (!ms) return '';
    var s = Math.round((Date.now() - ms) / 1000);
    if (s < 5)    return 'just now';
    if (s < 60)   return s + 's ago';
    if (s < 3600) return Math.round(s / 60) + 'm ago';
    if (s < 86400) return Math.round(s / 3600) + 'h ago';
    return Math.round(s / 86400) + 'd ago';
  }
  function stamp(ms) {
    return ms ? new Date(ms).toISOString().replace('T', ' ').slice(0, 19) + ' UTC' : '—';
  }

  function title(path) {
    var name = path.split('/').pop().replace(/\.md$/, '');
    if (name === 'README' || name === 'index') {
      var parts = path.split('/'); name = parts[parts.length - 2] || name;
    }
    return name.replace(/^\d+[-_]/, '').replace(/[-_]/g, ' ')
               .replace(/\b\w/g, function (c) { return c.toUpperCase(); });
  }

  D.mount = async function (cfg) {
    var body = el('vdocs-body'), nav = el('vdocs-nav');
    var reader;
    try {
      reader = await new D.VaultReader(cfg).init();
      await reader.open();
    } catch (e) {
      body.innerHTML = '<div class="warnbox"><b>Could not open the vault.</b> ' +
        'This page reads its content live from an SG/Send server; if that server is ' +
        'unreachable from your network the docs cannot render. <br><small>' +
        String(e).replace(/</g, '&lt;') + '</small></div>';
      return;
    }

    var files = await reader.files();
    var docs  = Object.keys(files).filter(function (p) { return /\.md$/.test(p); }).sort();

    // ---- nav, grouped by top-level folder
    var groups = {};
    docs.forEach(function (p) {
      var g = p.indexOf('/') === -1 ? '' : p.split('/')[0];
      (groups[g] = groups[g] || []).push(p);
    });
    var html = '';
    Object.keys(groups).sort().forEach(function (g) {
      if (g) html += '<div class="vdocs-group">' + g.replace(/[-_]/g, ' ') + '</div>';
      groups[g].forEach(function (p) {
        html += '<a href="#' + p + '" data-path="' + p + '">' + title(p) + '</a>';
      });
    });
    nav.innerHTML = html;

    // ---- debug panel
    function paintDebug() {
      var s = reader.stats;
      el('vdbg-body').innerHTML =
        '<div class="vdbg-grid">' +
          row('endpoint', cfg.endpoint.replace(/^https?:\/\//, '')) +
          row('vault id', cfg.vault_id) +
          row('read key', cfg.read_key.slice(0, 12) + '… (public, read-only)') +
          row('HEAD', reader.head) +
          row('commit msg', reader.message || '—') +
          row('committed', new Date(reader.commit.timestamp_ms).toISOString().replace('T', ' ').slice(0, 19) + ' UTC') +
          row('files', String(Object.keys(files).length)) +
        '</div>' +
        '<div class="vdbg-h">cache</div>' +
        '<div class="vdbg-grid">' +
          row('network fetches', String(s.fetch) + '  (' + fmtBytes(s.bytesNet) + ')') +
          row('cache hits', String(s.cacheHit) + '  (' + fmtBytes(s.bytesCache) + ')') +
          row('memory hits', String(s.memHit)) +
          row('decryptions', String(s.decrypts)) +
          row('transfer time', s.ms.toFixed(0) + ' ms') +
          row('cached locally', s.newestCache
                ? stamp(s.newestCache) + '  (' + ago(s.newestCache) + ')'
                : (s.fetch ? 'this page load — ' + stamp(Date.now()) : '—')) +
          (s.oldestCache && s.oldestCache !== s.newestCache
                ? row('oldest entry', stamp(s.oldestCache) + '  (' + ago(s.oldestCache) + ')') : '') +
        '</div>' +
        '<div class="vdbg-h">requests <span class="vdbg-dim">(newest last)</span></div>' +
        '<div class="vdbg-log">' + (reader.log.length ? reader.log.slice(-60).map(function (e) {
          return '<div><span class="' + (e.src === 'cache' ? 'g' : 'cy') + '">' +
                 (e.src === 'cache' ? 'CACHE' : ' NET ') + '</span> ' +
                 e.path.slice(0, 24).padEnd(24) + ' ' +
                 String(e.bytes).padStart(6) + 'B ' + String(e.ms.toFixed(0)).padStart(4) + 'ms' +
                 (e.cachedAt ? '  <span class="dimc">' + ago(e.cachedAt) + '</span>' : '') +
                 '</div>';
        }).join('') : '<span class="vdbg-dim">list cleared — navigate to a page to see its objects</span>') + '</div>';
      function row(k, v) { return '<div class="k">' + k + '</div><div class="v">' + String(v).replace(/</g, '&lt;') + '</div>'; }
    }

    // ---- routing
    async function show(path) {
      if (!files[path]) path = docs[0];
      nav.querySelectorAll('a').forEach(function (a) {
        a.classList.toggle('here', a.getAttribute('data-path') === path);
      });
      body.innerHTML = '<p class="dim">decrypting ' + path + ' …</p>';
      try {
        var md = await reader.readText(path);
        body.innerHTML = '<div class="vdocs-src">' + path +
          ' · <span class="dim">decrypted in your browser from commit ' + reader.head + '</span></div>' +
          D.markdown(md, path);
        body.querySelectorAll('[data-vault-link]').forEach(function (a) {
          a.addEventListener('click', function (ev) {
            ev.preventDefault();
            var t = a.getAttribute('data-vault-link');
            if (files[t]) location.hash = t; else window.open(t, '_blank');
          });
        });
        var anchor = document.querySelector('.vdocs');
        if (anchor) {
          var navH = (document.querySelector('nav.site') || {}).offsetHeight || 56;
          var y    = anchor.getBoundingClientRect().top + window.scrollY - navH - 8;
          if (Math.abs(window.scrollY - y) > 4) window.scrollTo({ top: Math.max(0, y), behavior: 'smooth' });
        }
      } catch (e) {
        body.innerHTML = '<div class="warnbox">Could not read <code>' + path + '</code>: ' + String(e) + '</div>';
      }
      paintDebug();
    }

    window.addEventListener('hashchange', function () { show(decodeURIComponent(location.hash.slice(1))); });

    // panel open/closed survives navigation and reloads
    function setPanel(open) {
      el('vdbg').classList.toggle('open', open);
      try { localStorage.setItem('sgit-vdbg-open', open ? '1' : '0'); } catch (e) {}
    }
    var wasOpen = false;
    try { wasOpen = localStorage.getItem('sgit-vdbg-open') === '1'; } catch (e) {}
    if (wasOpen) el('vdbg').classList.add('open');

    el('vdbg-toggle').addEventListener('click', function () { setPanel(!el('vdbg').classList.contains('open')); });
    el('vdbg-close').addEventListener('click', function () { setPanel(false); });
    el('vdbg-reset').addEventListener('click', function () {
      reader.resetStats();
      el('vdbg-note').textContent = 'list cleared — the caches are untouched; load a page to see just its objects';
      paintDebug();
    });
    el('vdbg-clear').addEventListener('click', async function () {
      await reader.clearCaches(); reader.log.length = 0;
      reader.stats = { fetch: 0, cacheHit: 0, memHit: 0, bytesNet: 0, bytesCache: 0, decrypts: 0, ms: 0 };
      await reader.open(); files = await reader.files();
      show(decodeURIComponent(location.hash.slice(1)));
    });
    el('vdbg-refresh').addEventListener('click', async function () {
      var before = reader.head;
      await reader.open();
      if (reader.head !== before) { reader._files = null; files = await reader.files(); }
      el('vdbg-note').textContent = reader.head === before
        ? 'up to date — HEAD unchanged' : 'new commit picked up: ' + reader.head;
      show(decodeURIComponent(location.hash.slice(1)));
    });

    await show(decodeURIComponent(location.hash.slice(1)) || docs[0]);
  };
})();
