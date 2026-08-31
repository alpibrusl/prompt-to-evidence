# The Tool, Not the Answer

Chapter 3 introduced the move: ask for the general method, and treat today's specific question as one input to it. This chapter is what that actually looks like in practice, and how to tell whether you got it.

## The test that actually matters

Here is the concrete question to ask about anything computed for you: **if next month arrived with different numbers, would this same code still work — or would someone have to go back in and edit it?**

A script written to answer one specific question has the answer's shape baked into its own logic. Ask Bellwood's agent for "checkout conversion rate for March, for mobile visitors" and it is entirely possible to get back code that works, produces the right number for March and mobile, and would need to be rewritten — not re-run, rewritten — to answer the same question about April, or about desktop visitors. That code is not a tool. It is the answer, dressed up as code, and it inherits every weakness a plain one-off answer has: nobody checked what it assumes, because there was never a second case to check it against.

A **parameter** is the part that separates cleanly: the values that change from one run to the next — the month, the device type, the visitor segment — kept apart from the logic that computes the answer once those values are supplied. "Checkout conversion rate, for a given month and a given visitor segment" is a tool with two parameters. "Checkout conversion rate in March, for mobile" is that same tool with the parameters already baked in and welded shut. The computation inside might be identical in both cases. Only one of them can be handed a different month without being rebuilt from scratch.

## Why this is not a matter of taste

It would be easy to file this under code style — cleaner, more elegant, a nice-to-have. It isn't. Three concrete things go wrong without it, none of them cosmetic.

**You lose the ability to test it.** Chapter 7 is about checking a method against a case where you already know the right answer before trusting it on the case you don't. That only works if the method can *take* a different case as input. A script wired to March and mobile cannot be pointed at a toy example with a hand-checkable answer — there is nothing to point, because nothing about it takes a case as an argument in the first place. Testing and parameters are not two separate good habits. The second is a precondition for the first.

**Consistency across time quietly breaks.** If Bellwood's checkout conversion rate is rebuilt from scratch every month rather than the same tool re-run with a new date, nothing guarantees the method stayed the same between them — a rounding choice, a filter, a definition of "conversion," each rewritten slightly differently without anyone deciding to change it. The trend line built from those numbers is comparing months that were never actually computed the same way, which is a subtler, quieter version of the unfair comparison Chapter 8 spends a full chapter on.

**Assumptions stay hidden.** Chapter 3 named this once, in passing; this is where it actually gets fixed. A general tool has to declare, as parameters, what it needs — which forces the assumptions behind it into a form you can actually see and question. A one-off script can bury the same assumption three lines deep inside logic nobody is looking at, because nothing about its shape demands it be stated up front.

## What to look for

You do not need to read the code to apply this chapter. You need to be able to ask one question and recognise whether the answer describes a tool or an answer wearing code as a costume:

**"What are the parameters — the things that change between runs — and what's the logic that stays fixed regardless?"**

A real tool answers this cleanly: here are the two or three inputs, here is what happens to them once supplied. A disguised one-off answer produces a hedge, a re-explanation of March and Spain specifically, or code where the values you'd expect to be parameters turn out to be typed directly into the middle of the logic. That is the tell, and you do not need to read a single further line to have caught it.

## What to ask for

> "Don't just answer this — write it as a function with the month and the segment as parameters, so it can be re-run for any month or segment without editing the code."

The default request, not a special one reserved for when you already suspect a problem.

> "What are the parameters here, and what would I need to change to run this for a different time period or a different group?"

The verification question. A clean, short answer means you got a tool. A shrug, or an answer describing what the code does specifically for this case, means you didn't.

> "Now run this same function against last month as well, and show me both results side by side."

The cheapest real test of whether it's actually reusable — asking it to prove the claim rather than state it.
