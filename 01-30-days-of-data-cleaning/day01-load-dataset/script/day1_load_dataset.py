import pandas as pd

def load_dataset(path):
    print("Loading dataset...")
    df = pd.read_csv(path)

    print("\n HEAD")
    print(df.head())

    print("\n INFO:")
    print(df.info())

    print("\n SHAPE:", df.shape)

    print("\n COLUMNS:", df.columns.tolist())

    print("\n SAMPLE:")
    print(df.sample(3))

    return df

if __name__ == "__main__":
    df = load_dataset("../dataset/day1_dataset.csv")