# A Note from the Human Author

> **Afterword**

Everything in this book describes how people learned to trust a number. Every check in it — a known-answer test, a consistency check, a range instead of a point — was invented by humans, for humans who could not simply watch the computation happen and know it was right.

That is worth sitting with for a moment because it is not obviously true of an agent. A person running a regression by hand, or even in a spreadsheet they built line by line, absorbed a rough sense of where it could go wrong along the way — which is exactly the sense this book has spent its length trying to hand you without the years it usually takes to earn. An agent has something different: it can execute the actual computation mechanically, exactly as instructed, and still have no more insight than you do into whether the comparison behind it was fair, or the right one to have run at all. Fluency and understanding came bundled in a person. They don't have to come bundled in a tool, and increasingly they don't.

I have argued elsewhere — at `alpibru.com/manifesto` — that this is the deeper shift underneath all of it: comprehension used to be the only practical basis for trusting a result because it was the only one available. It no longer is. A known-answer test that a method visibly passes tells you something a beautiful derivation you merely nodded along to never did. Comprehension was a strategy. It is not the only one.

So I should be honest about what this book actually is. It teaches verification, not comprehension — and it teaches it because verification is the version of rigor available to a reader who was never going to derive a t-distribution from first principles, agent or no agent.

Look back at what actually did the work in each chapter. Test the method before trusting it. Carry a range, not a headline number. Check whether a comparison was genuinely fair before crediting it. Ask what else changed at the same time. Stay suspicious of every result, not only the ones that already look wrong. Every one of those is something you can do, and confirm was done, without following a single line of the mathematics underneath it. None of them asks you to comprehend anything. That is not a lesser version of rigor. For this book's reader, it is the only version that was ever actually available — an agent producing the number changes what you're checking, not whether checking was always the real job.

The parts I am less certain will age well are the ones that lean on a human doing the noticing — remembering to ask for the range, remembering that an unusually good result deserves the same suspicion as a bad one. I would not be surprised if, before long, an analytical pipeline runs consistency checks and reports its own confidence by default, the way a compiler now catches a class of mistake nobody has to remember to look for by hand. If that happens, this book's specific instructions age out. The habit underneath them — evidence, not just a number — does not.

What does not change, here or in the argument I make elsewhere, is where responsibility sits. An agent can run a comparison exactly as instructed and still not be the one accountable for the decision built on it. That was never going to be delegated, and no improvement in the tooling moves it.

Read what came before as the discipline available to you today. Not the last word on what evidence will require.

— Alfonso Sastre
