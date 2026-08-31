# When the Agent Wants to Build a Model

Somewhere in a conversation about predicting which of Bellwood's customers might churn, or what next month's demand will look like, the agent will offer to build a model. Worth being precise about what that word means here, because this book has already used it loosely. A **machine learning model** — ML model, for short — is built from data to predict an output, and it is judged by how well it performs on cases it hasn't already seen. That is a different thing from the regression used back in Chapters 8 and 9 to estimate the size of an effect or control for a confound, which is judged by a confidence interval, not by prediction on unseen cases. This chapter, and everywhere else in this book that says "model" without qualifying it, means the first kind.

This chapter is what to know before saying yes to one, and it starts with a distinction that matters more than anything about the model itself: what is this model actually going to *do*, once it exists.

## Two very different situations wearing the same word

A **batch model** runs once, or on a schedule you control — once a month, say — in an environment you control, produces a set of outputs, and then stops until next time. "Which of our current customers look likely to churn" computed on the first of the month, handed to the marketing team as a list, is a batch model. Someone still looks at the list before acting on it. If the model is wrong this month, the damage is one wrong list, caught the next time a human reviews it, fixable by rerunning it.

An **online model** is embedded inside a system that is actually running, making predictions continuously, in real time, as part of something people or other systems are actively using — pricing shown on a live page, a recommendation served the instant someone opens an app, a transaction scored for fraud as it happens. Nobody reviews each individual prediction before it takes effect; the model's output *is* the action, immediately, at whatever volume the system runs at.

This is not a technical footnote — it changes the entire risk category. A wrong batch model produces one wrong list that a person still gets to catch. A wrong online model is wrong continuously and automatically, at full speed, until someone notices something is off in the aggregate and intervenes. The blast radius, and how fast it accumulates, are not the same problem wearing different clothes; they are genuinely different problems.

Everything else in this chapter — testing honestly, comparing against a simple baseline, treating a suspiciously good result with suspicion — applies fully to both kinds of model, without exception. But an online model takes on a second, separate set of obligations once it goes live inside a running system: it needs watching for its inputs quietly changing shape over time, a way to roll it back the moment it starts behaving badly, the same operational discipline any live system needs. That discipline is this book's companion volume's whole subject, not this one's — if a model is headed for that kind of deployment, treat it as a live system first and a model second, and read accordingly.

## Overfitting: memorising instead of learning

A model that scores brilliantly on the exact data it was built from and considerably worse on anything new has not learned the pattern underneath that data. It has memorised the specific data, the way a student who studies last year's exact exam paper aces that one paper and struggles the moment a single question is phrased differently. The model looks capable right up until it meets a case it hasn't already seen — which, once it's actually in use, is every case.

**Held-out data** — also called a test set — is the fix: a portion of the data set aside and never shown to the model while it's being built, used only afterward to check how it performs on cases it genuinely hasn't seen. This is Chapter 7's known-answer test, specialised for this exact problem — you already have cases with known outcomes; the discipline is refusing to let the model peek at some of them until the evaluation, precisely so the evaluation means something.

## The suspicious 99%

Chapter 7 promised this moment would arrive again, and here it is: a model reporting startling accuracy — 99%, "gets it right almost every time" — is, more often than it is a genuine triumph, a sign that the held-out data wasn't really held out. A feature that quietly encodes the answer, the same records appearing on both sides of the split, a leak somewhere between training and evaluation — these produce a suspiciously perfect number far more often than an actual model does. Treat it the way Chapter 7 said to treat any extreme result: as a reason to look for the leak before you believe the accuracy, not as a reason to celebrate first.

## Does the complexity earn its keep?

Before trusting a sophisticated model, ask what the simplest possible approach would have scored — always predicting the average, always predicting last month's number, whatever the laziest reasonable guess would be. If the sophisticated model barely beats that baseline, the complexity is not paying for itself: it is harder to explain, harder to maintain, and easier to get subtly wrong, for a gain that may not be real once you account for how imprecisely it was measured (Chapter 10). A model earns the right to be complicated by clearly beating the boring alternative, not by existing.

## Keep a record of every attempt

Building a model is rarely one attempt. It's five, or twenty — different features, different algorithms, different ways of handling the same messy column — and whichever version ships is whichever one scored best among however many were tried. That's completely normal. It is also, unremarked, the exact multiple-comparisons problem from Chapter 8: test enough variations against the same data and one of them tends to look good by chance alone, the same way testing twenty metrics on an A/B test tends to turn up one significant-looking result even when nothing real is happening anywhere.

**Experiment tracking** is keeping a record of every attempt — what changed about it, what it scored, on which held-out data — not just the one that won. Purpose-built tools for this exist and are common in ML work (MLflow and similar experiment-tracking tools are the usual names); using one is a reasonable habit, and which specific one is beside the point this book cares about. A spreadsheet with one row per attempt does the identical job for a smaller effort, if that's genuinely all the scale in front of you calls for. The practice is what matters, not the product.

What the record actually buys you: when the winning model scores unusually well, it tells you whether it beat a field of twenty attempts by a real margin, or whether it simply got lucky on this one split among many tries — a question the suspicious-accuracy check two sections up cannot answer on its own without knowing how many attempts were made to get there. Two models tried, with a clear winner, and twenty tried, with the best one ahead by a hair, are very different situations wearing the same headline number. Only a record tells you which one you're actually looking at.

## What to ask for

> "How many different versions of this were tried before this one, and what did each one score? Show me all of them, not just the winner."

Turns the multiple-comparisons question from Chapter 8 into one you can actually ask about a model, and makes an unusually good score interpretable rather than just impressive-sounding.

> "Is this a batch model or an online one — will it run on a schedule I control, or will it be making live decisions inside a running system?"

The question that determines which set of obligations apply, asked before any of the rest of this chapter.

> "Was this tested on data it never saw during training? Show me the held-out results specifically, not the training results."

The known-answer test, applied to a model. A number reported only from data the model was trained on is not evidence of anything.

> "How does this compare to the simplest possible approach — just guessing the average, or repeating last period's number?"

Forces the complexity to justify itself against the boring alternative, rather than being trusted by default.

> "This accuracy looks unusually high — before we trust it, check for leakage between the training data and the test data."

The suspicious-99% question, asked directly rather than left as a private, easily-dismissed feeling.
