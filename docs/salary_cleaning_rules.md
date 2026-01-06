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

## Rule 5: Salary Range (Min–Max)

- **Definition**:
   Salary text contains two numeric values representing a range.
   Examples:
  - `RM 2,800 – RM 3,200`
  - `3000 - 4000`
  - `MYR 5k to 6k`
- **Decision**:
   Treat as bounded salary range.
- **Handling**:
  - salary_type = "range"
  - salary_min = lower bound
  - salary_max = upper bound
- **Rationale**:
   Salary ranges are common in job postings and convey meaningful constraints.
   Preserving both bounds enables accurate aggregation, filtering, and comparison.

------

## Rule 6: Directional Salary (Up to / From / Above)

- **Definition**:
   Salary text contains a directional qualifier with a numeric value.
   Examples:
  - `Up to RM 5,000`
  - `From RM 3,000`
  - `Above RM 4,000`
- **Decision**:
   Preserve the known bound and leave the unknown side empty.
- **Handling**:
  - If text contains `Up to`:
    - salary_type = "upper_bound"
    - salary_min = NaN
    - salary_max = extracted value
  - If text contains `From` / `Above`:
    - salary_type = "lower_bound"
    - salary_min = extracted value
    - salary_max = NaN
- **Rationale**:
   Directional salaries encode partial constraints and should not be collapsed into fixed values.
   Keeping the known bound preserves useful information without introducing assumptions.

------

## Rule 7: Unparseable Salary Text

- **Definition**:
   Salary text does not contain numeric information and does not match known patterns.
   Examples:
  - `Depends on experience`
  - `Market rate`
  - `Competitive package`
- **Decision**:
   Treat as unquantifiable salary.
- **Handling**:
  - salary_type = "unparseable"
  - salary_min = NaN
  - salary_max = NaN
  - retain raw salary text (optional)
- **Rationale**:
   These values cannot be normalized numerically but may still hold semantic meaning.
   Explicit categorization avoids silent data loss.

------

## Optional: Currency Normalization (Future Scope)

- **Note**:
   This project does not convert currencies at the current stage.
- **Rationale**:
   Currency conversion requires external exchange rate data and temporal alignment.
   Deferring this step keeps the pipeline focused and reproducible.

------

## Optional: Out-of-Scope Items

- Daily / hourly to monthly conversion
- Inflation adjustment
- Cost-of-living normalization

These may be added in later analytical stages if required.

------

## 
