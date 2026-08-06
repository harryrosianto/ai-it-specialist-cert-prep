# Domain 1: AI Problem Definition

Domain ini menguji kemampuan menentukan **apakah dan bagaimana** AI seharusnya digunakan untuk memecahkan sebuah masalah — sebelum satu baris kode pun ditulis.

---

## 1.1 Identifikasi Masalah yang Akan Dipecahkan dengan AI

Sebelum membangun solusi AI, tentukan dahulu:

- **Kebutuhan (need)** apa yang ingin diatasi — mis. segmentasi pengguna, peningkatan layanan pelanggan.
- **Input dan output**: data apa yang tersedia sebagai masukan, dan hasil seperti apa yang diharapkan?
- **Apakah AI memang diperlukan** — kadang aturan bisnis sederhana (rule-based) atau statistik dasar sudah cukup; AI tidak selalu jadi solusi terbaik.
- **Untung-rugi (upsides/downsides)** penggunaan AI dalam konteks tersebut (biaya, akurasi, risiko etis, kompleksitas maintenance).
- **Ukuran keberhasilan yang terukur** (measurable success) — mis. target akurasi, pengurangan waktu proses, peningkatan retensi pelanggan.
- **Benchmark risiko** — bandingkan dengan risiko spesifik domain/organisasi yang mungkin dihadapi proyek ini.

> 💡 **Poin ujian**: Selalu tanyakan dulu "apakah masalah ini benar-benar butuh AI?" sebelum masuk ke tahap teknis.

## 1.2 Klasifikasikan Masalah

- Periksa **data yang tersedia**: berlabel (labeled) atau tidak berlabel (unlabeled)?
- Tentukan **jenis masalah**:
  - **Classification** — data berlabel, output kategori (mis. spam/bukan spam)
  - **Regression** — data berlabel, output nilai numerik kontinu (mis. prediksi harga)
  - **Unsupervised learning** — data tidak berlabel, mencari pola/struktur (mis. clustering)
  - **Reinforcement learning** — belajar dari reward/penalty melalui interaksi dengan lingkungan

## 1.3 Identifikasi Keahlian yang Dibutuhkan

Sebuah proyek AI biasanya butuh 4 jenis keahlian:

1. **Business expertise** — memahami tujuan bisnis dan dampaknya
2. **Domain/subject-matter expertise** — pemahaman mendalam tentang bidang masalah (mis. dokter untuk AI medis)
3. **AI expertise** — pemilihan algoritma, tuning model
4. **Implementation expertise** — kemampuan membangun dan mengintegrasikan sistem

## 1.4 Membangun Rencana Keamanan (Security Plan)

- **Level akses internal / permission** — siapa yang boleh mengakses data dan model
- **Keamanan infrastruktur** — server, penyimpanan, jalur komunikasi
- **Risiko model & attack surface** — mis. *adversarial attack* pada model yang belajar secara real-time (real-time learning model rentan dimanipulasi dengan input yang sengaja menyesatkan)

## 1.5 Memastikan AI Digunakan Secara Tepat (Appropriate Use)

- Identifikasi potensi **misprediction/harm** terhadap kelompok pengguna tertentu (fairness)
- Buat **pedoman pengumpulan & penggunaan data**
- Buat **pedoman pemilihan algoritma dari sudut pandang pengguna** (bukan hanya performa teknis)
- Pertimbangkan **bagaimana subjek data akan menafsirkan hasil**
- Pertimbangkan **penggunaan hasil AI di luar konteks aslinya** (out-of-context use) — risiko hasil model disalahgunakan untuk keputusan yang bukan tujuan awalnya

## 1.6 Memilih Aktivitas Transparansi dan Validasi

- **Komunikasikan tujuan pengumpulan data** ke pihak terkait/pengguna
- **Tentukan siapa yang berhak melihat hasil** model
- **Tinjau persyaratan hukum/regulasi** yang spesifik untuk industri terkait masalah yang dipecahkan (mis. GDPR untuk data pribadi, HIPAA untuk data kesehatan)

---

## Ringkasan Cepat

| Sub-topik | Kata Kunci untuk Diingat |
|-----------|---------------------------|
| 1.1 | need, input/output, upsides/downsides, measurable success |
| 1.2 | labeled vs unlabeled, classification/regression/unsupervised/reinforcement |
| 1.3 | business, domain, AI, implementation expertise |
| 1.4 | access permission, infrastructure security, adversarial attack |
| 1.5 | harm ke user group, guideline data & algoritma, out-of-context use |
| 1.6 | transparansi tujuan, siapa lihat hasil, regulasi industri |
