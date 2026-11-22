---
description: Review a chapter in rounds — fix only safe, source-confirmed errors, re-review — until no critical or major findings remain (max 3 rounds). Every change is logged for the author.
argument-hint: <chapter number, e.g. 16>
---

Run a review loop on chapter **$ARGUMENTS**. Follow `CLAUDE.md` and `STYLE.md`.

## Stop condition
Stop when a fresh review round finds **no critical or major findings**, or after **3 rounds**, whichever comes first.

## Each round
1. **Review.** Do exactly what `/review-chapter $ARGUMENTS` does (three independent parallel checkers, then the false-positive filter). Save the round's findings in `reviews/$ARGUMENTS-review.md` under a heading "## Round N".
2. **Fix only safe items** — corrections that make the text match its own source, with no judgement about content:
   - wrong reference details (authors, year, journal, volume, pages, PMID, DOI) → correct them from PubMed;
   - a number or claim that differs from the cited abstract → change it to what the abstract says;
   - a claim that cannot be confirmed in its source → mark it **[UNVERIFIED]** inline and in the notes file (do not delete it);
   - a number that differs between text, table, figure and Key Points, where the source settles which is right → make them consistent.
3. **Do not fix — leave for the author** (mark "Author decision" in the review file): rewording overstatement, adding or replacing references, removing content, changing scope, structure or conclusions, or anything where two readings are reasonable.
4. After fixing: run `python3 -I tools/renum.py` on the chapter file (not the `.notes.md`), check citations against the reference list, and update any table or figure whose data changed (`figures/FIGURE-STYLE.md`).
5. Log every fix in the review file (finding number, old text, new text, PMID) and in the notes file under "## Review loop YYYY-MM-DD". Commit the round: `Review loop ch $ARGUMENTS, round N: <k> fixes`.

## End
- Update `PROGRESS.md` (reference count, UNVERIFIED totals; status "Draft 2 (review loop) — author decisions pending" if any remain).
- Report to the author in English: rounds run, why it stopped, fixes made (count by type), new UNVERIFIED items, and the list of "Author decision" items. Then use `/apply-review $ARGUMENTS` for the ones the author approves.
