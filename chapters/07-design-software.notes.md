# Review Notes — Chapter 7. Design Software: Principles and Tools

## Summary
- Word count: ~2,883 (body, excluding references).
- References: 19 (checked on PubMed: title, authors, journal, DOI/PMID and abstract).
- UNVERIFIED items: 0 (listed below; **not** marked inline, because Chapters 1–9 were frozen by the author).
- Notes written after the chapter was drafted, from the review comments given in chat at the time.

## References to check
- **Refs 2, 14, 16, 17, 18 (2025–2026):** recent AI-design papers. Confirm the final details. Ref 18 (Holiel 2026, Biomed Eng Comput Biol) is a lower-tier journal.
- **Ref 13 (Cho, J Dent 2024;141):** published online December 2023. Cited by print year.
- The AI-design section (7.8) will date quickly. Update it before publication.

## Weak evidence
- **AI crown design:** mostly in vitro and in silico, with limited clinical validation and no long-term data (stated in the text, following Holiel 2026).
- **Biogeneric model (Mehl 2005):** based on lower first molars only.
- **Margin AI (Alsheghri 2025):** one dataset. A 100–200 µm tolerance is clinically too large (noted).

## Caveats / uncited statements
- **Clinical Tip in 7.7.3 ("design single posterior crowns… 0 to 50 µm infra-occlusion"):** common practical advice, **uncited**. Keep it as expert opinion or add a source.
- **Table 7.1 design parameters:** deliberately gives **no numbers** for thickness or connectors. The reader is pointed to Chapters 13–15 and Appendix A.
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
