# Job Dataset Schema

## Purpose
This schema defines the final structured format of cleaned job posting data,
designed for analysis and downstream applications.

## Fields

| Field Name      | Type    | Description                           | Required |
| --------------- | ------- | ------------------------------------- | -------- |
| job_id          | string  | Unique identifier of the job posting  | Yes      |
| job_title       | string  | Title of the job position             | Yes      |
| company         | string  | Company offering the job              | Yes      |
| location        | string  | Job location as text                  | Yes      |
| is_remote       | boolean | Whether the job is remote             | No       |
| salary_min      | number  | Minimum salary value                  | No       |
| salary_max      | number  | Maximum salary value                  | No       |
| salary_currency | string  | Salary currency (e.g. USD)            | No       |
| salary_period   | string  | Salary period (year/hour/month)       | No       |
| job_type        | string  | Employment type (full-time, contract) | No       |
| posted_date     | date    | Job posting date                      | No       |
| source          | string  | Data source name                      | Yes      |

## Design Rationale

- job_title: Without a title, a job posting has no meaning.
- company: Used to identify duplicate postings and for grouping analysis.
- location: Required for geographic analysis and remote classification.
- salary_min / salary_max: Salaries are often given as ranges in text form.

