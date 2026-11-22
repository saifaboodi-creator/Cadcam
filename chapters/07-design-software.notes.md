# Review Notes — Chapter 7. Design Software: Principles and Tools

## Summary
- Word count: ~2,883 (body, excluding references).
- References: 21 (checked on PubMed: title, authors, journal, DOI/PMID and abstract).
- UNVERIFIED items: 0 (listed below; **not** marked inline, because Chapters 1–9 were frozen by the author).
- Notes written after the chapter was drafted, from the review comments given in chat at the time.

## References to check
- **Refs 2, 14, 16, 17, 18 (2025–2026):** recent AI-design papers. Confirm the final details. Ref 18 (Holiel 2026, Biomed Eng Comput Biol) is a lower-tier journal.
- **Ref 13 (Cho, J Dent 2024;141):** published online December 2023. Cited by print year.
- The AI-design section (7.8) will date quickly. Update it before publication.

## Weak evidence
- **AI crown design:** mostly in vitro and in silico, with limited prospective clinical validation and insufficient long-term follow-up (stated in the text, following Holiel 2026).
- **Biogeneric model (Mehl 2005):** based on lower first molars only.
- **Margin AI (Alsheghri 2025):** one dataset. A 100–200 µm tolerance is clinically too large (noted).

## Caveats / uncited statements
- **Clinical Tip in 7.7.3 ("design single posterior crowns… 0 to 50 µm infra-occlusion"):** common practical advice, **uncited**. Keep it as expert opinion or add a source.
- **Table 7.2 design parameters:** deliberately gives **no numbers** for thickness or connectors. The reader is pointed to Chapters 13–15 and Appendix A.
- **7.1 nine-step software structure, 7.3 Lab Note, 7.9 checklist:** practical synthesis, uncited.

## Decisions made
- I treated AI design as "a very fast first draft under human oversight", following Limpuangthip 2026 and Schwendicke 2020.
- I avoided naming commercial software except in reference titles.

## UNVERIFIED items
None.

## Figures and tables added
- **Figure 7.1** (`figures/fig-07-1-cad-workflow.svg`): the nine CAD steps of 7.1 in a serpentine flow, with margin definition highlighted. No data.
- **Figure 7.2** (`figures/fig-07-2-design-parameters.svg`): schematic crown cross-section labelling the path of insertion, minimum occlusal thickness, cement space starting above the margin, the margin line, and a blocked-out undercut giving a thicker cement layer. Not to scale; no numbers.
- **New Table 7.1:** sources of the shape proposal (library, biogeneric [3], copy, AI [4]), with the cusp-angle finding from [5] (biogeneric 67° vs natural 54°) taken from 7.4.4. The library limitation ("generic starting shape that usually needs editing") is general knowledge, uncited.
- **Renumbered:** old Table 7.1 (design parameters) → 7.2; old Table 7.2 (AI design) → 7.3.

## Update 2026-11 (quarterly update 1, 2026-11-17)
Search window 2026-10-01 to 2026-11-17 (PubMed, entry date). Full report: `updates/2026-11.md`.
- **Added (Section 7.8.3):** Husain et al. 2026, J Dent, online ahead of print (PMID 43035139, doi:10.1016/j.jdent.2026.107168), new ref 19: 28 studies, 10 pooled; design time difference −258.4 s (95% CI −543.2 to 26.4), not significant; inconclusive for morphology and fit; almost entirely in vitro. Vigroux et al. 2026, Eur J Dent, online ahead of print (PMID 42849515, doi:10.1055/s-0046-1829082), new ref 20: 9 studies of fully automated crown design; time consistently shorter; fit generally comparable; morphology mixed.
- **Conflict stated in text:** time savings were consistent in refs 17, 18 and 20 but not statistically significant in the pooled analysis of ref 19. Both shown; neither picked.
- **Changed:** Table 7.3 row 1 "faster" → "usually faster" (refs 13, 17–20); Key points AI bullet "much faster" → "usually faster ... evidence mostly in vitro" (refs 13–20).
- **Conflict of interest:** one author of ref 19 declared an honorarium from an AI design software company (stated in the PubMed record).
- **References to check:** new refs 19 and 20 are online-first.
- **Reference numbers changed.** `tools/renum.py` renumbered the list after the new reference was added. Reference numbers in the sections above this one use the **old** numbering. Old → new: 20→19, 21→20, 19→21. Unlisted numbers are unchanged.

## Review 2026-11-22
Applied all 22 findings from `reviews/07-review.md` (author: "approve all"). Each source was re-confirmed on PubMed (abstract and metadata) before the text was changed. No new references; reference numbering unchanged (21 refs, all cited). Inline [UNVERIFIED]: 0.
- **#1** 7.7.1: ref 10 now cited for the factors it lists (scanner, scan extension, edentulous areas, occlusal records, occlusal force, tooth mobility, alignment method); the bite-scan penetration sentence is marked expert opinion (Chapter 4).
- **#2** 7.7.3: RCT described (42 patients); added that it compared impression techniques, not occlusal design methods, so it supports on-screen occlusal design only indirectly. Heading kept.
- **#3** 7.8.1: ref 14 labelled in vitro (typodonts); better FDI clinical quality, particularly posterior; larger surface deviations; poorer diastema result attributed to the deep-learning program only.
- **#4** Table 7.3 implant row: "Comparable morphology [15–17]; proximal contacts similar in one study [15] but less accurate in another [16]".
- **#5** 7.2.1 "tens of micrometres" and 7.2.2 "100–200 µm is too large" marked as expert opinion / "in our view"; 7.7.3 box retitled "Clinical Tip (expert opinion)".
- **#6** 7.2.2: model trained on 1,035 scans (1,113 in the whole dataset).
- **#7** In vitro / in silico labels added for refs 1 (seven IOS), 5 (12 test cases, mandibular second premolars, in silico FE) and 13 (30 scans of prepared posterior teeth).
- **#8** Table 7.1 biogeneric row: [3] now cited for the statistical model only; fitting to tooth, neighbours and antagonists left uncited.
- **#9** "multi-unit FDPs" → "three-unit FDPs" in Table 7.1, Table 7.3 and Key Points.
- **#10** Figure 7.2: "Restoration" leader end moved from x = 592 to 582 (inside the restoration). Re-rendered and checked: labels fit, nothing clipped.
- **#11** Table 7.2 cement-space row: "Material- and machine-specific [6,7]; the actual gap often differs from the set value [6,8]".
- **#12** 7.6.1: ref 6 labelled in vitro, CAD/CAM endocrowns, ceramic vs resin composite materials; ref 7 labelled in vitro; ref 8 "almost matched", clinical study of CAD/CAM measurement copings.
- **#13** 7.7.1: "accuracy depends entirely" → "quality depends largely on the bite record and on how the arch scans are aligned [10]".
- **#14** 7.7.2: virtual articulator described as an additional diagnostic and treatment-planning tool to the mechanical articulator [11]; "valuable" removed.
- **#15** 7.8.2: ref 15 on 20 resin casts; "significantly more efficiently"; occlusal contacts differed; refinement reduced contour deviations and may improve the emergence profile angle (authors' suggestion).
- **#16** 7.8.2: ref 16 labelled proof-of-concept (291 training, 20 validation cases); "more natural" replaced with concave profiles similar to the technician's.
- **#17** 7.8.3 and "Weak evidence" above: "no long-term data" → "insufficient long-term follow-up".
- **#18** Table 7.3 row 1: "Comparable to technician [13,17–20]; usually faster [17,18,20], though not significantly in one meta-analysis [19]".
- **#19** 7.8.4: [21] now supports continuous human oversight only; professional responsibility marked expert opinion.
- **#20** Key Points: "All" → "Most" dental CAD software.
- **#21** Key Points: colour and geometry check [1], verify automated margins [2]; "never design on an unclear margin" left uncited.
- **#22** Summary reference count 19 → 21; caveat now refers to Table 7.2.

