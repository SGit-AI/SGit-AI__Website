# Performance, cost, and running everywhere, Fractal Semantic Graphs

> Measured answer to “performance of graph engineering versus fractal graph”: no live database, files in object storage, and the LETS cycle (Load, Extract, Transform, Save) with a disposable engine in the reader's tab. A 617-node graph opens in 94 KB and three requests, a question costs 7.8 s and 315 KB from cold against 65.4 s for a full clone, an ontology costs 4 KB, and the standing cost of thirty one published graphs is 295 MB of object storage with nothing running between questions. Plus the cost model line by line, the five places the same read key runs, fractal deployment, and six places it is slower.

*Source: <https://sgit.ai/demos/fractal-graphs/performance.html> · site v0.3.2 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../index.md) / [Fractal Semantic Graphs](index.md) / Performance and cost

# Performance, cost, and running everywhere

A reader of [the Fractal Semantic Graphs page](index.md) asked the right follow-up question: what is the **performance** of this against ordinary graph engineering? The honest answer needs the architecture said out loud first, because the two are not doing the same work. We run with **no live database**. A graph is a set of files in cloud storage, read directly. The engine that answers a question is created when the question is asked and destroyed when it is answered, either in the reader's browser tab or in a serverless function that lives for one request. We call the cycle **LETS**: Load, Extract, Transform, Save. This page gives the measured numbers, taken on 21 September 2026 against live published vaults, then the cost model, then the part that matters most in practice: the same graph runs in a browser, a terminal, a function and a build container, with one read key and nothing installed.

## The short answer

A graph database is very good at one thing this is not trying to do, and pays for it in a way we are not willing to pay. Both columns below are real engineering positions. The question is which bill you want.

|  | Classic graph engineering | Fractal Semantic Graph |
|---|---|---|
| **Where the graph lives** | Inside a database process, in its own storage format | In ordinary files in object storage, content addressed and encrypted |
| **What runs between questions** | A server, its indexes, its replicas, its backups | Nothing at all |
| **Cost of admission** | Everything must be loaded in, and conform to one schema | Publish the files and declare the ontology. Other worlds keep their own |
| **Where a query runs** | On the server, for every reader | In the reader's tab, or in a function that exists for one request |
| **What a query costs the owner** | Instance hours, whether anyone asks or not | The bytes that were actually read |
| **Joining two domains** | A shared schema, so a migration, so a project | An edge, because neither side gives up its own ontology |
| **Six hops over a hundred million edges** | **Its home ground.** Nothing here competes | Not this. See [where it is slower](#limits) |
| **Answering one question over a million** | Fast, once the server is up and loaded | Fast, and the server was never up |

The performance claim is therefore narrow and testable: **for the questions people actually ask of a semantic graph, the work is bounded by the answer, not by the graph**, and the numbers below are what that costs.

## LETS: Load, Extract, Transform, Save

The familiar cycle is ETL: extract from the sources, transform, load into the warehouse you then own and must keep alive. LETS inverts the order and the ownership. The store you already have *is* the database, so you load from it, build a throwaway engine around the slice you need, answer the question, and save the answer back as new immutable files beside the ones you read.

*[diagram]*

| **Load** | Fetch the bytes you need, straight from storage over an ordinary GET, and decrypt them where they are going to be used. No query planner, no connection pool, no session |
|---|---|
| **Extract** | Pull out the slice that the question is about, and the ontology that gives that slice its meaning. In a fractal graph these are separate files on purpose, so you can take the second without the first |
| **Transform** | Build a throwaway engine around it. SQLite compiled to WebAssembly for tabular questions, an RDF store for triple questions, ordinary in-memory structures for traversals. It is created for this question and thrown away after it |
| **Save** | Write the answer back as new immutable files with their provenance, a new version rather than an edit. The result is now itself loadable, which is what makes the cycle compose |

**The load-bearing consequence.** Because Save never overwrites, every object is immutable, and because every object is immutable, **every cache in the path is correct forever**. The browser cache, the CDN edge, the local clone and the agent's working copy never need invalidating. That is not a tuning trick. It is the reason there is no server: the hardest thing a database does for you, keeping one mutable truth consistent across readers, is a problem this architecture does not create.

## What it actually costs, measured

All of the following was measured on 21 September 2026 from an ordinary cloud container with no special network, against two live published vaults, using the read keys printed on their own pages. Anyone can repeat it.

### Opening a graph from the command line

The vault is the [DSIT AI Risk Toolkit](../vaults/dsit-ai-risk-toolkit/index.md), 42 files, 3.2 MB of content, a semantic graph of **617 nodes and 694 edges** across four worlds.

| Operation | Bytes moved | Time |
|---|---|---|
| Full clone, every file and the whole history | 15 MB on disk | **65.4 s** |
| Sparse clone: every path, size and hash, no content | 256 KB | **7.3 s** |
| Fetch one file that answers one question (a 59 KB topic shard) | 59 KB | **0.49 s** |
| Fetch a second file (marginal cost of the next question) | 63 KB | **0.87 s** |
| Fetch the entire graph as one file | 1.0 MB | **1.21 s** |
| Ask again for something already fetched | 0 | **0.18 s**, no network |

The first and third rows are the whole argument. **Cloning everything costs 65 seconds. Answering a question costs 7.8 seconds and 315 KB**, and the second question costs under a second. Nothing was indexed in advance, nothing was kept warm, and no service was running before the command was typed.

The sparse clone deserves its own sentence, because it is the step that makes the rest cheap. For 256 KB you get the complete file list with every size and content hash, which means **an agent can decide what is worth reading before reading anything**. The same call against the much larger [Regulation Graph](../vaults/regulation-graph/index.md) vault, 207 files and 14.9 MB, took **7.06 s and 360 KB**. The index does not grow with the content.

### Opening the same graph in a browser

Bytes and request counts for each view of that vault's app, measured by instrumenting the browser. This is the number that decides whether a page feels instant, and it is the number a graph database cannot improve, because the bottleneck was never the query.

*[diagram]*

Four things in that chart are worth naming.

- **The landing view of a 617-node semantic graph costs three requests and 94 KB.** Less than a typical web font pair. The graph file is not touched, because no question has been asked yet.
- **The most expensive view is a third of the vault.** There is no view that loads everything, because there is no question that needs everything.
- **The ontology is 2 KB.** In the Regulation Graph it is 4,217 bytes and fetched in 0.95 s. That is the entire price of arriving in a new world and learning its rules, which is what makes the [jump between worlds](index.md#what) affordable rather than theoretical.
- **The query engine is 859 KB and loads only if you query.** SQLite compiled to WebAssembly ships inside the vault. A reader who never opens the query view never pays for it, and one who does pays once and then queries for free, locally, offline, for as long as the tab is open.

The Regulation Graph shows the same shape at four times the size. It holds **1,523 nodes and 1,944 edges** over the EU AI Act. Its nodes file is 816 KB and its edges file 252 KB, so the graph is about 1.05 MB out of a 14.9 MB vault. Roughly 10 MB of that vault is raw source XML, retained so every claim can be traced back to the bytes it came from, and **never loaded to answer anything**. It also ships pre-cut slices: the Article 9 slice is 29,638 bytes and fetched in 0.75 s, so a question about Article 9 never touches the 1.05 MB graph at all.

## Why it is fast, in three sentences

| **Never render the graph, render the answer** | The unit of work is the question, not the dataset. Traditional graph tooling optimises traversal over a loaded graph. This skips the loading, which is the part that was expensive |
|---|---|
| **Each world is small because each world keeps its own ontology** | There is no global schema to carry around, so a traversal stays inside one world until it deliberately crosses an edge. Crossing costs one small file. This is the performance benefit of the fractal property, and it is not an accident of it |
| **Immutable and content addressed, so every cache is correct** | The CDN is the read replica. The browser cache is the local index. Neither can ever be stale, because an object's name is its content |

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

- **A full clone is slow.** 65 seconds for 3.2 MB, because every object is fetched and decrypted individually. If your workflow genuinely needs all of a large vault on disk, that is the price, and the answer is usually that it does not: use the sparse clone.
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
1.0 MB, the whole 617-node graph                   1.21 s
```

The read key is on [the vault's page](../vaults/dsit-ai-risk-toolkit/index.md), published on purpose. Browser figures were taken by instrumenting the page and recording every response, so they are exact byte counts rather than estimates, with network latency excluded; the latency numbers above are from the live API over an ordinary connection. Agents: the machine-readable list of every vault, with ids and read keys, is [/demos/vaults/llms.txt](../vaults/llms.txt).

## The answer to the question, in one paragraph

Graph engineering and fractal semantic graphs are not competing on the same benchmark. A graph database makes traversal fast by first making you pay to get everything inside it, and then keeps charging while nobody is asking. A fractal semantic graph leaves the data as files, lets each domain keep its own ontology, and builds a disposable engine around the small slice a question actually touches. The measured result is a 617-node graph that opens in 94 KB, a question answered in under eight seconds from a cold start with nothing running, a marginal question under a second, and an estate of thirty one graphs whose entire standing cost is 295 MB of object storage. What you give up is deep traversal over one enormous single-schema graph. What you gain is that the graphs you could never have merged into one schema can now be connected by an edge, and that the whole thing runs in a browser tab.

[← Fractal Semantic Graphs](index.md)[The vault that was measured →](../vaults/dsit-ai-risk-toolkit/index.md)


---

*[Site index for agents](../../llms.txt) · [HTML version](https://sgit.ai/demos/fractal-graphs/performance.html)*
