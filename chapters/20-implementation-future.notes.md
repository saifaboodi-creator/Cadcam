# Review Notes — Chapter 20. Implementation, Economics, Education and the Future

## Summary
- About 4,200 words including references (body about 3,700).
- 28 references, all found on PubMed and checked against their abstracts or metadata. 14 are reused from Chapters 1–9 and 16.
- **UNVERIFIED items: 3.** All are regulatory or legal statements: two in Section 20.6 and one in Key Points (listed below).
- Citation order was checked with `tools/renum.py`. Reference numbers in all sections of this file use the current numbering (converted on 2026-11-22).

## References to check
- **Recent or online-first, missing details:**
  - Ref 14, Wu 2026, *J Dent Educ*: online ahead of print; no volume or pages yet.
  - Ref 15, Corvalan-Diaz 2026, *Eur J Dent Educ*: no volume or pages yet; cited by DOI only.
  - Ref 24, Bijoch 2026, *BMC Oral Health*: no article number yet.
- **2026 papers whose final pagination should be confirmed:** refs 9, 11, 16, 17, 18, 20, 22, 23, 25, 26, 27, 28.
- **Ref 4 (Bessadet):** published online in 2024 and cited with the print year 2025, vol 133(1). This follows the convention used in the earlier chapters.
- **Ref 25 (Rosenblatt 2026, *Br Dent J*):** the title says "complete denture", but the abstract describes **removable partial denture** fabrication. The chapter follows the abstract. Check the full text and correct the wording if needed.
- **Ref 18 (Tousidonis 2026, *Medicina*):** article number 234 was taken from the `pii` (medicina62010234). Confirm it.

## Weak evidence
- **Economics (20.3):** there is no cost-effectiveness study for tooth-supported fixed prostheses [4]. The only cost data are from implant crowns [5] and one in vitro chairside comparison [7]. The return-on-investment framework in 20.3.2 is my structure, not taken from a study.
- **Education (20.5):** the student studies are small and rely on self-report (refs 12 and 13; ref 13 had 8 students). The VR and haptic evidence comes from reviews with variable methodological quality (15–17). Refs 16 and 17 are in *Frontiers in Oral Health*.
- **Sustainability (20.7.3):** there is one life cycle assessment for one indication [25], plus a scoping review [24] that warns against generalising. Ref 26 is a student survey of opinions.
- **Teledentistry (20.7.4):** one review is mostly of cross-sectional studies [27]. The other is limited to Saudi Arabia and to provider perceptions [28]; the chapter text now states this limit.
- **Clinic–laboratory communication (20.4):** the only study is in an educational setting [11].

## Caveats and uncited statements
- **20.6.1:** the description of custom-made devices, EU MDR and FDA is general knowledge, marked UNVERIFIED. No device classes or regulation articles are named on purpose.
- **20.6.3:** the statement that the prescribing clinician remains legally responsible is a general principle, marked UNVERIFIED. Only the AI-oversight point is cited [19]; ref 19 lists responsibility for AI as an open question, not as settled.
- **20.4.1:** the list of contents for a digital prescription is expert opinion. Only the benefit of mandatory fields is cited [11].
- **Table 20.1 and Table 20.3** (buyer's checklist and staged curriculum; the curriculum table was renumbered from 20.2 when the ROI worksheet was added) are synthesised from the book's earlier chapters and are not taken from a single source.
- **The three Clinical Tips and the Lab Note** (trial period, break-even calculation, remake log) are practical advice with no citation.
- **20.7.1:** the forecast of AI moving from design assistance to decision support is my own projection, not cited.
- **The sustainability suggestions** in 20.7.3 are practical inferences. Only "choose local laboratories" is directly supported [25].

## Decisions made
- Chairside economics is left to Chapter 16 and only cross-referenced. Chapter 20 deals with general and laboratory economics.
- Regulation is described by principle only (EU MDR, FDA, ISO 13485 via a real example) to avoid stating unverified legal detail.
- The concluding section (20.8) is framed as "seven principles" that summarise the whole book and point back to its chapters.
- Section 20.2.3 (institutional adoption) was added because the evidence on slow integration into large institutions [3] matters to the student and university part of the readership.
- I left out an "AI regulation" sub-section because no verified source was available. AI is covered under the future (20.7.1) and liability (20.6.3).

## UNVERIFIED items
1. **20.6.1:** specific regulatory classifications and obligations under EU MDR and FDA for each device type, and for in-house (chairside or hospital) manufacture. Marked **[UNVERIFIED — regulatory specifics not confirmed against primary legal texts]**.
2. **20.6.3:** legal specifics of liability (including who is responsible for AI-assisted work), and contractual allocation of responsibility between clinics, laboratories and software providers. Marked **[UNVERIFIED — general principle; legal specifics vary by jurisdiction]**.
3. **Key Points (regulation bullet):** documentation, traceability and quality obligations of in-house manufacture. Marked **[UNVERIFIED — regulatory specifics not confirmed against primary legal texts]** (review finding 20); ref 18 is cited only as an example of an ISO 13485-certified unit.

## Figures and tables added
All figures are original SVG diagrams/charts (`figures/`), drawn to `figures/FIGURE-STYLE.md`; no new facts, numbers or references were introduced.
- **Figure 20.1** (`fig-20-1-system-selection.svg`, end of Section 20.2.2): decision path for choosing a system (indications → independent evidence → total cost → break-even units per month → in-house manufacture or scanning only → trial period). Drawn from the chapter's own guidance (Sections 20.2–20.3); no citations needed.
- **Figure 20.2** (`fig-20-2-digital-twin.svg`, Section 20.7.2): the virtual patient / digital twin as an integration hub (data sources → uses), with data security and human oversight. Sources [19,21–23]; the accuracy note repeats Chapter 6.
- **New Table 20.2** (Section 20.3.2): return-on-investment worksheet built from the cost and benefit items already listed in the text, with the existing citations [4–6,8,9].
- **Renumbered:** the former Table 20.2 (curriculum) is now **Table 20.3**; the notes line above was updated.
- Decision: did **not** chart the life cycle assessment figures from [25]. The abstract pairs the values by laboratory (local 65.22 vs 77.29; global 78.63 vs 94.67 kg CO₂), and the text now states this pairing (review finding 17).

## Update 2026-11 (quarterly update 1, 2026-11-17)
Search window 2026-10-01 to 2026-11-17 (PubMed, entry date). Full report: `updates/2026-11.md`.
- **Added (Section 20.5.1):** Wu et al. 2026, J Dent Educ, online ahead of print (PMID 43002539, doi:10.1002/jdd.70420), new ref 14. Consensus recommendations (8-member working group, unanimous) from the 2026 Reimagining Dental Education Summit: AI and technology curriculum at all levels, a dedicated leadership role, AI for institutional effectiveness, calibration, patient care and learning. Labelled as expert consensus in the text.
- **References to check:** new ref 14 is online-first. The Corvalan-Diaz online-first item above is now **ref 15**.
- **Reference numbers changed.** `tools/renum.py` renumbered the list after the new reference was added. Reference numbers in the sections above were converted to the current numbering on 2026-11-22 (review finding 23). Old → new: 28→14, 14→15, 15→16, 16→17, 17→18, 18→19, 19→20, 20→21, 21→22, 22→23, 23→24, 24→25, 25→26, 26→27, 27→28. Unlisted numbers are unchanged.

## Review 2026-11-22
Applied all 23 findings from `reviews/20-review.md` (author: "approve all"). Each source was re-confirmed on PubMed (abstract and metadata) before the text was changed. No references added or removed (28 refs, all cited).
- **#1** 20.3.1: Joda 2017 review now says only three RCTs; the twofold time gain (75.3 vs 156.6 min) is from the one implant-crown trial; no recommendations could yet be given [6].
- **#2** 20.3.2 bullet and Table 20.2: "patient preference … many indications" replaced with patient comfort; one RCT of 42 patients (tooth-supported crowns/FDPs), less discomfort with digital impressions [8].
- **#3** 20.6.3: human oversight "should be expected" [19]; responsibility for AI-assisted work stated as an open question, covered by the existing UNVERIFIED general principle. Key Points reworded accordingly.
- **#4** 20.7.1: 15 non-randomised studies; single crowns generally comparable and faster to design; inlays and three-unit FDPs less acceptable; operator refinement recommended [20].
- **#5** 20.2.1: network meta-analysis scope stated as complete-arch; single units pointed to Chapters 3 and 4.
- **#6** "Accuracy" replaced with trueness and precision in 20.2.1, Table 20.1, Key Points and Figure 20.1 box 2.
- **#7** 20.3.1 and Key Points: 18% described as the cost-minimisation result; direct costs 1815 vs 2120 CHF; 20 patients; material differences between arms stated [5].
- **#8** 20.3.1 Evidence Box: savings-claims sentence labelled as expert opinion.
- **#9** 20.3.3, 20.5.4 and Table 20.2: training "associated with" better trueness (in vitro) and faster scanning; no change in precision; low certainty [9].
- **#10** Table 20.2 chair-time row: inconsistent for tooth-supported FDPs [4]; faster for implant crowns in one RCT [6].
- **#11** 20.3.3: "Narrative reviews consistently … main" replaced with "A narrative review lists … among the disadvantages" [10].
- **#12** 20.4.1 and Key Points: digital-form result limited to year-5 students and two sample cases in a dental school; communication benefit self-reported [11].
- **#13** 20.5.1: "taught effectively" replaced with "introduced early … well accepted by students".
- **#14** 20.5.2: summary sentence now "promising adjuncts" with citation [15–17].
- **#15** 20.6.1: "bridges" replaced with "fixed dental prostheses (FDPs)".
- **#16** 20.7.3 opening: cited to the scoping review (Bijoch). Renumbering swapped two references: **old 25 → new 24 (Bijoch), old 24 → new 25 (Rosenblatt)**. All other numbers unchanged.
- **#17** 20.7.3 LCA bullet: values paired by laboratory (local 65.22 vs 77.29; global 78.63 vs 94.67 kg CO₂); four modelled scenarios; causes as named by the authors; patient-travel emissions −20% [25].
- **#18** 20.7.4: "mostly asynchronous and mobile-based" replaced with "about half on tele-diagnosis and about half using asynchronous communication" [27].
- **#19** 20.7.4: barriers limited to 11 cross-sectional studies of providers in Saudi Arabia [28].
- **#20** Key Points: in-house manufacturing obligations marked [UNVERIFIED]; ref 18 cited only as an example ISO 13485 unit.
- **#21** Key Points: "will shape the next decade" replaced with "are likely to shape the field's future".
- **#22** Ref 9: title completed with the AAFP committee subtitle (from PubMed metadata).
- **#23** This file: Summary now 28 references; reference numbers in all earlier sections converted to the current numbering (including the #16 swap, so Rosenblatt = 25 and Bijoch = 24, not the 24/25 given in the review); LCA decision updated; UNVERIFIED count updated.
- Figure 20.1 (`fig-20-1-system-selection.svg`): box 2 subtitle changed to "trueness and precision for your indications, not brochures"; re-rendered and checked (fits the box, nothing clipped). Figure 20.2 unchanged (caption [19,21–23] still correct).
- UNVERIFIED count: 2 → 3 (new marker in Key Points, finding 20).
