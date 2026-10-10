# Long Tail Ledger, who pays to keep old machines working, sgit.ai

> A data-science vault on the economics of open source's long tail: one old iMac, the long tail measured from Homebrew and PyPI analytics, where money flows for old versions, the payment problem, five funding models simulated with break-even prices and a sensitivity tornado, the satellite support firms, and a calculator. Published with its read key.

*Source: <https://sgit.ai/demos/vaults/long-tail-ledger/index.html> · site v0.7.29 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../index.md) / Long Tail Ledger

# Long Tail Ledger: who pays to keep old machines working?

A data-science vault on the economics of open source's long tail: the old versions, old platforms, small users and customised builds that projects are not paid to support. It starts from one Intel iMac that could not run Homebrew or Docker Desktop, measures the long tail from Homebrew and PyPI analytics, sets out where money does flow for old versions and where it does not, shows what card fees do to a payment of pence, and simulates five ways to pay for it over 10,000 seeded draws. Every number is a sourced fact or a labelled assumption with its range and reason. It is a model, not a forecast. It was published with the article [Open source is not free: who pays to keep the long tail working?](../../../articles/open-source-is-not-free.md)

The short answer first, every number with its source or assumption id.

**Open it yourself. The key is the whole credential.**
 Read key: `sgit_public_read_12766388a2df439ffb439ef149470b4ae21e2a4aefa8d73db6e7ba6013b7a4d5:deqiwj7z`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_public_read_12766388a2df439ffb439ef149470b4ae21e2a4aefa8d73db6e7ba6013b7a4d5%3Adeqiwj7z) · From the CLI: `sgit clone sgit_public_read_12766388a2df439ffb439ef149470b4ae21e2a4aefa8d73db6e7ba6013b7a4d5:deqiwj7z`
Published deliberately under the `sgit_public_read_` prefix, and **derived** one-way from a vault key kept in the gitignored tier and never published. Classified with `check_credential.py` before it touched this page, read back with the published key alone by `catalogue_derive.py`, and verified with an all-zeros read key as the negative control. Created, pushed and audited with sgit-ai 0.20.0.

## See it live, here

The vault opens as an app: the question, one old iMac, the long tail, where money flows, the payment problem, five models, break-even, sensitivity, the satellites, your numbers, and every source and assumption. You can also [**open it in the official UI**](https://dev.vault.sgraph.ai/#sgit_public_read_12766388a2df439ffb439ef149470b4ae21e2a4aefa8d73db6e7ba6013b7a4d5%3Adeqiwj7z).

## The one idea

The long tail of open source has value to the people on it and no revenue stream back to the people who would have to support it. Where a vendor owns the code, the same need, "keep the version I have working and safe", is a large business: Oracle's support revenue, Red Hat's subscriptions, Windows 10 extended security updates. The vault asks what it would take for open source projects to earn from that need, at prices from pence to pounds, and answers with data and a simulation you can rerun with your own numbers.

## What is in it

one old iMac

### What failed, why, and what the story got wrong

Twenty-six dated case facts: Homebrew's installer refuses every Intel Mac since September 2026; Docker Desktop needs macOS 14 since 4.49; Ventura's last security update was 13.7.8 on 20 August 2025; the python.org installer runs on Ventura, but the built-in python3 is a stub. And the corrections: only 2017 iMacs stop at Ventura, and MacPorts still supports it.

Each failure has a date and a reason.

measured

### The long tail, from Homebrew and PyPI

6.99% of Homebrew macOS install events in the last 30 days, and 16.66% over a year, came from versions older than the newest three; 3.32% to 5.43% from Ventura or older. 18.55% of pip downloads run on end-of-life Python. Shares of install events, not machines, with the caveat on every chart.

Computed from the raw analytics in the vault.

where money flows

### Support prices per machine per year, against voluntary funding

From 10p a year per GitHub developer through GitHub Sponsors to £375 for an Ubuntu Pro server; Oracle's $19.8bn of support revenue; Red Hat's subscriptions at about 93% margin; Rimini Street's $136,000 a year per client.

The same need, priced very differently.

the payment problem

### What a 20p fee does to a payment of pence

The fee as a share of a payment from 10p to £50 on seven rails, and what aggregation does: one annual charge covering many projects spreads the fixed fee until pence become viable.

Below about five pounds, the fixed fee is the price.

simulated

### Five funding models, 10,000 draws each

Donations, a seat licence with a size threshold, support that rises with age, micro-paid supported builds and customised builds for companies, for one project at Homebrew's scale and one long-tail target. With typical conversion, micro-paid builds cover the cost in about six draws in ten, companies' builds in 94%, donations in 24%.

The same draws for every model.

break-even

### The price that pays for the long tail

About £1.80 a machine a year covers the cost in half the draws with typical conversion, and 70p with great conversion. No price from 50p to £25 reaches nine draws in ten, and with pessimistic conversion none reaches half.

The answer to "from cents to pounds".

sensitivity and satellites

### What matters most, and who else could live off it

The tornado: install events per machine, willingness to pay and the share of machines on the long tail move the answer most. The satellites: about 18 small support firms worldwide from one project's pool, and Rimini Street as the proof that the market exists where money flows.

The biggest uncertainty is how many machines there are.

your numbers

### A slider for every assumption

The same model runs in the page, with the same seeded draws and the same arithmetic as the Python model. The release gate compares them on 77 grids of inputs, 13,408 numbers, at zero tolerance.

Disagree with an assumption? Move it.

## How it is built

The research is in `research/economics.md` and `economics.json` (175 entries, each with its source, date, verbatim quote and a verified flag) and `research/case.md` (26 case facts), with the raw Homebrew and PyPI analytics it reads in `research/dl/`. Every assumption is in `data/assumptions.json` with its value, range and reason. `tools/model.py` writes everything in `data/` from seeded random numbers, and `docs/method.md` gives every formula in plain English. The app is on the design system of the earlier vault apps, its charts drawn in SVG to the rules of a data-visualisation skill: one axis, fixed hue order, a table view and a hover tooltip on every chart, and the palette validated for colour-vision deficiency in light and dark themes. `tools/gate.py` runs 18 checks, among them: the data reproduces byte for byte; the measured shares match their sources; every fact cites a source and every assumption is listed; the browser model equals the Python model exactly; no credential shape, em-dash or unsupported absolute; and every view renders at desktop and phone widths with no errors and no network requests.

## The audit, honestly

**What was scanned.** Every file before the first commit, and every file again after cloning with the published read key alone: vault-key shapes, every `sgit_` credential prefix, private-key headers, cloud key shapes, the SG/Send access token, the vault's own key and its write key. The clone matched the source, file by file.

**What was found.** Nothing. The negative control, an all-zeros read key against the same vault id, returned nothing.

**What it does not claim.** It is a model, not a forecast. Willingness to pay, the installed base, the Intel share and company behaviour are not measured in public data; they are labelled assumptions, and the sensitivity view shows which matter most. Intel against Apple silicon could not be measured. No maintainer is named or criticised; companies and projects appear only for their published numbers and policies.

**Write-key status:** escrowed, in the gitignored credential tier, before this page was written.

## Derived facts

From `admin/build/catalogue_derive.py deqiwj7z <read key hex>`, read-only, no token, no clone.

- **Files:** 68 · **plaintext size:** 1767 KB
- **Commits:** 2 · **last updated:** 2026-10-10 · **HEAD:** `obj-cas-imm-5821c411310f`
- **Top level:** `PUBLIC.md`, `README.md`, `REALITY.md`, `app.json`, `app/`, `data/`, `docs/`, `index.html`, `research/`, `tests/`, `tools/`, `versions/`
- **File types:** .json ×26, .js ×17, .py ×8, .md ×7, .css ×7, .html ×2, .csv ×1
- **Vault app:** yes, entry `index.html` · **browser-renderable:** yes

## Notes

**Where this came from.** An Intel iMac given to my agents as a desktop, in October 2026; the arguments on [open-source.sgit.ai](https://open-source.sgit.ai/); and the earlier [Agent Desk](../agent-desk/index.md) vault on giving an agent a Mac of its own.

**Who wrote this.** [agent@riskmandate.ai](mailto:agent@riskmandate.ai) (Claude Opus 5.5, `claude-opus-5-5`), in the sgit.ai site session, for RiskMandate.ai and sgit.ai. AI-generated text, disclosed as Article 50 of the EU AI Act asks; the person with editorial responsibility is Dinis Cruz. Replies to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

[← All published vaults](../index.md)


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/long-tail-ledger/index.html)*
