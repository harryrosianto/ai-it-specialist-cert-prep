# Domain 5: Maintaining and Monitoring AI in Production

---

## 5.1 Melakukan Oversight (Pengawasan)

- **Log performa aplikasi dan model** untuk keperluan keamanan, debug, akuntabilitas, dan audit
- Gunakan **sistem monitoring yang andal (robust)**
- **Bertindak atas alert** yang muncul
- **Amati sistem sepanjang waktu** dalam berbagai konteks untuk memeriksa **drift** atau **degraded mode of operation** (penurunan performa)
- **Deteksi cara sistem gagal** dalam mendukung informasi baru

## 5.2 Menilai Dampak Bisnis (KPI)

- **Lacak metrik dampak (impact metrics)** untuk menentukan apakah solusi berhasil memecahkan masalah
- **Bandingkan metrik sebelum dan sesudah** ada perubahan
- **Bertindak atas metrik yang tidak terduga (unexpected)** dengan mencari masalah dan memperbaikinya

## 5.3 Mengukur Dampak terhadap Individu dan Komunitas

- **Analisis dampak pada subgrup tertentu** (mis. apakah performa model berbeda signifikan antar kelompok demografis?)
- **Identifikasi dan mitigasi isu** yang muncul
- **Identifikasi peluang optimasi**

## 5.4 Menangani Feedback dari Pengguna

- **Ukur kepuasan pengguna**
- **Nilai apakah pengguna bingung** (mis. apakah mereka paham apa yang seharusnya dilakukan AI untuk mereka?)
- **Masukkan feedback ke versi mendatang**

## 5.5 Mempertimbangkan Peningkatan atau Decommission Secara Berkala

- **Gabungkan observasi dampak** (bisnis, komunitas, tren teknologi) untuk menilai nilai (value) AI
- **Putuskan**: melatih ulang (retrain) AI, tetap menggunakan AI apa adanya, atau **decommission** (menonaktifkan) AI

---

## Ringkasan Cepat

| Sub-topik | Kata Kunci untuk Diingat |
|-----------|---------------------------|
| 5.1 | logging, monitoring, alert, drift, degraded mode |
| 5.2 | impact metrics, bandingkan sebelum-sesudah |
| 5.3 | dampak subgrup, mitigasi, optimasi |
| 5.4 | kepuasan, kebingungan pengguna, feedback loop |
| 5.5 | retrain vs decommission |

## Konsep Model Drift (Sering Muncul di Ujian)

| Jenis Drift | Penjelasan |
|-------------|------------|
| **Data drift** | Distribusi data input di produksi berubah dibanding data training |
| **Concept drift** | Hubungan antara input dan output (pola yang dipelajari model) berubah seiring waktu |
| **Model/performance decay** | Penurunan akurasi model secara bertahap akibat drift yang tidak ditangani |

> 💡 **Poin ujian**: Monitoring bukan aktivitas satu kali di akhir proyek — ini adalah proses **berkelanjutan** sepanjang siklus hidup AI di produksi (continuous improvement).
