# Performance, cost, and running everywhere, Fractal Semantic Graphs

> Measured answer to “performance of graph engineering versus fractal graph”: no live database, files in object storage, and the LETS cycle (Load, Extract, Transform, Save) with a disposable engine in the reader's tab. A 617-node graph opens in 94 KB and three requests, a question costs 7.8 s and 315 KB from cold against 65.4 s for a full clone, an ontology costs 4 KB, and the standing cost of thirty one published graphs is 295 MB of object storage with nothing running between questions. Plus the cost model line by line, the five places the same read key runs, fractal deployment, and six places it is slower.

*Source: <https://sgit.ai/demos/fractal-graphs/performance.html> · site v0.6.4 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../index.md) / [Fractal Semantic Graphs](index.md) / Performance and cost

# Performance, cost, and running everywhere

A reader of [the Fractal Semantic Graphs page](index.md) asked the right follow-up question: what is the **performance** of this against ordinary graph engineering? The honest answer needs the architecture said out loud first, because the two are not doing the same work. We run with **no live database**. A graph is a set of files in cloud storage, read directly. The engine that answers a question is created when the question is asked and destroyed when it is answered, either in the reader's browser tab or in a serverless function that lives for one request. We call the cycle **LETS**: Load, Extract, Transform, Save. Most of the performance, though, comes from a design habit rather than a mechanism: [**start by asking what data the task at hand actually needs**](#design), and build on three layers that are already fast. Under that, three properties do the rest: **reading an encrypted file takes one request**, because the address is computed locally rather than looked up; **writes go to an append lane outside the commit tree**, so they never contend with reads; and **the cached bytes are ciphertext**, so every cache in the path can hold them without widening exposure. This page gives the measured numbers, taken on 21 September 2026 against live published vaults, then the cost model, then the part that matters most in practice: the same graph runs in a browser, a terminal, a function and a build container, with one read key and nothing installed.

## The short answer

A graph database is very good at one thing this is not trying to do, and pays for it in a way we are not willing to pay. Both columns below are real engineering positions. The question is which bill you want.

|  | Classic graph engineering | Fractal Semantic Graph |
|---|---|---|
| **Where the graph lives** | Inside a database process, in its own storage format | In ordinary files in object storage, content addressed and encrypted |
| **What runs between questions** | A server, its indexes, its replicas, its backups | Nothing at all |
| **Cost of admission** | Everything must be loaded in, and conform to one schema | Publish the files and declare the ontology. Other worlds keep their own |
| **Reading one item** | Connect, authenticate, plan, execute, serialise | **One unauthenticated GET**, because the address was derived locally from the read key rather than looked up |
| **If you need it faster** | A bigger instance | [Take the API out of the path.](#direct) The same clone is 65.4 s through the API and **2.63 s** against plain GETs, because the store is cloud storage and the bytes are ciphertext, so serving them directly is safe |
| **Where a query runs** | On the server, for every reader | In the reader's tab, or in a function that exists for one request |
| **Writes against reads** | Share the engine, so they contend | An [append lane outside the commit tree](#append). A write never touches a branch and never blocks a read |
| **What a query costs the owner** | Instance hours, whether anyone asks or not | The bytes that were actually read |
| **Joining two domains** | A shared schema, so a migration, so a project | An edge, because neither side gives up its own ontology |
| **Six hops over a hundred million edges** | **Its home ground.** Nothing here competes | Not this. See [where it is slower](#limits) |
| **Answering one question over a million** | Fast, once the server is up and loaded | Fast, and the server was never up |

The performance claim is therefore narrow and testable: **for the questions people actually ask of a semantic graph, the work is bounded by the answer, not by the graph**, and the numbers below are what that costs.

## The real optimisation is the question, not the engine

Everything below this line is detail. The architecture is fast mostly because of a design habit, and the habit is this: **start by asking what data the task at hand actually needs.** Not what the system holds, not what the schema allows, not what might be useful later. What this question needs. Once that is the first question, most performance work stops being necessary, because the expensive thing was never the engine. It was loading data nobody was going to look at.

The second half of the habit is refusing to reinvent anything underneath it. **Three layers are already fast, already solved, and already free**, so the job is to compose them rather than replace them.

| **The file system** | A high-performance indexed store with decades of tuning behind it and the operating system's page cache sitting in front. Nothing here writes a storage engine, because one is already installed |
|---|---|
| **A content-addressed hash store on top of it** | An object's name is the hash of its bytes, so a lookup is a path, deduplication is free, and a cache entry cannot be wrong. This is the layer that makes the store safe to spread everywhere |
| **A graph on top of that** | Which tells you *which bytes to ask for*. This is the part that is actually ours, and it is the part that decides how much work a question costs |

It is worth being fair about what a database does here, because the comparison is often unfair in our direction. **A database is fast largely because it keeps the working set in memory.** The buffer pool, the page cache, the in-memory index: most of the speed of a query comes from the answer already being in RAM rather than on disk. That is not cheating, it is good engineering, and it is the same insight. The difference is who chooses the working set. A database guesses it from access patterns and an eviction policy, in advance, for every reader at once. **We choose it per question, at the moment the question is asked, and throw it away afterwards.** It is the same trick, made explicit and made specific.

### Neither the disk nor the decryption is the cost

The habit only makes sense if loading is genuinely cheap, so here is what the layers actually cost. Measured on 21 September 2026 on an ordinary cloud container, on the 1.0 MB file that holds the whole DSIT graph.

| Step | Time for 1.0 MB | Rate |
|---|---|---|
| Fixed per-request overhead, before a single byte of the file | **347 ms** | [a deployment characteristic, not an architecture cost](#fixed) |
| Transfer of the 1.0 MB itself | **300 ms** | 3.5 MB/s on this link |
| Read it from local disk once it is there | **2.5 ms** | 418 MB/s |
| **Decrypt it, AES-256-GCM** | **0.35 ms** | **2,978 MB/s** |
| Parse the JSON | 3.2 ms | the largest local cost, and it is the parser |

Read that table twice. **Decryption is a tenth of the JSON parse, and half a thousandth of the transfer.** On a 59 KB shard it is 0.025 ms, which is not a number anybody needs to plan around. The same holds in a browser, where AES-GCM runs in WebCrypto against the same hardware instructions the measurement above used. Whenever somebody assumes that encrypting the data must have cost something in speed, this is the answer: at these sizes, on ordinary compute, **encryption is free**, the disk is free, and what is left is the request. Which puts the whole question back where it belongs, on how many requests you made and how many bytes you decided to ask for.

**The design rule, stated as a budget.** If you find yourself loading gigabytes to answer a question, something is wrong upstream, and no amount of tuning will fix it. Go back and cut the data, because the fix is always in the shape of the data and never in the engine.

| **Under 100 KB** | An answer. This is the normal case and it feels instant |
|---|---|
| **Around 1 MB** | A whole world at one altitude. Fine, and still under two seconds cold |
| **10 MB and up** | You are loading a store rather than an answer. Cut a slice, or move the question to a lower altitude |
| **Gigabytes** | A design error, not a performance problem. The graph exists so that this never has to happen |

## LETS: Load, Extract, Transform, Save

The familiar cycle is ETL: extract from the sources, transform, load into the warehouse you then own and must keep alive. LETS inverts the order and the ownership. The store you already have *is* the database, so you load from it, build a throwaway engine around the slice you need, answer the question, and save the answer back as new immutable files beside the ones you read.

*[diagram]*

| **Load** | Fetch the bytes you need, straight from storage over an ordinary GET, and decrypt them where they are going to be used. No query planner, no connection pool, no session |
|---|---|
| **Extract** | Pull out the slice that the question is about, and the ontology that gives that slice its meaning. In a fractal graph these are separate files on purpose, so you can take the second without the first |
| **Transform** | Build a throwaway engine around it. SQLite compiled to WebAssembly for tabular questions, an RDF store for triple questions, ordinary in-memory structures for traversals. It is created for this question and thrown away after it |
| **Save** | Write the answer back as new immutable files with their provenance, a new version rather than an edit, and **shaped for the question that comes next**. The result is now itself loadable, which is what makes the cycle compose |

**The Save step is where the compounding happens, and it is the part people skip.** Saving is not filing the answer away. It is leaving behind an artefact cut to the shape of the next question, so that the next pass through the loop loads less than this one did. The Article 9 slice in the Regulation Graph exists because somebody answered a question about Article 9 once and then saved the answer in a form that makes asking again cost 29 KB instead of a megabyte. Do that a few times and the expensive queries have all been pre-answered, each by the run that first needed them, and none of it required deciding in advance which queries would matter. **Build time replaces query time, one question at a time, paid by whoever asked first.**

**The load-bearing consequence.** Because Save never overwrites, every object is immutable, and because every object is immutable, **every cache in the path is correct forever**. The browser cache, the CDN edge, the local clone and the agent's working copy never need invalidating. That is not a tuning trick. It is the reason there is no server: the hardest thing a database does for you, keeping one mutable truth consistent across readers, is a problem this architecture does not create.

## What it actually costs, measured

All of the following was measured on 21 September 2026 from an ordinary cloud container with no special network, against two live published vaults, using the read keys printed on their own pages. Anyone can repeat it.

### Opening a graph from the command line

The vault is the [DSIT AI Risk Toolkit](../vaults/dsit-ai-risk-toolkit/index.md), 42 files, 3.2 MB of content, a semantic graph of **1,051 nodes and 1,289 edges** across five worlds.

**A version drift, caught by measuring.** That vault's [own page here](../vaults/dsit-ai-risk-toolkit/index.md) says 617 nodes and 694 edges, which was true when it was published on 20 September. The vault released 0.2.1 on 21 September and the graph grew. The figures on this page are from the file as cloned today, counted rather than quoted, and the discrepancy is only visible because the vault keeps its versions rather than overwriting them.

| Operation | Bytes moved | Time |
|---|---|---|
| Full clone, every file and the whole history | 15 MB on disk | **65.4 s** |
| Sparse clone: every path, size and hash, no content | 256 KB | **7.3 s** |
| Fetch one file that answers one question (a 59 KB topic shard) | 59 KB | **0.49 s** |
| Fetch a second file (marginal cost of the next question) | 63 KB | **0.87 s** |
| Fetch the entire graph as one file | 1.0 MB | **1.21 s**(raw GET of the same object: 0.65 s) |
| Ask again for something already fetched | 0 | **0.18 s**, no network |

The first and third rows are the whole argument. **Cloning everything costs 65 seconds. Answering a question costs 7.8 seconds and 315 KB**, and the second question costs under a second. Nothing was indexed in advance, nothing was kept warm, and no service was running before the command was typed.

The sparse clone deserves its own sentence, because it is the step that makes the rest cheap. For 256 KB you get the complete file list with every size and content hash, which means **an agent can decide what is worth reading before reading anything**. The same call against the much larger [Regulation Graph](../vaults/regulation-graph/index.md) vault, 207 files and 14.9 MB, took **7.06 s and 360 KB**. The index does not grow with the content.

### Opening the same graph in a browser

Bytes and request counts for each view of that vault's app, measured by instrumenting the browser. This is the number that decides whether a page feels instant, and it is the number a graph database cannot improve, because the bottleneck was never the query.

*[diagram]*

Four things in that chart are worth naming.

- **The landing view of a 1,051-node semantic graph costs three requests and 94 KB.** Less than a typical web font pair. The graph file is not touched, because no question has been asked yet.
- **The most expensive view is a third of the vault.** There is no view that loads everything, because there is no question that needs everything.
- **The ontology is 2 KB.** In the Regulation Graph it is 4,217 bytes and fetched in 0.95 s. That is the entire price of arriving in a new world and learning its rules, which is what makes the [jump between worlds](index.md#what) affordable rather than theoretical.
- **The query engine is 859 KB and loads only if you query.** SQLite compiled to WebAssembly ships inside the vault. A reader who never opens the query view never pays for it, and one who does pays once and then queries for free, locally, offline, for as long as the tab is open.

The Regulation Graph shows the same shape at four times the size. It holds **1,523 nodes and 1,944 edges** over the EU AI Act. Its nodes file is 816 KB and its edges file 252 KB, so the graph is about 1.05 MB out of a 14.9 MB vault. Roughly 10 MB of that vault is raw source XML, retained so every claim can be traced back to the bytes it came from, and **never loaded to answer anything**. It also ships pre-cut slices: the Article 9 slice is 29,638 bytes and fetched in 0.75 s, so a question about Article 9 never touches the 1.05 MB graph at all.

## Getting at an encrypted file takes one request

This is the property underneath every number above, and it is the one most people do not expect, because encryption is usually assumed to add a lookup. It does not here.

**The address is derived, not discovered.** Every file id in a vault is produced by HMAC-SHA256 over the read key under a named domain: `sg-vault-v1:file-id:ref`, `:branch-ref`, `:branch-index`, and so on. The CLI and the browser client both do this, from the same constants. A client that holds the read key can therefore **compute the address of the branch ref, the index and the settings before making any request at all**. There is no discovery round trip, no directory to consult and no session to establish, which is the round trip that usually dominates a small read.

**Reading is then a plain CORS GET with no auth header**, because the bytes are useless without the key. Measured against a live vault on 21 September 2026:

| Request | Returned | Time |
|---|---|---|
| One object, `GET /api/vault/read/{vault_id}/bare/data/{object_id}`, no headers | 2,364 bytes of ciphertext | **0.35 s** best of six |
| The same, a larger object | 59,324 bytes of ciphertext | **0.31 s** best of six, [the same as the small one](#fixed) |
| Five objects, one `POST /api/vault/batch/{vault_id}` | 0.08 MB | **0.87 s**, one round trip |
| **Twenty objects, one POST** | **3.76 MB** | **2.79 s**, one round trip |
| Forty two objects, one POST | **502** | The server's response-size limit. The CLI already handles this by splitting the chunk |

### What that latency actually is, and why it is not an architecture cost

It would be easy to read the numbers above as the cost of reading encrypted data. They are not. Almost all of that time is **fixed per-request overhead, and it is completely insensitive to how many bytes come back**. Measured six times each, best of run:

| One GET returning | Best | Median |
|---|---|---|
| 340 bytes | 0.331 s | 0.381 s |
| 41 KB | **0.309 s** | 0.390 s |
| 2.3 KB | 0.347 s | 0.530 s |
| 1.0 MB | 0.647 s | 0.992 s |

**A 340-byte response and a 41 KB response take the same time.** Only at a megabyte does transfer become visible at all, and then it accounts for 0.300 s of the 0.647 s. One request that returned in 4.8 s during the run is the shape of the thing: a cold start, not a slow read.

So the floor of roughly a third of a second is **the per-invocation cost of running this API serverless**. It is a deployment choice with a known fix: SG/API also runs on EC2, where a warm process is already listening and that per-invocation cost does not exist. We have not measured that deployment here, so this page does not put a number on it, but the honest reading of the table above is that **the architecture is not what costs 350 ms, the invocation model is**, and anybody comparing this against a database on a warm connection should hold that separately.

Which makes the second optimisation the interesting one, because it works on either deployment.

### Batching, which is how the fixed cost gets amortised

`POST /api/vault/batch/{vault_id}` takes **up to 100 operations in one request**, and they can be **mixed reads and writes**. Measured on small objects, so that bytes stay out of the way and only the per-object cost shows:

| Objects in one batch | Best time | Per object |
|---|---|---|
| 1 | 0.590 s | 590 ms |
| 2 | 0.394 s | 197 ms |
| 5 | 0.560 s | 112 ms |
| 10 | 0.872 s | 87 ms |
| **18** | **1.528 s** | **85 ms** |

That fits a straight line, and the line is the cost model worth carrying around:

**time ≈ 0.25 s fixed, plus about 71 ms per object, plus transfer**

Eighteen objects fetched one at a time would be about 6.3 seconds. In one batch they took **1.53 seconds, a little over four times faster**, and the saving grows with the count until the response-size ceiling stops you. This is the optimisation that matters most in practice, because it is the one that turns a page needing thirty small files into a single round trip.

The batch endpoint does more than amortise reads, and the rest is worth knowing before building on it.

| **Mixed reads and writes in one request** | Operations are `read`, `write`, `write-if-match` and `delete`, authorised per operation, so a read-then-write cycle can be one round trip instead of two |
|---|---|
| **Atomic compare-and-swap across many files** | `write-if-match` carries the SHA-256 of the content you believe is there, and **if any match fails the entire batch is rejected**. That is optimistic concurrency over a set of files, in one request, with no lock anywhere |
| **A ceiling you will meet** | 100 operations per request is the hard limit, and there is a response-size limit well before that: our 42-object read returned 502. The CLI chunks at 50, and on a 502 it splits the chunk and then falls back to presigned S3 reads per file |
| **Large objects route around the body** | Presigned URLs rather than the request body, so a big blob never has to fit inside a batch response at all |

**The next thing worth optimising, named rather than glossed.** That 71 ms per object inside a batch is server-side work, and it is close to linear, which is the signature of the objects being fetched from storage one after another inside the handler. Fetching them concurrently would bring a twenty-object batch close to the cost of a one-object batch. That, and chunking by accumulated size rather than by file count so the 502 stops happening, are the two changes that would move these numbers most. Both are in the API and the client, not in the design.

Two things fall out of all of this. The first is that **the transport is not the bottleneck anywhere**: twenty files and 3.76 MB, which is more than half the vault's bytes, came back in one round trip in under three seconds. The second is the honest correction to the clone figure above, which is worth stating rather than hiding.

**Why the 65 second clone is a client-side cost, not a transport one.** The clone log says what happened: seven commits walked, twenty eight trees walked, and **106 blobs** downloaded rather than 42, because a full clone takes the history as well as the current files. Then one batch of 50 hit the server's response-size limit and fell back to fetching those 50 files one at a time, which is most of the 65 seconds. The transport moved 3.76 MB in 2.79 seconds when asked in one request. That gap is an engineering finding for the CLI, chunk by accumulated size rather than by file count, and not a property of the architecture.

**Encryption costs 28 bytes per object, flat.** The two measurements above were 2,364 bytes of ciphertext for 2,336 of plaintext, and 59,324 for 59,296. That is a 12-byte nonce plus a 16-byte authentication tag, the same 28 bytes whether the file is two kilobytes or two megabytes. There is no percentage overhead to budget for and no padding to reason about.

**There are two ways to address a file, and the choice is a performance decision.** Pin the content-addressed object id in your page and reading it is exactly one GET, valid forever, because the id is a hash of the ciphertext and those bytes can never change. Or give a path and let the client resolve HEAD to tree to blob, which costs a small number of extra hops and always gives you the current version. Neither is better. They answer different questions, and a well-built page uses both.

## If speed really matters, take the API out of the path

Everything measured so far went through the API, and the API turned out to be most of the cost. It is worth saying plainly what that API is: **a convenience over a store, not a requirement of it**. The store is cloud storage holding encrypted objects whose names are hashes. Nothing prevents a reader going straight to the bucket, or to a CDN in front of it, with no function in the path at all.

**And nothing much is risked by doing so**, which is the part that makes this a real option rather than a dangerous one. Every object is ciphertext under a key the server never had, and every name is a hash of those bytes. Exposing the objects as ordinary public GETs discloses object sizes and request timing, which is the same exposure the API already has and which [the security model](../../security/index.md) names as an acknowledged side channel. It discloses nothing else. That is why reads need no auth header today, and it is why a bucket behind a CDN is a legitimate deployment rather than a hole.

### It already ships, and here is what it costs

The CLI has a transport for exactly this. `--transport static` points at any host that answers GETs, sniffs which of two published layouts it uses on the first successful read, then fans out **eight parallel requests at a time**. It also records every URL it touches, so a test can assert that no request ever carried key material, which is the kind of check that proves a property rather than asserting one.

So the same clone can be run twice, same client, same 106 objects, same decryption, with only the path to the bytes changed.

| Path to the bytes | Full clone of the same vault |
|---|---|
| Through the serverless API | **65.4 s** |
| **Plain GETs, no API in the path** | **2.63 s** |
| Straight off a local folder | 2.05 s |

**Twenty five times faster, with nothing about the vault changed.** The honest caveat: that static host was on localhost, so the network was free, and a real CDN would add edge latency. But the comparison still isolates what it is meant to, because the client, the objects and the work were identical in both rows. The difference is the function in the middle. If a workload is request-heavy, this is the lever, and it is a bigger one than any tuning inside the API.

### The direct path is already in production for large files

This is not a hypothetical route. Anything over **4 MB** already takes it, because that is the safe margin under the serverless base64 response limit of about 4.7 MB. The client asks the API for a presigned URL and then **fetches the bytes straight from storage**. The same fallback catches a batch that returns 502: split the chunk, and if a single object still fails, go around the API entirely and read it presigned.

Which means the architecture already has two paths to every byte, and the only reason the small case goes through a function is that nobody has needed it not to. The options from here are ordinary storage engineering rather than anything exotic.

| **A CDN in front of the bucket** | Immutable objects with hash names are the ideal cache key. Every edge holds them correctly and forever, and reads never reach the origin twice |
|---|---|
| **Ranged and parallel GETs** | Object storage serves byte ranges, so a very large object comes down as many chunks at once rather than one stream. This is how a 100 MB or 500 MB file should be read, and it is available because the store is a standard one |
| **Lower-latency storage classes** | The newer single-digit-millisecond classes, such as S3 Express One Zone, exist precisely for small-object read latency. We have not benchmarked one, so there is no number here, only the observation that the store is ordinary enough to move onto one |
| **Somewhere else entirely** | The store is cloud storage, so it is not tied to one provider. Another object store, another CDN, or a service dedicated to serving files fast will all work, because what is being served is opaque bytes at deterministic paths |

### Finding the object you want, in a handful of requests

Direct access is only useful if you can work out which object to ask for. In most cases you already know, because the id is pinned in the page or held in an index you have. When you do not, the walk is short: the branch ref, which gives you the commit, which gives you a tree, which gives you the file or the next tree down. **A couple of requests, not a clone.**

Measured against the static host, counting every GET it received: reading one named file out of a sparse clone cost **two requests**, and one of those was the client re-probing which layout the host uses, a 404 it could skip by remembering the answer. The real cost is one GET.

**This is the thing git cannot do.** Pulling one file out of a git repository generally means cloning the repository, because the objects are packed and the transport is negotiated. Here every object is individually addressable at a deterministic path, so one file is one request against a plain web server. It is also why `--sparse` exists and works: **structure only, 256 KB and 7.3 s, then fetch content on demand**, which is the shallow clone of this world. `--bare` takes the structure with no working copy at all.

One gap, stated because it is the cause of the 65 second figure: **there is no history-depth flag today.** A full clone takes every version of every file, 106 blobs where the current tree is 42 files. A sparse clone avoids the content but still walks all seven commits and twenty eight trees. Depth control, so that a reader can ask for the current tree and nothing older, is the missing option, and it would do more for clone time than anything else on this list.

## Live evidence: a whole knowledge base served from encrypted vaults

[sgraph.ai/en-gb/library/](https://sgraph.ai/en-gb/library/) is a public knowledge base whose content does not exist on the web server. It is a static shell that reads everything out of two encrypted vaults, in the visitor's browser, with read keys published in the page on purpose.

| **The shell** | 28 KB of HTML plus 242 KB of CSS and components, **270 KB in total**, entirely static and cacheable by anything. Measured 21 September 2026 |
|---|---|
| **The content** | Every article, the navigation tree, the blog and the what's-new entries come from vaults, decrypted in the tab. The server hosting that site cannot read a word of what it is serving |
| **Pinned reads** | Blog and what's-new entries carry their content-addressed object id in the page source, so opening one is a single GET straight to the bytes |
| **Resolved reads** | The navigation is deliberately *not* pinned. Its own source comment says why: no hardcoded nav object id, the client resolves HEAD to tree to blob at runtime, so the nav is always current |
| **The cache** | A small script loaded before anything else patches `fetch` and keeps immutable objects in IndexedDB. See below |

That is the architecture argued on this page, running as somebody's production documentation site rather than as a demo. The interesting part is not that it works. It is that the performance profile is the one a plain static site has, while the data underneath it stays encrypted, versioned and owned by whoever holds the vault key.

## Append mode: writes that never touch the graph

The read path is only half of it. Writing into a vault would normally be the expensive, contended operation: read the current state, modify, commit, rebuild the tree, take a lock, resolve a conflict. **Append lanes skip all of that.**

A lane lives at `bare/append/{token}/pending/`, **outside the version-controlled commit tree**. The consequence is stated plainly in [the API documentation](../../api/append-lanes.md): appends never touch a branch and never conflict with a push. The performance implications follow directly.

| **A write is one POST** | The token goes in the body, and the call is **account-less**: no access token, no session, no login. Nothing is read before writing, so there is no read-modify-write cycle to lose a race in |
|---|---|
| **Nothing is rebuilt** | No commit, no tree, no index update, no branch move. The object is placed in a lane and that is the whole operation |
| **Writes never contend with reads** | The lane is not in the commit tree, so a reader walking the graph never looks at it. A million appends do not slow a single read, and they cannot conflict with somebody else pushing at the same moment |
| **The response is deliberately blind** | `{"ok":true}`, with no id and no count. The server does no extra work to compose an answer and leaks nothing about lane contents by timing or size |
| **Senders scale sideways** | Register several anchors and each sender writes into their own lane. One correspondent flooding you does not bury another, and revoking one sender is removing one anchor with no effect on the rest |

The published limits are the shape of the envelope: 5 MB per payload, 1,000 pending per token, 100 file ids per batch, 3 MB inline content, pages of 50 up to 200. This is what makes telemetry, logs, signals, control messages and state flows cheap enough to be ordinary, and it is the transport behind [vault-to-vault messaging](../../docs/vault-messaging.md). A vault whose read key is public can collect anonymous usage from its own readers without anybody holding a credential that could change it.

## Caching encrypted data, which turns out to be the easy case

The usual reason not to cache aggressively is that a cache becomes a second place the data lives, with its own exposure and its own staleness. Neither applies here, and both for the same reason.

- **The cached bytes are ciphertext.** A cache holding them is not a trust boundary, because the decryption key never goes near it. The browser cache, IndexedDB, a CDN edge, a corporate proxy and a local clone can all hold vault objects without widening exposure by one byte. That is why a vault can sit behind a CDN at all.
- **The name proves the bytes.** An `obj-cas-imm-` id is SHA-256 *over the ciphertext*. A cache entry under that name can never be stale and can never be wrong, so no invalidation logic is needed anywhere. It also gives deduplication without the server ever knowing a byte of plaintext, and it makes the caching rule derivable from the id alone.
- **Mutable refs are the exception, and the failure is silent.** A stale ref renders a previous commit's tree from ciphertext that is itself perfectly valid, so nothing errors and the reader simply sees an old version of the vault. Refs must never be cached. [The caching contract](../../api/vault-objects.md) is explicit about the split.

The library site above ships this as a small script loaded before any module, which patches `fetch` and does three things: keeps immutable objects in **IndexedDB so later page loads need no network round trip at all**; collapses concurrent callers for the same URL into a single request, which it says was introduced to kill a duplicate fetch between two navigation components; and times out in-flight entries after 30 seconds. It labels every response it serves, `idb-hit`, `inflight` or `network`, and emits an event per fetch, so the caching is observable rather than magic.

**A gap found while measuring this, reported rather than smoothed over.** Our own [caching contract](../../api/vault-objects.md) says an immutable object should be served with `Cache-Control: public, max-age=31536000, immutable` and a ref with `no-store`. On 21 September 2026 the read endpoint returned **no `Cache-Control` header at all** for an immutable object, and the CDN reported a miss. The mechanism is unaffected, because the client cache keys on the id rather than trusting a header, which is the more robust design and is exactly why the library site ships its own. But the documented header is not live on that path today, and the page that documents it should not be read as describing what is currently served.

## Restructuring into context is the compression

The fractal property is usually argued as a point about meaning: each world keeps its own ontology, so nothing is forced to conform. It is also, and less obviously, a point about **volume**. Restructuring data into context *is* compression, and unlike ordinary compression it costs nothing to reverse, because every level keeps the edge down to the level below.

Here is the ladder with real bytes, measured in the [Regulation Graph](../vaults/regulation-graph/index.md) vault, which models the EU AI Act.

| Altitude | What it is | Bytes | Against the level below |
|---|---|---|---|
| **The source** | The law as published, raw Formex XML, retained so every claim traces to the bytes it came from | 11,216,043 |  |
| **The graph** | Nodes and edges: 1,523 nodes, 1,944 edges, the whole instrument | 1,073,915 | **10x smaller** |
| **One article's slice** | Article 9, pre-cut because it was asked about | 29,638 | **36x smaller** |
| **The ontology** | The rules of this world: partitions, namespaces, what may and may not be claimed | 4,217 | **7x smaller** |

Top to bottom that is **11.2 MB down to 4.2 KB, a factor of about 2,660**, and not one byte has been thrown away. The source is still there, still hashed, still one link below. This is why the fractal structure is a performance feature rather than only a modelling one: **you query the small thing, and you follow the link down only when the answer actually requires it.** A reader asking what the Act says about risk management systems loads 29 KB. A reader who then wants to see the exact published wording follows an edge and loads that. Nobody loads 11 MB, and nobody is prevented from reaching it.

The same shape is in the [DSIT vault](../vaults/dsit-ai-risk-toolkit/index.md), where 503 KB of retained sources sit under a graph, under an ontology of 2,336 bytes that explains the whole thing.

**Which is why this scales in the direction that usually breaks things.** In a schema-first system, more data means a bigger index, more memory and a bigger machine: the cost of a query grows with the size of the store. Here it does not. The store can be gigabytes or terabytes, and **what a question loads stays in the megabytes, because the graph is what tells you which bytes matter.** Adding a terabyte adds nodes you did not load. That is the claim worth testing against your own data, and it is the one that makes the architecture interesting at scale rather than merely cheap at rest.

## Why it is fast, in four sentences

| **Never render the graph, render the answer** | The unit of work is the question, not the dataset. Traditional graph tooling optimises traversal over a loaded graph. This skips the loading, which is the part that was expensive |
|---|---|
| **Each world is small because each world keeps its own ontology** | There is no global schema to carry around, so a traversal stays inside one world until it deliberately crosses an edge. Crossing costs one small file. This is the performance benefit of the fractal property, and it is not an accident of it |
| **Immutable and content addressed, so every cache is correct** | The CDN is the read replica. The browser cache is the local index. Neither can ever be stale, because an object's name is its content, and neither is a trust boundary, because what it holds is ciphertext |
| **The address is computed, not looked up** | File ids are derived by HMAC from the read key, so reading an encrypted file is one unauthenticated GET with no discovery round trip, and twenty of them are one POST |
| **And the design does most of it** | The habit of asking what data this question needs, on top of three layers that were already fast, beats any amount of engine tuning. Decryption runs at 2,978 MB/s and a local read at 418 MB/s, so [the only real variables are how many requests you made and how many bytes you asked for](#design), and [a batch collapses the first of those](#batching) |

## The cost model, which is the part that changes the decision

Performance arguments are usually won or lost on the invoice rather than the benchmark. Here is what is on ours and what is not.

| What you normally pay for | Here |
|---|---|
| Database instance hours, around the clock | **Zero.** There is no instance |
| Memory sized to hold the index | **Zero.** The index is a 256 KB file, and it is the reader who holds it |
| Read replicas for concurrency | **Zero.** Concurrency is the CDN's problem, and it is already solved |
| Backups, snapshots, point-in-time recovery | **Zero as a separate line.** Every version is already retained, because nothing is ever overwritten |
| A staging copy of the database | **Zero.** A clone is a clone. That is the whole mechanism |
| Query compute | **Paid by the reader's own device**, in the tab they already have open, or by a function that ran for a fraction of a second |
| Storage | **The only standing line.** Object storage at rest |
| Egress | **The only variable line.** The bytes that were actually read, which the numbers above show is a small fraction of what is stored |

To put a size on the standing line: the entire published estate on this site, [thirty one vaults](../vaults/index.md), is **2,662 files and 295 MB**. That is the whole corpus, including a 66 MB vault and a 43 MB one. It sits in object storage and costs what a third of a gigabyte costs, which at every major provider's standard rate is small change per month. There is no second bill, because there is no second thing running.

The shape of this matters more than the absolute figure. **Cost scales with what is read, not with what exists, and not with time.** A graph nobody opened this month cost only its storage. A graph that got a hundred thousand readers cost its egress and nothing else, because every one of those readers brought their own compute. There is no capacity to plan, nothing to right size, and no traffic spike that can produce an outage in a component that does not exist.

**The part that surprises people.** Scale to zero is normally a property you buy with a serverless platform and give back the moment you attach a database, because the database cannot scale to zero: it is holding the state. Here the state is in files, so the zero is real. Between questions, this architecture is *not running*, in the literal sense, and it still answers the next question in under a second.

## Running everywhere, on one read key

Because the graph is files and the engine is disposable, the same artefact runs in four very different places with no porting, no build, no account and nothing installed beyond what is already there.

| Where | What it needs | What it does |
|---|---|---|
| **A browser tab** | The URL and the read key in the fragment | Fetches ciphertext over ordinary CORS GETs, decrypts in the page, runs SQLite in WebAssembly. [The primitive is documented](../../docs/vault/reading-a-vault-file.md) and every live embed on this site uses it |
| **A terminal** | `pip install sgit-ai` | Clone, sparse clone, fetch one file. The measurements above were taken this way |
| **A serverless function** | Outbound HTTPS | Load the slice, build the ephemeral engine, answer, return. Nothing to keep warm and nothing to tear down, because the function dying *is* the teardown |
| **A CI container or an agent's sandbox** | The read key as a variable | The same clone the human gets, in a pipeline, with the history attached so a build can assert on what changed |
| **A static host with no backend at all** | GitHub Pages or an S3 bucket | Deterministic GET paths and client-side decryption, degrading cleanly to read only. [Documented here](../../docs/vault/static-hosting.md) |

The same applies to the API itself, which is the point most easily missed. **SG/API is not tied to a serverless runtime.** The measurements on this page were taken against the serverless deployment, which is why every request carries the invocation cost described above. The same API runs on EC2, with a warm process already listening, and that cost is simply not there. And [the API can be left out of the path altogether](#direct), with readers going straight to the bucket or a CDN in front of it, which measured 25 times faster on the same clone. **Where the bytes are served from is a deployment decision, separate from the architecture**, and it is the right lever to reach for when a workload is request-heavy rather than byte-heavy.

**And a real database comes with it, wherever it lands.** A browser tab or a function can stand up a full SQL engine over the slice it just loaded: SQLite compiled to WebAssembly, in memory, with real indexes and real joins. That is not a workaround for lacking a server. It is the same thing the managed services do, and it is worth noticing that they do it: plenty of serverless and scale-to-zero database products work by loading the dataset into an in-memory SQLite or MySQL when an instance wakes, and serving queries from there. The dataset being small enough to hold in memory is what makes them viable. **We do explicitly what they do implicitly**, with two differences: the working set is chosen by the question rather than by an instance lifecycle, and nothing has to wake up, because the engine is built where the answer is needed.

This is also the disaster recovery story, and it is short. Every reader who ever cloned has a complete, verifiable copy including history. There is no primary to fail over from.

## Fractal deployment: the same shape at every altitude

The architecture repeats the property the graphs have. A vault holds files. A vault can hold another vault, by reference, with its own owner and its own read key. A vault can hold the app that reads it, and that app can hold the engine that queries it. A site can read a vault it does not own. At each of those altitudes the thing you are looking at is the same kind of thing, addressed the same way, opened with the same one credential.

| **Deploy one graph** | Publish the files. The read key is the deployment |
|---|---|
| **Deploy a graph of graphs** | [Sub-vaults](../../docs/vault/sub-vaults.md): a link file pointing at another vault, which has its own owner, its own key and its own ontology. Nobody merges anything |
| **Deploy it inside somebody else's boundary** | The same files in their bucket, or their GitHub Pages, or their air-gapped copy. The app does not care where the GETs are answered from |
| **Deploy the reader, not the data** | A site page that reads a vault it does not own, decrypting in the visitor's browser. The trust direction inverts and [the surfaces page](../../docs/surfaces.md) says how |

The practical consequence for anyone with a data boundary to respect: **the deployment unit is a set of files and a key**, so putting a graph inside a regulated environment, a customer's tenancy or a machine with no internet is a copy, not a project. And two organisations can join their graphs by exchanging an edge and a read key, without either one adopting the other's schema or hosting the other's database.

## Where it is slower, stated plainly

This page would not be worth sending if it only listed wins.

- **A full clone is slow, and not for the reason it looks.** 65 seconds for 3.2 MB, but the same clone against plain GETs with no API in the path took **2.63 seconds**. It is slow because it takes the history too, 106 blobs rather than 42 files, and because one batch of 50 exceeded the server's response-size limit and degraded to 50 individual fetches. None of that is the architecture. Until it is fixed, use the sparse clone or [the static transport](#direct).
- **There is no history-depth flag.** You can skip the content with `--sparse`, but you cannot yet ask for the current tree without its ancestors. That is the single change that would most improve clone time.
- **Every request pays about a third of a second before it returns a byte**, on the serverless deployment measured here. That is the invocation, not the read, and it does not grow with the response. It is also the most improvable number on this page: batch up to a hundred operations into one request, or run SG/API on EC2 where a warm process is already listening.
- **There is no server-side query.** Whatever the client needs, the client downloads. That is fine at a megabyte and wrong at a gigabyte, which is why partitions and pre-cut slices are a design step rather than an optimisation you reach for later.
- **Deep traversal over a very large single-domain graph is not our ground.** Six hops across a hundred million edges in one schema is exactly what a graph database was built for. Use one. The fractal argument is about the case where those hundred million edges were never going to live in one schema in the first place.
- **Writes are single writer per branch.** There is no concurrent multi-writer transaction, by design. [The two-branch model](../../docs/two-branch-model.md) is how several agents work without one.
- **Cutting good slices is real work.** The Article 9 slice is fast because somebody decided Article 9 was a question worth pre-answering. Build time replaces query time, and the judgement of what to cut does not come for free.
- **Revocation is not retroactive.** A published read key cannot be unpublished, and anyone who cloned keeps their copy. That is the same property as the disaster recovery win, seen from the other side. [The credentials page](../../docs/credentials.md) is explicit about it.

## Repeat the measurements

Every number on this page came from these commands, against a vault whose read key is published on its own page and cannot write anything.

```
$ pip install sgit-ai
$ time sgit clone <read-key> dsit
  42 files, 3.2 MB                                  65.4 s
$ time sgit clone --sparse <read-key> sparse
  structure only, 256 KB on disk                     7.3 s
$ cd sparse && time sgit fetch data/questions/security.json
  59 KB                                              0.49 s
$ time sgit fetch data/graph.json
1.0 MB, the whole 1,051-node graph                 1.21 s
         the raw GET of that object, without the client: 0.65 s
```

The direct path needs no vault host at all, only something that answers GETs:

```
$ sgit clone --transport static --base-url https://<any-get-host>/ <read-key> v
  106 objects, 60 files extracted                    2.63 s
  the same clone through the API:                   65.40 s
```

The transport figures used no client at all. One encrypted object, no auth header, no account:

```
$ curl "https://send.sgraph.ai/api/vault/read/0q4sfr57/bare%2Fdata%2F<object-id>"
  59,324 bytes of ciphertext                         0.63 s
$ curl -X POST "https://send.sgraph.ai/api/vault/batch/0q4sfr57" \
       -d '{"operations":[{"op":"read","file_id":"bare/data/<id>"}, ...]}'
  20 objects, 3.76 MB, one round trip                2.79 s
```

Object ids come from `sgit ls --json` against a sparse clone, which prints every path with its size and its `blob_id` without downloading anything.

The disk and crypto figures are local, so they need no vault at all. Decryption was timed over 200 iterations of AES-256-GCM on random data of each size, after a warm-up, using the same `cryptography` library the CLI uses:

```
$ python3 -c "measure AESGCM(key).decrypt over 1.0 MB, 200 runs"
0.351 ms per call                              2,978 MB/s
  the same call on a 59 KB shard: 0.025 ms
```

The read key is on [the vault's page](../vaults/dsit-ai-risk-toolkit/index.md), published on purpose. Browser figures were taken by instrumenting the page and recording every response, so they are exact byte counts rather than estimates, with network latency excluded; the latency numbers above are from the live API over an ordinary connection. Agents: the machine-readable list of every vault, with ids and read keys, is [/demos/vaults/llms.txt](../vaults/llms.txt).

## The answer to the question, in one paragraph

Most of the win is a design habit rather than a technology: ask what data this question needs, and build on three layers that are already fast, the file system, a content-addressed hash store, and a graph that tells you which bytes to ask for. Decryption runs at nearly 3 GB/s and a local read at 418 MB/s, so what is left is the request: a fixed cost of roughly a third of a second on the serverless deployment, insensitive to size, which a batch of up to a hundred operations amortises away and a warm process on EC2 removes. The remaining variable is how many bytes you decided to load, and the fractal structure is what keeps that number small, by restructuring data into context and keeping a link down to the source. Graph engineering and fractal semantic graphs are not competing on the same benchmark. A graph database makes traversal fast by first making you pay to get everything inside it, and then keeps charging while nobody is asking. A fractal semantic graph leaves the data as encrypted files, lets each domain keep its own ontology, and builds a disposable engine around the small slice a question actually touches. Reading one of those files is a single unauthenticated GET, because the address was derived from the read key rather than looked up, and twenty of them are one POST. Writes go to a lane outside the commit tree, so they never contend with reads. The cached bytes are ciphertext, so every cache in the path can hold them safely and none of them can go stale, because an object's name is a hash of its content. The measured result is a 1,051-node graph that opens in 94 KB, a question answered in under eight seconds from a cold start with nothing running, a marginal question under a second, and an estate of thirty one graphs whose entire standing cost is 295 MB of object storage. What you give up is deep traversal over one enormous single-schema graph. What you gain is that the graphs you could never have merged into one schema can now be connected by an edge, and that the whole thing runs in a browser tab.

[← Fractal Semantic Graphs](index.md)[The vault that was measured →](../vaults/dsit-ai-risk-toolkit/index.md)


---

*[Site index for agents](../../llms.txt) · [HTML version](https://sgit.ai/demos/fractal-graphs/performance.html)*
