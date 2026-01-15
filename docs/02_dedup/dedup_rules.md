# Deduplication Rules

## Background
Job posting data may contain duplicated entries due to
multi-source aggregation or repeated scraping.

This document defines business rules for identifying duplicates.

---

## Scope
This deduplication step only handles **strict duplicates**.
Probable duplicates are intentionally excluded to avoid false removal.

---

## Definition of Strict Duplicate

Two job records are considered strict duplicates if ALL of the following fields are identical:

- company
- role
- location
- employment_type

Salary and listing date are NOT used as deduplication keys
at this stage.

---

## Rationale

- These fields jointly define the core business identity of a job posting.
- Minor salary or date variations may occur across reposts and should not block deduplication.
- Restricting to strict duplicates minimizes data loss risk.

---

## Out of Scope

- Probable duplicates with partial field mismatch
- Semantic similarity or fuzzy matching
- Cross-location role aggregation
