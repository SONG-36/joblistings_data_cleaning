import pandas as pd
import os

INTERIM_FILE = "data/interim/jobs_interim.csv"
OUT_FILE = "data/sample/jobs_sample.csv"

# Load interim data
df = pd.read_csv(INTERIM_FILE)

# Manually select representative rows (example indices)
sample_indices = [0, 1, 2, 3, 5, 8, 10, 12, 15, 18, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]

sample_df = df.loc[sample_indices]

os.makedirs(os.path.dirname(OUT_FILE), exist_ok=True)
sample_df.to_csv(OUT_FILE, index=False)

print(f"[DONE] Sample written to {OUT_FILE}")
