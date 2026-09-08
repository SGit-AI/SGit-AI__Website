/* sgit.ai — the site chat pane: a model that can CALL TOOLS over this site's own content.
 *
 * Three tiers, same shape as the network chooser (assets/network-chat.js):
 *
 *   Tier 0  no key    — the tools run directly. Plain text searches the site; slash commands
 *                       (/vaults, /sites, /updates, /board, /read PATH, /help) call one tool each.
 *                       Instant, free, private, works offline once the index is loaded.
 *   Tier 1  BYOK      — an OpenRouter key in localStorage. The model is given the tools below as
 *                       OpenAI-style function definitions and calls them; every call is executed
 *                       HERE, in the page, over the build-emitted index (assets/site-index.json)
 *                       and the .md twin of any page. The model never sees anything it did not
 *                       ask a tool for, and the pane shows every call it made.
 *   Tier 2  sg.llm    — inside a vault the host holds the key below the permission floor. Not
 *                       wired yet: the bridge's tool-calling contract is unconfirmed (board T11).
 *
 * The key lives in this page's origin and goes to openrouter.ai and nowhere else — never to
 * sgit.ai, which has no server to send it to. The pane says so rather than burying it.
 *
 * Loaded by the BOOT block after site.js, through the same vfs-or-fetch loader, so it works on a
 * blob: origin. Never referenced by a script src — the validator refuses those, correctly.
 */
(function () {
  if (window.__sgitChatLoaded) return;
  window.__sgitChatLoaded = true;
  if (!document.querySelector('nav.site')) return;           // not a site page

  var B = window.__sgitBoot || {};
  var LS_KEY = 'sgit.chat.orkey', LS_MODEL = 'sgit.chat.ormodel', LS_OPEN = 'sgit.chat.open';
  var DEFAULT_MODEL = 'openai/gpt-4o-mini';
  var MAX_ROUNDS = 6, PAGE_CHARS = 6000, HITS = 8;

  // ---------------------------------------------------------------- where is the root?
  var ROOT = '';
  var brand = document.querySelector('nav.site .brand');
  if (brand) ROOT = (brand.getAttribute('href') || '').replace(/index\.html$/, '');
  var HERE = (function () {
    var c = document.querySelector('link[rel="canonical"]');
    var u = c ? c.getAttribute('href') : location.pathname;
    return (u || '').replace(/^https?:\/\/[^/]+\//, '').replace(/^\//, '') || 'index.html';
  }());

  function grab(path) {
    if (B.grab) return B.grab(ROOT + path);
    return fetch(ROOT + path).then(function (r) { return r.ok ? r.text() : null; }).catch(function () { return null; });
  }

  var IDX = null;
  function loadIndex() {
    if (IDX) return Promise.resolve(IDX);
    return grab('assets/site-index.json').then(function (t) {
      IDX = t ? JSON.parse(t) : null;
      if (!IDX) IDX = { pages: [], vaults: [], sites: [], updates: [], articles: [], roles: [], issues: [] };
      return IDX;
    });
  }

  // ---------------------------------------------------------------- scoring (shared with the chooser)
  var STOP = ('i we you a an the to for of and or my our is are do does how what which where when '
    + 'who why can could should would will with without on in at by from as it its this that these '
    + 'those be been being have has had about into over than then there here not no yes if so '
    + 'me us them they their your his her page site sgit vault vaults').split(' ');
  function terms(s) {
    return (s || '').toLowerCase().replace(/[^a-z0-9\s.-]/g, ' ').split(/\s+/)
      .filter(function (w) { return w.length > 2 && STOP.indexOf(w) < 0; });
  }
  function scoreText(qt, strong, weak) {
    var n = 0, hits = [];
    for (var i = 0; i < qt.length; i++) {
      var w = qt[i];
      if (strong.indexOf(w) >= 0) { n += 3; hits.push(w); }
      else if (weak.indexOf(w) >= 0) { n += 1; hits.push(w); }
    }
    return { n: n, hits: hits };
  }

  // ---------------------------------------------------------------- the tools
  var TOOLS = {
    search_site: {
      desc: 'Search everything on sgit.ai — pages, published vaults, sibling sites, articles, release notes, team roles and board cards — by keywords. Returns up to 8 results with a path you can pass to read_page. Use this first for any question about what the site has.',
      params: { query: { type: 'string', description: 'keywords' } }, required: ['query'],
      run: function (a) {
        return loadIndex().then(function (ix) {
          var qt = terms(a.query), out = [];
          ix.pages.forEach(function (p) {
            var s = scoreText(qt, (p.title + ' ' + p.section).toLowerCase(), (p.desc || '').toLowerCase());
            if (s.n) out.push({ kind: 'page', title: p.title, path: p.path, summary: p.desc, score: s.n, matched: s.hits });
          });
          ix.vaults.forEach(function (v) {
            var s = scoreText(qt, (v.name + ' ' + v.category + ' ' + v.vault_id).toLowerCase(), (v.what || '').toLowerCase());
            if (s.n) out.push({ kind: 'vault', title: v.name, path: v.path, summary: v.what, score: s.n + 1, matched: s.hits });
          });
          ix.sites.forEach(function (x) {
            var s = scoreText(qt, (x.domain + ' ' + (x.thesis || '') + ' ' + (x.aliases || '')).toLowerCase(), (x.tagline || '').toLowerCase());
            if (s.n) out.push({ kind: 'sibling site', title: x.domain, path: x.path || null, url: x.url, summary: x.thesis || x.tagline, score: s.n, matched: s.hits });
          });
          ix.updates.forEach(function (u) {
            var s = scoreText(qt, u.title.toLowerCase(), '');
            if (s.n) out.push({ kind: 'release note', title: u.title, path: u.path, summary: u.version + ' · ' + u.date, score: s.n, matched: s.hits });
          });
          ix.issues.forEach(function (c) {
            var s = scoreText(qt, c.title.toLowerCase(), '');
            if (s.n) out.push({ kind: 'board card', title: c.id + ' ' + c.title, path: c.path, summary: c.status + ' · ' + c.role, score: s.n, matched: s.hits });
          });
          out.sort(function (x, y) { return y.score - x.score; });
          return { query: a.query, results: out.slice(0, HITS) };
        });
      }
    },
    read_page: {
      desc: 'Read one page of sgit.ai as markdown — the full text, up to 6000 characters. Pass the path exactly as returned by search_site (e.g. "docs/vault-messaging.html"). Quote it rather than paraphrasing it.',
      params: { path: { type: 'string', description: 'a path from search_site' } }, required: ['path'],
      run: function (a) {
        var p = String(a.path || '').replace(/^\//, '').replace(/#.*$/, '').replace(/\.html$/, '.md');
        if (!/\.md$/.test(p)) p = p.replace(/\/?$/, '/index.md');
        return grab(p).then(function (t) {
          if (!t) return { path: p, error: 'not found — pass a path from search_site' };
          var cut = t.length > PAGE_CHARS;
          return { path: p, truncated: cut, chars: t.length, text: cut ? t.slice(0, PAGE_CHARS) + '\n\n[truncated — ' + (t.length - PAGE_CHARS) + ' more characters]' : t };
        });
      }
    },
    list_vaults: {
      desc: 'List the published vaults (newest first), optionally filtered by category: Application, Analysis, Reference, Record, Presentation, Briefing, Report, Gallery.',
      params: { category: { type: 'string' } },
      run: function (a) {
        return loadIndex().then(function (ix) {
          var v = ix.vaults.filter(function (x) { return !a.category || x.category.toLowerCase() === String(a.category).toLowerCase(); });
          return { count: v.length, vaults: v.map(function (x) { return { n: x.n, name: x.name, vault_id: x.vault_id, category: x.category, what: x.what, files: x.files, size: x.size, published: x.published, path: x.path }; }) };
        });
      }
    },
    list_sites: {
      desc: 'List the sibling sites on *.sgit.ai with their category and each site\'s own one-line thesis. Optional category filter.',
      params: { category: { type: 'string' } },
      run: function (a) {
        return loadIndex().then(function (ix) {
          var s = ix.sites.filter(function (x) { return !a.category || (x.category || '').toLowerCase().indexOf(String(a.category).toLowerCase()) >= 0; });
          return { count: s.length, sites: s.map(function (x) { return { domain: x.domain, category: x.category, thesis: x.thesis, tagline: x.tagline, url: x.url, live: x.live }; }) };
        });
      }
    },
    latest_updates: {
      desc: 'The most recent release notes (what changed on the site and when). Default 8.',
      params: { n: { type: 'integer' } },
      run: function (a) {
        return loadIndex().then(function (ix) { return { updates: ix.updates.slice(0, Math.min(30, a.n || 8)) }; });
      }
    },
    get_board: {
      desc: 'The team board: open work as cards. Statuses: needs (only the author can supply), backlog, doing, review, done. Optional status filter.',
      params: { status: { type: 'string' } },
      run: function (a) {
        return loadIndex().then(function (ix) {
          var c = ix.issues.filter(function (x) { return !a.status || x.status === a.status; });
          return { count: c.length, cards: c };
        });
      }
    },
    current_page: {
      desc: 'The page the reader is looking at right now: its path and title. Call this when the question says "this page" or "here".',
      params: {},
      run: function () {
        return loadIndex().then(function (ix) {
          var p = null;
          ix.pages.forEach(function (x) { if (x.path === HERE) p = x; });
          return p || { path: HERE, title: document.title };
        });
      }
    }
  };

  function toolSchemas() {
    return Object.keys(TOOLS).map(function (n) {
      return { type: 'function', function: { name: n, description: TOOLS[n].desc,
        parameters: { type: 'object', properties: TOOLS[n].params || {}, required: TOOLS[n].required || [] } } };
    });
  }
  function runTool(name, args) {
    var t = TOOLS[name];
    if (!t) return Promise.resolve({ error: 'no such tool: ' + name });
    var a = {};
    try { a = typeof args === 'string' ? (args ? JSON.parse(args) : {}) : (args || {}); } catch (e) { a = {}; }
    return Promise.resolve().then(function () { return t.run(a); }).catch(function (e) { return { error: String(e && e.message || e) }; });
  }

  // ---------------------------------------------------------------- DOM helpers
  function el(tag, cls, txt) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (txt != null) e.textContent = txt;
    return e;
  }
  function href(path) {
    if (!path) return null;
    if (/^https?:\/\//.test(path)) return path;
    return ROOT + path.replace(/^\//, '');
  }
  // minimal, safe markdown: escape first, then bold / code / links; links only to http(s) or site paths
  function md(text) {
    var s = String(text).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    s = s.replace(/`([^`\n]+)`/g, '<code>$1</code>');
    s = s.replace(/\*\*([^*\n]+)\*\*/g, '<b>$1</b>');
    s = s.replace(/\[([^\]\n]+)\]\(([^)\s]+)\)/g, function (m, t, u) {
      if (!/^(https?:\/\/|[a-zA-Z0-9_./-]+(\.html|\.md)?(#[\w-]*)?)$/.test(u)) return t;
      var h = /^https?:/.test(u) ? u : ROOT + u.replace(/^\//, '').replace(/\.md(#|$)/, '.html$1');
      return '<a href="' + h + '"' + (/^https?:/.test(u) ? ' rel="noopener" target="_blank"' : '') + '>' + t + '</a>';
    });
    return s.split(/\n{2,}/).map(function (p) { return '<p>' + p.replace(/\n/g, '<br>') + '</p>'; }).join('');
  }

  // ---------------------------------------------------------------- the pane
  var launch = el('button', 'sc-launch', 'Ask this site');
  launch.type = 'button'; launch.setAttribute('aria-expanded', 'false');
  var pane = el('aside', 'sc-pane'); pane.hidden = true; pane.setAttribute('aria-label', 'Ask this site');
  pane.innerHTML =
    '<div class="sc-head"><b>Ask this site</b><span class="nc-mode sc-mode"></span>'
    + '<button type="button" class="sc-keytoggle nc-eg">Use my own LLM key</button>'
    + '<button type="button" class="sc-close" aria-label="Close">&times;</button></div>'
    + '<div class="nc-keypanel sc-keypanel" hidden><p class="small">An <a href="https://openrouter.ai/keys" rel="noopener" target="_blank">OpenRouter key</a>. '
    + 'It is stored in this browser and sent to openrouter.ai only — never to sgit.ai, which has no server. '
    + 'With no host to hold it, the key lives in this page\'s origin; that is your call to make.</p>'
    + '<input class="nc-key sc-key" type="password" placeholder="sk-or-v1-…" autocomplete="off"> '
    + '<input class="nc-key sc-model" type="text" placeholder="model (default ' + DEFAULT_MODEL + ')"> '
    + '<button type="button" class="nc-eg sc-keysave">Save</button></div>'
    + '<div class="nc-log sc-log" aria-live="polite"></div>'
    + '<form class="nc-form sc-form"><input class="nc-input sc-input" type="text" placeholder="Ask about any page, vault or site… or /help" autocomplete="off"><button type="submit" class="sc-send">Ask</button></form>'
    + '<div class="sc-foot small dim">Tools the answer can call: ' + Object.keys(TOOLS).join(' · ') + '. Every call is shown.</div>';
  document.body.appendChild(launch); document.body.appendChild(pane);

  var log = pane.querySelector('.sc-log'), form = pane.querySelector('.sc-form'), input = pane.querySelector('.sc-input');
  var keyPanel = pane.querySelector('.sc-keypanel'), keyInput = pane.querySelector('.sc-key'), modelInput = pane.querySelector('.sc-model');
  var modeLabel = pane.querySelector('.sc-mode'), keyToggle = pane.querySelector('.sc-keytoggle');

  function say(who, node) {
    var row = el('div', 'nc-msg nc-' + who);
    row.appendChild(node); log.appendChild(row); log.scrollTop = log.scrollHeight; return row;
  }
  function trace(name, args, summary) {
    var d = el('details', 'sc-trace');
    var s = el('summary', null, '→ ' + name + '(' + (args && Object.keys(args).length ? JSON.stringify(args) : '') + ')' + (summary ? ' · ' + summary : ''));
    d.appendChild(s); return d;
  }
  function hitCard(r) {
    var a = el('a', 'nc-hit');
    var h = href(r.path) || r.url; if (h) a.href = h;
    if (r.url && !r.path) { a.target = '_blank'; a.rel = 'noopener'; }
    a.appendChild(el('b', null, r.title));
    if (r.summary) a.appendChild(el('span', 'nc-hit-thesis', r.summary));
    a.appendChild(el('span', 'nc-hit-why', r.kind + (r.matched && r.matched.length ? ' · matched ' + r.matched.join(', ') : '')));
    return a;
  }
  function renderResult(name, res) {
    var w = el('div');
    if (name === 'search_site') {
      if (!res.results.length) { w.appendChild(el('p', null, 'Nothing matched. Try other words, or /vaults, /sites, /board.')); return w; }
      var list = el('div', 'nc-hits'); res.results.forEach(function (r) { list.appendChild(hitCard(r)); }); w.appendChild(list); return w;
    }
    if (name === 'read_page') { var pre = el('pre', 'sc-pre'); pre.textContent = res.error || res.text; w.appendChild(pre); return w; }
    if (name === 'list_vaults') { var l = el('div', 'nc-hits'); res.vaults.forEach(function (v) { l.appendChild(hitCard({ title: '#' + v.n + ' ' + v.name, path: v.path, summary: v.what, kind: v.category + ' · ' + v.files + ' files · ' + v.size + ' · ' + v.published })); }); w.appendChild(l); return w; }
    if (name === 'list_sites') { var l2 = el('div', 'nc-hits'); res.sites.forEach(function (x) { l2.appendChild(hitCard({ title: x.domain, url: x.url, summary: x.thesis || x.tagline, kind: x.category + (x.live ? '' : ' · not published yet') })); }); w.appendChild(l2); return w; }
    if (name === 'latest_updates') { var l3 = el('div', 'nc-hits'); res.updates.forEach(function (u) { l3.appendChild(hitCard({ title: u.title, path: u.path, summary: u.version + ' · ' + u.date, kind: 'release note' })); }); w.appendChild(l3); return w; }
    if (name === 'get_board') { var l4 = el('div', 'nc-hits'); res.cards.forEach(function (c) { l4.appendChild(hitCard({ title: c.id + ' — ' + c.title, path: c.path, summary: c.status + ' · ' + c.role + ' · ' + c.priority, kind: 'board card' })); }); w.appendChild(l4); return w; }
    var p2 = el('pre', 'sc-pre'); p2.textContent = JSON.stringify(res, null, 1); w.appendChild(p2); return w;
  }

  // ---------------------------------------------------------------- tier 0
  var HELP = 'No key needed for any of these:\n/vaults [category] · /sites [category] · /updates · /board [status] · /read PATH · /here\nOr type words to search everything on the site. Add an OpenRouter key and a model will call these same tools for you and answer in sentences.';
  function tier0(q) {
    var m = q.match(/^\/(\w+)\s*(.*)$/);
    var name, args = {};
    if (m) {
      var cmd = m[1].toLowerCase(), rest = m[2].trim();
      if (cmd === 'help') { say('bot', md(HELP) ? (function () { var d = el('div'); d.innerHTML = md(HELP); return d; }()) : el('p', null, HELP)); return; }
      if (cmd === 'vaults') { name = 'list_vaults'; if (rest) args.category = rest; }
      else if (cmd === 'sites') { name = 'list_sites'; if (rest) args.category = rest; }
      else if (cmd === 'updates') { name = 'latest_updates'; }
      else if (cmd === 'board') { name = 'get_board'; if (rest) args.status = rest; }
      else if (cmd === 'read') { name = 'read_page'; args.path = rest; }
      else if (cmd === 'here') { name = 'current_page'; }
      else { say('bot', el('p', 'nc-err', 'Unknown command. ' + HELP.split('\n')[1])); return; }
    } else { name = 'search_site'; args.query = q; }
    var row = say('bot', el('p', 'dim small', 'running ' + name + '…'));
    runTool(name, args).then(function (res) {
      row.innerHTML = '';
      row.appendChild(trace(name, args, res.count != null ? res.count + ' results' : (res.results ? res.results.length + ' results' : '')));
      row.appendChild(renderResult(name, res));
      log.scrollTop = log.scrollHeight;
    });
  }

  // ---------------------------------------------------------------- tier 1: the tool loop
  var history = [];
  function systemPrompt() {
    return 'You are the guide to sgit.ai, a site about sgit (git for encrypted vaults) built by one person and a team of AI agents. '
      + 'You answer ONLY from what the tools return: search_site to find things, read_page to read them, list_vaults / list_sites / latest_updates / get_board for structured lists, current_page for "this page". '
      + 'Call tools before answering; call read_page on the best result before making a claim about a page. Quote the page rather than paraphrasing. '
      + 'Never invent a page, vault, site or number. If the tools do not find it, say so. '
      + 'Answer in plain prose, at most a short paragraph or a short list, and end with the path(s) you used as markdown links like [title](path.html). '
      + 'The reader is on: ' + HERE + '.';
  }
  function askModel(q, row) {
    var key = localStorage.getItem(LS_KEY), model = localStorage.getItem(LS_MODEL) || DEFAULT_MODEL;
    var msgs = [{ role: 'system', content: systemPrompt() }].concat(history.slice(-8), [{ role: 'user', content: q }]);
    var status = el('p', 'dim small', 'thinking…'); row.appendChild(status);
    var round = 0;
    function call() {
      return fetch('https://openrouter.ai/api/v1/chat/completions', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + key, 'HTTP-Referer': 'https://sgit.ai/', 'X-Title': 'sgit.ai site chat' },
        body: JSON.stringify({ model: model, messages: msgs, tools: toolSchemas(), tool_choice: 'auto', max_tokens: 900 })
      }).then(function (r) {
        if (!r.ok) return r.text().then(function (t) { throw new Error('OpenRouter ' + r.status + ': ' + t.slice(0, 160)); });
        return r.json();
      }).then(function (j) {
        var m = j.choices && j.choices[0] && j.choices[0].message;
        if (!m) throw new Error('empty response');
        if (m.tool_calls && m.tool_calls.length && round < MAX_ROUNDS) {
          round++;
          msgs.push({ role: 'assistant', content: m.content || null, tool_calls: m.tool_calls });
          return Promise.all(m.tool_calls.map(function (tc) {
            var name = tc.function.name, args = {};
            try { args = JSON.parse(tc.function.arguments || '{}'); } catch (e) {}
            return runTool(name, args).then(function (res) {
              var summary = res.count != null ? res.count + ' results' : res.results ? res.results.length + ' results' : res.chars ? res.chars + ' chars' : (res.error ? 'error' : 'ok');
              row.insertBefore(trace(name, args, summary), status);
              msgs.push({ role: 'tool', tool_call_id: tc.id, name: name, content: JSON.stringify(res).slice(0, 20000) });
            });
          })).then(call);
        }
        status.remove();
        var answer = el('div', 'sc-answer'); answer.innerHTML = md(m.content || '(no answer)'); row.appendChild(answer);
        history.push({ role: 'user', content: q }, { role: 'assistant', content: m.content || '' });
        log.scrollTop = log.scrollHeight;
      });
    }
    return call().catch(function (err) {
      status.remove();
      row.appendChild(el('p', 'nc-err', 'The model call failed (' + err.message + '). Running the search tool directly instead:'));
      runTool('search_site', { query: q }).then(function (res) { row.appendChild(trace('search_site', { query: q }, res.results.length + ' results')); row.appendChild(renderResult('search_site', res)); });
    });
  }

  // ---------------------------------------------------------------- wiring
  function hasKey() { try { return !!localStorage.getItem(LS_KEY); } catch (e) { return false; } }
  function refreshMode() {
    var on = hasKey();
    modeLabel.textContent = on ? 'model + tools · your key' : 'tools only · no key, no network';
    modeLabel.className = 'nc-mode sc-mode' + (on ? ' on' : '');
    keyToggle.textContent = on ? 'Remove key' : 'Use my own LLM key';
  }
  function open(o) {
    pane.hidden = !o; launch.setAttribute('aria-expanded', String(o)); document.documentElement.classList.toggle('sc-open', o);
    try { localStorage.setItem(LS_OPEN, o ? '1' : ''); } catch (e) {}
    if (o) { loadIndex(); if (!log.children.length) { var d = el('div'); d.innerHTML = md('Ask about any page, vault or sibling site. ' + HELP.replace(/\n/g, '\n\n')); say('bot', d); } setTimeout(function () { input.focus(); }, 50); }
  }
  launch.addEventListener('click', function () { open(pane.hidden); });
  pane.querySelector('.sc-close').addEventListener('click', function () { open(false); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !pane.hidden) open(false); });
  keyToggle.addEventListener('click', function () {
    if (hasKey()) { try { localStorage.removeItem(LS_KEY); } catch (e) {} keyPanel.hidden = true; refreshMode(); return; }
    keyPanel.hidden = !keyPanel.hidden;
  });
  pane.querySelector('.sc-keysave').addEventListener('click', function () {
    var v = (keyInput.value || '').trim(); if (!v) return;
    try { localStorage.setItem(LS_KEY, v); var mm = (modelInput.value || '').trim(); if (mm) localStorage.setItem(LS_MODEL, mm); } catch (e) {}
    keyInput.value = ''; keyPanel.hidden = true; refreshMode();
  });
  form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    var q = (input.value || '').trim(); if (!q) return;
    say('you', el('p', null, q)); input.value = '';
    if (!hasKey() || q.charAt(0) === '/') return tier0(q);
    var row = say('bot', el('div'));
    askModel(q, row);
  });

  // expose for tests and for other modules (the network chooser can call the same tools)
  window.__sgitChat = { tools: TOOLS, run: runTool, loadIndex: loadIndex, open: open };
  refreshMode();
  try { if (localStorage.getItem(LS_OPEN) === '1' && window.innerWidth > 900) open(true); } catch (e) {}
}());
