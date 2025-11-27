# Day 2 — Dtype Fixing (Belajar Memperbaiki Tipe Data)

Hai Ashar! 👋  
Selamat datang di Day 2. Hari ini kita belajar **memperbaiki tipe data** supaya semua data kita bisa dipakai dengan aman.  

Jangan bingung, ini penting banget untuk semua latihan berikutnya.  

---

## 🍼 Apa itu Day 2?

Day 2 = belajar **dtype fixing**  
Artinya kita memastikan:

- Semua tanggal **jadi tanggal beneran** (datetime) 🗓️  
- Semua angka **jadi angka beneran** (numeric / float) 💰  
- Semua kategori **jadi kategori rapi** (category dtype) 🏷️  

Kenapa penting?  
Kalau data salah tipe:

- Kita gak bisa nambahin harga atau jumlah (error 😱)  
- Kita gak bisa filter data per tanggal (gagal 😢)  
- Kita gak bisa group category dengan rapi (bingung 😵)  

Intinya: **Day 2 itu pondasi untuk semua automation pipeline kita**.  

---

## 🐣 Struktur Folder Day 2

```

day02-dtype-fixing/
│── dataset/      # tempat data mentah
│── notebook/     # tempat coba-coba & lihat hasil
│── script/       # tempat bikin script otomatis
└── output/       # tempat data bersih & siap dipakai

```

### Penjelasan gampang:

- **dataset/** → data asli, jangan diubah  
- **notebook/** → laboratorium untuk coba-coba dan lihat apa yang salah  
- **script/** → mesin otomatis, nanti dipakai lagi di latihan lain  
- **output/** → hasil bersih, bisa langsung dipakai tanpa takut error

---

## 🍼 Dataset Contoh (dataset/hari2_dataset.csv)

| order_id | date       | qty | price     | category |
|----------|------------|-----|-----------|----------|
| A001     | 12/31/2024 | 3   | "10.000"  | makanan  |
| A002     | 2024-01-05 | 1   | 25,000    | minuman  |
| A003     | 01-07-2024 | 2   | Rp 30k    | makanan  |
| A004     | 7 Jan 2024 | 5   | "50.500"  | lainnya  |
| A005     | 2024/01/08 | 1   | 10000     | minuman  |

> Lihat kan? Harga dan tanggal kacau banget 😅  
> Day 2 akan benahin semuanya.

---

## 🍼 Script Penting

### 1. clean_dtype.py

- Fungsi `clean_dtypes(df)`  
- Membersihkan:
  - `date` → datetime  
  - `price` → numeric  
  - `category` → category dtype  

### 2. auto_fix_numeric.py

- Fungsi `auto_fix_numeric(df, cols)`  
- Bisa bersihin banyak kolom numeric sekaligus  
- Berguna banget untuk data besar & otomatisasi

---

## 🍼 Workflow Day 2 (Sederhana)

1. **Buka dataset** → dataset/hari2_dataset.csv  
2. **Lihat tipe data** → object, string, ada yang kacau 😵  
3. **Jalankan clean_dtype.py**  
4. **Ubah tipe data**:  
   - date → datetime  
   - price → float  
   - category → category  
5. **Simpan hasil ke output/cleaned_day02.csv**  
6. **Cek lagi** → semua sudah bener, siap dipakai 🎉

---

## 🍼 Cara Cek Day 2 Berhasil

- Jalankan `df_clean.dtypes` → harus keluar:

```

date       datetime64[ns]
price      float64
category   category

````

- Jalankan `df_clean['price'].sum()` → gak error  
- Jalankan `df_clean['category'].cat.categories` → rapi, gak ada typo  
- Lihat output/cleaned_day02.csv → data bersih, siap dipakai

Kalau semua ini ✅ → Day 2 sukses!

---

## 🍼 Kenapa Day 2 Penting Sekali?

Bayangkan ini:

- Data = rumah kita  
- Tipe data = fondasi rumah  
- Kalau fondasi jelek → rumah roboh 😱  
- Kalau fondasi kuat → rumah bisa dibangun sampai 30 hari pipeline tanpa takut runtuh 🏠

Jadi, Day 2 = **fondasi super penting**.  
Semua latihan Day 3 sampai Day 30 tergantung fondasi ini.  

---

## 🍼 Contoh Pakai Script

```python
import pandas as pd
from script.clean_dtype import clean_dtypes

# Load data mentah
df = pd.read_csv("dataset/hari2_dataset.csv")

# Bersihkan tipe data
df_clean = clean_dtypes(df)

# Simpan hasil
df_clean.to_csv("output/cleaned_day02.csv", index=False)

# Cek tipe data
print(df_clean.dtypes)
````

---

## 🍼 Tips Ashar

* Jangan pernah ubah dataset mentah
* Selalu cek dtype sebelum lanjut ke latihan berikutnya
* Simpan hasil bersih di output/ supaya gampang dilacak
* Anggap Day 2 = superhero fondasi untuk semua data automation 💪
