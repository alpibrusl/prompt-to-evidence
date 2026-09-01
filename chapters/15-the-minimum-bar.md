# The Minimum Bar

This chapter is a checklist and an argument about it.

The argument first, because a checklist you don't believe in is a checklist you'll skip the day it actually matters.

## What "trustworthy" means

There is no fixed line where a number becomes trustworthy enough. Trustworthiness is proportional to what's riding on it. A rough number satisfying your own curiosity, that nobody will act on, needs almost none of what follows. A number that will move real budget, or shape a decision touching customers' money or legal standing, needs all of it. Most of what lands on your desk sits somewhere in between, and the useful question isn't *is this rigorous enough* in the abstract. It's:

**What happens if this number is wrong, and who acts on it before anyone finds out?**

Everything below follows from your honest answer to that.

## The bar

Before a number drives a real decision. Grouped by what each part protects against.

### Getting a real number

- [ ] Calculations were computed with actual code, run and shown — not narrated in a sentence (Chapter 4).
- [ ] The method is a reusable tool with parameters, not a one-off script quietly tuned to today's numbers (Chapter 5).
- [ ] An established, well-known library was used for anything statistical — not a reimplemented formula (Chapter 6).
- [ ] The method was tested against a case with a known answer, and got it right, before being trusted on the real one (Chapter 7).

### Not fooling yourself

- [ ] The result passed a consistency check against something else already known — not only checked because it looked unusual (Chapter 7).
- [ ] An unusually good or unusually bad result specifically was checked for a bug or data problem before it was believed (Chapter 7).
- [ ] The comparison was genuinely fair — random assignment, or a clearly named reason it wasn't possible (Chapter 8).
- [ ] Anything else that changed at the same time has been considered, not just the thing you're hoping gets the credit (Chapter 9).
- [ ] You have a range, not just a headline number — and it's narrow enough to actually decide with (Chapter 10).

### Knowing what you're looking at

- [ ] The data has been profiled — missing values counted, category spellings checked, numeric ranges sanity-checked (Chapter 13).
- [ ] Missing data has been checked for whether it's random or related to the very thing being measured (Chapter 13).
- [ ] The sample is representative, not merely large — volume was not mistaken for information (Chapter 2).
- [ ] A chart's axis, date range, and comparison would tell the same story drawn the plain, unflattering way (Chapter 11).

### If a model is involved

- [ ] You know whether it's a batch model or an online one, and it's being handled accordingly — an online model gets this book's companion volume's full operational discipline on top, not just this book's (Chapter 12).
- [ ] It was evaluated on data it never saw during training, not the data it was built from (Chapter 12).
- [ ] It clearly beats the simplest possible baseline — the complexity has earned its place (Chapter 12).

## The short version

If that's too much to hold at once, five items carry most of the value, each answerable in minutes:

1. **Was it computed with real code, shown, not narrated?**
2. **Was it tested against a known answer before being trusted on the real one?**
3. **Does it survive a consistency check against something else you already know — not just checked if it looked unusual?**
4. **Do you have a range, not just a number?**
5. **Has the data actually been looked at, not just assumed to be fine?**

Fifteen minutes, most of it just asking.

## What it took, in the end

Chapter 1 opened with a single sentence: Bellwood's agent reported the new checkout page had lifted conversion 20%, and recommended shipping it immediately. Nothing about that sentence was dishonest. It was also not yet true, in the sense this book cares about.

Getting from that sentence to something worth trusting took most of this book. Chapter 3 checked what the number was actually counting. Chapters 4 through 7 made sure it was computed with real code, built as a reusable tool, using an established library, and tested against a case with a known answer — the discipline that has to hold for any number, this one included. Chapter 8 is where the real problem turned up: the new page had never been shown to a random half of visitors at all. It had simply gone live for everyone on March 15, and "conversion is up 12%" meant "the four weeks after March 15 outperformed the four weeks before it" — a real number, honestly computed by then, answering a comparison nobody had actually run. The honest, randomly-assigned retest that followed, and the range Chapter 10 put around it, landed on conversion up 2 percentage points — about half the headline once both were put in the same unit: smaller, real, and not the number that nearly shipped on its own.

Nine chapters between a plausible sentence and an actual answer is not this book being thorough for its own sake. It is what the gap between a number and evidence, named all the way back in Chapter 1, actually costs to close — once, carefully, so it doesn't have to be re-litigated by hand every time a number like it shows up again.

## What you have

You began this book unable to derive a p-value or explain what a regression is actually doing underneath. That hasn't changed, and it was never the point.

What you can do now is ask whether a comparison was fair, whether a number is a guess dressed as a fact, whether an unusually good result deserves suspicion instead of celebration, whether a chart would tell the same story drawn plainly. You can tell the difference between "sales went up after" and "the campaign caused it." You can hear "99% accurate" and know which question to ask before you believe it. That is the actual job this book was for, and it was never about doing the math yourself.

## The last thing

One question, worth asking about every number before it drives a decision:

> **"How do you know — and what would have to be true for that to be wrong?"**

That question is this whole book, compressed. It asks for evidence rather than a number (Chapter 1). It asks what the method assumed (Chapter 3). It asks what would falsify the result rather than just confirm it — which is the difference between checking and hoping.

Ask it about every number before you act on it. The answer doesn't have to be elaborate. Sometimes "we randomly held out ten percent, tested the method on a known case first, and the interval doesn't include zero" is completely sufficient. What matters is that there is an answer, and that someone actually has it — rather than finding out, after the budget is spent, that nobody ever did.

## What to ask for

One last time:

> "Walk me through this checklist against what you just gave me. For each item: done, not done, or not applicable — and if not applicable, why."

Ask before the first real decision rides on it. Ask again the next time something looks too good. The gaps are where your actual risk is, and unlike most lists of open questions, this one eventually runs out.
