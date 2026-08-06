# Domain 2: Data Collection, Processing, and Engineering

Domain ini adalah domain dengan jumlah sub-objektif terbanyak (2.1–2.9) — prioritaskan waktu belajar di sini.

---

## 2.1 Memilih Cara Mengumpulkan Data

- Tentukan **tipe/karakteristik data** yang dibutuhkan (teks, gambar, numerik, time series, dll.)
- Putuskan apakah menggunakan **dataset yang sudah ada** atau perlu **membuat dataset sendiri**
- Jika membuat sendiri, tentukan apakah pengumpulan bisa **diotomasi** atau **butuh input manual dari pengguna**

## 2.2 Menilai Kualitas Data

- Apakah dataset **memenuhi kebutuhan tugas**?
- Cari **data yang hilang (missing)** atau **rusak/korup (corrupt)**

## 2.3 Memastikan Data Representatif

- Periksa **teknik pengumpulan** untuk potensi sumber **bias**
- Pastikan **jumlah data cukup** untuk membangun model yang tidak bias (unbiased)

> 💡 **Poin ujian**: "Representative" ≠ "banyak". Data yang besar tapi tidak mencerminkan populasi sesungguhnya tetap menghasilkan model bias.

## 2.4 Identifikasi Kebutuhan Sumber Daya

- Nilai apakah masalah **bisa dipecahkan dengan sumber daya komputasi yang tersedia**
- Pertimbangkan **budget proyek** dan sumber daya yang ada (waktu, tenaga, biaya cloud/compute)

## 2.5 Mengonversi Data ke Format yang Sesuai

- Konversi data ke bentuk **biner/numerik** (mis. gambar → piksel)
- Konversi data mentah menjadi **fitur yang cocok untuk AI** (mis. kalimat → token, untuk NLP)

## 2.6 Memilih Fitur (Feature Selection) untuk Model AI

- Tentukan **fitur data mana yang akan disertakan**
- Bangun **feature vector awal** untuk dataset test/train
- **Konsultasi dengan subject-matter expert** untuk mengonfirmasi pemilihan fitur — ini penting karena tim teknis belum tentu paham konteks domain

## 2.7 Feature Engineering

- Tinjau fitur dan tentukan **transformasi standar** yang dibutuhkan (normalisasi, encoding kategori, scaling, dll.)
- Buat **dataset yang sudah diproses** (processed dataset)

## 2.8 Menentukan Dataset Training dan Test

- Pisahkan data yang tersedia menjadi **dataset training dan test**
- Pastikan **dataset test representatif** terhadap keseluruhan populasi data (bukan hanya subset yang mudah)

## 2.9 Mendokumentasikan Keputusan Data

- Catat **asumsi, predikat, dan batasan (constraints)** yang mendasari pilihan desain
- Sediakan informasi ini untuk **regulator dan pengguna akhir** yang menuntut transparansi mendalam (deep transparency)

---

## Ringkasan Cepat

| Sub-topik | Kata Kunci untuk Diingat |
|-----------|---------------------------|
| 2.1 | existing vs generate dataset, otomasi vs manual |
| 2.2 | missing/corrupt data |
| 2.3 | bias sumber data, jumlah data cukup |
| 2.4 | compute resource, budget |
| 2.5 | data → biner, kalimat → token |
| 2.6 | feature vector, konsultasi subject-matter expert |
| 2.7 | transformasi standar, processed dataset |
| 2.8 | train/test split, test representatif |
| 2.9 | dokumentasi asumsi, transparansi ke regulator |

## Konsep Terkait yang Sering Muncul di Ujian

- **Data leakage**: informasi dari test set "bocor" ke training set, membuat evaluasi model terlihat lebih baik dari kenyataan.
- **Class imbalance**: satu kelas jauh lebih dominan dari kelas lain dalam data berlabel, berpotensi membuat model bias terhadap kelas mayoritas.
- **Data augmentation**: memperbanyak variasi data (mis. rotasi gambar) untuk meningkatkan generalisasi model, terutama saat data terbatas.
