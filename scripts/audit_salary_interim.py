"""
Salary data audit for interim dataset (B30).

Purpose:
- Inspect salary availability and explicitness
- Quantify missing vs explicit salary information
- Provide evidence for downstream inference decisions (B31)

This script performs READ-ONLY analysis.
"""

import pandas as pd

INTERIM_PATH = "data/interim/jobs_interim.csv"


def audit_salary():
    df = pd.read_csv(INTERIM_PATH)

    total_jobs = len(df)

    # Salary provided or not
    has_salary = df["salary_raw"].notna() & (df["salary_raw"].str.strip() != "")
    missing_salary = ~has_salary

    # Period explicit or missing
    explicit_period = df["salary_period_source"] == "explicit"
    missing_period = df["salary_period_source"] == "missing"

    print("=== Salary Availability Audit ===")
    print(f"Total jobs: {total_jobs}")
    print(f"Jobs with salary provided: {has_salary.sum()} ({has_salary.mean():.2%})")
    print(f"Jobs with salary missing: {missing_salary.sum()} ({missing_salary.mean():.2%})")
    print()

    print("=== Salary Period Explicitness ===")
    print(f"Explicit salary period: {explicit_period.sum()} ({explicit_period.mean():.2%})")
    print(f"Missing salary period: {missing_period.sum()} ({missing_period.mean():.2%})")
    print()

    print("=== Top Companies with Missing Salary (Top 10) ===")
    print(
        df.loc[missing_salary]
        .groupby("company")
        .size()
        .sort_values(ascending=False)
        .head(10)
    )
    print()

    print("=== Salary Missing Rate by Category ===")
    print(
        df.assign(missing_salary=missing_salary)
        .groupby("category")["missing_salary"]
        .mean()
        .sort_values(ascending=False)
    )


if __name__ == "__main__":
    audit_salary()
