# Project conventions

## What this book is and who it is for

*Prompt to Evidence* teaches data literacy to people who are not experts in
math or statistics but need to make decisions from data — in economics,
science, marketing, wherever an agent can now produce a number on request.
Reading an A/B test result, or measuring whether a marketing campaign
actually caused the lift it's credited with, are the kind of concrete
questions this book is written toward. The reader works comfortably in
Excel and wants to go where their data team already lives, not become a
statistician.

Companion to [*Prompt to Production*](https://github.com/alpibrusl/prompt-to-production),
same voice and structure, different subject: that book is software
engineering discipline for people who cannot read code; this one is
analytical discipline for people who are not mathematicians. Chapter 1 of
that book explicitly excludes ML and statistical work from its scope — this
book is what fills that gap, not a competitor to it.

The spine is four rules, and every chapter either builds toward them or
applies them to a specific kind of decision:

1. Make the agent compute, never guess — force code execution, not
   token-level arithmetic that merely looks like calculation.
2. Write the general tool; treat this case as one input to it, not a script
   tuned to look right for today's numbers.
3. Use established, heavily-used libraries over reimplemented statistics —
   the same supply-chain trust logic as *Prompt to Production* chapter 2,
   aimed at numerical correctness instead of security.
4. Test against a case where you already know the answer, and be suspicious
   of extreme results in *both* directions — a suspiciously perfect number
   and a suspiciously terrible one get the same treatment: stop and look for
   a bug before you believe either one.

## Author identity — do not guess

The author is:

    Alfonso Sastre <alfonso@alpibru.com>

Same person, same convention as *Prompt to Production*. Use exactly this
for `book.yaml`, git commit authorship, and anywhere an author is named. If
a field about a real person is unknown, leave it blank and ask — do not
infer.

## The manuscript is source

Markdown in `chapters/` is the source; everything in `build/` is derived and
gitignored, as is `GLOSSARY.md`. Never edit `GLOSSARY.md` by hand — it is
generated from `glossary.yaml` by `make glossary`.

## The concept ledger and the gate

`glossary.yaml` is the canon: every term the book teaches, with one
definition, one committed analogy, the defining chapter, and prerequisite
terms.

`make check` lints the manuscript against it and exits 8 on error. It runs
in CI on every push and pull request. When adding prose:

- Define a term before using it, or signpost the forward reference
  explicitly with "(Chapter N)" — the linter allows a signposted one and
  rejects a bare one.
- Add any new term to `glossary.yaml` rather than defining it only in prose.
- Keep an analogy consistent with the one the ledger commits to.
- Chapter numbers in the rendered book come from `book.yaml`'s per-chapter
  `title` override (`"Chapter N — Title"`), not from the Markdown H1 — see
  the equivalent convention in *Prompt to Production*'s `book.yaml` if this
  needs re-deriving.

## Absolutes

Distinguish a prescription from an assertion. "Never trust a result you
have not tested against a known case" is a rule of practice and its force
is the point — keep it. A claim about the world takes a softer edge, so a
reader absorbs the lesson instead of arguing with the sentence. Check
`never`, `always`, `only`, `every`, `exactly`, `not negotiable` when
editing: keep them in rules, soften them in claims.

## Build

    make check    # the gate
    make epub / make html / make pdf
    make all      # check + epub + html (pdf needs Pango, see README)

## Audio

`make audiobook` emits a podcastkit project under `build/audiobook/` —
derived, gitignored, one episode per chapter. Rendering it to MP3 needs a
TTS backend and is not wired into CI, because it costs money per character
on the paid backends and hours of CPU on the free ones.

## Licences

Manuscript CC BY-NC 4.0; code EUPL-1.2. New files under `scripts/` need an
`SPDX-License-Identifier: EUPL-1.2` header. See `COPYING.md`.
