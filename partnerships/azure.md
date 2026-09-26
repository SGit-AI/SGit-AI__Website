# A proposed partnership between sgit.ai and Microsoft Azure

> sgit runs on Azure. We just have not written it down yet. The founder has deployed the vault server on Azure and it works, but the published documentation covers Docker, AWS, Google Cloud and static hosts, not Azure. We would like to close that gap with Microsoft: a documented, reviewed deployment on Azure services, a listing in Microsoft Marketplace, and a route to the many organisations whose data already lives in Azure and Microsoft 365.

*Source: <https://sgit.ai/partnerships/azure.html> · site v0.6.10 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Partnerships](index.md) / [Cloud platforms](cloud-platforms.md) / Microsoft Azure

A proposed partnership · sgit.ai with Microsoft Azure · public material only · 24 September 2026

# A proposed partnership between sgit.ai and Microsoft Azure

**sgit runs on Azure. We just have not written it down yet.** The founder has deployed the vault server on Azure and it works, but the published documentation covers Docker, AWS, Google Cloud and static hosts, not Azure. We would like to close that gap with Microsoft: a documented, reviewed deployment on Azure services, a listing in Microsoft Marketplace, and a route to the many organisations whose data already lives in Azure and Microsoft 365.

**Nothing on this page is confidential, and there has been no conversation yet.** Every statement about Microsoft Azure comes from its own public pages, linked. Every statement about sgit points at the [deployment documentation](../deploy/index.md), a published vault or a page on this site. sgit is Apache-2.0, so Microsoft Azure does not need our permission to run it or to build on it. A partnership is about doing that well and together. The general argument is on [the cloud platforms page](cloud-platforms.md).

## In short

- **The vault server is one container.** On Azure that is Azure Container Apps or Azure Functions, configured only by environment variables.
- **Storage is the work.** Azure Blob Storage is not natively S3-compatible, and the server's durable storage mode targets Amazon S3. On Azure today that means a disk volume, S3 with cross-cloud credentials, or a native Blob Storage backend, which would be the right answer and is the main engineering in this partnership.
- **Sovereignty fits.** Microsoft completed the [EU Data Boundary](https://blogs.microsoft.com/on-the-issues/2025/02/26/microsoft-completes-landmark-eu-data-boundary-offering-enhanced-data-residency-and-transparency/) in February 2025 and offers [Microsoft Sovereign Cloud](https://learn.microsoft.com/en-us/azure/azure-sovereign-clouds/microsoft-sovereign-cloud). A vault adds the layer that makes it hold for the data itself: the host only ever sees ciphertext.
- **What we would like:** engineering help on the Blob Storage backend, a documented deployment, a place in [ISV Success](https://learn.microsoft.com/en-us/partner-center/membership/isv-success), and a listing in [Microsoft Marketplace](https://learn.microsoft.com/en-us/partner-center/marketplace-offers/marketplace-containers).

## How vaults map onto Azure

| sgit needs | On Microsoft Azure | Status |
|---|---|---|
| **A small stateless API** | Azure Container Apps, or Azure Functions | Working in the founder's own deployment; not yet documented. |
| **Object storage** | Azure Blob Storage | Not S3-compatible. Needs a native backend, or a disk volume or cross-cloud S3 in the meantime. |
| **Static readers** | Azure Static Web Apps, Azure Front Door | Should work, as for any static host. Not tested by us. |
| **Sovereign data** | EU Data Boundary, Microsoft Sovereign Cloud | Complementary: the host holds ciphertext only, in the region chosen. |
| **Data that already lives in Microsoft 365** | Agents with Microsoft 365 connectors | RiskMandate.ai has published a behaviour policy for Claude with Microsoft 365, and the risk side is being written there. |

## Where we are with Microsoft Azure today

Azure is the clearest case of something that works and is not yet written down. The deployment was done and it ran; what it lacks is a guide, a storage backend that uses Blob Storage natively, and a review by someone who knows Azure. The reason it has not been done is simply that our credits and our history are on AWS. That is a gap we would rather close with Microsoft than around it.

## What a partnership could be

| Shape | What it would be | On their side |
|---|---|---|
| **1 · A native Blob Storage backend** | A storage mode for Azure Blob Storage in the open-source server, so a vault on Azure keeps its ciphertext in Azure with no cross-cloud credentials. | An engineer who knows the Blob Storage APIs, and credits to test on. |
| **2 · A documented Azure deployment** | A guide and a template for Container Apps with Blob Storage, reviewed and published in the deployment docs next to AWS and Google Cloud. | A technical reviewer. |
| **3 · A Marketplace offer** | The open-source server as a free container offer in Microsoft Marketplace, which supports Free and BYOL container billing. | ISV Success, part of the Microsoft AI Cloud Partner Program. |

## What we are asking Microsoft Azure for

1. Engineering help, or a reviewer, for a native Azure Blob Storage backend.
2. A technical review of the Azure deployment guide before we publish it.
3. A place in [ISV Success](https://learn.microsoft.com/en-us/partner-center/membership/isv-success) and a route into Microsoft Marketplace.
4. Credits through [Microsoft for Startups](https://www.microsoft.com/en/startups), so the Azure path gets the same testing the AWS path had.
5. An introduction to a customer who needs encrypted handover inside an Azure estate.

## What this page does not claim

- **No endorsement.** Microsoft Azure has not endorsed sgit, and we have not spoken to anyone there about this. Programme and product descriptions quote Microsoft Azure's own pages as of 24 September 2026.
- **"Working" means the founder's own deployment.** It is not documented, not reviewed, and does not yet use Blob Storage natively.

## If you work at Microsoft Azure

This page is written to be forwarded as it is, and everything on it can be checked by the person who receives it. [Who is asking, and how to reach them →](../about/index.md)

[← AWS](aws.md)[Google Cloud →](google-cloud.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/partnerships/azure.html)*
