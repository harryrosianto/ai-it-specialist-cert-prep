# Latihan Soal — Domain 5: Maintaining and Monitoring AI in Production

---

**1.** Tim operasional mencatat setiap prediksi model, waktu respons, dan input yang diterima ke dalam sistem log terpusat untuk keperluan audit dan debugging di masa depan. Ini termasuk aktivitas sub-objektif...

A. 5.1 — Engage in oversight
B. 5.2 — Assess business impact
C. 4.4 — Support the AI solution
D. 2.9 — Document data decisions

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: A**

Sub-objektif 5.1 mencakup "Log application and model performance to facilitate security, debug, accountability, and audit".
</details>

---

**2.** Setelah tiga bulan model deployment, akurasi model dalam mendeteksi transaksi mencurigakan turun dari 96% menjadi 84% secara bertahap, meski tidak ada perubahan kode. Penjelasan **paling mungkin** untuk fenomena ini adalah...

A. Bug pada kode aplikasi
B. Model/concept drift — pola data di dunia nyata berubah dibanding saat training
C. Kesalahan pada dokumentasi API
D. Kurangnya pelatihan tim support

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: B**

Penurunan performa bertahap tanpa perubahan kode adalah ciri khas **drift** (data drift/concept drift) — pola atau distribusi data di dunia nyata bergeser dari kondisi saat model dilatih.
</details>

---

**3.** Tim bisnis membandingkan metrik konversi penjualan sebelum dan sesudah fitur rekomendasi AI diluncurkan, untuk menilai apakah solusi benar-benar berdampak positif terhadap tujuan bisnis. Aktivitas ini termasuk sub-objektif...

A. 5.2 — Assess business impact (KPI)
B. 5.1 — Engage in oversight
C. 3.5 — Evaluate model performance
D. 4.2 — Plan to address potential challenges

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: A**

Sub-objektif 5.2 mencakup "Track impact metrics... Compare previous metrics with new metrics when changes are made" — tepat menggambarkan skenario ini. Perbedaan dengan 3.5: 3.5 fokus pada metrik *teknis model* (akurasi, precision), sedangkan 5.2 fokus pada metrik *dampak bisnis* (konversi, revenue, dsb).
</details>

---

**4.** Sebuah audit menemukan bahwa model persetujuan pinjaman memiliki tingkat penolakan jauh lebih tinggi untuk aplikan dari satu wilayah geografis tertentu dibanding wilayah lain, meski profil finansial serupa. Tim kemudian menyelidiki penyebabnya dan merancang perbaikan. Ini adalah aktivitas dari sub-objektif...

A. 5.3 — Measure impacts on individuals and communities
B. 5.5 — Consider improvement or decommission
C. 4.1 — Train customers
D. 2.3 — Ensure that data are representative

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: A**

Sub-objektif 5.3 mencakup "Analyze impact on specific subgroups" dan "Identify and mitigate issues" — persis menganalisis dampak berbeda pada subkelompok tertentu (dalam hal ini wilayah geografis) setelah AI berjalan di produksi.
</details>

---

**5.** Setelah menerima banyak masukan bahwa pengguna tidak memahami mengapa aplikasi kesehatan mereka merekomendasikan konsultasi dokter, tim UX melakukan survei kepuasan dan menemukan tingkat kebingungan tinggi. Ini termasuk aktivitas sub-objektif...

A. 5.4 — Handle feedback from users
B. 5.1 — Engage in oversight
C. 1.5 — Ensure that AI is used appropriately
D. 3.4 — Tell data stories

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: A**

Sub-objektif 5.4 mencakup "Assess whether users are confused (e.g., do they understand what the AI is supposed to do for them?)" — tepat menggambarkan skenario ini.
</details>

---

**6.** Setelah dua tahun berjalan, sebuah model rekomendasi konten dinilai sudah tidak relevan lagi karena tren konsumsi pengguna berubah drastis, dan biaya maintenance lebih besar dari manfaat bisnis yang dihasilkan. Tim akhirnya memutuskan untuk menghentikan penggunaan model ini. Keputusan ini termasuk sub-objektif...

A. 5.5 — Consider improvement or decommission on a regular basis
B. 4.2 — Plan to address potential challenges
C. 3.3 — Select specific model after experimentation
D. 5.2 — Assess business impact

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: A**

Sub-objektif 5.5 secara eksplisit mencakup keputusan "Decide whether to retrain AI, continue to use AI as is, or to decommission AI" berdasarkan gabungan observasi dampak bisnis, komunitas, dan tren teknologi.
</details>

---

**7.** Manakah dari berikut ini yang **BUKAN** merupakan bagian dari "engage in oversight" (5.1)?

A. Menggunakan sistem monitoring yang robust
B. Bertindak atas alert yang muncul
C. Melakukan survei kepuasan pelanggan
D. Mengamati sistem dari waktu ke waktu untuk memeriksa drift

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: C**

Survei kepuasan pelanggan termasuk dalam sub-objektif 5.4 ("Handle feedback from users"), bukan 5.1. Sub-objektif 5.1 berfokus pada pengawasan teknis sistem (logging, monitoring, alert, drift).
</details>

---

**8.** Sebuah tim menemukan model prediksi churn pelanggan yang mereka gunakan mulai gagal mendeteksi pola churn baru yang muncul akibat perubahan model bisnis kompetitor. Langkah paling tepat berikutnya berdasarkan siklus monitoring AI adalah...

A. Menghapus model dan tidak menggantinya sama sekali
B. Menggabungkan observasi dampak dan mempertimbangkan retraining model dengan data terbaru
C. Mengabaikan temuan karena model masih "cukup baik"
D. Mengubah seluruh tim pengembang

<details>
<summary>Lihat Jawaban</summary>

**Jawaban: B**

Ini adalah alur kerja standar sub-objektif 5.5 — menggabungkan observasi dampak (termasuk tren bisnis/kompetitor) untuk memutuskan retrain, lanjutkan, atau decommission. Retraining adalah respons yang tepat terhadap concept drift yang terdeteksi.
</details>

