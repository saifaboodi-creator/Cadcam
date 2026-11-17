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

| Ch | Title | File | Status | Refs | UNVERIFIED | Notes file |
|---|---|---|---|---|---|---|
| 1 | Introduction to CAD/CAM in Dentistry | `chapters/01-introduction.md` | Draft 1 | 22 | 1 | `chapters/01-introduction.notes.md` |
| 2 | The Digital Workflow and Data Formats | `chapters/02-digital-workflow-and-data.md` | Draft 1 | 19 | 0 | `chapters/02-digital-workflow-and-data.notes.md` |
| 3 | Accuracy in Digital Dentistry | `chapters/03-accuracy.md` | Draft 1 | 31 | 2 | `chapters/03-accuracy.notes.md` |
| 4 | Intraoral Scanners | `chapters/04-intraoral-scanners.md` | Draft 1 | 28 | 1 | `chapters/04-intraoral-scanners.notes.md` |
| 5 | Laboratory Scanners and Model Digitisation | `chapters/05-laboratory-scanners.md` | Draft 1 | 14 | 0 | `chapters/05-laboratory-scanners.notes.md` |
| 6 | Three-Dimensional Imaging Beyond the Teeth | `chapters/06-imaging-beyond-teeth.md` | Draft 1 | 21 | 0 | `chapters/06-imaging-beyond-teeth.notes.md` |
| 7 | Design Software: Principles and Tools | `chapters/07-design-software.md` | Draft 1 | 21 | 0 | `chapters/07-design-software.notes.md` |
| 8 | Designing Tooth-Supported Restorations | `chapters/08-tooth-supported-restorations.md` | Draft 1 | 17 | 0 | `chapters/08-tooth-supported-restorations.notes.md` |
| 9 | Designing Implant Restorations | `chapters/09-implant-restorations.md` | Draft 1 | 25 | 0 | `chapters/09-implant-restorations.notes.md` |
| 10 | Subtractive Manufacturing: Milling and Grinding | `chapters/10-subtractive-manufacturing.md` | Draft 1 | 26 | 1 | `chapters/10-subtractive-manufacturing.notes.md` |
| 11 | Additive Manufacturing (3D Printing) | `chapters/11-additive-manufacturing.md` | Draft 1 | 26 | 0 | `chapters/11-additive-manufacturing.notes.md` |
| 12 | Finishing, Characterisation and Quality Control | `chapters/12-finishing-quality-control.md` | Draft 1 | 23 | 0 | `chapters/12-finishing-quality-control.notes.md` |
| 13 | Glass-Ceramics | `chapters/13-glass-ceramics.md` | Draft 1 | 25 | 0 | `chapters/13-glass-ceramics.notes.md` |
| 14 | Zirconia | `chapters/14-zirconia.md` | Draft 1 | 28 | 0 | `chapters/14-zirconia.notes.md` |
| 15 | Resin-Based and Hybrid Materials; Metals | `chapters/15-resins-hybrids-metals.md` | Draft 1 | 26 | 0 | `chapters/15-resins-hybrids-metals.notes.md` |
| 16 | Chairside CAD/CAM in Restorative Dentistry | `chapters/16-chairside-cadcam.md` | Draft 1 | 21 | 1 | `chapters/16-chairside-cadcam.notes.md` |
| 17 | Digital Implant Dentistry | `chapters/17-digital-implant-dentistry.md` | Draft 1 | 25 | 0 | `chapters/17-digital-implant-dentistry.notes.md` |
| 18 | Removable Prosthodontics | `chapters/18-removable-prosthodontics.md` | Draft 1 | 27 | 0 | `chapters/18-removable-prosthodontics.notes.md` |
| 19 | Orthodontics and Other Specialties | `chapters/19-orthodontics-other-specialties.md` | Draft 1 | 26 | 0 | `chapters/19-orthodontics-other-specialties.notes.md` |
| 20 | Implementation, Economics, Education and the Future | `chapters/20-implementation-future.md` | Draft 1 | 28 | 2 | `chapters/20-implementation-future.notes.md` |

## Figures and tables
- 57 original SVG figures in `figures/` (2–3 per chapter; style in `figures/FIGURE-STYLE.md`), 62 tables (at least 3 per chapter). Data charts reuse only numbers and citations already in the text. Each chapter's notes file lists its figures and tables under "Figures and tables added".
- Preview a figure: `node tools/render_svg.js figures/<file>.svg`. Rebuild the PDF: `python3 -I tools/build_pdf.py` (220 pages after update 2026-11).

## UNVERIFIED totals
- Marked inline: Ch 10 (1), Ch 16 (1), Ch 20 (2) = 4.
- Chapters 1–9 (marked inline after the author approved changes): Ch 1 (1 item, 5 inline marks), Ch 3 (2 items, 3 inline marks), Ch 4 (1) = 4.
- **Book total: 8 UNVERIFIED items, all now marked inline.**
- Chapter 8 survival data updated to Pjetursson 2026 (author request).

## Quarterly literature updates
- **Last update: 2026-11-17** (quarterly update 1; search window 2026-10-01 to 2026-11-17). Report: `updates/2026-11.md`. Next update due about 2027-02.
- Update 1: 10 references added in 9 chapters (Ch 3, 4, 6, 7, 11, 14, 17, 18, 20); 3 reference entries completed (Ch 15 article numbers); 0 new UNVERIFIED items. Reference list entries across the book: 468 → 478.
- Renumbering: where a new reference was added, `tools/renum.py` renumbered the chapter. Old → new maps are in each changed notes file under "Update 2026-11"; older notes sections use the old numbers.

## Blockers
None. All 20 chapters at Draft 1 (Chapters 10–20 completed in one run; author review pending).
