# Creating and writing a vault from JavaScript, SG/Vault

> Create, open, read, write and push a vault from any web page with the library that runs dev.vault.sgraph.ai: the one code base to use, the exact methods, what goes over the wire, and where it stands against sgit 0.21.

*Source: <https://sgit.ai/docs/vault/vault-from-javascript.html> · site v0.7.75 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../index.md) / [Docs](../index.md) / Creating and writing a vault from JavaScript

**Surface:** a page on a `*.sgit.ai` site, outside every vault host. [The other surfaces →](../surfaces.md)

# Creating, opening and writing a vault from JavaScript

A web page that wants its own vault (newsroom.sgit.ai keeping a reader's notes, a tool saving its output) needs the same five actions the CLI has: create, open, read, write and commit, push. All five already exist in the browser, in the library that runs [dev.vault.sgraph.ai](https://dev.vault.sgraph.ai). This page is the recommendation to use that library and nothing else, the exact methods for each action, and a technical account of what goes over the wire. [Reading one file with a read key](reading-a-vault-file.md) is the read-only half of the same story.

**The one-sentence version.** Load the twelve vault library scripts from dev.vault.sgraph.ai, construct an `SGSend` with the API endpoint and an access token, then `SGVault.create` or `SGVault.open`; every file write is one encrypted commit sent as one `POST /batch`, and `pushIfMatch()` publishes it. **One code base**: every site that writes vaults uses this library, so a fix in it is a fix everywhere.

Checked on 12 October 2026. The library is vault UI `v0.2.3` (`sgraph_ai_app_send__ui__vault/v0/v0.2/v0.2.3/_common/js/lib/` in [SGraph-AI__App__Send](https://github.com/the-cyber-boardroom/SGraph-AI__App__Send/tree/dev/sgraph_ai_app_send__ui__vault)); the twelve files served by dev.vault.sgraph.ai are byte-identical to that folder. Every code sample below was run: create, write and push with the library, `sgit clone` and `sgit push` with sgit-ai 0.21.0, then open and read back with the library.

## The recommendation: one code base

| Code | Where it lives | Use it for |
|---|---|---|
| **The vault UI library**: `SGSend`, `SGVault` and its parts | SGraph-AI__App__Send, served at `dev.vault.sgraph.ai/_common/js/lib/` | **Everything that writes**: create, open with a vault key, read, write, commit, push, pull, merge, history. It is what dev.vault.sgraph.ai itself runs, so it is the most exercised writer there is |
| The tools modules: `core/vault-client`, `vault-session`, `vault-write`, the `sg-vault-*` components | SGraph-AI__Tools, served at `dev.tools.sgraph.ai/core/` as versioned ES modules | Read-only embedding (`sg-vault-content`, `sg-vault-key`, `sg-vault-fetch`). Their write path is an older port of the library above: one PUT per object, no compare-and-swap, no branch index, and vault creation from token-style keys only |
| The readers on this site: `assets/vault-embed.js`, `assets/vault-docs.js` | This repo | Reading one file with a published read key, [as documented here](reading-a-vault-file.md) |
| The sgit CLI | [SGit-AI__CLI](https://github.com/SGit-AI/SGit-AI__CLI), on PyPI as `sgit-ai` | The reference for the format: agents, scripts, and the 0.21 features the browser does not have yet ([below](#compat)) |

So a site does not write its own vault writer, and does not copy one from the tools modules. Two ports drift: the tools port needed its own fix before it could open vaults made by sgit 0.16, and the format is moving again with 0.19 to 0.21. Gaps found by using the library are fixed in the library, in SGraph-AI__App__Send, and every site picks them up.

## Loading the library

The files are plain scripts, not ES modules: each declares a global class, and the `sg-vault--*.js` files add methods to `SGVault.prototype`. Order matters. A classic `<script src>` from another origin needs no CORS, so this works on any page:

```
<script src="https://dev.vault.sgraph.ai/_common/js/lib/sg-send/sg-send-crypto.js"></script>
<script src="https://dev.vault.sgraph.ai/_common/js/lib/sg-send/sg-send.js"></script>
<script src="https://dev.vault.sgraph.ai/_common/js/lib/sg-vault/sg-vault-crypto.js"></script>
<script src="https://dev.vault.sgraph.ai/_common/js/lib/sg-vault/sg-vault-object-store.js"></script>
<script src="https://dev.vault.sgraph.ai/_common/js/lib/sg-vault/sg-vault-ref-manager.js"></script>
<script src="https://dev.vault.sgraph.ai/_common/js/lib/sg-vault/sg-vault-commit.js"></script>
<script src="https://dev.vault.sgraph.ai/_common/js/lib/sg-vault/sg-vault.js"></script>
<script src="https://dev.vault.sgraph.ai/_common/js/lib/sg-vault/sg-vault--file-ops.js"></script>
<script src="https://dev.vault.sgraph.ai/_common/js/lib/sg-vault/sg-vault--folder-ops.js"></script>
<script src="https://dev.vault.sgraph.ai/_common/js/lib/sg-vault/sg-vault--sync.js"></script>
<script src="https://dev.vault.sgraph.ai/_common/js/lib/sg-vault/sg-vault--history.js"></script>
<script src="https://dev.vault.sgraph.ai/_common/js/lib/sg-vault/sg-vault--branches.js"></script>
```

Three things to know about that list:

- **The path is not versioned.** Every deploy of the vault UI overwrites it. A site that must not change under its readers (any site holding keys, newsroom.sgit.ai included) copies these twelve files into its own repo at a known commit and loads them from its own origin; [the passkey design](../../articles/the-passkey-opens-the-vault.md) already requires that. It is still one code base: the copy is pinned, never edited, and refreshed from upstream.
- **The API takes any origin.** Measured against `dev.send.sgraph.ai`: the preflight answers `access-control-allow-origin: *` and allows `x-sgraph-access-token` and `x-sgraph-vault-write-key`. Do not add `X-API-Key` to a browser request (the Python CLI sends it); it is not on the allowed list, so the preflight fails and nothing is sent.
- **Web Crypto needs a secure context**, https or localhost. Key derivation is two PBKDF2 runs of 600,000 iterations, done in parallel: about a second on a laptop, more on a phone, once per open.

## The five actions

### 1 · Create a vault

```
const sgSend = new SGSend({ endpoint: 'https://dev.send.sgraph.ai', token: accessToken })
const passphrase = randomPassphrase()                 // 24 chars of [a-z0-9], as sgit init makes
const vault = await SGVault.create(sgSend, passphrase, { name: 'My notes' })
const vaultKey = vault.getVaultKey()                  // "<passphrase>:<vault_id>": store it, it is the only way back in

function randomPassphrase(n = 24) {
  const abc = 'abcdefghijklmnopqrstuvwxyz0123456789', out = []
  while (out.length < n) {                             // rejection sampling: no modulo bias
    for (const b of crypto.getRandomValues(new Uint8Array(n))) if (b < 252 && out.length < n) out.push(abc[b % 36])
  }
  return out.join('')
}
```

`create` picks a random 8-character vault id, derives the keys, and sends the first commit, the named ref, the clone ref and the branch index as **one** `POST /batch`. There is no separate "create vault" endpoint: the server creates the vault on the first write and remembers the SHA-256 of the write key that made it, and from then on only that write key can write. The write needs an access token, so **creating a vault needs an access token**; opening and reading do not.

The passphrase is the caller's to choose, and its strength is the vault's strength: there is no rate limit on guessing it offline. Use 24 random characters as above, the same shape `sgit init` generates. The vault's display name is stored encrypted, in `.vault-settings.json`.

### 2 · Open a vault

```
const vault = await SGVault.open(sgSend, vaultKey, { cloneBranch: deviceBranch })   // see the box below
vault.writable        // true: a vault key carries the write key
vault.name            // decrypted from .vault-settings.json
vault.listFolder('/') // [{ name, type: 'file'|'folder', size, content_hash }]
```

`open` reads the branch index, then the named ref **live** (refs are never cached), then this browser's clone ref, and loads the root folder. Sub-folders load lazily. If the CLI or another browser published while this one sat still, open shows the newer published head rather than the stale clone. A key copied from sgit output carries a prefix (`sgit_private_vault_` followed by the key); `open` does not strip it, so pass the key through `SGVaultCrypto.stripKeyPrefix()` first. For a read key instead of a vault key, see [read-only access](#readonly).

**Give every device its own clone branch.** The clone branch defaults to `web-ui`, so two browsers opening the same vault key commit to the *same* working ref, and when their work diverges `open` keeps showing that shared clone head rather than what was published. Pass `{ cloneBranch: id }` with an id made once per device and kept in local storage, for example `'nr-' + crypto.randomUUID().slice(0, 8)`. A client that only reads should use its own name too, or [`openReadOnly`](#readonly).

### 3 · Read a file

```
async function ensureLoaded(vault, folder) {          // load every folder on the path
  let path = ''
  for (const part of folder.split('/').filter(Boolean)) {
    path += '/' + part
    if (vault.needsLoading(path)) await vault.loadSubTreeOnDemand(path)
  }
}
await ensureLoaded(vault, '/notes')
const bytes = await vault.getFile('/notes', 'today.md')  // ArrayBuffer, decrypted
const text  = new TextDecoder().decode(bytes)
```

Files are addressed as `(folder, name)`, folder paths start with `/`. Files over 4 MB are fetched through a presigned S3 URL automatically.

### 4 · Write: every write is a commit

```
async function writeFile(vault, folder, name, data) {
  await ensureLoaded(vault, folder)                       // REQUIRED, see the warning below
  let path = ''
  for (const part of folder.split('/').filter(Boolean)) { // create missing folders
    path += '/' + part
    if (!vault.listFolder(path)) await vault.createFolder(path)
  }
  const bytes  = typeof data === 'string' ? new TextEncoder().encode(data) : data
  const exists = (vault.listFolder(folder) || []).some(e => e.name === name && e.type === 'file')
  return exists ? vault.updateFile(folder, name, bytes) : vault.addFile(folder, name, bytes)
}
await writeFile(vault, '/notes', 'today.md', '# Today\n')
```

There is no staging area, and no separate commit call. `addFile`, `updateFile`, `removeFile`, `renameFile`, `moveFile`, `createFolder` and the other folder operations each make one commit, with a generated message such as `Add today.md`, and send the blob, the changed trees, the commit and the clone ref as one `POST /batch`. `addFiles([{ folderPath, fileName, fileData }])` writes many files as one commit. A commit lands on this browser's private clone branch; nobody else sees it until it is pushed.

**Load a folder before writing into it.** After `open`, sub-folders are placeholders. `addFile('/notes', …)` on a folder that was never loaded makes a commit called `Add …` whose tree still points at the old folder, so the file is silently missing and the push reports success. Reproduced on 12 October 2026 with v0.2.3. The `ensureLoaded` call in `writeFile` above prevents it; the fix belongs in the library ([below](#upstream)).

### 5 · Push: publish with compare-and-swap

```
async function publish(vault) {
  if (vault._refManager.lastRawRef(vault._refFileId) === undefined)
    await vault.getBehindCount()               // only if never read: arms the compare-and-swap
  try { await vault.pushIfMatch(); return }
  catch (e) { if (e.code !== 'ECAS') throw e } // somebody else published first
  const theirs = await vault._refManager.readRef(vault._refFileId)
  const r = await vault.merge(theirs, { publish: false })   // fast-forward or three-way, file level
  if (r.conflicts.length) throw new Error('conflicts: ' + r.conflicts.join(', '))
  await vault.pushIfMatch()
}
```

`pushIfMatch()` moves the named ref only if the server still holds the exact bytes this client last read for it. If someone else published in between, it throws `ECAS` and the caller merges and retries. That is the pattern the vault host's own headless kernel uses (`kernel-app-handlers.js`, `_safePush`), and the two `_refManager` calls are copied from it, which is why they reach into an underscore field; a public `safePush()` is on the [upstream list](#upstream).

- **Do not call `push()`.** It moves the named ref unconditionally, which silently drops whatever another client published since your last read. The vault UI's shells still call it; the CLI reports the result as a rewind.
- **Read the ref once after `create`, and only then.** A new vault has only ever *written* its named ref, so `pushIfMatch` throws `ENOMATCH` until something reads it; `open` has already read it. But any read re-arms the comparison: calling `getBehindCount()` or `readRef` immediately before every `pushIfMatch` compares against the bytes just fetched, which turns the compare-and-swap into a blind overwrite. That is why `publish` reads only when the ref has never been read. Tested with two writers racing on 12 October 2026: with the guard, the second gets `ECAS`, merges, and both changes survive; without it, the first writer's commit is lost.
- **Pull** with `pull()` when there is nothing unpushed (it refuses otherwise), or with `merge(theirs)` when there is. `getAheadCount()` and `getBehindCount()` report the distance.

### Read-only access

A read key, 64 hex characters plus the vault id, decrypts but cannot write:

```
const cred = SGVaultCrypto.parseReadOnlyCredential(readKey)   // "<64 hex>:<vault_id>", prefix optional
const c    = await SGVaultCrypto.deriveReadOnlyCreds(cred.vaultId, cred.readKeyHex)
const ro   = await SGVault.openReadOnly(new SGSend({ endpoint }), c.vaultId, c.readKeyB64, c.refFileId)
ro.writable   // false
```

For a page that only shows one file, the 90-line reader in [Reading one file out of a vault](reading-a-vault-file.md) is smaller.

## The methods

| Call | What it does |
|---|---|
| `new SGSend({ endpoint, token })` | The HTTP client. `endpoint` is `https://dev.send.sgraph.ai` (or `https://send.sgraph.ai`); `token` is the access token, sent as `x-sgraph-access-token`, needed only for writes |
| `SGVault.create(sgSend, passphrase, { name, description })` | New vault with a random id; one batch write. Returns an open, writable vault |
| `SGVault.open(sgSend, vaultKey, { cloneBranch })` | Open with `passphrase:vault_id`. `cloneBranch` names this client's private branch; the default, `web-ui`, is shared by every browser, [so set it](#open) |
| `SGVault.openReadOnly(sgSend, vaultId, readKeyB64, refFileId)` | Open with a read key; `writable` is false |
| `vault.getVaultKey()` · `vaultId` · `name` · `writable` · `setName(n)` · `getStats()` | Key and properties. `setName` is a commit |
| `listFolder(path)` · `needsLoading(path)` · `loadSubTreeOnDemand(path)` | Browse; sub-folders load on demand |
| `getFile(folder, name)` | Decrypted bytes |
| `addFile` · `addFiles` · `updateFile` · `removeFile` · `renameFile` · `moveFile` | One commit each (`addFiles`: one for the lot) |
| `createFolder` · `removeFolder` · `renameFolder` · `moveFolder` | One commit each |
| `pushIfMatch()` · `pull()` · `merge(commitId, { publish })` · `getAheadCount()` · `getBehindCount()` | Sync. `push()` also exists; [do not use it](#push) |
| `logCommits({ limit, from })` · `listTreeAt(commitId, path)` · `readFileAt(commitId, path)` | History: `[{ id, parents, tree_id, timestamp_ms, message }]`, and any file at any commit |
| `getBranches()` · `switchBranch(headRefId)` | Branches from the branch index |
| `SGVaultCrypto.stripKeyPrefix` · `classifyKey` · `parseVaultKey` · `deriveKeys` | Key handling, no network |

Errors carry a `code` where the caller is expected to act: `ECAS` (the named ref moved: merge and retry), `ENOMATCH` (compare-and-swap before any read), `EREADONLY` (a static host, no write API). HTTP failures throw with the status and the server's detail, for example a 403 when the access token is missing.

## How it works

### Keys: everything comes from the vault key

| Derived | How | Used for |
|---|---|---|
| **read key**, 32 bytes | PBKDF2-HMAC-SHA256, 600,000 iterations, password = passphrase, salt `sg-vault-v1:<vault_id>` | AES-256-GCM over every object, ref and name; the HMAC key for file ids. This is the read key sgit prints, in hex |
| **write key**, 32 bytes | The same PBKDF2 with salt `sg-vault-v1:write:<vault_id>` | Never encrypts anything. Sent as lowercase hex in `x-sgraph-vault-write-key`; the server compares its SHA-256 with the one the first writer set |
| **named ref id** | `ref-pid-muw-` + first 12 hex of `HMAC-SHA256(read key, "sg-vault-v1:file-id:ref:<vault_id>")` | Where the published head lives |
| **branch index id** | `idx-pid-muw-` + HMAC of `sg-vault-v1:file-id:branch-index:<vault_id>` | The list of branches |
| **clone ref id** | `ref-pid-snw-` + HMAC of `sg-vault-v1:file-id:branch-ref:<vault_id>:<branch>` | This client's working head (`web-ui` by default) |

The server receives none of this except the write key's hex, and stores only its hash. Addresses are computed, never looked up: a holder of the read key knows where the head is before making a request.

### Objects: four kinds, all ciphertext

- **Encryption.** AES-256-GCM, a random 12-byte IV, stored as `IV || ciphertext || tag`: exactly what `crypto.subtle.encrypt` returns with the IV in front.
- **Object ids.** `obj-cas-imm-` + the first 12 hex of SHA-256 over the *ciphertext*, stored at `bare/data/<id>`. Content-addressed, so immutable and cacheable forever.
- **Blob**: the file's bytes, encrypted.
- **Tree** (`tree_v1`): `{ schema, entries: [{ name_enc, size_enc, content_hash_enc, blob_id, tree_id }] }`. Names, sizes and hashes are encrypted one by one, so the folder listing is itself ciphertext; a sub-folder is an entry with a `tree_id`.
- **Commit** (`commit_v2`): `{ schema, parents, tree_id, timestamp_ms, message_enc, branch_id, signature }`, the message encrypted.
- **Ref**: `{"commit_id": "obj-cas-imm-…"}`, encrypted, at `bare/refs/<ref id>`. The only mutable files are refs and the branch index.

### Two refs: the clone branch and the named branch

Each client commits to its own clone ref; `push` copies that commit id into the named ref, which is what everyone else reads. This is the [two-branch model](../two-branch-model.md) the CLI uses, so a browser and a terminal are two clones of the same vault. The branch index (`branch_index_v1`) lists the branches so that `sgit clone` can find the named ref.

### The wire

| Call | Auth | Used by |
|---|---|---|
| `GET /api/vault/read/<vault_id>/<path>` | none | refs (with `cache: 'no-store'`), the branch index, objects |
| `POST /api/vault/batch/<vault_id>` with `{"operations": [{op, file_id, data, match}]}` | token + write key when any op writes | every commit, every push, bulk reads. `op` is `read`, `write` or `write-if-match`; `data` and `match` are base64; chunked at 50 operations. A compare-and-swap miss comes back as `"status": "conflict"` inside an HTTP 200 |
| `PUT /api/vault/write/<vault_id>/<path>` | token + write key | single writes outside a batch |
| `GET /api/vault/presigned/read-url/<vault_id>/<path>` | none | files over 4 MB |

So one file write is one request carrying four or more encrypted objects, and one push is one request carrying the ref and the index. The full endpoint list is in [API: vault objects](../../api/vault-objects.md), the headers in [API: authentication](../../api/authentication.md).

## With sgit 0.21: what holds and what does not

**What holds, tested 12 October 2026.** A vault made with `SGVault.create` was cloned by sgit-ai 0.21.0 with every file intact; a CLI commit and push was then opened and read back by the library; a library `updateFile` and `pushIfMatch` was pulled by the CLI, which then pushed again without complaint. For a vault at the default format, which is every vault until its owner raises it, the browser and the CLI interoperate in both directions.

**What does not hold yet**, from the code and [History integrity](../history-integrity.md):

| sgit 0.19–0.21 feature | The library today | Consequence |
|---|---|---|
| Signed commits; `--feature signatures-required` | Writes `signature: null` | On a vault that requires signatures, the CLI refuses to pull or clone past a browser commit. Do not write from the browser to such a vault |
| Format 2: 32-hex object ids | Always 12-hex | Readable by everyone, but a format-2 vault receives 48-bit ids from the browser |
| The branch index as a shared document, written with compare-and-swap | `pushIfMatch` and `push` overwrite it with a single entry | Drops the other clones' entries and the format gate from the server's copy. The CLI merges its local copy back on its next pull, so nothing is lost while some clone still holds it; an entry no surviving clone holds is gone |
| Deterministic tree encryption | Random IVs for tree entries | Harmless: trees still decrypt; an unchanged folder rewritten by the browser gets a new id instead of the old one |

None of that matters to a site keeping its own vaults (newsroom.sgit.ai's reader vaults are written only by newsroom.sgit.ai) as long as nobody raises their format. It matters as soon as a vault is shared with the CLI under the 0.21 policies, and the fix is in the library, not around it.

## What the library needs, in SGraph-AI__App__Send

In priority order, each a change to `_common/js/lib/sg-vault/` that every site then inherits:

1. **Fix the lazy-folder write.** A write into an unloaded folder should load it (or refuse), never commit a tree that drops the file.
2. **A public `safePush()`**: read the ref if it was never read, `pushIfMatch`, merge and retry once on `ECAS`. Then retire unconditional `push()`.
3. **A clone branch per device by default**, made once and remembered, instead of the shared `web-ui`.
4. **`create(…, { vaultId })`**: let the caller supply the vault id. A vault whose id and passphrase are *derived* (the passkey's computed top vault) cannot be created through the public API today, only opened.
5. **Publish at a versioned path** (`/_common/js/lib/v0.2.3/…`, or one bundled file) so a site can pin a version without copying, and move the inline `SGVault.createFromToken` out of `index.html`. Token-style keys were dropped from the CLI in 0.15 as guessable, so new sites should not use that path at all.
6. **Merge the branch index** with compare-and-swap instead of overwriting it, keeping other entries, the gate, the keys and the tags.
7. **Sign commits** (P-256, JCS signing bytes, `author_key_id`; the CLI's `tests/_fixtures/interop_vectors.json` is the test vector), then **format 2** ids when the gate says so.

## For newsroom.sgit.ai

- **Keys.** The newsroom already stores vault keys behind a passkey ([the design](../../articles/the-passkey-opens-the-vault.md), `passkey/lab.js` for the derivation). A vault made with `SGVault.create` and a random passphrase goes into that keyring as `getVaultKey()`, and is opened next time with `SGVault.open`. The lab's own derivation (`sgitKeys`) is the same PBKDF2 as `SGVaultCrypto.deriveKeys`, checked against vectors generated with the CLI's own `Vault__Crypto`.
- **The computed top vault** needs item 3 above; until then it can be opened but not created by the library.
- **The access token** is needed for every write. Pasted once and then kept inside the reader's own vault is the shape the design already describes.
- **Load a pinned copy** of the twelve files from the newsroom's own origin, per the design's no-third-party-scripts rule.

[Reading one file out of a vault](reading-a-vault-file.md) · [API: vault objects](../../api/vault-objects.md) · [The two-branch model](../two-branch-model.md) · [History integrity](../history-integrity.md) · [Credentials](../credentials.md)

[← Reading a vault file](reading-a-vault-file.md)[Static hosting →](static-hosting.md)


---

*[Site index for agents](../../llms.txt) · [HTML version](https://sgit.ai/docs/vault/vault-from-javascript.html)*
