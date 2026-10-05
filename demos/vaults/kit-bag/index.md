# Kit Bag, a business plan for a Chrome extension you build yourself, with its policy written first, published as a vault

> A recovery-shopping companion for football and padel players on hollandandbarrett.com, as a Chrome extension loaded unpacked from a folder, no store. Two ideas ride on it: open-source apps that an agent customises per person, with the vault as the distribution channel; and an Agent Behaviour Policy, written before the code, that types every barrier honestly: four boundaries Chrome enforces, the rest code as written. Working extension tested on a fixture, two stacks of label facts, an encrypted record, a risk register as an acceptance record, a build-it-yourself guide with the checks an agent runs, and a chapter for whoever commercialises it.

*Source: <https://sgit.ai/demos/vaults/kit-bag/index.html> · site v0.6.58 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../index.md) / Kit Bag

# Kit Bag, a business plan for an extension you build yourself, with its policy written first

A recovery-shopping companion for football and padel players on hollandandbarrett.com, the shop the author actually uses: label facts read from the page's own structured data, stacks, one item added to the basket per click by pressing the shop's own button, an encrypted record the person holds, and an optional model ask that shows its request before it sends it. It is a Chrome extension, and it is not on the Chrome Web Store. You build it yourself, or your agent does, and load it from a folder. Two ideas ride on that small tool, and the plan is about them.

Publish the source. Let an agent make it yours. Load it from a folder. The vault is the distribution channel and the policy travels with every copy.

**Open it yourself. The key is the whole credential.**
 Read key: `sgit_public_read_2777cf970b68ef8be761a63351991d1e73a2ab6a423eb66abd234bb9a6d0f848:r53ldcxt`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_public_read_2777cf970b68ef8be761a63351991d1e73a2ab6a423eb66abd234bb9a6d0f848%3Ar53ldcxt) · From the CLI: `sgit clone sgit_public_read_2777cf970b68ef8be761a63351991d1e73a2ab6a423eb66abd234bb9a6d0f848:r53ldcxt`
Published deliberately under the `sgit_public_read_` prefix, and **derived** one-way from a vault key kept in the gitignored tier and never published. Classified with `check_credential.py` before it touched this page, and verified with an all-zeros read key as the negative control.

## See it live, here

The plan opens as an app: the two ideas, the policy with every row typed, the stacks, a sample record, the register, how to build your own and what a business inherits. You can also [**open it in the official UI**](https://dev.vault.sgraph.ai/#sgit_public_read_2777cf970b68ef8be761a63351991d1e73a2ab6a423eb66abd234bb9a6d0f848%3Ar53ldcxt).

## Idea one: apps you build for yourself, from source somebody published

For fifteen years a Chrome extension has meant a product: somebody else's, reviewed by a store, permissions negotiated with a form, updated when they choose, monetised how they choose. Most of the value of an extension, though, is one person's: their shop, their sport, their regimen, their rules about what a script may touch. This plan takes the other road. The source is published, open, in a vault anyone can read. A person who wants it gives the read key to an agent and says: make it mine. Change the stacks to my sport. Drop the chatbot. Tighten the policy so it cannot see my account page at all. Then load it unpacked in Chrome, from the folder, with no store, no review, no listing and no permissions dialogue with anyone but Chrome itself. **An open-source app is the starting point, and an agent customises it per person.** The app's job is to be worth starting from, small enough to read in an afternoon, and to carry its own policy so the customising agent knows what it must not break.

This also leaves the problems of publishing to whoever wants to publish. The plan's last chapter is written for them: the store, a name and a mark, the retailer conversation, support when the site changes, the claims rules that bite a listing, and key custody. Loading unpacked removed three rows from the original brief's risk register. It did not remove the interesting ones.

## Idea two: the policy is the control, and it says so

A content script on a retailer's site can read the whole page. Signed in, that includes what the header says about the customer, and on the pages that show them, orders, addresses and the last four digits of a card. It can click any button, checkout included. It can call the shop's own endpoints as the customer, with the customer's cookies. Every browser-side helper has that reach, from Greasemonkey scripts to the agentic browsers of 2025, and almost none writes down what it does with it. This one did, before any code was written, in RiskMandate's four questions: **the grant**, measured from the manifest; **the mandate**, elicited from the owner; **the delta**, listed; and for every row in the delta, **the barrier and its kind**. A boundary the platform enforces, a setting our own code enforces, an expectation that nothing enforces, or none.

Thirteen rows. Four boundaries, and the rest is code as written. That is the condition of every script that runs in a page, and the reason the table exists.

The count is the point. Chrome enforces four things: the script runs only on product and basket paths, on no other site, never in the background, and reaches no model endpoint until the person grants one. Everything else that keeps the extension away from the account page and the checkout button is a rule in the code, and a rule in the code is changed by editing the code. **The policy is, at first, the only thing standing between the tool and the user's data.** We would rather say that in a table than hide it in a privacy policy. It is also why the customising agent needs the policy: it is the thing it must not loosen without telling the person. The rule in `abp.json` is one sentence: narrow any row freely; widen a boundary, or turn a setting into an expectation, only in writing.

The delta table in the app, from the same `abp.json` the extension carries.

## What is in it

the extension

### Label facts from the page's own structured data

The shop publishes an `application/ld+json` Product block on every product page, and it carries the name, brand, SKU, price, availability, ingredients, directions and nutrition. Kit Bag reads that block and nothing else on the page. The panel shows the facts, dated, and offers four actions: save the facts, add to a stack, record a purchase, add to basket. The last presses the shop's own button, once, and reports whether it found it.

The Facts tab on the test fixture, a stand-in page shaped like the shop's, with one real product's public data.

tested, not promised

### The customer's name never reaches the record

The fixture page deliberately shows a signed-in customer in its header: a name, an order count, a card ending. The Playwright test saves the facts, records a purchase, exports the record and asserts that none of those three strings is in it, that the record at rest is AES-256-GCM ciphertext, that one click on Add to basket added exactly one item to the page's counter, and that the Policy tab shows the same thirteen rows as `abp.json`. Row d5 of the policy is an expectation. The test is what makes it a checked one.

The fixture: a header full of customer details, and a panel that is proven not to read them.

the policy tab

### The table, inside the tool

The panel's fifth tab is the policy itself: the counts, the thirteen rows, the kind of each barrier coloured. Somebody who loads a customised copy can read what it may and may not do without opening a file. The panel's copy is inlined from `abp.json` by a build step, and one of the checks an agent runs is that the two still agree.

The Policy tab. Green is a boundary, blue a setting, amber an expectation, red none.

the record

### Encrypted in the browser, exported as files, versioned with sgit

The kit bag is shaped like the [Supplement Stack](../supplement-stack/index.md) record: stacks, products with dated facts, purchases, doses as what happened rather than what was planned, notes, every model ask kept whole, and a log of every action with the page it was on. The passphrase derives the key with PBKDF2-SHA256 and the record is sealed with AES-256-GCM, the primitives sgit uses. Export downloads the tree as one file; a small tool writes it out as folders; `sgit init --existing` makes it a vault with history. There is no recovery, by design, and the plan says so at first run.

The Record tab after the test saved facts and a purchase.

the stacks

### Label facts only, from eleven real products

Two templates ship: a padel weekend and a football pre-season block, twelve items from eleven products whose facts were read from the shop's structured data on 30 September 2026. Each item carries the price and availability as seen that day, the label's directions, and why the author put it there, which is a fact about the author rather than a claim about the product. Nothing states a benefit. The UK's retained Nutrition and Health Claims Regulation says what a seller may claim; a stack claims nothing.

The padel weekend stack. Prices dated, reasons attributed, no claims.

the register

### Eight risks, as an acceptance record

Written the way the [Risk Acceptance Office](../risk-acceptance/index.md) plan says: established on facts, held by a named person, accepted until a date, then accepted again, escalated or fixed. There is no deny button. Loading unpacked removed the store review, the affiliate policy and the listing takedown from the brief's register. What is left is the site changing under the button, a lost passphrase, the browser profile, label facts read as advice, the optional model call, a customising agent widening the policy quietly, a retailer's objection, and Chrome's own roadmap. The retailer row is about objection rather than law: the person using the tool is the retailer's customer, in their own browser, and permission is not the retailer's to grant.

The register in the app, parsed from the same Markdown table in the vault.

## Build it yourself, or have an agent do it

Clone the vault with the read key above. Open `chrome://extensions`, turn on Developer mode, choose Load unpacked, pick `kit-bag/extension/`. Read the Policy tab. Or hand the read key to a Claude Code or Codex session with: make it mine, my sport, my shop, drop the chatbot, keep every boundary, write any policy change into `abp.json`. The checks it runs before handing the folder back are four: the manifest's grant is unchanged, the expectations still hold in the code, the policy file and the panel's copy agree, and the fixture test passes. They are cheap, and they are the whole point.

## For whoever commercialises this

The author built this for themself and will not run a business on it. Publish it and you inherit the store review, a name and a mark of your own, the retailer conversation, support when the site changes, and the claims rules that bite a listing. Without publishing you still inherit key custody, and the honest options are no recovery, stated loudly, or the person's own vault key, backed up by them. Six ways to pay that keep the policy true: paid stacks from coaches and physios, which ties to [Lesson Loop](../lesson-loop/index.md), whose players already hold a record with the same training load in it; a club or team subscription; white-label for a physiotherapy practice or a gym; more retailers, since the parser reads `ld+json` and most large shops publish it; affiliate links, disclosed and on user action, which Chrome's policy permits; or the retailer adopting it, at which point it stops being independent and says so. What you may not do and still call it this: widen a boundary without writing it down, add telemetry without a row, hold a user's key, make a health claim, or use the retailer's mark as though you were them.

## The audit, honestly

**What was scanned.** Every one of the 33 files, from a clone made with the published read key alone, compared byte for byte with the source folder. Patterns: vault-key shapes, every `sgit_` credential prefix, the SG/Send access token, email addresses.

**What was found.** Nothing. The sample record's person is invented. The product facts are the shop's own public structured data, dated. The vault contains no email addresses. The negative control, an all-zeros read key against the same vault id, produced no clone.

**What the plan says about its own risks.** The add-to-basket button is rendered by the shop's client-side code and was not present in the fetched HTML, so the extension finds it by its text at click time and degrades to a link when it cannot; that click was exercised against the fixture, not the live shop, from the build environment. The basket comparison is a heuristic. The model ask, when enabled, sends product facts to an endpoint the person configured with their own account; the body is shown first and kept. Everything the extension does not do, it does not do because the code says so, which is what the policy's table is for.

**Independence.** Not affiliated with, endorsed by or sponsored by Holland & Barrett, whose name is used descriptively to say which shop the tool works on. No affiliate links, codes or ads. No contact with the retailer was sought, on purpose; the register says why.

**Write-key status:** escrowed, in the gitignored credential tier, before this page was written.

## Derived facts

From `admin/build/catalogue_derive.py r53ldcxt <read key hex>`, read-only, no token, no clone.

- **Files:** 33 · **plaintext size:** 565 KB
- **Commits:** 2 · **last updated:** 2026-09-30 · **HEAD:** `obj-cas-imm-047ee30c1a88`
- **Top level:** `PUBLIC.md`, `README.md`, `app.json`, `content.json`, `diagrams/`, `extension/`, `index.html`, `plan/`, `record/`, `stacks/`, `tools/`
- **File types:** .md ×12, .json ×9, .py ×3, .html ×2, .svg ×2, .webp ×2, .js ×1, .css ×1, .mjs ×1
- **Vault app:** yes, entry `index.html` · **browser-renderable:** yes

## Notes

**Where this came from.** A brief the founder drafted with Perplexity on 30 September 2026 for an independent Holland & Barrett companion extension, then a conversation that changed three things: no store, so the extension is loaded unpacked and the publishing problems are left in writing to whoever wants them; no letter to the retailer, because the client side is the customer's; and the Agent Behaviour Policy written before the code, because on a content script the policy is initially the only control, and the plan should say so rather than hide it. The founder is a customer of the shop and plays both sports; the stacks are theirs.

**Who wrote this.** [agent@riskmandate.ai](mailto:agent@riskmandate.ai) (Claude Fable 5.1, `claude-fable-5-1`), in the [agent@sgit.ai](https://sgit.ai/agents/) session, for RiskMandate.ai and sgit.ai. AI-generated text, disclosed as Article 50 of the EU AI Act asks; the person with editorial responsibility is Dinis Cruz. Replies to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

[← All published vaults](../index.md)


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/kit-bag/index.html)*
