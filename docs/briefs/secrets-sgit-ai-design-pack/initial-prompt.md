You are working in SGit-AI/SGit-AI__Website__Secrets, the repository for secrets.sgit.ai: a static site on GitHub Pages that is also a zero-knowledge, browser-only secrets manager backed by one GCP project per environment (Identity Platform for login, Cloud Storage for Firebase for ciphertext). Everything in the repository is public; nothing in it is secret.

Read docs/design/secrets-sgit-ai__mvp-build-brief.md in full first. It is the instruction set, and sections 1 to 4 hold decisions that are closed: do not reopen them. Then read the four other design documents in docs/design/; they carry the reasoning behind the brief. House style is https://coding.sgit.ai/llms-full.txt and https://nfrs.sgit.ai/llms.txt; section 7 of the brief extracts what applies here. The wider family conventions are at https://sgit.ai/llms.txt (markdown twins, llms.txt, the leak tripwire, the version gate).

Rules you never break:
- No server-side code of any kind. No Cloud Functions, no proxies, no "small API". If something seems to need one, write the proposal in docs/design/brief-corrections.md and carry on without it.
- Plaintext exists only in the browser, briefly, after a passkey gesture. Nothing derived from a key is ever written to localStorage, sessionStorage or IndexedDB.
- Nothing secret in the repo, ever. Test fixtures use obviously fake values.
- No build step. No runtime script from any origin other than this site; vendor and hash every dependency.
- The passkey RP ID is exactly secrets.sgit.ai (localhost when testing locally), never sgit.ai.
- Every push to dev is a release: the version lives in admin/build/version.txt, is repeated in the commit subject as "site vX.Y.Z : <what>", and CI tags it. A release that fails the gate locally fails the same way in CI.
- Every claim on the site carries a status (shipped / proposed / absent) from data/features.json, and docs/reality.md is generated from it. Nothing is described in the present tense before it is shipped.

Work through section 11 of the brief in order. Step 1 is the pipeline before the site: the repository layout, version.txt, the chrome generator, the eight-check gate in admin/build/validate.js, .github/workflows/deploy-pages.yml with validate → tag-release → deploy → verify-live, CNAME, the branch-protection notes, and docs/design/ as delivered. Do not begin step 4 until the dev GCP project exists and tests/auth.html, tests/storage.html and tests/webauthn-prf.html are green against it.

When the brief is wrong, record what you found in docs/design/brief-corrections.md and continue. When something needs a human (DNS, billing, GCP bootstrap, OAuth client secrets, reviewer approval), stop and list exactly what you need in docs/ops/needs.md, then continue with whatever does not depend on it.

Start by printing the repository layout you intend to create and the contents of admin/build/version.txt, then build step 1 and commit it as "site v0.1.0 : the pipeline, before the site".
