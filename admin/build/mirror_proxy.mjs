/* mirror_proxy.mjs — the local half of `capture_shots.mjs --mirror`.

   Why this exists: in a sandbox the browser has no direct egress, but curl does
   (it honours the environment's HTTPS proxy and CA bundle). capture_shots.mjs's
   --mirror flag rewrites every *.sgraph.ai request to
   http://localhost:8898/PROXY/<host><path><query>; this server is what answers,
   fetching the real URL with curl and handing back status, content-type and bytes.

   Read-only by construction: GET only, and only to the hosts the capture harness
   is allowed to reach. Anything else is refused rather than forwarded.

     node admin/build/mirror_proxy.mjs [port]
*/
import http from 'http';
import fs from 'fs';
import os from 'os';
import path from 'path';
import crypto from 'crypto';
import { execFile } from 'child_process';

const PORT  = Number(process.argv[2] || 8898);
const HOSTS = new Set(['dev.vault.sgraph.ai', 'dev.send.sgraph.ai', 'dev.sgraph.ai', 'dev.tools.sgraph.ai']);

// Headers go to a temp file rather than to stderr: with both streams piped, curl
// fails the body write (error 23). The body stays on stdout as raw bytes, so
// binary responses (images, fonts) survive — decoding them would corrupt them.
const fetchUpstream = url => new Promise((resolve, reject) => {
  const hdr = path.join(os.tmpdir(), `mirror-${crypto.randomUUID()}.head`);
  execFile('curl', ['-sS', '-L', '--max-time', '60', '-D', hdr, url],
    { encoding: 'buffer', maxBuffer: 256 * 1024 * 1024 },
    (err, stdout) => {
      let head = '';
      try { head = fs.readFileSync(hdr, 'latin1'); } catch {}
      fs.rmSync(hdr, { force: true });
      if (err) return reject(err);
      // A proxied request answers "HTTP/1.1 200 Connection Established" first and
      // a redirect chain adds one line per hop, so the LAST status line is the real one.
      const status = Number((head.match(/HTTP\/[\d.]+ (\d{3})/g) || []).pop()?.slice(-3) || 200);
      const ctype  = (head.match(/^content-type:\s*(.+)$/im) || [])[1]?.trim()
                     || 'application/octet-stream';
      resolve({ status, ctype, body: stdout });
    });
});

http.createServer(async (req, res) => {
  const m = req.method === 'GET' && req.url.match(/^\/PROXY\/([^/]+)(\/.*)?$/);
  if (!m || !HOSTS.has(m[1])) {
    res.writeHead(403, { 'content-type': 'text/plain' });
    return res.end('refused\n');
  }
  try {
    const { status, ctype, body } = await fetchUpstream(`https://${m[1]}${m[2] || '/'}`);
    res.writeHead(status, { 'content-type': ctype, 'access-control-allow-origin': '*' });
    res.end(body);
  } catch (e) {
    res.writeHead(502, { 'content-type': 'text/plain' });
    res.end(String(e.message));
  }
}).listen(PORT, '127.0.0.1', () => console.log(`mirror proxy on http://127.0.0.1:${PORT}`));
