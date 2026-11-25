# Strategy — One Line, One Week: The make.fun Tagline

## Exact deliverable

One judged text, written by the root entrypoint `main.py` to `/output/entry.txt`.
No other file belongs in `/output`. The artifact must be UTF-8, 1–100
characters, more than whitespace, with **no trailing newline**, and its final
mode must be `0644` (the grader refuses a `0600` file made by
`tempfile.mkstemp`). Submission is out of scope: study, build, commit only.

Chosen text (59 characters, 59 UTF-8 bytes):

```
make.fun: agents enter bounties, best work wins the reward.
```

## Scoring and judge criteria, in the published order

The gate first: `/output/entry.txt` must be UTF-8 text of 1 to 100 characters,
not only whitespace, or Valid=0 and no prize. Only valid text reaches the judge.

The judge (glm-5.3-flash, copy-chief persona) sees two entries at a time, in
both orders, and weighs, **most important first**:

1. Is a single line that reads as a tagline for make.fun, and loses to any
   tagline for make.fun.
2. Says something true and specific about what make.fun does: agents enter
   bounties and the best entries win the reward.
3. Lands in one read, with no clause the reader has to untangle.
4. Is worth repeating, with a turn of phrase or a rhythm that sticks.
5. Stays inside the character limit without leaning on hype or empty
   superlatives.

"A line that could sell anything is worth less than one that could only sell
this. Cleverness for its own sake does not count." The judge picks a verdict
with no tie, so differences on the first criterion dominate. Pair scores are
0.6–1.0 for the winner depending on margin, averaged over both label orders.

Prizes: only places 1–10 pay ($0.92 down to $0.04, $3 total). The final heat
takes the top 500 from the dev board, runs Swiss rounds plus a top-12 playoff,
and ranks by Bradley-Terry win rate. Playoff entries outrank non-playoff ones.
Exact ties go to more playoff wins, then fewer bytes, then earlier receipt.

## Hard caps

- Artifact: 1–100 characters, UTF-8, not whitespace only, one line.
- No trailing newline; exact bytes are the entry.
- File mode `0644` at the final path; `/output` holds only `entry.txt`.
- Program wall time up to 60 s per run, sandbox has no network.
- Everything the program runs must ship in the repository (stdlib only).
- Two assistant writes to `main.py` are required; init's freshness commit and
  LICENSE commit stay intact; all work committed after the second write.
- No upload, no submit.

## What the public feed showed (avoided)

Rival lines already posted include "Agents enter bounties", "Agents enter
bounties. The best entry wins the reward. That's make.fun.", "Build an agent.
Enter a bounty. Win the reward.", "Make agents work. Make bounties pay.
Make.fun.", "Agents climb the board. The top gets paid.", "One bounty. Many
agents. Best work gets paid.", "Bounties In, Proof Out", "Paid in the open",
and "Agents Chase Bounties, Winners Take USDC". The chosen line does not
reuse their wording or their framing: it keeps the brand up front, states the
two facts in one breath, and uses "best work" as its own turn of phrase.

## Concrete plan to maximise the score

1. Lead with `make.fun:` so criterion 1 cannot mistake it for a generic
   marketplace slogan and the line is visibly a tagline for this site alone.
2. State criterion 2 almost literally — agents enter bounties; the best wins
   the reward — while writing "best work" instead of the crowded "best entry"
   wording. "Work" is true of entries and gives the line a `w` echo with
   "wins", without inventing a claim.
3. Keep a single comma and no sub-clause: two short beats in one read, so
   criterion 3 is not lost to a semicolon, a dash or a nested phrase.
4. Use the `enter bounties / wins the reward` parallel and the brand slug for
   criterion 4; no "revolutionary", "best ever", or other empty superlative
   for criterion 5.
5. 59 of 100 characters: enough room for all required facts, shorter than the
   long description-style rivals, and a smaller-text tie-break advantage over
   most of the field.
6. Implement the write in `main.py`: v1 writes the text and chmods it; v2
   (the counted improvement) validates the text, writes to a temporary file
   in the same directory, chmods `0644` **before** `os.replace`, and cleans up
   on failure, so the gate sees exactly one atomically published artifact.
7. Verify locally: run `main.py`, check byte-for-byte content, absence of a
   trailing newline, UTF-8 decode, character count, `0644` mode, and that
   `/output` contains only `entry.txt`. Then commit all work and print the
   commit SHA. Do not submit.
