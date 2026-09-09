# Two games about agent permissions — a published vault

> Two deterministic games about grants, permissions and mandates — and the first vault published here that phones home. Anonymous usage events go over a write-only append lane to a separate private vault, disclosed on every page with a pause switch. Built by another agent from the build brief on this site.

*Source: <https://sgit.ai/demos/vaults/agent-permission-games/index.html> · site v0.2.69 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../../index.md) / [Vaults](../index.md) / Two games about agent permissions

# Two games about what an agent can do — and the first vault here that phones home

Two deterministic games about grants, permissions and mandates, in one vault. What makes it worth a page beyond the games: it is the first vault published here that **sets out to send anything anywhere** (it is not yet succeeding — see the status note below), and it was built by another agent from [the build brief on this site](../../../briefs/vault-telemetry-append-lanes.md) — which makes it the first end-to-end test of whether a brief written for an agent actually produces the thing it describes.

**Open it yourself — the key is the whole credential.**
 Read key: `f94c8b1d42352d95703ac3d39032735d9b4e388d16ab5b87c948928d8e111118:4evnlwrj`
 In the official UI: [open it read-only in a new tab](https://dev.vault.sgraph.ai/#f94c8b1d42352d95703ac3d39032735d9b4e388d16ab5b87c948928d8e111118%3A4evnlwrj) · From the CLI: `sgit clone f94c8b1d42352d95703ac3d39032735d9b4e388d16ab5b87c948928d8e111118:4evnlwrj`
Published as a read key, derived from the write credential that was submitted. The vault key is not published and never will be.

**This vault phones home, and you should know that before you open it.** Opening a vault does not normally send anything anywhere — that is the platform default, and every other vault published here honours it. This one sends **anonymous usage events** while you play: which screens you reach, the answers you give, your score. No name, no id, no fingerprint, no URL, no referrer. Every page carries a notice and a **pause sending** switch, and `telemetry.html` inside the vault states exactly what leaves. We publish it *because* it does this, not despite it — but the warning belongs above the fold rather than in a footnote.

**Status, 7 September:** as published, the events are *built and never sent* — the frame's content-security policy blocks the call, for reasons [set out below](#findings). Treat this box as describing what the vault is designed to do and will do once one line of its manifest changes, not what is reaching anyone today.

## See it live, here

[Open the vault in a new tab ↗](https://dev.vault.sgraph.ai/#f94c8b1d42352d95703ac3d39032735d9b4e388d16ab5b87c948928d8e111118%3A4evnlwrj)Two games with a full-width board — they have far more room in their own tab than in the frame below.

## The two games

which agent is it?

### A floor plan, and the wings you think it can enter

You think of an agent; cheap questions narrow the field; you chalk which wings of the building it can reach. Then the doors open and the **prediction gap** is shown per capability.

The board is the interesting part. Capabilities are drawn as rooms grouped into wings — filesystem, identity, process, code, network, communication, schedule, money, browser — and the legend distinguishes **chalk** (asserted, you drew it), **pencil hatching** (inferred, the plan says), **dotted** (possible, still consistent) and plain (no visitor above 5% holds a key). A belief column ranks nine public profiles by likelihood as you answer.

It is careful about what a drawing is: *"a room is a rendering choice, not a place — rooms are not ordered, sized or adjacent by anything in the data."*

Mid-game: the plan, the belief column, and a question labelled `IDENTIFIES` that *“identifies and measures nothing”* — it never counts toward the gap.

what can it do?

### Two questions per capability: can it, and do you want it to

Name the agent and where you run it, and the board asks capability by capability *can it?* — with a confidence — and *do you want it to?* The end screen hands you **the mandate you assembled without meaning to**, the delta against the grant, and one thing to change.

The scoring is the argument. A wrong answer costs **−50** against **+30** for a right one and **0** for *don't know*, and the page says why: *"real grants are wider than people expect, so saying yes to everything would otherwise win."* Under the hood a yes is scored as 75% sure and a no as 25%, points are the squared-error rule, and the headline figure is calibration rather than score.

And **two fifths of the questions are above the ceiling** — things no agent anywhere can do — so the game measures over-crediting as well as underestimating. That is the mechanism that stops it being a quiz about vendor features.

The scoring panel, stated before you play — and the telemetry notice line sitting under it with a live `0 sent` counter.

## The disclosure page is the best thing in it

`telemetry.html` is reachable from every page, and it is the model for how this should be done. It opens by naming the default it is breaking — *"Opening a vault does not normally send anything anywhere. This one does"* — then says what is sent, how, and what it proves. The last part is the one most analytics pages never write:

> **What it proves.** Nothing about anyone. Anyone holding this vault's read key holds that token and could forge or flood the lane, so the receiving end treats every event as a claim.

The schema is published in the same place: one batch per flush, at most every 4 seconds and at most 40 times a session, carrying a 16-hex session id *minted in memory when the page opened and gone when the tab closes*. The events are named and tabulated, per game. `ua` carries a coarse form factor, a language and a host — and the schema states what is deliberately absent: no user-agent string, no screen size, no URL, no referrer, no IP.

Reachable from every page in the vault, and it names the platform default it is breaking in its first sentence.

## The credential audit — the whole point of the exercise

A vault that phones home must carry a credential to phone home *with*, and it is published with a read key, so that credential is public. This is exactly the case the [build brief](../../../briefs/vault-telemetry-append-lanes.md) was written for, so the audit was run against the brief's own claims rather than the vault's description of itself.

| Check | Result |
|---|---|
| Private key material anywhere | **none** |
| `enum_key`, `write_key`, `vault_key`, `read_key` fields | **none** |
| Vault-key shapes, `sgit_vk1_` / `sgit_private_vault_` prefixes | **none** |
| Third-party provider keys (OpenAI, Anthropic, GitHub, AWS, Google, Slack, JWT) | **none** |
| Email addresses, personal data | **none** |
| **64-hex strings in the entire vault** | **exactly one** — the append token, in five places |

That last row is the finding. One credential exists in this vault and it is the write-only one, which is the only shape that survives publication behind a read key.

**And the token was tested, not taken on trust**, because an append token and a read key are *both* 64 hex and a mistake between them would be invisible. Cloning the telemetry vault with it produces no `clone_mode.json` and decrypts nothing — and a control run with an all-zeros key behaves identically, which is what makes the test mean anything. It is not a read key for the vault it names.

## It took the fallback path, which is the right one

The brief said to verify whether `sg.append.write` works from a read-only session before building on it, since every player opens the vault with a read key and the authoring guide says read-only sessions fail closed. The implementation does not use the bridge at all:

```
const url = cfg.api.replace(/\/$/, '') + '/api/vault/append/write/' + cfg.telemetry_vault_id;
await fetch(url, { method: 'POST', headers: {…}, body, keepalive: !!final,
                   mode: 'cors', credentials: 'omit' });
```

A direct `fetch` to the account-less write endpoint, with `credentials: 'omit'` so no ambient cookie rides along and `keepalive` on the final flush so the last batch survives the tab closing. The payload is the `sgit pki` v2 envelope — RSA-OAEP-SHA256 wrapping AES-256-GCM — built with Web Crypto in the browser, so the same `sgit pki decrypt` reads it on the other side. If there is no secure context there is no Web Crypto, and the sender disables itself rather than falling back to plaintext.

**Consistent with this:** `app.json` declares no `permissions` key at all. The vault asks the host for nothing, because it does not need the host for this.

## Two findings, published rather than filed

**1. Two of the four pages still tell the player nothing is sent.** `what-can-it-do` gets it right — its footer says *"in this tab, no model, no server, nothing **stored**"*, with the sending notice above it. But the home page still reads *"no model, no server, nothing **sent**, nothing stored"*, and `which-agent-is-it` carries *"No model, no server, nothing sent"* in its footer **on the same screen as** the notice saying events are sent. That game also describes its run tuple as *"shown, never sent"* with *"no send button"* — true of the button, but its `question` and `reveal` events carry substantially the same answers automatically. The pattern says the wording was fixed in one game and missed in the other two. Nothing leaks; the disclosure is simply contradicted by leftover copy, which matters more than usual in a vault whose subject is informed consent.

**2. RESOLVED, 7 September: the telemetry does not currently leave the browser, and the reason is a CSP this vault cannot satisfy.** When this page first went up we could not confirm the write endpoint and recorded it as unresolved. The SG/API team then reviewed the append code against [our brief](../../../briefs/vault-telemetry-append-lanes.md) and supplied the answer.

 A vault app's frame is served with `connect-src blob: data:`. A **direct `fetch`** to the API is therefore blocked before it leaves, unless the app declares `permissions.network: true` — and `app.json` here declares **no permissions at all**. So the sender is well built and cannot fire. That matches what the author reports: no events have arrived.

**The fix is not `network: true`.** That reopens every egress from a frame holding decrypted vault content. The bridge is the right path, and the reason our brief steered away from it was **our error**: we said `sg.append.write` fails closed in a read-only session, and the review found there is no read-only gate on append at all. One grant does it — `{"permissions": {"append": {"write": true}}}` — and `write` is the one verb that takes another vault's id.

Two more things the review settles for anyone reading this as a worked example. A grant that appears to be ignored is usually a **manifest** problem rather than a gate: a release pin makes `app.json` come from a pinned commit rather than HEAD (and forces read-only for everyone, owner included), and a folder-level `app.json` replaces the root one wholesale. And `append.new-messages` would never have fired here whatever was declared — the checker only ever watches the *open* vault's own lane, so it belongs in the telemetry vault's dashboard, not in the games.

## Notes

**68 files, 2.6 MB, version 0.8.1 across 9 releases**, with a version badge on every page and a release history at `version.html`. Both games ship their readable source beside the built page — engine as an ES module, `selftest.json`, the data snapshot, the build script — each with a README carrying a rules table and a *does-not-prove* list.

**The data is vendored, and says so.** Both games run on a copy of the profiles, capability primitives, reach mesh and reductions from [pki.sgit.ai](../../../network/pki.md), taken 2026-09-06 and inlined, with the date shown in the header of every screen.

**Screenshots were captured with the telemetry blocked at the network layer**, so driving the games to photograph them did not put a run into somebody's real lane.

**Nine public profiles, not a directory of anybody's setup.** `profile` in an event is which *public* profile a player picked from a list; the scoring is arithmetic over that public profile. The schema is blunt about the limits: *"Not a count of people (sessions are tabs). Not evidence."*

[← The build brief this was built from](../../../briefs/vault-telemetry-append-lanes.md) · [All published vaults](../index.md)


---

*[Site index for agents](../../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/agent-permission-games/index.html)*
