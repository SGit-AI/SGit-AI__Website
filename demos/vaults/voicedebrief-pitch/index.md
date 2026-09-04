# A three-minute pitch, delivered from a vault — a published vault

> The VoiceDebrief pitch to Founder Institute: a presenter app with timed slides, speaker notes and a countdown, shipped with the outline, script, research and exports it was built from — and the first vault here that asks for any permission at all.

*Source: <https://sgit.ai/demos/vaults/voicedebrief-pitch/index.html> · site v0.2.53 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../index.md) / VoiceDebrief pitch

# A three-minute pitch, delivered from a vault

The VoiceDebrief pitch to Founder Institute, 2 September 2026 — not a deck *about* a vault but a deck **presented from** one. Twelve slides and five backup slides, speaker notes, a three-minute countdown, PDF and PPTX exports, and every source the pitch was built from, all behind one read key.

**Open it yourself — the key is the whole credential.**
 Read key: `23cbc4c65c24cb23ef3efb78e34593391c6709f0106ea81799aa14fe97f4d211:95i2xqrd`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#23cbc4c65c24cb23ef3efb78e34593391c6709f0106ea81799aa14fe97f4d211%3A95i2xqrd) · From the CLI: `sgit clone 23cbc4c65c24cb23ef3efb78e34593391c6709f0106ea81799aa14fe97f4d211:95i2xqrd`
Published as a read key. The vault key is not published and never will be.

## See it live, here

[Open the vault in a new tab ↗](https://dev.vault.sgraph.ai/#23cbc4c65c24cb23ef3efb78e34593391c6709f0106ea81799aa14fe97f4d211%3A95i2xqrd)A presenter app — arrow keys, `N` notes, `T` countdown. Much better in its own tab.

## What is in it

the app

### A presenter, not a PDF

The vault opens straight into the deck: a slide index down the left with **per-slide target timings** (0:00, 0:15, 0:30 … 2:50), a live 3:00 countdown, speaker notes on `N`, Focus, Fullscreen, and a Materials view listing everything else in the vault.

Twelve slides run from *"The buried action"* and *"Audio is everywhere, meaning is not"* through the product, the market, the money and the ask. Five backup slides sit below them for Q&A — including one titled *"WhatsApp / ChatGPT already does this"*, which is the objection answered rather than avoided, and a 60-second version of the whole pitch.

The footer says where it is running from: *delivered from an encrypted SG/Vault*.

Slide 7 of 12, with the timing ladder and the backup Q&A set below it.

the working

### The sources ship with the pitch

What makes this a vault rather than an export is everything *underneath* the slides: the approved outline with its claims-to-keep-exact list, the spoken script per slide with timings, the fifteen-part pitch pack, the event and research notes, the original product screenshots, and the PDF and PPTX exports of the same twelve slides.

A deck emailed as a PDF is the conclusion with the working removed. Here the argument and the evidence for it travel as one object, and the deck itself is built from `deck/src/deck.template.html` by a script in the vault — so the slides are generated, not hand-maintained.

Every claim on a slide has a script line and a source behind it in the same vault.

## The first vault here that asks for anything

Every other vault on this site declares `"permissions": {}`. This one is the exception, and it is a useful one:

```
"permissions": { "downloads": true, "externalLinks": true }
```

It offers PDF and PPTX buttons, so it asks for **downloads**. It links out to the live product, so it asks for **external links**. And that is the entire request — **no filesystem access at all**, not read, not write, at any path.

That is the permission model doing exactly what it is for. The grant is short enough to read in one line, it maps one-to-one onto two things you can see in the interface, and anything not on that line is not available to the app no matter what its code tries. Compare it with the [Risk Graph Explorer](../risk-graph-explorer/index.md)'s empty grant and the difference is legible at a glance.

## Notes

**Audited before publishing.** No sgit credentials, no third-party API keys, no private keys.

**What becomes public with it,** all of it apparently by design, but worth naming: the **unit economics and commercial terms** (measured ≈£0.003 for a 42-second note, under £0.20 for three minutes, a £5 minimum top-up, and a 75/25 split on the key), the author's contact address on the closing slide, and the **three named judges** of the Founder Institute session with their affiliations. Those three appear as names, roles and affiliations only — there are no tactical notes about them anywhere in the vault.

**It is a pitch, so it is arguing a case.** Read the numbers as a founder's stated plan rather than as audited results; the vault's own ground truth for product claims is the live site at [voicedebrief.ai ↗](https://voicedebrief.ai), which it names as canonical over the deck.

[← All published vaults](../index.md)


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/voicedebrief-pitch/index.html)*
