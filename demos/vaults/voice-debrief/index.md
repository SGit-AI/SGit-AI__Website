# VoiceDebrief — a published vault

> Four apps in one encrypted vault: lifting meaning from fictional voice notes to Article 9(2) of the EU AI Act into typed semantic graphs — with read scoped to one folder, write nowhere, and the briefings it was built from shipped beside the work.

*Source: <https://sgit.ai/demos/vaults/voice-debrief/index.html> · site v0.2.54 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../index.md) / VoiceDebrief

# VoiceDebrief · Fractal Semantic Graphs

Four apps in one vault: lifting meaning out of text — from fictional voice notes to Article 9(2) of the EU AI Act — into typed semantic graphs. The current app requests read over one folder, write over nothing, and the vault ships the briefings it was built from beside the work: source material dated across June to August 2026, assembled into this vault over two days.

**The idea it is built on, in one line.** A paragraph is not a string, it is a **graph** — and so is the paragraph next to it. Lift both into typed nodes and the two can be joined *node-to-node* through an intermediate layer, never paragraph-to-paragraph. That is the fractal claim, and part 4 works it end to end against one real legal provision. The corpus in parts 1–3 is **fictional**, and the vault says so in its own README.

**Open it yourself — the key is the whole credential.**
 Read key: `sgit_rk1_31e8196d3e83b37277083c29f105b8310dbac4569e22715b5e0f85d46878eec1:k6xy9z4d`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_rk1_31e8196d3e83b37277083c29f105b8310dbac4569e22715b5e0f85d46878eec1%3Ak6xy9z4d) · From the CLI: `sgit clone sgit_rk1_31e8196d3e83b37277083c29f105b8310dbac4569e22715b5e0f85d46878eec1:k6xy9z4d`
Published deliberately, and **derived**: this vault was submitted as a vault key, and only the one-way read key derived from it appears here. It grants read, and only read.

## See it live, here

Both surfaces open automatically below. You can also [**open the app in its own window ↗**](https://dev.vault.sgraph.ai/#sgit_rk1_31e8196d3e83b37277083c29f105b8310dbac4569e22715b5e0f85d46878eec1%3Ak6xy9z4d).

## What this vault demonstrates

| Feature | How this vault uses it |
|---|---|
| **Read scoped to one folder, write nowhere** | `app.json` declares `fs.read` over `part-4/` and **nothing else** — no write, no mkdir, at any path. The app is a reader, so the capability it never asked for cannot be misused. The host's own chrome shows the result as `R3 W0`: three reads granted, zero writes |
| A nested app entry | `entry` is `part-4/index.html`, not a root file. The app that opens is four folders into the tree, which is what lets the vault keep *four* apps without one of them having to own the root |
| Lineage kept, not overwritten | `part-2/` and `part-3/` hold **frozen app snapshots** at the state they shipped in; `part-4/` is current. A shared Parts nav links all three, so the earlier thinking stays openable rather than surviving only as a commit message |
| Two surfaces, one vault | `_page.json` gives the vault browser a themed landing page (hero, dark mode, accent `#d9a63f`); `app.json` makes the Article 9 app auto-open. The same objects serve a document reader and an application without either being converted into the other |
| The app-folder pattern over the bridge | from part 4 on, each app is a slim `index.html` shell plus `app/styles.css` and `app/app.js`, pulled in at runtime through `sg.loadCss` / `sg.loadJs` — the vault's own files loaded over the bridge rather than inlined into one unreadable page |
| Licensing declared inside the vault | `LICENSE` and `NOTICE` dual-license the contents: **Apache 2.0** for anything executable, **CC BY 4.0** for the written packs — with the tie-break stated ("the more permissive reading applies"). Terms travel with the objects, not with the page that links to them |
| Git-compatible by construction | `.gitattributes` and `.gitignore` ship inside the vault, and `guides/publish-sgit-vault-to-github.md` documents the round trip — trust-boundary analysis, the Secrets pattern, and a restore drill. The same tree can be an sgit vault and a git repository, which is [how this website is built](../../../case-studies/one-tree-two-remotes.md) |
| The source travels with the work | `briefings/` is 50 files of everything this was built against, and `concepts/` carries a principles register (P1–P15, each with origin, implementation and evolution) plus a notation spec. The reasoning is *in* the artefact — the difference between a demo and a record |

## What is going on here, step by step

The embeds above are the real vault, which makes it easy to scroll past the parts that matter. Each row points at one of them. Every screenshot is of this vault, driven by a script holding nothing but the published read key.

what opens

### The vault opens four folders deep

Opening the read key does not land you in a file listing. `app.json` sets `auto_open` and points `entry` at `part-4/index.html`, so the Article 9 app boots directly — with the Parts nav across the top and the seven views as tabs.

Note the chrome: **Read-only**, and `R3 W0`. The host is reporting the capabilities this app actually holds, and the write count is zero.

The vault auto-opens `part-4/index.html` — badged **Read-only**, `R3 W0`.

the finding is an absence

### Five annotation layers — and the empty one is the point

The paragraph view renders Article 9(2) with five toggleable annotation classes over it: deontic · 2, defined terms · 5, cross-refs · 2, qualifiers · 4, concepts · 3.

There is a sixth layer, **actors**, and it is deliberately empty. The app says why: *no duty-holder appears anywhere in the text*. A view that can show you nothing, and tell you that nothing is the result, is doing something a highlighter cannot.

Five annotation classes as layers — and an actors layer that is empty on purpose.

compression with a thread back

### Six altitudes over the same provision

Intent → five words → one sentence → compressed paragraph → the notation → the text, each rung labelled with what it costs. **L4 · intent**: *"Make risk management a standing duty, not a document."* **L3 · five words**: *"Continuously find, judge, address risks"* — annotated *"lossy on its own — lossless with the links held."* **L1.5** compresses ~140 words to ~60, with the note that *every clause maps to a span; the gap survives compression.*

Between each pair of rungs the app prints `↓ compresses · links held`. That is the whole claim, and it is checkable rather than asserted: tap a notation line and its source span lights up in the original.

Six altitudes, each tethered to the span below it.

divergence as output

### Every term carries two senses, and the gap between them

The Concepts view is a graph page per term. Focus `risk management system` and you get its **Act sense** (self-defining: no Article 3 entry — Article 9 defines it functionally), its **industry sense** (ISO 31000's framework + process; ISO/IEC 23894 for AI), and then the finding:

*"The Act names a SYSTEM (something you can audit) where ISO names a FRAMEWORK + PROCESS — close, not identical; the audit surface differs."* The divergence is not an error to reconcile; it is the product. Below it sit nine outgoing and three incoming computed edges, external standards among them as first-class nodes.

Act sense, industry sense, and the divergence between them — with computed edges.

where the empty layer comes from

### The grammar answers the question the annotation raised

The Grammar view merges dependency arcs with the word-class tree of the same sentence, then labels the semantic roles on `understand`: `ARGM-MOD` *shall — the deontic carrier*, `ARG1` *the risk management system*, `ARG2` *as a continuous iterative process* — and `ARG0` marked **implicit**, *recovered from Art 9(1) + 16(a)*.

That is the explanation for the empty actors layer two rows up: *"Deontic modal + agentless passive: the obligation is explicit and the duty-holder is grammatical absence."* The missing party is not an oversight in the drafting or a gap in the extraction — it is a property of the legal register, and the parse is what demonstrates it.

Dependency arcs, word classes and semantic roles — with `ARG0` implicit.

two axes, one knot

### Structure upward, meaning outward

The bow-tie here is not the risk practitioner's diagram. It is the paragraph as a **knot** with two different axes running through it. Upward is *structure*, the taxonomy: Regulation (EU) 2024/1689 → Chapter III → Section 2 → Article 9 → paragraph 2. Outward is *meaning*, the ontology: typed edges with their inverses named, and — pointedly — the gap edge and the undefined threshold marked as such.

The line under the stack is the one to take away: **the positional hash is stable under amendment; the content hash moves with the wording.** Two identities for the same paragraph, so a citation can survive a renumbering without pretending the text did not change.

Taxonomy upward, ontology outward — and two hashes for one paragraph.

the fractal claim, working

### Two graphs, one junction — never paragraph-to-paragraph

This is the row that justifies the vault's title. It takes a plain operations paragraph with **no regulation in it** — a fictional security product, NetSentinel, watching a fictional grid operator's SCADA estate — and lifts it into its own nodes: *"nobody signs off on that feed, it just lands"*, *"there hasn't been one since spring"*, *"an engineer copied the model onto a personal laptop"*.

Then it joins that graph to the Article 9 graph **node-to-node**, through the intermediate layer. The app states the rule it is obeying: *"this paragraph never links to the Act's paragraph. Its extracted nodes link to the NODES extracted from Article 9(2) — the steps, the defined terms, the threshold — and through them to the text."* The obligations attach at the twin: the running instance and its telemetry, not beside the risks.

An operations paragraph with no law in it, joined to the Act at the node layer.

least authority

### The permission block, read out of the store

Here is the vault's own `app.json`, opened in the vault browser. The whole manifest is 217 bytes, and the permission block is three lines: `fs.read` over `part-4/`.

There is no write grant, no mkdir grant, and no read grant over `briefings/`, `concepts/` or the other parts — the app simply cannot reach them. A commit message in this vault's history dates the change: *"declare fs.read [part-4/] grant ahead of the deny-by-default flip"*. The grant was narrowed **before** the platform started refusing by default, which is the direction that indicates intent rather than compliance.

`app.json`: a nested entry, read over one folder, and no write anywhere.

the reference layer

### The briefings it was built from ship with it

Expand `briefings/` in the vault browser and there are **50 files**: the VoiceDebrief pack, the fractal-semantic-graphs pack with its supporting documents grouped by theme, and the v0.33.57 interim briefs. Beside them, `concepts/` holds the principles register and notation spec, and `guides/` the operational how-tos.

The vault's README draws the line explicitly: everything in `part-*/`, `concepts/` and `guides/` is *produced work*; everything in `briefings/` is *source*. A reader with the read key can check the output against the input that produced it, without asking anyone for access to either.

Source and produced work, in one tree, under one key.

history as evidence

### Eighteen commits, and the reasoning is in them

The SGit view lists the whole history against the working HEAD. The messages are not "wip": they record the refactor to the app-folder pattern, the retirement of the root hub so part 4 could boot directly, the rename of the vault, and the licensing commit that added Apache 2.0 and CC BY 4.0.

This matters for a published vault specifically. A read key hands over *every* commit, not just the current tree — so the history is part of what you publish, and here it reads as a record somebody would be content to have read.

Eighteen commits — the record a read key also hands over.

## Why this shape matters beyond one provision

The transferable part is the **junction rule**. Most attempts to connect a regulation to an operation link document to document — a control mapped to a clause, a policy citing an article — and the link is only as good as the sentence somebody wrote around it. Here both sides are lifted into typed nodes first, and the join happens between nodes at an intermediate layer. Any domain with two bodies of text that must be reconciled — a standard and an implementation, a contract and a delivery, an incident and a policy — can borrow it.

The vault-shaped part is that all of this is **one credential**. The apps, the source briefings that produced them, the licence terms and the full history arrive together, decrypt in the reader's browser, and can be re-derived by anyone. Compare it with [Regulation Graph](../regulation-graph/index.md), which takes the other route to the same subject: the whole EU AI Act parsed from official Formex XML and hash-verified to source bytes, where this one works a single provision to exhaustion.

## The audit, honestly

Every vault is audited before its read key appears here. This one arrived as a **vault key** — the legacy `passphrase:vault_id` form with no prefix to give it away — and was classified as a write credential by `admin/build/check_credential.py` before it touched anything. The vault key was stored in the gitignored tier, the read key derived from it one-way, and only the derived key appears on this page. That derivation cannot be reversed.

The content scan is **clean on credentials**: no vault key inside the vault's own files, no `sgit_vk1_` or `sgit_private_read_` string, no API keys, tokens, `delete_auth` or `append_token` values, no private-key blocks, and no `.vault/` operational bookkeeping.

Two hits were ruled out by reading them, and both are worth naming because a clean sheet asserted is worth less than a finding explained. A 2FA worked example contains the sentence *"Leaked or reused passwords can be tried at scale"* — prose about passwords in a risk chain, matched by a pattern looking for assignments. And `guides/publish-sgit-vault-to-github.md` contains the literal string `BEGIN PRIVATE KEY`, in a table of the things its `.gitignore` must exclude. That is the same shape as [a mistake this site made itself](../publishing.md): a tripwire firing on the exact string a document needs in order to teach people to recognise it.

On personal data: parts 1–3 are built on a corpus the README states is **fictional** — invented companies, invented voice notes — and the part 4 cyber instantiation is likewise a fictional provider and grid operator. The only real-world entities named are public ones: Regulation (EU) 2024/1689, ISO 31000, ISO/IEC 23894.

The rule that goes with any published key applies here too: **revocation is not retroactive.** Anybody who fetches these objects keeps them, and rotating the key protects future commits only.

## Derived facts

92 files · 1,154 KB · 18 commits · HEAD `obj-cas-imm-3026ed53e995` · last updated 10 Aug 2026 · app entry `part-4/index.html` · 71 markdown, 11 JSON, 3 HTML — derived from the read key alone by `admin/build/catalogue_derive.py`, the same derivation that populates [the catalogue](../../../catalogue/index.md), with no token and no clone.


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/voice-debrief/index.html)*
