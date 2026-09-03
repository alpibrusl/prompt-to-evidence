# The fixture

One generated dataset, reused across Sessions 4, 5, and 6 rather than
inventing new demo material each time — students meet the same number from
three different angles, the same way the book itself does.

It's Bellwood's checkout-page story, the one that opens Chapter 1 and closes
Chapter 15: "conversion is up 20%, ship it," and everything that turns out to
be wrong with that sentence once someone actually checks it.

## Generate it

```bash
./generate_bellwood_data.py                      # → ./bellwood-evidence
./generate_bellwood_data.py /path/to/output       # or choose where
```

Run this **fresh before each session** that uses it, not once at the start
of the cohort. A student who's already seen the honest numbers loses the
"cold" reaction Session 4's exercise depends on, and nothing about the
fixture is meant to persist between sessions or cohorts. The seed is fixed,
so the story lands the same way every time — 20% naive, 2 points honest —
which matters more here than novelty would.

The generated data is disposable: this script is the source, the folder it
produces is a build artifact, and `.gitignore` keeps it out of the repo the
same way `build/` stays out of the book's own.

## What's in it, and which session uses it

- **`headline-report.md`** — the memo exactly as it was first presented:
  "conversion is up 20%, ship it," with the truncated-axis chart described
  the way Chapter 11 says these things get shown.
- **`checkout_daily.csv`** — the real daily numbers behind that headline.
  Deliberately has no random-assignment column, because there wasn't one —
  every visitor got the new page starting March 15. This is Chapter 8's
  whole subject, planted rather than explained.
- **`deploy-notes.md`** — what actually shipped alongside the checkout page
  on March 15: a lowered free-shipping threshold and a homepage refresh.
  Chapter 9's confound, sitting in plain sight for anyone who thinks to ask
  "what else changed that week."
- **`retest-headline.md`** — the honest follow-up: "up 2 percentage
  points," with no range attached. Chapter 10's whole subject — a point
  estimate is not yet the same claim as a range.
- **`customers.csv`** — 400 customer rows for Session 7, to profile before
  trusting. Nothing in the file says what is wrong with it.
- **`retest_daily.csv`** — the raw daily counts behind the honest retest: a
  real randomly-assigned holdout, control against treatment, small enough
  that the range around "2 points" is a genuine range and not a rounding
  error.

**Session 4** hands students only `headline-report.md` and
`checkout_daily.csv`, cold, with nothing but "audit this before it ships."
They have to notice, unprompted, that there's no group column — the
comparison was never randomized, just a date split — and that the four
weeks after outperforming the four weeks before is not the same claim as
"the new page beat the old one."

**Session 5** adds `deploy-notes.md`. Same story, one layer deeper: even
setting the before/after problem aside, three things shipped that week, not
one, and the naive number was never just measuring the checkout page.

**Session 6** adds `retest-headline.md` and `retest_daily.csv`. Students
compute the honest point estimate and its confidence interval from the raw
counts, then redraw the chart both ways — axis truncated to 20–24%, and
axis running the full range — and decide for themselves whether the story
holds up drawn plainly.

## The numbers underneath, for facilitators

The generator's true values (never stated in the fixture's own files,
recoverable only by actually running the numbers):

- Conversion was already rising through the spring: a straight-line ramp
  from 18.2% to 19.6% across the 28 days before launch, continuing at the
  same slope across the 28 days after. Averaged, the before window sits
  near 18.9% and the after window's counterfactual near 20.3%. This is the
  missing-randomization problem in the data itself — the "before" window
  is not a fair stand-in for the "after" window even with nothing else
  going on.
- True effect of the new checkout page alone: **+2.0 percentage points**
- Naive before/after also picks up a **confound** — the free-shipping
  change and spring banner shipped the same week — worth roughly another
  +0.4 points on top of the trend.
- In one unit, percentage points of conversion: the naive before/after
  comparison lands at about **+3.9 points** (18.8% → 22.7%, or +21%
  relative — the memo's "up 20%"); a trend-extrapolated counterfactual
  leaves about **+2.8 points**; the honest randomized retest lands at
  **+2.0 points** (21.1% → 23.1%), with a 95% confidence interval of
  roughly +0.2 to +3.8 — excluding zero, but only just, and wide enough to
  be worth actually reporting as a range. That is the number in Chapter
  10, and the reason the retest's control arm sits above the launch-day
  rate is that the spring ramp had levelled off near 21–22% by May.
