import pandas as pd
import numpy as np

IN_FILE = "data/interim/jobs_interim.csv"
OUT_FILE = "data/processed/jobs_salary_parsed_v0.1.csv"

# Rule 2: Negotiable keywords
NEGOTIABLE_KEYWORDS = [
    "negotiable",
    "nego",
    "面议",
    "discuss"
]


def parse_salary(text: str) -> dict:
    """
    Parse raw salary text into structured salary fields.

    Implemented rules (so far):
    - Rule 1: Missing Salary
    - Rule 2: Negotiable / 面议
    """

    result = {
        "salary_type": None,
        "salary_min": np.nan,
        "salary_max": np.nan,
        "salary_period": "unknown"
    }

    # ---------- Rule 1: Missing Salary ----------
    if pd.isna(text) or str(text).strip() == "":
        result["salary_type"] = "missing"
        return result

    text_l = str(text).lower()

    # ---------- Rule 2: Negotiable ----------
    for kw in NEGOTIABLE_KEYWORDS:
        if kw in text_l:
            result["salary_type"] = "negotiable"
            return result

    # ---------- Placeholder for future rules ----------
    result["salary_type"] = "unparsed"
    return result


def main():
    df = pd.read_csv(IN_FILE)

    # Preserve original salary text
    df["salary_raw"] = df["salary"]

    # Apply parsing
    parsed_df = df["salary"].apply(parse_salary).apply(pd.Series)

    # Merge results
    df = pd.concat([df, parsed_df], axis=1)

    df.to_csv(OUT_FILE, index=False)
    print(f"[DONE] Saved {len(df)} rows to {OUT_FILE}")


if __name__ == "__main__":
    main()
