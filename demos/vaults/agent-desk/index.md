# Agent Desk, a business plan for a Mac of the agent's own, sgit.ai

> A business plan for somebody else to build: a dedicated macOS desktop for AI agents, clean per run, built from encrypted vaults by a short bootstrap, keys by PKI, locked down and observed, erased at the end. Apple's licence quoted, with the five shapes it allows and the one it rules out; three Agent Behaviour Policies for the same customer service agent; economics with a calculator; a Wardley map. Published with its read key.

*Source: <https://sgit.ai/demos/vaults/agent-desk/index.html> · site v0.7.20 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../index.md) / Agent Desk

# Agent Desk: a business plan for a Mac of the agent's own

A business plan, written for somebody else to build: a dedicated macOS desktop for AI agents, started from a clean state per run, built from encrypted vaults by a short bootstrap, given its credentials by key, locked down and observed far beyond what a person's own Mac allows, and erased when the work is done. With what Apple's macOS licence allows, quoted, and the shapes that fit it; the economics with a calculator; a Wardley map; and three Agent Behaviour Policies for the same customer service agent, on your own Mac, on a dedicated Mac and on a hardened one. It was published with the article [A Mac of the agent's own](../../../articles/a-mac-of-the-agents-own.md).

The overview, as the app opens.

**Open it yourself. The key is the whole credential.**
 Read key: `sgit_public_read_77f48a9980032bbbed4ddd389cf60c7c9391a8449dd060f88c58fa05c602097f:5ej8boc8`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_public_read_77f48a9980032bbbed4ddd389cf60c7c9391a8449dd060f88c58fa05c602097f%3A5ej8boc8) · From the CLI: `sgit clone sgit_public_read_77f48a9980032bbbed4ddd389cf60c7c9391a8449dd060f88c58fa05c602097f:5ej8boc8`
Published deliberately under the `sgit_public_read_` prefix, and **derived** one-way from a vault key kept in the gitignored tier and never published. Classified with `check_credential.py` before it touched this page, read back with the published key alone by `catalogue_derive.py`, and verified with an all-zeros read key as the negative control. Created, pushed and audited with sgit-ai 0.20.0.

## See it live, here

The vault opens as an app: the plan, the need, the architecture, the three desktops, the customer service agent, the economics calculator, the licence, the map, the market, and every file with a download button. You can also [**open it in the official UI**](https://dev.vault.sgraph.ai/#sgit_public_read_77f48a9980032bbbed4ddd389cf60c7c9391a8449dd060f88c58fa05c602097f%3A5ej8boc8).

## The one idea

A Mac of the agent's own, holding only what the agent is meant to have, behind controls it cannot switch off, and gone when the work is done. The pool of Macs rented by the minute that the idea started as is not what Apple's licence allows, so the plan is the shapes that are: a dedicated Mac per customer, run for them, with a per-minute meter on top; developer agents on leased Macs; software for the Mac mini you keep; and a request to Apple for written terms.

## What is in it

the three desktops

### The same agent, three behaviour policies

The customer service agent from [Hope or enforcement](../hope-or-enforcement/index.md) on three desktops, every row in the published ABP grammar. The excess over the mandate that nothing bounds falls from 23 rows on your own Mac, to 11 on a dedicated Mac, to 3 on a hardened one; rows held by a boundary rise from 0 to 1 to 9.

Barriers: none, expectation, setting, boundary.

the customer service agent

### Twenty-two hostile inputs, three answers

Sixteen inputs from the Hope or enforcement mailbox and six written for a desktop. A boundary or an empty grant stops 0, 2 and 12 of them. On the hardened Mac most of what still depends on the agent comes down to one screen: the shop admin view that shows every customer.

What stopped each input, desktop by desktop.

architecture

### A clean Mac, a key, a vault

Boot a clean macOS, install sgit, decrypt one key with the desktop's own private key, clone the set-up vault scoped, verify and run its signed entry program. Profiles, allowlists, the proxy, the policy and the agent's slice of code and data all come from vaults; the record goes to an audit vault; the session is erased at the end.

Each party holds only its slice.

economics

### A meter on a Mac one customer holds

Usage profiles, a standard price a minute, a premium for the first hour, a taper after, and five options a month: your Mac run for you, a dedicated Mac metered, a Mac mini you run yourself, a monthly Mac you run yourself, and daily 24-hour leases. For the author's 104 hours a month: about £211 on a dedicated Mac with the meter, £119 for a Mac mini you look after, £390 for daily leases. Only Apple's prices are sourced; the rest are labelled assumptions.

Move the sliders; the Python model and the page agree.

the 24-hour problem

### The licence, quoted, and five shapes against it

Leasing only for Permitted Developer Services, for at least 24 hours, with sole and exclusive use; at most two virtual copies, and no time-sharing; one user at a time; the new "except as otherwise provided in writing" in macOS 27. Then the shapes, A to E, how each sits against those clauses, and the recommendation. A reading, not legal advice.

Legal advice before anything is sold.

the map

### Productising the agent's desktop

A Wardley map with its Mermaid source: the agent desktop moves from custom-built to product, carrying state, keys and lock-down with it, on parts that are already products or commodities.

Placements are claims to argue with.

## How it is built

Eleven plan documents from `plan/00-START-HERE.md`; prototypes (the bootstrap, the set-up vault layout, example configuration profiles and allowlists); `data/` written only by `tools/model.py`; three diagrams with their Mermaid sources; and an app on the design system of the [agency scale](../agency-scale/index.md) and [local evidence log](../local-evidence-log/index.md) vaults. `tools/gate.py` runs 21 checks: the data reproduces byte for byte; every ABP row uses only the 23 published capability primitives and the four barrier kinds, and every count is recomputed; the calculator agrees with the Python model on 1,736 inputs; no hosting provider is named; no credential shape, em-dash or unsupported absolute appears; and every view renders at desktop and phone widths with no errors and no network requests.

## The audit, honestly

**What was scanned.** Every file before the first commit, and every file again after cloning with the published read key alone: vault-key shapes, every `sgit_` credential prefix, private-key headers, cloud key shapes, the SG/Send access token and the vault's own key. The clone matched the source, file by file.

**What was found.** Nothing. The negative control, an all-zeros read key against the same vault id, returned nothing.

**What was tested, and what was not.** The bootstrap's key steps were run on Linux with sgit-ai 0.20.0: a key pair generated, a read key encrypted to it and decrypted, an entry program signed and verified, a tampered one refused; the clone flags were checked against `sgit clone --help`. Nothing ran on a Mac. Every boundary in the hardened policy is a design, not a measurement, and the five-minute boot is an assumption.

**What it does not claim.** The licence section is a reading of Apple's published text, not legal advice. Every number other than Apple's prices is an assumption. No provider is named.

**Write-key status:** escrowed, in the gitignored credential tier, before this page was written.

## Derived facts

From `admin/build/catalogue_derive.py 5ej8boc8 <read key hex>`, read-only, no token, no clone.

- **Files:** 79 · **plaintext size:** 2633 KB
- **Commits:** 2 · **last updated:** 2026-10-09 · **HEAD:** `obj-cas-imm-d145bd24a6c8`
- **Top level:** `PUBLIC.md`, `README.md`, `REALITY.md`, `app.json`, `app/`, `data/`, `diagrams/`, `index.html`, `plan/`, `prototypes/`, `tools/`, `versions/`
- **File types:** .json ×17, .md ×15, .js ×14, .css ×13, .png ×3, .svg ×3, .webp ×3, .mmd ×3, .py ×3, .html ×2, .mobileconfig ×2, .sh ×1
- **Vault app:** yes, entry `index.html` · **browser-renderable:** yes

## Notes

**Where this came from.** A voice memo by Dinis Cruz, after two companies replied with interest to the research behind [A locked-down desktop for an agent, by the minute, is still hard to rent](../../../articles/an-agent-desktop-by-the-minute.md); licence and platform research done for this plan; and the customer service case from [Hope or enforcement](../hope-or-enforcement/index.md).

**Who wrote this.** [agent@riskmandate.ai](mailto:agent@riskmandate.ai) (Claude Opus 5.5, `claude-opus-5-5`), in the sgit.ai site session, for RiskMandate.ai and sgit.ai. AI-generated text, disclosed as Article 50 of the EU AI Act asks; the person with editorial responsibility is Dinis Cruz. Replies to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

[← All published vaults](../index.md) · [All business plans](../../../startups/business-plans.md)


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/agent-desk/index.html)*
