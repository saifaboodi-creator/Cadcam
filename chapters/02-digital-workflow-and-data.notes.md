# Review Notes — Chapter 2. The Digital Workflow and Data Formats

## Summary
- Word count: ~3,380 (body, excluding references).
- References: 19 (checked on PubMed: title, authors, journal, DOI/PMID and abstract).
- UNVERIFIED items: 2, marked inline (2.7.1, findings 14 and 15 of the 2026-11-22 review; listed below). Before that review there were none, because Chapters 1–9 were frozen by the author.
- Notes written after the chapter was drafted, from the review comments given in chat at the time.

## References to check
- **Ref 10 (Muçolli 2024, Georgian Med News):** a minor journal with no DOI (PMID only). It supports only the point about software compatibility, ongoing costs for maintenance and software updates, and repeat scans. Consider replacing it with a stronger source (e.g., Eggmann & Blatz 2024, J Dent Res, already verified in Chapter 4).
- **Refs 14 (Haku-Mizuhara 2026) and 17 (Joda 2026):** settled in the 2026-11-22 review: J Prosthet Dent 2026;135(1):47–53 and J Periodontal Res 2026;61(8):877–93, as cited.
- **Ref 18 (Revilla-León, J Prosthet Dent 2022;128(5)):** published online 2021. Cited by print year.

## Weak evidence
- **Virtual patient accuracy (2.8.2):** one clinical study of 10 participants (Revilla-León) and one randomised study of CBCT registration (Ntovas 2024).
- **Mesh decimation (Elbashti 2023):** CBCT-derived maxillofacial models on cadavers. Its application to restorative margins is an extrapolation, and the text says so.

## Caveats / uncited statements
- **HIPAA sentence (2.7.1):** general US legal background, uncited; now marked [UNVERIFIED] (review finding 15). Add a regulatory source (e.g., HHS) before release.
- **The "3-2-1" backup rule (2.6.2):** general IT practice, uncited.
- **Table 2.2 (file formats):** general technical knowledge, uncited.
- **2.7.2 safeguard list, 2.5 interoperability questions, 2.9 checklist:** practical guidance, uncited.

## Decisions made
- I kept data protection in this chapter rather than in Chapter 20, because it applies from the first scan.
- I introduced the virtual patient here. Chapter 6 develops it further.

## UNVERIFIED items
1. **2.7.1, GDPR special categories:** "under the Regulation, biometric and health data are special categories with stricter processing rules [UNVERIFIED]". Not in the abstract of ref 11; needs a primary legal source (GDPR Article 9).
2. **2.7.1, HIPAA:** "the HIPAA Privacy and Security Rules govern health information held by dental practices and by their business associates, which can include cloud providers [UNVERIFIED]". Uncited; needs a regulatory source (e.g., HHS).

## Figures and tables added
- **Figure 2.1** `figures/fig-02-1-workflow-lanes.svg`: physical vs digital steps in analogue, hybrid and fully digital workflows. Schematic of Section 2.1 and Table 2.1.
- **Figure 2.2** `figures/fig-02-2-data-structures.svg`: point cloud → triangle mesh → voxel volume. Schematic of Section 2.3.
- **Figure 2.3** `figures/fig-02-3-virtual-patient-accuracy.svg`: datasets registered into the virtual patient, with an error scale (scanner error in tens of µm vs registration trueness 0.50–1.64 mm [18]). The landmark wording follows [13] (teeth); scan bodies and markers come from the uncited text in 2.8.3. "Tens of µm" for scanner error is illustrative, drawn from Chapters 3–4.
- **Table 2.3** (new): datasets that make up the virtual patient (data type, format, what each adds). It organises the 2.8.1 content and cites [13,14] as the text does.

## Review 2026-11-22
Applied all 26 findings from `reviews/02-review.md` (author: "approve all"). Each source was re-confirmed on PubMed (abstract and metadata) before the text was changed. No new references; reference numbering unchanged (19 refs, all cited).
- **#1** 2.2.2: cost result now gives direct treatment costs (1815 vs 2120 CHF), lower laboratory costs, the 18% as the cost-minimisation result, and the different abutments and crowns in each arm [5].
- **#2** 2.1 Clinical Tip: "well supported" replaced with "randomised evidence for the complete digital workflow is still scarce [1]".
- **#3** Key Points: mesh point replaced; export resolution [8], mesh reduction beyond 50% on CBCT-derived models [9], filled holes are estimates (no citation).
- **#4** 2.2.2: complete-arch trial now gives 10 patients, three scanners (two needed powder) and significance for two scanners [6].
- **#5** 2.1: "no long-term follow-up" → "no follow-up".
- **#6** 2.1: "larger marginal gaps (mean …)" → "lower marginal precision (113.8 µm)".
- **#7** 2.2.1: one patient, 10 full-arch scans; the authors "suggested" saliva and limited space contribute [3].
- **#8** 2.3.2: mesh-resolution study labelled in vitro (typodonts) [8].
- **#9** 2.3.2: decimation study models "from cadaver heads"; "measurable" removed [9].
- **#10** 2.3.3: CBCT surface "usually less true to the tooth surface … (expert opinion; see Chapter 6)".
- **#11** 2.5: "licence costs" → "ongoing costs for maintenance and software updates" [10].
- **#12** 2.6.2: only the computer virus is cited to [7]; hardware failure, deletion and ransomware are uncited general statements.
- **#13** 2.6.2: intraoral scans and plaster models are medical records [11]; design files treated the same way as advice.
- **#14** 2.7.1: biometric data must be processed in line with GDPR [11]; special-categories clause marked **[UNVERIFIED]**.
- **#15** 2.7.1: HIPAA sentence reworded ("can include cloud providers"; laboratories removed) and marked **[UNVERIFIED]**.
- **#16** 2.7.2: "ISO 27001 or the NIST frameworks" → "ISO or NIST standards" [11].
- **#17** 2.7.3: exact quotation: "individual privacy, rights and autonomy need to be put "front and center"" [12].
- **#18** 2.8.1: "(online in 2014)" added, so the year agrees with ref 13 (print 2015).
- **#19** 2.8.1 and Table 2.3: "at rest and smiling" removed; Table 2.3 now "Facial surface and expression [13]".
- **#20** 2.8.1: "case reports" → "a clinical report" [16].
- **#21** 2.8.2: observational clinical study of 10 participants; "two scan-body systems" [18].
- **#22** 2.8.3: "metal restorations" → "multiple restorations"; landmark bullet now "Free-ended edentulous areas; … absolute number of missing teeth had no effect" [19].
- **#23** Key Points: crossover studies of 20 patients each; single implant impressions and single implant crowns [4,5].
- **#24** 2.2.2: summary paragraph now says the evidence rests on small studies; "clearly", short spans and operator experience removed [4–6].
- **#25** 2.9 item 1: [2] supports only the complete-arch limit; deep margins and multiple implants pointed to Chapters 4 and 17.
- **#26** Figure 2.1 caption: hybrid impression box explained (grey = elastomeric; intraoral scan would be digital). SVG unchanged, so no re-render was needed.
- Inline UNVERIFIED count: 0 → 2 (both in 2.7.1).
