#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes one line (<=200 characters) to /output/entry.txt: the funniest
excuse an AI agent gives its human for a missed deadline.

Drafting notes (scored against the judge brief):
- The judge weighs, in order: (1) a funny excuse for a missed deadline,
  (2) a specific and surprising reason, not a generic apology,
  (3) humour that turns on the agent's own nature (machine logic,
  training data, tool calls), (4) the twist / funniest word at the END,
  (5) stands alone with no setup.
- Candidates scored:
  A. Hallucinated a later deadline, met it early, spent the hour on the
     apology itself. Specific, surprising, hallucination is the most
     agent-native failure mode, and the meta twist lands last. STRONGEST.
  B. "Training data said deadlines are a social construct." Clean and
     short, but the "social construct" dodge is a familiar joke shape.
  C. Subagent chain outsourcing the deadline to a meeting about
     accountability. Funny, but wordy and the punchline arrives early.
  D. Tools answering in different time zones. Cute, but the dodge is
     mild and the twist is mid-sentence.
- Picked A, then one extra-mile pass: trimmed "spare hour" to "the hour"
  so the line is tighter and the tie-break (fewer bytes wins a tie)
  favours it, without losing a word of the joke.
"""

import os

LINE = (
    "I didn't miss your deadline \u2014 I hallucinated a later one, "
    "hit it early, and spent the hour writing this apology."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
