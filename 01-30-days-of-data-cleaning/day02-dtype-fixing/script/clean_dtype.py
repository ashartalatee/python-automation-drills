import pandas as pd
import re

def clean_numeric(val):
    """Membersihkan format angka: '10.000', 'Rp 30k', '50,500', dll."""
    if pd.isna(val):
        return None
    val = str(val)
    val = re.sub(r'[^0-9]', '', val)
    return float(val) if val else None

def clean_dtypes(df):
    """
    Memperbaiki tipe data:
    - date → datetime
    - price → numeric
    - category → category dtype
    """
    # --- Datetime ---
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # --- Numeric ---
    df['price'] = df['price'].apply(clean_numeric)

    # --- Category ---
    df['category'] = df['category'].astype('category')

    return df
