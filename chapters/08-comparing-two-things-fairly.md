# Comparing Two Things Fairly

Back to the opening example: did Bellwood's new checkout page actually beat the old one. Everything in this chapter is what has to be true for "conversion is up 12%" to mean what it sounds like it means, rather than being a number that happened to come out of a comparison that was never fair to begin with.

## What "fair" actually requires

A comparison is fair when the two groups differ in exactly one thing: the change you're testing. Everything else about them — who they are, when they arrived, what else was happening at the time — has to be, as close as possible, the same.

**Random assignment** is how this is achieved in practice: each person or unit being compared is put into group A or group B by chance, not by anything about who they are or when they showed up. This matters for a specific, mechanical reason, not a procedural one: randomness spreads every *other* difference between the groups roughly evenly, on average — age, device, time of day, how much they already liked the product. If the groups end up looking different in outcomes despite starting out alike in everything else, the one thing left to explain the gap is the change itself.

Without it, a comparison can look exactly as clean and still be worthless. Version B shown only after a certain date is really "before versus after," with everything else that changed on that date riding along uninvited. Version B shown only to people who opted into an early-access list is really "the kind of person who opts into things versus everyone else." Both produce a real, computable, entirely misleading number, and nothing about the number itself gives away which kind you have.

This is exactly what turned up in Bellwood's number from Chapter 1. The new checkout page had never been shown to a random half of visitors at all — it simply went live for everyone on March 15. By the time Chapters 3 through 7 had made sure the arithmetic was sound, the comparison underneath it still wasn't: "conversion is up 12%" meant "the four weeks after March 15 beat the four weeks before it," a real number, honestly computed by then, quietly answering a comparison nobody had actually run.

<div style="margin:1.6rem 0;">
<svg viewBox="0 0 620 232" width="100%" style="display:block;" xmlns="http://www.w3.org/2000/svg">
<text x="295" y="16" text-anchor="middle" font-family="EB Garamond, Georgia, serif" font-size="10.5" letter-spacing="0.06em" fill="#9a9a9a">WHAT BELLWOOD ACTUALLY COMPARED</text>
<circle cx="600" cy="12.5" r="7" fill="none" stroke="#8a3324" stroke-width="1.2"/>
<path d="M596.2,8.7 L603.8,16.3 M603.8,8.7 L596.2,16.3" fill="none" stroke="#8a3324" stroke-width="1.2"/>
<rect x="20" y="25" width="290" height="44" fill="none" stroke="#1a1a1a" stroke-width="1.2"/>
<text x="165" y="52" text-anchor="middle" font-family="EB Garamond, Georgia, serif" font-size="12.5" fill="#1a1a1a">BEFORE — 4 weeks</text>
<rect x="310" y="25" width="290" height="44" fill="none" stroke="#1a1a1a" stroke-width="1.2"/>
<text x="455" y="52" text-anchor="middle" font-family="EB Garamond, Georgia, serif" font-size="12.5" fill="#1a1a1a">AFTER — 4 weeks</text>
<line x1="310" y1="20" x2="310" y2="74" stroke="#666" stroke-width="1.2" stroke-dasharray="3,3"/>
<text x="310" y="88" text-anchor="middle" font-family="EB Garamond, Georgia, serif" font-size="10.5" font-style="italic" fill="#444">March 15 — new page ships to everyone, all at once</text>
<text x="295" y="128" text-anchor="middle" font-family="EB Garamond, Georgia, serif" font-size="10.5" letter-spacing="0.06em" fill="#9a9a9a">A FAIR COMPARISON</text>
<path d="M596,124 L599,130 L604,120" fill="none" stroke="#8a3324" stroke-width="1.4"/>
<rect x="20" y="140" width="580" height="26" fill="none" stroke="#1a1a1a" stroke-width="1.2"/>
<text x="32" y="157" font-family="EB Garamond, Georgia, serif" font-size="12.5" fill="#1a1a1a">GROUP A — existing page</text>
<rect x="20" y="172" width="580" height="26" fill="none" stroke="#1a1a1a" stroke-width="1.2"/>
<text x="32" y="189" font-family="EB Garamond, Georgia, serif" font-size="12.5" fill="#1a1a1a">GROUP B — new page</text>
<text x="310" y="223" text-anchor="middle" font-family="EB Garamond, Georgia, serif" font-size="10.5" font-style="italic" fill="#444">Same eight-week window, both groups running the whole time — assignment by chance, not by date.</text>
</svg>
</div>

## Could this just be noise?

Even with a genuinely fair comparison, one more question has to be answered before the gap means anything: could a difference this size have shown up by chance alone, even if the two versions were actually identical?

This is Chapter 2's noise, reappearing in its most consequential form. Flip a coin twenty times and you will rarely get exactly ten heads — small, meaningless wobbles are the normal behaviour of anything measured on a limited sample, not evidence of anything. **Statistical significance** is the answer to a precise question: if the two versions truly made no difference at all, how surprising would a gap this size actually be? A result is called significant when the honest answer is *quite surprising* — when a gap this large would be unlikely to appear from noise alone.

Two things about this are worth being exact on, because both are commonly gotten backwards. Significance is not a measure of how big or important the effect is — a tiny, commercially irrelevant difference can be statistically significant if the sample is large enough, and a large, genuinely important one can fail to reach significance if the sample is small. And significance is not the probability that the effect is real — it's the probability of seeing a gap this size *if there were truly no effect at all*, which is a related but distinctly different question from the one people usually think they're asking.

Sample size is what connects this back to Chapter 2 directly: more data reduces noise, which is exactly why a small test struggles to tell a real small effect apart from a lucky fluctuation, and a larger one can. If you're testing something you expect to move the number only slightly, you need more data to see it clearly than if you're testing something you expect to move it dramatically — ask what size of effect the test is actually built to detect, not just whether it ran long enough to feel thorough.

## Two traps specific to this kind of test

**Stopping the moment it looks good.** Checking a running test constantly and calling it the instant the result crosses into "significant" territory produces significant-looking results far more often than the test's own math assumes it should — because among all the natural ups and downs a fair test goes through on its way to a stable answer, you're choosing to stop at whichever passing moment happens to look best. The fix is procedural, not statistical: decide the sample size or the running time in advance, before you look at a single result, and hold to it.

**Testing many things and reporting the one that worked.** Test twenty different metrics, or twenty different customer segments, against the same change, and — by chance alone — roughly one of them tends to look significant even when nothing real is happening anywhere. This is not dishonesty, usually; it's simply what "significant" starts to mean once you've quietly given chance twenty tries to produce one for you. Decide beforehand what you're actually measuring, or treat anything found by scanning afterward as a lead to test properly next, not as a result to act on now.

Bellwood ran the honest version once the before/after problem was caught: a randomly-assigned holdout, decided and locked in before the retest launched, held for a fixed window regardless of how the numbers looked partway through. Chapter 10 picks up exactly where that retest left off.

## What to ask for

> "Was this actually randomly assigned — could anything about who ended up in each group, other than the change itself, explain a difference in outcomes?"

The fairness question, asked directly rather than assumed from a clean-looking dashboard.

> "How many people or events is this based on, and is that enough to tell a real effect this size apart from ordinary noise?"

The sample-size question. "Enough to feel confident" and "enough, given how small an effect we're trying to detect" are different standards, and only one of them is checkable.

> "Was the sample size or running time decided before the test started, or did we stop once it looked good? And were we testing one specific metric, or several — and is this the one that happened to come out significant?"

Both traps in one question. An honest answer to either half is worth having before you act on the result.
