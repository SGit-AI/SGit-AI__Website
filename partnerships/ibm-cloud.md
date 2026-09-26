# A proposed partnership between sgit.ai and IBM Cloud

> We would like to work with IBM on sovereign, regulated data. IBM made digital sovereignty a product with IBM Sovereign Core, generally available since May 2026. sgit adds the piece that makes sovereignty hold at the data layer: encrypted vaults whose host, whoever runs it, only ever sees ciphertext. IBM Cloud has the storage and the serverless compute sgit needs, and IBM's customers have the regulated data that needs it.

*Source: <https://sgit.ai/partnerships/ibm-cloud.html> · site v0.6.9 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Partnerships](index.md) / [Cloud platforms](cloud-platforms.md) / IBM Cloud

A proposed partnership · sgit.ai with IBM Cloud · public material only · 24 September 2026

# A proposed partnership between sgit.ai and IBM Cloud

**We would like to work with IBM on sovereign, regulated data.** IBM made digital sovereignty a product with IBM Sovereign Core, generally available since May 2026. sgit adds the piece that makes sovereignty hold at the data layer: encrypted vaults whose host, whoever runs it, only ever sees ciphertext. IBM Cloud has the storage and the serverless compute sgit needs, and IBM's customers have the regulated data that needs it.

**Nothing on this page is confidential, and there has been no conversation yet.** Every statement about IBM Cloud comes from its own public pages, linked. Every statement about sgit points at the [deployment documentation](../deploy/index.md), a published vault or a page on this site. sgit is Apache-2.0, so IBM Cloud does not need our permission to run it or to build on it. A partnership is about doing that well and together. The general argument is on [the cloud platforms page](cloud-platforms.md).

## In short

- **The fit is regulated enterprise data.** Data rooms, evidence for auditors, and agent work handed over inside a regulated organisation.
- **The platform pieces exist.** [IBM Cloud Object Storage](https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-compatibility-api) supports a subset of the S3 API, and IBM Code Engine runs containers.
- **Sovereignty as software.** [IBM Sovereign Core](https://newsroom.ibm.com/2026-05-05-think-2026-ibm-makes-digital-sovereignty-operational-with-general-availability-of-ibm-sovereign-core) is deployed by customers or partners on OpenShift. The vault server is one container that could sit alongside it.
- **What we would like:** a place in [IBM Partner Plus](https://www.ibm.com/partnerplus/isv), a listing in the IBM Cloud Catalog, and a first regulated customer.

## How vaults map onto IBM Cloud

| sgit needs | On IBM Cloud | Status |
|---|---|---|
| **A small stateless API** | IBM Code Engine, or OpenShift | Should work: it is one container. Not tested by us. |
| **Object storage** | IBM Cloud Object Storage | Supports a subset of the S3 API. Whether it covers what the server uses is untested. |
| **Static readers** | Cloud Object Storage static website hosting | Should work, as for any static host. Not tested. |
| **Sovereign deployment** | IBM Sovereign Core | Complementary. Not tested. |

## Where we are with IBM Cloud today

We have not deployed sgit on IBM Cloud. The pieces it needs are there, and IBM's customers are the organisations for whom encrypted, versioned, auditable data is not a feature but a requirement. This page is an invitation to test that together.

## What a partnership could be

| Shape | What it would be | On their side |
|---|---|---|
| **1 · A tested deployment** | The server on Code Engine or OpenShift with Cloud Object Storage, documented and reviewed. | A technical contact and a test account. |
| **2 · Sovereign Core pairing** | A reference for running vaults inside a Sovereign Core deployment, so the data stays encrypted end to end. | The Sovereign Core team. |
| **3 · A Catalog listing** | The server in the IBM Cloud Catalog, through self-service Partner Center. | IBM Partner Plus, Build track. |

## What we are asking IBM Cloud for

1. A test account and a technical contact for Code Engine and Cloud Object Storage.
2. A conversation with the Sovereign Core team.
3. A place in [IBM Partner Plus](https://www.ibm.com/partnerplus/isv) and a route into the [IBM Cloud Catalog](https://www.ibm.com/cloud/partners/catalog-sell).

## What this page does not claim

- **No endorsement.** IBM Cloud has not endorsed sgit, and we have not spoken to anyone there about this. Programme and product descriptions quote IBM Cloud's own pages as of 24 September 2026.
- **Nothing here has run on IBM Cloud yet.** Every "should work" on this page is a reasoned expectation.

## If you work at IBM Cloud

This page is written to be forwarded as it is, and everything on it can be checked by the person who receives it. [Who is asking, and how to reach them →](../about/index.md)

[← Google Cloud](google-cloud.md)[The European clouds →](european-clouds.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/partnerships/ibm-cloud.html)*
