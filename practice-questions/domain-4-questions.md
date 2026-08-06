# Latihan Soal — Domain 4: Application Integration and Deployment

---

**1.** Sebuah perusahaan meluncurkan fitur rekomendasi produk berbasis AI, tetapi tidak memberi tahu pengguna bahwa rekomendasi bisa saja kurang relevan untuk produk baru yang belum punya banyak data historis. Ini adalah kelalaian dalam sub-objektif...

A. 4.1 — Train customers on how to use product and what to expect from it
B. 4.3 — Design a production pipeline
C. 4.4 — Support the AI solution
D. 3.9 — Obtain stakeholder approval

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: A**

Sub-objektif 4.1 mencakup "Inform users of model limitations" dan "Manage customer expectations" — kegagalan menyampaikan keterbatasan model kepada pengguna.
</details>

---

**2.** Tim engineering menyadari bahwa pipeline yang berhasil di lingkungan eksperimen (Jupyter notebook, data statis) perlu dirombak total agar bisa menangani data streaming secara real-time saat digunakan di aplikasi produksi. Prinsip yang mendasari kebutuhan ini adalah...

A. Pipeline produksi mungkin perlu berbeda dari pipeline saat eksperimen, sesuai kebutuhan produk
B. Pipeline eksperimen selalu identik dengan pipeline produksi
C. Data streaming tidak pernah digunakan dalam AI production
D. Retraining model tidak diperlukan setelah deployment

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: A**

Sub-objektif 4.3 secara eksplisit menyatakan "Create a pipeline (training, prediction) that can meet the product needs (may be different from the experiment)".
</details>

---

**3.** Setelah AI dideploy di aplikasi mobile, tim menguji apakah model masih berjalan cukup cepat dan tidak menghabiskan terlalu banyak baterai/memori pada perangkat dengan spesifikasi rendah. Ini termasuk aktivitas...

A. 4.3 — Test application to fit size of use case
B. 4.2 — Plan to address potential challenges of models in production
C. 5.1 — Engage in oversight
D. 2.4 — Identify resource requirements

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: A**

Sub-objektif 4.3 secara spesifik memberi contoh "Test application to fit size of use case (e.g., in AI for mobile applications)".
</details>

---

**4.** Tim support diberi pelatihan tentang cara kerja model, potensi bug yang mungkin muncul, dan cara menangani keluhan pengguna terkait hasil AI yang tidak sesuai harapan. Aktivitas ini adalah bagian dari sub-objektif...

A. 4.4 — Support the AI solution
B. 4.1 — Train customers on how to use product
C. 5.4 — Handle feedback from users
D. 1.3 — Identify areas of expertise needed

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: A**

Sub-objektif 4.4 mencakup "Train a support team" sebagai bagian dari mendukung solusi AI pasca-deployment.
</details>

---

**5.** Sebuah tim membangun mekanisme otomatis yang akan memberi peringatan ketika distribusi data input di produksi mulai berbeda signifikan dari data training. Alat ini disebut...

A. Feature selector
B. Drift detector
C. Data augmenter
D. Hyperparameter tuner

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: B**

Sub-objektif 4.4 menyebutkan "Implement drift detector" — alat untuk mendeteksi pergeseran (drift) data/performa model secara otomatis.
</details>

---

**6.** Sebuah AI customer service chatbot sering salah memahami pertanyaan tentang kebijakan pengembalian barang karena pola bahasa yang digunakan pelanggan berubah setelah kampanye marketing baru diluncurkan. Manakah langkah **preventif** dari domain 4 yang seharusnya sudah diantisipasi tim sejak awal?

A. Memahami jenis tantangan yang mungkin dihadapi model di produksi dan cara memitigasinya (4.2)
B. Membangun ulang seluruh arsitektur model dari nol
C. Menonaktifkan chatbot secara permanen
D. Mengabaikan keluhan karena dianggap kasus minor

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: A**

Sub-objektif 4.2 mencakup pemahaman jenis tantangan (mis. perubahan pola bahasa pengguna) dan cara memitigasinya sebelum menjadi masalah besar di produksi.
</details>

---

**7.** Manakah aktivitas berikut yang **paling tepat** dikategorikan sebagai bagian dari membangun mekanisme umpan balik pengguna dalam production pipeline?

A. Menambahkan tombol "apakah jawaban ini membantu?" pada hasil chatbot
B. Menambah jumlah hidden layer pada neural network
C. Mengganti algoritma dari decision tree ke neural network
D. Membuat dokumentasi API untuk developer eksternal

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: A**

Sub-objektif 4.3 mencakup "Build mechanism to gather user feedback" — tombol feedback sederhana seperti ini adalah contoh nyata dari mekanisme tersebut.
</details>

---

**8.** Tim developer menulis dokumentasi teknis lengkap tentang bagaimana setiap fungsi dalam sistem AI bekerja, termasuk cara menangani edge case tertentu, agar developer lain di masa depan bisa melakukan maintenance tanpa harus bertanya ke tim asli. Ini adalah bagian dari...

A. 4.4 — Support the AI solution (dokumentasi fungsi untuk maintenance)
B. 4.1 — Train customers
C. 1.6 — Choose transparency and validation activities
D. 3.4 — Tell data stories

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: A**

Sub-objektif 4.4 secara eksplisit mencakup "Document the functions within the AI solution to allow for maintenance (updates, fixing bugs, handling edge cases)".
</details>

