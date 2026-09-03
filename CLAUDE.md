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
4. Test against a case where you already know the answer, and stay
   suspicious of every result, not just the extreme-looking ones — the
   scalable version is a consistency check: does this agree with something
   else already known? Extreme results just fail that check loudly; an
   ordinary-looking wrong number fails it quietly, which is why the check
   has to run on everything.

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
- "Chapters 6 and 7" and "Chapters 7 through 10" count as signposts too.
- A single-word term that is unambiguous jargon opts into prose scanning
  with `scan: true`. Do not opt in an ordinary English word — the gate is
  only worth having while it is quiet enough to be believed. If a term's
  *alias* is the ordinary word, scan the distinctive name alone:
  `scan: ["known-answer test"]`.
- A chapter that deliberately introduces no term belongs in
  `teaches_no_terms`, with a comment saying why. Do not invent a term to
  silence that warning.
- Chapter numbers in the rendered book come from `book.yaml`'s per-chapter
  `title` override (`"Chapter N — Title"`), not from the Markdown H1 — see
  the equivalent convention in *Prompt to Production*'s `book.yaml` if this
  needs re-deriving.

## The books are standalone

Decided deliberately: the four books are **standalone volumes that also work as
a set**, not one course in four parts. Someone must be able to read this one
alone and finish it without ever having opened another.

That has three consequences, and they are the reason this section exists rather
than the decision being re-argued each time it comes up.

**Every cross-reference names its book.** Not "the second book in this series",
which a reader holding only this one cannot resolve — *Prompt to Evidence*. The
series map in the front matter tells them what that is. A reference that merely
points somewhere without saying where is a dead end, and there are none left.

**Each book owns its vocabulary.** `glossary.yaml` is self-contained on purpose.
A term used in two books gets an entry in both, with the same definition — see
`counterfactual`, shared by *Evidence* and *Decision*. Do not replace a
definition with a pointer to another volume.

**Shared chapters are acceptable, and still worth reducing.** *Evidence* and
*Ledger* carry the same four-rule method, and under a standalone reading that
duplication is defensible: no reader is expected to meet it twice. It is not
free, though — someone who buys both notices — so the argument stays parallel
while the examples and failure cases should become each book's own. `bookkit
check duplication -b . --against ../sibling` measures it.

What this decision does *not* license is contradicting a sibling on shared
facts. Ledgerly is one company across three books; see the canon section.

## Absolutes

Distinguish a prescription from an assertion. "Never trust a result you
have not tested against a known case" is a rule of practice and its force
is the point — keep it. A claim about the world takes a softer edge, so a
reader absorbs the lesson instead of arguing with the sentence. Check
`never`, `always`, `only`, `every`, `exactly`, `not negotiable` when
editing: keep them in rules, soften them in claims.

## Voice

The house voice, written down because "sound like the other chapters" is not
something anyone — a person or an agent — can act on.

It is deliberately *not* an imitation of a named writer. A reader suggested one
as a reference and the register she was pointing at is right: practical,
concrete, unpretentious, example-first. But "is this Osmani enough?" has no
answer, so it cannot be checked, taught, or handed to an agent, and an agent
told to imitate a person produces pastiche. What follows is the same target,
stated as rules that can actually be applied.

**Explain the thing; do not announce that you are about to.** This is the one
that matters most, and the one this manuscript gets wrong most often. "This
chapter is that path." "Now the shape." "Here is what they are for." "The last
idea here is what turns all this from data into decisions." Every one of these
is the narrator stepping out from behind the material to describe the material.
Cut the announcement and start with the content — the reader can see a new
section beginning; they do not need to be told that one is beginning. A
transition earns its place only when it carries information the next paragraph
does not, which is rare.

**One metaphor, stated once, and never explained.** An analogy that has to be
unpacked over the following three sentences was not doing its job in the first
one. The ledger already commits each concept to a single analogy; using it means
dropping it in and moving on, not returning to admire it. Where an image has a
famous source, either credit it or do not use it — an unattributed allusion
reads as borrowed profundity to every reader who recognises it.

**Concrete before abstract, always.** Name the file, the command, the number,
the amount of time. "The budget alert takes four minutes" beats any sentence
about the importance of cost awareness. Bellwood exists so that every claim in
the book has somewhere specific to land; use it rather than reaching for a
hypothetical.

**Prescriptions may be absolute; claims about the world may not.** See
[Absolutes](#absolutes) above — the distinction is load-bearing and predates
this section.

**Jargon is compression, not decoration.** A word that saves a sentence earns
its place. Define it once, in the chapter the ledger assigns it, and then use it
plainly without re-explaining or apologising for it.

**Write to a capable reader who happens not to know this yet.** Not a beginner
to be protected, not a peer to be impressed. No flattery, no "as we all know",
no warnings that a topic is about to get difficult. Say the thing.

**Sentence rhythm.** Vary it, and let the short sentence be a real one rather
than a drum-beat. A one-line paragraph is a strong instrument with a small
budget: it is right for a definition, for the gloss under a suggested prompt,
and occasionally for a line the chapter genuinely turns on. It is wrong as a
way to make an ordinary transition sound consequential.

### The mechanical part

`make prose` checks what a machine can honestly check, and reports warnings
only — prose is not a build failure. `make prose-fix` applies the corrections
that need no judgement.

- **No comma before a restrictive because-clause.** "Worth knowing by name
  because it is the answer" — not "by name, because". The comma belongs only
  when the main clause is negative (where it changes the meaning) or when the
  clause is a genuine afterthought. This one is a Spanish habit carried into
  English, and a reader spotted it before the linter did.
- **No "because … is not because."** Two because-clauses in a sentence are fine
  when they are a pair ("not because X, but because Y"); they are hard to follow
  when the second is the predicate of the first.

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

Manuscript CC BY-NC 4.0; code EUPL-1.2. New code files in this repository (the
`Makefile`, `style.css`, CI workflows) need an `SPDX-License-Identifier:
EUPL-1.2` header. See `COPYING.md`.
