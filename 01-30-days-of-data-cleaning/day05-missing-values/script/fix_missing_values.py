import pandas as pd
import numpy as np
import os

# 1. LOAD DATASET
input_path = "../dataset/raw_data.csv"
output_clean_path = "../output/cleaned_data.csv"
output_report_path = "../output/report_missing_values.txt"

df = pd.read_csv(input_path)

# 2. CEK MISSING VALUES
missing_counts = df.isna().sum()
missing_percent = (df.isna().sum() / len(df)) * 100

# Buat laporan text
report_lines = ["LAPORAN MISSING VALUES (DAY 5)\n", "," * 50 + "\n"]

for col in df.columns:
    report_lines.append(
        f"{col:<20} | missing: {missing_counts[col]:<5} | {missing_percent[col]:.2f}%\n"
    )

with open(output_report_path, "w") as f:
    f.writelines(report_lines)

print("Laporan missing values dibuat:", output_report_path)

# 3. HANDLING MISSING VALUES
df_clean = df.copy()

# A. string kosong dan "?" dianggap missing
df_clean.replace("", pd.NA, inplace=True)
df_clean.replace("?", pd.NA, inplace=True)

# B. fill numeric dengan median
numeric_cols = df_clean.select_dtypes(include=["int64", "float64"]).columns
for col in numeric_cols:
    df_clean[col].fillna(df_clean[col].median(), inplace=True)

# C. fill object dengan 'Unknown'
object_cols = df_clean.select_dtypes(include=["object"]).columns
for col in object_cols:
    df_clean[col].fillna("Unknown", inplace=True)

# 4. SAVE OUTPUT
df_clean.to_csv(output_clean_path, index=False)

print("Dataset bersih disimpan:", output_clean_path)
print("\nDAY 5 SELESAI: Semua missing values telah ditangani!")