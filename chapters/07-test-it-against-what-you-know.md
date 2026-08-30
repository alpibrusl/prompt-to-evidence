# Test It Against What You Already Know

Every chapter so far has been about reducing the chance a method is wrong. This one is about catching it anyway, because reducing the chance is never the same thing as reaching zero, and the last line of defence is the cheapest one in this entire book.

## The known-answer test

A **known-answer test** is running a method against a case where you already know what the correct result should be, before trusting it on the case where you don't. Build a small example by hand — a handful of rows, simple enough that you could work out the answer yourself, or one you already know from experience — and run the exact same tool against it. If it gets that case right, that's real evidence, not proof, but real evidence, that it will get your actual case right too. If it gets the known case wrong, you have just been saved from trusting it on the case that mattered, for the cost of a few minutes.

This is precisely why Chapter 5 insisted on a tool with parameters rather than a one-off script. A method that only knows how to answer today's specific question cannot be pointed at a toy example instead — there is nowhere to point it. A method built to take a case as input can be handed *any* case, including one you've rigged to have a known answer, run first, cheaply, before it ever touches the data you're actually deciding something from.

Building the known case does not need to be elaborate. Five made-up rows where you can compute the average by hand. A month of last year's real numbers where you already remember roughly what happened. A textbook example with a published answer. The bar is not rigor — it's simply *having something to check against*, which is a bar almost every real analysis currently clears zero times.

## Suspicion is not a special mode

Extreme results are not the only ones worth doubting. They are simply the ones that announce themselves — startling enough to trigger doubt without you having to go looking for it. An ordinary, unremarkable-looking number can be wrong for exactly the same reasons — a leak, a bug, an unfair comparison — and it gets a pass for no better reason than that it happened to land somewhere plausible. The honest posture is not *trust it unless something about it looks extreme*. It's suspicion as the default setting for every result, and what an extreme one actually earns is not a monopoly on scrutiny — only how loudly it demands it.

Constant suspicion sounds exhausting, and would be, if it meant re-deriving every number from first principles. It doesn't have to. The workable version is the same discipline as the known-answer test above, run continuously instead of once: a **consistency check** — does this result agree with something else you already know, arrived at a different way? Does this month's number sit near the trend the surrounding months have been showing, even though nothing about it looks dramatic on its own? Does a total match the sum of its parts, computed independently? Does it roughly match what a colleague, a different report, or your own general sense of the business would have predicted before seeing it? When two things that should roughly agree don't, that disagreement deserves exactly the attention an extreme result gets — even though neither number, looked at alone, seemed wrong.

This is deliberately more sustainable than treating distrust as an occasional event reserved for outliers. A consistency check needs no particular expertise. The question is simply *does this agree with that*, and a mismatch is the finding, regardless of which of the two you would have been inclined to trust more going in.

## Suspicion cuts both ways

One instance of this is common enough, and easy enough to get exactly backwards, that it earns its own name: the result comes back, and it's either much better than expected or much worse — and one of those two reactions is celebration, and the other is despair, and neither one is *checking*.

Treat both the same way. **A suspiciously good result and a suspiciously bad result get identical treatment: stop, and look for a bug or a data problem before you believe either one.**

The reasoning underneath this is not superstition, it's arithmetic about how often things actually happen. Genuinely enormous effects are rare — most real changes to most real systems move a number by a few percent, not by a factor of three. Bugs and data problems, on the other hand, are common; a leaked answer, a double-counted row, a comparison that silently wasn't fair, all of these are far more frequent events than a real result several times larger than anything you've seen before. When a result is extreme, the honest calculation is that it is more likely to be one of the common causes wearing an exciting costume than a rare, genuine breakthrough wearing an ordinary one. Chapters 9 and 12 will each hand you a version of this exact moment — a campaign that appears to have caused a startling lift, an ML model that reports startling accuracy — and the instruction there will be the same one this chapter is giving you now: extraordinary looks, on either end, earn extra scrutiny, not extra trust.

The failure mode to watch for in yourself is asymmetric relief: quietly re-checking the bad-looking results harder than the good-looking ones, because the good ones feel like they've already earned belief. They haven't. A number that flatters what you were hoping for is not thereby more likely to be correct.

## What checking actually looks like

Chapter 3 already gave you the diagnostic habit — the *shape* of a wrong-feeling result points at a different link in the chain. For the extreme case specifically: a suspiciously good result, check the data and the assumptions behind the method first — something is probably leaking into the answer that shouldn't be there. A suspiciously bad one, check the computation first — something in the arithmetic likely broke. For an ordinary-looking result that simply failed a consistency check, the diagnostic habit is the same one, applied more broadly: find the specific link where the two disagreeing numbers diverge, rather than assuming the newer or less-trusted one is automatically the culprit.

## What to ask for

> "Before you run this on the real data, build a small example where we already know the answer, run the same method on it, and show me that it gets it right."

The default request — not something reserved for results that already look suspicious.

> "This result seems unusually [good / bad] compared to what we'd normally expect. Before I act on it, check for a bug or a data problem — don't just re-explain why the number makes sense."

The extreme-result instruction. Asking it to "explain" a suspicious result invites a plausible-sounding story; asking it to check invites an actual answer.

> "Even though this doesn't look unusual, does it agree with [a related number, a different report, last period's trend]? If they don't roughly match, find out why before either one gets used."

The consistency check, asked routinely rather than only when something already feels wrong — which is the actual point of this chapter, not just the extreme-result case.
