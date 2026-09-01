# Measuring What You Did

Bellwood's marketing team reports that sales rose 18% in the month after their spring campaign launched. They also rose 15% in the same month the year before, when no campaign existed at all.

That second sentence is the entire chapter. The first one answers a question nobody actually asked — *did anything happen after the campaign* — and the real question, *did the campaign cause it*, is still sitting there unanswered, wearing the first question's clothes.

## The question a report never quite answers

"Sales went up after the campaign" and "the campaign caused sales to go up" are different claims, and the second one is the only one worth anything when you're deciding whether to spend the money again. The first is true almost by default — something is always happening after any given date, because time only moves one direction. The second requires knowing what would have happened *without* the campaign, and comparing that against what actually happened with it.

## The counterfactual you cannot see

A **counterfactual** is what would have happened if the thing you did had not happened — the sales you would have gotten with no campaign at all, running in parallel to the world where you ran one. This is the fundamental difficulty underneath everything in this chapter: you never get to observe it directly. You only ever see the one world that actually happened. Every method in this chapter is really a different way of building a stand-in for the world you didn't get to see.

Before-and-after uses last month as that stand-in, silently. It is usually a poor one, because most businesses were already moving up or down for reasons that have nothing to do with this particular campaign — growth, season, a slow general trend — and before-and-after credits all of that movement to whatever changed most recently.

## What quietly explains it instead

A **confound** is something that affects both whether — or when — you ran the campaign and the outcome you're measuring, creating the appearance of a relationship that isn't really about the campaign at all. Holiday timing is the classic one: campaigns often launch before a holiday on purpose, and sales rise before a holiday regardless of any campaign; measuring the two together credits the campaign with a lift the calendar was going to produce anyway. A competitor's outage during the same window, a price change that shipped the same week, a general trend that was already climbing — all confounds, all invisible in a report that only shows before and after.

Finding a confound is not a chore you do once someone else raises the possibility — it's worth doing to your own result, on purpose, before you present it. The useful question is not *does anything here contradict my story* but the sharper version of it: *what, if it turned out to be true, would prove my story wrong* — and then going to check whether that thing is true. A campaign result that survives you actively trying to break it is worth far more than one nobody ever tried to.

This is Chapter 8's fairness question again, in a harder setting. An A/B test can usually engineer its way to a fair comparison through random assignment. A campaign, launched once, to everyone, at a moment you chose for business reasons, rarely gets that gift by accident — which is exactly why this chapter needs more than that one.

It is also where Chapter 7's suspicion cuts both ways rule earns its keep hardest. A campaign report crediting a startling lift — a number that dwarfs anything the same campaign type has produced before — is, precisely because confounds are this easy to miss here, more often a confound wearing a success story than an actual breakthrough in what marketing can do. Treat the startling number the way that chapter said: as a reason to look harder for what else changed, not as a reason to celebrate first and check later.

## Building a fair comparison, without a true experiment

Three approaches, genuinely different in strength, and worth being honest about which one you actually have.

**A randomized holdout** is the strongest available option, and the one most people don't realise is still open to them: deliberately withhold the campaign from a small, randomly-chosen slice of the audience, and compare that group against everyone else. This turns the campaign into exactly the kind of comparison Chapter 8 already covered — the same logic, the same strength of evidence, because the mechanism producing a fair comparison is identical. The one requirement is that the decision to hold a group out has to be made *before* the campaign launches. You cannot reconstruct a randomized holdout after the fact from data that was never collected that way.

**A comparable, unaffected group** is the next best thing when a true holdout wasn't set up in advance: a region, store, or segment that didn't receive the campaign, compared against one that did. This is real evidence, but weaker evidence — the two groups weren't randomly split, so any other way they differ (one region simply performing better than another, for reasons that have nothing to do with the campaign) can still confound the comparison. Naming which specific differences might explain the gap instead of the campaign is part of using this method honestly, not an optional extra.

**Extrapolating the prior trend** is the weakest of the three, and often the only thing available after the fact: project forward what the trend already looked like before the campaign, and compare the actual result against that projection rather than against a flat "before" number. It is a real improvement over plain before-and-after. It remains fully exposed to anything else that changed during the same window — the confound problem, in undiluted form.

The order these are listed in is not incidental. It runs from *decided in advance, strong evidence* to *reconstructed afterward, weak evidence*, and the single highest-leverage habit in this entire chapter is choosing the first one before the next campaign launches, rather than reaching for the third one after this one has already run.

<div style="margin:1.6rem 0;">
<svg viewBox="0 0 660 300" width="100%" style="display:block;" xmlns="http://www.w3.org/2000/svg">
<defs>
<marker id="pte3-arrow" viewBox="0 0 6 6" refX="5.5" refY="3" markerWidth="7" markerHeight="7" orient="auto">
<path d="M0,0 L6,3 L0,6" fill="none" stroke="#1a1a1a" stroke-width="1.1"/>
</marker>
</defs>
<text x="330" y="18" text-anchor="middle" font-family="EB Garamond, Georgia, serif" font-size="10.5" letter-spacing="0.06em" fill="#9a9a9a">EVIDENCE STRENGTH, RANKED</text>
<rect x="20" y="40" width="185" height="62" fill="none" stroke="#1a1a1a" stroke-width="1.2"/>
<text x="112.5" y="64" text-anchor="middle" font-family="EB Garamond, Georgia, serif" font-size="12.5" font-weight="600" fill="#1a1a1a">RANDOMIZED</text>
<text x="112.5" y="80" text-anchor="middle" font-family="EB Garamond, Georgia, serif" font-size="12.5" font-weight="600" fill="#1a1a1a">HOLDOUT</text>
<text x="112.5" y="95" text-anchor="middle" font-family="EB Garamond, Georgia, serif" font-size="9.5" fill="#666">Strongest — decided in advance</text>
<rect x="235" y="112" width="185" height="62" fill="none" stroke="#1a1a1a" stroke-width="1.2"/>
<text x="327.5" y="136" text-anchor="middle" font-family="EB Garamond, Georgia, serif" font-size="12.5" font-weight="600" fill="#1a1a1a">COMPARABLE,</text>
<text x="327.5" y="152" text-anchor="middle" font-family="EB Garamond, Georgia, serif" font-size="12.5" font-weight="600" fill="#1a1a1a">UNAFFECTED GROUP</text>
<text x="327.5" y="167" text-anchor="middle" font-family="EB Garamond, Georgia, serif" font-size="9.5" fill="#666">Weaker — not randomly split</text>
<rect x="450" y="184" width="185" height="62" fill="none" stroke="#1a1a1a" stroke-width="1.2"/>
<text x="542.5" y="208" text-anchor="middle" font-family="EB Garamond, Georgia, serif" font-size="12.5" font-weight="600" fill="#1a1a1a">TREND</text>
<text x="542.5" y="224" text-anchor="middle" font-family="EB Garamond, Georgia, serif" font-size="12.5" font-weight="600" fill="#1a1a1a">EXTRAPOLATION</text>
<text x="542.5" y="239" text-anchor="middle" font-family="EB Garamond, Georgia, serif" font-size="9.5" fill="#666">Weakest — reconstructed afterward</text>
<line x1="205" y1="71" x2="233" y2="143" stroke="#1a1a1a" stroke-width="1.1" marker-end="url(#pte3-arrow)"/>
<line x1="420" y1="143" x2="448" y2="215" stroke="#1a1a1a" stroke-width="1.1" marker-end="url(#pte3-arrow)"/>
<text x="330" y="278" text-anchor="middle" font-family="EB Garamond, Georgia, serif" font-size="10.5" font-style="italic" fill="#444">Choose from the top of this list before the campaign launches — the bottom is what's left after it already has.</text>
</svg>
</div>

## What to ask for

> "Was any part of the audience deliberately held out of this campaign, so we have a real comparison group? If not, can we set that up before the next one launches?"

Forward-looking, and the question most likely to actually change what happens next time rather than only diagnosing what already happened.

> "What else changed around the same time as this campaign — seasonality, competitors, pricing, anything — that could explain some or all of this result instead of the campaign itself?"

The confound question, asked directly rather than left for someone to notice by accident.

> "Compared to what, exactly — last month, the same month last year, a region that didn't get the campaign? And how strong is that specific comparison, versus the alternatives?"

Forces the counterfactual being used into the open, and asks for an honest word on how much it's actually worth.
