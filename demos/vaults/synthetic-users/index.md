# Synthetic users — five people who do not exist, shopping

> Five invented buyers walked through store.sgit.ai one screenshot at a time, asked what they made of each screen and interviewed at the end: 43 screenshots, 15 questions the site did not answer, 10 confusions and 18 findings — three of them costing a sale, four already fixed and kept rather than deleted.

*Source: <https://sgit.ai/demos/vaults/synthetic-users/index.html> · site v0.2.88 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../index.md) / Synthetic users

# Synthetic users — five people who do not exist, shopping

Five invented buyers were walked through [store.sgit.ai](../../../network/index.md) one screenshot at a time, asked what they made of each screen, and interviewed at the end. The vault holds all of it: **43 screenshots, 43 steps, 15 questions the site did not answer, 10 places somebody got lost, and 18 findings — three of them costing a sale.** It is the most useful vault published here that contains no real data at all.

**Open it yourself — the key is the whole credential.**
 Read key: `b70c317b7aa4b6084e05669795dc89e6bf1e46b4e948b9f6c475948ae502823c:g2hei4u6`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/en-gb/#b70c317b7aa4b6084e05669795dc89e6bf1e46b4e948b9f6c475948ae502823c%3Ag2hei4u6) · From the CLI: `sgit clone b70c317b7aa4b6084e05669795dc89e6bf1e46b4e948b9f6c475948ae502823c:g2hei4u6`
Derived one-way from a vault key that is not published and never will be.

**Everybody in it is invented, and the vault says so first.** The personas are fictional, the names are fictional, and every word attributed to them was written by a language model reading screenshots. The vault's own banner calls this out before you can scroll past it: **it is not user research**, and no sentence in it is evidence about a real person. What *is* evidence is the part a machine produced — the screenshots, the URLs, the step order, the viewport sizes and the page-error counts, captured by driving Chromium against the store's built bytes at `v0.1.12`, verified byte-identical to the live site by SHA-256.

## See it live, here

[Open the vault in a new tab ↗](https://dev.vault.sgraph.ai/en-gb/#b70c317b7aa4b6084e05669795dc89e6bf1e46b4e948b9f6c475948ae502823c%3Ag2hei4u6)A five-person rail with a run, an interview and a findings list behind each — roomier in its own tab than in the frame below.

Five people, five outcomes, and the disclosure above the fold rather than in a footnote.

## The idea worth stealing: hand the agent the screenshot, not the DOM

This is the whole method, and the vault states it in one sentence:

> “An agent that drives a store by reading the DOM finds the buy button every time, and therefore finds no confusion — which is the only thing worth running this for.”

So the loop is deliberately crippled. The agent gets **a screenshot**, the same thing a person would have, and has to work out what to do from it. Seven steps, run until the persona buys, leaves, or runs out of patience — and patience is a field on their record, not a judgement call made mid-run:

|  | Step | Why it is there |
|---|---|---|
| **1** | Observe | Screenshot at the persona's own window size. **Do not read the DOM.** Do not read the markdown twin unless this persona would |
| **2** | Say what you see | At the level of detail this persona would take in — *“a skimmer sees three things; a slow reader sees the caveat under the price”* |
| **3** | Think | What they are weighing, and what they are suspicious of. The vault calls this *“the part that is worth more than the click path”* |
| **4** | Record a question | Something the page raised and did not answer. Null when there is none. **These are the output** |
| **5** | Record confusion | Where the page lost them, or where they guessed. *“A run with no confusion anywhere is a run that was not done properly”* |
| **6** | Act | One action, with the reason given **in the persona's terms, not the site's** |
| **7** | Loop | Until bought, left, or out of patience |

The protocol is published *inside* the vault, which is what makes a second run in a month's time comparable rather than merely later.

## The five runs, and what each one cost

Every number below is computed from the run records, not from the summary:

| Persona | Outcome | Steps | Questions | Confusions | Viewport |
|---|---|---|---|---|---|
| **Priya Raghavan** — staff engineer, pays on her own card | **bought** | 10 | 3 | 2 | 1440×900 |
| **Tomás Beckett** — technical co-founder, £500 is his call alone | **stalled** | 10 | 5 | 4 | **390×844** |
| **Marguerite Okonjo** — fund partner | left, favourably | 8 | 2 | 1 | 1440×900 |
| **Dan Whitlock** — COO, signs to £10,000 | left | 7 | 4 | 3 | 1512×820 |
| **Ines Halvorsen** — security engineer, never the buyer | left, and sent it on | 8 | 1 | 0 | 1680×1050 |

**Read the viewport column.** The persona carrying the largest decision a single person makes alone on that site did the whole thing **on a phone** — and produced the most questions and the most confusion of anyone. That is not a finding the vault announces; it falls out of the table once the numbers are in one place.

Zero page errors across all five runs, which is worth stating because it means none of the confusion below was a bug in the store's code. It was the copy.

Every step pairs the image with four things: what they saw, what they thought, what they asked, what they did. The screenshot is the citation.

## What it found: 18 things, three of them costing a sale

The findings are ordered by what they cost rather than by who found them, and each one points at a page you can go and check. The three blockers:

1. **The £500 page carries no duration of any kind.** The buyer's single decisive question is *how long does this take*, and it was answerable nowhere before purchase. Earlier copy had carried a figure and it was lost in an edit three versions back. Found by the persona who left without buying and said so in the interview.
2. **The same page describes its own process two ways, and the post-sale page a third.** A buyer would have had to pay to find out which was true.
3. **The add-on built for a board has no price, no range and no next action** — on a page whose heading is exactly the question its buyer arrives with.
Grouped by cost, tagged by page, and attributed to the run that produced them.

**Four are already marked fixed**, in the store release that followed the runs — and they are kept, annotated, rather than deleted, on the stated grounds that *“a findings list that loses the fixed ones cannot be compared with the next set of runs.”* That is the same instinct as this site's own [version log](../../../admin/versions.md), applied to somebody else's bugs.

One fix is better than the finding asked for. The duration problem was not answered by inventing a number: the page now says that the time from a buyer's reply **has never run for a paying buyer, so there is no measurement to quote** — with a ledger row to match. A synthetic user asked for a figure and got a disclosure instead, which is the more honest answer and the harder one to write.

## Where it stops being a checklist

The interviews are the part that does not read like tooling output. The adversarial persona — a security engineer who reads vendor sites for sport and is *never* the buyer — was asked whether she believed it:

> “More than any vendor site I have read this year, and I read them for sport. The reason is narrow and specific: **three times I found the weak point and the site had already written it down, in stronger words than I would have used.**”

And the buyer who stalled, asked what made him believe it:

> “Two things did it: the ‘never sold once’ chip on the thing they want me to buy, and the deposit split I did not ask for. **Nobody invents either of those to sell harder.**”

Then, asked what he still did not know at the end: *“The date. I have a term sheet expected in six weeks and this site does not contain a single duration for the thing I would buy.”* The same gap as finding #1, in the voice of the person it cost.

The same questions for everyone, so the answers can be read down a column as well as across a run.

## What it refuses to claim

The thing that makes this publishable rather than embarrassing is how hard it works to be less than it appears:

- **The disclosure is above the fold and in the README's second heading** — *“Everybody in here is invented”* — not in a footnote a reader reaches after forming a view.
- **It separates the invented part from the captured part** explicitly: the narration is a model's; the screenshots, URLs, step order, viewports and error counts are a browser's.
- **It names the build it ran against** (`v0.1.12`), verified byte-identical to the live site by hash, and says why it ran against local bytes rather than the live host.
- **Three findings are recorded as claims that held** rather than defects — a checkout page with no form element and no off-origin request, an admin page absent from three indexes, and three pages that cost the seller sales and were kept anyway.
- **It ends on an open question** it does not answer: whether one world-readable page is a decision or an accident.

## What to take from it

- **Cripple the agent on purpose.** Give it the screenshot, not the DOM. Competence at finding the button is the thing standing between you and the finding.
- **Write the expected journey before the run.** The vault stores what each persona was *expected* to do beside what they did, so a surprise is visible as a difference rather than only as a result.
- **Make “where did you guess” a required field.** A run with no confusion is treated as a run done badly, not a site that passed.
- **Keep the fixed findings.** Deleting them destroys the comparison the next run exists to make.
- **Put the protocol in the artefact.** Two runs a month apart are only comparable if the loop is written down where both can see it.

## Shape

| **Vault** | `g2hei4u6` · 67 files · 6.4 MB · 43 PNG screenshots |
|---|---|
| **App** | `index.html` with CSS, JS and a fallback copy of the data inlined — so it renders outside a vault host too, which is how the screenshots on this page were taken |
| **Permissions** | `app.json` declares **none** — no filesystem, no network, no LLM. It reads its own bundle and draws |
| **Data** | `personas`, `journeys` (written before the runs), `protocol`, `runs`, and `bundle.json` — the concatenation the app actually reads |
| **Tools** | `runner.mjs` drives the browser, `narrate.py` adds the persona layer, `bundle.py` rebuilds the app's data |

## The pre-publication audit

Run with the read key printed above, against a full clone, before this page existed:

- **The credential submitted was a vault key, not a read key.** It was classified before it touched anything, the read key was derived one-way from it, and **only the derived read key appears here**. The vault key is not on this site and will not be.
- **The derivation was verified with a negative control.** The derived key produced 67 files and a `clone_mode.json`; an all-zeros key against the same vault id produced an empty directory. [That control exists because we once called a leak on a directory an invalid key created identically.](../publishing.md)
- **Nothing secret-shaped in the contents.** The one credential-looking string, `SYNTH4DELTA`, is a discount code **the store publishes itself**; the vault says so, and says the store's build fails if a published hundred-per-cent code and a live payment rail ever coexist.
- **Every screenshot on this page was taken by driving the vault's own app**, served locally from the clone, at 1440×1000 on a 2× display.

Published as row #27 on the [vaults table](../index.md). The store it examines is [store.sgit.ai](../../../network/index.md); the method is the one on [publishing a vault](../publishing.md). [← All published vaults](../index.md)


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/synthetic-users/index.html)*
