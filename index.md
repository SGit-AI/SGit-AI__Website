# sgit — the encrypted git for humans and AI agents

> sgit is git for encrypted vaults: clone, commit, branch and merge files that are encrypted before they leave your machine. Zero knowledge — the server stores ciphertext, not your data.

*Source: <https://sgit.ai/index.html> · site v0.2.51 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

Agents need private, versioned state

# The encrypted git for
humans and AI agents

Version, branch, and share vaults of files that are encrypted before they leave your machine. Zero knowledge: the server stores ciphertext, not your data.

[Or try it in your browser →](try/index.md) [5-minute quickstart →](docs/quickstart.md)

Pure Python · two runtime dependencies · Apache-2.0

$sgit create my-vault
✓ Vault created and registered
✓ Initial commit pushed

 Vault key: <24-char-passphrase>:<vault-id>

Keep this safe — it is the address, the auth, and the
encryption key in one string. Without it, nobody — including
the server — can read this vault.

$vim notes/positioning.md
$sgit status
 On clone branch branch-clone-3f9c → named branch main
modified: notes/positioning.md
added: drafts/hero-copy.md

$sgit commit -m "first draft of hero copy"
✓ Committed 2 files (no staging area — commit snapshots the folder)

$sgit history log --oneline
c4e81a first draft of hero copy
b2d70f initial commit

$sgit history diff
--- a/notes/positioning.md
+++ b/notes/positioning.md
- sgit is a CLI for encrypted sync
+ sgit is git for encrypted vaults

$sgit push
✓ Pushed 2 objects (delta push — only changed, only ciphertext)

# on another machine (or another agent)
$sgit clone <vault-key>
✓ Cloned and decrypted 12 files

$sgit pull
✓ Up to date

# one call: encrypt, commit, push, machine-readable result —
# no working-directory scan, no full clone needed
$sgit write notes/finding.md --file result.md \
 --message "agent A: analysis" --push --json
 {
"status": "pushed",
"path": "notes/finding.md",
"blob_id": "obj-cas-imm-9c2e41ab77d0"
 }

The vault key is the address, the auth, and the encryption key — one high-entropy string. Keep it safe.

## Git workflows. Encrypted vaults. Zero knowledge.

sgit is git for encrypted vaults: clone, commit, branch, diff and merge folders of files that are encrypted with AES-256-GCM before they leave your machine.

**Git-like version control**commit, branch, merge, diff, log, stash, revert your encrypted files

**Client-side encryption**AES-256-GCM before upload; keys derived from your vault key, never sent to the server

**Real three-way merge**conflict files plus a base/ours/theirs `resolve --show` view

**The two-branch model**a private clone branch per machine or agent; shared named branches for collaboration

**Sparse & thin clones**structure now, content on demand — for agents on a time budget

**Browser interop**open the same vault in SG/Vault on the web — CLI and browser speak one wire format

## What the server sees

### Your machine

- filenames & folder structure
- file contents
- commit messages
- branch names
- the vault key & derived keys

*[diagram]*

### The server

- obj-cas-imm-3f9c41ab77d0
- ref-pid-muw-8e02cc194b3a
- ciphertext blobs (AES-256-GCM)
- object sizes · timestamps
- the vault id

That's the whole list — and we publish the threat model, including what the server *can* see (sizes, timing, vault ID). [Read the security model →](security/index.md)

## Built for agents

Agents need shared state. Shared state needs versioning — and privacy. sgit is the encrypted, versioned workspace for humans and AI agents.

Persistent memory

### A vault is just a folder

An agent clones it, reads and writes files normally, commits, pushes. The next session pulls and continues. State survives the context window.

Multi-agent, human-merged

### A branch per agent

Each agent gets its own private clone branch; work meets on named branches; a human reviews the merge — in the terminal or in the SG/Vault browser.

Agent-grade plumbing

### Machine-readable everything

`sgit write` for surgical single-call commits, `--json` on every read path, `cat --id` with zero network calls, sparse clones for fast cold starts.

[Read the agent guide →](docs/agents.md) · [Install the skills →](skills/index.md) · [llms.txt](llms.txt)

## What people use it for

[Use case### Private memory for AI agentsDurable, versioned state between sessions — encrypted end to end.Read →](use-cases/index.md#ai-agents)

[Use case### Multi-agent collaborationAgents on their own branches, humans reviewing the merge.Read →](use-cases/index.md#multi-agent)

[Use case### Human ↔ agent workspacesYou in the SG/Vault browser, the agent in the CLI — same vault.Read →](use-cases/index.md#human-ai)

[Use case### Encrypted folders with historyA shared folder the hosting provider cannot read, with rollback.Read →](use-cases/index.md#encrypted-backup)

[Use case### Signed & encrypted exchangePKI: sign, verify, encrypt and decrypt files for named recipients.Read →](use-cases/index.md#secure-file-exchange)

## In production — and honest about it

sgit is in beta, powering production workflows daily. No superlatives — just the evidence, and a page that tells you when *not* to use it.

**~4,000** tests**mutation testing** in CI**integration tests** against a real server**2** runtime dependencies**Apache-2.0** [**security model** published](security/index.md) [**when NOT** to use sgit](docs/limitations.md) [**why** does this exist?](why/index.md)

## One vault, three doors

Think of it as

**sgit** — git, for encrypted vaults

Open source CLI. Free. Apache-2.0. `pip install sgit-ai`

Think of it as

**SG/Vault** — the web app for your vaults

Browse, edit and review the same vaults in the browser — an independent implementation of the same wire format.

[Platform docs →](vault/index.md) · [sgraph.ai](https://sgraph.ai)

Think of it as

**SG/Send** — the transfer API underneath

The zero-knowledge storage service both clients speak to — the same server the integration tests run against.

[Platform docs →](vault/index.md) · [sgraph.ai](https://sgraph.ai)

## Nineteen sites, one question each

Most of the thinking behind sgit no longer lives on this site. It moved out to **`*.sgit.ai`** — a family of focused sites, each taking one question further than a section here could, each with its own version history and repository. This site stayed about sgit.

[**Agents & AI**identity for agents · calling an LLM with no API key · how the code is written](network/index.md#agents-ai) [**Risk & governance**you cannot deny a risk · cite the provision · the requirements nobody writes down](network/index.md#risk-governance) [**Graphs & method**meaning lives in the edges · issues as files · maps are claims](network/index.md#graphs-method) [**Security & infrastructure**a key registry for agents · an edge guard · ephemeral environments](network/index.md#security-infrastructure) [**Business & publishing**open source is a strategy · subscriptions are not rent · provenance as the product](network/index.md#business-publishing)

[Find the one that answers your question →](network/index.md)

## Start with an argument, not a menu

The articles are the readable way in: one page, one argument, with the screenshots and the links to check it. If you only read one thing here, read one of these.

[2026-08-27**A chat box on a site with no server — the plan, and the trade it makes**Nineteen sibling sites is too many to browse, so the directory now answers questions. The design problem is that sgit.ai has no server and no vault host, which means the honest options are a local matcher, a key in your browser, or moving the page into a vault — and only one of those is free.Read it →](articles/chat-on-a-static-site.md) [2026-08-26**Twenty sites in fifteen days, and what that did to the writing**The thinking behind sgit stopped fitting on one site. It moved out to nineteen siblings on *.sgit.ai — what forced the split, what it cost, and why the index into them now starts with a question instead of a list.Read it →](articles/nineteen-sites.md) [2026-08-25**Git for things you cannot put on GitHub**An introduction to sgit and sgit.ai — what an encrypted vault is, why version control had to be rebuilt to get one, and what nineteen published vaults look like when the server storing them cannot read a byte.Read it →](articles/what-sgit-is.md)

[All articles →](articles/index.md)

Encrypted vaults. **Git workflows.** Zero knowledge.

[5-minute quickstart →](docs/quickstart.md) [Star on GitHub →](https://github.com/SGit-AI/SGit-AI__CLI)


---

*[Site index for agents](llms.txt) · [HTML version](https://sgit.ai/index.html)*
