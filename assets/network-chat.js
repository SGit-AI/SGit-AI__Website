/* network-chat.js — "which of these sites is mine?" as a conversation.
 *
 * THREE TIERS, and the reason the default is the boring one.
 *
 *   Tier 0  MATCH (shipped, default, no key, no network)
 *           A deterministic scorer over the site catalogue emitted at build time.
 *           Works offline, costs nothing, and answers the actual question — which of
 *           the nineteen sites is mine — for the large majority of phrasings. It is
 *           the default because a reader should never have to hold a credential to
 *           use an index.
 *
 *   Tier 1  BYOK (this file, gated behind an explicit opt-in)
 *           The reader pastes their own OpenRouter key. The browser calls
 *           https://openrouter.ai/api/v1/chat/completions directly, streaming, with
 *           the catalogue as context. This is the pattern already proven in the
 *           SG/Vault workbench vault, which uses the same endpoint and the versioned
 *           sg-llm-request module on dev.tools.sgraph.ai.
 *           THE HONEST COST: on a static site there is no host, so the key lives in
 *           this page's origin — localStorage and the fetch call. That is a real
 *           trust boundary the reader is accepting, and the UI says so rather than
 *           burying it. Never sent anywhere but openrouter.ai; never to sgit.ai.
 *
 *   Tier 2  BRIDGE (not implemented here — see the plan)
 *           Serve this directory as a vault app and the key stops being our problem:
 *           sg.llm.chat keeps the credential in .vault/llm/config.json, below the
 *           permission floor, and the app never sees it. Two of the three chat
 *           surfaces documented at llms.sgit.ai need no application code at all.
 *           The qualification travels with the claim: that bridge protects the key,
 *           it is not yet an egress boundary.
 *
 * Nothing here talks to sgit.ai. Tier 0 is pure computation; Tier 1 talks only to
 * openrouter.ai using a key the reader supplied.
 */
(function () {
  'use strict';

  var LS_KEY = 'sgit.network.orkey';
  var LS_MODEL = 'sgit.network.ormodel';
  var DEFAULT_MODEL = 'openai/gpt-4o-mini';
  var root = document.getElementById('netchat');
  if (!root) return;

  var CAT = window.__SGIT_SITES__ || [];
  if (!CAT.length) return;

  // ---------------------------------------------------------------- tier 0
  // Score a question against each site. Deliberately simple and inspectable: the
  // reader can see why a site was suggested, which an LLM answer does not give you
  // for free. Stopwords keep "I need to" from matching everything equally.
  var STOP = ('i we you a an the to for of and or my our is are do does how what which '
    + 'want need have has with without on in at it that this me my about can could would '
    + 'should from make making get getting use using build building').split(' ');

  function terms(s) {
    return (s || '').toLowerCase().replace(/[^a-z0-9\s-]/g, ' ').split(/\s+/)
      .filter(function (w) { return w.length > 2 && STOP.indexOf(w) < 0; });
  }

  function score(q, site) {
    var qt = terms(q), hay = (site.hay || '').toLowerCase(), n = 0, hits = [];
    for (var i = 0; i < qt.length; i++) {
      var w = qt[i];
      if (hay.indexOf(w) >= 0) {
        // a hit in the thesis or the domain is worth more than one in the summary
        var weight = ((site.thesis || '') + ' ' + site.domain).toLowerCase().indexOf(w) >= 0 ? 3 : 1;
        n += weight;
        if (hits.indexOf(w) < 0) hits.push(w);
      }
    }
    return { score: n, hits: hits };
  }

  function match(q) {
    var out = [];
    for (var i = 0; i < CAT.length; i++) {
      var r = score(q, CAT[i]);
      if (r.score > 0) out.push({ site: CAT[i], score: r.score, hits: r.hits });
    }
    out.sort(function (a, b) { return b.score - a.score; });
    return out.slice(0, 3);
  }

  // ---------------------------------------------------------------- rendering
  function el(tag, cls, txt) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (txt != null) e.textContent = txt;
    return e;
  }

  var log = root.querySelector('.nc-log');

  function say(who, node) {
    var row = el('div', 'nc-msg nc-' + who);
    row.appendChild(node);
    log.appendChild(row);
    log.scrollTop = log.scrollHeight;
    return row;
  }

  function siteCard(s, hits) {
    var a = el('a', 'nc-hit');
    a.href = s.href;
    if (s.external) { a.target = '_blank'; a.rel = 'noopener'; }
    a.appendChild(el('b', null, s.domain));
    a.appendChild(el('span', 'nc-hit-thesis', s.thesis || s.tagline));
    if (hits && hits.length) {
      a.appendChild(el('span', 'nc-hit-why', 'matched: ' + hits.slice(0, 5).join(', ')));
    }
    return a;
  }

  function answerLocally(q) {
    var res = match(q);
    var wrap = el('div');
    if (!res.length) {
      wrap.appendChild(el('p', null,
        'Nothing matched that. Try naming the thing you are working on — a risk, a regulation, '
        + 'an agent, a graph, a licence, an API key — or browse the areas below.'));
      return wrap;
    }
    wrap.appendChild(el('p', null, res.length === 1
      ? 'One site looks like yours:' : 'These look closest:'));
    var list = el('div', 'nc-hits');
    res.forEach(function (r) { list.appendChild(siteCard(r.site, r.hits)); });
    wrap.appendChild(list);
    return wrap;
  }

  // ---------------------------------------------------------------- tier 1
  function catalogueForModel() {
    return CAT.map(function (s) {
      return '- ' + s.domain + ' — ' + (s.thesis || s.tagline) + ' (' + s.category + ')';
    }).join('\n');
  }

  function askModel(q, onToken, onDone, onErr) {
    var key = localStorage.getItem(LS_KEY);
    var model = localStorage.getItem(LS_MODEL) || DEFAULT_MODEL;
    if (!key) return onErr(new Error('no key'));
    var sys = 'You route readers to one of the sgit.ai family of sites. Here is the whole '
      + 'catalogue:\n\n' + catalogueForModel()
      + '\n\nAnswer in at most three sentences. Name at most two sites, exactly as written '
      + 'above. If none fit, say so plainly rather than stretching. Never invent a site.';
    fetch('https://openrouter.ai/api/v1/chat/completions', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + key },
      body: JSON.stringify({
        model: model, stream: true, max_tokens: 300,
        messages: [{ role: 'system', content: sys }, { role: 'user', content: q }]
      })
    }).then(function (r) {
      if (!r.ok) throw new Error('OpenRouter returned ' + r.status);
      var reader = r.body.getReader(), dec = new TextDecoder(), buf = '';
      (function pump() {
        reader.read().then(function (res) {
          if (res.done) return onDone();
          buf += dec.decode(res.value, { stream: true });
          var lines = buf.split('\n'); buf = lines.pop();
          lines.forEach(function (line) {
            if (line.indexOf('data: ') !== 0) return;
            var d = line.slice(6).trim();
            if (d === '[DONE]') return;
            try {
              var j = JSON.parse(d);
              var t = j.choices && j.choices[0] && j.choices[0].delta && j.choices[0].delta.content;
              if (t) onToken(t);
            } catch (e) { /* keep-alive fragments are expected */ }
          });
          pump();
        }).catch(onErr);
      }());
    }).catch(onErr);
  }

  // ---------------------------------------------------------------- wiring
  var form = root.querySelector('.nc-form');
  var input = root.querySelector('.nc-input');
  var keyPanel = root.querySelector('.nc-keypanel');
  var keyInput = root.querySelector('.nc-key');
  var modeLabel = root.querySelector('.nc-mode');

  function hasKey() { try { return !!localStorage.getItem(LS_KEY); } catch (e) { return false; } }

  function refreshMode() {
    var on = hasKey();
    modeLabel.textContent = on ? 'answering with your OpenRouter key' : 'instant match · no key, no network';
    modeLabel.className = 'nc-mode' + (on ? ' on' : '');
    root.querySelector('.nc-keytoggle').textContent = on ? 'Remove key' : 'Use my own LLM key';
  }

  root.querySelector('.nc-keytoggle').addEventListener('click', function () {
    if (hasKey()) {
      try { localStorage.removeItem(LS_KEY); } catch (e) {}
      keyPanel.hidden = true; refreshMode(); return;
    }
    keyPanel.hidden = !keyPanel.hidden;
  });

  root.querySelector('.nc-keysave').addEventListener('click', function () {
    var v = (keyInput.value || '').trim();
    if (!v) return;
    try { localStorage.setItem(LS_KEY, v); } catch (e) {}
    keyInput.value = '';
    keyPanel.hidden = true;
    refreshMode();
  });

  form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    var q = (input.value || '').trim();
    if (!q) return;
    say('you', el('p', null, q));
    input.value = '';

    if (!hasKey()) { say('bot', answerLocally(q)); return; }

    var p = el('p', null, '');
    var row = say('bot', p);
    var got = false;
    askModel(q,
      function (t) { got = true; p.textContent += t; },
      function () {
        if (!got) { row.remove(); say('bot', answerLocally(q)); return; }
        var res = match(q);
        if (res.length) {
          var list = el('div', 'nc-hits');
          res.slice(0, 2).forEach(function (r) { list.appendChild(siteCard(r.site, null)); });
          row.appendChild(list);
        }
      },
      function (err) {
        row.remove();
        var w = el('div');
        w.appendChild(el('p', 'nc-err', 'The model call failed (' + err.message
          + '). Falling back to the instant match, which needs no key:'));
        w.appendChild(answerLocally(q));
        say('bot', w);
      });
  });

  Array.prototype.forEach.call(root.querySelectorAll('.nc-eg'), function (b) {
    b.addEventListener('click', function () {
      input.value = b.textContent.replace(/^[""]|[""]$/g, '');
      form.dispatchEvent(new Event('submit', { cancelable: true }));
    });
  });

  refreshMode();
}());
