---
title: sg-sentinel.sgit.ai
domain: sg-sentinel.sgit.ai
tagline: An app-coupled edge guard — Layer 1 decides, Layer 2 acts
summary: A design for an edge security and logging layer you own rather than rent, built on the observation that your own app already knows what a valid request looks like — so the edge can allowlist rather than denylist. Published as a complete design that has deliberately not been built.
observed: 2026-08-20
seen_version: v0.1.1
repo: SGit-AI__Website__SG_Sentinel
hero: sentinel-home.webp
tags: edge, security, design
---

## It says, at the top of every page, that it does not exist

This is the most unusual thing on the network and the reason to read it. A banner sits above every page:

> **Not built.** SG/Sentinel is a published design from May 2026 — *"this is how I would build it"* — not a product. No plans to build it unless somebody funds it.

The status pill reads `NOT BUILT` where its siblings read `MVP DRAFT`. And the note goes further than a disclaimer usually does: the design exercise produced an agent-built prototype whose testing manual reports **149 passing tests**, and the site immediately bounds what that means — *"not deployed anywhere, not in production use, not maintained, and not packaged for you to install. Every 'built' or 'proven' on this site refers to that prototype exercise, nothing more."*

That paragraph is the whole house style in one place: publish the work, then say precisely what it is worth.

!shot sentinel-home.webp | images/ | The home page, with the not-built banner above the thesis and the full status note below it.

## The problem, and the inversion

Edge security and logging today means renting AWS WAF plus CloudWatch and Kinesis Firehose. The site names three costs — no real-time view of your own traffic, logging priced per gigabyte for a job that is *"write a clean record to S3"*, and a WAF you cannot reason about — and one origin story underneath them: *a single client-side bug once caused runaway redirect traffic, and nothing at the edge would catch the next one before the bill did.*

The inversion is the good idea. A generic WAF is blind to the application it protects, so it **denylists** known-bad and passes everything else. But if you control both client and server, the edge knows the valid request space — so it can **allowlist**, and no invalid request reaches the origin at all.

## One correction that reshaped the design

The architecture page opens with a governing constraint, and it is a genuinely instructive piece of engineering writing:

> **Layer 1 never acts and never writes — it only decides and signals. Layer 2 is the sole actor and the sole I/O owner.**

The reason is physical, not stylistic: a CloudFront Function has no network and no filesystem, so it *cannot* write to S3 and must not enforce. L1's whole job is to assign a request ID, evaluate deterministic rules, and emit a structured signal. Blocking, deflecting and logging are **actions**, and actions belong to the layer that can perform I/O. L1 can only *recommend* a block.

The site is explicit that this corrected an earlier version of its own design in which L1 blocked inline — a category error, named as such.

!shot sentinel-arch.webp | images/ | The layer model: one actor, one I/O owner, and both use cases flowing through a single path.

## Rules are the engine, not configuration on it

The second inversion: *"rules are not configuration on top of a fixed engine — rules are the engine."* The core is a small stable machine for executing them, and every block, allow and log action is a rule. Each is a pure function `(captured) → {verdict, reason, rule_id, action} | null`, run in order, first block wins.

The MVP core is deliberately tiny — six deterministic rules, each mapped to an ATT&CK technique:

| Rule | Catches | Action |
|---|---|---|
| `capture-all` | every request; pure observation and the allow fallthrough | pass |
| `banned-ip` | source IP in the embedded list | `drop_403` |
| `malformed-request` | no method, no path, path not starting `/` | `drop_403` |
| `path-never-valid` | `/etc/passwd`, path traversal | `drop_403` |
| `hidden-file-probe` | `/.env`, `/.git/…` | `deflect_404` |
| `wp-scan-on-static` | `/wp-login.php`, `/xmlrpc.php` on a static site | `deflect_404` |

Rules are data, versioned in git, carrying their own metadata. The prototype exercise ran the same engine across **three targets** with a parity matrix asserting identical decisions — which is what makes "rules are data" a testable claim rather than a slogan.

!shot sentinel-rules.webp | images/ | The six rules of the tiny core, each with what it catches, its ATT&CK mapping and its action.

## Why it is relevant here

Two connections, and the second is the sharper one.

**Rules as versioned data** is what sgit is for. A rule set that must be auditable, diffable and attributable — but whose contents may reveal exactly what you are watching for — is a natural fit for a vault: git semantics over content the host cannot read.

**And it is the third site here to publish a design before the thing exists.** [pki.sgit.ai](/network/pki.html) publishes four registry rules before the registry; this one publishes an entire architecture and then declines to build it. Both rest on the same wager: *publishing the design now is cheap, and claiming it afterwards is impossible.* If somebody does build this, the parity matrix and the six rules are already on the record.

## Sections

- **Architecture** — the layer model, the signal spine, the three targets
- **Rules** — rules as data, the six-rule core, and where the graph goes
- **Research** — 68 days of design, tabletop-tested
- **Try it · Code · Roadmap** — the prototype snapshot and what would come next
