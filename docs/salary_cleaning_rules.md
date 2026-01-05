# Salary Cleaning Rules

## Background
Job posting salary data is highly inconsistent and partially missing.
This document defines the normalization rules applied before analysis.

---

## Rule 1: Missing Salary
- Definition:
  Salary field is empty or null.
- Decision:
  Keep the record.
- Handling:
  - salary_type = "missing"
  - salary_min = NaN
  - salary_max = NaN
- Rationale:
  Many real-world job postings do not disclose salary.
  Dropping them would introduce sampling bias.

---

## Rule 2: Negotiable / 面议
- Definition:
  Salary text contains keywords such as "Negotiable", "面议".
- Decision:
  Treat as a distinct category.
- Handling:
  - salary_type = "negotiable"
  - salary_min = NaN
  - salary_max = NaN
- Rationale:
  Negotiable salary conveys business information and should not be treated as missing.

---

## Rule 3: Salary Period
- Supported periods:
  - Monthly
  - Yearly
  - Hourly
- Handling:
  - Extract numeric values
  - Normalize period into salary_period field
- Rationale:
  Preserve full information for downstream analysis.

---

## Rule 4: Single Value Salary
- Definition:
  Salary contains a single numeric value.
- Decision:
  Treat as fixed salary.
- Handling:
  - salary_min = salary_max = value
  - salary_type = "fixed"
- Rationale:
  Enables unified numeric processing without losing information.
