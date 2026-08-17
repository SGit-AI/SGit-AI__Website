/* compare.js — render the executed checks, and make staleness visible.

   The brief this page was built from is right that a date in small print is not a
   freshness mechanism: a reader takes the claim as current. So every result carries
   an explicit STATE derived from its age against the expiry threshold, and a result
   past the threshold renders as "unverified" rather than as fact — the entry ages
   out loudly instead of quietly becoming wrong.

   Results come from compare/results.json, written by admin/build/compare_tests.py.
   Loading them at runtime (rather than baking them in at build time) means a re-run
   refreshes the page with no site deploy — the same pattern the catalogue uses. */
(function () {
  'use strict';

  var LABEL = { pass: 'holds', fail: 'FAILED', absent: 'absent' };

  function ageDays(d) {
    var then = Date.parse(d + 'T00:00:00Z');
    if (isNaN(then)) return null;
    return Math.floor((Date.now() - then) / 86400000);
  }

  function state(days, expiry) {
    if (days === null) return { cls: 'stale', text: 'undated' };
    if (days > expiry) return { cls: 'stale', text: 'UNVERIFIED — last checked ' + days + ' days ago, past the ' + expiry + '-day threshold' };
    if (days <= 1) return { cls: 'fresh', text: days === 0 ? 'verified today' : 'verified yesterday' };
    return { cls: 'fresh', text: 'verified ' + days + ' days ago' };
  }

  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }

  async function run() {
    var host = document.getElementById('cmp-results');
    var banner = document.getElementById('cmp-freshness');
    if (!host) return;
    var data;
    try {
      var r = await fetch('results.json');
      if (!r.ok) throw new Error(r.status);
      data = await r.json();
    } catch (e) {
      host.textContent = 'Could not load the check results (' + e.message + '). The claims above stand on their stated dates.';
      if (banner) banner.textContent = '';
      return;
    }

    var expiry = data.expiry_days || 30;
    var oldest = 0, anyFail = false;
    var rows = data.tests.map(function (t) {
      var days = ageDays(t.checked);
      if (days !== null && days > oldest) oldest = days;
      if (t.outcome === 'fail') anyFail = true;
      var st = state(days, expiry);
      return '<div class="cmp-check cmp-' + t.outcome + ' cmp-' + st.cls + '">' +
        '<div class="cmp-check-h"><b>' + esc(t.claim) + '</b>' +
        '<span class="cmp-badge cmp-b-' + t.outcome + '">' + LABEL[t.outcome] + '</span></div>' +
        '<div class="cmp-ev"><code>' + esc(t.id) + '</code> · ' + esc(t.evidence) + '</div>' +
        '<div class="cmp-meta">fails if: ' + esc(t.fails_if) + ' · ' + esc(st.text) + '</div>' +
      '</div>';
    });
    host.classList.remove('dim');
    host.innerHTML = rows.join('');

    if (banner) {
      var s = state(oldest, expiry);
      banner.className = 'small cmp-banner cmp-' + s.cls;
      banner.innerHTML = '<b>Machine-verified rows:</b> ' + data.tests.length + ' checks, last run ' +
        esc(data.generated) + ' — ' + esc(s.text) + '. Threshold: ' + expiry + ' days.' +
        (anyFail ? ' <b>One or more checks are FAILING and the entries above may now be wrong.</b>' : '');
    }
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', run);
  else run();
}());
