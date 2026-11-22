---
description: Apply only the author-approved findings from reviews/NN-review.md to a chapter.
argument-hint: <chapter number, e.g. 07>
---

Apply the approved review findings for chapter **$ARGUMENTS**.

1. Read `CLAUDE.md`, `STYLE.md`, `reviews/$ARGUMENTS-review.md`, the chapter and its notes file.
2. Apply **only** findings marked `Y` in the Approve column. Skip anything unmarked or marked `N`. If the author wrote a comment on a finding, follow the comment.
3. For each fix, re-confirm the source on PubMed before changing text. Never invent references or numbers; if a fix cannot be confirmed, mark the sentence **[UNVERIFIED]** instead.
4. Run `python3 -I tools/renum.py` on the chapter file (`chapters/$ARGUMENTS-<slug>.md`, not the `.notes.md`) and check citations against the reference list. Update any table or figure whose data changed (follow `figures/FIGURE-STYLE.md`).
5. In the notes file, add a dated section "## Review YYYY-MM-DD" listing each applied finding by number. In the review file, mark applied findings `Done`.
6. Update `PROGRESS.md` (reference count, UNVERIFIED totals, status → "Draft 2 (reviewed)").
7. Commit with a message naming the chapter and the findings applied. Report to the author in English.
