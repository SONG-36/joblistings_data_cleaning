# Data Issues Analysis

## Background
The dataset is sourced from Kaggle and provided in CSV format.
Although the data is already structured, several critical fields are not analysis-ready.

---

## 1. Missing Values
The salary field contains a large number of missing values.
These missing values are not random and may reflect real-world business decisions.

Decision:
- Do not drop missing salary records.
- Explicitly preserve missing salary as a category.

---

## 2. Inconsistent Representations
The salary field is expressed in multiple textual formats, including ranges, single values, negotiable terms, and empty values.

This inconsistency prevents direct numerical comparison or aggregation.

---

## 3. Overloaded Field Semantics
The salary field mixes numeric values, salary periods, and business semantics in a single column.

This violates normalization principles and requires structural decomposition.

---

## 4. Non-numeric Anomalies
Values such as "Negotiable" or "面议" are neither numeric nor missing.
They must be treated as explicit categories rather than discarded.

---

## 5. Raw Field Inspection (B9)

This section documents a direct inspection of raw CSV fields
before any transformation or cleaning is applied.

### 5.1 Raw Field Overview

| Field Name   | Raw Type | Example Value | Can Be Used Directly? | Notes |
|-------------|----------|---------------|------------------------|-------|
| company     | string   | Coca-Cola Bottlers (Malaysia) Sdn Bhd | Yes | Clean company name |
| description | string   | Long free-text job description | No | Unstructured, mixed content |
| location    | string   | Negeri Sembilan | Partially | Granularity varies (state / city) |
| category    | string   | Manufacturing, Transport & Logistics | Yes | Controlled vocabulary |
| subcategory | string   | Purchasing, Procurement & Inventory | Mostly | Sometimes missing |
| role        | string   | procurement-executive | Yes | Hyphen-separated |
| type        | string   | Full time | Yes | Case inconsistent |
| salary      | string   | RM 2,800 – RM 3,200 | No | Mixed semantics |
| listingDate | string   | 2024-03-21T05:58:35Z | Yes | ISO-8601 format |

### 5.2 Field-Level Conclusions

- Most categorical fields (company, category, role, type) are analysis-ready.
- The `description` field requires NLP-specific processing and is out of scope for basic analysis.
- The `salary` field is the primary blocker for numerical analysis and requires structural decomposition.
- No fields are dropped at this stage; all issues are explicitly documented.

## Conclusion
Although the dataset is provided in a structured CSV format, it should be treated as structured raw data.
Further transformation is required before it can be used for analysis or modeling.
