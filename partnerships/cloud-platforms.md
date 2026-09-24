# sgit runs on every cloud: proposed partnerships with the cloud platforms, sgit.ai

> What sgit needs from a cloud (mostly storage, a little compute), where it stands today on each (AWS templates in beta, Google Cloud planned, Azure deployed but undocumented, Docker everywhere), the two partnerships in one (vaults in the cloud's environment, and services on top of vaults), why it is good for a cloud, and one page per cloud: AWS, Azure, Google Cloud, IBM Cloud, the European clouds, DigitalOcean, Rackspace and Netlify.

*Source: <https://sgit.ai/partnerships/cloud-platforms.html> · site v0.6.5 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Partnerships](index.md) / Cloud platforms

Proposed partnerships · sgit.ai with the clouds · public material only · 24 September 2026

# sgit runs on every cloud. We would like to work with them properly.

**An invitation from our side, published in the open.** [sgit.ai](../index.md) makes encrypted vaults: folders versioned like git, encrypted on the owner's device, stored as ciphertext, and opened in a browser with a key. What it needs from a cloud is mostly storage and a little compute, which means it runs on all of them. Today our story is mostly AWS, for historical reasons and because our startup credits are AWS credits. It should not stay that way. This page, and the page for each cloud linked from it, sets out what vaults bring to a cloud, how the partnership could work, and what we are asking for.

**Nothing on these pages is confidential, and there has been no conversation yet.** Every statement about a cloud comes from its own public pages, linked. Every statement about sgit points at a published vault, the [deployment documentation](../deploy/index.md) or a page on this site. And because sgit is Apache-2.0, **no cloud needs our permission to run it or to build a service on it.** A partnership is about doing that well and together, and it would be the best validation the technology could have.

## In short

- **sgit needs very little from a cloud.** The heavy work, encryption and decryption, happens on the user's device. The cloud holds ciphertext in object storage, and a small stateless API moves it. Readers can even be served from a plain static host behind a CDN, with no server at all.
- **So it can run anywhere.** The server ships as one Docker image, configured only by environment variables. Its durable storage mode targets Amazon S3 today, and most other clouds offer an S3-compatible store, so wiring those in is the obvious next step. It is not documented or tested yet.
- **Our history is AWS.** The AWS templates are written and in beta, and the vault service behind this site's published vaults answers from Amazon S3 behind CloudFront. Google Cloud is documented as planned. The founder has deployed it on Azure and on Google Cloud, but neither is documented yet. That gap is the first thing a partnership would close.
- **There are two partnerships in one.** First, deploying vaults in the cloud's environment, with documentation, reference architectures and a marketplace listing, for customers who already run there. Second, services the cloud or its partners can sell on top of vaults.
- **Vaults are sovereign by construction.** The host only ever holds ciphertext, in whichever region the customer picks, and moving a vault between clouds is a copy. For European clouds, that is the whole pitch.
- **We want to be where customers look.** That means the clouds' marketplaces, their partner programmes, and their startup programmes.

## What sgit needs from a cloud

Mostly storage, a little compute. Everything that needs a key happens on the user's device.

| Piece | What it does | What it needs from a cloud |
|---|---|---|
| **The client** | The `sgit` CLI or a browser. Encrypts every file, file name and commit message before upload, and decrypts on the way back. | Nothing. It runs on the user's machine. |
| **The vault API** | Batch reads and writes of ciphertext objects, plus the write-only [append lanes](../api/append-lanes.md). Stateless: no database, no sessions. | One container or one function. The same image runs on Docker, AWS Lambda, ECS Fargate, EC2, Cloud Run and Heroku, configured only by environment variables. |
| **Storage** | Ciphertext objects under opaque identifiers. Content-addressed objects never change, so they can be cached forever. | Object storage. The server's `s3` mode uses Amazon S3 today. Other clouds' S3-compatible stores are the next step, not yet tested. A `disk` mode runs on any mounted volume, and a `memory` mode serves ephemeral and air-gapped runs. |
| **Readers, optionally** | A published vault can be read from a static host with no API at all: the browser fetches ciphertext and decrypts locally. | A static host and a CDN. The deployment docs name GitHub Pages, S3 with CloudFront, Netlify, Cloudflare Pages, and Cloud Storage with Firebase. |

That is the whole footprint. [The measured cost page](../demos/fractal-graphs/performance.md) puts the estate behind this site at 2,662 files and 295 MB of object storage, measured on 21 September 2026. Storage and egress are the costs. There are no instance hours to speak of.

## Where we are today, honestly

| Target | Status |
|---|---|
| **Docker, anywhere** | Works today. Memory, disk and S3-backed modes, documented in the [deployment docs](../deploy/index.md). |
| **AWS** | The historical home. CloudFormation templates for Lambda (container image with a function URL) and ECS Fargate are written, lint-clean and in beta. There is also an EC2 appliance and runbooks for new accounts and regions. The vault service the published vaults use answers from Amazon S3 behind CloudFront, [sg-compute](https://sg-compute.sgit.ai/) builds agent environments on AWS, and our startup credits are AWS credits. This website itself is served from GitHub Pages. |
| **Google Cloud** | The image is Cloud Run-ready: it honours the injected port and is configured by environment variables. The Cloud Run guide is documented as planned. Durable storage there means either Amazon S3 with cross-cloud credentials, or native Cloud Storage, which is planned. |
| **Microsoft Azure** | Deployed and working in the founder's own tests. It is not documented yet. |
| **Static hosts** | Documented. A published vault reads from any static host behind a CDN. |
| **Everyone else** | Any cloud with a container runtime can run the image today with disk or memory storage. Durable object storage on a non-AWS cloud needs its S3-compatible endpoint wired in, which is not yet documented or tested. Each cloud's page says so. |

## Two partnerships in one

### 1 · Vaults in your environment

For customers who already run on a cloud and want vaults there, in their own account, region and budget. This needs:

- a documented deployment for the cloud's own services, reviewed by someone who knows them;
- a reference architecture a customer's architect can approve;
- a template the customer can launch in one step;
- a marketplace listing, so procurement can buy through the channel it already uses.

We will write the documentation either way. With a partner it gets reviewed, tested on credits, and published where the cloud's customers look.

### 2 · Services on top of vaults

The more interesting half. Because sgit is open source, a cloud or any of its consulting partners can build and sell services on it without asking. Some that follow directly from what is published here:

| Service | What the customer gets | Worked example on this site |
|---|---|---|
| **A managed vault service** | Vaults run for them, in their account, where the operator never holds a key. | [Deployment docs](../deploy/index.md) |
| **Encrypted data rooms** | A deal, a board or an audit shared as one vault with a read key per party, and full history. | [The board, as a vault](../demos/vaults/board/index.md) |
| **Agent handover** | The output of an AI agent delivered as a vault: the result, its history and its app, in one read key. | [A penetration test, delivered as a vault](../demos/vaults/pentest-report/index.md) |
| **Connector twins** | A journal and replay of everything an agent did through Gmail, Calendar or Slack, with a revert plan. | [Connector Twin](../demos/vaults/connector-twin/index.md) |
| **Evidence and compliance vaults** | Regulation, controls and evidence as a versioned, hash-verified record an auditor can open. | [AIUC-1 conformance](../demos/vaults/aiuc-1-conformance/index.md), [Regulation Graph](../demos/vaults/regulation-graph/index.md) |
| **Encrypted publishing** | Documentation and sites served from a static host, readable only with a key, and updated with a push. | [Deploy Docs](../demos/vaults/deploy-docs/index.md) |

## Why it is good for a cloud

- **It is storage-shaped.** Every vault is object storage and egress in the cloud's own billing, growing with use, with no competing database or runtime to displace.
- **It lives in the customer's account.** Nothing about sgit pulls data out of the cloud or into ours.
- **It answers the sovereignty question at the data layer.** The host holds ciphertext it cannot read, in the region the customer picks, so a cloud can say that and have it be true.
- **It gives agents somewhere to put their work.** Every cloud now sells agent platforms. Those agents need a handover format that a person can open, check and keep.
- **It carries no vendor risk for the cloud's customers.** Apache-2.0, with the code, the plans and the investor materials public.

## The pages, one per cloud

Each page stands on its own, so it can be sent to someone who works there. Each says where we are with that cloud, how vaults map onto its services, what a partnership could be, and what we are asking for.

| Cloud | Why them first | The page |
|---|---|---|
| **AWS** | Our historical home and the only cloud with templates written. The European Sovereign Cloud makes the sovereignty argument concrete. | [**The AWS page →**](aws.md) |
| **Microsoft Azure** | Deployed by the founder and working, but undocumented. The biggest gap between what runs and what is written down. | [**The Microsoft Azure page →**](azure.md) |
| **Google Cloud** | The image is already Cloud Run-ready and the guide is planned. Cloud Marketplace now lists AI agents as well as containers. | [**The Google Cloud page →**](google-cloud.md) |
| **IBM Cloud** | IBM Sovereign Core became generally available in May 2026. Enterprise customers with regulated data are exactly the vault use case. | [**The IBM Cloud page →**](ibm-cloud.md) |
| **The European clouds** | OVHcloud, Scaleway, Hetzner, IONOS and STACKIT. S3-compatible storage everywhere, and sovereignty as the reason customers choose them. | [**The European clouds page →**](european-clouds.md) |
| **DigitalOcean** | S3-compatible Spaces with a built-in CDN, simple App Platform, and a Marketplace that explicitly invites open-source projects. | [**The DigitalOcean page →**](digitalocean.md) |
| **Rackspace Technology** | A managed-services partner across the hyperscalers, with UK sovereign clouds for government, healthcare and police. | [**The Rackspace Technology page →**](rackspace.md) |
| **Netlify** | The static host a published vault needs, already named in our deployment docs. Encrypted sites on a CDN, updated with a push. | [**The Netlify page →**](netlify.md) |

## What we ask of every cloud

1. **A technical review** of the deployment guide for your platform, by someone who knows it, before we publish it.
2. **Credits to test on**, so the guides are run end to end rather than written from documentation.
3. **A route into your marketplace** for the open-source server, and later for vault products built on it.
4. **An introduction** to your startup and ISV partner teams.
5. **A first customer conversation**, where one of your customers needs encrypted handover or sovereign storage.

## What these pages do not claim

- **No cloud has endorsed sgit**, and we have not spoken to any of them about this. Where a page describes a programme or a product, it quotes the cloud's own page.
- **"Should work" is not "tested".** Each page says which it is. Docker works today, the AWS templates are in beta, and the founder's Azure and Google Cloud deployments are not yet written up.
- **sgit holds no certification.** It is open-source software with a stated [security model](../security/index.md) and stated [limits](../docs/limitations.md).

## If you work at one of these clouds

These pages are written to be forwarded as they are. Everything on them can be checked by the person who receives them. [Who is asking, and how to reach them →](../about/index.md) The same argument, from the model side, is on [the AI providers page](ai-providers.md).

[← Partnerships](index.md)[AI providers →](ai-providers.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/partnerships/cloud-platforms.html)*
