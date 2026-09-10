# An infographic of the published vaults — build brief

> A brief for a companion to the network infographic, grouping the 26 published vaults by use case and industry — starting with the two blockers upstream of any image: neither grouping exists in vaults.json yet, and the network infographic it copies has already gone stale in its own headline count.

*Source: <https://sgit.ai/docs/briefs/vault-map-infographic.html> · site v0.2.76 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../../index.md) / [Docs](../index.md) / [Briefs](index.md) / The vault map infographic

**Surface:** a published image, and the data behind it. [The three code surfaces →](../surfaces.md)

# An infographic of the published vaults, grouped by use case and industry

A brief for producing a companion to the network infographic: the same treatment applied to the **26 published vaults** rather than to the sites, grouped by **what someone is trying to do** and **the industry they are in**. It is written to be executed, and it opens with the two things that will otherwise sink it — the groupings do not exist as data yet, and an infographic is a snapshot that rots.

**Do not start with the picture.** Two blockers below are upstream of any image being generated. Fix them first and the infographic becomes a rendering job; skip them and an image model will invent the groupings, which is the one failure nobody will notice until a customer reads it back to us.

## Blocker one: the network infographic is already wrong

The companion image this one is modelled on carries a footer reading **“19 sites · 18 published · 1 forthcoming”**, and lists `skills.sgit.ai` as *Forthcoming*. Both were true when it was generated. Today [the network](../../network/index.md) lists **27 sites** and skills.sgit.ai has been live for some time — so a picture that is roughly a week old is now wrong in its headline number and in one of its cells.

That is not an argument against making it. It is the constraint the work has to be designed around:

- **Every count in the image must be computed from the data at generation time** and pasted in, never estimated, never carried over from a previous version.
- **The image carries the version and date it was generated**, in the footer, in the same way [every vault app carries its version](../guidance/index.md#versions). A picture with a stamp is a snapshot; one without is a claim.
- **The page that publishes it links to the live list beside it**, so a reader who wants today's answer has one click to it. The infographic is the overview; [the table](../../demos/vaults/index.md) is the truth.
- **Regenerating is a scheduled chore, not an event.** Add it to the release checklist as a diff: if the vault count changed, the image is stale.

## Blocker two: neither requested grouping exists yet

The brief asks for **use case** and **industry**. Checked against `admin/content/vaults.json`, which is what the vaults table and [the catalogue](../../demos/vaults/llms.txt) are generated from, the fields today are:

| Field | Coverage | What it actually is |
|---|---|---|
| `category` | **26 of 26** | The vault's *shape*, not its use case — Application (5), Analysis (5), Record (4), Reference (4), Presentation (3), Briefing (3), Report (1), Gallery (1). Useful, and not what was asked for |
| `job` | **6 of 26** | The closest thing to a use case that exists (“Publish a standard as data”, “Pitch an investor”, “Hand over a report”) — but it was added for the homepage bands and covers under a quarter of them |
| `industry` | **0 of 26** | Does not exist |

**So the first deliverable is not an image, it is two fields.** Add `use_case` and `industry` to every entry in `vaults.json`, and the infographic becomes a view over data the site already publishes — which is the rule the rest of this estate runs on: *indexes are generated from the data they index, because an index maintained by hand becomes a lie on a schedule.*

- **Write both fields from the vault, not from its title.** Open each one, read what it does, and say what job it does for whom. The pages under [Published vaults](../../demos/vaults/index.md) already contain that judgement in prose — this is turning it into data.
- **Keep the vocabularies small and closed.** Six to eight use cases and six to eight industries, reused; a taxonomy where most values appear once is not a taxonomy. Write the allowed values down in the file and have the build fail on an unknown one.
- **Be honest where a vault has no industry.** Several are method demonstrations that belong to no sector. `"industry": "cross-industry"` is a real answer; inventing “FinTech” because a vault mentions money is not.
- **Do not delete `category`.** Shape and use case are different questions and the table uses shape. Add, do not replace.

## What the picture has to show

Match the network infographic so the two read as a pair: dark ground, one luminous shared foundation at the top, numbered columns beneath it, a footer of counts, and a horizontal band of cross-links near the bottom.

| Element | Content |
|---|---|
| **The foundation** | What every vault shares: encrypted files, version history, and a published read key that is the whole credential. The network image put “sgit.ai vaults” here; this one can say **one vault format** |
| **Primary grouping — columns** | **Use case.** Each column is a job somebody is trying to do, with the vaults that do it listed as cells: name plus one short line, exactly as the sites image does |
| **Secondary grouping — a mark on each cell** | **Industry**, as a small tag or colour key rather than a second set of columns. Two nested column systems in one image is unreadable; a legend is not |
| **The band** | Genuine relationships between vaults — the conformance layer forking the catalogue, the Risk Graph Explorer sharing the licence-to-operate acceptance model. **Carry the same disclaimer the sites image carries**: illustrative links, not deployed integrations |
| **The footer** | The computed counts, the site version and the date. Nothing typed by hand |

## The accuracy rules, because an image model will not follow them on its own

An image model renders text as shapes. It will misspell a domain, drop a hyphen, invent a plausible vault that does not exist, and produce a confident number that came from nowhere — and none of that throws an error.

1. **Generate the caption text from the data first**, as a list, and treat the image as a rendering of that list. If the list and the image disagree, the image is wrong.
2. **Read every string in the output back against `vaults.json`** — every vault name, every count, every label. Character by character on the names.
3. **Count the cells.** If the data says 26 vaults and the picture shows 24, it dropped two, and it will not tell you which.
4. **No vault appears that is not in the file.** A generated name that reads plausibly is the most dangerous output this process can produce.
5. **If the model cannot render the text reliably, render the text separately.** Generating the artwork and setting the labels as real text over it is a legitimate and more honest answer than fighting the model.

## Publishing it on this site

- **The validator bans `<img src=>`.** Images here go through the `data-shot` mechanism that `assets/shots.js` fills, because a declarative image reference cannot be served when a page is rendered inside a vault. Use the existing pipeline; do not add an exception for this one.
- **Write real alt text**, and treat it as the accessible equivalent rather than a caption: an infographic whose content exists only as pixels is invisible to a search engine, to `llms-full.txt` and to any agent reading this site — which is the same gap the video pages had to state.
- **Put the grouped list on the page in HTML too**, under or beside the image. Then the picture is the overview and the text is the content, and the `.md` twin carries the substance rather than a broken reference to a picture.
- **State how it was made.** The network image was generated by an image model; say so on the page. This site's whole method is that a reader can check the provenance of what it publishes.

## The prompt to hand the agent

```
Produce a vault map infographic for sgit.ai, as a companion to the existing
network infographic, grouping the published vaults by USE CASE and INDUSTRY.

Read https://sgit.ai/docs/briefs/vault-map-infographic.md first. Do the two
upstream steps before generating any image.

STEP 1 — the data. admin/content/vaults.json has category on all 26 vaults, job
on 6, and no industry field at all. Neither requested grouping exists yet. Add
use_case and industry to every entry, written from the vault itself and not from
its title, using a closed vocabulary of 6-8 values each, declared in the file,
with the build failing on an unknown value. Keep category — shape and use case
are different questions. Use "cross-industry" where a vault genuinely serves no
sector; do not invent one.

STEP 2 — the caption list. Generate the full text of the infographic from
vaults.json as a plain list: every column heading, every cell, every count.
This list is the source of truth; the image is a rendering of it.

STEP 3 — the image. Match the network infographic: dark ground, one shared
foundation at the top, numbered columns for use cases, industry as a tag or
colour key rather than a second column system, a cross-links band carrying the
same "illustrative, not deployed integrations" disclaimer, and a footer with the
computed counts plus the site version and date.

STEP 4 — check it. Read every string in the image back against vaults.json,
character by character on the names. Count the cells against the vault count. No
vault may appear that is not in the file. If the model cannot render text
reliably, render the artwork and set the labels as real text over it.

STEP 5 — publish it. Use the data-shot pipeline, never an img src, which the
validator bans. Write real alt text. Put the grouped list on the page as HTML as
well, so the markdown twin carries the substance. Say on the page that the image
was generated by an image model.

Report: the two vocabularies you chose, how many vaults landed in each value,
and any vault whose use case or industry you could not determine from its
contents.
```

The companion piece is the network infographic, which is what this one should look like and also what it should learn from — it is a good picture with a footer that has already gone stale. [All briefs](index.md) · [Working on a vault: start here](../guidance/index.md) · [The published vaults](../../demos/vaults/index.md)


---

*[Site index for agents](../../llms.txt) · [HTML version](https://sgit.ai/docs/briefs/vault-map-infographic.html)*
