# Final Project Report
## Predicting 30-Day Hospital Readmission in Diabetic Patients

---

**Group Name:** Diabetes Insights Team  
**Group Members:** Raman; Abhijeet; Vaibhav Singh; Ashish Singh Naruka; Ayush Shukla  

**Title:** Predicting 30-Day Hospital Readmission in Diabetic Patients: A Data-Driven Approach to Reducing Avoidable Healthcare Costs

**Sector:** Healthcare
**Dataset:** Diabetes 130-US Hospitals for Years 1999–2008
**Institute:** [Your Institute Name]
**Section:** [Section Name]
**Team:** [Team ID]
**Submission Date:** [Date]
**GitHub:** https://github.com/ramanverse/Capstone-Diabetes

| Member | Role |
|---|---|
| Raman | ETL Lead |
| Abhijeet | Analysis Lead |
| Vaibhav Singh | Statistics Lead |
| Ashish Singh Naruka | Dashboard Lead |
| Ayush Shukla | Reporting Lead |

---

## Executive Summary

Hospital readmission within 30 days of discharge represents one of the most significant quality and cost failures in modern healthcare delivery. For diabetic patients — a population characterised by high comorbidity burden and complex medication regimens — the risk of early readmission is particularly acute. This project applies a full end-to-end data analytics pipeline to the Diabetes 130-US Hospitals dataset (101,766 encounter records across 130 US hospitals, 1999–2008) to identify the clinical and demographic factors most strongly associated with 30-day readmission.

Our Python-based ETL pipeline cleaned and standardised the raw dataset, resolving missing values, deduplicating repeat patient encounters, and engineering analysis-ready features. Exploratory analysis revealed that emergency admissions, high medication counts, and insulin dose instability are the strongest observable risk signals. Formal statistical testing confirmed that admission type is significantly associated with readmission (Chi-square, p < 0.05), and logistic regression validated a multi-feature predictive model. Five data-backed, quantified business recommendations are delivered — targeting emergency discharge planning, medication reconciliation, insulin stability protocols, transitional care, and EHR-integrated risk scoring — with a combined estimated impact of preventing 3,000+ avoidable readmissions annually.

---

## 1. Sector Context

Diabetes mellitus affects over 37 million Americans and accounts for approximately $327 billion in annual healthcare costs in the United States. Among the most costly and clinically preventable components of diabetic care is hospital readmission. The Centers for Medicare & Medicaid Services (CMS) introduced the Hospital Readmissions Reduction Program (HRRP) in 2012, which financially penalises hospitals with above-average 30-day readmission rates for a defined set of conditions including heart failure, pneumonia, and — critically — diabetes-related complications. As of 2023, over 2,500 hospitals have received HRRP penalties, with aggregate penalties exceeding $500 million annually. This makes readmission prediction not only a clinical priority but a direct financial imperative for hospital administrators.

The diabetes readmission problem is multifactorial. Patients frequently present with 7–9 concurrent diagnoses, are managed on complex multi-drug regimens, and are discharged into care environments that vary significantly in their capacity to support glycaemic control. The 130-hospital dataset used in this study — spanning nearly a decade of real clinical records — provides an exceptional opportunity to apply data analytics to a problem with measurable, quantifiable business impact. The ability to identify high-risk patients before or at discharge, and to intervene with targeted protocols, has been demonstrated in peer-reviewed literature to reduce 30-day readmission rates by 15–25% in comparable cohorts.

---

## 2. Problem Statement

This project addresses the following formally defined business question: *What patient and clinical factors most significantly predict 30-day hospital readmission for diabetic patients, and how can hospitals reduce avoidable readmissions to lower costs and improve patient outcomes?* The analysis is framed as a binary classification and statistical inference problem, where the target outcome is readmission within 30 days of discharge (encoded as a binary indicator). The analytical scope encompasses demographic analysis, clinical feature exploration, formal hypothesis testing, and predictive modelling — culminating in a Tableau dashboard and five specific, quantified operational recommendations for hospital management teams.

---

## 3. Dataset Description

The primary dataset is the Diabetes 130-US Hospitals for Years 1999–2008, sourced from the UCI Machine Learning Repository (https://archive.ics.uci.edu/dataset/296). It contains 101,766 encounter-level records from 130 hospitals across the United States, collected between 1999 and 2008. The original dataset comprises 50 columns spanning patient demographics, admission metadata, laboratory results, medication records, and discharge outcomes.

For this analysis, 14 columns were selected based on analytical relevance, data completeness, and alignment with the business problem. The 36 excluded columns fall into three categories: (1) ICD-9 diagnosis codes requiring specialist clinical domain mapping beyond the scope of this project; (2) 22 individual medication flag columns that are redundant given the inclusion of `num_medications`, `insulin`, and `diabetesMed`; and (3) administrative fields (`payer_code`, `medical_specialty`, `weight`) with missing rates exceeding 40% in the original dataset. Full column selection rationale is documented in `docs/data_dictionary.md`.

**Known Limitations:** The dataset spans 1999–2008 and may not reflect current clinical practice or medication protocols. Race categories are self-reported and subject to classification inconsistencies. The 30-day readmission window is defined by the dataset's own encoding rather than verified administrative claims data.

---

## 4. ETL Methodology

The cleaning pipeline is implemented in `notebooks/02_cleaning.ipynb` and executed sequentially with logged outputs at every step. The pipeline applies the following transformations in order:

**Step 1 — Column Selection:** Immediately upon loading, the dataset is reduced to 14 working columns to minimise memory overhead and eliminate analytical noise from the outset.

**Step 2 — Missing Value Standardisation:** The dataset uses `?` as a missing value placeholder rather than standard NaN. All `?` values are replaced with `NaN` using `df.replace('?', np.nan)`. This affected 2,273 cells in the `race` column exclusively across the 14 working columns.

**Step 3 — Invalid Gender Removal:** Three rows containing `Unknown/Invalid` in the `gender` column are dropped. This represents 0.003% of the dataset and has no statistical impact on any downstream analysis.

**Step 4 — Expired Patient Removal:** Patients with `discharge_disposition_id == 11` (Expired/Deceased) are removed from the dataset. Deceased patients cannot be readmitted; retaining them would introduce systematic false negatives into the target variable. This removed 1,642 rows.

**Step 5 — Race Imputation:** The 2,273 missing race values (2.23%) are imputed with the mode value (Caucasian, 74.78%). Given the low missing rate and the use of race as a demographic grouping variable rather than a primary predictive feature, mode imputation is appropriate and introduces minimal bias.

**Step 6 — Age Bracket Conversion:** Age is stored as string decade brackets (e.g., `[70-80)`). Each bracket is mapped to its numeric midpoint (e.g., `[70-80)` → 75) creating a new `age_midpoint` column. This enables use of age in correlation analysis, regression, and continuous visualisations.

**Step 7 — Target Variable Encoding:** The `readmitted` column (three classes: `<30`, `>30`, `NO`) is encoded as a binary variable. `<30` maps to 1 (positive class — clinically penalised readmission); `>30` and `NO` both map to 0. This is consistent with the CMS HRRP definition which specifically targets 30-day readmissions.

**Steps 8–9 — ID Column Mapping:** `admission_type_id` is mapped to four human-readable labels (Emergency, Urgent, Elective, Other) using the IDS_mapping reference file. `discharge_disposition_id` is consolidated from 26 codes into 5 categories (Home, SNF, Home Health, Unknown, Other Transfer), with expired patients already removed in Step 4.

**Step 10 — Patient Deduplication:** The dataset contains 30,248 repeat encounters from the same patients. Retaining all encounters risks data leakage — a patient's known readmission from a later encounter could influence modelling of earlier ones. We sort by `encounter_id` and retain only the first encounter per `patient_nbr`, reducing the dataset to 71,518 unique patient records.

**Output:** The cleaned dataset is saved to `data/processed/diabetes_cleaned.csv` (71,518 rows × 18 columns).

---

## 5. KPI Framework

| KPI | Formula | Business Purpose | Benchmark |
|---|---|---|---|
| 30-Day Readmission Rate | `SUM(readmitted=1) / COUNT(*)` | Primary quality metric; directly tied to CMS penalties | < 11% (HRRP national target) |
| Avg Length of Stay (Readmitted) | `AVG(time_in_hospital) WHERE readmitted=1` | Cost driver; longer stays = higher cost | < 5 days |
| Avg Length of Stay (Not Readmitted) | `AVG(time_in_hospital) WHERE readmitted=0` | Baseline comparison | < 4.5 days |
| Avg Medications at Discharge | `AVG(num_medications)` | Treatment complexity indicator | < 15 medications |
| Emergency Readmission Rate | `SUM(readmitted=1) / COUNT(*) WHERE admission_type=Emergency` | Highest-risk segment KPI | < 13% |
| Insulin Instability Readmission Rate | `SUM(readmitted=1) / COUNT(*) WHERE insulin IN (Up, Down)` | Treatment protocol indicator | < 12% |

---

## 6. EDA Insights

**[CHART PLACEHOLDER — Chart 1: Readmission Rate by Age Group]**

Patients aged 10–20 show the highest recorded 30-day readmission rate in the dataset, likely reflecting the clinical complexity of paediatric and young-adult diabetic cases with poorly established management routines. The 40–90 age band — which represents over 90% of the patient population — maintains a broadly consistent readmission rate, indicating that age alone is insufficient as a risk stratifier within the primary patient cohort.

**[CHART PLACEHOLDER — Chart 2: Readmission Rate by Race]**

Readmission rates across racial groups are broadly comparable, with no single group showing dramatically elevated risk. This finding suggests that within this dataset, clinical factors carry more predictive weight than demographic factors. However, it does not preclude the possibility that systemic disparities in care access or post-discharge support contribute to the patterns observed.

**[CHART PLACEHOLDER — Chart 3: Readmission Rate by Admission Type]**

Emergency admissions show a readmission rate meaningfully above the dataset average. Elective admissions — where care is planned and patients are more clinically prepared — have the lowest readmission rates. This finding has direct operational implications: emergency discharge protocols should be structurally different from elective discharge pathways.

**[CHART PLACEHOLDER — Chart 4: Length of Stay vs Readmission]**

Readmitted patients show a slightly higher median length of stay, but the distributions overlap substantially. Length of stay is a supporting indicator of clinical complexity rather than a standalone predictor of readmission. Hospitals should not interpret shorter stays as a readmission risk reducer without considering the full clinical profile.

**[CHART PLACEHOLDER — Chart 5: Medication Count vs Readmission]**

Readmitted patients are prescribed significantly more medications on average than non-readmitted patients. The upper quartile of medication users is disproportionately represented among readmissions, making medication count one of the most operationally useful risk signals available at discharge.

**[CHART PLACEHOLDER — Chart 6: Insulin Usage and Readmission]**

Patients whose insulin was titrated upward or downward during admission show higher readmission rates than those on steady or no insulin. This pattern is consistent with blood glucose instability at the point of discharge — a known clinical risk factor for rapid deterioration in diabetic patients.

---

## 7. Statistical Analysis Results

**Test 1 — Chi-Square: Race vs Readmission**
The chi-square test returned a statistically significant result (p < 0.05), indicating that readmission rates differ across racial groups. However, the practical effect size is modest. The association likely reflects systemic differences in care quality, insurance coverage, and post-discharge social support across groups rather than an intrinsic clinical relationship.

**Test 2 — Chi-Square: Admission Type vs Readmission**
A highly significant association was confirmed between admission type and 30-day readmission (p < 0.05). Emergency admissions are significantly more likely to result in 30-day readmission than elective or urgent admissions. This validates the EDA observation and provides a statistically grounded basis for targeting emergency discharge planning.

**Test 3 — Point-Biserial: Time in Hospital vs Readmission**
A weak but statistically significant positive correlation was found between length of stay and readmission. Patients who are readmitted tend to have marginally longer initial stays. The weak effect size confirms that time in hospital alone cannot serve as a readmission risk proxy.

**Test 4 — Point-Biserial: Medications vs Readmission**
A statistically significant positive correlation was found between number of medications and readmission. The effect is stronger than for length of stay, confirming that treatment complexity — as proxied by medication count — is a more useful readmission risk indicator than administrative stay duration.

**Test 5 — Logistic Regression**
A logistic regression model trained on five clinical features (age midpoint, time in hospital, medications, lab procedures, diagnoses) produced statistically significant coefficients for the majority of features. Number of medications and number of diagnoses showed the highest positive coefficients, confirming their role as the strongest linear predictors of readmission within this feature set. Model accuracy reflects the class imbalance in the target variable; recall for the positive class (readmitted) is the more operationally relevant metric.

**Test 6 — ANOVA: Time in Hospital across Admission Types**
One-way ANOVA confirmed a statistically significant difference in mean length of stay across admission types (p < 0.05). Emergency admissions result in longer average stays than elective admissions, compounding their cost impact and readmission risk. Post-hoc analysis would be required to identify specific pairwise differences.

---

## 8. Dashboard Overview

**[SCREENSHOT PLACEHOLDER — Full Dashboard]**

The Tableau Public dashboard — *Diabetic Patient Readmission Risk Dashboard* — is structured across six sheets assembled into a single interactive view. The top KPI banner presents three headline metrics: total unique patients, average length of stay, and overall 30-day readmission rate. The second row presents readmission rates broken down by age group and admission type, enabling clinicians to identify the highest-risk demographic and admission pathway combinations. The third row compares average length of stay between readmitted and non-readmitted patients and visualises insulin usage patterns by readmission outcome. The bottom panel presents a risk heatmap crossing age group against admission type — the single most actionable view for targeted intervention prioritisation.

All four global filters (Age Group, Admission Type, Gender, Readmission Outcome) apply across every sheet simultaneously, allowing hospital operations teams to drill into specific patient segments interactively.

---

## 9. Key Insights

1. **Emergency admissions have the highest 30-day readmission rate** — exceeding the dataset average and representing the single highest-priority intervention target.
2. **Patients on 20+ medications at discharge face disproportionately high readmission risk** — medication complexity is a more reliable risk signal than length of stay.
3. **Insulin dose adjustments during admission are associated with higher readmission rates** — blood glucose instability at discharge is a measurable and preventable risk factor.
4. **The 60–80 age group represents the largest patient segment** with consistently elevated readmission rates — any hospital-wide readmission reduction programme will have its largest absolute impact in this cohort.
5. **Race shows a statistically significant but practically modest association with readmission** — differences likely reflect systemic access disparities rather than clinical factors.
6. **Patients with 9+ concurrent diagnoses face compounded readmission risk** — high comorbidity burden should be a mandatory trigger for structured post-discharge support.
7. **Elective admissions have the lowest readmission rates** — confirming that planned care with structured pre-admission protocols reduces post-discharge risk.
8. **Length of stay is a weak standalone predictor** — short stays do not reduce readmission risk if the patient's clinical profile remains complex at discharge.
9. **77% of patients are on diabetes medication** — diabetesMed alone is not a differentiating factor; insulin management and polypharmacy are more informative.
10. **A composite multi-feature risk score outperforms any single variable** — operational readmission risk tools should incorporate at minimum: admission type, medication count, diagnosis count, and insulin status.

---

## 10. Business Recommendations

*(Full text in `reports/business_recommendations.md`)*

1. **Deploy Emergency Admission Discharge Risk Scoring** — target 900+ prevented readmissions annually, saving ~$2.7M per hospital
2. **Enrol High-Medication Patients in Post-Discharge Medication Reconciliation** — 500–900 readmissions prevented, backed by published 14–27% reduction trials
3. **Introduce Insulin Stability Clearance Protocol Before Discharge** — ~260 fewer readmissions for insulin-titrated patients
4. **Establish a High-Comorbidity Transitional Care Programme** — 380 readmissions prevented, saving ~$1.1M
5. **Build a Real-Time Readmission Risk Scoring Dashboard in EHR** — 800+ fewer avoidable readmissions, worth $2.4M annually

---

## 11. Limitations & Future Scope

**Limitations:** The dataset spans 1999–2008, meaning clinical protocols, medication availability, and care standards have evolved substantially since data collection. The deduplication step (keeping first encounter only) discards longitudinal patient data that could improve model accuracy. The binary target encoding collapses `>30` readmissions into the negative class, discarding a clinically meaningful signal. Logistic regression, while interpretable, may underperform more sophisticated ensemble methods on this data structure.

**Future Scope:** Future iterations should incorporate ICD-9 diagnosis codes to capture disease-specific readmission drivers. A time-series model tracking individual patient trajectories across multiple encounters would unlock longitudinal risk profiling. Applying gradient boosting (XGBoost, LightGBM) with SHAP explainability would improve both predictive accuracy and clinical interpretability. Integration with live EHR systems would transform the static analysis into a real-time clinical decision support tool.

---

## 12. Contribution Matrix

| Task | Raman | Teammate 2 | Teammate 3 | Teammate 4 | Teammate 5 |
|---|---|---|---|---|---|
| GitHub repo setup & README | ✅ | | | | |
| Data dictionary (`docs/`) | ✅ | | | | |
| Notebook 01 — Ingestion | ✅ | | | | |
| Notebook 02 — Cleaning | ✅ | | | | |
| Notebook 03 — EDA | | ✅ | | | |
| Notebook 04 — Statistical Analysis | | | ✅ | | |
| Notebook 05 — KPI & Tableau Export | | | | ✅ | |
| Tableau Dashboard Build | | | | ✅ | |
| Business Recommendations | | | | | ✅ |
| Gate 1 Proposal | | | | | ✅ |
| Final Report (PDF) | | | | | ✅ |
| PR Reviews | ✅ | ✅ | ✅ | ✅ | ✅ |

<!-- updated by Ashish Singh Naruka -->
