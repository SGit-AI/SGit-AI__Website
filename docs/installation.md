# Installation, sgit Docs

> Install sgit with pip, verify with sgit doctor, upgrade with sgit update. Python 3.11+, two runtime dependencies.

*Source: <https://sgit.ai/docs/installation.html> · site v0.6.89 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Docs](index.md) / Introduction

# Installation

Pure Python, two runtime dependencies. Python 3.11 or newer.

```
$ pip install sgit-ai
# or, on externally-managed systems:
$ pipx install sgit-ai
```

This installs two entry points: `sgit` and `sgit-ai` (they are identical, use whichever you like).

## Verify

```
$ sgit version
sgit-ai v0.18.0
$ sgit doctor
✓ remote reachable   ✓ TLS ok   ✓ config valid
```

`sgit doctor` checks connectivity and configuration and prints per-OS fix instructions for the common problems (including SSL certificate issues). Add `--json` if a script or an agent is doing the checking.

## Upgrade

```
$ sgit update   # wraps pip install --upgrade sgit-ai
```

The current release is 0.18.0, published 7 October 2026. If `sgit version` still shows an older number after `sgit update`, you have more than one Python environment; run `python -m pip install --upgrade sgit-ai` in the one your tools use. What changed, and the one command an agent team should change: [Update sgit-ai to 0.18.0](update-to-0-18-0.md).

[← What is sgit](what-is-sgit.md)[Quickstart →](quickstart.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/docs/installation.html)*
