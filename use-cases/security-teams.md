# Findings about your own weaknesses — sgit use cases

> Pentest and vulnerability findings with history, diffs and multi-person workflow, in a store that cannot read them — plus the key-hygiene rule we learned the hard way.

*Source: <https://sgit.ai/use-cases/security-teams.html> · site v0.2.25 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Use cases](index.md) / Security teams

# Findings about your own weaknesses

Pentest output is a map of how to get in. It needs history, diffs and several people — and it is the last thing to hand to a SaaS you don't control.

## The problem

Assessment work produces exactly the document an attacker would most like to have: what is exposed, how to reach it, what has not been fixed yet, and which excuse each owner gave. It is also work that genuinely needs version control — findings get re-tested, severities change, remediation gets tracked across months, and several people edit the same report.

So it goes into a ticketing system or a shared repo, because those are the tools that do the workflow. Both are readable by the provider, and both are now a single place holding the complete attack path for the organisation. That is a concentration of risk that a security team, of all teams, can see clearly.

## What sgit does about it

The findings live in a vault: versioned, diffable, multi-person, and ciphertext everywhere but on the machines of the people working on them. The host is a key-value store for opaque ids; compromising it yields encrypted objects and traffic timing.

It also gives you a defensible answer to the question that follows an incident — "where was this stored, and who could read it?" — that does not depend on a vendor's access-control configuration being correct on the day.

## The recipe

**A vault per engagement or per client**, with the report and the raw evidence separated so you can share one without the other:

```
$ sgit create acme-pentest-2026q3
$ mkdir report evidence retest && sgit commit -m "structure" && sgit push
```

**Re-test cycles as commits**, so severity changes are a diff rather than a claim:

```
$ sgit commit -m "retest: SQLi in /search fixed, XSS in /profile still open"
$ sgit history log --oneline
$ sgit history diff --commit <initial-report> --files-only
```

**Deliver read-only** to the client, keeping the write side entirely on your team:

```
$ sgit dev derive-keys '<vault-key>'
$ sgit clone --read-key <read-key> <vault-id> report   # what the client runs
```

**One rule, learned the hard way:** never let the vault key reach a tracked file, a CI variable, or a chat message. Put a check in your pipeline that greps for it, and make that check read the secret from somewhere ignored rather than hardcoding it. That is not hypothetical advice — it is the exact fix from [our own incident](../case-studies/exposed-vault-key.md).

## Evidence status

PARTIAL — adjacent evidence only

We have not published a pentest firm running this. What we can point at is the closest thing we own: this project's [exposed-key incident](../case-studies/exposed-vault-key.md) — a real key leak, in a public commit, with the detection gap, the rekey, the measured blast radius (336 objects out, 90 in, zero overlap) and the structural fix written up rather than quietly patched.

That write-up is the artefact a security team would actually judge us on, so it is on the site rather than in a drawer. If you run assessment work on sgit, the failure modes you hit are the ones we want to hear about.

## Brief for an agent

Paste this into an agent that has the [sgit skill](../skills/index.md) installed, or point it at the markdown directly.

```
# everything on this site is readable as markdown — no HTML parsing needed
$ curl -s https://sgit.ai/use-cases/security-teams.md
$ curl -s https://sgit.ai/llms.txt          # the index of everything
```

> Read https://sgit.ai/use-cases/security-teams.md and https://sgit.ai/docs/agents.md. Then set up an assessment vault for this project: create the vault, structure the folders as described, commit and push, and report the vault key back to me once — I will store it. Do not write the key to any file in the repository. Also add a pre-push check that fails if the vault key appears in any tracked file, reading the secret from a gitignored path rather than hardcoding it.

That last sentence matters. We have a [write-up of the day we got it wrong](../case-studies/exposed-vault-key.md).

## Related

- [If a vault key is exposed](../case-studies/exposed-vault-key.md) — the runbook and the case study
- [Security model](../security/index.md) — the crypto stack and the honest side channels
- [Self-hosting](../deploy/index.md) — when the storage layer has to be yours too

[← Professional services](professional-services.md)[Health & regulated →](health-regulated.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/use-cases/security-teams.html)*
