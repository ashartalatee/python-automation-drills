# Day 1 — Load Dataset Dasar (Belajar Membaca Data)

Hai Ashar! 👋  
Selamat datang di Day 1. Hari ini kita belajar **membaca dataset** dan melihat **struktur data** supaya kita tahu data kita seperti apa.  

Ini adalah **langkah pertama yang sangat penting** sebelum kita mulai membersihkan atau memproses data.

---

## 🍼 Apa itu Day 1?

Day 1 = belajar **load dataset dan cek struktur dasar**.  
Artinya:

- Buka file CSV atau Excel 📂  
- Lihat 5 baris pertama & terakhir 👀  
- Cek jumlah baris & kolom 📊  
- Cek tipe data awal (`object`, `int`, `float`)  
- Lihat apakah ada missing value awal ❓  

Kenapa penting?  
Kalau kita gak ngerti data mentah kita, nanti:

- Bisa salah bersihin data 😵  
- Bisa salah detect missing value 😭  
- Bisa salah ketika buat pipeline otomatis 😱  

Jadi Day 1 itu **langkah “intip rumah dulu sebelum dibersihin”**.

---

## 🐣 Struktur Folder Day 1

```

day01-load-dataset/
│── dataset/      # tempat data mentah
│── notebook/     # tempat coba-coba & eksplorasi
│── script/       # script kecil untuk load & cek data
└── output/       # tempat menyimpan hasil inspection

````

### Penjelasan gampang:

- **dataset/** → data asli, jangan diubah  
- **notebook/** → tempat coba-coba lihat data, visualisasi awal  
- **script/** → script reusable, misalnya fungsi load & cek data  
- **output/** → simpan hasil print/summary supaya gampang dilacak  

---

## 🍼 Dataset Contoh (dataset/hari1_dataset.csv)

| order_id | date       | qty | price     | category |
|----------|------------|-----|-----------|----------|
| A001     | 12/31/2024 | 3   | 10000     | makanan  |
| A002     | 2024-01-05 | 1   | 25000     | minuman  |
| A003     | 01-07-2024 | 2   | 30000     | makanan  |
| A004     | 7 Jan 2024 | 5   | 50500     | lainnya  |
| A005     | 2024/01/08 | 1   | 10000     | minuman  |

> Lihat kan? Ini data mentah awal. Belum kita cek atau bersihin.

---

## 🍼 Script Penting

### 1. load_data.py

- Fungsi `load_csv(file_path)`  
- Bisa load CSV atau Excel  
- Bisa langsung print head, tail, shape, dan info

### 2. inspect_data.py

- Fungsi `check_missing(df)` → cek missing value  
- Fungsi `check_dtype(df)` → lihat tipe data awal  

---

## 🍼 Workflow Day 1 (Sederhana)

1. **Buka dataset** → dataset/hari1_dataset.csv  
2. **Lihat baris pertama & terakhir** → `df.head()`, `df.tail()`  
3. **Cek jumlah baris & kolom** → `df.shape`  
4. **Cek tipe data** → `df.dtypes`  
5. **Cek missing value awal** → `df.isna().sum()`  
6. **Simpan hasil** ke folder `output/` (misal: summary.csv)

---

## 🍼 Cara Cek Day 1 Berhasil

- Bisa print 5 baris pertama → lihat data benar  
- Bisa print 5 baris terakhir → lihat data benar  
- Bisa cek shape → jumlah baris & kolom sesuai  
- Bisa cek dtypes → tahu kolom mana string, angka, tanggal  
- Bisa cek missing → tahu kolom mana perlu di-handle nanti  

Kalau semua ini ✅ → Day 1 sukses! 🎉

---

## 🍼 Kenapa Day 1 Penting Sekali?

Bayangkan ini:

- Data = rumah kita  
- Day 1 = lihat rumah dulu, cek kondisi atap & lantai  
- Kalau kita lompat bersihin tanpa lihat → bisa salah bersih 😵  

Intinya: **Day 1 itu tahap “kenalan dengan data” sebelum mulai cleaning**.  

---

## 🍼 Contoh Pakai Script

```python
import pandas as pd
from script.load_data import load_csv
from script.inspect_data import check_missing, check_dtype

# Load dataset
df = load_csv("dataset/hari1_dataset.csv")

# Cek dtype & missing
check_dtype(df)
check_missing(df)

# Simpan summary ke output/
df.describe().to_csv("output/summary_day1.csv")
````

---

## 🍼 Tips Ashar

* Jangan ubah data mentah di folder dataset
* Selalu lihat head & tail sebelum bersih-bersih
* Simpan summary di folder output untuk dokumentasi
* Anggap Day 1 = “intip rumah dulu sebelum renovasi” 🏠