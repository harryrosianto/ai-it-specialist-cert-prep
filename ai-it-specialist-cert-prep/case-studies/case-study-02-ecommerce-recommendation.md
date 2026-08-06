# Studi Kasus 2: Sistem Rekomendasi E-Commerce

## Skenario

Toko Belanja Nusantara, sebuah platform e-commerce, ingin membangun sistem rekomendasi produk untuk meningkatkan nilai belanja rata-rata pelanggan. Mereka memiliki data:

- Riwayat pembelian 3 tahun terakhir (jutaan transaksi)
- Riwayat klik dan waktu yang dihabiskan di halaman produk
- Rating dan ulasan produk (banyak yang tidak terisi/kosong)

Tim memutuskan menggunakan model **collaborative filtering** berbasis neural network yang cukup kompleks. Setelah dilatih, model mencapai metrik precision yang sangat baik di lingkungan eksperimen (notebook Jupyter dengan data snapshot statis).

Saat di-deploy ke aplikasi mobile, tim menghadapi masalah:
- Waktu respons rekomendasi mencapai 4–5 detik, membuat pengguna mobile frustrasi
- Model tidak bisa menangani produk baru yang belum punya riwayat interaksi (cold start problem)
- Setelah 2 bulan, tim marketing melaporkan bahwa metrik konversi penjualan tidak meningkat signifikan meski metrik precision model tetap tinggi

---

## Pertanyaan

**1.** Precision model tinggi di eksperimen tetapi konversi penjualan tidak meningkat di dunia nyata. Jelaskan mengapa hal ini bisa terjadi, dan sub-objektif mana yang relevan untuk menjelaskan gap ini.

<details>
<summary>Lihat Jawaban</summary>

Ini menggambarkan perbedaan antara **metrik teknis model** (3.5 — precision, akurasi) dan **metrik dampak bisnis** (5.2 — impact metrics/KPI). Precision tinggi berarti model secara statistik "benar" dalam merekomendasikan produk yang relevan, tetapi ini tidak otomatis berarti pengguna benar-benar membeli lebih banyak.

Kemungkinan penyebab: rekomendasi relevan tapi tidak mendorong keputusan beli (mis. pengguna sudah tahu produk itu tapi harga tidak kompetitif), atau ada faktor UX/UI lain yang menghambat konversi meski rekomendasi sudah tepat. Ini menegaskan pentingnya sub-objektif 5.2: selalu bandingkan metrik model dengan **dampak bisnis nyata**, jangan berhenti hanya di metrik teknis.
</details>

---

**2.** Waktu respons 4–5 detik pada aplikasi mobile adalah kegagalan pada sub-objektif mana di domain 4? Apa yang seharusnya diuji sebelum deployment?

<details>
<summary>Lihat Jawaban</summary>

Ini adalah kegagalan sub-objektif **4.3** — khususnya poin "Test speed of AI" dan "Test application to fit size of use case (e.g., in AI for mobile applications)". Sebelum deployment, tim seharusnya sudah menguji latency model dalam kondisi mendekati produksi (bukan hanya di notebook dengan data statis), termasuk mempertimbangkan trade-off kecepatan vs akurasi (relevan juga dengan 3.3 — avoid overengineering, karena model neural network kompleks mungkin bukan pilihan terbaik jika kecepatan adalah prioritas untuk mobile).
</details>

---

**3.** "Cold start problem" (produk baru tanpa riwayat interaksi tidak bisa direkomendasikan dengan baik) seharusnya sudah diantisipasi di tahap mana dalam AI lifecycle?

<details>
<summary>Lihat Jawaban</summary>

Idealnya sudah diantisipasi di:
- **1.1** — saat mendefinisikan masalah, tim seharusnya mempertimbangkan "upsides and downsides of AI" termasuk keterbatasan pendekatan collaborative filtering untuk item baru.
- **4.2** — "Plan to address potential challenges of models in production": cold start adalah tantangan yang **diketahui dan umum** dalam sistem rekomendasi berbasis collaborative filtering, sehingga seharusnya sudah direncanakan mitigasinya (mis. menggabungkan dengan pendekatan content-based filtering untuk produk baru) sebelum deployment, bukan ditemukan sebagai masalah setelahnya.
</details>

---

**4.** Sebagai rekomendasi perbaikan menyeluruh, sebutkan **3 tindakan** dari domain berbeda (boleh domain 3, 4, atau 5) yang harus dilakukan tim untuk memperbaiki sistem ini.

<details>
<summary>Lihat Jawaban</summary>

Contoh jawaban yang valid:

1. **Domain 3 (3.3)**: Evaluasi ulang trade-off model — pertimbangkan model yang lebih ringan/cepat jika penurunan precision kecil sepadan dengan peningkatan kecepatan besar (avoid overengineering).
2. **Domain 4 (4.2 & 4.3)**: Rancang strategi khusus untuk item baru (hybrid content-based + collaborative filtering), dan uji ulang speed & robustness di lingkungan mendekati produksi sebelum rilis berikutnya.
3. **Domain 5 (5.2)**: Bangun dashboard yang melacak **metrik bisnis** (konversi, revenue per user) berdampingan dengan metrik model (precision), sehingga tim bisa langsung melihat korelasi (atau ketidaksesuaian) antara performa teknis dan dampak nyata — dan menyesuaikan strategi lebih cepat di masa depan.
</details>

