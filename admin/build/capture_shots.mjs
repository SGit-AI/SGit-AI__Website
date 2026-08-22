/* capture_shots.mjs — drive a published vault in a real browser and save cropped
   screenshots for the site's walkthrough rows.

   Why this exists: the walkthrough explains things a new reader cannot infer from a
   live embed alone (that clicking a photo opens a carousel; that the app ships a
   debug pane with a REPL; that the source is readable in the browser). Each claim
   needs a picture of the actual product, not a mock-up — so this drives the real
   UI with only a PUBLISHED READ KEY, performs the navigation, and crops the result.

   Read-only by construction: every shot opens with a read key. No vault key is ever
   passed to this tool.

     node admin/build/capture_shots.mjs [--mirror] [--vault <slug>] [--only <name>]

   --mirror routes *.sgraph.ai through a local curl-backed proxy on :8898 (needed in
   sandboxes whose browser cannot egress; omit it on a normal machine).

   Selectors are documented where they are non-obvious — the HUD and the debug pane
   live in shadow DOM, and the app itself runs in a nested frame. */
import { chromium } from 'playwright';
import sharp from 'sharp';
import fs from 'fs';
import path from 'path';

const ROOT     = path.resolve(path.dirname(new URL(import.meta.url).pathname), '../..');
// One folder per vault, images inside it: demos/vaults/<slug>/images/<name>.webp —
// so a vault's page and its pictures are a single self-contained unit.
const outDir   = slug => path.join(ROOT, 'demos/vaults', slug, 'images');
const ORIGIN   = 'https://dev.vault.sgraph.ai';
const MIRROR   = process.argv.includes('--mirror');
const ONLY     = process.argv.includes('--only') ? process.argv[process.argv.indexOf('--only') + 1] : null;
const VAULT    = process.argv.includes('--vault') ? process.argv[process.argv.indexOf('--vault') + 1] : null;
const HOSTS    = new Set(['dev.vault.sgraph.ai', 'dev.send.sgraph.ai', 'dev.sgraph.ai', 'dev.tools.sgraph.ai']);

// The Algarve gallery vault — read key published on /vaults/algarve-photos.html.
const ALGARVE = 'sgit_rk1_0a0f34839d737eef0f8f66e5236990b1f397af064763e3f71dca2717015f9d15:3d04e6b9ca98';

const RISK = 'sgit_rk1_a702fba803faac4369eb5d5a320b4dfa017af62bd2425fb298aac4b99e95c0ae:4zf6pf2z';

const RISKGRAPH = 'sgit_rk1_92cad4cea8f58c55f59b686c71c935225a1ba7c41ecb6922a8aa570467604f6e:0610gsp9';

const EXPLORER = 'sgit_rk1_1c1b95f5903e35850a9bc0541ffa09c6b5d4017cbf18817d2ad6f894127e5638:3simlnqe';

const REGGRAPH = 'sgit_rk1_c004daae386e8d17fa648884acc527018bd4ea1116ad673fb2f1b068011695c9:73heuprz';

const SUPPLEMENT = 'sgit_rk1_047186b559528058c66d1792b7345639b1238cb95c166d1d5f5b65c59813c2ee:r7zes477';

const VOICEDEBRIEF = 'sgit_rk1_31e8196d3e83b37277083c29f105b8310dbac4569e22715b5e0f85d46878eec1:k6xy9z4d';

/* Each shot: which surface to open, what to do, and what to crop.
   target: 'app'   → an element inside the vault app's own frame
           'page'  → an element (or shadow path) on the SG/App or SG/Vault page
           'clip'  → an explicit viewport rectangle */
const SHOTS = [
  { name: 'gallery-row', vault: 'algarve-may-2026', cred: ALGARVE, surface: 'app', viewport: [1600, 1000],
    steps: [{ appScroll: '.grid-row' }, { wait: 1200 }],
    target: 'app', sel: '.grid-row' },

  { name: 'lightbox', vault: 'algarve-may-2026', cred: ALGARVE, surface: 'app', viewport: [1600, 1000],
    // Clicking a figure opens the app's own lightbox: .lb with prev/next and a caption.
    steps: [{ appClick: '.grid-row figure' }, { wait: 1800 }],
    target: 'clip', clip: [0, 0, 1600, 1000] },

  { name: 'hud-vault', vault: 'algarve-may-2026', cred: ALGARVE, surface: 'app', viewport: [1800, 1000],
    // The HUD's "more" menu is hidden in minimal mode, but its debug button still
    // works when clicked through the shadow root — that is how the pane opens.
    steps: [{ shadowClick: ['app-hud', '.hud-debug-btn'] }, { wait: 3000 }],
    target: 'page', shadowSel: ['app-debug-pane'], trim: 0.42 },

  { name: 'hud-repl', vault: 'algarve-may-2026', cred: ALGARVE, surface: 'app', viewport: [1800, 1000],
    steps: [{ shadowClick: ['app-hud', '.hud-debug-btn'] }, { wait: 2500 },
            { shadowClickText: ['app-debug-pane', '.dp-tab', 'REPL'] }, { wait: 1200 },
            { replType: ['vfs.list', 'vfs.list /photos'] }, { wait: 1500 }],
    target: 'page', shadowSel: ['app-debug-pane'], trim: 0.46 },

  { name: 'source-view', vault: 'algarve-may-2026', cred: ALGARVE, surface: 'vault', viewport: [1700, 1000],
    // The vault browser: expand photos/originals, then open index.html as source.
    steps: [{ wait: 2500 }, { clickText: ['.sb-tree__folder-name', 'photos'] }, { wait: 1500 },
            { clickText: ['.sb-tree__folder-name', 'originals'] }, { wait: 1500 },
            { clickText: ['.sb-action-btn', 'Source'] }, { wait: 2500 }],
    target: 'clip', clip: [0, 0, 1700, 1000] },

  { name: 'sgit-history', vault: 'algarve-may-2026', cred: ALGARVE, surface: 'vault', viewport: [1700, 1000],
    steps: [{ wait: 1500 }, { navView: 'sgit' }, { wait: 3500 }],
    target: 'clip', clip: [0, 0, 1700, 1000] },

  // ---- Supplement Stack (r7zes477) — the patient-held record ----
  { name: 'today', vault: 'supplement-stack', cred: SUPPLEMENT, surface: 'app', viewport: [1500, 1000],
    steps: [{ appClickText: ['button', 'Today'], frameHas: '#p-today' }, { wait: 1500 }],
    target: 'app', sel: '#p-today' },

  { name: 'stack', vault: 'supplement-stack', cred: SUPPLEMENT, surface: 'app', viewport: [1500, 1100],
    steps: [{ appClickText: ['button', 'Stack'], frameHas: '#p-stack' }, { wait: 2500 }],
    target: 'app', sel: '#p-stack', trim: 0.5 },

  { name: 'totals', vault: 'supplement-stack', cred: SUPPLEMENT, surface: 'app', viewport: [1500, 1100],
    steps: [{ appClickText: ['button', 'Totals'], frameHas: '#p-totals' }, { wait: 2000 }],
    target: 'app', sel: '#p-totals', trim: 0.55 },

  { name: 'briefing', vault: 'supplement-stack', cred: SUPPLEMENT, surface: 'app', viewport: [1500, 1100],
    steps: [{ appClickText: ['button', 'Briefing'], frameHas: '#p-briefing' }, { wait: 2000 }],
    target: 'app', sel: '#p-briefing', trim: 0.6 },

  // ---- Risk Mandate (4zf6pf2z) — a software project built inside a vault ----
  { name: 'app-open', vault: 'risk-mandate', cred: RISK, surface: 'app', viewport: [1500, 1000],
    steps: [{ wait: 4000 }],
    target: 'clip', clip: [0, 0, 1500, 1000] },

  // The whole privilege claim in one file: LLM use granted, key never granted,
  // and write scoped to one workspace folder.
  { name: 'permissions', vault: 'risk-mandate', cred: RISK, surface: 'vault', viewport: [1700, 1000],
    steps: [{ wait: 2500 }, { clickText: ['.sb-tree__file-name', 'app.json'] }, { wait: 2500 }],
    target: 'clip', clip: [0, 0, 1700, 820] },

  { name: 'history', vault: 'risk-mandate', cred: RISK, surface: 'vault', viewport: [1700, 1000],
    steps: [{ wait: 2000 }, { navView: 'sgit' }, { wait: 4000 }],
    target: 'clip', clip: [0, 0, 1700, 1000] },

  // ---- Agentic Browser Isolation (0610gsp9) — a living risk graph ----
  { name: 'app-open', vault: 'agentic-browser-isolation', cred: RISKGRAPH, surface: 'app', viewport: [1500, 1050],
    steps: [{ wait: 5000 }],
    target: 'clip', clip: [0, 0, 1500, 1050] },

  { name: 'stakeholders', vault: 'agentic-browser-isolation', cred: RISKGRAPH, surface: 'app', viewport: [1500, 1050],
    steps: [{ wait: 4000 }, { appClickLink: 'people.html' }, { wait: 5000 }],
    target: 'clip', clip: [0, 0, 1500, 1050] },

  { name: 'graph', vault: 'agentic-browser-isolation', cred: RISKGRAPH, surface: 'app', viewport: [1500, 1050],
    steps: [{ wait: 4000 }, { appClickLink: 'graphviz.html' }, { wait: 6000 }],
    target: 'clip', clip: [0, 0, 1500, 1050] },

  { name: 'permissions', vault: 'agentic-browser-isolation', cred: RISKGRAPH, surface: 'vault', viewport: [1700, 1000],
    steps: [{ wait: 2500 }, { clickText: ['.sb-tree__file-name', 'app.json'] }, { wait: 2500 }],
    target: 'clip', clip: [0, 0, 1700, 780] },

  // ---- Risk graph explorer (3simlnqe) — public by design ----
  // The two states are the app's argument: nothing at stake -> a short register.
  { name: 'empty', vault: 'risk-graph-explorer', cred: EXPLORER, surface: 'app', viewport: [1500, 1050],
    steps: [{ wait: 5000 }],
    target: 'clip', clip: [0, 0, 1500, 1050] },

  { name: 'exposed', vault: 'risk-graph-explorer', cred: EXPLORER, surface: 'app', viewport: [1500, 1050],
    steps: [{ wait: 4500 }, { appClickText: ['button', 'Exposed'] }, { wait: 4000 }],
    target: 'clip', clip: [0, 0, 1500, 1050] },

  // Its own publication rules, written in the vault and enforced by its build.
  { name: 'public-md', vault: 'risk-graph-explorer', cred: EXPLORER, surface: 'vault', viewport: [1700, 1000],
    steps: [{ wait: 2500 }, { clickText: ['.sb-tree__file-name', 'PUBLIC.md'] }, { wait: 3000 }],
    target: 'clip', clip: [0, 0, 1700, 1000] },

  { name: 'permissions', vault: 'risk-graph-explorer', cred: EXPLORER, surface: 'vault', viewport: [1700, 1000],
    steps: [{ wait: 2500 }, { clickText: ['.sb-tree__file-name', 'app.json'] }, { wait: 2500 }],
    target: 'clip', clip: [0, 0, 1700, 760] },


  // ---- Risk graph explorer: the seven views, under the Exposed preset ----
  // Each is the same answers seen from a different altitude — which is the point.
  { name: 'view-estate', vault: 'risk-graph-explorer', cred: EXPLORER, surface: 'app', viewport: [1600, 1080],
    steps: [{ wait: 4500 }, { appClickText: ['button', 'Exposed'] }, { wait: 3000 },
            { appClickText: ['button.tab', 'The estate'] }, { wait: 3000 }],
    target: 'clip', clip: [0, 0, 1600, 1080] },
  { name: 'view-context', vault: 'risk-graph-explorer', cred: EXPLORER, surface: 'app', viewport: [1600, 1080],
    steps: [{ wait: 4500 }, { appClickText: ['button', 'Exposed'] }, { wait: 3000 },
            { appClickText: ['button.tab', 'Context'] }, { wait: 3000 }],
    target: 'clip', clip: [0, 0, 1600, 1080] },
  { name: 'view-role-risk-map', vault: 'risk-graph-explorer', cred: EXPLORER, surface: 'app', viewport: [1600, 1080],
    steps: [{ wait: 4500 }, { appClickText: ['button', 'Exposed'] }, { wait: 3000 },
            { appClickText: ['button.tab', 'Role risk map'] }, { wait: 3000 }],
    target: 'clip', clip: [0, 0, 1600, 1080] },
  { name: 'view-risk-chains', vault: 'risk-graph-explorer', cred: EXPLORER, surface: 'app', viewport: [1600, 1080],
    steps: [{ wait: 4500 }, { appClickText: ['button', 'Exposed'] }, { wait: 3000 },
            { appClickText: ['button.tab', 'Risk chains'] }, { wait: 3000 }],
    target: 'clip', clip: [0, 0, 1600, 1080] },
  { name: 'view-register', vault: 'risk-graph-explorer', cred: EXPLORER, surface: 'app', viewport: [1600, 1080],
    steps: [{ wait: 4500 }, { appClickText: ['button', 'Exposed'] }, { wait: 3000 },
            { appClickText: ['button.tab', 'The register'] }, { wait: 3000 }],
    target: 'clip', clip: [0, 0, 1600, 1080] },
  { name: 'view-acceptance', vault: 'risk-graph-explorer', cred: EXPLORER, surface: 'app', viewport: [1600, 1080],
    steps: [{ wait: 4500 }, { appClickText: ['button', 'Exposed'] }, { wait: 3000 },
            { appClickText: ['button.tab', 'Acceptance'] }, { wait: 3000 }],
    target: 'clip', clip: [0, 0, 1600, 1080] },
  { name: 'view-what-next', vault: 'risk-graph-explorer', cred: EXPLORER, surface: 'app', viewport: [1600, 1080],
    steps: [{ wait: 4500 }, { appClickText: ['button', 'Exposed'] }, { wait: 3000 },
            { appClickText: ['button.tab', 'What happens next'] }, { wait: 3000 }],
    target: 'clip', clip: [0, 0, 1600, 1080] },
  { name: 'role-map-typical', vault: 'risk-graph-explorer', cred: EXPLORER, surface: 'app', viewport: [1600, 1080],
    steps: [{ wait: 4500 }, { appClickText: ['button', 'Typical'] }, { wait: 3000 },
            { appClickText: ['button.tab', 'Role risk map'] }, { wait: 3000 }],
    target: 'clip', clip: [0, 0, 1600, 1080] },

  { name: 'role-map-governed', vault: 'risk-graph-explorer', cred: EXPLORER, surface: 'app', viewport: [1600, 1080],
    steps: [{ wait: 4500 }, { appClickText: ['button', 'Governed'] }, { wait: 3000 },
            { appClickText: ['button.tab', 'Role risk map'] }, { wait: 3000 }],
    target: 'clip', clip: [0, 0, 1600, 1080] },

  // ---- walkthrough moments: the states the author narrates in the videos ----
  // Node shapes were found with appProbe rather than guessed: chain entries are
  // g.cnode (.inh inherent, .corp corporate register), roles are g.role (.board),
  // estate twins are g.tw (.stake at stake, .ghost nobody has said).

  // "if you look at this guy here, for example, you have risk 6" — the exact node the
  // Risk Chains walkthrough names, selected so its upstream and downstream colour.
  { name: 'chain-r6', vault: 'risk-graph-explorer', cred: EXPLORER, surface: 'app', viewport: [1600, 1080],
    steps: [{ wait: 4500 }, { appClickText: ['button', 'Exposed'] }, { wait: 3000 },
            { appClickText: ['button.tab', 'Risk chains'] }, { wait: 3500 },
            { appClickMatch: ['g.cnode', 'R6 '] }, { wait: 2500 }],
    target: 'clip', clip: [0, 0, 1600, 1080] },

  // "this particular risk, corporate 2, who is assigned to, and then to the CEO" —
  // the top of the chain, interrogated backwards.
  { name: 'chain-corp2', vault: 'risk-graph-explorer', cred: EXPLORER, surface: 'app', viewport: [1600, 1080],
    steps: [{ wait: 4500 }, { appClickText: ['button', 'Exposed'] }, { wait: 3000 },
            { appClickText: ['button.tab', 'Risk chains'] }, { wait: 3500 },
            { appClickMatch: ['g.cnode.corp', 'CORP-2'] }, { wait: 2500 }],
    target: 'clip', clip: [0, 0, 1600, 1080] },

  // "if you have the govern, we can see it's a much cleaner sort of flow of events."
  { name: 'chain-governed', vault: 'risk-graph-explorer', cred: EXPLORER, surface: 'app', viewport: [1600, 1080],
    steps: [{ wait: 4500 }, { appClickText: ['button', 'Governed'] }, { wait: 3000 },
            { appClickText: ['button.tab', 'Risk chains'] }, { wait: 3500 }],
    target: 'clip', clip: [0, 0, 1600, 1080] },

  // "if you have no agent, you have nothing" — the org chart before any answer.
  { name: 'role-map-new', vault: 'risk-graph-explorer', cred: EXPLORER, surface: 'app', viewport: [1600, 1080],
    steps: [{ wait: 4500 }, { appClickText: ['button', 'New'] }, { wait: 3000 },
            { appClickText: ['button.tab', 'Role risk map'] }, { wait: 3500 }],
    target: 'clip', clip: [0, 0, 1600, 1080] },

  // "the CTO has a couple risks of itself but also inherits all the risks below" —
  // the clearest instance of assigned versus through.
  { name: 'role-cto', vault: 'risk-graph-explorer', cred: EXPLORER, surface: 'app', viewport: [1600, 1080],
    steps: [{ wait: 4500 }, { appClickText: ['button', 'Exposed'] }, { wait: 3000 },
            { appClickText: ['button.tab', 'Role risk map'] }, { wait: 3500 },
            { appClickMatch: ['g.role', 'CTO'] }, { wait: 2500 }],
    target: 'clip', clip: [0, 0, 1600, 1080] },

  // "the SRE is holding risk 2, risk 6, risk 9, risk 21, and risk 31" — the bottom of
  // the same chain, where the risks the CTO inherits are actually held.
  { name: 'role-sre', vault: 'risk-graph-explorer', cred: EXPLORER, surface: 'app', viewport: [1600, 1080],
    steps: [{ wait: 4500 }, { appClickText: ['button', 'Exposed'] }, { wait: 3000 },
            { appClickText: ['button.tab', 'Role risk map'] }, { wait: 3500 },
            { appClickMatch: ['g.role', 'SRE'] }, { wait: 2500 }],
    target: 'clip', clip: [0, 0, 1600, 1080] },

  // ---- Regulation Graph (73heuprz) — the EU AI Act as an evidence layer ----
  // app.json's entry is lab/index.html, so opening the vault lands in the Art 9 lab,
  // which is deliberately its own area with no main nav. Everything else is reached
  // through the lab's `a.home` back-link ("← Regulation Graph") — found by probing the
  // running app rather than guessed, after browse.html was not linked from the entry.
  { name: 'app-open', vault: 'regulation-graph', cred: REGGRAPH, surface: 'app', viewport: [1500, 1050],
    steps: [{ wait: 6000 }],
    target: 'clip', clip: [0, 0, 1500, 1050] },

  { name: 'overview', vault: 'regulation-graph', cred: REGGRAPH, surface: 'app', viewport: [1500, 1050],
    steps: [{ wait: 6000 }, { appClickMatch: ['a.home', 'Regulation Graph'] }, { wait: 7000 }],
    target: 'clip', clip: [0, 0, 1500, 1050] },

  { name: 'browse', vault: 'regulation-graph', cred: REGGRAPH, surface: 'app', viewport: [1500, 1050],
    steps: [{ wait: 6000 }, { appClickMatch: ['a.home', 'Regulation Graph'] }, { wait: 6000 },
            { appClickLink: 'browse.html' }, { wait: 7000 }],
    target: 'clip', clip: [0, 0, 1500, 1050] },

  { name: 'graphviz', vault: 'regulation-graph', cred: REGGRAPH, surface: 'app', viewport: [1500, 1050],
    steps: [{ wait: 6000 }, { appClickMatch: ['a.home', 'Regulation Graph'] }, { wait: 6000 },
            { appClickLink: 'graphviz.html' }, { wait: 9000 }],
    target: 'clip', clip: [0, 0, 1500, 1050] },

  // Its publication rules, in the vault itself rather than asserted on our page.
  { name: 'public-md', vault: 'regulation-graph', cred: REGGRAPH, surface: 'vault', viewport: [1700, 1000],
    steps: [{ wait: 3000 }, { clickText: ['.sb-tree__file-name', 'PUBLIC.md'] }, { wait: 3500 }],
    target: 'clip', clip: [0, 0, 1700, 1000] },

  // The scoped-write claim, shown in the vault's own app.json rather than asserted.
  { name: 'permissions', vault: 'supplement-stack', cred: SUPPLEMENT, surface: 'vault', viewport: [1700, 1000],
    steps: [{ wait: 2500 }, { clickText: ['.sb-tree__file-name', 'app.json'] }, { wait: 2500 }],
    target: 'clip', clip: [0, 0, 1700, 760] },

  // ---- VoiceDebrief · Fractal Semantic Graphs (k6xy9z4d) ----
  // Seven views over one legal paragraph. The tabs are `div.tab` whose textContent is
  // exactly the label (read from part-4/app/app.js), so appClickText matches exactly.
  { name: 'app-open', vault: 'voice-debrief', cred: VOICEDEBRIEF, surface: 'app', viewport: [1500, 1050],
    steps: [{ wait: 5000 }],
    target: 'clip', clip: [0, 0, 1500, 1050] },

  // The annotation layers, where the finding is an absence: the actors layer is empty
  // because no duty-holder appears anywhere in Article 9(2).
  { name: 'paragraph', vault: 'voice-debrief', cred: VOICEDEBRIEF, surface: 'app', viewport: [1500, 1050],
    steps: [{ wait: 4500 }, { appClickText: ['div.tab', 'The paragraph'] }, { wait: 2500 }],
    target: 'clip', clip: [0, 0, 1500, 1050] },

  // Compression that stays lossless while the links hold: intent → five words →
  // sentence → paragraph → notation → text.
  { name: 'altitudes', vault: 'voice-debrief', cred: VOICEDEBRIEF, surface: 'app', viewport: [1500, 1050],
    steps: [{ wait: 4500 }, { appClickText: ['div.tab', 'Altitudes'] }, { wait: 2500 }],
    target: 'clip', clip: [0, 0, 1500, 1050] },

  { name: 'concepts', vault: 'voice-debrief', cred: VOICEDEBRIEF, surface: 'app', viewport: [1500, 1050],
    steps: [{ wait: 4500 }, { appClickText: ['div.tab', 'Concepts'] }, { wait: 3000 }],
    target: 'clip', clip: [0, 0, 1500, 1050] },

  { name: 'grammar', vault: 'voice-debrief', cred: VOICEDEBRIEF, surface: 'app', viewport: [1500, 1050],
    steps: [{ wait: 4500 }, { appClickText: ['div.tab', 'Grammar'] }, { wait: 3000 }],
    target: 'clip', clip: [0, 0, 1500, 1050] },

  { name: 'bow-tie', vault: 'voice-debrief', cred: VOICEDEBRIEF, surface: 'app', viewport: [1500, 1050],
    steps: [{ wait: 4500 }, { appClickText: ['div.tab', 'Bow-tie'] }, { wait: 3000 }],
    target: 'clip', clip: [0, 0, 1500, 1050] },

  // The join: a cyber scenario whose obligations attach at the same nodes.
  { name: 'cyber-instance', vault: 'voice-debrief', cred: VOICEDEBRIEF, surface: 'app', viewport: [1500, 1050],
    steps: [{ wait: 4500 }, { appClickText: ['div.tab', 'Cyber instance'] }, { wait: 3000 }],
    target: 'clip', clip: [0, 0, 1500, 1050] },

  // Least privilege in the vault's own manifest: the app declares read on part-4/
  // only, and requests no write anywhere.
  { name: 'permissions', vault: 'voice-debrief', cred: VOICEDEBRIEF, surface: 'vault', viewport: [1700, 1000],
    steps: [{ wait: 2500 }, { clickText: ['.sb-tree__file-name', 'app.json'] }, { wait: 2500 }],
    target: 'clip', clip: [0, 0, 1700, 760] },

  // The reference layer that makes the vault a record rather than a demo: the packs
  // it was built against, kept beside the work.
  { name: 'tree', vault: 'voice-debrief', cred: VOICEDEBRIEF, surface: 'vault', viewport: [1700, 1000],
    steps: [{ wait: 3000 }, { clickText: ['.sb-tree__folder-name', 'briefings'] }, { wait: 2000 }],
    target: 'clip', clip: [0, 0, 1700, 1000] },

  { name: 'history', vault: 'voice-debrief', cred: VOICEDEBRIEF, surface: 'vault', viewport: [1700, 1000],
    steps: [{ wait: 2500 }, { navView: 'sgit' }, { wait: 4000 }],
    target: 'clip', clip: [0, 0, 1700, 1000] },
];

async function route(ctx) {
  if (!MIRROR) return;
  await ctx.route('**/*', async r => {
    const u = new URL(r.request().url());
    if (!HOSTS.has(u.hostname)) return r.continue();
    if (r.request().method() !== 'GET') return r.abort();
    try {
      let res;
      for (let a = 0; a < 5; a++) {
        try { res = await fetch(`http://localhost:8898/PROXY/${u.hostname}${u.pathname}${u.search}`); break; }
        catch (e) { if (a === 4) throw e; await new Promise(s => setTimeout(s, 300 * (a + 1))); }
      }
      r.fulfill({ status: res.status, body: Buffer.from(await res.arrayBuffer()),
        headers: { 'content-type': res.headers.get('content-type') || 'application/octet-stream',
                   'access-control-allow-origin': '*' } });
    } catch (e) { r.abort(); }
  });
}

// The vault app renders in a nested frame with no URL of its own (srcdoc). Identify
// it by a selector the app is known to contain — the /en-gb/app shell frame also has
// text, so "first frame with content" picked the wrong one.
async function appFrame(page, must = null, timeout = 90000) {
  const t0 = Date.now();
  while (Date.now() - t0 < timeout) {
    for (const f of page.frames()) {
      if (f === page.mainFrame()) continue;
      const ok = await f.evaluate(m => {
        if (m) return !!document.querySelector(m);
        // no selector given: any frame that has rendered real content. The /en-gb/app
        // shell frame stays empty, so this distinguishes it from the vault's own app.
        return !!document.body && document.body.innerText.trim().length > 30;
      }, must).catch(() => false);
      if (ok) return f;
    }
    await page.waitForTimeout(1000);
  }
  return null;
}

// Query through arbitrarily nested shadow roots (the REPL input is two deep:
// app-debug-pane -> app-debug-repl -> input).
const DEEP_QUERY = `(sel) => {
  function walk(root) {
    const hit = root.querySelector(sel);
    if (hit) return hit;
    for (const el of root.querySelectorAll('*')) {
      if (el.shadowRoot) { const r = walk(el.shadowRoot); if (r) return r; }
    }
    return null;
  }
  return walk(document);
}`;

async function runStep(page, step) {
  if (step.wait) return page.waitForTimeout(step.wait);

  if (step.appScroll || step.appClick) {
    const sel = step.appScroll || step.appClick;
    const f = await appFrame(page, sel.split(' ')[0]);
    if (!f) throw new Error('app frame not found for ' + sel);
    const act = step.appScroll ? 'scroll' : 'click';
    return f.evaluate(([s, a]) => {
      const el = document.querySelectorAll(s)[a === 'scroll' ? 1 : 0];
      if (!el) throw new Error('no ' + s);
      if (a === 'scroll') el.scrollIntoView({ block: 'center' }); else el.click();
    }, [sel, act]);
  }

  if (step.appClickText) {
    const [sel, text] = step.appClickText;
    const f = await appFrame(page, step.frameHas || sel.split(' ')[0]);
    if (!f) throw new Error('app frame not found');
    return f.evaluate(([s, t]) => {
      const el = [...document.querySelectorAll(s)].find(x => (x.textContent || '').trim() === t);
      if (!el) throw new Error('no control "' + t + '"');
      el.click();
    }, [sel, text]);
  }

  if (step.appClickLink) {
    const f = await appFrame(page, step.frameHas || null);
    if (!f) throw new Error('app frame not found');
    await f.evaluate(h => {
      const a = [...document.querySelectorAll('a[href]')].find(x => (x.getAttribute('href') || '').endsWith(h));
      if (!a) throw new Error('no link ending ' + h);
      a.click();
    }, step.appClickLink);
    return;
  }

  if (step.shadowClick) {
    const [host, sel] = step.shadowClick;
    return page.evaluate(([h, s]) => {
      const el = document.querySelector(h);
      const b = el && el.shadowRoot && el.shadowRoot.querySelector(s);
      if (!b) throw new Error('no ' + h + ' >> ' + s);
      b.click();
    }, [host, sel]);
  }

  if (step.shadowClickText) {
    const [host, sel, text] = step.shadowClickText;
    return page.evaluate(([h, s, t]) => {
      const el = document.querySelector(h);
      const root = el && el.shadowRoot;
      if (!root) throw new Error('no shadow ' + h);
      const b = [...root.querySelectorAll(s)].find(x => (x.textContent || '').includes(t));
      if (!b) throw new Error('no tab ' + t);
      b.click();
    }, [host, sel, text]);
  }

  if (step.appClickMatch) {
    // appClickText needs an EXACT textContent match, which is unusable for the graph
    // views: a node's text is its whole label ("CTO4 assigned · 25 through"). This
    // matches a substring instead, and dispatches a real MouseEvent rather than
    // calling .click() — the risk and role nodes are SVG <g> elements, where the
    // app listens for the event rather than relying on the HTMLElement method.
    const [sel, text] = step.appClickMatch;
    const f = await appFrame(page, step.frameHas || null);
    if (!f) throw new Error('app frame not found');
    return f.evaluate(([s, t]) => {
      const el = [...document.querySelectorAll(s)].find(x => (x.textContent || '').includes(t));
      if (!el) throw new Error('no element matching "' + t + '" for ' + s);
      el.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true, view: window }));
    }, [sel, text]);
  }

  if (step.appProbe) {
    // Selector reconnaissance. Every new vault costs a round of "what is this element
    // called?", and guessing burns a full capture run per guess. This asks the app
    // directly and prints the answer, so the next step can be written from fact.
    //   { appProbe: '.chain-node' }  ->  count, and the first few trimmed textContents
    const f = await appFrame(page, step.frameHas || null);
    if (!f) throw new Error('app frame not found');
    const out = await f.evaluate(s => {
      const els = [...document.querySelectorAll(s)];
      const seen = new Set();
      els.forEach(e => seen.add(e.tagName.toLowerCase() + '.' + [...e.classList].join('.')));
      return { count: els.length, shapes: [...seen].slice(0, 10),
               sample: els.slice(0, 8).map(e => (e.textContent || '').trim().slice(0, 50)) };
    }, step.appProbe);
    console.log('  probe', step.appProbe, '->', out.count);
    console.log('    shapes', JSON.stringify(out.shapes));
    console.log('    text  ', JSON.stringify(out.sample));
    return;
  }

  if (step.replType) {
    // Playwright's selector engine pierces open shadow roots, so the REPL input is
    // addressable directly and can be typed into for real rather than by dispatching
    // synthetic events — what gets captured is what a visitor would produce.
    const input = page.locator('app-debug-repl input').first();
    await input.waitFor({ state: 'visible', timeout: 30000 });
    for (const cmd of step.replType) {
      await input.click();
      await input.fill(cmd);
      await input.press('Enter');
      await page.waitForTimeout(1200);
    }
    return;
  }

  if (step.clickText) {
    const [sel, text] = step.clickText;
    return page.evaluate(([s, t]) => {
      const cand = [...document.querySelectorAll(s)]
        .filter(e => (e.textContent || '').trim().toLowerCase().includes(t.toLowerCase()));
      // the shallowest match is the row itself rather than an ancestor container
      cand.sort((a, b) => (a.textContent || '').length - (b.textContent || '').length);
      if (!cand[0]) throw new Error('no row matching ' + t);
      cand[0].click();
    }, [sel, text]);
  }

  if (step.navView) {
    return page.evaluate(v => {
      const nav = document.querySelector('vault-nav');
      const root = nav ? (nav.shadowRoot || nav) : document;
      const el = root.querySelector(`.vn-item[data-view="${v}"]`);
      if (!el) throw new Error('no nav item ' + v);
      el.click();
    }, step.navView);
  }
}

async function capture(browser, shot) {
  const ctx = await browser.newContext({ viewport: { width: shot.viewport[0], height: shot.viewport[1] }, deviceScaleFactor: 2 });
  await route(ctx);
  const page = await ctx.newPage();
  page.setDefaultTimeout(120000);
  page.setDefaultNavigationTimeout(120000);

  // Read-key open: the root inbox for App Mode, /en-gb/vault for the browser surface.
  await page.goto(ORIGIN + '/#' + encodeURIComponent(shot.cred), { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(9000);
  if (shot.surface === 'vault') {
    await page.goto(ORIGIN + '/en-gb/vault/', { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(14000);
  } else {
    const must = shot.frameHas || (shot.target === 'app' ? shot.sel : null);
    if (!await appFrame(page, must)) throw new Error('app never rendered');
  }

  for (const step of shot.steps) await runStep(page, step);

  let buf;
  if (shot.target === 'clip') {
    buf = await page.screenshot({ clip: { x: shot.clip[0], y: shot.clip[1], width: shot.clip[2], height: shot.clip[3] } });
  } else if (shot.target === 'app') {
    const f = await appFrame(page, shot.sel.split(' ')[0]);
    buf = await f.locator(shot.sel).first().screenshot();
  } else {
    // element in the top-level page, possibly a custom element with shadow content
    buf = await page.locator(shot.shadowSel[0]).first().screenshot();
  }

  const dir = outDir(shot.vault);
  fs.mkdirSync(dir, { recursive: true });
  const out = path.join(dir, shot.name + '.webp');
  let img = sharp(buf);
  if (shot.trim) {
    const m = await img.metadata();
    img = sharp(buf).extract({ left: 0, top: 0, width: m.width, height: Math.round(m.height * shot.trim) });
  }
  await img.resize({ width: 1500, withoutEnlargement: true }).webp({ quality: 76 }).toFile(out);
  const kb = (fs.statSync(out).size / 1024).toFixed(0);
  console.log(`  ✓ ${shot.vault}/${shot.name.padEnd(14)} ${kb} KB`);
  await ctx.close();
}

const browser = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium' });
console.log('capturing vault walkthrough shots' + (MIRROR ? ' (through the local mirror)' : '') + ':');
for (const shot of SHOTS) {
  if (ONLY && shot.name !== ONLY) continue;
  if (VAULT && shot.vault !== VAULT) continue;
  try { await capture(browser, shot); }
  catch (e) { console.log(`  ✗ ${shot.name.padEnd(14)} ${String(e.message).slice(0, 90)}`); }
}
await browser.close();
