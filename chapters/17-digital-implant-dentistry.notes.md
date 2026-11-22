# Review Notes: Chapter 17, Digital Implant Dentistry

## Summary
- Word count: about 4,200 including the reference list (about 3,600 words of body text).
- References: 25 (24 + Hijazi Muwaquet 2026 added in quarterly update 1). All found on PubMed, and each figure in the text was checked against the abstract and metadata.
- UNVERIFIED items: 0.
- Cross-references: Chapter 6 (CBCT and registration), Chapter 9 (restoration design, scan bodies, passive fit), Chapter 11 (guide printing), Chapters 3 and 5 (complete-arch implant data).

## References to check
- **Online ahead of print, with no volume or pages yet:**
  - Ref 14, Castro 2025 (IJOMI). PubMed lists "volume 0, pages 1–45".
  - Ref 17, Zhu 2026 (J Dent). Article number 107155 only, no volume.
  - Ref 9, Lee 2026 (Eur J Dent). No volume or pages.
- **Recent 2025–2026 papers; confirm final volume and pages:** refs 1, 3, 6, 7, 8, 11, 16, 18, 22.
- **Publication year:** Ref 23 (Pedrinaci) appeared online in November 2024 but is in volume 27 (2025). Ref 10 (Herschdorfer) appeared online in 2020 but is in volume 125 (2021). Both are cited by volume year.
- **Weaker journals:**
  - Ref 18, Pisla (*Dentistry Journal*, MDPI): descriptive review with no meta-analysis.
  - Ref 24, Carosi (*J Biol Regul Homeost Agents*): case series in a non-dental journal.
  - Ref 21, Donker (*Case Reports in Dentistry*): three cases only.

## Weak evidence
- **Static versus dynamic guidance is not settled.** Jorba-García (ref 13) found dCAIS slightly better in angle. Castro (ref 14) found the two equivalent. Werny (ref 6) found fully guided sCAIS the most accurate. The chapter presents all three rather than picking a winner.
- **Robotics:** pooled accuracy data come mostly from single-arm studies. The edentulous meta-analysis (ref 17) had only 35 patients, and certainty was very low. There is no RCT-level comparative evidence.
- **Immediate provisionalisation:** one in vitro study (ref 20), one case series of three patients (ref 21) and one proof of concept with 12 patients and 6-month follow-up (ref 22).
- **Edentulous immediate-loading workflows:** case series only (refs 23–25). The chapter states this explicitly.
- **Novice-operator data (refs 7–9)** are in vitro or model studies.
- **Survival:** the claim that guided surgery does not improve survival rests on one systematic review (ref 15, first 5 years).

## Caveats and uncited statements
- The **"dual-scan" protocol** for edentulous arches (radiopaque markers on the denture, scanned in the mouth and alone) is standard practice but has **no citation**; since review 2026-11-22 it is labelled "expert opinion" in the text. Consider adding a primary source.
- The **list of error sources** in section 17.3.4 is general knowledge with no citation. The citation to Tahmaseb was removed because its abstract does not list these sources.
- The **advantages and disadvantages of dynamic navigation** in section 17.5.1 (no guide needed, view of the field, learning curve, looking at the screen) are uncited general knowledge; since review 2026-11-22 they are labelled "expert opinion" in the text.
- The **robot autonomy categories** (haptic, semi-autonomous, task-autonomous) come from Linn (ref 16), which reports the subgroups. The definitions themselves are general.
- The **Clinical Tips** (plan crown-down; keep a reline option; design single-tooth immediate provisionals out of occlusion) are expert opinion.
- **Table 17.2** combines pooled means from different meta-analyses with different inclusion criteria. Its caption warns readers about this.

## Decisions made
- Did not repeat CBCT registration detail (Chapter 6) or restoration and scan-body design (Chapter 9). Both are cross-referenced instead.
- Used Werny 2025 (ref 6) as the main comparative source, because it is the only meta-analysis that separates pilot-drill from fully guided sCAIS.
- Kept the 2 mm safety margin as a recommendation, because three meta-analyses state it (refs 6, 12, 13).
- Included the guide-printer study (ref 10) to link to Chapter 11. It had been verified earlier in this session (PMID 32499166).
- Did not cite an AI accuracy-prediction model I found (Mino 2026, PMID 42329583). It is niche and exploratory.

## UNVERIFIED items
None.

## Figures and tables added
All figures are original SVG diagrams/charts (`figures/`), drawn to `figures/FIGURE-STYLE.md`; no new facts, numbers or references were introduced.
- **Figure 17.1** (`fig-17-1-planning-workflow.svg`, Section 17.2.1): prosthetically driven planning workflow (scans + wax-up + CBCT → registration → planning crown-first with ≥2 mm margin → static guide / navigation / robot → surgery and provisional). Caption cites [1,4] (since review 2026-11-22: registration [4], transfer by CAIS [1]). The caption first cited [1,4,11,12], which caused renum.py to reorder references; this was reversed exactly and the caption trimmed to [1,4] so the citation order stays identity.
- **Figure 17.2** (`fig-17-2-deviation-measures.svg`, Section 17.3.2): definitional diagram of entry, apex and angular deviation (planned vs placed implant), deviations exaggerated for clarity (stated in the figure and caption).
- **Figure 17.3** (`fig-17-3-guidance-accuracy.svg`, Section 17.3.2): two-panel bar chart (separate scales, both from zero) of mean angular deviation (7.46°, 5.94°, 2.57°, 3.67°) and apex deviation (2.22, 1.43, 0.88, 1.36 mm) for freehand, pilot-drill, fully guided and dynamic placement. Data from [6] (Werny 2025, 55 studies), as already given in the text and Table 17.2.
- No new tables (chapter already had three).

## Update 2026-11 (quarterly update 1, 2026-11-17)
Search window 2026-10-01 to 2026-11-17 (PubMed, entry date). Full report: `updates/2026-11.md`.
- **Added (Section 17.3.4, after the error list):** Hijazi Muwaquet et al. 2026, J Clin Med 15(20):7935 (PMID 42941450, doi:10.3390/jcm15207935), new ref 11. 11 studies (10 in vitro, 1 RCT): sleeve-free guides lower angular (MD −0.61°) and apical (MD −0.27 mm) deviation; no difference at platform; prediction intervals crossed zero. Reason: first meta-analysis on sleeve design, a factor already listed in 17.3.4.
- **Weak evidence:** mostly in vitro; MDPI journal.
- Linn 2026 (robotic accuracy, PMID 42866607) and Zhu 2026 (robotic, edentulous) were already cited; no change.
- **Reference numbers changed.** `tools/renum.py` renumbered the list after the new reference was added. Reference numbers in the sections above this one were converted to the current numbering on 2026-11-22 (review finding 29). Old → new: 25→11, 11→12, 12→13, 13→14, 14→15, 15→16, 16→17, 17→18, 18→19, 19→20, 20→21, 21→22, 22→23, 23→24, 24→25. Unlisted numbers are unchanged.

## Review 2026-11-22
Applied all 29 findings from `reviews/17-review.md` (author: "approve all"). Each source was re-confirmed on PubMed (abstract and metadata) before the text was changed. No new references; `tools/renum.py` gave an identity mapping (25 refs, all cited, no number changes).
- **#1** Fig 17.1 caption: registration cited to [4], transfer by CAIS to [1]. Key Points: "prosthetically driven" now cited to [21]; integration of CBCT, IOS, planning, guided surgery and CAD/CAM cited to [1].
- **#2** 17.5.3 and Key Points: 88 of 90 patients completed; no difference in the *magnitude* of pain, swelling or painkiller use, but duration of pain, speaking limitations and impact on routine activities differed [19].
- **#3** 17.6.2: unsupported "rotation is the main risk… non-indexed or round connections" removed; in vitro study on 10 typodonts stated; connection design not tested. Key Points: feasibility [21,22], rotational error [20]. Review Question 8 reworded.
- **#4** Learning objective 2: three levels of guidance (pilot-drill, partially, fully guided).
- **#5** 17.1: "lifelong" replaced by "comprehensive"; robotics described as possible.
- **#6** 17.2.1: 19–368 µSv across 14 devices (20-fold), strongly related to field size [2].
- **#7** 17.2.1: in vitro pilot study, 20 sites, partially edentulous models, fully guided; "did not significantly affect" [3].
- **#8** 17.2.2: operator experience mattered with restoration artefacts; free-ended areas affected accuracy; number of missing teeth did not [4].
- **#9** 17.3.1: meta-analysis pooled four studies (599 implants); retrospective-only analysis not significant for entry and apex [5].
- **#10** Fig 17.3 caption ends at "Data from [6]."; new body paragraph "Laboratory (model) studies… support…".
- **#11** 17.3.2 bullet 3: advantage limited to horizontal platform and apex deviation; angle and vertical similar in extraction sockets [9].
- **#12** 17.3.3: passive seating through the guide on a cast, no drilling [10].
- **#13** 17.4.3: "fully edentulous or terminal-dentition"; four of five studies single-arm [17].
- **#14** 17.4.3: 43 studies = 17 clinical, 26 in vitro; "study-level" means [18].
- **#15** Table 17.2: row renamed "sCAIS (clinical)".
- **#16** 17.4.4: three meta-analyses [6,12,13], "at least" in one; Key Points limited to static and dynamic CAIS.
- **#17** Evidence Box: survival benefit "could not be demonstrated" [15]; novice advantage from model studies [7–9]; complex cases as a recommendation [15].
- **#18** 17.5.1: practical advantages labelled expert opinion; Table 17.3 "No guide fabrication (practical point)".
- **#19** 17.5.3: patient-motivation sentence replaced by "should therefore be recommended for its predictability".
- **#20** 17.6.2: delayed placement 4 months after ridge preservation [21]; Table 17.3 row "Aesthetic site, immediate provisionalisation".
- **#21** 17.7.1 and Key Points: registration point limited to free-ended edentulous areas in partially dentate patients [4].
- **#22** 17.7.2: dual-scan protocol labelled expert opinion (no primary source added).
- **#23** Key Points and Table 17.3: novice advantage stated as from model studies [7–9]; overall ranking cited to [6].
- **#24** Table 17.3: apex 1–2 mm [6,12]; > 1 mm with navigation [13].
- **#25** Review Question 2: asks which error sources (17.3.4) might explain the difference.
- **#26** 17.3.2: definition of "accuracy" in placement studies added (mean deviation ≈ trueness, ISO 5725; precision rarely reported).
- **#27** Deviations kept in mm and degrees as in the sources (no text change). The recommended STYLE.md exception ("Implant positional deviations are given in mm and degrees, as in the source literature") is left to the lead session, which may edit STYLE.md.
- **#28** Ref 9: "(online ahead of print)" added.
- **#29** This notes file: reference count 25; earlier sections converted to current numbering; 2 mm decision now "three meta-analyses (refs 6, 12, 13)".
- Figures: no SVG data or labels changed (only the Fig 17.1 and 17.3 captions in the chapter text), so no re-render was needed.
- UNVERIFIED count unchanged (0).
