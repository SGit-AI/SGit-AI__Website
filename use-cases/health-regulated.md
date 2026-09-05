# Data that changes what is permissible — sgit use cases

> What client-side encryption does and does not change for regulated data, stated precisely and without compliance claims.

*Source: <https://sgit.ai/use-cases/health-regulated.html> · site v0.2.54 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Use cases](index.md) / Health & regulated

# Data that changes what is permissible

When the host provably cannot read the content, the conversation stops being about the provider's access controls — because there is nothing for them to control access to.

**Read this first.** sgit holds no compliance certification of any kind — no HIPAA attestation, no ISO 27001, no SOC 2, no GDPR adequacy finding. Nothing on this page is legal or regulatory advice, and client-side encryption does not by itself make a processing activity lawful. What follows is a description of a technical property and what it does and does not change. Your compliance function decides the rest.

## The problem

Regulated data drags its rules with it. The moment a document is stored somewhere a third party can read, that third party is in scope: they become a processor, they need an agreement, their jurisdiction matters, their breach becomes your notification, and their sub-processors become your problem too. Most of the effort in these projects is not securing the data — it is the paperwork proving who could have seen it.

And the work itself still needs versions and collaboration, which is why it so often ends up in a general-purpose tool with a data-processing addendum stapled on.

## What the property actually changes

Content is encrypted before it leaves the client; the store holds ciphertext under opaque ids and never receives a key. That moves specific arguments, and it is worth being exact about which:

| Question | What changes |
|---|---|
| Can the host read the content? | No — not with a warrant, a rogue administrator, or a breach. This is the strong claim, and it is structural rather than procedural. |
| What does the host still learn? | The vault id, the size of each object, and request timing. Sizes and timing are a real if narrow side channel — see the [security page](../security/index.md). |
| Does this remove the processor relationship? | **Not automatically.** Storing ciphertext may still be processing, depending on the regime and on who holds keys. Ask your counsel; do not take a vendor's word for it, including ours. |
| Does it help with access logging and minimisation? | Partly: a vault is a natural boundary, and read access is a key rather than an account, which makes "who could read this" a shorter list. |
| Does it help with retention and deletion? | Partly, and awkwardly: history keeps old ciphertext until pruned, so "delete" needs thought. See [limitations](../docs/limitations.md). |

## The recipe

**Scope one vault to one purpose.** The vault is the access boundary, so make it match the lawful basis for the data in it — not the team, not the project folder.

```
$ sgit create study-1234-analysis
$ sgit commit -m "structure" && sgit push
```

**Key management is the whole control.** There is no reset and no recovery: the key is the access control, so it has to be managed like one — in a password manager or an HSM-backed store, with a named owner and a documented rotation path.

```
$ sgit vault backup --include-key     # archive and key stored separately
$ sgit vault rekey                          # rotation — see the exposed-key runbook
```

**Self-host if the storage layer is itself in scope.** The [deployment guidance](../deploy/index.md) covers Docker, AWS, GCP and a static host — and is itself served from an encrypted vault, which is a small demonstration of the property.

## A worked example you can open right now

The abstract version of this page is "the host cannot read it". The concrete version is a vault you can open in your browser in the next ten seconds: [**the Supplement Stack vault**](../demos/vaults/supplement-stack/index.md) — a real, patient-held health record, published with a read key.

It is worth reading because it answers the questions this page raises in the specific rather than the general:

| The question | How that vault answers it |
|---|---|
| Who holds the data? | The patient. The vault is theirs; the write key never leaves them |
| How is it shared with a clinician? | By handing over a **read key** — no account on anyone's platform, no PDF emailed into permanent circulation. The reader sees everything and can change nothing |
| What stops the app doing more than it should? | `app.json` grants write over `adherence/` and nothing else. The record-keeping app cannot alter the record it reports on — least authority, declared in the vault |
| Where does AI fit without being dangerous? | A model does the fuzzy work (reading amounts off a label photograph, each value traceable back to its image); **code** does the exact work (summing them). Every fuzzy step is checkable against its source |
| Does it give medical advice? | No — and that is designed in. It computes the total nobody else computes and produces a *briefing for somebody qualified*, with the open questions listed. It never concludes |
| Whose reference values? | UK RNIs and EFSA upper limits, named and dated, explicitly not US Daily Values — because comparing a UK intake against US references without saying so is a quiet error |

It is a demonstration rather than a deployed clinical system, and it makes no compliance claim of any kind — but every mechanism above is running, readable, and open to inspection with the key on its page.

## Evidence status

PATTERN — and the most caveated page here

No published healthcare or regulated-industry deployment, no certification, and no audit of the implementation by a third party. What exists is: standard primitives (AES-256-GCM, PBKDF2-SHA256 at 600k, HKDF) with no custom cryptography, ~4,000 tests, byte-for-byte test vectors against the browser's Web Crypto, two independent implementations of the same wire format, and a [published threat model](../security/index.md) that names its own side channels.

That is evidence of engineering care. It is not evidence of compliance, and we are not going to blur the two.

## Brief for an agent

Paste this into an agent that has the [sgit skill](../skills/index.md) installed, or point it at the markdown directly.

```
# everything on this site is readable as markdown — no HTML parsing needed
$ curl -s https://sgit.ai/use-cases/health-regulated.md
$ curl -s https://sgit.ai/llms.txt          # the index of everything
```

> Read https://sgit.ai/use-cases/health-regulated.md and https://sgit.ai/docs/agents.md. Then set up a scoped vault for regulated data for this project: create the vault, structure the folders as described, commit and push, and report the vault key back to me once — I will store it. Do not write the key to any file in the repository. Do not claim any compliance property in what you write; describe only the technical behaviour.

That last sentence matters. We have a [write-up of the day we got it wrong](../case-studies/exposed-vault-key.md).

## Related

- [Security model](../security/index.md) — including what the server still observes
- [When NOT to use sgit](../docs/limitations.md) — retention, deletion and the key-loss trade-off
- [Run your own server](../deploy/index.md) — when the storage layer must be in your own boundary

[← Security teams](security-teams.md)[All use cases →](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/use-cases/health-regulated.html)*
