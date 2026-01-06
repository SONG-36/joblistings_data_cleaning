# Job Dataset Schema

## Purpose
This schema defines the structured format of cleaned job posting data,
designed for analysis and downstream applications.

Fields are classified based on data availability and processing stage.

---

## Fields

| Field Name      | Type    | Description                                   | Required | Notes |
|---------------|---------|-----------------------------------------------|----------|-------|
| job_id        | string  | Generated job identifier (hash)               | No       | Generated in processed stage |
| job_title     | string  | Title of the job position                     | Yes      | Raw field |
| company       | string  | Company offering the job                      | No       | May be missing or confidential |
| location      | string  | Raw job location text                         | Yes      | Free-text |
| is_remote     | boolean | Whether the job is remote                     | No       | Derived field |
| salary_raw    | string  | Original salary text                          | No       | From raw |
| salary_type   | string  | Salary category (missing, range, negotiable…) | No       | Derived from rules |
| salary_min    | number  | Minimum salary value                          | No       | Parsed |
| salary_max    | number  | Maximum salary value                          | No       | Parsed |
| salary_currency | string | Salary currency                               | No       | Parsed |
| salary_period | string  | Salary period (month/year/hour)               | No       | Parsed |
| job_type      | string  | Employment type                               | No       | Raw |
| posted_date   | string  | Job posting date                              | No       | Parsed to date later |
| source        | string  | Data source name                              | Yes      | Required |

---

## Design Notes

- Raw ambiguity is preserved until explicitly resolved.
- Derived fields are clearly distinguished from raw fields.
- No assumptions are made for missing values.
- Schema supports incremental enrichment.

