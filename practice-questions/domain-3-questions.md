# Latihan Soal — Domain 3: AI Algorithms and Models

---

**1.** Tim ingin model yang mudah dijelaskan kepada auditor eksternal — setiap keputusan model harus bisa ditelusuri berdasarkan aturan yang jelas. Algoritma yang **paling sesuai** untuk kebutuhan ini adalah...

A. Deep neural network dengan banyak hidden layer
B. Decision tree
C. Ensemble dari puluhan model black-box
D. Reinforcement learning agent

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: B**

Decision tree dikenal sebagai algoritma yang **explainable** — keputusan bisa ditelusuri melalui alur percabangan yang jelas (feature importance mudah diinterpretasi), sesuai kebutuhan sub-objektif 3.1 dan 3.3 (explainability requirements).
</details>

---

**2.** Setelah beberapa iterasi tuning, sebuah model mencapai akurasi 99.8% pada data training tetapi hanya 62% pada data test. Kondisi ini disebut...

A. Underfitting
B. Overfitting
C. Data drift
D. Class imbalance

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: B**

Performa sangat tinggi di training tapi jauh lebih rendah di data test adalah ciri khas **overfitting** — model terlalu menyesuaikan diri (menghafal) data training dan gagal melakukan generalisasi ke data baru.
</details>

---

**3.** Sebuah model deteksi penyakit langka memiliki recall (sensitivity) tinggi tetapi precision rendah. Apa artinya secara praktis?

A. Model jarang salah memprediksi kasus negatif sebagai positif
B. Model berhasil mendeteksi hampir semua kasus positif sebenarnya, tetapi juga banyak menghasilkan false positive
C. Model sangat cepat dalam melakukan inferensi
D. Model tidak bisa digunakan sama sekali

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: B**

Recall/sensitivity tinggi = model menangkap hampir semua kasus positif sebenarnya (sedikit false negative). Precision rendah = dari semua yang diprediksi positif, banyak yang sebenarnya negatif (banyak false positive). Ini trade-off umum, sering diterima dalam kasus medis karena melewatkan kasus positif (false negative) lebih berbahaya daripada false alarm.
</details>

---

**4.** Tim menemukan bahwa model klasifikasi kelayakan kredit secara tidak sengaja "belajar" korelasi antara kode pos (yang berkorelasi dengan ras) dan keputusan kredit historis yang bias. Ini adalah contoh risiko dari sub-objektif...

A. 3.4 — Tell data stories
B. 3.6 — Look for potential sources of bias in the algorithm
C. 3.2 — Train a model using the selected algorithm
D. 3.8 — Confirm adherence to regulatory requirements

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: B**

Ini persis skenario "self-fulfilling prophecy berdasarkan bias historis" dan "korelasi tidak relevan yang tidak ingin diandalkan classifier" yang disebutkan dalam sub-objektif 3.6.
</details>

---

**5.** Sebuah tim memiliki dua model kandidat: Model A dengan akurasi 94% tapi butuh 2 detik untuk inferensi, dan Model B dengan akurasi 91% tapi hanya butuh 0.1 detik. Aplikasi membutuhkan respons real-time. Pertimbangan memilih di antara keduanya termasuk sub-objektif...

A. 3.2 — Train a model
B. 3.3 — Select specific model after experimentation, avoiding overengineering
C. 2.4 — Identify resource requirements
D. 5.2 — Assess business impact

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: B**

Sub-objektif 3.3 secara eksplisit mencakup "Consider cost, speed, and other factors in evaluating models" — trade-off akurasi vs kecepatan adalah contoh nyata dari aktivitas ini.
</details>

---

**6.** Untuk memverifikasi bahwa model robust terhadap data yang belum pernah dilihat sebelumnya, tim memasukkan batch data baru yang dikumpulkan setelah periode training selesai. Aktivitas ini disebut...

A. Feature engineering
B. Cross-validation dengan data test baru untuk menguji robustness
C. Hyperparameter tuning
D. Data augmentation

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: B**

Sub-objektif 3.5 mencakup "Introduce new test data to cross-validate robustness, testing how model handles unforeseen data".
</details>

---

**7.** Sebelum solusi AI dianggap final, tim mengadakan sesi presentasi hasil model kepada manajer produk, tim legal, dan perwakilan pengguna untuk mendapatkan persetujuan. Ini adalah bagian dari sub-objektif...

A. 3.9 — Obtain stakeholder approval
B. 3.7 — Evaluate model sensitivity
C. 1.5 — Ensure that AI is used appropriately
D. 4.1 — Train customers on how to use product

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: A**

Sub-objektif 3.9 mencakup "Hold sessions to evaluate solution" bersama stakeholder — persis skenario ini.
</details>

---

**8.** Regulator kesehatan menetapkan bahwa model diagnosis harus memiliki sensitivity minimal 95% sebelum boleh digunakan secara klinis. Tim mengevaluasi apakah model mereka memenuhi ambang batas ini. Aktivitas ini termasuk...

A. 3.8 — Confirm adherence to regulatory requirements
B. 3.4 — Tell data stories
C. 2.9 — Document data decisions
D. 3.1 — Consider applicability of specific algorithms

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: A**

Sub-objektif 3.8 mencakup "Evaluate outputs according to thresholds defined in requirements" — mengevaluasi output berdasarkan ambang batas regulasi.
</details>

---

**9.** Manakah pasangan istilah berikut yang **paling tepat** menggambarkan perbedaan antara sensitivity dan specificity?

A. Sensitivity mengukur kecepatan model; specificity mengukur akurasi model
B. Sensitivity = true positive rate; specificity = true negative rate
C. Sensitivity hanya berlaku untuk regression; specificity hanya untuk classification
D. Keduanya adalah istilah lain untuk akurasi keseluruhan

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: B**

Sensitivity (recall) = TP/(TP+FN) — kemampuan mendeteksi kasus positif sebenarnya. Specificity = TN/(TN+FP) — kemampuan mendeteksi kasus negatif sebenarnya.
</details>

---

**10.** Sebuah startup memilih untuk membangun model neural network yang sangat kompleks untuk tugas klasifikasi sederhana (memprediksi apakah email termasuk 2 kategori), padahal model logistic regression sederhana sudah mencapai akurasi setara. Ini adalah contoh pelanggaran prinsip...

A. Feature engineering
B. Overengineering — sub-objektif 3.3
C. Data representativeness
D. Model drift

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: B**

Sub-objektif 3.3 secara eksplisit menekankan "avoiding overengineering" — memilih model paling kompleks padahal solusi lebih sederhana sudah cukup adalah bentuk overengineering yang harus dihindari.
</details>

