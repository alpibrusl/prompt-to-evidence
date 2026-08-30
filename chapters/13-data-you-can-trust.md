# Data You Can Trust

Every discipline in this book so far — compute properly, use established libraries, test against known cases, build a fair comparison — protects you from a good method applied badly. None of it protects you from a good method applied perfectly to data that was wrong before any of it started. This chapter is the one link in the chain that everything else depends on and none of it can fix.

## Missing data is rarely missing at random

An empty cell looks like nothing happened. Often, something happened — the customer who churned stopped answering satisfaction surveys before they left, which means your satisfaction data is systematically short exactly the people you most need to hear from. Filling that gap with an average, or simply ignoring the missing rows, doesn't restore the missing information. It quietly assumes the missing customers looked like the ones who stayed, which is frequently the opposite of true.

This is Chapter 2's bias, in its most common real-world form. The question worth asking about any gap in the data is not just *how much is missing* but *is the reason it's missing related to the very thing being measured* — because if it is, the honest answer contains a hole exactly where the most important information would have been.

## The same thing, spelled three ways

"USA", "United States", and "us" are, to a person, obviously the same country. To a computation that groups rows by matching text exactly, they are three different categories, and a total that should have combined them silently splits into three smaller, individually less noticeable numbers. Dates stored as text in three different formats, currency values with the symbol baked into the text instead of a number, a category field where "yes" sometimes means `Y` and sometimes means `1` — none of these crash anything. They produce a computation that runs cleanly and quietly counts less than it appears to, and the shortfall is invisible unless someone actually looks at what the raw values in a column actually are.

## When a number moves because the definition did

A metric that jumps or drops sharply for no business reason worth reporting deserves the same treatment Chapter 7 gave any startling result — but here the leading suspect is different: not a bug in the computation, but a change in what the data itself means. A field renamed, a system upgrade that started counting something slightly differently, a new source added to a "total" that used to mean something narrower. The number looks like news. It's often an artifact of a definition changing under the analysis's feet, silently, on a date nobody thought to mention as relevant to anything you were measuring.

## Look at the data before you trust it

**Data profiling** is checking the basic shape of a dataset before analysing it — how much is missing in each column, what the actual unique values in a category field really are, what the minimum and maximum of a numeric field look like — not to answer the real question yet, but to catch the kind of problem this chapter is about before it quietly corrupts everything built on top of it. A country field with forty spellings for six countries, an age column with a maximum of 300, a date range that inexplicably starts three years before the business existed: none of these require statistical sophistication to catch, only the discipline of actually looking, which is exactly the step that gets skipped when a deadline is close and the data looks fine at a glance.

## What to ask for

> "For the fields that matter most here, how much data is missing — and is there any reason to think the missing rows are different from the ones we have, rather than a random subset?"

The bias-in-missingness question, asked before it has a chance to quietly shape the result.

> "Show me the actual unique values in each category column, and the min and max of each numeric one. Anything look wrong?"

The data-profiling habit, made concrete and requested directly rather than assumed to have already happened.

> "Has the meaning or source of any of these fields changed over the time period we're looking at?"

Catches a shifted definition before it gets mistaken for a real change in the business.
