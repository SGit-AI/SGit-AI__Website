/* sgit.ai — shared behaviour (loaded via the SG bridge: sg.loadJs / sg.vfs.readText) */
(function () {
  'use strict';

  /* terminal tabs (landing) */
  var tabs = document.querySelectorAll('.ttab');
  if (tabs.length) {
    var cap = document.getElementById('tcap');
    tabs.forEach(function (t) {
      t.addEventListener('click', function () {
        tabs.forEach(function (x) { x.classList.remove('active'); });
        document.querySelectorAll('.tbody .pane').forEach(function (p) { p.classList.remove('active'); });
        t.classList.add('active');
        var pane = document.getElementById(t.getAttribute('data-pane'));
        if (pane) pane.classList.add('active');
        if (cap) cap.textContent = t.getAttribute('data-cap') || '';
      });
    });
  }

  /* copy-to-clipboard buttons */
  document.querySelectorAll('[data-copy]').forEach(function (btn) {
    var label = btn.querySelector('.cp');
    btn.addEventListener('click', function () {
      var done = function (ok) {
        if (label) { label.textContent = ok ? 'copied!' : 'copy'; setTimeout(function () { label.textContent = 'copy'; }, 1600); }
      };
      try {
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(btn.getAttribute('data-copy')).then(function () { done(true); }, function () { done(false); });
        } else { done(false); }
      } catch (e) { done(false); }
    });
  });

  /* reveal-on-scroll */
  var revs = document.querySelectorAll('.rev');
  if (revs.length) {
    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (es, o) {
        es.forEach(function (e) {
          if (e.isIntersecting) { e.target.classList.add('in'); o.unobserve(e.target); }
        });
      }, { threshold: 0.06 });
      revs.forEach(function (r) { io.observe(r); });
    } else {
      revs.forEach(function (r) { r.classList.add('in'); });
    }
  }
})();
