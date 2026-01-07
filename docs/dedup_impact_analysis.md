# Deduplication Impact Analysis

This document evaluates the quantitative impact of deduplication
to ensure that duplicate removal is effective but not overly aggressive.

---

## Dataset Size Comparison

| Stage | Row Count |
|-----|----------|
| Before Deduplication | 69,024 |
| After Deduplication  | 68,749 |
| Removed Rows         | 275 |

---

## Removal Ratio

- Removal ratio: **0.40%**

---

## Interpretation

- The removal ratio is low (<1%), indicating conservative deduplication.
- Removed records are primarily exact or near-exact repostings of the same job.
- The majority of records are preserved, avoiding over-collapse of distinct roles.

---

## Conclusion

Deduplication reduces redundant noise while preserving
the diversity and integrity of the original dataset.
The resulting dataset is suitable for downstream salary normalization
and analytical tasks.
