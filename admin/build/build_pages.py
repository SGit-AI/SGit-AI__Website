#!/usr/bin/env python3
"""Generate every page of the sgit.ai vault site from a shared template.

Release process (see admin/index.html):
  1. bump SITE_VERSION below (v0.1.n — n increases on every push)
  2. add a row to VERSION_LOG
  3. run this script, run the validation suite, sgit commit + push
"""
import os

SITE_VERSION = 'v0.1.14'

def find_vault_root():
    d = os.path.dirname(os.path.abspath(__file__))
    while not os.path.exists(os.path.join(d, 'app.json')):
        parent = os.path.dirname(d)
        if parent == d:
            raise SystemExit('vault root not found (no app.json above this script)')
        d = parent
    return d

VERSION_LOG = [
    ('v0.1.14', '2026-08-12', 'this release',
     'Two new pages, both linked this time: docs/exposed-vault-key.html (the rotation runbook plus the case study of this site\'s own key leak) and briefs.html (cross-team briefs — which v0.1.13 built but never registered, so nothing linked to it). New validator rule: every generated page must be reachable from another page, or the build fails. Added a fourth CLI-team ask: history-preserving rekey.'),
    ('v0.1.13', '2026-08-12', 'obj-cas-imm-5168ef3fe1a7',
     'SECURITY: the vault passphrase had been written into admin/build/validate.js as an anti-leak tripwire regex — which put the literal secret into a tracked, public file (present in 3 commits). Removed; the tripwire now reads the secret from the gitignored local/ tier and scans for it, so it can never be hardcoded again. The key must be treated as compromised and rotated. Also: a /briefs page collecting the cross-team briefs (multi-agent collaboration log), and a "contacting the server" notice before network commands in the browser terminal.'),
    ('v0.1.12', '2026-08-11', 'obj-cas-imm-e8ceb3fc2239',
     'In-browser clone completes: serial-executor shim for Pyodide (WebAssembly cannot spawn threads, so all parallel blob transfers run sequentially in the browser) — validated natively against the live server with thread creation disabled: full 225-blob clone of this site vault. A serial/auto-detect mode is proposed upstream to the sgit CLI.'),
    ('v0.1.11', '2026-08-11', 'obj-cas-imm-c9afa76a79cb',
     'Browser-transport fix for in-browser clone: drop the redundant X-API-Key header (the servers CORS-allow x-sgraph-access-token but not x-api-key, and one disallowed header fails the whole preflight — diagnosed live from the first user clone attempt); CORS/network failures now surface as readable HTTP 599 errors instead of a Pyodide SystemError.'),
    ('v0.1.10', '2026-08-11', 'obj-cas-imm-deac6363bff9',
     'In-browser terminal on /try: the real sgit CLI in-process (init, commit, status, history — and network commands via a browser XHR transport: clone/push/pull straight to the SG/Send servers), plus a busybox of file commands over the in-memory filesystem. Key hygiene: every example key on the site is now an obviously-invalid placeholder (format-valid example keys are squattable namespaces), enforced by a new validator rule.'),
    ('v0.1.9', '2026-08-11', 'obj-cas-imm-83b8c23a1baa',
     '"Try sgit in your browser" page: the real sgit-ai wheel running client-side under Pyodide (verified in headless Chromium first) — key derivation, encrypt/decrypt, an in-memory vault round trip, and a Python REPL. Plus: bootstrap fast-path for static hosting (no 2.5s bridge wait on GitHub Pages), CNAME for sgit.ai, and GitHub Pages deployment via Actions in the SGit-AI__Website repo.'),
    ('v0.1.8', '2026-08-11', 'obj-cas-imm-775783f31110',
     'Skills promoted to a top-level nav item with a new /skills page and the three agent skills shipped in the vault (latest versions, verbatim); llms.txt added at the vault root — encrypted for key-holders today, a standard public llms.txt when the site deploys to GitHub Pages; Home nav link retired (the brand mark covers it).'),
    ('v0.1.7', '2026-08-11', 'obj-cas-imm-c226a3aff160',
     'SG/Vault section rebuilt from the official docs bundle: corrected security-page structure-key claim to current reality, git page aligned with the publishing guide (three-rule boundary, leak audit, GitHub round trip, restore drill), new pages for static hosting on GitHub Pages, sub-vaults, and no-code content authoring; .gitignore extended with work/ and *.pem rules.'),
    ('v0.1.6', '2026-08-11', 'obj-cas-imm-f62d9bd2d0d4',
     'Corrected git integration to the side-by-side design: git now tracks the encrypted .sg_vault store (only the plaintext local/ folder is excluded), so a git remote doubles as a zero-knowledge mirror of the vault. Pattern documented on the git-and-vaults page.'),
    ('v0.1.5', '2026-08-11', 'obj-cas-imm-353038cc3e56',
     'Git integration: .gitignore (keeps .sg_vault/ — above all local/ keys and token — plus git metadata and build noise out of git and out of vault snapshots) and .gitattributes (raw sgit store files marked binary/-diff/-merge; generated *.html marked linguist-generated).'),
    ('v0.1.4', '2026-08-11', 'obj-cas-imm-90254d9591ff',
     'New SG/Vault section — for now the official sgraph platform documentation: SG/Vault & the platform, building vault apps, the window.sg bridge & host capabilities, and "git repos inside vaults" (engineering preview of the pure-Python git reader, verified against a real 906-commit repo).'),
    ('v0.1.3', '2026-08-11', 'obj-cas-imm-46a8b14d4fca',
     'Beta status (in production use), light theme, admin & engineering section, per-push version badge on every page, SG/Vault & SG/Send now link to sgraph.ai, design-improvements brief for Claude Code.'),
    ('v0.1.2', '2026-08-11', 'obj-cas-imm-c3084abbba8c',
     'Replaced the proposal app with the sgit.ai MVP site: 12 individually-navigable pages, shared CSS/JS loaded through the SG bridge, full-strength keys in all examples.'),
    ('v0.1.1', '2026-08-11', 'obj-cas-imm-7f1fbacf0485',
     'Initial vault app: the positioning & messaging proposal microsite with an embedded landing-page prototype.'),
]

ROOT = find_vault_root()

BOOT = """<script>
(function(){var R=document.documentElement.getAttribute('data-root')||'';var C=[R,'','../','/'].filter(function(v,i,a){return a.indexOf(v)===i});
function wait(ms){return new Promise(function(res){var t=Date.now();(function p(){if(window.sg)return res(window.sg);if(Date.now()-t>ms)return res(null);setTimeout(p,60)})()})}
function grab(sg,p){return new Promise(function(res){(async function(){if(sg&&sg.vfs&&sg.vfs.readText){try{var t=await sg.vfs.readText(p);if(t)return res(t)}catch(e){}}try{var r=await fetch(p);if(r.ok)return res(await r.text())}catch(e){}res(null)})()})}
async function css(sg){for(var i=0;i<C.length;i++){var p=C[i]+'assets/site.css';if(sg&&sg.loadCss){try{await sg.loadCss(p);return}catch(e){}}var t=await grab(sg,p);if(t){var s=document.createElement('style');s.textContent=t;document.head.appendChild(s);return}}}
async function js(sg){for(var i=0;i<C.length;i++){var p=C[i]+'assets/site.js';if(sg&&sg.loadJs){try{await sg.loadJs(p);return}catch(e){}}var t=await grab(sg,p);if(t){try{(0,eval)(t)}catch(e){console.error('[site] js failed',e)}return}}}
async function boot(){var inVault=false;try{inVault=(window!==window.parent)||location.protocol==='blob:'}catch(e){inVault=true}
var sg=inVault?await wait(2500):null;await css(sg);await js(sg);document.documentElement.classList.add('ready');try{window.parent&&window.parent.postMessage({type:'sg-app-ready'},'*')}catch(e){}}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',boot);else boot();})();
</script>"""

CRITICAL = ("<style>html{background:#faf9f5}body{margin:0;background:#faf9f5;color:#1c1d21;"
            "font-family:ui-sans-serif,system-ui,sans-serif;opacity:0;transition:opacity .25s}"
            "html.ready body{opacity:1}</style>")

def nav(p, here):
    def cls(k):
        return 'nl here' if k == here else 'nl'
    return f"""<nav class="site"><div class="row">
  <a class="brand" href="{p}index.html">sgit<span>.ai</span></a>
  <span class="stage-pill">beta</span>
  <a class="ver" href="{p}admin/versions.html" title="Site release history">{SITE_VERSION}</a>
  <a class="{cls('try')}" href="{p}try.html">Try</a>
  <a class="{cls('use-cases')}" href="{p}use-cases.html">Use Cases</a>
  <a class="{cls('docs')}" href="{p}docs/index.html">Docs</a>
  <a class="{cls('vault')}" href="{p}vault/index.html">SG/Vault</a>
  <a class="{cls('skills')}" href="{p}skills.html">Skills</a>
  <a class="{cls('security')}" href="{p}security.html">Security</a>
  <a class="gh" href="https://github.com/SGit-AI/SGit-AI__CLI">★ GitHub</a>
</div></nav>"""

def footer(p):
    return f"""<footer class="site"><div class="cols">
  <div>
    <div class="brandline">sgit<span>.ai</span></div>
    <p>sgit is git for encrypted vaults — clone, commit, branch and merge files that are encrypted with AES-256-GCM before they leave your machine. Open source, Apache-2.0, in beta and powering production workflows.</p>
    <p class="vaultnote">🔒 This site is itself served from an encrypted SG/Send vault — the page you are reading was decrypted in your browser. The medium is the message.</p>
    <p class="verline">site <a href="{p}admin/versions.html">{SITE_VERSION}</a> · <a href="{p}admin/index.html">engineering</a></p>
  </div>
  <div>
    <h4>Docs</h4>
    <a href="{p}docs/what-is-sgit.html">What is sgit</a>
    <a href="{p}docs/installation.html">Installation</a>
    <a href="{p}docs/quickstart.html">Quickstart</a>
    <a href="{p}docs/sgit-for-git-users.html">sgit for git users</a>
    <a href="{p}docs/agents.html">Working with AI agents</a>
    <a href="{p}docs/limitations.html">When NOT to use sgit</a>
  </div>
  <div>
    <h4>SG/Vault platform</h4>
    <a href="{p}vault/index.html">SG/Vault &amp; the platform</a>
    <a href="{p}vault/vault-apps.html">Building vault apps</a>
    <a href="{p}vault/sg-bridge.html">The window.sg bridge</a>
    <a href="{p}vault/content-authoring.html">Content authoring</a>
    <a href="{p}vault/sub-vaults.html">Sub-vaults</a>
    <a href="{p}vault/git-and-vaults.html">Git repos inside vaults</a>
    <a href="{p}vault/static-hosting.html">Static hosting</a>
    <a href="https://sgraph.ai">More at sgraph.ai</a>
  </div>
  <div>
    <h4>Project</h4>
    <a href="https://github.com/SGit-AI/SGit-AI__CLI">GitHub</a>
    <a href="{p}security.html">Security</a>
    <a href="{p}use-cases.html">Use cases</a>
    <a href="{p}skills.html">Skills for AI agents</a>
    <a href="{p}briefs.html">Cross-team briefs</a>
    <a href="{p}llms.txt">llms.txt</a>
    <a href="{p}admin/index.html">Admin &amp; engineering</a>
    <a href="{p}admin/versions.html">Release history</a>
  </div>
</div></footer>"""

def page(path, title, desc, here, body):
    p = '../' if '/' in path else ''
    html = f"""<!doctype html>
<html lang="en" data-root="{p}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
{CRITICAL}
</head>
<body>

{nav(p, here)}

{body}

{footer(p)}

{BOOT}
</body>
</html>
"""
    out = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w') as f:
        f.write(html)
    print('wrote', path, f'({len(html)} bytes)')


# ============================================================ index.html
INDEX = """<header class="hero">
  <div class="eyebrow">Agents need private, versioned state</div>
  <h1>The encrypted git for<br>humans and AI agents</h1>
  <p class="sub">Version, branch, and share vaults of files that are encrypted before they leave your machine. Zero knowledge: the server stores ciphertext, not your data.</p>
  <div class="ctas">
    <button class="pipbtn" type="button" data-copy="pip install sgit-ai">$ pip install sgit-ai <span class="cp">copy</span></button>
    <a class="cta2" href="try.html">Or try it in your browser →</a>
    <a class="cta2" href="docs/quickstart.html">5-minute quickstart →</a>
  </div>
  <p class="install-note">Pure Python · two runtime dependencies · Apache-2.0</p>
</header>

<!-- terminal walkthrough -->
<section class="band" id="demo">
  <div class="term">
    <div class="ttabs">
      <button class="ttab active" data-pane="t1" data-cap="The vault key is the address, the auth, and the encryption key — one high-entropy string. Keep it safe." type="button"><span class="n">1</span>Create</button>
      <button class="ttab" data-pane="t2" data-cap="Same muscle memory as git. No staging area: commit snapshots the folder." type="button"><span class="n">2</span>Work like git</button>
      <button class="ttab" data-pane="t3" data-cap="Full history and diffs — decrypted locally, never on the server." type="button"><span class="n">3</span>History &amp; diffs</button>
      <button class="ttab" data-pane="t4" data-cap="Only ciphertext travels. Another machine — or another agent — clones with the key." type="button"><span class="n">4</span>Sync</button>
      <button class="ttab" data-pane="t5" data-cap="Tab 5 is the command your AI agent uses." type="button"><span class="n">5</span>Agent mode</button>
    </div>
    <div class="tbody">
      <div class="pane active" id="t1">
<span class="p">$</span> <span class="cmd">sgit create my-vault</span><br>
<span class="g">✓</span> Vault created and registered<br>
<span class="g">✓</span> Initial commit pushed<br><br>
&nbsp;&nbsp;Vault key: <span class="y">&lt;24-char-passphrase&gt;:&lt;vault-id&gt;</span><br><br>
<span class="d">Keep this safe — it is the address, the auth, and the</span><br>
<span class="d">encryption key in one string. Without it, nobody — including</span><br>
<span class="d">the server — can read this vault.</span>
      </div>
      <div class="pane" id="t2">
<span class="p">$</span> <span class="cmd">vim notes/positioning.md</span><br>
<span class="p">$</span> <span class="cmd">sgit status</span><br>
&nbsp;&nbsp;On clone branch <span class="cy">branch-clone-3f9c</span> → named branch <span class="cy">main</span><br>
&nbsp;&nbsp;<span class="y">modified:</span>&nbsp;&nbsp;notes/positioning.md<br>
&nbsp;&nbsp;<span class="g">added:</span>&nbsp;&nbsp;&nbsp;&nbsp;drafts/hero-copy.md<br><br>
<span class="p">$</span> <span class="cmd">sgit commit -m "first draft of hero copy"</span><br>
<span class="g">✓</span> Committed 2 files <span class="d">(no staging area — commit snapshots the folder)</span>
      </div>
      <div class="pane" id="t3">
<span class="p">$</span> <span class="cmd">sgit history log --oneline</span><br>
<span class="y">c4e81a</span> first draft of hero copy<br>
<span class="y">b2d70f</span> initial commit<br><br>
<span class="p">$</span> <span class="cmd">sgit history diff</span><br>
<span class="d">--- a/notes/positioning.md</span><br>
<span class="d">+++ b/notes/positioning.md</span><br>
<span class="r">- sgit is a CLI for encrypted sync</span><br>
<span class="g">+ sgit is git for encrypted vaults</span>
      </div>
      <div class="pane" id="t4">
<span class="p">$</span> <span class="cmd">sgit push</span><br>
<span class="g">✓</span> Pushed 2 objects <span class="d">(delta push — only changed, only ciphertext)</span><br><br>
<span class="d"># on another machine (or another agent)</span><br>
<span class="p">$</span> <span class="cmd">sgit clone &lt;vault-key&gt;</span><br>
<span class="g">✓</span> Cloned and decrypted 12 files<br><br>
<span class="p">$</span> <span class="cmd">sgit pull</span><br>
<span class="g">✓</span> Up to date
      </div>
      <div class="pane" id="t5">
<span class="d"># one call: encrypt, commit, push, machine-readable result —</span><br>
<span class="d"># no working-directory scan, no full clone needed</span><br>
<span class="p">$</span> <span class="cmd">sgit write notes/finding.md --file result.md \\</span><br>
<span class="cmd">&nbsp;&nbsp;&nbsp;&nbsp;--message "agent A: analysis" --push --json</span><br>
{<br>
&nbsp;&nbsp;<span class="cy">"status"</span>: <span class="g">"pushed"</span>,<br>
&nbsp;&nbsp;<span class="cy">"path"</span>: <span class="g">"notes/finding.md"</span>,<br>
&nbsp;&nbsp;<span class="cy">"blob_id"</span>: <span class="g">"obj-cas-imm-9c2e41ab77d0"</span><br>
}
      </div>
    </div>
    <p class="tcap" id="tcap">The vault key is the address, the auth, and the encryption key — one high-entropy string. Keep it safe.</p>
  </div>
</section>

<!-- durable identity + features -->
<section class="band alt" id="features">
  <h2>Git workflows. Encrypted vaults. Zero knowledge.</h2>
  <p class="blurb">sgit is git for encrypted vaults: clone, commit, branch, diff and merge folders of files that are encrypted with AES-256-GCM before they leave your machine.</p>
  <div class="feat">
    <div class="f rev"><b>Git-like version control</b><span>commit, branch, merge, diff, log, stash, revert your encrypted files</span></div>
    <div class="f rev"><b>Client-side encryption</b><span>AES-256-GCM before upload; keys derived from your vault key, never sent to the server</span></div>
    <div class="f rev"><b>Real three-way merge</b><span>conflict files plus a base/ours/theirs <code>resolve --show</code> view</span></div>
    <div class="f rev"><b>The two-branch model</b><span>a private clone branch per machine or agent; shared named branches for collaboration</span></div>
    <div class="f rev"><b>Sparse &amp; thin clones</b><span>structure now, content on demand — for agents on a time budget</span></div>
    <div class="f rev"><b>Browser interop</b><span>open the same vault in SG/Vault on the web — CLI and browser speak one wire format</span></div>
  </div>
</section>

<!-- server sees -->
<section class="band" id="zero-knowledge">
  <h2>What the server sees</h2>
  <div class="sees">
    <div class="cols">
      <div class="col you rev">
        <h3>Your machine</h3>
        <ul>
          <li>filenames &amp; folder structure</li>
          <li>file contents</li>
          <li>commit messages</li>
          <li>branch names</li>
          <li>the vault key &amp; derived keys</li>
        </ul>
      </div>
      <div class="arrow">
        <svg width="46" height="24" viewBox="0 0 46 24" fill="none"><path d="M2 12h36m0 0-7-7m7 7-7 7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </div>
      <div class="col srv rev">
        <h3>The server</h3>
        <ul>
          <li>obj-cas-imm-3f9c41ab77d0</li>
          <li>ref-pid-muw-8e02cc194b3a</li>
          <li>ciphertext blobs (AES-256-GCM)</li>
          <li>object sizes · timestamps</li>
          <li>the vault id</li>
        </ul>
      </div>
    </div>
    <p class="cap">That's the whole list — and we publish the threat model, including what the server <em>can</em> see (sizes, timing, vault ID). <a href="security.html">Read the security model →</a></p>
  </div>
</section>

<!-- agents -->
<section class="band alt" id="agents">
  <h2>Built for agents</h2>
  <p class="blurb">Agents need shared state. Shared state needs versioning — and privacy. sgit is the encrypted, versioned workspace for humans and AI agents.</p>
  <div class="cards">
    <div class="card rev"><span class="tag">Persistent memory</span><h3>A vault is just a folder</h3><p>An agent clones it, reads and writes files normally, commits, pushes. The next session pulls and continues. State survives the context window.</p></div>
    <div class="card rev"><span class="tag">Multi-agent, human-merged</span><h3>A branch per agent</h3><p>Each agent gets its own private clone branch; work meets on named branches; a human reviews the merge — in the terminal or in the SG/Vault browser.</p></div>
    <div class="card rev"><span class="tag">Agent-grade plumbing</span><h3>Machine-readable everything</h3><p><code>sgit write</code> for surgical single-call commits, <code>--json</code> on every read path, <code>cat --id</code> with zero network calls, sparse clones for fast cold starts.</p></div>
  </div>
  <p class="blurb" style="margin-top:1.6rem;margin-bottom:0"><a href="docs/agents.html">Read the agent guide →</a> &nbsp;·&nbsp; <a href="skills.html">Install the skills →</a> &nbsp;·&nbsp; <a href="llms.txt">llms.txt</a></p>
</section>

<!-- use cases -->
<section class="band" id="use-cases">
  <h2>What people use it for</h2>
  <div class="cards">
    <a class="card rev" href="use-cases.html#ai-agents"><span class="tag">Use case</span><h3>Private memory for AI agents</h3><p>Durable, versioned state between sessions — encrypted end to end.</p><span class="go">Read →</span></a>
    <a class="card rev" href="use-cases.html#multi-agent"><span class="tag">Use case</span><h3>Multi-agent collaboration</h3><p>Agents on their own branches, humans reviewing the merge.</p><span class="go">Read →</span></a>
    <a class="card rev" href="use-cases.html#human-ai"><span class="tag">Use case</span><h3>Human ↔ agent workspaces</h3><p>You in the SG/Vault browser, the agent in the CLI — same vault.</p><span class="go">Read →</span></a>
    <a class="card rev" href="use-cases.html#encrypted-backup"><span class="tag">Use case</span><h3>Encrypted folders with history</h3><p>A shared folder the hosting provider cannot read, with rollback.</p><span class="go">Read →</span></a>
    <a class="card rev" href="use-cases.html#secure-file-exchange"><span class="tag">Use case</span><h3>Signed &amp; encrypted exchange</h3><p>PKI: sign, verify, encrypt and decrypt files for named recipients.</p><span class="go">Read →</span></a>
  </div>
</section>

<!-- trust -->
<section class="band alt" id="trust">
  <h2>In production — and honest about it</h2>
  <p class="blurb">sgit is in beta, powering production workflows daily. No superlatives — just the evidence, and a page that tells you when <em>not</em> to use it.</p>
  <div class="trust">
    <span><b>~4,000</b> tests</span>
    <span><b>mutation testing</b> in CI</span>
    <span><b>integration tests</b> against a real server</span>
    <span><b>2</b> runtime dependencies</span>
    <span><b>Apache-2.0</b></span>
    <span><a href="security.html"><b>security model</b> published</a></span>
    <span><a href="docs/limitations.html"><b>when NOT</b> to use sgit</a></span>
  </div>
</section>

<!-- ecosystem -->
<section class="band" id="ecosystem">
  <h2>One vault, three doors</h2>
  <div class="eco">
    <div class="e rev"><div class="think">Think of it as</div><b>sgit</b> <span class="as">— git, for encrypted vaults</span><p>Open source CLI. Free. Apache-2.0. <code>pip install sgit-ai</code></p></div>
    <div class="e rev"><div class="think">Think of it as</div><b>SG/Vault</b> <span class="as">— the web app for your vaults</span><p>Browse, edit and review the same vaults in the browser — an independent implementation of the same wire format.</p><p><a href="vault/index.html">Platform docs →</a> · <a href="https://sgraph.ai">sgraph.ai</a></p></div>
    <div class="e rev"><div class="think">Think of it as</div><b>SG/Send</b> <span class="as">— the transfer API underneath</span><p>The zero-knowledge storage service both clients speak to — the same server the integration tests run against.</p><p><a href="vault/index.html">Platform docs →</a> · <a href="https://sgraph.ai">sgraph.ai</a></p></div>
  </div>
</section>

<!-- closer -->
<section class="band alt" id="get-started">
  <div class="triplet" style="margin-bottom:1.4rem">Encrypted vaults. <b>Git workflows.</b> Zero knowledge.</div>
  <div class="ctas">
    <button class="pipbtn" type="button" data-copy="pip install sgit-ai">$ pip install sgit-ai <span class="cp">copy</span></button>
    <a class="cta2" href="docs/quickstart.html">5-minute quickstart →</a>
    <a class="cta2" href="https://github.com/SGit-AI/SGit-AI__CLI">Star on GitHub →</a>
  </div>
</section>"""

# ============================================================ use-cases.html
UC = """<main class="doc">
  <h1>Use cases</h1>
  <p class="lead">Five things people point sgit at today. Every workflow below runs on shipped commands — nothing aspirational.</p>

  <section class="uc" id="ai-agents">
    <h2>Private memory for AI agents</h2>
    <p>An agent's context window ends; its work shouldn't. A vault is just a folder — the agent clones it, reads and writes files normally, commits, and pushes. The next session pulls and continues where the last one stopped. Everything is encrypted before it leaves the agent's machine, so the shared state can hold things you would never put in a third-party database: client documents, security findings, personal data.</p>
<pre class="shell"><span class="d"># session 1</span>
<span class="p">$</span> <span class="cmd">sgit clone &lt;vault-key&gt; workspace</span>
<span class="p">$</span> <span class="cmd">sgit commit -m "session 1: research notes" &amp;&amp; sgit push</span>
<span class="d"># session 2, days later, different machine</span>
<span class="p">$</span> <span class="cmd">sgit pull</span>   <span class="d"># continue exactly where session 1 stopped</span></pre>
    <p><a href="docs/agents.html">Full agent guide →</a></p>
  </section>

  <section class="uc" id="multi-agent">
    <h2>Multi-agent collaboration</h2>
    <p>Give each agent its own named branch. Every clone also gets a private clone branch whose key never leaves that agent's session, so agents cannot trample each other's work-in-progress. Work meets on named branches, and a human reviews the merge. Agents can inspect each other's commits read-only with <code>sgit history show</code> and <code>sgit history diff</code> — without pulling, so looking never means merging.</p>
<pre class="shell"><span class="d"># agent A</span>  <span class="p">$</span> <span class="cmd">sgit branch new feature-analysis</span> … <span class="cmd">sgit push</span>
<span class="d"># agent B</span>  <span class="p">$</span> <span class="cmd">sgit branch new feature-report</span>   … <span class="cmd">sgit push</span>
<span class="d"># human  </span>  <span class="p">$</span> <span class="cmd">sgit pull</span> → review → merge, with <span class="cmd">sgit resolve --show</span> on conflicts</pre>
  </section>

  <section class="uc" id="human-ai">
    <h2>Human ↔ agent workspaces</h2>
    <p>The same vault has two doors: you in the SG/Vault web app, the agent in the CLI. The browser client is an independent implementation of the same wire format — you browse, edit and review in a UI while the agent works the same files from the terminal. Both sides see each other's commits; neither side's plaintext ever touches the server. (How the browser side works: <a href="https://sgraph.ai">sgraph.ai</a>.)</p>
<pre class="shell"><span class="p">$</span> <span class="cmd">sgit vault info</span>
  Web URL: <span class="cy">https://vault.sgraph.ai/en-gb/#&lt;your-vault-key&gt;</span></pre>
  </section>

  <section class="uc" id="encrypted-backup">
    <h2>Encrypted folders with history</h2>
    <p>A shared folder where the hosting provider cannot read the contents — with commits, diffs, and rollback. Work offline, commit locally, push when ready; restore any prior version with <code>sgit history revert</code>. Vault-level <code>backup</code> and <code>restore</code> produce portable archives, and <code>sgit vault move</code> rotates keys if a key is ever exposed.</p>
<pre class="shell"><span class="p">$</span> <span class="cmd">sgit init --existing</span>        <span class="d"># vault-ify a folder you already have</span>
<span class="p">$</span> <span class="cmd">sgit commit -m "baseline" &amp;&amp; sgit push</span>
<span class="p">$</span> <span class="cmd">sgit history revert --commit obj-cas-imm-b2d70f</span>   <span class="d"># roll back</span></pre>
  </section>

  <section class="uc" id="secure-file-exchange">
    <h2>Signed &amp; encrypted file exchange</h2>
    <p>Alongside vault sync, sgit ships a PKI toolset: generate keypairs, exchange public keys as contact bundles, then sign, verify, encrypt and decrypt individual files for named recipients — useful when a file has to travel outside a vault but still needs integrity and confidentiality.</p>
<pre class="shell"><span class="p">$</span> <span class="cmd">sgit pki keygen --label "release keys"</span>
<span class="p">$</span> <span class="cmd">sgit pki sign report.pdf --fingerprint &lt;fp&gt;</span>
<span class="p">$</span> <span class="cmd">sgit pki encrypt report.pdf --recipient &lt;fp&gt;</span></pre>
  </section>
</main>"""

# ============================================================ security.html
SEC = """<main class="doc">
  <h1>Security model</h1>
  <p class="lead">Zero knowledge, precisely stated: every file is encrypted on your machine before upload, keys are derived locally from your vault key, and the server stores ciphertext under opaque identifiers. This page tells you exactly what that means — including what the server <em>can</em> see.</p>

  <h2 id="server-sees">What the server sees — and never sees</h2>
  <div class="tablewrap"><table>
    <tr><th>The server never sees</th><th>The server does see</th></tr>
    <tr><td>File contents (encrypted client-side, AES-256-GCM)</td><td>The vault ID (an opaque random identifier)</td></tr>
    <tr><td>Filenames and folder structure</td><td>Encrypted object sizes</td></tr>
    <tr><td>Commit messages and branch names</td><td>Timing of reads and writes</td></tr>
    <tr><td>Your vault key or any derived key</td><td>Approximate activity volume (object counts)</td></tr>
  </table></div>
  <p class="small dim">We state the right-hand column deliberately. Traffic analysis of sizes and timing is a real (if narrow) channel, and pretending otherwise would be marketing, not security.</p>

  <h2 id="crypto">The crypto stack</h2>
  <div class="tablewrap"><table>
    <tr><th>Layer</th><th>Construction</th></tr>
    <tr><td>Content encryption</td><td>AES-256-GCM, 12-byte IV, 16-byte tag — byte-compatible with the browser's Web Crypto API</td></tr>
    <tr><td>Key derivation from the vault key</td><td>PBKDF2-HMAC-SHA256, 600,000 iterations, distinct per-vault salts for read and write keys</td></tr>
    <tr><td>Purpose-specific keys</td><td>HKDF-SHA256 — per-file keys and a structure key, one-way derived from the read key</td></tr>
    <tr><td>Server-side identifiers</td><td>HMAC-SHA256-derived opaque IDs — the server addresses files it cannot name</td></tr>
    <tr><td>Object identity</td><td>Content-addressed: <code>obj-cas-imm-&lt;sha256-prefix&gt;</code> over ciphertext, enabling dedup without plaintext knowledge</td></tr>
  </table></div>
  <p>One precision note, because precision beats marketing: the key hierarchy derives a <em>structure key</em> (one-way from the read key) designed to separate access to vault metadata from access to file contents. Today, vault objects are encrypted under the read key — activating the structure-key split across structural objects is an in-progress, reviewed design change, and this page will say so when it lands, not before.</p>

  <h2 id="keys">Key strength</h2>
  <p>Vault keys are generated, not chosen. A generated passphrase is 24 characters over a 36-symbol alphabet — about <b>124 bits of entropy</b> (36<sup>24</sup> ≈ 2<sup>124</sup>), far beyond brute-force reach — before key derivation adds 600,000 rounds of PBKDF2-SHA256 on top. The key never travels to the server: it is the address, the credential, and the root of the encryption hierarchy in one string, and it stays on your machines.</p>
  <div class="warnbox"><b>Consequence you should want:</b> there is no password reset. If you lose the vault key, nobody — including us — can recover the contents. Keep it in a password manager, and use <code>sgit vault backup</code> for belt-and-braces.</div>

  <h2 id="interop">Two implementations, one wire format</h2>
  <p>The sgit CLI and the SG/Vault browser client are independent implementations of the same encrypted wire format, kept interoperable through a versioned contract with test vectors. Every crypto operation must produce byte-for-byte identical output to the Web Crypto API given the same inputs — that requirement is enforced with mandatory test vectors, and it means a second, independent codebase continuously exercises the same format. (More on the browser side at <a href="https://sgraph.ai">sgraph.ai</a>.)</p>

  <h2 id="secrets">Secrets safety by default</h2>
  <p>sgit is not a secrets manager, and it actively refuses to become an accidental one: files like <code>.env*</code>, <code>.netrc</code>, <code>.pgpass</code>, <code>.git-credentials</code> and private key files (<code>id_rsa</code>, …) are <em>always</em> excluded from commits, so a stray credential can't get swept into a vault snapshot.</p>

  <h2 id="process">Open security process</h2>
  <ul>
    <li>Open source under Apache-2.0, with a deliberately tiny dependency surface: two runtime dependencies.</li>
    <li>~4,000 tests including mutation testing in CI and integration tests against a real server — no mocks.</li>
    <li>An internal security review series (twelve findings, each individually worked through and debriefed — covering key residency, IV determinism trade-offs, logging hygiene, and more) is being prepared for publication on this page.</li>
    <li>Found something? Report it via <a href="https://github.com/SGit-AI/SGit-AI__CLI/issues">GitHub</a> — security reports get priority.</li>
    <li><b>Key exposed?</b> <a href="docs/exposed-vault-key.html">The rotation runbook</a> — including a worked case study of the day this site's own vault key leaked, and what it cost to fix.</li>
  </ul>

  <div class="note"><b>Honesty note:</b> sgit is in beta — it powers production workflows daily, and the cryptography is conservative and standard (AES-GCM, PBKDF2, HKDF — nothing exotic). Still: read <a href="docs/limitations.html">when NOT to use sgit</a> before trusting it with anything critical.</div>
</main>"""

# ============================================================ try.html
TRY = """<main class="doc" style="max-width:840px">
  <h1>Try sgit in your browser</h1>
  <p class="lead">This page downloads a Python runtime (Pyodide, ~20&nbsp;MB) and installs the <b>real <code>sgit-ai</code> wheel from PyPI</b> — the same code <code>pip install</code> gives you — then runs it right here: a working terminal with the actual <code>sgit</code> CLI, an in-memory filesystem, and a network transport routed through your browser. Keys are derived and content encrypted locally; nothing you type leaves this page except the ciphertext sgit itself sends when <em>you</em> run a network command.</p>
  <div class="note"><b>What this is:</b> sgit's engine, client-side. File commands run against this tab's in-memory filesystem (gone on refresh; the remote vault persists). Network commands (<code>clone</code>, <code>push</code>, <code>pull</code>, <code>doctor</code>) go straight from your browser to the SG/Send servers over CORS — the page freezes while they run (synchronous transport; it's a demo, not a product). First load is heavy (~20&nbsp;MB, cached afterwards); 600,000 PBKDF2 rounds take ~1–2&nbsp;s in WebAssembly.</div>

  <div class="btnrow">
    <button class="btn" id="btn-load" type="button">Load the sgit engine (~20 MB)</button>
  </div>
  <div class="try-term" id="term">— engine not loaded —</div>

  <div class="btnrow">
    <button class="btn alt" id="btn-keys" type="button" disabled>1 · Derive vault keys</button>
    <button class="btn alt" id="btn-crypt" type="button" disabled>2 · Encrypt &amp; decrypt</button>
    <button class="btn alt" id="btn-vault" type="button" disabled>3 · In-memory vault round trip</button>
  </div>

  <h2>The terminal</h2>
  <p class="small dim">The real <code>sgit</code> CLI plus a small toolbox of file commands (<code>ls</code>, <code>cd</code>, <code>cat</code>, <code>mkdir</code>, <code>echo &gt; file</code>, <code>tree</code>, …). Type <code>help</code> for the list. History with ↑/↓.</p>
  <div class="try-term" id="shterm">— load the engine above to start —</div>
  <div class="shrow">
    <span class="shp" id="shp">/workspace $</span>
    <input class="shin" id="shin" type="text" spellcheck="false" autocomplete="off" disabled placeholder="help">
  </div>
<pre class="shell"><span class="d"># a session to try (the vault key can be any vault you hold a key for):</span>
<span class="cmd">sgit init my-vault</span>&nbsp;&nbsp;<span class="cmd">cd my-vault</span>&nbsp;&nbsp;<span class="cmd">echo "hello" &gt; notes.md</span>
<span class="cmd">sgit status</span>&nbsp;&nbsp;<span class="cmd">sgit commit -m "from a browser"</span>
<span class="d"># and the one that makes it real — clone straight from the SG/Send servers:</span>
<span class="cmd">sgit clone &lt;vault-key&gt; demo</span>&nbsp;&nbsp;<span class="cmd">cd demo</span>&nbsp;&nbsp;<span class="cmd">ls</span>&nbsp;&nbsp;<span class="cmd">sgit history log --oneline</span></pre>

  <h2>Python console</h2>
  <p class="small dim">The full <code>sgit_ai</code> package is importable. The last expression's value is printed.</p>
  <textarea class="pyin" id="pyin" spellcheck="false">from sgit_ai.crypto.Vault__Crypto import Vault__Crypto
vc = Vault__Crypto()
vc.derive_keys('my-passphrase', 'DEMO-VAULT')</textarea>
  <div class="btnrow"><button class="btn alt" id="btn-run" type="button" disabled>Run</button></div>

  <p class="small dim">How this works: <a href="vault/static-hosting.html">the same site</a> serves from an encrypted vault or GitHub Pages; this page pulls Pyodide from a CDN and the wheel from PyPI at runtime, so it needs an internet connection — the one page on this site that does.</p>
</main>

<script>
(function(){
  'use strict';
  var py = null;
  var term = null;

  async function grabText(path){
    try { if (window.sg && window.sg.vfs && window.sg.vfs.readText) { var t = await window.sg.vfs.readText(path); if (t) return t; } } catch(e){}
    try { var r = await fetch(path); if (r.ok) return await r.text(); } catch(e){}
    return null;
  }

  function tlog(msg){
    if (!term) term = document.getElementById('term');
    if (term.textContent === '— engine not loaded —') term.textContent = '';
    term.textContent += msg + '\\n';
    term.scrollTop = term.scrollHeight;
  }
  function setEnabled(on){
    ['btn-keys','btn-crypt','btn-vault','btn-run'].forEach(function(id){
      var el = document.getElementById(id); if (el) el.disabled = !on;
    });
  }

  async function loadEngine(){
    var btn = document.getElementById('btn-load');
    btn.disabled = true; btn.textContent = 'Loading…';
    try {
      tlog('› fetching Pyodide (CPython 3.12 → WebAssembly)…');
      var loadPyodide = null;
      try {
        var sgMod = await import('https://tools.sgraph.ai/core/pyodide/v1/v1.0/v1.0.0/sg-pyodide.js');
        loadPyodide = function(){ return sgMod.loadPyodide({ onProgress: function(e){ tlog('  [' + (e.stage||'') + '] ' + (e.detail||'')); } }); };
        tlog('  using sg-pyodide loader from tools.sgraph.ai');
      } catch (e) {
        tlog('  tools.sgraph.ai unavailable — falling back to jsDelivr');
        var offMod = await import('https://cdn.jsdelivr.net/pyodide/v0.27.4/full/pyodide.mjs');
        loadPyodide = function(){ return offMod.loadPyodide({ indexURL: 'https://cdn.jsdelivr.net/pyodide/v0.27.4/full/' }); };
      }
      var t0 = Date.now();
      py = await loadPyodide();
      tlog('✓ Pyodide ready in ' + ((Date.now()-t0)/1000).toFixed(1) + 's');
      py.setStdout({ batched: function(s){ tlog(s); } });
      py.setStderr({ batched: function(s){ tlog('! ' + s); } });

      tlog('› loading cryptography (WASM), micropip, ssl…');
      await py.loadPackage(['cryptography', 'micropip', 'ssl']);
      var micropip = py.pyimport('micropip');

      tlog('› installing osbot-utils from PyPI…');
      await micropip.install('osbot-utils');

      tlog('› installing the real sgit-ai wheel from PyPI…');
      var meta  = await (await fetch('https://pypi.org/pypi/sgit-ai/json')).json();
      var wheel = null;
      for (var i = 0; i < meta.urls.length; i++) if (meta.urls[i].filename.slice(-4) === '.whl') wheel = meta.urls[i];
      var bytes = new Uint8Array(await (await fetch(wheel.url)).arrayBuffer());
      py.FS.writeFile('/tmp/' + wheel.filename, bytes);
      await micropip.install.callKwargs('emfs:///tmp/' + wheel.filename, { deps: false });
      tlog('✓ installed ' + wheel.filename);

      await py.runPythonAsync('import sgit_ai');

      tlog('› wiring the browser network transport + terminal…');
      var setup = await grabText('assets/try-setup.py');
      if (setup) { await py.runPythonAsync(setup); tlog('✓ terminal ready — network transport routed through this browser.'); shellReady(); }
      else { tlog('! terminal setup not found — demos and console still work.'); }

      tlog('✓ sgit engine loaded — the buttons and terminal below run the real thing.');
      btn.textContent = 'Engine loaded ✓';
      setEnabled(true);
    } catch (e) {
      tlog('✗ load failed: ' + e);
      tlog('  (This page needs internet access to a CDN and PyPI. If you are viewing');
      tlog('   it inside a restricted context, try the hosted site at sgit.ai.)');
      btn.disabled = false; btn.textContent = 'Retry load';
    }
  }

  async function runPy(code, label){
    if (!py) return;
    if (label) tlog('\\n$ ' + label);
    try {
      var out = await py.runPythonAsync(code);
      if (out !== undefined && out !== null) tlog(String(out));
    } catch (e) {
      tlog('✗ ' + e);
    }
  }

  var DEMO_KEYS = [
    "import time, json",
    "from sgit_ai.crypto.Vault__Crypto import Vault__Crypto",
    "vc = Vault__Crypto()",
    "t0 = time.time()",
    "keys = vc.derive_keys('not-a-real-passphrase', 'DEMO-VAULT')",
    "ms = int((time.time()-t0)*1000)",
    "rk = vc.derive_read_key('not-a-real-passphrase', 'DEMO-VAULT')",
    "print(f'PBKDF2-SHA256 x 600,000 iterations: {ms} ms (in WebAssembly)')",
    "print('read key   :', rk.hex()[:32] + '…')",
    "print('ref file id:', 'ref-pid-muw-' + vc.derive_ref_file_id(rk, 'DEMO-VAULT'))",
    "'— keys derived locally; the passphrase never left this page —'"
  ].join('\\n');

  var DEMO_CRYPT = [
    "from sgit_ai.crypto.Vault__Crypto import Vault__Crypto",
    "vc = Vault__Crypto()",
    "rk = vc.derive_read_key('not-a-real-passphrase', 'DEMO-VAULT')",
    "ct = vc.encrypt_metadata(rk, 'the server never sees this sentence')",
    "print('ciphertext (AES-256-GCM, b64):', ct[:56] + '…')",
    "pt = vc.decrypt_metadata(rk, ct)",
    "print('decrypted  :', pt)",
    "'— round trip: ' + ('OK' if pt == 'the server never sees this sentence' else 'FAILED') + ' —'"
  ].join('\\n');

  var DEMO_VAULT = [
    "from sgit_ai.crypto.Vault__Crypto import Vault__Crypto",
    "from sgit_ai.network.api.Vault__API__In_Memory import Vault__API__In_Memory",
    "vc  = Vault__Crypto()",
    "api = Vault__API__In_Memory().setup()",
    "rk  = vc.derive_read_key('not-a-real-passphrase', 'DEMO-VAULT')",
    "plaintext = b'hello from an in-browser vault'",
    "ct  = vc.encrypt(rk, plaintext)",
    "oid = vc.compute_object_id(ct)",
    "api.write('DEMO-VAULT', oid, 'write-key', ct)",
    "print('stored object:', oid, f'({len(ct)} encrypted bytes)')",
    "back = vc.decrypt(rk, bytes(api.read('DEMO-VAULT', oid)))",
    "print('read back    :', back.decode())",
    "'— content-addressed, encrypted, round-tripped — entirely in this tab —'"
  ].join('\\n');

  var shHist = [], shIdx = -1;
  function shlog(msg){
    var t = document.getElementById('shterm');
    if (t.textContent === '— load the engine above to start —') t.textContent = '';
    t.textContent += msg + '\\n';
    t.scrollTop = t.scrollHeight;
  }
  function shellReady(){
    var inp = document.getElementById('shin');
    inp.disabled = false;
    shlog("sgit terminal ready — type 'help' to see what's here.");
    inp.addEventListener('keydown', async function(ev){
      if (ev.key === 'ArrowUp'){ if (shIdx < shHist.length - 1){ shIdx++; inp.value = shHist[shHist.length - 1 - shIdx]; } ev.preventDefault(); return; }
      if (ev.key === 'ArrowDown'){ if (shIdx > 0){ shIdx--; inp.value = shHist[shHist.length - 1 - shIdx]; } else { shIdx = -1; inp.value = ''; } ev.preventDefault(); return; }
      if (ev.key !== 'Enter') return;
      var line = inp.value; inp.value = ''; shIdx = -1;
      if (line.trim()) shHist.push(line);
      shlog(document.getElementById('shp').textContent + ' ' + line);
      if (!line.trim()) return;
      var lc = line.trim();
      if (/^sgit(-ai)?\s+(clone|push|pull|fetch|doctor|remote)/.test(lc)) {
        shlog('⏳ contacting the SG/Send servers — the tab freezes until this returns (synchronous transport; output appears on completion)…');
        await new Promise(function(r){ setTimeout(r, 30); });   // let the notice paint before the blocking call
      }
      inp.disabled = true;
      try {
        py.globals.set('__CMD', line);
        var out = await py.runPythonAsync('__sh(__CMD)');
        if (out === '\\x00__CLEAR__') { document.getElementById('shterm').textContent = ''; }
        else if (out) shlog(out);
        var cwd = await py.runPythonAsync('import os; os.getcwd()');
        document.getElementById('shp').textContent = cwd + ' $';
      } catch (e) { shlog('✗ ' + e); }
      inp.disabled = false; inp.focus();
    });
  }

  document.getElementById('btn-load').addEventListener('click', loadEngine);
  document.getElementById('btn-keys').addEventListener('click', function(){ runPy(DEMO_KEYS, 'derive vault keys'); });
  document.getElementById('btn-crypt').addEventListener('click', function(){ runPy(DEMO_CRYPT, 'encrypt / decrypt'); });
  document.getElementById('btn-vault').addEventListener('click', function(){ runPy(DEMO_VAULT, 'in-memory vault round trip'); });
  document.getElementById('btn-run').addEventListener('click', function(){ runPy(document.getElementById('pyin').value, 'console'); });
})();
</script>"""

# ============================================================ skills.html
SKILLS = """<main class="doc">
  <h1>Skills — sgit for AI agents</h1>
  <p class="lead">A skill is a packaged set of instructions an AI agent loads to do a job well: the commands that matter, the patterns that work, the traps already hit and documented so the agent doesn't hit them again. sgit treats agents as first-class users, so its skills are first-class artifacts — versioned, verified against specific releases, and shipped right here in this vault.</p>

  <h2>The three skills</h2>
  <div class="dochub">
    <div class="grp">
      <h2>Operate</h2>
      <a href="skills/use_sgit-and-vaults__SKILL.md">use sgit and vaults<small>The CLI end to end — and the cross-session pattern: clone/pull at session start, commit + push at session end, so state survives the context window. Includes the multi-agent branch-per-agent workflow.</small></a>
    </div>
    <div class="grp">
      <h2>Build</h2>
      <a href="skills/create-vault-apps__SKILL.md">create vault apps<small>The vault-app playbook: the authoring contract, what the host gives you for free, proven layout patterns, the validation gate, and a nine-row table of failure modes with fixes — all bug-fixed against real vault behaviour.</small></a>
    </div>
    <div class="grp">
      <h2>Author</h2>
      <a href="skills/create-vault-content__SKILL.md">create vault content<small>Structured content without code: the full _page.json schema (embedded — no repo clone needed) and vault markdown authoring, with checklists and copy-paste templates.</small></a>
    </div>
  </div>

  <h2>Installing a skill</h2>
  <p>For Claude Code and compatible agents: drop the skill file into your skills directory (e.g. <code>~/.claude/skills/&lt;name&gt;/SKILL.md</code>) or paste it into the session as context. The skill's own description tells the agent when to trigger it. A minimal bootstrap for a fresh session is one line:</p>
<pre class="shell"><span class="p">$</span> <span class="cmd">pip install sgit-ai &amp;&amp; sgit clone &lt;vault-key&gt; workspace</span>
<span class="d"># then read skills/ inside any vault that ships them — like this one</span></pre>
  <p>The skills above are the canonical current versions, verified against sgit-ai v0.14.x and the current app-shell. They carry their own honesty markers — including which CLI commands are disabled right now and which platform features are trial-only — so an agent reading them gets ground truth, not marketing.</p>

  <div class="note"><b>Also for agents:</b> this site ships an <a href="llms.txt">llms.txt</a> at the vault root — the standard machine-readable index. Inside the vault it is encrypted like everything else (agents holding the key read it via <code>sgit cat llms.txt</code>); on a static deployment it becomes a plain public llms.txt. Same file, two trust contexts.</div>

  <div class="pagenav"><a href="docs/agents.html">← Working with AI agents</a><a href="vault/index.html">The SG/Vault platform →</a></div>
</main>"""

# ============================================================ docs/index.html
DOCS_HUB = """<main class="doc">
  <h1>Documentation</h1>
  <p class="lead">Start with the five-minute quickstart. If you know git, the Rosetta stone will make sgit feel familiar in one read.</p>
  <div class="dochub">
    <div class="grp">
      <h2>Introduction</h2>
      <a href="what-is-sgit.html">What is sgit<small>The pitch, the mechanism, the architecture</small></a>
      <a href="installation.html">Installation<small>pip install, verify, upgrade</small></a>
      <a href="quickstart.html">Quickstart<small>Create, commit, push, clone — in 5 minutes</small></a>
    </div>
    <div class="grp">
      <h2>Concepts</h2>
      <a href="sgit-for-git-users.html">sgit for git users<small>The Rosetta stone: same verbs, three differences</small></a>
      <a href="two-branch-model.html">The two-branch model<small>Clone branches, named branches, and why</small></a>
      <a href="../security.html">The security model<small>What the server sees; the crypto stack</small></a>
    </div>
    <div class="grp">
      <h2>Guides</h2>
      <a href="agents.html">Working with AI agents<small>write, --json, sparse clones, multi-agent patterns</small></a>
      <a href="../use-cases.html">Use cases<small>Five workflows, all on shipped commands</small></a>
      <a href="../vault/index.html">SG/Vault platform<small>The browser app, vault apps, the window.sg bridge</small></a>
    </div>
    <div class="grp">
      <h2>Project</h2>
      <a href="limitations.html">When NOT to use sgit<small>The honest page</small></a>
      <a href="exposed-vault-key.html">If a vault key is exposed<small>The rotation runbook, with a real case study</small></a>
      <a href="../briefs.html">Cross-team briefs<small>Open asks to the CLI and API teams</small></a>
      <a href="../admin/index.html">Admin &amp; engineering<small>How this site is built and released</small></a>
      <a href="https://github.com/SGit-AI/SGit-AI__CLI">GitHub<small>Source, issues, changelog</small></a>
    </div>
  </div>
  <div class="note"><b>Coming next:</b> a full per-command CLI reference, generated directly from the CLI's own argument parser on every release — so the reference can never drift from the shipped tool.</div>
</main>"""

# ============================================================ docs/what-is-sgit.html
WHATIS = """<main class="doc">
  <p class="crumb"><a href="index.html">Docs</a> / Introduction</p>
  <h1>What is sgit</h1>
  <p class="lead"><b>sgit is git for encrypted vaults.</b> Clone, commit, branch, diff and merge folders of files that are encrypted with AES-256-GCM before they leave your machine. The server stores ciphertext under opaque IDs — it never sees your filenames, your contents, or your commit messages.</p>
  <p>It's like git and a password vault had a baby.</p>

  <h2>How it works</h2>
  <p>A vault is an ordinary folder plus a <code>.sg_vault/</code> directory. When you commit, sgit snapshots the folder into a git-like object graph — commits pointing at trees pointing at content blobs — and encrypts every object client-side. When you push, only changed ciphertext travels. Object IDs are content-addressed (<code>obj-cas-imm-…</code>), so unchanged files are never re-uploaded, and the server can deduplicate data it cannot read.</p>
<pre class="shell">your-folder/
├── &lt;your files&gt;            <span class="d"># untouched — a vault is just a folder</span>
└── .sg_vault/
    ├── bare/                <span class="d"># encrypted objects, refs, branch keys</span>
    └── local/               <span class="d"># your private clone-branch key — never pushed</span></pre>
  <p>The <b>vault key</b> (<code>passphrase:vault-id</code>) is three things in one string: the address of the vault on the server, the credential to access it, and the root of the local key-derivation hierarchy. Whoever holds it can decrypt the vault; nobody else — including the server — can. See the <a href="../security.html">security model</a> for the full derivation chain.</p>

  <h2>What makes it different from git</h2>
  <ul>
    <li><b>Everything is encrypted client-side</b> — content, filenames, messages, branch names.</li>
    <li><b>No staging area</b> — commit snapshots the whole folder, like <code>git commit -a</code> for everything.</li>
    <li><b>A two-branch model</b> — a private clone branch per machine or agent plus shared named branches, which is what makes safe multi-agent collaboration possible. <a href="two-branch-model.html">Details →</a></li>
  </ul>

  <h2>One vault, three doors</h2>
  <ul>
    <li><b>sgit</b> — this CLI. Open source, Apache-2.0, <code>pip install sgit-ai</code>.</li>
    <li><b>SG/Vault</b> — the web app: browse, edit and review the same vaults in a browser, via an independent implementation of the same wire format. <a href="https://sgraph.ai">How it works →</a></li>
    <li><b>SG/Send</b> — the zero-knowledge transfer API both clients speak to. <a href="https://sgraph.ai">How it works →</a></li>
  </ul>

  <div class="note"><b>Maturity:</b> sgit is in beta and has been powering production workflows for a while. The vault format is versioned and <code>sgit migrate</code> handles upgrades. Read <a href="limitations.html">when NOT to use sgit</a> for the honest edges.</div>

  <div class="pagenav"><span></span><a href="installation.html">Installation →</a></div>
</main>"""

# ============================================================ docs/installation.html
INSTALL = """<main class="doc">
  <p class="crumb"><a href="index.html">Docs</a> / Introduction</p>
  <h1>Installation</h1>
  <p class="lead">Pure Python, two runtime dependencies. Python 3.11 or newer.</p>
<pre class="shell"><span class="p">$</span> <span class="cmd">pip install sgit-ai</span>
<span class="d"># or, on externally-managed systems:</span>
<span class="p">$</span> <span class="cmd">pipx install sgit-ai</span></pre>
  <p>This installs two entry points: <code>sgit</code> and <code>sgit-ai</code> (they are identical — use whichever you like).</p>

  <h2>Verify</h2>
<pre class="shell"><span class="p">$</span> <span class="cmd">sgit version</span>
sgit-ai v0.14.x
<span class="p">$</span> <span class="cmd">sgit doctor</span>
<span class="g">✓</span> remote reachable   <span class="g">✓</span> TLS ok   <span class="g">✓</span> config valid</pre>
  <p><code>sgit doctor</code> checks connectivity and configuration and prints per-OS fix instructions for the common problems (including SSL certificate issues). Add <code>--json</code> if a script or an agent is doing the checking.</p>

  <h2>Upgrade</h2>
<pre class="shell"><span class="p">$</span> <span class="cmd">sgit update</span>   <span class="d"># wraps pip install --upgrade sgit-ai</span></pre>

  <div class="pagenav"><a href="what-is-sgit.html">← What is sgit</a><a href="quickstart.html">Quickstart →</a></div>
</main>"""

# ============================================================ docs/quickstart.html
QUICK = """<main class="doc">
  <p class="crumb"><a href="index.html">Docs</a> / Introduction</p>
  <h1>Quickstart</h1>
  <p class="lead">From zero to a synced, encrypted, versioned vault in five minutes.</p>

  <h2>1 — Create a vault</h2>
<pre class="shell"><span class="p">$</span> <span class="cmd">pip install sgit-ai</span>
<span class="p">$</span> <span class="cmd">sgit create my-vault</span>
<span class="g">✓</span> Vault created and registered
<span class="g">✓</span> Initial commit pushed

  Vault key: <span class="y">&lt;24-char-passphrase&gt;:&lt;vault-id&gt;</span></pre>
  <div class="warnbox"><b>Save the vault key now</b> — in a password manager, not a text file. It is the address, the credential, and the encryption key in one string. There is no reset: lose it and the vault is unrecoverable, by design.</div>
  <p class="small dim">Already have a folder full of files? <code>cd</code> into it and run <code>sgit init --existing</code> instead — the current contents become the first snapshot.</p>

  <h2>2 — Work like git</h2>
<pre class="shell"><span class="p">$</span> <span class="cmd">cd my-vault</span>
<span class="p">$</span> <span class="cmd">echo "# Plan" &gt; plan.md</span>
<span class="p">$</span> <span class="cmd">sgit status</span>
  <span class="g">added:</span> plan.md
<span class="p">$</span> <span class="cmd">sgit commit -m "add the plan"</span>
<span class="g">✓</span> Committed 1 file</pre>
  <p>There is no staging area — <code>sgit commit</code> snapshots the whole folder. Files like <code>.env</code> and private keys are always excluded, automatically.</p>

  <h2>3 — Push</h2>
<pre class="shell"><span class="p">$</span> <span class="cmd">sgit push</span>
<span class="g">✓</span> Pushed 1 commit — only ciphertext left this machine</pre>

  <h2>4 — Clone somewhere else</h2>
<pre class="shell"><span class="d"># on another machine, or in an agent's session</span>
<span class="p">$</span> <span class="cmd">sgit clone &lt;vault-key&gt;</span>
<span class="g">✓</span> Cloned and decrypted 1 file
<span class="p">$</span> <span class="cmd">sgit pull</span>      <span class="d"># pick up new commits any time</span></pre>

  <h2>5 — Look around</h2>
<pre class="shell"><span class="p">$</span> <span class="cmd">sgit history log --oneline</span>     <span class="d"># commit history</span>
<span class="p">$</span> <span class="cmd">sgit history diff</span>              <span class="d"># what changed</span>
<span class="p">$</span> <span class="cmd">sgit vault info</span>                <span class="d"># identity, remote, web URL</span></pre>
  <p>The web URL printed by <code>sgit vault info</code> opens the same vault in the SG/Vault browser app — decrypted in the browser, never on the server.</p>

  <h2>Where next</h2>
  <ul>
    <li><a href="sgit-for-git-users.html">sgit for git users</a> — the Rosetta stone</li>
    <li><a href="two-branch-model.html">The two-branch model</a> — how collaboration works</li>
    <li><a href="agents.html">Working with AI agents</a> — give an agent a private, versioned workspace</li>
  </ul>

  <div class="pagenav"><a href="installation.html">← Installation</a><a href="sgit-for-git-users.html">sgit for git users →</a></div>
</main>"""

# ============================================================ docs/sgit-for-git-users.html
ROSETTA = """<main class="doc">
  <p class="crumb"><a href="index.html">Docs</a> / Concepts</p>
  <h1>sgit for git users</h1>
  <p class="lead">If you know git, you know most of sgit. Same verbs, same mental model — with three deliberate differences that exist because the payload is encrypted.</p>

  <h2>The Rosetta stone</h2>
  <div class="tablewrap"><table>
    <tr><th>git</th><th>sgit</th><th>Notes</th></tr>
    <tr><td><code>git init</code></td><td><code>sgit init</code></td><td><code>--existing</code> vault-ifies a non-empty folder</td></tr>
    <tr><td><code>git clone &lt;url&gt;</code></td><td><code>sgit clone &lt;vault-key&gt;</code></td><td>the key is URL + auth + decryption in one</td></tr>
    <tr><td><code>git status</code></td><td><code>sgit status</code></td><td><code>--explain</code> teaches the branch model</td></tr>
    <tr><td><code>git commit -am</code></td><td><code>sgit commit -m</code></td><td>always whole-folder — there is no staging area</td></tr>
    <tr><td><code>git push / pull / fetch</code></td><td><code>sgit push / pull / fetch</code></td><td>push is delta + ciphertext only</td></tr>
    <tr><td><code>git log</code></td><td><code>sgit history log</code></td><td><code>--oneline</code>, <code>--patch</code>, <code>--json</code>, ranges</td></tr>
    <tr><td><code>git diff</code></td><td><code>sgit history diff</code></td><td><code>--remote</code>, <code>--commit</code>, <code>--files-only</code></td></tr>
    <tr><td><code>git show</code></td><td><code>sgit history show</code></td><td>read-only — fetches missing objects without merging</td></tr>
    <tr><td><code>git revert / reset</code></td><td><code>sgit history revert / reset</code></td><td></td></tr>
    <tr><td><code>git stash</code></td><td><code>sgit vault stash</code></td><td><code>pop</code>, <code>list</code>, <code>drop</code></td></tr>
    <tr><td><code>git branch / checkout</code></td><td><code>sgit branch new / switch / checkout</code></td><td></td></tr>
    <tr><td><code>git merge</code> conflicts</td><td><code>sgit resolve --show</code></td><td>three-way base/ours/theirs view with a verdict per file</td></tr>
    <tr><td><code>git remote</code></td><td><code>sgit remote add / list / set-url</code></td><td></td></tr>
    <tr><td><code>git fsck</code></td><td><code>sgit check fsck</code></td><td>verifies encrypted object integrity, can repair</td></tr>
  </table></div>

  <h2>The three differences that matter</h2>
  <h3>1. No staging area</h3>
  <p>Every commit snapshots the whole folder. This removes git's most confusing concept, and it fits the security model: partial staging would leak "which parts changed" into workflows that are supposed to be opaque. Use branches where you would have used the index.</p>
  <h3>2. The vault key is URL, auth, and encryption key in one</h3>
  <p><code>passphrase:vault-id</code>. There is no separate remote URL to configure, no separate credential to manage, and no password reset. Whoever holds the key holds the vault — treat it like the private key it is.</p>
  <h3>3. Two layers of branches</h3>
  <p>You never work directly on a shared branch. Every clone works on a private <b>clone branch</b> (its key never leaves your machine) and <code>push</code> forwards commits to the shared <b>named branch</b>. That's why two agents on the same vault can't corrupt each other's work-in-progress. <a href="two-branch-model.html">The full story →</a></p>

  <div class="pagenav"><a href="quickstart.html">← Quickstart</a><a href="two-branch-model.html">The two-branch model →</a></div>
</main>"""

# ============================================================ docs/two-branch-model.html
TWOBRANCH = """<main class="doc">
  <p class="crumb"><a href="index.html">Docs</a> / Concepts</p>
  <h1>The two-branch model</h1>
  <p class="lead">sgit's central architectural idea: every clone works on a private branch, and sharing is an explicit act.</p>

  <h2>Clone branches and named branches</h2>
<pre class="shell">        agent A's machine                    the server                    agent B's machine
  ┌───────────────────────┐        ┌───────────────────────────┐        ┌───────────────────────┐
  │  clone branch (A)     │  push  │   named branch "main"     │  pull  │  clone branch (B)     │
  │  key: local only ─────┼───────▶│   key: shared via vault   │◀───────┼─ key: local only      │
  └───────────────────────┘        └───────────────────────────┘        └───────────────────────┘</pre>
  <ul>
    <li><b>Named branches</b> (<code>main</code>, <code>feature-x</code>, …) are shared and live on the server — encrypted, like everything else.</li>
    <li><b>Clone branches</b> are created per clone. Their key is stored only in <code>.sg_vault/local/</code> and is never pushed. All your commits land here first.</li>
    <li><code>sgit push</code> re-encrypts your clone-branch commits with the named branch's key and forwards them. <code>sgit pull</code> brings named-branch commits down and merges them into your clone branch.</li>
  </ul>
  <p>Run <code>sgit status --explain</code> any time — it prints this model with your vault's actual branch names filled in.</p>

  <h2>Why it works this way</h2>
  <ul>
    <li><b>Isolation by construction.</b> Two machines — or two agents — on the same vault physically cannot overwrite each other's uncommitted or unpushed work: they're on different branches with different keys.</li>
    <li><b>Sharing is explicit.</b> Nothing you commit is visible to anyone until you <code>push</code>. An agent can iterate messily in private and publish only the result.</li>
    <li><b>Safe concurrent pushes.</b> Pushes use compare-and-swap on the server (atomic batch writes): if someone pushed before you, your push is rejected cleanly instead of silently clobbering — pull, merge, push again.</li>
  </ul>

  <h2>Merging and conflicts</h2>
  <p>When histories diverge, sgit runs a genuine three-way merge (common ancestor + ours + theirs) per file. Non-conflicting changes merge automatically; conflicting paths get <code>.conflict</code> files, and:</p>
<pre class="shell"><span class="p">$</span> <span class="cmd">sgit resolve --show</span>
  notes/plan.md   <span class="y">CONFLICT (both changed)</span>
    base   │ ship in Q3
    ours   │ ship in Q4          <span class="d">← your clone branch</span>
    theirs │ ship in Q3, beta Q2 <span class="d">← the named branch</span>
    verdict: <span class="y">genuine conflict</span>  <span class="d">(not one-sided, not identical)</span></pre>
  <p>The verdict line matters in multi-writer vaults: it distinguishes genuine conflicts from one-sided or identical changes, so you (or an agent) only spend attention where a human decision is actually required. <code>sgit merge-abort</code> backs out of a merge cleanly.</p>

  <div class="pagenav"><a href="sgit-for-git-users.html">← sgit for git users</a><a href="agents.html">Working with AI agents →</a></div>
</main>"""

# ============================================================ docs/agents.html
AGENTS = """<main class="doc">
  <p class="crumb"><a href="index.html">Docs</a> / Guides</p>
  <h1>Working with AI agents</h1>
  <p class="lead">sgit is designed to be driven by AI agents as well as humans. A vault is just a folder — the agent reads and writes files normally; sgit handles versioning, encryption, and sync. This page covers the agent-facing surface.</p>

  <h2>The session pattern</h2>
<pre class="shell"><span class="d"># start of session: get the workspace</span>
<span class="p">$</span> <span class="cmd">sgit clone &lt;vault-key&gt; workspace</span>   <span class="d"># or: sgit pull, if already cloned</span>
<span class="d"># … agent works on files normally …</span>
<span class="d"># end of session: persist the state</span>
<span class="p">$</span> <span class="cmd">sgit commit -m "session: findings and next steps"</span>
<span class="p">$</span> <span class="cmd">sgit push</span></pre>
  <p>The next session — hours or weeks later, on any machine — runs <code>sgit pull</code> and continues. State survives the context window, encrypted end to end.</p>

  <h2><code>sgit write</code> — the surgical commit</h2>
  <p>When an agent needs to record one result, cloning a whole vault is waste. <code>write</code> commits a file directly to the vault HEAD in a single call: no working-directory scan, no full clone needed.</p>
<pre class="shell"><span class="p">$</span> <span class="cmd">sgit write notes/finding.md --file result.md \\
    --message "agent A: analysis" --push --json</span>
{ "status": "pushed", "path": "notes/finding.md",
  "blob_id": "obj-cas-imm-9c2e41ab77d0" }</pre>
  <ul>
    <li><code>--also vault-path:local-file</code> (repeatable) makes a multi-file write <b>atomic</b> — one commit, all or nothing.</li>
    <li>Content-hash dedup: writing identical content returns <code>unchanged</code> and creates no commit.</li>
    <li><code>--json</code> gives a machine-readable result for the calling pipeline.</li>
  </ul>

  <h2>Machine-readable everything</h2>
  <div class="tablewrap"><table>
    <tr><th>Need</th><th>Command</th></tr>
    <tr><td>Read one file, structured</td><td><code>sgit cat &lt;path&gt; --json</code> · <code>sgit cat --id &lt;blob-id&gt;</code> (zero network calls)</td></tr>
    <tr><td>List files with fetch state</td><td><code>sgit ls --json</code> / <code>--ids</code></td></tr>
    <tr><td>History for pipelines</td><td><code>sgit history log --json</code> · <code>history diff --json</code></td></tr>
    <tr><td>Health checks</td><td><code>sgit doctor --json</code></td></tr>
  </table></div>

  <h2>Fast cold starts</h2>
  <p>Agents run on time budgets. Three clone modes keep startup cheap:</p>
  <ul>
    <li><code>sgit clone --sparse</code> — structure now, file content on demand via <code>sgit fetch &lt;path&gt;</code>.</li>
    <li><code>sgit clone-branch</code> — full history, but only HEAD's content.</li>
    <li><code>sgit clone-headless</code> — credentials only: derive keys and write config, fetch nothing.</li>
  </ul>

  <h2>Multi-agent collaboration</h2>
  <p>Give each agent a named branch; the <a href="two-branch-model.html">two-branch model</a> guarantees isolation of work-in-progress. Two commands make peer review safe:</p>
  <ul>
    <li><code>sgit history show &lt;commit&gt;</code> and <code>sgit history diff</code> are <b>read-only</b> — they fetch missing objects on demand without merging, so an agent can inspect a peer's commit without touching its own working copy.</li>
    <li><code>sgit resolve --show</code> renders base/ours/theirs with a per-file verdict, so genuine conflicts are distinguishable from noise — by a human or by an agent.</li>
  </ul>
<pre class="shell"><span class="d"># agent A</span>  <span class="p">$</span> <span class="cmd">sgit branch new feature-analysis</span> … commit … push
<span class="d"># agent B</span>  <span class="p">$</span> <span class="cmd">sgit history show obj-cas-imm-c4e81a</span>   <span class="d"># look, don't merge</span>
<span class="d"># human  </span>  <span class="p">$</span> <span class="cmd">sgit pull</span> → review in SG/Vault → merge</pre>

  <div class="note"><b>For Claude users:</b> a packaged sgit Skill teaches a Claude session this entire workflow — install, clone, work, commit, push — so cross-session persistent state works out of the box.</div>

  <div class="pagenav"><a href="two-branch-model.html">← The two-branch model</a><a href="limitations.html">When NOT to use sgit →</a></div>
</main>"""

# ============================================================ docs/exposed-vault-key.html
EXPOSED_KEY = """<main class="doc">
  <p class="crumb"><a href="index.html">Docs</a> / Project</p>
  <h1>If a vault key is exposed</h1>
  <p class="lead">A vault key is a <b>bearer credential</b>: whoever holds it can read and write the vault, from anywhere, with no account and no reset. There is no revocation list to add it to. So an exposed key has exactly one remedy — <b>rotate it</b>, which means taking the old vault off the server and re-encrypting the content under a new key.</p>
  <div class="warnbox"><b>Act first, investigate second.</b> Rotation takes minutes and costs you a commit history. Working out exactly who saw what takes hours. Do them in that order.</div>

  <h2>The runbook</h2>
  <ol>
    <li><b>Confirm you hold a complete local clone.</b> The rotation re-encrypts from your working copy — if your only full copy is on the server, clone it before you delete anything. <code>sgit status</code> should be clean, and <code>sgit vault backup</code> is cheap insurance.</li>
    <li><b>Delete the vault from the server:</b> <code>sgit vault delete-on-remote --token &lt;token&gt;</code>. This is the step that actually revokes the old key. Rekeying <em>without</em> it leaves the old vault — and the old key's access to it — alive on the server.</li>
    <li><b>Rotate:</b> <code>sgit vault rekey</code>. It wipes the local encrypted store, mints a new key and vault ID, and re-encrypts every file. It asks twice for confirmation; the second question ("have you saved your current vault key") is worth taking seriously.</li>
    <li><b>Save the new key</b> — password manager, before you do anything else. It cannot be recovered.</li>
    <li><b>Publish:</b> <code>sgit push</code>. The vault is now live under the new key with a fresh ID.</li>
    <li><b>Verify the old key is dead</b> (see below). Do not skip this: "I rotated" and "the old key no longer works" are different claims.</li>
    <li><b>Re-point every consumer</b> — other machines, agents, CI secrets, share links, bookmarks into the web client. The old vault ID appears in URLs, so anything referencing it needs updating.</li>
    <li><b>Then</b> investigate: where did the key appear, for how long, and who could have fetched it.</li>
  </ol>

  <h2>Verifying the old key is dead</h2>
  <p>Four independent checks — each should fail or 404:</p>
<pre class="shell"><span class="d"># 1. the obvious one</span>
<span class="p">$</span> <span class="cmd">sgit clone &lt;old-vault-key&gt; /tmp/check</span>     <span class="d"># must fail: no branch index found</span>

<span class="d"># 2-4. raw HTTP against the old vault id — derive the ids, then GET/PUT them</span>
<span class="d">#   - the old ref file id            → expect 404</span>
<span class="d">#   - a known old object id          → expect 404</span>
<span class="d">#   - a PUT with the old write key   → expect rejection</span></pre>
  <p>A successful clone or a 200 on any of those means the rotation did not take — most often because <code>delete-on-remote</code> was skipped.</p>

  <h2>What rotation costs</h2>
  <ul>
    <li><b>Vault history resets to a single commit.</b> Rekey re-encrypts your current files, not the object graph. (A history-preserving rotation is <a href="../briefs.html">proposed to the CLI team</a>.) If the vault is <a href="../vault/git-and-vaults.html">mirrored to git</a>, the content history survives there — which is one of the better arguments for running the two side by side.</li>
    <li><b>Every object ID changes.</b> IDs are content hashes <em>of the ciphertext</em>, so identical plaintext under a new key produces an entirely new store — zero overlap with the old one. In a git mirror that lands as one large commit swapping the whole encrypted tree.</li>
    <li><b>The vault ID changes</b>, so every URL and stored reference to it breaks.</li>
  </ul>

  <h2>The limit worth understanding: mirrors</h2>
  <p><b>A rotation protects the server. It cannot un-publish a mirror.</b> Encrypted objects already pushed to a git remote stay in that history and remain decryptable by the old key. If the old key was <em>also</em> committed there, anyone who clones the repository can still read the old content, forever, regardless of what you rotate.</p>
  <ul>
    <li><b>Public content</b> (a website, published docs): a non-issue — the plaintext was public anyway. Rotate and move on.</li>
    <li><b>Private content:</b> the rotation is only half the job. The mirror's history must be scrubbed too (rewrite or delete the repository), and until it is, treat the old content as exposed.</li>
  </ul>

  <h2>Case study: this website, 11 August 2026</h2>
  <p>This page exists because it happened here, to the vault that serves this site.</p>
  <p><b>What went wrong.</b> The site's build has a validator that blocks secrets and stale terms from being published. To catch the vault passphrase specifically, an agent (me) added a rule matching that exact passphrase — and wrote the literal secret into <code>admin/build/validate.js</code>, a <em>tracked</em> file. The guard against leaking became the leak. Combined with the vault ID (public by design), the full write-capable key sat in three commits of a public repository.</p>
  <p><b>How it was caught.</b> Not by tooling — by a question. The vault owner asked "you haven't leaked that key, right?", which triggered the audit documented on the <a href="../vault/git-and-vaults.html">git page</a>: grep the working tree and every commit for the passphrase, for private-key headers, and for readable content in the encrypted store. The first two checks passed. The history grep found it.</p>
  <p><b>The response,</b> inside the hour: <code>delete-on-remote</code> (336 files removed from the server) → <code>rekey</code> (39 files re-encrypted under a new key and ID) → <code>push</code>. Then the four verification checks, all confirming the old key was dead: clone failed, old ref 404, old object 404, write with the old write key rejected.</p>
  <p><b>The aftermath, measured.</b> 336 old objects out, 90 new in, <b>zero overlap</b> — no object ID survived, because the addressing hashes ciphertext. Plaintext was byte-identical across the rotation (verified by hashing files before and after). Vault history went from 14 commits to one; the git mirror kept all 14.</p>
  <p><b>What changed structurally.</b> The tripwire now reads the passphrase from the gitignored <code>.sg_vault/local/</code> tier at runtime and scans for it, instead of carrying it — so the secret can no longer live in a tracked file, and the check still works. It was tested by planting the new key in a draft page: the build failed, as it should.</p>
  <div class="note"><b>The transferable lessons.</b> (1) Never write a secret into a file that ships — derive it at runtime from the ignored tier. (2) A leak audit is worth running before your first publish <em>and</em> after anything touches your build config. (3) Grep the full history, not just the working tree; <code>git grep &lt;secret&gt; $(git rev-list --all)</code> is the check that found this. (4) Rotate before you investigate. (5) Write the incident down — this page is more useful than a quiet fix.</div>

  <div class="pagenav"><a href="limitations.html">← When NOT to use sgit</a><a href="../security.html">The security model →</a></div>
</main>"""

# ============================================================ docs/limitations.html
LIMITS = """<main class="doc">
  <p class="crumb"><a href="index.html">Docs</a> / Project</p>
  <h1>When NOT to use sgit</h1>
  <p class="lead">Every tool earns trust faster by stating its edges. Here are sgit's, plainly.</p>

  <h2>Don't use sgit if…</h2>
  <ul>
    <li><b>You need a secrets manager.</b> sgit refuses to commit <code>.env</code> files, <code>.netrc</code>, private keys and friends — deliberately. Use a purpose-built secrets manager for credentials; use sgit for documents, data, and working files.</li>
    <li><b>You need long-term API stability guarantees today.</b> sgit is in beta: it powers production workflows daily and the vault format is versioned (<code>sgit migrate</code> handles upgrades), but commands and flags can still evolve between minor versions. Keep <code>sgit vault backup</code> archives of anything precious.</li>
    <li><b>You need partial commits.</b> There is no staging area — a commit snapshots the whole folder. If your workflow depends on committing three of seven changed files, sgit will fight you (use branches instead, or split folders into separate vaults).</li>
    <li><b>Your data is huge binaries that change constantly.</b> Large files work (they're chunk-uploaded past a ~4&nbsp;MB threshold), but sgit is built for working sets of documents and code-sized files, not video archives. Storage is versioned: history keeps old ciphertext around until pruned.</li>
    <li><b>You want the server to do things with your data.</b> Zero knowledge cuts both ways: the server cannot index, search, preview, or process your content. All intelligence lives client-side — that is the point.</li>
    <li><b>You lose keys.</b> There is no password reset, no recovery, no back door. That's a feature — but only if your key management is real. Password manager, plus <code>sgit vault backup --include-key</code> somewhere safe.</li>
  </ul>

  <h2>Current gaps (roadmap, honestly)</h2>
  <ul>
    <li><b>Commit author attribution</b> is not yet recorded — in multi-agent vaults, per-agent identity currently comes from branch IDs, not signed authorship. Signature slots exist in the format; population is planned work.</li>
    <li><b>Merge drivers</b> are whole-file three-way. Structured merges (JSON-aware, union) are designed but not yet shipped.</li>
    <li><b>Bare clones</b> (<code>clone --bare</code>) are incomplete.</li>
    <li><b>The full CLI reference</b> on this site is still being wired to its generator (it will be produced from the CLI's own argument parser on every release, so it can never go stale).</li>
  </ul>

  <p>If one of these gaps blocks you, say so on <a href="https://github.com/SGit-AI/SGit-AI__CLI/issues">GitHub</a> — real usage reports move the roadmap.</p>

  <div class="pagenav"><a href="agents.html">← Working with AI agents</a><span></span></div>
</main>"""

# ============================================================ vault/index.html
VAULT_HUB = """<main class="doc">
  <p class="crumb"><a href="../index.html">Home</a> / SG/Vault</p>
  <h1>SG/Vault &amp; the vault platform</h1>
  <p class="lead">This section is — for now — the official documentation for the SGraph vault platform: the <b>SG/Vault</b> browser app, the <b>SG/Send</b> zero-knowledge API, and <b>vault apps</b> — websites and applications that live <em>inside</em> encrypted vaults. Product background lives at <a href="https://sgraph.ai">sgraph.ai</a>; the working documentation lives here.</p>

  <h2>What SG/Vault is</h2>
  <p>SG/Vault is the browser client for the same vaults sgit manages from the terminal. It is an <b>independent implementation of the same encrypted wire format</b> — not a wrapper around the CLI — kept interoperable through a versioned contract with test vectors (see the <a href="../security.html#interop">security model</a>).</p>
  <p>You open a vault by its key, carried in the URL <em>fragment</em> (the part after <code>#</code>):</p>
<pre class="shell">https://vault.sgraph.ai/en-gb/<span class="y">#&lt;vault-key&gt;</span>
<span class="d"># the fragment never leaves the browser — it is not sent in the HTTP request,</span>
<span class="d"># so the server serves the app without ever seeing the key</span></pre>
  <p>From there you get a file browser over the decrypted vault — history, branches, editing — and, if the vault contains an app, <b>App Mode</b>: the vault boots straight into its own user interface.</p>

  <h2>The three pieces</h2>
  <div class="tablewrap"><table>
    <tr><th>Piece</th><th>What it is</th><th>Where it runs</th></tr>
    <tr><td><b>sgit</b></td><td>The CLI — git workflows over encrypted vaults</td><td>Your terminal, your agents' sessions</td></tr>
    <tr><td><b>SG/Vault</b></td><td>The browser client — browse, edit, review, App Mode</td><td>Any browser; all crypto via Web Crypto, client-side</td></tr>
    <tr><td><b>SG/Send</b></td><td>The transfer API — stores ciphertext under opaque IDs</td><td>The server; the only piece that never sees plaintext</td></tr>
  </table></div>

  <h2>Vault apps: the app <em>is</em> the vault</h2>
  <p>A vault can contain an <code>index.html</code> plus an <code>app.json</code>. When the vault opens, the app launches — full-screen, talking to the vault through a runtime bridge, with the encrypted blob serving as both the storage and the distribution mechanism. Sharing the vault link <em>is</em> deploying the app.</p>
  <div class="note"><b>You are looking at one.</b> This entire website is a vault app: generated pages, shared assets loaded through the bridge, deployed by <code>sgit push</code>. The <a href="../admin/index.html">admin section</a> documents its engineering and doubles as the reference implementation.</div>

  <h2>Three on-ramps</h2>
  <div class="tablewrap"><table>
    <tr><th>You want to…</th><th>Use</th><th>Code needed</th></tr>
    <tr><td>Publish documents, galleries, hub pages</td><td><a href="content-authoring.html">Markdown + <code>_page.json</code></a> in the browse view</td><td>None</td></tr>
    <tr><td>Ship an interactive experience</td><td><a href="vault-apps.html">A vault app</a> on the <a href="sg-bridge.html"><code>window.sg</code> bridge</a></td><td>HTML/JS</td></tr>
    <tr><td>Automate, script, collaborate, back up</td><td>The <a href="../docs/index.html">sgit CLI</a>, plus <a href="git-and-vaults.html">git side-by-side</a> and <a href="static-hosting.html">static hosting</a></td><td>A terminal</td></tr>
  </table></div>
  <p><a href="sub-vaults.html">Sub-vaults</a> cut across all three: vaults pointing at other vaults, rendered inline like folders — composition without copying.</p>

  <h2>In this section</h2>
  <div class="dochub">
    <div class="grp">
      <h2>Publish</h2>
      <a href="content-authoring.html">Content without code<small>Markdown + _page.json layouts, themes, print</small></a>
      <a href="static-hosting.html">Static hosting<small>GitHub Pages / S3, zero backend, still encrypted</small></a>
    </div>
    <div class="grp">
      <h2>Build</h2>
      <a href="vault-apps.html">Building vault apps<small>The project shape, app.json, and the authoring contract</small></a>
      <a href="sg-bridge.html">The window.sg bridge<small>The runtime API, permissions, and the sovereignty rail</small></a>
    </div>
    <div class="grp">
      <h2>Compose &amp; integrate</h2>
      <a href="sub-vaults.html">Sub-vaults<small>Vaults inside vaults — links, embeds, extract &amp; seed</small></a>
      <a href="git-and-vaults.html">Git repos inside vaults<small>git + sgit side by side; the encrypted mirror pattern</small></a>
    </div>
  </div>

  <div class="pagenav"><span></span><a href="vault-apps.html">Building vault apps →</a></div>
</main>"""

# ============================================================ vault/vault-apps.html
VAULT_APPS = """<main class="doc">
  <p class="crumb"><a href="../index.html">Home</a> / <a href="index.html">SG/Vault</a> / Vault apps</p>
  <h1>Building vault apps</h1>
  <p class="lead">A vault app is a single <code>index.html</code> (plus data and assets) that lives inside a vault and renders straight from it. The experience and the security are the same artifact: the app ships encrypted, the link-holder holds the key, and the server never sees the page you're reading.</p>

  <h2>The project shape</h2>
<pre class="shell">my-vault/
├── index.html          <span class="d"># the app — self-contained entry point</span>
├── app.json            <span class="d"># auto-launch config (below)</span>
├── content.json        <span class="d"># editable content, separate from the app</span>
├── assets/             <span class="d"># css / js, loaded through the bridge</span>
└── &lt;your data&gt;         <span class="d"># the files the app presents</span></pre>
  <p>Keep content in data files, not in HTML — so you (or an agent) can edit captions, prose, and structure without touching the app. Then the manifest (preferred location <code>.vault/app.json</code>; a legacy root <code>app.json</code> is still read):</p>
<pre class="shell">{
  "entry":       "index.html",
  "present":     true,        <span class="d"># boot into App Mode instead of the file browser</span>
  "title":       "My app",
  "permissions": { "fs": { "read": true } },
  "hud":         { "mode": "full" }
}</pre>
  <p>One rule with teeth: <b>an app cannot write its own manifest</b> — <code>.vault/**</code> and the legacy root <code>app.json</code> are a protected floor (<code>EPROTECTED</code>). The manifest <em>is</em> the grant; letting an app edit it would defeat the model. Edit it via the vault browser or sgit.</p>

  <h2>The authoring contract</h2>
  <p>Vault pages render inside a sandboxed frame, and the browser fetches declarative resources <em>before</em> the vault bridge can install. Anything declarative pointing at a vault path will fail. The contract:</p>
  <ul>
    <li><b>No</b> <code>&lt;link rel="stylesheet" href="…"&gt;</code>, <code>&lt;script src="…"&gt;</code>, or <code>&lt;img src="…"&gt;</code> against vault files — inline it, or load it from JS through the bridge (<code>sg.loadCss</code> / <code>sg.loadJs</code>, or read + inject via <code>sg.vfs.readText</code>; set <code>img.src</code> from JS).</li>
    <li><b>No external resources at all</b> — no CDNs, fonts, or analytics. A vault app is self-contained by construction; inline SVG is the graphics format.</li>
    <li><b><code>fetch()</code> of vault paths does not work</b> — use <code>sg.vfs.readText(path)</code> / <code>sg.vfs.read(path)</code>. Plain <code>fetch</code> is only useful as a fallback for static hosting.</li>
    <li><b>Plain <code>&lt;a href&gt;</code> links between vault pages work</b> — the host intercepts clicks and routes them, so multi-page sites navigate normally (this site is the proof). Hash anchors work too; <b>query strings don't</b> (<code>page.html?x=1</code> lands on the broken-link overlay), and never assign <code>location.hash</code> from JS — the sandboxed frame re-navigates.</li>
    <li><b>Signal readiness</b> — post <code>{type:'sg-app-ready'}</code> to the parent when your page has rendered (in the error path too), or users stare at the host's loading overlay. The host also watches for blank apps: ~2.5&nbsp;s after load with nothing painted, it tells the user so — if you legitimately render late, paint a spinner first.</li>
    <li><b>Provide fallbacks</b> — embed critical styles inline and degrade gracefully, so the page stays readable if the bridge is slow or absent.</li>
  </ul>

  <h2>Ship it with sgit</h2>
<pre class="shell"><span class="p">$</span> <span class="cmd">sgit clone &lt;vault-key&gt; my-app</span>     <span class="d"># or sgit create my-app</span>
<span class="d"># … build index.html, app.json, assets …</span>
<span class="p">$</span> <span class="cmd">sgit commit -m "app v1"</span>
<span class="p">$</span> <span class="cmd">sgit push</span>                          <span class="d"># deployment == pushing the vault</span></pre>
  <p>There is no separate hosting step, no build server, no CDN configuration. The vault is the deployment target, the version history, and the rollback mechanism (<code>sgit history revert</code>) in one.</p>

  <h2>The reference implementation</h2>
  <p>This website follows every rule on this page and carries its own build system in-vault: a page generator, a validation suite (contract scan, link check, JS parse check), and a versioned release process. Start at <a href="../admin/index.html">admin &amp; engineering</a> and read <code>admin/build/</code> — cloning this vault gives you a complete working example.</p>

  <div class="pagenav"><a href="index.html">← SG/Vault &amp; the platform</a><a href="sg-bridge.html">The window.sg bridge →</a></div>
</main>"""

# ============================================================ vault/sg-bridge.html
SG_BRIDGE = """<main class="doc">
  <p class="crumb"><a href="../index.html">Home</a> / <a href="index.html">SG/Vault</a> / The bridge</p>
  <h1>The <code>window.sg</code> bridge</h1>
  <p class="lead">Inside App Mode, the host injects a bridge object — <code>window.sg</code> — that gives your page mediated access to the vault and to host capabilities. It installs synchronously while <code>&lt;head&gt;</code> parses, so any inline script can use it. The app frame never holds the vault key: every operation goes through the host, which owns the crypto and the consent UI.</p>

  <h2>Namespaces at a glance</h2>
  <div class="tablewrap"><table>
    <tr><th>Namespace</th><th>What it does</th><th>Grant</th></tr>
    <tr><td><code>sg.vfs</code></td><td><code>read</code> / <code>readText</code> / <code>list</code> / <code>write</code> / host-fulfilled <code>download</code>. Writes cap at ~3&nbsp;MB (<code>EFBIG</code>); reads have no cap</td><td><code>fs.read</code> / <code>fs.write</code></td></tr>
    <tr><td><code>sg.loadCss</code> / <code>sg.loadJs</code></td><td>Top-level functions (not under <code>vfs</code>) — the sanctioned way to load vault CSS/JS; injects into <code>&lt;head&gt;</code></td><td>rides <code>fs.read</code> — no separate verb</td></tr>
    <tr><td><code>sg.fs</code></td><td><code>move</code> (grant needed on both paths) / <code>delete</code> / <code>mkdir</code></td><td><code>fs.*</code> + first-use consent</td></tr>
    <tr><td><code>sg.vault</code></td><td>Cross-vault lifecycle: <code>create(opts)</code> (options object — <code>label</code>, <code>seedFrom</code>, <code>returnKey</code>, <code>custody</code>, <code>link</code>), <code>getKey</code>, <code>openApp</code>, <code>list</code>, <code>unlink</code>, <code>mount</code>, <code>embed</code></td><td><code>vault.*</code>; <code>embed</code> needs none — the key is the capability</td></tr>
    <tr><td><code>sg.history</code></td><td>Read-only commit history: <code>log</code>, <code>list</code>, <code>read</code>/<code>readText</code> at a commit — works on read-only opens</td><td>no</td></tr>
    <tr><td><code>sg.sync</code></td><td><code>status</code> / <code>push</code> / <code>pull</code> / <code>refresh</code> against the named branch (<code>sg.git.*</code> survives as a deprecated alias)</td><td>writable vault</td></tr>
    <tr><td><code>sg.auth</code></td><td>The write gate — the server access token, separate from the encryption key: <code>hasKey</code>, <code>setKey</code>, <code>check</code>, <code>clear</code></td><td>no</td></tr>
    <tr><td><code>sg.ui</code></td><td>Host toasts (<code>message</code>), quick-look <code>preview</code> (incl. PDFs — in-frame PDF rendering is sandbox-blocked), <code>requestPermission</code></td><td>no</td></tr>
    <tr><td><code>sg.state</code></td><td>Device-local prefs (64&nbsp;KiB/key, kernel localStorage, survives reload, not a vault write — "a theme toggle shouldn't create a commit")</td><td>no</td></tr>
    <tr><td><code>sg.llm</code></td><td><code>available</code> / <code>models</code> / <code>chat</code> (streaming, cancel, image parts) / <code>usage</code> / voice <code>listen</code> — the vault's LLM key stays in the host; your frame never sees it</td><td><code>llm.chat</code> / <code>llm.listen</code> / …</td></tr>
    <tr><td><code>sg.append</code></td><td>Append-only transport (write verb is <code>write</code>): <code>configure</code>, <code>write</code>, <code>list</code>, <code>fetch</code>, <code>markProcessed</code>, <code>purge</code>. Lives outside the commit tree</td><td><code>append.*</code></td></tr>
    <tr><td><code>sg.on</code> / <code>sg.off</code></td><td>Host events pushed to the app (e.g. <code>append.new-messages</code> on tab focus — the kernel checks; your app does not poll)</td><td><code>host_events</code> allowlist (top-level key)</td></tr>
    <tr><td><code>sg.app</code></td><td>Read-only context: <code>writable</code>, <code>selfPath</code>, <code>vaultName</code>, <code>vaultId</code>, <code>context</code></td><td>no</td></tr>
  </table></div>

  <h2>The permission model</h2>
  <p>Grants live in <code>app.json</code> (preferred location: <code>.vault/app.json</code>; a legacy root <code>app.json</code> is still read). Each permission is <code>true | false | string[]</code>, and path lists are <b>prefix-based, not glob</b>: a trailing <code>/</code> means "this folder and everything under it"; no slash means an exact file. <code>"data/**"</code> is not valid — use <code>"data/"</code>.</p>
<pre class="shell">{
  "entry": "index.html",
  "permissions": {
    "fs":    { "read": true, "write": ["data/"], "delete": ["data/"] },
    "vault": { "create": ["runs/"] },
    "llm":   { "chat": true },
    "externalLinks": true,
    "downloads": true
  },
  "host_events": ["append.new-messages"]
}</pre>
  <ul>
    <li><b>Mutations are deny-by-default.</b> Writes, deletes, vault lifecycle, append and llm all throw <code>EPERM</code> without a grant. <b>Reads are default-allow today</b> — and are planned to flip to deny-by-default, so declare <code>fs.read</code> anyway.</li>
    <li><b>Two independent gates on every mutation:</b> the server access token (is the vault writable at all?) <em>and</em> the <code>app.json</code> grant. The manifest is a hard ceiling — an app can only ever do what it declares.</li>
    <li><b>The floor is never grantable:</b> <code>.vault/**</code> is invisible and untouchable (<code>EPROTECTED</code>) — which is also why an app cannot edit its own manifest: the manifest <em>is</em> the grant.</li>
    <li><b>Consent is host chrome.</b> Grant-gated verbs raise the host's own confirmation, cached per (vault, app, verb); <code>permissions.consent</code> can tune (never widen) the prompting. Apps can't fake or suppress it.</li>
    <li><b>LLM calls are budgeted:</b> the host clamps <code>maxTokens</code>, filters models, enforces spend caps (<code>EBUDGET</code>) — call <code>sg.llm.available()</code> before rendering any AI UI, and render costs as estimates (<code>~</code>), never as a bill. Deliberate design: there is no tool-calling loop — <em>the LLM never gets ambient authority over the vault</em>; your app decides what to do with a reply, under its own grants.</li>
  </ul>

  <h2>Error codes worth branching on</h2>
  <div class="tablewrap"><table>
    <tr><th>Code</th><th>Meaning</th></tr>
    <tr><td><code>EPERM</code></td><td>verb not granted in <code>app.json</code></td></tr>
    <tr><td><code>EPROTECTED</code></td><td>the floor — <code>.vault/**</code> or the manifest itself</td></tr>
    <tr><td><code>ECONSENT</code></td><td>user declined the consent prompt</td></tr>
    <tr><td><code>ENOENT</code></td><td>no such file — the usual cause when <code>loadCss</code>/<code>loadJs</code> "doesn't work" (typo, or written locally but never pushed)</td></tr>
    <tr><td><code>EFBIG</code></td><td>single write over ~3&nbsp;MB</td></tr>
    <tr><td><code>EREADONLY</code></td><td>static host or read-only session</td></tr>
    <tr><td><code>EBUDGET</code> · <code>ENOKEY</code> · <code>EMODEL</code> · <code>EABORT</code></td><td>llm namespace: spend cap, no key configured, model not allowed, cancelled</td></tr>
  </table></div>

  <h2>Host chrome vs API — two different things</h2>
  <p><b>Chrome you configure but never call</b> (via <code>app.json</code>'s <code>hud</code> block — <code>mode: full | minimal | hidden | none</code> plus per-button <code>show.*</code> flags): the nav row, Print, the ✨&nbsp;AI chat panel (text and voice, entirely at the host origin — your frame never sees the conversation, the key, or the microphone), the file-activity meter, friendly 404 overlays, and the external-link confirm. <b>API you call, with grants:</b> <code>sg.ui.preview</code>, <code>sg.vfs.download</code>, <code>sg.llm.*</code>.</p>
  <p>And the <b>sovereignty rail</b> — three things an app can never suppress, whatever its <code>hud</code> config: consent prompts always render; <code>mode:"hidden"</code> keeps a corner exit pill; and the user can force the full HUD back on from their side, at a level app code cannot reach. The HUD config is for app <em>preferences</em>, not app <em>authority</em>.</p>

  <div class="warnbox"><b>Versioning note:</b> this page is an orientation map, verified against the app-shell bridge (v0.2.x, 2026-08). The authoritative, always-current API reference ships with the app-shell source; where they disagree, the source-side reference wins.</div>

  <div class="pagenav"><a href="vault-apps.html">← Building vault apps</a><a href="content-authoring.html">Content authoring →</a></div>
</main>"""

# ============================================================ vault/git-and-vaults.html
GIT_VAULTS = """<main class="doc">
  <p class="crumb"><a href="../index.html">Home</a> / <a href="index.html">SG/Vault</a> / Git repos inside vaults</p>
  <h1>Git repos inside vaults</h1>
  <p class="lead"><span class="dim">Engineering preview.</span> A git repository is, in the end, just files — which means a vault can hold a complete repo, <code>.git</code> folder included, giving you an end-to-end-encrypted remote for your full history. The missing piece is <em>legibility</em>: making that history readable wherever the vault lands, without assuming a git binary. That piece now exists.</p>

  <h2>A pure-Python git reader</h2>
  <p>The sgit project has a working git reader — ~600 lines of implementation in the same Type_Safe style as sgit itself — that reads the <code>.git</code> object store directly: loose objects, packfiles (index v2, including large offsets), delta reconstruction (both OFS and REF deltas), symbolic refs and <code>packed-refs</code>. No <code>git</code> binary, no gitpython, no dulwich — its only dependency is the same type-safety framework sgit already uses.</p>
  <p>Verified against sgit's own development repository (900+ commits) during review:</p>
<pre class="shell"><span class="p">&gt;&gt;&gt;</span> <span class="cmd">svc = Git_Repo__Reader__Service(repo_path='…/SGit-AI__CLI')</span>
<span class="p">&gt;&gt;&gt;</span> <span class="cmd">[b.name for b in svc.branches()]</span>
['dev', 'claude/sgit-positioning-proposal…']
<span class="p">&gt;&gt;&gt;</span> <span class="cmd">svc.head_commit()</span>
HEAD 2e2dd4c · 1 file changed · author + message parsed
<span class="p">&gt;&gt;&gt;</span> <span class="cmd">len(svc.object_parser.flatten_tree(head.tree_sha))</span>
1161   <span class="d"># every file in HEAD, resolved through packfiles and deltas</span></pre>

  <h2>Why this matters for vaults</h2>
  <ul>
    <li><b>Legible encrypted code archives.</b> Clone a vault containing a repo, and an agent — or a vault app — can render its history, branches, and per-commit file changes anywhere Python runs: sandboxes, Lambdas, CI containers, none of which need git installed.</li>
    <li><b>A repo view for SG/Vault.</b> The same parsing logic, ported to the browser client, would let SG/Vault show commit history for repos stored in vaults — GitHub-style legibility over content the server cannot read.</li>
    <li><b>Agent code-analysis on a time budget.</b> Combine a <a href="../docs/agents.html">sparse clone</a> with the reader: fetch only <code>.git</code>, walk the history, fetch working-tree files on demand.</li>
    <li><b>One mental model, twice.</b> git's object graph (commits → trees → blobs, refs on top) is exactly the model sgit rebuilt over an encrypted content-addressed store. The reader proves the model small enough to reimplement legibly in ~600 typed lines — which is the same bet sgit made, in the other direction.</li>
  </ul>

  <h2>Run git and sgit side by side</h2>
  <p>The integration runs the other way too: the same folder can be a git repository <em>and</em> an sgit vault at once — git's ecosystem (remotes, pull requests, CI, GitHub Pages) over the working files, sgit's zero-knowledge sync over the same content, and a git remote that doubles as an <b>encrypted mirror of the vault itself</b>.</p>
  <p>Why this is safe by construction: the <code>bare/</code> store is byte-parity with what the sync server holds, and the server is untrusted <em>by design</em> — everything in <code>bare/</code> is protected by the vault key, not by where it sits. Git exposure of <code>bare/</code> is therefore equivalent to server exposure, which the zero-knowledge model already accepts. A git remote is just a second untrusted server — one that also gives you distribution, replication and history for free.</p>
  <p>The boundary reduces to three rules:</p>
<pre class="shell"><span class="d"># .gitignore — the whole of it</span>
.sg_vault/local/   <span class="d"># plaintext tier: vault key, push token, unwrapped private keys</span>
.sg_vault/work/    <span class="d"># scratch area — may hold plaintext transiently</span>
*.pem              <span class="d"># defence in depth: no unwrapped key material anywhere, ever</span></pre>
  <p>Pair it with a <code>.gitattributes</code> that marks <code>.sg_vault/**</code> as <code>binary -diff -merge</code>: ciphertext has no meaningful line diff, and a textual merge would corrupt it. Everything else is committed — including the <b>plaintext working tree, which is the point</b>: the vault's contents readable, searchable and reviewable on GitHub, with blame, PRs and CI on top. That makes repo visibility a <em>content</em> decision, not a crypto one: <code>bare/</code> is safe either way; your documents are what you are choosing to expose.</p>

  <h3>The round trip: edit on GitHub, pull back into the vault</h3>
  <p>Because the working tree is real files, the flow runs both ways. Edit a file in the GitHub web editor, merge a colleague's pull request, let a CI job rewrite a document — then <code>git pull</code> into the local clone, and <b>sgit sees exactly what changed</b>, the same way it sees your own edits: <code>sgit status</code> reports them, <code>sgit commit</code> records them in the vault's history, <code>sgit push</code> seals them to the server. Two provenance trails, both kept: git records who proposed and reviewed a change; sgit records it landing in the encrypted vault.</p>

  <h3>Before first publication: audit, then keep the discipline</h3>
  <ul>
    <li><b>Run the leak audit from the vault root</b> before the first <code>git add</code>: the vault-key secret must not appear in the working tree, no <code>BEGIN PRIVATE KEY</code> outside <code>local/</code>, and <code>bare/</code> must contain no greppable filenames or content. (The vault serving this site passed all checks before its dotfiles shipped.)</li>
    <li><b>Write the protection files before the first <code>git add -A</code></b> — once <code>local/</code> is in a commit it is in history, and removing it later means a history rewrite plus key rotation.</li>
    <li><b>For CI</b>, the vault key goes in GitHub Actions Secrets (and a password manager) — never in files, commit messages, issues or workflow YAML.</li>
    <li><b>Disaster recovery comes free:</b> a git clone of the repo plus the key reconstitutes everything — content, sgit history, all branches — even if the sync server is gone. Do one restore drill before you need it in anger.</li>
  </ul>
  <p>The vault serving this site ships the full <code>.gitignore</code> / <code>.gitattributes</code> pair — clone it for a working example. And once the vault is on GitHub, the same repo can serve the app itself: see <a href="static-hosting.html">static hosting on GitHub Pages</a>.</p>

  <h3>What a key rotation does to the mirror</h3>
  <p>Rotating a vault key (<code>delete-on-remote</code> → <code>rekey</code> → <code>push</code>) re-encrypts every object under a new key, so every content-addressed ID changes and the entire store is replaced. In the git mirror that lands as one large commit — for this site, 336 objects deleted and a fresh set added. Nothing breaks (the <code>.gitattributes</code> binary rule means no diff churn), but two consequences are worth knowing before you rotate:</p>
  <ul>
    <li><b>Git becomes the history.</b> A rekey resets the vault's own commit history to a single commit. The git mirror still holds every previous version — which is the side-by-side pattern earning its keep: each remote covers the other's gap.</li>
    <li><b>A rekey protects the server, not the mirror.</b> Old ciphertext already pushed to git stays in git history, and remains decryptable by the old key. If that key was ever exposed <em>and</em> the repo is public, rotating does not un-publish the old content — for public content (like this site) that is a non-issue, but for a private vault, treat a rotation as incomplete until the mirror's history is scrubbed too. Rotate first, then decide about history.</li>
  </ul>
  <p class="small dim">This section exists because it happened here: the passphrase for this site's own vault was written into a tracked build file (an anti-leak regex that became the leak), reached three public commits, and was caught by the audit above. The key was rotated the same hour and the old vault deleted from the server; the exposed content was this public website. Recorded rather than quietly fixed — see the <a href="../admin/versions.html">release history</a>.</p>

  <h2>Status — honestly</h2>
  <ul>
    <li>The reader is <b>in review, not shipped</b>. It is read-only, follows first parents (no merge traversal), and skips submodules and shallow clones by design.</li>
    <li>Review has already produced fixes: two schemas needed the project's own default-value convention applied, and the string-sanitization rules need loosening so file paths and commit messages round-trip byte-faithfully before this ships.</li>
    <li>When it lands, it lands the way everything here does: typed, tested against real repositories, and documented on this page.</li>
  </ul>

  <div class="pagenav"><a href="sub-vaults.html">← Sub-vaults</a><a href="static-hosting.html">Static hosting →</a></div>
</main>"""

# ============================================================ vault/content-authoring.html
CONTENT_AUTHORING = """<main class="doc">
  <p class="crumb"><a href="../index.html">Home</a> / <a href="index.html">SG/Vault</a> / Content authoring</p>
  <h1>Publishing content without code</h1>
  <p class="lead">Not everything needs an app. The vault browser renders two kinds of structured content natively — <b>markdown documents</b> and <b><code>_page.json</code> page layouts</b> — so a vault full of files becomes a navigable, themed, printable site with no HTML written at all. This is the lighter on-ramp; <a href="vault-apps.html">vault apps</a> are the heavier one.</p>

  <h2>Which one, when</h2>
  <div class="tablewrap"><table>
    <tr><th>Reach for markdown</th><th>Reach for <code>_page.json</code></th></tr>
    <tr><td>Prose-first documents, articles, reports, specs, step-by-step guides, linked hierarchies of notes</td><td>Designed pages: hero banners, galleries and slideshows, hub pages with clickable cards, decks, embedded PDFs, explicit theme control</td></tr>
  </table></div>
  <p>Both can coexist in one folder — <code>_page.json</code> takes priority in the browse view. A file named exactly <code>_page.json</code> is auto-detected, no registration; one at the vault root renders immediately on open.</p>

  <h2><code>_page.json</code> in one screen</h2>
<pre class="shell">{
  "title": "Q3 Report",
  "theme": { "mode": "light", "accent": "#0f766e", "font": "serif", "density": "spacious" },
  "navigation": [ { "label": "Overview", "anchor": "overview" } ],
  "components": [
    { "type": "hero",    "title": "Q3 Report", "height": "medium" },
    { "type": "section", "title": "Overview", "layout": "narrow", "children": [
      { "type": "text",     "content": "…" },
      { "type": "gallery",  "images": ["img/a.webp","img/b.webp"], "columns": 3 },
      { "type": "markdown", "file": "notes/summary.md" }
    ]}
  ]
}</pre>
  <ul>
    <li><b>Eleven component types:</b> <code>hero</code>, <code>section</code> (the only container — everything else nests in its <code>children</code>), <code>text</code>, <code>bullet-points</code>, <code>title</code>, <code>image</code>, <code>gallery</code> (click-to-lightbox), <code>slides</code>, <code>pdf</code>, <code>markdown</code>, <code>cards</code>, <code>columns</code>.</li>
    <li><b>Themes:</b> <code>dark</code>/<code>light</code> shorthand or a full block (mode, accent, font, density, background); six named schemes exist, and all but the dark deck are print-safe.</li>
    <li><b>Paths are vault-relative to the folder holding <code>_page.json</code></b> — <code>../</code> allowed but never outside the vault, and <b>no external URLs</b>: vault files only, so a page never phones home.</li>
    <li><b>Live edit preview:</b> the browse view has a split JSON-editor with a debounced preview — but it <b>cannot save</b>; you copy the JSON out and push it with sgit. (The intended loop, verbatim from the internal skill: paste in JSON suggested by an AI, preview it immediately, then commit.)</li>
  </ul>

  <h2>Markdown in vaults — the extras</h2>
  <ul>
    <li><b>Print-aware front matter</b> (first line, <code>---</code>-delimited): <code>page_break_before: h1</code> and a literal <code>print_css</code> block, so a markdown file prints like a document, not a web page. Plus <code>&lt;!-- page-break --&gt;</code> anywhere for an explicit break.</li>
    <li><b>Image sizing with the pipe syntax</b> — <code>![caption|400](img.png)</code>, <code>|60%</code>, <code>|800x600</code> — inside the alt text, so it degrades gracefully in any other renderer.</li>
    <li><b>Internal links open as tabs</b>, with extension fallbacks; link folders via <code>folder/README.md</code>, not <code>folder/</code>. The browse view auto-opens the alphabetically first file — name your entry <code>README.md</code> or <code>00-INDEX.md</code>, or add a root <code>_page.json</code>.</li>
    <li><b>Editing saves</b> — unlike the <code>_page.json</code> editor, the markdown split-editor persists to the vault (writable vaults only).</li>
    <li><b>The traps:</b> raw HTML is stripped and shows as escaped text; nested lists, task lists, footnotes and anchor-id headings are not supported. Write flat, plain markdown.</li>
  </ul>

  <div class="note"><b>The agent angle:</b> both formats are plain JSON and plain text — which makes them ideal surfaces for AI agents to author. An agent writes <code>_page.json</code> or markdown into a vault with <code>sgit write --json</code>, a human previews it in the browser, and the whole loop stays end-to-end encrypted.</div>

  <div class="pagenav"><a href="sg-bridge.html">← The window.sg bridge</a><a href="sub-vaults.html">Sub-vaults →</a></div>
</main>"""

# ============================================================ vault/sub-vaults.html
SUBVAULTS = """<main class="doc">
  <p class="crumb"><a href="../index.html">Home</a> / <a href="index.html">SG/Vault</a> / Sub-vaults</p>
  <h1>Sub-vaults: vaults inside vaults</h1>
  <p class="lead">A vault can point at other vaults. A pointed-to vault shows up inline in the file tree, exactly like a folder — expand it and browse. A clinic's parent vault can hold many per-patient vaults; a demos vault can gather live project vaults — <b>without copying their contents</b>.</p>

  <h2>The mechanism is a convention — like git submodules</h2>
  <p>Nothing is baked into the vault format. A sub-vault is a small pointer file plus UI behaviour: any file named <code>*.link.json</code> is treated as a link, and renders as an expandable folder at its own path. It really is "just create some files" — write the pointer, <code>sgit commit</code>, <code>sgit push</code>.</p>
<pre class="shell"><span class="d"># demos/acme.link.json → renders as folder demos/acme</span>
{ "vault_id": "75f1c88be33d", "ref_id": "lk-37939d3b9b1a", "label": "ACME PoC" }</pre>
  <p>Two levels of setup:</p>
  <ul>
    <li><b>Link file only</b> — the sub-vault appears; each device enters the child's key once.</li>
    <li><b>Link file + owner record</b> — a <code>.vault/owner/ro-links.json</code> entry stores the child's <b>read key only, never its write key</b>; the child then opens silently, read-only, on any device that has the parent. This is what makes it usable for a team.</li>
  </ul>
  <p>The same pointer convention covers <b>external resources</b> (a YouTube video, an image, a page) — with a privacy default worth advertising: external embeds are <b>click-to-load</b>, showing a placeholder until the user acts, so opening a vault never phones home on its own; and external frames get no bridge and a visible "cannot read this vault" banner.</p>

  <h2>Apps read across the boundary</h2>
  <p>To an app, an inner-vault file is just another path: <code>sg.vfs.readText('patients/alice/score.json')</code> auto-opens the child read-only with the stored key — no prompt fires during a read, and if no key is available the read simply fails: the zero-knowledge boundary holds. This is the workflow that lets one dashboard read across many per-user vaults without anyone seeing raw vault UI.</p>

  <h2>Extract &amp; embed — one primitive, three techniques</h2>
  <p>The reverse direction: pull a folder out into its own vault (separate lifecycle, separate sharing, separate history) and bring it back into the parent's app. Extraction is one call from inside a vault app:</p>
<pre class="shell">await sg.vault.create({
  label: 'Q3 Report', seedFrom: 'self:reports/q3',
  returnKey: true, custody: true, link: { path: 'sub/q3-report' }
})</pre>
  <p>The new vault gets a strong random passphrase; the seed copy <b>structurally cannot carry <code>.vault/**</code></b> — so a child can never inherit the parent's owner secrets or tokens. Then choose how to surface it: a <b>read-only sub-vault link</b> (the default, and the recommended one today), a <b>live embedded app</b> via <code>sg.vault.embed</code> (host-managed key handshake — the key never touches the URL or storage; the frame is sandboxed to scripts only, and the host refuses escape-hatch sandbox tokens even if asked), or a <b>cross-vault mount</b> where the child performs operations under its own grants — your app never gains cross-vault write authority itself.</p>
  <div class="warnbox"><b>Honesty notes:</b> the mount technique's credential resolution is explicitly a trial-only stub in current code — prefer the link or embed forms for real users today. And treat an extract-and-link split as an <em>organisational</em> boundary (lifecycle, sharing, history), not a confidentiality boundary from the parent's own readers. Sub-vault access from the sgit CLI is proposed, not shipped — today sub-vaults are a browser-side capability.</div>

  <div class="pagenav"><a href="content-authoring.html">← Content authoring</a><a href="git-and-vaults.html">Git repos inside vaults →</a></div>
</main>"""

# ============================================================ vault/static-hosting.html
STATIC_HOSTING = """<main class="doc">
  <p class="crumb"><a href="../index.html">Home</a> / <a href="index.html">SG/Vault</a> / Static hosting</p>
  <h1>Static hosting — GitHub Pages / S3</h1>
  <p class="lead">The same vault-app HTML runs against the live API <b>or</b> a 100% static file host, transparently. The app only talks to <code>window.sg</code>; static vs live is a property of the transport, not the app. Shipped, opt-in, default-off.</p>

  <h2>Why it works</h2>
  <p>Everything needed to open and browse a vault is a plain GET to a deterministic path: file IDs (commits, trees, refs, indexes) are content hashes or HMACs of the key, computed client-side — <b>no discovery or listing call exists</b>. So a static host that serves those exact paths just works: the browser GETs ciphertext from GitHub Pages or S3 and decrypts locally. No backend, no server, still zero-knowledge — the bytes on the CDN are ciphertext.</p>
<pre class="shell"><span class="d">&lt;!-- on the hosting page, before the host boots --&gt;</span>
&lt;script&gt;
  window.SG_STATIC   = true;                    <span class="d">// batch reads → GETs; writes → EREADONLY</span>
  window.SG_ENDPOINT = 'https://my-org.github.io/my-vault';
&lt;/script&gt;</pre>

  <h2>What works statically — and what doesn't</h2>
  <div class="tablewrap"><table>
    <tr><th>Call</th><th>Static?</th></tr>
    <tr><td>Open, browse, read files, history — <code>sg.vfs.read/readText/list</code></td><td>✅ plain GETs</td></tr>
    <tr><td>Large reads</td><td>✅ falls back from presigned to direct GET</td></tr>
    <tr><td>Batch reads</td><td>✅ fan out to parallel GETs, identical result shape</td></tr>
    <tr><td>Writes, deletes, <code>sg.append.*</code>, vault creation</td><td>❌ rejected cleanly with <code>EREADONLY</code></td></tr>
  </table></div>
  <p>A static vault is a <b>read-only snapshot</b> — ideal for published docs, reports, dashboards and view-only shares. The app detects it via <code>sg.app.writable === false</code> and hides its editing UI; the same HTML runs writable against the live endpoint. <em>Same app, two backends.</em></p>

  <h2>The layout — path mirroring is the one hard requirement</h2>
  <p>The live API serves <code>GET /api/vault/read/&lt;vaultId&gt;/&lt;filePath&gt;</code>; the static host must serve the vault's encrypted <code>bare/</code> tree at exactly that path under your base:</p>
<pre class="shell">&lt;repo root&gt;/                    <span class="d">→ https://my-org.github.io/my-vault/</span>
└── api/vault/read/&lt;vaultId&gt;/
    └── bare/
        ├── data/      obj-cas-imm-*    <span class="d"># immutable — cache forever</span>
        ├── refs/      ref-pid-muw-*    <span class="d"># mutable head — no-store</span>
        ├── indexes/   idx-pid-muw-*
        └── keys/      key-rnd-imm-*</pre>
  <p>If the repo is your vault's own git remote (working tree + <code>bare/</code> committed per the <a href="git-and-vaults.html">side-by-side pattern</a>), the encrypted tree is already in the repo — publishing is just placing it under the right path prefix. Visitors open <code>https://…/my-vault/#&lt;key&gt;</code>: the key travels in the URL fragment (never sent to the host), the transport GETs ciphertext, the browser decrypts and renders.</p>

  <h2>Honest caveats</h2>
  <ul>
    <li><b>Read-only and frozen.</b> The static tree is a snapshot at export time; new live commits appear only when you re-export.</li>
    <li><b>Paths must match exactly</b>, or reads 404. (A configurable read-path template is a proposed follow-on, not shipped.)</li>
    <li><b>Cross-origin setups need CORS</b> on the static host for GETs; same-origin needs nothing.</li>
    <li><b>The key is the read capability.</b> Anyone with the full URL can read the snapshot — that is the point of publishing one — but the host itself only ever holds ciphertext.</li>
  </ul>

  <div class="pagenav"><a href="git-and-vaults.html">← Git repos inside vaults</a><span></span></div>
</main>"""

# ============================================================ briefs.html
BRIEFS = """<main class="doc">
  <h1>Cross-team briefs</h1>
  <p class="lead">This site is built and run by an AI agent — and it doesn't work alone. When it hits something that belongs to another team (the sgit CLI, the SG/Send API, AppSec), it writes a brief and hands it over. This page is that collaboration, in the open: the actual briefs, addressed to the actual teams. Point an agent here and it has the context.</p>
  <div class="note"><b>For the agent reading this:</b> each brief below is a concrete, scoped request with evidence. The canonical markdown copies live in the <a href="https://github.com/SGit-AI/SGit-AI__CLI">SGit-AI__CLI</a> repo under <code>team/humans/dinis_cruz/claude-code-web/</code>; this page is the human-readable index and the shareable URL (<code>sgit.ai/briefs.html</code>).</div>

  <h2>→ To the sgit CLI team: serial transfer mode for Pyodide/WASM</h2>
  <p><b>Status:</b> open · <b>Discovered:</b> live, during the first in-browser clone from the SG/Send servers.</p>
  <p>sgit now runs in the browser under Pyodide (CPython → WebAssembly), and <a href="try.html">the Try page</a> clones real vaults from the live servers. The blocker: sgit parallelises blob transfer with <code>ThreadPoolExecutor</code>, and WebAssembly cannot spawn OS threads — so a clone dies at the blob stage with <code>can't start new thread</code> (index, branch metadata, commits and trees all download fine first, since those paths are sequential).</p>
  <p><b>The ask:</b> make sgit threadless-safe natively, auto-detected — no flag needed for the common case:</p>
<pre class="shell">SERIAL_TRANSFERS = (sys.platform == 'emscripten') or bool(os.environ.get('SGIT_SERIAL_TRANSFERS'))</pre>
  <p><code>sys.platform == 'emscripten'</code> is true under Pyodide and false everywhere else. One small <code>Transfer__Executor</code> helper (Type_Safe, per house rules) returns either a real thread pool or a trivial serial executor with the same surface, across the six call sites (four in <code>clone/Vault__Sync__Clone.py</code>, two in <code>push/Vault__Batch.py</code> — all import the executor at call time, which is what let the browser patch it).</p>
  <p><b>Evidence it's correct:</b> validated natively against the live dev server with thread creation disabled and the executor swapped for a serial one — a full clone of this site's own vault (13 commits, 59 trees, <b>225 blobs</b>) produced a byte-correct working copy. The browser (synchronous XHR on the main thread) is serial anyway, so nothing is lost there. The website already ships this exact shim client-side (<code>assets/try-setup.py</code>, section 0) — proof of the interface; the ask is to make it native so no shim is needed.</p>

  <h2>→ To the sgit CLI team: preserve history across a rekey</h2>
  <p><b>Status:</b> open · <b>Discovered:</b> live, rotating this site's own vault key after an exposure (see the <a href="docs/exposed-vault-key.html">case study</a>).</p>
  <p>Today <code>sgit vault rekey</code> wipes the local encrypted store, mints a new key, and re-encrypts the <em>current working files</em> — so the vault's commit history resets to a single commit. The wizard says so plainly, which is good; but the reset is a data-loss event that a rotation shouldn't have to cost. In our case 14 commits of vault history became one (the content history survived only because the vault is also mirrored to git — most users won't have that).</p>
  <p><b>The ask:</b> a history-preserving rotation — <code>sgit vault rekey --preserve-history</code>, or the default once proven. Everything required is already local in a full clone:</p>
  <ol>
    <li>Walk the commit DAG from every ref.</li>
    <li>Decrypt each object (blob, tree, commit) under the old key.</li>
    <li>Re-encrypt under the new key — which yields a new content-addressed ID, since IDs hash the ciphertext.</li>
    <li>Rewrite bottom-up: blobs first, then trees with their new child IDs, then commits with new tree and parent IDs; finally the refs and branch index.</li>
  </ol>
  <p>It is a full graph rewrite with an ID remap table, not a new crypto design — the same walk <code>clone</code> already does, run locally in reverse. Worth pairing with a <code>--dry-run</code> that reports how many objects would be rewritten, and a verification pass (re-read every rewritten commit under the new key) before the old store is wiped.</p>
  <p><b>One honest limit to document alongside it:</b> a rotation cannot un-publish what a mirror already holds. Ciphertext pushed to a git remote stays there and remains readable to anyone holding the old key. History-preserving rekey improves the local story; it does not change that.</p>

  <h2>→ To the SG/Send API team: two browser-transport findings</h2>
  <ul>
    <li><b>CORS allow-list is missing <code>x-api-key</code>.</b> sgit sends its token on both <code>x-sgraph-access-token</code> (allowed) and <code>X-API-Key</code> (not allowed). A single disallowed header fails the whole browser preflight — Starlette returns <code>400 Disallowed CORS headers</code> — which is what blocked the first in-browser clone. Either add <code>x-api-key</code> to the CORS middleware's <code>allow_headers</code>, or treat the second header as native-CLI-only. (The website's browser transport currently drops <code>X-API-Key</code> client-side as a workaround.)</li>
    <li><b>The presigned-S3 fallback dodges transport patching.</b> <code>_presigned_read_fallback</code> (large blobs) uses a function-local <code>urlopen</code> import, invisible to a monkey-patched transport and untested under CORS from a browser origin. Worth a look before large-blob vaults meet the browser.</li>
  </ul>

  <h2>→ Roadmap note: a Web-Worker async transport</h2>
  <p>The in-browser terminal uses <em>synchronous</em> XHR, so the tab freezes during a network command and output appears only on completion. Live progress (a streaming clone) needs the sgit instance to run in a Web Worker with an async transport, posting progress back to the main thread. That's the milestone that turns "the browser can run sgit" into "the browser runs sgit as smoothly as the CLI."</p>

  <h2>The collaboration log so far</h2>
  <p>Other briefs this site's agent has produced and handed off (in the CLI repo):</p>
  <ul>
    <li><b>git_reader review</b> — verified a pure-Python git reader against a real 906-commit repo; fixed one Type_Safe defaults bug, flagged a sanitization bug before ship.</li>
    <li><b>Pyodide-in-browser verification</b> — proved sgit-ai v0.14.27 runs under WebAssembly, with the <code>ssl</code>-package and <code>.setup()</code> discoveries the tools team's handoff didn't have.</li>
    <li><b>Design-improvements brief</b> — a standing request for a design pass, with the site's hard constraints spelled out.</li>
  </ul>
  <p class="small dim">This is what "the encrypted git for humans and AI agents" looks like from the inside: agents doing real work, filing real bugs, handing off with receipts.</p>

  <div class="pagenav"><a href="index.html">← Home</a><a href="admin/index.html">Admin &amp; engineering →</a></div>
</main>"""

# ============================================================ admin/index.html
ADMIN = """<main class="doc">
  <p class="crumb"><a href="../index.html">Home</a> / Admin</p>
  <h1>Admin &amp; engineering</h1>
  <p class="lead">How this site is built, shipped, and versioned. sgit.ai is not hosted on a web server — it is a <b>vault app</b>: a set of HTML pages living inside an encrypted SG/Send vault, decrypted and rendered in your browser. The site about sgit is delivered by sgit.</p>

  <h2>Architecture</h2>
<pre class="shell">vault root
├── index.html · use-cases.html · security.html      <span class="d"># root pages</span>
├── docs/*.html                                      <span class="d"># 8 documentation pages</span>
├── vault/*.html                                     <span class="d"># 4 SG/Vault platform pages</span>
├── admin/                                           <span class="d"># this section</span>
│   ├── index.html · versions.html
│   ├── brief-design-improvements.md                 <span class="d"># brief for Claude Code</span>
│   └── build/                                       <span class="d"># the build system itself</span>
│       ├── build_pages.py                           <span class="d"># generates every page</span>
│       └── validate.js                              <span class="d"># pre-push checks</span>
├── assets/site.css · assets/site.js                 <span class="d"># shared, loaded at runtime</span>
└── app.json                                         <span class="d"># auto-launch config</span></pre>
  <ul>
    <li><b>The authoring contract.</b> Vault pages render inside a sandboxed frame, so declarative references to vault files (<code>&lt;link&gt;</code>, <code>&lt;script src&gt;</code>, <code>&lt;img src&gt;</code>) would 404 before the vault bridge installs. Every page therefore carries only a tiny critical-style block plus a ~20-line bootstrap.</li>
    <li><b>Shared assets over the bridge.</b> The bootstrap waits for the <code>window.sg</code> bridge and loads <code>assets/site.css</code> / <code>assets/site.js</code> through it — trying <code>sg.loadCss</code>/<code>sg.loadJs</code> first, then <code>sg.vfs.readText</code> + inject, then plain <code>fetch</code> as a static-hosting fallback. Worst case, pages degrade to readable unstyled HTML.</li>
    <li><b>Multi-page navigation.</b> Plain relative <code>&lt;a href&gt;</code> links between pages — the vault host intercepts clicks and routes them, giving normal browser-style navigation (back/forward/history come from the host chrome).</li>
    <li><b>Read-only by design.</b> The app requests no write permissions in <code>app.json</code>; reads need no grant. Nothing on this site can modify the vault.</li>
  </ul>

  <h2>Build system</h2>
  <p>Every page is generated from a single Python script holding one shared template (nav, footer, bootstrap, version stamp) plus per-page content. Nothing is hand-edited twice: change the template once, regenerate, and every page updates consistently — including the version badge you can see in the nav.</p>

  <h2>Validation before every push</h2>
  <ul>
    <li>Every inline script and <code>site.js</code> is parse-checked with Node.</li>
    <li>A contract scan proves no <code>&lt;link href&gt;</code>, <code>&lt;script src&gt;</code>, or <code>&lt;img src&gt;</code> references a vault path.</li>
    <li>Every internal link is resolved against the real file tree — broken links fail the build.</li>
    <li>A banned-words scan keeps retired concepts and legacy naming out of the content.</li>
  </ul>

  <h2>Release process</h2>
<pre class="shell"><span class="d"># 1. bump SITE_VERSION (v0.1.n — n increases on every push) + add a versions row</span>
<span class="d"># 2. regenerate + validate</span>
<span class="p">$</span> <span class="cmd">python3 admin/build/build_pages.py &amp;&amp; node admin/build/validate.js</span>
<span class="d"># 3. ship to the vault — the encrypted deployment</span>
<span class="p">$</span> <span class="cmd">sgit commit -m "site vX.Y.Z: …" &amp;&amp; sgit push</span>
<span class="d"># 4. ship to git — same folder, second remote; GitHub Pages deploys from it</span>
<span class="p">$</span> <span class="cmd">git add -A &amp;&amp; git commit -m "site vX.Y.Z" &amp;&amp; git push origin dev</span></pre>
  <p>One folder, one source of truth, two remotes: the same working tree is an sgit vault <em>and</em> a git repository (<code>SGit-AI/SGit-AI__Website</code>). Every release pushes both — sgit carries the encrypted history; git carries the public mirror and triggers the GitHub Pages deployment. A release isn't done until both remotes report in sync. See <a href="versions.html">release history</a>.</p>

  <h2>Design &amp; contributions</h2>
  <p>A standing brief for Claude Code sessions proposing design improvements lives at <a href="brief-design-improvements.md">admin/brief-design-improvements.md</a> — it carries the constraints (authoring contract, self-contained assets, validation suite, version bump) that any change must respect.</p>

  <div class="pagenav"><a href="../index.html">← Home</a><a href="versions.html">Release history →</a></div>
</main>"""

def versions_body():
    rows = '\n'.join(
        f'    <tr><td class="vnum">{v}</td><td>{d}</td><td class="vid">{c}</td><td>{note}</td></tr>'
        for v, d, c, note in VERSION_LOG)
    return f"""<main class="doc">
  <p class="crumb"><a href="../index.html">Home</a> / <a href="index.html">Admin</a> / Versions</p>
  <h1>Release history</h1>
  <p class="lead">This site ships by pushing its vault, and the site version — <b>{SITE_VERSION}</b>, shown in the nav of every page — increments on every push. Each release is also an sgit commit, so the vault's own <code>sgit history log</code> is the authoritative audit trail; this page is the human-readable index of it.</p>
  <div class="tablewrap"><table class="vers">
    <tr><th>Version</th><th>Date</th><th>Vault commit</th><th>Changes</th></tr>
{rows}
  </table></div>
  <p class="small dim">Numbering: v0.1.n while the site is in its first structure; the middle digit will bump on structural redesigns. The "vault commit" of the newest row reads "this release" because the commit ID only exists once the release is committed — it is recorded here retroactively by the next release.</p>
  <div class="pagenav"><a href="index.html">← Admin &amp; engineering</a><span></span></div>
</main>"""

PAGES = [
    ('index.html', 'sgit — the encrypted git for humans and AI agents',
     'sgit is git for encrypted vaults: clone, commit, branch and merge files that are encrypted before they leave your machine. Zero knowledge — the server stores ciphertext, not your data.',
     'home', INDEX),
    ('use-cases.html', 'Use cases — sgit', 'Five real workflows sgit enables today: agent memory, multi-agent collaboration, human-AI workspaces, encrypted backup with history, and signed file exchange.', 'use-cases', UC),
    ('security.html', 'Security model — sgit', "sgit's zero-knowledge security model, precisely stated: the crypto stack, what the server can and cannot see, key strength, and the open security process.", 'security', SEC),
    ('try.html', 'Try sgit in your browser — sgit.ai',
     'The real sgit-ai package running client-side under Pyodide: derive keys, encrypt, run an in-memory vault, and use a Python console — nothing you type leaves the page.',
     'try', TRY),
    ('skills.html', 'Skills for AI agents — sgit', 'Packaged, versioned instructions that make any AI agent an effective sgit and vault user: operate the CLI, build vault apps, author vault content.', 'skills', SKILLS),
    ('docs/index.html', 'Documentation — sgit', 'sgit documentation: quickstart, concepts, guides for humans and AI agents, and the honest limitations page.', 'docs', DOCS_HUB),
    ('docs/what-is-sgit.html', 'What is sgit — Docs', 'sgit is git for encrypted vaults: how it works, what makes it different from git, and the ecosystem around it.', 'docs', WHATIS),
    ('docs/installation.html', 'Installation — sgit Docs', 'Install sgit with pip, verify with sgit doctor, upgrade with sgit update. Python 3.11+, two runtime dependencies.', 'docs', INSTALL),
    ('docs/quickstart.html', 'Quickstart — sgit Docs', 'From zero to a synced, encrypted, versioned vault in five minutes: create, commit, push, clone, pull.', 'docs', QUICK),
    ('docs/sgit-for-git-users.html', 'sgit for git users — Docs', 'The Rosetta stone: every git command mapped to its sgit equivalent, plus the three deliberate differences.', 'docs', ROSETTA),
    ('docs/two-branch-model.html', 'The two-branch model — sgit Docs', "sgit's central idea: private clone branches per machine or agent, shared named branches, and explicit publishing.", 'docs', TWOBRANCH),
    ('docs/agents.html', 'Working with AI agents — sgit Docs', 'The agent-facing surface: sgit write, --json everywhere, sparse clones, the session pattern, and multi-agent collaboration.', 'docs', AGENTS),
    ('docs/limitations.html', 'When NOT to use sgit — Docs', "The honest page: sgit's edges, stated plainly, plus the current roadmap gaps.", 'docs', LIMITS),
    ('docs/exposed-vault-key.html', 'If a vault key is exposed — sgit Docs', 'The runbook for a leaked vault key — rotate, verify, re-point — plus a worked case study of the time it happened to this website.', 'docs', EXPOSED_KEY),
    ('briefs.html', 'Cross-team briefs — sgit.ai', "Briefs this site's agent has filed to the sgit CLI and SG/Send API teams: serial transfer mode for WASM, history-preserving rekey, browser-transport findings.", 'briefs', BRIEFS),
    ('vault/index.html', 'SG/Vault & the vault platform — sgit.ai',
     'The official working documentation for the SGraph vault platform: the SG/Vault browser app, the SG/Send zero-knowledge API, and vault apps.', 'vault', VAULT_HUB),
    ('vault/vault-apps.html', 'Building vault apps — SG/Vault', 'How to build apps that live inside encrypted vaults: the project shape, app.json, the authoring contract, and shipping with sgit push.', 'vault', VAULT_APPS),
    ('vault/sg-bridge.html', 'The window.sg bridge — SG/Vault', 'The vault app runtime: sg.* namespaces, the deny-by-default permission model, and the capabilities the host chrome provides for free.', 'vault', SG_BRIDGE),
    ('vault/content-authoring.html', 'Content authoring — SG/Vault', 'Publish documents, galleries and hub pages from a vault with no code: markdown with print-aware extras, and _page.json layouts with eleven component types.', 'vault', CONTENT_AUTHORING),
    ('vault/sub-vaults.html', 'Sub-vaults — SG/Vault', 'Vaults inside vaults: link files, owner records, read-only team access, click-to-load external embeds, and the extract-and-embed workflow.', 'vault', SUBVAULTS),
    ('vault/git-and-vaults.html', 'Git repos inside vaults — SG/Vault', 'Run git and sgit side by side: the encrypted store in a git remote, the leak-audit boundary, the GitHub round trip — plus a pure-Python git reader preview.', 'vault', GIT_VAULTS),
    ('vault/static-hosting.html', 'Static hosting on GitHub Pages — SG/Vault', 'Serve an encrypted vault and its app from GitHub Pages or S3 with zero backend: deterministic GET paths, client-side decryption, clean read-only degradation.', 'vault', STATIC_HOSTING),
    ('admin/index.html', 'Admin & engineering — sgit.ai', 'How the sgit.ai site is built: a vault app with generated pages, bridge-loaded assets, a validation suite, and sgit itself as the deployment pipeline.', 'admin', ADMIN),
    ('admin/versions.html', 'Release history — sgit.ai', 'Every release of the sgit.ai site: version, date, vault commit, and changes. The version increments on every push.', 'admin', versions_body()),
]

for path, title, desc, here, body in PAGES:
    page(path, title, desc, here, body)

print('done:', len(PAGES), 'pages —', SITE_VERSION)
