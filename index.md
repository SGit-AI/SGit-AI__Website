# sgit — the encrypted git for humans and AI agents

> sgit is git for encrypted vaults — and a vault is a unit of work: data, app, history and sources, versioned like git and handed over with a single read key. No account, no hosting, nothing to install for the reader; the server stores ciphertext it cannot read. Twenty-five real vaults you can open.

*Source: <https://sgit.ai/index.html> · site v0.2.60 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

Git for encrypted vaults — for humans and AI agents

# A vault is a unit of work:
data, app, history and sources, shipped as one string

Version it like git. Hand it over with a single read key — no account, no hosting, no install for the reader. And the server that stores it cannot read it.

[**Open a real vault →**](demos/vaults/index.md) [5-minute quickstart →](docs/quickstart.md)

Pure Python · two runtime dependencies · Apache-2.0 · [or try it in your browser](try/index.md)

[Reference — **AIUC-1 conformance layer** — The AIUC-1 standard as a graph, plus a conformance layer that computes insurability — Open it →](demos/vaults/aiuc-1-conformance/index.md) [Application — **Agent permission games** — Two games about grants and mandates — the first vault here that phones home — Open it →](demos/vaults/agent-permission-games/index.md) [Presentation — **AI vs. AI — Black Hat EU 2025** — The Black Hat EU 2025 keynote, with its PDF exports and eight research papers — Open it →](demos/vaults/blackhat-eu-2025/index.md) [Report — **Penetration Test Report** — A penetration test report (fictional) with a re-test script per finding — Open it →](demos/vaults/pentest-report/index.md)

Four of **25 published vaults**. Each opens with a read key printed on its page — no account, nothing to install, and the server that stores it cannot read it. [See all 25 →](demos/vaults/index.md)

## What people actually ship

Not categories — things. Each one is a real vault you can open, and each is hard to make any other way, for a reason that has little to do with encryption.

[Hand over a report — **Penetration Test Report** — Findings, evidence and a retest script per finding travel as one unit. The client opens it with one string and can re-run the tests themselves. — vault `o4lrwx02` · open it →](demos/vaults/pentest-report/index.md) [Publish a standard as data — **AIUC-1 conformance layer** — 53 controls as a graph you can cite, 82 hashed source snapshots — and a fork that added a conformance layer without changing a byte of the original. — vault `2wzct4k7` · open it →](demos/vaults/aiuc-1-conformance/index.md) [Give a talk — **AI vs. AI — Black Hat EU 2025** — 26 slides, six PDF exports and the eight papers the talk cites, in the vault it was presented from. The deck and its sources never separate. — vault `k1izvg7e` · open it →](demos/vaults/blackhat-eu-2025/index.md) [Pitch an investor — **VoiceDebrief pitch (FI)** — A presenter app with timings and speaker notes, shipped with the script, the research and the exports it was built from. — vault `95i2xqrd` · open it →](demos/vaults/voicedebrief-pitch/index.md) [Ship a game that reports back — **Agent permission games** — Anonymous telemetry over a write-only lane — the one credential shape that survives being published with a read key. — vault `4evnlwrj` · open it →](demos/vaults/agent-permission-games/index.md) [Give an agent a workspace — **Risk Mandate** — 124 files, 98 commits, eight entry points: a software project delivered as a vault — that calls an LLM without ever holding the API key. — vault `4zf6pf2z` · open it →](demos/vaults/risk-mandate/index.md)

[All published vaults, sortable →](demos/vaults/index.md)

## One human, a team of agents

This site, and every vault on it, is built by one person working with several AI agents — and the agents build for each other. The state that makes that possible is a vault: versioned, shareable, and readable by whoever holds the key.

88site releases, each verified live before it was called done

25vaults published with a deliberately public read key

19sibling sites on `*.sgit.ai`, one question each

10cross-team briefs filed or received, in the open

1A [build brief](briefs/vault-telemetry-append-lanes.md) was published here on a Saturday. Another agent read it and shipped [a vault from it](demos/vaults/agent-permission-games/index.md) the same day.

2The team that owns the API reviewed that vault against the brief, found the brief wrong in two places, and [the correction now sits above the mistake](briefs/index.md).

3One agent [forked another agent's vault](demos/vaults/aiuc-1-conformance/index.md), kept every byte, added a layer — and the original's tests still pass inside the fork.

→The record is the site itself: [the briefs](briefs/index.md), [the case studies](case-studies/index.md), [every release](admin/versions.md). And the diagnosis that produced this homepage is [an article, with the before pictures](articles/proof-behind-the-claim.md).

## Under the hood, it is git

Same muscle memory. Files are encrypted before they leave your machine; the server stores ciphertext and hashes, nothing else.

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

**Git-like version control**commit, branch, merge, diff, log, stash, revert your encrypted files

**Client-side encryption**AES-256-GCM before upload; keys derived from your vault key, never sent to the server

**Real three-way merge**conflict files plus a base/ours/theirs `resolve --show` view

**The two-branch model**a private clone branch per machine or agent; shared named branches for collaboration

**Apps live inside the data**a vault can carry its own sandboxed app, with the permissions it asks for declared in a file

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

[Read the agent guide →](docs/agents.md) · [Install the skills →](skills/index.md) · [Use cases →](use-cases/index.md) · [llms.txt](llms.txt)

## In production — and honest about it

sgit is in beta, powering production workflows daily. No superlatives — just the evidence, and a page that tells you when *not* to use it.

**~4,000** tests**mutation testing** in CI**integration tests** against a real server**2** runtime dependencies**Apache-2.0** [**security model** published](security/index.md) [**when NOT** to use sgit](docs/limitations.md) [**why** does this exist?](why/index.md) [**sgit · SG/Vault · SG/Send** — the three doors](docs/what-is-sgit.md)

## Nineteen sites, one question each

Most of the thinking behind sgit no longer lives on this site. It moved out to **`*.sgit.ai`** — a family of focused sites, each taking one question further than a section here could, each with its own version history and repository. This site stayed about sgit.

[**Agents & AI**identity for agents · calling an LLM with no API key · how the code is written](network/index.md#agents-ai) [**Risk & governance**you cannot deny a risk · cite the provision · the requirements nobody writes down](network/index.md#risk-governance) [**Graphs & method**meaning lives in the edges · issues as files · maps are claims](network/index.md#graphs-method) [**Security & infrastructure**a key registry for agents · an edge guard · ephemeral environments](network/index.md#security-infrastructure) [**Business & publishing**open source is a strategy · subscriptions are not rent · provenance as the product](network/index.md#business-publishing)

[Find the one that answers your question →](network/index.md)

## Start with an argument, not a menu

The articles are the readable way in: one page, one argument, with the screenshots and the links to check it. If you only read one thing here, read one of these.

[2026-09-07**The proof is two clicks behind the claim — what the homepage gets wrong, and the fix**Twenty-five real vaults a stranger can open in one click are the most persuasive thing on this site, and the homepage shows none of them. It leads with encryption, which cannot be seen, and buries the artefacts under a table. This is the diagnosis, with screenshots, before the rebuild — and the second article will show what changed.Read it →](articles/proof-behind-the-claim.md) [2026-09-07**The proof moved up — the homepage after the rebuild, next to the before pictures**The previous article diagnosed a homepage that led with encryption and buried twenty-five real vaults under a table. This is the rebuild, put beside those screenshots — what moved, what was cut, what it is generated from, and the one thing it still cannot show.Read it →](articles/proof-moved-up.md) [2026-08-27**A chat box on a site with no server — the plan, and the trade it makes**Nineteen sibling sites is too many to browse, so the directory now answers questions. The design problem is that sgit.ai has no server and no vault host, which means the honest options are a local matcher, a key in your browser, or moving the page into a vault — and only one of those is free.Read it →](articles/chat-on-a-static-site.md)

[All articles →](articles/index.md)

Encrypted vaults. **Git workflows.** Zero knowledge.

[5-minute quickstart →](docs/quickstart.md) [Star on GitHub →](https://github.com/SGit-AI/SGit-AI__CLI)


---

*[Site index for agents](llms.txt) · [HTML version](https://sgit.ai/index.html)*
