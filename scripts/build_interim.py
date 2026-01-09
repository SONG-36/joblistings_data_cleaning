"""
Build interim dataset from raw job postings.

B30 scope:
- Read raw job data
- Preserve original salary text (salary_raw)
- Extract ONLY explicitly stated salary period and currency
- Attach source and confidence for full traceability
- Write structured interim dataset

IMPORTANT:
- No inference
- No normalization
- No salary conversion
"""

import pandas as pd

from src.salary.parse_salary_period import (
    extract_salary_period,
    extract_currency,
)


RAW_PATH = "data/raw/jobs_raw.csv"
INTERIM_PATH = "data/interim/jobs_interim.csv"


def build_interim() -> None:
    """
    Build interim job dataset with structured salary metadata.

    The interim dataset is designed to be:
    - Auditable: every derived field can be traced back to salary_raw
    - Reversible: no irreversible transformation is applied
    - Extendable: future inference stages can be layered on top
    """
    # Load raw job data (immutable input)
    df = pd.read_csv(RAW_PATH)

    # Preserve original salary text for traceability
    # This column MUST remain unchanged in all downstream stages
    df["salary_raw"] = df["salary"]

    # Extract salary period and currency from raw text
    period_results = df["salary_raw"].apply(extract_salary_period)
    currency_results = df["salary_raw"].apply(extract_currency)

    # Expand salary period fields
    df["salary_period"] = period_results.apply(
        lambda x: x["salary_period"]
    )
    df["salary_period_source"] = period_results.apply(
        lambda x: x["salary_period_source"]
    )
    df["salary_period_confidence"] = period_results.apply(
        lambda x: x["salary_period_confidence"]
    )

    # Expand currency fields
    df["currency"] = currency_results.apply(
        lambda x: x["currency"]
    )
    df["currency_source"] = currency_results.apply(
        lambda x: x["currency_source"]
    )

    # Write interim dataset
    df.to_csv(INTERIM_PATH, index=False)

    print(f"[OK] Interim dataset written to: {INTERIM_PATH}")
    print(f"[INFO] Total records processed: {len(df)}")


if __name__ == "__main__":
    build_interim()
