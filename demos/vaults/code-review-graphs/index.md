# Code review graphs: the sgit CLI, layer by layer, published as a vault

> One real codebase read as a fractal semantic graph from its syntax tree: eleven stories, 72 commands, 13 packages, 377 classes, 1,111 methods and 2,592 calls, two method streams, one commit read upwards to the nine commands and six stories it can reach, and ten house rules checked against the graph. Nothing produced by running the code; the scripts are in the vault.

*Source: <https://sgit.ai/demos/vaults/code-review-graphs/index.html> · site v0.7.8 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../index.md) / Code Review Graphs

# Code review graphs: the sgit CLI, layer by layer

One real codebase, the `sgit-ai` command-line tool, read as a fractal semantic graph from its own syntax tree: eleven user stories at the top, then 72 commands, 13 packages, 427 modules, 377 classes, 1,111 methods and the 2,592 calls between them, down to 177,313 syntax-tree nodes. Two method streams, the code on one path and only that code. One commit read upwards, from the seven methods it changed to the nine commands and six stories that can reach them. Ten house rules checked against the graph. Nothing in it was produced by running the code. It is the worked example for the article [Code review as a fractal semantic graph](../../../articles/code-review-as-a-fractal-semantic-graph.md).

**The argument is in the article.** This vault is the worked example for [**Code review as a fractal semantic graph**](../../../articles/code-review-as-a-fractal-semantic-graph.md): why source code is already layers within layers, what C4 and Gherkin saw, why a review should diff every layer, how a refactor and a fix look different in the graph, method streams from the O2 Platform, and what makes the whole thing trustworthy. Read it for the why; this page is the how, with the numbers.

The ladder as the vault opens: seven altitudes of one repository, with how many nodes at each one commit touched. Rendered from the read-key clone, served locally.

**Open it yourself. The key is the whole credential.**
 Read key: `sgit_public_read_d27c20b6309ff0ad3ab228372d174a04d1c40e44e2d3077465bf1d998b4e1578:7w90lvd3`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_public_read_d27c20b6309ff0ad3ab228372d174a04d1c40e44e2d3077465bf1d998b4e1578%3A7w90lvd3) · From the CLI: `sgit clone sgit_public_read_d27c20b6309ff0ad3ab228372d174a04d1c40e44e2d3077465bf1d998b4e1578:7w90lvd3`
This key is published on purpose, under the `sgit_public_read_` prefix. It is **derived** one way from a vault key that is kept in the gitignored tier and never published. `check_credential.py` classified it as a public read key before it was put on this page. A read-only clone with it produced the same twenty files as the source folder, and a commit and push from that clone were refused with "cloned read-only". An all-zeros key as a control failed to find a vault.

## See it live, here

The vault opens as an app. Pick a layer along the top, filter the classes or methods, open a method stream, or read the commit upwards. You can also [**open it in its own window ↗**](https://dev.vault.sgraph.ai/#sgit_public_read_d27c20b6309ff0ad3ab228372d174a04d1c40e44e2d3077465bf1d998b4e1578%3A7w90lvd3).

## What was derived, and from what

The source is the `sgit-ai` repository at two commits: `0e4727f`, and `397be83`, whose message reads "auto transport no longer flips a fresh vault to read-only on an object 404". Three scripts in the vault's `tools/` folder did the work. `analyse.py` parses every file with Python's own parser and writes one JSON file per layer: packages and the imports between them, classes with their bases and typed fields, methods with the calls that resolve inside the repository, the commands parsed out of the argparse wiring, the test modules mapped to the classes they import, and ten pattern checks. `stream.py` follows the call tree from one method and writes the code on that path as one file. `delta.py` compares the two snapshots' method fingerprints and climbs the reverse call graph, including dynamic dispatch, to the commands and stories a change can reach. The stories are the one layer written by hand, from the CLI's help text; everything under them is derived, and the app says which is which.

Call resolution is static and conservative. `self.x()` resolves through the class and its bases; `self.field.x()` through the field's declared type, which is why typed fields matter; constructors by imported name; a call to a base class method is taken to reach its subclasses. What cannot be resolved is counted, not guessed. That is a floor on the graph, not a ceiling: the article says what a model would add on top of it.

## What is in it

one commit, read upwards

### The blast radius of a change, before anyone runs it

The text diff of the commit is 75 lines added and 7 removed in three files. The graph reads the same change at every altitude: one method in the transport class and six command handlers changed; no signature, field or class shape moved; a test module with six tests was added. Climbing the call graph from the changed methods reaches nine of the 72 commands and six of the eleven stories. The pattern across the layers, bodies moved and shapes still and a new assertion, is the shape of a fix; a refactor is its mirror image.

Commit 397be83 at every altitude, the fix-or-refactor reading, and the commit message beside it as evidence to check.

packages

### The architecture people draw, read from the code

Twelve packages and the 45 import relations between them, weighted by how many modules import. It is the whiteboard picture, except that nobody drew it and the two packages the commit touched are red. Every circle opens into the class graph beneath it, which has a different vocabulary: typed fields and base classes instead of imports.

The package graph. Arrow weight is the number of importing modules; red is touched by the commit.

method streams

### The code on one path, and only that code

The stream from `cmd_push` to depth five is 100 methods and 1,703 lines from 20 classes: 7.5 percent of the repository's method code, and the whole of what a reviewer of "publish a new vault" has to read. The clone stream is 32 methods and 469 lines. Both are written out in full as Markdown in the vault, in breadth-first order, with each method's source.

The two streams, with the push stream's 100 methods expanded by depth.

patterns

### The house rules, checked against the graph

Ten rules from the project's own CLAUDE.md and coding practice, each run as a query over the graph. No raw primitives in Type_Safe fields holds on all but 19 of 755 fields. No module-level functions has eleven exceptions in 427 modules. No static methods, immutable defaults only, nothing but imports in the CLI package's init file, and no init files under tests all hold. A mirrored test file per domain class is missing for 143 of 253. The ordering is itself a finding: the rules stated most firmly hold best.

The ten checks, their counts, and the nodes checked.

classes and tests

### A class is a card with its edges, including the tests that import it

Filter the 377 classes by name or package and open one: its typed fields, its methods, the classes it has fields of and the classes that have fields of it, its subclasses, and the test modules that import it. The tests view turns that around, per package: which classes no test imports, read from the imports without running anything.

The network package's classes, with one opened.

## What to connect next

The stories are hand-written; the next pass has a model propose them from the command help and the tests, and a person accept or correct each. The call graph stops at the repository's edge; the standard library and the dependencies are counted, not followed. The syntax-tree layer is fingerprinted but not yet diffed node by node. And this vault analyses one Python project with its own strong conventions; a second language is the test of whether the layers hold their shape. All of the scripts are in the vault, Apache-2.0 like the code they read.

## Read the article

[**Code review as a fractal semantic graph: source code is already one, and the review should read every layer of it**](../../../articles/code-review-as-a-fractal-semantic-graph.md). The case this vault demonstrates, with five figures, the prior art it builds on, the evidence on generated code, what does not exist yet, and a company for somebody to build.


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/code-review-graphs/index.html)*
