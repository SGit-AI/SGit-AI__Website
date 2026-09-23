# An application for a job, as a vault, interim CISO pack

> A candidate pack delivered as an encrypted vault instead of a CV on an email: three routes for three readers, four documents each in PDF, Word, Markdown and JSON, a disclosed redaction, and a client named nowhere, with the pre-publication privacy audit stated in full.

*Source: <https://sgit.ai/demos/vaults/interim-ciso-pack/index.html> · site v0.5.9 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../index.md) / Interim CISO application pack

# An application for a job, as a vault

A candidate pack for an interim CISO role, delivered as an encrypted vault instead of a CV attached to an email. **Three routes through one artefact** (the recruiter, the hiring company, and anyone curious) over four documents that each exist as PDF, Word, Markdown *and* JSON. The claim it makes about how the candidate works is the same claim the artefact demonstrates by existing.

**Open it yourself. The key is the whole credential.**
 Read key: `sgit_public_read_699401f6cb3bdb1d6e19bfa690d8e0006a5379070ff320b5a8ae2fc21968f5c9:8brojsem`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_public_read_699401f6cb3bdb1d6e19bfa690d8e0006a5379070ff320b5a8ae2fc21968f5c9%3A8brojsem) · From the CLI: `sgit clone sgit_public_read_699401f6cb3bdb1d6e19bfa690d8e0006a5379070ff320b5a8ae2fc21968f5c9:8brojsem`
Submitted as a read key and published unchanged. **The hiring company is not named anywhere in the vault**: see the audit below.

## See it live, here

[Open the vault in a new tab ↗](https://dev.vault.sgraph.ai/#sgit_public_read_699401f6cb3bdb1d6e19bfa690d8e0006a5379070ff320b5a8ae2fc21968f5c9%3A8brojsem)The document viewer needs room, better in its own tab than in the frame.

One artefact, three declared readers, and a front page that tells you which one you are.

## The idea worth stealing: the pack is the evidence

Every candidate pack asserts something about how the candidate works. This one is constructed so that the assertion and the demonstration are the same object. Its own front page says it plainly:

> “This pack is itself an example of how he works: a voice memo became a brief, a team of AI agents researched and built the material, and it is delivered as an encrypted, versioned vault.”

A claim to work with agents, made in a document that agents built. A claim about handling sensitive material, made in an artefact whose server cannot read it. The reviewer does not have to believe the claim, the thing in their hands is the test of it.

## Three routes, because three people read a CV for different reasons

The interesting structural choice: rather than one document that compromises between audiences, the pack splits at the front door and lets each route stand alone.

| Route | For | What is behind it |
|---|---|---|
| **Recruiter** | The person putting the candidate forward | An embedded document viewer, four documents in four formats each, **a submission summary to copy**, key facts, and answers to screening questions, the things a recruiter has to paste into a form |
| **Company** | The hiring organisation | The mandate, the shape of the function, the regulatory calendar, a four-stage plan, a typical week, **what to settle before signing**, a conflict disclosure and a section titled *honest tensions* |
| **About** | Anyone | A skills map, a career timeline, thirteen recommendations, the agentic team and its rules, and how the pack was built |

A recruiter needs text to paste; a hiring manager needs an argument; a curious reader needs context. Those are genuinely different documents, and the vault holds all three without any of them being a compromise.

The company route runs to eleven sections, and two of them are *Before signing* and *Tensions*.

## Four formats, and the fourth is the interesting one

Each of the four documents (short CV, full CV, the one-page case, the recommendations) exists as **PDF, Word, Markdown and JSON**, generated from one source by the pack's own build.

PDF is for the human. Word is because recruiters still ask for it. Markdown is for whoever pastes it somewhere. **JSON is the one that matters**: a CV as structured data, so a machine reading the pack gets fields rather than a page it has to parse. It is the same instinct as this site's [`llms.txt`](../../../llms.txt), publish the thing, and publish it again in the shape a machine wants.

Page counts and byte sizes are computed at build time and recorded with SHA-256 hashes, so the sidebar cannot describe a file it did not produce.

## The build refuses what the authoring contract refuses

The pack's own pipeline fails if the page declares a vault resource with `<link href>`, `<script src>` or `<img src>`, uses `fetch()`, writes `location.hash`, references a missing file, or contains a JavaScript syntax error. That is [the vault authoring contract](../../../docs/vault/vault-apps.md) enforced by the artefact's own build rather than discovered after a push, and the last of those checks is the one that [caught a shipped bug on riskmandate.ai](../synthetic-users-riskmandate/index.md) the day before.

The viewer degrades honestly too: inside a vault host it loads PDF.js through `sg.loadJs` and reads bytes through `sg.vfs.read`, with `isEvalSupported: false`; where PDF.js cannot run, it falls back to page images rendered at build time. `app.json` asks for exactly one permission, `downloads`, so files save without a prompt each time, and the app never writes to the vault.

## What it refuses to do, which is the part to copy

- **It does not name the client.** The role is described as an interim CISO position at a FTSE 250 company and nothing further; one line in the strategy brief states outright that *“nothing here characterises the client, which is not named.”*
- **It discloses its own redaction rather than hiding it.** The strategy brief carries an editor's note saying which sections were removed for publication (the off-payroll analysis, pricing, and two contract items on status and rate) and that nothing else changed. The brief keeps its original date.
- **It states its limits inside the argument.** The same note records that this is not legal or tax advice, that several paragraph numbers could not be read at the primary source and are marked, that one tribunal outcome comes from commentary rather than the decision, and that no reported case was found on one question, *“reported as a gap rather than as comfort.”*
- **It includes a conflict disclosure and a section called *Tensions*** in the material written for the people deciding whether to hire.
- **The recommendations are dated and sourced.** Thirteen of them, each carrying its 2019 job title and relationship, attributed to the candidate's own 2019 deck (CC BY-SA), which ships in the vault's `archive/` so the source can be checked rather than taken on trust.

## The pre-publication audit

Run against a full clone with the published read key, before this page existed. The submitter's position was that the vault holds no sensitive data, does not identify the company, and reuses material that was already public. **Checked, and it holds**: with one point worth a reader knowing:

| Checked | Result |
|---|---|
| Client identification | **Not named.** Described only as FTSE 250, with regulatory applicability raised as open questions rather than answered |
| Day rates, IR35, pricing | **Absent.** The only monetary figures in the vault are statutory penalty amounts. The removal is disclosed in the brief itself |
| Contact details | **None**: no phone, no address. One email address, the candidate's own long-public OWASP one |
| Credentials and secrets | **None.** No keys, tokens or credential-shaped strings |
| Named third parties | **Thirteen**, in the recommendations, with their 2019 job titles and employers. Public twice over, LinkedIn recommendations, republished in the candidate's own CC BY-SA 2019 deck, which is in the vault. Labelled `title_2019` throughout, with the provenance stated |
| Read key | Verified with an all-zeros negative control against the same vault id: the real key produced 56 files, the control an empty directory |

This page quotes the candidate and the pack's own framing; it does not reproduce the individual recommendations, which stay where their provenance is stated.

## What to take from it

- **Split at the front door, not inside the document.** If three people read a thing for three reasons, three routes beat one compromise.
- **Ship the machine-readable copy beside the human one.** A CV as JSON costs one build step and changes what a machine can do with it.
- **Put the redaction note in the artefact.** A document that says what was removed is more trustworthy than one that reads as though nothing was.
- **Let the artefact be the proof of the claim it makes.** This is the most portable idea here and it is not about hiring.

## Shape

| **Vault** | `8brojsem` · 56 files · 17 MB |
|---|---|
| **App** | `index.html` with CSS, JS and a fallback copy of `content.json` inlined |
| **Permissions** | `downloads: true`, and nothing else. No writes |
| **Documents** | Four, each as PDF, Word, Markdown and JSON, with sizes and SHA-256 hashes recorded at build time |
| **Licence** | Content CC BY 4.0; the 2019 decks and recommendation slides CC BY-SA as originally published; PDF.js Apache-2.0 |

Published as row #29. [← All published vaults](../index.md) · [The publishing method](../publishing.md)


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/interim-ciso-pack/index.html)*
