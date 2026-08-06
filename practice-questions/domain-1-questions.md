# Latihan Soal — Domain 1: AI Problem Definition

Klik **Lihat Jawaban** untuk membuka jawaban dan pembahasan.

---

**1.** Sebuah perusahaan retail ingin mengurangi keluhan pelanggan yang lambat direspons. Tim data mengusulkan chatbot berbasis AI. Langkah **pertama** yang paling tepat sebelum membangun solusi ini adalah...

A. Mengumpulkan data percakapan customer service sebanyak mungkin
B. Menentukan apakah AI benar-benar diperlukan dan mendefinisikan ukuran keberhasilan yang terukur
C. Memilih algoritma NLP yang akan digunakan
D. Membangun prototipe chatbot untuk diuji langsung ke pelanggan

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: B**

Sebelum masuk ke tahap teknis (data, algoritma, prototipe), sub-objektif 1.1 menekankan pentingnya menentukan apakah AI memang dibutuhkan dan mendefinisikan ukuran keberhasilan (measurable success) terlebih dahulu. Ini mencegah proyek AI yang "solusi mencari masalah".
</details>

---

**2.** Sebuah tim memiliki dataset ulasan produk **tanpa label** (tidak ada kategori sentimen yang ditentukan) dan ingin menemukan kelompok-kelompok topik tersembunyi dalam ulasan tersebut. Jenis masalah ini paling tepat diklasifikasikan sebagai...

A. Classification
B. Regression
C. Unsupervised learning
D. Reinforcement learning

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: C**

Data tidak berlabel + tujuan menemukan pola/struktur tersembunyi (topic clustering) adalah ciri khas **unsupervised learning**. Classification dan regression membutuhkan data berlabel, sedangkan reinforcement learning melibatkan agent yang belajar dari reward/penalty.
</details>

---

**3.** Manakah dari berikut ini yang **BUKAN** merupakan salah satu dari empat jenis keahlian (expertise) yang perlu diidentifikasi dalam sub-objektif 1.3?

A. Business expertise
B. Domain/subject-matter expertise
C. Marketing expertise
D. Implementation expertise

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: C**

Empat jenis keahlian yang disebutkan dalam exam objectives adalah: business, domain (subject-matter), AI, dan implementation expertise. Marketing expertise tidak termasuk dalam empat kategori ini.
</details>

---

**4.** Sebuah organisasi sedang membangun model AI yang melakukan **real-time learning** (terus belajar dari data yang masuk secara langsung). Risiko keamanan spesifik apa yang paling relevan untuk dipertimbangkan dalam rencana keamanan (security plan)?

A. Kebocoran kredensial database
B. Adversarial attack yang memanipulasi model melalui input yang sengaja menyesatkan
C. Serangan DDoS ke server web
D. Pencurian source code aplikasi

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: B**

Sub-objektif 1.4 secara eksplisit menyebutkan risiko *adversarial attack pada real-time learning model* sebagai contoh attack surface yang perlu dinilai — karena model yang terus belajar dari input baru bisa "diracuni" (data poisoning) melalui input yang dirancang khusus untuk menyesatkan model.
</details>

---

**5.** Sebuah bank menggunakan model AI untuk menyetujui/menolak pengajuan kredit. Setelah model dideploy, ditemukan bahwa hasil prediksi model digunakan oleh pihak ketiga untuk tujuan lain (mis. profiling pelanggan untuk keperluan pemasaran) yang tidak pernah dimaksudkan sejak awal. Isu ini paling tepat dikategorikan sebagai kegagalan dalam...

A. Feature engineering
B. Mempertimbangkan penggunaan hasil AI di luar konteks (out-of-context use)
C. Evaluasi model sensitivity
D. Pemilihan algoritma

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: B**

Sub-objektif 1.5 menekankan pentingnya mempertimbangkan *out-of-context use* dari hasil AI — yaitu risiko hasil model disalahgunakan untuk tujuan di luar rancangan awalnya.
</details>

---

**6.** Sebuah tim AI di sektor kesehatan perlu memastikan solusi mereka mematuhi hukum yang berlaku sebelum data pasien dikumpulkan. Aktivitas ini termasuk dalam sub-objektif...

A. 1.2 — Classify the problem
B. 1.4 — Build a security plan
C. 1.6 — Choose transparency and validation activities
D. 1.3 — Identify areas of expertise needed

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: C**

Sub-objektif 1.6 mencakup "Review legal requirements specific to the industry with the problem being solved" — meninjau persyaratan hukum sesuai industri (mis. regulasi data kesehatan).
</details>

---

**7.** Manakah pernyataan yang **paling tepat** menggambarkan hubungan antara "mengidentifikasi kebutuhan (need)" dan "mendefinisikan input/output" dalam sub-objektif 1.1?

A. Keduanya tidak saling terkait dan bisa dilakukan di tahap manapun
B. Mendefinisikan input/output harus dilakukan sebelum kebutuhan diidentifikasi
C. Memahami kebutuhan membantu menentukan data apa yang relevan sebagai input dan hasil apa yang diharapkan sebagai output
D. Input/output hanya relevan pada tahap deployment, bukan problem definition

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: C**

Kedua aktivitas ini saling terkait secara logis: pemahaman kebutuhan bisnis akan mengarahkan tim untuk menentukan data masukan yang relevan dan hasil keluaran yang diharapkan dari solusi AI.
</details>

---

**8.** Sebuah perusahaan asuransi ingin menggunakan AI untuk menentukan premi pelanggan. Tim etika perusahaan mengingatkan agar mempertimbangkan bagaimana pelanggan (subjek data) akan **menafsirkan** skor risiko yang dihasilkan model. Ini adalah bagian dari sub-objektif...

A. 1.2
B. 1.5
C. 1.3
D. 1.4

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: B**

Sub-objektif 1.5 ("Ensure that AI is used appropriately") mencakup poin "Consider how the subject of the data can interpret the results" — mempertimbangkan bagaimana subjek data akan menafsirkan hasil AI.
</details>

---

**9.** Tim proyek AI perlu memutuskan siapa saja yang akan memiliki akses untuk melihat hasil prediksi model sebelum sistem di-deploy. Keputusan ini termasuk dalam...

A. 1.6 — Choose transparency and validation activities
B. 2.6 — Select features for the AI model
C. 3.9 — Obtain stakeholder approval
D. 5.4 — Handle feedback from users

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: A**

Sub-objektif 1.6 mencakup "Decide who should see the results" — menentukan siapa yang berhak melihat hasil.
</details>

---

**10.** Manakah dari opsi berikut yang merupakan contoh **benchmarking risiko domain/organisasi** seperti dimaksud pada sub-objektif 1.1?

A. Membandingkan akurasi model dengan model kompetitor
B. Meninjau insiden keamanan data serupa yang pernah dialami perusahaan lain di industri yang sama
C. Menguji kecepatan inferensi model
D. Memilih framework machine learning yang akan digunakan

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: B**

"Benchmark against domain or organization-specific risks" berarti membandingkan/meninjau risiko yang relevan dengan domain atau organisasi tertentu — seperti insiden yang pernah terjadi di industri sejenis — bukan sekadar membandingkan performa teknis model.
</details>

