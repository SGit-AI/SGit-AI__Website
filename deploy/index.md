# Run your own SG/Send server — sgit.ai

> Deployment guidance for self-hosting a zero-knowledge SG/Send server — rendered live in your browser from an encrypted vault, with no copy stored on this site.

*Source: <https://sgit.ai/deploy/index.html> · site v0.2.33 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / Deploy

# Run your own SG/Send server

Deployment guidance for standing up your own zero-knowledge vault server — Docker, AWS, GCP, Heroku, or a static host. **These pages are not part of this website.** They live in an encrypted vault maintained by the SG/Send team, and your browser is decrypting them right now with a published read-only key.

**How this page works:** the vault's ciphertext is fetched straight from the SG/Send server over CORS, and the AES-256-GCM decryption happens in this tab using the Web Crypto API. There is no build step and no copy of the content on sgit.ai — when the SG/Send team runs `sgit push`, the next load of this page has it. Open the **vault panel** (right edge) to watch the objects being fetched, see which came from cache, and check the exact commit you are reading. [**Full architecture, with diagrams →**](../case-studies/live-vault-docs.md)

opening vault…

Fetching the encrypted index…

### Vault debug [how this works →](../case-studies/live-vault-docs.md)

not open yet

what you are looking at

 Every row above is an encrypted object pulled from the SG/Send API and decrypted locally — click one to see what it actually contains. Objects whose id contains **-imm-** are content-addressed and therefore immutable, so they are cached permanently; the mutable **ref** is the one mutable object, so it is checked at most once per freshness window (120s) rather than once per page — inside the window, reading the docs makes no requests at all, and **check for new commit** forces one whenever you want it.

The **tree** objects are the reason a first visit reads more than one file: filenames are encrypted inside them, so building the navigation means reading every directory. That index is a pure function of the commit id, so it is memoised — after the first visit, an unchanged commit reads no tree objects at all. Nothing here is stored on sgit.ai.

[How this page works →](../case-studies/live-vault-docs.md) Architecture diagrams, the object model, the cache tiers, and how two Claude Code sessions publish into this vault.


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/deploy/index.html)*
