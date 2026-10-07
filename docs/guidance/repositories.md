# Every sgit repository: how the sites, the tools and the code are built, guidance

> The page above the vault guidance, the team section, coding.sgit.ai and nfrs.sgit.ai: what every repository in the estate carries regardless of what it is for. The brief published in full, written by a person or an agent; the reality and corrections files; one version going up on every push; the gate and the release discipline; the review folder with its self set; the code rules by reference to coding.sgit.ai; credentials; the requirements that are not features; people, agents and writing; and two checklists, one for a new repository and one for an existing one.

*Source: <https://sgit.ai/docs/guidance/repositories.html> · site v0.6.89 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../index.md) / [Guidance](index.md) / Every repository

# Every sgit repository: how the sites, the tools and the code are built

The page to read before starting or changing any repository in this estate, whether it is a `*.sgit.ai` site, a tool such as the sgit CLI, a vault app or a service. Until now this guidance lived in four places, each covering one slice: [the vault guidance](index.md) here, which says of itself that it stops at vaults; [the team section](../../team/index.md), which is how this one site is run; [coding.sgit.ai](https://coding.sgit.ai/), which measured how the code is written; and [nfrs.sgit.ai](https://nfrs.sgit.ai/), which holds the requirements that are not features. This page is the one above them: what every repository carries regardless of what it is for, with the edge to the page that owns each detail. It is short on purpose and mostly links, for the reason [the vault guidance gives](index.md#why).

**The one-minute version.** A repository here starts from a **brief, published in full**, written by a person or by an agent from the person's words. It carries a **reality file** that says what exists, a **corrections file** that says where the brief was wrong, **one version number** that goes up on every push, a **gate** that fails the build, and from now a **review folder** that reads every change upwards to the brief. Code follows **the house style coding.sgit.ai measured**, not a style somebody preferred. **Read keys may be published; vault keys never.** A release is not done until the live thing serves the new version. Every number on a page is counted, not remembered, and the page says what it does not prove.

Status: first version, written 6 October 2026 from what sgit.ai, coding.sgit.ai, nfrs.sgit.ai, the sgit CLI and the SG/Send repository actually do, and from the briefs that started the secrets.sgit.ai repository. Where the five disagree, this page says which to follow and why; where it is wrong, the first repository to find out records it in its corrections file and this page is corrected from there.

## 1. Three kinds of repository, one shape

| Kind | Examples | What differs |
|---|---|---|
| **A site** | sgit.ai, coding.sgit.ai, nfrs.sgit.ai, graphs.sgit.ai and the rest of [the network](../../network/index.md); secrets.sgit.ai next | Static HTML built by a script from content files, deployed by GitHub Pages from the development branch; every page has a `.md` twin and the site has an `llms.txt`; nav and footer injected at build so they cannot drift; a participant disclosure |
| **A tool or library** | the sgit CLI, osbot-utils, the Send server and its services | Python under the Type_Safe rules with a test suite that runs against real objects; a package version in one file; releases tagged and published |
| **A vault app or a component set** | the Code Review Graphs app, the How Much Evidence app, the tools components, the review navigator this page asks for | JavaScript as native web components, three files each on one base component, no framework and no build step; versions shown in the app's own chrome; published as a vault with a read key |

What is the same is everything below. A site is not excused from tests because it is content, and a tool is not excused from a brief because it is code.

## 2. What every repository carries

| Thing | Where it lives and what it is for | The page that owns it |
|---|---|---|
| **The brief, in full** | The document the work started from, published as written, dated, with its status, and never edited to look right afterwards. A brief may be written by a person or by an agent from a voice memo or a conversation; what makes it the brief is that the person read it and said go. Corrections go in the corrections file, not into the brief. | [The briefs](../briefs/index.md); [coding.sgit.ai on the network](https://coding.sgit.ai/network/index.html): "a commissioning brief published in full, a static site written from it" |
| **The reality file** | What exists, by domain, kept current by whoever ships. The rule from the Send repository's Librarian: a feature that is not in the reality file does not exist, and nobody may say a thing works because a brief describes it. | [The Librarian's reality files](https://github.com/the-cyber-boardroom/SGraph-AI__App__Send/blob/dev/team/roles/librarian/reality/README.md); [nfrs.sgit.ai, the reality system](https://nfrs.sgit.ai/) |
| **The corrections file** | `BRIEF-CORRECTIONS.md`, or the equivalent the brief names: where the brief was wrong, what was found, what was done instead. Every brief on this site says it will be corrected from this file; a repository without one has nowhere to put the finding. | [The review brief](../briefs/code-review-graphs-in-the-repository.md), section 12; [the secrets design pack](../briefs/secrets-sgit-ai-design-pack.md), the initial prompt |
| **One version, going up on every push** | A single source of truth for the version, in the repository root or the build script, bumped on every push, shown on every page or in the app's chrome, and linked to a release history with a sentence per release that says what changed and why, not "UI improvements". | [Version everything, show the version](index.md#versions); [this site's release history](../../admin/versions.md) |
| **The gate** | A validator that fails the build and a release script that refuses to push until it passes. What it checks is the repository's business, listed on its admin page; that it exists and is run before every push is not. | Section 4 below; [this site's admin page](../../admin/index.md) |
| **Tests that run against real things** | No mocks. Tests build the real object, call the real code and check the real result; a credential test has a negative control; a crypto test has a published vector. | [coding.sgit.ai, the rules and the four testing non-negotiables](https://coding.sgit.ai/rules/index.html); [nfrs.sgit.ai, testing](https://nfrs.sgit.ai/) |
| **The review folder** | `review/`: the project as layered graphs, intent written from the brief and the code derived from the tree, every commit read upwards, a navigator, and `review/self/` reviewing the tool itself. New repositories from the first commit; existing ones from their next change. | [Code review graphs in the repository](../briefs/code-review-graphs-in-the-repository.md) |
| **Roles and a board, as files** | Who does what, as one file per role with the rules it enforces and the mistake behind each; the work as files with a status line, in the repository or in a vault of its own. A new agent reads the team page and one role and begins. | [How this site is run](../../team/index.md); [issues-fs.sgit.ai](https://issues-fs.sgit.ai/); the Explorer team in the CLI repository |
| **A credentials tier that is never committed** | A gitignored directory for keys, scanned by a tripwire before every commit, with the write key escrowed there before anything is published. The repository's own secrets and other people's are both scanned for. | Section 6 below; [Publishing: the method](../../demos/vaults/publishing.md) |
| **Machine-readable twins** | On a site, a `.md` twin for every page and an `llms.txt` at the root and per section, generated from the same data as the pages. On a tool, the same role is played by the reality file and the docs an agent is pointed at first. | [this site's llms.txt](../../llms.txt); [coding.sgit.ai on the markdown twin](https://coding.sgit.ai/html/index.html) |
| **Licences and the disclosure** | Code Apache-2.0, content CC BY 4.0, each file or page saying which; a site published by the project that builds what it measures says so on a participant disclosure page. | [open-source.sgit.ai](https://open-source.sgit.ai/); [coding.sgit.ai's disclosure](https://coding.sgit.ai/about/participant.html) |

## 3. The release discipline

- **Bump, build, validate, push, verify.** In that order, by one script, every time. The version goes up on every push, the commit subject carries it, the validator must pass, and the script polls the live thing for the new version and aborts if it never appears. A clean push is not a release.
- **One sentence per release** in the release history, saying what changed and why, in words a reader can act on. The history is the repository's memory and the first place an agent in a fresh session reads.
- **Publish, then correct above the mistake.** When another team's review or a reader finds the work wrong, the correction is published where the mistake was, dated, with the mistake left visible. This has run for every release of this site since 14 August 2026 and the count is computed on the homepage, not typed.
- **Count, don't remember.** Every number on a page is computed from the thing it counts; every number in prose is checked against a file that day and the file is named.
- **Say what it is worth.** Each release states precisely what it does not prove. A measured finding, a position with the evidence attached and a guess are three different things and are labelled as such.

## 4. The gate

Each repository decides what its gate checks and lists it on its admin or engineering page. The checks below are the ones that exist today in at least one repository and have each caught a real defect; a new repository starts from this list and removes nothing without saying why in its corrections file.

| Check | What it caught | Where it runs today |
|---|---|---|
| Every internal link resolves against the real file tree; a page nothing links to fails | Orphan pages that were published and unfindable | sgit.ai validator |
| Every inline script and site script parse-checks | A syntax error that only showed on one page | sgit.ai validator |
| No `<link href>`, `<script src>` or `<img src>` reaches outside a vault app | Apps that worked on a dev machine and not in the host | sgit.ai validator, the vault-app contract |
| Every page has its `.md` twin and appears in `llms.txt` | Pages agents could not read | sgit.ai validator |
| Banned words and retired names; em-dashes in prose; unsupported absolutes as an advisory | Legacy naming, and prose that sounded alarmist | sgit.ai validator |
| The leak tripwire: sgit credential shapes, private key markers, cloud key prefixes, named people's data, and the secret parts of every locally held vault key, against the staged diff | A vault key in a log, a live third-party key in a field that matched no sgit pattern | sgit.ai release script; the method in [Publishing](../../demos/vaults/publishing.md) |
| Type_Safe structural guards: no raw primitives in schema classes, no module-level functions, round-trip `from_json(obj.json()).json() == obj.json()` | Schemas that serialised differently from how they parsed | sgit CLI and Send test suites |
| Crypto test vectors against the browser's output, byte for byte | A derivation that matched itself and not the Web Crypto API | sgit CLI |
| Determinism: the same inputs produce byte-identical derived files | Not yet caught anything; required by the review brief | The review folder, section 8 of its brief |
| Freshness: a derived folder older than the tree it describes fails | Not yet caught anything; required by the review brief | The review folder |

The secrets.sgit.ai MVP brief names its own version of this an eight-check gate; it is the newest and it is the one a new repository should copy first. coding.sgit.ai's finding stands and should be read as a warning: as of its last count, no linter, formatter or type-checker ran anywhere in the estate, and the structural guards were the whole automated enforcement surface. Enforcement lives in each repository's gate or it does not live.

## 5. The code, by reference

The style is not a preference; it was counted out of the code and published with the numbers that do not flatter. This page does not restate it. The rules a new repository adopts on day one, with the page that owns each:

| Language | The rules that matter most | Read |
|---|---|---|
| **Python** | Type_Safe for every data class; `Safe_Str`, `Safe_Int` and their domain subclasses instead of raw primitives; classes for everything, no module-level functions, no static methods; immutable defaults; one idea per file; per-block alignment of annotations; the round-trip invariant for every schema; no Pydantic, no boto3 in domain code, no mocks. | [coding.sgit.ai, Python](https://coding.sgit.ai/python/index.html); the CLI repository's `CLAUDE.md` |
| **JavaScript** | Native web components, no framework, no bundler, no build step; exactly three files per component with the same basename; a base component that supplies the lifecycle, self-location through `static jsUrl = import.meta.url`, and `onReady()` instead of `connectedCallback`; events namespaced and dispatched through `document` with `bubbles` and `composed`; frozen, centralised constants; ESM only. A large single-file app is a build output, never a source. | [coding.sgit.ai, JavaScript](https://coding.sgit.ai/javascript/index.html) |
| **HTML** | A component's markup is a fragment; semantic elements, a real control for every interaction, ARIA on each; `data-*` for behaviour and classes for styling, never mixed; nav and footer injected at build time; a markdown twin for every page. | [coding.sgit.ai, HTML](https://coding.sgit.ai/html/index.html) |
| **CSS** | `:host` first; every colour a token and no literal colour outside the token file; per-block value alignment; flexbox with gap; no BEM, because shadow DOM removes the leak it was written for. | [coding.sgit.ai, CSS](https://coding.sgit.ai/css/index.html) |
| **Bash** | As little as possible; generated shell from a Python section pattern where it is needed. | [coding.sgit.ai, Bash](https://coding.sgit.ai/bash/index.html) |
| **Dependencies** | Nothing fetched at build or run time that is not vendored, pinned and hashed; a public component served from a versioned path is pinned at the depth the consumer wants, major, minor or exact. | [the versioned CDN path](https://coding.sgit.ai/javascript/index.html); [the review brief](../briefs/code-review-graphs-in-the-repository.md), section 8 |

coding.sgit.ai also lists what is not settled: semicolons, two banner styles, a legacy event namespace, the underscore-private rule that contradicts a Python rule. A repository picks one answer to each, writes it in its gate, and records the choice in its corrections file so the site can be updated. It does not reopen the question in every file.

## 6. Credentials

- **Read keys yes, vault keys never.** A read key is derived one-way and cannot become write access. A vault key is write access and has no partly-public form. Escrow the write key before publishing, not after.
- **Scan for other people's secrets too.** A scan built for sgit credential shapes will not catch a provider's API key in a field with an unrelated name. The tripwire checks the generic shapes as well, and the secret part of every key the repository has ever held locally.
- **Every credential test needs a negative control.** A clone succeeds as a directory whether or not the key was valid; the marker that discriminates is the clone mode file. A test that would pass with a wrong input has proven nothing.
- **Session-only credentials stay in the session.** A comms vault, an access token or a write key an agent is handed for a task is used in that session and never written to a repository, a vault or a page. Masked output is the default when a tool prints a key.
- **Nothing a repository needs to run is a secret.** Configuration that differs per environment is read at run time in the browser or from the environment; a repository that cannot build without a secret has a design problem, not a configuration problem.

The method, with the classification step that comes before anything touches a key: [Publishing: the method](../../demos/vaults/publishing.md); the key classes themselves: [Vault credentials](../credentials.md).

## 7. The review

From 6 October 2026 every repository carries a `review/` folder as [the review brief](../briefs/code-review-graphs-in-the-repository.md) specifies: the intent written top down from the brief, by a person or an agent and accepted by a person; the code derived bottom up from the syntax tree by a parser, never by a model; the join between the two with a coverage figure; every commit read upwards to the surfaces and stories it can reach, with the claim in the commit message checked against the evidence; a navigator built as web components; and `review/self/`, the same folder for the tool, both green before a release. A repository that starts after this date builds it before its first source file. One that already has history starts from its next commit and lets the graph grow along the paths people walk. secrets.sgit.ai is the first of the former; this site and the sgit CLI are the first two of the latter.

## 8. The requirements that are not features

Version control, reliability, resilience, security, backups, consistency, explainability and documentation are the project's own list, written before any site existed, and [nfrs.sgit.ai](https://nfrs.sgit.ai/) is its table of contents: testing and CI, resilience, the reality system, budgets as a discipline, project management, and an honest column with a scorecard and a page that names backups as a gap. A repository does not restate them. It adds one row to the honest column for itself: which of these it meets, measured, and which it does not yet, said plainly. The budgets page applies to agents in particular: each script in a pipeline has a time and size budget written down, and a run that exceeds it is a finding rather than a delay.

## 9. People and agents

- **Briefs come from a person's words, in either hand.** The person speaks or writes; an agent often drafts; the person accepts. Both are recorded. An agent never edits the person's own briefs directory; it writes next to it, under its own name and date.
- **Roles are files** with the rules each enforces and the mistake that produced each rule; a starting prompt per role; a board of work as files. The sgit.ai team section and the Explorer team in the CLI repository are the two instances, and they mirror each other on purpose.
- **Agents run under a behaviour policy.** What an agent may reach, what it is mandated to do, the gap between the two and the barriers in place are written before it runs, in the shape [RiskMandate's Agent Behaviour Policy](https://riskmandate.ai/abp.html) gives; its footprint afterwards is read from the logs and compared.
- **Other teams review the work**, and the review is published with the reply. The newsroom's briefing to this site and the answer to it are the pattern; a review that stays in a chat did not happen.

## 10. Writing

- State the status of everything: published, draft, proposed, verified, reconstructed. Say when a thing does not exist yet rather than describing it in the present tense.
- Source every claim to a file, a commit, a count or a named document; where a claim is a position, attach the evidence and call it a position.
- Avoid absolutes the evidence does not carry: say what was found and what was done, not what nobody has or what is impossible. The validator lists them as an advisory on every build of this site.
- No em-dashes in prose; sentences with verbs; numbers in tables; figures with fictional names and example domains only, and no real contact data.
- Publish the finding. An audit result, a gap, a correction goes on the page, not in a file nobody reads.

## 11. Two checklists

| A new repository, before the first source file | An existing repository, in this order |
|---|---|

1.
2.
3.
4.
5.
6.
7.
8.
9.
10.

1.
2.
3.
4.
5.
6.
7.
8.

| The brief, published in full, with its status and date, and the initial prompt that will start the first session.`BRIEF-CORRECTIONS.md`, empty, and the reality file, saying nothing exists.The version in one place, the release history with its first entry, the release script that bumps, builds, validates, pushes and verifies live.The gate, starting from section 4 with nothing removed.The gitignored credentials tier and the leak tripwire wired into the release script.`review/intent/` from the brief, each node carrying its section; the navigator's shell and base component; `review/self/` for the tools.The roles file and the board, even if one person and one agent fill every role.The licence notices and, for a site, the participant disclosure, the `.md` twins and `llms.txt`.The code rules from section 5 copied into the gate as checks, not into a document as wishes.The honest column row on nfrs.sgit.ai, saying what is not yet met. | Find the brief it started from and publish it as it was; if there was none, write down that there was none.Add the corrections file and the reality file, and fill the reality file from the code, not from memory.Check the version is one number in one place that goes up on every push; if not, make it so before anything else.Run the leak tripwire over the whole history once, and over the staged diff from now on.Add `review/` from the next commit, delta first, and `review/self/` with it.Compare the gate with section 4 and add what is missing, one check per release.Write the roles that are actually being played and the board that actually exists.Add the honest column row, including the gaps the first six steps found. |

## 12. Where the rest lives

This page is the node above four others and it should stay that way. For vaults specifically, [Working on a vault: start here](index.md). For how one site is run day to day, [the team section](../../team/index.md). For how code is written, measured, [coding.sgit.ai](https://coding.sgit.ai/). For what a system owes the people who depend on it, [nfrs.sgit.ai](https://nfrs.sgit.ai/). For the grammar every graph in the estate uses, [graphs.sgit.ai](https://graphs.sgit.ai/). For the open-source position and the licences, [open-source.sgit.ai](https://open-source.sgit.ai/). For the whole map of sites and what each answers to, [the network](../../network/index.md). If a question about a repository is answered on none of these, that is a gap, and the place to record it is this page's own corrections, in [the briefs](../briefs/index.md) as a reply.

Written 6 October 2026 by the sgit.ai site team, after the author asked whether a central guidance for the estate's repositories existed and the check found that it did not. Companion material: the vault guidance, the team section, the review brief, the secrets design pack, coding.sgit.ai and nfrs.sgit.ai. CC BY 4.0.


---

*[Site index for agents](../../llms.txt) · [HTML version](https://sgit.ai/docs/guidance/repositories.html)*
