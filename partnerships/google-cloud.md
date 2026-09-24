# A proposed partnership between sgit.ai and Google Cloud

> We would like to finish the Google Cloud path with Google. The vault server image is already Cloud Run-ready, the Cloud Run guide is written down as planned, and the founder has deployed it on Google Cloud. What is missing is native Cloud Storage support, a reviewed guide, and a listing in Google Cloud Marketplace, which accepts open-source container images and, now, AI agents.

*Source: <https://sgit.ai/partnerships/google-cloud.html> · site v0.6.4 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Partnerships](index.md) / [Cloud platforms](cloud-platforms.md) / Google Cloud

A proposed partnership · sgit.ai with Google Cloud · public material only · 24 September 2026

# A proposed partnership between sgit.ai and Google Cloud

**We would like to finish the Google Cloud path with Google.** The vault server image is already Cloud Run-ready, the Cloud Run guide is written down as planned, and the founder has deployed it on Google Cloud. What is missing is native Cloud Storage support, a reviewed guide, and a listing in Google Cloud Marketplace, which accepts open-source container images and, now, AI agents.

**Nothing on this page is confidential, and there has been no conversation yet.** Every statement about Google Cloud comes from its own public pages, linked. Every statement about sgit points at the [deployment documentation](../deploy/index.md), a published vault or a page on this site. sgit is Apache-2.0, so Google Cloud does not need our permission to run it or to build on it. A partnership is about doing that well and together. The general argument is on [the cloud platforms page](cloud-platforms.md).

## In short

- **Cloud Run is the natural home.** The image honours the injected port and is configured only by environment variables, as Cloud Run expects.
- **Storage is the step to take.** Cloud Storage offers S3 interoperability through its XML API with HMAC keys, which may be enough for the server's S3 mode; a native backend is planned. Neither is tested by us yet.
- **The marketplace fits both halves.** [Google Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs/partners/offer-products) lists open-source container images, and partner agents listed there appear in the Gemini Enterprise Agent Gallery.
- **What we would like:** a reviewed Cloud Run guide, Cloud Storage support, a place in [Partner Advantage](https://cloud.google.com/partners/become-a-partner), and a Marketplace listing.

## How vaults map onto Google Cloud

| sgit needs | On Google Cloud | Status |
|---|---|---|
| **A small stateless API** | Cloud Run | The image is Cloud Run-ready. The guide is documented as planned; the founder has run it. |
| **Object storage** | Cloud Storage | S3 interoperability through the XML API may be enough for the server's S3 mode. Not tested. A native backend is planned. |
| **Static readers** | Cloud Storage with Cloud CDN, or Firebase Hosting | Cloud Storage with Firebase is named in the static hosting guide. |
| **Sovereign data** | [Google Cloud's sovereign offerings](https://cloud.google.com/sovereign-cloud) | Complementary: the host holds ciphertext only. |
| **Agents** | Gemini, and the Gemini Enterprise Agent Gallery | See [the Google Gemini page](google-gemini.md) for the model side. |

## Where we are with Google Cloud today

Google Cloud is the second-best documented path after AWS: the image is ready for Cloud Run and the guide is on the plan. The founder has deployed it there. What stands between that and a customer running vaults on Google Cloud is storage, a review, and a listing.

## What a partnership could be

| Shape | What it would be | On their side |
|---|---|---|
| **1 · Finish the Cloud Run path** | A reviewed Cloud Run guide with Cloud Storage, tested end to end, in the deployment docs. | A reviewer and credits. |
| **2 · A Marketplace listing** | The server as an open-source container image in Google Cloud Marketplace, and later a vault agent listed through the Agent Gallery. | Partner Advantage, Build engagement. |
| **3 · Gemini and vaults** | A vault connector for Gemini CLI and Google's agent products, so agent work lands in a vault on Google Cloud. | See the Gemini page. |

## What we are asking Google Cloud for

1. A technical review of the Cloud Run guide, and help confirming Cloud Storage through its S3 interoperability.
2. A place in [Partner Advantage](https://cloud.google.com/partners/become-a-partner) and a route into Google Cloud Marketplace.
3. Credits through the [Google for Startups Cloud Program](https://cloud.google.com/startup).
4. An introduction to the team behind the Gemini Enterprise Agent Gallery.

## What this page does not claim

- **No endorsement.** Google Cloud has not endorsed sgit, and we have not spoken to anyone there about this. Programme and product descriptions quote Google Cloud's own pages as of 24 September 2026.
- **Cloud Storage through the S3 interoperability layer is untested by us.** It is the obvious first thing to try, not a claim that it works.

## If you work at Google Cloud

This page is written to be forwarded as it is, and everything on it can be checked by the person who receives it. [Who is asking, and how to reach them →](../about/index.md)

[← Microsoft Azure](azure.md)[IBM Cloud →](ibm-cloud.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/partnerships/google-cloud.html)*
