# When an AI assistant keeps making mistakes, more rules make it worse

**The point.** A friend checked a software tool using several agents (AI programs that do tasks by themselves), one writing and others checking. The tool held up: 812 attacks produced no failures. The process around it kept breaking: "Every mistake added a rule, and every new rule caused new mistakes." The answer is to stop adding rules and build small, tested pieces that make each mistake impossible, using plain files and version history.

**An example.** When a command failed, the software running the agents did not save its output and cut out the middle, so a whole test run was lost. The fix is not a rule saying "save the output". It is one small script that every command goes through, which writes the output to a file before anything reads it.

**Why it matters to you.** Asked whether all this rigour was overdoing it, the author says: for the process, yes; for the intent, no. If you are not getting faster, complexity is winning, and the answer is to slow down and break the work into small pieces.

**If you remember one thing.** When a rule fails, replace it with something that makes the mistake impossible, then delete the rule.

**Words used.**
- **Compaction:** a long AI conversation replaced by a short summary, losing detail.
- **Wardley map:** a chart of a system's parts, showing which are custom-made and which are standard products.
