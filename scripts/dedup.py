# scripts/dedup.py
import pandas as pd
import os

INPUT_FILE = "data/interim/jobs_interim.csv"
OUTPUT_FILE = "data/processed/jobs_dedup_strict.csv"

DEDUP_KEYS = [
    "company",
    "role",
    "location",
    "salary_raw",
    "listing_date",
]

def main():
    # 1. Load interim data
    df = pd.read_csv(INPUT_FILE)

    before_rows = len(df)

    # 2. Normalize dedup keys (string safety)
    for col in DEDUP_KEYS:
        if col in df.columns:
            df[col] = (
                df[col]
                .fillna("")
                .astype(str)
                .str.strip()
                .str.lower()
            )

    # 3. Strict deduplication
    df_dedup = df.drop_duplicates(subset=DEDUP_KEYS, keep="first")

    after_rows = len(df_dedup)

    # 4. Save result
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    df_dedup.to_csv(OUTPUT_FILE, index=False)

    # 5. Report
    print("[DEDUP SUMMARY]")
    print(f"Rows before dedup: {before_rows}")
    print(f"Rows after dedup : {after_rows}")
    print(f"Removed rows     : {before_rows - after_rows}")
    print(f"[DONE] Output written to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
