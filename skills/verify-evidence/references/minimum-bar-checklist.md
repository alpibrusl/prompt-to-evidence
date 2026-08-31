# The Minimum Bar — checklist with inspection guidance

This is the checklist from *Prompt to Evidence*, chapter 15 ("The Minimum
Bar"), verbatim in substance. Each item is tagged with how the skill should
actually resolve it:

- **[checkable]** — there's real work product (code, output, a chart, a
  documented step) that settles it. Go look at what was actually done.
- **[ask-human]** — this describes something that happened outside any
  artifact you have access to (a manual cross-check against a bank
  statement, a decision about what counts as "unusual") — ask, don't infer.
- **[mixed]** — checkable if the relevant step shows up in the actual
  work; if it doesn't show up, that's evidence it wasn't done, but confirm
  with a question rather than silently assuming absence of evidence means
  it never happened at all.

"The actual work" means the real code, notebook, script output, or chart
behind the number — not the prose summary of it. A sentence describing what
was done is not the same artifact as the thing that was done, and this
skill's whole point is to check the artifact, not the summary of it.

## Getting a real number

- **Calculations were computed with actual code, run and shown — not
  narrated in a sentence.** [checkable] — is there real, executed code (or
  spreadsheet formulas) behind the number, with visible output? "The data
  shows a 12% lift" with no code attached is a claim, not evidence.
- **The method is a reusable tool with parameters, not a one-off script
  quietly tuned to today's numbers.** [checkable, needs real reading] —
  look for hardcoded thresholds/cutoffs in the code that suspiciously match
  the result being reported (e.g. a filter cutoff that happens to be
  exactly where the effect appears). Flag specific lines, not a vague
  impression.
- **An established, well-known library was used for anything
  statistical — not a reimplemented formula.** [checkable] — check imports:
  scipy/statsmodels/numpy/pandas or the language's standard equivalent, vs.
  a hand-rolled t-test or confidence-interval formula.
- **The method was tested against a case with a known answer, and got it
  right, before being trusted on the real one.** [mixed] — checkable if a
  validation step against synthetic or known data appears in the actual
  work; if it doesn't appear, ask whether it happened somewhere not shown
  rather than assuming it definitely didn't.

## Not fooling yourself

- **The result passed a consistency check against something else already
  known — not only checked because it looked unusual.** [mixed] — the
  book's point is this should happen on *every* result, not just
  suspicious ones. Check whether a cross-check against an independent
  number appears anywhere in the work; if not, ask whether one exists.
- **An unusually good or unusually bad result specifically was checked for
  a bug or data problem before it was believed.** [mixed] — same pattern:
  look for evidence of the investigation, ask if it isn't visible.
- **The comparison was genuinely fair — random assignment, or a clearly
  named reason it wasn't possible.** [checkable, needs real reading] — this
  is the single most important item to actually verify by reading the
  methodology, not skimming it. A before/after comparison, or "the group
  that opted in vs. the group that didn't," is not a randomized comparison
  even when the write-up implies causality. Name specifically what kind of
  comparison was actually run.
- **Anything else that changed at the same time has been considered, not
  just the thing hoping for credit.** [mixed] — checkable if confounders
  are explicitly addressed in the analysis; otherwise ask what else changed
  in the same window.
- **You have a range, not just a headline number — and it's narrow enough
  to actually decide with.** [checkable] — is there a confidence interval,
  standard error, or explicit uncertainty range in the actual output, or
  only a single point estimate?

## Knowing what you're looking at

- **The data has been profiled — missing values counted, category
  spellings checked, numeric ranges sanity-checked.** [checkable] — look
  for an actual profiling step (null counts, `.describe()`/`value_counts()`
  equivalent, range checks) in the work, not just a claim the data "looked
  clean."
- **Missing data has been checked for whether it's random or related to
  the very thing being measured.** [checkable, needs judgment] — look for
  explicit analysis of *why* data is missing, not just how much.
- **The sample is representative, not merely large.** [mixed] — checkable
  if sampling methodology is documented; otherwise a judgment call — ask
  what population the sample was actually drawn from and how.
- **A chart's axis, date range, and comparison would tell the same story
  drawn the plain, unflattering way.** [checkable, if a chart exists] —
  inspect the actual chart/code for a truncated y-axis, a cherry-picked
  date range, or a comparison baseline chosen to flatter the result.

## If a model is involved

- **You know whether it's a batch model or an online one, and it's being
  handled accordingly.** [mixed] — checkable from deployment code/context
  if available; otherwise ask. Note in the report that an online model
  needs *Prompt to Production*'s full operational discipline on top of this
  checklist, not instead of it.
- **It was evaluated on data it never saw during training, not the data it
  was built from.** [checkable] — look for an actual train/test split or
  held-out evaluation set in the code; evaluating on training data is a
  specific, nameable bug, not a vague concern.
- **It clearly beats the simplest possible baseline.** [checkable] — is
  there an explicit baseline comparison (e.g. "always predict the mean," a
  simple rule) in the actual work, with numbers, not just an assertion that
  the model is "accurate"?

## The short version (five highest-value items)

For a lighter sanity check rather than a full pre-decision review:

1. Computed with real code, shown, not narrated. [checkable]
2. Tested against a known answer before being trusted on the real one.
   [mixed]
3. Survives a consistency check against something else already known — not
   just checked because it looked unusual. [mixed]
4. A range exists, not just a headline number. [checkable]
5. The underlying data has actually been looked at, not assumed fine.
   [checkable]
