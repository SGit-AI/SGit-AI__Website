# Reading a vault from a *.sgit.ai site page — build brief

> For devs coding the estate’s sites: the vault API answers plain CORS GETs with no auth header, so a site page reads ciphertext directly and decrypts in the visitor’s browser. The house reader to copy rather than rewrite, the trust rule that inverts on this surface, the ref-caching trap, and the prompt to hand the site’s agent.

*Source: <https://sgit.ai/docs/briefs/sgit-ai-site-pages.html> · site v0.2.76 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../index.md) / [Briefs](index.md) / Reading a vault from a site page

**Surface:** a page on a `*.sgit.ai` site — outside every vault host. [The other two surfaces →](../surfaces.md)

# Reading a vault from a `*.sgit.ai` site page

A build brief for whoever is coding one of the sites in this estate. Vault content can be published on an ordinary web page — indexed, linkable, readable with no key and no account — because the vault API answers **cross-origin GETs** and the decryption happens in the visitor's browser. This is the surface with the most reach and the least protection, and the two facts are related.

**The enabling fact, in one line.** `GET /api/vault/read/<vault_id>/…` is a plain CORS request with **no auth header**, from any origin. The server can afford that because what it returns is ciphertext under a key it has never held — so `graphs.sgit.ai`, `risks.sgit.ai` or any other site can read a published vault directly, with no proxy, no backend and no build step.

## Do not write the reader

It already exists, it is small, and it is deliberately in the open so you can copy it rather than reimplement the derivations:

| File | What it gives you |
|---|---|
| `assets/vault-embed.js` | The reader, ~90 lines — import the key, derive the ref id, fetch, decrypt, walk commit → tree → blob, `readText` / `readBytes` by path. It exports `SGVaultEmbed.Reader` so nothing else has to copy the derivations. It also mounts a whole vault app in a sandboxed frame if that is what you want |
| `assets/vault-docs.js` | The same reader with cache accounting and a markdown renderer — the instrumented version, useful when you want to show a reader what the page actually fetched |
| `assets/vault-deck.js` | A worked viewer built on the reader: [decks and PDFs](vault-decks-on-a-site.md), with the sandbox policy already right |
| `assets/vault-ui-embed.js` | Frames the official SG/Vault UI on your page, read-only, from a read key — when you want the whole product rather than a view of it |

All four are on this site under `/assets/` and are MIT-spirited house code: copy them into your site, do not fetch them across origins at runtime. The mechanism they share is written up at [**Reading one file out of a vault**](../vault/reading-a-vault-file.md).

## The rule that changes on this surface

Inside a vault host, the host protects the reader: it sandboxes apps, gates permissions, and keeps a sovereignty rail the app cannot suppress. **On your site there is no host. You are the host.** And the bytes you are rendering were written by whoever holds that vault's write key, which is a different question from who can read it.

So the rule inverts, and it is the single most important thing on this page:

> **The viewer is the site's. The data is the vault's. A vault must be able to change what is shown, and never what the page does.**

| Vault content | How to render it |
|---|---|
| **Text and numbers** | Escape it. It is a string from a third party, and it belongs in `textContent`, never in `innerHTML` |
| **Markup — a document, a slide** | `<iframe sandbox>` with **no**`allow-scripts`, plus a CSP of `default-src 'none'; img-src data:; style-src 'unsafe-inline'`. Static content does not need scripting, so switch it off rather than contain it |
| **Anything that must run** | `<iframe sandbox="allow-scripts">` — opaque origin, no `allow-same-origin`, ever — and serve its reads over `postMessage`. **Never `eval` vault code in your page.** |
| **Images** | Decrypt them yourself and pass `data:` URIs in, or mint blob URLs *inside* the frame. A vault path in a `src` resolves against an opaque origin and 404s |
| **PDFs** | Download, never embed. Chrome refuses to render a PDF in a sandboxed frame, and un-sandboxing it to make the viewer work defeats the point |
| **Links inside vault content** | Rewrite or restrict them. A link is a place a vault author can send your visitor |

## Keys, on a page anyone can view source on

- **A read key belongs in the page.** That is what it is for — it is derived one-way, it cannot be turned into write access, and printing it is how a reader clones the vault themselves. Put it in the markup where a human can copy it, not only in a script.
- **A vault key must never touch a site.** It is write access. There is no such thing as a partly-public vault key.
- **Grep the built site before every release**, and make it a step that can fail the build rather than a habit. This site's release aborts on a key-shaped match.
- **A credential scan built for sgit shapes will not catch other secrets.** We nearly published an OpenRouter key sitting in a vault file, in a field called `openrouter_key`, that matched none of the sgit patterns. Scan for what the vault holds, not only for what sgit issues.

## Two things that will bite a site dev specifically

- **Cache immutable objects, never the ref.** An object id containing `-imm-` is content-addressed and safe to cache forever. The ref is the mutable HEAD pointer, and caching it fails *silently*: the page renders an older commit from perfectly valid ciphertext, so nothing errors and the content is simply stale. Keep a short freshness window on the ref instead.
- **Decide what happens when the vault moves ahead of your page.** A vault can be pushed to at any time, and your site rebuilds on its own schedule. Either read live and accept that your prose may describe an older state, or snapshot at build time and say so. What breaks trust is a page that reads live in one panel and from a stale snapshot in the next without telling anyone which is which.

## What not to put on this surface

Reach is the point of a site page, so the failure mode is putting things there that should have stayed in the vault:

- **Do not duplicate vault prose into the page.** If a paragraph exists in both, they will disagree, and the vault is the one that is right. Render it from the vault or link to it.
- **Do not rebuild the vault's app.** If a visitor needs the full thing, frame the official UI or link them to it with the read key.
- **Do not make the site the only way to read the vault.** The read key on the page should be enough for anyone to bypass your site entirely. If it is not, something is being withheld that should not be.

## Before you call it done

- Every frame holding vault content has a `sandbox` attribute, and none has `allow-same-origin`.
- No vault string reaches `innerHTML` unescaped and unframed.
- The page works from a cold cache and from a warm one, and a fresh push shows up within your stated freshness window.
- The built site has been grepped for vault-key shapes and for other credential shapes, as a build step that can fail.
- The read key is visible to a human reading the page, not only to the script.
- A visitor with no key, no account and nothing installed can read the thing you published.

## The prompt to hand the site's agent

```
Publish content from vault VAULT_ID on SITE, read live with the published read
key READ_KEY.

Read https://sgit.ai/docs/surfaces.md first to confirm a site page is the right
surface, then https://sgit.ai/briefs/sgit-ai-site-pages.md, then
https://sgit.ai/vault/reading-a-vault-file.md for the mechanism.

Do not write the reader. Copy assets/vault-embed.js from sgit.ai, which exports
SGVaultEmbed.Reader; assets/vault-deck.js is a worked viewer built on it. Copy
them into the site rather than fetching them across origins at runtime.

The vault API answers plain CORS GETs with no auth header, so no proxy and no
backend is needed. The bytes are ciphertext; decryption happens in the visitor's
browser.

The rule: the viewer is the site's and the data is the vault's. A vault must be
able to change what is shown and never what the page does. Vault text is escaped
into textContent. Vault markup goes in a sandboxed frame with no allow-scripts
and a default-src none CSP. Anything that must run goes in a sandboxed frame
with allow-scripts and never allow-same-origin, served over postMessage. Never
eval vault code in the page origin. PDFs are downloads, not embeds.

Cache objects whose id contains -imm-; never cache the ref, because a stale ref
renders an older commit from valid ciphertext and nothing errors.

Print the READ key where a human can copy it. Never put a vault key on a site.
Add a build step that greps the built output for key shapes and fails.

Report: what is read live vs snapshotted at build time, and how a visitor with
no key reads the published content.
```

This is one of [three surfaces](../surfaces.md); the guidance for the other two is [content authoring](../vault/content-authoring.md) and [vault apps](../vault/vault-apps.md). [All briefs](index.md) · [A worked example on this surface](vault-decks-on-a-site.md)


---

*[Site index for agents](../../llms.txt) · [HTML version](https://sgit.ai/docs/briefs/sgit-ai-site-pages.html)*
