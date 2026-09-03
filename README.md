# Prompt to Evidence

**The data literacy your AI agent assumes you already know.**

A short book for people who are not experts in math or statistics but need
to make decisions from data — in economics, science, marketing, wherever an
agent can now produce a number on request. Reading an A/B test result,
measuring whether a campaign actually caused the lift it's credited with:
the reader works comfortably in Excel and wants to go where their data team
already lives, not become a statistician.

One of three companions to [*Prompt to
Production*](https://github.com/alpibrusl/prompt-to-production) — same
voice, same tooling, different subject each time. That book is software
engineering discipline for people who cannot read code; this one is
analytical discipline for people who are not mathematicians. Its own
Chapter 1 explicitly excludes ML and statistical work from scope — this
book is what fills that gap. The third, [*Prompt to
Ledger*](https://github.com/alpibrusl/prompt-to-ledger), is financial
discipline for people who are not accountants. The fourth, [*Prompt to
Decision*](https://github.com/alpibrusl/prompt-to-decision), is the layer
above all three: deciding whether to act on a recommendation, not just
verifying it.

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

**Status: complete draft**, plus a closing afterword. 16 chapters; ~17,700 words, 24 defined terms, 81 pages.

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
4. **Test against a case where you already know the answer, and stay
   suspicious of every result, not just the extreme-looking ones** — the
   scalable version is a consistency check: does this agree with something
   else you already know? A suspiciously perfect number and a suspiciously
   terrible one both fail that check loudly; an ordinary-looking wrong
   number just fails it quietly, which is exactly why the check has to run
   on everything, not only on what already looks wrong.

## The book is source

The manuscript is Markdown. The EPUB and PDF are build artifacts — derived
from the source, never committed, rebuilt on demand. This is
[bookkit](https://github.com/alpibrusl/content-kit)'s premise, shared with
this book's companion volumes.

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
`bookkit check terms` lints the manuscript against it and fails the build if
a term is used before its chapter defines it, and `GLOSSARY.md` is generated
by `bookkit glossary` rather than hand-written.

The gate used to be a `scripts/` directory copied byte for byte into each of
the four books. It now lives upstream in
[bookkit](https://github.com/alpibrusl/content-kit) — one implementation, four
books, no copies to keep in step — so this repository holds only what is
actually specific to this volume: the manuscript, its ledger, and its
`verify-*` skill. Full design:
[`docs/ledger.md`](https://github.com/alpibrusl/content-kit/blob/main/packages/bookkit/docs/ledger.md).

## Installing the skill

`skills/verify-evidence/` is this book's closing checklist, packaged so an agent runs
it. It is what Session 8 of the bootcamp asks students to run, and it works in
any agent that reads the `SKILL.md` format.

Copy the whole folder — `SKILL.md` and the `references/` directory beside it.
The checklist the skill actually works from lives in `references/`, so
`SKILL.md` on its own loads and then has nothing to read.

**Claude Code** — `~/.claude/skills/verify-evidence/` for every project, or
`.claude/skills/verify-evidence/` for one.

**opencode** — reads `~/.claude/skills/` as well, so the line above may be all
you need. Otherwise `~/.config/opencode/skills/verify-evidence/`, or point at this
repository without copying anything:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "skills": { "paths": ["/path/to/prompt-to-evidence/skills"] },
  "permission": { "read": "allow", "external_directory": "allow", "edit": "deny" }
}
```

The `permission` block matters when the skill lives outside the working
directory, as `paths` implies. opencode asks before reading there, and
`opencode run` — the headless form the capstone uses — has nobody to ask, so
it waits silently and looks like a hang. Granting it up front avoids that.
`edit: deny` is optional; the skill only reads.

`opencode debug skill` lists every skill it can see and where each came from.
Needs 1.17.12 or newer — `references/` path resolution was fixed in 1.17.10 and
1.17.12, and on older builds the skill loads but cannot read its own checklist.

The agent decides when the skill applies; you do not invoke it by name. The
same instructions are in the book itself, as *Appendix — Running the Skill*.

## Licence

Manuscript: [CC BY-NC 4.0](COPYING.md). Code: [EUPL-1.2](LICENSE), matching
content-kit and this book's companion volumes. See [COPYING.md](COPYING.md).
