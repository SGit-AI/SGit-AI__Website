# Try sgit in your browser — sgit.ai

> The real sgit-ai package running client-side under Pyodide: derive keys, encrypt, run an in-memory vault, and use a Python console — nothing you type leaves the page.

*Source: <https://sgit.ai/try/index.html> · site v0.2.39 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

# Try sgit in your browser

This page downloads a Python runtime (Pyodide, ~20 MB) and installs the **real `sgit-ai` wheel from PyPI** — the same code `pip install` gives you — then runs it right here: a working terminal with the actual `sgit` CLI, an in-memory filesystem, and a network transport routed through your browser. Keys are derived and content encrypted locally; nothing you type leaves this page except the ciphertext sgit itself sends when *you* run a network command.

**What this is:** sgit's engine, client-side. File commands run against this tab's in-memory filesystem (gone on refresh; the remote vault persists). Network commands (`clone`, `push`, `pull`, `doctor`) go straight from your browser to the SG/Send servers over CORS — the page freezes while they run (synchronous transport; it's a demo, not a product). First load is heavy (~20 MB, cached afterwards); 600,000 PBKDF2 rounds take ~1–2 s in WebAssembly.

— engine not loaded —

## The terminal

The real `sgit` CLI plus a small toolbox of file commands (`ls`, `cd`, `cat`, `mkdir`, `echo > file`, `tree`, …). Type `help` for the list. History with ↑/↓.

— load the engine above to start —

/workspace $

```
# a session to try (the vault key can be any vault you hold a key for):
sgit init my-vault  cd my-vault  echo "hello" > notes.md
sgit status  sgit commit -m "from a browser"
# and the one that makes it real — clone straight from the SG/Send servers:
sgit clone <vault-key> demo  cd demo  ls  sgit history log --oneline
```

## Python console

The full `sgit_ai` package is importable. The last expression's value is printed.

from sgit_ai.crypto.Vault__Crypto import Vault__Crypto vc = Vault__Crypto() vc.derive_keys('my-passphrase', 'DEMO-VAULT')

How this works: [the same site](../vault/static-hosting.md) serves from an encrypted vault or GitHub Pages; this page pulls Pyodide from a CDN and the wheel from PyPI at runtime, so it needs an internet connection — the one page on this site that does.


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/try/index.html)*
