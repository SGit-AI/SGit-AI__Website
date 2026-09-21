# Updates (sgit.ai

> What changed on sgit and on this site, as it happens) one entry per story rather than per release, each linked to the release that carries it. RSS and JSON feeds included.

*Source: <https://sgit.ai/updates/index.html> · site v0.3.9 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

# Updates

What changed on sgit and on this site, as it happens, one entry per story rather than per release. The [version log](../admin/versions.md) is the complete technical record; this is the readable one.

Follow along: [RSS](feed.xml) · [JSON](updates.json). Every entry links to the release that carries it.

## 2026-09-21

### [The design is the performance, and the crypto is free](#the-design-is-the-performance) [v0.3.4](../admin/versions.md)

architectureperformancegraphsmethod

Two releases of [the performance page](../demos/fractal-graphs/performance.md) covered the mechanisms and buried the thing that actually does the work. Performance here comes from an architectural habit, and the habit is one question: **what data do I need for the task at hand?**

Not what the system holds. Not what the schema allows. What *this* question needs. Once that is the first question, most performance work stops being necessary, because the expensive thing was never the engine. It was loading data nobody was going to look at.

## Standing on three giants, none of them ours

The second half of the habit is refusing to reinvent what is underneath.

The **file system** is a high-performance indexed store with decades of tuning and the operating system's page cache in front of it. A **content-addressed hash store** sits on top: a name is a hash of the bytes, so a lookup is a path, deduplication is free, and a cache entry cannot be wrong. The **graph** sits on top of that, and it is the only part that is ours. It is also the part that decides how much a question costs, because it tells you which bytes to ask for.

And the fair version of the database comparison, which usually gets told unfairly in our favour: **a database is fast largely because it keeps the working set in memory.** That is not cheating, it is the same insight. The difference is who picks the working set. A buffer pool guesses it in advance, from access patterns, for every reader at once. We pick it per question, at the moment the question is asked, and throw it away afterwards.

## Measured, because the habit only works if loading is cheap

On the 1.0 MB file that holds the whole DSIT graph:

| Step | Time | Rate |
|---|---|---|
| Fetch over the network, cold | **1,210 ms** | the only number that matters |
| Read from local disk | **2.5 ms** | 418 MB/s |
| **Decrypt, AES-256-GCM** | **0.351 ms** | **2,978 MB/s** |
| Parse the JSON | 3.2 ms | the largest local cost |

**Decryption is 0.03% of the cold fetch and about a tenth of the JSON parse.** On a 59 KB shard it is 0.025 ms. Whenever somebody assumes encrypting the data must have cost something in speed, that is the answer: at these sizes, on ordinary compute, encryption is free and the network is everything. Which puts the question back where it belongs, on how many bytes you decided to ask for.

So the design rule, as a budget. Under 100 KB is an answer. Around 1 MB is a whole world. **10 MB and up means you are loading a store rather than an answer.** Gigabytes is a design error, not a performance problem, and no tuning will fix it.

## Save is where the loop compounds

The step people skip in LETS. Saving is not filing the answer away, it is leaving behind an artefact cut to the shape of the **next** question. The Article 9 slice in the Regulation Graph exists because somebody answered a question about Article 9 once and saved it in a form that makes asking again cost 29 KB instead of a megabyte. Do that a few times and the expensive queries have all been pre-answered, each by the run that first needed them, with nothing decided in advance.

## Restructuring into context is the compression

The fractal property is usually argued as a point about meaning. It is also a point about volume. Measured in the Regulation Graph vault:

| Altitude | Bytes | Against the level below |
|---|---|---|
| Raw Formex source, the law as published | 11,216,043 |  |
| The graph: 1,523 nodes, 1,944 edges | 1,073,915 | **10x smaller** |
| One article's pre-cut slice | 29,638 | **36x smaller** |
| The ontology, the rules of this world | 4,217 | **7x smaller** |

**11.2 MB down to 4.2 KB, a factor of about 2,660, with nothing thrown away**, because every level keeps the edge down to the one below. You query the small thing and follow the link only when the answer requires it.

Which is why this scales in the direction that usually breaks things. In a schema-first system, more data means a bigger index, more memory and a bigger machine. Here the store can be gigabytes or terabytes while **what a question loads stays in the megabytes, because the graph is what tells you which bytes matter.** Adding a terabyte adds nodes you did not load.

## A correction the measuring turned up

This page said 617 nodes and 694 edges, quoting the vault's page. The file as cloned today has **1,051 nodes and 1,289 edges** across five worlds, because the vault released 0.2.1 today and the graph grew. Every count on the page is now counted rather than quoted, and the drift was only visible because the vault keeps its versions instead of overwriting them.

### [That was a cold start, not an architecture cost](#that-was-a-cold-start-not-an-architecture-cost) [v0.3.5](../admin/versions.md)

architectureperformanceapimethod

Yesterday's [performance page](../demos/fractal-graphs/performance.md) put "cold network fetch, 1,210 ms" at the top of a table and let it stand as the cost of reading encrypted data. It is not. It is mostly the cost of a serverless invocation, which is a deployment choice with a known fix, and the page now says so.

## The fixed cost has nothing to do with bytes

Six runs each, best of run:

| One GET returning | Best | Median |
|---|---|---|
| 340 bytes | 0.331 s | 0.381 s |
| 41 KB | **0.309 s** | 0.390 s |
| 2.3 KB | 0.347 s | 0.530 s |
| 1.0 MB | 0.647 s | 0.992 s |

**A 340-byte response and a 41 KB response take the same time.** Only at a megabyte does transfer become visible, and then it is 0.300 s of the 0.647 s. One request in the run came back in 4.8 s, which is what a cold start looks like when you catch one.

So the floor of roughly a third of a second is the **per-invocation cost of running this API serverless**. SG/API also runs on EC2, where a warm process is already listening and that cost does not exist. We have not measured that deployment, so the page puts no number on it, but it no longer lets the invocation model be read as an architecture cost. Where the API runs is a deployment decision, and it is the right lever when a workload is request-heavy rather than byte-heavy.

## Batching is the answer, and the page was missing most of it

`POST /api/vault/batch/{vault_id}` takes **up to 100 operations in one request**. Measured on small objects so that only the per-object term shows:

| Objects in one batch | Best | Per object |
|---|---|---|
| 1 | 0.590 s | 590 ms |
| 2 | 0.394 s | 197 ms |
| 10 | 0.872 s | 87 ms |
| **18** | **1.528 s** | **85 ms** |

That is a straight line, and the line is the cost model worth carrying:

**time ≈ 0.25 s fixed + about 71 ms per object + transfer**

Eighteen objects fetched one at a time would be about 6.3 seconds. In one batch, **1.53 seconds, a little over four times faster**, and the saving grows with the count.

The endpoint also does more than reads, which the page had not covered at all. Operations are `read`, `write`, `write-if-match` and `delete`, authorised per operation, so a read-then-write cycle can be one round trip. And `write-if-match` carries the SHA-256 of the content you believe is there: **if any match fails, the entire batch is rejected.** That is optimistic concurrency across a set of files, in one request, with no lock anywhere.

## The next optimisation, named rather than glossed

71 ms per object inside a batch is server-side, and it is close to linear. That is the signature of objects being fetched from storage one after another inside the handler. Fetching them concurrently would bring a twenty-object batch close to the cost of a one-object batch.

That, and chunking by accumulated size rather than by file count so the 502 stops happening, are the two changes that would move these numbers most. Both are in the API and the client rather than in the design.

### [Take the API out of the path, and the same clone is 25 times faster](#take-the-api-out-of-the-path) [v0.3.6](../admin/versions.md)

architectureperformanceapistorage

The [performance page](../demos/fractal-graphs/performance.md) has been measuring the API and calling it the architecture. Worth saying plainly what that API is: **a convenience over a store, not a requirement of it.** The store is cloud storage holding encrypted objects whose names are hashes. Nothing stops a reader going straight to the bucket, or to a CDN in front of it, with no function in the path at all.

## The measurement

Same client, same vault, same 106 objects, same decryption. Only the path to the bytes changed.

| Path to the bytes | Full clone |
|---|---|
| Through the serverless API | **65.4 s** |
| **Plain GETs, no API in the path** | **2.63 s** |
| Straight off a local folder | 2.05 s |

**Twenty five times faster, with nothing about the vault changed.** The honest caveat: that static host was on localhost, so the network was free, and a real CDN adds edge latency. But the client, the objects and the work were identical in both rows, so what the comparison isolates is the function in the middle.

## It already ships

`sgit clone --transport static` points at any host that answers GETs. It sniffs which of two published layouts the host uses on the first successful read, then fans out **eight parallel requests at a time**. It also records every URL it touches, so a test can assert that no request ever carried key material, which proves the property rather than asserting it.

## Why it is safe to serve the bytes directly

Because there is nothing in them. Every object is ciphertext under a key the server never had, and every name is a hash of those bytes. Exposing them as ordinary public GETs discloses object sizes and request timing, which is the same exposure the API already has and which [the security model](../security/index.md) already names as an acknowledged side channel. It discloses nothing else. That is why reads need no auth header today, and why a bucket behind a CDN is a legitimate deployment rather than a hole.

## And the direct path is already in production

Anything over **4 MB** already takes it, because that is the safe margin under the serverless base64 response limit of about 4.7 MB. The client asks for a presigned URL and fetches the bytes straight from storage. The same route is the fallback when a batch returns 502.

So there are already two paths to every byte, and the only reason the small case goes through a function is that nobody has needed it not to. What follows from there is ordinary storage engineering: a CDN in front of the bucket, where immutable hash-named objects are the ideal cache key; ranged and parallel GETs, which is how a 100 MB or 500 MB object should be read; lower-latency storage classes such as S3 Express One Zone, which we have not benchmarked so there is no number on the page; or another provider entirely, since what is being served is opaque bytes at deterministic paths.

## Finding the object you want

Usually you already know the id, because it is pinned in the page. When you do not, the walk is short: the branch ref gives you the commit, which gives you a tree, which gives you the file or the next tree down. **A couple of requests, not a clone.**

Counted against the static host: reading one named file out of a sparse clone cost **two requests**, and one of those was the client re-probing which layout the host uses, a 404 it could skip by remembering the answer.

This is the thing git cannot do. Pulling one file out of a git repository generally means cloning it, because the objects are packed and the transport is negotiated. Here every object is individually addressable at a deterministic path, so one file is one request against a plain web server.

## One gap, stated outright

**There is no history-depth flag.** `--sparse` skips the content (256 KB, 7.3 s) and `--bare` skips the working copy, but a full clone still takes every version of every file: 106 blobs where the current tree is 42 files, and a sparse clone still walks all seven commits and twenty eight trees. Depth control is the single change that would most improve clone time.

### [Graph engineering versus fractal graph, the measured answer](#performance-and-cost) [v0.3.2](../admin/versions.md)

graphsarchitectureperformancecost

A reader of [the Fractal Semantic Graphs page](../demos/fractal-graphs/index.md) asked the follow-up that page had coming: what is the **performance** of this against ordinary graph engineering?

[Performance, cost, and running everywhere](../demos/fractal-graphs/performance.md) is the answer, and every figure on it was measured on 21 September 2026 from an ordinary cloud container against live published vaults, using the read keys printed on their own pages. Anyone can repeat the commands.

## The architecture the numbers come from

We run with **no live database**. A graph is a set of encrypted files in object storage, read directly. The engine that answers a question is created when the question is asked and destroyed when it is answered, either in the reader's browser tab or in a serverless function that exists for one request. The cycle is **LETS**: Load the bytes, Extract the slice and the ontology that explains it, Transform in a disposable engine, Save the answer as new immutable files.

Save never overwrites, and that one property carries the rest. Because every object is immutable, every cache in the path is correct forever, which is why there is no server: the hardest thing a database does for you, keeping one mutable truth consistent across readers, is a problem this architecture never creates.

## What it costs, measured

Against the [DSIT AI Risk Toolkit](../demos/vaults/dsit-ai-risk-toolkit/index.md) vault, 42 files, 3.2 MB, a semantic graph of 617 nodes and 694 edges:

| Operation | Time |
|---|---|
| Full clone, every file and the whole history | **65.4 s** |
| Sparse clone: every path, size and hash, no content | **7.3 s**, 256 KB |
| Fetch one file that answers one question | **0.49 s**, 59 KB |
| Fetch the entire graph as one file | **1.21 s**, 1.0 MB |
| Ask again for something already fetched | **0.18 s**, no network |

Cloning everything costs 65 seconds. **Answering a question costs 7.8 seconds and 315 KB**, and the second question costs under a second. Nothing was indexed in advance and no service was running before the command was typed.

In the browser, measured by recording every response, so these are exact byte counts: the landing view of that 617-node graph is **94 KB in three requests**. The graph view is 1.12 MB in five. No view loads the whole vault, because no question needs it. The ontology is **2 KB**, and 4,217 bytes in the larger Regulation Graph, which is the entire price of arriving in a new world and learning its rules. That is what makes the jump between worlds affordable rather than theoretical.

## The cost model, which is where the decision usually gets made

Zero instance hours. Zero replicas. Zero index memory. No separate backup line, because every version is already kept. No staging copy, because a clone is a clone. Storage and egress only, and query compute paid by the reader's own device.

The entire published estate on this site, thirty one vaults, is **2,662 files and 295 MB** of object storage. **Cost scales with what is read, not with what exists, and not with time.** Scale to zero is normally a property you give back the moment you attach a database, because the database is holding the state. Here the state is in files, so the zero is real.

## Running everywhere, including inside somebody else's boundary

The same artefact runs in a browser tab, a terminal, a serverless function, a CI container and a static host with no backend, on one read key and nothing installed. That is also the fractal deployment story: the deployment unit is a set of files and a key, so putting a graph inside a regulated environment or an air-gapped machine is a copy rather than a project, and two organisations can join their graphs by exchanging an edge and a read key without either one adopting the other's schema.

## And six places it is slower

The page would not be worth sending if it only listed wins. Full clones are slow. There is no server-side query, so whatever the client needs, the client downloads. Cutting good slices is real work that moves query time to build time. Writes are single writer per branch. Revocation is not retroactive.

And one a graph database wins outright: six hops across a hundred million edges in a single schema is exactly what it was built for. The fractal argument is about the case where those hundred million edges were never going to live in one schema in the first place.

### [One request, an append lane, and a cache full of ciphertext](#one-request-append-and-ciphertext-caching) [v0.3.3](../admin/versions.md)

architectureperformancecryptocaching

Yesterday's [performance page](../demos/fractal-graphs/performance.md) answered the question it was asked and left out the three things that make the architecture fast in the first place. They have been measured and added.

## Reading an encrypted file takes one request

The property most people do not expect, because encryption usually implies a lookup. It does not here.

**The address is derived, not discovered.** Every file id is produced by HMAC-SHA256 over the read key under a named domain, `sg-vault-v1:file-id:ref`, `:branch-ref`, `:branch-index`, from the same constants in the CLI and in the browser client. A client holding the read key computes the address of the ref, the index and the settings **before issuing any request at all**. There is no discovery round trip, which is the cost that usually dominates a small read.

Reading is then a plain CORS GET with no auth header, because the bytes are useless without the key. Measured against a live vault:

|  |  |
|---|---|
| One object, no headers | 2,364 bytes of ciphertext, **0.86 s** |
| A larger object | 59,324 bytes, **0.63 s**, best of five 0.33 s |
| Five objects, one POST | **0.87 s**, one round trip |
| **Twenty objects, one POST** | **3.76 MB in 2.79 s**, one round trip |

Encryption costs a flat **28 bytes per object**, a 12-byte nonce and a 16-byte tag, the same whether the file is two kilobytes or two megabytes. No percentage overhead to budget for.

### Which corrects yesterday's clone number

The transport returned 3.76 MB in 2.79 seconds, so the 65-second clone needed a better explanation than the one v0.3.2 gave. The clone log has it: seven commits, twenty eight trees and **106 blobs** rather than 42 files, because a full clone takes the history too, and then one batch of fifty hit the server's response-size limit and fell back to fetching those fifty one at a time. That is a client-side chunking bug, chunk by accumulated size rather than by file count, and not a property of the architecture. The page now says so.

## Append mode: writes that never touch the graph

A lane lives at `bare/append/{token}/pending/`, **outside the version-controlled commit tree**. A write is one account-less POST with the token in the body: no session, no read-modify-write, no commit, no tree rebuild, no lock, no merge. It never conflicts with a push, and it never contends with a read, because a reader walking the graph never looks at a lane. The response is deliberately blind, so the server does no extra work composing it and leaks nothing by size or timing. Several anchors means several lanes, so one flooding sender cannot bury another.

## Caching encrypted data, which is the easy case

Two reasons, and they are the same reason.

**The cached bytes are ciphertext**, so a cache is not a trust boundary. The browser cache, IndexedDB, a CDN edge, a corporate proxy and a local clone can all hold vault objects without widening exposure by one byte. **And the name proves the bytes**: an `obj-cas-imm-` id is SHA-256 over the ciphertext, so an entry under that name can never be stale and can never be wrong, which is why no invalidation logic exists anywhere. Mutable refs are the exception, and their failure is silent: a stale ref renders an old commit from ciphertext that is itself perfectly valid.

## A high-performance site running on exactly this

[sgraph.ai/en-gb/library/](https://sgraph.ai/en-gb/library/) is a public knowledge base whose content does not exist on its web server. A **270 KB static shell**, 28 KB of HTML plus 242 KB of CSS and components, and every article, nav entry and blog post comes out of two encrypted vaults and is decrypted in the visitor's tab. The server cannot read a word of what it serves.

Its blog entries pin their content-addressed object ids in the page source, so opening one is a single GET straight to the bytes. Its navigation is deliberately **not** pinned and resolves HEAD to tree to blob at runtime, so it stays current. Both choices are in its source with the reasoning attached. Its cache script keeps immutable objects in IndexedDB so later page loads need no network at all, collapses concurrent callers for the same URL into one request, and labels every response it serves.

## And a gap found while measuring

Our own [caching contract](../api/vault-objects.md) says an immutable object is served with `Cache-Control: public, max-age=31536000, immutable` and a ref with `no-store`. Today the read endpoint returned **no `Cache-Control` header at all** for an immutable object, and the CDN reported a miss.

The mechanism is unaffected, because a client cache that keys on the id rather than trusting a header is the more robust design and is exactly what the library site ships. But the documented header is not live on that path, and the page that documents it should not be read as describing what is currently served.

## 2026-09-20

### [The newest vaults were at the bottom of the table, and at the top of the machine list](#vault-table-order) [v0.2.99](../admin/versions.md)

vaultsbuildmethod

[The published-vaults table](../demos/vaults/index.md) opened at #26 and ended at #30. Three bugs behind one symptom.

**The table read file order.** Its own docstring claimed *"the rows ship newest-first in the HTML"*, but the generator loaded `vaults.json` directly and rendered it as written. The four most recent vaults had been appended to the end of the file rather than inserted at the top, so they rendered last.

**The machine list was right, which is worse.** The generator for [`/demos/vaults/llms.txt`](../demos/vaults/llms.txt) sorted by ordinal. So the human table and the machine list have disagreed for four releases, on a page whose own footnote says the two are generated from the same file and therefore cannot drift.

**And one found on the way.** The routine that lifts each read key out of its vault page knew the legacy prefix and the private one, but not `sgit_public_read_`. The two keys [relabelled yesterday](../updates/index.md) were being republished in the machine list stripped of the declaration they had just been given.

## One order for the whole site

`_vaults()` now sorts newest-first and every caller reads it, so there is one ordering rather than one per consumer. It also asserts what makes the ordinal trustworthy as a sort key: unique, running 1 to N with no gaps, and in the same order as the published dates. Both assertions were tested by breaking the data on purpose, and each fails the build by name.

The homepage is untouched: its hero row and its job bands use a hand-curated order, which is exactly why nobody noticed this there.

### [The vault named after the concept was not on the concept's page](#the-vault-named-after-the-concept) [v0.2.96](../admin/versions.md)

graphsvaultsmethod

Asked whether the GitHub repository `VoiceDebrief/VoiceDebrief__Fractal-Semantic-Graphs` was in the collection, the answer was yes. It is the plaintext mirror of [vault #11](../demos/vaults/voice-debrief/index.md), `k6xy9z4d`, published here on 22 August. Cloning both and comparing showed the repository's 90 content files matching the vault's HEAD file for file, and both last moved on 10 August.

What was missing was the reverse link. [Fractal Semantic Graphs](../demos/fractal-graphs/index.md) walked seven graph vaults and never cited the one that carries the name. That vault holds the fifteen-principle register the definition comes from (P4 *everything is a node*, P6 *fractal descent*, P7 *the junction rule*, P11 *altitude*, P15 *structure points down; meaning radiates out*), the leading brief of 6 August whose one sentence says what the page took five revisions to reach (*"each level is the same operation applied to a larger span, which is what makes the structure fractal rather than merely nested"*), and a notation spec with two laws worth carrying everywhere: every statement must read aloud as a sentence and decompose into triples, and every statement must link to the span it compresses, because *"claims from memory are not allowed anywhere in this system."*

A new section, **where the idea was worked first**, quotes all of that in a principle-to-page table, credits the Article 9(2) example in the zoom diagram to the vault that works that provision to exhaustion, and adds the vault to the table of vaults to open.

**The vault's own page gains a mirror section.** The vault practises its own guide: plaintext tree and encrypted store side by side on GitHub, `local/` gitignored. Three consequences are stated. The content is public twice over, so the read key adds the history and the app, not access. The repository is a snapshot, not a live mirror, and will drift if the vault moves and it does not, which is the failure this site's own mirror had before it was retired. And the encrypted store is safe in the open for the reason the guide gives.

### [We published read keys under a prefix that declares them secret, and an agent refused to open them](#the-prefix-said-private) [v0.2.98](../admin/versions.md)

keyssecuritydocsagents

An agent asked to inspect the two AIUC-1 vaults declined, and said so plainly: their credentials are labelled private read, despite being published on sgit.ai, and it would not work around that restriction.

**It was right. Our label was wrong.** The sgit CLI defines three current prefixes and states which is which in its own source: `sgit_private_vault_` is a write credential, `sgit_private_read_` is read-only and *kept secret*, and `sgit_public_read_` is read-only and *deliberately published*. Seven published credentials across [the AIUC-1 conformance layer](../demos/vaults/aiuc-1-conformance/index.md) and [the AIUC-1 catalogue](../demos/vaults/aiuc-1-graph/index.md) carried the middle one. They now carry the right one, with a dated line on each page saying what changed and that the bytes, the access and the vault are identical.

**Verified before relabelling**, on sgit-ai v0.16.2: the bare form, the legacy prefix, the private read prefix and the public read prefix all clone the same 699-file vault; an all-zeros key under the same prefix produces nothing; and the SG/Vault web loader strips all five prefixes in its own format module.

## The structural fix matters more than the seven strings

The validator now **bans both current private prefixes in tracked files**, using the same trailing-character rule the write-key tripwire already used: documentation can print a prefix as a name, a real key fails the build. And `check_credential.py` learned the public prefix and now **refuses** the private read one. That credential is read-only and leaks no capability, and it is still not publishable, because the label says the opposite of what publishing it does.

## The page that was missing

[Vault credentials](../docs/credentials.md) explains this for the first time: the two capabilities and the one-way derivation between them, drawn; the five prefixes in a table with publish-or-not on each row; why classification is by declaration and never by shape, which is the CLI's own hard-won lesson; why the word matters when the bytes do not; and what a read key can and cannot do, including that revocation is never retroactive.

**Not done, and a decision to make:** 99 published keys across 27 pages still carry the legacy `sgit_rk1_` prefix. That one is neutral rather than wrong, so normalising it is a consistency call, not a correction.

### [The em-dash is gone from the prose, and so is the legacy key prefix](#no-more-em-dashes) [v0.3.0](../admin/versions.md)

writingkeysbuildmethod

Two site-wide normalisations, each with a guard so they stay done.

## 3,200 em-dashes, rewritten rather than deleted

A good many readers now find the character off-putting, so it is gone from every sentence on the site. This was not a find-and-replace. A rewriter classified each occurrence by its context and chose the punctuation the sentence actually wanted: brackets or commas around a parenthetical pair, a colon before an explanation, a full stop with the next word capitalised where the tail was an independent clause, and a comma otherwise.

Code was left alone by construction, and the same exclusions are now written into the validator so the two agree: `pre`, `code`, `svg`, fenced and inline markdown code, inline script, the assets folder, the skills folder (upstream artifacts shipped verbatim) and the board, which is rendered from a vault this site does not author.

**Four bugs, found by checking rather than assuming.** A whitespace tidy reflowed the ASCII diagrams inside `pre` until it was made mask-aware. The pair rule bridged adjacent table cells, leaving seven brackets that opened in one cell and closed in another, each caught by a balance check and fixed by hand. The try page's JavaScript compared against placeholder text the markup no longer had, which would have broken its terminal. And a colon reads badly in front of a conjunction, so 35 of them became commas.

## The legacy key prefix, and a brief that closed itself

102 published read keys carried `sgit_rk1_` and 24 carried no prefix at all. All of them now carry `sgit_public_read_`, which declares the intent rather than leaving it unstated. Only real keys were rewritten, so the documentation that names the legacy prefix still names it.

The bare ones were bare for a reason worth recording: the prefixed form used to **fail on the CLI**, which has been an open brief to the CLI team since August. Re-running [the comparison suite](../compare/index.md) today closed it. All six checks pass on sgit-ai v0.16.2, including *prefixed clone succeeded*.

### [The article that introduces Fractal Semantic Graphs, published here with its pictures](#introducing-fsg-article) [v0.2.97](../admin/versions.md)

graphsarticlesfractal-semantic-graphs

[Fractal Semantic Graphs: everything connects to everything, and nobody has to share a schema](../articles/introducing-fractal-semantic-graphs.md) is the introduction to the term, written for LinkedIn from [the page that defines it](../demos/fractal-graphs/index.md). LinkedIn cannot carry the diagrams, so this is the canonical copy: the same text, with nine figures placed where the prose earns them.

The three diagrams from the page are rendered as images (the zoom, the jump, the ladder). Beside them sit the screenshots the argument rests on: the GDPR atlas at altitude zero with its own *you are at the top of the fractal* panel, the Regulation Graph's hash-verified landing view, the AIUC-1 explorer with two vaults on one canvas, the ThreatModCon zoom ladder, the role risk map, and Article 45's timeline of rulings over an article that has not changed a word since 2016.

The bare URLs at the end became links, and the vault where the idea was first worked, [VoiceDebrief · Fractal Semantic Graphs](../demos/vaults/voice-debrief/index.md), joins the list. The article is CC BY 4.0, as written.

### [Vault #31 reaches the same conclusion about fractality, in its own words](#dsit-ai-risk-toolkit) [v0.3.1](../admin/versions.md)

vaultsgraphsgovernmentmethod

[The DSIT AI Risk Toolkit](../demos/vaults/dsit-ai-risk-toolkit/index.md) is an independent reference edition of the UK government's AI Risk Management Toolkit, and it is the first vault submitted under the `sgit_public_read_` prefix that [the credentials page](../docs/credentials.md) now asks for.

It models the guidance, the official workbook, the risk method and the cited frameworks as **four separate worlds with named bridges**: 617 nodes, 694 edges, eight predicates, every one of which declares an inverse. And the first of its four declared limits is this:

"Containment alone is not fractality. Cross-world edges make the semantic transitions inspectable."

That is the correction [the fractal graphs page](../demos/fractal-graphs/index.md) made yesterday, reached independently by another author in another vocabulary. The page now cites it, and the ladder gains a rung.

## The honesty is the other reason it is here

Every edge is labelled **curated** or **lexical**, with the limit written down: *"lexical mentions are not validated meaning."* Five source snapshots are retained with their URLs, retrieval dates and SHA-256, and two of its eight checks exist only to prove the official spreadsheet's bytes were not touched.

It publishes six gaps about itself. It corrects its own earlier count, to 208 formula cells from 227, and keeps the earlier briefing rather than overwriting it. It preserves a contradiction in the source instead of resolving it: the official file is named v1.1 and its own Welcome sheet says v1.0, so both labels stay. It leaves two broken defined names broken, because repairing somebody else's document is an edit. And it declines the flattering reading, stating that starter rows are not evidence of adoption.

**Audited before the key was published:** no credentials, no personal data, two published DSIT institutional contacts, the Open Government Licence acknowledged, official status disclaimed, and an all-zeros negative control that produced no clone where the real key produced 42 files.

## 2026-09-19

### [The site's own vault mirror is gone, deleted, purged from history, force-pushed](#the-mirror-is-gone) [v0.2.84](../admin/versions.md)

workflowgitmethodvaults

For 76 releases this site was one folder that was both an sgit vault and a git repository, and every release pushed both. Today the vault mirror was **removed from the tree, purged from all 112 commits with `git filter-repo`, and the branch force-pushed.** The repository went from 276 MB to 21 MB.

The question that led here was asked at v0.2.83: *do we still need it?* The honest answer was no, on four counts.

- **It had no reader.** Every session that built the site cloned it from GitHub. Not one release was ever produced from a vault clone.
- **It had no published read key.** The site publishes read keys for thirty vaults; its own was the one nobody could open. A zero-knowledge mirror of public content that nobody can read is storage, not publication.
- **It had been dead since v0.2.76, and nothing noticed.** The container holding the write key was recycled, `.sg_vault/local/` is gitignored by design, and seven releases went out over git alone with the live site correct throughout.
- **It was 91% of the repository.** 258 MB in 15,933 files, against 24 MB of content in about 750.

The purge is safe for the same reason the mirror was: everything removed was ciphertext under a key that was never in the repository. The vault itself, on the server, is untouched.

## What changed on the site

[The case study](../case-studies/one-tree-two-remotes.md) is now a retrospective, the workflow as it ran, the boundary that made it safe, the ordering rule, and a *why we stopped* section with the numbers. Every other page that described the pattern as current was rewritten: [why](../why/index.md), [admin](../admin/index.md), the [git-and-vaults](../docs/vault/git-and-vaults.md) note, the release-engineer role and prompt. Historical release notes stay as the dated records they are.

The tooling followed. `release.sh` no longer requires `.sg_vault` or pushes sgit, it still pulls the board vault first, and still refuses to call a release done until sgit.ai serves the new version. The key-leak tripwire now reads demo vault write keys from a gitignored `admin/local/demo-keys/` folder instead of the dead vault's local tier. And the [release history](../admin/versions.md) switches its commit column to git ids from v0.2.77 onward, which filled the seven rows the missing key had left blank.

## The three Vaults-menu pages were stale too

- [Demos](../demos/index.md) listed three vaults as *published* when there were thirty, and its *coming next* pointed at a plan already delivered. It now leads with the gallery and keeps the three original walkthroughs as what they are.
- [The catalogue](../catalogue/index.md) renders a vault live, and that vault holds **nine** entries against the gallery's thirty. The page now says so, with the date, and names [the gallery](../demos/vaults/index.md) as the complete list until the catalogue's key holder catches up. This is a write-key problem, not a publishing one: the twenty-one missing vaults are live on their own pages.
- The gallery's footer stopped calling the catalogue the place *new entries start*, because for twenty-one of them it was not.

**The rule that came out of it:** give a mirror a reader before giving it a remote. The board vault earns its place because the release pulls it and a page renders it. The site's own vault never did.

### [The jump, what the fractal property actually adds](#the-jump) [v0.2.95](../admin/versions.md)

graphsmethodcorrection

The Fractal Semantic Graphs page said that in a hierarchy *depth gives you more detail but no new meaning, because the only verb is "contains"*. The author's objection came in four parts, and all four are right.

A single layer's ontology can have a very large number of verbs, each carrying meaning. As long as the links make sense inside that ontology, knowledge is gained one link at a time, and it is a great deal of knowledge; a risk register with ten thousand well-named edges is not a hierarchy and not yet a fractal. **What the fractal architecture adds is the ability, on one of those links, to jump into another universe** with its own rules and definitions. And what makes that fractal is that every such self-contained world is built from the same blocks: nodes, edges, ontologies, taxonomies, triplets, provenance.

[The test section](../demos/fractal-graphs/index.md#what) is rewritten on the worked example he gave: a risk register whose incident fact jumps into security operations (alerts, signals, ATT&CK techniques, attack trees), whose suspicious DNS entry jumps into the DNS estate (zones, records, every request the resolvers logged, possibly millions of nodes served through an abstraction layer over SQL, a graph database or GraphQL), whose one record jumps into a packet capture. Four worlds, four ontologies, one path of named edges. A third diagram draws it.

Two consequences follow, in his words. **Every connection you follow should teach you something**, even when the answer is *nothing to see here*; whether a link added value is for the observer, or the query, to decide. And **more granularity means a better representation of reality**, chosen per context, with custom views on top of the whole being what makes it scale. It also runs upward: all four worlds are one node in a bigger graph, and the schema itself can be fractal in the Mandelbrot sense.

### [The root llms.txt was pointing agents at two 404s, and burying the guidance it should lead with](#llms-txt-routing) [v0.2.83](../admin/versions.md)

llmsagentsdocsmethod

Asked to check that an agent reading [`/llms.txt`](../llms.txt) finds the newest guidance, the answer was that **coverage was complete and routing was broken**.

Everything was in the file, the generator adds every page. But [the guidance front door](../docs/guidance/index.md) sat at line 149 of 239, as page entry 83 of 138, indistinguishable from `installation.md`. Meanwhile the orientation block at the top still said *"task-shaped guidance with recipes and agent briefs lives under /use-cases/"*, which is where that guidance lived **before** it moved to `/docs/guidance/` and `/docs/briefs/`. And none of the six scoped `llms.txt` files were advertised, so an agent reading the root had no way to learn that `/docs/guidance/llms.txt` or `/demos/vaults/llms.txt` exist.

Fixed with a **START HERE, BY WHAT YOU ARE DOING** block before the page list: four entry points by intent (building a vault, choosing a surface, writing a viewer, looking for a worked example) plus the list of scoped indexes.

## Two broken links, found by the guard rather than by reading

The routing block is hand-written prose naming generated files, which is exactly the drift this site keeps warning about. So the build now asserts that **every path the preamble points at is a file the build actually produces.**

It failed on the first run, and on the most important line in the file:

*"Never write a vault key into a tracked file. See `/docs/exposed-vault-key.md` for what that costs."*

That page is at `/case-studies/exposed-vault-key.md`. The advice about the costliest mistake in the product had been pointing at a 404. Widening the guard to every section then caught `/security.md`, referenced twice, where the page is `/security/index.md`.

Both were 404 on the live site, and the site's own validator had never looked, it checks links *inside pages*, and `llms.txt` is not a page. A file that exists to be read by machines had never been link-checked by one.

**Also corrected:** the preamble claimed this site *"is itself served from an encrypted vault."* The vault mirror last moved at v0.2.76 and six releases have gone out over git alone, so the claim came out rather than being left to rot.

### [The ladder's right column looked like links and was not, now it is](#ladder-links) [v0.2.88](../admin/versions.md)

graphsdesign

Second read of [Fractal Semantic Graphs](../demos/fractal-graphs/index.md), two fixes.

The *why this page exists* note, the LinkedIn back-story, is gone. The page stands without it.

The ladder diagram's right-hand column was long blue monospace text that read as a row of links nobody could click. Each rung now has two lines: the vault's name as a **real link** to that vault's page, where its read key is, and the detail beneath it in plain grey. Twelve links, each tested by clicking it in a browser and checking where it landed. The rule it re-learns: if it is blue, it must be clickable; if it is not clickable, it must not be blue.

### [How far down does the graph go? A page for the question that got three bare URLs](#how-far-down-does-the-graph-go) [v0.2.85](../admin/versions.md)

graphsvaultsmethodnetwork

Asked on LinkedIn whether we had *"defined the dimensions/layers needed to map this all the way down to say the EA and system configurations"*, the author answered with three links. The answer was right and the form was poor. [How far down does the graph go?](../demos/fractal-graphs/index.md) is the same answer with the pictures.

**The ladder.** Eleven altitudes from the text of a law to a compute instance, drawn as one diagram, each rung mapped to the published vault where that altitude is a live graph you can open: the [Regulation Graph](../demos/vaults/regulation-graph/index.md) for the law, the [Standards Atlas](../demos/vaults/standards-atlas-gdpr/index.md) for the layer the text omits, the [AIUC-1 conformance layer](../demos/vaults/aiuc-1-conformance/index.md) for the standard, its evidence and the policy it computes, the [Risk Graph Explorer](../demos/vaults/risk-graph-explorer/index.md) and [Agentic Browser Isolation](../demos/vaults/agentic-browser-isolation/index.md) for fact, risk, owner and acceptance, and [ThreatModCon 2025](../demos/vaults/threatmodcon-2025/index.md) for the eleven linked threat models that reach a method, a source file and a runtime.

**The rule.** One grammar at every rung, every edge a verb with a named inverse, `relates-to` banned, properties carrying data and never meaning, supersede rather than delete, which is what makes *fractal* a testable claim rather than an adjective. The GDPR atlas says it in its own graph view: *"You are at the top of the fractal."*

## The screenshots are new, and real

The atlas refuses to run outside a vault host. So a read-key clone was served locally behind a shim that implements `sg.vfs` over `fetch`, and its graph view was captured at three altitudes: the Regulation and its eight domains, then *Principles* and Article 5's seven, then one principle with its provenance. Nothing about the rendering changes between the levels; only the question does. [The vault's page](../demos/vaults/standards-atlas-gdpr/index.md) gained those views too.

## The honest section

The bottom four rungs (environment, runtime, compute) are modelled layers, not imports from a CMDB or an infrastructure repository. No published vault holds an enterprise-architecture repository as a graph joined upward to obligations; that is the rung the page cannot yet point at. The AIUC-1 crosswalks resolve at article level only. The GDPR atlas is a dated seed pass and uses the banned `relates` edge six times, counted from its own `graph/edges.json`. standards.sgit.ai models one instrument and has zero crosswalks. abp.sgit.ai's 23 capability primitives are the right shape to attach to a real permission set, and nothing published yet does. Named gaps get filled.

## Also fixed

The footer on every page still read *"this site is itself served from an encrypted SG/Send vault."* It has been false since the mirror died at v0.2.76, and was never true of the deployed pages, which GitHub Pages has always served. It now says what is true: thirty vaults open in your browser with published read keys, and the pages that describe them are static files.

### [Fractal Semantic Graphs, the page now leads with the definition](#fractal-semantic-graphs-defined) [v0.2.87](../admin/versions.md)

graphsmethoddocs

The author's first read of yesterday's page made three points, and all three were right. *How far down does the graph go?* is a section, not a title. The page must start by defining and visualising the term. And the first screens must work for a visitor who knows graphs, semantic graphs and ontologies but has never met the idea of a **Fractal Semantic Graph**, which for a while went by *graphs of graphs of graphs* and *ontologies of ontologies of ontologies*.

[The page](../demos/fractal-graphs/index.md) is now titled **Fractal Semantic Graphs** and opens with the definition in three sentences: a semantic graph is nodes joined by verbs with named inverses; a fractal one is a graph where every node is itself a semantic graph built by the same rules, down to the smallest thing that still matters to the question, in most of our work a word, a number or a symbol.

**The diagram.** Three panels of inline SVG: a four-node semantic graph; the Law node zoomed into articles and paragraphs, with an amendment drawn as an edge rather than a footnote; one paragraph zoomed into the terms it uses, each one edge from the article that defines it. The rules are the same in all three, which is the whole point, and the test for the word follows: *if zooming into a node needs a new format or a special case, the system is hierarchical, not fractal.*

**Why connect everything with everything.** Because every file format is already a graph (a PDF, a spreadsheet, a codebase, a JSON document) and only needs its edges named. Then questions cross formats without a join table, a correction propagates instead of being republished, the smallest node is whatever the question needs rather than what the format offers, and provenance comes free when the leaf is a word tied to a byte range and a hash. The discipline that keeps this from being noise: the edge has to be a verb.

A four-word table closes the opening (graph, semantic graph, ontology, fractal semantic graph) with what each adds and where it stops. Everything from *How far down does the graph go?* onward is unchanged.

### [Fractal means the inside is different, not the same. The definition had it backwards](#fractal-means-different-not-same) [v0.2.89](../admin/versions.md)

graphsmethodcorrection

Two releases ago [Fractal Semantic Graphs](../demos/fractal-graphs/index.md) defined the term as a graph where *every node is itself a semantic graph built by the same rules*, and gave the test as *if zooming into a node needs a new format or a special case, the system is hierarchical*. The author's read of the page caught that this is the wrong way round.

**Same types, same verbs, same rules at every level is a hierarchy.** A folder tree is the clean case: folders inside folders inside folders, one schema all the way down, and the deeper you go the less you learn. **It becomes fractal at the moment zooming in lands you somewhere different** (a node whose inside has its own node types, its own verbs, its own taxonomy, a new format or a special case) and that new world is still joined by an edge to the one above. Graphs of graphs, ontologies of ontologies. The plural is the point.

What stays constant is the **grammar**, never the schema: edges are verbs with named inverses, meaning lives in connectivity, every claim keeps its provenance. That is exactly what lets everything connect to everything without anyone being forced to conform. An organisation, a division, a single person, a regulator can each define their own world in their own vocabulary and connect to everyone else's by declaring edges, not by adopting a shared schema. And granularity becomes a decision per situation: a paragraph can be a mini-world with more definition than the document around it, because somebody needed it there and nowhere else.

The page is rewritten accordingly, lead, definition, the diagram's captions (panel two is now a legal ontology, panel three a lexical one, and the footer reads *the grammar never changes; the ontology does*), the test, the four-word table, and the ladder's intro: *eleven altitudes, eleven ontologies, one grammar.*

**One wording to pass upstream.** graphs.sgit.ai's boundaries page states the test with the word *format*. Read as "stops being a semantic graph and becomes JSON-plus-prose" it agrees with this page; read as "schema" it says the opposite, and this page read it the wrong way first. It should say *grammar*. Recorded on the page with the date rather than silently corrected.

### [Deleting files from git history, the exact scenario, drawn out](#deleting-files-from-history) [v0.2.86](../admin/versions.md)

gitworkflowmethodsecurity

Yesterday's purge of the vault mirror raised the right question: *did the force push actually happen, and what exactly did it do?* It did, git reported `+ e70d582d...b5ae665d dev -> dev (forced update)`, and [the new case study](../case-studies/purging-history.md) writes the whole scenario down with diagrams.

**The setup.** One folder that was both an sgit vault and a git repository; a remote with two branches, `dev` and a working branch from August that had been merged and forgotten. **What we wanted gone:** everything under `.sg_vault/`, 15,933 files, 91% of the repository, in every one of 112 commits.

**Why `git rm` is not deletion.** Every commit is a full snapshot, and a blob lives as long as any commit points at it. Removing the folder at the tip leaves 111 snapshots that still carry it; a clone downloads them all. **What the rewrite does:** `git filter-repo` rebuilds every commit without the path, and because a commit's id hashes its tree and its parent, not one of the 112 ids survived. **Why the push had to be forced:** the remote's tip is not an ancestor of the new tip, so a normal push is refused; `--force-with-lease` pinned to the old id makes the overwrite a compare-and-swap rather than a stomp.

## The part people miss

Git keeps every object reachable from *any* ref. The forgotten branch still pointed at the old chain (68 commits with 6,191 encrypted files in its tree) so after the force push a fresh clone still downloaded the purged objects, old commit URLs still rendered, and a single `git fetch` re-imported the lot into a clean clone. We verified that by doing it. Forks and `refs/pull/N/head` are the two places a branch deletion does not reach.

**When the branch is deleted,** three things happen on three timescales: fresh clones stop receiving the chain immediately; old ids stop resolving when GitHub's garbage collection runs, on its schedule or on request to Support; and clones made before the deletion keep the objects forever. That last one is why a history rewrite is never the first step for a leaked secret. Rotate, then rewrite.

**Recorded plainly:** the branch deletion was refused three times by the session's git proxy and is pending in the GitHub UI. Until it is done, the "still downloadable" section of the page is true as published. Everything purged was ciphertext under a key that was never in the repository, which is what makes this housekeeping rather than an incident.

### [A brief for graphs.sgit.ai, in place of a footnote](#brief-for-graphs-sgit-ai) [v0.2.94](../admin/versions.md)

graphsnetworkbriefs

The Fractal Semantic Graphs page carried a small footnote saying that graphs.sgit.ai had the fractal test backwards. The author asked for the footnote to go and for a proper brief in its place, since the sgit.ai page is now the fullest worked application of that site's two theses, *meaning through connectivity* and *thinking in graphs*.

[The brief](../docs/briefs/graphs-sgit-ai-fractal-semantic-graphs.md) quotes the boundaries page's own table and shows it contradicts itself: the Recursion row says *identical rules, no new format, no special case*, while the author's quote two paragraphs below says an article may be *so meaty that it requires its own ontology and taxonomy, and that's the power of the fractal element*. The quote is the side to keep. Replacement text separates the grammar, which survives every zoom, from the ontology, which is free to change at each.

It then lists what to adopt (the name and its lineage, the precise form of the thesis for the fractal case, *the deeper you go the more you learn*, *nobody is forced to conform*), where to link the page, what to reuse (both diagrams, the Standards Atlas screenshots), the four graph vaults missing from their evidence estate, a second cross-vault finding, three small corrections, and what not to change. The prompt to paste is at the end.

## 2026-09-18

### [Vault #30, the same pack, written for an archetype instead of a company](#the-same-pack-for-an-archetype) [v0.2.82](../admin/versions.md)

vaultsmethodprivacy

[Vault #30](../demos/vaults/fractional-ciso-pack/index.md) is a sibling of [#29](../demos/vaults/interim-ciso-pack/index.md) from the same generator, one day later, a fractional CISO pack: two days a month, on a retainer, for a company that is already certified. The interesting thing is how it solves the publication problem.

**#29 described a real role and withheld the company.** That meant auditing whether an unnamed FTSE 250 client could be inferred from what was said about it. **#30 describes a type of company instead**: six rows derived from public sources: what it does, who buys it, where the risk sits, what it already has, what it usually lacks, who governs it, and everything after follows from the archetype. There is nothing to redact, because nothing was ever about an instance.

The rule that generalises past hiring: **a document written for a class can be published; a document written for an instance has to be scrubbed.**

Three things are new. An **engagement document** with the monthly rhythm, a twelve-month map, and a section headed *what two days a month is not*, not cover, not a DPO, not delivery, not an audit, and not a substitute for a full-time CISO once the company needs one, *"part of the job is saying when that point arrives."* A **one-page infographic** rendered from `content.json` rather than drawn separately, which is the page's hero because it is the pitch on one sheet. And the three 2019 decks, now rendered in the viewer rather than only archived.

The *Honest tensions* section does something a sales document rarely does, it names how the offer could be misused against the buyer: a fractional CISO is cheaper than a permanent one, *"and that same economy can be used to defer a hire the company genuinely needs. Naming the trigger early is the only honest defence."*

Audit run and stated on the page: no company named or implied, no rate or tax status (*retainer* appears as a word with no figure attached), one public email, no secrets, read key verified against an all-zeros control. The two packs are worth reading as a pair, the same machinery giving two answers to *how do you publish a document about a job*.

### [The summit sheets get a preview grid, and their numbers are dated rather than corrected](#summit-sheets-preview-grid) [v0.2.81](../admin/versions.md)

publishingmethod

[The four Lisbon handouts](../summit/index.md) now appear on the parent page as four A4 previews (page one of each printed sheet, rendered from the PDF at build time and shown as a card) so a reader sees all four at a glance and clicks through to the page with the table, the embed and the download.

**The author's call on the stale vault count.** Yesterday's release made a point of *"26 public vaults"* having become 29 during summit week. The author's instruction is that the sheets are a dated record of what was said in September 2026 and should be kept as printed. So the correction became a dating note: the figures are those that were true when printed, [the live table](../demos/vaults/index.md) is the current answer, and the sheets are the historical one.

That is the right call, and the reason is worth writing down: **a printed artefact that gets silently re-edited to match today stops being a record of anything.** Date it, keep it, and point at the computed thing beside it.

## 2026-09-17

### [The Lisbon summit sheets, as pages, and as the PDFs they were handed out as](#the-lisbon-summit-sheets) [v0.2.80](../admin/versions.md)

publishingmethodnetwork

Four audience sheets written for a startup summit in Lisbon, [founders](../summit/founders.md), [startups](../summit/startups.md), [investors](../summit/investors.md), [corporate](../summit/corporate.md), are now [on the site](../summit/index.md), with a parent page, one page each, and the PDF both embedded and downloadable.

**The PDF is the download, not the page.** The capability table is rendered as real HTML, because a PDF is invisible to a search engine, to `llms-full.txt` and to any agent reading this site, the same argument [the deck viewer](../docs/briefs/vault-decks-on-a-site.md) makes. The handout stays a handout; the content is a page.

**What makes them worth publishing rather than filing** is the *what exists today* column, which is unflattering on purpose: *"no payment link"*, *"not yet packaged as its own product"*, *"research design; implementation not claimed"*, *"write-only intake built, never sold"*. A capability sheet that cannot say which rows are unfinished is a brochure.

Two things the check turned up, both while the sheets were still being handed out:

- **The filenames say RiskMandate.ai; the contents say sgit.ai.** Every page inside is branded sgit.ai and every footer points at `sgit.ai/network`. The copies here are renamed to match what is in them.
- **"26 public vaults" is now 29.** True when printed; three vaults were published during the week of the summit. The pages here do not restate the number and link [the live table](../demos/vaults/index.md) instead.

Which is the rule worth extracting from a stale line on a printed sheet: **a printed artefact should point at a computed one for anything that moves.**

### [A job application as a vault, and the privacy audit published beside it](#a-job-application-as-a-vault) [v0.2.79](../admin/versions.md)

vaultsmethodprivacy

[Vault #29](../demos/vaults/interim-ciso-pack/index.md) is an interim CISO candidate pack delivered as an encrypted vault instead of a CV attached to an email.

**The idea worth stealing is that the pack is the evidence for its own claim.** It says the candidate works with a team of AI agents and ships encrypted, versioned artefacts, and it *is* one. A reviewer does not have to believe the claim; the thing in their hands is the test of it. That idea is portable and has nothing to do with hiring.

Three structural choices are worth copying:

- **Split at the front door, not inside the document.** The recruiter gets a submission summary to copy and answers to screening questions, the things they actually have to paste into a form. The company gets eleven sections, two of them *Before signing* and *Tensions*. Anyone else gets the skills map and the history. Three readers, three routes, none of them a compromise.
- **Ship the machine-readable copy beside the human one.** Each of the four documents exists as PDF, Word, Markdown **and JSON**. The JSON is the one that matters: a CV as structured data, so a machine reading the pack gets fields rather than a page to parse. Same instinct as an `llms.txt`.
- **Let the build enforce the contract.** The pipeline fails if the page declares a vault resource, uses `fetch()`, writes `location.hash`, references a missing file, or contains a JavaScript syntax error, the last being exactly the check that [caught a shipped bug on riskmandate.ai](../demos/vaults/synthetic-users-riskmandate/index.md) the day before.

## The audit is on the page, not merely performed

The pack was submitted with a stated position: nothing sensitive, the company not identified, material already public. That is exactly the kind of claim that should be checked rather than accepted, so it was, and **it holds**.

The client is not named anywhere, described only as a FTSE 250 company, with regulatory applicability raised as open questions rather than answered. Day rates and the off-payroll analysis are absent, removed before publication, and the removal is **disclosed in the brief's own editor's note**, which is the harder and better choice. No phone, no address, one long-public email, no credentials. The read key was verified against an all-zeros negative control.

One point is stated rather than waved through: **thirteen named third parties** appear in the recommendations with their 2019 job titles. They are public twice over, LinkedIn recommendations, republished in the candidate's own CC BY-SA 2019 deck, which ships inside the vault so the source can be checked. They are labelled `title_2019` throughout. This site quotes the pack's own framing and does not reproduce the individual recommendations, which stay where their provenance is stated.

## 2026-09-16

### [The synthetic-user method runs a second time, and the second run is the better argument](#synthetic-users-second-run) [v0.2.78](../admin/versions.md)

vaultstestingagentsmethod

[Vault #28](../demos/vaults/synthetic-users-riskmandate/index.md) applies [#27's method](../demos/vaults/synthetic-users/index.md) to riskmandate.ai, one day later. That is the point: **one run is an anecdote, two sites is a method.**

It is not a repeat. The first vault **narrated**; this one **measures**: words above the fold, character offsets, scroll positions in pixels and screens. And more confusion from fewer steps (12 from 30, against 10 from 43) is the number to look at: the first site lost people slowly, this one lost them on the first screen.

**The headline finding is that the product is never named where it is sold.** Above the fold the home page says *policy* six times, *insure* three times and *underwriters* once, shows a £5 price, and never says **Agent Behaviour Policy**, which first appears **58% of the way down**. Two of the five read *"Buy one, from £5"* as buying an insurance policy for five pounds. The one who held that reading longest was the insurance professional: the reader best equipped to recognise the vocabulary, and therefore the most confidently wrong.

**A claim that specific is checkable, so it was checked.** The live page was fetched, rendered at the same 1440×900, and measured independently of the vault. Every structural number reproduces to the character: 9,270 characters of page text, first mention at 5,387, 6,481px and 7.2 screens, zero mentions of the product's name above the fold. Two count lines differ, and the page says *why* rather than hiding it: a broader `insur*` pattern that also catches "insurance", and one word at the fold boundary.

**The most useful finding in it is not an opinion.** The first pass recorded a JavaScript error on *every page it visited*. Both had shipped; the insurance page had been broken since it launched. As the vault puts it: *"every existing test passed, because the HTML still rendered and only the console knew."* Fixed in the same session, with a test added that parses every inline script on every page and fails the build if one does not. A study justified by its qualitative output paid for itself on a defect that has nothing to do with users, because the method happens to require driving a real browser and recording what it throws.

One persona, **Priya Raghavan**, walks both vaults. A persona reused across products is what turns two separate studies into a comparison, and it costs nothing but keeping the records in the same shape.

**Noted, not fixed:** the site's sgit vault mirror is behind its git mirror. The container holding the write key was recycled, `.sg_vault/local/` is gitignored by design, and the last two releases have gone out over git alone, which is what deploys the site, so the live pages are correct. The vault copy needs one `sgit push` from someone holding the key.

## 2026-09-15

### [Synthetic users, five people who do not exist, shopping](#synthetic-users) [v0.2.77](../admin/versions.md)

vaultstestingagentsmethod

[The 27th vault](../demos/vaults/synthetic-users/index.md) is the most useful one published here that contains no real data at all. Five invented buyers were walked through store.sgit.ai one screenshot at a time, asked what they made of each screen, and interviewed at the end: **43 steps, 15 questions the site did not answer, 10 recorded confusions, and 18 findings, three of them costing a sale.**

**The idea worth stealing is a deliberate handicap.** The agent is handed the *screenshot*, never the DOM, and the vault says why in one sentence: *"an agent that drives a store by reading the DOM finds the buy button every time, and therefore finds no confusion, which is the only thing worth running this for."* Competence at finding the button is the thing standing between you and the finding, so it is removed on purpose.

Three more things make it a method rather than an anecdote. The protocol is published **inside** the vault, so two runs a month apart are comparable rather than merely sequential. *Where did you guess* is a required field. And a run with no confusion anywhere is treated as a run done badly, not a site that passed.

**Read the viewport column.** The persona carrying the largest decision a single person makes alone on that site did the whole thing on a **390-wide phone**, and produced the most questions and the most confusion of anyone. The vault never states that. It falls out of the table once all five runs are counted in one place, which is the argument for putting runs in a vault instead of a document.

Zero page errors across all five runs, which is worth saying because it means none of the confusion was a bug in the store's code. It was the copy.

**Four findings are already marked fixed and kept rather than deleted**, on the stated grounds that *"a findings list that loses the fixed ones cannot be compared with the next set of runs."* The best of those fixes answered a request for a number with a disclosure instead: the page now says the time from a buyer's reply has never run for a paying buyer, so there is no measurement to quote. A synthetic user asked for a figure and got the harder, more honest answer.

**On the credential.** What was submitted was a **vault key**, not a read key. It was classified before it touched anything, the read key was derived one-way from it, and only the derived key is published, the vault key is not on this site and will not be. The derivation was proved rather than assumed: the derived key produced 67 files and a `clone_mode.json`, and an all-zeros key against the same vault id produced an empty directory. [That control exists](../demos/vaults/publishing.md) because we once called a leak on a directory an invalid key had created identically.

## 2026-09-10

### [The transfer API gets documented, and a dangling reference closes](#the-transfer-api-gets-documented) [v0.2.76](../admin/versions.md)

apitransferssecuritymethod

The team that owns the SG/Send API wrote an integration guide for sending an encrypted bundle to SG/Send from an agent workflow, and asked whether it belonged on this site. Checking rather than assuming turned up something worse than a missing page.

**The reference named a header for an API it never described.** [The authentication page](../api/authentication.md) has always listed `x-sgraph-transfer-delete-auth` among its six headers, *"transfer deletion, SG/Send transfers, not vaults"*, while the API section documented **zero transfer endpoints**. And the section's own lead called it *"the protocol surface"* while covering one of the two families that share this host. A reader following that header had nowhere to go, and a reader trusting that lead was being told something untrue.

[**The transfers page now exists**](../api/transfers.md), the header links to it, and the lead says plainly that two families share the host.

## What was taken, and what was not

The protocol is canonical and belongs here:

- **The two secrets that must never be confused.** An *access key* authorises **you to upload** and lives in a header. A *decryption key* authorises **anyone to read** and lives in the URL fragment, everything after `#`, which no browser sends to the server. They are unrelated values, and that distinction is the whole reason a share link can be both shareable and private.
- **The SGMETA envelope**, which exists so the filename never reaches the server: magic bytes, a big-endian length, the metadata JSON, then the file, wrapped *before* encryption, because the other order produces a corrupt download with no name.
- **The two traps in the create body**: `expires_at` is in **milliseconds**, not seconds; and `max_downloads: 0` means **unlimited**, not none.
- **The `download_url` that returns 404.** `complete` hands back `/d/{id}`, which is not a live route, build the share link yourself.
- **Revocation is opt-in at create time and impossible afterwards.** No `delete_auth_hash` when the transfer was created means that transfer can never be deleted.

The workflow half (credential wiring, node shapes, one product's bundle layout) stays with the product it was written for. It is good material; it is not protocol.

## The editorial contribution is knowing when not to use a vault

The page opens with a **transfer or vault** decision table, because restating someone else's endpoints adds nothing. What this site can usefully say is the other thing: a transfer has no history, hands over the whole payload or nothing, expires, and can be revoked. **A vault is the wrong answer for a handover that happens once**, and the API team reached the same conclusion independently for their own flow, which is worth more than either of us asserting it alone.

**Their verification is attributed, not adopted.** Every status code on that page was executed by them against production on 9 September 2026. We have not re-run it, the page says so, and the date is the thing to check it against.

## 2026-09-09

### [The shorts page rewritten for someone who arrives with no context](#the-shorts-page-rewritten-for-a-cold-arrival) [v0.2.66](../admin/versions.md)

vaultsvideoriskmandatemethod

A page of videos is a landing page whether or not it was designed as one. Traffic reaches [the seven shorts](../demos/vaults/licence-to-operate/videos/index.md) from a feed, lands on it directly, and has never seen the vault, this site, or the argument. What sat above the seven players yesterday was an apology about missing transcripts and a note explaining why a row number in the vaults table could not go stale, two pieces of internal housekeeping, both written for a reader who already knew everything the page had to sell.

Both are gone from the first screen. In their place, in the order a cold visitor needs them:

- **Four words, and the gap between two of them.** Grant, mandate, delta, licence to operate, defined in a table with the counts from the demo beside each: **12** capabilities in the grant, **4** in the mandate, **8** in the delta, and a licence priced per turn. The whole model is now legible before a single video plays.
- **Open the thing the videos are showing.** [The Licence to Operate vault](../demos/vaults/licence-to-operate/index.md), with its read key printed as the complete credential and both routes offered, its page here, or straight into the vault UI.
- **Where this goes commercially.** [RiskMandate.ai](https://riskmandate.ai/) named on the page: the business risk layer for autonomous systems, every autonomous system mapped to its blast radius, given a business owner, and driven to a time-bound decision, *accept, fund, or fix*. The vault is the demonstration; RiskMandate is the product it demonstrates; [the Risk Graph Explorer](../demos/vaults/risk-graph-explorer/index.md) is the same engine already published as a vault.

**The transcript gap is not hidden, it is right-sized.** It is still stated, in one sentence in the footer, and [board card T12](../team/board.md) is still open. A gap worth disclosing was not worth the first screen. The page was leading with what it lacks instead of what it shows.

Nothing changed about the seven videos, their order, or the three movements they fall into.

### [The llms.txt stops being a URL you have to guess](#the-llms-txt-stops-being-a-url-you-guess) [v0.2.73](../admin/versions.md)

llmsdocsagentsmethod

Six `llms.txt` files are published across this site, [the site-wide map](../llms.txt), [the vault catalogue](../demos/vaults/llms.txt), [the guidance entry point](../docs/guidance/llms.txt), and one each for [`/docs`](../docs/llms.txt), [`/docs/vault`](../docs/vault/llms.txt) and [`/api`](../api/llms.txt). Until now the only way to find one was to type it onto the end of an address and hope.

**Every page now carries a chip above its title** naming the one that covers it: *for agents*, the path, and the version and date it was generated.

Resolution is deepest-folder-wins. A page under `/docs/vault/` points at that section's index rather than at `/docs/llms.txt`; a page with no closer index falls back to the site-wide one. So every page has exactly one, and it is always the most specific one that exists.

**The stamp is the point, not decoration.** These files are regenerated on every release, so the chip says which release produced the index a reader is about to fetch. An agent editing a page can see at a glance whether the index has caught up with the page, if the page changed and the stamp did not, it has not.

Two details worth recording. The chip is **chrome, not content**, emitted between the nav and the page body, so it never reaches the markdown twins and cannot drift from them. And a **build assertion** now fails the build if the chip ever points at a folder no generator actually writes, which is precisely the failure this feature would otherwise have introduced quietly.

**Caught by building it.** The guidance page still *said* `/guidance/llms.txt` in two places, because [yesterday's move](../updates/index.md) relocated the file to `/docs/guidance/` and the rewriter fixed the `href` but not the prose around it. The page linked correctly while displaying a path that 404s. Fixed, and a reminder that a link rewriter fixes links, not sentences.

### [The build brief for putting a vault's decks on a website](#the-build-brief-for-decks-on-a-site) [v0.2.69](../admin/versions.md)

briefsvaultsdecksagents

Two releases documented this from the inside: [reading one file out of a vault](../docs/vault/reading-a-vault-file.md) explains the mechanism, and the deck pages demonstrate it. Neither told another agent how to do it to *their* vault. [**That brief now exists.**](../docs/briefs/vault-decks-on-a-site.md)

It follows the shape of [the telemetry brief](../docs/briefs/vault-telemetry-append-lanes.md), the shape that worked, because another team's agent built a vault from it and then sent back a review that corrected it.

- **The contract a vault must publish.** Where the manifest may live, deck sources pushing `t` / `notes` / `html` onto `S`, screenshots named symbolically rather than pathed, the CSS in the shell's style block, the PDFs. Plus the fallback for a vault that published only its built decks.
- **The rule that governs the design**, stated as a test anyone can apply: *a vault must be able to change what is shown and never what the page does.* If a vault can add a button, change where a link goes, or read anything belonging to the host page, the split is wrong.
- **The two frames, with their exact CSPs**, and the detail that a deck source must be handed to the parse frame over `postMessage` rather than baked into a `srcdoc`, or a deck containing the characters that close a script tag breaks out of the bootstrap running it.
- **Why a decrypted PDF cannot go in an iframe at all**, with the console message Chrome actually emits.

**It publishes both bugs, not just the finished design.** The image-name pattern that excluded underscores and failed silently on fifteen slides; the unscoped `closest()` that killed every button on exactly the pages it was written for. A brief that only describes the working version teaches less than one that names the two places a careful implementer will still go wrong.

It ends with a done-means checklist, walk every slide and assert zero unresolved images, byte-count a downloaded PDF against the vault, grep the built site for vault-key shapes, and a prompt to hand the builder agent.

One thing caught in review, worth recording because it is the third time: the `.md` twin rule strips inline code spans but not fenced blocks, so tag names inside the prompt failed the build. Rewritten to the site's uppercase-placeholder convention.

### [The agent chip becomes one object, and the network list catches up with the org](#the-agent-chip-and-the-network-catches-up) [v0.2.74](../admin/versions.md)

designnetworkllmsagents

**The chip.** [Last release](../updates/index.md) put an `llms.txt` link on every page, and it worked but looked like three loose fragments (a pill, a boxed path, and a long sentence) floating in the dead space between the nav and the breadcrumb, belonging to neither. Four directions were drawn against the site's own tokens and one was chosen: **a single bordered control** with a tinted *for agents* cell, the path in mono as the only emphasised element, and the version and date behind a dashed rule. It now reads as one thing you can click rather than three things you cannot.

The always-on sentence moved into the link's tooltip. It renders on all 124 pages, and as visible text it was instruction noise sitting above every headline on the site, the stamp beside it already carries the point.

**The network list was eight sites behind.** Checked against the organisation's 31 repositories rather than against memory: **games**, **what-can-it-do.games**, **providers**, **ungovr.providers**, **elevenlabs.providers**, **teams**, **threat-modeling** and **chrome-extensions** all had repositories, all answered 200, and none of them was listed here. Each new entry is written from what that site says about itself (its own title, description and version, fetched) rather than from a guess about what it probably contains. [The network](../network/index.md) now lists 27.

Two corrections fell out of the same check:

- **skills.sgit.ai** was still described here as *"the repository and subdomain exist; GitHub Pages has not published yet, so there is nothing to read at the address."* It has been live for some time. The entry now carries its real thesis (*skills are software packages, and here is the proof*) and its version.
- **The ElevenLabs repository describes its domain as `elevenlabs.provider.sgit.ai`**, singular. That does not resolve; the live host is `elevenlabs.providers.sgit.ai`, plural. The listing uses the one that answers.

A list of sites maintained by hand drifts from the sites that exist. This one drifted by eight in about a week, worth a check against the org on every release rather than when somebody notices.

### [Seven shorts on the Licence to Operate vault, indexed, and put in the right order](#seven-shorts-on-the-licence-to-operate) [v0.2.65](../admin/versions.md)

vaultsvideoagentsrisk

The author recorded seven vertical videos walking through [the Licence to Operate vault](../demos/vaults/licence-to-operate/index.md). None of them was on the site. [They now have a page](../demos/vaults/licence-to-operate/videos/index.md), collected in the order they are meant to be watched rather than the order a feed shows them:

- **The mechanism** (1–3), grant against mandate, what a block looks like when an agent exceeds its mandate, and how risk cascades from the support team to the CFO.
- **The artefact** (4), how to find and open the vault. The shortest one, and the one to send someone who wants to poke at it themselves.
- **The model** (5–7), why the grant/mandate gap is where risk lives, the insurance framing that governs it, and the policy, claim and premium mechanics underneath.

Each carries the author's own description plus a line mapping it to what it demonstrates: the **delta** for 5, [the AIUC-1 conformance layer's](../demos/vaults/aiuc-1-conformance/index.md) insurability query for 6, and risks.sgit.ai's *there is no deny button* for 7.

**What the page refuses to pretend.** These are descriptions, **not transcripts**. All four of YouTube's `timedtext` endpoints return empty for every one of the seven, so there is no caption track to pull, and the words actually spoken are absent from this site, from `llms-full.txt`, and from the chat pane's `read_page` tool. That is precisely the failure [the Risk Graph Explorer walkthroughs](../demos/vaults/risk-graph-explorer/videos/index.md) page was built to avoid, so the gap is stated in a box at the top, measured rather than guessed, and opened as board card T12.

**A number that cannot rot, demonstrated by accident.** Video 4 tells the viewer to look for *"Vault #23"*. Checked against the table: Licence to Operate is still #23, and always will be, v0.2.58 made that column a permanent publication ordinal rather than a row position. A recorded video naming a row number would have been wrong within a day. Naming an identity is safe, and this is the first time that decision has paid for itself.

Embeds go through `youtube-nocookie.com` with `loading="lazy"`, so opening the page sets no YouTube cookie until somebody presses play. The players needed new 9:16 CSS, the existing embed box is 16:9, and a Short in it is two black pillars.

### [One front door for vault guidance, and every document moved under /docs/](#one-front-door-for-vault-guidance) [v0.2.72](../admin/versions.md)

docsguidancevaultsmethod

The guidance here had accumulated across three top-level folders, `/briefs`, `/vault`, and a `/guidance` page written this morning. That is three places to look for one kind of thing. **Everything readable now lives under `/docs/`**: [`/docs/briefs`](../docs/briefs/index.md), [`/docs/vault`](../docs/vault/index.md), [`/docs/guidance`](../docs/guidance/index.md), beside the CLI docs that were already there.

Fourteen pages moved. The links were rewritten by resolving each one through the move map rather than by prefixing `../`, a blanket prefix would have broken every link that stayed *inside* the moved subtree, which was most of them. No redirects, by instruction: the estate is in flux and has few external users. One thing nearly went missing: two hand-written `.md` briefs live only in the built output and not in the content tree, so the cleanup deleted them; they were restored from git into the new location before anything was pushed.

## The front door

[**Working on a vault: start here**](../docs/guidance/index.md) is the page that did not exist. The first thing on it is the guidance that gets repeated to agents more than any other:

**Version everything, show the version, link what changed.**

The number belongs in the app chrome (small, always visible, not in a footer or an About box) and it must link to *that version's own details*, not to a generic changelog. A reader who clicks `v0.1.7` wants to know what v0.1.7 was. Versions live in the vault as `versions/index.json` plus one file per version, each naming the commit it was built from and saying whether it was recorded or reconstructed. [The AIUC-1 conformance vault](../demos/vaults/aiuc-1-conformance/index.md) is named as the reference implementation, because it already does exactly this.

Seven more practices follow, each stated with the failure that produced it, including the one about negative controls, which exists because `sgit clone` creates a directory whether or not the key is valid, and we once called a leak on a directory an all-zeros key produced identically.

## The agent-shaped twin

[`/docs/guidance/llms.txt`](../docs/guidance/llms.txt) is the same thing for an agent: five rules, a reading order, the briefs, and reference implementations to go and check rather than take our word for. It ends with edges out to **coding.sgit.ai**, **nfrs.sgit.ai** and **graphs.sgit.ai**, because a page about vaults should not also try to be the style guide, the resilience argument, or the grammar of semantic graphs. Each of those has a site with room to do it properly, and an agent that stops at this domain gives a worse answer than one that follows the edge.

The page closes by saying why it is mostly links, which is graphs.sgit.ai's own thesis applied to the thing you are reading:

"A node is just a node. **Meaning lives in the edges.**"

Three properties keep that working, and they are worth preserving in anything built here: every page is reachable and has a `.md` twin, with the build failing on an orphan; indexes are generated from the data they index, so [the vault catalogue](../demos/vaults/llms.txt) cannot disagree with the table it comes from; and each site says one thing properly and links out rather than summarising the rest badly.

### [The second build brief, and it mostly says don't build it](#markdown-and-file-viewers-what-not-to-build) [v0.2.70](../admin/versions.md)

briefsvaultsagentsmethod

Two of the most common things an agent is asked to add to a vault are a **markdown viewer** and a **file/folder browser with raw views**. Both already exist in the vault platform, and most requests for them are answered by publishing files in the right shape and writing no code at all. [**The brief now says so.**](../docs/briefs/markdown-and-file-viewers.md)

It is a decision rather than a syntax reference, [the syntax reference already existed](../docs/vault/content-authoring.md). A four-rung ladder, with the instruction to stop at the first rung that works:

1. **Publish `.md` files.** The browse view renders them and its file tree *is* the folder viewer.
2. **Add a `_page.json`** if you need a designed page rather than a document, and use its `markdown` component to pull in the `.md` files you already wrote, so the prose exists once.
3. **Build an app** only when a view has to *compute* something the host cannot know.
4. **Build a site viewer** only when the content must live outside a vault host, [the decks brief](../docs/briefs/vault-decks-on-a-site.md) covers that case.

It names the markdown rules that actually catch people, rather than the full syntax: raw HTML is stripped and shows as escaped text, images size through the pipe syntax inside the alt text, folder links must go through `folder/README.md` because a bare folder link resolves by sort order, and nested and task lists are unsupported.

**The raw-view contract comes from a vault that already lives by it.** [The AIUC-1 conformance vault](../demos/vaults/aiuc-1-conformance/index.md) has a file explorer, and its own source states the principle better than a brief could:

"Raw is the point, a catalog that asks to be trusted has to be readable in the form it was written."

The brief adopts that whole: raw always available for every file, a reader as an addition and never a replacement, the tree driven by a build-time manifest rather than a runtime walk, files fetched on click. Generalised, it is a habit that runs through the whole estate, `_page.json` has its `{ } Source` toggle, every page on this website has a `.md` twin, the deck viewer offers the printed PDF beside the rendered slides. **Anything rendered should be one click from the thing it was rendered from.**

One correction made while checking the schema: the content-authoring page said *eleven* component types and then listed twelve. It says twelve.

### [Guidance now splits by surface, and the third surface finally has its own brief](#guidance-splits-by-surface) [v0.2.71](../admin/versions.md)

briefsdocsvaultsmethod

The guidance here had been organised by **task**: decks, markdown, file viewers. That hid something: every one of those questions has three different right answers depending on *where the code runs*.

[**Three surfaces**](../docs/surfaces.md) is the router. `_page.json` inside a vault, an HTML vault app inside a vault, and a page on a `*.sgit.ai` site outside every vault host, compared on where they run, who reads the vault, which credential is used, what the reader needs, whether search engines and agents can see them at all, and the row people get wrong:

**Trust direction.** Inside a vault host, the host protects the reader: it sandboxes the app, gates permissions, keeps a sovereignty rail the app cannot suppress. On a site page there is no host, *you* are the host, and vault bytes are untrusted input arriving in your origin. The same content, the opposite posture.

A second table does the same job the other way round: markdown, file browsing, decks, PDFs, computing over data, and being findable by someone who has never heard of you, which only one of the three surfaces does at all.

**[Reading a vault from a site page](../docs/briefs/sgit-ai-site-pages.md)** is the brief that did not exist, for whoever is coding the estate's sites. It leads with the enabling fact, which is easy to miss: the vault API answers **plain CORS GETs with no auth header, from any origin**. The server can afford that because what it returns is ciphertext under a key it has never held, so a page on `graphs.sgit.ai` or `risks.sgit.ai` reads a published vault directly, with no proxy and no backend.

It then says **do not write the reader** and names the four house files to copy instead, `vault-embed.js` exports the reader so nothing has to reimplement the derivations, `vault-docs.js` is the instrumented version, `vault-deck.js` a worked viewer, `vault-ui-embed.js` frames the official UI. It states the inverted trust rule with a table of how to render each kind of vault content, covers the ref-caching trap that fails *silently* by rendering an older commit from perfectly valid ciphertext, and says what should not go on a site page at all: duplicated vault prose, a rebuilt vault app, and any arrangement where the site is the only way to read the vault.

Six guidance pages now carry a **surface label** above their title, so the distinction is visible where someone actually lands rather than only on the router. Unlabelled pages apply to all three.

### [Decks and PDFs read straight out of a vault, with the viewer owned by the site](#decks-read-straight-out-of-a-vault) [v0.2.67](../admin/versions.md)

vaultsdeckssecuritymethod

The vaults publish presentations. Four of them sit in [the AIUC-1 conformance vault](../demos/vaults/aiuc-1-conformance/index.md#decks) and five in [Licence to Operate](../demos/vaults/licence-to-operate/index.md#decks), and until this release the only way to see one was to open the vault's own app and drive it. They now play on the vault pages themselves, fetched as ciphertext with the read key already printed at the top of each page and decrypted in the reader's browser.

**The split is the whole point.** From the vault come the manifest, the slide sources, the speaker notes, the screenshots and the printed PDF. From the site comes every control you can click, the deck tabs, the slide list, prev and next, the notes toggle, the PDF button, the deep links. A vault decides what is *shown*; it never decides what the page *does*.

That matters because a read key is public, but the bytes behind it were written by whoever holds the write key, so vault content arriving in a page is untrusted input. It reaches these pages through two opaque-origin frames and nothing else:

- **A deck has to run.** It builds its slides by calling `S.push({t, notes, html})`, so it executes in a sandboxed frame with `default-src 'none'` and posts back a plain array. The site never evaluates it.
- **A slide does not.** Its markup renders in a second frame with `allow-scripts` withheld entirely and a CSP whose only permitted load is a `data:` image the host decrypted itself. Nothing in a slide can phone home.

**Why the PDF is a download and not an embed, measured, not assumed.** The obvious move is to decrypt the PDF, wrap it in a blob and point a sandboxed iframe at it. Chrome refuses, in every sandbox combination tested: *"failed to load as a plugin, because the frame into which the plugin is loading is sandboxed."* The browser's PDF viewer is a plugin and plugins do not run in sandboxed frames. Dropping the sandbox would work and would hand vault bytes this origin, which is the one thing the design exists to prevent. So the bytes are decrypted in the page and handed to the browser's own download instead, a 2.1 MB deck arrives byte-identical, while the slides, the thing anyone actually wants to read on a web page, render live.

**A real bug, found by walking everything.** The first pattern for image names excluded underscores. Fifteen slides in the Licence to Operate decks therefore rendered with a silently missing screenshot: no error in the console, no gap in the layout, just an absence nobody would notice by clicking through a few slides. The browser test now walks all 113 slides across all nine decks and counts missing images; the count is zero.

Two published deck shapes are handled, because the two vaults genuinely differ (one shipped its deck sources, the other only its built decks) so the reader prefers the source and falls back to the built file, truncated where the vault's own viewer begins.

New page: [**Reading one file out of a vault**](../docs/vault/reading-a-vault-file.md), which is the primitive underneath every live embed on this site, written down on its own for the first time, with the sandbox rules for what comes back.

### [A page per deck, a focus mode, and a vault catalogue an agent can read](#a-page-per-deck-and-a-catalogue-agents-can-read) [v0.2.68](../admin/versions.md)

vaultsdecksllmsmethod

Yesterday's release put the decks on the vault pages. Three things were missing, and this release adds them.

**A page per deck.** Each of the nine published decks now has one, [four under the AIUC-1 conformance vault](../demos/vaults/aiuc-1-conformance/decks/index.md), [five under Licence to Operate](../demos/vaults/licence-to-operate/decks/index.md). A deck page opens that deck alone, tab strip gone, and carries what the slides cannot: the level it answers, the vocabulary it introduces, who it is for, where it deliberately stops, the question it ends on, and which deck picks that question up. Each also has a **Notes on this deck** section that is deliberately empty and says so, that room is the whole reason a deck deserves a page rather than a tab, and it is where a narrated recording will be linked once one is mapped to a deck.

**Focus.** A button that drops the slide list so the stage takes the full width, for presenting, and for recording a screen capture where the chrome is just noise. The stage is re-fitted rather than merely revealed, so the slide actually gets bigger.

**A bug the new pages exposed within a minute of existing.** The mount element carries `data-deck` on a single-deck page, and the click router used an unscoped `closest('[data-deck]')`, so it matched the mount element for every click inside the viewer and returned early. Prev, next, notes, focus and the PDF button were all silently dead, on exactly the pages just built. Nothing threw; the buttons simply did nothing. Scoped to the tab strip, and caught because the browser test asserts on the *effect* of clicking rather than on the click landing.

**A catalogue an agent can read.** [`/demos/vaults/llms.txt`](../demos/vaults/llms.txt) is the published-vault catalogue as an agent index: all 26 vaults with id, category, published date, size, file count and published read key. It is generated from `vaults.json`, the same file [the vaults table](../demos/vaults/index.md) is built from, and each read key is lifted from the vault's own page rather than kept in a second list that could disagree with the first. Read keys are the whole credential for reading and are published deliberately; vault keys appear nowhere, here or anywhere else.

Three more sections got their own: [`/vault/llms.txt`](../docs/vault/llms.txt), [`/api/llms.txt`](../api/llms.txt) and [`/docs/llms.txt`](../docs/llms.txt). An agent pointed at one part of the site now gets that part's index instead of the whole map.

### [A brief for the vault map infographic, which spends its first half on why not to start with the picture](#a-brief-for-the-vault-map-infographic) [v0.2.75](../admin/versions.md)

briefsvaultsdesignmethod

An image model produced an infographic of the `*.sgit.ai` sites, one shared foundation, five numbered columns, a band of conceptual links, a footer of counts. It is good. The ask was for a companion covering the **26 published vaults**, grouped by use case and industry. [The brief now exists](../docs/briefs/vault-map-infographic.md), and it leads with the two things that sit upstream of any image being generated at all.

**The picture it copies has already gone stale.** The network infographic's footer reads *"19 sites · 18 published · 1 forthcoming"*, and its cell for `skills.sgit.ai` says *Forthcoming*. [The network](../network/index.md) now lists **27**, and skills.sgit.ai has been live for some time. A picture roughly a week old is wrong in its headline number and in one of its cells.

That is not an argument against making one. It is the constraint to design around. So: every count computed from the data at generation time; the image stamped with the version and date, the same way [every vault app should carry its version](../docs/guidance/index.md#versions); the live table linked beside it, because the infographic is the overview and [the table](../demos/vaults/index.md) is the truth; and regeneration on the release checklist as a diff, if the vault count changed, the image is stale.

**Neither requested grouping exists in the data.** Checked rather than assumed: `vaults.json` carries `category` on all 26 (but that is the vault's *shape* (Application, Analysis, Record, Reference…), not its use case) `job` on only **6 of 26**, and **no `industry` field at all**. So the first deliverable is two fields, not an image: `use_case` and `industry`, written from each vault rather than from its title, with closed vocabularies the build enforces, and `cross-industry` treated as a real answer rather than a sector invented because a vault mentions money.

That is the same rule the rest of the estate runs on, indexes are generated from the data they index, because one maintained by hand becomes a lie on a schedule.

**Then the rules for a model that renders text as shapes.** Generate the caption list from the data first and treat the image as a rendering of it; read every string back against `vaults.json`, character by character on the names; count the cells; and let no vault appear that is not in the file, a plausible invented name is the most dangerous output this process can produce, because nothing throws.

And the publishing rules this site already imposes: the validator bans `img src`, so the `data-shot` pipeline applies; alt text is the accessible equivalent, not a caption; and the grouped list goes on the page as HTML beside the picture, so the markdown twin carries the substance instead of a reference to pixels.

## 2026-09-07

### [Two new sections, the team, written for the agents; and investors, in the open](#the-team-for-the-agents-and-investors-in-the-open) [v0.2.62](../admin/versions.md)

teamagentsinvestorsboardmethod

**[The team](../team/index.md)** is the agentic section: how this site is run by one person and a team of AI agents, written for the agents. A new agent should be able to read that page and one role page and begin.

- **Nine roles, each a file.** Sherpa, Publisher, Auditor, Journalist, Cartographer, Ambassador, Designer, Release engineer, Historian, mirroring the Explorer team in the CLI repository, specialised for running a site rather than building a tool. Each page carries the role's mission, what it owns and must not touch, the files it works in, the checks it runs, **the rules it enforces with the mistake that produced each one**, and the prompt that starts it from nothing. The Publisher and Auditor exist because this site publishes read keys on purpose and has to be certain what they reach.
- **[Twelve starting prompts](../team/prompts.md)** for the work that recurs, publish a vault, audit it, write the update, write an article, add a sibling site, handle an inbound brief, cut a release, fix a phone bug, turn markup into data, correct a claim, update the board, re-verify the read keys. Each is written to be pasted into a fresh agent, and each ends before the release step on purpose: the release engineer's prompt is the one that ships, and the Sherpa decides when it runs.
- **[The board](../team/board.md)** is a kanban of files. Each card is a markdown file with a `status` line; the five columns are those lines rendered. **Needs**, items only the author can supply, are kept apart from tasks and never discovered late. This follows issues-fs.sgit.ai's *issues are files* and the open comms board on open-source.sgit.ai. It is seeded with the real open work, including six things only the author can answer.

**[Investors](../investors/index.md)** follows the founder's practice of publishing investor material in the open, and the structure of the pitch his other companies publish: the problem, what it is, the open-source zero-knowledge architecture, traction, business model, the beachhead market, what could go wrong, and the materials. Two rules hold it honest:

- **Traction is computed from the site**, with the same generator the homepage team band uses. If a number is wrong, the site is wrong somewhere else too.
- **The ask is left visibly open.** Round size, instrument and use of funds are the founder's to state; the page has a dashed box saying so and tracks it as board item N1, rather than a number nobody supplied.

The business-model section does not restate the founder's position on open source; it points at it through the new sibling-site card, so the argument is read in its own words.

**Nav:** *Try* folds into Docs; *Why* becomes a group with Investors; *Team* is new. Eight top-level items, as before.

One build lesson, recorded because it bit twice: angle-bracket placeholders inside code spans broke the markdown twin while being regex-wrapped. The whole team section now uses `UPPERCASE` placeholders with no angle brackets, one convention that survives every renderer this site has.

### [The proof moved up, the homepage, rebuilt to show vaults before it explains them](#the-proof-moved-up) [v0.2.60](../admin/versions.md)

homepagepositioningvaultsagents

The homepage is rebuilt, following [the diagnosis published this morning](../articles/proof-behind-the-claim.md) rather than a fresh opinion, and [the "after" article](../articles/proof-moved-up.md) puts each new band beside a screenshot of what it replaced, so the comparison is honest rather than flattering.

**The first screen now shows vaults.** The headline changed from *"the encrypted git for humans and AI agents"* to *"a vault is a unit of work: data, app, history and sources, shipped as one string."* Encryption did not leave, it became the subordinate clause, which is where a property nobody can look at belongs. Under it: **four real published vaults**, a screenshot each, one click from open. Which four is a field in the vault data, so changing the front door is a data edit.

**The use cases became things.** A new band, *what people actually ship*, replaces five category cards with six vaults chosen by the job they do, hand over a report, publish a standard as data, give a talk, pitch an investor, ship a game that reports back, give an agent a workspace, each with one line on why it is hard any other way. None of those lines is about encryption.

**The collaboration story got a front door.** *One human, a team of agents*: four numbers computed at build time (releases, vaults, sibling sites, cross-team briefs) and the loop told in three beats with the artefacts linked. The numbers are not typed here or on the page, and this sentence deliberately does not repeat them: the first draft did, and was off by one within the hour because a release had happened. The tile cannot drift; prose can.

**Cut:** the abstract use-case band (the pages remain, in the nav) and the *three doors* band (now one pill in the trust strip). **Moved down:** the terminal walkthrough, under *Under the hood, it is git*, because for a visitor who has just opened a real vault, *how* is now the question. The band count is unchanged (nine before, nine after; three cut, three added) so what changed is the order and the first screen. The page got longer in bytes, because ten screenshots replaced paragraphs, and shorter in words.

**One thing the computed number caught.** The network heading had been retyped as "Twenty sites" while the tile beside it said 19. The tile was right (nineteen siblings, twenty with this one) and it is the tile that cannot drift.

**The gap stands.** No published vault yet shows two agents on one vault with a human merging their branches. The band tells the story of agents building *for* each other, which is evidenced, and is written so as not to pretend it shows more.

### [The diagnosis before the rebuild, and a card for pointing at the sibling sites](#the-diagnosis-before-the-rebuild) [v0.2.59](../admin/versions.md)

homepagearticlesnetworkmethod

Asked to step back and say how this site should present its twenty-five published vaults, the answer was a diagnosis rather than a redesign, and it is published first, as [an article with screenshots of the current site](../articles/proof-behind-the-claim.md), so the rebuild that follows can be compared against it honestly.

The short version: **the proof is two clicks behind the claim.**

- The homepage leads with encryption, which cannot be looked at, and a terminal walkthrough of `create`, `commit`, `history` and `clone`, commands every git user has watched a thousand times. The word *vault* appears three times in the hero and the visitor is never shown one.
- The twenty-five artefacts a stranger can open in one click, with no account, sit under a dropdown as a table. A good table now, but a table is the right shape for *finding* a vault and the wrong shape for being *convinced* by one.
- The use-case cards are categories. Concrete examples of every one of them exist one level down.
- The strongest story, agents building for agents; a brief published here turned into a vault the same day, then reviewed by the team that owns the API, is filed under Docs, as a log.

One gap named plainly: the homepage's strongest multi-agent claim, *a branch per agent and a human reviews the merge*, has **no published vault behind it**. Every vault here was built by one agent, or by one agent on another's finished work.

The fix is set out in order (proof before mechanism; reorder and cut rather than add) and is the next release.

**Also new: a card for pointing at the sibling sites.** The `*.sgit.ai` sites exist so each topic gets the depth a section here could not give it, which only pays off if this site points at them constantly, and a bare link does not say *this continues elsewhere, on purpose*. A one-line `!site` directive now renders a card that pulls the target site's own category and thesis from the network directory, so it describes that site the way the site describes itself. It debuts in the article pointing at [open-source.sgit.ai/about](https://open-source.sgit.ai/about/index.html), which is also a decision recorded there: this site will get an About page about **sgit**, and link to the fuller record rather than duplicate it.

### [The board moves into a vault of its own, and its read key is published](#the-board-moves-into-a-vault) [v0.2.64](../admin/versions.md)

boardvaultsteammethod

Two releases after [the board](../team/board.md) appeared as files in the site repository, the shape was right and the home was wrong: moving a card from *review* to *done* cost a full site release, build, validate, two pushes, and a wait for the deploy to verify. A board should be cheaper to update than the thing it tracks.

So the cards moved into [a vault of their own](../demos/vaults/board/index.md), `pdulwi6i`, and its read key is published, because every task, bug and need on it is public, and a read key is the complete credential for reading them.

- **The vault is the truth; the site is a reader.** The release script pulls the vault before it builds, and the columns on the board page are labelled as a snapshot at the site version. Between releases the vault is ahead, and opening it shows the live board.
- **Moving a card is `sgit push`.** Edit one `status` line, regenerate the index, commit, push. No site release.
- **A board app that asks for nothing.** `index.html` lists `issues/` through `sg.vfs` and draws five columns; `app.json` declares `permissions: {}`. Served outside a vault host it falls back to `issues/index.json`, so it can be screenshotted, tested and read from a script, a board that only renders inside one host is a board nobody can check.
- **Cloned in place.** The site's `admin/content/team/issues/` *is* the vault's working tree: its encrypted store is gitignored, its card files are tracked as the build's input. If the two ever disagree, the vault is right.

Published as row #26 on the [vaults table](../demos/vaults/index.md), following the method: write key escrowed, audit run (nothing secret-shaped beyond the read key in its own README), the app screenshotted by driving it, permissions stated. The Sherpa's [board prompt](../team/prompts.md#board) now ends with a push rather than a build.

### [Our build brief was wrong, and the team that owns the code said so precisely](#our-brief-was-wrong-and-the-team-that-owns-the-code-said-so) [v0.2.58](../admin/versions.md)

briefsapicorrectionagents

Two days ago v0.2.55 published a [build brief](../docs/briefs/vault-telemetry-append-lanes.md) on getting telemetry out of a vault whose read key is public. An agent [built a vault from it](../demos/vaults/agent-permission-games/index.md) and could not get events out. The SG/API team read the append-lane code against our page and returned a line-referenced review.

**Both of the things the brief told a builder to *verify*, it had already answered wrongly.**

- We said `sg.append.write` fails closed in a read-only session. **It does not.** There is no read-only gate on append anywhere; `permissions.append.write: true` is the entire requirement, and `sg.app.writable` is irrelevant to it. The `EREADONLY` we cited belongs to `sg.vfs.write`, a different code path that happens to deny with the same string, which is exactly how the misdiagnosis propagated.
- We steered readers to a direct `fetch` instead. That path is **blocked by default**: the frame ships `connect-src blob: data:`. The escape hatch is `permissions.network: true`, which the reviewer notes appears *"zero times"* in the authoring guide and zero times on our page, *"discoverable only by reading `app-permissions.js`."* It is also the wrong fix, since it reopens every egress from a frame holding decrypted vault content.

The brief now recommends the bridge, and the correction sits in a box **above** the section it corrects rather than being edited in quietly. The prompt at the bottom, the part written to be pasted to a builder, is reversed.

**It also resolved an open finding.** When the games vault was published we could not confirm the write endpoint and said so rather than guessing. The answer is that its telemetry is *built and never sent*: the vault declares no permissions at all, so the CSP blocks its sender. That matches the author's report that nothing arrived, and [its page](../demos/vaults/agent-permission-games/index.md) now leads with that status instead of claiming it phones home.

**Three facts that existed nowhere public** are now on [the API reference](../api/append-lanes.md): only `write` takes a `vault_id` while the other five verbs bind to the currently open vault, so listing a remote lane is impossible by design; `fetch` maps to `append.read`, not `append.fetch`; and the `inbox` field in a listing is the lane folder, which today is the **raw append token** while config stores only its hash.

Seven questions went back, including the two we most want to publish: whether the enum-key derivation is stable enough to document as a spec, and whether any non-destructive way exists to tell an append token from a read key. They are the same 64-hex shape, and confusing them would be a serious leak.

Also in this release: the `#` column on [the vaults table](../demos/vaults/index.md) was renumbering 1–25 on every sort, which said nothing. It is now a permanent publication ordinal, `#1` is the first vault ever published here, so it never changes, and sorting by it is by construction the same order as sorting by date.

### [Ask this site, a pane on every page whose model calls tools over the site's own content](#ask-this-site) [v0.2.63](../admin/versions.md)

chatllmtoolsbyokagents

Every page now carries a pane, bottom right: **Ask this site**. It follows the three tiers the [network chooser](../articles/chat-on-a-static-site.md) set out, with one difference that matters. The model does not read a catalogue pasted into its prompt. It is given **seven tools** and calls them.

| Tool | What it does |
|---|---|
| `search_site` | keyword search over pages, vaults, sibling sites, release notes, articles, roles and board cards |
| `read_page` | the markdown twin of any page, up to 6,000 characters, so the model quotes rather than paraphrases |
| `list_vaults` · `list_sites` | the vaults table and the network directory, filterable by category |
| `latest_updates` · `get_board` | the feed and the kanban |
| `current_page` | what the reader is looking at, for "this page" questions |

- **No key:** the tools run directly. Type words to search everything, or `/vaults`, `/sites`, `/updates`, `/board`, `/read PATH`, `/here`. Instant, private, no network once the index has loaded.
- **Your own OpenRouter key:** the model gets the seven tools as function definitions, calls them, and **every call is shown** as a trace line above the answer. Each call executes in the page over a build-emitted index and the `.md` twins, so the model can only say what a tool returned. It ends with the paths it used, as links.
- **Inside a vault:** the host could hold the key below the permission floor through `sg.llm`. Not wired yet, blocked on whether the bridge's chat contract carries tool calls, and on [the board as T11](../team/board.md#T11).

The index the tools read, `assets/site-index.json`, is written beside `llms.txt` from the same data as the vaults table, the directory, the feed and the board. One derived file: an answer given in the pane is an answer the site already gives somewhere.

The key goes to openrouter.ai and nowhere else, sgit.ai has no server to send it to, and the pane says so in the same words the chooser uses. Model output is escaped, and links are allowed only to `http(s)` or to paths on this site.

The [chat article](../articles/chat-on-a-static-site.md) gains an addendum, and its *shared component: not started* row becomes *partly*: this is one site's copy, not yet the versioned module the other eighteen could load.

## 2026-09-06

### [The vaults table stops being a key dump, sortable, categorised, newest first](#the-vaults-table-you-can-sort) [v0.2.57](../admin/versions.md)

vaultsuxmobile

Reported from an iPad, where the failure was obvious in a way it never is on a desktop. The read key is a 64-hex string; giving it room squeezed the vault id down to **one character per line**: `ookq4mn4` rendered as a vertical stack.

The fix was not narrower columns. It was noticing that the two widest columns were the two nobody needs on an index: the read key and the *open live* link are both already on each vault's own page, one click away. So [the index](../demos/vaults/index.md) now answers *which of these do I want*, and the vault's page answers *how do I open it*.

**Gone:** the read key, the open-live link, and the dense contents blob. **New:** a `#` column, a one-line **what it is**, a **category** pill, files and size as separate numeric columns, and a **published** date. **Click any heading to sort**: default newest first, because the recent ones tend to be the interesting ones. The count line carries the total and the breakdown: 25 vaults across 8 categories.

**Generated, not hand-written.** Twenty-five hand-written table rows could not be sorted, counted, or kept consistent, so the table now comes from `admin/content/vaults.json` through a `VAULTS` comment marker, the same mechanism the homepage articles band uses.

**The published date is not a date anybody typed.** It is the commit on which each vault's page first appeared in git, recovered with `git log --diff-filter=A`. Two weaker sources were tried and rejected first: update posts missed ten vaults and false-matched `health-score` against a later release that merely mentioned it in passing, and the version log had no line for two of them at all.

**Sorting is progressive enhancement.** The rows ship newest-first in the HTML, so with JavaScript off the table is still correct and still in the most useful order; the headings are keyboard-operable. On a narrow viewport the *what it is* column drops out rather than wrapping to nothing, since that sentence is on the vault's page anyway.

Verified at 1280 and 390 wide: 25 rows, **zero** 64-hex strings on the page, zero open-live links, no horizontal overflow, and the sorting checked by asserting the order actually flips rather than by looking at it.

### [The brief came back as a vault, and it is the first one here that phones home](#the-brief-came-back-as-a-vault) [v0.2.56](../admin/versions.md)

vaultstelemetryagentsauditbriefs

v0.2.55 published a [build brief](../docs/briefs/vault-telemetry-append-lanes.md) on getting telemetry out of a vault whose read key is public. Another agent read it and shipped the thing, so [two games about agent permissions](../demos/vaults/agent-permission-games/index.md) now joins the published vaults, two deterministic games about grants, permissions and mandates, sending anonymous usage events over an append lane to a separate private vault.

It is the first vault published here that **sends anything anywhere**, and the first end-to-end test of whether a brief written for an agent produces what it describes.

- **It took the fallback path**, which is the part the brief was least sure about. Not `sg.append` through the bridge, a direct `fetch` to the account-less write endpoint, `credentials: 'omit'`, `keepalive` on the final flush, payload in the `sgit pki` v2 envelope. `app.json` declares no `permissions` key at all, which is consistent: it does not need the host for this.
- **Exactly one 64-hex string exists in the whole vault**: the append token, in five places. No private keys, no enum/write/vault/read key fields, no third-party secrets, no personal data. One credential, and it is the write-only one.
- **The disclosure page is the model.** `telemetry.html` opens by naming the default it breaks, *"Opening a vault does not normally send anything anywhere. This one does"*, publishes the event schema, and then writes the sentence most analytics pages never do: *"What it proves. Nothing about anyone. Anyone holding this vault's read key holds that token and could forge or flood the lane."*

**A method correction that cost nothing only because the control was run.** The first version of the token test called a leak on the strength of `sgit clone` creating a directory. Then an all-zeros key produced the identical result. The directory is created regardless, and the test discriminated nothing. The marker that actually works is `.sg_vault/local/clone_mode.json`. A credential test with no negative control is not a test, and that now belongs in [the publishing method](../demos/vaults/publishing.md).

**Two findings, published rather than filed.** Two of the four pages still tell the player *"nothing sent"*, `what-can-it-do` was corrected to *"nothing stored"*, the home page and `which-agent-is-it` were missed, and the latter contradicts itself on a single screen. Nothing leaks; but the subject of this vault is informed consent, which raises the stakes on leftover copy. And the write endpoint could not be confirmed from this container, 404 on both hosts under both names, so that is recorded as unresolved rather than dressed up as a conclusion.

### [Briefs gets a second kind, references written to be executed, not asks waiting on a reply](#briefs-gets-a-second-kind) [v0.2.55](../admin/versions.md)

briefsagentsdocsmulti-agent

[Briefs](../docs/briefs/index.md) has been a single scroll of cross-team asks since v0.1.13, each addressed to another team, each carrying a status, each closing when it is answered. A brief arrived this week that is a different species, so the page now says so and separates them.

- **Build briefs**: a durable reference an agent executes: the mechanism, the traps, what to verify first, and the prompt to paste. It never closes.
- **Cross-team asks**: the seven that were already there, untouched, addressed to the sgit CLI, SG/Send API and SG/Vault UI teams.

The first build brief is [**telemetry from a published vault**](../docs/briefs/vault-telemetry-append-lanes.md): how one vault sends messages to another, and how a vault whose read key is public reports anonymous usage back to its author. The mechanism is an **append lane**, and it works for one reason worth stating plainly, the sender's `append_token` grants **write only**. A visitor who extracts it from the published vault (and they can, because a read key decrypts everything) cannot list the lane, cannot fetch anything, and cannot read another reader's events. The write response is blind by design: exactly `{"ok": true}`.

It is the only credential shape that survives being published inside a public vault. What it does not buy is authenticity: events can be forged, and the real failure mode is **1000 pending files per token → 507**, not a confidentiality breach.

The new group starts with two entries rather than one, because [publishing a vault](../demos/vaults/publishing.md) was already a build brief, *"written to be followed by another site's agent"*, filed in the vaults section where nobody looking for a method would find it. That is the same misfiling that created `case-studies/` in v0.1.14.

**Briefs also moves in the nav**, out of Evidence and into Docs beside Skills. The section's centre of gravity is now agent-facing documentation rather than a record of conversations, and Docs is where an agent looks. Evidence keeps comparisons, case studies and use cases.

One editorial call, recorded because it went the other way from the obvious. The source brief opened by answering *"is there a doctor/patient case study for this?"*. There is not; the [health-score vault](../demos/vaults/health-score/index.md) is one vault with three audiences, not two vaults exchanging messages. In the repo copy that section earned its place because the question was asked. On a published page nobody asked it, and listing that vault among the pages to read implies it is a source for cross-vault messaging. So it is cut from the reading list and kept as a single line of signposting, because that vault is exactly where the next reader will go looking, and a named absence beats a hidden one.

## 2026-09-05

### [Provenance is not conformance, the AIUC-1 vault, forked and layered](#provenance-is-not-conformance) [v0.2.54](../admin/versions.md)

vaultsstandardsconformancegraphspermissions

[Provenance is not conformance](../demos/vaults/aiuc-1-conformance/index.md) joins the published vaults. It is a **fork** of the [AIUC-1 catalogue vault](../demos/vaults/aiuc-1-graph/index.md) that keeps every byte of it and adds one directory above it, 649 files against the catalogue's 135. Both vaults stay published, and the catalogue page now says what it is and links to the fork.

The distinction the whole thing rests on is two edges that are never allowed to touch:

| edge | answers | absent means |
|---|---|---|
| `evidenced_by` | does the standard say this? | a build defect |
| `attested_by` | does **this subject** do this? | the control is unevidenced, **which is the finding** |

- **Unevidenced is a state, and it is the default.** Every control in scope gets a row whether or not anybody has looked at it, so an absent row is never read as compliance. The first build across all 53 controls comes out 2 evidenced, 48 unevidenced, 3 contradicted, the designed answer, not an unfinished one.
- **Insurability is computed, not asserted.** Conformance states become conditions and exclusions on a `policy/v1`: 1 condition met, 52 exclusions, 0 of 5 consequences covered. Move the `as_of` date to 2027-01-15 with nothing edited by anybody and the condition has expired, leaving 53 exclusions.
- **A crosswalk becomes a join between two vaults.** 62 of AIUC-1's 1,126 crosswalks resolve into article nodes in the published [regulation graph](../demos/vaults/regulation-graph/index.md), with CELEX and a hash on each edge; the other 1,064 are reported unresolved rather than forced. The join then finds something neither vault knew alone: **8 of the 27 target articles are amended by Regulation (EU) 2026/1744**, so the crosswalk was published against the text before amendment.
- **The first vault here to ask for a write grant**: `fs.write` scoped to `["chat/"]` and nothing else, plus `sg.llm.*`. The chat is stored in the vault; the authored terms the query depends on cannot be written by the app at all.

The claim that makes a fork readable is that it did not edit what it copied, and that claim is checkable rather than decorative. Run from the clone before publishing: the catalogue's own tests report **21/21 passed**, including the one that rebuilds every source document to the word, and the added layer's report **19 tests, 0 failed**.

It remains unofficial and derivative, not approved, certified, endorsed or reviewed by AIUC, and not a substitute for the standard. The subjects it measures are invented for the demonstration. The catalogue's open question about reuse rights applies here too, doubled, and is stated on the page rather than tidied away.

## 2026-08-27

### [The directory answers questions now, and the default tier needs no key](#the-directory-answers-questions-now) [v0.2.47](../admin/versions.md)

chatllmnetworkvaults

Two things: [the network directory](../network/index.md) grew a chat box, and a second conference vault went up.

**Ask it which of the nineteen sites is yours.** Type *"I have to sign off a risk"* and it points at risks.sgit.ai, and shows you the words it matched on. It runs in your browser against the catalogue generated from the same files the cards and the table come from, so it cannot drift from the directory underneath it.

- **No key, no account, no network call** in the default tier. A reader should not have to hold a credential to use an index.
- **It tells you why it chose.** A hit in a site's thesis or domain outweighs one in its summary, and the answer names the matched terms. An LLM answer does not give you that for free.
- **Bring your own key if you want prose.** Opt-in, OpenRouter, streaming, reusing the pattern already proven in the workbench vault. The cost is stated on the panel rather than buried: with no host there is no permission floor, so the key lives in the page's origin. If the call fails it falls back to the local matcher and says so.
- **[The plan](../articles/chat-on-a-static-site.md)** covers the third tier, serving the directory as a vault app, where `sg.llm.chat` keeps the key below the permission floor and the app never sees it. Not built; scoped honestly, including the parts that are not started.

One fix worth recording. The matcher first sent *"I need to cite a regulation precisely"* to **wardley-maps**, because it only knew each site's own vocabulary, standards.sgit.ai says *provision*, and the reader typed *regulation*. Site entries now carry an `aliases` field holding the words readers actually arrive with. Five real questions, five correct first hits; nonsense still returns nothing rather than a confident wrong answer.

Also live: **[Scaling Threat Modeling with Semantic Knowledge Graphs](../demos/vaults/threatmodcon-2025/index.md)**: ThreatModCon 2025, Barcelona. Eleven linked threat models from customer to compute instance, so a vulnerability in a line of code traces up to the revenue it risks. 51 nodes, 179 threats, five interactive views and five Wardley walkthroughs, all running offline in the vault. Two of its data files are **invalid JSON upstream** and are repaired here, with the repair proved rather than asserted: the only differences are four stray brackets removed and one `],` added, and the multiset of content lines is unchanged.

### [An insurance policy for an agent, and the delta is the risk](#the-delta-is-the-risk) [v0.2.52](../admin/versions.md)

vaultsagentspermissionsrisk

[Licence to Operate](../demos/vaults/licence-to-operate/index.md) joins the published vaults, one agent, its policy, and a simulated conversation where every reply carries its price.

**The idea worth stealing is the delta.** Three sets:

- **CAN DO**: the grant. 12 capabilities.
- **MAY DO**: the mandate. 4, and the only thing the policy insures: `crm:read`, `kb:search`, `llm:generate`, `mail:draft`.
- **THE DELTA**: 8 capabilities inside the agent's reach and outside its authority, including `crm:write`, `crm:export`, `mail:send` and `shell:exec`. **No policy covers these.**

The mandate is *"answer a customer's question from their own record and the help centre, and draft, never send, a reply."* The grant includes `shell:exec`. Nobody asked for it, nothing insures it, and the agent can reach it. That is [nhi.sgit.ai](../network/nhi.md)'s blast-radius argument made countable, and here the gap is priced rather than described.

The simulation makes you spend it: a customer cannot log in, and each of three replies shows its cost before you commit, 1,400 tokens in band, 4,800 tokens and three records which *claims*, or a password reset that is `mail:send` and outside the mandate entirely. Underneath is a live rate table with a normal band, an ask-above threshold, a pool with an untouchable reserve, and customer records marked *uninsurable above 20*.

**The permission grant proves the architecture rather than asserting it.** The vault holds the terms; your browser holds the run. And `app.json` requests `fs.read` and `downloads`, **read, no write, at any path**. An app that simulates spending against a policy is structurally incapable of editing the policy it spends against; not because it behaves, but because it never asked for the grant that would let it.

One process note. The agent that built this vault supplied its own audit of all 16 commits, and it was accurate, but it was checked rather than accepted. Re-verified against a fresh read-key clone: no credentials anywhere, the `/home/claude/` build paths baked into the PDF are gone (zero occurrences), and the one full-length credential in the vault is the vault's **own** read key, confirmed by deriving it independently and matching byte for byte, rather than by trusting the label on it.

### [A standard as a graph, and the one line that makes it trustworthy](#a-standard-as-a-graph-and-the-line-that-makes-it-trustworthy) [v0.2.49](../admin/versions.md)

vaultsgraphsprovenancestandards

[AIUC-1, as a graph you can cite](../demos/vaults/aiuc-1-graph/index.md) joins the published vaults, an **unofficial, derivative** machine-readable catalog of the public AIUC-1 agent standard. It is not approved, certified or endorsed by AIUC, and the page carries that in a box above everything else rather than in a footnote.

- **53 controls, 144 requirements, 1,126 crosswalks** to 13 external frameworks, resolving to 1,238 nodes and 3,526 edges across five releases.
- **Every field names its source.** Each control carries the official page it was read from; each of the 82 captured pages carries its HTTP status, retrieval timestamp, the **SHA-256 of the bytes**, and the retained gzipped snapshot inside the vault.
- **A control is drawn as its edges** (`has_requirement`, `maps_to`, `evidenced_by`, `applies_to_capability`) which is [graphs.sgit.ai](../network/graphs.md)'s argument applied to a compliance standard.
- **A release that could not be built is recorded as unbuilt.** AIUC names a 2025-07-22 release that carries no commit, so the catalog says so rather than dropping it.

The best thing in it is a refusal. It publishes the five places where the official website and the official changelog repository disagree, classifies each as presentation rather than meaning, and then declines to pick:

**"None of these is resolved here. Resolving one means choosing a source, and that is not this build's to choose."**

A derived artefact that silently picks a winner when its sources conflict has stopped being derived and become an opinion, and the reader cannot tell which. This one preserves both readings and stops a release being marked `validated` if a difference changes meaning.

Its collection policy is worth copying too: an identifying user agent, one request per second, no authentication, no slug guessing, every page reached from a page already fetched, and `robots.txt` fetched first, returning 404 at capture time, **with the manifest recording that observation verbatim rather than the conclusion alone**.

One thing stated plainly rather than buried: the vault's own `NOTICE.md` records that **reuse rights for the full AIUC-1 control text have not been confirmed with AIUC**, and that anyone republishing publicly should confirm first. Publishing this read key is that kind of republication, and it is here at the author's decision with the vault's disclaimers reproduced rather than summarised. The vault's undertaking, *"If you are AIUC and want something here changed or removed… removal will be honoured"*, is repeated on the page and applies to it too.

### [A three-minute pitch, delivered from a vault, and the first grant that is not empty](#a-pitch-delivered-from-a-vault) [v0.2.51](../admin/versions.md)

vaultspermissionspresentation

[The VoiceDebrief pitch to Founder Institute](../demos/vaults/voicedebrief-pitch/index.md) joins the published vaults, the 23rd, and not a deck *about* a vault but a deck **presented from** one.

- **A presenter, not a PDF.** Twelve slides with per-slide target timings, a live 3:00 countdown, speaker notes, Focus and Fullscreen, plus five backup slides for Q&A, one of them titled *"WhatsApp / ChatGPT already does this"*, which is the obvious objection answered rather than avoided.
- **The working ships with the conclusion.** The approved outline and its claims-to-keep-exact list, the spoken script per slide, the fifteen-part pitch pack, the research notes, the screenshots, and the PDF and PPTX exports, all in the same object as the slides. The deck is generated from a template by a script inside the vault, so the slides are built, not hand-maintained.

**It is also the first vault here that asks for anything.** Every other one declares `"permissions": {}`. This one declares:

```

"permissions": { "downloads": true, "externalLinks": true }

```

It offers PDF and PPTX buttons, so it asks for downloads. It links to the live product, so it asks for external links. That is the whole request, **no filesystem access at all**, not read, not write, at any path. The grant is one line, it maps onto two things you can point at in the interface, and nothing outside it is reachable however the app is written. Set beside the [Risk Graph Explorer](../demos/vaults/risk-graph-explorer/index.md)'s empty grant, the difference is legible without reading any code.

Audited clean on credentials. Three things become public with it, all apparently by design and all named on the page rather than left to be discovered: the unit economics and commercial terms, the author's contact address on the closing slide, and the three named judges of the session with their affiliations, names and roles only, with no tactical notes about them anywhere in the vault.

## 2026-08-26

### [Nineteen sibling sites, and a way to find the one that is yours](#nineteen-sites-and-a-way-to-find-yours) [v0.2.44](../admin/versions.md)

networknavigationrefactor

[The network](../network/index.md) was four sites. It is **nineteen**: seventeen live, two with the repository and subdomain in place but nothing published yet. That is no longer a footnote on this site; it is where most of the writing now lives.

- **The page now starts with a question, not a list.** Seventeen lines, each one something somebody actually arrives with, *"I need to give an AI agent an identity"*, *"I have to sign off a risk and I do not want to rubber-stamp it"*, *"my app has to call an LLM and I do not want it holding an API key"*, and the site that takes it seriously. At four siblings a list was fine. At nineteen, a list is a directory you have to read before it helps you.
- **Grouped by area** (Agents &amp; AI, Risk &amp; governance, Graphs &amp; method, Security &amp; infrastructure, Business &amp; publishing) with a full scannable table underneath for anyone who would rather see all nineteen at once.
- **Every thesis is the site's own words**, quoted from its H1 or lede rather than summarised here, so an entry cannot drift into describing a site that no longer says that.
- **Network moved to the top-level navigation.** It had been the third child of Updates, which was a reasonable filing decision at four entries and a bad one at nineteen.
- **And the homepage says it out loud**, with five doors in by area, because a reader who does not yet know these sites cannot pick one from a list of domains.

Two sites appear with no screenshot and no link to a live page: `skills.sgit.ai` and `influences.sgit.ai` have DNS and a repository but GitHub Pages has not published them. They are listed as *not published yet*, pointing at their repositories, rather than quietly left out, the same reason a missing tag is preferable to a missing page.

This is the refactor it looks like from the outside. Material that would have made this site sprawl has a better home; this page is the index back into it. Adding the twentieth site is writing one markdown file.

### [Articles get a place on the homepage, and a band gets its width back](#articles-get-a-home-and-a-band-gets-its-width-back) [v0.2.45](../admin/versions.md)

articleshomepagelayout

Three changes, one of them a bug I shipped yesterday.

- **The network band ran the full viewport width.** The homepage bands each carry their own measure (`.eco` has `max-width:1100px` on the component itself, not on a wrapper) and the band added in v0.2.44 simply had none, so it stretched edge to edge on a wide screen while everything above it stayed in the column. Measured after the fix: `.eco`, `.netpick` and the new `.artcards` all report exactly **1100px**, with no horizontal overflow. The five area cards also now lay out 3+2 rather than 4+1, which stops the last card sitting alone.
- **[A new article](../articles/nineteen-sites.md)** on what the split actually was: twenty repositories in fifteen days, fifteen of them in the last five, and what that did to the writing, what forced it, what it cost (discovery got worse before it got better), and why the directory now opens with a question rather than an inventory.
- **Articles now have a place on the homepage.** They turned out to be the readable surface over all of this, a reader who will not work through a docs tree will read one argued page. The band is **derived from the articles list**, so a new article appears there by being written. No list to maintain, same rule as everywhere else here.

Also: [influences.sgit.ai](../network/index.md#business-publishing) went live and is now a full entry with its screenshot, *"where the thinking came from"*, an influence map in three tiers with a changelog recording when a source moves between them. That leaves **eighteen of nineteen live**; `skills.sgit.ai` still has DNS and a repository and nothing published, and is still listed as such rather than hidden.

### [A conference keynote as a vault, the deck, its exports, and the research it came from](#a-conference-keynote-as-a-vault) [v0.2.46](../admin/versions.md)

vaultspresentationprovenance

[AI vs. AI, Black Hat Europe 2025](../demos/vaults/blackhat-eu-2025/index.md) joins the published vaults. It is the twentieth, and the first that is a **talk** rather than a document set or an app.

- **The whole chain, one credential.** The deck as presented (26 slides), six PDF exports from v0.1.1 to v0.2.0, the eight research papers it was built from, and the slide system's own source at ten versions, all in one vault, opened with one read key.
- **The slide content is data, not markup.** `deck/blackhat-eu-2025.json` is read through the vault bridge at load time, so changing a slide is a commit rather than a rebuild. That separation is why the vault can carry ten versions of the renderer beside one deck without either owning the other.
- **It asks for nothing.** `"permissions": {}` with `present: true`, the deck opens full-screen and never touches the filesystem.

The argument is worth the click on its own. It opens by conceding the ground (*security's four pillars, all broken*) then lands on four publicly documented outages that were **not** attacks: a timing bug that wiped a global database, a config inconsistency that detonated worldwide, a routine change that halted traffic, and a faulty update that bricked 8.5 million machines. The turn is one line: *"These weren't sophisticated attacks. They were minor glitches that cascaded. Now imagine if they were deliberate."*

Several of its later slides describe things this site now demonstrates rather than proposes, *assume compromise, contain blast radius*, *version control everything*, *identity graphs for least privilege*. Those threads have their own homes in [the network](../network/index.md) now.

Audited clean before publishing: no sgit credentials, no third-party API keys, no private keys, no emails, no client named. The organisations that appear (AWS, Azure, Cloudflare, CrowdStrike) are cited for public incidents, which is what the slide is about. The deck uses Black Hat Europe's official speaker template because it is a talk that was given there; the page says plainly that it is published as the speaker's own material, not as anything endorsed by or affiliated with the conference.

## 2026-08-25

### [Six vaults published, three held back, and the check that nearly missed one](#six-vaults-published-three-held-back) [v0.2.43](../admin/versions.md)

vaultsauditsecurity

Nine vaults were submitted for publication. **Six are now live**, [in the gallery](../demos/vaults/index.md). Three were held, and the third one is the reason this post exists.

- **[Penetration Test Report](../demos/vaults/pentest-report/index.md)**: a pentest delivered as a vault instead of a PDF. Eight audience-specific views over one engagement, and every finding ships a retest script that exits `0` if it is fixed and `1` if it is not. Entirely fictional, with a `SIMULATED DEMO` badge on its own front page.
- **[Standards Atlas, GDPR](../demos/vaults/standards-atlas-gdpr/index.md)**, *"the standard is the graph."* Rulings, regulator guidance and per-country variation as first-class nodes over the articles they bend, with corrections written back into `feedback/` and nowhere else.
- **[RiskMandate · File security](../demos/vaults/riskmandate-file-security/index.md)**: risk acceptance moved from a rubber stamp at the end to the centre of the flow, over versioned JSON queried live by SQLite in the browser.
- **[Content-Transformation Proxy](../demos/vaults/content-transformation-proxy/index.md)**, **[SG Commercialisation](../demos/vaults/commercialisation/index.md)** and the **[SG/Payments Brief Pack](../demos/vaults/payments-brief-pack/index.md)** complete the six.

**Two were held for carrying credentials.** One contained two live vault keys in plaintext, including **its own write key**, which would have turned a published read key into full write access. The other is a private working log that was never meant to be public.

**The third is the one worth recording.** A vault whose app reads an LLM key from a file scored *clean* on the first credential pass, and then a screenshot of it showed a chip reading `key: vault key.json`. The file held a live OpenRouter API key. The scan had looked for vault-key shapes, `sgit_` prefixes, private-key blocks and the string `api_key`; the field was named `openrouter_key`, so nothing matched.

That is a real gap, not a near miss reframed as a win. The credential tooling here was built to protect *sgit* credentials and does that well; it had no opinion about third-party API keys, which are just as costly to leak and far more common. A broader sweep (OpenAI, Anthropic, GitHub, AWS, Google, Slack and JWT shapes, with placeholders filtered out) now runs over every candidate, and it found exactly one other hit: a forged `alg:none` token in the pentest vault, which *is* the finding it documents.

The lesson is the cheap one to state and the easy one to skip: **a scan that has never surprised you is not evidence that you are clean.** It was a screenshot, not the scanner, that caught this.

## 2026-08-22

### [The ninth published vault, four apps in one tree, and a reader that asked for nothing it did not need](#the-ninth-vault-four-apps-in-one-tree) [v0.2.40](../admin/versions.md)

vaultsgraphspermissions

[VoiceDebrief](../demos/vaults/voice-debrief/index.md) joins [the published vaults](../demos/vaults/index.md). Four apps in one encrypted vault, lifting meaning out of text, from fictional voice notes to Article 9(2) of the EU AI Act, into typed semantic graphs.

*Written up from the vault and the release that published it; the page itself is the primary record.*

- **The claim in one line.** A paragraph is not a string, it is a **graph**, and so is the paragraph next to it. Lift both into typed nodes and the two join *node-to-node* through an intermediate layer, never paragraph-to-paragraph. Part 4 works that end to end against one real legal provision. Parts 1–3 run on a **fictional** corpus, and the vault says so in its own README.
- **Read over one folder, write over nothing.** `app.json` declares `fs.read` on `part-4/` and nothing else, no write, no mkdir, at any path. The host's own chrome renders the result as `R3 W0`. A capability never requested cannot be misused.
- **Lineage kept rather than overwritten.** `part-2/` and `part-3/` hold frozen app snapshots at the state they shipped in, with a shared nav linking all three, so the earlier thinking stays openable instead of surviving only as a commit message.
- **A nested entry point**, `part-4/index.html`, which is what lets one vault hold four apps without one of them having to own the root.
- **The credential is derived.** It arrived as a vault key, was classified as a write credential before it touched anything, and only the one-way read key is published.

Ten screenshots, captured by driving the live vault from that published read key, no mock-ups.

It was written and pushed a day before it appeared here: [the tag gate](../updates/#an-ordinary-commit-should-not-be-able-to-take-the-site-down) had the deploy blocked.

### [An ordinary commit should not be able to take the site down](#an-ordinary-commit-should-not-be-able-to-take-the-site-down) [v0.2.40](../admin/versions.md)

cideployrelease

Two good commits landed on `dev` after v0.2.39 and sgit.ai served neither for a day. Nothing was wrong with either of them. The CI tag gate failed, and the deploy is gated on the tag gate.

- **What the error said, and what was actually true.** The job read `SITE_VERSION`, found `v0.2.39` already tagged on the *earlier* commit, and failed with *"SITE_VERSION was not bumped for this release."* But this was not a release. It was an ordinary commit on top of one. The message described a discipline failure where the real event was a category mistake in the check.
- **Why it became an outage rather than a warning.** The deploy job runs when `tag-release` is `success` **or** `skipped`. A *failure* is neither. So a missing tag, bookkeeping, silently became an unpublished site. Re-running could not help: the check is deterministic, and it failed identically on the second attempt.
- **The fix is to ask the right question.** What makes a push a release is now its **commit subject**, which is where `release.sh` already writes the version. No `site vR.M.N:` subject means an ordinary push: tagged nothing, published anyway.
- **And a commit that does claim a version is held to more than before.** The subject and `SITE_VERSION` must agree, previously that was only ever inferred, from whether the backfill loop had happened to produce the tag. The version must not already have shipped, and it must still be the next minor.

The asymmetry is the point, and it is written into the workflow so the next person changing it knows why: **a missing tag is a bookkeeping gap, a blocked deploy is an outage.**

Checked before shipping rather than after, by extracting the job's own script and running it over five cases in a throwaway clone: the exact commit that failed today now exits 0, a proper release tags, and subject/`SITE_VERSION` disagreement, a reused version and a skipped minor all still fail, each with a message that names what is actually wrong.

There was a quieter second consequence, and it is the one worth remembering. Those commits went to git only, so the vault remote never received them: `sgit status` showed all fifteen new files as uncommitted. Both stores are meant to move together, which is exactly [why CI does not author commits itself](../case-studies/one-tree-two-remotes.md), a CI-written commit would exist on the git side alone. This release carries them across.

## 2026-08-21

### [A fourth sibling site, and the first one that links back](#the-first-sibling-that-links-back) [v0.2.39](../admin/versions.md)

networkgraphsmethod

[graphs.sgit.ai](../network/graphs.md) joins [the network](../network/index.md). It argues for a grammar of semantic graphs, from five rules you can apply tomorrow up to a full positioning against schemas and vector search, and it opens by disowning the product category a reader arrives expecting: *"this is not a graph database pitch… there is no graph database anywhere in the work behind this site."*

- **The thesis fits in two sentences.** Two nodes both hold `8080`. One is connected to a type, to a library, to a version; the other to nothing. *"The difference is not in the value. The difference is in the connectivity."*
- **The best argument needs no background.** 10,000 hours came from a 1993 violinist study where it was an *average*, not a threshold, and half the top group had not reached it. The corrections never attached: by then the claim had been carried through 242 papers and 200,000+ citation paths. A document cannot fix that. A graph can mark a claim superseded and make *"what did we build on this?"* a query.
- **`relates-to` is banned**, for a mechanical reason rather than a stylistic one: an edge with no verb carries no constraint, so it cannot narrow a traversal. It costs fan-out and buys nothing.
- **It separates ships from argues, and concedes the harder half**, *"this site's subject matter is almost entirely design"*, then lists what is running: the vault commit DAG, `*.link.json` cross-vault edges, the read-only query API handed to untrusted sandboxed apps, and a live typed property graph of 71 nodes and 141 edges across 107 issue files.

**It is the first sibling with a reciprocal link.** Its nav carries an `↗ part of sgit.ai` chip and its footer points back at this network page. Until now `/network/` was a one-way index.

Two build changes came with it. A site entry can now carry a `url:` that differs from its `domain:`, `graphs.sgit.ai` does not resolve yet, and an entry should link to the address that works rather than wait for the CNAME, so the page says which one it is instead of shipping a dead link. And the audit that comes with every network entry found one: the graphs site links to `sentinel.sgit.ai`, which does not exist. The site is `sg-sentinel.sgit.ai`; the `sg-` prefix is load-bearing.

## 2026-08-20

### [The audit that stopped a publication, and the vault we built instead](#the-audit-that-stopped-a-publication) [v0.2.37](../admin/versions.md)

vaultssecuritypublishing

A vault arrived for publication: the **EU AI Act as a citable graph**: 113 articles, 1,523 nodes, 1,944 edges, every node traced to hash-verified source bytes. Good demo, obvious yes.

It did not ship. The audit step, *open every file with the exact credential you are about to publish*, found a **live vault key in plaintext**, inside a handoff document, granting write access to a **different** vault. Publishing the read key would have handed that away to anyone who read the page.

- **Deleting the file would not have been enough.** Vault objects are content-addressed and immutable, so a credential committed once may stay reachable from history. The only clean remedy is history that never contained it.
- **So there is a new vault.** Same 206 files, two credentials redacted in place with visible `<VAULT-KEY-REMOVED>` markers rather than silent deletions, plus a `PUBLIC.md` stating what changed and why.
- **Re-audited from a fresh read-key clone**: 205 text files, zero findings. That is [Regulation Graph](../demos/vaults/regulation-graph/index.md), and it is live.

One rule got verified rather than assumed. The vault's Graph REPL is an LLM chat, and its code looks for an OpenRouter key at `/key.json` *inside the vault* before falling back to device storage, so a shipped key would be an open tab on somebody else's budget. There is no `key.json`, confirmed in the read-key clone. Bring your own key; nothing metered ships.

The rule that caught all of this came from the [Risk Graph Explorer](../demos/vaults/risk-graph-explorer/index.md) vault's own `PUBLIC.md`, not from us. It has now paid for itself.

### [A third sibling site, one that says, at the top of every page, that it does not exist](#a-third-sibling-site-that-says-it-does-not-exist) [v0.2.38](../admin/versions.md)

networkedgesecurity

[sg-sentinel.sgit.ai](../network/sg-sentinel.md) joins [the network](../network/index.md). It is a design for an app-coupled edge guard that replaces rented AWS WAF plus CloudWatch and Firehose with a layer you own, and its status pill reads `NOT BUILT` where its siblings read `MVP DRAFT`.

- **The inversion is the idea.** A generic WAF is blind to the app it protects, so it denylists known-bad and passes the rest. If you control both client and server, the edge knows the valid request space, so it can **allowlist**, and no invalid request reaches the origin.
- **One correction reshaped the design**, and it is stated as a governing constraint: *"Layer 1 never acts and never writes, it only decides and signals. Layer 2 is the sole actor and the sole I/O owner."* The reason is physical: a CloudFront Function has no network and no filesystem. The site names the earlier version, where L1 blocked inline, as a category error of its own making.
- **Rules are the engine, not configuration on it.** Six deterministic rules, each a pure function, each mapped to an ATT&CK technique, run in order with first-block-wins. The prototype ran the same engine across three targets with a parity matrix asserting identical decisions.
- **And it bounds its own evidence.** The prototype's testing manual reports 149 passing tests; the site immediately says *"not deployed anywhere, not in production use, not maintained, and not packaged for you to install."*

It is the third site here to publish a design **before** the thing exists, after [pki.sgit.ai](../network/pki.md)'s four registry rules. Same wager: publishing the design now is cheap, claiming it afterwards is impossible.

Adding it took one markdown file and three screenshots. The renderer gained pipe-table support on the way, since the six-rule core wanted a table and got a paragraph of vertical bars instead.

## 2026-08-19

### [The first two sibling sites, with screenshots](#the-first-two-sibling-sites) [v0.2.36](../admin/versions.md)

networkidentitypki

Two focused sites now run on `*.sgit.ai` subdomains, and [a network section](../network/index.md) covers both, what each argues, why it is relevant here, and screenshots of the real pages.

- **[nhi.sgit.ai](../network/nhi.md)** splits "how do I give my agents an identity?" into **agents you run** and **agents you rent**, and shows that everything on the market answers only the first. For rented agents (the ones in Claude, Codex, behind an API) the honest current answer is to hand over a broad credential and hope. Its sharpest idea is that **the real authorization is the closure**: inbox access is every account resettable by email.
- **[pki.sgit.ai](../network/pki.md)** designs a key registry from the 2019 keyserver catastrophe, publishing four rules **before the registry exists** so they stay checkable. The resolution it reaches is worth borrowing: append-only is safe when a writer appends only to objects it *owns*, and fatal when anyone may append to somebody else's. The rule to carry forward is not "append-only". It is *the writer owns what it writes*.

Both connect directly to work here. Read keys and [append lanes](../api/append-lanes.md) are credentials with a provably bounded closure, which is the nhi problem stated as a mechanism; and an append lane is owner-configured, which is pki's rule 1 already shipped in another corner of the system.

More subdomains are coming. Adding one to this site is now writing a single markdown file and capturing its screenshots, the index, the cards and the page are all derived.

## 2026-08-18

### [Verify the fix pack, not just the bug](#verify-the-fix-pack-not-just-the-bug) [v0.2.34](../admin/versions.md)

processpkiaccuracy

The documentation gap above arrived as a well-built fix pack from the SG/API team: a gap analysis, code-verified source material, and a draft of the missing page. The most valuable line in it was its own instruction to check the claims before publishing. **Three did not survive.**

- **"The security page actively denies PKI."** It did not. A sweep for *symmetric*, *asymmetric*, *public key*, *PKI* and *keypair* returned zero occurrences. The page was silent, not wrong, and publishing a correction for a claim we never made would have put a false statement in our own changelog.
- **"Search the site for stale `inbox` naming."** There is none. Two hits, both ordinary English; no `/api/vault/inbox/*` path anywhere.
- **"Seal to the recipient's X25519 key."** Not what ships. Running `sgit pki keygen` prints **RSA-OAEP 4096-bit** and **ECDSA P-256**. Publishing the draft as written would have told integrators to build against the wrong primitive.

Two more corrections came from running the CLI rather than reading about it: `sgit pki export` emits a **JSON bundle** of two PEM blocks, not the `.pem` file the draft redirected into, so the draft's `sha256sum public-key.pem` derivation of a lane address is not well defined, and `keygen` requires a passphrase, which no draft step mentioned.

The whole exchange, including what we got wrong, is on [the briefs page](../docs/briefs/index.md).

### [The API reference we did not have](#the-api-reference-we-did-not-have) [v0.2.34](../admin/versions.md)

apimessagingdocs

An agent was asked how to send an encrypted message between two vaults. It read this site and could not find out. The capability had shipped months earlier.

The diagnosis was uncomfortable and simple: **we documented both halves and never wrote the sentence that joins them.** The transport was on one page as `sg.append`, the crypto on another as `sgit pki`, and neither referenced the other. There was also no HTTP API reference anywhere, awkward for a project whose whole argument is that the API *is* the surface.

- **[Sending messages between vaults](../docs/vault-messaging.md)** is the page that was missing: append lanes composed with keypairs, worked end to end in CLI, curl and `sg.append`.
- **[An /api/ section](../api/index.md)** now exists, [authentication](../api/authentication.md), [vault objects](../api/vault-objects.md), [append lanes](../api/append-lanes.md) and [errors](../api/errors.md).
- **[The PKI page](../docs/pki.md)** documents the keypair lifecycle, run against the shipped CLI rather than recalled.
- **[The security page](../security/index.md#pki)** gained the asymmetric layer it never mentioned. It never claimed sgit had no public-key layer, it simply said nothing, and on a page like that one, silence reads as denial.

The one step that is not wired end to end is labelled **PROPOSED** with an interim recipe, rather than quietly documented as working.

## 2026-08-17

### [Three walkthroughs, read back as documents](#three-walkthroughs-read-back-as-documents) [v0.2.32](../admin/versions.md)

vaultsvideorisk-graph-explorer

A video is invisible to a search engine, to `llms-full.txt`, and to any agent reading this site as documentation. It is also full of *"this guy here"* and *"look at this"*, pointing that a transcript cannot resolve.

So [the Risk Graph Explorer walkthroughs](../demos/vaults/risk-graph-explorer/videos/index.md) now carry the player at the top and **the same session read back underneath**: fifteen moments, each a timestamp that deep-links into the video, the frame the screen was showing then, and what is actually happening in it.

- Nine frames come from a narrated-review export; the other six were captured from the **live vault** with its published read key, driven to the exact state being described.
- What the frames turned up is most of the value, because none of it is audible: negative answers draw **named edges** (`never-exercised-on`, `absent-for`) rather than silence; "no egress" draws a single assurance-coloured edge in a field of amber; and every risk ships with a **"ceases when any of these hold"** list, its own falsification condition, cited to facts.

The [seven views page](../demos/vaults/risk-graph-explorer/views/index.md) covers the same vault view by view.

### [Printing stopped costing every reader](#printing-stopped-costing-every-reader) [v0.2.31](../admin/versions.md)

printperformance

Save a walkthrough page as a PDF and it used to come out wrong in two ways: the site navigation painted **across the middle of page 2**, translucent, with the prose showing through it, and any screenshot you had not scrolled past exported as a blank gap.

The first was a sticky header: Chrome paints a sticky box once, wherever it happens to fall in the paginated flow. The second was subtler. Screenshots load lazily, and `loading="lazy"` defers the **decode**, not just the download, so an image far below the viewport sat there fetched, at zero width, and printed as nothing.

- The first fix made every reader pay: it pre-loaded all the images so printing would work. That was the wrong trade and it was rejected.
- **The bypass now fires only on print**: on `beforeprint`, and on the Cmd/Ctrl-P keystroke, which lands a few hundred milliseconds earlier and buys the images a head start.
- Measured on a page nobody scrolled: **1 image loaded while reading, 9 of 9 in the PDF.**

Also in this release: `@page` margins, colour preservation so the amber/green distinction survives, `break-inside` rules so a caption is never stranded on the page after its picture, and per-release cache-busting on assets, because for ten minutes after every release, returning readers were running new HTML against old CSS.

### [Green does not mean live](#green-does-not-mean-live) [v0.2.33](../admin/versions.md)

cideployprocess

Two consecutive releases pushed cleanly, reported success, and **never reached the site.** A human noticed on a phone, forty minutes later, because the version badge still showed the old number.

The release script verified that both remotes were in sync, and they were. The failure was in a job neither remote knows about: GitHub Pages could not download `actions/configure-pages`, got a **429 Too Many Requests**, and the deploy died in "Set up job" before running a single step. Validation passed. Tagging passed. The site served a two-release-old page.

- **A release now ends by asking the live site what version it is serving**, polling with a cache-buster until the badge matches, and **aborting loudly** if it never does.
- The cost is up to eight minutes per release. The alternative, demonstrated twice in one afternoon, is telling somebody a fix is live when it is not.
- Same principle as the rules already in the build: a page nothing links to, a page the index omits, and a page the deploy never published are all equally unpublished.

There is a longer account of this one in [Green does not mean live](../articles/green-does-not-mean-live.md).


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/updates/index.html)*
