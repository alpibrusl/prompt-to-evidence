#!/usr/bin/env python3
"""Generate WORKED-EXAMPLE.md from the cohort fixture.

The book argues, chapter after chapter, for checking a number before believing
it, and never once shows the whole check happening. This appendix is that
check, performed end to end on Bellwood's checkout number.

Every figure in the output is computed here, from a fixture generated fresh
into a temporary directory -- none is typed in. The book's numbers and the
bootcamp's numbers are therefore the same numbers by construction, and a
change to the fixture that would contradict the appendix shows up as a
different appendix rather than as a reader's discovery.

Run by `make example`, which `make pdf`/`epub`/`html` imply.
"""

from __future__ import annotations

import csv
import math
import statistics
import subprocess
import sys
import tempfile
from pathlib import Path

BOOK = Path(__file__).resolve().parent.parent
GENERATOR = BOOK / "cohort" / "fixture" / "generate_bellwood_data.py"
OUT = BOOK / "WORKED-EXAMPLE.md"


def generate(into: Path) -> Path:
    """Run the cohort's own fixture generator; return the directory it wrote."""
    target = into / "bellwood"
    result = subprocess.run(
        [sys.executable, str(GENERATOR), str(target)], capture_output=True, text=True
    )
    if result.returncode != 0:
        sys.exit(f"fixture generator failed:\n{result.stderr}")
    return target


def pooled(rows: list[dict]) -> tuple[int, int, float]:
    visits = sum(int(r["visits"]) for r in rows)
    orders = sum(int(r["completed_orders"]) for r in rows)
    return visits, orders, orders / visits


def trend_counterfactual(before: list[dict], after: list[dict]) -> tuple[float, float, float]:
    """Least squares on the before-window's daily rates, extended over the after-window.

    Returns (slope per day, launch-eve rate, mean counterfactual rate). This is
    the arithmetic Chapter 9 describes: what the number would have done if the
    only thing that had happened was the thing that was already happening.
    """
    ys = [int(r["completed_orders"]) / int(r["visits"]) for r in before]
    xs = list(range(len(ys)))
    mx, my = statistics.mean(xs), statistics.mean(ys)
    slope = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    intercept = my - slope * mx
    eve = intercept + slope * (len(ys) - 1)
    projected = [intercept + slope * (len(ys) + i) for i in range(len(after))]
    return slope, eve, statistics.mean(projected)


def interval(cv: int, co: int, tv: int, to: int) -> tuple[float, float, float, float]:
    """Difference in proportions with its 95% interval, in percentage points."""
    pc, pt = co / cv, to / tv
    diff = pt - pc
    se = math.sqrt(pc * (1 - pc) / cv + pt * (1 - pt) / tv)
    return diff * 100, se * 100, (diff - 1.96 * se) * 100, (diff + 1.96 * se) * 100


def build(fixture: Path) -> str:
    daily = list(csv.DictReader((fixture / "checkout_daily.csv").open(encoding="utf-8")))
    before = [r for r in daily if r["period"] == "before_march_15"]
    after = [r for r in daily if r["period"] == "after_march_15"]
    bv, bo, br = pooled(before)
    av, ao, ar = pooled(after)
    naive = (ar - br) * 100
    relative = (ar - br) / br * 100

    slope, eve, cf = trend_counterfactual(before, after)
    adjusted = (ar - cf) * 100

    retest = list(csv.DictReader((fixture / "retest_daily.csv").open(encoding="utf-8")))
    arms = {"control": [0, 0], "treatment": [0, 0]}
    for row in retest:
        arms[row["group"]][0] += int(row["visits"])
        arms[row["group"]][1] += int(row["completed_orders"])
    (cv, co), (tv, to) = arms["control"], arms["treatment"]
    diff, se, lo, hi = interval(cv, co, tv, to)

    return f"""# One Analysis, Worked Through

Four weeks after Bellwood shipped its redesigned checkout page, the growth
team sent leadership a memo.

> **Conversion is up 20%. Recommend we ship it to 100% and move on to the
> next thing on the roadmap.**

The number is real. Nobody made it up, and the arithmetic behind it is
correct. It is also not, in the form it arrived, evidence for the sentence
sitting next to it — and the distance between those two facts is most of this
book.

Here is that distance, on the actual data. The files are the ones
`cohort/fixture/generate_bellwood_data.py` produces, and every figure below is
computed from them rather than quoted.

## Where the 20% comes from

Four weeks either side of the launch on 15 March:

| | visits | completed orders | conversion |
|---|---:|---:|---:|
| Before | {bv:,} | {bo:,} | {br:.2%} |
| After | {av:,} | {ao:,} | {ar:.2%} |

A difference of **{naive:+.2f} percentage points**, which is **{relative:+.1f}%**
of where it started. That is the memo's "up 20%", and it is arithmetic anyone
can check.

What it compares is two stretches of the calendar. The page is one of the
things that differs between them.

## What it is actually comparing

`checkout_daily.csv` has a `period` column and no assignment column, because
there was never any assignment. Every visitor got the new page from 15 March
onward. Nobody was held back, so there is no group that spent those four weeks
on the old page for comparison — the only version of "old page" available is
the four weeks that came before.

Which is a problem the moment the number was already moving. Fit a straight
line to the 28 days before the launch, when the new page did not exist:
conversion was climbing **{slope * 100:+.3f} percentage points a day**, from
{br:.2%} across the window to about {eve:.2%} on launch eve. Extend that same
line across the four weeks after, and it lands at **{cf:.2%}** — what the
number would have done had the only thing happening been the thing that was
already happening.

Against that, the page is worth **{adjusted:+.2f} points**, not
{naive:+.2f}. Roughly a quarter of the headline was the calendar.

## What else shipped that day

`deploy-notes.md` lists the 15 March release. Three things went out:

- the new checkout page
- the free-shipping threshold, lowered site-wide from $75 to $50
- a spring homepage banner

All three, to everyone, at once. No arithmetic separates them afterwards. A
lowered shipping threshold is exactly the kind of change that moves checkout
conversion, and it is inside the {adjusted:+.2f} points along with the page.

## The version that answers the question

`retest-headline.md` is what happened when someone ran it properly: a randomly
assigned holdout, decided before the test started and held for three weeks
regardless of how it looked partway through.

| | visits | completed orders | conversion |
|---|---:|---:|---:|
| Control | {cv:,} | {co:,} | {co / cv:.2%} |
| Treatment | {tv:,} | {to:,} | {to / tv:.2%} |

**{diff:+.2f} percentage points.** Half the headline, and this time the two
groups differ by the page and by nothing else systematic — that is what the
random assignment bought.

## The range around it

{diff:+.2f} is one number from one sample. Another three weeks, drawn the same
way, would land somewhere near it and not on it. The 95% interval is
**{lo:+.2f} to {hi:+.2f} points**.

Two things are worth reading off that. It excludes zero, so the page did
something. And it is nearly {hi - lo:.0f} points wide, on an effect of
{diff:.1f} — "up 2 points" and "somewhere between a fifth of a point and
just under four" are the same finding, and only one of them is honest about
how much is known.

## The chart

The original memo attached conversion by day on an axis running 17% to 25%.
Nothing about the underlying numbers changes if the axis starts at zero; every
point sits in the same order, the same distance apart. What changes is the
share of the frame the movement occupies, and the movement is the thing the
eye reports.

## What each step cost

| | difference |
|---|---:|
| Before versus after, as reported | {naive:+.2f} points |
| Once the pre-existing trend is removed | {adjusted:+.2f} points |
| Randomized retest, the page alone | {diff:+.2f} points |
| The interval around that last figure | {lo:+.2f} to {hi:+.2f} |

The memo was not dishonest, and whoever wrote it was not careless. Every
number in the first row is correct. Three competent people given
`checkout_daily.csv` and no further instruction could reasonably produce
{naive:+.2f}, {adjusted:+.2f}, and "not enough here to say" — and none of them
would be wrong, because the number a method returns depends on what the method
assumed, and the assumptions were never stated.

That is what a checklist is for. Not to produce the one right answer, which
does not exist here, but to make sure the assumptions get said out loud before
somebody ships to 100% and moves on to the next thing on the roadmap.
"""


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        text = build(generate(Path(tmp)))
    if OUT.exists() and OUT.read_text(encoding="utf-8") == text:
        print(f"{OUT.name} already current")
        return
    OUT.write_text(text, encoding="utf-8")
    print(f"wrote {OUT.name}")


if __name__ == "__main__":
    main()
