# Make It Compute, Not Guess

Chapter 3 named the computation link in the chain, and gave it one line: arithmetic done by pattern-matching instead of by running actual code. This chapter is that line, in full, because it is the single most avoidable way a number in this book's sense fails to become one.

## Why the agent is worst at exactly the thing it sounds most confident about

An agent produces a response one piece at a time, each one chosen because it is the most plausible continuation of everything written so far. For most of what it writes, *most plausible* and *correct* are the same thing, which is why it reads as fluent and reliable. Arithmetic is the case where they quietly come apart.

A calculator does not predict what 47 times 83 is. It computes it, mechanically, tracking every digit through every step, the same way on the millionth calculation as on the first. An agent asked to state that same product in the middle of a sentence is doing something different: producing the number that *looks like* the kind of number that would follow, built from patterns in everything it has read before, not from mechanically carrying digits the way a calculator does by construction. For short, common, heavily-seen arithmetic — small sums, round numbers — this usually lands on the right answer anyway, because the pattern and the truth line up often enough. Chain several steps together, or use numbers that aren't round, or compute something with more than one intermediate quantity — a percentage of a percentage, a rate normalised by a shifting denominator — and the pattern and the truth have more room to separate, quietly, with nothing in the tone of the answer to tell you it happened.

That last part is the one to sit with. A wrong number produced this way carries exactly the same confident, unhedged delivery as a right one. There is no stammer, no qualifier, no visible seam. This is the same failure this book's companion volume calls *confidence that is not evidence*, showing up here in its rawest form: not a claim about how code behaves, but a claim about what a number *is*, stated with total fluency regardless of whether it's true.

## The fix is mechanical, not motivational

Asking the agent to "double-check" or "be careful" does not reliably help, because the thing that produced the wrong answer — pattern completion — is also the thing that would "double-check" it, using the same mechanism, sometimes landing on the same wrong number again and sometimes a different, equally confident, equally wrong one.

The actual fix is not more care. It is a different method entirely: **have the agent write code that performs the calculation, and run it, rather than asking it to state the result of a calculation directly.** Code execution has the property text generation doesn't — a script that computes a percentage does the arithmetic the same mechanical way every single time, regardless of how plausible or implausible the answer looks. This is not a nicer way of getting the same thing. It is a categorically different process, and it is the one that actually deserves your trust.

## What "trivial" actually means

This does not mean demanding a Python script to answer "how many rows are in this file." That is retrieval, not inference — the agent is reading a count, not deriving one through several steps of reasoning, and the risk this chapter is about does not apply to it in the same way.

Genuine computation is different: percentages, rates, anything statistical, anything that chains more than one operation together to reach the final figure. That is where the rule applies without exception. If you are ever unsure which category something falls into, treat it as the second one. The cost of asking for code on a calculation simple enough not to have needed it is nothing. The cost of skipping that ask on one that did need it is a wrong number that will sit underneath a decision looking exactly as trustworthy as a right one would have.

## How to tell whether it actually happened

You cannot read code well enough to verify that a calculation was implemented correctly — that is a real skill, and Chapters 6 and 7 are what to do about it (established libraries, and testing against a case where you already know the answer). But there is a much lower bar you can check yourself, right now, without reading a line: **did execution happen at all.**

Ask directly, and expect one of two things back: an actual block of code together with the output it produced, or a plain statement of what ran it. "Show me the code that produced this number, and what it printed" is a fair, answerable request regardless of your own fluency — you are not being asked to judge whether the code is right, only whether a real run happened and produced this number, rather than the number having been typed as though a run had happened. If the agent cannot produce that trail on request, treat what you have as a guess wearing the outfit of an answer, no matter how confident it sounded going in.

## What to ask for

> "Don't compute this in your response directly — write code that performs the calculation, run it, and show me the result the code actually produced, not a restated version of it."

The core instruction. Ask for it by default on anything past simple retrieval, not only when a number looks suspicious.

> "Was this number computed by running code, or estimated from a pattern? If it was estimated, redo it properly."

A direct question with a direct answer, useful for anything that arrived without a visible trail.

> "Compute this two ways — independently, in separate code — and confirm the two results actually match."

Cheap, and it catches the case where the code itself has a bug rather than the number being an outright guess; Chapter 7 is the fuller version of this habit.
