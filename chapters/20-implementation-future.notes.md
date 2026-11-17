# Review Notes — Chapter 20. Implementation, Economics, Education and the Future

## Summary
- About 4,200 words including references (body about 3,700).
- 27 references, all found on PubMed and checked against their abstracts or metadata. 14 are reused from Chapters 1–9 and 16.
- **UNVERIFIED items: 2.** Both are regulatory or legal statements in Section 20.6 (listed below).
- Citation order was checked with `tools/renum.py`; it was already in order of first appearance.

## References to check
- **Recent or online-first, missing details:**
  - Ref 14, Corvalan-Diaz 2026, *Eur J Dent Educ*: no volume or pages yet; cited by DOI only.
  - Ref 24, Bijoch 2026, *BMC Oral Health*: no article number yet.
- **2026 papers whose final pagination should be confirmed:** refs 9, 11, 15, 16, 17, 19, 21, 22, 23, 25, 26, 27.
- **Ref 4 (Bessadet):** published online in 2024 and cited with the print year 2025, vol 133(1). This follows the convention used in the earlier chapters.
- **Ref 23 (Rosenblatt 2026, *Br Dent J*):** the title says "complete denture", but the abstract describes **removable partial denture** fabrication. The chapter follows the abstract. Check the full text and correct the wording if needed.
- **Ref 17 (Tousidonis 2026, *Medicina*):** article number 234 was taken from the `pii` (medicina62010234). Confirm it.

## Weak evidence
- **Economics (20.3):** there is no cost-effectiveness study for tooth-supported fixed prostheses [4]. The only cost data are from implant crowns [5] and one in vitro chairside comparison [7]. The return-on-investment framework in 20.3.2 is my structure, not taken from a study.
- **Education (20.5):** the student studies are small and rely on self-report (refs 12 and 13; ref 13 had 8 students). The VR and haptic evidence comes from reviews with variable methodological quality (14–16). Refs 15 and 16 are in *Frontiers in Oral Health*.
- **Sustainability (20.7.3):** there is one life cycle assessment for one indication [23], plus a scoping review [24] that warns against generalising. Ref 25 is a student survey of opinions.
- **Teledentistry (20.7.4):** one review is mostly of cross-sectional studies [26]. The other is limited to Saudi Arabia and to provider perceptions [27].
- **Clinic–laboratory communication (20.4):** the only study is in an educational setting [11].

## Caveats and uncited statements
- **20.6.1:** the description of custom-made devices, EU MDR and FDA is general knowledge, marked UNVERIFIED. No device classes or regulation articles are named on purpose.
- **20.6.3:** the statement that the prescribing clinician remains legally responsible is a general principle, marked UNVERIFIED. Only the AI-oversight point is cited [18].
- **20.4.1:** the list of contents for a digital prescription is expert opinion. Only the benefit of mandatory fields is cited [11].
- **Table 20.1 and Table 20.3** (buyer's checklist and staged curriculum; the curriculum table was renumbered from 20.2 when the ROI worksheet was added) are synthesised from the book's earlier chapters and are not taken from a single source.
- **The three Clinical Tips and the Lab Note** (trial period, break-even calculation, remake log) are practical advice with no citation.
- **20.7.1:** the forecast of AI moving from design assistance to decision support is my own projection, not cited.
- **The sustainability suggestions** in 20.7.3 are practical inferences. Only "choose local laboratories" is directly supported [23].

## Decisions made
- Chairside economics is left to Chapter 16 and only cross-referenced. Chapter 20 deals with general and laboratory economics.
- Regulation is described by principle only (EU MDR, FDA, ISO 13485 via a real example) to avoid stating unverified legal detail.
- The concluding section (20.8) is framed as "seven principles" that summarise the whole book and point back to its chapters.
- Section 20.2.3 (institutional adoption) was added because the evidence on slow integration into large institutions [3] matters to the student and university part of the readership.
- I left out an "AI regulation" sub-section because no verified source was available. AI is covered under the future (20.7.1) and liability (20.6.3).

## UNVERIFIED items
1. **20.6.1:** specific regulatory classifications and obligations under EU MDR and FDA for each device type, and for in-house (chairside or hospital) manufacture. Marked **[UNVERIFIED — regulatory specifics not confirmed against primary legal texts]**.
2. **20.6.3:** legal specifics of liability, and contractual allocation of responsibility between clinics, laboratories and software providers. Marked **[UNVERIFIED — general principle; legal specifics vary by jurisdiction]**.

## Figures and tables added
All figures are original SVG diagrams/charts (`figures/`), drawn to `figures/FIGURE-STYLE.md`; no new facts, numbers or references were introduced.
- **Figure 20.1** (`fig-20-1-system-selection.svg`, end of Section 20.2.2): decision path for choosing a system (indications → independent evidence → total cost → break-even units per month → in-house manufacture or scanning only → trial period). Drawn from the chapter's own guidance (Sections 20.2–20.3); no citations needed.
- **Figure 20.2** (`fig-20-2-digital-twin.svg`, Section 20.7.2): the virtual patient / digital twin as an integration hub (data sources → uses), with data security and human oversight. Sources [18,20–22]; the accuracy note repeats Chapter 6.
- **New Table 20.2** (Section 20.3.2): return-on-investment worksheet built from the cost and benefit items already listed in the text, with the existing citations [4–6,8,9].
- **Renumbered:** the former Table 20.2 (curriculum) is now **Table 20.3**; the notes line above was updated.
- Decision: did **not** chart the life cycle assessment figures from [23], because the chapter does not state what the paired values (65.22/78.63 and 77.29/94.67 kg CO₂) correspond to; labelling them would have required information not in the text.

## Update 2026-11 (quarterly update 1, 2026-11-17)
Search window 2026-10-01 to 2026-11-17 (PubMed, entry date). Full report: `updates/2026-11.md`.
- **Added (Section 20.5.1):** Wu et al. 2026, J Dent Educ, online ahead of print (PMID 43002539, doi:10.1002/jdd.70420), new ref 14. Consensus recommendations (8-member working group, unanimous) from the 2026 Reimagining Dental Education Summit: AI and technology curriculum at all levels, a dedicated leadership role, AI for institutional effectiveness, calibration, patient care and learning. Labelled as expert consensus in the text.
- **References to check:** new ref 14 is online-first. The Corvalan-Diaz online-first item above is now **ref 15**.
- **Reference numbers changed.** `tools/renum.py` renumbered the list after the new reference was added. Reference numbers in the sections above this one use the **old** numbering. Old → new: 28→14, 14→15, 15→16, 16→17, 17→18, 18→19, 19→20, 20→21, 21→22, 22→23, 23→24, 24→25, 25→26, 26→27, 27→28. Unlisted numbers are unchanged.
