# Day 5 — *Handling Missing Values*

### *Belajar cara menangani data yang bolong-bolong (missing values)*

---

## Kenapa Day 5 Ini Penting?

Di dunia nyata, **data itu sering kotor** dan salah satu kotoran paling sering muncul adalah:

> **Nilai yang hilang (missing values)** — kosong, NaN, None, null, atau tidak ada datanya.

Kalau missing values tidak ditangani dengan benar, kamu bisa mengalami:

* ❌ Hasil analisis salah
* ❌ Model machine learning kacau
* ❌ Perhitungan statistik tidak bisa jalan
* ❌ Dashboard error
* ❌ Data jadi tidak bisa diproses

**Day 5 ini mengajarkan kamu ilmu dasar Wajib-Ada dalam Data Cleaning.**
Tanpa skill ini, data kamu seperti rumah tanpa fondasi.

---

## Tujuan Day 5

1. **Mampu mendeteksi missing values**
2. **Mampu memahami pola missing values**
3. **Mampu memilih strategi penanganan** (drop, fill, replace)
4. **Mampu menerapkan solusi dengan Python**
5. **Menghasilkan dataset bersih tanpa nilai kosong**

---

## Apa Saja Missing Values Itu?

Missing values bisa muncul karena berbagai alasan:

| Penyebab                  | Contoh                        |
| ------------------------- | ----------------------------- |
| User tidak isi form       | kolom email kosong            |
| Error sistem              | tanggal tidak terekam         |
| Data tidak wajib          | kolom "catatan" kosong        |
| Data salah format         | `" "` (spasi) dianggap kosong |
| Hilang saat export/import | csv error                     |

### Di Python, bentuk missing values biasanya:

* `NaN`
* `None`
* `""` (string kosong)
* `" "` (spasi)
* `"NULL"`
* `"NA"`

---

## Apa yang Kita Lakukan di Day 5?

### **1. Deteksi missing values**

```python
df.isna().sum()
```

### **2. Lihat persentasenya**

```python
(df.isna().sum() / len(df)) * 100
```

### **3. Visualisasi sederhana (opsional)**

Melihat kolom mana yang paling banyak bolongnya.

### **4. Tentukan strategi penanganan**

Ada 3 strategi utama:

---

## **A. Drop Missing Values (Buang Data Bolong)**

Digunakan kalau:

* Missing values **sedikit**
* Data penting tidak hilang kalau dibuang

```python
df_clean = df.dropna()
```

---

## **B. Fill Missing Values (Isi Data Kosong)**

Dipakai kalau:

* Kolomnya wajib
* Kamu butuh data tetap utuh
* Nilai bisa diprediksi

Contoh:

```python
df['age'] = df['age'].fillna(df['age'].median())
df['city'] = df['city'].fillna("Unknown")
```

---

## **C. Replace Khusus (Case by Case)**

Misal:

* String kosong dianggap NaN
* "?" diganti None

```python
df.replace("", pd.NA, inplace=True)
df.replace("?", pd.NA, inplace=True)
```

---

## Struktur Folder Day 5

```
day05-missing-values/
│── dataset/
│   └── raw_data.csv
│
│── notebook/
│   └── day05_missing_values.ipynb
│
│── script/
│   └── fix_missing_values.py
│
└── output/
    ├── report_missing_values.txt
    └── cleaned_data.csv
```

---

## Cara Mengecek Apakah Day 5 Berfungsi Dengan Baik?

Checklist berikut harus **YES semua**:

### ✔ 1. Ada laporan missing values

`output/report_missing_values.txt` terisi data seperti:

```
Kolom        Jumlah Missing   Persentase
email        45               12.5%
birth_date   10               2.7%
city         0                0%
```

### ✔ 2. Kolom yang seharusnya diisi sudah terisi

Misal sebelumnya `age` ada NaN, sekarang tidak.

### ✔ 3. Tidak ada lagi `NaN` di kolom penting

```python
df.isna().sum()
```

harus menghasilkan:

```
0 0 0 0...
```

### ✔ 4. `cleaned_data.csv` sudah rapi

Tidak ada nilai kosong.

---

## Output Final Day 5

| File                         | Fungsi                                      |
| ---------------------------- | ------------------------------------------- |
| `report_missing_values.txt`  | Ringkasan missing values sebelum diperbaiki |
| `cleaned_data.csv`           | Dataset bersih final                        |
| `day05_missing_values.ipynb` | Notebook pembelajaran                       |
| `fix_missing_values.py`      | Script otomatis cleaning missing values     |

---

## Ringkasan Bahasa Bayi (Agar Kamu Tak Bingung Saat Buka Lagi)

Day 5 itu belajar **mengisi atau membersihkan kolom yang bolong**.
Kalau data bolong tidak dibereskan, nanti:

* analisis error
* model salah
* hasil bohong
* skrip tidak jalan

Makanya **Day 5 adalah fondasi setelah tipe data (Day 2–3) dan duplikasi (Day 4)**.
Sebelum masuk ke analisis, kamu wajib pastikan:

> **"Tidak ada data penting yang bolong-bolong."**

Setelah Day 5, dataset kamu **sudah rapi, sehat, dan siap dipakai**.
