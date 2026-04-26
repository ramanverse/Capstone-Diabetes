# Data Dictionary — Diabetic Patient Readmission Dataset

**Dataset:** Diabetes 130-US Hospitals for Years 1999–2008
**Source:** [UCI ML Repository](https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008)
**Working Columns:** 14 (selected subset from original 50)

---

## Column Definitions

| # | Column Name | Data Type | Role | Description | Possible Values | Known Quality Issues |
|---|---|---|---|---|---|---|
| 1 | `encounter_id` | Integer | Identifier | Unique identifier for each hospital encounter/visit | Unique integers | None — complete, no duplicates |
| 2 | `patient_nbr` | Integer | Identifier | Unique identifier for each patient across encounters | Unique integers per patient | 30,248 patients have multiple encounters — deduplication required |
| 3 | `race` | Categorical | Feature | Patient's reported race/ethnicity | Caucasian, AfricanAmerican, Hispanic, Asian, Other, ? | 2,273 rows (2.23%) contain `?` representing missing values |
| 4 | `gender` | Categorical | Feature | Patient's reported gender | Female, Male, Unknown/Invalid | 3 rows contain "Unknown/Invalid" — negligible, to be dropped |
| 5 | `age` | Categorical (ordinal) | Feature | Patient age in decade brackets | [0-10), [10-20), [20-30), [30-40), [40-50), [50-60), [60-70), [70-80), [80-90), [90-100) | Stored as string brackets — converted to numeric midpoints in ETL |
| 6 | `time_in_hospital` | Integer | Feature / KPI | Number of days the patient stayed in hospital | 1 to 14 | No missing values. Capped at 14 by dataset design |
| 7 | `num_medications` | Integer | Feature | Count of distinct medications administered during encounter | 1 to 81 | Right-skewed distribution; max of 81 is an outlier — investigate |
| 8 | `num_lab_procedures` | Integer | Feature | Count of lab tests performed during encounter | 1 to 132 | Right-skewed; max 132 may be valid for complex cases |
| 9 | `number_diagnoses` | Integer | Feature | Total number of diagnoses entered in the system | 1 to 16 | Clean, no issues |
| 10 | `admission_type_id` | Integer (mapped) | Feature | Numeric code for type of admission | 1=Emergency, 2=Urgent, 3=Elective, 4=Newborn, 5=Not Available, 6=NULL, 7=Trauma, 8=Not Mapped | IDs 5 and 6 represent missing/unknown — mapped to "Other" in ETL |
| 11 | `discharge_disposition_id` | Integer (mapped) | Feature | Numeric code for how the patient was discharged | 1=Home, 3=SNF, 6=Home Health, 11=Expired, 18=NULL, others=transfers | 26 unique codes. ID=11 (Expired, 1,642 rows) must be removed — deceased patients cannot be readmitted |
| 12 | `insulin` | Categorical | Feature | Whether insulin was prescribed and direction of dosage change | No, Steady, Down, Up | No missing values. Treated as ordinal in analysis |
| 13 | `diabetesMed` | Categorical (binary) | Feature | Whether any diabetes medication was prescribed | Yes, No | No missing values. Strong skew: 77% Yes |
| 14 | `readmitted` | Categorical | **Target** | Whether the patient was readmitted and how soon | `<30` (within 30 days), `>30` (after 30 days), `NO` (not readmitted) | No missing values. Class imbalance: `<30` is only 11.16% |

---

## Target Variable Encoding (ETL)

| Original Value | Encoded Value | Meaning |
|---|---|---|
| `<30` | 1 | Readmitted within 30 days — **positive class** |
| `>30` | 0 | Readmitted after 30 days — treated as not readmitted for binary task |
| `NO` | 0 | Not readmitted |

> **Rationale:** The clinical and regulatory focus (CMS Hospital Readmissions Reduction Program) penalises hospitals specifically for readmissions within 30 days. Readmissions after 30 days are not penalised and are analytically treated the same as no readmission for binary classification purposes.

---

## Columns Excluded from Working Set

The original dataset contains 50 columns. The following categories were excluded:

| Category | Columns Excluded | Reason |
|---|---|---|
| Diagnosis codes | `diag_1`, `diag_2`, `diag_3` | ICD-9 codes require specialist domain mapping; out of scope |
| Other medications | `metformin`, `glipizide`, `glyburide`, etc. (22 cols) | Redundant with `insulin` and `diabetesMed` for this analysis scope |
| Admin fields | `payer_code`, `medical_specialty`, `weight` | >40% missing in original dataset |

---

## Data Quality Summary

| Issue | Column(s) | Count | % of Rows | Action |
|---|---|---|---|---|
| Missing (`?`) | `race` | 2,273 | 2.23% | Impute with mode (Caucasian) |
| Invalid category | `gender` | 3 | 0.00% | Drop rows |
| Dead patients | `discharge_disposition_id == 11` | 1,642 | 1.61% | Drop rows |
| Duplicate patients | `patient_nbr` | 30,248 extra rows | 29.72% | Keep first encounter only |
| String brackets | `age` | All 101,766 | 100% | Convert to numeric midpoints |
| Numeric codes | `admission_type_id`, `discharge_disposition_id` | All rows | 100% | Map to readable labels |

<!-- updated by Ayush Shukla -->
