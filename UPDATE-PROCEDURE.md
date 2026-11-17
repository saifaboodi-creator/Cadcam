# Quarterly Literature Update Procedure

The book is updated every 3 months. Each update session follows these steps exactly.

## Goal
Keep the evidence current. Add important new studies (especially systematic reviews, meta-analyses, RCTs and guidelines), replace superseded data, and fix reference details of online-first papers. Do **not** rewrite chapters, change their structure or invent anything.

## Steps
1. **Read first:** `PROGRESS.md`, `STYLE.md`, `figures/FIGURE-STYLE.md` and the latest report in `updates/` (if any). The search window starts at the date of the last report, or 2026-11-17 for the first update.
2. **Fix pending reference details.** In every `chapters/*.notes.md`, look under "References to check" for papers listed as online-first or missing volume/pages. Look each up on PubMed. Where final details now exist, update the reference entry in the chapter and remove the item from the notes.
3. **Search for new evidence**, chapter by chapter, using PubMed (`search_articles` with `date_from` = window start). Prioritise systematic reviews and meta-analyses, RCTs, large cohorts and clinical guidelines on each chapter's key topics (see `OUTLINE.md`). Ignore single small in vitro studies unless they change a stated conclusion.
4. **Decide per finding:**
   - **Supersedes existing data** (e.g., a newer review of the same question): update the sentence, numbers and table, keep the older reference only as historical context if useful.
   - **Adds an important new result**: add one or two sentences in the relevant section.
   - **Conflicts with the text**: present both and state the conflict. Do not silently pick one.
   - Otherwise: do nothing.
5. **Verification rules (unchanged from the original writing):**
   - Every number or claim attached to a reference must appear in its PubMed abstract or metadata. Never invent references, numbers or studies.
   - Anything that cannot be confirmed is marked **[UNVERIFIED]** inline and in the notes file.
   - After editing a chapter, run `python3 -I tools/renum.py chapters/NN-slug.md` and check that citations match the reference list.
   - If a figure or table shows data that changed, update it as well (follow `figures/FIGURE-STYLE.md`; preview with `node tools/render_svg.js`).
6. **Record:**
   - In each changed chapter's notes file, add a dated section "## Update YYYY-MM" listing what changed and why.
   - Write `updates/YYYY-MM.md`, including:
     - the search window;
     - chapters checked;
     - each change with its PMID or DOI;
     - references whose details were completed;
     - new UNVERIFIED items;
     - candidate papers considered but not added, with the reason;
     - the top 5 items for the author to review.
   - Update `PROGRESS.md`: reference counts, UNVERIFIED totals and last update date.
7. **Rebuild** the PDF with `python3 -I tools/build_pdf.py`, then check the page count and that there are no missing images.
8. **Commit and push** to the book branch (`claude/cad-cam-dentistry-book-5d2foe`). Commit in logical steps, for example one commit per chapter group plus one for the report and PDF.
9. If PubMed or GitHub is unavailable, write the report with status **BLOCKED** and the reason, commit what is possible, and stop.

## Scope limits
- Do not change the outline, chapter order, style or figure style.
- Keep each chapter within roughly ±10% of its current length unless a major new guideline requires more.
- The author reviews every update. The report must make every change easy to find.
