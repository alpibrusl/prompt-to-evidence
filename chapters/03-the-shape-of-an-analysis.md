# The Shape of an Analysis

Bellwood's growth team has been burned by this before. Someone asks for the conversion rate, the agent finds a column that looks right, computes a percentage, and hands it back — clean, plausible, three decimal places of confidence. Only later does it come out that the column counted *added to cart*, not *completed purchase*, and the real conversion rate was a third of what everyone had been discussing in meetings for a week. It's the kind of mistake this chapter exists to catch before it reaches a number like the one in Chapter 1.

Nothing broke. Every step ran correctly. The chain connecting the question to the number simply had a weak joint, and a weak joint produces a perfectly well-formed wrong answer.

## The chain, revisited

Chapter 1 named it: a question, then data, then a method applied to that data, then a computation, then a number, then a decision. Six links, and the point of this chapter is what happens at each one — because "the analysis is wrong" is not a diagnosis, it is a shrug with extra steps. *Which link* is wrong is a question with a checkable answer, and knowing the shape is what lets you ask it.

Two moves matter more than the rest, and they sit right at the start of the chain, before any computation happens at all.

## Generalize before you compute

The instinct, reasonably, is to answer the question in front of you: *what was our conversion rate last month.* Resist answering it directly. Ask instead: *what is the general method for computing a conversion rate, for any month, any segment* — and treat "last month" as simply the one input you happen to be running it against today.

This is not pedantry. A calculation built to answer one specific question hides its own assumptions inside itself, because nothing forces them into the open. A general method has to state, out loud, what it needs: which column counts as a completed purchase, what counts as the denominator, what date range means "a month." Writing the general version is what makes those choices visible enough to check — and checkable is the entire subject of this book. Chapter 5 is this idea, in full, as the discipline for how the agent should actually work.

## Check that your data fits

Having a general method is only half the move. The other half, easy to skip because it feels like a formality, is confirming that *this specific data* actually satisfies what the method assumes about it.

An **assumption**, in the sense this book uses the word, is a condition that has to hold about the data for a method's output to mean what it claims to mean. Every method has some, whether or not anyone states them. A method that computes "average order value per customer" assumes one row per order, not one row per line item — feed it line-item rows and it will compute something real, just not that. A method comparing two groups assumes the groups are actually comparable, which is Chapter 8's entire subject. A method treating five weekly check-ins from the same person as five independent data points is quietly overcounting that one person's opinion by five, which is Chapter 2's noise-versus-bias distinction wearing a different coat.

None of these failures look like failures. The method runs. It returns a number in the range you expected. The mismatch between what the data actually is and what the method assumed it was is invisible from the output alone — which is exactly why it has to be checked *before* the computation runs, not inferred afterward from whether the answer feels right.

## The rest of the chain, briefly

The other four links get full treatment later; here is where each tends to snap.

**Data.** Missing rows, wrong types, a field that quietly changed meaning. Chapter 13.

**Method.** Reimplemented instead of borrowed, or borrowed but applied outside the conditions it was built for. Chapters 6 and 7.

**Computation.** Arithmetic done by pattern-matching instead of by running actual code. Chapter 4.

**Number.** A number is the output of the first four links, nothing more. It is not yet evidence — Chapter 1 already made this the whole book's opening point, and the rest of this chapter is what "not yet" actually consists of.

**Decision.** The only link that was ever the actual goal. Everything before it exists to make this one defensible.

## Diagnosing a joint, not guessing at the whole

The useful habit this chapter is building toward: when a result feels off, you are not stuck choosing between "trust it" and "distrust it" as a single vague judgement. You can ask which specific link is the suspect, and the kind of "off" tells you where to look first.

A result that is suspiciously *good* — a lift far bigger than anything reasonable, an accuracy that seems too clean — points first at the data-fit and method links: something is probably leaking information into the answer that shouldn't be there. A result that is suspiciously *bad*, or simply inexplicable, points first at the computation link: something in the arithmetic likely broke. Chapter 7 makes this into a full habit; the point to take now is narrower — the shape of the wrongness is itself a clue about where in the chain to look, and "somewhere" is never the only available answer.

## What to ask for

> "State the general method you're using here in one sentence — not the answer for this case specifically, but the rule that would produce an answer for any similar case."

Forces the generalising move into the open, where you can actually inspect it.

> "What does this method assume has to be true about the data — one row per what, independent of what, covering what date range — and does our data actually satisfy that?"

The assumption check, asked directly rather than hoped for.

> "If this number turns out to be wrong, which link in the chain — the data, the method, the computation — is most likely to be where it broke?"

Turns a vague doubt into a specific, checkable place to look next.
