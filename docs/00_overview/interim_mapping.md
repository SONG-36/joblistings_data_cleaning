# Interim Field Mapping

## Design Principles

- Interim layer focuses on **structural normalization**, not value judgment.
- No records are dropped at this stage.
- No business assumptions are introduced.
- Raw information must be preserved and traceable.

## Raw to Interim Field Mapping

| Raw Field | Interim Field(s) | Transformation Type | Notes |
|----------|------------------|---------------------|-------|
| company | Company | Keep | Direct mapping |
| description | description_raw | rename | Preserve full text |
| location | location_raw | rename | No standardization yet |
| category | category | keep | Controlled vocabulary |
| subcategory | subcategory | keep | May contain missing |
| role | role | keep | Normalized later if needed |
| type | employment_type | rename | Case normalization later |
| listingDate | listing_date | rename | ISO format preserved |
| salary | salary_raw | split | Overloaded semantic field |

## Salary Field Decomposition

The raw `salary` field mixes multiple semantic dimensions and must be decomposed.
| Interim Field | Description |
|--------------|-------------|
| salary_raw | Original salary text |
| salary_type | missing / negotiable / fixed / range / lower_bound / upper_bound / unparseable |
| salary_min | Lower numeric bound (if available) |
| salary_max | Upper numeric bound (if available) |
| salary_period | monthly / yearly / hourly / unknown |
| currency | Raw currency symbol or code |

## Out of Scope for Interim Layer

- Salary currency conversion
- Period normalization (hourly → monthly)
- Inflation or cost-of-living adjustment
- Salary reasonableness checks
- Outlier removal

## Conclusion

The interim mapping defines a stable, analysis-ready schema
while preserving all raw information.
This enables downstream cleaning and modeling
without losing traceability to the original data source.

