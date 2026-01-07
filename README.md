# Job Listings Data Cleaning Pipeline

## Project Overview

This project builds a **reproducible data cleaning pipeline**
to transform raw job listing data into a structured,
analysis-ready dataset.

The focus is on **real-world data quality problems**, including:

* Inconsistent salary formats
* Duplicate job postings
* Overloaded text fields with mixed semantics

The project emphasizes **decision transparency** and
**business-aligned data cleaning**, rather than blind preprocessing.

---

## Data Source

* Source: Public job listings dataset (CSV format)
* Origin: Kaggle
* Scale: ~69,000 records

Although the data is provided as CSV,
it should be treated as **structured raw data**,
not directly usable analytical input.

Key issues include:

* Free-text salary descriptions
* Reposted job listings
* Mixed business semantics in single fields

---

## Pipeline Structure

```
data/raw
   ↓
data/interim
   ↓
data/processed
```

### Stage Definitions

* **Raw**
  Original dataset, untouched.

* **Interim**
  Schema-aligned staging data.
  No filtering, no deletion, no business decisions.

* **Processed**
  Business-rule–aware cleaned datasets,
  suitable for analysis and downstream AI tasks.

---

## Processing Stages

### Stage 1: Data Issue Analysis

* Identified missing values, semantic overload,
  and inconsistent representations.
* No code written at this stage.
* Decisions documented before implementation.

Document:

* `docs/data_issues_analysis.md`

---

### Stage 2: Salary Rule Design

* Explicit salary normalization rules designed
  **before** coding.
* Covered patterns:

  * Missing salary
  * Negotiable salary
  * Fixed value
  * Range (min–max)
  * Directional (from / up to)

Document:

* `docs/salary_cleaning_rules.md`

---

### Stage 3: Deduplication

* Removed duplicate job postings based on
  **business semantics**, not naive text matching.

Deduplication criteria:

* Same company
* Same role
* Same location
* Same salary text (if present)

#### Quantitative Result

| Metric      | Value        |
| ----------- | ------------ |
| Rows before | 69,024       |
| Rows after  | 68,749       |
| Removed     | 275 (≈0.40%) |

Supporting documents:

* Row-level examples: `docs/dedup_examples.md`
* Impact analysis: `docs/dedup_impact_analysis.md`

---

## Current Status

* ✅ Data issue analysis completed
* ✅ Salary rule design completed
* ✅ Deduplication completed
* ⏳ Salary normalization (next stage)
* ⏳ Fully analysis-ready dataset (planned)

---

## Output Artifacts

| File                                   | Description                    |
| -------------------------------------- | ------------------------------ |
| `data/interim/jobs_interim.csv`        | Schema-aligned staging dataset |
| `data/processed/jobs_dedup_strict.csv` | Deduplicated dataset           |

---

## Design Principles

* Decisions precede implementation
* Cleaning is conservative to avoid data loss
* Business semantics are preserved
* All transformations are traceable

---

## Next Steps

* Implement salary normalization based on documented rules
* Produce a fully normalized dataset
* Enable salary analytics and AI applications
