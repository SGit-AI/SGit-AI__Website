# A proposed partnership between sgit.ai and AWS

> We would like to work with AWS more closely, and we are already most of the way there. sgit's deployment templates were written for AWS first, the vault service behind the vaults published on this site answers from Amazon S3 behind CloudFront, and our startup credits are AWS credits. What is missing is the partnership: a reviewed reference architecture, a listing in AWS Marketplace, and a route to AWS customers who need encrypted handover or sovereign storage.

*Source: <https://sgit.ai/partnerships/aws.html> · site v0.6.5 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Partnerships](index.md) / [Cloud platforms](cloud-platforms.md) / AWS

A proposed partnership · sgit.ai with AWS · public material only · 24 September 2026

# A proposed partnership between sgit.ai and AWS

**We would like to work with AWS more closely, and we are already most of the way there.** sgit's deployment templates were written for AWS first, the vault service behind the vaults published on this site answers from Amazon S3 behind CloudFront, and our startup credits are AWS credits. What is missing is the partnership: a reviewed reference architecture, a listing in AWS Marketplace, and a route to AWS customers who need encrypted handover or sovereign storage.

**Nothing on this page is confidential, and there has been no conversation yet.** Every statement about AWS comes from its own public pages, linked. Every statement about sgit points at the [deployment documentation](../deploy/index.md), a published vault or a page on this site. sgit is Apache-2.0, so AWS does not need our permission to run it or to build on it. A partnership is about doing that well and together. The general argument is on [the cloud platforms page](cloud-platforms.md).

## In short

- **sgit fits AWS naturally.** Encrypted vaults are ciphertext in Amazon S3, a small stateless API on Lambda or Fargate, and optionally a static copy behind CloudFront.
- **The templates exist.** CloudFormation for Lambda (a container image with a function URL) and for ECS Fargate is written, lint-clean and in beta, with an EC2 appliance and runbooks for new accounts and regions.
- **The sovereignty story is real on AWS.** The [AWS European Sovereign Cloud](https://aws.amazon.com/blogs/aws/opening-the-aws-european-sovereign-cloud) has been generally available since 14 January 2026, in Brandenburg, with S3, Lambda and ECS. A vault there is ciphertext in a sovereign region, readable by nobody but the key holder.
- **What we would like:** a review of the templates, a listing in [AWS Marketplace](https://aws.amazon.com/partners/marketplace/), a place in the [AWS Partner Network](https://aws.amazon.com/partners/), and a first customer conversation.

## How vaults map onto AWS

| sgit needs | On AWS | Status |
|---|---|---|
| **Object storage** | Amazon S3 | Works today: the server's `s3` storage mode, with buckets named per account and region. |
| **A small stateless API** | AWS Lambda (container image and function URL), ECS Fargate, or an EC2 appliance | CloudFormation templates written and in beta. |
| **Static readers** | S3 and CloudFront | Documented in the deployment docs. |
| **Sovereign region** | AWS European Sovereign Cloud | Not yet tested. S3, Lambda and ECS are available there, so the same templates should apply. |
| **Agent environments** | Ephemeral compute | [sg-compute](https://sg-compute.sgit.ai/) builds agent environments on AWS today. |

## Where we are with AWS today

AWS is where sgit grew up, for two reasons that have nothing to do with preference: the founder has built on AWS for years, and the startup credits sgit has are AWS credits. The result is that the AWS path is the most complete one: the templates, the runbooks, the S3 storage mode and the published vaults all run there. That is also why this page asks for more than documentation. The next step on AWS is not whether it works but whether AWS customers can find it and buy it through the channel they already use.

## What a partnership could be

| Shape | What it would be | On their side |
|---|---|---|
| **1 · A reviewed reference architecture** | The Lambda and Fargate templates reviewed by an AWS solutions architect, published as a reference architecture, and tested end to end in a standard region and in the European Sovereign Cloud. | A partner solutions architect, and credits for the testing. |
| **2 · A Marketplace listing** | The open-source vault server as a free container product in AWS Marketplace, launched into the customer's own account. AWS Marketplace accepts free products and container delivery. | AWS Marketplace, through the AWS Partner Network. |
| **3 · Services on top** | Encrypted data rooms, agent handover and connector twins, offered by AWS consulting partners on their customers' accounts. Every one is published here as a working vault. | The AWS Partner Network's consulting partners. |

## What we are asking AWS for

1. A review of the CloudFormation templates by someone who knows Lambda and Fargate well.
2. Help testing in the AWS European Sovereign Cloud.
3. A route into [AWS Marketplace](https://aws.amazon.com/partners/marketplace/) for the open-source server as a free container product.
4. Membership of the [AWS Partner Network](https://aws.amazon.com/partners/) and an introduction to the ISV team.
5. Continued support through [AWS Activate](https://aws.amazon.com/startups/credits/), which is how the AWS path was built.

## What this page does not claim

- **No endorsement.** AWS has not endorsed sgit, and we have not spoken to anyone there about this. Programme and product descriptions quote AWS's own pages as of 24 September 2026.
- **Beta means beta.** The Lambda and Fargate templates are written and lint-clean; they are not yet a reviewed reference architecture.
- **The sovereign region is untested by us.** We say the templates should apply there because the services they use are available, not because we have run them.

## If you work at AWS

This page is written to be forwarded as it is, and everything on it can be checked by the person who receives it. [Who is asking, and how to reach them →](../about/index.md)

[← Cloud platforms](cloud-platforms.md)[Microsoft Azure →](azure.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/partnerships/aws.html)*
