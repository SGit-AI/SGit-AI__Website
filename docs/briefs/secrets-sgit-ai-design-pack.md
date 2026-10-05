# The identity and secrets design pack, 4 to 5 October 2026, sgit.ai

> Five design documents and a starter prompt from the week a plan to give every agent and user a Google Workspace identity met Google's terms: the Workspace architecture briefing, the onboarding design with the terms research and the tier model, the AWS Cognito variant and why no secret can live in an identity provider, the all-GCP key vault and password manager design, and the secrets.sgit.ai MVP build brief. Published as written, to be corrected.

*Source: <https://sgit.ai/docs/briefs/secrets-sgit-ai-design-pack.html> · site v0.6.68 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../index.md) / [Briefs](index.md) / The identity and secrets design pack

# The identity and secrets design pack, 4 to 5 October 2026

**Five design documents and a starter prompt, published as written.** Status: a design pack handed to a new repository, `SGit-AI__Website__Secrets`, for the site that will be `secrets.sgit.ai`. Written 4 and 5 October 2026 by Dinis Cruz with the RiskMandate and sgit teams. Nothing in it is built yet; the MVP brief's own reality file will say when something is. The argument around it is in the article [The identity we wanted to give the agents](../../articles/the-identity-we-wanted-to-give-the-agents.md).

**Why this is here, and in this order.** The pack is the record of a design changing under its own research. The first document assumes one Google Workspace tenant with a seat per customer, per user and per agent. The second reads Google's terms and finds that a tenant may hold one organisation's people unless Google agrees otherwise in writing, and rebuilds the tiers. The third asks whether AWS Cognito would be simpler and finds the rule that no secret can live inside an identity provider. The fourth picks one cloud per deployment and designs the keyring. The fifth is the instruction set for building it, with the decisions marked closed. Read in order, it is a week of thinking; read the fifth alone, it is a build plan.

## The documents

| Document | What it holds | Date |
|---|---|---|
| [**Workspace as identity, storage and deployment substrate**](secrets-sgit-ai-design-pack/riskmandate-workspace-architecture-briefing.md) | The first plan: a Workspace account per customer as identity provider, data home and cloud organisation, with sgit encrypting before Google and a passkey PRF unwrapping the key. Three tiers, shared to private. Section 11 adds the Marketplace domain install for client-side Drive and Gmail reads. The hard constraint found here: standard Workspace storage has no admin-proof zone, so encryption has to happen before Google. | 4 Oct |
| [**User onboarding and account experience**](secrets-sgit-ai-design-pack/riskmandate-user-onboarding-account-experience.md) | Password once, then passkey; provisioning variants; the first-run flow; the admin checklist; the rejected alternatives. Then the update that changed the design: Research A on Google's commercial terms, with the clauses and their impact, and Research B on who else has done each half of this. The five-tier model that resulted, and the request to put to Google in writing. | 4 Oct, updated 5 Oct |
| [**AWS Cognito client-side architecture**](secrets-sgit-ai-design-pack/riskmandate-aws-cognito-architecture.md) | The AWS variant: Cognito for login, an identity pool for short-lived credentials, S3 per user prefix, and the per-user keyring. The argument that nothing stored inside Cognito or KMS can be kept from the account's administrator, so the authority to decrypt must come from the user's authenticator. The attack table: what a full administrator compromise can and cannot do, and the one place client-side crypto does not hold, the served JavaScript. | 5 Oct |
| [**GCP key vault architecture and password manager MVP**](secrets-sgit-ai-design-pack/riskmandate-gcp-key-vault-password-manager-mvp.md) | The decision to build all in GCP, one project per deployment, with Identity Platform, Cloud Storage for Firebase, Security Rules and a passkey PRF as the only thing that decrypts. The keyring, the sharing scheme with a key pair per user, the storage layout, and why a password manager is the right first build: if an administrator with full access cannot read a password, the model holds for vault keys. | 5 Oct |
| [**secrets.sgit.ai MVP build brief**](secrets-sgit-ai-design-pack/secrets-sgit-ai__mvp-build-brief.md) | The instruction set, written to be executed. Principles, architecture, the GCP environments and Terraform, browser-side environment configuration, the site's pages, the house style, the keyring and crypto specification v1 with its key hierarchy, the CI pipeline with its eight-check gate, testing, the build order in nine releases, and what not to do. | 5 Oct |
| [**The initial prompt**](secrets-sgit-ai-design-pack/initial-prompt.md) | What is pasted into the first Claude Code session in the new repository: the rules never to break, the order of work, and where to record what the brief got wrong. | 5 Oct |

## What to read it against

- [Who holds the keys?](../../partnerships/vault-key-management.md), the partnership call of 24 September that asked for exactly this: a way for a person to keep vault keys in the password manager or identity system they already use, opened with a passkey, with scoped and time-limited keys for agents.
- [Credentials](../credentials.md) and [sgit pki](../pki.md): the key classes, the one-way derivation of a read key, and the key pair algorithms the keyring reuses.
- [Six agents, one inbox](../../articles/six-agents-one-inbox.md) and [Replicating the agentic inbox](../../articles/replicating-the-agentic-inbox.md): the agent identities as they run today, one Workspace seat, one Claude seat and one GitHub account per agent, which is the arrangement the terms research bears on.
- [Agent Contact](../agent-contact.md): "the site is the identity", the lane identity for signed agent mail that is not a mailbox.

These documents are published under CC BY 4.0 and will also live at `secrets.sgit.ai/docs/design/` once that site exists, with a corrections file beside them. Where this copy and that one differ, that one is current. Terms research in them is not legal advice.


---

*[Site index for agents](../../llms.txt) · [HTML version](https://sgit.ai/docs/briefs/secrets-sgit-ai-design-pack.html)*
