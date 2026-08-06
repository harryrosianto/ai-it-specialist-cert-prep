# Studi Kasus 3: Deteksi Cacat Produk di Pabrik Manufaktur

## Skenario

PT Industri Presisi memproduksi komponen elektronik dan ingin menggunakan AI berbasis computer vision untuk mendeteksi cacat produksi (retak, goresan, ketidaksesuaian dimensi) secara otomatis melalui kamera di jalur produksi, menggantikan inspeksi manual yang lambat.

Kondisi data:
- Hanya tersedia 800 gambar produk cacat (dari total 500.000 gambar produk yang diperiksa dalam 6 bulan terakhir) — sangat sedikit dibanding produk normal
- Gambar diambil dengan pencahayaan yang bervariasi tergantung shift kerja (siang/malam)
- Tim berhasil melatih model dengan akurasi keseluruhan 98%

Enam bulan setelah deployment, pabrik menambah **lini produksi baru** dengan jenis komponen berbeda dan pencahayaan kamera yang di-upgrade menjadi lebih terang. Setelah perubahan ini, tim quality control melaporkan peningkatan tajam jumlah produk cacat yang **lolos** tanpa terdeteksi model (false negative meningkat drastis), meski dashboard monitoring masih menunjukkan "akurasi 98%".

---

## Pertanyaan

**1.** Mengapa akurasi 98% bisa menyesatkan dalam kasus ini? Sub-objektif domain 2 mana yang relevan dengan akar masalah data ini?

<details>
<summary>Lihat Jawaban</summary>

Dengan hanya 800 gambar cacat dari 500.000 gambar (sekitar 0.16%), ini adalah kasus **class imbalance** parah. Model bisa mencapai akurasi 98% hanya dengan memprediksi "tidak cacat" untuk hampir semua gambar, karena mayoritas data memang produk normal — akurasi keseluruhan menjadi metrik yang menyesatkan.

Relevan dengan sub-objektif **2.3 (Ensure that data are representative)** — "Make sure the amount of data is enough to build an unbiased model" — 800 sampel kemungkinan tidak cukup untuk mewakili keragaman jenis cacat yang mungkin terjadi. Metrik yang lebih tepat untuk kasus ini adalah **sensitivity/recall** (sub-objektif 3.7) — seberapa baik model menangkap cacat yang sebenarnya ada, bukan akurasi keseluruhan.
</details>

---

**2.** Mengapa peningkatan false negative terjadi setelah lini produksi baru dan pencahayaan kamera di-upgrade? Jelaskan menggunakan konsep dari domain 5.

<details>
<summary>Lihat Jawaban</summary>

Ini adalah contoh klasik **data drift** (sub-objektif 5.1) — distribusi data input (jenis komponen baru + pencahayaan berbeda) berubah signifikan dari kondisi saat model dilatih. Model yang dilatih pada gambar dengan karakteristik pencahayaan dan jenis produk tertentu tidak lagi mampu menggeneralisasi dengan baik ke kondisi visual yang baru.

Dashboard yang masih menunjukkan "akurasi 98%" kemungkinan adalah metrik keseluruhan yang **tidak sensitif** terhadap peningkatan false negative pada kelas minoritas (cacat) — ini menegaskan pentingnya sub-objektif 5.1 untuk "observe the system over time in a variety of contexts to check for drift or degraded modes of operation", bukan hanya mengandalkan satu metrik agregat.
</details>

---

**3.** Apa yang seharusnya dilakukan tim **sebelum** menambah lini produksi baru, berdasarkan sub-objektif 4.2 (Plan to address potential challenges)?

<details>
<summary>Lihat Jawaban</summary>

Tim seharusnya sudah:
- Memahami bahwa **perubahan kondisi visual** (pencahayaan, jenis produk baru) adalah jenis tantangan yang **diketahui** dapat memengaruhi model computer vision (sub-objektif 4.2 poin pertama: "Understand the types of challenges you are likely to encounter").
- Menyiapkan **rencana validasi ulang model** sebelum lini produksi baru resmi berjalan — misalnya menguji model pada sampel gambar dari kondisi pencahayaan baru terlebih dahulu, bukan langsung menerapkannya secara penuh.
- Menyiapkan **indikator dini** (early warning indicators), bukan hanya bergantung pada laporan manual dari tim QC yang baru muncul setelah masalah sudah terjadi.
</details>

---

**4.** Rancang rencana perbaikan yang mencakup: (a) satu tindakan pada data (domain 2), (b) satu tindakan pada model (domain 3), dan (c) satu tindakan monitoring berkelanjutan (domain 5).

<details>
<summary>Lihat Jawaban</summary>

**(a) Domain 2 (2.1 & 2.3)**: Kumpulkan lebih banyak sampel gambar cacat dari lini produksi baru dengan pencahayaan ter-upgrade; pertimbangkan teknik **data augmentation** untuk memperkaya variasi kondisi pencahayaan pada data training yang ada.

**(b) Domain 3 (3.5 & 3.6)**: Latih ulang (retrain) model dengan data gabungan lama + baru, dan evaluasi menggunakan metrik **recall/sensitivity per jenis lini produksi**, bukan hanya akurasi keseluruhan, untuk memastikan tidak ada bias performa terhadap lini produksi tertentu.

**(c) Domain 5 (5.1 & 5.5)**: Implementasikan dashboard monitoring yang melacak metrik **recall pada kelas cacat secara terpisah** per lini produksi/kondisi kamera, dengan alert otomatis jika terjadi penurunan signifikan — serta jadwal evaluasi berkala untuk memutuskan kapan model perlu di-retrain seiring perubahan kondisi pabrik di masa depan.
</details>

