# Comparisons, as tests you can re-run — sgit.ai

> What a task costs with vaults and without, published by a participant and built to be challenged: every entry states the steps, the date, the result and how to re-run it. Includes a privilege vocabulary, and one comparison vaults lose.

*Source: <https://sgit.ai/compare/index.html> · site v0.2.52 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / Comparisons

# Comparisons, as tests you can re-run

What a task costs with vaults, and without them. This page is not unbiased — it is published by a participant, and nobody should read it as neutral. It is built to be **challengeable** instead: every entry states the exact steps attempted, the date, what happened, and how to run it yourself.

**Why not "unbiased".** A comparison published by one of the parties is not a neutral instrument, and claiming otherwise would be the least credible thing on this site. The achievable and stronger property is reproducibility: **an assertion that is wrong gets screenshotted; an experiment that is wrong gets corrected.** If an entry here is out of date or simply mistaken, the fix is a re-run, and the correction improves the page rather than discrediting it. [Tell us](mailto:) or open an issue on [GitHub](https://github.com/SGit-AI/SGit-AI__CLI).

## The asymmetry, stated up front

Our rows can be **executed**. A script opens a published vault, tries the operation and records what happened — it runs on demand and fails loudly when reality moves. Rows about anybody else's product cannot work that way: there is no API for "how many steps does this take in a desktop app", and automating someone's product against their terms is not something we will do. Those rows are **checked by hand, by a person, on a stated date**.

So the two kinds of row carry different badges, and you should trust them differently:

| Badge | Means | Ages |
|---|---|---|
| **machine-verified** | An automated check against the live service, in `admin/build/compare_tests.py`. The evidence below each claim is its actual output | Re-run any time; the date is the last run |
| **hand-checked** | A person performed the steps on the date shown and wrote down what happened | Decays. Past the expiry it renders as **unverified**, not as fact |

Loading verification status…

## The entry format

Every entry answers the same eight things. Anything that cannot be filled in honestly does not get published.

| Field | Why it is there |
|---|---|
| **Task** | Stated concretely enough that somebody can attempt it |
| **Steps** | Countable and disputable on facts. The number is a *summary*; the transcript below it is the evidence, because step counts are gamed by where you start counting |
| **Prerequisites** | Accounts, subscriptions, installs. This is where cost actually lands |
| **Privileges granted** | What the counterparty can now reach. The column that usually decides the answer — see the vocabulary below |
| **Where it runs** | Your machine, or theirs |
| **Survives the vendor** | Whether the artefact still works if the service stops |
| **Verified** | The date, and whether by machine or by hand |
| **Re-run it** | The command or the steps, so the claim is auditable rather than trusted |

## The privilege vocabulary

"Share it with them" hides the entire question. These seven properties make two grants comparable, and each is a fact rather than a judgement. This vocabulary is the part of this page most likely to be wrong at first — it is offered to be argued with.

| Property | Values | What it answers |
|---|---|---|
| **scope** | file · folder · vault · account · all-vaults | How much does the grant reach? |
| **operations** | read · write · delete · administer | What can be done with it? |
| **bearer** | person · program-on-their-machine · vendor-server · any-holder | Who actually holds it? "any-holder" means the grant is a string: whoever has it, has it |
| **mediation** | server-enforced · key-enforced | Who says no? A server can refuse and can log. A key cannot refuse — possession *is* access |
| **duration** | session · until-withdrawn · forever | When does it lapse on its own? |
| **withdrawal** | effective · future-only · none | Can you take it back — and does taking it back reach what they already have? |
| **observability** | per-reader-log · aggregate · none | Can you see who read what? |

Written compactly, a published read key is: `scope:vault · ops:read · bearer:any-holder · mediation:key · duration:forever · withdrawal:future-only · observability:none`. Three of those seven are **worse** than a mainstream sharing link, and saying so is the point of having a vocabulary.

**One shape the vocabulary above could not express, until a vault demonstrated it.** An app can be granted the *use* of a credential without being given the credential: the [Risk Mandate vault](../demos/vaults/risk-mandate/index.md) seals its OpenRouter key under the vault key, and the host makes the call on the app's behalf. So `ops` and `bearer` come apart — `ops:llm-chat` is granted while `bearer` of the key is not, and a read-key holder auditing the vault (as we did) finds ciphertext where the secret would be. Most sharing models cannot say this, because handing over the capability and handing over the credential are the same act.

## The entries

Three to start with, chosen to be different: one small and verifiable in seconds, one we lose, one that is the actual differentiator. More arrive as they are tested — not as they are thought of.

### 1 · Print a markdown file that somebody sent you

Small, universally understood, checkable in under a minute — the kind of entry that earns the credibility the larger claims spend.

|  | A markdown file in a vault | A markdown file on your disk |
|---|---|---|
| **Steps** | **2** — open the file in the vault UI (it renders), press **Print** | **3–5**, depending on what you already have: many editors render markdown but print the *source*; the common workarounds are convert-to-HTML, paste into a browser, or install something |
| **Prerequisites** | A browser | An editor that both renders *and* prints, or a converter, or an online tool |
| **Privileges granted** | None beyond the key you already hold | None — *unless* you use an online converter, which is `scope:file · ops:read · bearer:vendor-server · withdrawal:none`. Uploading a document to a stranger to reformat it is a privilege grant that does not feel like one |
| **Where it runs** | Your browser; the print component renders locally | Your machine, or a stranger's |
| **Verified** | **hand-checked, 2026-08-16** — the vault UI exposes a **Print** control on an open markdown file, backed by `SgPrint.printMarkdown`; confirmed present and reachable in a browser driven with a published read key |
| **Re-run it** | Open `https://dev.vault.sgraph.ai/#sgit_rk1_0a0f34839d737eef0f8f66e5236990b1f397af064763e3f71dca2717015f9d15:3d04e6b9ca98`, go to the vault browser, click `README.md`, look for **Print**. For the other column, take any `.md` file and try to produce a formatted page with whatever you already have installed — count what it takes |

**What would change this entry:** an editor that renders and prints markdown in one action, which several are close to. If you know one, that column's step count should drop and this entry should say so.

### 2 · Take access back after you have shared something we lose this one

A comparison where our column always wins is discounted on sight, so here is one where the mainstream answer is straightforwardly better.

|  | A vault, shared by read key | A hosted document, shared by link |
|---|---|---|
| **Steps to withdraw** | **Rotate the key and re-publish.** Future commits are protected | **1–2** — remove the share; the next request is refused |
| **Does it reach what they already have?** | **No.** Anything already fetched stays readable forever, with no way to reach it | **Largely yes** — unless they exported or screenshotted, the server stops serving it |
| **privileges** | `withdrawal:future-only · mediation:key · observability:none` | `withdrawal:effective · mediation:server-enforced · observability:per-reader-log` |
| **Why** | Possession of a key *is* access, so there is no server in the loop to refuse a later request. The objects are content-addressed and immutable — the same id returns the same bytes forever, which is exactly what makes an already-taken copy permanent |
| **Verified** | **machine-verified** — the immutability that causes this is checked automatically (`objects-immutable` below). The hosted-side behaviour is **hand-checked, 2026-08-16**, and is the ordinary documented behaviour of mainstream sharing |
| **Re-run it** | `python3 admin/build/compare_tests.py` — the immutability check fetches one object twice and compares bytes |

**The honest summary:** if the ability to revoke access after the fact matters more to you than the host being unable to read your content, a server-mediated platform is the better tool and you should use one. Vaults trade revocation for the host knowing nothing. That is a real trade, not a free win.

### 3 · Let a program record data for you without letting it change your records

The differentiator. Note that the step counts are similar — it is the privileges column that separates these, which is why it is the column to lead with.

|  | A vault app | An assistant with folder access |
|---|---|---|
| **Steps** | Declare the grant in `app.json` and open the vault | Grant access to the folder, then run it |
| **Privileges granted** | `scope:folder(adherence/) · ops:write,mkdir · mediation:key+host` — read broadly, but write to **one folder**. The app cannot alter the records it reports on | Typically `scope:folder · ops:read,write · bearer:vendor-server` for the whole shared folder — the granularity available is the folder you shared |
| **Where it runs** | Your browser, in a sandboxed frame with an opaque origin | Usually the vendor's infrastructure, with your files sent to it |
| **Survives the vendor** | The data is files with a documented layout; the reader is replaceable (we wrote a ~170-line one to prove it) | The conversation and any generated artefacts live where the vendor put them |
| **Verified** | **machine-verified** — `scoped-write-declared` below reads the live vault's `app.json` and asserts the write scope is exactly `["adherence/"]`. The comparison column is **hand-checked, 2026-08-16** and describes the general shape of folder-level sharing, which varies by product — corrections welcome, per-product rows to follow |
| **Re-run it** | Open the [Supplement Stack vault](../demos/vaults/supplement-stack/index.md) and read its `app.json`, or run `python3 admin/build/compare_tests.py` |

**The caveat that keeps this honest:** read granularity is coarser than write granularity here. A read key opens the *whole vault*, not one file. Finer read boundaries mean separate vaults with separate keys, decided in advance — granularity costs structure. If you need per-file read control without pre-planning the shape, this is not yet the tool.

## The checks behind the machine-verified rows

These run against the live service using only published read keys, and each states what would make it fail — a test that cannot fail is not evidence.

Loading results…

## What is deliberately not here

| Not here | Why |
|---|---|
| Anything we plan to ship | A comparison page is exactly where planned capability must not sit beside shipped capability. One unshipped row and a reader re-reads every other row as marketing |
| Ease-of-use scores | A judgement published by a participant is the thing this page cannot defend. Steps, prerequisites and privileges are facts |
| A deployment-features comparison | It would be the most linked and the fastest to rot, and our own story has a caveat worth resolving first: a vault's files are portable, but the polished viewer is currently one hosted implementation |
| A maturity model | Those score an organisation's practice over time. This scores a task against a tool stack on a date — a different instrument |


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/compare/index.html)*
