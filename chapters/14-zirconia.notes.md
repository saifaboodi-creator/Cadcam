# Review notes — Chapter 14. Zirconia

## Summary
- Word count: ~3,840 (including references).
- References: 26. All found on PubMed; claims and numbers checked against each abstract/metadata.
- UNVERIFIED items: 0 marked inline. Uncited statements are listed below.

## References to check
- **Ref 4 (Bernauer, J Prosthodont Res 2026;70(2):173–82):** e-published 2025; confirm final volume and pages.
- **Ref 6 (Lohbauer, J Funct Biomater 2026;17(6):300):** article number inferred from PII "jfb17060300". Confirm.
- **Ref 8 (Johansson, Dent Mater 2026):** online-first, so no volume or pages yet.
- **Ref 17 (Pjetursson, Int J Prosthodont 2026;39(3):308–24):** new 2014–2024 update of the Sailer/Pjetursson reviews. Chapter 8 cites the 2015 version. Consider updating Chapter 8 to match. I didn't change it, per the instructions.
- **Ref 5 (Wang, J Mech Behav Biomed Mater):** PubMed date is Dec 2023; volume 150 is the 2024 volume. I cited it as 2024. Confirm.
- **Ref 15 (Tajti):** cited as 2024;132(5); e-published 2023.
- **Ref 19 (Ghaffari, Dent Res J 2022;19:108):** PMID only, no DOI in PubMed record.

## Weak evidence
- **Ref 20 (Shah 2024 umbrella review)** and **Ref 19 (Ghaffari 2022)** are in lower-impact journals and summarise mostly in vitro wear data.
- **Ref 22 (Ayedi 2025, J Contemp Dent Pract)** is a systematic review of in vitro bond-strength studies in a lower-tier journal. Its conclusion matches Özcan 2015 (Ref 21) and Al-Bermani (Ref 23).
- **Ref 25 (Kern & Gläser 2023)** is a long-term case report series. It's cited only for the abrasion protocol and as expert evidence of durability.
- **Ref 26 (Demir 2024)** is a single in vitro study for the cleaning-paste recommendation.
- **Ref 5** is about additively manufactured zirconia. I used it only for the general phase–strength–translucency–ageing relationship.
- There are no long-term (>10-year) clinical data on monolithic 4Y/5Y zirconia, and LTD under clinical conditions is weakly evidenced.

## Caveats / uncited statements (general textbook knowledge)
- The ~20–25% linear sintering shrinkage of pre-sintered zirconia (14.4.1) has no citation.
- The volume increase on t→m transformation is stated as "several percent" (14.2.1). The commonly cited value is ~3–5%. Not cited.
- That saliva phosphates block MDP bonding, and that phosphoric acid should not be used to clean zirconia (14.7.3), is widely taught but not cited. Ozkan Ata 2025 (Am J Dent) was found but **not used**: its abstract reports implausible bond strengths ("1768 MPa"), probably a units error.
- Table 14.2's recommendation of conventional or self-adhesive cements for retentive preparations has no citation.
- The aggressive-abrasion caution for 4Y/5Y (Clinical Tip, 14.7.4) is expert opinion. The parameters come from Kern & Gläser (50 µm, 0.25 MPa).
- Steam sterilisation and ageing (14.5.3) is a general caution, not cited.
- "LTD has not emerged as a common clinical cause of failure" (14.5.3) is an expert judgement, not directly cited.

## Decisions made
- I cross-referred to Chapters 8, 9 and 13 for survival, implant and glass-ceramic content, and repeated only zirconia-specific findings.
- Ceramic implants are excluded (out of scope). Ref 14 is used only for its chipping data on veneered versus monolithic restorations.
- Printed zirconia is left to Chapter 11 and not discussed here.
- Brand names appear only in reference titles, per STYLE.md.
- Ref 18 (S3 guideline) is reused from Chapter 9 for the statement that only 3Y-TZP is supported for implant FDPs and complete arches.

## UNVERIFIED items
None.

## Figures and tables added
- **Figure 14.1** (`figures/fig-14-1-toughening-and-ageing.svg`): grain-level schematic. (A) Transformation toughening [1]. (B) Low-temperature degradation (Section 14.5). The caption cites only [1], so the first citation of [10,11] stays in 14.5.1; that text now also points to "Figure 14.1B".
- **Figure 14.2** (`figures/fig-14-2-strength-translucency.svg`): a schematic trade-off scale (3Y → 4Y → 5Y) plus a bar chart of pooled flexural strength, mean ± SD: 4Y-PSZ 803 ± 233 MPa and 5Y-PSZ 570 ± 116 MPa [4]. No 3Y value is plotted, because none was reported in the chapter.
- **Figure 14.3** (`figures/fig-14-3-multilayer-nesting.svg`): an FDP nested in a composition-gradient blank, with connectors in the body layers. Values (up to 1,143 MPa; about 572 MPa; only one of four above 800 MPa in all layers) from [6]. The layer arrangement is schematic; the caption says it varies by product.
- No new tables (the chapter already has three).
- References unchanged (renumbering identity confirmed).

## Update 2026-11 (quarterly update 1, 2026-11-17)
Search window 2026-10-01 to 2026-11-17 (PubMed, entry date). Full report: `updates/2026-11.md`.
- **Added (Section 14.6.1, new paragraph after the Pjetursson 2026 data):** Sengottaiyan et al. 2026, Int J Dent 2026:8282494 (PMID 42965118, doi:10.1155/ijod/8282494), new ref 18: 17 clinical studies, tooth-supported veneered zirconia FPDs, survival 92% (5 y), 86% (7 y), 83% (10 y); chipping most frequent. Abbasi et al. 2026, BMC Oral Health 26(1):2182 (PMID 42983805, doi:10.1186/s12903-026-09551-5), new ref 19: 14 RCTs, veneered zirconia vs metal-ceramic, chipping RR 0.59 (95% CI 0.48–0.72), survival RR 1.03 (1.00–1.09), low certainty.
- **Conflict stated in text:** ref 19 found less chipping for veneered zirconia than metal-ceramic, which partly conflicts with the chapter's narrative that veneered zirconia is chipping-prone (refs 12–15). The text keeps both: veneered zirconia chips more than monolithic restorations (ref 17), but whether it chips more than metal-ceramic is "not settled". **Author review requested.**
- **Weak evidence:** ref 18 is in a lower-tier journal and mixes RCTs and observational studies; ref 19 reports small-study effects and high heterogeneity.
- **Reference numbers changed.** `tools/renum.py` renumbered the list after the new reference was added. Reference numbers in the sections above this one use the **old** numbering. Old → new: 27→18, 28→19, 18→20, 19→21, 20→22, 21→23, 22→24, 23→25, 24→26, 25→27, 26→28. Unlisted numbers are unchanged.
