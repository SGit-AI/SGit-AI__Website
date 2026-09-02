# AIUC-1, as a graph you can cite — a published vault

> An unofficial, derivative machine-readable catalog of the public AIUC-1 agent standard: 53 controls, 144 requirements, 1,126 crosswalks and 1,238 nodes, where every field names the page or commit it was read from with the SHA-256 of the retrieved bytes. Not approved or endorsed by AIUC.

*Source: <https://sgit.ai/demos/vaults/aiuc-1-graph/index.html> · site v0.2.51 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../index.md) / AIUC-1 graph

# AIUC-1, as a graph you can cite

**Unofficial and derivative. Read this first.** This vault is a machine-readable catalog of the public AIUC-1 agent standard, built by the sgit.ai graph estate. In its own words: *"It is **not** approved, certified, endorsed or reviewed by AIUC. It is **not** an official AIUC API, export or data feed. It is **not** a substitute for the standard."* The canonical sources are [aiuc-1.com ↗](https://www.aiuc-1.com/) and the [official changelog repository ↗](https://github.com/aiunderwriting/AIUC-1-Changelog). **Where anything here disagrees with those, those are right and this is wrong.** It makes no compliance, certification, underwriting, insurance, legal or security claim about anybody, and cannot be used to make one.

A standard read from its own pages, normalised, cross-checked against its official changelog repository, and decomposed into one graph — where every field points back at the page or commit it came from, with the SHA-256 of the retrieved bytes and the time they were retrieved. **53 controls, 144 requirements, 1,126 crosswalks, 1,238 nodes and 3,526 edges**, over five releases.

[Open the vault in a new tab ↗](https://dev.vault.sgraph.ai/#sgit_private_read_4435037d6936ef6986d0646ff23ed3affc46eb74bf8a65ca1f729fd5d3a4ae00%3Ahq21tlqu)It is a full application — it has a lot more room in its own tab than in the frame below.

**Open it yourself — the key is the whole credential.**
 Read key: `sgit_private_read_4435037d6936ef6986d0646ff23ed3affc46eb74bf8a65ca1f729fd5d3a4ae00:hq21tlqu`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_private_read_4435037d6936ef6986d0646ff23ed3affc46eb74bf8a65ca1f729fd5d3a4ae00%3Ahq21tlqu) · From the CLI: `sgit clone sgit_private_read_4435037d6936ef6986d0646ff23ed3affc46eb74bf8a65ca1f729fd5d3a4ae00:hq21tlqu`
Published as a read key. The vault key is not published and never will be.

## See it live, here

[Open the vault in a new tab ↗](https://dev.vault.sgraph.ai/#sgit_private_read_4435037d6936ef6986d0646ff23ed3affc46eb74bf8a65ca1f729fd5d3a4ae00%3Ahq21tlqu)Or read it in the frame below.

## What is in it

a control, in edges

### The graph is the point, not the list

Open any control and the app draws what it *is* in terms of its relationships: `has_requirement`, `maps_to`, `evidenced_by`, `includes`, `applies_to_capability`, `tagged`. Control A001 alone resolves to 1 domain, 3 requirements, 20 crosswalks, 4 sources, 4 releases, 1 capability and 3 keywords.

That is [graphs.sgit.ai](../../../network/graphs.md)'s argument applied to a compliance standard: a verb-per-edge vocabulary rather than a bag of properties, so *"what does this control map to"* is a traversal instead of a search.

Every control carries its official page URL, so a reader can leave for the source in one click.

The disclaimer sits above every view, in the app itself.

the evidence

### Eighty-two pages, each with the hash of what was received

The Evidence tab is one row per captured page: the URL, the HTTP status, the retrieval timestamp, **the SHA-256 of the bytes**, and the path to the retained gzipped snapshot inside the vault. As it puts it: *"any claim above can be checked against the bytes it was read from rather than against this catalog's word for it."*

It also publishes **where its two sources disagree** — five reconciliation findings where the website and the official repository differ on guidance formatting or bullet order, each classified as presentation rather than meaning. And then the line that makes the whole thing trustworthy:

Validation, reconciliation and drift, each with its own counter.

**"None of these is resolved here. Resolving one means choosing a source, and that is not this build's to choose."**

That is the discipline the rest of the catalog rests on. A derived artefact that silently picks a winner when its sources conflict has stopped being derived and started being an opinion — and the reader cannot tell which. This one preserves both readings, classifies the difference, and stops a release being marked `validated` if a difference changes meaning.

## Five releases, one of them deliberately unbuilt

The catalog covers 2025-10-01, 2026-01-15, 2026-04-15 and 2026-07-15. A fifth — 2025-07-22 — is **named by AIUC but carries no commit**, so it could not be built, and it is recorded as unbuilt rather than quietly dropped. That is the same instinct as listing an unpublished site in [the network directory](../../../network/index.md) instead of omitting it: an absence somebody can see is worth more than a tidy list.

Alongside the releases sit **194 derived change events** from release-to-release differences, kept separate from the **104 change rows AIUC publishes itself** — derived and official never mixed.

## How it was collected

The source policy is unusually explicit, and worth quoting because most scrapers do not write one:

- An identifying user agent naming the build and where to complain.
- **At most one request per second** per host.
- `robots.txt` fetched before any page. It returned 404 at capture time, so there were no directives — and *the manifest records that observation verbatim rather than the conclusion alone*.
- No authentication, no private endpoints, no slug guessing: **every page fetched was linked from a page already fetched**.

## Notes

**It asks for nothing.** `app.json` declares `"permissions": {}` with `present: true`.

**Audited before publishing.** No sgit credentials, no third-party API keys, no private keys.

**One open question, which the vault raises itself and we are not hiding.** Its `NOTICE.md` and `docs/source-policy.md` — both of which are files **inside the vault**, readable by opening it above rather than in any GitHub repository — record that **reuse rights for the full AIUC-1 control text have not been confirmed with AIUC**, and that anyone republishing the catalog publicly should confirm them first. Publishing this read key is exactly that kind of republication. It is here at the author's decision, with the vault's own disclaimers reproduced above rather than summarised away. The vault also states the remedy plainly: *"If you are AIUC and want something here changed or removed, the fastest route is the sgit.ai project behind graphs.sgit.ai. Removal will be honoured."* That undertaking is repeated here and applies to this page too.

[Open the vault in a new tab ↗](https://dev.vault.sgraph.ai/#sgit_private_read_4435037d6936ef6986d0646ff23ed3affc46eb74bf8a65ca1f729fd5d3a4ae00%3Ahq21tlqu)

[← All published vaults](../index.md)


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/aiuc-1-graph/index.html)*
