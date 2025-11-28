from utils import load_csv, save_csv
import pandas as pd

df = load_csv("dataset/sample_with_missing.csv")

missing = df.isnull().sum().reset_index()
missing.columns = ["column", "missing_count"]

save_csv(missing, "output/missing_report.csv")