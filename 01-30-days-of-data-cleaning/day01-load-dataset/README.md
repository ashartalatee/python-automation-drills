# Day 1 — Load Dataset

## Tujuan
Memahami cara membaca dataset pertama kali:
- read_csv
- mengecek struktur data
- mendeteksi masalah awal sebelum cleaning

## File dalam folder ini
- dataset/day1_dataset.csv → data mentah
- notebook/day1.ipynb → eksplorasi & catatan
- script/day1_load_dataset.py → script loading otomatis
- output/ (belum digunakan di Day 1)

## Tugas
1. Load dataset.
2. Tampilkan:
   - head
   - info
   - shape
   - sample
3. Identifikasi:
   - format tanggal
   - missing value
   - tipe data yang salah
   - kolom numerik yang terbaca sebagai string

# **Tabel Ringkas Perintah Pandas (Data Profiling)**

### *Day 1 – Wajib hafal untuk semua project Data Automation*

| Kategori             | Perintah                        | Fungsi Singkat           | Kapan Dipakai                                       |
| -------------------- | ------------------------------- | ------------------------ | --------------------------------------------------- |
| **Melihat Data**     | `df.head()`                     | Lihat 5 baris pertama    | Cek data berhasil dibaca, lihat struktur awal       |
|                      | `df.head(10)`                   | Lihat 10 baris           | Saat dataset besar, ingin lihat lebih banyak contoh |
|                      | `df.tail()`                     | Lihat baris terakhir     | Cek baris rusak, footer aneh, baris kosong          |
|                      | `df.sample(5)`                  | Ambil sample acak        | Cek variasi data, deteksi noise                     |
| **Struktur Dataset** | `df.shape`                      | Jumlah baris × kolom     | Pastikan ukuran dataset benar                       |
|                      | `df.columns`                    | Daftar kolom             | Cek nama kolom, banyak dipakai untuk rename         |
|                      | `df.info()`                     | Tipe data & Missing      | Cek apakah numeric → object, cek missing            |
| **Statistik Dasar**  | `df.describe()`                 | Statistik angka          | Cek outlier, range angka janggal                    |
|                      | `df.describe(include='object')` | Statistik teks/kategori  | Cek frekuensi kategori, nilai paling sering         |
| **Quality Check**    | `df.isna().sum()`               | Jumlah missing per kolom | Menentukan langkah cleaning                         |
|                      | `df.duplicated().sum()`         | Jumlah baris duplikat    | Untuk day 12 (duplicate handling)                   |
|                      | `df.nunique()`                  | Jumlah nilai unik        | Cek apakah kolom benar-benar kategori               |
| **Tipe Data**        | `df.dtypes`                     | Cek tipe data cepat      | Pastikan angka ≠ object, tanggal ≠ string           |
|                      | `df.select_dtypes('number')`    | Ambil kolom numeric      | Untuk cleaning numeric/day 10                       |
|                      | `df.select_dtypes('object')`    | Ambil kolom teks         | Untuk cleaning text/day 8–9                         |

---

# **Ringkasan Super Penting**

Day 1 itu bukan cleaning.

Day 1 itu **MEMAHAMI DATA**.

Karena tanpa paham:

* shape
* tipe data
* missing
* struktur
* statistik dasar

…maka semua cleaning setelah itu **salah arah**.

Oleh karena itu, semua perintah di tabel ini adalah **core Pandas for Profiling**.

## Output Day 1
Hanya pemahaman struktur data,
belum melakukan perbaikan tipe data atau cleaning.
