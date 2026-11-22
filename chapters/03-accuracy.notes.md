# Review Notes — Chapter 3. Accuracy in Digital Dentistry: Concepts and Measurement

## Summary
- Word count: ~3,610 (body, excluding references).
- References: 31 (checked on PubMed: title, authors, journal, DOI/PMID and abstract).
- UNVERIFIED items: 2 (listed below; marked inline as **[UNVERIFIED]** in the chapter at the author's request).
- Notes written after the chapter was drafted, from the review comments given in chat at the time.

## References to check
- **Ref 1 (ISO 5725-1:1994):** the standard has since been revised. Confirm which edition the publisher wants, and check the ISO catalogue entry.
- **Ref 2 (ISO 12836:2015):** confirm the current edition in the ISO catalogue.
- **Refs 9, 12–15, 29 (2025–2026, J Prosthet Dent and others):** recent. Several were online-first when cited. Confirm the final volume and pages.
- **Ref 8 (Son 2022) and Ref 19 (Shin 2025):** published online one to two years earlier. Cited by print year.

## Weak evidence
- **Complete-arch scanner studies (Ender 2015/2016, Kuhr 2016, Renne 2017):** devices now obsolete. The patterns still hold, but the numbers are dated.
- **Implant scan meta-analysis (Revilla-León 2026):** high heterogeneity and significant publication bias (stated in the text).
- **Operator-experience meta-analysis (Limones 2026):** low to very low certainty (stated).
- **Cement-space studies (Zheng 2022, Elbadawy 2022, Shin 2025):** single in vitro studies of specific materials.

## Caveats / uncited statements
- **3.3.2 (best-fit alignment hides systematic distortion):** a methodological principle stated without a specific citation. Consider adding a methods paper.
- **Table 3.1 (target analogy) and the 3.8 checklist:** didactic material, uncited.
- **Table 3.4 control measures:** expert synthesis. Only some rows are tied to references.
- **"An angular error of 1° is often quoted as a limit for passive fit":** this is attributed to Pozzi 2025 [16], which uses the 1° threshold, but the threshold's original source is not given.

## Decisions made
- I defined trueness and precision formally here and used them consistently in later chapters.
- I chose the 3.8 critical-appraisal checklist as a reusable tool for the rest of the book.
- I merged a duplicate reference (Shin et al. had appeared as two entries) into one.

## UNVERIFIED items
1. **Ref 18 (McLean & von Fraunhofer 1971) — the 120 µm threshold (3.5.2):** the PubMed record has **no abstract**, so the 120 µm figure attributed to this paper could not be confirmed from the source. It is the conventionally cited value. Confirm against the full text.
2. **Refs 1–2 (ISO standards):** not verifiable on PubMed. The edition, title wording and content (e.g., the test objects described for ISO 12836) were not confirmed against the ISO catalogue.

## Figures and tables added
- **Figure 3.1** `figures/fig-03-1-trueness-precision.svg`: four targets (trueness × precision). A visual form of Table 3.1, with no data.
- **Figure 3.2** `figures/fig-03-2-alignment.svg`: the same distorted scan under best-fit vs local alignment. Illustrates the methodological point in 3.3.2. Note: that point is itself uncited (see Caveats above).
- **Figure 3.3** `figures/fig-03-3-holmes-fit.svg`: half cross-section of a crown margin labelling the internal gap, marginal gap, vertical and horizontal marginal discrepancy, and absolute marginal discrepancy, after Holmes et al. [17]. Schematic, not to scale. The crown is drawn deliberately unseated and overextended.
- A chart of complete-arch implant trueness by method was considered but not added, to keep to 3 figures per chapter.
- No new tables (the chapter already has 4).

## Update 2026-11 (trial run)
- Ref 15 (Altalla, J Prosthet Dent 135(5):e60–e70, PMID 41241558): year corrected from 2025 to 2026, to match the volume year (issue 135(5) = 2026) and the print-year convention used throughout the book. The error was found by the trial update run.

## Update 2026-11 (quarterly update 1, 2026-11-17)
Search window 2026-10-01 to 2026-11-17 (PubMed, entry date). Full report: `updates/2026-11.md`.
- **Added (Section 3.4.3, Implant scans):** Li et al. 2026, J Prosthet Dent, online ahead of print (PMID 42946612, doi:10.1016/j.prosdent.2026.09.031), new ref 17. Systematic review of 23 studies (22 in vitro, 1 clinical): plain intraoral scans (with or without scan aid) more accurate than the splinted open-tray impression for short spans, less accurate for long spans; calibrated scans appeared better in long spans (2 studies only); no studies of intraoral photogrammetry. Reason: adds a technique-category comparison with the conventional impression that the section lacked.
- **References to check:** new ref 17 is online-first (no volume or pages yet).
- **Reference numbers changed.** `tools/renum.py` renumbered the list after the new reference was added. Reference numbers in the sections above this one use the **old** numbering. Old → new: 31→17, 17→18, 18→19, 19→20, 20→21, 21→22, 22→23, 23→24, 24→25, 25→26, 26→27, 27→28, 28→29, 29→30, 30→31. Unlisted numbers are unchanged.

## Review 2026-11-22
Applied all 25 findings from `reviews/03-review.md` (author: "approve all"). Each source was re-confirmed on PubMed (abstract and metadata) before the text was changed. No new references (31, all cited).
- **#1** 3.4.2: 11.5–60.2 µm range now covers the conventional and digital methods tested; VSE materials and CEREC Bluecam had the highest trueness and precision; digital systems had higher local deviations [6].
- **#2** 3.6 lead-in: "Two studies compared measurement methods directly, with different results:".
- **#3** 3.7.1: Zheng endocrowns labelled in vitro micro-CT; 60/120 µm now described as the best agreement between designed and measured marginal gap, not the best fit.
- **#4** 3.8 item 1: unsupported "usually overestimate clinical accuracy [3,4]" removed; replaced by an uncited methodological point referring to Section 3.2.4.
- **#5** 3.3.1: "most in vivo studies" → "in vivo studies often"; study size (5 participants × 3 impressions) added [4].
- **#6** 3.3.3: [4,6] now cites only the percentile metric; outlier sentence reworded without the unsupported "edges of the scan" claim.
- **#7** 3.4.1: "narrow, deep" → "narrow, long" proximal boxes [8].
- **#8** 3.4.1: operator-experience results split into in vitro (trueness, ~2.5 µm; training ~19 µm, two studies) and clinical (scanning time; satisfaction in one trial); certainty "low to very low" [9].
- **#9** 3.4.2: in vivo study size added (five participants, three impressions per method) [4].
- **#10** 3.4.2 summary: device variation cited [11], pattern by impression method cited [4,6]; ends-of-arch/cross-arch location now labelled expert opinion.
- **#11** 3.4.3: "meta-analysis of 26 studies" → "systematic review and meta-analysis in which 26 studies assessed extraoral photogrammetry" [14].
- **#12** 3.4.3: study counts added (14 [15]; 13, 10 in vitro [16]); pooled analyses in [16] were of in vitro studies only.
- **#13** Key Points: splinting improves linear but not angular trueness [13]; photogrammetry clinically acceptable [14] and more true and precise [15,16]; [12] cited for complete-arch implant scans.
- **#14** 3.5.2: "Many modern studies" → "recent studies, for example [20]".
- **#15** 3.5.2: lead-in "ceramic and CAD/CAM restorations"; Contrepois review described as 54 studies (48 in vitro, 6 in vivo) of 17 ceramic crown systems [21].
- **#16** 3.5.2: Boitelle review now described by its stated aim only (abstract reports no findings) [22].
- **#17** Key Points: [UNVERIFIED] marker added after [19]; ref 21 cited only for ceramic restorations within the threshold; ref 23 for digital vs conventional impressions in single-unit ceramic restorations.
- **#18** 3.6: Alabdullah study labelled in vitro; acceptable limit stated as the 300 µm standard used in that study [26].
- **#19** 3.7.1: Elbadawy (in vitro micro-CT; marginal fit and absolute marginal discrepancy) [28] and Shin (in vitro) [20] labelled.
- **#20** 3.7.2 and Key Points: Sengottaiyan meta-analysis described as nine in vitro studies, mostly single crowns; Key Points now "In vitro, … within clinically acceptable limits".
- **#21** 3.7.3: De Freitas study labelled in vitro (polyurethane teeth); "axial internal gap" → "axial gap".
- **#22** Table 3.4: citations narrowed to what the sources support (Manufacture: "printing system [29]"; Post-processing: "crystallisation (lithium disilicate) [30]"); the other items are uncited expert synthesis (see Caveats).
- **#23** Figure 3.3 caption: "so that the main terms (A–E) can be drawn; seating discrepancy is not shown". The SVG is unchanged (no data or labels changed), so no re-render.
- **#24** Refs 9, 12, 14: AAFP committee subtitle added. For ref 12 the PubMed title is truncated ("…American Academy of Fixed Prosthodon."); the full committee name was taken from the identical subtitle on refs 9 and 14 (PubMed). The journal page could not be reached from this session, so confirm ref 12's wording at the proofs stage.
- **#25** Summary above: references 30 → 31.
- **Reference numbers changed.** Because Table 3.4 no longer cites [29,30] in the Manufacture row, the De Freitas paper is now cited first; `tools/renum.py` swapped two numbers. Old → new: 30→31 (Sengottaiyan 2026), 31→30 (De Freitas 2020). Unlisted numbers are unchanged. Sections above this one use the old numbering.
- Inline [UNVERIFIED] markers: 3 → 4 (the new one is the Key Points repeat of the existing ref 19 item, listed as UNVERIFIED item 1 above under its old number 18). UNVERIFIED items unchanged (2).
