# Manuscript Style Guide

## Voice
- Write as an experienced clinician-teacher: direct and precise, without hype. Avoid marketing language ("revolutionary", "game-changing").
- Separate what the evidence shows from expert opinion. State the level of evidence (in vitro, case series, RCT, systematic review) when it matters.
- Use brand names only when they matter historically or the evidence is specific to a product. Otherwise use generic terms.

## Chapter template
1. Chapter title
2. Learning objectives (4–6 bullets)
3. Numbered sections (1.1, 1.2, ...)
4. Boxes where useful: **Clinical Tip**, **Lab Note**, **Evidence Box**
5. Key points (summary bullets)
6. Review questions (for students)
7. References (Vancouver)

## Terminology
- "CAD/CAM" (not CAD-CAM or CADCAM).
- "Intraoral scanner (IOS)"; "digital impression" or "optical impression" for the act of scanning.
- Accuracy is reported as **trueness** and **precision** (ISO 5725), not as "accuracy" alone.
- "Fixed dental prosthesis (FDP)" rather than "bridge" in formal text; "bridge" may be given in parentheses on first use.
- Units: µm for fit and deviation; MPa for strength. Exception: implant positional deviations are given in mm and degrees, as in the source literature (author-approved, Ch 17 review, 2026-11-22).

## References
- Vancouver style, numbered by first citation within the chapter: [1], [2–4].
- Verify every reference on PubMed. Record the DOI.
- Prefer systematic reviews and clinical trials for clinical claims. Use in vitro data only for mechanisms or properties, and label it as in vitro.
- Never cite a paper whose abstract or full text has not been checked.
- **Verification notes (author, 2026-11-25):** every paragraph, caption, table or Key Point with an [UNVERIFIED] mark is followed directly by a "**Verification note — Major/Minor conflict.**" table (Claim not confirmed | Conflict | Reason | To resolve), so it prints on the same page. Not an appendix. Major = a clinical instruction or threshold, or a specific number without a confirmed source; minor = everything else. Do not write the word UNVERIFIED inside the note (it would change the counts). References in notes are plain "ref N", which `renum.py` does not renumber: update them by hand after renumbering. When a mark is resolved, delete its row (and the note if it is empty). Master list: `reviews/UNVERIFIED-table.md`.
