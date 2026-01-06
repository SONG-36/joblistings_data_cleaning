# Job Listings Data Cleaning

## Project Goal

Transform raw job listing data into a structured, analysis-ready dataset
through explicit, documented, and reproducible data processing steps.

This project focuses on data understanding, normalization, and rule design,
rather than premature modeling or visualization.

---

## Data Source

- Source: Kaggle – JobStreet Job Postings Dataset
- Format: CSV
- Nature:
  - Tabular and structured
  - Not analysis-ready
  - Contains overloaded and ambiguous fields

Although the data is provided as CSV, it is treated as structured raw data.

---

## Project Structure

data/
├── raw/        # Original source data (not tracked)
├── interim/    # Structured but uncleaned data (not tracked)
├── sample/     # Small representative samples (tracked)
└── processed/  # Final cleaned dataset (future)

docs/
├── schema.md
├── data_issues.md
├── salary_cleaning_rules.md

scripts/
├── build_interim.py   # Raw → Interim (structure only)
└── (future parsing & cleaning scripts)

README.md

---

## Data Processing Philosophy

The pipeline follows a strict staged design:

Raw → Interim → Processed

### Raw
- Direct output from data source
- No assumptions about quality
- No modification
- Not version-controlled

### Interim
- Column names standardized
- Field meanings made explicit
- No cleaning or judgment applied
- Ambiguity is preserved

### Processed (future)
- Rule-based cleaning
- Numeric normalization
- Ready for analysis or modeling

---

## Identified Data Issues

Documented in docs/data_issues.md.

Key issues:

1. Missing Values  
   Salary is frequently missing and non-random.

2. Inconsistent Representations  
   Salary appears as ranges, single values, text, or negotiable terms.

3. Overloaded Field Semantics  
   Numeric values, periods, and business meaning are mixed in one column.

4. Non-numeric Anomalies  
   Values such as “Negotiable”, “面议”, “Competitive package”.

These prevent direct numeric analysis.

---

## Schema Design

Defined in docs/schema.md.

Key design decision:

The original salary column is decomposed into:

- salary_raw
- salary_type
- salary_min
- salary_max
- salary_period
- currency

This avoids hiding ambiguity and enables explicit rule-based normalization.

---

## Salary Normalization Rules

All salary handling rules are defined before implementation in:

docs/salary_cleaning_rules.md

Covered cases include:

- Missing salary
- Negotiable salary
- Fixed numeric salary
- Salary ranges
- Directional bounds (e.g. “Up to”, “From”)
- Unparseable salary text

No implicit assumptions are made.

---

## Current Status

Completed:
- Project initialization
- Raw data inspection
- Data issues analysis
- Target schema design
- Salary rule design
- Raw → Interim transformation
- Sample dataset generation

In Progress:
- Salary parsing and normalization implementation

Not Started:
- Final processed dataset
- Aggregation, analysis, visualization

---

## Design Principles

- One transformation per stage
- Raw data is immutable
- Rules are documented before code
- Intermediate outputs must be explainable
- Ambiguity is preserved until explicitly resolved

---

## Reproducibility

- Raw data can be re-downloaded from Kaggle
- All assumptions are documented
- Sample data is included for inspection
- Pipeline can be rerun end-to-end

---

## Next Steps

1. Validate schema completeness (must-have fields)
2. Implement salary parsing based on documented rules
3. Generate processed dataset
4. Perform downstream analysis if required
