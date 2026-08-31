---
name: verify-evidence
description: Use this skill before telling a non-technical user that an analysis, an A/B test result, or a data-driven claim is solid, significant, or ready to act on — and whenever the user directly asks something like "can I trust this number," "is this analysis solid," "did the campaign actually cause this," or "is this result real or just noise." Runs the pre-decision checklist from the book *Prompt to Evidence* against the actual analysis — the real code, output, and charts behind a number, not the prose summary of it — and is explicit about which items it verified versus which it can't and must ask a human about. Do not use it for routine exploratory data work (a quick chart to look around, debugging a query) that isn't heading toward a claim someone will act on — only when a number or result is about to be presented as something to decide with.
---

# Verify Evidence

This skill exists because a number that's real and a number that's evidence
for a specific claim are different things, and reporting the first while
implying the second is exactly the failure mode *Prompt to Evidence* (this
repo's own manuscript, under `chapters/`) teaches non-technical readers to
watch for. This skill is that book's closing checklist, run by the agent on
the analysis it just produced, before the human has to ask for it.

## The one rule that matters more than the checklist

Check the actual artifact, not the sentence describing it. "The data was
profiled for missing values" and a `.isnull().sum()` call actually appearing
somewhere in the work are different claims — the first can be typed by
anyone, the second is evidence. Where the checklist item is about a
methodological choice (random assignment, a held-out test set, a stated
uncertainty range), go read the real code or output and name specifically
what was done, not a generic reassurance that it "looks fine."

Some items describe something that happened outside anything you can see —
whether a result was actually cross-checked against a bank statement or a
board member's intuition, whether "unusual" results get scrutiny as a
matter of habit rather than only when they're suspicious. Don't infer these
from the absence or presence of adjacent artifacts; ask. Marking a habit or
an off-artifact check "done" because the number happens to look plausible
is the specific mistake the book spends chapter 7 warning about — an
unusually good result deserves *more* scrutiny than a plausible one, not
less, and this skill should apply that same suspicion to its own report.

## Workflow

1. **Decide the scope.** A real decision riding on this number (budget,
   a launch, a claim going to stakeholders) warrants the full checklist. A
   lighter sanity check mid-conversation can use the short version in
   `references/minimum-bar-checklist.md`. If it's ambiguous which is
   warranted, ask rather than guessing.

2. **Read `references/minimum-bar-checklist.md`** for the full item list,
   each tagged `[checkable]`, `[ask-human]`, or `[mixed]`, with notes on
   what to actually look for.

3. **For checkable items, read the real code/output/chart**, not a summary
   of it. Name what you found specifically — "the comparison groups were
   self-selected (opted into the new checkout), not randomly assigned" is
   useful; "the methodology looks reasonable" is not.

4. **For ask-human and the human half of mixed items, actually ask** —
   particularly the habit-shaped ones (is *every* result cross-checked, or
   only the surprising ones). Don't award a pass because nothing in front
   of you contradicts it.

5. **Report the results** using the format below, then close with the
   book's own framing question.

## Output format

One table per checklist section actually run, one row per item:

| Item | Status | Detail |
|---|---|---|
| Computed with real code, shown | ✅ Done | `analysis.py` lines 12-40, output attached |
| Random assignment | ❌ Not done | Groups were self-selected (opted in), not randomly assigned — this is a before/after comparison, not a causal test |
| Tested against a known-answer case first | ❓ Ask | Not visible in the provided work — confirm whether this happened |
| ... | | |

Four statuses, used honestly:

- **✅ Done** — checkable, and the actual work shows it.
- **❌ Not done** — checkable, and it's missing or the work shows a problem.
  Name the specific problem, not just its absence.
- **➖ N/A** — the thing the item protects against doesn't apply here (e.g.
  no model is involved, so the "If a model is involved" section doesn't
  apply) — say what would have to be true for it to apply.
- **❓ Ask** — a fact only a human can confirm, or a `[mixed]` item whose
  artifact-half wasn't found. Don't round this up to ✅ just because
  nothing contradicts it, and don't round it down to ❌ just because it
  wasn't shown — say plainly it's unconfirmed.

Then close with, verbatim or close to it:

> **How do you know — and what would have to be true for that to be
> wrong?**
>
> That's the question this whole checklist unpacks. The gaps above are
> where the answer is currently "we don't, yet" — decide how much that
> matters based on what's riding on this number: a headline for internal
> curiosity can carry more open items than something that will move real
> budget or a customer-facing claim.

Don't soften a real methodological problem (like a non-random comparison)
to make the summary read better — that's precisely the kind of number this
skill exists to catch before it ships as "the campaign caused a 12% lift."
