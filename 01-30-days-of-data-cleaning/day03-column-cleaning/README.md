# Day 3 — Cleaning Nama Kolom (Normalisasi Kolom Data)

Halo Ashar! 👋  
Selamat datang di Day 3. Hari ini kita fokus pada **membersihkan dan menormalisasi nama kolom** di dataset.  

---

## 🍼 Apa itu Day 3?

Day 3 = belajar **merapikan nama kolom** agar rapi dan konsisten.  

Kenapa penting?  

- Kolom bisa memiliki spasi, huruf besar/kecil, simbol aneh → bikin script susah jalan  
- Jika kolom tidak konsisten → `df['Total_Price']` kadang muncul sebagai `total price` atau `TotalPrice`  
- Semua pipeline automation, groupby, merge, filter, dll, **butuh kolom rapi**  

Intinya: **Day 3 memastikan kolom bisa dipanggil dengan mudah dan konsisten**.

---

## 🍼 Tujuan Day 3

1. Membersihkan spasi, huruf besar, simbol aneh dari nama kolom  
2. Mengubah semua nama kolom ke **format standar** (contoh: snake_case)  
3. Membuat script reusable untuk pipeline automation  

---

## 🍼 Contoh Masalah

Dataset awal:

| Order ID | Tanggal Pesanan | Jumlah | Harga (Rp) | Kategori Produk |
|----------|----------------|--------|------------|----------------|

Masalah:  

- Ada spasi → `Order ID`  
- Ada simbol → `Harga (Rp)`  
- Huruf besar/kecil campur → `Kategori Produk`  

---

## 🍼 Hasil Setelah Cleaning

| order_id | tanggal_pesanan | jumlah | harga_rp | kategori_produk |
|----------|----------------|--------|----------|----------------|

Semua rapi, lowercase, snake_case → siap dipakai script otomatis.

---

## 🍼 Struktur Folder (Sesuai Standard)

```

day03-column-cleaning/
│── dataset/      # dataset mentah
│── notebook/     # eksplorasi & testing
│── script/       # script automation cleaning kolom
└── output/       # dataset kolom sudah bersih

````

### Penjelasan:

- **dataset/** → data asli jangan diubah  
- **notebook/** → coba-coba transformasi kolom  
- **script/** → fungsi normalisasi kolom, reusable  
- **output/** → dataset kolom bersih siap pipeline

---

## 🍼 Script Penting

### clean_columns.py
- Fungsi: `clean_column_names(df)`  
- Membersihkan spasi, simbol, huruf besar/kecil  
- Mengubah ke format **snake_case**

Contoh:

```python
import re

def clean_column_names(df):
    df.columns = [
        re.sub(r'\W+', '_', col).strip().lower()
        for col in df.columns
    ]
    return df
````

---

## 🍼 Workflow Day 3

1. Load dataset mentah dari folder `dataset/`
2. Jalankan notebook untuk eksplorasi
3. Terapkan fungsi `clean_column_names(df)`
4. Simpan hasil ke folder `output/cleaned_day03.csv`
5. Pastikan semua nama kolom rapi, lowercase, snake_case

---

## 🍼 Cara Cek Berhasil

* Semua kolom sudah **huruf kecil**
* Tidak ada spasi atau simbol → `_`
* Bisa dipanggil langsung di script: `df['order_id']`
* File `output/cleaned_day03.csv` berisi kolom bersih

---

## 🍼 Kenapa Day 3 Penting?

* Kolom rapi = script aman jalan
* Kolom konsisten = merge, join, groupby, filter aman
* Kolom standar = pipeline automation lebih cepat dan mudah di-maintain

Day 3 = **fondasi kedua setelah Day 2**, agar pipeline automation berjalan lancar.

---

## 📝 Contoh Pakai Script

```python
import pandas as pd
from script.clean_columns import clean_column_names

df = pd.read_csv("dataset/hari3_dataset.csv")
df_clean = clean_column_names(df)
df_clean.to_csv("output/cleaned_day03.csv", index=False)
print(df_clean.columns)
```

✅ Semua kolom rapi dan siap pakai.
