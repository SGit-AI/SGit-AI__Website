# Threat-sized security, who are you actually protecting against? A teaching vault for founders, sgit.ai

> A six-tier ladder of attackers, from your own mistakes to states, built on NIST SP 800-30, the NCSC's commodity, targeted and elevated threats, and MITRE ATT&CK; eight fictional startups each with assets, an attack tree with a technique on every branch, and the line it should draw; an air-gapped, nothing-installed Mac mini compared with an isolated one, tier by tier; and five questions to draw your own line. Published with its read key.

*Source: <https://sgit.ai/demos/vaults/threat-sized-security/index.html> · site v0.7.40 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../index.md) / Threat-sized security

# Threat-sized security: who are you actually protecting against?

A teaching vault for founders who want to do security properly and need to know where to stop. It sets out a ladder of six kinds of attacker, from your own mistakes to states, built on NIST SP 800-30, the NCSC's commodity, targeted and elevated threats, and MITRE ATT&CK; walks eight fictional startups up it, each with its assets, an attack tree and the line it should draw; compares an air-gapped, nothing-installed Mac mini with an isolated one, tier by tier; and ends with five questions to draw your own line. The startups are invented. The sources are real. It was published with the article [Who are you protecting against?](../../../articles/who-are-you-protecting-against.md)

The overview, as the app opens.

**Open it yourself. The key is the whole credential.**
 Read key: `sgit_public_read_206cfea74d57482f35fa8a1c2e33cf27d604006ca908b2da3d2a7c144c2c2260:zwlqqvkm`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_public_read_206cfea74d57482f35fa8a1c2e33cf27d604006ca908b2da3d2a7c144c2c2260%3Azwlqqvkm) · From the CLI: `sgit clone sgit_public_read_206cfea74d57482f35fa8a1c2e33cf27d604006ca908b2da3d2a7c144c2c2260:zwlqqvkm`
Published deliberately under the `sgit_public_read_` prefix, and **derived** one-way from a vault key kept in the gitignored tier and never published. Classified with `check_credential.py` before it touched this page, read back with the published key alone by `catalogue_derive.py`, and verified with an all-zeros read key as the negative control.

## See it live, here

The vault opens as an app: the ladder, the eight startups with their attack trees and lines, a compare matrix, the Mac mini, the questionnaire, every ATT&CK technique used, the sources and every file with a download button. You can also [**open it in the official UI**](https://dev.vault.sgraph.ai/#sgit_public_read_206cfea74d57482f35fa8a1c2e33cf27d604006ca908b2da3d2a7c144c2c2260%3Azwlqqvkm).

## The one idea

Before choosing a control, name the attacker. Three questions decide how secure a design needs to be: who the threat agent is, what the attack vector is, and how sophisticated they are. Read against a ladder of attackers, most startups should plan for everything up to organised crime for money, do the basics consistently because, in the NCSC's words, "Organisations that defend effectively against commodity threats present a very hard target for all attackers", sell something better than what the customer has rather than beyond what they need, and write down what they accept above their ceiling. A line drawn too low leaves you exposed to the attacks you are most likely to meet. A line drawn too high is a disservice too.

## What is in it

the ladder

### Six tiers, from your own mistakes to states

T0 your own mistakes, T1 opportunistic automation, T2 ideology and attention, T3 organised crime for money, T4 targeted commercial attackers and insiders, T5 elevated threats. Each tier carries its NIST threat source type and capability level, its motive, how it chooses targets, whether it uses commodity or bespoke capability, the ATT&CK techniques it typically uses, what stops it, and who usually faces it. The UK's AI Risk Management Toolkit asks "Who are the new threat actors?" without defining them; this is one way to answer.

The ladder, with a NIST capability level and ATT&CK techniques on every tier.

an attack tree

### The attacker's goal at the root, a technique on every branch

Each startup has an attack tree in the form Bruce Schneier described in 1999. Every branch carries the ATT&CK technique it uses, the tier of attacker who would use it and a rough cost; branches above the startup's ceiling are dashed and labelled above the line. Each tree also has a list version for screen readers.

The accounting firm assistant: the usual way in does not involve the Mac mini at all.

the line

### Must, should, over the line, under the line

The line is drawn on the ladder at the startup's ceiling. Below it: what the startup must do and should do. Above it: the tiers it accepts and writes down, with a reason, and the over-engineering it should not build, struck through with why. And the under-engineering to avoid, as warnings.

The line at T3, with the air gap above it as over-engineering.

compare

### Eight startups by six tiers

The padel booking app stops at T1. Four of the eight stop at T3. The legal review platform, which sells to law firms in disputes, plans for T4 because hack-for-hire against litigants is documented. Two reach T5 for opposite reasons: the open-source library, maintained by two people, because one malicious release reaches everyone downstream; the government drafting tool, because its customer is a government department that already owns the controls.

Where each startup draws its line, and how many plan for each tier.

the Mac mini

### Air-gapped, or isolated and not disconnected

A founder decides a Mac mini will never touch the internet, will have nothing installed, and will run scripts in the Perl that ships with macOS. The vault compares that with a design that has no inbound ports, an outbound allowlist, containers, scanning and logs, tier by tier. They differ on two tiers, and the air gap is the weaker on both.

Two of six tiers differ: T0 and T4.

your line

### Five questions, one ceiling

What could an attacker take or break, who would pay to attack you specifically, what environment you sell into, how far one breach reaches, and what your customers use today. The ceiling is the highest tier any answer points to, with the customer's baseline adding a tier below T4. The result lists the controls for every tier up to it. Nothing is stored or sent. A result can be opened from a link, such as `#line/3.3.2.2.1`, and copied as text to share.

A startup selling to mid-size businesses, holding money and credentials: T3.

## How the app is built

The same design system as the [bridge simulation](../bridge-simulation/index.md): four themes (Night, Day, Paper and Ember) whose colours live in one file, a template that escapes by default, one folder per view, and a bundle script that inlines everything into one `index.html` that runs in the vault host, on a web server or on its own. `tools/gate.py` runs nineteen checks before a release: the bundle contract, every data file, every technique id against `data/attack.json`, every tier reference against the ladder, the questionnaire's scoring against twelve hand-worked answers, theme completeness, no colour outside the theme file, no secret-shaped strings, the house wording, and every view rendered in headless Chromium at desktop and phone widths with no console errors and no network requests.

## The audit, honestly

**What was scanned.** Every file in the vault folder before the first commit, and every file again after cloning it with the published read key alone: vault-key shapes, every `sgit_` credential prefix, private-key headers, cloud key shapes, the SG/Send access token and the vault's own key. The clone was compared with the source, file by file, and matched.

**What was found.** Nothing. The negative control, an all-zeros read key against the same vault id, returned nothing.

**What it does not claim.** The ladder is a synthesis for teaching, not a standard: NIST, the NCSC and ATT&CK each define their own terms, and the tiers map onto them rather than replacing them. The startups are fictional and their ceilings are judgements made to illustrate the method, not assessments. The questionnaire is a rough guide; a real threat model needs the people who know the business.

**Write-key status:** escrowed, in the gitignored credential tier, before this page was written.

## Derived facts

From `admin/build/catalogue_derive.py zwlqqvkm <read key hex>`, read-only, no token, no clone.

- **Files:** 56 · **plaintext size:** 469 KB
- **Commits:** 4 · **last updated:** 2026-10-10 · **HEAD:** `obj-cas-imm-cf0cc786022b`
- **Top level:** `BRIEF-CORRECTIONS.md`, `PUBLIC.md`, `README.md`, `REALITY.md`, `app.json`, `app/`, `data/`, `index.html`, `tests/`, `tools/`, `versions/`
- **File types:** .js ×15, .json ×14, .css ×14, .py ×7, .md ×4, .html ×2
- **Vault app:** yes, entry `index.html` · **browser-renderable:** yes

## Sources

NIST SP 800-30 Rev. 1, Appendix D, Tables D-2 and D-3; the NCSC's *Common Cyber Attacks: Reducing the Impact* and *Design guidelines for high assurance products*; MITRE ATT&CK Enterprise; Bruce Schneier, *Attack Trees*, Dr. Dobb's Journal, December 1999; DSIT's AI Risk Management Toolkit guidance; Apple's macOS Catalina 10.15 release notes; and the reporting behind three real precedents: the Vastaamo breach in Finland, Reuters' 2022 report on hack-for-hire in litigation, and the xz Utils backdoor, CVE-2024-3094. All were read on 8 October 2026 and are linked in `data/sources.json`. ATT&CK is a registered trademark of The MITRE Corporation.

## Notes

**Where this came from.** A voice memo by Dinis Cruz about an entrepreneur's design, and his request: "let's create a vault for this, and let's actually map it out".

**Who wrote this.** [agent@riskmandate.ai](mailto:agent@riskmandate.ai) (Claude Opus 5.5, `claude-opus-5-5`), in the sgit.ai site session, for RiskMandate.ai and sgit.ai. AI-generated text, disclosed as Article 50 of the EU AI Act asks; the person with editorial responsibility is Dinis Cruz. Replies to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

[← All published vaults](../index.md)


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/threat-sized-security/index.html)*
