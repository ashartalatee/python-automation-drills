# **README.md — Day 4 (Deteksi Missing Values)**

```markdown
# Day 4 — Deteksi Missing Values (Mengecek Kekosongan Data)

Halo Ashar! 👋  
Selamat datang di Day 4. Hari ini kamu belajar **mendeteksi missing values** — salah satu langkah penting sebelum melakukan cleaning lebih dalam.

---

## Apa itu Day 4?

Day 4 = belajar **mengecek ada tidaknya data yang kosong** di setiap kolom.

Kenapa penting?

- Missing values bisa bikin perhitungan salah  
- Bisa menyebabkan error ketika pipeline automation berjalan  
- Sumber data nyata (ads, finance, e-commerce, CRM) selalu punya missing  
- Sebelum mengisi atau menghapus (Day 5), kita harus **tahu dulu** apa yang kosong  

Day 4 = fondasi *sebelum* masuk bagian “Handling Missing Values”.

---

## Tujuan Day 4

1. Menemukan kolom/record yang kosong  
2. Menghitung jumlah dan persentase missing per kolom  
3. Menandai area yang berpotensi bermasalah  
4. Menyiapkan data untuk Day 5 (mengisi & memperbaiki missing)

---

## Konsep Penting

### Apa itu missing values?

Missing =  
- `NaN`  
- Kosong  
- String kosong `""`  
- Null  
- Isi rusak (misalnya “—”, “n/a”, “?“, “null”)

### Kenapa missing values bahaya?

- Tidak bisa dihitung → error saat sum, mean, groupby  
- Mengganggu training model AI  
- Bisa salah interpretasi (contoh: qty kosong ≠ qty 0)

---

## Struktur Folder Day 4

```

day04-missing-detection/
│── dataset/      # data mentah yang mengandung missing
│── notebook/     # explorasi & pengecekan missing
│── script/       # script otomatis untuk deteksi missing
└── output/       # laporan missing hasil deteksi

````

---

## Script Penting

### Script: `missing_report.py`

Fungsi utama:

- `check_missing(df)` → melihat jumlah missing per kolom  
- `missing_percentage(df)` → menghitung persentase missing  
- `generate_missing_report(df)` → membuat laporan lengkap  

Keluaran bisa berupa:
- Tabel missing  
- File CSV laporan  
- Notifikasi kolom yang paling bermasalah

---

## Contoh Kode Day 4

```python
import pandas as pd

def missing_report(df):
    missing_count = df.isna().sum()
    missing_pct = (df.isna().sum() / len(df)) * 100

    report = pd.DataFrame({
        "missing_count": missing_count,
        "missing_percentage": missing_pct.round(2)
    })

    return report
````

---

## Workflow Day 4

1. Load dataset mentah
2. Jalankan fungsi deteksi missing
3. Buat tabel:

   * jumlah missing per kolom
   * persentase missing
4. Simpan laporan ke folder `output/`
5. Tandai kolom yang harus diperbaiki di Day 5

---

## Cara Cek Day 4 Berhasil

* Kamu mampu menghasilkan **tabel laporan missing**
* Kamu bisa menjawab:

  * Kolom mana paling banyak missing?
  * Seberapa parah missing-nya (persentase)?
  * Missing perlu di-drop atau diisi?
* File `output/missing_report.csv` berhasil dibuat

Jika semua ini terpenuhi → Day 4 sukses

---

## Kenapa Day 4 Penting?

Day 4 adalah *checkpoint* dalam data pipeline:

* Tanpa deteksi missing → kamu tidak bisa mengambil keputusan cleaning
* Tanpa laporan missing → pipeline automation tidak bisa divalidasi
* Banyak perusahaan mengalami error produksi karena missing tidak terdeteksi lebih awal
* Day 4 membantu kamu membangun mindset **“data diagnosis sebelum tindakan”**

Day 4 = kemampuan yang sangat wajib di Data Cleaning level profesional.

---

## Contoh Penggunaan Script

```python
import pandas as pd
from script.missing_report import missing_report

df = pd.read_csv("dataset/hari4_dataset.csv")
report = missing_report(df)

report.to_csv("output/missing_report.csv")
print(report)
```

Hasilnya akan menunjukkan kolom mana yang kosong dan seberapa besar persentasenya.

---

## Penutup

Day 4 adalah langkah penting untuk membangun pipeline cleaning end-to-end.
Besok di Day 5 kamu akan belajar **Handling Missing Values** (mengisi, menghapus, memperbaiki).`
