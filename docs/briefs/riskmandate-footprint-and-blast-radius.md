# For RiskMandate.ai: footprint and blast radius, two additions to the Agent Behaviour Policy

> A vocabulary brief to the RiskMandate.ai team. The policy's four words, reach, mandate, gap and barriers, are written before the agent runs. Footprint is what the agent actually did, read afterwards from logs, vault history or a connector twin, and compared with the mandate it gives near misses and dormant rows. Blast radius is the measure on any row: what it would cost the business if used in full, with a reversibility flag. Five asks in order of usefulness, a schema sketch, and four questions, including which words are current.

*Source: <https://sgit.ai/docs/briefs/riskmandate-footprint-and-blast-radius.html> · site v0.7.38 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../index.md) / [Briefs](index.md) / RiskMandate: footprint and blast radius

# For RiskMandate.ai: footprint and blast radius, two additions to the Agent Behaviour Policy

**A vocabulary brief from the sgit.ai site team to the RiskMandate.ai team.** Status: under review by the founders; how to make it happen will be decided with the RiskMandate team. Written 2 October 2026.

The founder proposed two additions to the policy's vocabulary in conversation on 2 October, and the argument is written up in full in the article [Footprint and blast radius: what the agent actually did, and what it would have cost](../../articles/footprint-and-blast-radius.md). This brief carries the part that is yours: what to add to the policy, the schema, and the questions we could not settle from here. Read the article first; it is the reasoning. This is the ask.

## What to read first

- [The article](../../articles/footprint-and-blast-radius.md), including the lead figure, which is the proposal in one frame: the gap as a map, each row shaded by blast radius and marked if there is no way back.
- [Your own abp.html](https://riskmandate.ai/abp.html), which at the time of writing defines the four primitives as grant, mandate, delta and barrier. The founder tells us the current words are reach, mandate, gap and barriers. The article uses the current words and notes the older ones; see the first question below.
- [The connector twin article](../../articles/connector-twin-before-you-deploy-an-agent.md), because the twin is the footprint recorder for connectors, and [append lanes](../../api/append-lanes.md), because the lane record is the footprint recorder for vaults.
- [The earlier brief](riskmandate-partnership-risk-and-sgit-mapping.md), for the house rules on facts and claims, which apply here too: no "nobody has", no "the first"; say what we found and what we did.

## The two words

**Footprint.** The set of things the agent actually did in a period, read afterwards from the record: the connector's audit log, the model's tool-call log, the vault's commit history, the append lane's record, a connector twin's replay. The same kind of thing as reach and mandate, a list of rows, which is what makes the comparisons possible. Evidence, not a decision. Passive, no production access, accumulates over time.

**Blast radius.** Not a set; a measure that attaches to a row or a set of rows. What it would cost the business if that row were used in full, today. Defined over the reach, because whoever takes the agent over inherits its reach and ignores its mandate. Two readings: potential, from the reach, before the agent runs; realised, from the footprint, against the context at the time. Two axes: how much, on a short scale the owner fills in against the business, and whether there is a way back.

Derived terms the article uses and we would like the policy to share, so that the two sites do not fork:

- **Footprint in the gap**: a near miss. Resolves to a mandate edit (the mandate was incomplete) or a new boundary (the agent should not have gone there). The owner decides which.
- **Dormant mandate**: a mandate row the footprint never shows. Three causes: over-stated mandate, a check that never ran, or a shortfall the reach missed. Judged against the row's expected-use hint, below.
- **Footprint outside reach**: should be impossible; when it appears, the reach inventory is wrong.
- **Barrier hits**: attempts a boundary stopped. The footprint of the barriers.
- **The mandate as practised**: the footprint read alone, as a view, for an agent with no written policy yet. The mandate as written is the one the owner gave.

## The ask, in order of usefulness

1. **Footprint as a section of the policy.** A period, a source per row, and the four derived findings listed above. The section is produced from evidence, never hand-edited, in the same way the gap is derived and never hand-edited today.
2. **An expected-use hint on every mandate row.** One of `always`, `sometimes`, `rarely`, `hopefully-never`. Without it a dormant row cannot be told from a contingency that was never needed. "Escalate to a human when a payment is mentioned" is hopefully-never on a quiet month and a finding when fourteen payment threads passed.
3. **Blast radius on every row of the gap**, on a five-step scale the owner fills in against the business, with the reversibility flag beside it. The article uses `none`, `low`, `bad-day`, `serious`, `the-business`; use your own words if you have better ones, but keep it to five and keep it the owner's judgement, not the tool's. The blast radius of the gap as a whole is what the risk owner accepts; the policy should say it.
4. **The mandate as practised as a view** the tooling can produce from a footprint alone, for the elicitation conversation: "here is what your agent does; which of these did you mean, and which worries you?"
5. **A review cadence.** Monthly for a new agent, quarterly once the potential and realised blast radius readings have converged, because the footprint accumulates and the context moves.

## Schema sketch

Field names are suggestions. The shapes are what matter: the footprint is derived, every row names its source, and blast radius lives on the gap rows with the reversibility flag beside it.

```
{
  "mandate": [
    { "capability": "escalate when a payment is mentioned",
      "expected_use": "hopefully-never" }
  ],
  "gap": [
    { "capability": "send as the owner",
      "direction": "excess",
      "barrier": { "kind": "expectation", "enforced_by": "nobody" },
      "blast_radius": { "level": "the-business", "reversible": false,
                        "basis": "mail sent in the founder's name cannot be unsent",
                        "assessed_by": "owner", "assessed_on": "2026-10-02" } }
  ],
  "footprint": {
    "period": { "from": "2026-09-01", "to": "2026-09-30" },
    "sources": ["workspace-audit-log", "vault-history:<vault-id>", "connector-twin:gmail"],
    "rows": [
      { "capability": "send as the owner", "count": 3, "source": "workspace-audit-log",
        "finding": "footprint-in-gap", "first_seen": "2026-09-12", "last_seen": "2026-09-27" },
      { "capability": "escalate when a payment is mentioned", "count": 0,
        "finding": "dormant-mandate", "context": "14 payment threads in period" }
    ],
    "barrier_hits": [ { "capability": "delete messages permanently", "count": 2, "barrier": "boundary" } ]
  }
}
```

Values above are illustrative. No real footprint has been published yet.

## What sgit.ai will do

- **Read our own footprint.** Ten agents, six with a written policy, all in vaults, eight days of history and several hundred messages between them. We will read the footprint against the six policies and publish which rows were used, which were dormant, where the footprint went into the gap, and what each finding resolved into. Counts from the vaults' history; no contact named, no message quoted. We are building that now, and it is the second article.
- **Record footprints by default.** Append lanes already record every message with its token and time, and vault history records every file. We will document how to read both as a footprint with a read key only, so a reviewer never needs a write credential or production access.
- **Keep the vocabulary aligned.** Once you settle the words and the schema, we will update the article and the earlier pages on this site that still say grant and delta.

## Questions for you

1. **Which words are current?** abp.html says grant, mandate, delta, barrier. The founder says reach, mandate, gap, barriers. The article uses the second set and notes the first. If the site is mid-rename, say so and we will align; if both are meant to live, say which is canonical.
2. **Is blast radius a field on the gap row, or a separate table keyed by capability?** We lean to the field, because the person filling it in is looking at the gap row when they do it. A separate table makes the potential and realised readings easier to compare over time. Your call.
3. **Who assesses blast radius?** We say the owner, against the business, and the tool never guesses it. If you want a default to make the form faster, make it the top of the scale, so that the owner's job is to argue it down.
4. **How should the policy carry the footprint's sources?** A reviewer needs to know where each row came from to trust it. A short enum of source kinds plus a free identifier is our suggestion.

**House rules, restated.** The comparison of permissions granted with permissions used is not new: AWS IAM Access Analyzer, Google Cloud's role recommendations and Microsoft Entra's Permission Creep Index all do it, and the article cites them. What the policy adds is the mandate, the owner's intent, which a permission set does not carry, and which is what makes a near miss and a dormant mandate possible to name. Say that, and nothing larger.


---

*[Site index for agents](../../llms.txt) · [HTML version](https://sgit.ai/docs/briefs/riskmandate-footprint-and-blast-radius.html)*
