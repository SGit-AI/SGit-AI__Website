# Vault App Mode — a published vault

> Nine progressive proof-of-concepts and a four-page demo showing how to load CSS, JavaScript and data inside an encrypted vault — including a fifteen-test harness over the vault filesystem, and the audit that found the original could not be opened by a read key at all.

*Source: <https://sgit.ai/demos/vaults/vault-app-pocs/index.html> · site v0.2.46 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../index.md) / Vault App Mode

# Vault App Mode — nine POCs and a demo

The simplest vault on this site, and the one to read first if you are going to build one. Nine proof-of-concepts climb from a single inline HTML file to a fifteen-test diagnostic harness over the vault filesystem, then a small four-page app puts the lot together. It answers one question end to end: how do you load CSS, JavaScript and data when your files live in an encrypted vault instead of on a web server?

**The one problem everything here solves.** The HTML parser fires requests for `<link>` and `<script src>` the moment it meets them — before the vault bridge has patched `fetch`. Those requests hit the iframe's blob origin, where no files exist, and 404. So vault pages load their resources at *runtime*, with `sg.loadCss()` and `sg.loadJs()`. Every POC in this vault is a consequence of that one race.

**Open it yourself — the key is the whole credential.**
 Read key: `sgit_rk1_05f2391f22e4135ea27bca6b697dca18c54ab91b046325bef74f62f5324b8bc8:xth1xt78`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#sgit_rk1_05f2391f22e4135ea27bca6b697dca18c54ab91b046325bef74f62f5324b8bc8%3Axth1xt78) · From the CLI: `sgit clone sgit_rk1_05f2391f22e4135ea27bca6b697dca18c54ab91b046325bef74f62f5324b8bc8:xth1xt78`
Published deliberately. It grants read, and only read. This is a republication — the vault this content was authored in could not be opened by a read key at all, for a reason worth reading in the audit below.

## See it live, here

Both surfaces open automatically below. You can also [**open the app in its own window ↗**](https://dev.vault.sgraph.ai/#sgit_rk1_05f2391f22e4135ea27bca6b697dca18c54ab91b046325bef74f62f5324b8bc8%3Axth1xt78).

## What this vault demonstrates

| Feature | How this vault uses it |
|---|---|
| **Runtime resource loading** | `sg.loadCss()` and `sg.loadJs()` fetch vault files through the bridge and inject them, because declarative tags lose the race against the parser. POC-02 and POC-03 isolate each one; POC-04 shows dependency order between modules |
| The filesystem, read and written | `sg.vfs.readText()` in POC-07, `sg.vfs.write()` in POC-08 — which persists a real JSON file into the vault and lists it back. Writes are **local-first**: they live in the working copy until an `sgit push`, and the POC says so rather than implying instant durability |
| **A test harness for the platform itself** | POC-09 is the unusual one: fifteen graded operations over `sg.vfs` — read, write, list, nested folders, binary round-trips, deliberate error cases, path-variant comparison — each showing the exact call, the raw result, per-assertion pass/fail and timing. It exists because guessing at the API's behaviour cost a session; instrumenting it settled the question |
| Paths, the thing that actually bites | `sg.vfs` takes **vault-absolute** paths, and a page's own folder is knowable only from `sg.app.selfPath` — `location.pathname` is always `/` inside the iframe. The vault documents this as its most important rule, and POC-09's environment readout prints the ground truth |
| FOUC handled deliberately | pages hide the body until their CSS resolves, then reveal by **removing a class**. The distinction matters: clearing an inline style cannot override a stylesheet rule, which is exactly the bug this vault was carrying when it arrived (see the audit) |
| Its own failure modes, on a page | the survey ships a **Try the failure modes** panel that attempts writes which *should* be rejected — path traversal, URL-encoded traversal, a protected `.vault-settings.json`, a null byte, a 1500-character path — so the guards are demonstrated rather than asserted |
| The reasoning ships with it | `_docs/` carries a field guide (the canonical page skeleton and path rules), a gotchas manual written by symptom, and a debrief explaining why the code looks the way it does. It is the best-documented vault on this site for its size |

## What is going on here, step by step

The embeds above are the real vault, which makes it easy to scroll past the parts that matter. Each row points at one of them. Every screenshot is of this vault, driven by a script holding nothing but the published read key.

what opens

### A contents page, not a file listing

Opening the read key lands on the POC hub — `app.json` sets `entry` to `_poc-hub/index.html`. The steps are numbered like a magazine contents page, each card tagged with the API it exercises and a difficulty level, with the diagnostic lab and the demo as full-width cards beneath.

It is worth noticing what this *is*: a static HTML file in an encrypted store, rendering as a navigable site, with no server anywhere in the path.

The hub — nine numbered steps, tagged by the API each one exercises.

the baseline

### POC-01: everything inline, so nothing can fail

The first step deliberately has no external files at all — CSS in a `<style>` block, JS in a `<script>` block. It is the control case: if this renders, the vault is serving your HTML correctly and anything that breaks later is about *resource loading*, not about the vault.

It is also the one page that does not use the shared stylesheet, because loading one would contradict the point it is making.

The control case — no external files, so nothing can 404.

the fix, isolated

### POC-02: one CSS file, loaded at runtime

The smallest possible demonstration of the pattern. One `sg.loadCss()` call in a head script, and the FOUC guard around it: the body starts hidden and is revealed when the promise settles — *including* when it rejects, so a failed load leaves a readable page rather than a permanently invisible one.

The status pill on the page reports the load lifecycle as it happens, which makes the async step visible instead of theoretical.

One `sg.loadCss()`, with the reveal guarded on both outcomes.

order matters

### POC-04: two modules, and the dependency between them

Once JavaScript arrives at runtime, load order becomes yours to manage. `utils.js` must execute before `app.js` can call into it, so the POC awaits them in sequence and logs each step with a `[poc-04]` prefix.

The parallel case is covered too: independent resources go through `Promise.all`, because serialising things that do not depend on each other is just a slower page.

Sequential where there is a dependency, parallel where there is not.

data

### POC-05: `fetch()` works, because the bridge intercepts it

Once the bridge is installed, an ordinary `fetch('data.json')` resolves against the vault. No special API, no rewriting of your data layer — the call you would already have written works, which is the point of intercepting `fetch` rather than replacing it.

This is the step where a vault app stops looking exotic and starts looking like a normal front end that happens to have an encrypted origin.

An ordinary `fetch()`, resolved against encrypted storage.

writing

### POC-08: a form that puts a real file in the vault

Submitting writes `responses/poc-08-<timestamp>.json` through `sg.vfs.write()`, then the page lists what is there and lets you edit or delete it. The delete control only appears if `sg.vfs.delete` actually exists — capability-checked rather than assumed.

The callout that matters is the honest one: writes are **local-first**. They live in the working copy until someone runs `sgit push`, which the vault demonstrated the hard way — a submission made in one browser session was gone from a fresh one until the push happened.

A real write, with the local-first caveat stated rather than glossed.

the interesting one

### POC-09: testing the platform instead of trusting it

Fifteen graded tests over `sg.vfs`, each card showing the exact call with its resolved arguments, the raw result, a live progress log, per-assertion pass/fail and a runtime in milliseconds. Above them, an environment readout printing `location.href`, `location.pathname`, `sg.app.selfPath` and the keys actually present on `sg.vfs` and `sg.app`.

It was built mid-project when path bugs kept multiplying, on the reasoning that the API should be measured rather than guessed at. It is the most transferable idea in the vault: when a platform surprises you, instrument it and keep the instrument.

A test harness for the vault filesystem, kept as part of the vault.

all together

### The cities demo: four pages, one data file

The demo hub offers a bar chart, a world map, a survey and a responses viewer — each tagged **READ-ONLY** or **WRITES** so you know what it will do before you click. The chart and the map read the same `cities.json` and render it two ways; editing that one file in the vault browser changes both.

This hub could not be reached at all before publication — see the audit. It is now linked from the POC hub, which is how you get here.

Four pages over one data file, each labelled with what it will do.

read and render

### The same data, drawn two ways

The bar chart reads `cities.json` through the bridge and draws from it directly. The map projects the same records onto an equirectangular world and doubles as a navigation test — proving that same-vault `<a href>` links resolve correctly between pages.

Nothing here is fetched from the network. The data, the code and the styling are all objects in the encrypted store, decrypted in the reader's browser.

One `cities.json`, rendered by two pages that never touch the network.

write, then read back

### The survey, and its own failure modes

The form writes a JSON file per submission and offers two submit buttons — the canonical `sg.vfs.write()` and the `window.sgVault.writeFile` alias — so you can confirm both produce identical commits.

Underneath is the panel worth the visit: **Try the failure modes**, six buttons that attempt writes which must be refused. Path traversal, URL-encoded traversal, the protected settings file, a null byte, a path past the length cap. A demo that shows you its guards working is a stronger claim than one that tells you they exist.

Two write paths, and six writes that are supposed to be refused.

list, read, aggregate

### The viewer — including the response that is trying to attack it

`sg.vfs.list()` enumerates the responses folder, `sg.vfs.readText()` reads each file, and the page aggregates live: total responses, average excitement, top role, total bytes. A **View raw** control dumps the unprocessed listing so you can see what the API actually returned.

The first card is deliberate. One stored response carries `<img src=x onerror=alert(1)>` in its name field, and the viewer renders it as *visible text*. It is a standing escaping test, kept in the data so that a regression on either render path would be obvious on sight — which matters, because that is a bug this vault actually had.

Three responses, aggregates computed live — and a payload rendered, correctly, as text.

the source

### Everything is readable, including the parts that explain it

The vault browser shows the whole tree under the same read key: nine POC folders, the shared stylesheet, the demo, and `_docs/` — a field guide, a gotchas manual organised by symptom, and a project debrief.

That last folder is why this vault is worth copying as a pattern. The code demonstrates the technique; the docs record what went wrong on the way, which is the part that usually evaporates when a project ends.

The tree under one read key — including the write-up of its own mistakes.

## The audit, honestly

This vault was reviewed before its key was published, and the review changed both the vault and what got published. Findings first.

**The submitted vault could not be opened by a read key at all.** Its read key decrypted every object correctly — verified by decrypting its HEAD ref by hand — but the reader could never *find* HEAD. sgit has two ways of assigning a vault's ref file id: `Vault__Crypto` derives it from the read key and vault id, while `Vault__Branch_Manager` falls back to `'ref-pid-muw-' + secrets.token_hex(6)` — a random value. This vault got a random one. Browser readers derive the id, so they looked in the right place for a file stored under a name nothing could compute. The CLI worked throughout, because it resolves HEAD through the branch index instead. sgit's own tooling states the consequence plainly: *"write_key, ref_file_id, and branch_index_file_id are not derivable from a read_key alone."* A read key published for that vault would have been a credential that decrypts everything and opens nothing — so the content was republished into a new vault, `xth1xt78`, created through the deriving path.

**The whole cities demo rendered blank.** Four pages set `body { display: none }` in a stylesheet and cleared it with `document.body.style.display = ''`. That clears an *inline* property which was never set; the stylesheet rule kept applying and the pages stayed invisible. The host said so out loud — *"App loaded but is showing nothing — hidden (display:none)"* — for the hub, the map, the survey and the responses viewer. Only the bar chart, which has no such script, was unaffected. Fixed by hiding through a class and removing it, which is the pattern the POCs already used and the vault's own gotchas file documents.

**The demo was unreachable.** `app.json` opens the POC hub; the hub linked only the nine POCs; and the demo's own hub linked back to it. A one-way door, with a third of the vault behind it. The hub now carries a card for it.

**Two survey pages pointed at files that were not there.** Both live in `demo-cities/survey/` but named `style.css` and `hub.html` as though they sat a level up, so each had a missing stylesheet and a dead back-link. Separately, both used relative paths for `sg.vfs` — `list('responses/')` returned *"No such path"* — which is precisely the gotcha this vault's own documentation warns about. They now derive the folder from `sg.app.selfPath`, the way POC-09 does, and normalise `entry.path` to absolute before reading, which was doubling the prefix.

**A stored-XSS gap on the error path.** The responses viewer escaped every field it rendered on the success path, and interpolated the filename and error text raw on its two failure paths. The vault contained an unlabelled XSS payload in a leftover test response, so someone had clearly probed this and fixed only the half that showed. Both paths now escape, and the payload has been kept deliberately — rewritten as a labelled escaping test, so the property stays visible in the UI rather than living in a comment.

**Removed, not fixed:** an empty zero-byte `check-undefined.html` referenced by nothing, and `POC_STRUCTURE.md`, whose guidance had been superseded by `_docs/` and whose structure diagram described a six-POC vault under a former name. `README.md` was rewritten for the same reason — it named the wrong entry point and omitted three POCs. Both files remain in the vault's history.

**The credential finding.** The vault's own documentation recorded the project's push token in plain text, three times, as part of the workflow instructions. Publishing a read key would have handed that out with the content. The token has been replaced with a placeholder; the instructions still read correctly. The vault is otherwise clean on credentials — no vault key inside its own files, no `sgit_vk1_` or `sgit_private_vault_` string, no `delete_auth`, no API keys or private-key blocks. All 57 files were fetched back after publication *using only the read key above* and re-scanned.

On data: the survey responses are the only personal-shaped content, and all three are invented for the demo. The rest is code, styling and documentation. The rule that goes with any published key applies here too: **revocation is not retroactive** — anybody who fetches these objects keeps them.

## Derived facts

57 files · 251 KB · 8 commits · HEAD `obj-cas-imm-4517bfe1735d` · app entry `_poc-hub/index.html` · 15 HTML, 12 JSON, 12 CSS, 10 JS, 6 markdown — derived from the read key alone by `admin/build/catalogue_derive.py`, the same derivation that populates [the catalogue](../../../catalogue/index.md), with no token and no clone.


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/vault-app-pocs/index.html)*
