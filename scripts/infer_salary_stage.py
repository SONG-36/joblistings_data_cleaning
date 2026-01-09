"""
B31-A: Controlled inference for salary period and currency.

Scope:
- ONLY infer when salary_raw is present
- ONLY infer when explicit extraction is missing
- Assign LOW confidence to all inferred values
- Never override explicit values

This script produces a new stage file with inferred fields appended.
"""

import re
import pandas as pd

INPUT_PATH = "data/interim/jobs_interim.csv"
OUTPUT_PATH = "data/processed/jobs_salary.csv"


def infer_period(row):
    """Infer salary period with conservative rules."""
    if not isinstance(row["salary_raw"], str):
        return None, None, 0.0

    if row["salary_period_source"] == "explicit":
        return (
            row["salary_period"],
            row["salary_period_source"],
            row["salary_period_confidence"],
        )

    text = row["salary_raw"].lower()

    # Text-based weak signals
    if any(k in text for k in ["per month", "/month", "monthly rate", "per mo"]):
        return "monthly", "inferred", 0.6

    if any(k in text for k in ["per year", "/year", "per annum", "annually"]):
        return "yearly", "inferred", 0.6

    # Numeric heuristic (very weak)
    numbers = re.findall(r"\d+(?:,\d{3})*", text)
    if numbers:
        try:
            value = int(numbers[0].replace(",", ""))
            if 1000 <= value <= 10000:
                return "monthly", "inferred", 0.4
        except ValueError:
            pass

    return row["salary_period"], row["salary_period_source"], row["salary_period_confidence"]


def infer_currency(row):
    """Infer currency with conservative rules."""
    if not isinstance(row["salary_raw"], str):
        return None, None, 0.0

    if row["currency_source"] == "explicit":
        return row["currency"], row["currency_source"], 1.0

    text = row["salary_raw"]

    if "$" in text:
        return "USD", "inferred", 0.6

    if re.search(r"\bRM\b", text):
        return "MYR", "inferred", 0.5

    return row["currency"], row["currency_source"], 0.0


def run():
    df = pd.read_csv(INPUT_PATH)

    # Infer period
    period_results = df.apply(infer_period, axis=1, result_type="expand")
    df["salary_period"] = period_results[0]
    df["salary_period_source"] = period_results[1]
    df["salary_period_confidence_"] = period_results[2]

    # Infer currency
    currency_results = df.apply(infer_currency, axis=1, result_type="expand")
    df["currency"] = currency_results[0]
    df["currency_source"] = currency_results[1]
    df["currency_confidence"] = currency_results[2]

    df.to_csv(OUTPUT_PATH, index=False)
    print(f"[OK] salary inference written to {OUTPUT_PATH}")
    print(f"[INFO] Total records processed: {len(df)}")


if __name__ == "__main__":
    run()
