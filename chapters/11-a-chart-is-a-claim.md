# A Chart Is a Claim

The same ten numbers can be drawn a dozen honest ways and look like a dozen different stories. Nothing about a chart being clean, professional, and correctly labelled tells you whether the particular way it was drawn happens to be the one that flatters the point someone wanted to make.

## Every choice in a chart is an editorial one

A chart is not a neutral photograph of data. Someone — or, now, an agent acting on a request — decided where the axis starts, which dates to include, whether to show every point or a smoothed average, what to compare against what. None of those choices are forced by the data itself; each one is a decision, and each decision can tell the same underlying numbers as a dramatic story or a boring one without a single value being altered.

**Where the axis starts.** A line that climbs gently from 48 to 52 looks like a modest change on an axis running from 0 to 100, and looks like a dramatic one on an axis running from 47 to 53. Neither is automatically the lie — a temperature chart or a stock price often genuinely needs an axis that doesn't start at zero, because zero isn't a meaningful floor for that quantity. The question worth asking isn't "does it start at zero," it's "would the story change if it did" — and if the honest answer is yes, that's worth knowing before you repeat the story.

**Which dates are shown.** A chart covering the three best weeks of the year tells a real, accurate, entirely misleading story about the year. The fix is not complicated: ask what the same chart looks like extended backward and forward, and treat a chart that was never shown that way as an incomplete one rather than a false one — the distinction rarely matters to the decision either way.

**What got averaged away.** An **aggregation** is a single summary value standing in for many underlying ones — a monthly average standing in for thirty days of real numbers, an overall trend line standing in for several groups that may not be moving together at all. This is Chapter 2's noise-and-bias problem again, wearing a picture instead of a table: a single smooth line can hide wild day-to-day swings, and an overall average can hide two groups moving in opposite directions that happen to cancel out into a flat-looking line. The chart is not wrong. It is simply answering a much narrower question than "what happened" — and it's worth knowing which narrower question that actually was.

## One chart, one point

There is a failure mode that has nothing to do with dishonesty and does almost as much damage: a chart genuinely trying to be thorough, carrying eight metrics across three axes, that nobody can actually read. If understanding what it claims takes ten minutes of someone talking you through it, it has already failed at the one thing a chart is for — the entire advantage a chart has over a table is that a reader takes in the shape of an answer in a glance, and a chart that demands a guided tour has given up that advantage while keeping all of a table's density.

This is not only a clarity problem. It's the same trust problem the rest of this chapter is about, arriving from a different direction. The test two sections up — would the story hold up drawn the plain, obvious way — needs a single identifiable story to test in the first place. Ten overlapping lines on dual axes have no one story; they have as many as there are lines, and no one has the patience to audit each of them, so the whole thing gets nodded past instead of actually read. Complexity doesn't need to be dishonest to have the same effect as dishonesty: nothing about it gets checked, because nothing about it is checkable in the time anyone is actually willing to spend.

Ask of a chart the same question Chapter 12 will ask of a model: does the complexity earn its keep against the simplest version that would still do the job? Does showing all of this on one chart earn its place, or would one clear comparison, or several separate charts each making one point, actually serve the decision better than a single crowded one trying to hold everything at once. A chart's job is to make one thing legible, not to prove that all the analysis behind it happened.

## The test that doesn't require a design eye

You do not need training in visualization to catch most of this. One question does most of the work: **would this chart tell a meaningfully different story if drawn the obvious alternative way** — axis starting at zero, full date range instead of a flattering window, individual groups shown instead of one blended average?

If the story holds up across those alternatives, you're very likely looking at an honest representation, whichever specific version you were handed. If the story changes the moment you ask for one of those alternatives, that's the finding — not proof of dishonesty, since these choices get made constantly without any intent to mislead, but a real signal that the specific version in front of you was the flattering one, deliberately or not.

## What to ask for

> "Show me this same chart with the axis starting at zero, and with the full date range instead of just this window. Does the story still hold?"

The direct version of the test above — cheap to ask for, and it either confirms the chart or reveals which choices were doing the work.

> "Is this chart showing an average or a total across several groups? Show me the individual groups separately as well."

Catches the aggregation problem specifically — an overall trend that's actually two very different trends cancelling each other out in the summary.

> "Could someone unfamiliar with this data understand what this chart is claiming within about ten seconds, without you explaining it? If not, simplify it — fewer metrics, one clear comparison, or split it into more than one chart."

The complexity test. A chart that needs a guided tour has failed at its one job regardless of how accurate every number on it is.

> "What choices did you make in how to draw this — axis range, date range, what to compare — and why those specifically, rather than the alternatives?"

Forces the editorial decisions behind the chart into the open, the same way Chapter 5 asked for a method's assumptions to be stated rather than left implicit.
