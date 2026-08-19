# The seven views, explained — Risk Graph Explorer

> A deep walk through each view of the risk graph explorer — the estate, context, role risk map, risk chains, the register, acceptance and what happens next — with screenshots of the live vault and the mechanism behind each, grounded in the author’s own walkthroughs.

*Source: <https://sgit.ai/demos/vaults/risk-graph-explorer/views/index.html> · site v0.2.36 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../../index.md) / [Vaults](../../index.md) / [Risk Graph Explorer](../index.md) / The seven views

# The seven views, explained

One set of answers, seen from seven altitudes. This page walks each view of the [Risk Graph Explorer](../index.md) with a screenshot of the live vault and an explanation grounded in [the author’s own walkthroughs](../videos/index.md) — because the reasoning behind a view is rarely visible in a picture of it.

**The spine, in one line.** An answer becomes a **fact**; facts combine into **risks**; risks are **assigned** to a role and **chain** upward to the corporate register; a role **accepts** what it holds; acceptance produces **what happens next**. Every view below is that same spine, cut at a different angle — which is why changing one answer moves all seven.

Screenshots are of the live vault under the **Exposed** preset, captured with the published read key. Open it yourself from [the vault page](../index.md) and follow along.

1 · The estate

### Every answer becomes a fact, and the graph is the evidence

This is where answering happens, and the first thing to notice is that **a "no" is still information**. From the walkthrough: *"if you don't have an agent, then we only have one piece of information here — but this is a fact."*

The questions walk a deliberate path: what the agent is, what data is in its reach, whether its output decides about a person, what it can do with that data (*cannot see it · reads it · reads and changes it*), whether it can change production, how it is stopped, who may stop it, how long stopping takes, whether stopping was ever tested, what it can reach if it misbehaves, whether it has outbound access, whether the damage is reversible, whether there is a written procedure, whether the actions could be reconstructed, and whose account it acts under.

Each answer lands as an `F-nn` fact chip, and the graph draws the relationships between them — amber for exposure, green for assurance, **ghosted for nobody has said either way**. That last one matters: an unanswered question is drawn as an absence rather than silently treated as a pass.

The estate: answers on the left, the fact graph they build on the right.

2 · Context

### The same technical answers, weighed against what is at stake

Context is the view that makes the app's core claim enforceable. The technical answers can be as alarming as you like; if nothing is behind them, little follows. The header carries the verdict in plain language — *decides about a person · in production · at stake* — and those three phrases are what turn a list of facts into a register worth reading.

This is the difference between a risk tool and a checklist: a checklist scores the agent, this weighs the agent *against the estate it runs in*.

Context: what is at stake, and where it runs, applied to the same answers.

3 · Role risk map

### The org chart, with risks flowing up it

The view the author calls *"crazy powerful"*, and the header states its invariant outright: **every risk is assigned to somebody, and every risk reaches the board**.

Read the counts under each role and you can see the two modes the walkthrough describes. The CISO shows `14 assigned · 14 through`; the CTO `4 assigned · 25 through`; the board simply `37 arrive here`. **Assigned** is what you personally hold. **Through** is what arrives because the risk graph says it must — *"he arrives because of the risk graph says so"*. The SRE holds a set; the platform owner inherits those and adds its own; the CTO inherits everything below and adds its own; the CEO connects the dots.

The consequence is the one worth quoting: *"no risk then becomes orphaned, because every risk will flow upwards, and that's super important."* An owner cannot be surprised at the top by something nobody carried up.

Role risk map: assigned vs through, with every path terminating at the board.

4 · Risk chains

### Risks that cause risks, and the ability to walk it backwards

The second graph, and a different question: not *who holds this* but *what produced it*. Columns are levels — inherent at the left, operational rising by causal depth, and the **corporate register pinned to the right, because that is where the question stops**.

Click any entry and it colours what produced it (**upstream**) and what it produces (**downstream**). The walkthrough uses it in both directions: *"if you go to 'led by' at the bottom, you arrive at the bottom of the risk; if you go 'leads to', you're navigating upwards."* So a corporate-level entry can be interrogated — *"why is it? It's because we have that one, and that one, and this one"* — until you reach the specific answers that caused it.

One detail that only an honest tool ships: **a dashed edge is a cycle, and the cycles are real**. Rather than hiding a loop that the model does not like, it draws it.

Risk chains: inherent to corporate, left to right, with upstream and downstream colouring.

5 · The register

### The familiar artefact — with its provenance attached

This is the output most organisations already recognise: a risk register. What is different is that every row carries where it came from. Per the walkthrough: *"for every risk that you have here, you can see who's assigned, who causes it, and who leads to, and how does it connect."*

A conventional register is a list of assertions someone typed. This one is a **projection of the graph** — which means it cannot contain a risk that nothing produced, and it cannot lose a risk that something did.

The register: the conventional artefact, generated rather than authored.

6 · Acceptance

### Nobody can accept on anybody else’s behalf

Acceptance is where the register stops being a document and becomes a decision. Each role holds what it holds and must accept it personally — and the author is explicit that this is where the value shows up: *"everybody that is going to accept it is going to push back."*

That pushback is the feature. The walkthrough contains a live example of the author disagreeing with his own tool — *"I actually don't agree with these risks… I don't buy that"* — and the point is what happens next: because every risk is fact-derived, the disagreement resolves into *which fact is wrong* rather than whose opinion is louder. *"The cool thing is that we start to have the evidence to show exactly why we are saying this."*

Acceptance: per role, per risk, with no delegation and no deny button.

7 · What happens next

### Decisions become incidents and projects

The last view closes the loop. Acceptance is not the end of a risk; it is a commitment that produces consequences — the things that will happen if the exposure materialises, and the work that would change it.

In the parent vault this is where a board refusal *funds a project* that flips the whole graph to the safer option. Here it is the same mechanism in miniature: the register does not merely describe a position, it names what follows from holding it.

What happens next: the consequences and the work that would change them.

## The same estate, at three settings

The presets are the fastest way to feel what the tool actually does. These are the **role risk map** for the same organisation under three different sets of answers — nothing about the org chart changed, only what is true about the agent.

typical

### A typical deployment

An agent is present and the estate is ordinary. Risks exist, they are held, and they reach the board — but the shape is contained.

Typical: risks present, shape contained.

governed

### The same estate, governed

Approvals, a tested stop, a named authority, bounded reach. From the walkthrough: *"you have the govern, we can see it's a much cleaner sort of flow of events."* The risks do not vanish — they arrive with far less weight, and by shorter paths.

**This is the argument the whole tool exists to make.** The register is not a verdict on whether you should run an agent; it is a picture of what you are carrying, which changes when the controls change.

Governed: same organisation, cleaner flow.

## Why this workflow is powerful

| What it does | Why it matters |
|---|---|
| **Answers are facts, and facts are cited** | Every risk traces to the specific answers that produced it. Disagreement becomes "which fact is wrong", not "whose judgement wins" |
| **No risk is orphaned** | Every risk is assigned and every path terminates at the board. Nothing can sit in a register held by nobody |
| **Assigned is distinguished from inherited** | A role sees what it personally holds and what merely passes through it — two very different conversations |
| **Acceptance is personal and cannot be delegated** | The register becomes a set of decisions with names on them, and the pushback that follows is the point rather than a failure |
| **Cycles are drawn, not hidden** | A model that shows its own loops is one you can argue with |
| **Nothing is at stake ⇒ a short register** | The output scales with exposure, which is what separates a register from a checklist |
| **It runs in a vault, in your browser** | No account, no upload, no network call. The answers you give about your estate never leave the page |

The last row is what makes the rest publishable. A tool that asks these questions is asking for an unusually candid description of your weakest controls — and this one can be handed to somebody as [a read key](../index.md) that carries the whole application, with nothing to send anywhere.


---

*[Site index for agents](../../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/risk-graph-explorer/views/index.html)*
