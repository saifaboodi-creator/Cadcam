# Review Notes — Chapter 18. Removable Prosthodontics

## Summary
- Word count: about 4,100 including references (body about 3,500).
- References: 27, all found on PubMed and checked against their abstracts. Two are reused from earlier chapters: Alabdullah 2022 (Ch 3/11) and Smets 2026 (Ch 11).
- UNVERIFIED: 0.
- Citation order fixed with `tools/renum.py` (it was already in order).

> Reference numbers in the sections from "References to check" to "Figures and tables added" use the pre-update numbering; see the old → new map under "Update 2026-11".

## References to check
- **Ref 5, Prott 2026 (J Esthet Restor Dent):** online-first. No volume or pages in PubMed yet. It is also cited in Ch 11.
- **Ref 4, Dos Santos 2026 (BMC Oral Health 26(1)):** no article number yet.
- **Several papers are 2026 or carry 2026 volume numbers:** refs 6, 9, 10, 12, 14, 16 and 24. Their year is given as the print volume year where PubMed showed a later volume than the epub date (e.g. Fouda: epub 2024, J Prosthodont 35(5), 2026; Korkes: epub 2024, 35(6), 2026; Alqutaibi: epub 2025, J Prosthodont Res 70(2)). Confirm the final citation format.
- **Ref 2, Thu (J Prosthet Dent 2024;132(5)):** epub 2023, cited with the 2024 print year.
- **Ref 19, Chia (J Prosthet Dent 2024;131(1)):** epub 2022, cited with the 2024 print year.
- **Ref 11, Yunizar 2022 (Int J Comput Dent):** no DOI. Cited by PMID.

## Weak evidence
- **Complete dentures:** the systematic reviews conflict on retention. Prott (25 RCTs) found a small advantage for printed over milled. Sivaswamy and Avelino found conventional better than printed. Zandinejad (6 studies) and Srinivasan found CAD/CAM better than conventional. Certainty is mostly very low (Prott). The chapter presents this as conflicting evidence.
- **Ref 4, Dos Santos 2026:** in vitro studies only (flexural strength).
- **RPD frameworks:** most data are in vitro on single casts with n = 5–10 per group (refs 14–17). There is only one RCT (ref 19) and one 2-year RCT on PEEK (ref 20). Alqutaibi (ref 12) rated a moderate risk of bias in many included studies.
- **Ref 13, Ahmed 2021 (Biomed Res Int):** a mid-tier journal.
- **Maxillofacial:** case reports and technique papers only (refs 3, 21–24), one cadaver study (ref 25), and a systematic review covering only 23 patients (ref 26). The chapter states this in an Evidence Box.

## Caveats / uncited statements
- Section 18.1, on mobile tissue, few landmarks and the difficulty of jaw relations, is general prosthodontic knowledge. It cross-refers to Ch 4.
- Table 18.1 (manufacturing routes) describes common commercial workflows generically. Its notes on the tooth–base bond and the wear resistance of printed teeth are general statements; the wear point cross-refers to Ch 11. Only the disc-size limitation is cited (ref 3).
- Section 18.2.2 (the design steps) and Section 18.4.1 (the RPD design steps) are standard procedural descriptions without citations.
- The PEEK statement that "long-term data on clasp retention, wear and durability are still limited" is an author judgement.
- Section 18.5.1, on why digital workflows help maxillofacial patients (trismus, fragile tissue), is general reasoning without a direct citation.

## Decisions made
- To avoid repeating Chapter 11, I cross-referred to it for printed resin orientation, post-curing and biocompatibility. Prott, Sivaswamy and Smets are summarised here at clinical-decision depth only.
- Retention findings are reported as conflicting, not resolved. The clinical recommendations follow Thu 2024: border-moulded impressions and a trial denture.
- I recommended milled PMMA for definitive bases where strength and colour stability matter, based on in vitro and meta-analytic material data (refs 1, 4) and the Prott aesthetics and complications finding. This is framed as a preference, not proven clinical superiority.
- I excluded Awinashe 2026 (Ann Afr Med, single author, unclear methods) and El-Asfahani 2026 (an in vitro wear study) as weak or peripheral.
- I didn't find a systematic review of digital extraoral facial prostheses beyond nasal prostheses. Tanveer 2021 is used and its narrow scope is stated.
- The chapter runs slightly above the target length: about 3,500 words of body text, against the 3,000–3,800 target.

## UNVERIFIED items
None.

## Figures and tables added
All figures are original SVG diagrams/charts (`figures/`), drawn to `figures/FIGURE-STYLE.md`; no new facts, numbers or references were introduced.
- **Figure 18.1** (`fig-18-1-digital-denture-workflow.svg`, Section 18.2.1): digital complete denture workflow (records → design → printed trial denture with feedback → milled / printed / conventionally processed → insertion; stored design for remakes). Sources [1,2].
- **Figure 18.2** (`fig-18-2-rpd-framework-workflow.svg`, Section 18.4.1): digital RPD framework design steps (survey, blockout/relief, components, thickness) and the three manufacturing routes of 18.4.2.
- **Figure 18.3** (`fig-18-3-rpd-framework-fit.svg`, Section 18.4.3): bar chart of mean gaps, SLM from conventional impression 79.5 µm, SLM from intraoral scan 85.3 µm, conventional casting 114.2 µm. Data from [14]; the caption and figure note it is a single in vitro study with differences of minimal clinical significance.
- **New Table 18.2** (end of Section 18.4.4): RPD framework manufacturing routes, summarising evidence already cited in 18.4 ([11,12,14–20]). The "printed pattern + casting" row states that no route-specific outcome data are summarised in the chapter (no claim invented). Placed after 18.4.4 so that no reference is cited before its first appearance in the text.
- **Renumbered:** the former Table 18.2 (summary) is now **Table 18.3**.

## Update 2026-11 (quarterly update 1, 2026-11-17)
Search window 2026-10-01 to 2026-11-17 (PubMed, entry date). Full report: `updates/2026-11.md`.
- **Added (Section 18.3.1):** Malikhao et al. 2026, J Prosthet Dent, online ahead of print (PMID 42951779, doi:10.1016/j.prosdent.2026.10.002), new ref 5. Meta-analysis of in vitro studies (10 included, 4 pooled): surface treatment raised printed tooth–base shear bond strength by MD 5.43 MPa (95% CI 2.21–8.66); airborne-particle abrasion effective; MMA alone not significant. Reason: the chapter flags the tooth–base bond as a weak point (Table 18.1) without evidence on how to treat it.
- **References to check:** new ref 5 is online-first. The Prott 2026 online-first item above is now **ref 6**.
- **Reference numbers changed.** `tools/renum.py` renumbered the list after the new reference was added. Reference numbers in the sections above this one use the **old** numbering. Old → new: 27→5, 5→6, 6→7, 7→8, 8→9, 9→10, 10→11, 11→12, 12→13, 13→14, 14→15, 15→16, 16→17, 17→18, 18→19, 19→20, 20→21, 21→22, 22→23, 23→24, 24→25, 25→26, 26→27. Unlisted numbers are unchanged.

## Review 2026-11-22
Applied all 26 findings from `reviews/18-review.md` (author: "approve all"). Each source was re-confirmed on PubMed (abstract and metadata) before the text was changed. No new references; `tools/renum.py` left the numbering unchanged (27 refs, all cited, no out-of-range citations). UNVERIFIED count unchanged (0).
- **#1** 18.3.2 Zandinejad: six studies included, two pooled (SMD 0.501, high heterogeneity) [9].
- **#2** 18.4.3 and Table 18.2: SLM accuracy described as "low" with no casting comparator; the casting comparison is kept for binder jetting only [12].
- **#3** 18.4.4, Table 18.2 and Table 18.3: PEEK and Co-Cr frameworks described as indirect CAD/CAM (30 patients); "milled PEEK" removed [21].
- **#4** Key Points, Table 18.2 and Table 18.3: SLM fit qualified by build orientation; deep (not medium) palatal vaults [15–18,20].
- **#5** Table 18.2 printed-pattern row: in vitro evidence from [16,17] added; caveat "In vitro only, n = 5 per group".
- **#6** Key Points: border-moulded preference attributed to the review and to one study of maxillary bases [2].
- **#7** Learning Objective 4: compares SLM, printed-pattern casting and conventional casting; describes milled and indirectly produced PEEK frameworks.
- **#8** 18.1: "accuracy" → "trueness and precision"; 18.4.3 ref 13 "accuracy (the authors' term)".
- **#9** 18.2.1 item 3 now cross-refers to Chapter 4; 18.2.3 citation moved to the trial-denture recommendation; Clinical Tip 1 scan-only caveat labelled expert opinion.
- **#10** 18.3.1, Table 18.3 and Key Points: "longer polymerisation times"; milled-base superiority labelled as mainly laboratory data [1,4].
- **#11** 18.3.2 lead-in: reviews broadly agree on patient-important outcomes but conflict on retention.
- **#12** 18.3.2 Prott: complications, aesthetics and processing-time findings attributed to single trials (very low certainty) [6].
- **#13** 18.3.2 Sivaswamy: "systematic review and meta-analysis of 12 studies"; comparisons are printed vs conventional or milled [7].
- **#14** 18.3.2 Fouda: learning curve hedged ("may face") [10].
- **#15** 18.4.3 Korkes: added "occlusal rest fit was similar in all groups"; Figure 18.3 caption no longer names the alloy and gives n = 10 per group. SVG unchanged (title/desc do not name the alloy; no data changed), so no re-render was needed.
- **#16** 18.4.3 Boontherawara: values in µm (194 and 92 µm), in vitro trueness, n = 5 per group [16].
- **#17** 18.4.3 Sasithornvechakul: lingual plates SLM 141 µm vs casting 207 µm, SLM = printed-pattern casting; lingual bars SLM 91 µm [17].
- **#18** 18.4.3 Elhadery: clinical part had only three patients [18].
- **#19** 18.4.3 Alabdullah: 70.7 µm is a root-mean-square gap; both below the 300-µm standard [19].
- **#20** Lab Note: only build orientation cited to [18]; support and heat treatment follow the manufacturer's protocols.
- **#21** 18.5.2 Guo: technical report, "with the aim of" restoring facial support [25].
- **#22** 18.5.2 Vosselman: five cadavers, 10 zygomatic implants; prosthetic-point deviation 1.03 mm added [26].
- **#23** Evidence Box, Table 18.3 and Key Points: "small series" removed; cadaver study and 23-patient review named [3,22–27].
- **#24** Key Points: uncited author framing no longer cited to [2].
- **#25** Key Points: time and digital record cited to [1,2]; complications to [2,11].
- **#26** Notes Summary: reference count corrected to 27; a line added above "References to check" saying the older sections use the pre-update numbering.
- Figures: none changed (Figure 18.3 caption text only). Tables 18.2 and 18.3 updated as above.
