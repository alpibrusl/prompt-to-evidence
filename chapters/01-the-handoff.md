# The Handoff

You ask the agent whether Bellwood's new checkout page actually beat the old one. It answers in one sentence: *conversion is up 12%, ship it.* The sentence arrives fast, sounds definite, and reads exactly the way a correct answer would read.

It might be correct. That is the entire problem this book is about.

## The number on the screen is not the answer

Here is the first idea, and everything else in this book follows from it.

What the agent gave you is a **number**: a value that came out of a calculation. A number is not evidence. **Evidence** is a result you could defend to someone who doubts it — someone who asks *how do you know*, and expects an answer that survives the question. Getting from a number to evidence takes several steps, and any one of them can fail silently while the number itself looks exactly the same.

The path runs: a question, then data, then a method applied to that data, then a computation, then a number, then a decision made on the strength of it. Six links. The agent can produce the last one — the number — in under a second. Whether the five links before it were sound is a separate matter entirely, and the number does not carry that information on its face. A 12% lift computed correctly and a 12% lift computed on a broken comparison look identical in a chat window.

You have almost certainly done this kind of work before, in a spreadsheet, and trusted the result — because in a spreadsheet, the method is usually just arithmetic, and arithmetic is easy to check by eye. `=AVERAGE(B2:B40)` either looks right or it does not; you can glance at the range and know if it's the wrong column. What an agent can now do that Excel never asked of you is run an actual statistical comparison, fit an actual model, compute an actual causal estimate — categories of calculation where "does it look right" stops being something you can judge by glancing at the formula bar. The number gets harder to eyeball exactly as the machinery producing it gets more capable. That gap is this book.

## This is not like checking a formula

One comfort from spreadsheet work has to be set aside now, early, because holding onto it will mislead you for the rest of this book: a formula is either right or wrong, and checking it means finding the mistake. `=SUM(B2:B40)` either sums the correct range or it doesn't — fix it, and it's fixed, completely, for good, for this data.

Almost nothing else in this book works that way, and it's worth being honest about that before going any further. A statistical comparison, a measured impact, a prediction — these are not answers waiting to be checked against a known correct value the way a formula is. They are estimates, built from limited data, carrying real uncertainty that doesn't disappear no matter how carefully the method was applied. Two people can both do everything in this book correctly and still land on different numbers from the same data — a different but equally defensible way of handling an outlier, a slightly different time window — without either one having made a mistake.

That is not a gap better tools will eventually close. It is the actual difference between measuring something in the world, where the truth is only partly visible through whatever data you happened to collect, and checking a calculation, where the truth is fixed and just has to be located. Chapter 10 is entirely about the shape this takes in practice — a range instead of a single point, and what to do with one honestly. For now, the thing worth carrying forward is smaller: stop expecting a single correct answer to fall out of an analysis the way one falls out of a spreadsheet formula, and most of what follows will make a great deal more sense.

## Two kinds of wrong

There is the kind of wrong you can see. A formula pointing at the wrong column, a chart with no data in it, a percentage above 100. You look, you notice, you fix it. This kind is not really the subject here — you already know how to catch it, because you have been catching it in spreadsheets for years.

The other kind is quieter, and it is what the rest of this book is for. The analysis runs cleanly. The number is a plausible size — not absurd, not obviously broken. And it is still wrong, for reasons that never show up in the output itself:

- The two groups you compared were never actually comparable — one skewed toward returning customers, the other toward new ones, and the "effect" is that difference wearing a disguise.
- The sample was too small for the result to mean anything, and nothing about a single clean-looking number tells you that.
- Something else happened at the same time as the change you're measuring — a price drop, a holiday, a competitor's outage — and it is quietly doing all the work you're crediting to your campaign.
- The code computing the comparison has a bug that happens not to crash. It runs. It returns a number. The number is simply wrong.

None of these announce themselves. A dashboard does not turn red when the comparison behind it was unfair. This is the kind of wrong you own the system, not fixing a chart — Chapter 8 onward is a set of specific, checkable questions built to catch exactly this category, because *looking plausible* and *being true* are different properties, and only one of them is visible from the chat window.

## Why nobody told you this

It is worth being precise about why this gap exists, because it did not exist through neglect.

For as long as doing real statistical or causal analysis required writing code and knowing the mathematics behind it, the two came bundled together. Nobody could run a regression without first learning what a regression assumes, what can go wrong with one, and how to sanity-check the result — because doing it *at all* required climbing most of that hill first. The rigor came along for the ride, unavoidably, the same way a person who learned to drive a manual transmission absorbed something about how an engine works whether they meant to or not.

What has changed is that the bundle came apart. An agent will now fit that regression, run that comparison, build that model, on request, in seconds — without you climbing the hill that used to guarantee you picked up the caution along the way. That is genuinely useful. It is also why the caution has to be taught separately now, on purpose, rather than absorbed as a side effect of the only available path.

## The asymmetry

**The agent will compute almost any comparison you ask for, and will rarely tell you whether the comparison was a fair one.**

Ask whether B beat A and you will get an answer about whether B beat A, computed on whatever data was at hand. Whether that data came from a properly randomized test, whether the two groups were comparable to begin with, whether the sample was large enough to mean anything — that depends entirely on whether you asked, because the agent answered the question you actually posed, not the one you meant underneath it.

It is not withholding caution from you. It is answering precisely. The skill this book teaches is not computation — the agent has that — it is knowing which questions a trustworthy number needs to have survived.

## What this book is not about

It is not a statistics course, and finishing it will not make you able to derive a confidence interval (Chapter 10) by hand or explain why a t-distribution has the shape it has. That is real expertise, it takes real time, and this book would be lying if it promised to shortcut it.

It is also not about spreadsheets versus code, which tool or library to prefer, or how to build a dashboard — the mechanics move quickly and are not the point. And it does not cover research-grade statistics: clinical trials, academic publication standards, anything where the bar is peer review rather than a decision you are personally accountable for. Those have their own literature, written for that different bar.

What it covers is narrower and, for this audience, more useful: the handful of questions that separate a number from evidence, applied to the decisions that actually land on a desk — did this change work, did this campaign cause what we're crediting it with, can this pattern in a chart be trusted, is this model's confidence deserved. Vocabulary and judgement, not a credential.

## If you already have an answer sitting in front of you

You may already be looking at a result — a test, a report, a chart someone built for you — and want to know how much to trust it before you act.

| | Question | Where |
|---|---|---|
| 1 | Was the comparison actually fair — were the two groups alike in everything except what you changed? | Chapter 8 |
| 2 | Could something else happening at the same time explain the result instead of the thing you're crediting? | Chapter 9 |
| 3 | Do you know how uncertain the number is, or only the number itself? | Chapter 10 |
| 4 | If you fed the same method a case where you already knew the true answer, would it get that one right? | Chapter 7 |
| 5 | Was the result unusually good or unusually bad — and if so, has anyone looked for a bug before believing it? | Chapter 7 |
| 6 | Does the chart's axis, range, or comparison flatter the story, or would it look the same drawn plainly? | Chapter 11 |
| 7 | If it's an ML model — was it ever tested on data it hadn't already seen? | Chapter 12 |
| 8 | Is the underlying data missing anything important, or skewed toward who happened to respond? | Chapter 13 |

Nothing here requires you to run the check yourself. You can ask your agent every one of these questions today and get a direct answer — the pattern of shaky answers tells you where to spend your skepticism, which is rarely the place you'd have guessed.

The same list appears in full at the end of the book, as Chapter 15, with the reasoning behind each item. This version is the map; that one is the audit.

## The arc of this book

**Part I — The Ground.** Where this chapter sits: what a number is versus what evidence is, where data actually comes from, and the shape a trustworthy analysis takes from question to decision.

**Part II — Trusting the Number.** The four rules this whole book rests on: force computation instead of guessing, build the general tool rather than a one-off script, reach for established libraries instead of reimplementing statistics by hand, and test against a case you already know the answer to — with suspicion as the default for every result, not just the ones that already look wrong.

**Part III — Making the Decision.** The two concrete situations that brought you here: comparing two things fairly, and measuring whether something you did actually caused what followed. Plus the uncertainty that sits underneath both.

**Part IV — Seeing and Learning.** Reading a chart as a claim rather than a picture, what happens the moment "build me a model" enters the conversation, and the data-quality problems that make everything upstream of them unreliable.

**Part V — Working With the Agent.** Turning all of it into instructions: how to ask a question precisely enough that the answer can be checked, and a closing checklist for what must be true before you act on a number.

## A note on the words

There is real jargon ahead — not much, and every piece of it earns its place because Excel never required you to learn it. Each term is defined the first time it appears, used the same way every time after, and collected in a glossary at the back. When a term has a clean everyday image behind it — and several of the ideas in this book do — I commit to that image once and keep using it, rather than reaching for a new metaphor each chapter and leaving you to reconcile them.

That consistency is checked automatically, the same way it is in this book's companion volume: the manuscript is source, kept in a repository with its full history, and a script fails the build if a chapter uses a term before the book has defined it. The discipline this book asks of you is the discipline it holds itself to.

## One thing to take from this chapter

If you keep one sentence from everything above, keep this one:

**A number is what the agent gives you. Whether it is evidence is yours to establish.**

Every chapter after this one is an answer to some part of how.

## What to ask for

> "Before I act on this number — walk me through where it came from: what data, what method, and what would have to be true about that data for the method to be valid here."

You will not follow every word of the answer yet. Ask it anyway, and keep the reply. By the end of this book you will be able to read it properly, and watching it get more legible is a genuinely useful thing to notice about your own progress.
