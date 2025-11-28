from utils import load_csv, save_csv

df = load_csv("dataset/sample_with_missing.csv")

# imputasi groupby contoh
df["price"] = df.groupby("category")["price"].transform(
    lambda x: x.fillna(x.median())
)

# imputasi tipe data
for col in df.select_dtypes(include="object"):
    df[col].fillna(df[col].mode()[0], inplace=True)

save_csv(df, "output/cleaned_data_advanced.csv")