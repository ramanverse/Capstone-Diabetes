# Tableau Dashboard Build Guide
# Diabetic Patient Readmission Risk Dashboard

**Tool:** Tableau Public (Free)
**Data Source:** `data/processed/tableau_ready.csv`
**Published Title:** Diabetic_Readmission_Risk_Dashboard

---

## Pre-Build Setup

1. Open Tableau Public Desktop
2. Connect to Text File → select `tableau_ready.csv`
3. Verify field types:
   - `readmitted_binary` → Number (whole)
   - `time_in_hospital`, `num_medications`, `num_lab_procedures`, `number_diagnoses` → Number
   - `age_midpoint` → Number
   - All label fields → String
4. Create calculated field: **Readmission Rate**
   ```
   SUM([Readmitted Binary]) / COUNT([Encounter Id])
   ```
   Format as Percentage (2 decimal places)

---

## Sheet 1 — KPI Banner

**Business Question:** What is the overall readmission burden?

| Setting | Value |
|---|---|
| Chart Type | Text / BAN tiles (use 3 separate text marks) |
| Tile 1 | `COUNT([Encounter Id])` — label: "Total Patients" |
| Tile 2 | `AVG([Time In Hospital])` — label: "Avg Length of Stay (Days)" — format: 1 decimal |
| Tile 3 | `[Readmission Rate]` — label: "30-Day Readmission Rate" — format: % |
| Font | Bold, 36pt for numbers, 12pt for labels |
| Background | Dark navy (#1a2235) with white text for premium look |
| Sheet Name | `KPI_Banner` |

---

## Sheet 2 — Readmission Rate by Age Group

**Business Question:** Which age groups carry the highest readmission risk?

| Setting | Value |
|---|---|
| Chart Type | Horizontal Bar Chart |
| Rows | `Age Group` |
| Columns | `[Readmission Rate]` (calculated field) |
| Sort | Descending by Readmission Rate |
| Color | Single blue gradient — darker = higher rate |
| Labels | Show `[Readmission Rate]` on end of each bar |
| Reference Line | Add average line across all bars |
| Sheet Name | `Readmission_By_Age` |

**Steps:**
1. Drag `Age Group` to Rows
2. Drag `Readmission Rate` to Columns
3. Right-click axis → Add Reference Line → Average
4. Right-click bars → Add Labels

---

## Sheet 3 — Readmission by Admission Type

**Business Question:** Do emergency admissions readmit more than elective?

| Setting | Value |
|---|---|
| Chart Type | Bar Chart |
| Columns | `Admission Type` |
| Rows | `[Readmission Rate]` |
| Color | Red if above average, blue if below (use calculated color field) |
| Reference Line | Overall average readmission rate |
| Labels | Percentage on top of each bar |
| Sheet Name | `Readmission_By_Admission` |

**Color Calculated Field:**
```
IF [Readmission Rate] > WINDOW_AVG(SUM([Readmitted Binary])/COUNT([Encounter Id]))
THEN "Above Average"
ELSE "Below Average"
END
```

---

## Sheet 4 — Time in Hospital vs Readmission

**Business Question:** Do longer stays reduce readmissions?

| Setting | Value |
|---|---|
| Chart Type | Side-by-side bar |
| Rows | `Readmission Label` |
| Columns | `AVG([Time In Hospital])` |
| Color | Green = Not Readmitted, Red = Readmitted |
| Labels | Show average value |
| Sheet Name | `LOS_vs_Readmission` |

---

## Sheet 5 — Insulin Usage and Readmission

**Business Question:** Does insulin treatment affect readmission risk?

| Setting | Value |
|---|---|
| Chart Type | Bar Chart |
| Columns | `Insulin` |
| Rows | `[Readmission Rate]` |
| Color | Purple gradient by rate |
| Sort | Descending |
| Labels | Rate % on bars |
| Sheet Name | `Insulin_Readmission` |

---

## Sheet 6 — Readmission Heatmap

**Business Question:** Which age + admission type combination is highest risk?

| Setting | Value |
|---|---|
| Chart Type | Highlight Table (Heatmap) |
| Rows | `Age Group` |
| Columns | `Admission Type` |
| Values (Color) | `[Readmission Rate]` |
| Color Palette | Orange-Red diverging (low=white, high=dark red) |
| Labels | Show rate % in each cell |
| Sheet Name | `Risk_Heatmap` |

---

## Dashboard Assembly

**Canvas Size:** 1200 × 800 px (fixed)

```
┌─────────────────────────────────────────────┐
│            KPI_Banner  (full width)          │  Row 1 — height 120px
├─────────────────────────┬───────────────────┤
│   Readmission_By_Age    │ Readmission_By_   │  Row 2 — height 300px
│                         │ Admission         │
├─────────────────────────┬───────────────────┤
│   LOS_vs_Readmission    │ Insulin_          │  Row 3 — height 300px
│                         │ Readmission       │
├─────────────────────────────────────────────┤
│           Risk_Heatmap  (full width)         │  Row 4 — height 280px
└─────────────────────────────────────────────┘
```

---

## Global Filters (Apply to All Sheets)

Add these filters to the dashboard and set **"Apply to All Worksheets Using This Data Source"**:

| Filter | Type | Field |
|---|---|---|
| Age Group | Dropdown (Single Select) | `Age Group` |
| Admission Type | Checkbox (Multi-Select) | `Admission Type` |
| Gender | Radio Button | `Gender` |
| Readmission Outcome | Toggle | `Readmission Label` |

---

## Publishing Steps

1. File → Save to Tableau Public As...
2. Name: `Diabetic_Readmission_Risk_Dashboard`
3. Copy the public URL
4. Paste into `tableau/dashboard_links.md`
5. Take screenshots of each sheet and the full dashboard
6. Save to `tableau/screenshots/`
7. Commit: `git add tableau/ && git commit -m "feat: add Tableau dashboard screenshots and URL"`
