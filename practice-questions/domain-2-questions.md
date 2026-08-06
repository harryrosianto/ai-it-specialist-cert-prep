# Latihan Soal — Domain 2: Data Collection, Processing, and Engineering

---

**1.** Sebuah tim tidak menemukan dataset publik yang sesuai untuk kasus penggunaan mereka (deteksi cacat pada produk tekstil lokal). Mereka memutuskan memasang kamera di jalur produksi untuk mengumpulkan gambar secara otomatis. Keputusan ini termasuk aktivitas pada sub-objektif...

A. 2.1 — Choose the way to collect data
B. 2.4 — Identify resource requirements
C. 2.7 — Engage in feature engineering
D. 2.9 — Document data decisions

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: A**

Sub-objektif 2.1 mencakup keputusan menggunakan dataset yang ada vs membuat dataset sendiri, dan apakah pengumpulan bisa diotomasi (seperti kamera otomatis) atau butuh input manual.
</details>

---

**2.** Setelah dataset terkumpul, tim menemukan bahwa 15% baris data memiliki nilai kosong pada kolom penting. Aktivitas memeriksa hal ini termasuk dalam sub-objektif...

A. 2.2 — Assess data quality
B. 2.3 — Ensure that data are representative
C. 2.5 — Convert data into suitable formats
D. 2.8 — Identify training and test datasets

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: A**

Sub-objektif 2.2 mencakup "Look for missing or corrupt data elements" — mencari data yang hilang atau rusak.
</details>

---

**3.** Sebuah dataset wajah untuk sistem pengenalan wajah ternyata 90% berasal dari satu kelompok demografis tertentu. Meskipun jumlah datanya besar (1 juta gambar), model yang dihasilkan berkinerja buruk pada kelompok demografis lain. Masalah utama di sini adalah kegagalan dalam...

A. 2.4 — Identify resource requirements
B. 2.3 — Ensure that data are representative
C. 2.6 — Select features for the AI model
D. 2.1 — Choose the way to collect data

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: B**

Ini adalah contoh klasik data yang **besar tapi tidak representatif** — sub-objektif 2.3 secara spesifik menyebutkan bahwa jumlah data harus cukup untuk membangun model yang tidak bias, bukan hanya soal kuantitas total.
</details>

---

**4.** Tim proyek AI dengan budget terbatas perlu memutuskan apakah akan melatih model deep learning besar atau model yang lebih ringan, berdasarkan ketersediaan GPU dan dana cloud computing. Ini adalah aktivitas dari sub-objektif...

A. 2.4 — Identify resource requirements
B. 2.7 — Engage in feature engineering
C. 3.3 — Select specific model after experimentation
D. 4.3 — Design a production pipeline

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: A**

Sub-objektif 2.4 mencakup penilaian apakah masalah bisa dipecahkan dengan sumber daya komputasi yang tersedia dan pertimbangan budget proyek.
</details>

---

**5.** Dalam proyek NLP (pemrosesan bahasa alami), kalimat-kalimat mentah perlu diubah menjadi token sebelum diproses oleh model. Aktivitas ini termasuk dalam sub-objektif...

A. 2.5 — Convert data into suitable formats
B. 2.6 — Select features for the AI model
C. 2.8 — Identify training and test datasets
D. 3.2 — Train a model using the selected algorithm

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: A**

Sub-objektif 2.5 secara eksplisit memberi contoh "sentences become tokens" sebagai bagian dari mengonversi data komputer menjadi fitur yang sesuai untuk AI.
</details>

---

**6.** Tim data science membangun beberapa kandidat feature vector, lalu mengonsultasikannya dengan dokter spesialis (untuk kasus AI diagnosis medis) guna memastikan fitur yang dipilih relevan secara klinis. Ini adalah bagian dari sub-objektif...

A. 2.5 — Convert data into suitable formats
B. 2.6 — Select features for the AI model
C. 1.3 — Identify areas of expertise needed
D. 3.6 — Look for potential sources of bias in the algorithm

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: B**

Sub-objektif 2.6 mencakup "Consult with subject-matter experts to confirm feature selection" — berkonsultasi dengan pakar domain untuk mengonfirmasi pemilihan fitur.
</details>

---

**7.** Setelah fitur dipilih, tim menerapkan normalisasi (menyamakan skala) pada fitur numerik dan one-hot encoding pada fitur kategorikal. Aktivitas ini adalah bagian dari...

A. 2.6 — Select features for the AI model
B. 2.7 — Engage in feature engineering
C. 2.9 — Document data decisions
D. 3.1 — Consider applicability of specific algorithms

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: B**

Sub-objektif 2.7 mencakup "Review features and determine what standard transformations are needed" — normalisasi dan encoding adalah contoh transformasi standar dalam feature engineering.
</details>

---

**8.** Ketika membagi dataset menjadi data training dan test, mengapa penting memastikan **dataset test representatif**?

A. Agar proses training menjadi lebih cepat
B. Agar evaluasi model mencerminkan performa sesungguhnya pada data dunia nyata, bukan hanya pada subset yang mudah
C. Agar ukuran file dataset menjadi lebih kecil
D. Agar model tidak perlu dilatih ulang

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: B**

Sub-objektif 2.8 menekankan "Ensure test dataset is represented" — jika test set tidak representatif, hasil evaluasi bisa menyesatkan dan tidak mencerminkan performa model di dunia nyata.
</details>

---

**9.** Sebuah regulator meminta perusahaan menjelaskan asumsi dan batasan yang mendasari pemilihan dataset untuk model AI yang mereka gunakan dalam proses seleksi kerja. Perusahaan idealnya sudah memiliki dokumentasi ini dari sub-objektif...

A. 2.9 — Document data decisions
B. 2.2 — Assess data quality
C. 1.6 — Choose transparency and validation activities
D. 5.1 — Engage in oversight

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: A**

Sub-objektif 2.9 mencakup "List assumptions, predicates, and constraints... Make this information available to regulators and end users who demand deep transparency" — persis skenario ini.

(Catatan: 1.6 juga menyentuh regulasi tetapi dari sisi *legal requirement review*, sedangkan 2.9 lebih spesifik pada dokumentasi *keputusan data* itu sendiri.)
</details>

---

**10.** Sebuah tim melatih model deteksi penipuan kartu kredit. Karena kasus penipuan sangat jarang (hanya 0.1% dari total transaksi), model yang dilatih tanpa penanganan khusus cenderung memprediksi "tidak penipuan" untuk semua transaksi dan tetap mendapat akurasi tinggi. Masalah data ini disebut...

A. Data drift
B. Class imbalance
C. Feature leakage
D. Overfitting

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: B**

Ini adalah contoh klasik **class imbalance** — satu kelas (transaksi normal) jauh lebih dominan dibanding kelas lain (penipuan), sehingga model bisa "curang" mendapat akurasi tinggi tanpa benar-benar belajar mendeteksi kelas minoritas.
</details>

