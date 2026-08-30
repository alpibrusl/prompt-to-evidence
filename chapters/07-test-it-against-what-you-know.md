# Test It Against What You Already Know

Every chapter so far has been about reducing the chance a method is wrong. This one is about catching it anyway, because reducing the chance is never the same thing as reaching zero, and the last line of defence is the cheapest one in this entire book.

## The known-answer test

A **known-answer test** is running a method against a case where you already know what the correct result should be, before trusting it on the case where you don't. Build a small example by hand — a handful of rows, simple enough that you could work out the answer yourself, or one you already know from experience — and run the exact same tool against it. If it gets that case right, that's real evidence, not proof, but real evidence, that it will get your actual case right too. If it gets the known case wrong, you have just been saved from trusting it on the case that mattered, for the cost of a few minutes.

This is precisely why Chapter 5 insisted on a tool with parameters rather than a one-off script. A method that only knows how to answer today's specific question cannot be pointed at a toy example instead — there is nowhere to point it. A method built to take a case as input can be handed *any* case, including one you've rigged to have a known answer, run first, cheaply, before it ever touches the data you're actually deciding something from.

Building the known case does not need to be elaborate. Five made-up rows where you can compute the average by hand. A month of last year's real numbers where you already remember roughly what happened. A textbook example with a published answer. The bar is not rigor — it's simply *having something to check against*, which is a bar almost every real analysis currently clears zero times.

## Suspicion cuts both ways

There is a specific moment worth naming, because it is exactly when people stop being careful: the result comes back, and it's either much better than expected or much worse — and one of those two reactions is celebration, and the other is despair, and neither one is *checking*.

Treat both the same way. **A suspiciously good result and a suspiciously bad result get identical treatment: stop, and look for a bug or a data problem before you believe either one.**

The reasoning underneath this is not superstition, it's arithmetic about how often things actually happen. Genuinely enormous effects are rare — most real changes to most real systems move a number by a few percent, not by a factor of three. Bugs and data problems, on the other hand, are common; a leaked answer, a double-counted row, a comparison that silently wasn't fair, all of these are far more frequent events than a real result several times larger than anything you've seen before. When a result is extreme, the honest calculation is that it is more likely to be one of the common causes wearing an exciting costume than a rare, genuine breakthrough wearing an ordinary one. Chapters 9 and 12 will each hand you a version of this exact moment — a campaign that appears to have caused a startling lift, a model that reports startling accuracy — and the instruction there will be the same one this chapter is giving you now: extraordinary looks, on either end, earn extra scrutiny, not extra trust.

The failure mode to watch for in yourself is asymmetric relief: quietly re-checking the bad-looking results harder than the good-looking ones, because the good ones feel like they've already earned belief. They haven't. A number that flatters what you were hoping for is not thereby more likely to be correct.

## What checking actually looks like

Chapter 3 already gave you the diagnostic habit — the *shape* of a wrong-feeling result points at a different link in the chain. This chapter is where you actually use it: a suspiciously good result, check the data and the assumptions behind the method first — something is probably leaking into the answer that shouldn't be there. A suspiciously bad one, check the computation first — something in the arithmetic likely broke.

Alongside that, one plain habit worth having regardless: does the number's *size* make sense given what you already know about the situation, independent of any formal test? A conversion lift of thirty percent from changing a button's colour should not sit comfortably next to everything else you know about how much small design changes typically move a number. That discomfort is data. It is not proof of an error, but it is a completely legitimate reason to run the known-answer test before you act on the result, rather than after.

## What to ask for

> "Before you run this on the real data, build a small example where we already know the answer, run the same method on it, and show me that it gets it right."

The default request — not something reserved for results that already look suspicious.

> "This result seems unusually [good / bad] compared to what we'd normally expect. Before I act on it, check for a bug or a data problem — don't just re-explain why the number makes sense."

The direct instruction for the moment this chapter is really about. Asking it to "explain" a suspicious result invites a plausible-sounding story; asking it to check invites an actual answer.

> "Does this number's size make sense compared to similar things we've measured before? If not, why not?"

The sniff test, asked out loud rather than left as a private, easily-dismissed feeling.
