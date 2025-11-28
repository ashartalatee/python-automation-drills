from utils import load_csv, save_csv

df = load_csv("dataset/sample_with_missing.csv")

df_filled = df.fillna(df.median(numeric_only=True))

df_filled = df_filled.fillna(df.mode().iloc[0])

save_csv(df_filled, "output/cleaned_data_basic.csv")