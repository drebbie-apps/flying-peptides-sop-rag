---
doc_id: "TM-104"
doc_type: "Method SOP"
title: "Microflow MRM LC-MS acquisition"
manufacturer: "Positive Climb Diagnostics"
assay: "3-plex immuno-MRM DKD assay"
source: "Bringans et al. 2020, CC BY 4.0"
version: "1.0"
status: "Effective"
approval_date: 2022-01-20
effective_date: 2022-02-03
supersedes: null
superseded_by: null
iso_clause: ["4.2.5", "6.3", "7.5.1", "7.5.6", "7.6", "8.3"]
author: "Dr. LC Proton, Associate Scientist"
reviewer: "Mira Armstrong, Technical Reviewer"
approver: "Tess Lindqvist, Quality Assurance"
training_case: true
---

# TM-104: Microflow MRM LC-MS acquisition

**Positive Climb Diagnostics · Standard Operating Procedure**

*Flying Peptides training case · Fictitious manufacturer: Positive Climb Diagnostics · Not a real company, product or QMS.*

*Adapted from: Bringans S, Ito J, Casey T, et al. "A robust multiplex immunoaffinity mass spectrometry assay (PromarkerD) for clinical prediction of diabetic kidney disease." Clin Proteomics 2020;17:37. doi:10.1186/s12014-020-09302-w. Licensed under CC BY 4.0 ([https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)). The methods were restructured and rewritten as controlled procedures for a fictitious company; procedural detail was added for training purposes. The authors, Proteomics International and Atturos do not endorse this document.*

*Names and roles are illustrative (training case); all roles were performed by Dr. Ebbie. Drafted with AI assistance; reviewed and approved by Dr. Ebbie.*

## 1 Purpose

This procedure defines how a processed plate of the 3-plex immuno-MRM DKD assay is measured by microflow LC-MS/MS in MRM mode on a triple quadrupole mass spectrometer (short: LC-MRM), including the system suitability test (SST) that must pass before samples are injected and the checks that run during the sequence, so that acquisition takes place under controlled conditions (ISO 13485 §7.5.1) and the raw data are fit for data analysis under TM-105.

## 2 Scope

### 2.1 Applicability

LC-MRM acquisition of one processed 96-well plate (one batch) from TM-103: system preparation, LC and MS settings, the method files, the SST and its reference values, the injection sequence with its in-run checks, and the transfer of raw data files to controlled storage.

### 2.2 Qualifications and training

Associate Scientists with documented training on TM-104 and on the LC-MS system and its acquisition software. Training must be recorded before the first independent run. An Associate Scientist without recorded training does not run batches under this SOP until the training is recorded.

### 2.3 Exclusions

Sample processing and the plate map (TM-103); data analysis (TM-105); batch acceptance and run release (TM-106); installation, operational and performance qualification and preventive maintenance of the LC-MS system (QMS-008, Equipment qualification and maintenance) [ID proposed; document not yet drafted].

## 3 Responsibilities

| Role | Responsibility |
| :---- | :---- |
| Associate Scientist | Prepares the LC-MS/MS system, establishes the SST reference values, runs and records the SST and the in-run checks, builds and runs the injection sequence, and stops and raises an NCR when a check fails. |
| Technical Reviewer | Approves the SST reference values; signs off the SST before samples are injected; reviews the batch record, the SST record and the instrument log before releasing the raw data to TM-105; verifies the method files against their sources before first use. |
| Quality Assurance | Decides the disposition of nonconforming runs (QMS-003 §6.3) and approves changes to method parameters, method files, instruments or acquisition software (QMS-005). |

## 4 Definitions and abbreviations

### 4.1 General terms and abbreviations (ISO 13485 / ISO 9000)

| Term | Definition |
| :---- | :---- |
| Batch / lot | A defined quantity of material or product processed in one process or series of processes. For this assay, one 96-well plate is one batch. |
| Critical control point (CCP) | A step where a check must pass and be signed off before the procedure continues. |
| Nonconformity | Non-fulfilment of a specified requirement. |
| Rework | Action on nonconforming product to make it conform to its requirements, followed by re-verification (QMS-003 §4). In this SOP: re-injection of wells of the same processed plate (TM-104 §7.6.9). |
| Technical Reviewer | Role with technical review authority. Under QMS-001 §6.3 it reviews controlled documents; in this SOP it approves the SST reference values, signs off the SST and releases the raw data. |
| SST reference values | Approved mean retention time and mean peak area of each SIS peptide, and the mean LC pressure at starting conditions, against which the SST and the in-run checks are evaluated (TM-104 §7.5.12 to §7.5.15). |
| SST reference record | Part of the instrument log that holds the SST reference values with the serial numbers of the trap and analytical columns, the SST sample lot, the date and the Technical Reviewer's approval. |
| ACN | Acetonitrile |
| APOA4 | Apolipoprotein A4 |
| CAM | Carbamidomethyl (cysteine modified by iodoacetamide) |
| CD5L | CD5 antigen-like |
| CV | Coefficient of variation |
| DKD | Diabetic kidney disease |
| FA | Formic acid |
| IAM | Iodoacetamide |
| IBP3 | Insulin-like growth factor-binding protein 3 |
| ID | Identifier (e.g. plate ID, batch ID, document ID) |
| LC | Liquid chromatography |
| LC-MS | Liquid chromatography–mass spectrometry |
| MS | Mass spectrometry; mass spectrometer |
| *m/z* | Mass-to-charge ratio |
| NCR | Nonconformity record (QMS-003-F01) |
| PBS | Phosphate buffered saline |
| Q1 / Q3 | First / third quadrupole of the triple quadrupole mass spectrometer |
| QC | Quality control |
| S/N | Signal-to-noise ratio |
| SST | System suitability test |
| TEAB | Triethylammonium bicarbonate |

### 4.2 Immuno-MRM terms (method SOPs only)

| Term | Definition |
| :---- | :---- |
| MRM | Multiple reaction monitoring: targeted measurement of defined precursor-to-product ion pairs on a triple quadrupole mass spectrometer. |
| Transition | One precursor-to-product ion *m/z* pair. In this assay all transitions of a peptide are summed into its peak area; no transition is designated quantifier or qualifier (TM-104 §7.4). |
| Signature peptide | Tryptic peptide of a target protein measured as its surrogate. |
| Light / heavy peptide | Endogenous (unlabelled) signature peptide / its 13C15N-labelled SIS peptide. |
| SIS | Stable isotope-labelled internal standard: a synthetic heavy-isotope peptide used to normalise signal across samples. |
| Ab-beads | Magnetic beads conjugated with the capture antibody for one target protein. |
| Calibrator | Recombinant target proteins at known concentrations, processed alongside samples to convert signal into concentration. |
| Reference plasma | Pooled plasma processed in every batch to monitor assay performance (QC). |
| Microflow LC | Liquid chromatography at flow rates in the µL/min range. |
| Trap column | Short guard column that receives the injected sample at the loading flow, removes salts and is then switched in line with the analytical column. |
| Double blank | Well with 200 µL PBS and no Ab-beads, processed in TM-103 (Bringans et al. 2020, Sample processing). |
| Carryover | Signal in an injection that comes from an earlier injection. |
| Dwell time | Time the mass spectrometer spends measuring one transition in each cycle. |
| Retention time | Time from injection to the apex of a peptide's chromatographic peak. |
| SST: System suitability test | Injections of the SST sample (TM-104 §5.1) before the first sample of a batch, showing that the LC-MS system performs as required on the day (TM-104 §7.5, §8.2). |
| Bracketing / closing SST injection | Single injection of the SST sample after every 24 sample injections (bracketing) and after the last sample (closing), showing that performance is maintained through the sequence (TM-104 §7.6.1). |

## 5 Materials, reagents and equipment

### 5.1 Reagents and consumables

| Material / reagent | Grade / composition | Catalogue no. / specification | Lot tracking | Storage |
| :---- | :---- | :---- | :---- | :---- |
| Water | LC-MS grade | In-house water purification system | Date of dispensing | Room temperature |
| Acetonitrile (ACN) | LC-MS grade | [Cat. no.] | Record lot no. in the batch record | Flammables cabinet |
| Formic acid (FA) | LC-MS grade | [Cat. no.] | Record lot no. in the batch record | Corrosives cabinet |
| Mobile phase A | Water, 0.1% (v/v) FA | Prepared per TM-104 §7.1.6 | Record preparation date and component lots | Room temperature; use within 7 days |
| Mobile phase B | ACN, 0.1% (v/v) FA | Prepared per TM-104 §7.1.6 | Record preparation date and component lots | Room temperature; use within 7 days |
| Loading solvent | 2% (v/v) ACN, 0.1% (v/v) FA in water (Bringans et al. 2020, Targeted (MRM) LC-MS analysis) | Prepared per TM-104 §7.1.6 | Record preparation date and component lots | Room temperature; use within 7 days |
| SST sample | Each of the three SIS peptides (TM-104 §7.4) at 400 fmol per 72 µL (5.56 fmol/µL) in 50 mM TEAB; one 25 µL injection puts 139 fmol of each SIS peptide on column. (calculation in the note below). | Prepared under TM-102 [section to be cited when TM-102 is drafted] | Record SST sample lot and SIS peptide lots in the batch record | Single-use 100 µL aliquots at −80 °C for up to 6 months; in the autosampler at 4 °C for up to 24 h |
| Processed plate | 300 µL V-bottom 96-well plate (Greiner) | From TM-103 [section to be cited when TM-103 is drafted] | Record plate ID in the batch record | 4 °C in the autosampler (TM-104 §7.6.7) |
| Plate seal | Pierceable foil heat seal for 96-well plates, compatible with the autosampler needle | [Cat. no.] | Record lot no. in the batch record | Room temperature |

*The loading solvent composition is from Bringans et al. 2020, Targeted (MRM) LC-MS analysis. The paper states acetonitrile with 0.1% formic acid for the gradient but not the composition of the aqueous phase, so both mobile-phase compositions contain 0.1% FA. The SST sample concentration is derived from Bringans et al. 2020, Sample processing: 400 fmol of each SIS peptide in 56 µL, followed by 6 µL IAM and 10 µL trypsin, gives 72 µL per well; 25 µL of that is injected (Bringans et al. 2020, Targeted (MRM) LC-MS analysis), so 400 fmol × 25/72 = 139 fmol on column. Its solvent, aliquot volume and shelf life were added for illustrative purposes. A new SST sample lot needs new SST reference values (TM-104 §7.5.12). Catalogue numbers, storage, shelf lives and the plate seal were added for illustrative purposes.*

### 5.2 Equipment and instrumentation

| Equipment | Model / manufacturer | Minimum specification | Calibration / maintenance check |
| :---- | :---- | :---- | :---- |
| Microflow LC system | Shimadzu Prominence HPLC (1st development laboratory); Agilent 1290 LC (2nd development laboratory) | Shimadzu Prominence HPLC: loading pump at 40 µL/min; two nano pumps at a combined 5 µL/min; column oven at 40 °C; cooled autosampler at 4 °C; Agilent 1290 LC: not stated in the paper | Qualification and maintenance status confirmed before use (ISO 13485 §6.3; TM-104 §7.1.1) |
| Trap column | MicroLC Guard Column C18 (Sciex) | C18 | Record serial no. and injection count in the column log |
| Analytical column | ChromXP C18 (Sciex) | 3 µm, 120 Å, 300 µm internal diameter, 5 cm | Record serial no. and injection count in the column log |
| Triple quadrupole mass spectrometer | QTRAP 5500 (Sciex) (1st development laboratory); 6495B (Agilent) (2nd development laboratory) | QTRAP 5500: Turbo V ion source with 50 µm electrode and grounding unit. 6495B: Agilent Jet Stream (AJS) thermal gradient focusing ion source | Mass calibration within the manufacturer's interval (ISO 13485 §7.6; TM-104 §7.1.2); qualification and maintenance status confirmed before use (ISO 13485 §6.3; TM-104 §7.1.1) |
| Acquisition software | [Name and version] | Validated for its intended use (QMS-006) | Version recorded in the batch record; changes only via QMS-005 |
| MRM method file TM-104-M01 | Controlled acquisition method file | Holds the MS settings of TM-104 §7.3 and the transition settings of TM-104 §7.4 | Version recorded in the batch record. Verified by the Technical Reviewer against TM-104 §7.3 and Bringans et al. 2020, Additional file 1 before first use and after each change; changed only under QMS-005 |
| LC method file TM-104-M02 | Controlled LC method file | Holds the LC settings of TM-104 §7.2 | Version recorded in the batch record. Verified by the Technical Reviewer against TM-104 §7.2 before first use and after each change; changed only under QMS-005 |
| Nitrogen supply | [Generator or cylinder] | Purity and pressure as specified by the MS manufacturer | Supply pressure checked before each run (TM-104 §7.1.4) |

*The LC and MS models are those named for the development laboratories in Bringans et al. 2020, Targeted (MRM) LC-MS analysis, the section the equipment rows rely on. The paper is not consistent on this point: its Inter-laboratory comparisons section places a 4000 QTRAP at the development laboratory. That comparison covered 8 samples prepared by the original immunodepletion method, run with the same LC-MS method on a 4000 QTRAP and a 5500 QTRAP (Bringans et al. 2020, Inter-laboratory comparisons; Results). The transfer of the immunoaffinity method to the 2nd development laboratory used an Agilent 1290 LC with a 6495B mass spectrometer (Bringans et al. 2020, Inter-laboratory comparisons). Neither comparison qualifies another instrument model for this SOP: use another model only after an equivalence assessment under change control (QMS-005).*

## 6 Safety and environmental controls

### 6.1 Health and safety

Wear a lab coat, nitrile gloves and eye protection at all times. Handle human plasma under biosafety level 2 (BSL-2) containment. Dispose of chemical and biohazardous waste according to local regulations and QMS-009 (Laboratory safety and waste) [ID proposed; document not yet drafted].

### 6.2 Solvents and chemicals (method SOPs)

Handle acetonitrile and formic acid in a fume hood. Acetonitrile is highly flammable and harmful; formic acid is corrosive (see the safety data sheets). Collect LC waste in a labelled solvent waste container and empty it before it is 80% full.

### 6.3 Instrument gases and exhaust (method SOPs)

The nitrogen supply (curtain, ion source and collision gases) is checked before each run (TM-104 §7.1.4). Vent the source exhaust and the roughing-pump exhaust to the laboratory extraction. Caution: the ion source runs at 250 °C and 5500 V. Put the instrument in standby and let the source cool before touching it.

### 6.4 Environmental requirements

Ambient laboratory temperature 18 to 25 °C, recorded daily in the laboratory log by the Associate Scientist. Autosampler at 4 °C (Bringans et al. 2020, Table 1); its temperature is recorded at the start and the end of each sequence (TM-104 §7.6.3, §7.6.11).

## 7 Procedure

### 7.1 System preparation

| Who | Task |
| :---- | :---- |
| Associate Scientist | 7.1.1 Check that the LC-MS system is qualified and within its maintenance interval (ISO 13485 §6.3; QMS-008). Record the status in the batch record. |
| Associate Scientist | 7.1.2 Check that the mass spectrometer is within its mass-calibration interval (ISO 13485 §7.6). Record the status in the batch record. |
| Associate Scientist | 7.1.3 Check that the acquisition software version matches the validated version recorded in the batch record (QMS-006). |
| Associate Scientist | 7.1.4 Check that the nitrogen supply pressure meets the MS manufacturer's specification (TM-104 §5.2). |
| Associate Scientist | 7.1.5 If any check in TM-104 §7.1.1 to §7.1.4 fails, stop, do not acquire, and inform the Technical Reviewer. |
| Associate Scientist | 7.1.6 Prepare mobile phase A, mobile phase B and the loading solvent (TM-104 §5.1). Label each bottle with content, lot numbers, preparation and expiry dates and initials. |
| Associate Scientist | 7.1.7 Install the trap column and the analytical column (TM-104 §5.2). Record their serial numbers and injection counts in the column log. |
| Associate Scientist | 7.1.8 If a column serial number differs from the one in the SST reference record, establish new SST reference values (TM-104 §7.5.12 to §7.5.15) before the SST. |
| Associate Scientist | 7.1.9 Purge the LC pumps. |
| Associate Scientist | 7.1.10 Set the column oven to 40 °C (TM-104 §7.2). |
| Associate Scientist | 7.1.11 Set the autosampler to 4 °C (TM-104 §7.2). |
| Associate Scientist | 7.1.12 Equilibrate the columns at the starting conditions of TM-104 §7.2 for at least 15 min. |
| Associate Scientist | 7.1.13 Load the LC method file TM-104-M02 in the version listed in the batch record (TM-104 §5.2). |
| Associate Scientist | 7.1.14 Load the MRM method file TM-104-M01 in the version listed in the batch record (TM-104 §5.2). |
| Associate Scientist | 7.1.15 Receive the processed plate from TM-103 and check that its plate ID and plate map match the batch record. |
| Associate Scientist | 7.1.16 If the plate ID or the plate map does not match, keep the plate at 4 °C and follow TM-104 §8.3. |
| Associate Scientist | 7.1.17 Seal the plate with the plate seal (TM-104 §5.1). |
| Associate Scientist | 7.1.18 Place the plate in the autosampler at 4 °C. |
| Associate Scientist | 7.1.19 Record the time of placing the plate in the autosampler in the batch record. The time limit of TM-104 §7.6.7 starts at this time. |

### 7.2 LC method

The LC method file TM-104-M02 (TM-104 §5.2) contains the settings in the table below. All values come from Bringans et al. 2020, *Targeted (MRM) LCMS analysis* or Table 1, except those marked [ADDED FOR TRAINING].

**Timing.** The run starts at injection (time zero) and lasts 8 min in total. The first 2 min are trap loading: the loading pump transfers the sample from the loop onto the trap column at 40 µL/min. The 8 min do not include the time the autosampler needs to draw the sample.

This table governs: if the method file differs from it, do not acquire and follow TM-104 §8.3.

| Parameter | Setting |
| :---- | :---- |
| Configuration | Loading pump to the trap column; two nano pumps for the analytical gradient |
| Injection volume | 25 µL per well from the 300 µL V-bottom plate |
| Autosampler temperature | 4 °C |
| Trap column | MicroLC Guard Column C18 |
| Trap loading, 0.0–2.0 min | 2% (v/v) ACN, 0.1% (v/v) FA, isocratic, 40 µL/min |
| Analytical column | ChromXP C18, 3 µm, 120 Å, 300 µm internal diameter, 5 cm |
| Column temperature | 40 °C |
| Analytical flow | 5 µL/min (two nano pumps combined), through the trap column onto the analytical column |
| Mobile phases | A and B as in TM-104 §5.1; % B equals % acetonitrile |
| Gradient 2.0–4.0 min | 10% → 40% B |
| Gradient 4.0–4.2 min | 40% → 98% B |
| Gradient 4.2–4.4 min | Hold at 98% B |
| Gradient 4.4–4.5 min | 98% → 10% B |
| Re-equilibration 4.5–8.0 min | 10% B |
| Total run time | 8 min |

### 7.3 MS source and global settings

The MRM method file TM-104-M01 (TM-104 §5.2) holds these settings. Bringans et al. 2020, Targeted (MRM) LC-MS analysis gives these values without units; the units in brackets are the acquisition software's default units.

| Parameter | Setting |
| :---- | :---- |
| Mass spectrometer | Triple quadrupole: QTRAP 5500 (Sciex) at the 1st development laboratory; 6495B (Agilent) at the 2nd development laboratory. The settings in this table are those of the QTRAP 5500 |
| Ion source | Turbo V with 50 µm electrode and grounding unit |
| Polarity | Positive |
| Scan type | MRM |
| Source temperature | 250 °C |
| IonSpray voltage | 5500 (V) |
| Curtain gas | 25 (psi) |
| Collision gas | Medium |
| Ion source gas 1 and 2 (GS1, GS2) | 25 each (psi) |
| Entrance potential | 10 (V) |
| Collision cell exit potential | 14 (V) |
| Q1 and Q3 resolution | Low |
| Declustering potential, collision energy, dwell time | Per transition, in the MRM method file TM-104-M01 (TM-104 §7.4) |

### 7.4 MRM transitions

Each target protein is measured by one signature peptide and its SIS peptide, labelled with 13C and 15N at the C-terminal arginine (Bringans et al. 2020, Reagents). The light sequences are the SIS sequences without the label. All transitions of a peptide are summed into its peak area (Skyline Total Area, TM-105 §7.2); no transition is designated quantifier or qualifier and no ion-ratio check is applied. The MRM method file TM-104-M01 (TM-104 §5.2) contains the transitions in the table below. All values come from Bringans et al. 2020, Additional file 1. This table governs: if the method file differs from it, do not acquire and follow TM-104 §8.3. [C\* = Carbamidomethylated Cys]

| Protein | Peptide | Q1 *m/z* (2+) | Product ion | Q3 *m/z* | Dwell (ms) | DP (V) | CE (V) |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| APOA4 | LEPYADQLR | 552.788 | y7 | 862.442 | 60 | 71.4 | 27.2 |
| APOA4 | LEPYADQLR | 552.788 | y6 | 765.389 | 60 | 71.4 | 27.2 |
| APOA4 | LEPYADQLR[13C6,15N4] | 557.792 | y7 | 872.450 | 60 | 71.4 | 27.2 |
| APOA4 | LEPYADQLR[13C6,15N4] | 557.792 | y6 | 775.397 | 60 | 71.4 | 27.2 |
| CD5L | LVGGDNLC\*SGR | 574.280 | y9 | 935.400 | 60 | 73.0 | 28.5 |
| CD5L | LVGGDNLC\*SGR | 574.280 | y4 | 479.203 | 60 | 73.0 | 28.5 |
| CD5L | LVGGDNLC\*SGR[13C6,15N4] | 579.284 | y9 | 945.408 | 60 | 73.0 | 28.5 |
| CD5L | LVGGDNLC\*SGR[13C6,15N4] | 579.284 | y4 | 489.211 | 60 | 73.0 | 28.5 |
| IBP3 | FLNVLSPR | 473.279 | y6 | 685.399 | 60 | 65.6 | 22.7 |
| IBP3 | FLNVLSPR | 473.279 | y5 | 571.356 | 60 | 65.6 | 22.7 |
| IBP3 | FLNVLSPR[13C6,15N4] | 478.284 | y6 | 695.407 | 60 | 65.6 | 22.7 |
| IBP3 | FLNVLSPR[13C6,15N4] | 478.284 | y5 | 581.365 | 60 | 65.6 | 22.7 |

### 7.5 System suitability test [CRITICAL CONTROL POINT]

The SST shows on the day that the LC-MS system performs the validated process (ISO 13485 §7.5.6). Run it before the first sample injection of every batch, and again before resuming after an interruption longer than 2 h or after maintenance during the sequence [ADDED FOR TRAINING]. The SST sample is defined in TM-104 §5.1. The SST and the in-run checks are evaluated against approved SST reference values, established in TM-104 §7.5.12 to §7.5.15. Bracketing and closing SST injections are part of the injection sequence (TM-104 §7.6.1).

| Who | Task |
| :---- | :---- |
| Associate Scientist | 7.5.1 Inject one solvent blank (loading solvent). |
| Associate Scientist | 7.5.2 Inject the SST sample 3 times [ADDED FOR TRAINING] with the method files of TM-104 §5.2. |
| Associate Scientist | 7.5.3 Evaluate the blank and the SST injections against TM-104 §8.2 in the Skyline document template of TM-105 §5.1, and record each value on the SST record. |
| Technical Reviewer | 7.5.4 [CRITICAL CONTROL POINT] Verify and sign off the SST record as passed or failed. |
| **If all criteria pass** | |
| Associate Scientist | 7.5.5 Start the injection sequence (TM-104 §7.6). |
| **If any criterion fails** | |
| Associate Scientist | 7.5.6 Do not inject samples. Keep the plate at 4 °C in the autosampler. |
| Associate Scientist | 7.5.7 Raise an NCR (QMS-003-F01) under QMS-003 §6.1 (TM-104 §8.3.4). |
| Associate Scientist | 7.5.8 Troubleshoot only through actions recorded in the NCR (e.g. leak check, spray check, trap or column replacement). |
| Associate Scientist | 7.5.9 After a trap or analytical column replacement, MS source cleaning or MS maintenance, establish new SST reference values (TM-104 §7.5.12 to §7.5.15). |
| Associate Scientist | 7.5.10 Repeat TM-104 §7.5.1 to §7.5.4. |
| Quality Assurance | 7.5.11 Decide the disposition of the NCR (QMS-003 §6.3.2). If the SST cannot be passed in time to finish all injections within the limit of TM-104 §7.6.7, the plate is nonconforming product (QMS-003 §6.1). |
| **Establishing SST reference values** | |
| Associate Scientist | 7.5.12 Establish SST reference values when a trap or analytical column with a new serial number is installed, after MS source cleaning or maintenance, and for each new SST sample lot. |
| Associate Scientist | 7.5.13 Inject one solvent blank, then the SST sample 6 times. |
| Associate Scientist | 7.5.14 Calculate the mean apex retention time and mean peak area of each SIS peptide, and the mean LC pressure at starting conditions, from the 6 injections. Enter them in the SST reference record with the column serial numbers and the SST sample lot. |
| Technical Reviewer | 7.5.15 [CRITICAL CONTROL POINT] Approve the reference values only if every SIS peptide in the 6 injections meets the detection (S/N > 5) and precision (CV < 20%) criteria of TM-104 §8.2. Sign the SST reference record. No SST is evaluated against values that are not approved. |

### 7.6 Injection sequence and acquisition

At 8 min per injection (Bringans et al. 2020, Targeted (MRM) LC-MS analysis), a full plate with blanks and SST injections takes about 14 to 15 h (derived from the run time and the sequence in TM-104 §7.6.1), which leaves about 9 h of the 24-h limit of TM-104 §7.6.7 for a decision on any re-injection.

| Who | Task |
| :---- | :---- |
| Associate Scientist | 7.6.1 Build the sequence in this order: solvent blank and SST (TM-104 §7.5); PBS blanks (number as in the TM-103 plate map); double blank; calibrator (N = 4); solvent blank (carryover check); reference plasma replicates 1 and 2; samples in plate-map order, with one bracketing SST injection after every 24 sample injections; reference plasma replicates 3 and 4; closing SST injection; closing solvent blank (carryover check). Order, bracketing and closing SST injections, carryover blanks and the split of the reference plasma replicates; positions to be aligned with TM-106. |
| Associate Scientist | 7.6.2 Name each raw data file with the batch ID, the well position and the injection number. |
| Associate Scientist | 7.6.3 Record the autosampler temperature in the batch record before the first injection. |
| Associate Scientist | 7.6.4 Start the sample injections only after the SST sign-off (TM-104 §7.5.4). |
| Associate Scientist | 7.6.5 Check the LC pressure and the SIS signal against the in-run criteria of TM-104 §8.2 at the first sample injection and at least every 2 h. Record each check in the instrument log. |
| Associate Scientist | 7.6.6 Evaluate each bracketing and closing SST injection and each carryover blank against TM-104 §8.2 as soon as it is acquired, and record the values on the SST record. |
| Associate Scientist | 7.6.7 Complete all injections, including any re-injection, within 24 h of placing the plate in the autosampler at 4 °C (TM-104 §7.1.19). Processed extracts are stable for 24 h at 4 °C in the autosampler (N = 86, Bringans et al. 2020, Table 1). |
| Associate Scientist | 7.6.8 If an injection fails (e.g. pressure fault, loss of spray) or any in-run, bracketing, closing SST or carryover criterion of TM-104 §8.2 fails, pause the sequence and follow TM-104 §8.3. |
| Associate Scientist | 7.6.9 Re-inject affected wells only after the disposition "rework" is recorded in the NCR (TM-104 §8.3.5, §8.3.6), and only within the limit of TM-104 §7.6.7. |
| Associate Scientist | 7.6.10 Before resuming, repeat the SST when TM-104 §7.5 requires it. |
| Associate Scientist | 7.6.11 Record the autosampler temperature in the batch record after the last injection. |
| Associate Scientist | 7.6.12 Transfer the raw data files to controlled storage. |
| Associate Scientist | 7.6.13 Record the storage location of the raw data files in the batch record. |
| Associate Scientist | 7.6.14 Put the LC-MS system in standby. |
| Technical Reviewer | 7.6.15 Review the batch record, the SST record and the instrument log. |
| Technical Reviewer | 7.6.16 If the review finds a nonconformity that is not yet recorded, do not release the raw data files and follow TM-104 §8.3. |
| Technical Reviewer | 7.6.17 Release the raw data files to TM-105. |

### 7.7 Immuno-MRM workflow: which SOP owns which stage

Each stage is described in one SOP; other SOPs refer to it by ID and section. This SOP owns LC-MRM acquisition, including system suitability.

| Stage | Owning SOP |
| :---- | :---- |
| Ab-bead conjugation and QC | TM-101 |
| Calibrator, reference plasma and SIS preparation | TM-102 |
| Immunoaffinity capture, washing, and on-bead reduction, alkylation and digestion | TM-103 |
| LC-MRM acquisition, including system suitability | TM-104 |
| Data analysis | TM-105 |
| Batch acceptance and run release | TM-106 |

## 8 Acceptance criteria, nonconformities and records

### 8.1 Quantitative acceptance criteria

The acceptance criteria owned by this SOP are the system suitability, in-run and carryover criteria in TM-104 §8.2. Peak acceptance is owned by TM-105 §7.3 and §8.2. Batch acceptance, including the evaluation of the PBS blanks and the double blank, is owned by TM-106 [section to be cited when TM-106 is drafted].

Calibration-curve criteria do not apply: each batch is calibrated with a single-level calibrator processed in N = 4 replicates (Bringans et al. 2020, Standards and controls; Sample processing).

### 8.2 System suitability, in-run and carryover criteria

The SST criteria must be met before samples are injected. The in-run, bracketing, closing and carryover criteria apply during the sequence. S/N is calculated as in TM-105 §7.3.1, from the Skyline Total Area and Total Background of each peptide. The SST record lists each value and whether it passed.

| Criterion | Limit | Source |
| :---- | :---- | :---- |
| Solvent blank before the SST (system contamination) | No peak at the SIS retention times with a peak area above 1% of the approved reference area (TM-104 §7.5.14) | [ADDED FOR TRAINING] |
| SIS peak detection (SST, bracketing and closing SST, reference-value injections) | Every SIS peptide detected in every injection with S/N > 5 | S/N > 5: Bringans et al. 2020, Data analysis (a peak-integration criterion there); use as an SST criterion [ADDED FOR TRAINING] |
| Retention time (SST, bracketing and closing SST) | Each SIS peptide within ±0.2 min of its approved reference retention time (TM-104 §7.5.14) | [ADDED FOR TRAINING] |
| SIS peak area (SST) | Mean of the 3 SST injections within ±30% of the approved reference area for the SST sample lot in use (TM-104 §5.1, §7.5.14) | [ADDED FOR TRAINING] |
| SIS peak area (bracketing and closing SST) | Each injection within ±30% of the approved reference area for the SST sample lot in use | [ADDED FOR TRAINING] |
| SIS peak-area precision (SST, reference-value injections) | CV < 20% across the 3 SST injections, and across the 6 reference-value injections | < 20% CV: Bringans et al. 2020, Results (FDA bioanalytical guidance for ligand-binding assays, applied there to biomarker concentrations). Use for SIS peak area [ADDED FOR TRAINING] |
| LC pressure at starting conditions (SST) | Within ±10% of the approved reference pressure (TM-104 §7.5.14) | [ADDED FOR TRAINING] |
| LC pressure during the sequence (in-run check, TM-104 §7.6.5) | In the re-equilibration segment (4.5–8.0 min, TM-104 §7.2) of the checked injection, within ±10% of the approved reference pressure; no pressure fault | [ADDED FOR TRAINING] |
| SIS signal during the sequence (in-run check, TM-104 §7.6.5) | Peak area of each SIS peptide in the checked injection at least 50% of the approved reference area | [ADDED FOR TRAINING] |
| Light-peptide carryover (solvent blanks after the calibrator and at the end) | Peak area of each light peptide at most 1% of the mean light peak area of the calibrator replicates of the same batch | [ADDED FOR TRAINING]; no carryover limit is given in the paper |
| PBS blanks and double blank | Acquired under this SOP; evaluated in TM-106 [section to be cited when TM-106 is drafted] | Well types: Bringans et al. 2020, Sample processing |

### 8.3 Nonconforming results (ISO 13485 §8.3)

If an SST, in-run or carryover criterion is not met, an injection fails, or a step cannot be performed as written:

| Who | Task |
| :---- | :---- |
| Associate Scientist | 8.3.1 Stop. Do not inject samples after a failed SST, and do not resume a failed sequence without a disposition recorded in the NCR. |
| Associate Scientist | 8.3.2 Segregate. Keep the plate at 4 °C; if it leaves the autosampler, label it with QMS-003-F02. |
| Associate Scientist | 8.3.3 Mark the affected raw data files "not for analysis" in the batch record. After a failed bracketing or closing SST injection, all injections since the last passing SST injection are affected. |
| Associate Scientist | 8.3.4 Raise an NCR on QMS-003-F01 under QMS-003 §6.1 before any further action on the plate. The time limit of QMS-003 §7.1.1 is the latest permitted. |
| Quality Assurance | 8.3.5 Decide the disposition under QMS-003 §6.3.2. Re-injection is rework (QMS-003 §6.4) and is possible only if the re-injections can be completed within the limit of TM-104 §7.6.7; otherwise decide between re-processing the samples under TM-103 and scrap. |
| Technical Reviewer | 8.3.6 Before re-injection, record the assessment of possible adverse effects of the rework in the NCR (QMS-003 §6.4.2). |
| Quality Assurance | 8.3.7 Decide whether CAPA is needed (QMS-004), applying the triggers of QMS-003 §6.7.1. |

### 8.4 Control of records (ISO 13485 §4.2.5)

Records created: the batch record with the SST record and its sign-off, the injection sequence, the instrument log with the SST reference record, the column log, the verification records of the method files, the raw data files and any NCRs.

Storage: raw data files in controlled electronic storage with access control and audit trail, validated under QMS-006; paper records in the batch binder [ADDED FOR TRAINING].

Retention: for the period set in QMS-002 (Control of records) [section to be cited when QMS-002 is drafted].

## 9 References

| Document / standard | Title and relevant section |
| :---- | :---- |
| ISO 13485:2016 | 4.2.5 Control of records; 6.3 Infrastructure (maintenance); 7.5.1 Control of production and service provision; 7.5.6 Validation of processes for production and service provision; 7.6 Control of monitoring and measuring equipment; 8.3 Control of nonconforming product |
| ISO 14971:2019 | Application of risk management to medical devices (risk management file RMF-001 [ADDED FOR TRAINING]) |
| IVDR (EU) 2017/746 | In vitro diagnostic medical devices regulation |
| QMS-001 | Document control (§6.3 technical review, including the Technical Reviewer role; §6.4 QA approval) |
| QMS-002 | Control of records (retention period) [section to be cited when QMS-002 is drafted] |
| QMS-003 | Control of nonconforming product (§4 definitions; §6.1 identification and segregation; §6.3.2 disposition; §6.4 rework, §6.4.2 adverse-effects assessment; §6.7.1 CAPA triggers; §7.1.1 time limit for raising an NCR) |
| QMS-004 | Corrective and preventive action |
| QMS-005 | Change control |
| QMS-006 | Validation of QMS software (including acquisition software) |
| QMS-008 | Equipment qualification and maintenance [ID proposed; document not yet drafted] |
| QMS-009 | Laboratory safety and waste [ID proposed; document not yet drafted] |
| TM-102 | Calibrator, reference plasma and SIS preparation (SST sample) [section to be cited when TM-102 is drafted] |
| TM-103 | Immunoaffinity capture and digestion (processed plate and plate map) [section to be cited when TM-103 is drafted] |
| TM-105 | Skyline data analysis (§5.1 Skyline document template; §7.2 peak integration; §7.3 S/N check, §7.3.1 S/N calculation; §8.2 data review criteria) |
| TM-106 | Batch acceptance and run release [section to be cited when TM-106 is drafted] |
| Bringans et al. 2020 | Clin Proteomics 2020;17:37. Sections: Reagents; Sample processing; Standards and controls; Targeted (MRM) LC-MS analysis; Data analysis; Inter-laboratory comparisons; Results (< 20% CV from FDA bioanalytical guidance; 4000 versus 5500 QTRAP comparison); Table 1 (extract stability); Additional file 1 (transition settings) |

## 10 Revision history

| Version | Date | Description of change |
| :---- | :---- | :---- |
| 0.1 | 2021-06-01 | First draft. |
| 0.2 | 2021-08-11 | Review round 1 (TR-TM104-v0.1-01 to -22): SST sample defined with amount on column, solvent and shelf life (§5.1); method files TM-104-M01 and -M02 under change control (§5.2); time zero and governing table for the LC method, interpretations marked [ADDED FOR TRAINING] (§7.2); peptide sequences, transitions summed, no quantifier or qualifier (§7.4); SST reference values with triggers and approval (§7.5); bracketing and closing SST, split reference plasma, carryover blanks, in-run pressure and SIS-signal criteria (§7.6, §8.2); NCR, disposition and re-injection order within the 24-h limit (§7.6, §8.3); one action per step; autosampler temperature records; CV source corrected to Results; references by ID and section; QMS-002 for retention; ISO 13485 §6.3; definitions and abbreviations. TR-TM104-v0.1-02, -06, -07, -12 and -13 stay open until Additional file 1 is available and TM-102, TM-103, TM-106, QMS-002, QMS-008 and QMS-009 are drafted; -22 is deferred to a later version through QMS-001-F01. |
| 0.3 | 2021-10-07 | Review round 2: transition table with Q1 and Q3 m/z, dwell time, DP and CE from Bringans et al. 2020, Additional file 1, and C\* notation for carbamidomethylated Cys (§7.4); SST procedure split into pass, fail and reference-value blocks with one role per step, NCR disposition by Quality Assurance, and [ADDED FOR TRAINING] markers restored (§7.5); links to the reference-value steps renumbered to §7.5.12 to §7.5.15 (§4, §5.1, §7.1, §7.5, §8.2); version 0.3 in the page header and §12. |
| 1.0 | 2022-01-20 | Approved for release; no content change from 0.3. |

## 11 Approval

[Signatures are captured in the electronic QMS. ADDED FOR TRAINING]

| Role | Name | Signature | Date |
| :---- | :---- | :---- | :---- |
| Author | Dr. LC Proton, Associate Scientist | [Electronic signature] | 2021-11-11 |
| Technical Reviewer | Mira Armstrong, Technical Reviewer | [Electronic signature] | 2021-12-10 |
| Quality Assurance | Tess Lindqvist, Quality Assurance | [Electronic signature] | 2022-01-20 |

## 12 Document metadata

| Field | Value |
| :---- | :---- |
| **Document ID** | TM-104 |
| **Doc Type** | Method SOP |
| **Title** | Microflow MRM LC-MS acquisition |
| **Manufacturer** | Positive Climb Diagnostics |
| **Assay** | 3-plex immuno-MRM DKD assay |
| **Source** | Bringans et al. 2020, CC BY 4.0 |
| **Version** | 1.0 |
| **Status** | Effective |
| **Approval date** | 2022-01-20 |
| **Effective date** | 2022-02-03 |
| **Supersedes** | none |
| **Superseded by** | none |
| **ISO 13485 clause(s)** | 4.2.5, 6.3, 7.5.1, 7.5.6, 7.6, 8.3 |
| **Author** | Dr. LC Proton, Associate Scientist |
| **Reviewer** | Mira Armstrong, Technical Reviewer |
| **Approver** | Tess Lindqvist, Quality Assurance |
| **Training case** | True |
