# Business Recommendations
# Diabetic Patient Readmission Risk — McKinsey-Style Recommendations

---

**Recommendation 1: Deploy Emergency Admission Discharge Risk Scoring**

- **Data Evidence:** Emergency admissions account for 53% of all encounters and show the highest 30-day readmission rate in the dataset. Chi-square test confirms a statistically significant association (p < 0.05) between admission type and readmission.
- **Action:** Hospital operations teams should implement a structured discharge risk checklist — triggered automatically for all emergency admissions — assessing medication count, diagnosis burden, and insulin stability before discharge approval.
- **Expected Impact:** Targeting the emergency cohort alone (53% of patients) with a 15% reduction in readmission rate would prevent approximately 900+ readmissions annually per hospital, saving an estimated $2.7M per year at $3,000 average readmission cost.
- **Priority:** High
- **Owner:** Emergency Department + Case Management / Discharge Planning Team

---

**Recommendation 2: Enrol High-Medication Patients in Post-Discharge Medication Reconciliation**

- **Data Evidence:** Readmitted patients are prescribed an average of 1.6 more medications than non-readmitted patients (point-biserial r is statistically significant, p < 0.05). Patients on 20+ medications are disproportionately represented in the readmitted cohort.
- **Action:** Pharmacy teams should flag all patients discharged on 18+ medications for a mandatory 72-hour post-discharge pharmacist phone review to identify dosage errors, missed prescriptions, and drug interactions.
- **Expected Impact:** Medication reconciliation programmes have demonstrated 14–27% readmission reduction in published trials for high-complexity patients. Applying this to the top quartile of medication users (~25,000 patients) could prevent 500–900 readmissions annually.
- **Priority:** High
- **Owner:** Clinical Pharmacy / Medication Management Team

---

**Recommendation 3: Introduce Insulin Stability Clearance Protocol Before Discharge**

- **Data Evidence:** Patients with insulin dose adjustments (Up or Down) during admission show higher readmission rates than those on steady or no insulin. Insulin titration is a proxy for blood glucose instability — a known driver of diabetic readmission.
- **Action:** Endocrinology teams should require a 24-hour post-titration blood glucose stability window before discharge for any patient whose insulin was adjusted during the admission. Unstable patients should receive a mandatory outpatient follow-up within 7 days.
- **Expected Impact:** A 7-day post-discharge follow-up programme for insulin-titrated patients has been shown in literature to reduce 30-day readmission by up to 20% in diabetic cohorts. Applied to the ~23,500 Up/Down insulin patients, this equates to ~260 fewer readmissions annually.
- **Priority:** High
- **Owner:** Endocrinology / Diabetes Management Team

---

**Recommendation 4: Establish a High-Comorbidity Transitional Care Programme**

- **Data Evidence:** The majority of patients present with 7–9 concurrent diagnoses. ANOVA confirms that emergency admissions — which have the highest comorbidity burden — also have the longest stays. Patients with 9+ diagnoses face compounded readmission risk from multiple disease interactions.
- **Action:** Create a Transitional Care Unit (TCU) pathway for patients with 9+ diagnoses at discharge, providing structured care coordination for the first 30 days post-discharge including scheduled home visits, telehealth check-ins at days 3, 7, and 14, and GP handover documentation.
- **Expected Impact:** Transitional care programmes for high-comorbidity patients reduce 30-day readmission by 15–25% in peer-reviewed studies. Targeting the top comorbidity quartile (~17,000 patients) with a 20% reduction = ~380 readmissions prevented annually, saving approximately $1.1M.
- **Priority:** Medium
- **Owner:** Care Coordination / Social Work / Nursing Teams

---

**Recommendation 5: Build a Real-Time Readmission Risk Scoring Dashboard for Clinicians**

- **Data Evidence:** Logistic regression across 5 clinical features (age, time in hospital, medications, lab procedures, diagnoses) produces a statistically valid readmission risk score. No single feature is sufficient — a composite score outperforms individual variables.
- **Action:** Hospital IT and clinical informatics teams should integrate the logistic regression model into the Electronic Health Record (EHR) system to surface a live readmission risk score (0–100%) on the patient dashboard for every admitted diabetic patient. Scores above 15% should trigger an automatic case management referral.
- **Expected Impact:** EHR-integrated risk scoring has been shown to reduce unnecessary discharges and improve care team alerting. A conservative 10% improvement in identifying high-risk patients before discharge, applied to 71,000 unique patients, could prevent 800+ avoidable readmissions annually worth $2.4M.
- **Priority:** Medium
- **Owner:** Clinical Informatics / Hospital IT / Medical Director

<!-- updated by Abhijeet -->
