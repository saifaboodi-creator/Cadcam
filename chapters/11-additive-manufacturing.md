# Chapter 11. Additive Manufacturing (3D Printing)

## Learning Objectives

After reading this chapter, you should be able to:

1. Describe the main additive manufacturing technologies used in dentistry and the materials each can process.
2. Explain how build orientation, layer thickness, supports and post-processing affect accuracy and properties.
3. Select appropriate printing technology and parameters for models, guides, splints, provisional and definitive restorations, dentures and metal frameworks.
4. Summarise the evidence comparing printed with milled and conventional devices.
5. Recognise the biocompatibility risks of printable resins and the post-processing steps that control them.
6. Describe the current status of printing ceramics and zirconia.

---

## 11.1 From Layers to Devices

Additive manufacturing (AM), usually called 3D printing, builds an object **layer by layer** from a digital model. Subtractive manufacturing (Chapter 10) removes material from a solid blank. Chapter 1 outlined the strengths of AM: little material waste, the ability to make complex internal shapes, and the capacity to build many parts in a single run [1–3].

Early reviews predicted that layered fabrication would bring a "second revolution" in dental device manufacture, once suitable materials existed [2]. At the time, printing was limited mainly to polymers and did not yet include ceramics [4]. A decade later the prediction has largely come true for models, guides, trays, splints, provisional restorations, denture bases and metal frameworks [1]. Printed definitive restorations and ceramics are developing quickly, but the evidence on them is still mostly in vitro.

---

## 11.2 Printing Technologies

The international standard terminology groups AM processes into families. Table 11.1 summarises those used in dentistry [1,2].

**Table 11.1** Additive manufacturing technologies in dentistry

| Family | Technology | Principle | Typical dental materials | Typical uses |
|---|---|---|---|---|
| **Vat photopolymerisation** | Stereolithography (SLA) | A laser cures liquid resin point by point, layer by layer | Model, guide, splint, provisional and denture resins | Models, guides, splints, dentures |
| | Digital light processing (DLP) | A projector cures a whole layer at once | Same as SLA; also ceramic-filled slurries | All of the above; fast batch production |
| | LCD / masked SLA (MSLA) | An LCD screen masks a light source to cure a whole layer | Same as SLA | Low-cost chairside and laboratory printing |
| **Material jetting** | Inkjet-type ("PolyJet", "MultiJet") | Droplets of photopolymer are jetted and cured; several materials and colours possible | Model and guide resins | Multi-colour models, guides |
| **Material extrusion** | Fused deposition modelling (FDM / FFF) | A heated thermoplastic filament is extruded | Thermoplastics | Low-cost models, prototypes |
| **Powder bed fusion** | Selective laser melting / sintering (SLM, SLS, DMLS) | A laser fuses metal or polymer powder layer by layer | Cobalt-chromium, titanium; polyamide | RPD frameworks, crown and bridge copings, bars, surgical plates |
| **Binder jetting** | — | A binder is jetted onto a powder bed; part sintered afterwards | Metals, ceramics | Emerging |

Vat photopolymerisation (SLA, DLP and LCD) dominates in practices and laboratories because it is affordable and accurate, and because a wide range of dental resins is available. Powder bed fusion dominates metal printing, usually in production centres.

---

## 11.3 The Printing Workflow

Every print follows the same steps:

1. **Design** in dental CAD software (Chapter 7) and export as STL or 3MF (Chapter 2).
2. **Preparation in slicing software:** orientation, supports, nesting of parts on the build platform, layer thickness and exposure settings for the chosen resin.
3. **Printing.**
4. **Washing** to remove uncured resin, usually in isopropyl alcohol or a manufacturer-specified solvent.
5. **Post-curing** with light, and sometimes heat, in a validated curing unit.
6. **Support removal and finishing:** cutting supports, smoothing, polishing, staining or characterising.
7. **Quality control:** checking fit, accuracy and surface (Chapter 12).

Each step affects the result. In practice, printer settings and post-processing cause as many problems as the printer itself.

### 11.3.1 Build orientation

The angle at which a part is built affects its accuracy, surface, strength, support requirements, build time and how many parts fit on the platform.

- **Crowns.** In a study of DLP-printed crowns at nine build angles, accuracy depended on the angle. The best results came at **135°**, which also gave the most favourable deviation pattern and a self-supporting geometry. At 210° the deviations were concentrated around the critical margin area [5].
- **Definitive FDPs.** For three-unit resin-based definitive FDPs, the interaction between build orientation and layer thickness affected accuracy and fit. Orientations of 30° and 90° with 50 µm layers gave accuracy similar to milled FDPs, but the **milled FDPs still fitted better** internally [6].
- **Models.** A systematic review of 14 studies found that most favoured **horizontal** orientation for model accuracy and for time and cost efficiency in single-model production. **Vertical** orientation fits two to three times more models on the platform for large overnight batches [7]. In contrast, a study of 144 full-arch models found that technology (SLA or DLP), orientation (0°, 10° or 20°) and shell thickness had **no significant** effect on overall accuracy. All groups remained below 0.2 mm, with RMS trueness of 73.9–194 µm [8].
- **Denture bases.** A systematic review of 24 studies found that horizontal orientation (0°) generally gave higher **flexural strength**, whereas accuracy and adaptation were better at 45° and 90°. Surface roughness was highest at 45° [9].
- **Splints.** In a small study of printed occlusal splints for orthognathic surgery, build angles of 0°, 30° and 90° did not change the fit. The 90° orientation was preferred because it increased printing capacity and shortened manufacturing time per splint [10].

> **Lab Note.** There is no single "best" orientation. It depends on the device, the resin, the printer and the property that matters most: margin accuracy for crowns, strength for denture bases, throughput for models. Use the orientation validated by the resin manufacturer for each indication, and keep critical surfaces, such as margins and intaglio surfaces, free of supports.

### 11.3.2 Layer thickness

Thinner layers reduce the visible "stair-stepping" on curved surfaces, but they increase build time and do not automatically improve accuracy:

- For definitive FDPs, 50 µm layers generally gave lower deviations than 100 µm layers at the best orientations [6].
- For orthodontic models printed on a low-cost LCD printer, printing at **100 µm** generally gave **better** trueness than 50 µm. Accuracy also varied significantly between resins [11].

The effect depends on the printer, resin and geometry. Follow validated settings rather than assuming thinner is better.

### 11.3.3 Supports

Supports anchor the part to the platform and hold up overhangs. They leave marks when removed. Place them on non-critical surfaces, such as the occlusal or facial surfaces of a model or the polished surface of a denture, never on margins, intaglio surfaces or contact areas. Self-supporting orientations, such as 135° for crowns, reduce the need for supports [5].

### 11.3.4 Washing and post-curing

Printed resin parts leave the printer only partly polymerised. **Washing** removes uncured surface resin. **Post-curing** completes polymerisation, which affects mechanical properties, dimensions and biocompatibility (Section 11.6). Under-curing leaves residual monomer and weaker parts. Over-curing or excess heat can cause distortion. Use the curing unit, wavelength, time and temperature validated for the resin.

---

## 11.4 Dental Applications

### 11.4.1 Models

Printed models have replaced stone casts in many digital workflows. Uses include working models for crowns and FDPs (often with removable dies), orthodontic models for aligner fabrication, and study models.

- A systematic review of printed full-arch models found that all of the technologies studied (SLA, DLP, material jetting and FFF) produced clinically acceptable accuracy. DLP and material jetting showed better precision and trueness than SLA and FFF [12].
- Model accuracy for fixed prosthodontics was within 0.2 mm for SLA and DLP across orientations and shell thicknesses in one study [8]. That is acceptable for many uses but larger than typical crown-margin tolerances (Chapter 3).

> **Clinical Tip.** A printed model is a copy of the scan, not of the patient. It cannot be more accurate than the scan it came from, and it adds its own printing error. Use printed models to check contacts, contours and occlusion. Do not use them to "correct" the fit of a restoration designed on the scan.

### 11.4.2 Surgical guides

Implant surgical guides are among the most established printed devices (Chapter 17). In an in vitro study, guides made by SLA, material jetting (PolyJet) and MultiJet printing showed **no significant differences** in implant angular deviation (median about 1.1–1.3°) or offset at the entry point and apex [13]. Guide accuracy depends at least as much on planning, registration, guide design and seating as on the printer.

### 11.4.3 Occlusal splints

Splints can be printed in rigid or flexible resins, milled, or made conventionally. Printed splints are fast and inexpensive to reproduce. Build angle did not affect the fit of printed surgical splints in one small study [10]. Chapter 19 discusses therapeutic occlusal devices.

### 11.4.4 Provisional and definitive resin restorations

Resins are now available for long-term provisional and "permanent" crowns and FDPs. Most are ceramic-filled methacrylates.

- The **cement-space setting** matters for printed crowns. A 70 µm setting gave the best marginal and internal fit for one definitive printed resin (Chapter 3) [14].
- A systematic review and meta-analysis of in vitro studies found that **milled resin crowns had higher fracture resistance** than printed ones, especially after ageing. Printed crowns showed **smaller marginal gaps** when the analysis was restricted to comparable, directly measured conditions. The certainty of evidence was low to very low [15].
- For three-unit definitive FDPs, printed FDPs had larger internal deviations and gaps than milled composite FDPs [6].
- The **bond strength** of printed crown resins to luting cements was high and comparable to milled materials. Airborne-particle abrasion with alumina was generally recommended. The authors stressed that clinical evidence for permanent use is lacking [16].

> **Evidence Box.** Almost all the evidence on printed "permanent" resin restorations is in vitro, and clinical survival data are scarce. Until clinical trials are available, treat printed resin crowns and FDPs as **long-term provisional** or **selected definitive** restorations, for example in patients for whom low cost, fast replacement or reversibility matters more than long-term durability.

### 11.4.5 Complete dentures

Printed denture bases and teeth allow fully digital dentures (Chapter 18):

- A systematic review and meta-analysis of 25 randomised trials comparing conventional, milled and printed complete dentures found **no fabrication method with a clear advantage** in patient-important outcomes. Printed dentures had a small retention advantage over **milled** ones, but more mechanical complications and aftercare needs. Milled dentures were rated better for aesthetics. The certainty of evidence was mostly very low [17].
- Another meta-analysis found that **conventional** dentures were more retentive than printed ones. Other clinical outcomes did not differ significantly [18].
- A systematic review of complications found that the fabrication technique influenced the number and type of complications. Digital dentures needed a similar or greater number of post-insertion visits, depending on the method [19].

### 11.4.6 Metal frameworks

**Selective laser melting (SLM)** of cobalt-chromium is widely used for removable partial denture frameworks and for crown and bridge substructures.

- The fit of SLM cobalt-chromium RPD frameworks was within clinically acceptable limits whether it was measured with a silicone replica or digitally, although the two methods gave different values (Chapter 3) [20].
- For implant-supported cobalt-chromium FDPs, a systematic review of in vitro studies found clinically acceptable fit for three-unit frameworks with all methods. For **12-unit** complete-arch frameworks, printed frameworks fitted **less accurately than milled** ones but **better than cast** ones [21].

---

## 11.5 Printing Ceramics and Zirconia

Ceramic printing uses vat photopolymerisation of slurries highly loaded with ceramic particles. Other methods, such as material jetting, are also being developed. The printed "green" part is debound (the polymer is burned out) and sintered, and it shrinks considerably. Controlling this shrinkage and avoiding internal defects are the main technical challenges.

The first comparisons with milling are encouraging:

- A systematic review and meta-analysis of in vitro studies of monolithic zirconia crowns found **comparable trueness and margin quality** for printed and milled crowns. Milling was better at the margin, printing in the axial areas. Precision and adaptation were clinically acceptable for both [22].
- A more recent meta-analysis found **significantly smaller marginal gaps** for milled zirconia prostheses (mean difference about 13 µm). Internal adaptation did not differ, and both methods were clinically acceptable [23].

Clinical studies of printed ceramic restorations are still lacking. Printed zirconia is promising for complex shapes and material efficiency. For now, milling remains the established method for definitive ceramic restorations (Chapter 10).

---

## 11.6 Biocompatibility and Regulation

### 11.6.1 Why biocompatibility matters

Printable resins are photopolymers. If polymerisation is incomplete, **residual monomers** and other compounds can be released. Post-processing chemicals, such as washing solvents, may also remain on the part if it is not handled correctly. A review of biocompatibility testing of printed dental polymers concluded that 3D printing causes the release of residual monomers through incomplete polymerisation, and involves potentially toxic substances in post-processing that cannot be completely eliminated. Independent biocompatibility testing was therefore recommended [24].

Post-processing matters. In a cell-culture study of two printed denture base resins, **longer post-curing** improved cell metabolic activity and reduced markers of cell death for one resin, but the other resin responded less consistently. The authors concluded that evaluating only the released substances is not enough: printing parameters also influence cytotoxicity [25].

### 11.6.2 Practical safety rules

- Use only resins that are **cleared or approved for the intended dental use** in your jurisdiction (for example, as a medical device), and only within that indication.
- Use the **printer and curing unit validated** by the resin manufacturer, or follow its open-system settings exactly.
- Follow washing and post-curing protocols exactly; do not shorten them.
- Store resins correctly, observe shelf life, and mix them before use.
- Wear gloves and handle uncured resin and solvents with ventilation. Uncured methacrylate resins are skin sensitisers.
- Record the resin, batch, printer, settings and post-processing for each device (traceability).

A printed device made with an approved resin but the wrong post-processing is effectively a **different, untested device**.

---

## 11.7 Choosing Between Printing and Milling

**Table 11.2** Printing or milling? Current guidance by indication

| Device | Preferred route | Reason |
|---|---|---|
| Working and orthodontic models | Printing | Fast, inexpensive, batch production; acceptable accuracy [7,8,12] |
| Implant surgical guides | Printing | Established; printer type has little effect on accuracy [13] |
| Occlusal splints | Printing or milling | Printing fast and economical [10]; milling gives homogeneous material |
| Provisional crowns and FDPs | Printing or milling | Both suitable; printing economical for multiple units |
| Definitive resin crowns | Milling preferred; printing for selected cases | Milled resins more fracture-resistant; printed lack clinical data [15,16] |
| Definitive ceramic restorations | Milling | Clinical evidence; printed ceramics still in vitro [22,23] |
| Complete dentures | Printing or milling | No clear clinical advantage of either [17,18]; milled bases more homogeneous |
| RPD frameworks (Co-Cr) | SLM printing | Clinically acceptable fit; efficient [20] |
| Complete-arch implant frameworks | Milling preferred | Milled frameworks fit better than printed ones for long spans [21] |

---

## Key Points

- **Vat photopolymerisation** (SLA, DLP, LCD) dominates resin printing in dentistry. **Selective laser melting** dominates metal printing [1].
- Build orientation, layer thickness, supports, washing and post-curing **all** affect accuracy and properties. There is no universal best setting [5–11].
- Printed **models** and **guides** are well established and clinically acceptable [8,12,13].
- Printed **definitive resin** restorations are mechanically weaker than milled ones after ageing and lack clinical data [15,16].
- Printed, milled and conventional **complete dentures** show no clear difference in patient-important outcomes, but the certainty of evidence is very low [17–19].
- **SLM** cobalt-chromium frameworks fit acceptably. For complete-arch implant frameworks, milled frameworks fit better than printed, and printed better than cast [20,21].
- **Printed zirconia** is comparable to milled in vitro but slightly less accurate at the margin, with no clinical data yet [22,23].
- **Biocompatibility** depends on resin and post-processing. Use approved resins with validated settings and protocols [24,25].

---

## Review Questions

1. Compare SLA, DLP and LCD printing in terms of how each cures a layer of resin.
2. Why might a crown printed at 210° show more deviation at the margin than one printed at 135°?
3. A laboratory wants to print 30 orthodontic models overnight. Which orientation would you advise, and what is the trade-off?
4. Explain why printing at a thinner layer thickness does not always improve accuracy.
5. Summarise the in vitro evidence comparing printed and milled resin crowns for fracture resistance and marginal fit.
6. What did a meta-analysis of randomised trials conclude about printed versus milled versus conventional complete dentures?
7. List four steps a practice should take to make sure printed intraoral devices are biocompatible.
8. For which indications would you currently choose printing over milling, and why?

---

## References

1. Dawood A, Marti Marti B, Sauret-Jackson V, Darwood A. 3D printing in dentistry. Br Dent J. 2015;219(11):521–9. doi:10.1038/sj.bdj.2015.914
2. van Noort R. The future of dental devices is digital. Dent Mater. 2012;28(1):3–12. doi:10.1016/j.dental.2011.10.014
3. Abduo J, Lyons K, Bennamoun M. Trends in computer-aided manufacturing in prosthodontics: a review of the available streams. Int J Dent. 2014;2014:783948. doi:10.1155/2014/783948
4. Alghazzawi TF. Advancements in CAD/CAM technology: options for practical implementation. J Prosthodont Res. 2016;60(2):72–84. doi:10.1016/j.jpor.2016.01.003
5. Osman RB, Alharbi N, Wismeijer D. Build angle: does it influence the accuracy of 3D-printed dental restorations using digital light-processing technology? Int J Prosthodont. 2017;30(2):182–8. doi:10.11607/ijp.5117
6. Dönmez MB, Demirel M, Diken Türksayar AA, Yilmaz B. Influence of printing parameters on the fabrication and fit accuracy of additively manufactured resin-based definitive three-unit fixed partial dentures. J Dent. 2025;161:105937. doi:10.1016/j.jdent.2025.105937
7. Alghauli MA, Almuzaini SA, Aljohani R, Alqutaibi AY. Impact of 3D printing orientation on accuracy, properties, cost, and time efficiency of additively manufactured dental models: a systematic review. BMC Oral Health. 2024;24(1):1550. doi:10.1186/s12903-024-05365-5
8. García Gil I, Rodríguez Alonso V, Tobar Arribas C, Mosaddad SA, Peláez J, Suárez MJ. Effect of 3D printing technology, build orientation, and shell thickness on the accuracy of full-arch dental models for fixed dental prostheses: an in vitro study. Sci Rep. 2025;15(1):40938. doi:10.1038/s41598-025-24780-4
9. Alqutaibi AY, Aljohani R, Almuzaini S, Alghauli MA. Physical-mechanical properties and accuracy of additively manufactured resin denture bases: impact of printing orientation. J Prosthodont Res. 2025;69(4):461–71. doi:10.2186/jpr.JPR_D_24_00263
10. Zwerink LGJM, Xi T, Verhulst AC, Tellman JWH, Baan F, Maal TJ. [Innovations in dentistry. The influence of build angle on the fit of a 3D printed occlusal splint]. Ned Tijdschr Tandheelkd. 2020;127(3):171–6. Dutch. doi:10.5177/ntvt.2020.03.19094
11. Bor S, Oğuz F. Effect of different printing designs and resin types on the accuracy of orthodontic model. Polymers (Basel). 2025;17(20):2724. doi:10.3390/polym17202724
12. Mistry G, Sardar C, Pandey P, De Souza M, Kailaje V, Sachdev SS. 3D printed full-arch versus digital reference dental models: a systematic review. Bioinformation. 2024;20(9):1100–5. doi:10.6026/9732063002001100
13. Herschdorfer L, Negreiros WM, Gallucci GO, Hamilton A. Comparison of the accuracy of implants placed with CAD-CAM surgical templates manufactured with various 3D printers: an in vitro study. J Prosthet Dent. 2021;125(6):905–10. doi:10.1016/j.prosdent.2020.03.017
14. Shin H, Kang YJ, Kim H, Kim JH. Effect of cement space settings on the marginal and internal fit of 3D printed definitive resin crowns. J Prosthet Dent. 2025;133(3):821–6. doi:10.1016/j.prosdent.2023.03.021
15. Alawawda O, Kızıldağ Z, Yeşil Z. Fracture resistance and marginal adaptation of 3D-printed versus milled resin-based permanent crowns: a systematic review and meta-analysis. J Esthet Restor Dent. 2026;38(12):2261–72. doi:10.1111/jerd.70248
16. Kagaoan Z, Liu X, Cameron A, Aarts J, Choi JJE. Factors influencing the bond strength of additively manufactured crown materials in dentistry: a systematic review of in vitro studies. J Dent. 2024;144:104908. doi:10.1016/j.jdent.2024.104908
17. Prott LS, Peričić TP, D'Alessandro C, Rivera M, Graham L, Gierthmuehlen PC, et al. Conventional, milled, and 3D-printed complete dentures: a systematic review and meta-analysis of clinical and patient-centered outcomes. J Esthet Restor Dent. 2026. Epub ahead of print. doi:10.1111/jerd.70283
18. Sivaswamy V, Cahyanto A, Varma SR, Matinlinna JP. Clinical outcomes of 3D printed complete dentures: a systematic review and meta-analysis. J Prosthet Dent. 2026;136(1):60–8. doi:10.1016/j.prosdent.2026.02.003
19. Smets K, Vandeweghe S, Ongenae L, D'haese R. Complications of 3D printed dentures: a systematic review. J Prosthet Dent. 2026;135(4):754–61. doi:10.1016/j.prosdent.2025.05.019
20. Alabdullah SA, Hannam AG, Wyatt CC, McCullagh APG, Aleksejuniene J, Mostafa NZ. Comparison of digital and conventional methods of fit evaluation of partial removable dental prosthesis frameworks fabricated by selective laser melting. J Prosthet Dent. 2022;127(3):478.e1–478.e10. doi:10.1016/j.prosdent.2021.09.033
21. He Z, Bennani V, Aarts JM, Choi JJE, Veerasamy A. Fit accuracy of 3D printed Co-Cr multiunit implant-supported fixed dental prostheses: a systematic review of in vitro studies. J Prosthet Dent. 2026;135(1):64.e1–64.e10. doi:10.1016/j.prosdent.2025.08.033
22. da Silva SEG, da Silva NR, Santos JVDN, Moreira FGG, Özcan M, Souza ROAE. Accuracy, adaptation and margin quality of monolithic zirconia crowns fabricated by 3D printing versus subtractive manufacturing technique: a systematic review and meta-analysis of in vitro studies. J Dent. 2024;147:105089. doi:10.1016/j.jdent.2024.105089
23. Sengottaiyan AK, Bennani V, Veerasamy A. Marginal fit and internal adaptation of zirconia complete coverage fixed dental prostheses fabricated by milling versus 3D printing: a systematic review and meta-analysis of in vitro studies. J Prosthet Dent. 2026;136(2):379–89. doi:10.1016/j.prosdent.2026.02.051
24. Rus F, Neculau C, Imre M, Duica F, Popa A, Moisa RM, et al. Polymeric materials used in 3DP in dentistry — biocompatibility testing challenges. Polymers (Basel). 2024;16(24):3550. doi:10.3390/polym16243550
25. Dinescu M, Vasilescu VG, Ciocan LT, Voicu-Balasea B, Țâncu AMC, Ripszky A, et al. Evaluation of post-processing time's influence on biocompatibility of 3D-printed denture base resins. J Funct Biomater. 2026;17(4):188. doi:10.3390/jfb17040188
