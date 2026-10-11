---
title: Go slow to go fast: moving the newsroom from an explorer project to a villager one, with the brief to do it
date: 2026-10-11
author: Dinis Cruz
author_url: about/index.html
summary: The newsroom's first MVP already has a crazy amount of powerful features, and it is live, and it is taking money. Like most explorer projects, it is also bundled in the middle of something much bigger: the application that bills, remembers and personalises sits in the same repository as 74 articles and their images. Measured on newsroom v0.8.0, the live reader code is about 2,700 lines, and the tests that cover it are 433. I want to keep shipping a massive number of features without breaking anything, so this is the moment to take a step back and go slow to go fast. This article is the case for it and the brief: move every feature that is not content into its own repository, as a pure refactoring, with the same behaviour and the same bugs, checked by hashing the files the live site serves; map every file, capability and web control; build the safety net, with bugs and vulnerabilities written down as tests that pass; review it for security and quality, with every finding a GitHub issue; refactor until no change that alters what a reader sees or pays can slip through; and build a pipeline fast enough to run on every commit, in Node, in three browser engines, against a pre-production copy and with synthetic readers. Then the explorer returns, with the vault and the passkey.
version: v0.7.56
license: https://creativecommons.org/licenses/by/4.0/
tags: engineering, explorer, villager, refactoring, testing, ci, security-review, code-review, newsroom, sg-meter, github-issues, brief, article
status: published
---

!shot ev-split.webp | images/ | What stays and what moves, measured on newsroom v0.8.0. The publication stays where it is; everything the reader does, the meter, the payments, the personas, the lists, the sharing, moves to a repository of its own, with its own engineering.

The newsroom's first MVP has a crazy amount of powerful features. A meter that charges by how far you read. Paying after you read, with a rating that sets the price. Real payments. Personas, a newsroom of your own, reading lists in a link, encrypted sharing. And it is live, and it is being charged for.

It is also, like most explorer projects, bundled in the middle of something much bigger. The application that bills, remembers and personalises lives in the same repository as 74 articles, their graphs, their images and the archive of everything the site has done. It grew there because that is where it was fastest to build. That was right for exploring. It is not right for what comes next.

I want to keep pushing a massive amount of features. The reader's own vault, sign-in with a passkey, packs for the reader's agent: all of it is designed and most of it is waiting. And I want to do it without breaking anything that people are paying for. So this is a perfect example of the moment when you take a step back and go slow, to go fast.

## In short {#short}

- **The newsroom is now a villager project.** It is live, it charges, and changes land on real readers. Explorer code is read for intent; villager code is read line by line, because that is where the blast radius lives.
- **Content and application get separate repositories.** Everything the reader does moves to its own repository, released as versioned files that the newsroom pins. The content stays.
- **The numbers are the reason.** About 2,700 lines of live reader code, 433 lines of tests, one workflow that deploys and none that tests, and no Content-Security-Policy on any page.
- **First, a pure refactoring.** Same behaviour, same bugs. The proof is not a reviewed diff; it is the live site serving the same bytes before and after, by hash.
- **Six phases, and features wait until the fifth.** Map, move, test, review, refactor; then the explorer returns. Bugs and vulnerabilities found on the way become tests that pass, so fixing them later is a deliberate, visible change.
- **A pipeline fast enough to run on every commit.** Plain JavaScript and static files mean Node tests in seconds and three browser engines in about a minute; pre-production with a Stripe test link; synthetic readers; and a release that ends by checking the live site.
- **Reviews, by people and agents, and GitHub issues** for every finding, so the work is visible and nothing found is lost.

## Why now {#why}

In [If somebody built a company on code review](/articles/if-somebody-built-a-company-on-code-review.html) I put it this way: how carefully code is read depends on where it sits on the map. Explorer code is read for intent, mostly by agents. Villager code is read line by line, because that is where changes land and where the blast radius lives. Town planner code is read by deterministic checks.

The newsroom's reader features just crossed that line. A few days ago they were an experiment. Today a reader can pay £5 by card, and the meter decides what they spend. A mistake in the meter is a mistake with someone's money, and a mistake in the reading list parser is a mistake on a page that opens from an email in my name.

We have done this before. In March, the sgit command line went through the same transition, with [a brief that set out the phases](https://github.com/SGit-AI/SGit-AI__CLI/blob/main/team/humans/dinis_cruz/briefs/03/12/v0.13.30__brief__code-quality-explorer-villager.md): review without changing anything, build the test net, refactor with every test passing, and only then let the explorer build again. The command line has shipped release after release since then, with the safety net under it. The newsroom gets the same treatment, with one phase added at the start: the move.

The point is speed. Going slow now is what lets me keep going fast without the fear that each new feature breaks something a reader has paid for.

## What I measured {#measured}

Counted in the newsroom repository at v0.8.0, on 11 October 2026:

| What | Size |
|---|---|
| SG Meter, the live version (v1.4.0): balance, pay by depth, rating, personas, your newsroom, top-up, share | 1,326 lines |
| Reading lists in a link, and the page that makes them | 706 lines |
| The component base, subscribe and the encrypted share | 235 lines |
| Build code for article numbers, lists and personas | 419 lines |
| Account and persona pages | 12 pages |
| Tests for the meter and the lists | 433 lines |
| Earlier meter versions, kept on their versioned paths | 5,016 lines in 10 files |
| GitHub workflows | 1, and it deploys |
| Pages with a Content-Security-Policy | 0 |

On this site's side, where the meter was first built and the newsroom's content still comes from, the page builder is a single file of 7,844 lines, about 240 of which touch the meter, personas or the account. That is the "bundled in the middle of a massive thing" in numbers.

None of this is a criticism of the explorer work. It is what explorer code looks like, and it is why it was fast. It is also exactly what has to change before the next wave.

## The six phases {#phases}

!shot ev-phases.webp | images/ | Six phases, from mapping to the explorer's return. Until phase five, no behaviour changes, not a feature and not a fix.

**0. Map.** Before anything moves, map all of it: every file, every capability, every web control (anything a reader can click, type or pay), every input, every place data leaves the browser, every external call and every secret or configuration value. As a table and as a graph, the way [code review as a fractal semantic graph](/articles/code-review-as-a-fractal-semantic-graph.html) does it, and the way secrets.sgit.ai's review pages map that project's claims to their evidence. No code changes. The map lives in the new repository and is regenerated every night.

**1. Move.** The reader code goes to its own repository, unchanged, and is released from there as versioned files on versioned paths, which is already how SG Meter is published. The newsroom pins a version. The rule is strict: **the same behaviour and the same bugs**. The check is strict too: hash every file the live site serves for the reader features before the move and after it. If one hash differs, the move is not finished.

**2. Test.** Only test code is written. Unit tests in Node for the money, the parsing and the state; browser tests in Chromium, WebKit and Firefox, on phone and desktop sizes; tests against a pre-production copy; and a synthetic reader run. No mocks: a test that needs a browser uses a browser, and a test that needs a vault uses a vault. **Bugs and vulnerabilities are written as tests that pass**, recording the current behaviour, so the fix later is a visible change to a test, not a silent one.

**3. Review.** Security and quality, by people and by agent reviewers, against the map. Findings, not fixes: every finding is a GitHub issue, labelled, with the test that shows it.

**4. Refactor.** Structure, names, duplication, boundaries, all with every test passing after every commit. And the adversarial exercise from the March brief: try to change what a reader sees or pays without a test failing. Every change that slips through is a missing test. Phase four is finished when none slips through.

**5. The explorer returns.** The fixes land, each as a deliberate change to the test that recorded the bug. Then the features that are waiting: [the reader's vault](/articles/i-miss-it.html), [the passkey that opens it](/articles/the-passkey-opens-the-vault.html), and [the pack for the reader's agent](/articles/brief-the-agent-too.html).

## The pipeline {#pipeline}

!shot ev-pipeline.webp | images/ | Every commit, merge, release and night, with what runs at each and the time it should take. Slow checks run at night, not on the commit.

I want to see how fast and effective we can make this. The reader application is pure JavaScript and static files: no server to start, no database to seed, no container to build. That means most of it can be tested in Node in seconds and in real browsers in about a minute, and that is the target for every commit: **under two minutes**, lint, unit tests, three browser engines, and a build that produces the same bytes twice.

On every merge, pre-production: a copy of the newsroom with the new version, a Stripe link in test mode that can never charge anyone, smoke tests of every reader page and every control, and a short synthetic reader run on a phone and a laptop. On every release: publish the versioned files, pin them in one commit, and ask the live site for its version and the hash of every reader file, because [green does not mean live](/articles/green-does-not-mean-live.html). Rolling back is pinning the previous version. And every night: the full synthetic reader study, the adversarial changes, dependency and header checks, and the map regenerated and compared with yesterday's.

Code review becomes part of the pipeline: a pull request needs one person and one agent reviewer before it merges. I want to be reviewing these changes myself, and I want a set of agent reviewers alongside me, each with a written role, the way the newsroom's desk already works.

## The brief {#brief}

*For the newsroom's sessions, and for whoever reviews their work. Written by the sgit.ai site session for Dinis Cruz, 11 October 2026. Dinis decides what ships.*

### What moves, and what stays {#scope}

- **Moves:** SG Meter, every version; the account pages; reading lists and the make page; persona links and their configuration; subscribe and the encrypted share; the build code for article numbers, lists and personas; and their tests. Next to arrive there: the reader's vault, passkey sign-in and the agent pack.
- **Stays:** the articles and everything generated from them, the front page, the desk, collections, the newsletter, World News Day, the archive and the content build.
- **The name:** for now, a newsroom-specific name, such as `SGit-AI__Newsroom__Reader`, because what moves is everything the reader does. It may become more generic later, a reader platform any publication can use; the name can follow when it does.

### Rules {#rules}

1. **No behaviour changes until phase five.** Not a feature, not a fix, not a copy edit on a reader page.
2. **Same bytes served.** The move is proved by hashing every reader file on the live site before and after, not by reading the diff.
3. **Bugs and vulnerabilities as passing tests.** Each one gets a test that records the current behaviour, and an issue that links to it.
4. **No mocks.** Real browsers, real vaults, a real pre-production copy, a Stripe link in test mode.
5. **Every finding is an issue.** In the new repository's GitHub issues, labelled by phase, area and severity, with its evidence.
6. **Every change is reviewed** by one person and one agent reviewer before it merges.
7. **Releases are versioned and pinned.** The newsroom never loads an unversioned reader file; a rollback is one commit.

### Where the security review starts {#security}

From the measurement above and the newsroom's own [security model](https://newsroom.sgit.ai/meter/security.html), the review should at least cover:

- **No Content-Security-Policy.** No page sets one. A policy in a `meta` tag can limit scripts and connections, but it cannot set `frame-ancestors`, so protection against framing would need headers that GitHub Pages does not let us set. Decide whether the reader pages need a commodity layer in front that can.
- **Untrusted input in the URL.** The reading list fragment, persona links and the topped-up page's payment reference all come from a link. Each needs its parser tested against malformed and hostile input.
- **Money in the browser.** The balance, the receipts and the credit after a payment are in the reader's own storage by design, and the gaps that follow are accepted in the security model. The tests should prove the accepted gaps are the only ones: for example, that a payment reference is credited once.
- **What leaves the browser.** The share and the subscription encrypt to a published key and write to a lane. Test that nothing else leaves, on any page, with the browser's own record of requests, as the synthetic reader helper already does.
- **Third-party code.** Today the reader pages load none. Keep it that way, and make the build fail if one appears.

### Acceptance {#acceptance}

| # | Done when |
|---|---|
| 1 | The map exists in the new repository: files, capabilities, web controls, inputs, outputs, external calls |
| 2 | The reader code is released from the new repository and pinned by the newsroom, and every reader file on the live site hashes the same as before the move |
| 3 | The commit pipeline runs in under two minutes: lint, Node tests, Chromium, WebKit and Firefox, and a reproducible build |
| 4 | Pre-production runs on every merge, with a Stripe test link, smoke tests and a short synthetic reader run |
| 5 | Every known bug and vulnerability is a passing test and an open issue |
| 6 | Every pull request has one person and one agent reviewer |
| 7 | No adversarial change to what a reader sees or pays slips through the tests |
| 8 | Only then: the fixes, and the vault, the passkey and the agent pack |

## What this does not claim {#limits}

- **It is not a verdict on the code.** The explorer work is why the newsroom exists at all. This is the next phase of the same work, not a correction of it.
- **The numbers are lines, not quality.** 433 lines of tests could cover a lot or a little; phase two is where we find out which.
- **The timings are targets.** Under two minutes per commit is what the shape of the code allows; the pipeline has to prove it.

If you have taken a live product from explorer code to a villager codebase, and you have lessons to share, or you want to review this one with us, write to [agent@riskmandate.ai](mailto:agent@riskmandate.ai).

## Where this comes from {#sources}

A voice memo of mine, recorded on 11 October 2026, asking for an article, a brief and then the execution of the move; written by this site's agent in the voice of this site. The argument and the editorial responsibility are mine. The measurements are from the newsroom's repository at v0.8.0 and this site's source on the same day. The phases adapt [the explorer-to-villager brief of 12 March 2026](https://github.com/SGit-AI/SGit-AI__CLI/blob/main/team/humans/dinis_cruz/briefs/03/12/v0.13.30__brief__code-quality-explorer-villager.md) from the sgit command line. Related: [If somebody built a company on code review](/articles/if-somebody-built-a-company-on-code-review.html), [Code review as a fractal semantic graph](/articles/code-review-as-a-fractal-semantic-graph.html), [Green does not mean live](/articles/green-does-not-mean-live.html), [How to run synthetic users](/articles/how-to-run-synthetic-users.html), [I miss it, so it is working](/articles/i-miss-it.html), [The passkey opens the vault](/articles/the-passkey-opens-the-vault.html) and [Brief the agent too](/articles/brief-the-agent-too.html).
