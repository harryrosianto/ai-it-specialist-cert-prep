# Domain 3: AI Algorithms and Models

---

## 3.1 Mempertimbangkan Penerapan Algoritma Tertentu

- Evaluasi **keluarga algoritma AI** (neural network, tree-based, clustering, dll.)
- Tentukan algoritma mana yang cocok, mis.:
  - **Neural network** — untuk data kompleks/non-linear, gambar, teks
  - **Decision tree** — untuk klasifikasi yang mudah dijelaskan (explainable)
  - **K-means** — untuk clustering (unsupervised)

## 3.2 Melatih Model dengan Algoritma Terpilih

- **Train model** dengan parameter awal terbaik-tebak (best-guess starting parameters)
- **Tuning** model dengan mengubah parameter (hyperparameter tuning)
- **Kumpulkan metrik performa** model
- **Iterasi** sesuai kebutuhan

## 3.3 Memilih Model Spesifik Setelah Eksperimen (Hindari Overengineering)

- Pertimbangkan **biaya, kecepatan**, dan faktor lain dalam mengevaluasi model
- Tentukan apakah model terpilih **memenuhi kebutuhan explainability** (dapat dijelaskan)

> 💡 **Poin ujian**: "Avoid overengineering" berarti jangan memilih model paling kompleks jika model sederhana sudah cukup memenuhi kebutuhan bisnis.

## 3.4 Menceritakan Data (Tell Data Stories)

- Buat **visualisasi hasil** bila memungkinkan
- Cari **tren** dalam data/hasil
- Verifikasi bahwa **visualisasi berguna untuk pengambilan keputusan** (bukan sekadar dekoratif)

## 3.5 Mengevaluasi Performa Model

- Periksa **overfitting** (model terlalu menyesuaikan data training, buruk pada data baru) dan **underfitting** (model terlalu sederhana, gagal menangkap pola)
- Hasilkan **metrik atau KPI** (accuracy, precision, recall, F1-score, dll.)
- **Perkenalkan data test baru** untuk cross-validate robustness — menguji bagaimana model menangani data yang belum pernah dilihat

## 3.6 Mencari Potensi Sumber Bias dalam Algoritma

- Verifikasi bahwa **input menyerupai data training**
- Konfirmasi **training data tidak mengandung korelasi tidak relevan** yang tidak ingin diandalkan classifier
- Periksa **ketidakseimbangan (imbalance)** dalam data
- Jaga agar tidak menciptakan **self-fulfilling prophecy** berdasarkan bias historis (mis. model prediksi kejahatan yang dilatih dari data penegakan hukum yang bias historis akan terus memperkuat bias tersebut)
- Periksa **explainability algoritma** (mis. feature importance pada decision tree)

## 3.7 Mengevaluasi Sensitivitas Model

- **Sensitivity** (recall / true positive rate): seberapa baik model mendeteksi kasus positif yang sebenarnya
- **Specificity** (true negative rate): seberapa baik model mendeteksi kasus negatif yang sebenarnya

## 3.8 Memastikan Kepatuhan terhadap Persyaratan Regulasi

- Evaluasi output sesuai **ambang batas (threshold)** yang ditentukan regulasi
- **Dokumentasikan hasil**

## 3.9 Mendapatkan Persetujuan Stakeholder

- Kumpulkan hasil dan **benchmark risiko**
- Adakan **sesi evaluasi solusi** bersama stakeholder

---

## Ringkasan Cepat

| Sub-topik | Kata Kunci untuk Diingat |
|-----------|---------------------------|
| 3.1 | algorithm family, neural network/decision tree/k-means |
| 3.2 | best-guess parameter, tuning, iterasi |
| 3.3 | avoid overengineering, explainability |
| 3.4 | visualisasi, tren, keputusan |
| 3.5 | overfitting/underfitting, KPI, data test baru |
| 3.6 | bias, imbalance, self-fulfilling prophecy, feature importance |
| 3.7 | sensitivity (recall) vs specificity |
| 3.8 | threshold regulasi, dokumentasi |
| 3.9 | stakeholder approval, benchmark risiko |

## Formula/Konsep Metrik Penting

| Metrik | Formula/Definisi | Fokus |
|--------|-------------------|-------|
| Accuracy | (TP+TN)/(TP+TN+FP+FN) | Ketepatan keseluruhan |
| Precision | TP/(TP+FP) | Dari yang diprediksi positif, berapa yang benar |
| Recall (Sensitivity) | TP/(TP+FN) | Dari yang sebenarnya positif, berapa yang terdeteksi |
| Specificity | TN/(TN+FP) | Dari yang sebenarnya negatif, berapa yang terdeteksi benar |
| F1-score | 2 × (Precision × Recall)/(Precision + Recall) | Keseimbangan precision & recall |
