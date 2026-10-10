# Re-anchoring: keeping an agent's rules alive through every summary, and a canary that shows when they are not, sgit.ai

> Instructions given only in conversation can be lost when a long session is summarised. The session that runs this site has been summarised eighteen times in a month, each time keeping under 2% of what it replaced. Re-anchoring is the answer: keep the agent's rules in a behaviour policy file and have the harness print it back after every summary, so the rules are restored rather than remembered. And because you cannot see what a summary drops, add a canary: a short status report, computed from the transcript, that ends every few answers. If it stops appearing, something in the policy has not been read. Both are running in this session now. This is how they work, what each piece is for, and why the best way to do it today is a recipe that someone has to keep up to date.

*Source: <https://sgit.ai/articles/re-anchoring-agent-behaviour-policies.html> · site v0.7.26 · this file is generated from the same content as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links below point at them.*

---

[Home](../index.md) / [Articles](index.md) / Re-anchoring: keeping an agent's rules alive through every summary, and a canary that shows when they are not

# Re-anchoring: keeping an agent's rules alive through every summary, and a canary that shows when they are not

By [Dinis Cruz](../about/index.md) · 2026-10-10 · [v0.7.22](../admin/versions.md) · agentsclaude-codehooksagent-behaviour-policycompactioncontextre-anchoringguardrailsgovernancearticle

***Abstract:** Instructions given only in conversation can be lost when a long session is summarised. The session that runs this site has been summarised eighteen times in a month, each time keeping under 2% of what it replaced. Re-anchoring is the answer: keep the agent's rules in a behaviour policy file and have the harness print it back after every summary, so the rules are restored rather than remembered. And because you cannot see what a summary drops, add a canary: a short status report, computed from the transcript, that ends every few answers. If it stops appearing, something in the policy has not been read. Both are running in this session now. This is how they work, what each piece is for, and why the best way to do it today is a recipe that someone has to keep up to date.*

Claude Code's documentation says it plainly: "If an instruction disappeared after compaction, it was given only in conversation, lives in a nested CLAUDE.md that hasn't reloaded yet, or is a path-scoped rule that hasn't matched a file since" ([memory](https://code.claude.com/docs/en/memory)). Anthropic's own permission classifier has the same weakness, in its own words: a boundary "can be lost if context compaction removes the message that stated it" ([permission modes](https://code.claude.com/docs/en/permission-modes)).

That sentence is the most important one I have read this week about running agents, because it explains a failure I had just watched happen. On 9 October two emails drafted by one of my agents went out in my voice, against a rule that had been written down four times; one of the reasons was that the rule fell out of the agent's context when the conversation was summarised. I wrote about the fix for that email, [a second reader the agent cannot skip](../articles/a-second-reader-the-agent-cannot-skip.md). This article is about the general problem underneath it, and a technique for it that I have started calling **re-anchoring**.

What summarisation does to a long session: every compaction in the session that runs this site, read from its own transcript. Each turned about 785,000 tokens into 9,000 to 19,000. All eighteen were automatic.

## In short

- **Summaries are frequent, heavy and invisible.** This session has been summarised eighteen times in a month. Each time about 98% of the context was replaced by a summary written by the model, and nothing told me what was kept.
- **A rule held only in conversation has to win every summary.** It often will. When it does not, nothing tells you.
- **Re-anchoring takes the rule out of that contest.** The rules live in a file, an Agent Behaviour Policy, and a hook prints the file back into the context after every summary, verbatim. The rules are restored, not remembered.
- **Re-anchoring fixes forgetting, not the other two failures.** An agent that has its rules in view can still miss its own violation or argue itself into an exception. Those need a second reader and a gate.
- **A canary makes the invisible visible.** A short report, computed from the transcript, ends every few answers. If it stops appearing, the person notices before anything important goes wrong: the brown M&M.
- **The best recipe changes with every release.** The hooks this depends on arrived or changed in the last few months. Keeping the recipe current for each rule, on each platform, at each version, is work someone has to do continuously.

## What summarisation does to a session

Long agent sessions do not keep everything. When the context fills, the harness writes a summary of the conversation so far and continues from the summary. In Claude Code this is compaction, and it can be manual or automatic.

The transcript of this session records every one. Between 9 September and 9 October there were eighteen compactions, all automatic. Each started from about 780,000 to 800,000 tokens of context and replaced it with 9,000 to 19,000: on average **1.7% kept**. In total, 17.8 million tokens of conversation have been summarised away. Each summary took between 1.2 and 3.4 minutes to write.

None of that is a criticism. A summary is what makes a month-long session possible at all, and this site would not exist in its current form without it. But it changes what a rule given in conversation is. Every time a summary is written, the rule has to be judged important enough to keep, in words the summariser chooses. Often that works. You are not told when it does not.

The documentation is precise about what does survive: "Project-root CLAUDE.md survives compaction: after `/compact`, Claude re-reads it from disk and re-injects it into the session" ([memory](https://code.claude.com/docs/en/memory)). Skills that were invoked are re-injected too, but "capped at 5,000 tokens per skill and 25,000 tokens total; oldest dropped first", and context that hooks added earlier is "summarized with the rest of the conversation" ([context window](https://code.claude.com/docs/en/context-window#what-survives-compaction)). So there is already a pattern in the platform: what comes back from disk survives; what lived only in the conversation competes.

## Three ways a rule fails

A rule held by the agent it governs can fail in three different ways, and they need different fixes:

Three ways a rule fails. Re-anchoring fixes forgetting. A second reader fixes the violation the author cannot see. A gate fixes the exception the agent argues itself into.

Re-anchoring is the first and cheapest of the three, and the others depend on it: a checker that reads the rules, and a gate that enforces them, are only as good as the rules they are given. In the vocabulary of the [Agent Behaviour Policy](https://abp.sgit.ai/), re-anchoring does not change a rule's barrier. An expectation stays "a rule in prose, enforced by nobody". What changes is that the expectation is reliably in view, which is the precondition for everything else.

## Re-anchoring: the rules come back from disk

Claude Code has four documented places to do it ([hooks](https://code.claude.com/docs/en/hooks)):

| Hook | When it fires | What it can do for the policy |
|---|---|---|
| `SessionStart`, matcher `compact` | after every compaction, automatic or manual | print the whole policy back: "Claude Code adds a SessionStart hook's plain-text stdout to Claude's context" |
| `UserPromptSubmit` | before each prompt is processed, including turns the harness starts itself | add a short anchor every turn, or the full policy every Nth turn, as `additionalContext` |
| `PreCompact` | before compaction | log that it is about to happen, or block it |
| `Stop` | when the agent is about to end its turn | check that something the policy requires actually happened, and if not, send the agent back once |

The first is the heart of it. A hook with the `compact` matcher fires "after compaction", and whatever it prints goes back into the context. Point it at the policy file and the policy is back, verbatim, the moment the summary is done. This is the configuration running in this session:

```

{
  "hooks": {
    "SessionStart": [
      { "matcher": "compact",
        "hooks": [ { "type": "command", "command": "python3 ~/.claude/abp/abp.py reanchor" } ] } ],
    "UserPromptSubmit": [
      { "hooks": [ { "type": "command", "command": "python3 ~/.claude/abp/abp.py prompt" } ] } ],
    "Stop": [
      { "hooks": [ { "type": "command", "command": "python3 ~/.claude/abp/abp.py stop" } ] } ]
  }
}

```

The `reanchor` step prints a one-line header, "ABP re-anchored after compaction: v0.1 #a0d6d2. The rules below still apply, whatever the summary says", then the policy, and logs that it ran. The `prompt` step adds one line to every prompt, naming the policy, its version and its hash, so even a turn that starts from a thin summary knows the policy exists and where it lives.

The cheapest version needs no hooks at all: a line in the project-root CLAUDE.md that says "read the behaviour policy in this file before acting", since that file is re-read from disk after compaction. And the bluntest version needs no configuration: the person types "read your instructions again". Both work. The point of the hooks is that neither depends on someone remembering.

## One file, three jobs

This is where the Agent Behaviour Policy stops being a document and becomes infrastructure. The same file does three jobs:

1. **Memory.** It is what the re-anchoring hook prints back. The rules survive because they live on disk, not in the conversation.
2. **The checker's rulebook.** It is what an independent checker reads. The draft guard's numbered rule file, written by the inbox agent, is already an ABP fragment under another name.
3. **The enforcement list.** Every row carries its barrier, so the file says which rules are still expectations, and therefore which need a second reader or a gate next.

A policy can also shape memory directly. A row can say "keep decisions in `decisions.md`" or "write the sources file before drafting", which moves the important parts of a session out of the conversation, where they are summarised, and into files, where they are not. That is still an expectation, but a checkable one: a hook can see whether the file was written.

## The canary: a report that ends every few answers

Re-anchoring has a weakness of its own: you cannot see it working. A hook that silently stopped firing, a settings file that was not loaded, a policy file that was moved, all look exactly like a session where everything is fine. So the second half of the technique is a canary.

The idea is old. Van Halen's touring contract had a clause, in the middle of pages of technical requirements, asking for a bowl of M&M's with the brown ones removed. It was not vanity. As [Snopes](https://www.snopes.com/fact-check/brown-out/) and [NPR](https://www.npr.org/sections/therecord/2012/02/14/146880432/the-truth-about-van-halen-and-those-brown-m-ms) both report, it was a quick way to tell whether the venue had read the whole contract, including the parts about weight and power that kept the crew safe. Brown M&M's in the bowl meant: check everything else.

The agent version is a short status report at the end of every few answers. Here is how it looks on a phone, in this session, on its first day:

The report as it arrived on a phone, at the end of an answer in this session: the policy version and hash, re-anchors against compactions, cost, tokens, web requests, tool calls, and a measured rule.

Three design choices make it more than decoration:

- **The model does not write the numbers.** The `UserPromptSubmit` hook computes the report from the session transcript and the harness's own cost record, and hands it to the agent with the instruction to paste it. A report the model wrote from memory would be one more thing to verify.
- **The harness checks it was shown.** When a report was due, the `Stop` hook reads the end of the answer. If the report is missing it sends the agent back, once, with the block to add; if it is still missing, it lets the turn end and logs the miss. That one rule, show the report, moves from expectation to setting.
- **The person is part of the loop.** After a few days the report is expected. When it does not arrive, the question is "where is my report?", and the answers are two commands: `/abp-status` shows it now, and `/abp-reload` makes the agent read the policy again and say its version and hash.
Re-anchoring and the canary: one policy file, three hooks, two commands, and a person who notices when the report is missing.

**Re-anchoring and the canary, Mermaid source**

[rendered image](images/ra-loop.webp)

```
flowchart LR
  ABP[("ABP.md on disk<br/>versioned, hashed<br/>the session's rules")]
  subgraph H["Hooks the harness runs"]
    direction TB
    SS["SessionStart, matcher compact<br/>after every summary:<br/>print the whole ABP back"]
    UP["UserPromptSubmit<br/>every prompt: a one-line anchor<br/>every Nth: the status report,<br/>numbers already computed"]
    ST["Stop<br/>was a report due?<br/>is it in the answer?<br/>if not, ask once, then log"]
  end
  CTX["The agent's context<br/>rules restored, not remembered"]
  ANS["The answer<br/>ends with the report"]
  U["The person<br/>expects the report<br/>notices when it is missing"]
  CMD["/abp-status<br/>/abp-reload"]
  TR[("Transcript and the<br/>harness cost record")]
  ABP --> SS --> CTX
  ABP --> UP --> CTX
  TR --> UP
  CTX --> ANS --> ST
  ST -- "missing" --> CTX
  ANS --> U
  U -- "where is my report?" --> CMD --> CTX
```

Each line in the report earns its place:

| Line | What it tells you | What a surprise would mean |
|---|---|---|
| policy | the version and hash in force, and how many rules | the file changed, or a different one is loaded |
| anchor | re-anchors against compactions since the policy started | fewer re-anchors than compactions: the hook did not fire |
| cost | the session's cost, and the change since the last report | a long silent task, or a loop |
| tokens | output and cached tokens | how much context work the session is doing |
| web | searches and fetches | research happening that you did not ask for, or did not see |
| tools | tool calls and background agents | the shape of the work since the last report |
| commits | commits since the policy started, and how many were not preceded by a leak scan | a rule measured, not asserted: that number should be zero |

The last line is the one I like most. Rule 2 of this session's policy is "leak scan before every commit". The report does not ask the agent whether it complied; it reads the transcript and counts commits that were not preceded by a scan. A policy row with a number next to it is a different thing from a policy row on its own.

There is also a branded version, rendered as an image on request, for when the report is shown to someone else:

The same report as a card, rendered on request. The footer tells the reader what to do if it stops appearing.

## Living with it

The first observations, honestly, after one evening:

- **The hooks loaded mid-session.** They were added to a user settings file while the session was running, and the next prompt arrived carrying the policy's one-line anchor. The documentation says edits to hooks in settings files are "normally picked up automatically by the file watcher", and that is what happened here.
- **The first report rendered on a phone at 41 characters wide** without wrapping.
- **The re-anchor after a compaction has not been observed yet.** There has been no compaction since the hooks were installed. When there is, the `anchor` line will show it, and this article will be updated with what happened.
- **The cost line can lag.** It comes from the harness's cost record, which is written periodically rather than after every call.

We are going to live with it for a while: how often to show it (every three answers today), which lines people actually read, and what else belongs there. That is the point of running it in the session that writes about it.

## The recipe changes with the platform

Everything above depends on features that are recent. Mods, the event system the draft guard used, arrived in Claude Code v2.1.287. `onFailure: "block"`, which makes a settings hook fail closed, arrived in v2.1.295. Prompt hooks changed how they deny in v2.1.210. The `compact` matcher is what makes re-anchoring a five-line hook rather than a workaround. Six months ago the best way to re-anchor a policy was different, and six months from now it will be different again; on another platform it is different today.

So a behaviour policy row is not only a rule and its barrier. It is a rule, its barrier, and the current recipe for keeping it: on this platform, at this version, use these hooks, placed here, and expect this barrier. That table goes out of date with every release, and keeping it current, testing it, and noting what each recipe costs is real, continuous work. Some recipes carry costs of their own: a recipe that uses mods means running code the agent wrote, unsandboxed, with your permissions, which is itself a row in the policy. That is why this session's report runs on settings hooks rather than a mod.

That maintained, version-aware library of recipes is what I think people will pay for: not the policy, which they can write, but the current best way to make each row hold, curated for the tools they actually use.

## What it does not do

- **Re-anchoring does not enforce anything.** It keeps rules in view. A rule in view is still an expectation.
- **The canary is a setting, not a boundary.** It lives in a settings file the session could edit. It tells you the policy is being read; it cannot stop an agent that decides to ignore it.
- **A report can be pasted without the rules being followed.** It shows that the hooks fired and the policy was loaded, and it measures what can be measured from the transcript. For the rest you need a reader or a gate.
- **The summaries stay a black box.** Re-anchoring does not show what a summary kept. It makes what matters independent of it.

## Build your own

1. **Write the rules down as an ABP file**, short enough to re-read (a few hundred words), each rule with its barrier.
2. **Re-anchor after every compaction** with a `SessionStart` hook on the `compact` matcher that prints the file, and a one-line anchor on every prompt.
3. **Add a canary**: a short report every few answers, computed from the transcript, with a `Stop` hook that checks it was shown.
4. **Give the person two commands**: show the status, and reload the policy.
5. **Measure one rule** in the report, so the canary is also evidence.
6. **Move the rules that matter most** from expectation to a reader or a gate, using the file as the list.

*Written from a conversation between Dinis Cruz and agent@riskmandate.ai (Claude Opus 5.5, claude-opus-5-5) in the sgit.ai site session, which built and installed the re-anchoring hooks and the status report described here, on 9 and 10 October 2026, and runs under them. Compaction figures are from this session's own transcript. Claude Code behaviour is quoted from its documentation as read on 9 October 2026.*

## Threads

Agents & policySite & engineering[This article as a graph →](graphs.md#re-anchoring-agent-behaviour-policies)

### Builds on

- [A second reader the agent cannot skip: how two wrong emails became a gate on every draft](a-second-reader-the-agent-cannot-skip.md) Two emails went out in my voice despite a written rule. The fix: a hook that makes a second model approve every draft, failing closed.

[All articles](index.md) · [All graphs](graphs.md)

**Posting this article on LinkedIn?** The cover is [re-anchoring-agent-behaviour-policies.jpg](../articles/banners/re-anchoring-agent-behaviour-policies.jpg) (1920×1080, title and key ideas on it). Upload it as the article cover, paste the title, then select and copy the body from this page.

**Want the next issue by email.** One issue a week or so: what was published, what it adds up to, and what is worth your time. [Subscribe to the SGit Newsroom →](../subscribe/index.md)

[← All articles](index.md)


---

*[Site index for agents](../llms.txt) · [HTML version](https://sgit.ai/articles/re-anchoring-agent-behaviour-policies.html)*
