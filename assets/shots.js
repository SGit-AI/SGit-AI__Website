/* shots.js — fill walkthrough figures with their screenshots at runtime.

   The site's authoring contract forbids declarative <img src> (a page must survive
   being served from inside a vault, where the host answers reads over the bridge
   rather than serving declarative fetches). So the markup carries placeholders:

     <figure class="shot" data-shot="lightbox.webp" data-cap="…"></figure>

   and this fills them in. Two paths, in order of preference:
     1. sg.vfs.read — when the page is itself running inside a vault app
     2. plain fetch of assets/shots/<name> — the ordinary web case

   Loading is lazy (IntersectionObserver): the walkthrough sits at the foot of a
   long page, so its images cost nothing until the reader arrives. */
(function () {
  'use strict';

  async function bytes(path) {
    var sg = window.sg || (window.parent && window.parent.sg);
    if (sg && sg.vfs && sg.vfs.read) {
      try { return await sg.vfs.read(path); } catch (e) { /* fall through to fetch */ }
    }
    var r = await fetch(path);
    if (!r.ok) throw new Error(r.status + ' ' + path);
    return new Uint8Array(await r.arrayBuffer());
  }

  async function fill(fig) {
    var name = fig.getAttribute('data-shot');
    if (!name || fig.dataset.loaded) return;
    fig.dataset.loaded = '1';
    // Images live beside the page, in the vault's own folder:
    //   demos/vaults/<slug>/index.html  ->  demos/vaults/<slug>/images/<name>
    // A page-relative path means a vault folder is self-contained: move it, and its
    // pictures move with it.
    var path = 'images/' + name;
    try {
      var data = await bytes(path);
      var url = URL.createObjectURL(new Blob([data], { type: 'image/webp' }));
      var img = document.createElement('img');
      img.alt = fig.getAttribute('data-alt') || '';
      img.loading = 'lazy';
      img.addEventListener('load', function () { fig.classList.add('shot--in'); });
      img.src = url;
      fig.insertBefore(img, fig.firstChild);
    } catch (e) {
      fig.classList.add('shot--failed');
      var p = document.createElement('p');
      p.className = 'small dim';
      p.textContent = 'screenshot unavailable (' + name + ')';
      fig.insertBefore(p, fig.firstChild);
    }
  }

  function start() {
    var figs = [].slice.call(document.querySelectorAll('figure.shot[data-shot]'));
    if (!figs.length) return;
    if (!('IntersectionObserver' in window)) { figs.forEach(fill); return; }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { io.unobserve(e.target); fill(e.target); }
      });
    }, { rootMargin: '400px' });
    figs.forEach(function (f) { io.observe(f); });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
}());
