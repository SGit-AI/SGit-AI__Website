# Agent as Webmaster, a business plan published as a vault

> A complete business plan for a company that gives small businesses a website they can change by asking, with an AI agent as the webmaster: architecture, workflow, packages and prices, a unit-economics calculator, go-to-market, the first ninety days, the investor case, the risks, four mock-up sites and the prototypes to run the first customer. Published with its read key, written for somebody else to run.

*Source: <https://sgit.ai/demos/vaults/agent-webmaster/index.html> · site v0.6.9 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../index.md) / Agent as Webmaster

# Agent as Webmaster, a business plan for somebody else to run

A complete business plan published as a vault: the idea, the architecture, the workflow, the packages and prices, the unit economics with a calculator, go-to-market, the first ninety days, the investor case, the risks, four mock-up websites and the prototypes to run the first customer. It is the first of a set of plans published here for other people to build companies on, and it is written to be taken, not admired. **The business:** give small businesses a website they can change by asking, by putting an AI agent in the webmaster's chair.

**Open it yourself. The key is the whole credential.**
 Read key: `sgit_public_read_d5ba4a106276936456b0a108b3988aa777f5402ba6699fcd67becd620fe55828:ikrqeu5t`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_public_read_d5ba4a106276936456b0a108b3988aa777f5402ba6699fcd67becd620fe55828%3Aikrqeu5t) · From the CLI: `sgit clone sgit_public_read_d5ba4a106276936456b0a108b3988aa777f5402ba6699fcd67becd620fe55828:ikrqeu5t`
Published deliberately under the `sgit_public_read_` prefix, and **derived** one-way from a vault key that is kept in the gitignored tier and never published. Classified with `check_credential.py` before it touched this page, and verified with an all-zeros negative control: the real key cloned 32 files, the control cloned nothing.

## See it live, here

The plan opens as an app. You can also [**open it in its own window ↗**](https://dev.vault.sgraph.ai/#sgit_public_read_d5ba4a106276936456b0a108b3988aa777f5402ba6699fcd67becd620fe55828%3Aikrqeu5t), where the calculator and the mock-ups have more room.

## What is in it

the plan

### One page first, then everything behind it

The app opens on six things to know: the business, why now, the stack, the numbers, who runs it and why the plan is public. Below that, each section of the plan has a diagram and the detail: the architecture (a chat session, one public repository per customer, GitHub Pages on every push), the setup in three days and the change loop that runs forever, the three packages, the model, the market, the ninety days, the investor case and the risks.

The status pill says what the numbers are: **starting hypotheses**. Every price and every hour is a first guess for a UK operator in 2026, and the plan says to test them on the first ten customers and change them.

The plan as it opens: the status pill, the title, and six things to know.

what you sell

### Three things, priced three ways

Setup once (£300, £600 or £1,200) for the expert's time. Maintenance monthly (£50, £100 or £200, bronze, silver, gold) for keeping the site working, watched and tweaked, with a note to the customer each month. On demand (£40 to £250) for the changes that take an expert, and tokens passed through for heavy users.

The plan is careful about the middle one, because this site argues elsewhere that most subscriptions are rent on something ignored. Here the operator does something every month and the customer can see it in the commits, and the plan says what to do when a change log has been empty for three months: tell them, and offer bronze or nothing.

The three package tables, and the note on why a subscription is earned here.

the model

### A calculator, because the numbers are yours to change

Eleven sliders: customers, prices, setups and changes per month, direct costs, and the hours each thing takes. Six numbers update as you move them: recurring revenue, revenue, contribution, annual contribution, operator hours against the roughly 160 available, and contribution per operator hour. When the hours pass 160 the figure turns red and the app says it is time for the second operator.

Underneath, the three fixed scenarios the plan uses: 20, 50 and 80 customers, at £3,360, £7,300 and £11,450 of monthly contribution. Nothing runs anywhere to compute this. It is arithmetic in the page.

The calculator: sliders on the left, six numbers on the right, arithmetic in the page.

the mock-ups

### Three invented customers and the sales site

A bakery, a two-partner accountancy firm and a physiotherapy clinic, each a standalone HTML page with its styles inlined, each carrying a **"changed by the webmaster"** strip near the top showing the last three changes and when they went live. That strip is the product: a website that visibly gets changed.

The fourth mock-up is the operator's own sales site, built the way every customer's site would be, with a chat transcript as the hero, how it works in four steps, the three examples, the prices published, and the offer that converts: a free rebuild for two weeks, then it goes dark, then see whether they miss it.

Hollow Lane Bakery, an invented business, with the change strip under the header.

the sales site

### The demonstration is the sales process

The hero of the sales site is a four-message chat: a closure notice and new hours, live in 41 seconds; three photos added, live in a minute. The plan's go-to-market section says that showing a change happen live, in under a minute, is the whole pitch, and the mock-up is built to be that demonstration.

The prices are on the page. The plan argues that publishing them is itself a differentiator against a market that hides prices behind a quote.

The sales site: a chat transcript as the hero, then how it works.

## What this vault demonstrates

| Feature | The mechanism, not the marketing |
|---|---|
| **A business plan as the unit of handover** | The plan, its documents, the diagrams, four working mock-ups and the operating prototypes travel as one read key. Somebody who wants to run this business clones one thing and has everything, including the tool that keeps the app and the content in step. |
| **An app with nothing requested** | `app.json` declares `"permissions": {}`. The app reads its own content, computes in the page, and links to its own files. No LLM, no writes, no network, so a published read key in front of it costs nobody anything, which is the third of the three rules in its `PUBLIC.md`. |
| **Content and app kept in step** | Everything shown comes from `content.json`, inlined into `index.html` by `tools/inline-content.py`, which matches the placeholder exactly rather than by pattern. That tool exists because the first inliner matched an example command in an HTML comment and deleted the page. The rule that came out of it is in the tool's docstring. |
| **The same content, twice** | The app for reading, and eleven markdown documents in `plan/` for following, with a reading order, breadcrumbs and a one-page version at the top. The vault browser renders the markdown; the app renders the JSON; they were written together. |
| **Mock-ups that open from the vault** | Four standalone HTML pages with every style inlined and no external asset, so they render inside the vault host's sandbox, in the vault browser, and saved to a desktop. Links from the app to them are plain relative links, which the host intercepts. |
| **Written for another operator** | The plan names what to open and what to keep, what to measure at day ninety, and the one thing to send back. It follows the operating model in [the startups article](../../../articles/the-question-is-whether-they-miss-it.md): ship, give it away briefly, take it away, be profitable before you raise, open everything. |

## The audit, honestly

**What was scanned.** Every one of the 32 files, from a clone made with the published read key and nothing else: markdown, HTML, JSON, SVG and the one Python tool. Patterns: vault-key shapes (24 alphanumerics before a colon), every `sgit_` credential prefix, API-key shapes, private-key blocks, email addresses, bearer tokens and `delete_auth` values.

**What was found.** Nothing. No credentials, because the vault carries none by design; no email addresses, because the businesses in the mock-ups are invented and the contact forms are placeholders that say so; no personal data. The negative control, a clone attempted with an all-zeros read key against the same vault id, produced an empty directory.

**What the process found instead, in the CLI.** The first push of this vault failed. The CLI's automatic transport resolution treated a 404 on a not-yet-existing object, which is what every fresh vault's first push reads, as "this host has no live API" and flipped the vault to the read-only static transport. Two fixes went into the CLI repository from this session: the resolver now only flips on the batch endpoint answering 404, 405 or 501, and `push`, `pull`, `fetch`, `status` and `delete` now honour `--transport`, which they had been ignoring. A test pins the first fix. A vault published to teach a method produced a rule for the tool, which is the pattern this section keeps producing.

**Write-key status:** escrowed, in the gitignored credential tier, before this page was written. The vault is correctable.

## Derived facts

From `admin/build/catalogue_derive.py ikrqeu5t <read key hex>`, read-only, no token, no clone.

- **Files:** 32 · **plaintext size:** 666 KB
- **Commits:** 2 · **last updated:** 2026-09-23
- **Top level:** `PUBLIC.md`, `README.md`, `app.json`, `content.json`, `diagrams/`, `index.html`, `mockups/`, `plan/`, `prototypes/`, `tools/`
- **File types:** .md ×18, .html ×5, .svg ×3, .webp ×3, .json ×2, .py ×1
- **Vault app:** yes, entry `index.html` · **browser-renderable:** yes

## Notes

**Where this came from.** A voice memo by the founder on 23 September 2026, worked into a plan the same day. The memo's numbers were "300, 500 or 1,000 for setup" and "50 or 100 a month for maintenance"; the plan makes them £300, £600 and £1,200, and £50, £100 and £200, adds the on-demand tier and the token pass-through the memo asked for, and marks all of it as a hypothesis. **Where it goes next.** The [startups section](../../../startups/index.md) now has a place for plans like this one, and the intention is a set of them, each a vault, each written for somebody else to run.

[← All published vaults](../index.md)


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/agent-webmaster/index.html)*
