# Confidence, Not Certainty

Bellwood's honest, randomly-assigned retest from Chapter 8 came back smaller than the original headline: "Conversion is up 2 percentage points," not the 20% first reported. Those two numbers are in two different units, which is worth catching before comparing them at all: the new one is an absolute difference, from 21% of visitors to 23%, and put in the same relative terms as the headline it is a lift of about a tenth, not a fifth. An agent will happily report one number in each unit and let the contrast do work it hasn't earned; the comparison means something only once both are in the same unit, and in the same unit the honest result is about half the headline. Said plainly, even that revised number sounds like a fact with no give in it. It rarely is one. The 2 is a best guess, built from a limited sample, and the honest version of that sentence has a range attached to it whether or not anyone says the range out loud.

## The number is a guess, precisely stated

A **point estimate** is the single best-guess number a calculation produces — the 2 percentage points, the average order value, the conversion rate. It is real, it is the right answer to give when someone asks "what's your best guess," and it is also, always, a guess: computed from the particular sample you happened to have, which would have come out slightly different with a different sample of the same size, drawn the same way, on a different day.

A **confidence interval** is a range around that point estimate — not one number, but a plausible band, wide or narrow depending on how much the data actually pins the answer down. "Up 2 points" said alone hides a question that changes everything about what to do with it: is the honest range 1.8 to 2.2, or is it -0.1 to 4.1? The first is a result you can act on. The second contains zero — a genuine possibility that nothing happened at all — sitting quietly underneath a headline number that looked completely certain.

## What the range is telling you

Width is the part worth reading, more than the point estimate itself. A narrow interval means sampling noise isn't the problem — you have enough data that the estimate isn't moving around much from one sample to the next. A wide interval means the opposite: the honest answer is "somewhere in a fairly large range," even though the single headline number reports one specific point inside it with exactly the same confident formatting either way.

Read that narrow-interval claim precisely because it's easy to over-read: a narrow interval says the *noise* is small, and says nothing at all about *bias*. Chapter 2 drew that distinction and it applies here without exception — more data narrows the interval by shrinking noise; it does nothing about a sample that was never representative to begin with. A confidently narrow interval computed from a self-selected or otherwise skewed sample is not a trustworthy result with a nice tight range. It's a precisely wrong one. Narrowness is a reason to stop worrying about sample size. It is never, on its own, a reason to stop worrying about where the sample came from.

One precise thing is worth saying about what a range like "95% confidence" actually claims because the common shorthand for it — "there's a 95% chance the true value is in this range" — is not quite right, and this book would rather be exactly right than easy. What it actually claims is a statement about the method: if you repeated this same sampling process many times, about 95% of the intervals it produced would contain the true value. For a practical decision in front of you today, use the interval as the range of values reasonably compatible with the data under the method's assumptions — close enough to work with day to day — and leave the precise philosophical distinction to a statistics course, exactly as Chapter 1 warned this one wouldn't be.

Sample size is what narrows it, and this is Chapter 2's noise again, in the form that finally makes the connection obvious: more data reduces noise, and a confidence interval is that sampling noise made visible instead of hidden behind a single falsely-precise number — not eliminated, just measured and reported honestly as a range instead of a false point. A test that ran on four hundred people will almost always report a wider interval than the same test run on forty thousand, even if the point estimate happens to land in the same place for both.

## The decision this changes

Two results can carry the identical headline number and mean entirely different things once the range is visible. "Up 2 points, interval 1.8 to 2.2" is a result you can commit budget to with real confidence. "Up 2 points, interval -0.1 to 4.1" is a result where the honest position is closer to *we don't yet know* than to *it worked* — and no amount of repeating the point estimate more confidently changes which of those two situations you're actually in.

<div style="margin:1.6rem 0;">
<svg viewBox="0 0 660 280" width="100%" style="display:block;" xmlns="http://www.w3.org/2000/svg">
<text x="330" y="18" text-anchor="middle" font-family="EB Garamond, Georgia, serif" font-size="10.5" letter-spacing="0.06em" fill="#9a9a9a">SAME HEADLINE, TWO HONEST RANGES</text>
<line x1="150" y1="45" x2="150" y2="232" stroke="#666" stroke-width="1.1" stroke-dasharray="3,3"/>
<text x="150" y="38" text-anchor="middle" font-family="EB Garamond, Georgia, serif" font-size="10" fill="#666">0</text>
<text x="330" y="86" text-anchor="middle" font-family="EB Garamond, Georgia, serif" font-size="11" fill="#666">1.8 to 2.2</text>
<line x1="312" y1="95" x2="312" y2="105" stroke="#1a1a1a" stroke-width="1.2"/>
<line x1="348" y1="95" x2="348" y2="105" stroke="#1a1a1a" stroke-width="1.2"/>
<line x1="312" y1="100" x2="348" y2="100" stroke="#1a1a1a" stroke-width="1.6"/>
<circle cx="330" cy="100" r="3.5" fill="#1a1a1a"/>
<path d="M296,121 L299,126 L306,115" fill="none" stroke="#8a3324" stroke-width="1.3"/>
<text x="312" y="126" font-family="EB Garamond, Georgia, serif" font-size="12" font-weight="600" fill="#1a1a1a">commit budget</text>
<text x="330" y="156" text-anchor="middle" font-family="EB Garamond, Georgia, serif" font-size="11" fill="#666">-0.1 to 4.1</text>
<line x1="141" y1="165" x2="141" y2="175" stroke="#1a1a1a" stroke-width="1.2"/>
<line x1="519" y1="165" x2="519" y2="175" stroke="#1a1a1a" stroke-width="1.2"/>
<line x1="141" y1="170" x2="519" y2="170" stroke="#1a1a1a" stroke-width="1.6"/>
<circle cx="330" cy="170" r="3.5" fill="#1a1a1a"/>
<text x="330" y="196" text-anchor="middle" font-family="EB Garamond, Georgia, serif" font-size="12" font-weight="600" fill="#1a1a1a">we don't yet know</text>
<line x1="270" y1="201" x2="390" y2="201" stroke="#8a3324" stroke-width="1.1" stroke-dasharray="3,3"/>
<line x1="60" y1="232" x2="600" y2="232" stroke="#1a1a1a" stroke-width="1.2"/>
<line x1="150" y1="232" x2="150" y2="238" stroke="#1a1a1a" stroke-width="1.1"/>
<line x1="330" y1="232" x2="330" y2="238" stroke="#1a1a1a" stroke-width="1.1"/>
<text x="150" y="250" text-anchor="middle" font-family="EB Garamond, Georgia, serif" font-size="10" fill="#666">0</text>
<text x="330" y="250" text-anchor="middle" font-family="EB Garamond, Georgia, serif" font-size="10" fill="#666">2 (point estimate)</text>
<text x="330" y="270" text-anchor="middle" font-family="EB Garamond, Georgia, serif" font-size="10.5" font-style="italic" fill="#444">Same point estimate, two very different honest positions — width is the number that matters.</text>
</svg>
</div>

The practical rule: before acting on a number, ask whether the interval is narrow enough, relative to the decision on the table, to actually distinguish the options in front of you. If the interval spans the boundary between the outcomes that would change your decision — including zero, when zero is that boundary — the data alone does not clearly distinguish the options, regardless of which side of that line the point estimate happens to sit on. That does not automatically mean waiting for more data is the right call; a decision can still rationally be made under real uncertainty, depending on what waiting actually costs, how reversible the choice is, and how lopsided the downside is if you're wrong — questions this book leaves to you, because they're not questions a number can answer. What the wide interval means is that the number itself has stopped being the thing settling the question, and whatever settles it next should be named honestly rather than smuggled in behind a headline that sounds more certain than it is.

## What to ask for

> "Don't just give me the number — give me the range it could plausibly fall in, and tell me how wide that range is relative to the number itself."

The default request. A number with no range attached is a headline, not yet a result.

> "Does this range include the possibility that nothing actually happened — that the true effect is zero, or even negative?"

The single most decision-relevant question this chapter has. A confident-sounding point estimate can still be sitting on top of a range that includes "no effect at all."

> "Is this range narrow enough to actually tell the options apart, or do we need more data before this number can settle the decision?"

Turns "is the number good" into the question that actually determines what to do next.
