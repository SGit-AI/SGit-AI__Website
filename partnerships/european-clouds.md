# A proposed partnership between sgit.ai and the European clouds

> For European clouds, vaults are the sovereignty argument made concrete. OVHcloud, Scaleway, Hetzner, IONOS and STACKIT are chosen by customers who want their data in Europe, under European law, with a European provider. sgit adds the guarantee that even the provider cannot read it: the host holds ciphertext, the keys stay with the customer, and the code is open, so nobody can be bought out from under them. Every one of these clouds offers S3-compatible object storage, which is most of what sgit needs.

*Source: <https://sgit.ai/partnerships/european-clouds.html> · site v0.6.7 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Partnerships](index.md) / [Cloud platforms](cloud-platforms.md) / the European clouds

A proposed partnership · sgit.ai with the European clouds · public material only · 24 September 2026

# A proposed partnership between sgit.ai and the European clouds

**For European clouds, vaults are the sovereignty argument made concrete.** OVHcloud, Scaleway, Hetzner, IONOS and STACKIT are chosen by customers who want their data in Europe, under European law, with a European provider. sgit adds the guarantee that even the provider cannot read it: the host holds ciphertext, the keys stay with the customer, and the code is open, so nobody can be bought out from under them. Every one of these clouds offers S3-compatible object storage, which is most of what sgit needs.

**Nothing on this page is confidential, and there has been no conversation yet.** Every statement about the European clouds comes from its own public pages, linked. Every statement about sgit points at the [deployment documentation](../deploy/index.md), a published vault or a page on this site. sgit is Apache-2.0, so the European clouds does not need our permission to run it or to build on it. A partnership is about doing that well and together. The general argument is on [the cloud platforms page](cloud-platforms.md).

## In short

- **Storage is ready everywhere.** Each of the five offers S3-compatible object storage, which is the one thing a vault server really needs.
- **Compute varies.** Scaleway has Serverless Containers. The others run the container on managed Kubernetes, Cloud Foundry or a plain server, which the image supports.
- **Sovereignty is the sale.** [OVHcloud's public cloud qualified for SecNumCloud on 1 September 2026](https://corporate.ovhcloud.com/en/newsroom/news/ovhcloud-obtains-secnumcloud-qualification-snc-cloud-platform/); STACKIT and IONOS hold BSI C5; Hetzner has been independent since 1997; Scaleway is European-owned.
- **What we would like:** one tested deployment on each, and a listing in the marketplaces that exist.

## How vaults map onto the European clouds

| sgit needs | On the European clouds | Status |
|---|---|---|
| **OVHcloud** | Object Storage ("largely compatible with the S3 protocol"); Managed Kubernetes; [Open Trusted Cloud](https://opentrustedcloud.ovhcloud.com/en/program-description/) for the marketplace | Not tested by us. |
| **Scaleway** | S3-compatible Object Storage; [Serverless Containers](https://www.scaleway.com/en/serverless-containers/); Edge Services; Marketplace and Partner Program | Not tested. The closest match to the AWS Lambda shape. |
| **Hetzner** | [S3-compatible Object Storage](https://www.hetzner.com/storage/object-storage/); Cloud servers with Docker | Not tested. The simplest and cheapest path: one server, one bucket. |
| **IONOS Cloud** | S3-compatible Object Storage; Managed Kubernetes; CDN; [ISV Partner Program](https://cloud.ionos.com/partner/isv) and Marketplace | Not tested. |
| **STACKIT** | S3-compatible Object Storage; Kubernetes Engine or Cloud Foundry; CDN; [STACKIT Marketplace](https://stackit.com/en/partner/stackit-marketplace-partner) | Not tested. |

## Where we are with the European clouds today

We have not deployed on any of these yet, and we should have. The founder's view, stated on [the UK Sovereign AI page](sovereign-ai.md), is that sovereignty without open source is one acquisition deep. The same argument applies to European clouds: a sovereign host is necessary, and an open, client-side-encrypted data layer on top of it is what makes the sovereignty survive a change of owner, a court order or a breach.

## What a partnership could be

| Shape | What it would be | On their side |
|---|---|---|
| **1 · One tested deployment each** | The server with each provider's S3-compatible storage, documented in the deployment docs. This is also how the S3-endpoint support gets tested properly. | A test account and a technical contact. |
| **2 · A European reference** | A published reference for a fully European stack: a European cloud, a European model provider such as [Mistral](mistral.md), and vaults, with no key ever leaving the customer. | Joint publication. |
| **3 · Marketplace listings** | The server in OVHcloud's, Scaleway's, IONOS's and STACKIT's marketplaces, where their programmes allow it. | Each provider's ISV or partner programme. |

## What we are asking the European clouds for

1. A test account on each, to write and verify the deployment guide.
2. An introduction to each provider's ISV or partner programme, and to their marketplaces.
3. Startup programme support where it exists: [OVHcloud](https://startup.ovhcloud.com/en/), [Scaleway](https://www.scaleway.com/en/startup-program/), [IONOS](https://cloud.ionos.com/startup-program) and [STACKIT](https://stackit.com/en/why-stackit/benefits/startup-program) each run one.
4. A first European customer for whom "the host cannot read it" is the requirement.

## What this page does not claim

- **No endorsement.** None of these providers has endorsed sgit, and we have not spoken to anyone at them about this. Programme and product descriptions quote each provider's own pages as of 24 September 2026.
- **None of this is tested.** Every row above is what the providers document, not what we have run.

## If you work at the European clouds

This page is written to be forwarded as it is, and everything on it can be checked by the person who receives it. [Who is asking, and how to reach them →](../about/index.md)

[← IBM Cloud](ibm-cloud.md)[DigitalOcean →](digitalocean.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/partnerships/european-clouds.html)*
