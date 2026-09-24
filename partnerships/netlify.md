# A proposed partnership between sgit.ai and Netlify

> Netlify already hosts the kind of thing a published vault is. A vault can be read from a plain static host behind a CDN: the browser fetches ciphertext and decrypts it locally, with no server at all. Netlify is named in our static hosting guide for exactly that. The partnership we would like is to make "an encrypted site, readable only with a key, updated with a push" a documented pattern on Netlify.

*Source: <https://sgit.ai/partnerships/netlify.html> · site v0.6.6 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Partnerships](index.md) / [Cloud platforms](cloud-platforms.md) / Netlify

A proposed partnership · sgit.ai with Netlify · public material only · 24 September 2026

# A proposed partnership between sgit.ai and Netlify

**Netlify already hosts the kind of thing a published vault is.** A vault can be read from a plain static host behind a CDN: the browser fetches ciphertext and decrypts it locally, with no server at all. Netlify is named in our static hosting guide for exactly that. The partnership we would like is to make "an encrypted site, readable only with a key, updated with a push" a documented pattern on Netlify.

**Nothing on this page is confidential, and there has been no conversation yet.** Every statement about Netlify comes from its own public pages, linked. Every statement about sgit points at the [deployment documentation](../deploy/index.md), a published vault or a page on this site. sgit is Apache-2.0, so Netlify does not need our permission to run it or to build on it. A partnership is about doing that well and together. The general argument is on [the cloud platforms page](cloud-platforms.md).

## In short

- **Static hosting is the whole requirement.** A published vault is static files. Netlify's CDN serves them; the reader's browser decrypts them.
- **Named in the docs already.** The static hosting guide lists Netlify with GitHub Pages, S3 with CloudFront, Cloudflare Pages and Firebase.
- **The server is not needed for readers.** Netlify Blobs is key-value storage rather than S3, so the writing side of a vault stays on a vault server elsewhere; Netlify serves the published copy.
- **What we would like:** a documented pattern, and a place among [Netlify's technology partners](https://www.netlify.com/partners/technology/).

## How vaults map onto Netlify

| sgit needs | On Netlify | Status |
|---|---|---|
| **Static readers** | Netlify's CDN | Documented in our static hosting guide. |
| **Publishing on push** | Netlify builds from a Git push | Should work: publish the vault's ciphertext as the site. Not tested end to end. |
| **The writing side** | A vault server elsewhere | Netlify Blobs is not S3-compatible, so writes stay on a vault server. |

## Where we are with Netlify today

Netlify is already in the static hosting guide. We have not published a vault there ourselves yet; this site is on GitHub Pages. The pattern is simple enough that the first piece of work is a short guide and one live example.

## What a partnership could be

| Shape | What it would be | On their side |
|---|---|---|
| **1 · A documented pattern** | An encrypted site on Netlify: the vault's ciphertext deployed as static files, opened with a read key. | A technical reviewer. |
| **2 · An integration** | A Netlify integration that publishes a vault's current state on every push. | The Technology Partner Program. |
| **3 · Open-source hosting** | sgit's own documentation vaults hosted under the Netlify Open Source plan. | Netlify's open-source programme. |

## What we are asking Netlify for

1. A review of the static hosting pattern for Netlify.
2. A place in the [Technology Partner Program](https://www.netlify.com/partners/technology/).
3. A look at the [Netlify Open Source plan](https://www.netlify.com/legal/open-source-policy/) for sgit's documentation.

## What this page does not claim

- **No endorsement.** Netlify has not endorsed sgit, and we have not spoken to anyone there about this. Programme and product descriptions quote Netlify's own pages as of 24 September 2026.
- **Only the read side fits Netlify.** Writing to a vault needs a vault server, which runs elsewhere.

## If you work at Netlify

This page is written to be forwarded as it is, and everything on it can be checked by the person who receives it. [Who is asking, and how to reach them →](../about/index.md)

[← Rackspace Technology](rackspace.md)[Cloud platforms →](cloud-platforms.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/partnerships/netlify.html)*
