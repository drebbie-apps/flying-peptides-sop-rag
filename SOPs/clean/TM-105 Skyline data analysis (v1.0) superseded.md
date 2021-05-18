---
doc_id: "TM-105"
doc_type: "Method SOP"
title: "Skyline data analysis"
manufacturer: "Positive Climb Diagnostics"
assay: "3-plex immuno-MRM DKD assay"
source: "Bringans et al. 2020, CC BY 4.0"
version: "1.0"
status: "Superseded"
approval_date: 2021-05-18
effective_date: 2021-06-01
supersedes: null
superseded_by: "TM-105 v2.0"
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

This procedure defines how the raw data files of one batch of the 3-plex immuno-MRM DKD assay are analysed in Skyline v3.6 to give a peak area for each target (light) peptide and its SIS (heavy) peptide, and how the concentrations of APOA4, CD5L and IBP3 are calculated from the single-level calibrator, so that data analysis runs as a controlled production process (ISO 13485 §7.5.1, §7.5.6). The calibrator is defined in Bringans et al. 2020, Standards and controls; the calculation principle is from Bringans et al. 2020, Data analysis.

## 2 Scope

### 2.1 Applicability

Data analysis of one batch (one 96-well plate) acquired under TM-104: check of the Skyline version, import of the raw data files into Skyline v3.6, peak integration and review, signal-to-noise (S/N) check, calculation of the protein concentrations, second-person review and release of the results to TM-106.

### 2.2 Qualifications and training

Associate Scientists with documented training on TM-105 and on Skyline v3.6. Training must be recorded before the first independent analysis. An Associate Scientist without recorded training does not analyse batches under this SOP until the training is recorded. The Technical Reviewer of a batch is not the Associate Scientist who analysed it.

### 2.3 Exclusions

Acquisition of the raw data (TM-104); batch acceptance, including the evaluation of the reference plasma, the PBS blanks and the double blank, and run release (TM-106); calculation of a clinical risk score; validation of Skyline and of the calculation worksheet (QMS-006).

## 3 Responsibilities

| Role | Responsibility |
| :---- | :---- |
| Associate Scientist | Records and checks the Skyline version, imports the raw data, integrates and reviews the peaks, performs the S/N check, calculates the concentrations, and stops and raises an NCR when a check fails. |
| Technical Reviewer | Signs off the S/N check, performs the second-person review of integrations and calculations, re-verifies reworked results and releases the results to TM-106. |
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
| m/z | Mass-to-charge ratio |
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
| Calibrator | Recombinant target proteins at known concentrations, processed alongside samples to convert signal into concentration. |
| Double blank | Well with 200 µL PBS and no Ab-beads, processed in TM-103 (Bringans et al. 2020, Sample processing). |
| Light / heavy peptide | Endogenous (unlabelled) target peptide / its 13C15N-labelled SIS peptide. |
| Manual integration | A change of the peak boundaries set by Skyline, made by the Associate Scientist under TM-105 §7.2. |
| MRM | Multiple reaction monitoring: targeted measurement of defined precursor-to-product ion pairs on a triple quadrupole mass spectrometer. |
| PBS blank | Well with 50 µL PBS in place of a sample, processed with Ab-beads in TM-103 (Bringans et al. 2020, Sample processing). |
| Peak area | Integrated signal of one peptide's chromatographic peak: the sum of the areas of all its transitions (Skyline Total Area; TM-105 §7.2). |
| Peak area ratio | Light peak area divided by heavy (SIS) peak area for the same protein in the same injection (Bringans et al. 2020, Data analysis). |
| Reference plasma | Pooled plasma processed in every batch to monitor assay performance (QC). |
| Retention time | Time from injection to the apex of a peptide's chromatographic peak. |
| SIS | Stable isotope-labelled internal standard: a synthetic heavy-isotope peptide used to normalise signal across samples. |
| Skyline document | The Skyline file that holds the target list, the integration settings, the imported raw data and the integration results of one batch. |
| Total Area / Total Background | Skyline values for the integrated peak area and the background under the peak, used for the S/N check (Bringans et al. 2020, Data analysis). |
| Transition | One precursor-to-product ion m/z pair. All transitions of a peptide are summed into its peak area; no transition is designated quantifier or qualifier (TM-104 §7.4). |

## 5 Data inputs, software and equipment

### 5.1 Data inputs

| Input | Source | Control |
| :---- | :---- | :---- |
| Raw data files of one batch | Transferred to controlled storage under TM-104 §7.6.12 | Released by the Technical Reviewer (TM-104 §7.6.17) |
| Skyline document template TM-105-T01 (peptides, SIS peptides, transitions, integration settings) | Peptides and transitions: TM-104 §7.4 (Bringans et al. 2020, Reagents; Additional file 1). Integration settings: TM-105 §7.2 | Controlled template, ID TM-105-T01 [ADDED FOR TRAINING]; changed only under QMS-005 |
| Calibrator concentrations | TM-102 [section to be cited when TM-102 is drafted]; Bringans et al. 2020, Standards and controls | Effective plasma concentrations: APOA4 91.5 µg/mL, CD5L 3.45 µg/mL, IBP3 0.892 µg/mL |
| Plate map and batch record | TM-103 ; TM-104 §7.1.15 | Sample identity, well types and well positions |

The calibrator concentrations are those of Bringans et al. 2020, Standards and controls, and are stated only in this table. The IDs of the Skyline document template (TM-105-T01) and the calculation worksheet (TM-105-T02) are [ADDED FOR TRAINING].

### 5.2 Software and equipment

| Software / equipment | Version / manufacturer | Minimum specification | Validation / check |
| :---- | :---- | :---- | :---- |
| Skyline | Version 3.6, MacCoss Lab Software, University of Washington, Seattle, USA | Imports the raw data files of TM-104; reports peak areas, Total Area and Total Background | Validated for its intended use (QMS-006; ISO 13485 §4.1.6). Version recorded and checked before use (TM-105 §7.1.3, §7.1.4). |
| Calculation worksheet TM-105-T02 | Controlled worksheet [ID ADDED FOR TRAINING] | Calculates S/N, peak area ratios, the calibrator mean ratio and CV, and concentrations (TM-105 §7.3, §7.4) | Validated for its intended use (QMS-006) [ADDED FOR TRAINING]; changed only under QMS-005 |
| Workstation | [Model] [ADDED FOR TRAINING] | Meets the Skyline system requirements; access-controlled user accounts | Listed in the validated configuration (QMS-006) [ADDED FOR TRAINING] |

The software and version are those named in Bringans et al. 2020, Data analysis. A different Skyline version may be used only after validation under QMS-006 and a change of this SOP under QMS-005.

## 6 Safety and environmental controls

Not applicable: this procedure is performed at a computer workstation and involves no samples, chemicals or instruments. Access to raw data and Skyline documents follows the IT access rules of the electronic QMS [ADDED FOR TRAINING].

## 7 Procedure

### 7.1 Preparation

| Who | Task |
| :---- | :---- |
| Associate Scientist | 7.1.1 Check that the Technical Reviewer has released the raw data files of the batch (TM-104 §7.6.17). |
| Associate Scientist | 7.1.2 Check that the batch record shows the signed-off SST (TM-104 §7.5.4). |
| Associate Scientist | 7.1.3 Record the installed Skyline version (Help > About) in the batch record. |
| Associate Scientist | 7.1.4 Check that the recorded Skyline version is 3.6, the version validated under QMS-006. |
| Associate Scientist | 7.1.5 If a check in TM-105 §7.1.1, §7.1.2 or §7.1.4 fails, stop, do not analyse the data, and follow TM-105 §8.3. |
| Associate Scientist | 7.1.6 Open the Skyline document template TM-105-T01 (TM-105 §5.1) and save it under the batch ID. |

### 7.2 Import and peak integration

The Skyline document template TM-105-T01 holds the integration settings in this table.

| Parameter | Setting | Source |
| :---- | :---- | :---- |
| Peak area of a peptide | Sum of the areas of all transitions of the peptide (Skyline Total Area); no quantifier or qualifier transition | TM-104 §7.4 [ADDED FOR TRAINING] |
| Transitions | As held in the MRM method file TM-104-M01 (TM-104 §7.4) | Bringans et al. 2020, Additional file 1 |
| Peak picking | Skyline default peak picking | [ADDED FOR TRAINING] |
| Peak boundaries | The same boundaries for the light and heavy peptide of one protein in one injection | [ADDED FOR TRAINING] |
| Background | Skyline Total Background under the integrated peak | Bringans et al. 2020, Data analysis |

Steps for import, integration and peak review:

| Who | Task |
| :---- | :---- |
| Associate Scientist | 7.2.1 Import all raw data files of the batch into the Skyline document (File > Import > Results). |
| Associate Scientist | 7.2.2 Let Skyline integrate the light and heavy peptide peaks with the settings of TM-105 §7.2, giving one peak area per peptide (Bringans et al. 2020, Data analysis). |
| Associate Scientist | 7.2.3 Check that the apex retention times of the light and heavy peptide of each protein meet the co-elution limit in TM-105 §8.2. |
| Associate Scientist | 7.2.4 Check that the peak boundaries include the whole peak, from where the signal rises above the background to where it returns to it [ADDED FOR TRAINING]. |
| Associate Scientist | 7.2.5 If a peak fails TM-105 §7.2.3 or §7.2.4, adjust its boundaries only under a condition in the manual integration table of TM-105 §7.2. |
| Associate Scientist | 7.2.6 Record each manual integration on the manual integration list: well, peptide, condition, original and new boundaries. |
| Associate Scientist | 7.2.7 If no permitted condition applies, or the co-elution limit is still not met, do not adjust the peak; follow TM-105 §8.3. |
| Associate Scientist | 7.2.8 Export a peak report with Total Area and Total Background for every light and heavy peptide in every injection (Bringans et al. 2020, Data analysis). |

Manual integration table: manual integration is permitted only under these conditions [ADDED FOR TRAINING].

| Condition | Permitted adjustment |
| :---- | :---- |
| Skyline selected a peak at which the light and heavy apexes differ by more than the co-elution limit in TM-105 §8.2 | Move the boundaries to the peak at which the light and heavy apexes co-elute, if there is one. |
| The boundaries cut off part of the peak (TM-105 §7.2.4) | Widen the boundaries to include the whole peak. |
| The boundaries include a neighbouring peak | Narrow the boundaries to the peak of the peptide. |
| Any other case, including an adjustment made only to meet an S/N, CV or concentration criterion | Not permitted. |

### 7.3 Signal-to-noise check [CRITICAL CONTROL POINT]

Bringans et al. 2020 (Data analysis) accept peaks on S/N calculated from the Total Area and Total Background values provided by Skyline. The S/N limit for each well type and peak is stated in TM-105 §8.2. PBS blank and double-blank wells contain no plasma (Bringans et al. 2020, Sample processing), so no light peptide is expected in them; the S/N limit is not applied to them, and TM-106 evaluates them [section to be cited when TM-106 is drafted].

| Who | Task |
| :---- | :---- |
| Associate Scientist | 7.3.1 Calculate S/N for every light and heavy peak in every well as Total Area ÷ Total Background. |
| Associate Scientist | 7.3.2 Compare the S/N of each calibrator, reference plasma and sample peak with the S/N limit for its well type in TM-105 §8.2. |
| Associate Scientist | 7.3.3 If a light or heavy peak of a calibrator or reference plasma well fails the S/N limit, stop the analysis of the batch and follow TM-105 §8.3. |
| Associate Scientist | 7.3.4 If the heavy (SIS) peak of a sample fails the S/N limit, mark that protein result of the sample "invalid – SIS failure". |
| Associate Scientist | 7.3.5 For each result marked "invalid – SIS failure", follow TM-105 §8.3 as a sample-level nonconformity. |
| Associate Scientist | 7.3.6 If the light peak of a sample fails the S/N limit and its heavy peak passes, report that protein result as "not quantifiable" [ADDED FOR TRAINING]. This is a valid result, not a nonconformity. |
| Associate Scientist | 7.3.7 Record the S/N values of the PBS blank and double-blank wells for TM-106, without applying the S/N limit. |
| Technical Reviewer | 7.3.8 [CRITICAL CONTROL POINT] Verify and sign off the S/N check. Concentrations are calculated only after this sign-off. |

### 7.4 Concentration calculation

The SIS peptide normalises the signal across samples, and the calibrator replicates provide the concentrations (Bringans et al. 2020, Data analysis). The calibrator concentrations are those in TM-105 §5.1 (Bringans et al. 2020, Standards and controls). The paper gives no formula; the single-point calculation through the origin in TM-105 §7.4.5 is derived from Bringans et al. 2020, Data analysis [ADDED FOR TRAINING]. The quantification ranges in this table are from Bringans et al. 2020, Results; their use for reporting in TM-105 §7.4.8 and §7.4.9 is [ADDED FOR TRAINING].

| Protein | Quantification range in plasma | Source |
| :---- | :---- | :---- |
| APOA4 | 37.5 to 200 µg/mL | Bringans et al. 2020, Results |
| CD5L | 0.104 to 10.0 µg/mL | Bringans et al. 2020, Results |
| IBP3 | 0.0104 to 1.00 µg/mL | Bringans et al. 2020, Results |

Steps for the concentration calculation:

| Who | Task |
| :---- | :---- |
| Associate Scientist | 7.4.1 For each protein and injection, calculate the peak area ratio of the light peptide to its heavy SIS peptide (Bringans et al. 2020, Data analysis). |
| Associate Scientist | 7.4.2 For each protein, calculate the mean peak area ratio of the calibrator replicates, N = 4 (Bringans et al. 2020, Data analysis; Sample processing). |
| Associate Scientist | 7.4.3 For each protein, calculate the CV of the peak area ratios of the calibrator replicates. |
| Associate Scientist | 7.4.4 If a CV fails the precision limit in TM-105 §8.2, stop the analysis of the batch and follow TM-105 §8.3. |
| Associate Scientist | 7.4.5 Calculate the concentration of each sample as C (µg/mL) = (peak area ratio of the sample ÷ mean calibrator peak area ratio) × calibrator concentration (TM-105 §5.1). Derived from Bringans et al. 2020, Data analysis [ADDED FOR TRAINING]. |
| Associate Scientist | 7.4.6 Calculate the concentration of each reference plasma replicate (N = 4) with the formula of TM-105 §7.4.5, from its peak area ratio (TM-105 §7.4.1) and the calibrator mean ratio (TM-105 §7.4.2), for batch acceptance under TM-106. |
| Associate Scientist | 7.4.7 Report each concentration in µg/mL to 3 significant figures, the precision of the calibrator concentrations (Bringans et al. 2020, Standards and controls) [ADDED FOR TRAINING]. |
| Associate Scientist | 7.4.8 Report a sample concentration below the lower limit of its quantification range (TM-105 §7.4) as "< [lower limit] µg/mL" [ADDED FOR TRAINING]. |
| Associate Scientist | 7.4.9 Report a sample concentration above the upper limit of its quantification range (TM-105 §7.4) as "> [upper limit] µg/mL" [ADDED FOR TRAINING]. |

### 7.5 Review and release

| Who | Task |
| :---- | :---- |
| Technical Reviewer | 7.5.1 Review the Skyline document and the peak report of the batch. |
| Technical Reviewer | 7.5.2 Verify each entry on the manual integration list against the conditions in TM-105 §7.2. |
| Technical Reviewer | 7.5.3 Verify the calculations in the calculation worksheet TM-105-T02 (TM-105 §7.4). |
| Technical Reviewer | 7.5.4 Confirm that the Skyline version recorded in the batch record (TM-105 §7.1.3) is 3.6. |
| Technical Reviewer | 7.5.5 Record the second-person review in the batch record. |
| Technical Reviewer | 7.5.6 If the review finds a nonconformity that is not yet recorded, do not release the results and follow TM-105 §8.3. |
| Technical Reviewer | 7.5.7 Release the results to TM-106 for batch acceptance. Results withheld under TM-105 §8.3.2 are not released. |
| Associate Scientist | 7.5.8 Save the Skyline document, the peak report, the manual integration list and the calculation worksheet in controlled storage (TM-105 §8.4). |

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
| Skyline version (batch level) | 3.6, as validated under QMS-006 and recorded in the batch record (TM-105 §7.1.3) | Bringans et al. 2020, Data analysis |
| S/N of light and heavy peaks, calibrator and reference plasma wells (batch level) | > 5 | Bringans et al. 2020, Data analysis; application per well type [ADDED FOR TRAINING] |
| S/N of the heavy (SIS) peak, sample wells (sample level) | > 5; otherwise the result is invalid (TM-105 §7.3.4) | Bringans et al. 2020, Data analysis; outcome [ADDED FOR TRAINING] |
| S/N of the light peak, sample wells (sample level) | > 5 for a quantitative result; otherwise reported as "not quantifiable" (TM-105 §7.3.6) | Bringans et al. 2020, Data analysis; outcome [ADDED FOR TRAINING] |
| S/N, PBS blank and double-blank wells | Not applied in this SOP; evaluated in TM-106 | Well types: Bringans et al. 2020, Sample processing |
| Co-elution of light and heavy peptide | Apex retention times differ by no more than 0.05 min | [ADDED FOR TRAINING] |
| Calibrator peak area ratio precision (batch level) | CV < 20% across the calibrator replicates (N = 4), per protein | FDA bioanalytical guidance for ligand-binding assays |
| Manual integrations (batch level) | Only under the conditions in TM-105 §7.2; each one recorded and verified by the Technical Reviewer | [ADDED FOR TRAINING] |

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
| Associate Scientist | 8.3.7 Re-integrate or re-calculate only after the disposition "rework" is recorded in the NCR, following TM-105 §7.2 to §7.4 (QMS-003 §6.4.1). |
| Technical Reviewer | 8.3.8 Re-verify the reworked results against TM-105 §8.2 and record the result in the NCR (QMS-003 §6.4.3). |
| Quality Assurance | 8.3.9 Decide any re-injection under TM-104 §8.3.5; it is carried out under TM-104 §7.6.9, within the limit of TM-104 §7.6.7. |
| Quality Assurance | 8.3.10 Treat all results analysed with a Skyline version other than the validated version as nonconforming product (QMS-003 §6.1). |
| Quality Assurance | 8.3.11 Decide whether CAPA is needed (QMS-004), applying the triggers of QMS-003 §6.7.1. |

### 8.4 Control of records (ISO 13485 §4.2.5)

Records created: the Skyline version entry in the batch record (TM-105 §7.1.3), the Skyline document of the batch, the exported peak report, the manual integration list, the calculation worksheet, the S/N sign-off, the second-person review and any NCRs.

* **Storage**: electronic records in controlled storage with access control and audit trail, validated under QMS-006.
* **Retention**: for the period set in QMS-002 (Control of records).

## 9 References

| Document / standard | Title and relevant section |
| :---- | :---- |
| ISO 13485:2016 | 4.1.6 Validation of software used in the QMS; 4.2.5 Control of records; 7.5.1 Control of production and service provision; 7.5.6 Validation of processes for production and service provision; 8.3 Control of nonconforming product |
| ISO 14971:2019 | Application of risk management to medical devices (risk management file RMF-001 [ADDED FOR TRAINING]) |
| IVDR (EU) 2017/746 | In vitro diagnostic medical devices regulation |
| QMS-001 | Document control (§6.3 technical review, including the Technical Reviewer role; §6.4 QA approval; §6.5.1 effective date) |
| QMS-002 | Control of records (retention period) [section to be cited when QMS-002 is drafted] |
| QMS-003 | Control of nonconforming product (§4 definitions; §6.1 identification and segregation, §6.1.2 Quarantine status; §6.3.2 disposition; §6.4.1 rework procedure, §6.4.2 adverse-effects assessment, §6.4.3 re-verification; §6.7.1 CAPA triggers; §7.1.1 time limit for raising an NCR) |
| QMS-004 | Corrective and preventive action |
| QMS-005 | Change control |
| QMS-006 | Validation of QMS software (including Skyline v3.6 and the calculation worksheet TM-105-T02) |
| TM-101 | Ab-bead conjugation and QC |
| TM-102 | Calibrator, reference plasma and SIS preparation (calibrator concentrations) [section to be cited when TM-102 is drafted] |
| TM-103 | Immunoaffinity capture and digestion (plate map; PBS blanks and double blank) [section to be cited when TM-103 is drafted] |
| TM-104 | Microflow MRM LC-MS acquisition (§1 LC-MRM; §7.1.15 plate map; §7.4 transitions; §7.5 SST, §7.5.4 SST sign-off; §7.6.7 time limit; §7.6.9 re-injection; §7.6.12 transfer and §7.6.17 release of raw data files; §8.3.5 disposition of re-injection) |
| TM-106 | Batch acceptance and run release [section to be cited when TM-106 is drafted] |
| Skyline v3.6 | MacCoss Lab Software, University of Washington, Seattle, USA (external software, version as named in Bringans et al. 2020, Data analysis) |
| FDA guidance | Bioanalytical Method Validation, Guidance for Industry (2018), as cited in Bringans et al. 2020, Results |
| Bringans et al. 2020 | Clin Proteomics 2020;17:37. Sections: Reagents; Bead-antibody production; Standards and controls; Sample processing; Data analysis; Results (quantification ranges; < 20% CV from FDA bioanalytical guidance); Additional file 1 (transition settings) |

## 10 Revision history

| Version | Date | Description of change |
| :---- | :---- | :---- |
| 0.1 | 2021-01-27 | First draft. Data analysis in Skyline v3.6, as named in Bringans et al. 2020 (Data analysis). |
| 0.2 | 2021-03-03 | Review round 1 (TR-TM105-v0.1-01 to -24): calibrator source cited (§1); definitions completed and sorted alphabetically (§4); Skyline version recorded by a named step (§7.1); peak-area basis and integration settings defined, template and worksheet IDs assigned (§5.1, §5.2, §7.2); objective conditions for manual integration (§7.2); S/N outcome defined per well type and peak, blank wells passed to TM-106 (§7.3, §8.2); formula marked as derived, unit, reporting precision and quantification ranges stated (§7.4); co-elution and CV checks as steps with roles (§7.2, §7.4); CV source corrected to Results; one action per step; batch-level and sample-level nonconformities, rework under QMS-003 §6.4 (§8.3); one retention reference (§8.4); references completed (§9); future revision row removed; metadata version and status corrected. Also: AI statement made true for a draft; cross-references aligned with TM-104 v0.2; batch acceptance limit no longer restated (owned by TM-106); ISO 13485 clause lists aligned. TR-TM105-v0.1-10 and -19 stay open until TM-106 and QMS-002 are drafted. |
| 1.0 | 2021-05-18 | Approved for release; no content change from 0.2. |

## 11 Approval

[Signatures are captured in the electronic QMS. ADDED FOR TRAINING]

| Role | Name | Signature | Date |
| :---- | :---- | :---- | :---- |
| Author | Dr. LC Proton, Associate Scientist | [Electronic signature] | 2021-04-06 |
| Technical Reviewer | Mira Armstrong, Technical Reviewer | [Electronic signature] | 2021-04-06 |
| Quality Assurance | Tess Lindqvist, Quality Assurance | [Electronic signature] | 2021-05-18 |

## 12 Document metadata

| Field | Value |
| :---- | :---- |
| **Document ID** | TM-105 |
| **Doc Type** | Method SOP |
| **Title** | Skyline data analysis |
| **Manufacturer** | Positive Climb Diagnostics |
| **Assay** | 3-plex immuno-MRM DKD assay |
| **Source** | Bringans et al. 2020, CC BY 4.0 |
| **Version** | 1.0 |
| **Status** | Superseded |
| **Approval date** | 2021-05-18 |
| **Effective date** | 2021-06-01 |
| **Supersedes** | none |
| **Superseded by** | TM-105 v2.0 |
| **ISO 13485 clause(s)** | 4.1.6, 4.2.5, 7.5.1, 7.5.6, 8.3 |
| **Author** | Dr. LC Proton, Associate Scientist |
| **Reviewer** | Mira Armstrong, Technical Reviewer |
| **Approver** | Tess Lindqvist, Quality Assurance |
| **Training case** | True |
