# Where Your Data Actually Lives

Ask where the numbers came from and the honest answer is usually a shrug — *it's in the system* — as if that settles the question. It does not. Where data physically sits changes what can silently go wrong with it, and knowing the shape of your own data is the first thing a data team does before they trust anything built on top of it.

## The usual places

**A spreadsheet** is the most familiar shape, and the most deceptive one because every cell looks the same regardless of what put the value there. A cell can hold a number pulled fresh from a system this morning, or a number someone typed in by hand in March and never updated, or a formula referencing a cell three tabs away that got deleted last month and now silently returns zero. Nothing about how it looks tells you which.

**A database** is what a live system actually reads and writes while it runs. You rarely see it directly — you send it a query, and it sends back rows. This is more reliable than a spreadsheet in one specific way, structure is enforced, but it introduces a failure mode spreadsheets don't have: the query itself can be wrong, quietly returning a real, correctly-formatted answer to a slightly different question than the one you meant to ask.

**An API or a live feed** hands you data continuously from somewhere you do not control, inside or outside your organisation. The danger here is drift: a column that meant one thing in January can start meaning something adjacent in July, after a change nobody upstream thought to mention to you, and every request keeps returning cleanly-formatted data throughout.

**Logs and event streams** are the rawest of the four — one row per thing that happened, unfiltered, usually enormous, and genuinely useful precisely because nobody has shaped it into a story yet. It also means it needs real cleaning before it can answer anything; Chapter 13 is about that specifically.

Bellwood's checkout data lives in exactly this last category — one row per page view, click, and completed order, streaming continuously — which is exactly why the next section matters before any of it gets analysed.

None of these is inherently more trustworthy than another. Each fails differently, and knowing which one you're looking at tells you which questions are worth asking before you believe what it shows you.

## Volume is not information

Here is an idea worth being explicit about, because it is easy to nod along with and still act as though it isn't true: **more rows are not more information.**

A million identical rows carry exactly as much information as one of them does. Nothing about the other 999,999 changes what you know. This matters because there are two genuinely different problems a dataset can have, and they need entirely different fixes.

**Noise** is random scatter around the true answer — one customer happens to spend more this week, another less, for reasons that wash out across enough of them. More data cures noise. Average enough noisy observations together and the randomness cancels itself out; that is, mechanically, why a bigger sample gives a more precise estimate.

**Bias** is a systematic skew — a distortion that every single row carries in the same direction because of *how* the data was collected rather than what happened to be measured. A survey that only reached people who opened an email is missing everyone who didn't, in the same direction, every time. More responses from that survey do not fix this. They give you a more precise, more confident estimate of the wrong thing.

This is the distinction to hold onto: **more data fixes noise. It does nothing whatsoever for bias.** A well-designed sample of five thousand people, chosen so every group you care about is properly represented, can be worth more than five million rows scraped from whoever happened to click something. Chapters 8 and 9 are largely about spotting bias hiding inside a comparison that otherwise looks perfectly clean.

## Develop small, run large

*Prompt to Production* keeps a small, disposable copy of a system to experiment against, rather than testing changes on the version real customers touch. The same move applies here, for the same reasons.

Bellwood's checkout event log runs into the tens of millions of rows across a year; nobody develops a new analysis against all of them on the first attempt. If your dataset is a hundred thousand rows, or ten million, do not develop your analysis against the whole thing. Pull a **representative sample** — a smaller slice built so it still reflects the same mix the full dataset has, not just whichever rows happened to load first — a few hundred or a few thousand, enough to be genuinely like the whole but small enough to rerun in seconds. Get the method right there. A mistake found on a thousand rows costs you ten seconds and another attempt. The same mistake found only after running on the whole ten million can cost real money, if the computation is billed, or real time, if it is merely slow, and either way it costs you the far worse experience of debugging a method that is *also* still wrong, at the least convenient possible scale to be doing it at.

The word "representative" is doing the actual work in that sentence. Taking the first thousand rows of a file sorted by date gives you one particular week, not a picture of the whole year — a sample chosen badly is a sample with bias baked into it, the exact problem the previous section just named. A representative sample needs to be picked so it reflects the same proportions — of customer types, time periods, whatever varies in ways that matter — as the data it's standing in for; ask for this explicitly, because "just grab a subset" and "grab a subset that looks like the whole" are different instructions with different failure modes.

Once the method holds up on the small slice — checked, ideally, against a case where you already know what the right answer looks like (Chapter 7) — running it on everything is the easy part.

## What to ask for

> "How many rows do we actually have, and is this a representative sample or does it favour a particular time period, customer type, or group of people who happened to respond?"

The volume-versus-information question, asked directly. A confident "we have millions of rows" is not an answer to it.

> "Develop this against a small, representative sample first — a few hundred rows is plenty — and show me the result before running it against everything."

Cheap, fast, and it catches a wrong method before it has cost you real time or real money to be wrong at scale.

> "If this result turned out to be wrong, would the problem more likely be that we don't have enough data, or that the data we have is skewed in some direction? Those need different fixes, and it's worth knowing which one we'd be chasing."
