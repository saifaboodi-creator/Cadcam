# CAD/CAM in Dentistry: From Scan to Restoration

Working manuscript for a comprehensive, evidence-based book on computer-aided design and computer-aided manufacturing (CAD/CAM) in dentistry.

**Audience:** dental students, practising dentists, and dental technicians. Each chapter covers the science, the clinical workflow and the laboratory side.
**Language:** English.
**Referencing:** Vancouver style, numbered in order of first citation, with a separate reference list per chapter. Every reference is checked against PubMed (PMID/DOI recorded).

## Repository layout

| Path | Contents |
|---|---|
| `OUTLINE.md` | Full table of contents with section plans for every chapter |
| `chapters/` | One Markdown file per chapter (`01-introduction.md`, ...) |
| `STYLE.md` | Writing and formatting conventions for the manuscript |
| `PROGRESS.md` | Chapter status, UNVERIFIED totals, resume notes |
| `build/CADCAM-in-Dentistry-Draft.pdf` | Compiled book (all 20 chapters) |
| `tools/build_pdf.py` | Rebuilds the PDF: `python3 -I tools/build_pdf.py` (needs pandoc + Playwright/Chromium) |
| `tools/renum.py` | Renumbers citations in Vancouver order of first appearance |
| `UPDATE-PROCEDURE.md` | Quarterly literature-update procedure; reports go in `updates/` |

## Status

| Chapter | Status |
|---|---|
| Outline | Draft 1 |
| 1. Introduction to CAD/CAM in Dentistry | Draft 2 (reviewed) |
| 2. The Digital Workflow and Data Formats | Draft 2 (reviewed) |
| 3. Accuracy in Digital Dentistry | Draft 2 (reviewed) |
| 4. Intraoral Scanners | Draft 2 (reviewed) |
| 5. Laboratory Scanners and Model Digitisation | Draft 2 (reviewed) |
| 6. Three-Dimensional Imaging Beyond the Teeth | Draft 2 (reviewed) |
| 7. Design Software: Principles and Tools | Draft 2 (reviewed) |
| 8. Designing Tooth-Supported Restorations | Draft 2 (reviewed) |
| 9. Designing Implant Restorations | Draft 2 (reviewed) |
| 10–20 | Draft 2 (reviewed; review notes: `chapters/NN-*.notes.md`; status in `PROGRESS.md`) |
