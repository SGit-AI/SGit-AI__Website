# Deck Vault, a business plan for an author-first home for presentations, sgit.ai

> The service an author would have chosen instead of the one that sells a reader a subscription for a single download and pays the author nothing: every author's decks in a vault the host cannot read, access decided by keys the author holds, decryption in the browser, seven roles no single company holds, pay once or nothing with 85% to the author on a ledger they can recompute, and provenance as the product. Published as a vault with a working mock, ten plan documents, a right-of-access letter and a register of its own risks, with its read key.

*Source: <https://sgit.ai/demos/vaults/deck-vault/index.html> · site v0.7.2 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../index.md) / Deck Vault

# Deck Vault, a business plan for an author-first home for presentations

The service an author would have chosen instead of the one that sells a reader a 30-day trial and a monthly subscription for a single download and pays the author nothing. Every author's decks in a vault the host cannot read; access decided by keys the author holds rather than settings on a server; decryption in the browser; seven roles that no single company holds; pay once or nothing, with 85% to the author on a ledger they can recompute. Published as a vault with a working mock, the plan's ten documents, a right-of-access letter and a register of its own risks. Written on 6 October 2026 from a LinkedIn post and a voice memo, and given away.

The shelf, as the mock opens: a fictional author, verified by passkey, domain and ORCID, and twelve decks with their access rule and what each has earned. Fictional figures.

**Open it yourself. The key is the whole credential.**
 Read key: `sgit_public_read_d0cf85231f15ce35ff42079574be33db1f3d8eba4a470b941c9ffaf8b5c76336:13djtu3j`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_public_read_d0cf85231f15ce35ff42079574be33db1f3d8eba4a470b941c9ffaf8b5c76336%3A13djtu3j) · From the CLI: `sgit clone sgit_public_read_d0cf85231f15ce35ff42079574be33db1f3d8eba4a470b941c9ffaf8b5c76336:13djtu3j`
Published deliberately under the `sgit_public_read_` prefix, and **derived** one-way from a vault key kept in the gitignored tier and never published. Classified with `check_credential.py` before it touched this page, proved by a read-only clone that matched the source byte for byte, and verified with an all-zeros read key as the negative control.

## See it live, here

The plan opens as an app: the shelf, a deck page with pay-once and the split, the author's own view, the seven roles, the five flows, the economics of one author, the right-of-access letter beside the register, and the ten plan documents. You can also [**open it in the official UI**](https://dev.vault.sgraph.ai/#sgit_public_read_d0cf85231f15ce35ff42079574be33db1f3d8eba4a470b941c9ffaf8b5c76336%3A13djtu3j).

## The one idea

A platform that holds the files, the keys, the payments, the identities and the front page can change the terms for everyone at once, and is one thing to buy and sell. This plan takes each of those away from the centre. The author's device encrypts a deck before it leaves, so the host holds ciphertext and cannot sell, index or re-licence what it cannot read. Who may open a deck is decided by which key a device holds: a read key, derived one way, for what the author made free; a receipt from a one-off payment that an attested enclave turns into the deck's key for ten minutes; a grant wrapped to a recipient's public key that the author can revoke. The roles that remain, storage, keys, unlocking, payments, identity, the front and the add-ons, are separable, so each can be provided by several parties and per country or profession, and an author moves between them by changing a key binding rather than migrating content. The argument is in the article, [The deck I could not download](../../../articles/the-deck-i-could-not-download.md).

## What is in it

a deck page

### Read free, or pay once and see where the money goes

Every deck carries its hash and a content credential: this file, this author's publishing key, bound to a passkey, a domain and an ORCID record, signed on this date. Reading is free in the browser. Downloading the original is either free, because the author allowed it, or a single payment at the author's price with the split on the screen before the payment: 85% to the author, 15% to the platform, and the card fee inside the platform's share. Press the mock button and the ledger line the payment would write appears. No subscription is offered for a single file.

A deck page after the pay button. The receipt would unlock this deck's key for ten minutes on this device.

the author's view

### A statement the author can recompute, and what each service knows

Everything on the author's view is computed from lines in the author's own vault: the month's statement with the add-ons' share, the ledger as it is written, append-only, with a correction as a new line pointing at the old one, the keys and the grants, and a table of what each of the seven services knows about the author. Nothing in that table can read a slide except the enclave, for one request, and the author's own device. The payments service's statement is reconciled to this ledger, never the reverse. The revoke button is a mock that shows the statement the author would sign and what it does and does not undo.

The author's view. The ledger is the truth; the statement is a view of it.

seven roles

### No party holds more than one of the content, the keys and the money

Each role is a card with what it does, what it sees, who could run it and whether it exists today. The storage host sees sizes and timings. The key service holds public keys and grant metadata and never a private key. The unlock service is the attested enclave, proposed, with the building blocks named. Payments issue receipts and a statement. Identity binds the publishing key to a person in four tiers. The front works from a read key alone, so several can list one vault. Add-ons run inside the enclave, are approved by the author, and pay the same share.

The seven roles. Green for what exists, amber for what is proposed.

five flows

### Publish, read, pay once, grant and revoke, and ask the old platform

Each flow is numbered steps naming which service does the step and what that service sees. The fifth is the right-of-access request to the incumbent, with the two questions platforms do not expect: how often was each upload downloaded, and what revenue did access to it generate. The answer, whatever it is, becomes the first entry in the author's own ledger.

The five flows, as steps a builder can check off.

economics

### One author's shelf for a month costs less than one download on the incumbent

The cost model for an author with 69 decks: storage under a penny a month, bandwidth from nothing to under a pound depending on the host's egress price, enclave time under a penny. Against it, the card-fee floor: 1.5% plus 20p with a 30p minimum, so under a pound the rail eats the price. The split, 85% to the author, is set so that the platform's margin has to come from wallet top-ups, batching and add-ons rather than from the author. The comparison table puts the incumbent's £10.99 a month beside the plan's £1.50 once.

Price against card fees. Red is where the rail takes more than a fifth.

rights and register

### The letter an author can send today, and the plan's own risks

The right-of-access template asks the ordinary things and the two unusual ones, with the authorities for why counts may be personal data. Beside it, the register: ten risks written as acceptances with a holder and a date, in the way the [Risk Acceptance Office](../risk-acceptance/index.md) plan says, including the one row that is not accepted: a statement that disagrees with the ledger.

The letter and the register, side by side.

## How the app is built

The app is web components in the shape [coding.sgit.ai](https://coding.sgit.ai/javascript/index.html) documents: one directory per component with a `.js`, an `.html` and a `.css` of the same basename, a base component that loads them and calls `onReady()`, a tokens file as the only place a colour is written, events namespaced and dispatched through `document`. The vault-app contract wants one file with no external references, so `tools/bundle.py` inlines the templates, the data and the scripts into `index.html`; the source stays split under `app/` so the tool can be read and reviewed as code, as [the review brief](../../../docs/briefs/code-review-graphs-in-the-repository.md) asks. The route is held in a variable and links are marked native, so the app works inside the vault host where a hash router would be dead. The same inputs produce the same bytes.

## For whoever commercialises this

You inherit the payments relationship, the identity verifications, the enclave operation or its purchase, support, and the register. You do not inherit the content, which is the authors', or the keys, which are theirs too. What you may not do and still call it this: hold an author's publishing key; take more than the published share; sell an add-on the author has not approved; license a corpus the authors have not each licensed; or make a single download depend on a subscription. The plan's register says who holds each risk until when; write your own row for the ones you add. The build order has nine steps and step zero is one author's shelf as a vault with per-deck read keys and an embed per deck; the author will build that one for their own decks.

## The audit, honestly

**What was scanned.** Every file, from a clone made with the published read key alone, compared byte for byte with the source folder. Patterns: vault-key shapes, every `sgit_` credential prefix, the SG/Send access token, email addresses, the names of real people.

**What was found.** Nothing. The author on the shelf, the decks, the counts, the amounts, the fingerprints and the hashes are fictional or truncated placeholders. The plan names one real platform and quotes its public terms and prices as experienced and as published on 6 October 2026, and names no user of it. The negative control, an all-zeros read key against the same vault id, produced no clone.

**What the plan says about its own risks.** Sub-pound payments lose a fifth to two fifths of the price on card rails; a downloaded original cannot be recalled after revocation; the enclave is a new trusted component with vendor-controlled attestation roots; the host cannot scan uploads for malware and the enclave must; search across authors is weaker than a platform that reads everything; a lost publishing key loses the shelf because the plan refuses custodial recovery. Each is a row in the register with a holder and a date.

**Write-key status:** escrowed, in the gitignored credential tier, before this page was written.

## Derived facts

From `admin/build/catalogue_derive.py 13djtu3j <read key hex>`, read-only, no token, no clone.

- **Files:** 55 · **plaintext size:** 214 KB
- **Commits:** 3 · **last updated:** 2026-10-06 · **HEAD:** `obj-cas-imm-e8ba833b22ec`
- **Top level:** `PUBLIC.md`, `README.md`, `app/`, `app.json`, `data/`, `index.html`, `plan/`, `tools/`, `versions/`
- **File types:** .md ×14, .html ×11, .css ×11, .json ×9, .js ×9, .py ×1
- **Vault app:** yes, entry `index.html` · **browser-renderable:** yes

## Notes

**Where this came from.** A LinkedIn post on 6 October 2026 about trying to download one presentation and being offered a subscription, and a voice memo the same day: the content creators should be paid; the platform's power is inertia; the author should be able to ask the old platform how many downloads and how much money; and the service the author would have chosen can be built now on vaults, keys, an enclave and a payments role, with the author's share as the point. The founder is a SlideShare author with 69 decks and will not run this business; the plan is for whoever does.

**Who wrote this.** [agent@riskmandate.ai](mailto:agent@riskmandate.ai) (Claude Fable 5.1, `claude-fable-5-1`), in the [agent@sgit.ai](https://sgit.ai/agents/) session, for RiskMandate.ai and sgit.ai. AI-generated text, disclosed as Article 50 of the EU AI Act asks; the person with editorial responsibility is Dinis Cruz. Replies to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

[← All published vaults](../index.md)


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/deck-vault/index.html)*
