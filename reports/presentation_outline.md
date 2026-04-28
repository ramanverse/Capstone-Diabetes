# Capstone 2 Presentation: Diabetic Readmission Risk

## Slide 1: Title & Team
- **Project Title:** Predicting 30-Day Hospital Readmission in Diabetic Patients
- **Group Name:** Diabetes Insights Team
- **Members:** Raman; Abhijeet; Vaibhav Singh; Ashish Singh Naruka; Ayush Shukla

## Slide 2: Business Problem
- **Question:** What clinical factors predict 30-day readmission?
- **Impact:** CMS penalties and $26B annual cost in the US.

## Slide 3: Data ETL & Quality
- **Source:** UCI ML Repository (101,766 rows).
- **Process:** ? replacement, duplicate removal (30k rows), age mid-point conversion.

## Slide 4: Key EDA Findings
- **Admission Type:** Emergency admissions have highest risk.
- **Polypharmacy:** Patients on 20+ meds are high risk.
- **Insulin:** Dose changes (Up/Down) indicate instability.

## Slide 5: Statistical Analysis
- **Chi-Square:** Validated Admission Type as significant.
- **LogReg:** Multivariable model outperforms single features.
- **ANOVA:** Emergency stays are significantly longer.

## Slide 6: Tableau Dashboard
- Interactive filters for Clinicians.
- Risk Heatmap (Age vs Admission Type).

## Slide 7: Business Recommendations
1. Emergency risk scoring.
2. Medication reconciliation.
3. Insulin stability window.

## Slide 8: Q&A
- Thank you!
