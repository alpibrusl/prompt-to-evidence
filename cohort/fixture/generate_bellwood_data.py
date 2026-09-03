#!/usr/bin/env python3
# SPDX-License-Identifier: EUPL-1.2
"""Generates a fresh copy of the Session 4/5/6 teaching fixture — Bellwood's
checkout-page numbers, standing in for the fictional e-commerce company this
book's own chapters already follow, with the exact flaw Chapter 8 narrates
already planted:

  - headline-report.md      the memo as it was actually first presented —
                             "conversion is up 20%, ship it" — with the
                             truncated-axis chart described the way Chapter 11
                             says it was shown to leadership
  - checkout_daily.csv       the real daily numbers behind that headline: one
                             row per day, 28 days before March 15 and 28 days
                             after, with NO random-assignment column at all —
                             because there wasn't one. Every visitor after
                             March 15 got the new page; the "test" is really
                             a before/after split (Chapter 8's whole subject)
  - deploy-notes.md          what actually shipped on March 15 — the new
                             checkout page, and two other things that shipped
                             alongside it (Chapter 9's confound, planted so it
                             can be found, not just asserted)
  - retest-headline.md       the honest follow-up memo — "up 2 percentage
                             points" — with no range attached (Chapter 10's
                             whole subject: a point estimate is not the same
                             claim as a range)
  - retest_daily.csv          the raw daily counts behind the honest retest: a
                             real randomly-assigned holdout, control vs.
                             treatment, small enough that the range around
                             "2 points" is a real range and not a rounding
                             error

Usage: fixture/generate_bellwood_data.py [output-dir]
       (default: ./bellwood-evidence)

Run this fresh before each session that uses it — see sessions.yaml's
facilitator_notes on session 4 for why a clean handout matters. The generated
data is disposable and gitignored; this script is the source. The seed is
fixed on purpose: the story (20% naive, 2 points honest) has to land the
same way for every cohort, not drift with whoever happens to run this.
"""

from __future__ import annotations

import csv
import math
import random
import sys
from datetime import date, timedelta
from pathlib import Path

SEED = 20260315  # the date the story turns on, not a special number otherwise

# The true state of the world. Nobody in the fixture's own files states these
# numbers directly — they're what a correct analysis would recover.
#
# Conversion was already rising through the spring, before anything shipped:
# a straight-line ramp across the 28 days before launch, continuing at the
# same slope across the 28 days after. That trend is what makes the naive
# before/after comparison unfair on its own (Chapter 8): the "before" window
# is not a counterfactual for the "after" window even with nothing else
# going on. Averaged, the before window sits near 18.9% and the after
# window's counterfactual near 20.3%.
BEFORE_START_RATE = 0.182  # old page, day 1 of the before window
BEFORE_END_RATE = 0.196    # old page, day 28 of the before window (launch eve)
TREND_PER_DAY = (BEFORE_END_RATE - BEFORE_START_RATE) / 27

TRUE_LIFT = 0.02           # new checkout page's real effect, 2 points, confirmed
                            # only by the honest randomized retest
CONFOUND_LIFT = 0.004      # the free-shipping change + spring banner refresh
                            # that shipped the same day — inflates the naive
                            # before/after comparison on top of the real effect
                            # and on top of the trend

# By the May retest the spring ramp had levelled off; the old page converts
# at about 21% and the new one at 21% + TRUE_LIFT. The retest's control arm
# is the only clean measurement of the old page in the whole fixture.
RETEST_BASE_RATE = 0.21

# What a correct analysis recovers, in one unit (percentage points of
# conversion): naive before/after ~ +3.8 pts (~+20% relative, the memo's
# headline); trend-extrapolated counterfactual leaves ~ +2.4 pts; randomized
# retest ~ +2.0 pts. Trend explains most of the naive overstatement, the
# confound the rest.

LAUNCH_DATE = date(2026, 3, 15)
DAILY_VISITS_MEAN = 5000
DAILY_VISITS_SD = 300

RETEST_START = date(2026, 5, 4)   # after the naive numbers had already
RETEST_DAYS = 21                   # circulated — the "wait, let's do this
RETEST_ARM_VISITS_MEAN = 200       # properly" retest, on a small holdout,
RETEST_ARM_VISITS_SD = 25          # not the whole site

# --- Session 7: the customer sample to profile before trusting -------------
# Session 7 asks students to profile a customer table before answering any
# question about churn, and there was no customer table: the exercise had no
# data at all. Two things are planted, neither announced anywhere the student
# can read.
#
# The country field carries the same countries spelled several ways, so a
# naive "unique values" count reports far more countries than exist.
#
# And the satisfaction score is missing far more often for customers who went
# on to churn -- 60% against 8%. That is the checkpoint: missingness that
# lines up with the outcome being predicted is not missing at random, and a
# model trained on the rows that survive a dropna() has been handed the answer.
CUSTOMER_COUNT = 400
CHURN_RATE = 0.22
COUNTRY_SPELLINGS = {
    "United States": ["United States", "USA", "us", "U.S.", "united states"],
    "United Kingdom": ["United Kingdom", "UK", "gb", "Great Britain"],
    "Germany": ["Germany", "DE", "germany"],
    "Spain": ["Spain", "ES"],
    "Netherlands": ["Netherlands", "NL", "netherlands"],
}
SURVEY_MISSING_IF_CHURNED = 0.60
SURVEY_MISSING_IF_RETAINED = 0.08


def sample_conversions(rng: random.Random, visits: int, rate: float) -> int:
    """Binomial-ish sample via a normal approximation — good enough for
    teaching data, and avoids depending on anything beyond the standard
    library. Clipped to a legal range."""
    mean = visits * rate
    sd = math.sqrt(visits * rate * (1 - rate))
    value = round(rng.gauss(mean, sd)) if sd > 0 else round(mean)
    return max(0, min(visits, value))


def daterange(start: date, days: int):
    for i in range(days):
        yield start + timedelta(days=i)


def write_checkout_daily(rng: random.Random, out: Path) -> None:
    rows = []
    for i, d in enumerate(daterange(LAUNCH_DATE - timedelta(days=28), 28)):
        visits = max(1, round(rng.gauss(DAILY_VISITS_MEAN, DAILY_VISITS_SD)))
        rate = BEFORE_START_RATE + TREND_PER_DAY * i
        conversions = sample_conversions(rng, visits, rate)
        rows.append((d, "before_march_15", visits, conversions))
    for i, d in enumerate(daterange(LAUNCH_DATE, 28)):
        visits = max(1, round(rng.gauss(DAILY_VISITS_MEAN, DAILY_VISITS_SD)))
        counterfactual = BEFORE_START_RATE + TREND_PER_DAY * (28 + i)
        conversions = sample_conversions(rng, visits, counterfactual + TRUE_LIFT + CONFOUND_LIFT)
        rows.append((d, "after_march_15", visits, conversions))

    with (out / "checkout_daily.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["date", "period", "visits", "completed_orders", "conversion_rate"])
        for d, period, visits, conversions in rows:
            w.writerow([d.isoformat(), period, visits, conversions, round(conversions / visits, 4)])


def write_retest_daily(rng: random.Random, out: Path) -> None:
    rows = []
    for d in daterange(RETEST_START, RETEST_DAYS):
        for group, rate in (("control", RETEST_BASE_RATE), ("treatment", RETEST_BASE_RATE + TRUE_LIFT)):
            visits = max(1, round(rng.gauss(RETEST_ARM_VISITS_MEAN, RETEST_ARM_VISITS_SD)))
            conversions = sample_conversions(rng, visits, rate)
            rows.append((d, group, visits, conversions))

    with (out / "retest_daily.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["date", "group", "visits", "completed_orders", "conversion_rate"])
        for d, group, visits, conversions in rows:
            w.writerow([d.isoformat(), group, visits, conversions, round(conversions / visits, 4)])


def write_customers(rng: random.Random, out: Path) -> None:
    """The Session 7 sample: 400 customer rows to profile before trusting."""
    countries = list(COUNTRY_SPELLINGS)
    rows = []
    for i in range(1, CUSTOMER_COUNT + 1):
        churned = rng.random() < CHURN_RATE
        canonical = rng.choice(countries)
        spelling = rng.choice(COUNTRY_SPELLINGS[canonical])
        missing = SURVEY_MISSING_IF_CHURNED if churned else SURVEY_MISSING_IF_RETAINED
        if rng.random() < missing:
            satisfaction = ""
        else:
            # Churners who did answer skew lower, but not so much that the
            # score alone would carry a model -- the missingness is the finding.
            centre = 5.8 if churned else 7.6
            satisfaction = round(min(10.0, max(1.0, rng.gauss(centre, 1.4))), 1)
        rows.append(
            (
                f"C{i:04d}",
                spelling,
                rng.choice([1, 3, 6, 12, 24]),
                round(max(0.0, rng.gauss(240 if churned else 410, 120)), 2),
                satisfaction,
                "yes" if churned else "no",
            )
        )

    with (out / "customers.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(
            [
                "customer_id",
                "country",
                "tenure_months",
                "lifetime_value_eur",
                "satisfaction_score",
                "churned",
            ]
        )
        w.writerows(rows)


def write_headline_report(out: Path) -> None:
    (out / "headline-report.md").write_text(
        """# Growth Update — New Checkout Page

**To:** Leadership
**From:** Growth
**Re:** Checkout redesign, four weeks in

We shipped the redesigned checkout page on March 15. Comparing the four
weeks before the change to the four weeks since:

> **Conversion is up 20%. Recommend we ship it to 100% and move on to the
> next thing on the roadmap.**

See the attached chart — conversion by day, four weeks either side of the
launch. Axis runs 17%–25% so the trend is easy to read at a glance.

Raw numbers behind this are in `checkout_daily.csv`, if anyone wants to
check our work.
""",
        encoding="utf-8",
    )


def write_deploy_notes(out: Path) -> None:
    (out / "deploy-notes.md").write_text(
        """# Deploy notes — March 15

Everything that went out in the March 15 release:

- **New checkout page** (the redesign growth has been asking about)
- **Free-shipping threshold lowered from $75 to $50**, site-wide — Ops
  wanted this in before the spring push and it happened to be ready the
  same week
- **Spring homepage banner refresh** — no functional change, new creative
  only

All three shipped together, to everyone, at the same time. Nobody flagged
this as relevant to the checkout-page number — it wasn't the thing anyone
was trying to measure.
""",
        encoding="utf-8",
    )


def write_retest_headline(out: Path) -> None:
    (out / "retest-headline.md").write_text(
        """# Follow-up — Honest Retest

Growth ran it again properly this time: a randomly-assigned holdout,
control vs. treatment, decided and locked in before the retest started,
held for the full three weeks regardless of how it looked partway through.
Raw daily counts are in `retest_daily.csv`.

> **Conversion is up 2 percentage points.**

Chart attached — the two arms' three-week rates side by side, axis 20%–24%
so the gap between them is easy to see.
""",
        encoding="utf-8",
    )


def main() -> None:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("./bellwood-evidence")
    if out.exists():
        print(f"error: {out} already exists — remove it or pass a different output path", file=sys.stderr)
        sys.exit(1)
    out.mkdir(parents=True)

    rng = random.Random(SEED)
    write_headline_report(out)
    write_checkout_daily(rng, out)
    write_customers(rng, out)
    write_deploy_notes(out)
    write_retest_headline(out)
    write_retest_daily(rng, out)

    print(f"generated fixture at {out}")
    print("start students on headline-report.md + checkout_daily.csv — nothing else, cold")


if __name__ == "__main__":
    main()
