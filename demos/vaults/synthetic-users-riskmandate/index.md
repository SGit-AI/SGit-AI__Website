# Synthetic users, second run, five people who do not exist, reading riskmandate.ai

> The synthetic-user method applied to a second product one day later: 30 screenshots, 12 findings, two blocking a sale, and a headline finding that is measured rather than narrated, plus a JavaScript error on every page that had shipped and that every existing test had passed over.

*Source: <https://sgit.ai/demos/vaults/synthetic-users-riskmandate/index.html> · site v0.4.2 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../index.md) / Synthetic users · riskmandate.ai

# Synthetic users, second run, five people who do not exist, reading riskmandate.ai

The same method as [vault #27](../synthetic-users/index.md), pointed at a different product one day later. That is the interesting part: one run is an anecdote, two sites is a method. And the second run produced a **different class of finding** than the first, it measured rather than narrated, and it caught a bug that every existing test had passed over.

**Open it yourself. The key is the whole credential.**
 Read key: `sgit_public_read_a41174009cf6f3019147040ef0c759b6c84c86ffa37eb54af06011c161a12332:o3q6zhtr`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/en-gb/#sgit_public_read_a41174009cf6f3019147040ef0c759b6c84c86ffa37eb54af06011c161a12332%3Ao3q6zhtr) · From the CLI: `sgit clone sgit_public_read_a41174009cf6f3019147040ef0c759b6c84c86ffa37eb54af06011c161a12332:o3q6zhtr`
Submitted as a read key and published as one. Nothing was derived, and no vault key was involved.

**Everybody in it is invented**, and the vault says so above the fold, as the first one did. The personas and their words are a language model's. What is evidence is what a browser produced: the screenshots, the URLs, the scroll positions, **the word counts**, and the JavaScript errors the first pass recorded, all captured by driving a real browser against the deployed bytes at `v1.20.1`.

## See it live, here

[Open the vault in a new tab ↗](https://dev.vault.sgraph.ai/en-gb/#sgit_public_read_a41174009cf6f3019147040ef0c759b6c84c86ffa37eb54af06011c161a12332%3Ao3q6zhtr)Same app as vault #27, same five-across rail.

Five runs, six steps each, 30 screenshots. Two of the five would have paid; neither could.

## What the second run did that the first did not

It would have been easy for this to be the same vault with different names in it. It is not, and the difference is worth naming:

|  | [#27, store.sgit.ai](../synthetic-users/index.md) | This one, riskmandate.ai |
|---|---|---|
| **What the findings are made of** | What a persona said, in their voice | **Counted things.** Words above the fold, character offsets, scroll positions in pixels and screens |
| **Shape of the headline** | A page missing a fact a buyer needed | A product **never named where it is sold** |
| **Runs** | 5 · 43 steps · 15 questions · 10 confusions | 5 · 30 steps · 11 questions · **12 confusions** |
| **Page errors** | Zero, on every run | **On every page visited**, and they had shipped |
| **Findings** | 18, three blocking | 12, two blocking |

More confusion from fewer steps is the number to look at. The first site lost people slowly; this one lost them on the first screen.

## The headline: the product is not named where it is sold

Above the fold, the home page says *policy* six times, *insure* three times and *underwriters* once, shows a price of **£5**, and never once says **Agent Behaviour Policy**, which is what it sells. The name first appears **58% of the way down the page**.

The consequence is not subtle. **Two of the five read “Buy one, from £5” as buying an insurance policy for five pounds.** The persona who held that reading longest was the insurance professional, the reader best equipped to recognise the vocabulary, and therefore the most confidently wrong:

> “So: insurable, insurance, underwriters, and a policy you can buy for five pounds. On my reading of those words, **this is a product that places cover**.”, Claire Buckley, step 1

She understood the product only on the third page. The founder resolved it by accident, from a button caption. The vault also notes that the hero card is captioned *“A REAL POLICY · TEMPLATE”* beside a headline about insurability, and is the one caption on the page with room to say the product's actual name.

The reader best equipped to recognise the words was the one the words misled furthest.

### We re-measured it, and the structural numbers reproduce exactly

A claim this specific is checkable, so it was checked, the live page fetched today, rendered at the same 1440×900, and measured independently of the vault:

| Claim | The vault | Re-measured |
|---|---|---|
| Page text length | 9,270 chars | **9,270**: exact |
| First “Agent Behaviour Policy” | char 5,387 · 58% down | **char 5,387 · 58%**: exact |
| Whole page height | 6,481px · 7.2 screens | **6,481px · 7.2 screens**: exact |
| “Agent Behaviour Policy” / “ABP” above the fold | 0 and 0 | **0 and 0** |
| *underwriters* above the fold | 1 | **1** |
| *policy* / *insur** above the fold | 6 and 3 | 7 and 5, **a counting-rule difference, not a discrepancy** |

The last row: our `insur*` pattern also catches *insurance*, where the vault counted *insurable / insure / insurability* specifically; the *policy* count differs by one at the fold boundary. Every structural number, the ones the argument rests on, matches to the character.

## The bug that every test had passed over

The single most useful thing in this vault is not a persona's opinion. The first pass recorded a JavaScript error on **every page it visited**: `Unexpected token '}'` on the home page, `Unexpected end of input` on the insurance page. Both had shipped. The insurance page had been broken **since it launched**.

> “Every existing test passed, because the HTML still rendered and only the console knew.”

It was fixed in the same session, and, the right response, **a test was added that parses every inline script on every page and fails the build if one does not**. A synthetic-user run justified by its qualitative output paid for itself on a defect that has nothing to do with users at all, because the method happens to require driving a real browser and recording what it throws.

## What it says worked, which is the harder half to write

Three things were named unprompted by more than one persona, and are the reason two of the five would buy:

- **Sourced quotes.** The connector-scope section quotes vendors' own documentation with dates, *“the first page I have read on this subject that quotes the publisher instead of paraphrasing them.”*
- **The admissions.** That levels 3 and 4 have never run for a paying buyer; that the payment rails are not built; that one rung is still a design. *“Nobody oversells and then volunteers that.”*
- **The card.** Four numbers on a real vault were the only thing on the first screen that made the engineer stay. **The card is doing the work the headline is not.**

Both blocked sales were blocked by something that is not a price: **no duration anywhere**, and **no way to pay**. One founder would have paid £500 from his phone; one buyer would have paid £1,500 the same day against a deal worth more than her runway. The site correctly says the rails are not built. The honesty is right, and the consequence is that the highest-intent reader in the study had nowhere to go but an email address.

Twelve findings, tagged by what they cost rather than by severity words, *closes a segment*, *loses a channel*, *costs reach*.

## One persona walked both sites

**Priya Raghavan**, a staff engineer who pays on her own card, appears in [vault #27](../synthetic-users/index.md) and in this one. She bought on the store; on riskmandate.ai she would buy level 1. A persona reused across products is what turns two separate studies into a comparison, and it costs nothing but the discipline of keeping the records in the same shape.

## Shape, and the audit

| **Vault** | `o3q6zhtr` · 53 files · 3.5 MB · 30 PNG screenshots |
|---|---|
| **Permissions** | `app.json` declares **none** |
| **Credential** | Submitted as a **read key** and published unchanged. Verified with an all-zeros negative control: the real key produced 53 files and a `clone_mode.json`; the control produced an empty directory |
| **Secrets** | None. No tokens, keys or credentials in the contents |
| **Screenshots here** | Taken by driving the vault's own app, served from the clone at 1440×1000 on a 2× display |

Published as row #28. The first application of this method is [vault #27](../synthetic-users/index.md); the product it reads is [riskmandate.ai ↗](https://riskmandate.ai/), which this site points at from [the Licence to Operate vault](../licence-to-operate/index.md). [← All published vaults](../index.md)


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/synthetic-users-riskmandate/index.html)*
