# Review Notes — Chapter 4. Intraoral Scanners

## Summary
- Word count: ~3,459 (body, excluding references).
- References: 28 (27 at Draft 1; ref 27, Carvalho 2026, added in update 2026-11). Checked on PubMed: title, authors, journal, DOI/PMID and abstract.
- UNVERIFIED items: 2 (listed below; 3 inline **[UNVERIFIED]** marks in the chapter: Table 4.1 lead-in, the first Key Point and the Figure 4.3 caption). Updated at review 2026-11-22.
- Notes written after the chapter was drafted, from the review comments given in chat at the time.

## References to check
- **Ref 25 (Bittar 2026, BMC Oral Health 26(1)):** no article number yet. Cited by DOI.
- **Ref 17 (Son 2025, J Funct Biomater 16(9):309):** the article number is taken from the publisher identifier. Confirm it.
- **Ref 22 (Limones 2026):** recent. Confirm the final pages.
- **Ref 4 (Zimmermann 2015, Int J Comput Dent):** PMID only, no DOI.

## Weak evidence
- **Subgingival margin studies (An 2024; Son 2025):** in vitro.
- **Scanning strategy (Müller 2016; Medina-Sotomayor 2018):** in vitro, on specific (now older) devices.
- **NIR caries detection (Metzger 2022; Kanar 2024; Bittar 2026):** reference standards are bitewings or clinical examination, and the false-positive risk is noted in an Evidence Box.
- **Operator experience (Limones 2026):** low certainty.

## Caveats / uncited statements
- **"Turn the operating light away…" Clinical Tip:** extrapolated from in vitro lighting studies [11,12].
- **4.5.4 single-crown scan sequence and 4.6 Clinical Tip (scan immediately after cord removal):** practical guidance, uncited.
- **4.11 infection control steps:** general practice. Only the tip-reprocessing point is tied to Barenghi 2019.
- Brand names appear only in reference titles.

## Decisions made
- I presented scanners as diagnostic platforms (4.10) as well as impression devices, following Eggmann & Blatz 2024.
- I added a summary table of indications (Table 4.3) with three evidence levels.

## UNVERIFIED items
1. **Table 4.1 (optical principles), cited to Refs 1 and 4 (Richert 2017; Zimmermann 2015):** the technical descriptions of how each principle measures depth (confocal, triangulation, active wavefront sampling, stereophotogrammetry, OCT) come from general technical knowledge. The **abstracts** of the cited reviews do not detail them. Check against the full texts, or have an optics/engineering co-reviewer confirm. (Kuhr 2016's finding on powder plus active wavefront sampling **is** confirmed in its abstract.) Since review 2026-11-22 the first Key Point, which refers to Table 4.1 with the same citations, carries the same mark.
2. **Figure 4.3 and 4.7.2, bite-record tooth counts (Ref 18, Revilla-León 2023):** the abstract says "a bilateral and frontal record including 2 teeth" and "a bilateral posterior occlusal record including at least 4-teeth" without saying whether the counts apply per record or in total. The text now quotes the abstract wording; the figure draws one reading (2 teeth per record in option 1; 2 per side in option 2) and its caption is marked **[UNVERIFIED]**. The full text is not in PMC; check it.

## Figures and tables added
- **Figure 4.1** `figures/fig-04-1-scan-strategy.svg`: precision by scanning strategy, 7.9 / 8.5 / 35.0 µm, from Müller 2016 [15] (in vitro, one scanner). The numbers are as in 4.5.2.
- **Figure 4.2** `figures/fig-04-2-retraction.svg`: marginal fit at a 1.0 mm subgingival finish line, 189 µm without retraction vs 95 µm with cord [17] (in vitro). The 120 µm "acceptability" line was deliberately **not** drawn, because that threshold is UNVERIFIED (Chapter 3).
- **Figure 4.3** `figures/fig-04-3-bite-records.svg`: occlusal-view schematic of the recommended bite-record locations from the systematic review [18]. **Interpretation to check:** the review's wording "bilateral posterior record including at least 4 teeth" is drawn as 2 teeth per side (4 in total). Option 1, "bilateral and frontal record including 2 teeth", is drawn as 2 teeth in each of the three records (label changed from "2 teeth each" to "including 2 teeth" at review 2026-11-22). Confirm against the full text, as the abstract is ambiguous on whether this means per side or in total.
- No figure was drawn for the optical principles (Table 4.1), because those descriptions are UNVERIFIED.
- No new tables (the chapter already has 3).

## Update 2026-11 (quarterly update 1, 2026-11-17)
Search window 2026-10-01 to 2026-11-17 (PubMed, entry date). Full report: `updates/2026-11.md`.
- **Added (Section 4.10.1, Caries detection):** Carvalho et al. 2026, J Dent, online ahead of print (PMID 43025745, doi:10.1016/j.jdent.2026.107171), new ref 27. Systematic review and meta-analysis of 22 studies: clinical pooled sensitivity 0.61, specificity 0.94; no significant difference from conventional methods; too insensitive for screening. Reason: first meta-analysis on the question; supports the existing Evidence Box (adjunct, not replacement). Note: the review covers IOS-assisted detection in general, not only NIR.
- **References to check:** new ref 27 is online-first.
- **Reference numbers changed.** `tools/renum.py` renumbered the list after the new reference was added. Reference numbers in the sections above this one use the **old** numbering. Old → new: 28→27, 27→28. Unlisted numbers are unchanged.

## Review 2026-11-22
Applied all 26 findings from `reviews/04-review.md` (author: "approve all"). Each source was re-confirmed on PubMed (abstract and metadata) before the text was changed. No references added or removed (28, all cited). Numbers below use the **new** numbering.
- **Reference numbers changed.** Moving the Yuzbasioglu bullet (finding 1) changed the order of first citation. Old → new: 20→21, 21→20. Unlisted numbers are unchanged.
- **#1** 4.8: Yuzbasioglu (now [21]) moved out of the short-span list; last paragraph rewritten: complete-arch evidence is mixed (Sailer RCT, three scanners, two needing powder, conventional faster and preferred by clinicians [7]; 24 participants, polyether then powder-free scan two weeks later, digital more comfortable and more time-efficient [21]). Key Point now "more comfortable… faster for short spans [19,20]; for complete arches the evidence on time is mixed [7,21]". Review Question 6(b) still answerable from the new paragraph.
- **#2** 4.4.1 Clinical Tip: added that it is practical advice extrapolated from in vitro studies [11,12] and that the effect of the operating light varied between scanners [12]. Key Point rewritten (no darkness [12]; 500 lux and 3,900 K best, 2,500 lux lengthened scanning time [11]).
- **#3** 4.10.1 Evidence Box: "high sensitivity" removed; now cites more than twice as many lesions flagged as with bitewings [23] (549 vs 223) and pooled clinical sensitivity 0.61 [27].
- **#4** Table 4.3 complete-arch row: "varies by device [9]; a 2018 systematic review still recommended conventional impressions [28]".
- **#5** First Key Point: principles now referred to Table 4.1 and marked **[UNVERIFIED]**; "thousands" removed.
- **#6** Key Point on strategy: improved precision for one scanner in vitro [15]; most scanners tolerated different strategies [16].
- **#7** 4.2.2: in vitro, comparable overall accuracy for all but one of seven scanners [6]. Key Point: complete-arch accuracy [9], finish line [6].
- **#8** Table 4.2: "in some scanners colour helps identify the margin [6]".
- **#9** 4.6: Son 2025 labelled in vitro, one scanner, 3D-printed interim crowns [17].
- **#10** 4.5.2: both strategy studies labelled in vitro; Müller: one scanner, five scans per strategy on one model [15].
- **#11** 4.4.1 and 4.4.3: Revilla-León 2020 and Son 2022 labelled in vitro (Son: one scanner).
- **#12** 4.9 and Key Point: training "associated with" better trueness (in vitro, about 19 µm), no change in precision, shorter scanning time (clinical trials, about 76 s); greater gain in scanning time only for inexperienced operators.
- **#13** Table 4.3: row 1 "Accuracy equivalent… for crowns [28]; faster and far less discomfort for patients [19]"; row 2 "3–4 units" deleted, "Accuracy at the same level as conventional impressions [28]".
- **#14** 4.10.2: monitoring limited to tooth wear and soft-tissue dimensions [3].
- **#15** 4.6: limitation attributed to one narrative review [2] only.
- **#16** Table 4.3 orthodontics row: "Used for orthodontic planning and for monitoring tooth wear and soft tissues [3]".
- **#17** 4.11: [10] dropped after "sometimes blood"; tip bullet now says the reprocessing method determines the tip's optical characteristics and long-term use [10] ("windows and mirrors" removed). Table 4.2: [10] now attached to the tip optical-characteristics point instead of "running costs" (kept [10] there so reference order did not change).
- **#18** 4.7.2: "each" deleted. Figure 4.3 label changed to "including 2 teeth" (title/desc updated); caption marks the drawn tooth counts as one reading **[UNVERIFIED]** because the full text could not be checked. Added to "UNVERIFIED items" and "Interpretation to check". Figure re-rendered and checked: labels fit, nothing clipped.
- **#19** 4.7.2: occlusal-force result attributed to the one study that assessed it.
- **#20** Ref 22: AAFP committee subtitle added.
- **#21** Ref 27: "J Dent. 2026;107171." (PubMed: 2026 Nov 13, no volume yet; add it when assigned).
- **#22** Key Point on NIR: now cites [23–27].
- **#23** Key Point: blood removed; saliva reduced trueness in vitro, especially at subgingival margins [13].
- **#24** Key Point: "Retraction is essential" replaced with the in vitro results of [17] and [13].
- **#25** 4.1: "Thousands of images" → "Many images".
- **#26** Notes Summary: reference count updated to 28; UNVERIFIED count updated (2 items, 3 inline marks).
- Inline [UNVERIFIED] marks in the chapter: 1 → 3.

