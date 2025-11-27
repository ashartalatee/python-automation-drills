import re
import pandas as pd

def clean_column_names(df):
    """
    Membersihkan nama kolom:
    - Buang spasi & simbol → diganti underscore
    - Semua huruf kecil
    - Cocok untuk automation pipeline
    """
    df.columns = [
        re.sub(r'\W+', '_', col).strip().lower()
        for col in df.columns
    ]
    return df