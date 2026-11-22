# Review Notes — Chapter 6. Three-Dimensional Imaging Beyond the Teeth

## Summary
- Word count: ~2,941 (body, excluding references).
- References: 21 (checked on PubMed: title, authors, journal, DOI/PMID and abstract).
- UNVERIFIED items: 0 (listed below; **not** marked inline, because Chapters 1–9 were frozen by the author).
- Notes written after the chapter was drafted, from the review comments given in chat at the time.

## References to check
- **Refs 19 (Alwabel 2025, Cureus) and 20 (Saini 2025, Digit Health):** systematic reviews in lower-tier journals. They are accurate as cited, but consider strengthening the DSD evidence (6.5.3) with a higher-impact review or an RCT.
- **Refs 9 (Martins-de-Barros 2026) and 14 (Tafuri 2026):** recent. Confirm the final details.
- **Ref 8 (Andrews 2023):** the title says "photogrammetry application", but the abstract describes an iPhone TrueDepth near-infrared depth scanner. The text describes it as a depth-sensor system. Check against the full text.

## Weak evidence
- **Jaw-motion tracking (Tafuri 2026; Farook 2023):** high risk of bias, with more than half the studies below moderate certainty (stated).
- **DSD outcomes:** heterogeneous, small samples, publication bias in the AI-DSD meta-analysis (stated).
- **Smartphone facial scanning:** single-device studies. Apps change quickly.

## Caveats / uncited statements
- **6.2.2 Clinical Tip (dose justification, smallest FOV):** follows the general ALARA principle. It is supported by Pauwels 2012 on field-of-view size, but no radiation-protection guideline is cited. Consider adding a guideline reference.
- **6.5.1 DSD workflow steps 2–6 and 6.5.4 (the mock-up is the real test):** clinical practice and expert opinion. Only steps 1 and 3 are tied to Coachman 2017.
- **Table 6.2 (which dataset drives which decision):** the author's synthesis. The accuracies come from the cited studies.

## Decisions made
- I placed DSD in this chapter (as a data-integration method), with clinical aesthetics cross-referenced to Chapter 8.

## UNVERIFIED items
None.

## Figures and tables added
- **Figure 6.1** (`figures/fig-06-1-cbct-dose-range.svg`): range bar of effective dose across 14 CBCT devices, 19–368 µSv. Data from [2] (Pauwels 2012), as already stated in 6.2.2.
- **Figure 6.2** (`figures/fig-06-2-dsd-workflow.svg`): six-step digital smile design workflow from 6.5.1, with the mock-up highlighted. Steps 1 and 3 follow [17]; the other steps are the chapter's own synthesis (as noted in the earlier caveats).
- **Figure 6.3** (`figures/fig-06-3-dataset-accuracy.svg`): log-scale range chart of the typical error of each dataset, using the values already in the old Table 6.2 (now Table 6.3): surface scans "tens of µm" (an indicative pale band, Chapters 3–5), jaw tracking 50–330 µm [13], CBCT segmentation 0.10–0.98 mm with mean RMS 0.27 mm [4], facial registration 0.5–2 mm [8,9,12]. **Caveat:** the 0.10–0.98 mm figure is the discrepancy range between segmentation methods reported by [4], plotted as the text describes it.
- **New Table 6.1:** methods for registering CBCT with surface scans (point-based, surface-based, fiducial, AI). Summarises 6.2.5. The AI row cites [6], and the surface-based row cites [4] (restoration artefacts reduced automated segmentation, as in 6.2.4). The point-based and fiducial notes restate the chapter's Clinical Tip (uncited practice guidance).
- **Renumbered:** old Table 6.1 (facial scanning technologies) → Table 6.2; old Table 6.2 (data sources) → Table 6.3, including mentions in Key Points and Review Question 8.

## Update 2026-11 (quarterly update 1, 2026-11-17)
Search window 2026-10-01 to 2026-11-17 (PubMed, entry date). Full report: `updates/2026-11.md`.
- **Added (Section 6.4.3, JMT evidence):** Farronato et al. 2026, J Dent, online ahead of print (PMID 42869410, doi:10.1016/j.jdent.2026.107107), new ref 17. Umbrella review of 34 reviews: static digital articulation conditionally accurate in dentate short-span settings; contact location more reliable than intensity/area/force; jaw tracking and 4D virtual patient feasible but sparse clinical outcomes. Also added to the closing sentence of 6.4.3. Reason: highest-level synthesis on the topic; consistent with the text.
- **References to check:** new ref 17 is online-first.
- Figure 6.3 cites refs 4, 8, 9, 12, 13: unchanged by renumbering.
- **Reference numbers changed.** `tools/renum.py` renumbered the list after the new reference was added. Reference numbers in the sections above this one use the **old** numbering. Old → new: 21→17, 17→18, 18→19, 19→20, 20→21. Unlisted numbers are unchanged.

## Review 2026-11-22
Applied all 22 findings from `reviews/06-review.md` (author: "approve all", 2026-11-22). Each source was re-confirmed on PubMed (abstract and metadata) before the text was changed. No references added or removed; `tools/renum.py` left the numbering unchanged (21 refs, all cited; no old → new map needed). No inline [UNVERIFIED] marks were needed.
- **#1** 6.2.4 and Table 6.1 (surface-based row): "restoration artefacts reduced AI performance" removed; now states that the authors called for further development of AI segmentation for teeth with restoration artefacts [4]. The earlier note under "Figures and tables added" (Table 6.1 surface-based row) is superseded.
- **#2** 6.3.3 closing paragraph and Key Points: lower-third divergence attributed to one smartphone photogrammetry app [9].
- **#3** Evidence Box: facial-scan trueness 0.9–2 mm [8,9] separated from face–intraoral superimposition trueness 0.50–1.64 mm [12]. Table 6.3 cell qualified as trueness of facial scans and of superimposition. Figure 6.3 row label now "Facial scan / face–tooth superimposition" (two lines); alt text and SVG description updated.
- **#4** 6.5.3: "DSD clearly improves communication and patient involvement" replaced with the cited, hedged result of the systematic review of seven heterogeneous studies [20].
- **#5** 6.2.2: Pauwels study labelled as phantom dosimetry.
- **#6** Figure 6.1 caption, SVG footer and Key Points: dose "strongly related to" field-of-view size (no longer "mainly"); caption says "Phantom data from [2]".
- **#7** 6.2.4: "discrepancy for the AI-driven and manual segmentation methods", SD 0.11 mm added. Figure 6.3 caption explains that the CBCT bar is the range of discrepancies for the segmentation methods [4]; SVG description updated.
- **#8** 6.2.4: "slightly"/"much" replaced with significance-based wording and the authors' judgement of comparable accuracy.
- **#9** 6.2.4: mesh reduction now specific (cadaver maxillofacial defect models; 50% no deviation, 75% minor) [5].
- **#10** Trueness terminology: 6.2.4, Key Points, Table 6.3 column heading ("Typical error (trueness where reported)").
- **#11** 6.3.3 bullet 1: 10 participants, rear-camera app lowest accuracy but high realism [7]. Key Points rewritten (small validation studies; judicious use where fine detail is needed) [7,8].
- **#12** 6.3.3 bullet 2: "advised judicious use … limited resolution and longer acquisition time" [8].
- **#13** 6.3.4 and Key Points: markers "significantly affected" accuracy (10 registrations per condition); Key Points names marker-based matching with stereophotogrammetry [11].
- **#14** 6.4.2: "electromagnetic tracking" removed; device list follows the ref 13 abstract.
- **#15** 6.4.3: "A clinical report describes a digital workflow" (singular) [15].
- **#16** 6.4.3: 34 reports broken down (29 SRs, 4 scoping reviews, 1 evidence map; 12 of 29 at high risk of bias); "more defensible than … absolute force" [17].
- **#17** Figure 6.2 step 4: "ideally registered to a facial scan"; SVG description updated.
- **#18** 6.5.2: general software gave a more comprehensive smile analysis than most dedicated DSD programs [19].
- **#19** Key Points: artefacts can interfere with diagnosis [3] and with registration [6].
- **#20** Key Points: DSD bullet hedged; ref 21 cited only for improved aesthetic parameters.
- **#21** Ref 17: "J Dent. 2026 Oct 13:107107. doi:10.1016/j.jdent.2026.107107. Epub ahead of print." Add the volume when assigned.
- **#22** Summary: reference count updated to 21.
- Figures 6.1, 6.2 and 6.3 re-rendered and checked (geometry unchanged; labels fit; nothing clipped).
- UNVERIFIED count unchanged (0 inline, 0 listed).
