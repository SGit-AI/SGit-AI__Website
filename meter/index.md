# SG Meter: a reading meter you can add to any website, sgit.ai

> One web component that charges readers a few pence a page from a balance kept in their own browser, by how far down the page they read; never blocks, allows a negative balance, lets a reader decline with a reason. Install, views, config, events, storage, theming, Stripe.

*Source: <https://sgit.ai/meter/index.html> · site v0.7.28 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Docs](../docs/index.md) / SG Meter

A library · v1.0.0

# SG Meter: a reading meter you can add to any website

One web component that charges readers a few pence a page from a balance kept in their own browser, by how far down the page they read. It never blocks a page, it lets the balance go below zero, it lets a reader decline to pay for a page and say why, and it turns what they read into picks. No server, no account, no cookies, no third-party script. It is what runs on this site: the balance in the top bar is it.

**What it is, and what it is not.** An honesty box, not a paywall. Everything it knows is in the reader's browser, so a reader can change their own balance, and the page a payment returns to cannot check the payment. That is a choice, made because of who reads a site like this one and what cheating would cost; it is argued in [the security model](security.md) and, with the numbers, in [who will game the reading meter](../articles/who-will-game-the-reading-meter.md). If you need a meter that holds money, this is the wrong library.

## Install

Copy two folders into your site, keeping their paths: the component and the base class it extends (it imports the base by a relative path).

```
assets/components/base/v1/v1.0/v1.0.0/sg-component.js
assets/components/sg-meter/v1/v1.0/v1.0.0/sg-meter.js
assets/components/sg-meter/v1/v1.0/v1.0.0/sg-meter-core.js
assets/components/sg-meter/v1/v1.0/v1.0.0/sg-meter.tpl
assets/components/sg-meter/v1/v1.0/v1.0.0/sg-meter.css
```

The paths are versioned and immutable, as in [the estate's JavaScript guidance](https://coding.sgit.ai/javascript/index.html): a fix is a new path, so a page that works today keeps loading the same files. Read them first; they are short: [the rules](../assets/components/sg-meter/v1/v1.0/v1.0.0/sg-meter-core.js) (no rendering), [the element](../assets/components/sg-meter/v1/v1.0/v1.0.0/sg-meter.js), [its styles](../assets/components/sg-meter/v1/v1.0/v1.0.0/sg-meter.css), [the base class](../assets/components/base/v1/v1.0/v1.0.0/sg-component.js).

Then, on every page, load the module once, give it a config, and say what the page is:

```
<!-- in the top bar -->
<sg-meter view="balance"></sg-meter>

<!-- at the end of the text: charges this page, shows what it cost and the "don't charge me" choice -->
<sg-meter view="page" kind="article" date="2026-10-10" topics="news pricing" title="The page's title"></sg-meter>

<script type="application/json" id="sg-meter-config">
{ "storageKey": "mysite.meter.v1", "start": 500,
  "prices": { "article_new": 10, "article": 5, "page": 1, "free": 0 },
  "topup": { "amount": 500, "link": "https://buy.stripe.com/your-link" },
  "picks": { "feed": "articles/feed.json", "base": "articles/" } }
</script>
<script type="module" src="/assets/components/sg-meter/v1/v1.0/v1.0.0/sg-meter.js"></script>
```

Every key has a default, so an empty config works. Put `data-root` on `<html>` (for example `data-root="../"`) if your pages are not all at the top level; links the component writes are prefixed with it. This site loads the module with a dynamic `import()` from an inline script instead of a `src`, because its own build forbids script tags that point at files; either works.

## The six views

One element, one shared meter: an ES module is evaluated once per page, so however many `<sg-meter>` elements a page has, it is charged once.

| view | What it shows | Attributes |
|---|---|---|
| `balance` | The balance as a small link to the account. Shown in a warmer colour below zero, with a tooltip that says nothing is blocked. Nothing else: no banner, no count of articles read. |  |
| `page` | Opens this page on the meter and charges it by scroll depth. Shows what it has cost so far, the share read, the price to the end, and "Not worth it? Don't charge me" with four reasons. | `kind`, `date` (YYYY-MM-DD), `topics` (space separated), `title`, `quiet` (charge, show nothing) |
| `account` | Balance, pages opened, spend, what was declined, picks, spend by topic, the history with the depth read, top-ups; pause, export as JSON, start again. |  |
| `topup` | With `topup.link` set, one button to the payment page. Without, a simulated cart (packs, cart, review, receipt) that says it is simulated. |  |
| `topped-up` | The page a payment link returns to. Adds `topup.amount` once per `session_id` in the URL. It does not verify the payment; see [the security model](security.md#return). |  |
| `picks` | Unread pages from the reader's most-read topics. Hidden until there is a history to pick from. | `count` (default 4) |

This site's own: [account](../account/index.md), [top-up](../account/top-up.md), [topped-up](../account/topped-up.md) (opened without a payment reference, it adds nothing and says so), and the picks band on [the front page](../articles/index.md).

## The rules it charges by

- **By depth.** A page costs its price times the deepest point the reader has scrolled to, measured on the page's `main` element and rounded to 5%, never less than `minDepth` (default a tenth), so opening a page is not free. Read half, pay half.
- **Once per page per session.** Scrolling further later in the same browser session tops the same charge up; coming back does not start a second one.
- **Below zero is allowed.** Nothing is blocked and nothing nags. The balance is shown, that is all.
- **Declining is allowed.** A reader can refuse to pay for a page, with a reason: the headline promised more than the page gave, not relevant to me, I did not really read it, another reason. The charge is refunded and the reason kept in their history; "not relevant" counts against that page's topics in the picks.
- **New costs more.** An `article` whose `date` is within `newDays` is priced at `article_new`, judged in the reader's browser, so prices age without a rebuild. Any other `kind` is looked up in `prices`, falling back to `page`.
- **Storage may fail.** In a browser that blocks storage the page still works, and the account says it cannot keep a balance.

## Config reference

| Key | Default | Meaning |
|---|---|---|
| `storageKey` | `"sg.meter.v1"` | The localStorage key. Use your own per site. (This site keeps `sgit.meter.v1`, the key its first meter used, so balances carried over.) |
| `start` | `500` | Starting credit, in pence or cents. |
| `symbol` | `"£"` | Shown before amounts. |
| `prices` | 10 / 5 / 3 / 2 / 2 / 1 / 0 | Price of a page read to the end, by kind: `article_new`, `article`, `issue`, `note`, `collection`, `page`, `free`. Add your own kinds. |
| `newDays` | `7` | How long an article is new. |
| `depth` | `true` | Charge by scroll depth. `false` charges the whole price on opening. |
| `minDepth` | `0.1` | The least share of a page that is charged. |
| `topup` | `{"amount": 500, "link": ""}` | The payment link and what it adds. Empty link: the simulated cart. |
| `packs` | `[{"id":"p5","price":500,"bonus":0}]` | The simulated cart's packs. |
| `links` | `{"account": "account/index.html", "topup": "account/top-up.html"}` | Where your account and top-up pages are, relative to `data-root`. |
| `picks` | `{"feed": "", "base": ""}` | A JSON feed of `{"articles": [{slug, title, date, teaser, topics}], "topics": [{id, label}]}`, and the folder an article's `slug + ".html"` is in. Empty feed: no picks. This site uses [articles/graphs.json](../articles/graphs.json). |

Config can also be given as `window.SG_METER_CONFIG` before the module loads.

## Events

Dispatched on `document`, bubbling and composed, named `<namespace>:<noun>.<verb>`. Event names are API: renaming one is a major version.

| Event | detail |
|---|---|
| `sg:meter.charged` | `{path, depth, cost, balance}`, each time a charge grows |
| `sg:meter.declined` | `{path, reason, balance}` |
| `sg:meter.toppedup` | `{credit, source, balance}`; source is `simulated` or `link` |
| `sg:meter.reset` | `{}` |
| `sg:meter.changed` | `{balance}`, on any saved change; the elements repaint on it |
| `sg-meter:error` | `{why}`, if the component's markup or styles failed to load; the element also gets `data-state="error"` |

Nothing listens to these on this site: there is no analytics. They are there so a site that wants to count, for example, how many readers decline and why, can do it in its own code and say so.

## What is stored

One JSON value under `storageKey` in localStorage, and a map of this session's pages under `storageKey + ".seen"` in sessionStorage. The reader can export it from the account page.

```
{ "v": 2, "created": "2026-10-10T09:00:00.000Z",
  "balance": -12.5, "spent": 512.5, "reads": 91, "declined": 14, "paused": false,
  "log": [ { "id": "…", "at": "…", "path": "/articles/x.html", "title": "…", "kind": "article",
             "topics": ["news"], "price": 10, "depth": 0.55, "cost": 5.5,
             "declined": { "reason": "clickbait", "at": "…", "refunded": 4 } } ],
  "topups":   [ { "ref": "cs_…", "at": "…", "credit": 500, "source": "link" } ],
  "sessions": [ "cs_…" ], "cart": [] }
```

The log keeps the last 500 pages. A version 1 state (this site before v0.7.26) is read and upgraded in place.

## Theming

The component draws in a shadow root, so your stylesheet cannot reach in, but CSS custom properties cross the boundary and every colour reads one first: `--fg`, `--dim`, `--line`, `--line2`, `--panel`, `--accent`, `--accent-dk`, `--warm` (the colour of a negative balance), `--mono`, `--serif`, `--sans`. Each has a neutral fallback, so a site with none of them still gets a readable meter. The host element is yours to place and size: `sg-meter { display: block }`, and the root is exposed as `::part(root)`.

## Taking real payments with a Stripe Payment Link

1. In Stripe, create a product (for example "£5 of reading") and a **Payment Link** for it.
2. In the link's **After payment** settings, choose not to show Stripe's confirmation page and to redirect to your site, with this URL (Stripe fills in the placeholder):
`https://your.site/account/topped-up.html?session_id={CHECKOUT_SESSION_ID}`
3. Put the link in the config as `topup.link`, and the credit it buys as `topup.amount`.
4. Make a page at that path with `<sg-meter view="topped-up"></sg-meter>` on it.

Stripe's own guidance is that fulfilment should come from the `checkout.session.completed` webhook, not from the redirect, because a redirect can be skipped or faked. A static site has nowhere to receive a webhook, so this library credits on the redirect and says so. On a £5 payment with a standard UK card Stripe's listed fee is 1.5% + 20p, about 27.5p, or 5.5%; premium and international cards cost more. The arithmetic for this site is in [going live with the reading meter](../articles/going-live-with-the-reading-meter.md).

## Where its rules come from

The first version ran on [pt.newsroom.sgit.ai](https://pt.newsroom.sgit.ai/carteira/) as its wallet: says up front what it is, never blocks, one charge per page per session, storage allowed to fail. Its code follows [coding.sgit.ai's JavaScript guidance](https://coding.sgit.ai/javascript/index.html): ES modules, native web components on a shared base class, markup and styles in sibling files, page data set only as text, events as API. And two carried over from [the NFRs](https://nfrs.sgit.ai/), whose rule is "generate or date every number": the balance and the spend are running totals, but the log of every charge that made them sits beside them in the same export (the last 500), so a reader can check one against the other; and "a restore that has never been performed is not a backup", so the export is plain JSON a reader can open and read, the only copy of their history there is.

## Changelog

- **v1.0.0** (10 October 2026, site v0.7.26). First packaged release: scroll-depth charging, negative balances, decline with a reason, the balance view, the Stripe return page, picks that count "not relevant" against a topic. Replaces this site's `assets/meter.js` (v0.7.24), which charged on opening and showed a bar when credit ran out.

Next, not yet: rating a page, classifying it and keeping a note on it, all in the same local history; a balance that follows a reader between devices through an encrypted vault only they hold the key to. [Security model](security.md) · [this site's account page](../account/index.md).


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/meter/index.html)*
