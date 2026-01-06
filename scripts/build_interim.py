import pandas as pd
import os

RAW_FILE = "data/raw/jobs_raw.csv"
OUT_FILE = "data/interim/jobs_interim.csv"

# ============================================================
# Stage: Raw -> Interim
# Purpose:
# - Structural normalization only
# - Field decomposition WITHOUT interpretation
# - No salary parsing, no business logic
# ============================================================

# 1. Read raw CSV (read once, raw is immutable)
df_raw = pd.read_csv(RAW_FILE)

# 2. Normalize column names
df_raw.columns = (
    df_raw.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
)

# 3. Build interim dataframe with explicit schema
df = pd.DataFrame()

# --- Identity fields ---
df["job_id"] = df_raw.index.astype(str)
df["company"] = df_raw.get("company")
df["location"] = df_raw.get("location")
df["category"] = df_raw.get("category")
df["subcategory"] = df_raw.get("subcategory")
df["role"] = df_raw.get("role")
df["employment_type"] = df_raw.get("type")

# --- Salary decomposition (STRUCTURE ONLY) ---
df["salary_raw"] = df_raw.get("salary")

df["salary_type"] = None
df["salary_min"] = None
df["salary_max"] = None
df["salary_period"] = None
df["currency"] = None

# --- Metadata ---
df["listing_date"] = df_raw.get("listingdate")
df["source"] = "kaggle_jobstreet"

# 4. Trim whitespace in string fields
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()

# 5. Write interim file
os.makedirs(os.path.dirname(OUT_FILE), exist_ok=True)
df.to_csv(OUT_FILE, index=False)

print(f"[DONE] Interim file written to {OUT_FILE}")
