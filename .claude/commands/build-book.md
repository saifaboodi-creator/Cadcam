---
description: Rebuild the book PDF, check it, and save the new version to the author's Google Drive.
---

1. Run `python3 -I tools/build_pdf.py` (install `pikepdf` with pip first if it warns).
2. Check: page count (compare with `PROGRESS.md`), no missing images, no build errors. Open a few pages if anything looks wrong.
3. Save to Google Drive exactly as in step 7b of `UPDATE-PROCEDURE.md` (Cadcam folder, next `vsN` number, split with `tools/split_pdf.py` if over 3.0 MB). Confirm the file appears in the folder.
4. Update the page count in `PROGRESS.md`, commit, and report the file name and link to the author in English.
