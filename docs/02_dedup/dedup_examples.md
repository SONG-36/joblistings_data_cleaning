# Deduplication Examples

This document provides concrete before/after examples to explain
the business rationale behind the deduplication logic applied in this project.

---

## Example 1: Identical Job Posted Multiple Times

### Before (Raw / Interim)

| company | role | location | salary_raw |
|-------|------|----------|------------|
| Coca-Cola Bottlers (Malaysia) Sdn Bhd | procurement-executive | Negeri Sembilan | NaN |
| Coca-Cola Bottlers (Malaysia) Sdn Bhd | procurement-executive | Negeri Sembilan | NaN |

### Observation
- Same company  
- Same role  
- Same location  
- No distinguishing salary information  

### Decision
These records represent the same job posting.  
One record is retained, the other is removed.

### After (Deduped)

| company | role | location | salary_raw |
|-------|------|----------|------------|
| Coca-Cola Bottlers (Malaysia) Sdn Bhd | procurement-executive | Negeri Sembilan | NaN |

---

## Example 2: Duplicate Job with Salary Range

### Before

| company | role | location | salary_raw |
|-------|------|----------|------------|
| Acoustic & Lighting System Sdn Bhd | executive-assistant | Petaling | RM 2,800 – RM 3,200 per month |
| Acoustic & Lighting System Sdn Bhd | executive-assistant | Petaling | RM 2,800 – RM 3,200 per month |

### Observation
- Salary text is identical  
- No additional distinguishing attributes  

### Decision
Treated as repeated publication of the same job.

### After

| company | role | location | salary_raw |
|-------|------|----------|------------|
| Acoustic & Lighting System Sdn Bhd | executive-assistant | Petaling | RM 2,800 – RM 3,200 per month |

---

## Example 3: Same Role, Different Salary → NOT Deduplicated

### Before

| company | role | location | salary_raw |
|-------|------|----------|------------|
| MODE FAIR SDN BHD | software-quality-assurance-analyst | Kuala Lumpur | RM 4,000 – RM 6,000 |
| MODE FAIR SDN BHD | software-quality-assurance-analyst | Kuala Lumpur | RM 5,000 – RM 7,000 |

### Observation
- Salary ranges differ  
- Likely represent different seniority levels or different posting periods  

### Decision
Records are **not considered duplicates**.  
Both records are retained.

---

## Summary

Deduplication in this project is based on **business semantics**, not raw text equality.
Only postings that represent the *same job opportunity* are collapsed.
