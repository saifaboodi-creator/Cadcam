# Review Notes: Chapter 17, Digital Implant Dentistry

## Summary
- Word count: about 4,200 including the reference list (about 3,600 words of body text).
- References: 24. All found on PubMed, and each figure in the text was checked against the abstract and metadata.
- UNVERIFIED items: 0.
- Cross-references: Chapter 6 (CBCT and registration), Chapter 9 (restoration design, scan bodies, passive fit), Chapter 11 (guide printing), Chapters 3 and 5 (complete-arch implant data).

## References to check
- **Online ahead of print, with no volume or pages yet:**
  - Ref 13, Castro 2025 (IJOMI). PubMed lists "volume 0, pages 1–45".
  - Ref 16, Zhu 2026 (J Dent). Article number 107155 only, no volume.
  - Ref 9, Lee 2026 (Eur J Dent). No volume or pages.
- **Recent 2025–2026 papers; confirm final volume and pages:** refs 1, 3, 6, 7, 8, 15, 17, 21.
- **Publication year:** Ref 22 (Pedrinaci) appeared online in November 2024 but is in volume 27 (2025). Ref 10 (Herschdorfer) appeared online in 2020 but is in volume 125 (2021). Both are cited by volume year.
- **Weaker journals:**
  - Ref 17, Pisla (*Dentistry Journal*, MDPI): descriptive review with no meta-analysis.
  - Ref 23, Carosi (*J Biol Regul Homeost Agents*): case series in a non-dental journal.
  - Ref 20, Donker (*Case Reports in Dentistry*): three cases only.

## Weak evidence
- **Static versus dynamic guidance is not settled.** Jorba-García (ref 12) found dCAIS slightly better in angle. Castro (ref 13) found the two equivalent. Werny (ref 6) found fully guided sCAIS the most accurate. The chapter presents all three rather than picking a winner.
- **Robotics:** pooled accuracy data come mostly from single-arm studies. The edentulous meta-analysis (ref 16) had only 35 patients, and certainty was very low. There is no RCT-level comparative evidence.
- **Immediate provisionalisation:** one in vitro study (ref 19), one case series of three patients (ref 20) and one proof of concept with 12 patients and 6-month follow-up (ref 21).
- **Edentulous immediate-loading workflows:** case series only (refs 22–24). The chapter states this explicitly.
- **Novice-operator data (refs 7–9)** are in vitro or model studies.
- **Survival:** the claim that guided surgery does not improve survival rests on one systematic review (ref 14, first 5 years).

## Caveats and uncited statements
- The **"dual-scan" protocol** for edentulous arches (radiopaque markers on the denture, scanned in the mouth and alone) is standard practice but has **no citation**. Consider adding a primary source.
- The **list of error sources** in section 17.3.4 is general knowledge with no citation. The citation to Tahmaseb was removed because its abstract does not list these sources.
- The **advantages and disadvantages of dynamic navigation** in section 17.5.1 (no guide needed, view of the field, learning curve, looking at the screen) are uncited general knowledge.
- The **robot autonomy categories** (haptic, semi-autonomous, task-autonomous) come from Linn (ref 15), which reports the subgroups. The definitions themselves are general.
- The **Clinical Tips** (plan crown-down; keep a reline option; design single-tooth immediate provisionals out of occlusion) are expert opinion.
- **Table 17.2** combines pooled means from different meta-analyses with different inclusion criteria. Its caption warns readers about this.

## Decisions made
- Did not repeat CBCT registration detail (Chapter 6) or restoration and scan-body design (Chapter 9). Both are cross-referenced instead.
- Used Werny 2025 (ref 6) as the main comparative source, because it is the only meta-analysis that separates pilot-drill from fully guided sCAIS.
- Kept the 2 mm safety margin as a recommendation, because two independent meta-analyses state it (refs 11, 12).
- Included the guide-printer study (ref 10) to link to Chapter 11. It had been verified earlier in this session (PMID 32499166).
- Did not cite an AI accuracy-prediction model I found (Mino 2026, PMID 42329583). It is niche and exploratory.

## UNVERIFIED items
None.

## Figures and tables added
All figures are original SVG diagrams/charts (`figures/`), drawn to `figures/FIGURE-STYLE.md`; no new facts, numbers or references were introduced.
- **Figure 17.1** (`fig-17-1-planning-workflow.svg`, Section 17.2.1): prosthetically driven planning workflow (scans + wax-up + CBCT → registration → planning crown-first with ≥2 mm margin → static guide / navigation / robot → surgery and provisional). Caption cites [1,4]. The caption first cited [1,4,11,12], which caused renum.py to reorder references; this was reversed exactly and the caption trimmed to [1,4] so the citation order stays identity.
- **Figure 17.2** (`fig-17-2-deviation-measures.svg`, Section 17.3.2): definitional diagram of entry, apex and angular deviation (planned vs placed implant), deviations exaggerated for clarity (stated in the figure and caption).
- **Figure 17.3** (`fig-17-3-guidance-accuracy.svg`, Section 17.3.2): two-panel bar chart (separate scales, both from zero) of mean angular deviation (7.46°, 5.94°, 2.57°, 3.67°) and apex deviation (2.22, 1.43, 0.88, 1.36 mm) for freehand, pilot-drill, fully guided and dynamic placement. Data from [6] (Werny 2025, 55 studies), as already given in the text and Table 17.2.
- No new tables (chapter already had three).

## Update 2026-11 (quarterly update 1, 2026-11-17)
Search window 2026-10-01 to 2026-11-17 (PubMed, entry date). Full report: `updates/2026-11.md`.
- **Added (Section 17.3.4, after the error list):** Hijazi Muwaquet et al. 2026, J Clin Med 15(20):7935 (PMID 42941450, doi:10.3390/jcm15207935), new ref 11. 11 studies (10 in vitro, 1 RCT): sleeve-free guides lower angular (MD −0.61°) and apical (MD −0.27 mm) deviation; no difference at platform; prediction intervals crossed zero. Reason: first meta-analysis on sleeve design, a factor already listed in 17.3.4.
- **Weak evidence:** mostly in vitro; MDPI journal.
- Linn 2026 (robotic accuracy, PMID 42866607) and Zhu 2026 (robotic, edentulous) were already cited; no change.
- **Reference numbers changed.** `tools/renum.py` renumbered the list after the new reference was added. Reference numbers in the sections above this one use the **old** numbering. Old → new: 25→11, 11→12, 12→13, 13→14, 14→15, 15→16, 16→17, 17→18, 18→19, 19→20, 20→21, 21→22, 22→23, 23→24, 24→25. Unlisted numbers are unchanged.
