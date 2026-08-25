# SG/Payments Brief Pack — a published vault

> A ten-document briefing pack for a payments and metering platform, published as a vault while every word of it is still PROPOSED — the status is stamped on the pack index, not buried in a footnote.

*Source: <https://sgit.ai/demos/vaults/payments-brief-pack/index.html> · site v0.2.43 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../index.md) / SG/Payments Brief Pack

# SG/Payments Brief Pack

A briefing pack for a team that has not started building yet. Ten documents, a stated reading order, and a status pill that says **PROPOSED** — because nothing in the pack exists as code. It is the clearest example on the site of a vault used as the **unit of handover**: one credential moves the whole pack, its reading order and its provenance together.

**Open it yourself — the key is the whole credential.**
 Read key: `sgit_rk1_cd1987b87f719c2ff6da51128200665312afaeeadcbf7a1a20f870f03f9959f8:o3m0sz3q`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_rk1_cd1987b87f719c2ff6da51128200665312afaeeadcbf7a1a20f870f03f9959f8%3Ao3m0sz3q) · From the CLI: `sgit clone sgit_rk1_cd1987b87f719c2ff6da51128200665312afaeeadcbf7a1a20f870f03f9959f8:o3m0sz3q`
Published deliberately, and **derived** one-way from a vault key that is not published and never will be.

## See it live, here

Both surfaces open automatically below. You can also [**open the app in its own window ↗**](https://dev.vault.sgraph.ai/#sgit_rk1_cd1987b87f719c2ff6da51128200665312afaeeadcbf7a1a20f870f03f9959f8%3Ao3m0sz3q).

## What is in it

the pack

### A reading order, and a status that refuses to flatter itself

The index opens with **Status: PROPOSED — nothing in this pack exists as code yet**, then a numbered reading order through ten documents: overview and principles, platform grounding, a review of three human architecture briefs, target architecture, gateway spec, ledger and credentials, vault integration, build plan, open decisions, and a pattern audit.

The separation that makes it useful is between **01 · Platform Grounding — What Exists Today (code-verified)** and everything downstream of it. One document is what the code does; the rest is what somebody proposes to build on top. The pack keeps them apart on purpose.

The footer of the app states its own delivery mechanism: *rendered from an encrypted SG/Vault — the link-holder holds the key; the server sees only ciphertext.*

The pack index: PROPOSED status, the reading order, and the target named up front.

the grant

### Nothing requested, nothing granted

`app.json` declares `"permissions": {}`. A pack of documents needs no filesystem access, so it asks for none — the same posture as the [Risk Graph Explorer](../risk-graph-explorer/index.md).

It is worth seeing on a document pack precisely because nothing here is dangerous. The habit is what generalises: the grant is written down, it is short enough to read, and it is visible to anyone holding the read key.

The vault browser: the pack as files, and the empty permission grant.

## Notes

**Why this one is interesting beyond payments.** The grounding document records the substrate in terms this site documents elsewhere: PBKDF2 at 600k iterations deriving independent read and write keys, ref file *locations* themselves HMAC-derived from the read key, and the server storing only `SHA-256(write_key)` while reads stay tokenless. It is an outside-in description of the same design the [API pages](../../../api/index.md) describe from the inside.

[← All published vaults](../index.md)


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/payments-brief-pack/index.html)*
