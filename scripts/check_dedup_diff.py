import pandas as pd

RAW = "data/interim/jobs_interim.csv"
DEDUP = "data/processed/jobs_dedup_strict.csv"

df_raw = pd.read_csv(RAW)
df_dedup = pd.read_csv(DEDUP)

removed = df_raw.merge(
    df_dedup,
    how="left",
    indicator=True
)

removed = removed[removed["_merge"] == "left_only"]

print("Removed sample:")
print(
    removed[[
        "company",
        "role",
        "location",
        "salary_raw"
    ]].head(10)
)
