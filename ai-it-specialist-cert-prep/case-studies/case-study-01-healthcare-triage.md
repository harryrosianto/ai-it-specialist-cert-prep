# Studi Kasus 1: Sistem Triase Pasien Berbasis AI

## Skenario

RS Medika Sejahtera ingin membangun sistem AI untuk membantu perawat di ruang IGD melakukan **triase awal** — memprioritaskan pasien mana yang perlu ditangani lebih dulu berdasarkan gejala yang dilaporkan saat pendaftaran.

Data yang tersedia:
- 5 tahun catatan rekam medis IGD (label: tingkat urgensi 1–5, ditentukan oleh perawat senior saat itu)
- Data demografis pasien (usia, jenis kelamin, alamat)
- Gejala yang dilaporkan dalam bentuk teks bebas (free text)

Tim proyek terdiri dari 2 data scientist dan 1 software engineer. Mereka belum melibatkan dokter/perawat dalam proses desain sistem.

Setelah model dilatih dengan akurasi keseluruhan 89%, tim menemukan bahwa model secara konsisten memberi skor urgensi lebih rendah untuk pasien dari kode pos tertentu (area dengan mayoritas penduduk berpenghasilan rendah), meski gejala yang dilaporkan serupa dengan pasien area lain.

---

## Pertanyaan

**1.** Sebutkan minimal 3 jenis keahlian (sesuai sub-objektif 1.3) yang **belum dilibatkan** dalam tim proyek ini, dan jelaskan risikonya.

<details>
<summary>Lihat Jawaban</summary>

- **Domain/subject-matter expertise** (dokter/perawat IGD) — tanpa keterlibatan mereka, tim teknis mungkin salah menafsirkan gejala yang relevan secara klinis, atau melewatkan nuansa medis penting dalam data teks bebas.
- **Business expertise** — memahami bagaimana hasil triase AI akan benar-benar digunakan dalam alur kerja rumah sakit, termasuk implikasi hukum jika prioritas salah.
- **Implementation expertise** terkait integrasi ke sistem rumah sakit yang sudah ada (EHR/rekam medis elektronik).

Risiko utama: model dibangun tanpa validasi klinis, berpotensi menghasilkan keputusan triase yang secara medis tidak masuk akal meski secara statistik "akurat".
</details>

---

**2.** Skor urgensi yang lebih rendah untuk pasien dari kode pos tertentu adalah contoh masalah dari sub-objektif mana, dan mengapa ini bisa terjadi meski kode pos bukan fitur medis yang relevan?

<details>
<summary>Lihat Jawaban</summary>

Ini adalah contoh **bias algoritma** (sub-objektif 3.6) — kemungkinan besar terjadi **self-fulfilling prophecy berdasarkan bias historis**: jika di masa lalu pasien dari area berpenghasilan rendah secara sistematis diberi skor urgensi lebih rendah oleh perawat manusia (mis. karena bias implisit, keterbatasan waktu, atau asumsi terkait asuransi), maka model belajar meniru pola bias tersebut dari data training.

Kode pos sendiri mungkin tidak digunakan langsung sebagai fitur, tetapi bisa menjadi **proxy** melalui korelasi dengan fitur lain (mis. jenis asuransi, riwayat kunjungan, kosakata dalam catatan gejala) — ini adalah contoh "korelasi tidak relevan yang tidak ingin diandalkan classifier" yang disebutkan dalam sub-objektif 3.6.
</details>

---

**3.** Sebelum sistem ini digunakan secara langsung untuk keputusan medis, langkah-langkah apa dari **domain 1 (Problem Definition)** yang seharusnya sudah dilakukan sejak awal untuk mencegah situasi ini?

<details>
<summary>Lihat Jawaban</summary>

- **1.4 (Security plan)**: mengingat ini keputusan berdampak tinggi (high-stakes) pada keselamatan pasien.
- **1.5 (Ensure AI used appropriately)**: mengidentifikasi *potensi cara AI mispredict/merugikan kelompok pengguna tertentu* — seharusnya sudah diantisipasi sejak fase perencanaan dengan analisis fairness/bias per kelompok demografis, bukan ditemukan setelah deployment.
- **1.6 (Transparency & validation)**: meninjau persyaratan hukum spesifik industri kesehatan (mis. regulasi terkait diskriminasi dalam layanan kesehatan) sebelum data dikumpulkan dan sistem dibangun.
</details>

---

**4.** Rancang **satu langkah mitigasi** dari domain 3 (Algorithms and Models) dan **satu langkah dari domain 5 (Monitoring)** untuk mengatasi bias ini secara berkelanjutan.

<details>
<summary>Lihat Jawaban</summary>

**Domain 3**: Sub-objektif 3.6 — audit ulang training data untuk korelasi tersembunyi dengan kode pos/status sosioekonomi; lakukan analisis fairness per subkelompok (bukan hanya akurasi keseluruhan 89%) sebelum model dianggap layak digunakan.

**Domain 5**: Sub-objektif 5.3 — bangun mekanisme monitoring berkelanjutan yang secara khusus melacak metrik performa **per subgrup demografis** (bukan hanya metrik agregat), sehingga disparitas seperti ini bisa terdeteksi lebih awal, bukan setelah berbulan-bulan digunakan di produksi.
</details>

