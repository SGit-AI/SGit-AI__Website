#!/usr/bin/env python3
"""Generate every page of the sgit.ai vault site from a shared template.

Release process (see admin/index.html):
  1. bump SITE_VERSION below (v0.1.n — n increases on every push)
  2. add a row to VERSION_LOG
  3. run this script, run the validation suite, sgit commit + push
"""
import os
import re
import json

from content import Content_Loader, Content_Error
from html.parser import HTMLParser

SITE_VERSION = 'v0.2.48'
BUILD_DATE   = '2026-08-15'

def find_vault_root():
    d = os.path.dirname(os.path.abspath(__file__))
    while not os.path.exists(os.path.join(d, 'app.json')):
        parent = os.path.dirname(d)
        if parent == d:
            raise SystemExit('vault root not found (no app.json above this script)')
        d = parent
    return d

VERSION_LOG = [
    ('v0.2.48', '2026-08-27', 'this release',
     "BOTH PRESENTATION VAULTS NOW LINK THEIR PUBLIC SOURCE. Confirmed by the author that "
     "the-cyber-boardroom/Presentation__BlackHat-EU__Dec-2025 and "
     "DinisCruz/Presentation-Threat-Mod-Con-2025 are public repositories. This settles a question "
     "left open when the Black Hat vault shipped: the branding note was written without being "
     "able to establish whether the material was already in the open, because github.com returns "
     "403 to this container's proxy for any repo outside the session's scope — the same 403 for "
     "both repos, which is a proxy behaviour and not a signal about either. The consequence is "
     "worth stating precisely: the vault is a SECOND copy of material that already sits in public, "
     "not the thing that first exposes it, and the Black Hat speaker-template assets in "
     "particular are therefore not published here for the first time. The branding note itself is "
     "unchanged and still stands — the deck uses the official template because it is a talk that "
     "was given there, published as the speaker's own material and not as anything endorsed by or "
     "affiliated with the conference. On the ThreatModCon page the link earns its place for a "
     "different reason: that vault repairs two upstream files that are invalid JSON, and a repair "
     "expressed as a proof (four stray brackets removed, one `],` added, multiset of content lines "
     "unchanged) is only auditable if a reader can fetch the broken originals — so the link sits "
     "in the repair section rather than in a footer. Both URLs were taken verbatim from each "
     "vault's own README rather than retyped."),
    ('v0.2.47', '2026-08-27', 'obj-cas-imm-dac438a3ef81',
     "THE DIRECTORY ANSWERS QUESTIONS, and a second conference vault. Nineteen sibling sites is "
     "past the point where a list helps, so /network/ now carries a chat panel whose only job is "
     "routing: which of these is mine. THE DEFAULT TIER NEEDS NO KEY, NO ACCOUNT AND NO NETWORK "
     "CALL — a deterministic scorer running in the browser over a catalogue emitted at build time "
     "from admin/content/sites/*.md, the same data the cards and the table are built from, so the "
     "answers cannot drift from the directory underneath them. It also SHOWS ITS WORKING: a hit in "
     "a site's thesis or domain outweighs one in its summary, and the reply names the matched "
     "terms, which an LLM answer does not give you. Tier 1 is opt-in BYOK against OpenRouter, "
     "streaming, reusing the pattern already proven in the SG/Vault workbench vault (same "
     "endpoint, same versioned sg-llm-request module on dev.tools.sgraph.ai) rather than "
     "inventing a client; on failure it falls back to the local matcher and says so. The cost is "
     "stated on the panel, not buried: with no host there is no permission floor, so the key sits "
     "in the page's origin — never sent to sgit.ai, which has no server to send it to. Tier 2 (the "
     "vault-app build, where sg.llm.chat keeps the credential in .vault/llm/config.json below the "
     "permission floor) is NOT BUILT and is scoped in a new article including the rows that are "
     "not started. ONE REAL MISS FIXED: the matcher routed 'I need to cite a regulation precisely' "
     "to wardley-maps, because it knew only each site's own vocabulary — standards.sgit.ai says "
     "'provision' and the reader types 'regulation'. Site entries gained an `aliases` field for the "
     "words readers actually arrive with; five real questions now give five correct first hits, and "
     "nonsense still returns nothing rather than a confident wrong answer. TWO BUILD RULES CAUGHT "
     "ME on the way, both correctly: the validator refused a forward link to the unwritten plan "
     "article, and then refused a script tag with a src attribute outright — these pages must also render inside a "
     "vault on a blob: origin where a relative src does not resolve, so the loader is fetch+eval "
     "like every other component here. ALSO PUBLISHED: ThreatModCon 2025 Barcelona, 'Scaling "
     "Threat Modeling with Semantic Knowledge Graphs' — eleven linked threat models from customer "
     "to compute instance (51 nodes, 179 threats, 3 critical), five interactive views and five "
     "Wardley walkthroughs, libraries inlined at identical versions so no page touches the "
     "network. Two of its layer files are INVALID JSON UPSTREAM and are repaired in the vault, "
     "with the repair expressed as a proof rather than a changelog entry: four stray closing "
     "brackets removed, one `],` added, multiset of content lines unchanged, originals kept "
     "alongside. Its explorer screenshot was CAPTURED AND THEN DISCARDED — outside the vault host "
     "there is no sg.vfs.readText() to answer it, so the page sits on a loading spinner, and a "
     "screenshot of a spinner would have misrepresented the vault."),
    ('v0.2.46', '2026-08-26', 'obj-cas-imm-057b0451154a',
     "A CONFERENCE KEYNOTE AS A VAULT — the twentieth published vault and the first that is a "
     "TALK rather than a document set or an app. AI vs. AI: Building Resilient Enterprises in the "
     "Age of Autonomous Threats, Black Hat Europe 2025, AI Security Summit, ExCeL London, 9 "
     "December 2025. What makes it a good demonstration is that the whole chain travels together "
     "under one credential: the deck as presented (26 slides, ~976 KB self-contained app), six "
     "PDF exports v0.1.1 to v0.2.0, the eight research papers the talk was built from, and the "
     "slide system's own source at ten versions v0.1.0 to v0.1.9. A deck emailed as a PDF is a "
     "snapshot with its working removed; this is the working. The load-bearing design detail is "
     "that SLIDE CONTENT IS DATA: deck/blackhat-eu-2025.json is read through the vault bridge at "
     "load time, so editing a slide is a commit and needs no rebuild — which is also why ten "
     "renderer versions can sit beside one deck without either owning the other. permissions {} "
     "with present:true. INTAKE: the submitted credential carried the sgit_private_vault_ prefix "
     "and was refused as a WRITE credential by the classifier — the prefix family added in the "
     "v0.2.40 batch, working as intended on its first real submission since. Read key derived "
     "one-way, vault key to the gitignored tier. AUDIT clean across all four passes: no sgit "
     "credentials, no third-party API keys (the broadened sweep added after the OpenRouter miss), "
     "no private keys, no emails, no external company or client. AWS, Azure, Cloudflare and "
     "CrowdStrike appear cited for publicly documented outages, which is the subject of the "
     "slide. One judgement recorded rather than buried: the deck uses Black Hat Europe's OFFICIAL "
     "SPEAKER TEMPLATE, logo and trademark included, because it is a talk that was given there — "
     "published as the speaker's own material with the page stating plainly that it is not "
     "endorsed by or affiliated with the conference. Screenshots were captured by serving the "
     "cloned vault locally and driving the deck with its own arrow-key bindings, after keypresses "
     "sent to the hosted surface failed to reach the deck through the shadow DOM; the first three "
     "captures were also named one slide out of step with what they showed and were renamed to "
     "match rather than shipped with captions that did not describe the picture."),
    ('v0.2.45', '2026-08-26', 'obj-cas-imm-598b21e85f91',
     "ARTICLES GET A HOMEPAGE BAND, A NEW ARTICLE ON THE SPLIT, AND A LAYOUT BUG FIXED FROM "
     "YESTERDAY. The network band shipped in v0.2.44 ran the FULL VIEWPORT WIDTH: the homepage "
     "bands each carry their own measure on the component (.eco is max-width:1100px itself, there "
     "is no wrapper convention here) and the new band had none, so it stretched edge to edge on a "
     "wide screen while every other band stayed in the column. Reported from a screenshot rather "
     "than caught by the validator, which has no opinion about layout. Fixed and MEASURED: .eco, "
     ".netpick and the new .artcards all report exactly 1100px at a 1440px viewport with "
     "scrollWidth == innerWidth, and the five area cards now lay out 3+2 instead of 4+1 so the "
     "last card does not sit alone. NEW ARTICLE, 'Twenty sites in fifteen days, and what that did "
     "to the writing': the repositories were created between 11 and 26 August, fifteen of the "
     "twenty in the final five days, and the piece is about what that did to the writing rather "
     "than the count — what forced the split (an argument needs its own version history; nineteen "
     "arguments through one changelog produces a record nobody can read), what it cost (discovery "
     "got worse before it got better; consistency became discipline rather than construction; "
     "cross-site links became claims that can rot, as the sentinel.sgit.ai typo showed), and why "
     "the directory now opens with a question. ARTICLES BAND on the homepage, DERIVED from the "
     "articles list via an <!--ARTICLES--> marker the build fills — a new article appears there "
     "by being written, no list to maintain, the same one-file rule as updates and sites. Also: "
     "influences.sgit.ai went live mid-session and is now a full entry with its hero screenshot, "
     "taking the family to 18 live of 19; skills.sgit.ai still has DNS and a repository with "
     "nothing published and is still listed as such."),
    ('v0.2.44', '2026-08-26', 'obj-cas-imm-d629c8d66421',
     "THE NETWORK BECOMES A DIRECTORY. The sibling-site section was built for four entries "
     "and there are now NINETEEN — 17 live, 2 with repository and DNS in place but GitHub Pages "
     "not yet published (skills, influences), enumerated from the SGit-AI org and probed one by "
     "one for DNS, HTTP status and their own stated thesis. At four, a list of cards was the "
     "right shape; at nineteen it is a directory a reader has to read before it helps them. So "
     "the page now LEADS WITH THE QUESTION: seventeen lines, each one something somebody "
     "actually arrives with ('I need to give an AI agent an identity', 'I have to sign off a risk "
     "and I do not want to rubber-stamp it', 'I want an issue tracker with no database'), mapped "
     "to the site that takes it seriously. Under it, five thematic groups — Agents & AI, Risk & "
     "governance, Graphs & method, Security & infrastructure, Business & publishing — then a full "
     "scannable table of all nineteen. Every thesis is the SITE'S OWN WORDS, quoted from its H1 "
     "or lede rather than paraphrased here, so an entry cannot drift into describing a site that "
     "no longer says that. Engine: the sites content type gained `listing: true` (a directory row "
     "with no page of its own), plus `category`, `stage` and `thesis`; the four sites with a full "
     "write-up keep their pages and the other fifteen are one short markdown file each. Network "
     "promoted from the third child of Updates to a top-level nav group, and the homepage gained "
     "a network band with five doors in by area — a reader who does not know these sites cannot "
     "pick one from a list of domains. Thirteen new hero screenshots captured from the live sites "
     "through the local mirror. The two unpublished sites are listed AS unpublished, linking their "
     "repositories, rather than omitted. One engine bug found and fixed on the way: the first "
     "attempt to add the new fields landed in load_articles instead of load_sites, because the "
     "`'status': ...` + `'body': body` pair appears in both loaders and the articles one matched "
     "first — caught immediately by a KeyError at build, which is the argument for the build "
     "failing loudly rather than defaulting a missing field."),
    ('v0.2.43', '2026-08-25', 'obj-cas-imm-48fd5df1d329',
     "SIX VAULTS PUBLISHED, THREE HELD, and one audit gap found the hard way. Nine credentials "
     "were submitted; intake classified seven as WRITE keys and two as read keys, the seven read "
     "keys were derived one-way, and all nine were cloned and audited with the credential that "
     "would actually appear on the page. New pages: PENETRATION TEST REPORT (a pentest as a vault "
     "not a PDF — eight audience-specific views over one engagement, and a retest script per "
     "finding that exits 0 if fixed and 1 if not; entirely fictional and badged SIMULATED DEMO on "
     "its own front page), STANDARDS ATLAS GDPR ('the standard is the graph' — rulings, guidance "
     "and per-country variation as first-class nodes, corrections scoped to feedback/ so a "
     "reviewer can never alter the graph under review), RISKMANDATE FILE SECURITY (risk "
     "acceptance moved from end-of-flow rubber stamp to the centre, over versioned JSON queried "
     "live by SQLite in the browser), CONTENT-TRANSFORMATION PROXY, SG COMMERCIALISATION (whose "
     "most credible artefact is an engagement register with no rows) and the SG/PAYMENTS BRIEF "
     "PACK (ten documents stamped PROPOSED). HELD: one vault carrying two live vault keys in "
     "plaintext INCLUDING ITS OWN WRITE KEY — publishing its read key would have handed out write "
     "access, defeating the entire read/write split — and one private working log. THE THIRD HOLD "
     "IS THE FINDING: a vault whose app reads an LLM key from a file passed the first credential "
     "pass CLEAN, and was caught only because a screenshot of it showed a chip reading 'key: vault "
     "key.json'. The file held a live OpenRouter API key. The scan had looked for vault-key "
     "shapes, sgit_ prefixes, PRIVATE KEY blocks and the literal string api_key; the field was "
     "named openrouter_key and matched none of them. This is a genuine gap in the tooling, not a "
     "near miss to be reframed — the credential checks were built for sgit credentials and had no "
     "opinion about third-party API keys, which leak just as expensively. A broader sweep "
     "(OpenAI/Anthropic/GitHub/AWS/Google/Slack/JWT shapes, placeholders filtered) now runs over "
     "every candidate; across all nine it found exactly one further hit, a forged alg:none token "
     "in the pentest vault that IS the finding it documents. Content checks answered two specific "
     "questions asked at submission: the commercialisation vault holds no real data (empty "
     "register, no emails, no rates, and its 'team' files are agent role definitions, not people), "
     "and the proxy vault names no external company or project — verified in text and BY EYE "
     "across 120 slide and diagram images a text scan cannot read. The GDPR atlas does name real "
     "companies, and correctly so: they are published CJEU and FTC case records. Article updated: "
     "nineteen vaults, 1,389 files re-cloned and verified, plus the LinkedIn republication link."),
    ('v0.2.42', '2026-08-25', 'obj-cas-imm-75af1686df3e',
     "AN INTRODUCTION ARTICLE, and the first CLI imagery on the site. /articles/what-sgit-is.html "
     "is the piece to hand somebody who has never heard of this: the category of file that has "
     "nowhere good to live, the vault key as address+auth+encryption in one string, the one-way "
     "read key that makes sharing possible, and then the proof rather than the claim. Two new "
     "terminal screenshots carry that proof and are the first of their kind here — every one of "
     "the 73 existing screenshots was of a browser. Both were captured from real runs, not "
     "mocked: a clone of the published EU AI Act vault (273 objects, 207 files) and the same "
     "vault's stored object rendered as a hexdump, 786 bytes of AES-256-GCM ciphertext whose "
     "name is a SHA-256 of those encrypted bytes. Also written up: apps in vaults running under "
     "permissions {} — capability without credential — and the four-site network. VERIFIED "
     "BEFORE PUBLISHING: all eleven published read keys were cloned from scratch, 781 files "
     "total, zero failures. That check first reported the opposite. Every clone failed with 'no "
     "named ref on the server', which looked like every vault page on this site instructing "
     "readers to run a command that could not work — and the real cause was a stale CLI in the "
     "authoring container, v0.15.0, where sgit clone cannot reach these vaults. v0.16.0 clones "
     "all eleven. The finding was retracted rather than shipped, which is the whole reason the "
     "check exists: an intro article is exactly the page that must not repeat an instruction "
     "nobody re-ran. A LinkedIn-newsletter edition of the same piece was produced alongside it "
     "as plain text with image placement markers, since that editor renders no markdown and "
     "asterisks would paste literally."),
    ('v0.2.41', '2026-08-22', 'obj-cas-imm-f401ef7115e0',
     "GRAPHS.SGIT.AI RESOLVES — the CNAME landed hours after v0.2.39 shipped the entry, so the "
     "`url:` override comes back out and the card links the subdomain directly. Deleting one "
     "frontmatter line was the entire change, which was the point of adding the field: a site "
     "finished before its DNS should be linked at the address that answers, and should not need "
     "rewriting when the real one starts working. The DNS-pending chip and the note both "
     "disappear on their own because they were derived from url != domain rather than written "
     "into the page. Verified before and after: graphs.sgit.ai returned nothing from a resolver "
     "on 21 August and answers 200 today. The sentinel.sgit.ai correction on that entry was "
     "re-checked rather than carried forward on trust and still stands — the graphs site links "
     "to a host that does not resolve, and the site is sg-sentinel.sgit.ai. Also settled this "
     "release, for the record: the 34 historical tags CI could never push (v0.1.9-v0.2.16, "
     "blocked because GITHUB_TOKEN cannot push a ref at a commit carrying a different workflow "
     "blob) are now on the remote, pushed from a workflows-scoped credential. The first attempt "
     "was a plain `git push --tags`, which reported 'Everything up-to-date' and did nothing: the "
     "tags only ever existed inside destroyed CI runners, so no clone had them to push. They had "
     "to be recreated locally from the commit subjects first. All 58 release commits are now "
     "tagged, each verified to point at the commit whose subject names it, and the backfill loop "
     "is a no-op from here."),
    ('v0.2.40', '2026-08-22', 'obj-cas-imm-550fd7d8bac2',
     "THE TAG GATE TOOK THE SITE DOWN, and this release fixes the gate and publishes what it "
     "held back. Two good commits landed on dev after v0.2.39 — the VoiceDebrief vault (the ninth "
     "published vault, ten screenshots driven from its published read key) and a check_credential "
     "fix — and sgit.ai served neither for a day. Nothing was wrong with either commit. The CI "
     "tag job read SITE_VERSION, found v0.2.39 already tagged on the EARLIER commit, and failed "
     "with 'SITE_VERSION was not bumped for this release' — when the truth was that this was not "
     "a release at all. Because the deploy job needs tag-release to be success OR skipped, and a "
     "FAILURE is neither, the publish never ran. Re-running could not help: the check is "
     "deterministic, and attempt 2 failed identically. THE FIX: what makes a push a release is "
     "now its commit subject, which is where release.sh already writes the version. A commit "
     "carrying no 'site vR.M.N:' subject is an ordinary push — tagged nothing, published anyway. "
     "A commit that DOES claim a version is held to the full contract, and to a stricter one than "
     "before: the subject and SITE_VERSION must agree (previously only inferred, via whether the "
     "backfill loop had produced the tag), the version must not already have shipped, and it must "
     "be the next minor. The reasoning behind the asymmetry is recorded in the workflow: a "
     "missing tag is a bookkeeping gap, a blocked deploy is an outage. Verified before shipping "
     "by extracting the job's script and running it over five cases in a throwaway clone — the "
     "exact commit that failed today now exits 0; a proper release tags; subject/SITE_VERSION "
     "disagreement, a reused version and a skipped minor all still fail, each with a message that "
     "names what is actually wrong. SECOND CONSEQUENCE, less visible and worth recording: those "
     "commits went to git only, so the vault remote never received them and the two stores had "
     "drifted — sgit status showed all fifteen VoiceDebrief files as uncommitted. That is the "
     "invariant release.sh exists to hold and the reason CI does not author commits itself. This "
     "release carries them across. Also in: the VoiceDebrief vault page goes live, "
     "check_credential now recognises sgit_private_vault_/sgit_private_read_ (the prefixes the "
     "CLI actually prints on init and clone, where the classifier previously called a good read "
     "key 'unrecognised' — fail-closed, but the kind of refusal that tempts an operator to reach "
     "for the vault key instead), and validate.js skips node_modules."),
    ('v0.2.39', '2026-08-21', 'obj-cas-imm-3d8cf0d26b96',
     "Fourth site in the network: GRAPHS.SGIT.AI, a grammar for semantic graphs argued in "
     "increasing depth — five rules you can apply tomorrow, a working edge set with numbered "
     "gaps, then a full positioning against schemas and vector search. Its opening move is to "
     "disown the category a reader arrives expecting: 'this is not a graph database pitch… there "
     "is no graph database anywhere in the work behind this site'. The thesis is that two nodes "
     "both holding 8080 differ not in the value but in the connectivity, and the strongest "
     "argument on the site needs no technical background at all: 10,000 hours was an AVERAGE in "
     "a 1993 violinist study, not a threshold, half the top group had not reached it, and the "
     "author spent his career correcting the popularisation — but the correction never attached, "
     "because by then the claim had been carried through 242 papers and 200,000+ citation paths. "
     "A document cannot fix that; a graph can mark a claim superseded and turn 'what did we build "
     "on this?' into a query. Grammar highlights: every edge is a verb with a distinct inverse, "
     "the test being 'would a person in this business say this sentence?', and relates-to is "
     "BANNED for a mechanical reason — an edge with no verb carries no constraint, so it cannot "
     "narrow a traversal; it costs fan-out and buys nothing. Relevant here because the one "
     "indisputably shipped item on that site is sgit's own object model: a content-addressed "
     "commit DAG (SHA-256 over CIPHERTEXT, multi-parent, wave-BFS merge-base) plus *.link.json "
     "commit-pinned cross-vault edges and the sg.history read-only query API exposed to untrusted "
     "sandboxed apps. The grammar argument and the vault are not neighbours by theme; they share "
     "a data structure. It is also the FIRST SIBLING WITH A RECIPROCAL LINK — an '↗ part of "
     "sgit.ai' chip in its nav and a footer pointing back at /network/ — so the index stops being "
     "one-way. Engine change: a site entry may now carry a `url:` that differs from its `domain:`. "
     "graphs.sgit.ai does not resolve yet (verified: no DNS), and a finished site should be linked "
     "at the address that answers rather than held back for a CNAME, so the page states which one "
     "it is instead of shipping a dead link and needing a rewrite later. The network audit also "
     "found a broken link on the new site itself: it points at sentinel.sgit.ai, which does not "
     "resolve — the site is sg-sentinel.sgit.ai. Recorded on the entry for upstream."),
    ('v0.2.38', '2026-08-20', 'obj-cas-imm-b270f3424691',
     "Third site in the network: SG-SENTINEL.SGIT.AI, a design for an app-coupled edge guard "
     "replacing rented AWS WAF + CloudWatch/Firehose with a layer you own. Its central inversion "
     "is that a generic WAF is blind to the app it protects and must denylist, whereas an edge "
     "that knows the valid request space can ALLOWLIST — no invalid request reaches the origin. "
     "Two things make it worth a page rather than a link. First, a governing correction stated as "
     "a constraint: 'Layer 1 never acts and never writes — it only decides and signals; Layer 2 is "
     "the sole actor and the sole I/O owner', because a CloudFront Function physically has no "
     "network and no filesystem — and the site names its own earlier design, where L1 blocked "
     "inline, as a category error. Second, rules are the engine rather than configuration on it: "
     "six deterministic rules, each a pure function mapped to an ATT&CK technique, run "
     "first-block-wins, with a prototype exercise running the same engine across three targets "
     "under a parity matrix asserting identical decisions. It also carries the most honest status "
     "language on the network — the pill reads NOT BUILT, and where the prototype's 149 passing "
     "tests are cited the site immediately bounds them as 'not deployed anywhere, not in "
     "production use, not maintained, not packaged for you to install'. Adding it cost one "
     "markdown file and three screenshots, which is what the content type was built for. One "
     "engine gap surfaced doing it: the markdown renderer had no TABLE support, so the six-rule "
     "core rendered as a paragraph of vertical bars. Pipe tables now parse — header, separator, "
     "body — and emit into the site's own .tablewrap, so they scroll on a phone and survive print "
     "like every other table here. Caught by looking at the output rather than trusting the "
     "validator, which had nothing to object to: badly rendered markdown is still valid HTML."),
    ('v0.2.37', '2026-08-20', 'obj-cas-imm-1b229ee71709',
     "REGULATION GRAPH — the EU AI Act as a citable graph, and the first vault here whose "
     "publication the audit STOPPED rather than cleared. Regulation (EU) 2024/1689 parsed from "
     "official Formex XML retrieved from CELLAR, hash-verified to the source bytes: 113 articles, "
     "500 paragraphs, 180 recitals, 68 definitions, resolving to 1,523 nodes and 1,944 edges "
     "across eleven views — browse, Cytoscape citation graph, in-browser SQLite over sql.js, RDF "
     "via rdflib, concepts, external instruments, and an experimental Art 9 lab as the declared "
     "entry point. WHAT HAPPENED: the submitted credential was a VAULT KEY, not a read key — the "
     "fourth time, caught by the intake check. The read key was derived and the audit run with "
     "it across 204 text files, which is when it found a LIVE VAULT KEY IN PLAINTEXT inside a "
     "handoff document, granting write access to a DIFFERENT vault. Publishing our read key would "
     "have handed that away. No page was written; the finding was reported first. Deleting the "
     "file would not have been enough, because vault objects are content-addressed and immutable, "
     "so a credential committed once may stay reachable from history — the only clean remedy is "
     "history that never held it. So this is a REDACTED REPUBLICATION into a new vault: same 206 "
     "files, two credentials replaced in place with visible <VAULT-KEY-REMOVED> and "
     "<READ-KEY-REMOVED> markers rather than silent deletions, a PUBLIC.md stating the rules and "
     "the removals, and a re-audit from a fresh read-key clone: 205 files, zero findings. The "
     "second removal was a judgement call — a read key is publishable by its OWNER, and that one "
     "belonged to a third vault, so it goes and the decision stays with a human. RULE 3 VERIFIED "
     "RATHER THAN ASSUMED: the Graph REPL is an LLM chat, and repl.js looks for an OpenRouter key "
     "at /key.json INSIDE THE VAULT before falling back to device storage, so a shipped key would "
     "be an open tab on somebody else's budget. No key.json exists, confirmed in the read-key "
     "clone rather than in our working copy. The 370-plus bare 64-hex strings the scan flagged "
     "were all sha256 provenance hashes, checked individually — a scan that never produces a "
     "false positive is not scanning hard enough. The rule that caught all of this came from Risk "
     "Graph Explorer's own PUBLIC.md, not from us; it has now paid for itself."),
    ('v0.2.36', '2026-08-19', 'obj-cas-imm-18bcdab6db5d',
     "A NETWORK section for the sibling *.sgit.ai sites, built as a content type rather than as "
     "two pages, because many more are coming. nhi.sgit.ai argues that 'how do I give my agents "
     "an identity' splits into agents you RUN and agents you RENT, and that the industry answers "
     "only the first — SPIFFE for workloads you can attest, an open feature request for the "
     "agents anyone actually names. pki.sgit.ai designs a key registry from the 2019 keyserver "
     "failure and publishes four rules BEFORE the registry exists, reaching a resolution worth "
     "borrowing: append-only is safe when a writer appends only to objects it owns and fatal "
     "when anyone may append to somebody else's, so the rule to carry is not 'append-only' but "
     "'the writer owns what it writes' — which is append lanes, already shipped. Six screenshots "
     "captured from the live sites through the curl mirror the sandbox needs, since Chromium "
     "cannot egress here. Adding the next site is ONE markdown file plus its screenshots: the "
     "index, the cards and the per-site page are derived, same contract as updates and articles. "
     "Two engine fixes fell out of building it. The generator now WIRES THE SCREENSHOT COMPONENT "
     "AUTOMATICALLY for any page containing figures — a markdown author has no place to put a "
     "script tag, and the views page had already shipped once with figures and no loader, which "
     "errors nowhere and simply shows nothing. The first version of that check matched on "
     "'figure class=\"shot\"' and missed 'class=\"shot net-shot\"', leaving the new index in "
     "exactly the state the check existed to prevent; it now matches on data-shot=, the attribute "
     "the component actually selects on. Detect on what the consumer looks for, not on how it "
     "happened to be written."),
    ('v0.2.35', '2026-08-19', 'obj-cas-imm-1f3ce8d32a28',
     "Two new sections and the navigation restructure they forced. UPDATES and ARTICLES, both "
     "built on the VoiceDebrief journalist pipeline's central rule, which was worth adopting "
     "verbatim: PUBLISHING IS ADDING ONE FILE. No index to update, no manifest to hand-edit, no "
     "decision about where a post goes — ordering, permalinks, updates.json and feed.xml are all "
     "derived. That is not tidiness, it is the property that makes an unattended journalist agent "
     "safe: two agents publishing on the same day touch two different files and cannot conflict. "
     "Frontmatter is flat key: value with no YAML parser, the folder path must agree with the "
     "date, and slugs must be unique or the build fails. ONE DELIBERATE DIVERGENCE from their "
     "contract: they author root-relative links because their site sits at a domain root; ours "
     "must also render INSIDE A VAULT at an arbitrary mount path, where a leading slash escapes "
     "the app — so posts are still authored root-relative and the build rewrites each to a "
     "depth-relative path. Authors keep the simple rule; the vault still works. Updates are one "
     "entry per STORY rather than per release, which is the whole reason this is not the version "
     "log with a nicer stylesheet — v0.2.31 alone carried three separate stories. Five seeded "
     "from recent releases; the version log stays the complete technical record behind them. "
     "Articles carry two anti-rot rules stated on the page: never restate a fact you do not own "
     "(link to the page that does, so it cannot start lying when the fact changes), and link the "
     "test behind any testable claim. Two to open: GREEN DOES NOT MEAN LIVE on the deploy that "
     "reported success twice while serving a two-release-old page, and SEVEN VAULTS, ONE METHOD "
     "on what publishing seven vaults taught — including the three vault keys submitted as read "
     "keys. NAVIGATION: 14 flat items became 7 groups with a second level. The old bar wrapped to "
     "THREE ROWS on an iPhone before the page began — measured on a real screenshot, not guessed. "
     "Every group label is itself a link to that section's index, so nothing is reachable only by "
     "opening a menu. Desktop opens on hover and :focus-within in CSS alone; the phone collapses "
     "behind one button. The first mobile attempt made every submenu inline and measured 498px of "
     "navigation before the content — worse than what it replaced — so it was rebuilt as a "
     "collapsed menu: 91px, against 54px on desktop. Also adds an RSS feed and a JSON manifest, "
     "the first machine surfaces here aimed at a human follower rather than an agent."),
    ('v0.2.34', '2026-08-18', 'obj-cas-imm-97c957112852',
     "Acts on an inbound fix pack from the SG/API team, who audited this site against their route "
     "tables at v0.33.54 after an agent asked how to send a message between vaults and could not "
     "find the answer here. Their central finding was right: the site documented the TRANSPORT "
     "(sg.append) and the CRYPTO (sgit pki) on pages that never referenced each other, and never "
     "wrote the sentence saying they compose into vault-to-vault messaging. There was also no HTTP "
     "API reference anywhere, which is awkward for a project whose argument is that the API is the "
     "whole surface. SEVEN NEW PAGES: /docs/vault-messaging (the keystone — append lanes composed "
     "with PKI, worked end to end in CLI, curl and sg.append), /docs/pki (keypair lifecycle), and a "
     "/api/ section: index, authentication, vault-objects, append-lanes, errors. The security page "
     "gains the asymmetric layer it never had; sg.append is retitled as the message transport and "
     "cross-linked; limitations gains what PKI does NOT do; the skills page flags that the shipped "
     "agent skill still has both halves and no join. THREE OF THE PACK'S FINDINGS DID NOT SURVIVE "
     "CHECKING, which is the part worth recording. (1) It reported that the security page 'actively "
     "denies PKI'. It did not — a sweep for symmetric, asymmetric, public key, PKI and keypair "
     "returned zero occurrences. The page was SILENT, not wrong; publishing a correction for a claim "
     "we never made would have put a false statement in this log. (2) It asked us to hunt stale "
     "'inbox' naming; there is none — two hits, both ordinary English, and no /api/vault/inbox/* "
     "path anywhere. (3) It described X25519 sealing throughout. Running sgit pki keygen on v0.15.0 "
     "prints RSA-OAEP 4096 and ECDSA P-256. Publishing the draft as written would have told "
     "integrators to build against the wrong primitive. Two further corrections came from running "
     "the CLI rather than reading about it: export emits a JSON BUNDLE of two PEM blocks, not a .pem "
     "file, so the draft's sha256sum-the-pem derivation of the lane address is not well defined; and "
     "keygen requires a passphrase, which no draft step mentioned. The one genuinely unshipped step "
     "— append_token = H(public key) — is labelled PROPOSED with an interim recipe rather than "
     "quietly documented as working, and the two endpoints their audit could not resolve "
     "(/api/vault/zip, /join/*) are listed as unresolved rather than described. The pack's own "
     "acceptance test — give a fresh agent only llms.txt and ask how to send an encrypted message "
     "from vault A to vault B — now passes, including the lane-address fact and its PROPOSED "
     "caveat, answered in the preamble so it survives an agent that cannot follow a link."),
    ('v0.2.33', '2026-08-17', 'obj-cas-imm-ab458fd8611d',
     "A release now ends by asking the live site what version it is serving, because "
     "'both remotes in sync' turned out not to mean 'published'. v0.2.31 and v0.2.32 both "
     "pushed cleanly, both reported success, and NEITHER reached sgit.ai: GitHub Pages "
     "failed to deploy them because codeload returned 429 (Too Many Requests) for "
     "actions/configure-pages@v5, and the deploy job died in 'Set up job' before running a "
     "single step. Validation passed, tagging passed, the push was verified against both "
     "remotes — and the site served a two-release-old page for forty minutes, which is how "
     "long it took a human on a phone to notice the version pill still said v0.2.30. The "
     "failure was invisible to every check the release ran, because it happened in a job "
     "neither remote knows about. So release.sh gained a sixth step: poll the live URL with "
     "a cache-buster until the version pill matches this release, up to eight minutes, and "
     "ABORT LOUDLY if it does not — naming the Actions page and the fact that a 429 on the "
     "action download is transient and just needs a re-run. The cost is up to eight minutes "
     "of waiting per release. The alternative, demonstrated twice in one afternoon, is "
     "telling somebody a fix is live when it is not. Same principle as the orphan-page rule "
     "and the llms.txt guard: a page nothing links to, a page the index omits, and a page "
     "the deploy never published are all equally unpublished, so the build refuses all "
     "three. Ships the content of v0.2.31 and v0.2.32, which had been written but never "
     "served."),
    ('v0.2.32', '2026-08-17', 'obj-cas-imm-7f84b9ee6727',
     "The walkthroughs page becomes a document rather than a list of links. Each of the three "
     "videos now carries the recording at the top and THE SAME SESSION READ BACK underneath it: "
     "fifteen moments, each one a timestamp that deep-links into the video, the frame the screen "
     "was showing at that moment, and an explanation of what is happening in it. The transcripts "
     "are still there, folded away at the foot of each. The reason for the format is the one "
     "thing a transcript structurally cannot do: these recordings are full of 'this guy here' and "
     "'look at this', and the words alone name neither end of what is being pointed at. Pairing "
     "each phrase with its frame is what makes the argument survive being read instead of "
     "watched. TWO SOURCES OF FRAMES, and the page says which is which. The Graph Browser "
     "moments are frames of the recording, from a narrated-review export the author produced "
     "with tools.sgraph.ai — nine timestamped stills paired with the narration spoken over each. "
     "Risk Chains and Role risk map have no such export, so their six frames were captured from "
     "the LIVE VAULT with the published read key, driven to the exact state being described — "
     "including the entry he names out loud ('you have risk 6'). What the frames turned up is "
     "most of the value, because none of it is audible: negative answers produce NAMED EDGES "
     "(never-exercised-on, never-timed-for, absent-for) rather than silence; 'no egress' draws "
     "a single assurance-coloured edge in a field of amber, so a good answer is a finding rather "
     "than the absence of one; one selection can carry two fact ids; and every risk ships with a "
     "CEASES WHEN ANY OF THESE HOLD list — its own falsification condition, cited to facts. The "
     "role dashboard also separates three arrival routes where the video describes two: held, "
     "arrives by the risk chain, and arrives by the org chart. TOOLING: the capture rig gained "
     "appProbe (ask the running app what its elements are called instead of guessing and burning "
     "a capture run per guess — it found g.cnode for chain entries and g.role for roles) and "
     "appClickMatch (substring match plus a real MouseEvent, because the graph nodes are SVG). "
     "Videos print with the player hidden and the moments intact."),
    ('v0.2.31', '2026-08-17', 'obj-cas-imm-17f0b2693daf',
     "Corrects v0.2.30 on three counts, two of them reported and one of them the reason the "
     "report was possible at all. (1) THE LAZY-LOAD BYPASS IS NOW ONLY ON PRINT. v0.2.30 "
     "prefetched every screenshot once the page went idle, which fixed printing by making "
     "every reader pay for images they never scrolled to — the wrong trade, and correctly "
     "rejected. It is now driven entirely by the print itself, and it works because of a "
     "change one layer down: on the ordinary web the loader no longer fetches bytes and "
     "builds a blob: URL, it just sets img.src. That makes each screenshot an ordinary "
     "pending document resource, which the print pipeline knows to wait for, where a "
     "fetch-and-blob is invisible to it. Cmd/Ctrl-P is caught on keydown as well as "
     "beforeprint, because the keystroke lands a few hundred milliseconds before the "
     "dialog does and that head start is what removes the race. Measured on a page that "
     "was never scrolled: 1 image loaded while reading, 9 of 9 in the PDF. The blob path "
     "remains for pages served from inside a vault, where it is the only option. "
     "(2) THE PRINT-ONLY SOURCE LINE AND LANDSCAPE HINT ARE GONE — printing these pages is "
     "an uncommon case and did not warrant instructions on the page. (3) ASSETS ARE NOW "
     "CACHE-BUSTED PER RELEASE. GitHub Pages serves them with max-age=600, and the "
     "bootstrap fetched them by bare path, so for ten minutes after every release a "
     "returning reader ran the NEW html against the OLD css and js. That is not a "
     "hypothetical: it is exactly what produced the v0.2.30 bug report — new markup whose "
     "print-only elements the cached stylesheet did not know to hide, and a cached loader "
     "without the print handler. Every fetched asset now carries ?v=<site version>; the "
     "in-vault sg.vfs path stays unversioned, since a vault lookup is by path, not URL."),
    ('v0.2.30', '2026-08-17', 'obj-cas-imm-81dc22613ddf',
     "Print and save-as-PDF, prompted by an export of the seven views page that came out wrong. "
     "TWO DEFECTS, one reported and one found while looking at it. (1) The top nav is position:sticky; "
     "Chrome paints a sticky box ONCE, wherever it happens to fall in the paginated flow, so the whole "
     "nav landed across the middle of page 2 — translucent, with the prose showing through it. It is "
     "static in print now and flows once, at the top of page 1, as a masthead with the link list dropped. "
     "(2) WORSE, AND NOT REPORTED: screenshots are lazy — a figure starts at opacity:0 and its img is "
     "only created when an IntersectionObserver fires — so printing a page without first scrolling to "
     "the foot of it exported blank gaps where the pictures should be. Nothing errored; the img simply "
     "never existed. beforeprint cannot fix that alone (it is synchronous and will not wait for a fetch "
     "and decode), so the figures are now prefetched once the page goes idle, with beforeprint kept as "
     "the backstop. The export that prompted this was only correct by luck: it was taken after reading "
     "the whole page. Beyond the fixes: @page margins so Chrome's Default is ours rather than its own; "
     "print-color-adjust:exact, because on this site the tints carry meaning (amber exposure, green "
     "assurance) and Chrome drops backgrounds unless asked; break-inside:avoid on walkthrough rows, "
     "figures, notes, tables and transcripts, which fixes captions stranded on the page after their "
     "picture; orphan/widow control; live vault embeds hidden and labelled rather than exported as "
     "empty boxes; and a print-only source line carrying the canonical URL, since Chrome's own "
     "header and footer are frequently switched off. Finally, any page containing walkthrough rows "
     "now asks for LANDSCAPE — in portrait the two-column grid falls below the 820px breakpoint and "
     "collapses, which loses the alternating left-right rhythm that is the entire design of those "
     "pages. The reader can still override it. None of this was tested before; all of it is now."),
    ('v0.2.29', '2026-08-17', 'obj-cas-imm-8a68f249bd9f',
     "The first vault to get depth rather than a page. Risk Graph Explorer now has three: the overview, THE SEVEN VIEWS EXPLAINED, and THE AUTHOR'S WALKTHROUGHS. The views page captures each of the seven tabs from the live vault under the Exposed preset — the estate, context, role risk map, risk chains, the register, acceptance, what happens next — and explains the mechanism behind each, matched to how the author describes it in his own recorded demos. Highlights the screenshots alone would not carry: 'assigned' versus 'through' on the role map (what you personally hold, versus what arrives because the graph says it must), so that no risk is orphaned and every path terminates at the board; risk chains running inherent-to-corporate left to right, clickable in both directions ('leads to' navigates up, 'led by' walks back to the answers that caused it), with cycles drawn as dashed edges because the cycles are real; and acceptance as the place where the register stops being a document — with the author on camera disagreeing with his own tool, which resolves into WHICH FACT IS WRONG rather than whose judgement wins. Also captures the same organisation under the Typical and Governed presets, because that comparison is the whole argument: the org chart does not change, only what is true about the agent. The walkthroughs page carries all three videos with FULL TRANSCRIPTS — a video is invisible to a search engine, to llms-full.txt and to any agent reading this site as documentation, so the transcript is the content and the video is one rendering of it. Tooling: the shots component gained a data-dir override so deeper pages under a vault share ONE image folder; the site now runs to 53 pages. Three bugs caught by testing rather than assumption — a malformed selector expression that silently created no images at all, escape sequences leaking as literal text, and a page that never loaded the component it depended on."),
    ('v0.2.28', '2026-08-17', 'obj-cas-imm-6008b0bdfe27',
     "Seventh vault, and the method written down. RISK GRAPH EXPLORER (3simlnqe) is the fact-to-risk explorer extracted out of the risk-mandate work into a vault of its own — answer questions on the left, seven views recompute on the right, nothing leaves the page. Its argument is visible in two screenshots: empty at 0 facts / 0 risks, then 18 / 37 / 14 under the Exposed preset, because a register that produces the same output for a scratch service and a payments platform is a checklist, not a register. Unanswered relationships are drawn as ghosts — recording absence as information rather than as an implicit pass. It is the first vault here PUBLIC BY DESIGN: it carries its own PUBLIC.md whose three rules its build enforces — nothing private committed (the gate scans every file, not just the artefact), no write token, and NO METERED CAPABILITY, because a published read key in front of an LLM config is an open tab on somebody else's budget. That third rule is not in our guidance and is the one to adopt. It also sent us back to re-audit ourselves: risk-mandate does carry an LLM config, so we took its sealed credential and attempted to open it with the read key we had published — AES-GCM refused (InvalidTag), so no budget was exposed; the rule is satisfied there by sealing and here, more conservatively, by absence. Checked rather than assumed, and recorded either way. Its app.json is `permissions: {}` — the floor of a scale the catalogue now spans end to end. Zero audit findings, the cleanest yet. NEW PAGE: /demos/vaults/publishing.html — the seven steps behind every vault published here, written to be followed by another site's agent: classify the credential before it touches anything, derive rather than refuse, audit with the read key across every file, derive the facts, capture evidence by driving the real product, write the page (describe, show, then admit), and record what outlives it. It names the five tools and, more usefully, the five mistakes that produced each rule."),
    ('v0.2.27', '2026-08-17', 'obj-cas-imm-6f1decd85ad3',
     "Sixth vault: AGENTIC BROWSER ISOLATION (0610gsp9) — a living risk graph for one decision, does an AI agent browse inside the user's browser with their logged-in sessions, or inside an isolated browser with a scoped identity of its own. It is this site's own ambient-authority argument made by somebody else and in much more detail, so it is linked from the AI-agents use case. Seventeen app entry points, the most in the catalogue: a numbered narrative spine, one page per stakeholder altitude (IT · CISO · DPO · CFO · COO · CEO · Board), an explorer, two graph views and the raw data, over ~70 JSON files with RDF tooling vendored in so graph exploration works offline. The mechanism is the part worth copying: every altitude has one named owner, a risk stays PENDING until that owner accepts it personally, only an accepted risk escalates, and there is no deny button — the screenshots show IT holding five pending while every altitude above reads 'waiting', because nothing has been passed up. Its app.json declares fs.write: [] — an app that requests no write capability at all, which with supplement-stack (one folder) and risk-mandate (LLM use without the key) gives the catalogue three distinct points on the permissions scale, each declared in the vault rather than configured on a server. The intake check earned its keep on arrival: the submitted credential was again a vault key, refused for publication by shape, and only the one-way derivation published. Audit clean across 104 files — the six scanner hits were all digit runs inside a minified RDF library matching a phone-number pattern, recorded because ruling hits out by reading them is what an audit actually is. Also: upgraded the CLI to v0.15.0 (latest) specifically to re-test the prefix gap; it still derives the wrong ref from the canonical read-key prefix while the bare form clones correctly on the same binary, so the brief now says 'confirmed on latest' rather than 'may be a stale install' — and the machine-verified check updated its own evidence from v0.14.27 to v0.15.0 with nobody editing the claim."),
    ('v0.2.26', '2026-08-17', 'obj-cas-imm-6958c20644d8',
     "Credential intake becomes a check rather than a habit, prompted by yesterday's near-miss: a vault key was submitted for publication described as a read key, caught by shape, and only its derived read key published. The catch depended on somebody looking. New admin/build/check_credential.py classifies a credential BEFORE it touches a page, a catalogue entry or a commit — exit 0 means read-only and publishable, exit 1 means a write credential and stop. It works two ways because the problem has two eras: by PREFIX for vaults new enough to emit one (the canonical write prefix, which is exactly the change being rolled out, and the reason it is worth rolling out), and by SHAPE for everything older, where a read key is 64 hex characters and anything else before the colon is a passphrase. Verified against all eight real forms we have handled, including the actual key from yesterday, which it refuses with no prefix to help it. If a submission IS a vault key the entry is not blocked — the documented one-way derivation is printed instead. The rule is now in the catalogue vault's SCHEMA, so it renders on /catalogue/ with no site deploy, and summarised on the vaults index. Also: the release tripwire got more precise rather than more strict. Banning the bare write prefix outright had caught its own author three times, each time writing it in prose — and guidance that cannot show a reader what a write credential looks like cannot teach them to spot one. It now fires on the prefix followed by a CREDENTIAL character, so documentation may name it while every real key still fails the build; the bare passphrase:vault_id shape catches the body independently. Both directions proven before shipping (\\S was tried first and failed, because in documentation the prefix is followed by markup)."),
    ('v0.2.25', '2026-08-17', 'obj-cas-imm-8b39926aadb1',
     "Risk Mandate joins the catalogue — the most complete project ever published here, and the first to demonstrate CAPABILITY WITHOUT CREDENTIAL. It is a Black Hat field demo (hand someone an iPad, answer eight questions, a risk register assembles) built AS a vault app: 124 files, 98 commits, eight entry points, a test suite, build tooling, releases pinned to commit ids and offered as a live selector in the app chrome, and offline operation after one cached load. Its app.json grants llm:chat/models/usage/listen and fs.write over field/workspace/ and nothing else — while the OpenRouter credential itself is SEALED under the vault key in .vault/llm/config.json, so the host decrypts and calls and the app frame is handed results, never a secret. Auditing with the published read key, that field is ciphertext we cannot open, which is the claim demonstrating itself. The /compare/ privilege vocabulary gains the shape this revealed: ops and bearer come apart, so ops:llm-chat can be granted while bearer of the key is withheld — something most sharing models cannot express, because handing over the capability and handing over the credential are the same act. IMPORTANT PROCESS NOTE: the credential submitted for this vault was a VAULT KEY (format 3, passphrase:vault_id), not a read key — it matched this site's own banned-shape tripwire exactly. It was not published. It was stored in the gitignored local tier and the read key was derived from it one-way via the library's own Vault__Crypto.derive_read_key; only that derivation appears on the site, in the catalogue, and in the capture rig. The independent audit across all 124 files was clean, with two findings of the good kind recorded publicly: the sealed LLM key, and a single secret-scanner hit that turned out to be a deliberately fake sk-test- key inside a test asserting that a reachable API key IS caught."),
    ('v0.2.24', '2026-08-17', 'obj-cas-imm-244c5ecdeecf',
     "Comparisons, built as reproducible tests rather than as claims — the concrete proposal answering the 16 Aug comparison brief. New /compare/ section carrying (1) the entry format: task, steps, prerequisites, privileges granted, where it runs, survives-the-vendor, verified date, and how to re-run; (2) a PRIVILEGE VOCABULARY, which is the part most likely to be argued with and the reason it is published first — seven properties that make two grants comparable (scope, operations, bearer, mediation, duration, withdrawal, observability), under which a published read key reads scope:vault · ops:read · bearer:any-holder · mediation:key · duration:forever · withdrawal:future-only · observability:none, three of them WORSE than a mainstream sharing link; (3) three worked entries — printing a markdown file (small, checkable in a minute, we win), taking access back after sharing (WE LOSE, plainly: rotation protects future commits and reaches nothing already fetched, while a server-mediated platform simply refuses the next request), and letting a program record data without letting it alter records (the differentiator, where step counts tie and privileges separate). Behind it: admin/build/compare_tests.py executes the our-side claims against the live service with published read keys only, and writes compare/results.json — six checks, each stating what would make it FAIL. Five hold; one records an ABSENT capability and is kept until it stops reproducing: the installed CLI v0.14.27 does not strip the canonical sgit_rk1_ prefix the web loader now accepts, deriving the wrong ref id, while the bare form works on the same version — now also filed as a brief to the CLI team. The freshness mechanism is real rather than a date in small print: results carry an expiry threshold and a past-threshold result renders as UNVERIFIED instead of as fact, proven by forcing the dates old and watching all six rows flip. The page states its own asymmetry up front — our rows are machine-verified, rows about anyone else's product are hand-checked on a date — and lists what is deliberately absent, including the deployment comparison, which waits until our own portable-artefact/hosted-viewer caveat is resolved."),
    ('v0.2.23', '2026-08-16', 'obj-cas-imm-8af209891454',
     "Structure for scale, and the most interesting vault yet. (1) Every published vault is now a self-contained folder — demos/vaults/<slug>/index.html with its screenshots in demos/vaults/<slug>/images/ — so adding the hundredth vault is adding a folder, and a vault's page and pictures move together. The old flat /vaults/ section is gone (URLs lived one day). Two engine changes made it possible: the root-prefix was computed as 'one ../ if nested at all', which silently pointed the nav, stylesheet and every asset at the wrong level once pages nested three deep — now it is ../ times the depth, the same formula the markdown twins already used; and the screenshot rig writes per-vault, with a --vault filter. Image paths in the walkthrough are page-relative for the same reason. (2) New vault: SUPPLEMENT STACK (r7zes477), and it is the strongest healthcare demonstration on the site. Its idea: every label describes one product, nothing describes the sum, so the model extracts (fuzzy, with every amount traceable to the label photograph it was read from) and the code adds up (deterministic, rules stated in the open, a missing value flagged and never guessed), producing a briefing for somebody qualified and never a verdict. It is also the first vault here to use SCOPED WRITE PERMISSIONS: app.json grants write over adherence/ only, so the app that logs what was taken cannot alter the regimen, the labels or the references — least authority as a property of the vault rather than a server setting. Five walkthrough rows captured from the live vault, including its app.json permission block. The healthcare use case now opens with this as a worked example: who holds the data, how it reaches a clinician (a read key, not an account or a PDF), where AI fits safely, and why the reference set is UK RNI/EFSA rather than US Daily Values. The published audit: clean on credentials, no personal identifiers found — but it publishes a real regimen and the health context inferable from it, deliberately, and revocation is not retroactive."),
    ('v0.2.22', '2026-08-16', 'obj-cas-imm-b1d27e3295cf',
     "The walkthrough: six alternating rows at the foot of the Algarve page that explain what a live embed cannot say for itself — the app is real HTML (not a viewer template); clicking a photo opens the vault's own lightbox with captions from gallery.json; the debug pane's Vault tab times the decryption step by step; its REPL tab is a console over the sg.* bridge where vfs.write is refused because no write capability exists in a read key; the vault browser shows photos/originals and the app's own SOURCE; and the SGit tab carries 36 commits, because the history IS the storage. New tool behind it: admin/build/capture_shots.mjs drives the real product with only a published read key, performs each row's navigation (scroll to a chapter, click a photograph, open the debug pane through the HUD's shadow root, type vfs.list into the REPL, expand a folder, switch to the SGit view), crops the result and writes WebP — so the pictures are of the actual vault and regenerate when it changes. Getting there needed four fixes worth recording: the app frame must be identified by a selector it contains (the shell frame also has text and was winning the race), the REPL input sits two shadow roots deep and is reached with a shadow-piercing locator typed into for real, the file tree rows are .sb-tree__folder-name, and the slow test mirror needs navigation timeouts well past the 30s default. Images load through assets/shots.js — lazily, and via fetch-or-sg.vfs rather than <img src>, because the authoring contract forbids declarative refs so every page survives being served from inside a vault. Also adds a direct 'open the gallery app in its own window' link using the read-key fragment the UI now accepts."),
    ('v0.2.21', '2026-08-16', 'obj-cas-imm-10164a7a31ab',
     "Two reader reports from an iPhone, both fixed with the cause named. (1) The vault pages now open both surfaces ON LOAD — the reader lands on the vault, not on a row of buttons. The opens are sequential by design: the browser surface starts once App Mode reports vault-ready (grace-capped), so its objects come out of the client's encrypted-object cache and the second open mostly decrypts rather than fetches — the caching architecture demonstrating itself on every page view. Buttons are gone; each frame carries a label and its own status line, and a failed handshake leaves a retry control instead of a dead page. (2) The landscape-iPhone report — site and iframe not using the full width after a pinch-zoom — was hunted down empirically rather than guessed at: one unbreakable 702px token (the sgit clone command with its 90-character credential) on a 393px viewport made the page 743px wide, which drops Safari's fit-to-width scale below 1; pinch out and the entire site sits narrow with a white gutter. Fixed with overflow-wrap:anywhere on inline code (breaks only when a token would overflow) plus the html canvas painted the site colour so any zoomed-out or overscrolled area reads as the site rather than as white margin. Verified at iPhone viewports: every checked page now measures exactly the viewport width, and the auto-open completes with zero clicks."),
    ('v0.2.20', '2026-08-16', 'obj-cas-imm-23e6ea08a77d',
     "Both surfaces at once, reader-requested: on the vault pages, App Mode and the vault browser now each open in their OWN frame, stacked — the app first, the FILES/SGIT/SETTINGS browser under it — instead of one frame the buttons fought over. The second open is fast by design and the component says so: the encrypted objects are already in the client's cache from the first surface, so the second mostly decrypts rather than fetches — the caching story demonstrating itself. Each frame carries its own status line from its own handshake (one listener, replies routed by which frame sent them). The Full screen button is gone from these pages — with each surface getting a full-width, viewport-height frame of its own, it earned nothing. Verified headless: both surfaces open (5.0s through the slow test mirror, faster live), app above browser, two independent vault-ready events."),
    ('v0.2.19', '2026-08-16', 'obj-cas-imm-2773e0dfba35',
     "The site starts doing the thing it was building toward: publishing vaults. New /vaults/ section — an index of every read key this site has deliberately published, and one page per vault (five at launch: Field Notes, Strategy Maps, Deploy Docs, the Catalogue itself, and — new — Algarve · May 2026) with a real description, the features that vault exercises, what the shape is good for, the derived facts, the key as a copyable sgit_rk1_ credential with a CLI command and an open-in-the-official-UI link, and the vault RUNNING LIVE in the page via the reusable embed component (assets/vault-ui-embed.js — the two-surface embed-protocol host from the demo page, now attribute-driven; App Mode hidden for vaults without an app). Pages load the component contract-compliantly (fetch+eval, no script src — every page must survive being served from inside a vault). The Algarve vault is the first entry processed through the catalogue's submission queue as designed: read key supplied in chat, everything else derived — 71 files, 29 MB (60 WebP photos in originals/web/thumbs), 36 commits, auto-opening gallery app with a chaptered narrative. Its pre-publication audit is published on the page per the rules: one finding (a live delete_auth token in public-preview bookkeeping — narrow scope, the owner advised to rotate) and one counterpoint worth showcasing (the same vault's readonly-tokens bookkeeping decrypts to further ciphertext: owner secrets double-encrypted, the pattern that fixes the finding class). Catalogue vault updated in the same breath — new entry, trip-gallery-1 ticked off the awaiting list (7 remain) — and /catalogue/ picked it up with no site deploy, which is that design working."),
    ('v0.2.18', '2026-08-16', 'obj-cas-imm-68578f7b1bf4',
     "The tag pipeline's first contact with a real GitHub rule, fixed within the hour. v0.2.17's run DID tag itself — the first CI-authored tag — but the historical backfill push was rejected wholesale: a workflow's GITHUB_TOKEN cannot push any ref pointing at a commit whose tree carries a different version of a workflow file, and the `workflows` permission that would allow it is not grantable to that token. Every pre-v0.2.17 release predates the current deploy-pages.yml, so all 33 backfill tags bounced — and because the tag job failed, the deploy was skipped and v0.2.17 never reached the live site (this release carries its changes out). The fix splits the pushes by what they are: THIS release's tag at HEAD is load-bearing and fails the job if rejected (it never should be — HEAD's workflow blob matches the branch, which is why v0.2.17's own tag went through); the historical backfill is best-effort per tag, warns per rejection, and emits one notice with the single human command that completes the set — `git push origin --tags` from any workflows-scoped credential. Once a human has done that once, the backfill loop becomes a chain of no-ops. Lesson recorded for the case-studies pile: the same both-remotes discipline that made CI verify-and-tag instead of commit-and-tag also meant the failure cost nothing but a skipped deploy — no bump commit was stranded on one side of the two-VCS split."),
    ('v0.2.17', '2026-08-16', 'obj-cas-imm-24876be44e37',
     "Two reader-driven fixes and the release pipeline grows tags. (1) Layout: the embed buttons and their status line sit back in the text column where they belong — only the vault surface itself breaks out wide, since it is the thing with the big UX. (2) CI tagging, ported from the VoiceDebrief website pipeline (validate → tag → publish, every push to dev a minor release tagged v{release}.{major}.{minor}) with one deliberate adaptation: the upstream OSBot action has CI commit a version-file bump, but this repo is simultaneously an sgit vault, and a CI-authored commit would exist only on the git side — breaking the both-remotes-in-sync invariant release.sh enforces. Here CI verifies-and-tags instead of owning: SITE_VERSION (bumped once per release by release.sh) must match the release commit's subject and be the next minor after the latest tag, then the commit is tagged. No CI commits, no drift, same discipline — and a forgotten bump now fails the pipeline loudly instead of shipping quietly. The first run backfills tags for every historical release by parsing the commit subjects, so the whole v0.1.9→now history becomes navigable by tag. Also: validate.js now runs in CI as the gate before tagging and publishing, which puts the key-leak tripwire on the deployment path as well as the release path. (Tags could not be pushed from the authoring session — the session's git proxy authorizes branch pushes only, which settled the design question of who owns tags: CI does.)"),
    ('v0.2.16', '2026-08-16', 'obj-cas-imm-34ed83dd03e6',
     "The embed grows up: both official surfaces, one click each, over the UI's new embed protocol. Reading the deployed bundle found what the addendum's Phase 3 had shipped — embed-protocol.js and a shared embed-receiver on BOTH shells: the host page loads ?embed=1&parent=<origin>, the frame proves itself with vault-embed-ready, and only then is the key sent by postMessage with the targetOrigin pinned. Strictly better than the URL-fragment flow shipped yesterday: the key never appears in any URL, is never written to the frame's storage (verified — sessionStorage and localStorage empty after open, memory-only as the protocol promises), and the host gets structured vault-ready/vault-error events instead of guessing from load timings. The demo page now has two buttons: App Mode, and — new — the vault browser with the FILES/SGIT/SETTINGS rail, which previously needed a two-step trick because /en-gb/vault deliberately strips URL hashes and root is the only inbox. Headless-verified both: App Mode ready in 2.7s, browser in 9.7s, rail present, R1 W0 badge, no horizontal scroll. The embed area breaks out of the text column (94vw up to 1680px, height tracking the viewport) because the vault browser is a full working surface, plus a full-screen button — both asked for by a reader with big-UX vaults. What is still not possible is stated precisely on the page: vault-open carries {key, mode, deepLink} where deepLink is a file path, so a host can select a SURFACE but not a VIEW — SGIT and SETTINGS remain in-page events. The briefing gains an addendum thanking the UI team, recording the verification, and sharpening the last ask to one optional field: view:'files'|'sgit'|'settings' on vault-open, applied after mount. Also fixes a stale paragraph v0.2.15 left behind (a silent curly-quote replace failure) — the page no longer promises a swap that already happened."),
    ('v0.2.15', '2026-08-15', 'obj-cas-imm-576ba8a1a09f',
     "The gap closed: the official SG/Vault interface now opens from a published read key, and this site embeds it. Our v0.2.7 experiment had isolated the blocker to exactly one thing — the loader documented a read-only credential but rejected it, and the CLI shorthand was parsed as a passphrase and PBKDF2'd into the wrong ref id. The UI team shipped the fix: a read-key credential is now its own format (<64-hex>:<vault_id>, the shape sgit clone already accepted) and is tested BEFORE the passphrase formats, which was the precise ordering bug; canonical CLI key prefixes are stripped first. Re-running the same experiment against the deployed build, read key only, no vault key anywhere: all three credential forms parse; App Mode boots the Field Notes demo under full chrome with its six studies rendered and the bridge live; the vault browser opens with the FILES/SGIT/SETTINGS rail over the real decrypted tree; and the SGit view lists both commits with real object ids — all inside a cross-origin iframe, with an explicit R1 W0 / Read-only badge. So /demos/vault-app-embed.html now carries TWO hosts and keeps both on purpose: the ~170-line minimal host that shows the protocol with nothing hidden, and the official UI opened with the same published key. One ask stays open and is stated as such — no URL selects a view, so the SGit inspector cannot yet be framed in isolation. Also: the release tripwire learned the CLI's canonical WRITE-key prefix (its read-only sibling is deliberately exempt — we publish one), proven by making it fail before trusting it; it promptly caught this very release note's first draft, which had spelled the banned prefix out while explaining it. The hub capability audit is updated with verified evidence — row 1, the entry point for everything, flips from partial to present, which settles the spec's assembly-not-construction question for the forge's read-only tier."),
    ('v0.2.14', '2026-08-15', 'obj-cas-imm-2f3c360b2de1',
     "Ask B of the 14 Aug pack begins: the hub.sgit.ai briefing-pack plan lands in admin/plans/, and — per the spec's central instruction — the capability audit comes before any architecture. The audit table is already 13 rows deep, seeded entirely from evidence this project has produced: verified present (open-from-read-key in our readers, single-object decrypt, the app runtime under a sandboxed iframe, sparse per-object fetch, cross-session caching with the 120s ref window, frameability), verified partial with the exact gap named (the official UI parses but rejects its own documented read-only credential format), and honestly unknown (client-side merge, the in-UI diff and history views — enumerated in the bundle, never driven). The partial rows are flagged as the dangerous ones, because a partial capability gets assumed complete. The plan also fixes the pack's shape: six parts in order, the four absences stated up front, surfacing/adding/absent applied per feature (blame is adding, not surfacing), permissions as worked key topologies, and the private-vault key-handling flow named as the one needing a considered position. The crawler question is closed as answered: full text in the served HTML, noscript reveal since v0.1.26, and Google indexing confirmed."),
    ('v0.2.13', '2026-08-15', 'obj-cas-imm-35d4e3e3a906',
     "Fix: the catalogue page shipped without the vault debug panel markup that the shared reader wires unconditionally, so the reader threw on two missing elements and the first document never rendered (navigation and clicked entries worked; the initial body stalled at the fetching message). The panel is now on the page — which it should have been anyway, since watching the ciphertext arrive is half the point — and the headless check confirms the README renders on load with zero page errors."),
    ('v0.2.12', '2026-08-15', 'obj-cas-imm-15dbcf053020',
     "The catalogue: a vault indexing vaults, including itself. The 14 Aug briefing pack's Ask A lands as designed — a submission queue whose per-entry cost is a read key and one line, with everything else derived by opening the vault. The deriver (admin/build/catalogue_derive.py, ~120 lines, read-only, no token) turns a read key into file count, plaintext size, commit depth, HEAD, top-level layout, file types, app entries and browser-renderability; proven on all three published-key vaults (Field Notes 4bshby5n, the strategy/maps vault ookq4mn4 — both app entry points detected — and the deploy-docs vault fyofmkvr, markdown-only). The catalogue itself lives in a new vault (kc67yhgw) published with its own read key and listed in itself: README (how to submit), SCHEMA (supplied-vs-derived, and the two rules — read keys yes, vault keys never; escrow the write key BEFORE publishing, because a frozen vault can never be corrected), three processed entries, and the two public to-do lists the brief asked for — awaiting-a-read-key (seeded with eight vaults named in the memos, each carrying the pre-publish audit instruction the strategy-maps case taught) and awaiting-processing (the agent's queue, currently empty). /catalogue/ renders it live via the same reader as the deploy docs — updated by pushing to the vault, no site deploy. Write-key status is a first-class field: 'known and escrowed' or 'lost', stated publicly per entry."),
    ('v0.2.11', '2026-08-15', 'obj-cas-imm-1f8635c410ef',
     "sgit gets its own Wardley map analysis — six maps starting with git at full strength, because a map that flatters its author is not a map: version control today (git's moat is the platform layer, resting on readable storage), the files that cannot follow (a hole in the map where their foundation should be), sgit's move (no new verbs, invert the bottom layer), the boundary on one map (two chains from one team, split by 'may the store read this?'), agents as the new user (the serialised diff versus ambient authority), and the strategy (commoditise private version control). The maps are drawn as inline SVG by a ~90-line renderer — no images, no dependencies — and the analysis ships as a SECOND app inside the same vault as the SG/Send strategy essay (ookq4mn4): one encrypted store, two entry points, one published read key; the embed opens it by passing entry to the same host. The embed shim gained link handling — in-page anchors scroll manually (assigning location.hash re-navigates a srcdoc frame) and relative .html links remount the frame on the new entry, so the two apps cross-link inside the embed; verified headless: 6 maps, 42 nodes, 12 evolve arrows, and clicking the companion link lands on the strategy essay. Linked from the Why page's boundary section. Also: Google has confirmed indexing sgit.ai, which unblocks the component registry when its turn comes."),
    ('v0.2.10', '2026-08-15', 'obj-cas-imm-cedfb3d06f6a',
     "Plan bookkeeping: the why-expansion plan's status table now reflects reality — Why reframe done, serialised PR done with its CLI brief, two of three demo vaults live, embed at the minimal-host stage pending the UI team's credential fix."),
    ('v0.2.9', '2026-08-15', 'obj-cas-imm-2ce42cfd214e',
     "The two remaining pieces of the briefing-pack plan land. (1) The Why page is reframed from rebuttal to boundary map: it now opens with where git wins, then draws the boundary precisely — the operations are not the gap (commit through merge all exist; proposing reviewable changes without write access is present, as a serialised diff, and is a differentiator); what is absent is the hosted review interface and the ecosystem above the protocol; and git is also client-side, so the real difference is that the objects are encrypted there, with the losses stated as a given-up/in-exchange-for table. New protocol section: the six-step read path verbatim, the two keys named explicitly, the three modes (Local/API/Web), and the two-implementations proof point. The LinkedIn comment and the market answer move below the boundary, kept whole. (2) New lead use case: the serialised pull request — no credential issued at all, grounded in the 5 Aug Black Hat disclosure, with an honest shipped-vs-pattern table (emit exists as history diff --json; import is not first-class) and evidence status PARTIAL. The matching brief to the CLI team asks for sgit diff export/apply, a published diff format, and ignore-file support — the latter now a prerequisite for the one-folder-two-VCS pattern the site publishes."),
    ('v0.2.8', '2026-08-15', 'obj-cas-imm-4060eca3121d',
     "Second demo, and the first with real content: The Strategy in Seven Maps — the actual SG/Send strategy, published on LinkedIn in May 2026 — served live from a vault with a published read key. The page also publishes the audit that made this interesting: the original vault could NOT publish its read key, because its own read-write credential was written inside its content (a production briefing quoted the clone command verbatim), server-side bookkeeping under .vault/owner/ carried live delete_auth tokens, and the vault's keys derive from a legacy low-entropy token. The fix is the pattern the page teaches: republish, don't retrofit — sanitised copy, credentials redacted with a visible note, fresh full-entropy vault (ookq4mn4), and only then a published read key; a republish also sheds the history you cannot publish. The embed host gained vault-path image support (a MutationObserver swaps img.src vault paths for blob: URLs read over the bridge, the same job the real host's interceptor does) — verified: all eight Wardley Map PNGs travelled as ciphertext and rendered."),
    ('v0.2.7', '2026-08-15', 'obj-cas-imm-1b9cd77fb6d7',
     "The full-UI embed experiment, run and published. Driving the real SG/Vault interface framed inside a page: the UI is frameable (no X-Frame-Options, no frame-ancestors), and App Mode works completely inside a cross-origin iframe — with a valid credential the official app-shell booted the Field Notes demo under the full HUD chrome. The one gap is the credential: the loader documents a read-only format (vault_id + 64-hex read key) but the client rejects it, and the CLI's 64hex:vault_id shorthand gets PBKDF2'd as a passphrase and derives the wrong file ids. No URL selects the SGit view, either. Both are now precise, evidence-backed asks in the UI-team briefing — honour the documented format (which alone makes the official UI embeddable with only the published read key) and add a |view:sgit deep-link. The demo page carries the findings table."),
    ('v0.2.6', '2026-08-15', 'obj-cas-imm-966aed3bd862',
     "The first demo ships: a vault app running live inside a sgit.ai page from a published read-only key. A new vault (Field Notes, 4bshby5n) was created from scratch for it — a self-contained app following the authoring contract, generative SVG art, content in content.json read over the bridge — and /demos/vault-app-embed.html is the complete walkthrough: init, commit, push, derive the read key, publish it deliberately, embed. The embed host is assets/vault-embed.js (~170 lines): HMAC-derived ids, ciphertext over CORS, Web Crypto decryption, the app booted in a sandbox=allow-scripts iframe with an opaque origin, and its sg.vfs/loadCss/loadJs calls answered over postMessage — the same shape as SG/Vault's vault-in-vault, minimal by design until the UI team answers the reuse briefing. Also rewrites the one-tree-two-remotes ordering section as a clean rule (the discovery narrative is gone), adds the Demos nav section, and extends the key-leak tripwire to scan for every demo vault's passphrase, not only the site's own. Verified end to end in headless Chromium: bridge live (the app's status line reads content via sg.vfs.readText from the vault), six tiles rendered, frame origin opaque, mutations impossible by construction."),
    ('v0.2.5', '2026-08-14', 'obj-cas-imm-fedcfbd348c0',
     "Corrects the one-tree-two-remotes case study, prompted by a reader question: if sgit pushes first and git commits after, don't the files match? They do — tested rather than argued. With that ordering git captures the freshly written ref every time and a clean tree is the normal end state of a release; reads (ls, history, status, vault info), no-op commits and pushes, pull and fetch were all tried and none rewrites the ref. The section is now a rule about ordering rather than a claim of permanent drift, keeping the part that is true and useful: when the ref IS dirty, the bytes tell you nothing, because a rewritten ref never byte-matches even when it decrypts to the same commit."),
    ('v0.2.4', '2026-08-14', 'obj-cas-imm-854db222f8cb',
     "Wider layout across the site. The reading column was a classic 720px prose measure, which squeezed the content into the middle of a modern display and made every page longer than it needed to be. The measure is now 960px and the wide container 1360px, with the body type up a step (.93rem to .98rem) so the longer line keeps a comfortable character count; the home-page sections (hero, terminal, feature grid, cards) scaled in proportion, and the deploy-section nav column widened with them. Verified at 1600px (no overflow, content fills the frame) and at 390px (no horizontal scroll)."),
    ('v0.2.3', '2026-08-14', 'obj-cas-imm-6deb6376d9bd',
     "Plans and briefs from the 14 Aug briefing pack. Publishes the implementation plan for the Why reframe (boundary map), the serialised-pull-request lead example (with one honesty gap found while planning: the diff emit exists as history diff --json, but the CLI has no apply/import command, so the page will ship as PARTIAL and a brief goes to the CLI team asking for sgit diff export/apply plus a published diff format), three end-to-end demo vaults with deliberately published read keys, the embed-reuse work, and the component registry (components, never plugins — plugin stays reserved for capability grants; registry gated on indexing being observed). Files a briefing to the SG/Vault UI team with six concrete questions about reusing their app-iframe host code inside sgit.ai pages, linked from the briefs page."),
    ('v0.2.2', '2026-08-14', 'obj-cas-imm-29aa935bd44a',
     "New case study: one working tree, two version control systems — the workflow this site is actually developed with. One folder is both an sgit vault and a git repository; a release is two pushes of the same tree. The page covers what each remote carries, the one-file .gitignore boundary that makes it safe (everything encrypted is committed; only the plaintext local/ tier is excluded), and the finding that surprised us: the encrypted ref always looks modified to git because AES-GCM uses a fresh IV per write, so for that one file git status cannot detect staleness — proved by decrypting both sides to the same commit id. Ships admin/build/release.sh, which makes the discipline mechanical: build, validate (the key-leak tripwire gates BOTH pushes, not just the deployed one), push sgit, push git, and refuse to finish unless both remotes report in sync. The script deliberately never invokes commands that echo the vault key."),
    ('v0.2.1', '2026-08-14', 'obj-cas-imm-49cf3a524b0c',
     "Fixes a gap the v0.2.0 restructure opened: llms.txt is generated by walking a list of known sections, and the new case-studies section was not in it, so all three of those pages were silently absent from the machine index — present on the site, invisible to any agent reading llms.txt. The section is added, and the generator now refuses to build if any page would be omitted, which is the same guard as the orphan-page rule and for the same reason: a page nothing links to and a page the index does not list are both unpublished."),
    ('v0.2.0', '2026-08-14', 'obj-cas-imm-d8f580db4d0f',
     "Structural release — the middle digit moves, as the numbering note below promised it would. Two changes. (1) The root held 19 files and every page body was inlined in a 2,709-line generator; bodies now live one-per-file in admin/content/ with a pages.json manifest, and the generator is a 648-line engine that does not grow as the site does. Adding a page is a content file plus a manifest row; the build then produces the HTML, the markdown twin, the llms.txt row, the llms-full.txt section, the sitemap entry and the canonical/OG/JSON-LD tags. The refactor was verified output-preserving before any page moved: all 31 pages byte-identical. (2) Sections became folders — why/, try/, security/, skills/, briefs/ — leaving 9 files in the root, all of them ones that must be there. New case-studies/ section, which is where the leaked-key incident and the live-vault architecture now live; they were filed under docs/ and deploy/ where nobody looking for a case study would find them. Links were rewritten mechanically by resolving each href against the old path and re-expressing it from the new one, then verified by crawling every internal URL from the homepage: 29 URLs, zero broken."),
    ('v0.1.27', '2026-08-14', 'obj-cas-imm-87daa0751f0d',
     "Entity disambiguation, after checking what search actually returns. Google's AI Overview for the bare query already knows this project — and sources it from PyPI, because the PyPI page never linked here and this site was not in the index. \"sgit\" is also an Android Git client, an Indian engineering college and a class of shell shortcut, so the job is not only being indexed but being resolved to the right thing. Every page now carries JSON-LD: a SoftwareApplication node with sameAs pointing at the PyPI and GitHub identifiers that already rank, an explicit disambiguatingDescription naming the collisions, and a per-page TechArticle node. Google's own 2026 guidance says structured data is not required for generative-AI features — this is here for entity resolution, not ranking. The validator now fails the build if a page has no structured data or if any JSON-LD block does not parse."),
    ('v0.1.26', '2026-08-14', 'obj-cas-imm-5da2eb791bb2',
     "Acts on an inbound brief from an agent that tried to use this site as documentation and could not. It reported that the site did not rank for its own positioning language and guessed the pages might be client-side rendered. They are not — the full text is in the served HTML — but the fade-in that hides the unstyled flash left body{opacity:0} until a JavaScript bootstrap ran, so any client applying our CSS without running that bootstrap rendered a complete but entirely invisible page (measured: 15,733 characters at opacity 0), which is also a hidden-text signal to an indexer. Fixed with a noscript override and a CSS-only reveal failsafe, both now enforced by the validator. Adds the crawler surface that never existed: robots.txt, a generated sitemap.xml covering every page, and canonical plus Open Graph tags. Adds llms-full.txt — every page in one document — for the very common agent harness that will not follow a link out of a fetched file, and makes llms.txt self-sufficient: inline answers to the common questions (including exactly which git operations exist and which do not) and per-page key facts, on the brief's observation that for such an agent the descriptions are the only content it will ever see. The brief and what changed are published on the briefs page."),
    ('v0.1.25', '2026-08-14', 'obj-cas-imm-1861dd16dd11',
     "Three changes that go together. (1) Every page now has a .md twin at the same path, generated from the same content so the two cannot drift, with internal links rewritten to point at markdown — an agent can traverse the whole site without parsing HTML, and llms.txt is now generated from the page registry rather than hand-maintained. (2) A git-and-sgit comparison on the Why page that says plainly where git is better — performance at scale, ecosystem, bisect/blame/rebase, partial commits — and how the two run side by side, as they do on this site. (3) Use cases moved to /use-cases/ with a page per situation: the problem, a working recipe on shipped commands, an honest evidence status (proven / partial / pattern), and a brief you can hand to an agent. Validator gained three rules: every page has a markdown twin, markdown links resolve, and no raw HTML leaks into the markdown."),
    ('v0.1.24', '2026-08-14', 'obj-cas-imm-3c426ddbe9e9',
     "Why page rewritten around the right question. The first version answered \"is there a market\" with verticals and a comparison table; the sharper answer is what sgit makes possible that was not possible before, so that is now the headline: six capabilities running on this site — a live site its host cannot read, read access as a publishable capability, two agents sharing a workspace neither host can read, private data with CDN economics, storage as untrusted commodity, and transit security that does not rest on the CA system (including where that goes next: the read key never leaving the client, or PKI with a client-only private key). The page now assumes the reader knows git and only covers the delta. Also corrects the business-model answer: the client being open source IS the distribution strategy, with services built on top — not \"no revenue attached\"."),
    ('v0.1.23', '2026-08-14', 'obj-cas-imm-89a142ee3598',
     "A freshness window on the mutable HEAD pointer. The ref was the last per-page-view network request left; it is now checked at most once every ref_ttl_s seconds (120 by default, configurable in deploy/vault.json), so reading inside the window costs zero requests and server load scales with readers rather than page views. The cost is a bounded propagation delay — a new commit appears within the window at worst — and \"check for new commit\" forces a fetch that ignores it. The vault panel logs the reused ref as TTL and counts down live to the next check."),
    ('v0.1.22', '2026-08-14', 'obj-cas-imm-d9ac70d78c31',
     "Kills the load-time flicker of the vault panel. The panel's remembered width and open state were restored by the reader script, which loads asynchronously — so the panel painted at its CSS default width, then jumped and slid open a beat later. Restoration now happens synchronously, before the first paint, and the slide transition is suppressed until state has settled. Opening and closing the panel by hand still animates; restoring it never does."),
    ('v0.1.21', '2026-08-14', 'obj-cas-imm-5a60bc3bf25b',
     "Object bodies in the vault panel are now syntax-coloured like an editor — keys, strings, numbers, literals and punctuation each get their own colour — and word wrapping is off, so structure survives and long values (base64 ciphertext, object ids) scroll horizontally instead of folding into a wall of text. Highlighting is applied only when the decrypted object actually parses as JSON, so markdown blobs stay plain."),
    ('v0.1.20', '2026-08-14', 'obj-cas-imm-78146d2f4f86',
     "The vault panel now links to the page that explains it. There is a compact “how this works” link in the panel header (always visible) and a fuller card at the foot of the panel pointing at deploy/how-this-works.html — the panel is where you are when the question occurs to you, so it is where the answer should be offered."),
    ('v0.1.19', '2026-08-14', 'obj-cas-imm-fe67d9589a2e',
     "Fixes the resize grip, which shipped in v0.1.18 but was unusable: it was absolutely positioned inside the panel\'s scrolling area, so it scrolled out of reach as soon as you moved down the object list, and at 6px fully transparent it was invisible anyway. The panel is now a flex shell — a fixed 12px drag rail with a visible handle, plus a separately scrolling body — and dragging uses pointer events with capture (mouse, pen and touch). Double-click the rail to reset the width."),
    ('v0.1.18', '2026-08-14', 'obj-cas-imm-6eded1c95732',
     'Vault panel becomes an object inspector: every row now shows what the object IS (ref/commit/tree/blob), WHY it was read, and — on click — its decrypted contents, pretty-printed for JSON. The panel is width-resizable (dragged from its left edge, remembered). Plus a real optimisation the panel made obvious: the path→blob index is a pure function of the commit id, so it is now memoised in localStorage — a first visit walks every tree to learn the encrypted filenames, but subsequent visits to an unchanged commit read zero tree objects.'),
    ('v0.1.17', '2026-08-14', 'obj-cas-imm-9d5b50f68679',
     'Vault panel: a "clear list" button that resets the request log and counters without touching the caches (so you can see exactly which objects one page needs); the panel\'s open/closed state now persists across navigation and reloads; cached objects record when they were stored and the panel shows their age. Navigation now scrolls to the top of the content rather than the top of the document. New page: deploy/how-this-works.html — the full architecture with hand-drawn SVG diagrams of the two-session publishing pipeline and the client-side read path.'),
    ('v0.1.16', '2026-08-12', 'obj-cas-imm-34684a789fe6',
     'New /why page answering the sharpest public criticism of the project ("I see no market or value whatsoever") directly and without marketing: who actually has the problem, why git-crypt/Dropbox/S3+KMS do not cover it, the market question answered plainly (the CLI has no revenue attached; hosting is the commercial layer; no TAM claims), where the criticism is right, and a twelve-question FAQ pre-answering the promised follow-ups.'),
    ('v0.1.15', '2026-08-12', 'obj-cas-imm-0959988dd4fe',
     'New Deploy section: self-hosting guidance rendered LIVE in the browser from an encrypted SG/Send vault, using a published read-only key — ciphertext over CORS, AES-256-GCM decryption via Web Crypto, no copy stored on this site and no rebuild when the SG/Send team pushes. Includes a three-tier cache (session memory, permanent Cache API for immutable objects, always-fresh ref) and a vault debug panel showing the HEAD commit, per-object request log, and cache hit/miss stats.'),
    ('v0.1.14', '2026-08-12', 'obj-cas-imm-3b54c02dbb96',
     'Two new pages, both linked this time: docs/exposed-vault-key.html (the rotation runbook plus the case study of this site\'s own key leak) and briefs.html (cross-team briefs — which v0.1.13 built but never registered, so nothing linked to it). New validator rule: every generated page must be reachable from another page, or the build fails. Added a fourth CLI-team ask: history-preserving rekey.'),
    ('v0.1.13', '2026-08-12', 'obj-cas-imm-5168ef3fe1a7',
     'SECURITY: the vault passphrase had been written into admin/build/validate.js as an anti-leak tripwire regex — which put the literal secret into a tracked, public file (present in 3 commits). Removed; the tripwire now reads the secret from the gitignored local/ tier and scans for it, so it can never be hardcoded again. The key must be treated as compromised and rotated. Also: a /briefs page collecting the cross-team briefs (multi-agent collaboration log), and a "contacting the server" notice before network commands in the browser terminal.'),
    ('v0.1.12', '2026-08-11', 'obj-cas-imm-e8ceb3fc2239',
     'In-browser clone completes: serial-executor shim for Pyodide (WebAssembly cannot spawn threads, so all parallel blob transfers run sequentially in the browser) — validated natively against the live server with thread creation disabled: full 225-blob clone of this site vault. A serial/auto-detect mode is proposed upstream to the sgit CLI.'),
    ('v0.1.11', '2026-08-11', 'obj-cas-imm-c9afa76a79cb',
     'Browser-transport fix for in-browser clone: drop the redundant X-API-Key header (the servers CORS-allow x-sgraph-access-token but not x-api-key, and one disallowed header fails the whole preflight — diagnosed live from the first user clone attempt); CORS/network failures now surface as readable HTTP 599 errors instead of a Pyodide SystemError.'),
    ('v0.1.10', '2026-08-11', 'obj-cas-imm-deac6363bff9',
     'In-browser terminal on /try: the real sgit CLI in-process (init, commit, status, history — and network commands via a browser XHR transport: clone/push/pull straight to the SG/Send servers), plus a busybox of file commands over the in-memory filesystem. Key hygiene: every example key on the site is now an obviously-invalid placeholder (format-valid example keys are squattable namespaces), enforced by a new validator rule.'),
    ('v0.1.9', '2026-08-11', 'obj-cas-imm-83b8c23a1baa',
     '"Try sgit in your browser" page: the real sgit-ai wheel running client-side under Pyodide (verified in headless Chromium first) — key derivation, encrypt/decrypt, an in-memory vault round trip, and a Python REPL. Plus: bootstrap fast-path for static hosting (no 2.5s bridge wait on GitHub Pages), CNAME for sgit.ai, and GitHub Pages deployment via Actions in the SGit-AI__Website repo.'),
    ('v0.1.8', '2026-08-11', 'obj-cas-imm-775783f31110',
     'Skills promoted to a top-level nav item with a new /skills page and the three agent skills shipped in the vault (latest versions, verbatim); llms.txt added at the vault root — encrypted for key-holders today, a standard public llms.txt when the site deploys to GitHub Pages; Home nav link retired (the brand mark covers it).'),
    ('v0.1.7', '2026-08-11', 'obj-cas-imm-c226a3aff160',
     'SG/Vault section rebuilt from the official docs bundle: corrected security-page structure-key claim to current reality, git page aligned with the publishing guide (three-rule boundary, leak audit, GitHub round trip, restore drill), new pages for static hosting on GitHub Pages, sub-vaults, and no-code content authoring; .gitignore extended with work/ and *.pem rules.'),
    ('v0.1.6', '2026-08-11', 'obj-cas-imm-f62d9bd2d0d4',
     'Corrected git integration to the side-by-side design: git now tracks the encrypted .sg_vault store (only the plaintext local/ folder is excluded), so a git remote doubles as a zero-knowledge mirror of the vault. Pattern documented on the git-and-vaults page.'),
    ('v0.1.5', '2026-08-11', 'obj-cas-imm-353038cc3e56',
     'Git integration: .gitignore (keeps .sg_vault/ — above all local/ keys and token — plus git metadata and build noise out of git and out of vault snapshots) and .gitattributes (raw sgit store files marked binary/-diff/-merge; generated *.html marked linguist-generated).'),
    ('v0.1.4', '2026-08-11', 'obj-cas-imm-90254d9591ff',
     'New SG/Vault section — for now the official sgraph platform documentation: SG/Vault & the platform, building vault apps, the window.sg bridge & host capabilities, and "git repos inside vaults" (engineering preview of the pure-Python git reader, verified against a real 906-commit repo).'),
    ('v0.1.3', '2026-08-11', 'obj-cas-imm-46a8b14d4fca',
     'Beta status (in production use), light theme, admin & engineering section, per-push version badge on every page, SG/Vault & SG/Send now link to sgraph.ai, design-improvements brief for Claude Code.'),
    ('v0.1.2', '2026-08-11', 'obj-cas-imm-c3084abbba8c',
     'Replaced the proposal app with the sgit.ai MVP site: 12 individually-navigable pages, shared CSS/JS loaded through the SG bridge, full-strength keys in all examples.'),
    ('v0.1.1', '2026-08-11', 'obj-cas-imm-7f1fbacf0485',
     'Initial vault app: the positioning & messaging proposal microsite with an embedded landing-page prototype.'),
]

ROOT  = find_vault_root()
ADMIN = os.path.join(ROOT, 'admin')

BOOT = """<script>
(function(){var R=document.documentElement.getAttribute('data-root')||'';var V='?v=' + SITE_VERSION_TOKEN;var C=[R,'','../','/'].filter(function(v,i,a){return a.indexOf(v)===i});
function wait(ms){return new Promise(function(res){var t=Date.now();(function p(){if(window.sg)return res(window.sg);if(Date.now()-t>ms)return res(null);setTimeout(p,60)})()})}
function grab(sg,p){return new Promise(function(res){(async function(){if(sg&&sg.vfs&&sg.vfs.readText){try{var t=await sg.vfs.readText(p);if(t)return res(t)}catch(e){}}try{var r=await fetch(p+V);if(r.ok)return res(await r.text())}catch(e){}res(null)})()})}
async function css(sg){for(var i=0;i<C.length;i++){var p=C[i]+'assets/site.css';if(sg&&sg.loadCss){try{await sg.loadCss(p);return}catch(e){}}var t=await grab(sg,p);if(t){var s=document.createElement('style');s.textContent=t;document.head.appendChild(s);return}}}
async function js(sg){for(var i=0;i<C.length;i++){var p=C[i]+'assets/site.js';if(sg&&sg.loadJs){try{await sg.loadJs(p);return}catch(e){}}var t=await grab(sg,p);if(t){try{(0,eval)(t)}catch(e){console.error('[site] js failed',e)}return}}}
async function boot(){var inVault=false;try{inVault=(window!==window.parent)||location.protocol==='blob:'}catch(e){inVault=true}
var sg=inVault?await wait(2500):null;await css(sg);await js(sg);document.documentElement.classList.add('ready');try{window.parent&&window.parent.postMessage({type:'sg-app-ready'},'*')}catch(e){}}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',boot);else boot();})();
</script>"""

BOOT = BOOT.replace('SITE_VERSION_TOKEN', "'" + SITE_VERSION + "'")

# The fade-in hides the unstyled flash while site.css is bridge-loaded. It must never be able
# to leave the page invisible: a crawler that applies CSS but does not run our bootstrap would
# otherwise see a fully hidden body — invisible to a reader and a hidden-text signal to an
# indexer. Two failsafes: <noscript> reveals immediately, and a CSS-only animation reveals at
# 1.6s regardless of why the bootstrap never arrived.
CRITICAL = ("<style>html{background:#faf9f5}body{margin:0;background:#faf9f5;color:#1c1d21;"
            "font-family:ui-sans-serif,system-ui,sans-serif;opacity:0;transition:opacity .25s;"
            "animation:sg-reveal 0s linear 1.6s forwards}"
            "html.ready body{opacity:1;animation:none}"
            "@keyframes sg-reveal{to{opacity:1}}</style>"
            "<noscript><style>body{opacity:1;animation:none}</style></noscript>")

# Two levels, because one was failing. The flat nav reached FOURTEEN items and wrapped
# to three rows on an iPhone before the page content began — measured on a real
# screenshot, not guessed. Grouping is by what a reader is trying to do, and every
# group's own label is a real link, so nothing is reachable only by hovering.
# The network chooser. One line per question a reader actually arrives with, mapped to
# the site that takes it seriously — because at nineteen siblings the useful question is
# not "what exists" but "which of these is mine".
ASK = [
 ('I need to give an AI agent an identity', 'nhi.sgit.ai',
  'agents you run vs agents you rent, and why only one is answered'),
 ('My app has to call an LLM and I do not want it holding an API key', 'llms.sgit.ai',
  'the bridge that lets it call one without a credential'),
 ('I have to sign off a risk and I do not want to rubber-stamp it', 'risks.sgit.ai',
  'there is no deny button — only how long you accept it'),
 ('I need to cite a regulation precisely, not paraphrase it', 'standards.sgit.ai',
  'point at the provision, or you are asserting'),
 ('I want to distribute public keys without a central authority', 'pki.sgit.ai',
  'a key registry for agents, designed from a directory that was destroyed'),
 ('I am drawing a graph and want to get the edges right', 'graphs.sgit.ai',
  'five rules, and why relates-to is banned'),
 ('I want an issue tracker with no database', 'issues-fs.sgit.ai',
  'the issues are files and the files are a graph'),
 ('I need somewhere disposable to run an agent', 'sg-compute.sgit.ai',
  'ephemeral AWS environments, one command away'),
 ('I am deciding how to license and sustain an open-source project', 'open-source.sgit.ai',
  'open source is a strategy, not a charity'),
 ('I keep being asked what a digital twin actually is', 'twins.sgit.ai',
  'an interface to reality, not a simulation of it'),
 ('I want to protect an app at the edge without renting a WAF', 'sg-sentinel.sgit.ai',
  'an app-coupled edge guard — published as a design, not built'),
 ('I want to map a strategy without drawing a pretty picture', 'wardley-maps.sgit.ai',
  'maps are claims, not pictures'),
 ('I need the requirements nobody writes down until they break', 'nfrs.sgit.ai',
  'resilience, budgets and backups, from the inside'),
 ('I want to know how this code is actually written', 'coding.sgit.ai',
  'the style guide that measured itself'),
 ('I am pricing something and rent feels wrong', 'subscriptions.sgit.ai',
  'a subscription is a discount for regular use, not rent'),
 ('I care where a published fact came from', 'newsroom.sgit.ai',
  'the story is a graph; the article is a projection'),
 ('I just want the picture', 'infographics.sgit.ai',
  'every rendered brief in one catalogue'),
]


NAV = [
    ('why',   'Why',       'why/index.html',      []),
    ('try',   'Try',       'try/index.html',      []),
    ('docs',  'Docs',      'docs/index.html',     [
        ('docs',   'Documentation',   'docs/index.html'),
        ('api',    'HTTP API',        'api/index.html'),
        ('vault',  'SG/Vault',        'vault/index.html'),
        ('deploy', 'Deploy',          'deploy/index.html'),
        ('skills', 'Skills',          'skills/index.html'),
    ]),
    ('vaults', 'Vaults',   'demos/vaults/index.html', [
        ('vaults',    'Published vaults', 'demos/vaults/index.html'),
        ('catalogue', 'Catalogue',        'catalogue/index.html'),
        ('demos',     'Demos',            'demos/index.html'),
    ]),
    ('evidence', 'Evidence', 'compare/index.html', [
        ('compare',      'Comparisons',  'compare/index.html'),
        ('case-studies', 'Case studies', 'case-studies/index.html'),
        ('use-cases',    'Use cases',    'use-cases/index.html'),
        ('briefs',       'Briefs',       'briefs/index.html'),
    ]),
    ('updates', 'Updates', 'updates/index.html', [
        ('updates',  'Updates',     'updates/index.html'),
        ('articles', 'Articles',    'articles/index.html'),
        ('admin',    'Version log', 'admin/versions.html'),
    ]),
    ('network', 'Network', 'network/index.html', [
        ('network',  'All sites',   'network/index.html'),
        ('nhi',      'nhi',         'network/nhi.html'),
        ('pki',      'pki',         'network/pki.html'),
        ('graphs',   'graphs',      'network/graphs.html'),
        ('sg-sentinel', 'sg-sentinel', 'network/sg-sentinel.html'),
    ]),
    ('security', 'Security', 'security/index.html', []),
]


def nav(p, here):
    items = []
    for key, label, href, children in NAV:
        keys = {key} | {c[0] for c in children}
        on = ' here' if here in keys else ''
        if not children:
            items.append(f'  <div class="ni"><a class="nl{on}" href="{p}{href}">{label}</a></div>')
            continue
        subs = '\n'.join(
            f'      <a class="sl{" here" if here == ck else ""}" href="{p}{chref}">{clabel}</a>'
            for ck, clabel, chref in children)
        items.append(
            f'  <div class="ni ni-has">\n'
            f'    <a class="nl{on}" href="{p}{href}">{label}<span class="caret">&#9662;</span></a>\n'
            f'    <div class="sub">\n{subs}\n    </div>\n'
            f'  </div>')
    return f"""<nav class="site"><div class="row">
  <a class="brand" href="{p}index.html">sgit<span>.ai</span></a>
  <span class="stage-pill">beta</span>
  <a class="ver" href="{p}admin/versions.html" title="Site release history">{SITE_VERSION}</a>
  <button class="nav-toggle" type="button" aria-expanded="false" aria-label="Menu">Menu</button>
  <div class="nav-items">
{chr(10).join(items)}
  </div>
  <a class="gh" href="https://github.com/SGit-AI/SGit-AI__CLI">&#9733; GitHub</a>
</div></nav>"""

def footer(p, md=''):
    return f"""<footer class="site"><div class="cols">
  <div>
    <div class="brandline">sgit<span>.ai</span></div>
    <p>sgit is git for encrypted vaults — clone, commit, branch and merge files that are encrypted with AES-256-GCM before they leave your machine. Open source, Apache-2.0, in beta and powering production workflows.</p>
    <p class="vaultnote">🔒 This site is itself served from an encrypted SG/Send vault — the page you are reading was decrypted in your browser. The medium is the message.</p>
    <p class="verline">site <a href="{p}admin/versions.html">{SITE_VERSION}</a> · <a href="{p}admin/index.html">engineering</a> · <a href="{md}" title="The same page as plain markdown — for agents, and for reading without the styling">this page as markdown</a></p>
  </div>
  <div>
    <h4>Docs</h4>
    <a href="{p}docs/what-is-sgit.html">What is sgit</a>
    <a href="{p}docs/installation.html">Installation</a>
    <a href="{p}docs/quickstart.html">Quickstart</a>
    <a href="{p}docs/sgit-for-git-users.html">sgit for git users</a>
    <a href="{p}docs/agents.html">Working with AI agents</a>
    <a href="{p}docs/limitations.html">When NOT to use sgit</a>
  </div>
  <div>
    <h4>SG/Vault platform</h4>
    <a href="{p}vault/index.html">SG/Vault &amp; the platform</a>
    <a href="{p}vault/vault-apps.html">Building vault apps</a>
    <a href="{p}vault/sg-bridge.html">The window.sg bridge</a>
    <a href="{p}vault/content-authoring.html">Content authoring</a>
    <a href="{p}vault/sub-vaults.html">Sub-vaults</a>
    <a href="{p}vault/git-and-vaults.html">Git repos inside vaults</a>
    <a href="{p}vault/static-hosting.html">Static hosting</a>
    <a href="https://sgraph.ai">More at sgraph.ai</a>
  </div>
  <div>
    <h4>Project</h4>
    <a href="https://github.com/SGit-AI/SGit-AI__CLI">GitHub</a>
    <a href="{p}security/index.html">Security</a>
    <a href="{p}why/index.html">Why does this exist?</a>
    <a href="{p}use-cases/index.html">Use cases</a>
    <a href="{p}case-studies/index.html">Case studies</a>
    <a href="{p}skills/index.html">Skills for AI agents</a>
    <a href="{p}briefs/index.html">Cross-team briefs</a>
    <a href="{p}llms.txt">llms.txt</a>
    <a href="{p}llms-full.txt">llms-full.txt</a>
    <a href="{p}admin/index.html">Admin &amp; engineering</a>
    <a href="{p}admin/versions.html">Release history</a>
  </div>
</div></footer>"""

# ---------------------------------------------------------------- structured data
# Google's 2026 AI-optimisation guidance is explicit that structured data is not required
# to appear in generative-AI features — "it is still SEO". It is included here for a
# different and specific reason: "sgit" is an ambiguous string. It also names an Android
# Git client, an Indian engineering college, and a class of shell shortcut, and Google's
# AI Overview for the bare query currently disambiguates between them while sourcing this
# project from PyPI. sameAs links the site to the identifiers that already rank, which is
# how an entity gets resolved to the right thing rather than to the most popular thing.

def json_ld(path, title, desc):
    site = {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": "sgit",
        "alternateName": ["sgit-ai", "sgit CLI"],
        "applicationCategory": "DeveloperApplication",
        "applicationSubCategory": "Version control",
        "operatingSystem": "macOS, Linux, Windows",
        "url": "https://sgit.ai",
        "downloadUrl": "https://pypi.org/project/sgit-ai/",
        "installUrl": "https://pypi.org/project/sgit-ai/",
        "softwareHelp": "https://sgit.ai/docs/",
        "license": "https://www.apache.org/licenses/LICENSE-2.0",
        "programmingLanguage": "Python",
        "softwareRequirements": "Python >= 3.11",
        "description": ("git for encrypted vaults: clone, commit, branch and merge files that are "
                        "encrypted client-side with AES-256-GCM before they leave your machine. The "
                        "server stores ciphertext under opaque ids and never sees filenames, contents "
                        "or commit messages."),
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "sameAs": ["https://pypi.org/project/sgit-ai/",
                   "https://github.com/SGit-AI/SGit-AI__CLI",
                   "https://github.com/SGit-AI/SGit-AI__Website"],
        "disambiguatingDescription": ("Distinct from SGit, the Android Git client, and from SGIT, "
                                      "the Dr. Samuel George Institute of Engineering and Technology. "
                                      "This is the encrypted-vault CLI published to PyPI as sgit-ai."),
    }
    page_node = {"@context": "https://schema.org",
                 "@type": "TechArticle" if path != 'index.html' else "WebSite",
                 "name": title, "headline": title, "description": desc,
                 "url": f"https://sgit.ai/{path}",
                 "inLanguage": "en",
                 "isPartOf": {"@type": "WebSite", "name": "sgit.ai", "url": "https://sgit.ai"},
                 "about": {"@type": "SoftwareApplication", "name": "sgit",
                           "sameAs": "https://pypi.org/project/sgit-ai/"}}
    blocks = [site, page_node] if path == 'index.html' else [page_node]
    return '\n'.join('<script type="application/ld+json">' + json.dumps(b, ensure_ascii=False)
                      + '</script>' for b in blocks)


def page(path, title, desc, here, body):
    # Root prefix by DEPTH, not by "is nested at all" — pages now nest three deep
    # (demos/vaults/<slug>/index.html) and a single '../' silently pointed the nav,
    # the stylesheet and every asset at the wrong level. Same formula write_md uses.
    p = '../' * path.count('/')
    md_name = os.path.basename(path)[:-5] + '.md'
    # Same cache-busting as the bootstrap, applied to the components a page body
    # fetches for itself. Done here so no content file has to remember it.
    body = re.sub(r"(assets/[a-z-]+\.js)'", r"\1?v=" + SITE_VERSION + "'", body)
    # A page with walkthrough figures needs the component that fills them. Markdown
    # content types emit those figures from a `!shot` line, and a markdown author has
    # no place to put a script tag — so the engine notices and wires it, rather than
    # every content file having to remember. (The views page shipped once with the
    # figures and without the loader: nothing errored, and no images appeared.)
    # Match on data-shot= — the attribute shots.js actually selects on. Matching the
    # class string instead missed `class="shot net-shot"` and silently left an index
    # page with figures and no loader, which is the same failure this block exists to
    # prevent. Detect on the thing the consumer looks for, not on how it was written.
    if 'data-shot="' in body and 'assets/shots.js' not in body:
        body += (f'\n<script>\n(function () {{\n'
                 f"  fetch('{p}assets/shots.js?v={SITE_VERSION}')\n"
                 '    .then(function (r) { if (!r.ok) throw new Error(r.status); return r.text(); })\n'
                 '    .then(function (t) { (0, eval)(t); })\n'
                 "    .catch(function (e) { console.error('[shots] component failed to load:', e); });\n"
                 '}());\n</script>')
    html = f"""<!doctype html>
<html lang="en" data-root="{p}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://sgit.ai/{path}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="sgit.ai">
<meta property="og:url" content="https://sgit.ai/{path}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta name="twitter:card" content="summary">
<link rel="alternate" type="text/markdown" href="{md_name}" title="This page as markdown">
{json_ld(path, title, desc)}
{CRITICAL}
</head>
<body>

{nav(p, here)}

{body}

{footer(p, os.path.basename(path)[:-5] + '.md')}

{BOOT}
</body>
</html>
"""
    out = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w') as f:
        f.write(html)
    print('wrote', path, f'({len(html)} bytes)')


def versions_body():
    rows = '\n'.join(
        f'    <tr><td class="vnum">{v}</td><td>{d}</td><td class="vid">{c}</td><td>{note}</td></tr>'
        for v, d, c, note in VERSION_LOG)
    return f"""<main class="doc">
  <p class="crumb"><a href="../index.html">Home</a> / <a href="index.html">Admin</a> / Versions</p>
  <h1>Release history</h1>
  <p class="lead">This site ships by pushing its vault, and the site version — <b>{SITE_VERSION}</b>, shown in the nav of every page — increments on every push. Each release is also an sgit commit, so the vault's own <code>sgit history log</code> is the authoritative audit trail; this page is the human-readable index of it.</p>
  <div class="tablewrap"><table class="vers">
    <tr><th>Version</th><th>Date</th><th>Vault commit</th><th>Changes</th></tr>
{rows}
  </table></div>
  <p class="small dim">Numbering: v0.1.n while the site is in its first structure; the middle digit will bump on structural redesigns. The "vault commit" of the newest row reads "this release" because the commit ID only exists once the release is committed — it is recorded here retroactively by the next release.</p>
  <div class="pagenav"><a href="index.html">← Admin &amp; engineering</a><span></span></div>
</main>"""

# ============================================================ markdown mirror
# Every page is also written as .md next to its .html. This is not a nicety: agents
# are a first-class audience for this site, and asking them to parse styled HTML to
# reach guidance is a tax with no upside. The markdown is generated from the same
# body the HTML is built from, so the two can never drift.
#
# Internal .html links are rewritten to .md so an agent can traverse the whole site
# without ever touching HTML. Anything visual (SVG diagrams, terminal chrome) is
# reduced to its caption or its plain text — the words survive, the styling does not.

class Markdown_Writer(HTMLParser):
    SKIP       = {'script', 'style', 'svg', 'button', 'nav', 'footer'}
    SKIP_CLASS = {'capnum'}          # decoration whose text says nothing in prose
    VOID       = {'br', 'img', 'hr', 'input', 'meta', 'link', 'source'}
    BLOCK  = {'p', 'div', 'section', 'article', 'main', 'header', 'ul', 'ol', 'table', 'tr', 'blockquote', 'details'}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out       = []          # emitted chunks
        self.skipst    = []          # tag stack while inside a skipped element
        self.pre       = 0           # depth inside <pre>
        self.list      = []          # stack of ('ul'|'ol', counter)
        self.row       = None        # cells of the table row being built
        self.thead     = False
        self.cols      = 0
        self.href      = None
        self.link_text = None
        self.figcap    = False

    # ---- helpers
    def emit(self, s):
        if self.skipst: return
        if self.link_text is not None: self.link_text.append(s)
        elif self.row is not None:     self.row[-1] += s
        else:                          self.out.append(s)

    def block(self):
        if self.out and not self.out[-1].endswith('\n\n'):
            self.out.append('\n\n' if self.out[-1].strip() else '\n')

    # ---- tags
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if self.skipst:                                  # already inside a skipped subtree
            if tag not in self.VOID: self.skipst.append(tag)
            return
        if tag in self.SKIP or a.get('class') in self.SKIP_CLASS:
            self.skipst = [tag]
            return

        if   tag == 'pre':  self.pre += 1; self.block(); self.emit('```\n')
        elif tag == 'code' and not self.pre: self.emit('`')
        elif tag in ('b', 'strong'): self.emit('**')
        elif tag in ('em', 'i'):     self.emit('*')
        elif tag == 'br':            self.emit('  \n' if not self.pre else '\n')
        elif tag == 'a':
            self.href = a.get('href'); self.link_text = []
        elif tag in ('h1', 'h2', 'h3', 'h4'):
            self.block(); self.emit('#' * int(tag[1]) + ' ')
        elif tag in ('ul', 'ol'):
            self.block(); self.list.append([tag, 0])
        elif tag == 'li':
            if not self.list: self.list.append(['ul', 0])
            self.list[-1][1] += 1
            kind, n = self.list[-1]
            indent = '  ' * (len(self.list) - 1)
            self.out.append('\n' + indent + (f'{n}. ' if kind == 'ol' else '- '))
        elif tag == 'table':
            self.block(); self.thead = True; self.cols = 0
        elif tag == 'tr':
            self.row = []
        elif tag in ('td', 'th'):
            if self.row is not None: self.row.append('')
        elif tag == 'blockquote':
            self.block(); self.emit('> ')
        elif tag == 'summary':
            self.block(); self.emit('**')
        elif tag in self.BLOCK:
            self.block()
        if a.get('class') == 'figcap': self.figcap = True

    def handle_endtag(self, tag):
        if self.skipst:
            if tag in self.skipst:
                while self.skipst and self.skipst.pop() != tag:
                    pass
            if not self.skipst and tag == 'svg':
                self.out.append('\n\n*[diagram]*')
            return

        if   tag == 'pre': self.pre = max(0, self.pre - 1); self.emit('\n```\n\n')
        elif tag == 'code' and not self.pre: self.emit('`')
        elif tag in ('b', 'strong'): self.emit('**')
        elif tag in ('em', 'i'):     self.emit('*')
        elif tag == 'a':
            text = ''.join(self.link_text or []).strip()
            href, self.link_text, self.href = self.href, None, None
            if not text: return
            if href and not href.startswith(('http', 'mailto:', '#')):
                href = re.sub(r'\.html(#|$)', r'.md\1', href)
            self.emit(f'[{text}]({href})' if href else text)
        elif tag in ('h1', 'h2', 'h3', 'h4'): self.out.append('\n\n')
        elif tag in ('ul', 'ol'):
            if self.list: self.list.pop()
            self.out.append('\n')
        elif tag == 'tr':
            cells = [' '.join(c.split()) for c in (self.row or [])]
            self.row = None
            if not cells: return
            self.out.append('\n| ' + ' | '.join(cells) + ' |')
            if self.thead:
                self.out.append('\n|' + '---|' * len(cells))
                self.thead = False
        elif tag == 'table':  self.out.append('\n\n')
        elif tag == 'summary': self.emit('**\n')
        elif tag in self.BLOCK: self.block()
        self.figcap = False

    def handle_data(self, data):
        if self.skipst: return
        if self.pre:
            self.emit(data)
        else:
            text = re.sub(r'\s+', ' ', data)
            if text.strip() or (self.out and self.out[-1].endswith((')', '`', '*'))):
                self.emit(text)

    def markdown(self):
        md = ''.join(self.out)
        md = md.replace('\u00a0', ' ')
        md = re.sub(r'[ \t]+\n', '\n', md)
        md = re.sub(r'\n{3,}', '\n\n', md)
        md = re.sub(r'\n +([-*] |\d+\. )', r'\n\1', md)      # un-indent top-level bullets
        return md.strip() + '\n'


def to_markdown(body):
    w = Markdown_Writer()
    w.feed(body)
    return w.markdown()


def write_md(path, title, desc, body):
    depth = path.count('/')
    root  = '../' * depth
    md    = (f'# {title}\n\n> {desc}\n\n'
             f'*Source: <https://sgit.ai/{path}> · site {SITE_VERSION} · '
             f'this file is generated from the same content as the page, so the two cannot drift. '
             f'Every page on this site has a `.md` twin; internal links below point at them.*\n\n---\n\n'
             + to_markdown(body)
             + f'\n\n---\n\n*[Site index for agents]({root}llms.txt) · '
               f'[HTML version](https://sgit.ai/{path})*\n')
    out = os.path.join(ROOT, path[:-5] + '.md')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w') as f:
        f.write(md)
    return len(md)



# ============================================================ llms.txt
# Generated from PAGES, so it cannot go stale — the same reason the orphan and
# link checks exist. Every entry points at the .md twin: an agent following this
# index never has to parse HTML.

LLMS_PREAMBLE = """# sgit.ai

> sgit is git for encrypted vaults: clone, commit, branch and merge files that are
> encrypted client-side (AES-256-GCM) before they leave your machine. The server stores
> ciphertext under opaque IDs — it never sees filenames, contents, or commit messages.
> This site is the official documentation for sgit and the SGraph vault platform
> (SG/Vault, SG/Send) — and is itself served from an encrypted vault.

Every page below is markdown, generated from the same source as the HTML page at the
same path (swap `.md` for `.html`). Links inside the markdown point at markdown, so you
can traverse the entire site without parsing HTML.

Notes for agents:
- sgit is in beta and powers production workflows. Honest edges: /docs/limitations.md
- Install: pip install sgit-ai (Python >= 3.11; entry points `sgit` and `sgit-ai`)
- Vault keys are full-strength generated keys (`passphrase:vault_id`). No password reset exists.
- Never write a vault key into a tracked file. See /docs/exposed-vault-key.md for what that costs.
- The agent-facing command is `sgit write <path> --file <f> --message <m> --push --json`;
  every read path has a --json flag.
- Cross-session state pattern: clone/pull at session start, commit + push at session end.
- Task-shaped guidance with recipes and agent briefs lives under /use-cases/.

If your tooling cannot follow links out of this file, fetch /llms-full.txt — every page of
this site concatenated into one document (~155 KB). One request gets the complete set.

Quick answers (so you do not need a second request for the common questions):
- Does sgit do the git operations you know? Yes for: init, create, clone, status, commit,
  push, pull, fetch, branch (new/list/switch/checkout), merge with conflict resolution,
  history log/diff/show/revert/reset, stash. No for: pull requests (a hosting-platform
  construct layered on merge, not a git primitive), a staging area or partial commits
  (a commit snapshots the whole folder), bisect, blame, rebase, cherry-pick, hooks,
  submodules and tags. Full mapping: /docs/sgit-for-git-users.md
- The three deliberate differences from git: no staging area; every clone gets its own
  private branch and publishing to a shared branch is explicit; the vault key is address,
  credential and encryption key in one string.
- What the server can see: the vault ID, the size of each encrypted object, and request
  timing. Never filenames, contents, or commit messages. /security.md
- Read access is a separate, one-way-derived key: publishable, cannot be turned into write
  access, works against any server holding the ciphertext. This site publishes one.
- Crypto: AES-256-GCM, PBKDF2-HMAC-SHA256 at 600k iterations, HKDF-SHA256. No custom
  primitives; output matches the browser Web Crypto API byte for byte.
- Can two vaults SEND MESSAGES to each other? Yes. The transport is an APPEND LANE: a
  write-only channel on the recipient's vault, gated by a hex `append_token` the sender holds.
  The sender POSTs to /api/vault/append/write/{vault_id} with NO account and NO access token;
  the response is blind (`{"ok":true}` — no id, no count). The recipient lists and fetches with
  `x-sgraph-vault-enum-key` and decrypts client-side. Encrypt with `sgit pki encrypt --recipient`
  (RSA-OAEP 4096 + AES-256-GCM). Full worked example: /docs/vault-messaging.md
- The intended lane address is `append_token = H(recipient public key)`, so a sender can derive
  it from a published key. That derivation is PROPOSED — no shipped command emits it — so today
  you agree the token out of band. The server side is shipped. Do not code against the derivation.
- PKI exists. `sgit pki keygen/list/export/import/contacts/sign/verify/encrypt/decrypt`. The vault
  key is symmetric and roots the storage hierarchy; keypairs layer on top for identity and
  recipient-addressed encryption. /docs/pki.md · /security.md#pki
- The HTTP API is the whole surface — the CLI and the browser bridge are both clients. /api/index.md
- sgit is beta; it has no compliance certification of any kind.
"""

LLMS_SECTIONS = [
    ('why',       'Why this exists'),
    ('demos',     'Demos (live end-to-end examples with published read keys)'),
    ('catalogue', 'Catalogue (the index of published vaults — read keys, shapes, evidence and write-key status)'),
    ('vaults', 'Published vaults (one page per vault: description, features, live embed, and the read key that opens it)'),
    ('compare', 'Comparisons run as reproducible tests (the entry format, the privilege vocabulary, and the rows where vaults lose)'),
    ('use-cases', 'Use cases (task-shaped guidance: recipe, evidence status, agent brief)'),
    ('case-studies', 'Case studies (worked accounts of what actually happened, with numbers)'),
    ('docs',      'Docs'),
    ('api',       'HTTP API (the protocol surface: endpoints, auth headers, capability gates, limits)'),
    ('vault',     'SG/Vault platform'),
    ('deploy',    'Deploy (rendered live from an encrypted vault)'),
    ('try',       'Try it'),
    ('skills',    'Skills (packaged instructions for AI agents)'),
    ('briefs',    'Cross-team briefs'),
    ('updates',   'Updates (dated posts: what changed, one entry per story)'),
    ('articles',  'Articles (longer pieces that argue across pages, with the evidence linked)'),
    ('network',   'The sgit.ai network (sibling sites on *.sgit.ai subdomains, each pursuing one question)'),
    ('home',      'Optional'),
    ('security',  'Optional'),
    ('admin',     'Optional'),
]

LLMS_FACTS = {
    'docs/vault-messaging.html': 'Two vaults exchange encrypted messages over an APPEND LANE: a write-only channel on the recipient vault. The sender holds an append_token (hex, ^[0-9a-f]{16,128}$) and POSTs to /api/vault/append/write/{vault_id} with no account and no access token; the response is blind ({"ok":true}, no id, no count). The recipient lists/fetches with x-sgraph-vault-enum-key and decrypts locally. The intended lane address is append_token = H(recipient public key), but no shipped command emits it — PROPOSED; today agree the token out of band.',
    'docs/pki.html': 'sgit pki keygen makes TWO pairs: RSA-OAEP 4096 for encryption and ECDSA P-256 for signing (not X25519/Ed25519), passphrase-protected. export emits a JSON bundle {v,encrypt,sign,label,fingerprint,signing_fingerprint} of PEM blocks, not a bare PEM. encrypt --recipient <fingerprint>; decrypt --fingerprint <fingerprint> (required). Envelope v2 is base64 JSON {v,w,i,c}: RSA-OAEP wraps an AES-256-GCM content key. No revocation, no directory.',
    'api/index.html': 'The HTTP API is the whole surface; the CLI and the browser bridge are clients. The server is a capability-checked ciphertext store: it holds SHA-256 of each capability key and compares hashes, never a raw key and never a private key. Four capabilities: append_token (write one lane), enum_key (list/fetch/mark), write_key (configure/purge/write objects), private key (decrypt, client-side only).',
    'api/append-lanes.html': 'Six POST endpoints under /api/vault/append/: configure (write key), write (append_token in body, account-less), list (enum key), fetch, mark-processed (idempotent), purge (folder: pending|processed). Renamed from inbox in v0.32.7 — /api/vault/inbox/* is gone. Limits: 5MB payload (413), 1000 pending per token (507), 100 file_ids per batch (400), 3MB inline content (413), page 50/200.',
    'api/errors.html': '400 = malformed input, rejected before any gate; 403 = well-formed but wrong capability. A prefixed token (tok_..., or a CLI fingerprint sha256:...) returns 400, NOT 403 — append_token is hex only. 413 = too large, 507 = lane full at 1000 pending.',
    'api/authentication.html': 'Six headers: x-sgraph-access-token, x-sgraph-vault-write-key, x-sgraph-vault-enum-key, x-vault-read-key, x-vault-public, x-sgraph-transfer-delete-auth. append_token is NOT a header — it goes in the body. Vault reads need no auth on the shared host because the bytes are ciphertext under a key the server never had.',
    'api/vault-objects.html': 'Pointer store endpoints plus the caching contract: file ids containing -imm- are content-addressed and immutable (Cache-Control max-age=31536000, immutable); refs and indexes are mutable and no-store. Caching a ref renders a previous commit from valid ciphertext, so nothing errors and the reader silently sees the wrong version.',
    'docs/sgit-for-git-users.html': 'The three differences: no staging area; private clone branch per machine or agent with explicit publishing; the vault key is address + credential + encryption key in one string.',
    'docs/limitations.html':        'Not a secrets manager; no partial commits; no key recovery; the server cannot index or search; beta.',
    'docs/two-branch-model.html':   'Every clone commits to its own private branch; pushing to a shared named branch is a separate, explicit act.',
    'security.html':                'The server sees the vault ID, object sizes and request timing — nothing else. Sizes and timing are an acknowledged side channel.',
    'docs/agents.html':             'sgit write <path> --file <f> --message <m> --push --json is the one-shot agent command; every read path takes --json.',
    'docs/quickstart.html':         'sgit create <name> then commit/push; the vault key is printed once and there is no reset.',
    'docs/installation.html':       'pip install sgit-ai — Python >= 3.11, two runtime dependencies, entry points sgit and sgit-ai.',
    'use-cases/health-regulated.html': 'No HIPAA, ISO 27001, SOC 2 or GDPR finding exists; client-side encryption does not by itself make processing lawful.',
    'deploy/how-this-works.html':   'The ref is checked at most once per 120s freshness window; every other object is content-addressed and cached forever.',
}

LLMS_EXTRA = {
    'skills': ['- [use sgit and vaults](/skills/use_sgit-and-vaults__SKILL.md): the CLI + cross-session persistent state',
               '- [create vault apps](/skills/create-vault-apps__SKILL.md): build an app that lives inside a vault',
               '- [create vault content](/skills/create-vault-content__SKILL.md): author _page.json layouts and vault markdown'],
}


def write_llms(pages):
    out, seen, optional = [LLMS_PREAMBLE], set(), []
    for key, heading in LLMS_SECTIONS:
        rows = []
        for path, title, desc, here, _ in pages:
            if here != key or path in seen:
                continue
            seen.add(path)
            name = title.split(' — ')[0].split(' | ')[0]
            fact = LLMS_FACTS.get(path)
            rows.append(f'- [{name}](/{path[:-5]}.md): {desc}'
                        + (f' **Key fact:** {fact}' if fact else ''))
        rows += LLMS_EXTRA.get(key, [])
        if not rows:
            continue
        if heading == 'Optional':
            optional += rows
        else:
            out.append(f'## {heading}\n' + '\n'.join(rows) + '\n')
    missing = [p for p, *_ in pages if p not in seen]
    if missing:
        raise SystemExit('llms.txt would omit these pages (add their section to LLMS_SECTIONS): '
                         + ', '.join(missing))
    if optional:
        out.append('## Optional\n' + '\n'.join(optional) + '\n')
    text = '\n'.join(out)
    with open(os.path.join(ROOT, 'llms.txt'), 'w') as f:
        f.write(text)
    return text




# ============================================================ crawl + agent surface
# An agent reported that it could fetch llms.txt but could not follow a link out of it —
# its harness only allows URLs a search has already returned, and the site did not rank for
# its own positioning language. Two consequences, both handled here: the site has to be
# crawlable (robots + sitemap, and a page that is not invisible without JS — see CRITICAL),
# and the index has to be useful to an agent that will never follow a link, which means
# self-sufficient answers in llms.txt and a single-fetch concatenation in llms-full.txt.

def write_robots():
    text = f"""# sgit.ai — everything here is public and intended to be indexed.
User-agent: *
Allow: /

Sitemap: https://sgit.ai/sitemap.xml

# For agents and LLMs:
#   https://sgit.ai/llms.txt       annotated map of the site, one line per page
#   https://sgit.ai/llms-full.txt  every page concatenated — one fetch gets everything
# Every page is also available as markdown at the same path with .html swapped for .md.
"""
    with open(os.path.join(ROOT, 'robots.txt'), 'w') as f:
        f.write(text)
    return text


def write_sitemap(pages, today):
    urls = []
    for path, *_ in pages:
        pri = '1.0' if path == 'index.html' else ('0.8' if '/' not in path else '0.6')
        urls.append(f'  <url>\n    <loc>https://sgit.ai/{path}</loc>\n'
                    f'    <lastmod>{today}</lastmod>\n    <priority>{pri}</priority>\n  </url>')
    for extra in ('llms.txt', 'llms-full.txt'):
        urls.append(f'  <url>\n    <loc>https://sgit.ai/{extra}</loc>\n'
                    f'    <lastmod>{today}</lastmod>\n    <priority>0.5</priority>\n  </url>')
    text = ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + '\n'.join(urls) + '\n</urlset>\n')
    with open(os.path.join(ROOT, 'sitemap.xml'), 'w') as f:
        f.write(text)
    return text


def write_llms_full(pages):
    """Every page in one document. For agents whose harness will not follow a link out of a
    fetched file — a common restriction — this is the difference between the documentation
    being reachable and being unreachable."""
    parts = [f"""# sgit.ai — complete documentation, single file

> Every page of https://sgit.ai concatenated into one document, generated at build time
> ({SITE_VERSION}). Nothing here needs a second request. Individual pages live at the paths
> shown below, as markdown (`.md`) and as HTML (`.html`); the annotated map is /llms.txt.
>
> sgit is git for encrypted vaults: clone, commit, branch and merge files that are encrypted
> client-side (AES-256-GCM) before they leave your machine. The server stores ciphertext under
> opaque IDs — it never sees filenames, contents, or commit messages.
"""]
    for path, title, desc, here, body in pages:
        parts.append(f'\n\n{"=" * 78}\n# {title}\n\n> {desc}\n>\n> Page: https://sgit.ai/{path}\n\n'
                     + to_markdown(body))
    text = '\n'.join(parts).rstrip() + '\n'
    with open(os.path.join(ROOT, 'llms-full.txt'), 'w') as f:
        f.write(text)
    return text




# ============================================================ page registry
# Content lives in admin/content/<path>.html — one file per page, holding only the <main>
# body. This file is the engine: template, markdown mirror, llms/robots/sitemap, and the
# registry below. Adding a page is a new content file plus one row here; nothing in this
# file grows with the site.

MANIFEST = os.path.join(ADMIN, 'content', 'pages.json')


def load_pages():
    with open(MANIFEST) as f:
        rows = json.load(f)
    pages = []
    for r in rows:
        if r.get('dynamic') == 'versions':
            body = versions_body()
        elif r.get('dynamic') == 'updates':
            body = updates_body()
        elif r.get('dynamic') == 'articles':
            body = articles_index_body()
        elif r.get('dynamic') == 'network':
            body = network_index_body()
        else:
            with open(os.path.join(ADMIN, 'content', r['path'])) as f:
                body = f.read().rstrip('\n')
            # the homepage articles band is derived, not hand-listed
            if '<!--ARTICLES-->' in body:
                body = body.replace('<!--ARTICLES-->', home_articles_band())
        pages.append((r['path'], r['title'], r['desc'], r['section'], body))
    # One page per article, derived — an article is published by adding its markdown
    # file and nothing else, so it must not need a manifest row either.
    for a in ARTICLES:
        pages.append((f'articles/{a["slug"]}.html',
                      f'{a["title"]} — sgit.ai', a['summary'], 'articles', article_body(a)))
    for x in SITES:
        if x['listing']:
            continue
        pages.append((f'network/{x["slug"]}.html',
                      f'{x["domain"]} — {x["tagline"]} — sgit.ai', x['summary'],
                      'network', site_body(x)))
    return pages


# ============================================================ updates & articles
# Markdown content types. The rule, adopted from the VoiceDebrief journalist pipeline:
# PUBLISHING IS ADDING ONE FILE. The index below, the feed, the manifest and every
# permalink are derived — so two agents publishing on the same day touch two different
# files and cannot conflict. That property is what makes an unattended journalist safe.

LOADER   = Content_Loader(os.path.join(ADMIN, 'content'))
UPDATES  = [u for u in LOADER.load_updates()  if u['status'] == 'published']
ARTICLES = [a for a in LOADER.load_articles() if a['status'] == 'published']
SITES    = [x for x in LOADER.load_sites()    if x['status'] == 'published']


def _chips(tags):
    return ''.join(f'<span class="chip">{t}</span>' for t in tags)


def updates_body():
    """One page, newest first, each post with a #slug permalink. Posts are short by
    design — a release with three stories in it gets three of them, which is the whole
    reason this is not just the version log with a nicer stylesheet."""
    if not UPDATES:
        return '<main class="doc"><h1>Updates</h1><p>Nothing published yet.</p></main>'
    out = ['<main class="doc">',
           '  <h1>Updates</h1>',
           '  <p class="lead">What changed on sgit and on this site, as it happens — one entry per '
           'story rather than per release. The <a href="../admin/versions.html">version log</a> is '
           'the complete technical record; this is the readable one.</p>',
           '  <p class="small dim">Follow along: <a href="feed.xml">RSS</a> &middot; '
           '<a href="updates.json">JSON</a>. Every entry links to the release that carries it.</p>']
    last_date = None
    for u in UPDATES:
        if u['date'] != last_date:
            out.append(f'  <h2 class="upd-date">{u["date"]}</h2>')
            last_date = u['date']
        ver = (f'<a class="upd-ver" href="../admin/versions.html">{u["version"]}</a>'
               if u['version'] else '')
        out.append(f'  <article class="upd" id="{u["slug"]}">')
        out.append(f'    <h3><a href="#{u["slug"]}">{u["title"]}</a> {ver}</h3>')
        if u['tags']:
            out.append(f'    <p class="chips">{_chips(u["tags"])}</p>')
        out.append(LOADER.md_to_html(u['body'], depth=1, where=u['where']))
        out.append('  </article>')
    out.append('</main>')
    return '\n'.join(out)


def home_articles_band():
    """The articles band on the homepage, derived from ARTICLES.

    Articles turned out to be the readable surface over all of this — a reader who will
    not work through a docs tree will read one argued page. So they get a place on the
    homepage, and it is generated rather than hand-listed so a new article appears there
    by being written, which is the same rule as everywhere else here."""
    cards = []
    for a in ARTICLES[:3]:
        cards.append(
            f'    <a class="artcard" href="articles/{a["slug"]}.html">\n'
            f'      <span class="artcard-date">{a["date"]}</span>\n'
            f'      <b>{a["title"]}</b>\n'
            f'      <span class="artcard-sum">{a["summary"]}</span>\n'
            f'      <span class="artcard-go">Read it &rarr;</span>\n'
            f'    </a>')
    return ('<section class="band alt" id="articles">\n'
            '  <h2>Start with an argument, not a menu</h2>\n'
            '  <p class="bandlede">The articles are the readable way in: one page, one argument, '
            'with the screenshots and the links to check it. If you only read one thing here, '
            'read one of these.</p>\n'
            '  <div class="artcards">\n' + '\n'.join(cards) + '\n  </div>\n'
            '  <p class="bandcta"><a class="cta2" href="articles/index.html">All articles &rarr;</a></p>\n'
            '</section>')


def network_chat_block():
    """The 'which of these is mine?' panel, and the catalogue it runs on.

    The catalogue is emitted from SITES — the same data the cards and the table are
    built from — so the answers cannot drift from the directory underneath them. The
    default tier needs no key and no network; see assets/network-chat.js for why."""
    cat = []
    for x in SITES:
        href = f'{x["slug"]}.html' if not x['listing'] else x['url']
        cat.append({
            'domain': x['domain'],
            'thesis': x['thesis'] or x['tagline'],
            'category': x['category'],
            'href': href,
            'external': bool(x['listing']),
            # one lowercase blob per site for the matcher to score against
            'hay': ' '.join([x['domain'].replace('.', ' '), x['thesis'], x['tagline'],
                             x['summary'], x['category'], ' '.join(x['tags']),
                             x['aliases']]),
        })
    egs = ['I have to sign off a risk',
           'my app needs to call an LLM safely',
           'I am drawing a graph',
           'how should I license my open source project']
    btns = ''.join(f'<button type="button" class="nc-eg">{e}</button>' for e in egs)
    return (
        '  <div class="netchat" id="netchat">\n'
        '    <div class="nc-head"><b>Which of these is mine?</b>'
        '<span class="nc-mode">instant match &middot; no key, no network</span></div>\n'
        '    <div class="nc-log"><div class="nc-msg nc-bot"><p>Describe what you are trying to '
        'do and I will point at the site that takes it seriously. This runs in your browser '
        'against the catalogue on this page &mdash; no key needed, nothing sent anywhere.</p>'
        f'<div class="nc-egs">{btns}</div></div></div>\n'
        '    <form class="nc-form">\n'
        '      <input class="nc-input" type="text" autocomplete="off" '
        'placeholder="e.g. I need to give an AI agent an identity">\n'
        '      <button class="nc-send" type="submit">Ask</button>\n'
        '    </form>\n'
        '    <div class="nc-foot">\n'
        '      <button type="button" class="nc-keytoggle">Use my own LLM key</button>\n'
        '      <span class="small dim">Optional. Answers get more conversational; the matching '
        'does not get more correct.</span>\n'
        '    </div>\n'
        '    <div class="nc-keypanel" hidden>\n'
        '      <p class="small"><b>Bring your own key (OpenRouter).</b> It is stored in this '
        'browser only and sent only to <code>openrouter.ai</code> &mdash; never to sgit.ai, which '
        'is a static site with no server to send it to. <b>This page cannot protect it the way a '
        'vault app can</b>: with no host there is no permission floor, so the key lives in this '
        'page\'s origin. <a href="https://llms.sgit.ai" rel="noopener" target="_blank">llms.sgit.ai '
        '&#8599;</a> explains the difference, and <a href="../articles/chat-on-a-static-site.html">'
        'the plan</a> explains how we intend to remove the trade-off.</p>\n'
        '      <div class="nc-keyrow">\n'
        '        <input class="nc-key" type="password" autocomplete="off" placeholder="sk-or-v1-...">\n'
        '        <button type="button" class="nc-keysave">Save in this browser</button>\n'
        '      </div>\n'
        '    </div>\n'
        '  </div>\n'
        f'  <script>window.__SGIT_SITES__ = {json.dumps(cat, ensure_ascii=False)};</script>\n'
        # Fetched and evaluated rather than <script src>: these pages also render inside a
        # vault, on a blob: origin where a relative script src does not resolve. The
        # validator enforces this — see the contract check.
        '  <script>\n'
        '  fetch("../assets/network-chat.js")\n'
        '    .then(function (r) { if (!r.ok) throw new Error(r.status); return r.text(); })\n'
        '    .then(function (t) { (0, eval)(t); })\n'
        '    .catch(function (e) { console.error("[network] chat failed to load:", e); });\n'
        '  </script>'
    )


def network_index_body():
    """The sibling *.sgit.ai sites — a directory, not a list.

    This started at two entries and is now nineteen, which changes what the page is
    for: a reader arriving here does not want to read nineteen reviews, they want to
    be sent to the one that answers their question. So the page leads with questions,
    groups by what a site is *about*, and keeps the full table underneath for scanning.
    Everything below is derived from admin/content/sites/*.md."""
    live    = [x for x in SITES if _site_live(x)]
    pending = [x for x in SITES if not _site_live(x)]
    deep    = [x for x in SITES if not x['listing']]

    out = ['<main class="doc">',
           '  <h1>The sgit.ai network</h1>',
           '  <p class="lead">Nineteen focused sites on <code>*.sgit.ai</code>, each taking one '
           'question further than a section here could. They share this site\'s design and its '
           'discipline — sourced claims, a stated status, honest edges — and they publish their '
           'arguments <b>before</b> the things they describe exist, so the commitments stay '
           'checkable afterwards.</p>',
           f'  <p class="small dim">{len(live)} live, {len(pending)} with the repository and '
           'subdomain in place but nothing published yet. Screenshots are of the real sites, '
           'captured on the date each entry gives.</p>']

    out.append(network_chat_block())

    # ---- the chooser. The point of the page: a question, and where it is answered.
    out += ['  <h2 id="start">Start from what you need</h2>',
            '  <p>Each line is a question somebody actually arrives with, and the site that '
            'takes it seriously.</p>',
            '  <div class="chooser">']
    for q, dom, why in ASK:
        site = next((x for x in SITES if x['domain'] == dom), None)
        if not site:
            continue
        href = f'{site["slug"]}.html' if not site['listing'] else site['url']
        ext  = '' if not site['listing'] else ' rel="noopener" target="_blank"'
        arrow = '' if not site['listing'] else ' &#8599;'
        out.append(f'    <a class="ask" href="{href}"{ext}>'
                   f'<span class="ask-q">{q}</span>'
                   f'<span class="ask-a"><b>{dom}</b>{arrow} &middot; {why}</span></a>')
    out.append('  </div>')

    # ---- grouped cards
    order = ['Agents & AI', 'Risk & governance', 'Graphs & method',
             'Security & infrastructure', 'Business & publishing', 'Other']
    for cat in order:
        group = [x for x in SITES if x['category'] == cat]
        if not group:
            continue
        out.append(f'  <h2 id="{re.sub(chr(92) + "W+", "-", cat.lower()).strip("-")}">{cat}</h2>')
        out.append('  <div class="netlist">')
        for x in sorted(group, key=lambda y: (not _site_live(y), y['domain'])):
            shot = (f'<figure class="shot net-shot" data-shot="{x["hero"]}" data-dir="images/" '
                    f'data-alt="{x["title"]}"></figure>') if x['hero'] else ''
            stage = f'<span class="chip">{x["stage"]}</span>' if x['stage'] else ''
            ver   = f'<span class="chip">{x["seen_version"]}</span>' if x['seen_version'] else ''
            body  = (f'<a class="net-main" href="{x["slug"]}.html">' if not x['listing']
                     else f'<a class="net-main" href="{x["url"]}" rel="noopener" target="_blank">')
            thesis = x['thesis'] or x['tagline']
            deeplink = (f' <a href="{x["slug"]}.html">What it argues &rarr;</a> &middot;'
                        if not x['listing'] else '')
            openlink = (f'<a href="{x["url"]}" rel="noopener" target="_blank">'
                        f'Open {_site_host(x)} &#8599;</a>' if _site_live(x)
                        else '<span class="dim">not published yet</span> &middot; '
                             f'<a href="{x["url"]}" rel="noopener" target="_blank">repo &#8599;</a>')
            out.append(
                f'    <div class="netcard">\n'
                f'      {body}\n'
                f'        <b>{x["domain"]}</b>\n'
                f'        <span class="net-tag">{thesis}</span>\n'
                f'        <span class="net-sum">{x["summary"]}</span>\n'
                f'      </a>\n'
                f'      {shot}\n'
                f'      <p class="small dim">{stage}{ver}{deeplink} {openlink}</p>\n'
                f'    </div>')
        out.append('  </div>')

    # ---- the whole family, scannable
    out += ['  <h2 id="all">Every site, at a glance</h2>',
            '  <div class="tablewrap"><table>',
            '    <tr><th>Site</th><th>What it argues</th><th>Area</th><th>Status</th><th></th></tr>']
    for x in sorted(SITES, key=lambda y: (not _site_live(y), y['domain'])):
        st = x['stage'] or ('live' if _site_live(x) else 'not published yet')
        v  = f' &middot; <code>{x["seen_version"]}</code>' if x['seen_version'] else ''
        link = (f'<a href="{x["url"]}" rel="noopener" target="_blank">open &#8599;</a>'
                if _site_live(x) else
                f'<a href="{x["url"]}" rel="noopener" target="_blank">repo &#8599;</a>')
        name = (f'<a href="{x["slug"]}.html">{x["domain"]}</a>' if not x['listing']
                else f'<b>{x["domain"]}</b>')
        out.append(f'    <tr><td>{name}</td><td>{x["thesis"] or x["tagline"]}</td>'
                   f'<td class="small">{x["category"]}</td><td class="small">{st}{v}</td>'
                   f'<td>{link}</td></tr>')
    out += ['  </table></div>']

    out += [f'  <h2>Read one in full</h2>',
            '  <p>Four have a full write-up here — what the site argues, where it is honest '
            'about its limits, and why it is relevant to sgit:</p>',
            '  <ul>'] + [
            f'    <li><a href="{x["slug"]}.html"><b>{x["domain"]}</b></a> — {x["tagline"]}</li>'
            for x in sorted(deep, key=lambda y: y['domain'])] + ['  </ul>']

    out += ['  <h2>Why they are separate sites</h2>',
            '  <p>Each one is an argument that needs room and a reader who arrived for it. '
            'Splitting them out keeps this site about sgit while letting each question be '
            'pursued properly — and gives each its own version history, release cadence and '
            'repository. They are built from the same generator and hold to the same rules, so '
            'a reader moving between them is not changing register.</p>',
            '  <p class="small dim">This is also the refactor it looks like: material that '
            'would have made sgit.ai sprawl now has a better home, and this page is the index '
            'back into it. Adding the twentieth site is writing one markdown file.</p>',
            '</main>']
    return '\n'.join(out)


def _site_host(x):
    return x['url'].split('://', 1)[-1].rstrip('/')


def _site_live(x):
    """True once the site answers on its own subdomain."""
    return x['url'].rstrip('/') == f'https://{x["domain"]}'


def site_body(x):
    ver = f' &middot; <code>{x["seen_version"]}</code> when captured' if x['seen_version'] else ''
    repo = (f' &middot; <a href="https://github.com/SGit-AI/{x["repo"]}" rel="noopener" '
            f'target="_blank">{x["repo"]} &#8599;</a>') if x['repo'] else ''
    # A site can be finished before its subdomain resolves. Say which address works
    # rather than shipping a link that fails, and keep the intended one visible so the
    # entry does not need rewriting when DNS lands.
    pending = ('' if _site_live(x) else
               f'  <div class="note"><b><code>{x["domain"]}</code> does not resolve yet.</b> '
               f'The site is live and complete at its origin, linked below; the subdomain is '
               f'being pointed at it. Everything on this page was read there.</div>\n')
    return ('<main class="doc">\n'
            f'  <p class="crumb"><a href="../index.html">Home</a> / '
            f'<a href="index.html">Network</a> / {x["domain"]}</p>\n'
            f'  <h1>{x["domain"]}</h1>\n'
            f'  <p class="lead">{x["tagline"]}</p>\n'
            f'  <p class="small dim">Screenshots captured {x["observed"]}{ver}{repo}</p>\n'
            + pending +
            f'  <p><a class="btn" href="{x["url"]}" rel="noopener" target="_blank">'
            f'Open {_site_host(x)} &#8599;</a></p>\n'
            + LOADER.md_to_html(x['body'], depth=1, where=x['where'])
            + '\n  <p class="small dim" style="margin-top:2rem">'
              '<a href="index.html">&larr; All network sites</a></p>\n'
            '</main>')


def articles_index_body():
    out = ['<main class="doc">',
           '  <h1>Articles</h1>',
           '  <p class="lead">Longer pieces that make an argument across several pages — what a '
           'thing means, why it is shaped that way, and what it cost to find out. Shorter, dated '
           'notes on individual changes are in <a href="../updates/index.html">updates</a>.</p>',
           '  <div class="note"><b>Two rules keep these from going stale.</b> An article never '
           'restates a fact it does not own — it links to the page that does, so when the fact '
           'changes the article does not start lying. And an article that makes a testable claim '
           'links to the test, the same way <a href="../compare/index.html">the comparison '
           'pages</a> do.</div>',
           '  <div class="artlist">']
    for a in ARTICLES:
        out.append(f'    <a class="art" href="{a["slug"]}.html">'
                   f'<b>{a["title"]}</b>'
                   f'<span class="art-date">{a["date"]}</span>'
                   f'<span class="art-sum">{a["summary"]}</span>'
                   + (f'<span class="chips">{_chips(a["tags"])}</span>' if a['tags'] else '')
                   + '</a>')
    out.append('  </div>')
    out.append('</main>')
    return '\n'.join(out)


def article_body(a):
    ver = (f' &middot; <a href="../admin/versions.html">{a["version"]}</a>' if a['version'] else '')
    return ('<main class="doc">\n'
            f'  <p class="crumb"><a href="../index.html">Home</a> / '
            f'<a href="index.html">Articles</a> / {a["title"]}</p>\n'
            f'  <h1>{a["title"]}</h1>\n'
            f'  <p class="small dim">{a["date"]}{ver}'
            + (f' &middot; {_chips(a["tags"])}' if a['tags'] else '') + '</p>\n'
            f'  <p class="lead">{a["summary"]}</p>\n'
            + LOADER.md_to_html(a['body'], depth=1, where=a['where'])
            + '\n  <p class="small dim" style="margin-top:2rem">'
              '<a href="index.html">&larr; All articles</a></p>\n'
            '</main>')


PAGES = load_pages()

md_total = 0
for path, title, desc, here, body in PAGES:
    page(path, title, desc, here, body)
    md_total += write_md(path, title, desc, body)
print(f'wrote {len(PAGES)} markdown mirrors ({md_total} bytes)')
print('wrote llms.txt (%d bytes)' % len(write_llms(PAGES)))
print('wrote llms-full.txt (%d bytes)' % len(write_llms_full(PAGES)))
print('wrote robots.txt (%d bytes)' % len(write_robots()))
print('wrote sitemap.xml (%d bytes)' % len(write_sitemap(PAGES, BUILD_DATE)))

# The feed and the manifest: derived, never hand-edited — the same rule as the index.
os.makedirs(os.path.join(ROOT, 'updates'), exist_ok=True)
with open(os.path.join(ROOT, 'updates', 'feed.xml'), 'w') as f:
    feed = LOADER.render_feed(UPDATES); f.write(feed)
print(f'wrote updates/feed.xml ({len(feed)} bytes, {min(len(UPDATES), 20)} items)')
manifest = json.dumps({
    'site': 'https://sgit.ai', 'generated': BUILD_DATE, 'site_version': SITE_VERSION,
    'updates':  [{k: u[k] for k in ('slug', 'title', 'date', 'version', 'tags', 'summary')}
                 for u in UPDATES],
    'articles': [{k: a[k] for k in ('slug', 'title', 'date', 'version', 'tags', 'summary')}
                 for a in ARTICLES],
}, indent=2, ensure_ascii=False)
with open(os.path.join(ROOT, 'updates', 'updates.json'), 'w') as f:
    f.write(manifest)
print(f'wrote updates/updates.json ({len(manifest)} bytes)')
print(f'content: {len(UPDATES)} updates, {len(ARTICLES)} articles')
print('done:', len(PAGES), 'pages —', SITE_VERSION)
