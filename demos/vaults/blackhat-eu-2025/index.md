# AI vs. AI — Black Hat Europe 2025 — a published vault

> A conference keynote shipped as a vault: the deck as presented, six PDF exports, eight research papers and the full source history of the slide system that renders it — all behind one read key, with the slide content as data the app reads at load time.

*Source: <https://sgit.ai/demos/vaults/blackhat-eu-2025/index.html> · site v0.2.54 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../index.md) / Black Hat EU 2025

# AI vs. AI — Black Hat Europe 2025

A conference keynote shipped as a vault: the deck that was presented, the six PDF exports it went through, the eight research papers it was built from, and the entire source history of the slide system that renders it — behind one read key. Opening the vault launches the deck full-screen.

**Open it yourself — the key is the whole credential.**
 Read key: `sgit_rk1_147fa50d3c491aeea3e700d60ef21ea2897884e263700d95765dc8f624dc59ac:k1izvg7e`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_rk1_147fa50d3c491aeea3e700d60ef21ea2897884e263700d95765dc8f624dc59ac%3Ak1izvg7e) · From the CLI: `sgit clone sgit_rk1_147fa50d3c491aeea3e700d60ef21ea2897884e263700d95765dc8f624dc59ac:k1izvg7e`
Published deliberately, and **derived** one-way from a vault key that is not published and never will be.

## See it live, here

The deck opens automatically below and is driven with the arrow keys — `→` next, `←` previous, `F` for fullscreen. You can also [**open it in its own window ↗**](https://dev.vault.sgraph.ai/#sgit_rk1_147fa50d3c491aeea3e700d60ef21ea2897884e263700d95765dc8f624dc59ac%3Ak1izvg7e).

## The talk

**AI vs. AI: Building Resilient Enterprises in the Age of Autonomous Threats** — Dinis Cruz, AI Security Summit, Black Hat Europe 2025, ExCeL London, 9 December 2025. Twenty-six slides.

the setup

### Four pillars, and an admission

The argument opens by conceding the ground rather than claiming it. **Security's four pillars — all broken**, followed immediately by the more uncomfortable slide: **we've been getting away with it.**

The evidence there is four publicly documented outages, none of them attacks: a timing bug that wiped out a global database, a config inconsistency that propagated silently and then detonated worldwide, a routine config change that halted traffic, and a faulty update that bricked 8.5 million Windows machines.

The turn is one line at the bottom of the slide: *"These weren't sophisticated attacks — they were minor glitches that cascaded. Now imagine if they were deliberate, coordinated attacks."*

Slide 6 of 26. Four cascading failures, and the question underneath them.

the threat model

### The new insiders

The middle of the deck reframes agents as an insider-threat problem and then draws the comparison directly: human insiders have **natural limitations on skill and time** and rarely act at machine speed; AI agents have neither constraint.

From there it separates **three categories of AI-driven threat** and asks why enterprises are not ready — arriving at *fragile by default* as the diagnosis rather than a lack of tooling.

The insider comparison the rest of the talk builds on.

the answer

### The defender's edge

The second half is constructive, and several of its slides describe things this site now demonstrates: **assume compromise, contain blast radius**, **version control everything**, **identity graphs for least privilege at scale**, and **knowledge graphs** as the mechanism.

It also argues for funding non-functional requirements at unprecedented scale, treats *vibe coding* as the new spreadsheets — a governance problem rather than a fad — and ends on **don't become the department of 'no'**.

Those threads have their own homes now: [risks](../../../network/index.md#risk-governance) and [nfrs](../../../network/index.md#risk-governance), [graphs](../../../network/graphs.md), [nhi](../../../network/nhi.md) for agent identity, and [coding](../../../network/index.md#agents-ai).

The concession the talk opens with, before any solution is offered.

## Why it is a good vault

A deck emailed as a PDF is a snapshot with its working removed. This one ships the whole chain in a single object, addressed by one credential:

| Path | What it is |
|---|---|
| `index.html` | The deck as a self-contained vault app — 26 slides, ~976 KB |
| `deck/blackhat-eu-2025.json` | The slide content. Edit this, commit, push — the app reads it through the vault bridge at load time, so a content change needs no rebuild |
| `pdf/` | Six exports, v0.1.1 through v0.2.0 — the deck as it looked at each stage |
| `research/` | Eight background papers the talk was built from, Parts 1 through 7 |
| `source/v0/v0.1/` | The slide system itself at ten versions, v0.1.0 to v0.1.9, unmodified |

The separation worth noticing is the third row. **Content is data, not markup.** The deck is a JSON file the app reads at load time, so changing a slide is a commit rather than a rebuild — which is also why the vault can carry ten versions of the renderer beside one deck without either owning the other.

The whole chain in one tree — and `"permissions": {}` behind it.

## Notes

**It asks for nothing.** `app.json` declares `"permissions": {}` with `present: true`. A deck needs no filesystem access, so it requests none — the same posture as the [Risk Graph Explorer](../risk-graph-explorer/index.md).

**Audited before publishing.** No sgit credentials, no third-party API keys, no private keys, no email addresses, and no external company or client named. The organisations that do appear — AWS, Azure, Cloudflare, CrowdStrike — are cited for their publicly documented outages, which is what the slide is about.

**The conference branding is the real thing.** The deck uses Black Hat Europe's official speaker template, because it is a talk that was given there. It is published here as the speaker's own material, not as anything endorsed by or affiliated with Black Hat.

**The source is public too.** This vault republishes material that already sits in the open at [the-cyber-boardroom/Presentation__BlackHat-EU__Dec-2025 ↗](https://github.com/the-cyber-boardroom/Presentation__BlackHat-EU__Dec-2025), so nothing here is first exposed by the vault — this is a second, addressable copy that travels as one object.

[← All published vaults](../index.md)


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/blackhat-eu-2025/index.html)*
