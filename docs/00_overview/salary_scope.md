# Salary Cleaning Scope

## Purpose
This document defines what the project **will** and **will not** do when cleaning salary data.
The goal is to make salary information **structured, traceable, and reproducible**.

---

## What We Deliver (Outputs)

The pipeline must produce the following fields:

- `salary_raw`  
  Original salary text from the dataset. Must be preserved for traceability.

- `salary_type`  
  One of:
  - missing
  - negotiable
  - fixed
  - range
  - lower_bound
  - upper_bound
  - unparseable

- `salary_min`  
  Lower numeric bound if explicitly present and parseable, otherwise empty.

- `salary_max`  
  Upper numeric bound if explicitly present and parseable, otherwise empty.

- `salary_period`  
  One of:
  - monthly
  - yearly
  - hourly
  - unknown

- `currency`  
  Extracted currency symbol or code if present (e.g., RM, MYR, USD). Otherwise empty.

- (Optional) `parse_confidence`
  One of: high / medium / low

---

## What We Do NOT Do (Out of Scope)

To keep the pipeline conservative and reproducible, we explicitly do NOT:

- Convert currency (e.g., RM → USD)
- Convert salary period (e.g., hourly → monthly, monthly → yearly)
- Adjust for inflation or cost-of-living
- Infer salary from job title, category, seniority, or company
- Fill missing bounds with assumptions (e.g., "Up to X" does NOT imply min=0)
- Drop records with missing / negotiable salary (we classify them instead)

---

## Allowed Decisions (The Only Decisions We Make)

We only allow two types of decisions:

1. **Pattern classification**
   - Decide which `salary_type` a record belongs to based on explicit text patterns.

2. **Explicit numeric extraction**
   - Extract numeric values only when they are clearly present in the text.
   - If not explicit, leave numeric fields empty.

---

## Success Criteria

Salary cleaning is considered successful if:

- Every record keeps `salary_raw`
- Records are categorized into `salary_type`
- Numeric fields are filled only when justified by the text
- The result can be audited by sampling `salary_raw` vs parsed fields
