# Review Notes — Chapter 2. The Digital Workflow and Data Formats

## Summary
- Word count: ~3,380 (body, excluding references).
- References: 19 (checked on PubMed: title, authors, journal, DOI/PMID and abstract).
- UNVERIFIED items: 0 (listed below; **not** marked inline, because Chapters 1–9 were frozen by the author).
- Notes written after the chapter was drafted, from the review comments given in chat at the time.

## References to check
- **Ref 10 (Muçolli 2024, Georgian Med News):** a minor journal with no DOI (PMID only). It supports only the point about software compatibility, licence costs and repeat scans. Consider replacing it with a stronger source (e.g., Eggmann & Blatz 2024, J Dent Res, already verified in Chapter 4).
- **Refs 14 (Haku-Mizuhara 2026) and 17 (Joda 2026):** recent. Confirm the final volume and pages.
- **Ref 18 (Revilla-León, J Prosthet Dent 2022;128(5)):** published online 2021. Cited by print year.

## Weak evidence
- **Virtual patient accuracy (2.8.2):** one clinical study of 10 participants (Revilla-León) and one randomised study of CBCT registration (Ntovas 2024).
- **Mesh decimation (Elbashti 2023):** CBCT-derived maxillofacial models on cadavers. Its application to restorative margins is an extrapolation, and the text says so.

## Caveats / uncited statements
- **HIPAA paragraph (2.7.1):** general US legal background, uncited. Add a regulatory source if US readers matter.
- **The "3-2-1" backup rule (2.6.2):** general IT practice, uncited.
- **Table 2.2 (file formats):** general technical knowledge, uncited.
- **2.7.2 safeguard list, 2.5 interoperability questions, 2.9 checklist:** practical guidance, uncited.

## Decisions made
- I kept data protection in this chapter rather than in Chapter 20, because it applies from the first scan.
- I introduced the virtual patient here. Chapter 6 develops it further.

## UNVERIFIED items
None.

## Figures and tables added
- **Figure 2.1** `figures/fig-02-1-workflow-lanes.svg`: physical vs digital steps in analogue, hybrid and fully digital workflows. Schematic of Section 2.1 and Table 2.1.
- **Figure 2.2** `figures/fig-02-2-data-structures.svg`: point cloud → triangle mesh → voxel volume. Schematic of Section 2.3.
- **Figure 2.3** `figures/fig-02-3-virtual-patient-accuracy.svg`: datasets registered into the virtual patient, with an error scale (scanner error in tens of µm vs registration trueness 0.50–1.64 mm [18]). The landmark wording follows [13] (teeth); scan bodies and markers come from the uncited text in 2.8.3. "Tens of µm" for scanner error is illustrative, drawn from Chapters 3–4.
- **Table 2.3** (new): datasets that make up the virtual patient (data type, format, what each adds). It organises the 2.8.1 content and cites [13,14] as the text does.
