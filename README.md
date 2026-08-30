# Prompt to Evidence

**The data literacy your AI agent assumes you already know.**

A short book for people who are not experts in math or statistics but need
to make decisions from data — in economics, science, marketing, wherever an
agent can now produce a number on request. Reading an A/B test result,
measuring whether a campaign actually caused the lift it's credited with:
the reader works comfortably in Excel and wants to go where their data team
already lives, not become a statistician.

Companion to [*Prompt to
Production*](https://github.com/alpibrusl/prompt-to-production) — same
voice, same tooling, different subject. That book is software engineering
discipline for people who cannot read code; this one is analytical
discipline for people who are not mathematicians. Its own Chapter 1
explicitly excludes ML and statistical work from scope — this book is what
fills that gap.

> The agent will compute almost any comparison you ask for, and will rarely
> tell you whether the comparison was a fair one.

## Contents

| | Part | Chapters |
|---|---|---|
| **I** | The Ground | The handoff · where your data actually lives · the shape of an analysis |
| **II** | Trusting the Number | Make it compute, not guess · the tool, not the answer · borrowed, not reinvented · test it against what you already know |
| **III** | Making the Decision | Comparing two things fairly · measuring what you did · confidence, not certainty |
| **IV** | Seeing and Learning | A chart is a claim · when the agent wants to build a model · data you can trust |
| **V** | Working With the Agent | Asking the right question · the minimum bar |

**Status: complete draft.** All 15 chapters written; ~16,000 words, 23 defined terms, 73 pages.

## The four rules

Every chapter either builds toward these or applies them to a specific kind
of decision:

1. **Make the agent compute, never guess** — force code execution, not
   token-level arithmetic that merely looks like calculation.
2. **Write the general tool; treat this case as one input to it** — not a
   script tuned to look right for today's numbers.
3. **Use established, heavily-used libraries over reimplemented statistics**
   — the same supply-chain trust logic as *Prompt to Production* chapter 2,
   aimed at numerical correctness instead of security.
4. **Test against a case where you already know the answer, and be
   suspicious of extreme results in both directions** — a suspiciously
   perfect number and a suspiciously terrible one get the same treatment:
   stop and look for a bug before you believe either one.

## The book is source

The manuscript is Markdown. The EPUB and PDF are build artifacts — derived
from the source, never committed, rebuilt on demand. This is
[bookkit](https://github.com/alpibrusl/content-kit)'s premise, shared with
this book's companion volume.

```bash
pip install "content-kit-core @ git+https://github.com/alpibrusl/content-kit@main#subdirectory=packages/core"
pip install "bookkit[epub] @ git+https://github.com/alpibrusl/content-kit@main#subdirectory=packages/bookkit"

make check     # lint the manuscript against the concept ledger
make epub      # → build/prompt-to-evidence.epub
make html      # → build/prompt-to-evidence.html
make pdf       # → build/prompt-to-evidence.pdf   (needs Pango, see below)
make audiobook # → build/audiobook/chapter_NN/     (audio source)
make all       # check + epub + html
```

`make pdf` needs WeasyPrint's system libraries, which pip cannot install —
`libpango-1.0-0` and `libpangoft2-1.0-0` on Debian/Ubuntu, `pango` via
Homebrew on macOS. It is deliberately left out of `make all` so the default
build works without them; CI installs them and builds all three formats.

## The concept ledger and the gate

Same mechanism as *Prompt to Production*: `glossary.yaml` is the canon,
`scripts/check_terms.py` lints the manuscript against it and fails the build
if a term is used before its chapter defines it, and `GLOSSARY.md` is
generated rather than hand-written. See that book's README for the full
mechanics — this repository's tooling is a direct copy, unmodified.

## Licence

Manuscript: [CC BY-NC 4.0](COPYING.md). Code: [EUPL-1.2](LICENSE), matching
content-kit and this book's companion volume. See [COPYING.md](COPYING.md).
