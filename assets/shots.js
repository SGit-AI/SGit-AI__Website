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

  async function fill(fig, eager) {
    var name = fig.getAttribute('data-shot');
    if (!name) return;
    if (fig.dataset.loaded) {
      // Already has an <img>, but it may be one the observer created with
      // loading="lazy" that has not decoded yet. Promote it — see below.
      if (eager) [].forEach.call(fig.querySelectorAll('img'), function (i) { i.loading = 'eager'; });
      return;
    }
    fig.dataset.loaded = '1';
    // Images live in the vault's own folder:
    //   demos/vaults/<slug>/index.html  ->  demos/vaults/<slug>/images/<name>
    // A page-relative path means a vault folder is self-contained: move it, and its
    // pictures move with it. Deeper pages under the same vault (views/, videos/)
    // point back up with data-dir, so one vault keeps ONE image folder.
    // Deeper pages under the same vault (views/, videos/) point back up with data-dir,
    // so one vault keeps ONE image folder no matter how many pages describe it.
    var path = (fig.getAttribute('data-dir') || 'images/') + name;
    try {
      var data = await bytes(path);
      var url = URL.createObjectURL(new Blob([data], { type: 'image/webp' }));
      var img = document.createElement('img');
      img.alt = fig.getAttribute('data-alt') || '';
      // loading="lazy" defers the DECODE, not just the fetch, for an image far below
      // the viewport — and a page that is never scrolled never brings it into view, so
      // the element sat there complete:false, naturalWidth:0 and printed as a blank
      // gap. (Measured: the last three figures of the seven-views page, every time.)
      // It is only correct on the observer path, where the figure is by definition
      // about to be on screen; the prefetch and print paths must ask for eager.
      img.loading = eager ? 'eager' : 'lazy';
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

  function all() {
    return [].slice.call(document.querySelectorAll('figure.shot[data-shot]'));
  }

  function start() {
    var figs = all();
    if (!figs.length) return;
    // forEach passes (value, index) — never hand it fill directly, or the index
    // arrives as the `eager` flag and every figure but the first loads eagerly.
    if (!('IntersectionObserver' in window)) {
      figs.forEach(function (f) { fill(f, true); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { io.unobserve(e.target); fill(e.target); }
      });
    }, { rootMargin: '400px' });
    figs.forEach(function (f) { io.observe(f); });

    // Printing needs EVERY figure, not just the ones the reader scrolled past. A page
    // exported straight from the top used to come out with blank gaps where the
    // unscrolled screenshots were — nothing errored, the <img> simply never existed.
    //
    // beforeprint alone cannot fix it: it is synchronous, and Chrome will not wait for
    // an async fetch + decode before paginating. So the real fix is the prefetch —
    // once the page is idle, quietly pull the rest so the bytes are already in cache
    // by the time anyone reaches for Cmd-P. A walkthrough page is well under a
    // megabyte of WebP in total, and it costs nothing on the critical path.
    // beforeprint stays as the backstop for a print fired before idle.
    var eager = function () { io.disconnect(); all().forEach(function (f) { fill(f, true); }); };
    if ('requestIdleCallback' in window) requestIdleCallback(eager, { timeout: 4000 });
    else setTimeout(eager, 2500);
    window.addEventListener('beforeprint', eager);
    if (window.matchMedia) {                       // Safari fires no beforeprint
      var mq = window.matchMedia('print');
      if (mq.addEventListener) mq.addEventListener('change', function (e) { if (e.matches) eager(); });
    }
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
}());
