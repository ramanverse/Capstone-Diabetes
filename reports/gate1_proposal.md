# Gate 1 Proposal — Go/No-Go Checkpoint

**Course:** Capstone 2 — Data Analytics Simulation
**Submission Date:** [Date]
**Mentor:** [Mentor Name]
**Section:** [Section Name]

---

## 1. Team Details

| Role | Name | GitHub Handle |
|---|---|---|
| ETL Lead | Raman | [@ramanverse](https://github.com/ramanverse) |
| Analysis Lead | [Teammate 2] | [@username] |
| Statistics Lead | [Teammate 3] | [@username] |
| Dashboard Lead | [Teammate 4] | [@username] |
| Reporting Lead | [Teammate 5] | [@username] |

**GitHub Repository:** https://github.com/ramanverse/Capstone-Diabetes

---

## 2. Sector & Problem Statement

**Sector:** Healthcare

Hospital readmission within 30 days of discharge is one of the most significant and measurable indicators of care quality in modern healthcare systems. In the United States, the Centers for Medicare & Medicaid Services (CMS) actively penalises hospitals with high readmission rates under the Hospital Readmissions Reduction Program (HRRP), making this a direct financial and operational priority for hospital administrators. Diabetic patients are among the most frequently readmitted cohorts, carrying complex comorbidities and requiring careful post-discharge management.

Our team will analyse the Diabetes 130-US Hospitals dataset to answer the following business question: **"What patient and clinical factors most significantly predict 30-day hospital readmission for diabetic patients, and how can hospitals reduce avoidable readmissions to lower costs and improve patient outcomes?"** The analysis will span demographic profiling, clinical feature analysis, statistical hypothesis testing, and a Tableau dashboard designed for hospital operations decision-makers.

---

## 3. Dataset Details

| Field | Detail |
|---|---|
| **Dataset Name** | Diabetes 130-US Hospitals for Years 1999–2008 |
| **Source** | UCI Machine Learning Repository |
| **URL** | https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008 |
| **Row Count** | 101,766 hospital encounter records |
| **Total Columns** | 50 (we work with 14 selected columns) |
| **Format** | CSV, tabular, row-level records |
| **Time Period** | 1999–2008, 130 US hospitals |
| **Source Type** | Raw clinical records — not a competition dataset |

---

## 4. Why This Dataset Qualifies

| Rubric Requirement | Evidence |
|---|---|
| **≥ 5,000 rows** | 101,766 rows — exceeds requirement by 20× |
| **≥ 8 meaningful columns** | 14 selected analytical columns spanning demographics, clinical metrics, and outcomes |
| **Real quality issues present** | `race` has 2,273 missing values encoded as `?`; `age` is stored as string brackets requiring conversion; `admission_type_id` and `discharge_disposition_id` are numeric codes needing mapping; 30,248 duplicate patient encounters requiring deduplication logic |
| **Not a pre-cleaned Kaggle competition file** | Sourced directly from UCI ML Repository — raw clinical records with documented real-world messiness. No pre-built features, no leaderboard, no sample solutions |
| **Row-level records suitable for ETL** | Each row is one hospital encounter — ideal for Python ETL, KPI aggregation, and Tableau row-level calculations |
| **Suitable for statistical analysis** | Mixed types (categorical + numerical) support chi-square, correlation, regression, and ANOVA |

---

## 5. Initial Data Dictionary

| # | Column | Type | Description | Quality Issue |
|---|---|---|---|---|
| 1 | encounter_id | Integer | Unique encounter ID | None |
| 2 | patient_nbr | Integer | Patient ID | 30,248 repeat encounters |
| 3 | race | Categorical | Patient race | 2,273 `?` values |
| 4 | gender | Categorical | Patient gender | 3 "Unknown/Invalid" rows |
| 5 | age | Categorical | Age in decade brackets | String format — needs conversion |
| 6 | time_in_hospital | Integer | Days in hospital | None |
| 7 | num_medications | Integer | Medication count | Outliers (max 81) |
| 8 | num_lab_procedures | Integer | Lab test count | Outliers (max 132) |
| 9 | number_diagnoses | Integer | Diagnosis count | None |
| 10 | admission_type_id | Integer | Admission type code | Codes 5,6 = NULL/Unknown |
| 11 | discharge_disposition_id | Integer | Discharge code | ID 11 = Expired (must drop) |
| 12 | insulin | Categorical | Insulin dosage change | None |
| 13 | diabetesMed | Categorical | On diabetes medication | None |
| 14 | readmitted | Categorical | Readmission outcome | Class imbalance (`<30` = 11%) |

---

## 6. Backup Datasets

### Backup 1 — Heart Disease UCI Dataset
- **URL:** https://archive.ics.uci.edu/dataset/45/heart+disease
- **Rows:** 303 (small — use as methodology backup only)
- **Sector:** Healthcare
- **Notes:** Classic clinical dataset with real missing values and mixed types

### Backup 2 — MIMIC-III Clinical Notes (PhysioNet)
- **URL:** https://physionet.org/content/mimiciii/1.4/
- **Rows:** 58,000+ ICU admissions
- **Sector:** Healthcare
- **Notes:** Requires credentialing but contains rich real-world clinical data with significant quality issues. Strong alternative if primary is rejected.
