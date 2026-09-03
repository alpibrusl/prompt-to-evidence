# Asking the Right Question

Every chapter so far has been about catching a problem after it's already in the number. This one is about preventing most of them from getting there in the first place, by asking well the first time rather than auditing well after the fact.

## A vague question gets a vague answer wearing confidence

"Did Bellwood's checkout page do better?" sounds like a question. It is really several unstated ones bundled together — better by what measure, compared against what, tested how — and left unstated, each one gets filled in by whatever the agent finds convenient, not necessarily what you actually meant. The answer that comes back will sound just as confident either way because nothing about an under-specified question produces a hedge in the response to match it. It is, word for word, the question that opened this book in Chapter 1 — the one that got a fast, confident, wrong answer.

The difference is not length for its own sake. It's whether the request contains anything the rest of this book taught you to check for, stated up front instead of discovered afterward:

Vague:

> "Did the new checkout page do better?"

Better:

> "Compare conversion rate between the randomly-assigned control and treatment groups, over the full test period — don't stop early. Report the point estimate and the confidence interval, not just the headline number. Compute it with code, using a standard statistical library, and show me both the code and what it produced. Before running it on the real data, test the same method on a small example where we already know the answer."

Notice what the second version actually is. Every clause is a chapter from this book, stated as a requirement instead of hoped for: random assignment and a full run, not a peeked-at one (Chapter 8); a range, not a bare point (Chapter 10); genuine computation with a named library (Chapters 4 and 6); a known-answer test before trusting it on the real thing (Chapter 7). Nothing in that request demands you understand the statistics yourself. It only requires knowing which questions exist — which, if you've read this far, you now do. Asked this way from the start, it would have caught Bellwood's before/after problem the same week, not seven chapters later.

## What a complete request contains

Not every request needs every clause above — a quick internal count doesn't need a known-answer test the way a decision about real budget does. But for anything a real decision will lean on, the complete version specifies:

**What's being compared, and how the groups got assigned.** Randomly, or by some other means that might itself explain the difference (Chapter 8).

**What counts as the outcome, precisely.** Not "conversion" in the abstract, but the exact field and definition, checked against what the method assumes about it (Chapter 3).

**A range, not just a headline number.** How wide it is tells you whether the result can actually settle the decision (Chapter 10).

**The computation itself, visible.** Real code, run and shown, not narrated (Chapter 4), using a named, established library rather than something reimplemented from scratch (Chapter 6).

**Proof it was tested before it was trusted.** A known-answer case it got right, run before the case that actually matters (Chapter 7).

**A baseline, if a model is involved.** What the simplest possible approach would have scored, so the added complexity has to earn its place (Chapter 12).

## When the honest answer is to bring in a real expert

Most of what lands on your desk does not need this. Some of it does: a decision involving real money at stake, anything with legal or regulatory exposure, anything essentially impossible to walk back once acted on. For those, an hour of a real statistician's or data scientist's time is cheap relative to what a wrong version of that particular decision costs — not because this book's discipline stops applying, but because some decisions deserve a second, more expert set of eyes on the reasoning in addition to it, the same way a large irreversible engineering decision deserves the same in that world.

## What to ask for

There isn't a short list this time. There is one request, and it's the template from the start of this chapter, generalised:

> "Before you compute this: tell me what you're comparing and how the groups were assigned, what the outcome is measured as precisely, and how you'll test the method before running it on the real data. Then compute it in real code using a standard library, show me both the code and its output, and report a range alongside the headline number rather than just the number alone."

Ask it before the analysis starts, not after the number arrives. Everything else in this book is what to do when you didn't, or when the answer still doesn't add up once you have it.
