# Published vaults — sgit.ai

> Every vault whose read key sgit.ai has deliberately published: what each does, the features it uses, and the vault running live in the page. A read key is the complete credential — no account, no write capability.

*Source: <https://sgit.ai/demos/vaults/index.html> · site v0.2.62 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../index.md) / Vaults

# Published vaults

Every vault whose read key this site has deliberately published — with, for each one, a page describing what it does, the features it uses, what the shape is good for, and the vault itself running live inside that page — where you will also find its read key and a link that opens it. A read key is the complete credential: no account, no token, and no write capability anywhere in it.

**Publishing one of your own?** [**The method is written down**](publishing.md) — the seven steps behind every row below, the tools that do each one, and the mistakes that produced each rule. Written to be followed by another site's agent.

**Intake, since it nearly went wrong.** A credential submitted for publication here was once a **vault key** described as a read key — a legacy `passphrase:vault_id` form with no prefix to give it away. It was caught, only the derived read key was published, and nothing leaked; but the catch depended on somebody looking. Every submission now runs through `admin/build/check_credential.py` first, which refuses a write credential by **prefix** (`sgit_vk1_`, which new vaults emit) or, for anything older, by **shape** — a read key is 64 hex characters, and anything else before the colon is a passphrase. Prefixes are the better answer; the shape check covers the years of keys created before them.

**The two rules, applied to every row.** Read keys yes, vault keys never — a read key is a capability we hand out on purpose, and it cannot become write access. And every vault is audited before its key appears here, because content travels with the key forever; findings are published on the vault’s page, not filed away.

**25 published vaults** — 5 analysis, 5 application, 4 reference, 3 briefing, 3 presentation, 3 record, 1 gallery, 1 report. Newest first; **click any heading to sort**. Every read key and the live link are on the vault's own page.

| # | Vault | What it is | Category | Files | Size | Published |
|---|---|---|---|---|---|---|

| 25 | [Agent permission games](agent-permission-games/index.md)`4evnlwrj` | Two games about grants and mandates — the first vault here that phones home | Application | 68 | 2.6 MB | 2026-09-06 |

| 24 | [AIUC-1 conformance layer](aiuc-1-conformance/index.md)`2wzct4k7` | The AIUC-1 standard as a graph, plus a conformance layer that computes insurability | Reference | 649 | 43 MB | 2026-09-05 |

| 23 | [Licence to Operate](licence-to-operate/index.md)`posrhzp3` | An insurance policy for an agent, simulated: grant, mandate, and the delta nothing covers | Analysis | 121 | 13 MB | 2026-09-04 |

| 22 | [VoiceDebrief pitch (FI)](voicedebrief-pitch/index.md)`95i2xqrd` | A three-minute investor pitch as a presenter app, with script, timings and sources | Presentation | 48 | 17 MB | 2026-09-02 |

| 21 | [Scaling Threat Modeling](threatmodcon-2025/index.md)`0ict6flm` | ThreatModCon 2025: eleven linked threat models across 51 nodes and 179 threats | Presentation | 53 | 4.1 MB | 2026-08-27 |

| 20 | [AI vs. AI — Black Hat EU 2025](blackhat-eu-2025/index.md)`k1izvg7e` | The Black Hat EU 2025 keynote, with its PDF exports and eight research papers | Presentation | 87 | 20 MB | 2026-08-27 |

| 19 | [Standards Atlas — GDPR](standards-atlas-gdpr/index.md)`4zv4bvmu` | GDPR as a semantic graph, with writes scoped to a feedback folder | Reference | 116 | 6.3 MB | 2026-08-25 |

| 18 | [RiskMandate · File security](riskmandate-file-security/index.md)`wu365g94` | An eleven-step risk-acceptance walk, running SQLite in the browser | Analysis | 71 | 2.7 MB | 2026-08-25 |

| 17 | [Penetration Test Report](pentest-report/index.md)`o4lrwx02` | A penetration test report (fictional) with a re-test script per finding | Report | 93 | 6.4 MB | 2026-08-25 |

| 16 | [SG/Payments Brief Pack](payments-brief-pack/index.md)`o3m0sz3q` | A payments briefing pack, marked PROPOSED rather than dressed as decided | Briefing | 18 | 224 KB | 2026-08-25 |

| 15 | [Content-Transformation Proxy](content-transformation-proxy/index.md)`3c90c2bff2b1` | An as-built engineering brief, shipped with its slides, diagrams and source PDFs | Briefing | 140 | 63 MB | 2026-08-25 |

| 14 | [SG Commercialisation](commercialisation/index.md)`haeu7p1e` | A commercial operating model — with its customer register deliberately left empty | Briefing | 78 | 536 KB | 2026-08-25 |

| 13 | [Vault App Mode](vault-app-pocs/index.md)`xth1xt78` | Nine proofs of concept for vault app mode, with a hub that runs them | Reference | 57 | 251 KB | 2026-08-23 |

| 12 | [Private Health Score](health-score/index.md)`zc6abngv` | A clinical questionnaire scored by a versioned framework, with a clinician review screen | Application | 35 | 1.2 MB | 2026-08-23 |

| 11 | [VoiceDebrief](voice-debrief/index.md)`k6xy9z4d` | Four apps in one vault, from raw recording to structured debrief | Analysis | 92 | 1.2 MB | 2026-08-22 |

| 10 | [Regulation Graph](regulation-graph/index.md)`73heuprz` | The EU AI Act parsed from Formex into an evidence graph, article by article | Reference | 207 | 14.9 MB | 2026-08-20 |

| 9 | [Risk Mandate](risk-mandate/index.md)`4zf6pf2z` | A working software project delivered as a vault — and it calls an LLM holding no API key | Application | 124 | 1.9 MB | 2026-08-17 |

| 8 | [Risk Graph Explorer](risk-graph-explorer/index.md)`3simlnqe` | A fact-to-risk graph explorer, built to be public: its app.json requests nothing | Application | 33 | 428 KB | 2026-08-17 |

| 7 | [Agentic Browser Isolation](agentic-browser-isolation/index.md)`0610gsp9` | Should an agent browse with your logged-in sessions? A living risk graph, per stakeholder | Analysis | 104 | 2.4 MB | 2026-08-17 |

| 6 | [Supplement Stack](supplement-stack/index.md)`r7zes477` | A patient-held health record: a real regimen, label photos, totals against UK RNIs | Record | 23 | 2.3 MB | 2026-08-16 |

| 5 | [Strategy Maps](strategy-maps/index.md)`ookq4mn4` | The SG/Send strategy in seven Wardley maps, plus the sgit positioning analysis | Analysis | 33 | 830 KB | 2026-08-16 |

| 4 | [Field Notes](field-notes/index.md)`4bshby5n` | Six studies with generative SVG art — the smallest complete vault app | Application | 4 | 11 KB | 2026-08-16 |

| 3 | [Deploy Docs](deploy-docs/index.md)`fyofmkvr` | Living deployment documentation, updated by an sgit push with no site deploy | Record | 17 | 25 KB | 2026-08-16 |

| 2 | [The Vault Catalogue](catalogue/index.md)`kc67yhgw` | An index of published vaults that is itself a vault, and lists itself | Record | 9 | 11 KB | 2026-08-16 |

| 1 | [Algarve · May 2026](algarve-may-2026/index.md)`3d04e6b9ca98` | A travel diary: twenty photographs in three sizes and an eight-chapter narrative | Gallery | 71 | 29 MB | 2026-08-16 |

The machine-first version of this list is [the catalogue](../../catalogue/index.md) — an index of vaults that is itself a vault, updated by an sgit push with no site deploy. New entries start there: a read key and one line, the rest derived. The walkthrough of how a vault gets published at all — creation, audit, deliberate key publication, embed — is on [the embed demo page](../vault-app-embed.md).


---

*[Site index for agents](../../llms.txt) · [HTML version](https://sgit.ai/demos/vaults/index.html)*
