/* vault-ui-embed.js — the official SG/Vault interface, embedded via its embed
   protocol, as a reusable component.

   Usage (one div per embed):
     <div class="sgv-uiembed" data-vault="4bshby5n" data-readkey="<64-hex>"
          data-app="1"></div>
   data-app="0" hides the App Mode button (vaults without an app.json).

   The handshake (see the UI's embed-protocol.js): load ?embed=1&parent=<origin>,
   wait for {sg:'vault-embed-ready'} FROM THAT FRAME, then post
   {sg:'vault-open', key, mode} with targetOrigin pinned to the vault origin.
   The key is a published read-only credential; it never appears in any URL and
   the frame keeps it in memory only. vault-ready / vault-error come back as
   structured events and drive the status line. */
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
    var bApp = btn('▶ App Mode — the vault’s own app');
    var bVault = btn('▤ Vault browser — FILES / SGIT / SETTINGS');
    var bFs = btn('⛶ Full screen'); bFs.style.display = 'none';
    if (hasApp) row.appendChild(bApp);
    row.appendChild(bVault); row.appendChild(bFs);

    var note = document.createElement('p');
    note.className = 'small dim'; note.style.margin = '.5rem 0 0';
    note.innerHTML = 'Loads <code>dev.vault.sgraph.ai</code> in an iframe and completes the embed handshake — the read key below is all it is given.';

    var f = document.createElement('iframe');
    f.className = 'sgv-embed-frame sgv-embed-ui sgv-breakout';
    f.title = 'The official SG/Vault UI, opened read-only';
    f.setAttribute('allow', 'fullscreen'); f.setAttribute('allowfullscreen', '');
    f.style.display = 'none';

    el.appendChild(row); el.appendChild(note); el.appendChild(f);

    var armed = null, fallbackT = null;
    window.addEventListener('message', function (e) {
      if (e.origin !== ORIGIN || !f.contentWindow || e.source !== f.contentWindow) return;
      var d = e.data || {};
      if (d.sg === 'vault-embed-ready' && armed) {
        clearTimeout(fallbackT);
        e.source.postMessage({ sg: 'vault-open', key: cred, mode: armed }, ORIGIN);
        note.textContent = 'Handshake complete — key handed over postMessage, opening…';
      } else if (d.sg === 'vault-ready') {
        note.innerHTML = 'Opened <b>read-only</b> over the embed protocol — the key never appeared in a URL and was never written to the frame’s storage' +
          (d.fileCount ? '; ' + d.fileCount + ' files decrypted in the frame' : '') +
          '. The chrome’s <b>Read-only</b> badge is the server-side write gate reporting this credential has none.';
      } else if (d.sg === 'vault-error') {
        note.textContent = 'Vault open failed: ' + (d.message || 'unknown error');
      }
    });

    function open(mode) {
      armed = mode;
      f.style.display = 'block'; bFs.style.display = '';
      note.textContent = 'Handshaking with the vault UI…';
      var page = mode === 'vault' ? '/en-gb/vault/' : '/en-gb/app/';
      f.src = ORIGIN + page + '?embed=1&parent=' + encodeURIComponent(location.origin);
      clearTimeout(fallbackT);
      fallbackT = setTimeout(function () {
        if (mode === 'app') { f.src = ORIGIN + '/#' + encodeURIComponent(cred); note.textContent = 'Embed handshake timed out; fell back to the URL-fragment flow.'; }
        else { note.textContent = 'Embed handshake timed out. Reload and try again.'; }
      }, 12000);
    }
    bApp.addEventListener('click', function () { open('app'); });
    bVault.addEventListener('click', function () { open('vault'); });
    bFs.addEventListener('click', function () {
      try { if (f.requestFullscreen) f.requestFullscreen(); } catch (e) {}
    });
  }

  function btn(label) {
    var b = document.createElement('button');
    b.type = 'button'; b.className = 'sgv-embed-load'; b.textContent = label;
    return b;
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', mountAll);
  else mountAll();
}());
