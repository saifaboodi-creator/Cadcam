# Progress Log

Resume point for any new session. Update after every chapter.

## Rules for Chapters 10–20 (from the author)
- Same outline (`OUTLINE.md`), structure, style (`STYLE.md`) and depth as Chapters 1–9.
- Do **not** modify Chapters 1–9.
- Every reference checked on PubMed/DOI and checked to support its claim. Never invent references, numbers or studies. Anything not confirmed is marked **UNVERIFIED** in the chapter and in its notes file.
- Each chapter has a review-notes file next to it: `chapters/NN-slug.notes.md` (references to check, weak evidence, caveats, decisions made, UNVERIFIED list).
- Commit each chapter, then move straight on. If blocked, record why here and continue.
- Citation renumbering helper (Vancouver order of first appearance): `tools/renum.py` — run `python3 -I tools/renum.py chapters/NN-slug.md` (renumbers bracketed citations by first appearance and reorders the reference list).

## Status

| Ch | Title | File | Status | Refs | UNVERIFIED (inline marks) | Notes file |
|---|---|---|---|---|---|---|
| 1 | Introduction to CAD/CAM in Dentistry | `chapters/01-introduction.md` | Draft 2 (reviewed) | 22 | 8 | `chapters/01-introduction.notes.md` |
| 2 | The Digital Workflow and Data Formats | `chapters/02-digital-workflow-and-data.md` | Draft 2 (reviewed) | 19 | 2 | `chapters/02-digital-workflow-and-data.notes.md` |
| 3 | Accuracy in Digital Dentistry | `chapters/03-accuracy.md` | Draft 2 (reviewed) | 31 | 4 | `chapters/03-accuracy.notes.md` |
| 4 | Intraoral Scanners | `chapters/04-intraoral-scanners.md` | Draft 2 (reviewed) | 28 | 3 | `chapters/04-intraoral-scanners.notes.md` |
| 5 | Laboratory Scanners and Model Digitisation | `chapters/05-laboratory-scanners.md` | Draft 2 (reviewed) | 14 | 2 | `chapters/05-laboratory-scanners.notes.md` |
| 6 | Three-Dimensional Imaging Beyond the Teeth | `chapters/06-imaging-beyond-teeth.md` | Draft 2 (reviewed) | 21 | 0 | `chapters/06-imaging-beyond-teeth.notes.md` |
| 7 | Design Software: Principles and Tools | `chapters/07-design-software.md` | Draft 2 (reviewed) | 21 | 0 | `chapters/07-design-software.notes.md` |
| 8 | Designing Tooth-Supported Restorations | `chapters/08-tooth-supported-restorations.md` | Draft 2 (reviewed) | 17 | 0 | `chapters/08-tooth-supported-restorations.notes.md` |
| 9 | Designing Implant Restorations | `chapters/09-implant-restorations.md` | Draft 2 (reviewed) | 26 | 0 | `chapters/09-implant-restorations.notes.md` |
| 10 | Subtractive Manufacturing: Milling and Grinding | `chapters/10-subtractive-manufacturing.md` | Draft 2 (reviewed) | 26 | 1 | `chapters/10-subtractive-manufacturing.notes.md` |
| 11 | Additive Manufacturing (3D Printing) | `chapters/11-additive-manufacturing.md` | Draft 2 (reviewed) | 27 | 3 | `chapters/11-additive-manufacturing.notes.md` |
| 12 | Finishing, Characterisation and Quality Control | `chapters/12-finishing-quality-control.md` | Draft 2 (reviewed) | 23 | 0 | `chapters/12-finishing-quality-control.notes.md` |
| 13 | Glass-Ceramics | `chapters/13-glass-ceramics.md` | Draft 2 (reviewed) | 26 | 0 | `chapters/13-glass-ceramics.notes.md` |
| 14 | Zirconia | `chapters/14-zirconia.md` | Draft 2 (reviewed) | 28 | 12 | `chapters/14-zirconia.notes.md` |
| 15 | Resin-Based and Hybrid Materials; Metals | `chapters/15-resins-hybrids-metals.md` | Draft 2 (reviewed) | 26 | 0 | `chapters/15-resins-hybrids-metals.notes.md` |
| 16 | Chairside CAD/CAM in Restorative Dentistry | `chapters/16-chairside-cadcam.md` | Draft 2 (reviewed) | 21 | 1 | `chapters/16-chairside-cadcam.notes.md` |
| 17 | Digital Implant Dentistry | `chapters/17-digital-implant-dentistry.md` | Draft 2 (reviewed) | 25 | 0 | `chapters/17-digital-implant-dentistry.notes.md` |
| 18 | Removable Prosthodontics | `chapters/18-removable-prosthodontics.md` | Draft 2 (reviewed) | 27 | 0 | `chapters/18-removable-prosthodontics.notes.md` |
| 19 | Orthodontics and Other Specialties | `chapters/19-orthodontics-other-specialties.md` | Draft 2 (reviewed) | 26 | 0 | `chapters/19-orthodontics-other-specialties.notes.md` |
| 20 | Implementation, Economics, Education and the Future | `chapters/20-implementation-future.md` | Draft 2 (reviewed) | 28 | 3 | `chapters/20-implementation-future.notes.md` |

## Figures and tables
- 57 original SVG figures in `figures/` (2–3 per chapter; style in `figures/FIGURE-STYLE.md`), 62 tables (at least 3 per chapter). Data charts reuse only numbers and citations already in the text. Each chapter's notes file lists its figures and tables under "Figures and tables added".
- Preview a figure: `node tools/render_svg.js figures/<file>.svg`. Rebuild the PDF: `python3 -I tools/build_pdf.py` (226 pages after the full independent review, 2026-11-22; 234 pages after the verification notes were added, 2026-11-25).

## UNVERIFIED totals
- After the independent review (2026-11-22), inline marks per chapter: Ch 1 (8), Ch 2 (2), Ch 3 (4), Ch 4 (3), Ch 5 (2), Ch 10 (1), Ch 11 (3), Ch 14 (12), Ch 16 (1), Ch 20 (3) = **39 inline marks**. Each is listed in the chapter's notes file (one item can carry several marks, e.g. the same claim in text, caption and Key Points).
- **Verification notes (2026-11-25, author request):** 29 note tables, one under each paragraph, caption, table or Key Point that carries a mark, graded **10 major / 29 minor** marks (rule in `STYLE.md`; master list `reviews/UNVERIFIED-table.md`). Inline mark count unchanged (39). Draft PDF rebuilt (234 pages, `build/`); not yet saved to Drive.
- New marks came from review fixes that the PubMed abstract could not confirm (e.g. Ch 14 phosphoric acid and shrinkage figures; Ch 1 Duret claims; Ch 2 GDPR/HIPAA; Ch 5 mounting methods).
- Chapter 8 survival data updated to Pjetursson 2026 (author request).

## Independent reviews
- **All 20 chapters reviewed (2026-11-22).** Reports in `reviews/NN-review.md`: 540 confirmed findings (1 critical, 85 major, 454 minor). The author approved all findings ("approve all", 2026-11-22); all were applied to every chapter, which is now Draft 2 (reviewed). New references added: Ch 9 Staubli 2017, Ch 11 Cai 2025 (RCT), Ch 13 De Freitas 2020. Total references 482. PDF (226 pages, 3.06 MB, split for upload) saved to Google Drive as `CADCAM-in-Dentistry-vs5-part1.pdf` (pp. 1–113, https://drive.google.com/file/d/1GOZ3U4BY_EI42ALKnGZd-N21w0XpVlfA/view) and `-vs5-part2.pdf` (pp. 114–226, https://drive.google.com/file/d/1188nvF5ie8057gjBPnfoZdjakoNuV89w/view).
- Method: Ch 6–20 (and 16) used three independent checker subagents plus a separate filter subagent. Ch 1–5 were reviewed by one agent running the three checks and the filter as separate passes (subagents were not available to it); the reports say so.
- Critical: Ch 11 says printed zirconia/ceramics have no clinical data, but a 12-month RCT exists (Cai F et al. J Dent. 2025;162:106069; PMID 40885299), verified on PubMed.
- **Ch 16** (2026-11-22): 30 confirmed findings (5 major, 25 minor), all approved and applied; refs 21 → 21; UNVERIFIED unchanged (1). Figure 16.3 labels updated. PDF saved to Google Drive (Cadcam folder) as `CADCAM-in-Dentistry-vs4.pdf` (221 pages, 2.97 MB): https://drive.google.com/file/d/1UQUnqnDmgPAWtcy3oD7pHKZV2Gka_FLx/view

## Quarterly literature updates
- **Last update: 2026-11-17** (quarterly update 1; search window 2026-10-01 to 2026-11-17). Report: `updates/2026-11.md`. Next update due about 2027-02.
- Update 1: 10 references added in 9 chapters (Ch 3, 4, 6, 7, 11, 14, 17, 18, 20); 3 reference entries completed (Ch 15 article numbers); 0 new UNVERIFIED items. Reference list entries across the book: 468 → 478.
- Renumbering: where a new reference was added, `tools/renum.py` renumbered the chapter. Old → new maps are in each changed notes file under "Update 2026-11"; older notes sections use the old numbers.

## Blockers
None. All 20 chapters are Draft 2 (reviewed) after the 2026-11-22 independent review; next phase is author review.
