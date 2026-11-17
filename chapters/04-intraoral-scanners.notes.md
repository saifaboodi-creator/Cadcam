# Review Notes — Chapter 4. Intraoral Scanners

## Summary
- Word count: ~3,459 (body, excluding references).
- References: 27 (checked on PubMed: title, authors, journal, DOI/PMID and abstract).
- UNVERIFIED items: 1 (listed below; marked inline as **[UNVERIFIED]** in the chapter at the author's request).
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
1. **Table 4.1 (optical principles), cited to Refs 1 and 4 (Richert 2017; Zimmermann 2015):** the technical descriptions of how each principle measures depth (confocal, triangulation, active wavefront sampling, stereophotogrammetry, OCT) come from general technical knowledge. The **abstracts** of the cited reviews do not detail them. Check against the full texts, or have an optics/engineering co-reviewer confirm. (Kuhr 2016's finding on powder plus active wavefront sampling **is** confirmed in its abstract.)

## Figures and tables added
- **Figure 4.1** `figures/fig-04-1-scan-strategy.svg`: precision by scanning strategy, 7.9 / 8.5 / 35.0 µm, from Müller 2016 [15] (in vitro, one scanner). The numbers are as in 4.5.2.
- **Figure 4.2** `figures/fig-04-2-retraction.svg`: marginal fit at a 1.0 mm subgingival finish line, 189 µm without retraction vs 95 µm with cord [17] (in vitro). The 120 µm "acceptability" line was deliberately **not** drawn, because that threshold is UNVERIFIED (Chapter 3).
- **Figure 4.3** `figures/fig-04-3-bite-records.svg`: occlusal-view schematic of the recommended bite-record locations from the systematic review [18]. **Interpretation to check:** the review's wording "bilateral posterior record including at least 4 teeth" is drawn as 2 teeth per side (4 in total). Confirm against the full text, as the abstract is ambiguous on whether this means per side or in total.
- No figure was drawn for the optical principles (Table 4.1), because those descriptions are UNVERIFIED.
- No new tables (the chapter already has 3).

## Update 2026-11 (quarterly update 1, 2026-11-17)
Search window 2026-10-01 to 2026-11-17 (PubMed, entry date). Full report: `updates/2026-11.md`.
- **Added (Section 4.10.1, Caries detection):** Carvalho et al. 2026, J Dent, online ahead of print (PMID 43025745, doi:10.1016/j.jdent.2026.107171), new ref 27. Systematic review and meta-analysis of 22 studies: clinical pooled sensitivity 0.61, specificity 0.94; no significant difference from conventional methods; too insensitive for screening. Reason: first meta-analysis on the question; supports the existing Evidence Box (adjunct, not replacement). Note: the review covers IOS-assisted detection in general, not only NIR.
- **References to check:** new ref 27 is online-first.
- **Reference numbers changed.** `tools/renum.py` renumbered the list after the new reference was added. Reference numbers in the sections above this one use the **old** numbering. Old → new: 28→27, 27→28. Unlisted numbers are unchanged.
