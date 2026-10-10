# Stopping an AI assistant forgetting its rules

**The point.** When a long AI conversation fills up, the software swaps it for a short summary the AI writes, and a rule given only in conversation can vanish unnoticed. The article's fix, re-anchoring, keeps the rules in a file that the software pastes back after every summary, so they are restored, not remembered. A short status report every few answers is a warning light: if it stops appearing, something was not read.

**An example.** The session behind the author's site was summarised eighteen times in a month, each time keeping on average 1.7% of what it replaced. Its report measures one rule, "leak scan before every commit" (check for secrets before saving work). Rather than asking the AI, it counts saves with no scan before them. That number should be zero.

**Why it matters to you.** Re-anchoring keeps rules in view but does not enforce them; an AI can still miss its own mistake or argue itself into an exception. The right set-up also changes with each software release.

**If you remember one thing.** Keep the rules in a file that comes back after every summary, and watch for the report that shows it did.

**Words used.**
- **Compaction:** the software summarising a long conversation to make room.
- **Hook:** a step the software runs automatically, such as after every summary.
- **Canary:** a regular signal whose absence warns you something is wrong.
