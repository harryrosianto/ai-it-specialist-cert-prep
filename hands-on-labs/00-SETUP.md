# Hands-On Labs — Setup

Labs ini pakai Python + scikit-learn, dan sengaja memakai **dataset bawaan scikit-learn** (`load_breast_cancer`, `load_diabetes`, `load_iris`) supaya kamu bisa langsung jalankan **tanpa perlu download data dari internet**.

## 1. Install dependency

```bash
pip install scikit-learn pandas numpy matplotlib
```

(Kalau kamu pakai Python yang dikelola sistem dan kena error `externally-managed-environment`, tambahkan `--break-system-packages`, atau lebih baik buat virtual environment dulu:)

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
pip install scikit-learn pandas numpy matplotlib
```

## 2. Struktur Lab

Setiap lab punya 2 bagian:

- **`lab-XX-....py`** — versi **latihan**, berisi kode dengan bagian `# TODO` yang harus kamu isi sendiri. Baca komentar di tiap file, isi bagian yang kosong, lalu jalankan.
- **`solutions/lab-XX-....py`** — versi **jawaban lengkap** yang sudah bisa langsung dijalankan (`python solutions/lab-02-....py`). Cek ke sini setelah mencoba sendiri, jangan buka duluan.

## 3. Urutan Pengerjaan

| Lab | Domain | Topik |
|-----|--------|-------|
| `lab-01-problem-definition-worksheet.md` | 1 | Worksheet analisis masalah (non-coding, tapi harus diisi tertulis) |
| `lab-02-data-processing.py` | 2 | Cek missing value, class balance, scaling, train/test split |
| `lab-03-model-training-evaluation.py` | 3 | Training model, tuning, overfitting check, metrik evaluasi |
| `lab-04-deployment-simulation.py` | 4 | Bungkus model jadi "pipeline produksi": validasi input, uji kecepatan, uji robustness |
| `lab-05-monitoring-drift-detection.py` | 5 | Simulasi data drift & deteksi otomatis penurunan performa |

Jalankan satu per satu, berurutan — lab 3 memakai output dari lab 2, lab 4 memakai model dari lab 3, dan seterusnya (masing-masing juga bisa jalan standalone karena ada fallback loading data langsung).

## 4. Cara Jalankan

```bash
cd hands-on-labs
python lab-02-data-processing.py
```

Kalau ada error `ModuleNotFoundError`, berarti step 1 (install dependency) belum selesai.
