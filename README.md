# IT Specialist – Artificial Intelligence (Pearson) — Persiapan Sertifikasi

Repository ini berisi materi belajar mandiri untuk sertifikasi **Certiport/Pearson IT Specialist – Artificial Intelligence**, disusun berdasarkan dokumen resmi *Exam Objectives* (2025).

> Sertifikasi ini menguji pengetahuan dasar tentang proses pengembangan solusi AI, mulai dari definisi masalah, pengumpulan & pemrosesan data, pemilihan algoritma & pelatihan model, integrasi & deployment aplikasi, hingga pemantauan AI di lingkungan produksi — termasuk isu governance, transparansi, keamanan, dan etika AI.

## 🗂️ Struktur Repository

```
ai-it-specialist-cert-prep/
├── README.md                          # File ini
├── study-plan.md                      # Rencana belajar 2 minggu
├── glossary.md                        # Daftar istilah penting
├── docs/                              # Ringkasan materi per domain
│   ├── 01-ai-problem-definition.md
│   ├── 02-data-collection-processing-engineering.md
│   ├── 03-ai-algorithms-and-models.md
│   ├── 04-application-integration-and-deployment.md
│   └── 05-maintaining-monitoring-ai-production.md
├── practice-questions/                # Bank soal latihan per domain (+ jawaban & pembahasan)
│   ├── domain-1-questions.md
│   ├── domain-2-questions.md
│   ├── domain-3-questions.md
│   ├── domain-4-questions.md
│   └── domain-5-questions.md
├── hands-on-labs/                     # 🧪 LATIHAN CODING PYTHON (baru!) — lihat bagian di bawah
│   ├── 00-SETUP.md
│   ├── lab-01-problem-definition-worksheet.md
│   ├── lab-02-data-processing.py
│   ├── lab-03-model-training-evaluation.py
│   ├── lab-04-deployment-simulation.py
│   ├── lab-05-monitoring-drift-detection.py
│   └── solutions/                     # Jawaban lengkap tiap lab
├── case-studies/                      # Studi kasus terapan (skenario nyata)
│   ├── case-study-01-healthcare-triage.md
│   ├── case-study-02-ecommerce-recommendation.md
│   └── case-study-03-manufacturing-defect-detection.md
└── practice-exam/                     # Simulasi ujian penuh
    ├── full-practice-exam.md          # 40 soal campuran (tanpa jawaban terlihat)
    └── answer-key.md                  # Kunci jawaban + pembahasan singkat
```

## 📊 Bobot Domain (berdasarkan exam objectives)

| # | Domain | Sub-topik |
|---|--------|-----------|
| 1 | AI Problem Definition | 1.1–1.6 |
| 2 | Data Collection, Processing, and Engineering | 2.1–2.9 |
| 3 | AI Algorithms and Models | 3.1–3.9 |
| 4 | Application Integration and Deployment | 4.1–4.4 |
| 5 | Maintaining and Monitoring AI in Production | 5.1–5.5 |

Domain 2 dan 3 memiliki jumlah sub-objektif terbanyak, jadi kemungkinan besar proporsi soal di ujian sesungguhnya juga paling besar di kedua domain ini — alokasikan waktu belajar lebih banyak di sana.

## ✅ Cara Menggunakan Repo Ini

1. **Baca ringkasan materi** di folder `docs/` sesuai urutan domain.
2. **🧪 Kerjakan hands-on labs** di `hands-on-labs/` — ini bagian paling praktis: latihan Python asli (bukan cuma teori) untuk tiap domain, pakai dataset bawaan scikit-learn jadi bisa langsung jalan tanpa perlu download data. Lihat `hands-on-labs/00-SETUP.md` untuk mulai.
3. **Kerjakan bank soal** di `practice-questions/` per domain — jawaban ada di bagian `<details>` (klik untuk membuka) agar bisa latihan tanpa "curi lihat".
4. **Pelajari studi kasus** di `case-studies/` untuk melatih penerapan konsep pada skenario nyata (mirip gaya soal skenario di ujian sesungguhnya).
5. **Kerjakan simulasi ujian penuh** di `practice-exam/full-practice-exam.md` dalam kondisi seperti ujian asli (batasi waktu, tanpa membuka catatan), lalu cocokkan dengan `answer-key.md`.
6. Gunakan `glossary.md` sebagai referensi cepat istilah-istilah kunci.

## 🧪 Hands-On Labs — Detail

Setiap lab memetakan langsung ke satu domain ujian dan pakai kode Python asli yang bisa dijalankan (dataset bawaan scikit-learn, tidak perlu internet):

| Lab | Domain | Kamu akan praktik... |
|-----|--------|------------------------|
| `lab-01-problem-definition-worksheet.md` | 1 | Menulis analisis keputusan untuk skenario nyata (sistem deteksi mahasiswa berisiko DO) |
| `lab-02-data-processing.py` | 2 | Cek missing value, imputasi, cek class balance, scaling, train/test split representatif |
| `lab-03-model-training-evaluation.py` | 3 | Training decision tree, tuning `max_depth`, deteksi overfitting, hitung precision/recall/F1, cek feature importance |
| `lab-04-deployment-simulation.py` | 4 | Bungkus model jadi pipeline dengan validasi input, uji kecepatan, uji robustness terhadap outlier |
| `lab-05-monitoring-drift-detection.py` | 5 | Simulasikan data drift, deteksi otomatis pakai uji statistik (KS test), ambil keputusan retrain/decommission |

Setiap file `.py` punya bagian `# TODO` yang harus kamu isi sendiri. Jawaban lengkap ada di `hands-on-labs/solutions/`.

## 📌 Catatan Sumber

Materi disusun berdasarkan *IT Specialist Exam Objectives – Artificial Intelligence* © 2025 Pearson Education, Inc. Repo ini adalah **materi belajar mandiri (bukan produk resmi Pearson/Certiport)** dan tidak berisi soal ujian asli — semua soal dan studi kasus di sini adalah buatan sendiri untuk latihan konsep.

## 📄 Lisensi

Materi belajar ini bebas digunakan untuk keperluan edukasi pribadi/non-komersial.
