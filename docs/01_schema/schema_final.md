# Final Data Schema (Frozen)

This document defines the final frozen schema for the job dataset.

## Must-Have Fields

The following fields are required for all downstream usage:

- job_id  
- job_title  
- company  
- category  
- salary_raw  

## Salary Metadata (Structured)

These fields are included to support auditability and controlled inference:

- salary_period  
- salary_period_source (explicit | missing)  
- salary_period_confidence  

- currency  
- currency_source (explicit | missing)  
- currency_confidence  

## Optional / Contextual Fields

These fields may be missing without breaking downstream usage:

- location  
- listingDate  
- descriptions  

## Schema Freeze Decision

- [x] Schema is frozen
- [x] No additional derived fields will be added at this stage
- [x] All future logic must adapt to this schema
