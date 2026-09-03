# Borrowed, Not Reinvented

Chapter 4 got the agent computing instead of guessing. Chapter 5 turned that computation into a reusable tool. This chapter is about whether the arithmetic inside it can actually be trusted — because ask Bellwood's agent to compute the confidence interval (Chapter 10) around that checkout number, or any correlation or regression, and it will very happily write the formula from scratch: clean code, a recognisable structure, a number that comes out the other end looking exactly like it should. Whether that formula is correct is a separate question, and "it looks right" is not evidence either way.

## What a library is

A **library** is code someone else already wrote, tested, and published, so that using it does not require understanding — or reimplementing — everything happening inside it. `scipy`, `pandas`, `statsmodels`, `numpy`: these are not obscure specialist tools. They are the standard machinery most professional statistical and data work is built on, maintained by people whose whole job is getting this arithmetic right, used by enough people, on enough real datasets, that the sharp edges have mostly already been found by someone else, before you ever got there.

Writing the formula by hand instead is not more rigorous. It is a fresh implementation of something that has already been implemented, checked, and re-checked thousands of times over — starting from zero, with nobody but the agent that just wrote it having looked at whether it's right.

## Why the hand-written version is the riskier one

Statistical formulas have a specific, ordinary way of going wrong: not a crash, but a plausible-looking value computed with a small, easy mistake buried in it — a variance divided by n instead of n minus one, a test assuming two groups have equal variance when they don't. Neither announces itself. Both come out the right shape of answer, just computed slightly wrong.

An established library has had exactly these mistakes found already, by the accumulated weight of everyone who has used it before you, on data stranger and more varied than yours. A version written fresh for this one occasion has had none of that. It might still be correct. It has not earned the confidence a correct answer deserves, because nothing has actually tested it yet except the same process that might have gotten it subtly wrong in the first place.

This is not a claim that hand-written code is always wrong. It is a claim about where to place your trust by default: a widely-used library starts with a track record; fresh code starts with none, and "it compiles and the number looks reasonable" is not a track record.

## The library has to be the right kind

The rule is not "any library beats no library." A package with a handful of downloads and no real usage carries almost the same risk as code written from scratch — it simply hasn't been exercised enough for its bugs to have surfaced yet. The ones worth trusting by default are the boring, extremely widely used ones: the standard statistical and numerical libraries in whatever language the agent is using, not something obscure fetched because it happened to have a convenient-sounding name. If you don't recognise the name of what was used, that is worth a direct question rather than an assumption either way.

## Using the right tool does not mean using it right

One caution, because it is easy to over-trust the moment a familiar library name appears: reaching for the standard tool is necessary, not sufficient. Chapter 3's assumption check still applies fully — a correctly-implemented statistical test, called with the wrong inputs or applied to data that doesn't satisfy what it needs to be true, produces a wrong answer just as confidently as a badly hand-written one would. The library gives you much stronger reason to trust that the arithmetic inside the function is correct than a fresh implementation would — it does not guarantee it outright; established libraries have had real bugs too, just far fewer of them, and far more eyes finding them. What a library can never promise is that its function was the right one to call, or that your data was fit to feed it. Those checks still have to happen; borrowing correct machinery is one link in the chain, not the whole of it.

## What to ask for

> "What library and function did you actually use for this — name it specifically — or did you write the calculation from scratch?"

The direct question. A specific, recognisable name is a good sign. A hand-derived formula, with no library named, is worth a follow-up.

> "If you wrote this by hand instead of using a standard library, redo it with the standard one and show me whether the answer changes."

Cheap, and it turns a vague worry into a concrete comparison — if the two agree, that's real reassurance; if they don't, you've just found something worth understanding before you trust either.

> "Is this a widely-used, well-established library for this kind of calculation, or something obscure? If you're not sure, use the most standard option available."

Closes the gap this chapter's second half is about — a library name is not automatically a reason to relax.
