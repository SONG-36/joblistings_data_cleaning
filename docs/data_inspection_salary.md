# Salary Field Inspection (Human Review)

## Background

This project uses a public job postings dataset sourced from Kaggle (JobStreet Malaysia).

Although the dataset is provided in CSV format and appears structured, the `salary` field is **not analysis-ready** and requires careful inspection before any transformation or cleaning is applied.

This document records **manual inspection results** of the raw `salary` field to guide downstream design decisions.

---

## Dataset Context

- Source: Kaggle – JobStreet Malaysia job postings  
- Format: CSV  
- Record scale: Large-scale job listings  
- Inspection method: Manual inspection of raw CSV values (no transformation applied)

---

## What Does `salary_raw` Look Like?

After manually inspecting the raw CSV file, the `salary` field (`salary_raw`) is observed to be **free-form text**, not numeric data.

The content can be grouped into several recurring patterns.

---

## Pattern 1: Monthly Salary Range (Most Common)

Examples:
RM 2,800 – RM 3,200 per month
RM 3,000 – RM 3,500 per month
RM 5,000 – RM 7,000 per month
RM 1,600 – RM 2,000 per month


Characteristics:

- Currency symbol present (`RM`)
- Two numeric values representing a range
- Explicit salary period (`per month`)
- Textual separators (`–`, `-`)
- Human-readable business format

This is the **dominant pattern** in the dataset.

---

## Pattern 2: Single Salary Value with Period

Examples:

RM 3,000 per month
RM 5,000 per month


Characteristics:

- Only one numeric value
- Still embedded in free text
- Requires normalization for numeric processing
- Salary period is explicit

---

## Pattern 3: Missing Salary Values

Many records have an empty salary field:

salary_raw = NaN / empty


Observations:

- Missing salaries appear across different industries and roles
- Salary omission reflects real-world hiring practices
- Missing does not imply invalid or erroneous data

---

## Pattern 4: Non-Numeric Salary Descriptions (Rare)

Examples (common in job datasets, though rare in this sample):

Negotiable
Depends on experience
Market rate


Characteristics:

- No numeric information
- Contains business semantics
- Cannot be converted into numeric values
- Should not be silently dropped

---

## Frequency Observations

Based on manual inspection:

1. Monthly salary ranges are the most frequent pattern  
2. Missing salary values are the second most frequent  
3. Single-value salaries exist but are less common  
4. Negotiable or semantic-only salaries are rare  

This distribution reflects **real-world job market behavior**, not data corruption.

---

## Why `salary_raw` Is Not Analysis-Ready

Despite being delivered in CSV format, the `salary_raw` field violates several normalization principles:

- Numeric values, currency, salary period, and semantics are mixed in one column
- Direct aggregation or comparison is impossible
- Missing values carry business meaning
- Salary period cannot be separated without parsing

Therefore, this dataset must be treated as **structured raw data**, not cleaned data.

---

## Implications for Downstream Processing

This inspection leads to the following conclusions:

- The salary field must be **structurally decomposed**
- Numeric bounds must be extracted without assumptions
- Missing and non-numeric salaries must be explicitly preserved
- Parsing rules must prioritize information preservation over convenience

These findings directly inform the design of the interim schema and salary normalization rules.

---

## Status

- Manual inspection completed  
- No transformation or cleaning applied  
- Patterns documented for reproducibility  
- Ready to proceed to structural decomposition (Raw → Interim)

