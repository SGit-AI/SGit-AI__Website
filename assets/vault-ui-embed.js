/* vault-ui-embed.js — the official SG/Vault interface, embedded via its embed
   protocol, as a reusable component.

   Usage (one div per embed):
     <div class="sgv-uiembed" data-vault="4bshby5n" data-readkey="<64-hex>"
          data-app="1"></div>
   data-app="0" hides the App Mode button (vaults without an app.json).

   Each surface opens in its OWN frame, stacked — App Mode first, the vault
   browser under it — so both can be on screen at once. Opening the second is
   fast on purpose: the encrypted objects are already in the client's cache
   from the first open, so the second surface mostly decrypts rather than
   fetches.

   The handshake (see the UI's embed-protocol.js): load ?embed=1&parent=<origin>,
   wait for {sg:'vault-embed-ready'} FROM THAT FRAME, then post
   {sg:'vault-open', key, mode} with targetOrigin pinned to the vault origin.
   The key is a published read-only credential; it never appears in a URL and
   the frame keeps it in memory only. vault-ready / vault-error come back as
   structured events and drive each frame's status line. */
(function () {
  'use strict';
  var ORIGIN = 'https://dev.vault.sgraph.ai';

  function mountAll() {
    var hosts = document.querySelectorAll('.sgv-uiembed');
    for (var i = 0; i < hosts.length; i++) mount(hosts[i]);
  }

  function mount(el) {
    var vaultId = el.getAttribute('data-vault');
    var readKey = el.getAttribute('data-readkey');
    var hasApp  = el.getAttribute('data-app') !== '0';
    if (!vaultId || !readKey) return;
    var cred = 'sgit_rk1_' + readKey + ':' + vaultId;

    var row = document.createElement('div'); row.className = 'sgv-btnrow';
    el.appendChild(row);

    // One section per surface, stacked in this order: the app, then the browser.
    var sections = [];
    if (hasApp) sections.push(section(el, row, cred, 'app',
      '▶ App Mode — the vault’s own app'));
    sections.push(section(el, row, cred, 'vault',
      '▤ Vault browser — FILES / SGIT / SETTINGS'));

    // One listener for the mount; route replies by which frame sent them.
    window.addEventListener('message', function (e) {
      if (e.origin !== ORIGIN) return;
      for (var i = 0; i < sections.length; i++) {
        var s = sections[i];
        if (!s.frame.contentWindow || e.source !== s.frame.contentWindow) continue;
        var d = e.data || {};
        if (d.sg === 'vault-embed-ready' && s.armed) {
          clearTimeout(s.fallbackT);
          e.source.postMessage({ sg: 'vault-open', key: cred, mode: s.mode }, ORIGIN);
          s.note.textContent = 'Handshake complete — key handed over postMessage, opening…';
        } else if (d.sg === 'vault-ready') {
          s.note.innerHTML = 'Opened <b>read-only</b> over the embed protocol — the key never appeared in a URL and was never written to the frame’s storage' +
            (d.fileCount ? '; ' + d.fileCount + ' files decrypted in the frame' : '') + '.';
        } else if (d.sg === 'vault-error') {
          s.note.textContent = 'Vault open failed: ' + (d.message || 'unknown error');
        }
        return;
      }
    });
  }

  // Build one surface: its button in the shared row, its own note + frame.
  function section(el, row, cred, mode, label) {
    var s = { mode: mode, armed: false, fallbackT: null };

    var b = document.createElement('button');
    b.type = 'button'; b.className = 'sgv-embed-load'; b.textContent = label;
    row.appendChild(b);

    s.note = document.createElement('p');
    s.note.className = 'small dim'; s.note.style.margin = '.6rem 0 0';
    s.note.style.display = 'none';

    s.frame = document.createElement('iframe');
    s.frame.className = 'sgv-embed-frame sgv-embed-ui sgv-breakout';
    s.frame.title = 'The official SG/Vault UI (' + (mode === 'app' ? 'App Mode' : 'vault browser') + '), opened read-only';
    s.frame.style.display = 'none';

    el.appendChild(s.note); el.appendChild(s.frame);

    b.addEventListener('click', function () {
      s.armed = true;
      s.note.style.display = ''; s.frame.style.display = 'block';
      s.note.textContent = 'Handshaking with the vault UI…';
      var page = mode === 'vault' ? '/en-gb/vault/' : '/en-gb/app/';
      s.frame.src = ORIGIN + page + '?embed=1&parent=' + encodeURIComponent(location.origin);
      clearTimeout(s.fallbackT);
      s.fallbackT = setTimeout(function () {
        if (mode === 'app') {
          s.frame.src = ORIGIN + '/#' + encodeURIComponent(cred);
          s.note.textContent = 'Embed handshake timed out; fell back to the URL-fragment flow.';
        } else {
          s.note.textContent = 'Embed handshake timed out. Reload and try again.';
        }
      }, 12000);
    });
    return s;
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', mountAll);
  else mountAll();
}());
