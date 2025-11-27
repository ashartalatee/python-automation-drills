def auto_fix_numeric(df, cols):
    """
    Membersihkan banyak kolom numeric sekaligus.
    Cocok untuk dataset besar / multi kolom numeric.
    """
    for col in cols:
        df[col] = (
            df[col]
            .astype(str)
            .str.replace(r'[^0-9]', '', regex=True)
            .replace('', None)
            .astype(float)
        )
    return df
