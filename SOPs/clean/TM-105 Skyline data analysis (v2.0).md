---
doc_id: "TM-105"
doc_type: "Method SOP"
title: "Skyline data analysis"
manufacturer: "Positive Climb Diagnostics"
assay: "3-plex immuno-MRM DKD assay"
source: "Bringans et al. 2020, CC BY 4.0"
version: "2.0"
status: "Effective"
approval_date: 2026-10-16
effective_date: 2026-10-30
supersedes: "TM-105 v1.0"
superseded_by: null
iso_clause: ["4.1.6", "4.2.5", "7.5.1", "7.5.6", "8.3"]
author: "Dr. LC Proton, Associate Scientist"
reviewer: "Mira Armstrong, Technical Reviewer"
approver: "Tess Lindqvist, Quality Assurance"
training_case: true
---

# TM-105: Skyline data analysis

**Positive Climb Diagnostics · Standard Operating Procedure**

*Flying Peptides training case · Fictitious manufacturer: Positive Climb Diagnostics · Not a real company, product or QMS.*

*Adapted from: Bringans S, Ito J, Casey T, et al. "A robust multiplex immunoaffinity mass spectrometry assay (PromarkerD) for clinical prediction of diabetic kidney disease." Clin Proteomics 2020;17:37. doi:10.1186/s12014-020-09302-w. Licensed under CC BY 4.0 ([https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)). The methods were restructured and rewritten as controlled procedures for a fictitious company; procedural detail was added for training purposes. The authors, Proteomics International and Atturos do not endorse this document.*

*Names and roles are illustrative (training case); all roles were performed by Dr. Ebbie. Drafted with AI assistance; reviewed and approved by Dr. Ebbie.*

## 1 Purpose

This procedure defines how the raw data files of one batch of the 3-plex immuno-MRM DKD assay are analysed in Skyline v26.1 to give a peak area for each target (light) peptide and its SIS (heavy) peptide, and how the concentrations of APOA4, CD5L and IBP3 are calculated in Skyline from the single-level calibrator, so that data analysis runs as a controlled production process (ISO 13485 §7.5.1, §7.5.6). The calibrator is defined in Bringans et al. 2020, Standards and controls; the calculation principle is from Bringans et al. 2020, Data analysis.

## 2 Scope

### 2.1 Applicability

Data analysis of one batch (one 96-well plate) acquired under TM-104: check of the Skyline version, import of the raw data files into Skyline v26.1, peak integration and review, signal-to-noise (S/N) check, calculation of the protein concentrations, second-person review and release of the results to TM-106.

### 2.2 Qualifications and training

Associate Scientists with documented training on TM-105 and on Skyline v26.1. Training must be recorded before the first independent analysis. An Associate Scientist without recorded training does not analyse batches under this SOP until the training is recorded. The Technical Reviewer of a batch is not the Associate Scientist who analysed it.

### 2.3 Exclusions

Acquisition of the raw data (TM-104); batch acceptance, including the evaluation of the reference plasma, the PBS blanks and the double blank, and run release (TM-106); calculation of a clinical risk score; validation of Skyline and of the calculation worksheet (QMS-006).

### 2.4 Transition from TM-105 v1.0

TM-105 v1.0 and TM-105 v2.0 use different Skyline versions (TM-105 §8.2). Each batch is analysed under one TM-105 version from start to end. The comparison of results between the two Skyline versions is part of validation report VR-TM105-01, not of this SOP.

2.4.1 A batch whose analysis under TM-105 v1.0 is not complete on the effective date of TM-105 v2.0 is analysed again from TM-105 §7.1.1 under v2.0, because v1.0 is then Superseded (QMS-001 §7.1.1).

2.4.2 Rework of a batch analysed under TM-105 v1.0 starts again from its raw data files, in a new Skyline document created from TM-105-T01 (TM-105 §7.1.5). The stored v1.0 Skyline document is not opened in the new Skyline version or saved again (QMS-003 §6.4.1; ISO 13485 §4.2.5).

2.4.3 Training on TM-105 v1.0 does not qualify an Associate Scientist or Technical Reviewer for v2.0. Training on v2.0 is recorded before first use (QMS-001 §6.5.3). [ADDED FOR TRAINING]

## 3 Responsibilities

| Role | Responsibility |
| :---- | :---- |
| Associate Scientist | Records and checks the Skyline version, imports the raw data, integrates and reviews the peaks, performs the S/N check, assigns the sample types, exports the concentrations calculated by Skyline, and stops and raises an NCR when a check fails. |
| Technical Reviewer | Signs off the S/N check, performs the second-person review of the audit log, integrations, sample types and calculations, re-verifies reworked results and releases the results to TM-106. |
| Quality Assurance | Decides the disposition of nonconforming results (QMS-003 §6.3.2), decides on CAPA (QMS-004), and approves changes to the Skyline version, the Skyline document template or the calculation worksheet (QMS-005, QMS-006). |

## 4 Definitions and abbreviations

### 4.1 General terms and abbreviations (ISO 13485 / ISO 9000)

| Term | Definition |
| :---- | :---- |
| APOA4 | Apolipoprotein A4 |
| Batch / lot | A defined quantity of material or product processed in one process or series of processes. For this assay, one 96-well plate is one batch. |
| CAPA | Corrective and preventive action, managed under QMS-004. |
| CD5L | CD5 antigen-like |
| Critical control point | A step where a check must pass and be signed off before the procedure continues. |
| CV | Coefficient of variation |
| Disposition | The decision on suspected nonconforming product: no nonconformity confirmed, rework, use under concession, scrap or return to supplier (QMS-003 §4). |
| DKD | Diabetic kidney disease |
| FDA | U.S. Food and Drug Administration |
| IBP3 | Insulin-like growth factor-binding protein 3 |
| ID | Identifier (e.g. batch ID, document ID) |
| ISO | International Organization for Standardization |
| IT | Information technology |
| IVDR | In Vitro Diagnostic Medical Devices Regulation (EU) 2017/746 |
| LC-MRM | Liquid chromatography with MRM detection on a triple quadrupole mass spectrometer (TM-104 §1) |
| *m/z* | Mass-to-charge ratio |
| NCR | Nonconformity record (QMS-003-F01) |
| Nonconforming product | Material, reagent, assay run or result that does not meet its specified requirements (QMS-003 §4). |
| Nonconformity | Non-fulfilment of a specified requirement. |
| PBS | Phosphate buffered saline |
| QC | Quality control |
| QMS | Quality management system |
| Quarantine | Status that prevents use or release of product until a disposition is decided (QMS-003 §4). |
| Rework | Action on nonconforming product to make it conform to its requirements, followed by re-verification (QMS-003 §4). In this SOP: re-integration or re-calculation of the data of the same batch (TM-105 §8.3.7). |
| RMF | Risk management file (ISO 14971), here RMF-001 |
| S/N | Signal-to-noise ratio |
| SOP | Standard operating procedure |
| SST | System suitability test (TM-104 §7.5) |
| Technical Reviewer | Role with technical review authority. Under QMS-001 §6.3 it reviews controlled documents; in this SOP it acts as batch data reviewer: it signs off the S/N check, performs the second-person review and releases the results to TM-106 [ADDED FOR TRAINING]. |

### 4.2 Immuno-MRM terms (method SOPs only)

| Term | Definition |
| :---- | :---- |
| Ab-beads | Magnetic beads conjugated with the capture antibodies for the target proteins (Bringans et al. 2020, Bead-antibody production). |
| Audit log | The Skyline record of every change made to a Skyline document, with the user, the time and, for a manual integration, the mandatory reason (TM-105 §7.2.6). It is kept in its own file of the Skyline document (TM-105 §8.4). |
| Calculated Concentration | Skyline result for the concentration of one protein in one injection, calculated from its peak area ratio and the calibrator with the quantification settings of TM-105 §7.4. |
| Calibrator | Recombinant target proteins at known concentrations, processed alongside samples to convert signal into concentration. |
| Candidate Peaks view | Skyline view that lists the alternative peaks of a peptide in one injection with their scores (TM-105 §7.2 manual integration table). |
| Double blank | Well with 200 µL PBS and no Ab-beads, processed in TM-103 (Bringans et al. 2020, Sample processing). |
| Light / heavy peptide | Endogenous (unlabelled) target peptide / its 13C15N-labelled SIS peptide. |
| Manual integration | A change of the peak boundaries set by Skyline, made by the Associate Scientist under TM-105 §7.2 and recorded in the audit log. |
| MRM | Multiple reaction monitoring: targeted measurement of defined precursor-to-product ion pairs on a triple quadrupole mass spectrometer. |
| PBS blank | Well with 50 µL PBS in place of a sample, processed with Ab-beads in TM-103 (Bringans et al. 2020, Sample processing). |
| Peak area | Integrated signal of one peptide's chromatographic peak: the sum of the areas of all its transitions (Skyline Total Area; TM-105 §7.2). |
| Peak area ratio | Light peak area divided by heavy (SIS) peak area for the same protein in the same injection (Bringans et al. 2020, Data analysis). |
| Reference plasma | Pooled plasma processed in every batch to monitor assay performance (QC). |
| Retention time | Time from injection to the apex of a peptide's chromatographic peak. |
| Sample type | Skyline property of an injection that sets its role in the calculation: Standard, Quality Control, Unknown, Blank or Double Blank (TM-105 §7.4). |
| SIS | Stable isotope-labelled internal standard: a synthetic heavy-isotope peptide used to normalise signal across samples. |
| Skyline document | The Skyline file that holds the target list, the integration and quantification settings, the imported raw data, the integration results and the audit log of one batch. |
| Total Area / Total Background | Skyline values for the integrated peak area and the background under the peak, used for the S/N check (Bringans et al. 2020, Data analysis). |
| Transition | One precursor-to-product ion *m/z* pair. All transitions of a peptide are summed into its peak area; no transition is designated quantifier or qualifier (TM-104 §7.4). |
| Truncated peak | A light or heavy peak whose integration boundaries cut off part of its chromatographic signal, as flagged by Skyline (TM-105 §7.2 integration settings table). |

## 5 Data inputs, software and equipment

### 5.1 Data inputs

| Input | Source | Control |
| :---- | :---- | :---- |
| Raw data files of one batch | Transferred to controlled storage under TM-104 §7.6.12 | Released by the Technical Reviewer (TM-104 §7.6.17) |
| Skyline document template TM-105-T01 (peptides, SIS peptides, transitions, integration and quantification settings, report definitions, audit logging on) | Peptides and transitions: TM-104 §7.4 (Bringans et al. 2020, Reagents; Additional file 1). Integration settings: TM-105 §7.2. Quantification settings: TM-105 §7.4. Report definitions: TM-105 §7.2.8, §7.4.6 | Controlled template, ID TM-105-T01 [ADDED FOR TRAINING]; changed only under QMS-005 |
| Calibrator concentrations | TM-102 [section to be cited when TM-102 is drafted]; Bringans et al. 2020, Standards and controls | Effective plasma concentrations: APOA4 91.5 µg/mL, CD5L 3.45 µg/mL, IBP3 0.892 µg/mL; entered in TM-105-T01 as the analyte concentration of the calibrator |
| Plate map and batch record | TM-103 ; TM-104 §7.1.15 | Sample identity, well types and well positions; source of the sample types (TM-105 §7.4.1) |

The calibrator concentrations are those of Bringans et al. 2020, Standards and controls, and are stated only in this table. The IDs of the Skyline document template (TM-105-T01) and the calculation worksheet (TM-105-T02) are [ADDED FOR TRAINING].

### 5.2 Software and equipment

| Software / equipment | Version / manufacturer | Minimum specification | Validation / check |
| :---- | :---- | :---- | :---- |
| Skyline | Version 26.1, MacCoss Lab Software, University of Washington, Seattle, USA; exact version string in TM-105 §8.2 | Imports the raw data files of TM-104; reports peak areas, Total Area, Total Background and Ratio to heavy; calculates concentrations; keeps an audit log | Validated for its intended use in validation report VR-TM105-01 (QMS-006; ISO 13485 §4.1.6) [ID ADDED FOR TRAINING]. Version recorded and checked before use (TM-105 §7.1.3, §7.1.4). |
| Calculation worksheet TM-105-T02 | Controlled worksheet [ID ADDED FOR TRAINING] | Calculates S/N and the CV of the calibrator peak area ratios (TM-105 §7.3.1, §7.4.3) | Validated for its intended use in validation report VR-TM105-01 (QMS-006) [ADDED FOR TRAINING]; changed only under QMS-005 |
| Workstation | [Model] [ADDED FOR TRAINING] | Meets the system requirements of the validated Skyline version; access-controlled user accounts | Configuration recorded in validation report VR-TM105-01 (QMS-006) [ADDED FOR TRAINING] |

This SOP uses Skyline v26.1, introduced by change request CR-TM105-01 (QMS-001-F01; QMS-005) [ID ADDED FOR TRAINING]. Skyline v26.1 and the calculation worksheet TM-105-T02 are validated in validation report VR-TM105-01 (QMS-006). This version of TM-105 became effective only after VR-TM105-01 was approved. A different Skyline version may be used only after validation under QMS-006 and a change of this SOP under QMS-005.

## 6 Safety and environmental controls

Not applicable: this procedure is performed at a computer workstation and involves no samples, chemicals or instruments. Access to raw data and Skyline documents follows the IT access rules of the electronic QMS [ADDED FOR TRAINING].

## 7 Procedure

### 7.1 Preparation

| Who | Task |
| :---- | :---- |
| Associate Scientist | 7.1.1 Check that the Technical Reviewer has released the raw data files of the batch (TM-104 §7.6.17). |
| Associate Scientist | 7.1.2 Check that the batch record shows the signed-off SST (TM-104 §7.5.4). |
| Associate Scientist | 7.1.3 Record the full Skyline version string shown in Help > About in the batch record. |
| Associate Scientist | 7.1.4 Check that the recorded version string equals the validated version string in TM-105 §8.2. |
| Associate Scientist | 7.1.5 Open the Skyline document template TM-105-T01 (TM-105 §5.1) and save it under the batch ID. |
| Associate Scientist | 7.1.6 Check that audit logging is on in the batch Skyline document (TM-105 §7.2 integration settings table). |
| Associate Scientist | 7.1.7 If a check in TM-105 §7.1.1, §7.1.2, §7.1.4 or §7.1.6 fails, stop, do not analyse the data, and follow TM-105 §8.3. |

### 7.2 Import and peak integration

Integration settings table: the Skyline document template TM-105-T01 holds the integration and audit log settings in this table.

| Parameter | Setting | Source |
| :---- | :---- | :---- |
| Peak area of a peptide | Sum of the areas of all transitions of the peptide (Skyline Total Area); no quantifier or qualifier transition | TM-104 §7.4 [ADDED FOR TRAINING] |
| Transitions | As held in the MRM method file TM-104-M01 (TM-104 §7.4) | Bringans et al. 2020, Additional file 1 |
| Peak picking | Skyline default peak picking | [ADDED FOR TRAINING] |
| Peak boundaries | The same boundaries for the light and heavy peptide of one protein in one injection | [ADDED FOR TRAINING] |
| Background | Skyline Total Background under the integrated peak | Bringans et al. 2020, Data analysis |
| Peak truncation | Skyline Truncated flag: [measured quantity, threshold and unit to be taken from EXT-SKY-2601 and VR-TM105-01]; fixed in TM-105-T01 or confirmed in VR-TM105-01 not to be user-variable | EXT-SKY-2601; VR-TM105-01 [ADDED FOR TRAINING] |
| Audit log | Audit logging on for the whole life of the batch Skyline document; Detailed Info report with user name and Skyline version | EXT-SKY-2601 [ADDED FOR TRAINING] |

Steps for import, integration and peak review:

| Who | Task |
| :---- | :---- |
| Associate Scientist | 7.2.1 Import all raw data files of the batch into the Skyline document (File > Import > Results). |
| Associate Scientist | 7.2.2 Let Skyline integrate the light and heavy peptide peaks with the settings of TM-105 §7.2, giving one peak area per peptide (Bringans et al. 2020, Data analysis). |
| Associate Scientist | 7.2.3 Check that the apex retention times of the light and heavy peptide of each protein meet the co-elution limit in TM-105 §8.2. |
| Associate Scientist | 7.2.4 Check that every light and heavy peak meets the peak truncation criterion in TM-105 §8.2, so that the boundaries include the whole peak. |
| Associate Scientist | 7.2.5 If a peak fails TM-105 §7.2.3 or §7.2.4, adjust its boundaries only under a condition in the manual integration table of TM-105 §7.2. |
| Associate Scientist | 7.2.6 Enter the permitted condition from the manual integration table of TM-105 §7.2 as the reason for each manual integration in the Skyline audit log. The reason is mandatory. |
| Associate Scientist | 7.2.7 If no permitted condition applies, or the co-elution limit is still not met, do not adjust the peak; follow TM-105 §8.3. |
| Associate Scientist | 7.2.8 Export a peak report with the report definition held in TM-105-T01: Total Area and Total Background of every light and heavy peptide and Ratio to heavy of every protein, in every injection (Bringans et al. 2020, Data analysis). |

Manual integration table: manual integration is permitted only under these conditions [ADDED FOR TRAINING].

| Condition | Permitted adjustment |
| :---- | :---- |
| Skyline selected a peak at which the light and heavy apexes differ by more than the co-elution limit in TM-105 §8.2 | Move the boundaries to the peak at which the light and heavy apexes co-elute, selected in the Skyline Candidate Peaks view, if there is one. |
| Skyline flags the peak as truncated (TM-105 §7.2.4) | Widen the boundaries to include the whole peak. |
| The boundaries include a neighbouring peak | Narrow the boundaries to the peak of the peptide. |
| Any other case, including an adjustment made only to meet an S/N, CV or concentration criterion | Not permitted. |

### 7.3 Signal-to-noise check [CRITICAL CONTROL POINT]

Bringans et al. 2020 (Data analysis) accept peaks on S/N calculated from the Total Area and Total Background values provided by Skyline. The S/N limit for each well type and peak is stated in TM-105 §8.2. PBS blank and double-blank wells contain no plasma (Bringans et al. 2020, Sample processing), so no light peptide is expected in them; the S/N limit is not applied to them, and TM-106 evaluates them [section to be cited when TM-106 is drafted].

| Who | Task |
| :---- | :---- |
| Associate Scientist | 7.3.1 Calculate S/N for every light and heavy peak in every well as Total Area ÷ Total Background in the calculation worksheet TM-105-T02. |
| Associate Scientist | 7.3.2 Compare the S/N of each calibrator, reference plasma and sample peak with the S/N limit for its well type in TM-105 §8.2. |
| Associate Scientist | 7.3.3 If a light or heavy peak of a calibrator or reference plasma well fails the S/N limit, stop the analysis of the batch and follow TM-105 §8.3. |
| Associate Scientist | 7.3.4 If the heavy (SIS) peak of a sample fails the S/N limit, mark that protein result of the sample "invalid – SIS failure". |
| Associate Scientist | 7.3.5 For each result marked "invalid – SIS failure", follow TM-105 §8.3 as a sample-level nonconformity. |
| Associate Scientist | 7.3.6 If the light peak of a sample fails the S/N limit and its heavy peak passes, report that protein result as "not quantifiable" [ADDED FOR TRAINING]. This is a valid result, not a nonconformity. |
| Associate Scientist | 7.3.7 Record the S/N values of the PBS blank and double-blank wells for TM-106, without applying the S/N limit. |
| Technical Reviewer | 7.3.8 [CRITICAL CONTROL POINT] Verify and sign off the S/N check. Concentrations are exported only after this sign-off. |

### 7.4 Concentration calculation

The SIS peptide normalises the signal across samples, and the calibrator replicates provide the concentrations (Bringans et al. 2020, Data analysis). Skyline calculates the concentrations with the quantification settings held in the Skyline document template TM-105-T01 (quantification settings table, TM-105 §7.4); the calibrator concentrations are those in TM-105 §5.1 (Bringans et al. 2020, Standards and controls). The paper gives no formula; the single-point calculation through the origin is derived from Bringans et al. 2020, Data analysis [ADDED FOR TRAINING]. The quantification ranges in the quantification range table are from Bringans et al. 2020, Results; their use for reporting in TM-105 §7.4.8 and §7.4.9 is [ADDED FOR TRAINING].

Quantification settings table: the Skyline document template TM-105-T01 holds these settings; they are not changed for a batch.

| Parameter | Setting | Source |
| :---- | :---- | :---- |
| Normalization method | Ratio to heavy: light peak area ÷ heavy (SIS) peak area | Bringans et al. 2020, Data analysis |
| Regression fit | Linear through zero | Derived from Bringans et al. 2020, Data analysis [ADDED FOR TRAINING] |
| Regression weighting | None | [ADDED FOR TRAINING] |
| MS level | Fragment ions: all transitions of the peptide (TM-105 §7.2) | TM-104 §7.4 [ADDED FOR TRAINING] |
| Calibrator | Calibrator replicates (N = 4) with sample type Standard; analyte concentration as in TM-105 §5.1 | Bringans et al. 2020, Standards and controls; Sample processing |
| Excluded calibrator replicates | None permitted; an excluded replicate is a batch-level nonconformity (TM-105 §8.2, §8.3.1) | [ADDED FOR TRAINING] |
| Units | µg/mL | Bringans et al. 2020, Standards and controls |
| Limits of detection and quantification (Skyline figures of merit) | Not used; the reporting limits are the quantification ranges in the quantification range table of TM-105 §7.4 | [ADDED FOR TRAINING] |
| Sample types | Calibrator: Standard; reference plasma: Quality Control; sample: Unknown; PBS blank: Blank; double blank: Double Blank | Well types: Bringans et al. 2020, Sample processing; Skyline mapping [ADDED FOR TRAINING] |
| Other settings that affect Calculated Concentration | As held in TM-105-T01 and listed in VR-TM105-01 | VR-TM105-01 [ADDED FOR TRAINING] |

Quantification range table:

| Protein | Quantification range in plasma | Source |
| :---- | :---- | :---- |
| APOA4 | 37.5 to 200 µg/mL | Bringans et al. 2020, Results |
| CD5L | 0.104 to 10.0 µg/mL | Bringans et al. 2020, Results |
| IBP3 | 0.0104 to 1.00 µg/mL | Bringans et al. 2020, Results |

Steps for the concentration calculation:

| Who | Task |
| :---- | :---- |
| Associate Scientist | 7.4.1 Set the sample type of each injection in the Skyline document from the plate map (TM-105 §5.1), as listed in the quantification settings table of TM-105 §7.4. |
| Associate Scientist | 7.4.2 Check that the analyte concentration of each calibrator replicate (N = 4) in the Skyline document equals the calibrator concentration in TM-105 §5.1. |
| Associate Scientist | 7.4.3 For each protein, calculate the CV of the calibrator Ratio to heavy values from the peak report (TM-105 §7.2.8) in the calculation worksheet TM-105-T02. |
| Associate Scientist | 7.4.4 If a CV fails the precision limit in TM-105 §8.2, stop the analysis of the batch and follow TM-105 §8.3. |
| Associate Scientist | 7.4.5 Let Skyline calculate the concentration (Calculated Concentration, µg/mL) of each sample and reference plasma replicate. With one calibrator level, all N = 4 replicates included and a fit through zero, this equals (peak area ratio ÷ mean calibrator peak area ratio) × calibrator concentration. Derived from Bringans et al. 2020, Data analysis [ADDED FOR TRAINING]. |
| Associate Scientist | 7.4.6 Export a quantification report with the report definition held in TM-105-T01, giving the Calculated Concentration of every sample and reference plasma replicate (N = 4); the reference plasma results are for batch acceptance under TM-106. |
| Associate Scientist | 7.4.7 Report each concentration in µg/mL to 3 significant figures, the precision of the calibrator concentrations (Bringans et al. 2020, Standards and controls) [ADDED FOR TRAINING]. |
| Associate Scientist | 7.4.8 Report a sample concentration below the lower limit of its quantification range (TM-105 §7.4) as "< [lower limit] µg/mL" [ADDED FOR TRAINING]. |
| Associate Scientist | 7.4.9 Report a sample concentration above the upper limit of its quantification range (TM-105 §7.4) as "> [upper limit] µg/mL" [ADDED FOR TRAINING]. |

### 7.5 Review and release

| Who | Task |
| :---- | :---- |
| Technical Reviewer | 7.5.1 Review the Skyline document, the peak report and the quantification report of the batch. |
| Technical Reviewer | 7.5.2 Verify that the audit log covers the batch Skyline document without a gap, from its creation from TM-105-T01 (TM-105 §7.1.5) to the export of the quantification report (TM-105 §7.4.6), with audit logging on throughout. |
| Technical Reviewer | 7.5.3 Verify that Skyline opens the batch Skyline document with its audit log and reports no audit log integrity error [ADDED FOR TRAINING]. |
| Technical Reviewer | 7.5.4 Verify that every manual integration in the audit log Detailed Info report has a reason that is a permitted condition in the manual integration table of TM-105 §7.2. |
| Technical Reviewer | 7.5.5 Verify the S/N calculations in the calculation worksheet TM-105-T02 (TM-105 §7.3). |
| Technical Reviewer | 7.5.6 Verify the CV calculations in the calculation worksheet TM-105-T02 (TM-105 §7.4.3). |
| Technical Reviewer | 7.5.7 Verify the quantification settings of the batch Skyline document against the quantification settings table of TM-105 §7.4. |
| Technical Reviewer | 7.5.8 Verify the sample type of every injection in the batch Skyline document against the plate map (TM-105 §5.1). |
| Technical Reviewer | 7.5.9 Verify that all calibrator replicates (N = 4) are included in the Skyline calibration. |
| Technical Reviewer | 7.5.10 Confirm that the Skyline version string in the audit log Detailed Info report equals the batch record entry (TM-105 §7.1.3) and the validated version string in TM-105 §8.2. |
| Technical Reviewer | 7.5.11 Record the second-person review in the batch record. |
| Technical Reviewer | 7.5.12 If the review finds a nonconformity that is not yet recorded, do not release the results and follow TM-105 §8.3. |
| Technical Reviewer | 7.5.13 Release the results to TM-106 for batch acceptance. Results withheld under TM-105 §8.3.2 are not released. |
| Associate Scientist | 7.5.14 Save the records listed in TM-105 §8.4 in controlled storage, with the Skyline document saved as one Skyline archive (File > Share, complete) [ADDED FOR TRAINING]. |

### 7.6 Immuno-MRM workflow: which SOP owns which stage

Each stage is described in one SOP; other SOPs refer to it by ID and section. This SOP owns data analysis.

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

The acceptance criteria owned by this SOP are the data review criteria in TM-105 §8.2. Batch acceptance, including the evaluation of the reference plasma, the PBS blanks and the double blank, is owned by TM-106 [section to be cited when TM-106 is drafted].

Calibration-curve criteria do not apply: each batch is calibrated with a single-level calibrator processed in N = 4 replicates (Bringans et al. 2020, Standards and controls; Sample processing).

### 8.2 Data review criteria

S/N is calculated as in TM-105 §7.3.1. A batch-level criterion that is not met makes the batch nonconforming (TM-105 §8.3.1). A sample-level criterion that is not met affects only that protein result of that sample (TM-105 §8.3.2). All batch-level criteria must be met before results are released to TM-106.

| Criterion | Limit | Source |
| :---- | :---- | :---- |
| Skyline version (batch level) | Full version string [26.1.x.x, to be copied from VR-TM105-01], as shown in Help > About and in the audit log Detailed Info report; every part of the string must match | Change request CR-TM105-01; validation report VR-TM105-01 [ADDED FOR TRAINING] |
| S/N of light and heavy peaks, calibrator and reference plasma wells (batch level) | > 5 | Bringans et al. 2020, Data analysis; application per well type [ADDED FOR TRAINING] |
| S/N of the heavy (SIS) peak, sample wells (sample level) | > 5; otherwise the result is invalid (TM-105 §7.3.4) | Bringans et al. 2020, Data analysis; outcome [ADDED FOR TRAINING] |
| S/N of the light peak, sample wells (sample level) | > 5 for a quantitative result; otherwise reported as "not quantifiable" (TM-105 §7.3.6) | Bringans et al. 2020, Data analysis; outcome [ADDED FOR TRAINING] |
| S/N, co-elution and peak truncation, PBS blank and double-blank wells | Not applied in this SOP; evaluated in TM-106 | Well types: Bringans et al. 2020, Sample processing |
| Co-elution of light and heavy peptide (batch level for calibrator and reference plasma wells; sample level for sample wells) | Apex retention times differ by no more than 0.05 min | [ADDED FOR TRAINING] |
| Peak truncation, light and heavy peaks (batch level for calibrator and reference plasma wells; sample level for sample wells) | Not flagged as truncated by Skyline after review (TM-105 §7.2.4), with the threshold in the integration settings table of TM-105 §7.2 | EXT-SKY-2601; VR-TM105-01 [ADDED FOR TRAINING] |
| Calibrator peak area ratio precision (batch level) | CV < 20% across the calibrator replicates (N = 4), per protein | FDA Bioanalytical Method Validation guidance (2018), as cited in Bringans et al. 2020, Results |
| Manual integrations (batch level) | Only under the conditions in TM-105 §7.2; each one recorded in the audit log with its condition as the mandatory reason and verified by the Technical Reviewer | [ADDED FOR TRAINING] |
| Audit log (batch level) | Complete and intact for the whole batch Skyline document, with audit logging on throughout (TM-105 §7.5.2, §7.5.3) | [ADDED FOR TRAINING] |
| Sample types (batch level) | Match the plate map for every injection (TM-105 §7.5.8) | [ADDED FOR TRAINING] |
| Calibrator replicates in the calibration (batch level) | All N = 4 included; none excluded (TM-105 §7.5.9) | [ADDED FOR TRAINING] |

### 8.3 Nonconforming results (ISO 13485 §8.3)

If a criterion in TM-105 §8.2 is not met, or a step cannot be performed as written:

| Who | Task |
| :---- | :---- |
| Associate Scientist | 8.3.1 Batch-level nonconformity: stop the analysis of the batch and do not release its results to TM-106. |
| Associate Scientist | 8.3.2 Sample-level nonconformity: withhold the affected protein result of that sample from release; the analysis of the batch continues. |
| Associate Scientist | 8.3.3 Set the status of the affected results to Quarantine in the electronic QMS (QMS-003 §6.1.2). |
| Associate Scientist | 8.3.4 Raise an NCR on QMS-003-F01 under QMS-003 §6.1. The time limit of QMS-003 §7.1.1 is the latest permitted. |
| Quality Assurance | 8.3.5 Decide the disposition under QMS-003 §6.3.2. |
| Technical Reviewer | 8.3.6 Before any rework, assess its possible adverse effects and record the assessment in the NCR (QMS-003 §6.4.2). |
| Associate Scientist | 8.3.7 Re-integrate or re-calculate only after the disposition "rework" is recorded in the NCR, following TM-105 §7.2 to §7.4 (QMS-003 §6.4.1). Rework of a batch analysed under TM-105 v1.0 follows TM-105 §2.4. |
| Technical Reviewer | 8.3.8 Re-verify the reworked results against TM-105 §8.2 and record the result in the NCR (QMS-003 §6.4.3). |
| Quality Assurance | 8.3.9 Decide any re-injection under TM-104 §8.3.5; it is carried out under TM-104 §7.6.9, within the limit of TM-104 §7.6.7. |
| Quality Assurance | 8.3.10 Treat all results analysed with a Skyline version string other than the one validated for the TM-105 version in force (TM-105 §2.4, §8.2) as nonconforming product (QMS-003 §6.1). |
| Quality Assurance | 8.3.11 Decide whether CAPA is needed (QMS-004), applying the triggers of QMS-003 §6.7.1. |

### 8.4 Control of records (ISO 13485 §4.2.5)

Records created: the Skyline version entry in the batch record (TM-105 §7.1.3), the Skyline archive of the batch (File > Share, complete), which keeps the Skyline document, its audit log file and its results file together [ADDED FOR TRAINING]; the audit log Detailed Info report; the exported peak report; the quantification report; the calculation worksheet; the S/N sign-off; the second-person review; and any NCRs.

* **Storage**: electronic records in controlled storage with access control and audit trail, validated under QMS-006.
* **Retention**: for the period set in QMS-002 (Control of records).

## 9 References

| Document / standard | Title and relevant section |
| :---- | :---- |
| ISO 13485:2016 | 4.1.6 Validation of software used in the QMS; 4.2.5 Control of records; 7.5.1 Control of production and service provision; 7.5.6 Validation of processes for production and service provision; 8.3 Control of nonconforming product |
| ISO 14971:2019 | Application of risk management to medical devices (risk management file RMF-001 [ADDED FOR TRAINING]) |
| IVDR (EU) 2017/746 | In vitro diagnostic medical devices regulation |
| QMS-001 | Document control (§6.3 technical review, including the Technical Reviewer role; §6.4 QA approval; §6.5.1 effective date; §6.5.3 training before use; §6.8.1 external documents; §7.1.1 use of Effective versions only) |
| QMS-002 | Control of records (retention period) [section to be cited when QMS-002 is drafted] |
| QMS-003 | Control of nonconforming product (§4 definitions; §6.1 identification and segregation, §6.1.2 Quarantine status; §6.3.2 disposition; §6.4.1 rework procedure, §6.4.2 adverse-effects assessment, §6.4.3 re-verification; §6.7.1 CAPA triggers; §7.1.1 time limit for raising an NCR) |
| QMS-004 | Corrective and preventive action |
| QMS-005 | Change control (change request CR-TM105-01) [ID ADDED FOR TRAINING] |
| QMS-006 | Validation of QMS software (validation report VR-TM105-01 for Skyline v26.1 and the calculation worksheet TM-105-T02) [ID ADDED FOR TRAINING] |
| TM-101 | Ab-bead conjugation and QC |
| TM-102 | Calibrator, reference plasma and SIS preparation (calibrator concentrations) [section to be cited when TM-102 is drafted] |
| TM-103 | Immunoaffinity capture and digestion (plate map; PBS blanks and double blank) [section to be cited when TM-103 is drafted] |
| TM-104 | Microflow MRM LC-MS acquisition (§1 LC-MRM; §7.1.15 plate map; §7.4 transitions; §7.5 SST, §7.5.4 SST sign-off; §7.6.7 time limit; §7.6.9 re-injection; §7.6.12 transfer and §7.6.17 release of raw data files; §8.3.5 disposition of re-injection) |
| TM-106 | Batch acceptance and run release [section to be cited when TM-106 is drafted] |
| Skyline v26.1 | MacCoss Lab Software, University of Washington, Seattle, USA. Release notes held as controlled external document EXT-SKY-2601 in the document register (QMS-001 §6.8.1); the feature claims in this SOP are confirmed against that copy [ID ADDED FOR TRAINING] |
| FDA guidance | Bioanalytical Method Validation, Guidance for Industry (2018), as cited in Bringans et al. 2020, Results |
| Bringans et al. 2020 | Clin Proteomics 2020;17:37. Sections: Reagents; Bead-antibody production; Standards and controls; Sample processing; Data analysis; Results (quantification ranges; < 20% CV from FDA bioanalytical guidance); Additional file 1 (transition settings) |

## 10 Revision history

| Version | Date | Description of change |
| :---- | :---- | :---- |
| 0.1 | 2021-01-27 | First draft. Data analysis in Skyline v3.6, as named in Bringans et al. 2020 (Data analysis). |
| 0.2 | 2021-03-03 | Review round 1 (TR-TM105-v0.1-01 to -24): calibrator source cited (§1); definitions completed and sorted alphabetically (§4); Skyline version recorded by a named step (§7.1); peak-area basis and integration settings defined, template and worksheet IDs assigned (§5.1, §5.2, §7.2); objective conditions for manual integration (§7.2); S/N outcome defined per well type and peak, blank wells passed to TM-106 (§7.3, §8.2); formula marked as derived, unit, reporting precision and quantification ranges stated (§7.4); co-elution and CV checks as steps with roles (§7.2, §7.4); CV source corrected to Results; one action per step; batch-level and sample-level nonconformities, rework under QMS-003 §6.4 (§8.3); one retention reference (§8.4); references completed (§9); future revision row removed; metadata version and status corrected. Also: AI statement made true for a draft; cross-references aligned with TM-104 v0.2; batch acceptance limit no longer restated (owned by TM-106); ISO 13485 clause lists aligned. TR-TM105-v0.1-10 and -19 stay open until TM-106 and QMS-002 are drafted. |
| 1.0 | 2021-05-18 | Approved for release; no content change from 0.2. |
| 1.1 | 2026-07-07 | Revision draft for the change from Skyline v3.6 to v26.1 (change request CR-TM105-01, QMS-005): Skyline v26.1 named (§1, §2.1, §2.2); responsibilities updated for sample types, exported concentrations and audit log review (§3); Skyline terms defined (§4.2); template, plate map and software rows and validation note updated (§5.1, §5.2); Skyline calculates the concentrations with quantification settings held in TM-105-T01 (§7.4); the calculation worksheet TM-105-T02 keeps only the S/N and CV calculations (§7.3.1, §7.4.3); concentrations exported after S/N sign-off (§7.3.8); the audit log replaces the manual integration list and confirms the Skyline version (§7.1, §7.2, §7.5, §8.4); peak truncation criterion and Candidate Peaks view added to peak review (§7.2, §8.2); references updated (§9); approval fields reset (§11, §12). |
| 1.2 | 2026-08-28 | Review round 1 of the revision draft (TR-TM105-v1.1-01 to -22): change request CR-TM105-01, validation report VR-TM105-01 and release notes EXT-SKY-2601 named, and effectiveness tied to the approved validation (§5.2, §8.2, §9); exact version string compared (§7.1.3, §7.1.4, §7.5.10, §8.2); truncation threshold left as a placeholder until EXT-SKY-2601 and VR-TM105-01 exist (§7.2, §8.2); level stated for every §8.2 criterion, with new audit log, sample type and calibrator criteria (§8.2); audit logging checked at start, audit log completeness, integrity and mandatory reasons verified in review (§4.2, §7.1, §7.2.6, §7.5); every setting that affects Calculated Concentration fixed and calibrator exclusion prohibited (§7.4); CV taken from Ratio to heavy in the peak report (§7.2.8, §7.4.3); transition rule for v1.0 batches, rework and training (§2.4, §8.3.7, §8.3.10); one action per step (§7.2.5, §7.5); Skyline archive as the record (§7.5.14, §8.4); definitions and table captions (§4.2, §7.2, §7.4); report definitions held in TM-105-T01 (§5.1, §7.2.8, §7.4.6); workstation tied to the validated configuration (§5.2); FDA guidance name aligned (§8.2); Supersedes set to none for a draft (§12). TR-TM105-v1.1-01, -02, -03 and -15 stay open until CR-TM105-01, VR-TM105-01 and EXT-SKY-2601 exist. |
| 2.0 | 2026-10-16 | Approved for release; no content change from 1.2. |

## 11 Approval

[Signatures are captured in the electronic QMS. ADDED FOR TRAINING]

| Role | Name | Signature | Date |
| :---- | :---- | :---- | :---- |
| Author | Dr. LC Proton, Associate Scientist | [Electronic signature] | 2026-10-09 |
| Technical Reviewer | Mira Armstrong, Technical Reviewer | [Electronic signature] | 2026-10-14 |
| Quality Assurance | Tess Lindqvist, Quality Assurance | [Electronic signature] | 2026-10-16 |

## 12 Document metadata

| Field | Value |
| :---- | :---- |
| **Document ID** | TM-105 |
| **Doc Type** | Method SOP |
| **Title** | Skyline data analysis |
| **Manufacturer** | Positive Climb Diagnostics |
| **Assay** | 3-plex immuno-MRM DKD assay |
| **Source** | Bringans et al. 2020, CC BY 4.0 |
| **Version** | 2.0 |
| **Status** | Effective |
| **Approval date** | 2026-10-16 |
| **Effective date** | 2026-10-30 |
| **Supersedes** | TM-105 v1.0 |
| **Superseded by** | none |
| **ISO 13485 clause(s)** | 4.1.6, 4.2.5, 7.5.1, 7.5.6, 8.3 |
| **Author** | Dr. LC Proton, Associate Scientist |
| **Reviewer** | Mira Armstrong, Technical Reviewer |
| **Approver** | Tess Lindqvist, Quality Assurance |
| **Training case** | True |
