import pandas as pd
import os

RAW_FILE = "data/raw/jobstreet_all_job_dataset.csv"
OUT_FILE = "data/interim/jobs_interim.csv"

# 1. 读取 raw（只读一次）
df = pd.read_csv(RAW_FILE)

# 2. 统一列名：小写 + 下划线
df.columns = (
    df.columns
      .str.strip()
      .str.lower()
      .str.replace(" ", "_")
)

# 3. 去掉字符串列的首尾空格
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()

# 4. 写入 interim
os.makedirs(os.path.dirname(OUT_FILE), exist_ok=True)
df.to_csv(OUT_FILE, index=False)

print(f"[DONE] Staged file written to {OUT_FILE}")
